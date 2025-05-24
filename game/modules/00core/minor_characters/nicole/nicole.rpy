## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou, Digital Bonsai, and Wife Trainer

# Package Register
# register_package nicole name "Nicole, The Neighbor" description "Allows Nicole to be a minor character." dependencies core
register nicole_pregame 10 in core as "Nicole the Neighbor"

# Pregame
label nicole_pregame:
  python:
    ## Constants
    model_credits += [('support', "Nicole the Neighbor (Abrill Gerald)")]
    model_credits += [('bit', "Natalie the Lesbian (Christen Courtney)")]
    model_credits += [('bit', "Sandra the Lesbian (credited only as Cindy)")]

    ## Character Definition
    nicole = Person(Character("Nicole", who_color="#cccc99", what_color="#cccc99"), "nicole", cut_portrait = True, prefix = "", suffix = "the Neighbor")
    nicole.your_name = "Sir"

    # Other Characters
    # Navy
    nicole_husband = Character("Greg", who_color="#000080", what_color="#000080", window_background = gui.dialogue_background_dark_font_color)
    # Muted Lilac
    nicole_lesbian_partner_sandra = Character("Sandra", who_color="a47f9d", what_color="a47f9d")
    # Brown
    nicole_lesbian_partner_natalie = Character("Natalie", who_color="522e26", what_color="522e26")


    ## Actions
    nicole.action_send_home = nicole.add_action("Send her home", label = "_send_home", condition = "nicole.in_area('house') and nicole.fixed_location is None")
    ## NOTE: Nicole does not get a normal hypnotize action; instead she has the following for use during visits under the influence of your prior hypnosis
    nicole.action_hypnotize = nicole.add_action("Hypnotize her", label = "_hypnosis", condition = "nicole.hypnosis_visits_post_dildo and nicole.has_tag('hypnosis_visit_today') and nicole.in_area('house') and nicole.fixed_location is None")
    #nicole.action_train_teaching_aide = nicole.add_action("Train Your New Teaching Aide", label = "_first_visit", condition = "nicole.can_be_interacted and nicole.neighbour_arrangement and not nicole.has_tag('teaching_aide') and not nicole.has_tag('hypnosis_visit_today') and nicole.teaching_aide_training_available and nicole.in_area('house')")
    nicole.action_practice_strip = nicole.add_action("Practice her strip tease", label = "_practice_strip", condition = "nicole.can_be_interacted and nicole.has_tag('teaching_aide') and not nicole.has_tag('hypnosis_visit_today') and nicole.in_area('house')")
    nicole.action_practice_blowjob = nicole.add_action("Practice her blow jobs", label = "_practice_bj", condition = "nicole.can_be_interacted and nicole.has_tag('teaching_aide') and not nicole.has_tag('hypnosis_visit_today') and nicole.in_area('house')")
    nicole.action_practice_fuck = nicole.add_action("Practice her fucking", label = "_practice_fuck", condition = "nicole.can_be_interacted and nicole.has_tag('teaching_aide') and not nicole.has_tag('hypnosis_visit_today') and nicole.in_area('house')")
    nicole.action_practice_anal = nicole.add_action("Practice her anal", label = "_practice_anal", condition = "nicole.can_be_interacted and nicole.has_tag('teaching_aide') and not nicole.has_tag('hypnosis_visit_today') and nicole.in_area('house')")
    nicole.action_practice_submission = nicole.add_action("Practice her submission", label = "_practice_submission", condition = "nicole.can_be_interacted and nicole.has_tag('teaching_aide') and not nicole.has_tag('no_spanking') and not nicole.has_tag('hypnosis_visit_today') and nicole.in_area('house')")
    nicole.action_watch_dance = nicole.add_action("Watch her dance", label = "_watch_her_dance", condition = "nicole.can_be_interacted and nicole.has_tag('showgirl') and current_location == stage and not nicole.has_tag('watched_today')")
    nicole.action_rename = nicole.add_action("Rename her", label = "_rename", condition = "nicole.can_be_interacted and nicole.has_tag('slavegirl') and nicole.in_area('house')")
    nicole.action_slavegirl_entertain = nicole.add_action("Have her entertain you", label = "_slavegirl_entertain", condition = "nicole.can_be_interacted and nicole.has_tag('slavegirl') and nicole.in_area('house')")
    nicole.action_slavegirl_blowjob = nicole.add_action("Have her blow you", label = "_slavegirl_blowjob", condition = "nicole.can_be_interacted and nicole.has_tag('slavegirl') and nicole.in_area('house')")
    nicole.action_slavegirl_sex = nicole.add_action("Have sex with her", label = "_slavegirl_sex", condition = "nicole.can_be_interacted and nicole.has_tag('slavegirl') and nicole.in_area('house')")
    nicole.action_slavegirl_anal = nicole.add_action("Have anal sex with her", label = "_slavegirl_anal", condition = "nicole.can_be_interacted and nicole.has_tag('slavegirl') and nicole.in_area('house')")
    nicole.action_slavegirl_pleasure = nicole.add_action("Pleasure her", label = "_slavegirl_pleasure", condition = "nicole.can_be_interacted and nicole.has_tag('slavegirl') and nicole.in_area('house')")
    nicole.action_slavegirl_spanking = nicole.add_action("Punish her", label = "_slavegirl_spanking", condition = "nicole.can_be_interacted and nicole.has_tag('slavegirl') and nicole.in_area('house')")
    #nicole.action_lesbian = nicole.add_action("Arrange Lesbian Session for Nicole", label = "_lesbian_visit", condition = "nicole.can_be_interacted and nicole.has_tag('likes_girls') and nicole.has_tag('available_today') and nicole.in_area('house')")
    nicole.action_lend_to_master_m = nicole.add_action("Lend to Master M", label = "_lend_to_master_m", condition = "nicole.can_be_interacted and nicole.has_tag('slavegirl') and player.has_tag('m_waiting_for_slave') and nicole.in_area('house')")
    nicole.action_your_name = nicole.add_action("Tell her how to address you", label="_your_name", condition="nicole.has_tag('slavegirl')")


    ## Tags
    # Common Character Tags
    nicole.add_tags('no_hypnosis', 'likes_boys')

    # Character Specific Tags
    # N/A

    ## Items
    # Bonsai
    nicole_bonsai = Item('Housewarming Gift', 'bt', with_examine = True, unique = True)
    nicole_bonsai.add_stats_with_value('tended_at_living_room', 'tended_at_boudoir', 'tended_at_dungeon', 'tended_at_bedroom')
    nicole_bonsai.action_move = nicole_bonsai.add_action("Move it to another room", label = "_move_it", condition = "living_room.is_empty")
    nicole_bonsai.action_tend = nicole_bonsai.add_action("Tend to the tree", label = "_tend_to", condition = "not player.has_tag('tended_bonsai') and living_room.is_empty")
    nicole_bonsai.action_throw_away = nicole_bonsai.add_action("Throw it away", label = "_throw_away", condition = "living_room.is_empty", unseen = False, seen_result = True)
    player.remove_tags_weekly.add('tended_bonsai')
    start_day_labels.append('bt_start_day')


    # Bottle of Wine
    nicole_bottle_of_wine = Item("Bottle of Wine", 'bow', with_examine = True)
    nicole_bottle_of_wine.action_dinner = nicole_bottle_of_wine.add_action("Join Nicole and Greg for Dinner", label = nicole.short_name + "_dinner_invite", condition = "nicole.dinner_invite_open", ends_day = True)

    # Standard Object Actions
    living_room.action_nicole_train_first = living_room.add_action("Train Nicole to be Your Teaching Aide", label = nicole.short_name + "_first_visit", context = '_contact_other', condition = "living_room.is_empty and nicole.can_be_interacted and nicole.has_tag('available_today') and not nicole.has_tag('teaching_aide') and nicole.teaching_aide_training_available and nicole.fixed_location is None")
    living_room.action_nicole_train = living_room.add_action("Ask Nicole the Teaching Aide to Visit", label = nicole.short_name + "_visit", context = '_contact_other', condition = "living_room.is_empty and nicole.can_be_interacted and nicole.has_tag('available_today') and nicole.has_tag('teaching_aide') and nicole.fixed_location is None")
    living_room.action_nicole_visit = living_room.add_action("Suggest Nicole Visits", label = nicole.short_name + "_hypno_visit", context = '_contact_other', condition = "living_room.is_empty and nicole.can_be_interacted and nicole.has_tag('available_today') and nicole.hypnosis_visits_post_dildo and nicole.fixed_location is None")
    living_room.action_nicole_lesbian = living_room.add_action("Arrange Lesbian Session for Nicole", label = nicole.short_name + "_lesbian_visit", context = '_contact_other', condition = "living_room.is_empty and nicole.can_be_interacted and nicole.can_be_interacted and nicole.has_tag('likes_girls') and nicole.has_tag('available_today') and nicole.fixed_location is None")
    living_room.action_first_message_nicole = living_room.add_action("New Message", label = nicole.short_name + "_first_message", context = '_check_messages', condition = "living_room.is_empty and nicole.message_one_available and nicole.can_be_interacted")
    living_room.action_second_message_nicole = living_room.add_action("New Message from Nicole", label = nicole.short_name + "_second_message", context = '_check_messages', condition = "living_room.is_empty and nicole.message_two_available and nicole.can_be_interacted")
    #living_room.action_lesbian_nicole = living_room.add_action("Arrange Lesbian Session for Nicole", label = nicole.short_name + "_lesbian_visit", context = '_contact_other', condition = "living_room.is_empty and nicole.can_be_interacted and nicole.has_tag('likes_girls') and nicole.has_tag('available_today')")

    ## Locations
    nicole_house = Location("Nicole's House", 'nh', cut_portrait = True, enter_break_labels = ['nh_no_access'], enter_labels = ['nh_enter'], exit_labels = ['nh_exit'])

    ## Other
    nicole.change_status("minor_character")

    # Start Day Events
    start_day_labels.append("nicole_start_day_early_am_events", priority = 0) # the lower the number, the higher the priority; normal events are treated as priority 5
    start_day_labels.append("nicole_start_day_normal_events")

    ########### VARIABLES ###########
    # Common Character Variables
    nicole.add_stats_with_value('event_count', 'hypno_anal_count', 'hypno_blowjob_count', 'hypno_facial_count', 'hypno_orgasm_count', 'hypno_masturbation_count', 'hypno_sex_count', 'hypno_swallow_count', 'strip_count', 'spank_count')

    # Character Specific Variables
    nicole.add_stats_with_value('event_count', 'beg_count', 'revealed_to_neighbour','dance_outfit', 'hypno_outfit', 'visit_outfit', 'submission_count', 'blowjob_practice', 'slave_anal_outfit', 'slave_sex_outfit', 'buttplug_visit_week', 'lesbian_outfit')
    nicole.event_count = 1 # so that you get her first event to start the game; gets et to 0 when Nicole is lost or events otherwise finished
    nicole.begged_slave = False
    nicole.buttplug_visits_allowed = True
    nicole.buttplug_visits_first_complete = False
    nicole.dancing_at_club = False
    nicole.dinner_invite_open = False
    nicole.greg_fed_donna = False
    nicole.horny_from_dance = False
    nicole.hypnosis_visits_post_dildo = False
    nicole.teaching_aide_training_available = False
    nicole.neighbour_arrangement = False
    nicole.message_one_available = False
    nicole.message_two_available = False
    nicole.showgirl_possible = False
    nicole.slavegirl_possible = False
    nicole.slut_discussion = False
    nicole.spectacle_yet = False
    nicole_husband.searched_for_slavenicole = False

  return

# Display Portrait
# CHARACTER: Display Portrait
label nicole_update_media:
    if nicole.location == stage:
        if nicole.has_tag('watched_today'):
            if nicole.dance_outfit == 1:
                $ nicole.change_image('neighbour_strip_1_2')
            elif nicole.dance_outfit == 2:
                $ nicole.change_image('neighbour_strip_2_1')
            elif nicole.dance_outfit == 3:
                $ nicole.change_image('neighbour_strip_3_11')
            else:
                $ nicole.change_image('neighbour_strip_4_1')
        else:
            # note: image references are offset by one so she always shows the next dance outfit she will wear when you Watch Her Dance
            if nicole.dance_outfit == 1:
                $ nicole.change_image('neighbour_strip_2_1')
            elif nicole.dance_outfit == 2:
                $ nicole.change_image('neighbour_strip_3_11')
            elif nicole.dance_outfit == 3:
                $ nicole.change_image('neighbour_strip_4_1')
            else:
                $ nicole.change_image('neighbour_strip_1_2')
    else:
        if nicole.has_tag('slavegirl'):
          if nicole.has_tag('artwork_now'):
            $ nicole.change_image('neighbour_slavegirl_8')
          else:
            $ nicole.change_image('neighbour_slavegirl')
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label nicole_examine:
    if nicole.location == stage:
        "Thanks to your efforts, your neighbor Nicole has found a new hobby. Her husband Greg thinks she's spending a lot of time on charity work out of the house. She doesn't charge for her dances, so perhaps in a way she is."
    elif nicole.has_tag('slavegirl'):
        "Your former neighbor wasn't particularly submissive when you met her, but under your influence [nicole.full_name] has come to view life as your property as not just natural, but ideal."
    elif nicole.has_tag('teaching_aide'):
        "[nicole.description]"
    elif nicole.hypnosis_visits_post_dildo:
        "Your neighbor Nicole is always happy to drop by your house when her husband isn't home. She always goes home feeling good about the time she spends with you."
    else:
        pass
    return

## Character Specific Actions
# note, this summons Nicole for additional visits and training after her initial training
label nicole_visit:
    $ nicole.visit_outfit += 1
    if nicole.visit_outfit > 3:
        $ nicole.visit_outfit = 1
    if nicole.visit_outfit == 1:
        summon nicole
        $ nicole.change_image('neighbour_hypno_outfit_2_2')
        wt_image neighbour_hypno_outfit_2_2
        $ nicole.description = "Your neighbor dressed up today."
    elif nicole.visit_outfit == 2:
        call forced_movement(backyard) from _call_forced_movement_286
        summon nicole
        $ nicole.change_image('neighbour_outfit_2_11')
        wt_image neighbour_outfit_2_11
        $ nicole.description = "Your neighbor snuck over to your house wearing only her undergarments."
    else:
        summon nicole
        $ nicole.change_image('neighbour_outfit_3_1')
        wt_image neighbour_outfit_3_1
        $ nicole.description = "Your neighbor seems to be trying to figure out how little she can wear running from her house to yours without getting arrested."
    if nicole.has_tag('waiting_for_club_access') and player.has_tag('club_first_visit_complete') and nicole.dancing_at_club:
        "Now that you've found somewhere where she can safely take her clothes off, you give her directions to the Club.  She should do well there."
        rem tags 'waiting_for_club_access' from nicole
        call nicole_convert_showgirl from _call_nicole_convert_showgirl_1
    return

label nicole_send_home:
    call character_location_return(nicole) from _call_character_location_return_107
    rem tags 'available_today' 'hypnosis_visit_today' from nicole
    if not living_room.is_here:
        call forced_movement(living_room) from _call_forced_movement_287
    wt_image current_location.image
    return

# note, this summons post-hypnosis Nicole so that you can hypnotize her again
label nicole_hypno_visit:
    add tags 'hypnosis_visit_today' to nicole
    "You give Nicole a quick call and suggests that she visit you.  Under the influence of your prior hypnosis, she comes right over."
    $ nicole.hypno_outfit += 1
    # scroll from 4 to 1
    if nicole.hypno_outfit > 3:
        $ nicole.hypno_outfit = 1
    if nicole.hypno_outfit == 1:
        $ nicole.change_image('neighbour_inside_4')
    elif nicole.hypno_outfit == 2:
        $ nicole.change_image('neighbour_hypno_outfit_2_2')
    else:
        $ nicole.change_image('neighbour_hypno_outfit_3_1')
    summon nicole
    return

label nicole_hypnosis:
    rem tags 'available_today' 'hypnosis_visit_today' from nicole
    $ nicole.hypno_session() # deletes energy and records she was hypnotized
    if nicole.hypno_outfit == 1:
        wt_image neighbour_inside_4
        nicole.c "Hi!  You wanted to talk?"
        call focus_image from _call_focus_image_77
        player.c "Yes, Nicole.  I'm going to talk and you're going to listen.  Listen, Nicole.  Listen to me.  Only me now."
        wt_image neighbour_hypno_outfit_1_18
        player.c "You're here to please me, Nicole.  Start by baring your breasts to please me, Nicole."
        wt_image neighbour_hypno_outfit_1_19
        player.c "You enjoy this, Nicole.  You enjoy showing your body to me.  It excites you.  It excites you to please me.  You want to please me."
        wt_image neighbour_hypno_outfit_1_1
        player.c "Show me how it excites you, Nicole.  Show me how your body enjoys pleasing me."
        wt_image neighbour_hypno_outfit_1_20
        "Nicole caresses her nipples ..."
        wt_image neighbour_hypno_outfit_1_21
        "... teasing them until they start to swell."
        wt_image neighbour_hypno_outfit_1_22
        "Then her hypnotized brain remembers something."
        wt_image neighbour_hypno_outfit_1_2
        "She pulls a vibrator out of her handbag.  Did she pack that just for you, or does she now always carry one around with her?"
        wt_image neighbour_hypno_outfit_1_23
        "You could ask her, but you're too caught up in watching what she's doing with it."
        wt_image neighbour_hypno_outfit_1_4
        nicole.c "oohhhh"
        wt_image neighbour_hypno_outfit_1_24
        "Nicole spreads her legs wide to give you a good view as she jills herself, knowing from past experience that in doing so, she's pleasing you ..."
        nicole.c "oooohhhhhh"
        wt_image neighbour_hypno_outfit_1_25
        "... not to mention herself."
        nicole.c "OOOHHHH!!"
        wt_image neighbour_hypno_outfit_1_26
        "Between your continual hypnosis and the pleasure coursing through her body, she's no longer able to refuse you if you want her to please you in other ways."
        $ title = "What now?"
        menu:
            "Tell her to blow you":
                if nicole.hypno_blowjob_count == 0:
                    "Nicole doesn't want to betray her husband, so you need to take this in small steps. Sucking you off should cause her less conflict than spreading her legs for you."
                wt_image neighbour_hypno_outfit_1_10
                player.c "Kneel in front of me, Nicole. You want to please me. You want to please me with your body. Open your mouth, Nicole, and please me with your mouth."
                wt_image neighbour_hypno_outfit_1_6
                "She opens her mouth and accepts you inside."
                wt_image neighbour_bj_1
                player.c "Not like that, Nicole."
                wt_image neighbour_hypno_outfit_1_7
                player.c "Look at me while you please me with your mouth."
                wt_image neighbour_hypno_outfit_1_11
                "Her eyes locked on you, your neighbor pleasures you with her mouth ..."
                wt_image neighbour_hypno_outfit_1_17
                "... until you fill it with your jizz."
                player.c "[player.orgasm_text]"
                $ nicole.hypno_blowjob_count += 1
                $ nicole.hypno_swallow_count += 1
                orgasm
            "Fuck her" if nicole.hypno_blowjob_count > 0 and nicole.hypno_count > 2:
                if nicole.hypno_sex_count == 0:
                    "Nicole's betrayed her husband by opening her mouth to receive you. She's now ready to betray him by spreading her legs for you."
                wt_image neighbour_hypno_outfit_1_12
                player.c "Come here, Nicole."
                "She watches warily as you remove your pants and beckon her closer."
                player.c "That dildo felt good, but my cock will feel even better.  Having my cock inside you will feel so good."
                player.c "You want to please me. You want to please me by putting my cock inside you.  Riding my cock will please me and feel so good."
                wt_image neighbour_hypno_outfit_1_13
                "She needs no further coaxing.  She climbs on top of you, her pussy dripping wet from the orgasm she just gave herself ..."
                wt_image neighbour_hypno_outfit_1_14
                "... and lowers herself until you're fully inside her."
                wt_image neighbour_hypno_outfit_1_15
                "Then she begins riding you."
                player.c "Not like that, Nicole.  Look at me while you fuck me."
                wt_image neighbour_hypno_outfit_1_8
                "Your hypnotized neighbor rides your cock, up and down, never breaking eye contact with you ..."
                wt_image neighbour_hypno_outfit_1_16
                "... until her second orgasm of the day rips through her, bringing you over the edge as well."
                nicole.c "OOOHHHH!!"
                player.c "[player.orgasm_text]"
                $ nicole.hypno_sex_count += 1
                $ nicole.hypno_orgasm_count += 1
                orgasm
            "Fuck her ass" if nicole.hypno_blowjob_count > 0 and nicole.hypno_sex_count > 0 and nicole.hypno_count > 3:
                if nicole.hypno_anal_count == 0:
                    "Nicole's betrayal of her husband is complete. All that remains is to find out how much of her body she's willing to use to please you."
                wt_image neighbour_hypno_outfit_1_10
                player.c "Stand up and turn around, Nicole.  Turn around and show me your ass.  All of your ass, Nicole."
                wt_image neighbour_anal_7
                player.c "You want to use your body to please me, Nicole.  You want to use all of your body to please me."
                wt_image neighbour_anal_8
                player.c "Show me where I should put my cock, Nicole.  Show me a special place for me to put my cock to please me."
                wt_image neighbour_anal_9
                "It takes a bit of patience and a lot of lube ..."
                wt_image neighbour_anal_10
                "... but eventually you work your cock past her tight sphincter."
                wt_image neighbour_anal_1
                "After that, you can freely fuck her tight rear hole until you're ready to cum, which doesn't take long."
                player.c "[player.orgasm_text]"
                wt_image neighbour_anal_11
                "A shaken Nicole removes your cock from her stretched ass.  Even in her hypnotized state, she seems surprised by how far she's willing to go to please you."
                $ nicole.hypno_anal_count += 1
                orgasm
            "Nothing more today":
                pass
        wt_image neighbour_hypno_outfit_1_5
        "You have her dress and bring her out of her trance before you realize you forgot to tell her to put her vibrator back in her handbag.  Embarrassed, she'll tuck it back in before she leaves, assuming it fell out and hoping you didn't notice."
        nicole.c "Wow, I so love talking to you.  It always leaves me feeling so good afterwards!"
        $ nicole.hypno_masturbation_count += 1
        $ nicole.hypno_orgasm_count += 1
    elif nicole.hypno_outfit == 2:
        wt_image neighbour_hypno_outfit_2_2
        nicole.c "I came right over. I hope its nothing serious, and that you just wanted to chat."
        "Nicole's little black dress is rather formal for this time of day.  She says she came right over, but you suspect she dressed up special for you."
        player.c "I just wanted to talk to you, Nicole.  Relax.  Put your hand bag down.  Relax and look at this and listen to me."
        call focus_image from _call_focus_image_78
        player.c "I'm going to talk and you're going to listen.  Listen, Nicole.  Listen to me.  Only me now.   Only the sound of my voice."
        wt_image neighbour_hypno_outfit_2_3
        "That's a lovely dress, Nicole.  Did you wear that dress today because you thought it would please me?"
        nicole.c "Yes.  I think it looks nice on me.  I hoped wearing this would please you, because it looks nice on me."
        player.c "It does please me, Nicole.  That dress looks very nice on you.  That dress will also look very nice on the floor."
        player.c "Seeing your body will please me, Nicole.  Show me your body, Nicole.  Show me your breasts.  Bare your breasts and please me, Nicole."
        wt_image neighbour_hypno_outfit_2_4
        player.c "Now the rest of you, Nicole.  Show me the rest of your body to please me."
        wt_image neighbour_hypno_outfit_2_5
        player.c "You like this, Nicole. You enjoy pleasing me. It feels right to please me. It excites you. It excites you to please me.  You want to please me."
        player.c "Show me how much you want to please me, Nicole. Show me how much your body wants to please me. Show me how it excites you, Nicole.  Show me how excited your body gets pleasing me."
        wt_image neighbour_hypno_outfit_2_6
        "Under your influence, your hypnotized neighbor spreads her pussy lips open ..."
        wt_image neighbour_hypno_outfit_2_7
        "... then pushes a finger inside ..."
        wt_image neighbour_hypno_outfit_2_14
        "... proudly demonstrating how wet she is to please you."
        $ title = "What now?"
        menu:
            "Tell her to blow you":
                if nicole.hypno_blowjob_count == 0:
                    "Nicole doesn't want to betray her husband, so you need to take this in small steps.  Sucking you off should cause her less conflict than spreading her legs for you."
                wt_image neighbour_hypno_outfit_2_17
                player.c "Kneel in front of me, Nicole. You want to please me. You want to please me with your body.  Open your mouth, Nicole, and please me with your mouth."
                wt_image neighbour_hypno_outfit_2_18
                "She opens her mouth and accepts you inside."
                wt_image neighbour_first_visit_11
                player.c "Not like that, Nicole.  Look at me while you please me with your mouth."
                wt_image neighbour_hypno_outfit_2_11
                "Her eyes locked on you, your neighbor pleasures you with her mouth ..."
                wt_image neighbour_hypno_outfit_2_19
                "... until you fill it with your jizz."
                player.c "[player.orgasm_text]"
                $ nicole.hypno_blowjob_count += 1
                $ nicole.hypno_swallow_count += 1
                orgasm
            "Fuck her" if nicole.hypno_blowjob_count > 0 and nicole.hypno_count > 2:
                if nicole.hypno_sex_count == 0:
                    "Nicole's betrayed her husband by opening her mouth to receive you. She's ready now to betray him by spreading her legs for you."
                player.c "Your body wants my cock, Nicole. It wants my cock inside you. Show me how much you want my cock inside you."
                wt_image neighbour_hypno_outfit_2_20
                "Nicole turns around and offers herself to you."
                player.c "Where should my cock be, Nicole?  Show me where you want me to put my cock."
                wt_image neighbour_hypno_outfit_2_9
                "Without hesitation, she puts her finger in her pussy."
                wt_image neighbour_hypno_outfit_2_21
                "She moans as you replace her finger with the tip of her cock ..."
                nicole.c "oohhh"
                wt_image neighbour_hypno_outfit_2_10
                "... moans louder as you begin to fuck her ..."
                nicole.c "ooohhhh"
                wt_image neighbour_first_visit_13
                "... and moans louder still as she climaxes around your cock ..."
                nicole.c "OOOHHHH!!"
                wt_image neighbour_hypno_outfit_2_22
                "... bringing you over the edge with her."
                "[player.orgasm_text]"
                $ nicole.hypno_sex_count += 1
                $ nicole.hypno_orgasm_count += 1
                orgasm
            "Fuck her ass" if nicole.hypno_blowjob_count > 0 and nicole.hypno_sex_count > 0 and nicole.hypno_count > 3:
                if nicole.hypno_anal_count == 0:
                    "Nicole's betrayal of her husband is complete. All that remains is to find out how much of her body she's willing to use to please you."
                player.c "Your body wants my cock, Nicole. It wants my cock inside you. Show me how much you want my cock inside you."
                wt_image neighbour_hypno_outfit_2_20
                "Nicole turns around and offers herself to you."
                player.c "You want to use your body to please me, Nicole.  You want to use all of your body to please me."
                player.c "Show me where I should put my cock, Nicole.  Show me a special place for me to put my cock to please me."
                wt_image neighbour_hypno_outfit_2_23
                player.c "That's right, Nicole.  Put my cock in that special place.  Show me how you can use your entire body to please me."
                wt_image neighbour_anal_12
                "It takes a bit of patience and a lot of lube, but eventually she works your cock in past her sphincter ..."
                wt_image neighbour_anal_13
                "... allowing you to fuck her tight rear hole until you're ready to cum, which doesn't take long ..."
                wt_image neighbour_anal_14
                player.c "[player.orgasm_text]"
                wt_image neighbour_anal_15
                "A shaken Nicole slowly extracts herself from your shrinking cock as your cum drips down from her bowels.  Even in her hypnotized state, she seems surprised by how far she's willing to go to please you."
                $ nicole.hypno_anal_count += 1
                orgasm
            "Just have her play with herself":
                player.c "Pleasing me excites you, Nicole. Show me how much it excites you. Play with your pussy and show me how much you love to please me."
                wt_image neighbour_hypno_outfit_2_15
                "She rubs her fingers across her wet and tender labia ..."
                wt_image neighbour_hypno_outfit_2_16
                "... then pushes a finger back inside ..."
                nicole.c "oohhh"
                wt_image neighbour_hypno_outfit_2_7
                "... and quickly frigs herself to climax."
                wt_image neighbour_hypno_outfit_2_24
                nicole.c "ooohhhhh  ...  OOOHHHH!!"
                $ nicole.hypno_masturbation_count += 1
                $ nicole.hypno_orgasm_count += 1
            "Nothing more today":
                pass
        wt_image neighbour_hypno_outfit_2_8
        "You have her dress and bring her out of her trance."
        nicole.c "Wow, I so love talking to you.  It always leaves me feeling so good afterwards!"
    else:
        wt_image neighbour_hypno_outfit_3_1
        "Nicole arrives wearing shorts that push the boundaries of what passes for suitable while out and about in the neighborhood."
        nicole.c "Hi!  I'm so glad you wanted to chat again.  I really look forward to our talks."
        call focus_image from _call_focus_image_79
        player.c "I'll do the talking, Nicole. You do the listening. Listen to me, Nicole. Only to me. Only the sound of my voice now."
        wt_image neighbour_hypno_outfit_3_2
        player.c "Why are you dressed like that?"
        wt_image neighbour_hypno_outfit_3_8
        nicole.c "My body is for pleasing you.  This outfit shows off my body.  I thought it would please you."
        player.c "It does please me, Nicole. Now that we are alone in private, however, you can please me more by showing your entire body."
        wt_image neighbour_hypno_outfit_3_9
        "It doesn't take her long to strip, because she wasn't wearing much to begin with ..."
        wt_image neighbour_hypno_outfit_3_3
        "... and she's well past the point of being shy with you."
        player.c "You enjoy this. It feels good. It feels great. It feels right. You enjoy pleasing me. It excites you to please me. Show me how excited your body gets pleasing me."
        wt_image neighbour_masturbate_1
        "Her pussy is soon swollen and wet.  She's ready for you."
        $ title = "What now?"
        menu:
            "Tell her to blow you":
                if nicole.hypno_blowjob_count == 0:
                    "Nicole doesn't want to betray her husband, so you need to take this in small steps.  Sucking you off should cause her less conflict than spreading her legs for you."
                wt_image neighbour_face_1
                player.c "Kneel in front of me and open your mouth, Nicole. You want to please me. You want to please me with your body.  Open your mouth wider, Nicole, and please me with your mouth."
                wt_image neighbour_hypno_outfit_3_10
                "Opening her mouth wide, she wraps her soft lips around your hard cock."
                player.c "Not like that, Nicole.  Look at me while you please me with your mouth."
                wt_image neighbour_outfit_3_6
                "Her eyes locked on you, your neighbor pleasures you with her mouth ..."
                wt_image neighbour_shower_6
                "... until you fill it with your jizz, an experience she seems to enjoy nearly as much as you do."
                player.c "[player.orgasm_text]"
                $ nicole.hypno_blowjob_count += 1
                $ nicole.hypno_swallow_count += 1
                orgasm
            "Fuck her" if nicole.hypno_blowjob_count > 0 and nicole.hypno_count > 2:
                if nicole.hypno_sex_count == 0:
                    "Nicole's betrayed her husband by opening her mouth to receive you.  She's ready now to betray him by spreading her legs for you."
                player.c "Your body wants my cock, Nicole.  It wants my cock inside you.  You want to please me by putting my cock inside you."
                wt_image neighbour_hypno_outfit_3_4
                "Your neighbour dutifully complies, spreading her legs and guiding you inside her."
                wt_image neighbour_outfit_4_6
                "She cums long before you do ..."
                nicole.c "oooohhhhh  ...  OOOHHHH!!"
                wt_image neighbour_hypno_outfit_3_13
                "... then rides your cock until you reach your own climax."
                player.c "[player.orgasm_text]"
                $ nicole.hypno_sex_count += 1
                $ nicole.hypno_orgasm_count += 1
                orgasm
            "Fuck her ass" if nicole.hypno_blowjob_count > 0 and nicole.hypno_sex_count > 0 and nicole.hypno_count > 3:
                if nicole.hypno_anal_count == 0:
                    "Nicole's betrayal of her husband is complete. All that remains is to find out how much of her body she's willing to use to please you."
                player.c "Your body wants my cock, Nicole. It wants my cock inside you. Show me how much you want my cock inside you."
                wt_image neighbour_hypno_outfit_3_3
                "Your hypnotized neighbour spreads her legs wide for you."
                player.c "Not like that. You should put my cock in a special place. A special place to take my cock and please me. Show me how much you want to please me. Offer your ass to me, Nicole."
                wt_image neighbour_hypno_outfit_3_5
                "Nicole turns around and offers her ass to you."
                wt_image neighbour_anal_17
                "It takes a bit of patience and a lot of lube ..."
                wt_image neighbour_anal_5
                "... but eventually you work your cock in past her sphincter ..."
                wt_image neighbour_anal_16
                "... allowing you to fuck her tight rear hole ..."
                wt_image neighbour_anal_6
                "... until you fill it with your jizz."
                player.c "[player.orgasm_text]"
                wt_image neighbour_hypno_outfit_3_7
                "A shaken Nicole trembles as you remove your cock from her cum-soaked ass. Even in her hypnotized state, she seems surprised by how far she's willing to go to please you."
                $ nicole.hypno_anal_count += 1
                orgasm
            "Just have her play with herself":
                player.c "Pleasing me excites you, Nicole. Show me how much it excites you. Play with your pussy and show me how much you love to please me."
                wt_image neighbour_masturbate_2
                "The smell of her arousal fills the room as your hypnotized neighbor strokes her finger in and out ..."
                nicole.c "oohhh"
                wt_image neighbour_masturbate_3
                "... frigging herself to a quick, intense orgasm."
                nicole.c "ooohhhhh  ...  OOOHHHH!!"
                $ nicole.hypno_masturbation_count += 1
                $ nicole.hypno_outfit += 1
            "Nothing more today":
                pass
        wt_image neighbour_hypno_outfit_3_1
        "You have her dress and bring her out of her trance."
        nicole.c "Thanks for such a great time!  I can't wait until we can talk again."
    call character_location_return(nicole) from _call_character_location_return_108
    wt_image current_location.image
    return

# note: this is called the first time you train Nicole
label nicole_first_visit:
    $ nicole.training_session()
    rem tags 'available_today' from nicole
    $ nicole.visit_outfit -= 1
    if nicole.visit_outfit < 0:
        $ nicole.visit_outfit = 0
    wt_image neighbour_hypno_outfit_2_2
    "Your new Teaching Aide shows up dressed to the nines."
    nicole.c "I can't believe we're going to do this. You have no idea how nervous I am right now!"
    wt_image neighbour_shopping_1
    nicole.c "I haven't been with another man since Greg and I married. I haven't ever been with a man who gets paid to train women on how to please a man."
    call forced_movement(boudoir) from _call_forced_movement_288
    "Nicole follows nervously as you lead her into the boudoir."
    player.c "From what Greg told me, it sounds like you please him just fine. You're not here because he's unhappy with you. You're here because you said you wanted to sleep with me. Isn't that right?"
    wt_image neighbour_first_visit_30
    nicole.c "Yes"
    player.c "So tell me, Nicole, how have you pictured this taking place?  What do you want to have happen next?"
    wt_image neighbour_first_visit_31
    "Nicole takes a seat and a deep breath before replying."
    nicole.c "Wow. Okay. I guess I pictured you telling me what you want me to do, and me doing my best to please you."
    wt_image neighbour_hypno_outfit_2_8
    nicole.c "I have to warn you though, I'm a little nervous about anal. Greg and I tried it once, and I found it uncomfortable, and he's never asked to do that again."
    player.c "And if I decide you should be trained to perform anal sex, Nicole?  How will you feel about that?"
    wt_image neighbour_first_visit_32
    "Your neighbor takes another deep breath before squeaking out an answer."
    nicole.c "If that's what you decide, then I'll go along with it. Please treat me like one of your clients. Demand of me whatever you think I should be doing for you, and instruct me on anything I should be doing better."
    player.c  "Very well, Nicole.  Stand up."
    wt_image neighbour_first_visit_1
    "Your neighbor rises to her feet, nervously brushing her hair away from her face, a tell tale sign that she's excited."
    player.c "Turn around."
    wt_image neighbour_first_visit_2
    player.c "Keep going."
    wt_image neighbour_first_visit_25
    player.c "All the way around and lift the hem of your dress."
    wt_image neighbour_first_visit_26
    nicole.c "I feel like I'm on display."
    player.c "You are.  In order to teach other women to be comfortable with their bodies, you'll need to be comfortable displaying yours."
    wt_image neighbour_first_visit_3
    nicole.c "I am.  This feels weird, but nice, too."
    player.c "Lift your dress higher."
    wt_image neighbour_first_visit_4
    player.c "Turn around again."
    wt_image neighbour_first_visit_5
    player.c "You're very beautiful, Nicole."
    nicole.c "I'm glad you think so."
    wt_image neighbour_first_visit_6
    player.c "I do.  Greg's a lucky man.  Stop there for a moment."
    wt_image neighbour_first_visit_27
    "She waits as you ogle her ass.  Her shallow breathing tells you she's getting off on being objectified in this manner."
    player.c "Lose the dress."
    wt_image neighbour_first_visit_7
    player.c "And the bra."
    wt_image neighbour_first_visit_28
    nicole.c "Should I keep turning?"
    player.c "No, I want to enjoy a view of your breasts now."
    wt_image neighbour_first_visit_29
    "Her breathing fast and shallow, Nicole trembles slightly as you take your time looking at her.  Eventually you smile and gesture to the bed."
    if player.has_tag('dominant'):
        player.c "Kneel"
    else:
        player.c "Make yourself comfortable."
    wt_image neighbour_first_visit_8
    player.c "Can you show other women how to do that, to show off their bodies without being embarrassed?"
    nicole.c "Yes.  I could do that with someone else watching.  Did that really turn you on?"
    player.c "It did, but I also want you to learn how to tease a man by taking off your clothes without instructions.  You should practice with Greg."
    "She giggles."
    nicole.c "He'd like that."
    player.c "I may have you practice with me, too."
    nicole.c "I'd like that."
    player.c "I'll also want you to show other women how to please a man in other ways.  Can you do that, too?"
    "She nods, perhaps a little more eagerly than she intended as you step closer to her."
    wt_image neighbour_first_visit_9
    "Nicole leans up for a kiss while her hand seeks out your erection."
    wt_image neighbour_first_visit_10
    player.c "That's nice, Nicole. That's a good start, paying attention to the balls as well as the shaft. Show me what else you can do."
    wt_image neighbour_first_visit_11
    "Still cupping your balls, Nicole leans in and takes your cock in her mouth. You let her work on you for a while as she demonstrates her oral skills."
    wt_image neighbour_first_visit_12
    "Once you have a sense of her skill level, you take hold of her head and show her how you like your cock sucked."
    player.c "Follow my lead, Nicole. I'll show you where and how to use your lips, tongue, teeth and hands."
    wt_image neighbour_hypno_outfit_2_18
    "She's an eager student and is soon doing a really good job."
    player.c "Could you show other women how to do that?"
    wt_image neighbour_hypno_outfit_2_19
    nicole.c "You mean blow you while another woman watches?"
    player.c "Yes"
    nicole.c "Yes. Yes, I think I can do that. Should I keep practicing this, too?"
    player.c  "Greg will like that, don't you think?"
    "Nicole giggles again."
    player.c "Ready to show me what else you can do, sexually?"
    wt_image neighbour_hypno_outfit_2_23
    "Her only response is a nod and a small moan as she turns around."
    wt_image neighbour_hypno_outfit_2_22
    "Her moans intensify as you pull down her panties and slowly insert yourself into her sopping pussy."
    nicole.c "oohhh"
    wt_image neighbour_first_visit_13
    "With your hands on her hips, you guide her movements, directing her on how you want her to rock back and forth on your cock."
    nicole.c "ooohhhh"
    wt_image neighbour_first_visit_34
    player.c "Squeeze me tight on the back thrust, Nicole.  Grip me as tight as you can, then relax as you slide forward for the next thrust."
    wt_image neighbour_hypno_outfit_2_21
    "Nicole struggles to respond, overwhelmed by the pleasure building between her legs."
    nicole.c "Ye .. ye ... yes ... okay ... ooohhhh"
    wt_image neighbour_sex_7
    "You re-position her top of you. In this position, she can control the pressure on her clit and the pace of her own building climax."
    wt_image neighbour_first_visit_14
    "She doesn't use that control to slow her arousal down, though.  If anything, she speeds it up, bringing herself to an intense orgasm."
    wt_image neighbour_first_visit_35
    nicole.c "OOOHHHHHH!!"
    player.c "Don't stop moving, Nicole.  Don't let your orgasm break your rhythm.  Keep riding me while your pussy spasms."
    wt_image neighbour_first_visit_36
    "Your neighbor tries to respond, but can manage only gasps."
    nicole.c "oooohh ... gaawd ... oooooo ... OOOHHHHHH!!"
    $ nicole.orgasm_count += 2
    wt_image neighbour_first_visit_20
    "When she's recovered, she sits up and looks at you."
    nicole.c "I guess I'll need to control myself if you want me to do that while your client is watching."
    player.c "Unless I want you to demonstrate what it's like to be horny."
    "Nicole blushes."
    nicole.c "Speaking of which, you haven't cum yet, have you?  Should I be doing something about that?"
    $ title = "What should she be doing?"
    menu:
        "Sucking you off":
            wt_image neighbour_first_visit_37
            "You guide her head back to your cock.  Her hot mouth quickly cleans all her pussy juice off of you."
            wt_image neighbour_first_visit_22
            "She bobs her head up and down, following as best she can your earlier instructions on how you like your cock sucked ..."
            wt_image neighbour_first_visit_15
            "... and soon proves herself a good student."
            player.c "[player.orgasm_text]"
            wt_image neighbour_first_visit_23
            nicole.c "Was my technique okay?"
            player.c "You're on your way to becoming a great cocksucker, Nicole."
            wt_image neighbour_first_visit_16
            "She giggles."
            nicole.c "Coming from a professional cocksucker-trainer, I suppose I should be flattered."
            orgasm
            $ nicole.blowjob_count += 1
            $ nicole.swallow_count += 1
        "Riding you to climax":
            player.c "Do you know what Reverse Cowgirl is?"
            nicole.c "Yes"
            wt_image neighbour_sex_8
            "She turns around ..."
            wt_image neighbour_sex_4
            " ... and rides your cock while you enjoy the view."
            wt_image neighbour_sex_9
            player.c "[player.orgasm_text]"
            orgasm
            $ nicole.sex_count += 1
        "Offering you her ass":
            player.c "I'm going to take you anally now, Nicole."
            wt_image neighbour_first_visit_20
            nicole.c "Oh!  That's ... that's really ..."
            player.c "An area of deficiency you need training in?  It seems so.  Regardless of whether you think this is something you should be able to do for Greg, it's something you need to do as my Teaching Aide."
            wt_image neighbour_first_visit_24
            "Your neighbor half pants, have gasps her consent as she turns around to present her ass to you."
            nicole.c "I guess that's fair.  I did say I'd go along with whatever you felt I needed to learn."
            if player.has_tag('dominant'):
                "There's a submissive quality to the way Nicole offers her ass to you. It's clear anal sex is something she wants you to 'make' her do."
                "That combined with the glow of her recent orgasm, her obedience to your instructions so far, and your own naturally dominant nature have put her in a malleable state."
                "Your natural instinct is to stimulate her submissive feelings.  On the other hand, you could just get on with fucking her ass."
                $ title = "What do you do?"
                menu:
                    "Tell her to beg for it":
                        "You can't help yourself.  You like it when women humiliate themselves for you."
                        player.c "Before I put my cock in you, Nicole, you're going to ask me to fuck you in the ass.  In fact, you're going to beg me to fuck your ass."
                        wt_image neighbour_first_visit_17
                        "Your neighbor looks back at you, wide eyed."
                        nicole.c "Wh ... what??"
                        player.c "You heard me.  You as much as told me you wanted your ass fucked when you first got here.  It's possible the idea of having your ass fucked is the main reason you wanted to visit me."
                        nicole.c "No ... no, I just ..."
                        player.c "It's time to be honest, Nicole.  You want me to fuck your ass. You're longing to find out what it feels like to have your ass stretched around my cock."
                        player.c "Be honest, with me and with yourself.  Ask me for what you want, Nicole.  And since you haven't been honest up to now, don't just ask.  Beg.  Beg me for what you want, Nicole."
                        wt_image neighbour_anal_4
                        "Nicole's voice quivers as she speaks, so softly that you can barely hear her.  What you hear, though, is music to your ears."
                        nicole.c "Please ... please fuck me ... I'm begging you."
                        "You could leave it there, but that's not in your nature.  Besides, Nicole's as close to sub space as she's ever likely been before."
                        "Why not give her a taste of what its likely to be in submissive bliss?  It'll be a memory she can jill off to later, should she ever masturbate to submissive thoughts."
                        player.c "What are you begging me for, Nicole?  Say it clearly."
                        wt_image neighbour_first_visit_18
                        "Nicole lowers her head and closes her eyes when she replies.  She's still very quiet, but the quiver is almost gone."
                        nicole.c "I'm begging you to fuck my ass.  I want you to fuck my ass, please.  I want to feel your cock inside my ass."
                        player.c "Good girl, Nicole.  Of course, I'd be happy to."
                        add tags 'begged_for_anal' to nicole
                        $ nicole.beg_count += 1
                    "Just fuck her ass":
                        pass
            wt_image neighbour_anal_9
            "You lube up your cock and position it at Nicole's bottom.  Her only reaction is a soft moan as you apply gentle but steady pressure against her rear hole."
            nicole.c "ooooo"
            wt_image neighbour_anal_10
            "It takes patience and a second application of lube, but eventually her sphincter widens enough to allow the head of your cock to pass through."
            nicole.c "OH"
            player.c "Does that feel good?"
            wt_image neighbour_anal_4
            if nicole.has_tag('begged_for_anal'):
                nicole.c "Yeessss"
                player.c "Should I fuck your ass hard now, girl?"
                nicole.c "Yes.  Please.  Please fuck my ass hard."
                wt_image neighbour_anal_1
                "You thrust in and out of her tight ass.  It only takes a few strokes to bring your neighbor to her second orgasm of the day, and the first anal orgasm of her life."
                nicole.c "OOHH!!"
                $ nicole.orgasm_count += 1
            else:
                nicole.c "nnnnn ... I ... I'm not sure what it feels like."
                wt_image neighbour_anal_1
                "There's no question about how it feels for you.  It feels great as you thrust in and out of her tight ass."
            wt_image neighbour_anal_11
            player.c "[player.orgasm_text]"
            nicole.c "Oh, wow!!!"
            orgasm
            $ nicole.anal_count += 1
        "Nothing.  Time for her to go.":
            player.c "Not right now.  That's it for your lesson today."
            wt_image neighbour_first_visit_20
            "She looks crestfallen."
            nicole.c "You don't want me to do anything for you?  Was I that bad?"
            player.c "You were great.  And you'll get better, with practice.  And training."
            wt_image neighbour_first_visit_5
            nicole.c "I'm looking forward to it.  I guess I forget sometimes this is a job for you, not something you do for fun."
            player.c "I had fun, Nicole.  You're going to do just great as a teaching aide."
    wt_image neighbour_first_visit_5
    nicole.c "That was quite the experience."
    player.c "Worth every penny you're not paying me?"
    wt_image neighbour_first_visit_1
    "She laughs at your teasing."
    nicole.c 'Absolutely!  So, when can I visit you again?  And when do I start repaying you by being your "teaching aide"?'
    player.c "I'll let you know.  Now, get out of here.  I have paying clients I need to look after."
    call forced_movement(living_room) from _call_forced_movement_289
    wt_image neighbour_outfit_1_4
    nicole.c "Okay, okay ... I'm going!"
    call convert(nicole, "teaching_aide") from _call_convert_116
    $ player.desire_action_count += 1
    $ nicole.strip_count += 1
    $ nicole.teaching_aide_training_available = False
    call character_location_return(nicole) from _call_character_location_return_109
    change player energy by -energy_short notify
    wt_image living_room.image
    return

# note, this summons bi-sexual Nicole for a lesbian session
label nicole_lesbian_visit:
    $ nicole.training_session()
    rem tags 'available_today' from nicole
    $ nicole.lesbian_outfit += 1
    # scroll from 3 to 1
    if nicole.lesbian_outfit > 2:
        $ nicole.lesbian_outfit = 1
    if not living_room.is_here:
        call forced_movement(living_room) from _call_forced_movement_290
    # visits with Sandra
    if nicole.lesbian_outfit == 1:
        if not nicole.has_tag('met_sandra'):
            add tags 'met_sandra' to nicole
            wt_image neighbour_lesbian_1_1
            "It's not difficult for you to find a woman from your past interested in meeting Nicole. Nicole's interested in meeting Sandra, too, and dresses up to make a good first impression.  It works."
            wt_image neighbour_lesbian_1_2
            "They're both here for the same reason, and aren't interested in small talk. They can't keep their hands off of each other, and start making out while you watch from the sofa."
            wt_image neighbour_lesbian_1_3
            "Sandra takes the initiative, working her tongue into your neighbor's snatch."
            wt_image neighbour_lesbian_1_14
            "After a few minutes of Sandra's ministrations, Nicole's legs are too weak to stand.  She sinks to the floor.  Sandra follows, her tongue still buried in your neighbor's freshly shaved snatch."
            wt_image neighbour_lesbian_1_4
            "Still lapping vigorously between Nicole's legs, Sandra positions herself over her new friend's face.  Tentatively at first, then with more and more enthusiasm, Nicole tastes and teases Sandra's wet pussy."
            wt_image neighbour_lesbian_1_15
            "As you look on, Sandra brings Nicole to her first lesbian orgasm.  Nicole celebrates the occasion by increasing the pace at which she tongues the hard clit in front of her, soon bringing Sandra over the edge with her."
            nicole.c "OOOHHHH!!"
            nicole_lesbian_partner_sandra "Mmmmmm"
            wt_image neighbour_lesbian_1_5
            "Sweetly, they decide to bring you into their fun.  Sandra makes sure you're ready while Nicole continues to explore her new friend's body."
            "Sandra moans as Nicole slides a finger into her ass.  Nicole's eyes look like they're on fire as she turns to speak to you."
            nicole.c "Fuck her in the ass. I want to see you fuck her in the ass."
            $ title = "Fuck Sandra in the ass?"
            menu:
                "Yes":
                    wt_image neighbour_lesbian_1_6
                    "Sandra positions herself back on top of Nicole.  Your neighbor gets Sandra's ass well lubricated before guiding you over."
                    wt_image neighbour_lesbian_1_7
                    "Nicole makes sure this will be a fuck you all remember."
                    player.c "[player.orgasm_text]"
                    wt_image neighbour_lesbian_1_8
                    "Nicole looks on with fascination as you extract your cock from Sandra's cum-filled ass."
                    wt_image neighbour_lesbian_1_9
                    nicole.c "Thank you for introducing us!"
                    "You love that Nicole's mouth is still dripping with Sandra's juices as she thanks you."
                    add tags 'watched_sandra_anal' to nicole
                    #note: should probably come up with a generic character to track these additional sex act counts; for now, using same one used in swingers room
                    $ club_swingers.anal_count += 1
                    orgasm notify
                "No, but let Sandra blow you":
                    wt_image neighbour_lesbian_1_13
                    "As tempting as Nicole's request is, Sandra's mouth feels too good to leave."
                    wt_image neighbour_lesbian_1_10
                    "In fact, it feels good enough to warrant a deposit."
                    wt_image neighbour_lesbian_1_11
                    player.c "[player.orgasm_text]"
                    wt_image neighbour_lesbian_1_12
                    nicole_lesbian_partner_sandra "Thanks for introducing me to your friend."
                    wt_image neighbour_lesbian_1_9
                    nicole.c "Yes, thank you for introducing us!"
                    "You love that Nicole's mouth is still dripping with Sandra's juices as she thanks you."
                    #note: should probably come up with a generic character to track these additional sex act counts; for now, using same one used in swingers room
                    $ club_swingers.blowjob_count += 1
                    $ club_swingers.swallow_count += 1
                    orgasm notify
                "Nothing today":
                    wt_image neighbour_lesbian_1_9
                    "The ladies don't seem too disappointed that you chose to sit this one out."
                    nicole.c "Thank you for introducing us!"
                    "You love that Nicole's mouth is still dripping with Sandra's juices as she thanks you."
                    change player energy by -energy_very_short
        else:
            wt_image neighbour_lesbian_1_1
            "Nicole dresses up again for Sandra.  It seems she likes to impress her.  She needn't have worried.  Sandra's clearly smitten."
            wt_image neighbour_lesbian_1_2
            "They're both here for the same reason, and aren't interested in small talk. They can't keep their hands off of each other, and start making out while you watch from the sofa."
            wt_image neighbour_lesbian_1_3
            "Sandra takes the initiative, working her tongue into your neighbor's snatch."
            wt_image neighbour_lesbian_1_14
            "After a few minutes of Sandra's ministrations, Nicole's legs are too weak to stand.  She sinks to the floor.  Sandra follows, her tongue still buried in your neighbor's freshly shaved snatch."
            wt_image neighbour_lesbian_1_4
            "Still lapping vigorously between Nicole's legs, Sandra positions herself over her new friend's face.  Considering the enthusiasm with which Nicole starts to eat Sandra's wet pussy, it's hard to believe Nicole had never tasted another woman before meeting you."
            wt_image neighbour_lesbian_1_15
            "As you watch, Sandra brings Nicole to orgasm.  Her body still trembling from the climax, Nicole concentrates her attention on Sandra's hard clit, soon bringing the other woman over the edge with her."
            nicole.c "OOOHHHH!!"
            nicole_lesbian_partner_sandra "Mmmmmm"
            wt_image neighbour_lesbian_1_5
            "Sweetly, they decide to bring you into their fun.  Sandra wraps her mouth around your cock with a moan as Nicole slides a finger into her ass.  Nicole's eyes look like they're on fire as she turns to speak to you."
            nicole.c "Fuck her in the ass. I want to see you fuck her in the ass."
            $ title = "Fuck Sandra in the ass?"
            menu:
                "Yes":
                    wt_image neighbour_lesbian_1_6
                    "Sandra positions herself back on top of Nicole.  Your neighbor gets Sandra's ass well lubricated before guiding you over."
                    wt_image neighbour_lesbian_1_7
                    "Nicole makes sure this will be a fuck you all remember."
                    player.c "[player.orgasm_text]"
                    wt_image neighbour_lesbian_1_8
                    if nicole.has_tag('watched_sandra_anal'):
                        "As you extract your cock from Sandra's cum-filled ass, you're not sure if you or Nicole enjoyed this more?"
                        wt_image neighbour_lesbian_1_16
                        "When Nicole starts licking your cum out of Sandra's ass, though, you think you have your answer."
                        wt_image neighbour_lesbian_1_17
                        "With a combination of your cum and Sandra's juices dripping off her chin, Nicole hugs Sandra and smiles at you."
                        nicole.c "Thanks again for introducing me to Sandra!"
                    else:
                        "Nicole looks on with fascination as you extract your cock from Sandra's cum-filled ass."
                        wt_image neighbour_lesbian_1_1
                        nicole.c "Thank you for introducing us!"
                        add tags 'watched_sandra_anal' to nicole
                    #note: should probably come up with a generic character to track these additional sex act counts; for now, using same one used in swingers room
                    $ club_swingers.anal_count += 1
                    orgasm notify
                "No, but let Sandra blow you":
                    wt_image neighbour_lesbian_1_10
                    "As tempting as Nicole's request is, Sandra's mouth feels too good to leave."
                    wt_image neighbour_lesbian_1_11
                    "In fact, it feels good enough to warrant a deposit."
                    player.c "[player.orgasm_text]"
                    wt_image neighbour_lesbian_1_12
                    nicole_lesbian_partner_sandra "Thanks for inviting me over again."
                    wt_image neighbour_lesbian_1_1
                    nicole.c "Yes, thanks for suggesting that Sandra visit!"
                    #note: should probably come up with a generic character to track these additional sex act counts; for now, using same one used in swingers room
                    $ club_swingers.blowjob_count += 1
                    $ club_swingers.swallow_count += 1
                    orgasm notify
                "Nothing today":
                    wt_image neighbour_lesbian_1_1
                    "The ladies don't seem too disappointed that you chose to sit this one out."
                    nicole.c "Thanks again for introducing me to Sandra!"
                    change player energy by -energy_very_short
    # visits with Natalie
    elif nicole.lesbian_outfit == 2:
        if not nicole.has_tag('met_natalie'):
            add tags 'met_natalie' to nicole
            wt_image neighbour_lesbian_2_10
            "You owe another woman from your past, Natalie, a favor. With your neighbor's new found interest in women, she's the perfect way to repay your lesbian friend for her past assistance."
            wt_image neighbour_lesbian_2_1
            "Natalie can hardly believe her eyes as Nicole strips both of them down to their underwear while you watch."
            wt_image neighbour_lesbian_2_2
            "They both soon forget about you ..."
            wt_image neighbour_lesbian_2_3
            "... they're too busy getting to know each other ..."
            wt_image neighbour_lesbian_2_4
            "... and helping each other undress."
            wt_image neighbour_lesbian_2_5
            "Nicole's still learning her way around the female sex organs, but Natalie doesn't mind watching as Nicole tentatively explores her with her tongue."
            wt_image neighbour_lesbian_2_11
            "With a hand on the back of her head, Natalie shows the novice pussy licker where and how she wants to be licked."
            nicole_lesbian_partner_natalie "Aaahhh!"
            wt_image neighbour_lesbian_2_12
            "It takes a while, but your neighbour eventually has Natalie trembling, and then flooding her tongue with juices as she cums."
            wt_image neighbour_lesbian_2_13
            "Now its Natalie's turn between Nicole's legs."
            wt_image neighbour_lesbian_2_6
            "Unlike your neighbor, Natalie knows her way around a woman's cunt and clit."
            wt_image neighbour_lesbian_2_14
            "Nicole's orgasm is quick, hard, and intense ... and fun to watch, as her body trashes around, wracked by the sensations fromr Natalia's talented tongue."
            nicole.c "OOOHHHH!!"
            wt_image neighbour_lesbian_2_10
            "When she recovers, Nicole notices the bulge in your pants.  Natalie is only into girls, but she watches with amusement as Nicole takes your cock in her hand and begins stroking it."
            $ title = "Let Nicole jerk you off?"
            menu:
                "Yes":
                    wt_image neighbour_hj_1
                    "As Natalie looks on, Nicole uses her soft hand to relieve the pressure in your balls inspired by watching the two of them together."
                    player.c "[player.orgasm_text]"
                    wt_image neighbour_lesbian_2_10
                    "Presumably Natalie hasn't seen many guys cum before, as she seems to find the process funny.  She doesn't say anything about it, though, just waits until Nicole is done, then thanks you in a less personal way."
                    nicole_lesbian_partner_natalie "Thanks for letting me play with Nicole.  If you invite me over again, I'll try to teach her a new trick or two about pleasing girls."
                    add tags 'natalie_watched_handjob' to nicole
                    $ nicole.handjob_count += 1
                    orgasm notify
                "Not today":
                    nicole_lesbian_partner_natalie "Thanks for letting me play with Nicole.  If you invite me over again, I'll try to teach her a new trick or two about pleasing girls."
                    change player energy by -energy_very_short notify
        elif nicole.has_tag('natalie_used_dildo_last_visit'):
            rem tags 'natalie_used_dildo_last_visit' from nicole
            add tags 'used_dildo_on_natalie_last_visit' to nicole
            wt_image neighbour_lesbian_2_1
            "Nicole seems extra excited when she hears Natalie is coming over.  She strips both herself and Natalie down to their underwear as soon as the other woman arrives ..."
            wt_image neighbour_lesbian_2_19
            "... and aggressively maneuvers her onto her back."
            wt_image neighbour_lesbian_2_20
            "Nicole literally licks her lips as she exposes first the blonde's pussy ..."
            wt_image neighbour_lesbian_2_21
            "... and then her breasts ..."
            wt_image neighbour_lesbian_2_22
            "... which she proceeds to devour with a hunger matching the hunger in her eyes."
            wt_image neighbour_lesbian_2_23
            if not nicole.has_tag('used_dildo_on_natalie_before'):
                add tags 'used_dildo_on_natalie_before' to nicole
                "When she has the blonde worked up and sopping wet, Nicole suddenly stops and retrieves something from her purse."
                nicole.c "Turn around's fair play, isn't it?"
                wt_image neighbour_lesbian_2_24
                nicole.c "Open up."
                wt_image neighbour_lesbian_2_25
                "Natalie allows Nicole to use her mouth to wet the toy ..."
                wt_image neighbour_lesbian_2_26
                "... then turns over onto her knees on Nicole's instruction."
                wt_image neighbour_lesbian_2_27
                "Natalie moans as she feels the head of the dildo penetrate her butt ..."
                wt_image neighbour_lesbian_2_28
                "... then moans again as she feels the second prong enter her pussy."
                wt_image neighbour_lesbian_2_29
                "She moans a third time, louder, as Nicole fucks her to orgasm."
                nicole_lesbian_partner_natalie "Aaaahhhhh!!!"
                wt_image neighbour_lesbian_2_23
                "Nicole removes the toy, but she isn't finished with Natalie yet."
                wt_image neighbour_lesbian_2_30
                "Natalie doesn't hesitate as Nicole presents her ass to her."
                wt_image neighbour_lesbian_2_31
                "Flicking her tongue back and forth between Nicole's butthole and sex, Natalie soon has Nicole doing the moaning."
                nicole.c "OOOHHHH!!"
            else:
                "When she has the blonde worked up and sopping, she stops and gets out her toy again."
                wt_image neighbour_lesbian_2_24
                "As Natalie wets the toy with her mouth, Nicole turns and looks at you."
                wt_image neighbour_lesbian_2_25
                nicole.c "Should I use this to fuck both her holes?  Or just one?"
                $ title = "What do you tell her?"
                menu:
                    "Both":
                        wt_image neighbour_lesbian_2_32
                        "Natalie seems happy with your choice. She sighs contentedly as Nicole places the head of the dildo against her anus ..."
                        wt_image neighbour_lesbian_2_28
                        "... and then moans even more contentedly as Nicole slowly pushes the toy in until it's penetrating Natalie's pussy as well."
                        wt_image neighbour_lesbian_2_29
                        "Natalie was already worked up by Nicole's prior attention. It doesn't take long before the feel of the dildo stroking into and out of both her holes takes her over the edge."
                        nicole_lesbian_partner_natalie "Aaaahhhhh!!!"
                    "Just one":
                        if not nicole.has_tag('used_dildo_on_natalie_ass_only_before'):
                            add tags 'used_dildo_on_natalie_ass_only_before' to nicole
                            nicole.c "He picked the number, now I pick the hole.  Lie back and spread your legs."
                            wt_image neighbour_lesbian_2_33
                            nicole.c "Yes, that's right.  I'm picking your ass.  And no, I'm not using the wetted end.  I want to see if you can cum from the feeling of these beads in your ass alone."
                            wt_image neighbour_lesbian_2_34
                            "Nicole watches with rapt fascination as Natalie's ass opens and closes to accept the entrance and exit of each bead in turn."
                            wt_image neighbour_lesbian_2_35
                            "Natalie was already worked up by Nicole's prior attention. By the time the brunette has shoved the beaded end of the toy into and out of her ass a third time, she shudders to a short, but intense orgasm."
                            nicole_lesbian_partner_natalie "Aaahhhh!"
                        else:
                            wt_image neighbour_lesbian_2_33
                            nicole.c "He picked the number, and I think we both know which hole I'm choosing."
                            wt_image neighbour_lesbian_2_34
                            "Natalie holds herself wide open as Nicole slides the beaded end of the toy in and out of her ass, slowly at first, then faster and faster ..."
                            wt_image neighbour_lesbian_2_35
                            "... until the blonde lesbian is climaxing from the feeling of the dildo in her ass."
                            nicole_lesbian_partner_natalie "Aaaahhhhh!!!"
                wt_image neighbour_lesbian_2_30
                "When her orgasm subsides, Natalie's not surprised to find Nicole's ass in her face.  She snakes her tongue into the brunette's crack ..."
                wt_image neighbour_lesbian_2_31
                "... and liking back and forth between Nicole's butthole and sex, brings the already worked up woman over the edge."
                nicole.c "OOOHHHH!!"
            wt_image neighbour_lesbian_2_10
            if not nicole.has_tag('you_jerked_off_on_natalie_before'):
                nicole.c "I know you're not into boys, but I think he enjoyed watching me fuck your ass even more than he liked watching you fuck mine. If he wanted to jerk off on you, you wouldn't mind, would you?"
            else:
                nicole.c "You made him horny again. It's only fair you offer him your cute lesbian tush as a target while he relieves himself."
            $ title = "Take her up on the offer?"
            menu:
                "Yes, jerk off on Natalie":
                    if not nicole.has_tag('you_jerked_off_on_natalie_before'):
                        add tags 'you_jerked_off_on_natalie_before' to nicole
                        wt_image neighbour_lesbian_2_36
                        "Maybe's it the lingering submissive feeling from having been fucked in the ass and then made to eat Nicole's ass out, or maybe she just finds the idea kinky.  Either way Natalie turns around ..."
                        wt_image neighbour_lesbian_2_37
                        "... and offers you a view of her ass as you play with yourself."
                        wt_image neighbour_lesbian_2_38
                        player.c "[player.orgasm_text]"
                        wt_image neighbour_lesbian_2_39
                        nicole_lesbian_partner_natalie "That tickles.  I wasn't expecting it to tickle."
                        player.c "What did you think it would feel like?"
                        nicole_lesbian_partner_natalie "I swear, I've never given a single thought to what it would feel like to have a man cum on me."
                    else:
                        wt_image neighbour_lesbian_2_36
                        "Natalie still looks a little nervous as she turns around ..."
                        wt_image neighbour_lesbian_2_37
                        "... but as instructed, she gamely offers her ass to you as a target.  Nicole's right about it being a cute lesbian tush."
                        wt_image neighbour_lesbian_2_38
                        "... soon it's a cute lesbian tush coated in sperm."
                        player.c "[player.orgasm_text]"
                        wt_image neighbour_lesbian_2_39
                        nicole_lesbian_partner_natalie "That still tickles."
                        player.c "Maybe you're allergic to sperm?"
                        nicole_lesbian_partner_natalie "That'd be a novel explanation for my sexual orientation.  'Sorry, Mom, I know you wanted grandkids, but sperm feels ticklish to me.'"
                    orgasm
                "Not today":
                    nicole_lesbian_partner_natalie "Thanks for inviting me over again.  Nicole's a tiger when the mood strikes her."
                    change player energy by -energy_very_short notify
        elif nicole.has_tag('used_dildo_on_natalie_last_visit'):
            rem tags 'used_dildo_on_natalie_last_visit' from nicole
            wt_image neighbour_lesbian_2_2
            "When Natalie arrives, neither she nor Nicole pay any attention to you ..."
            wt_image neighbour_lesbian_2_3
            "... as they reacquaint themselves with each other's body."
            wt_image neighbour_lesbian_2_40
            "Nicole's nipples seem especially sensitive today ..."
            wt_image neighbour_lesbian_2_41
            "... which encourages Natalie to pay them extra attention."
            wt_image neighbour_lesbian_2_42
            "By the time Natalie spreads her legs, Nicole is already trembling and moaning ..."
            wt_image neighbour_lesbian_2_14
            "... and as soon as Natalia's tongue licks across her clit, Nicole bucks her hips and cums."
            nicole.c "OOOHHHH!!"
            wt_image neighbour_lesbian_2_13
            if not nicole.has_tag('natalie_asked_about_cum_from_nipple_play'):
                add tags 'natalie_asked_about_cum_from_nipple_play' to nicole
                nicole_lesbian_partner_natalie "Can you cum just from having your nipples played with?"
                nicole.c "No.  At least, I don't think so.  You got me really, really close, though."
                nicole_lesbian_partner_natalie "Do you want me to make you cum again?"
                nicole.c "Yes, please!"
            else:
                nicole_lesbian_partner_natalie "You're easy again today.  I want to see you do that again."
            wt_image neighbour_lesbian_2_14
            "The second orgasm takes longer, but not a lot longer."
            nicole.c "OOOHHHH!!"
            wt_image neighbour_lesbian_2_11
            nicole_lesbian_partner_natalie "For being so easy, I'm going to make you work hard for my orgasm.  You're going to spend the next hour between my legs before I let you make me cum."
            wt_image neighbour_lesbian_2_12
            nicole.c "Yes, Ma'am."
            "You're confident Nicole could make Natalie come a lot faster than that.  You're equally confident that she's in no mood to do so, and is looking forward to spending the next hour with her tongue in the blonde lesbian's snatch."
            wt_image neighbour_lesbian_2_11
            "This is going to take a while, so you leave the two of them to their fun."
            add tags 'this_will_take_a_while' to nicole
            change player energy by -energy_very_short notify
        else:
            wt_image neighbour_lesbian_2_2
            "When Natalie arrives, neither she nor Nicole pay any attention to you ..."
            wt_image neighbour_lesbian_2_3
            "... as they reacquaint themselves with each other's body ..."
            wt_image neighbour_lesbian_2_4
            "... and help each other undress."
            wt_image neighbour_lesbian_2_5
            "Nicole has become an expert cunt licker. You wonder if she's been practicing when you aren't around?"
            wt_image neighbour_lesbian_2_11
            "Natalie tries to force Nicole's tongue to where she wants it, but Nicole doesn't let her.  She keeps the blonde woman teetering on the edge of an orgasm ..."
            wt_image neighbour_lesbian_2_12
            "... until she's ready to let her have her release.  With a couple of quick, hard flicks of her tongue, your neighbor brings Natalie to a body wracking orgasm, then laps up every drop that escapes Natalie's quivering pussy"
            nicole_lesbian_partner_natalie "Aaaahhhhh!!!"
            wt_image neighbour_lesbian_2_13
            "Now its Natalie's turn between Nicole's legs."
            wt_image neighbour_lesbian_2_7
            if not nicole.has_tag('natalie_used_dildo_before'):
                "Natalie brings Nicole to the brink of an orgasm, then rolls her over so she can't see the toy she pulls from her purse.  Natalie looks over at you and shows you where she proposes to put the toy."
                $ title = "What do you do?"
                menu:
                    "Nod your approval":
                        add tags 'natalie_used_dildo_before' 'natalie_used_dildo_last_visit' to nicole
                        wt_image neighbour_lesbian_2_15
                        "Nicole looks back in confusion as Natalie pulls her to her knees, then even more confusion as she feels the head of the dildo presses against her rear opening."
                        wt_image neighbour_lesbian_2_16
                        "Natalie takes Nicole's silence as consent, and slowly pushes the double-headed phallus forward until it's not just stretching the brunette's ass, but penetrating her pussy, too.  A confused Nicole looks back, not at Natalie, but at you."
                        player.c "Yes, [nicole.name].  She's fucking your ass.  You like that, don't you?"
                        wt_image neighbour_lesbian_2_8
                        "Nicole's unable to answer, as Natalie begins stroking the phallus in and out.  The proof of your observation comes quickly, though ..."
                        wt_image neighbour_lesbian_2_9
                        "... as Nicole shivers to orgasm."
                        nicole.c "OOOHHHH!!"
                        wt_image neighbour_lesbian_2_18
                        "As Nicole recovers, Natalie leans over and whispers to her."
                        nicole_lesbian_partner_natalie "I think watching me fuck your ass turned him on.  He may need more than a handjob today.  Why don't you offer him your mouth?"
                    "Tell her no":
                        "You shake your head, no. Nicole may not react well to having a dildo of that size shoved in her butt."
                        wt_image neighbour_lesbian_2_6
                        "If Natalie's disappointed, she doesn't show it.  She resumes lapping Nicole's pussy ..."
                        wt_image neighbour_lesbian_2_14
                        "... soon bringing the dark-haired woman to climax."
                        nicole.c "OOOHHHH!!"
                        wt_image neighbour_lesbian_2_10
                        "As Nicole recovers, she reaches out and caresses your cock with her hand."
                        nicole.c "Would you like me to jerk you off?"
            else:
                wt_image neighbour_lesbian_2_17
                "Natalie licks Nicole to the brink of orgasm, then rolls her over and pulls out the toy again."
                wt_image neighbour_lesbian_2_16
                "Submissively, Nicole allows Natalie to pull her to her knees and insert the dildo."
                wt_image neighbour_lesbian_2_8
                "Nicole begins to moan as Natalia moves the dildo in and out, faster and faster ..."
                wt_image neighbour_lesbian_2_9
                "... and is soon shaking from wave after wave of orgasm ripping through her body as Natalie fucks her ass and pussy at the same time."
                nicole.c "OOOHHHH!!"
                wt_image neighbour_lesbian_2_18
                "As Nicole recovers, Natalie leans over and whispers to her."
                nicole_lesbian_partner_natalie "I think watching me fuck your ass turned him on.  He may need more than a handjob today.  Why don't you offer him your mouth?"
                add tags 'natalie_used_dildo_last_visit' to nicole
            $ title = "What do you say?"
            menu:
                "Yes, have Nicole blow you" if nicole.has_tag('natalie_used_dildo_last_visit'):
                    wt_image neighbour_bj_5
                    "Natalie watches as Nicole takes out your cock and puts it in her mouth.  You're not sure how many blowjobs she's witnessed, let alone suggested."
                    wt_image neighbour_bj_1
                    "Nicole's very submissive as she services you.  Having allowed Natalie to have her way with her ass, she now allows you to have your way with her mouth."
                    wt_image neighbour_bj_2
                    "When you're finished face-fucking her and let yourself go, Nicole closes her eyes ad swallows your load."
                    player.c "[player.orgasm_text]"
                    wt_image neighbour_lesbian_2_18
                    nicole_lesbian_partner_natalie "That was cute.  You might be almost as good at sucking cock as you are at licking pussy."
                    $ nicole.blowjob_count += 1
                    $ nicole.swallow_count += 1
                    orgasm
                "Yes, have Nicole jerk you off" if not nicole.has_tag('natalie_used_dildo_last_visit'):
                    wt_image neighbour_hj_1
                    if nicole.has_tag('natalie_watched_handjob'):
                        "Natalie's watched Nicole jerk you off before.  The male anatomy doesn't interest much interest her.  She dresses and leaves while Nicole uses her soft hand to relieve the pressure in your balls inspired by watching the two of them together."
                        player.c "[player.orgasm_text]"
                    else:
                        "As Natalie looks on, Nicole uses her soft hand to relieve the pressure in your balls inspired by watching the two of them together."
                        player.c "[player.orgasm_text]"
                        wt_image neighbour_lesbian_2_10
                        "Presumably Natalie hasn't seen many guys cum before, as she seems to find the process funny.  She doesn't say anything about it, though, just waits until Nicole is done, then thanks you in a less personal way."
                        nicole_lesbian_partner_natalie "Thanks for inviting me over to play with Nicole again."
                        add tags 'natalie_watched_handjob' to nicole
                    $ nicole.handjob_count += 1
                    orgasm notify
                "Not today":
                    nicole_lesbian_partner_natalie "Thanks for inviting me over to play with Nicole again."
                    change player energy by -energy_very_short notify
            if nicole.hypno_count > 1 or nicole.has_tag('teaching_aide'):
                wt_image neighbour_hj_1
                "Natalie is only into girls. So Nicole takes you into your boudoir by herself to make sure you feel appreciated after their show."
                player.c "[player.orgasm_text]"
                $ nicole.handjob_count += 1
                orgasm notify
            else:
                change player energy by -energy_very_short notify
    wt_image current_location.image
    if nicole.has_tag('this_will_take_a_while'):
        rem tags 'this_will_take_a_while' from nicole
        "If anything, it takes longer than an hour before Nicole finally removes herself from between Natalie's legs and they both go home."
    else:
        "The festivities over, Nicole makes herself scarce and you go on with your day."
    call character_location_return(nicole) from _call_character_location_return_110
    return

## Teaching Aide Training Content
label nicole_practice_strip:
    $ nicole.training_session()
    rem tags 'available_today' from nicole
    if nicole.visit_outfit == 1:
        wt_image neighbour_hypno_outfit_2_2
        player.c "You look nice today.  That little black dress suits you."
        wt_image neighbour_shopping_1
        nicole.c "Thanks!"
        player.c "Show me how nice you look taking it off."
        call forced_movement(boudoir) from _call_forced_movement_291
        summon nicole to boudoir
        wt_image neighbour_first_visit_1
        "Nicole giggles."
        nicole.c "I guess I can do that."
        wt_image neighbour_first_visit_2
        "She sways her hips and slowly turns ..."
        wt_image neighbour_first_visit_5
        "... as she pulls up her dress ..."
        wt_image neighbour_first_visit_6
        "... and wiggles her butt."
        wt_image neighbour_first_visit_7
        "Her bra comes off slowly ..."
        if nicole.strip_count < 2:
            wt_image neighbour_first_visit_8
            "... as she spreads her legs."
            nicole.c "Was that good?"
            player.c "You're not done yet.  Show me more."
            wt_image neighbour_outfit_1_3
            nicole.c "Like this?"
            player.c "You're learning.  Remember to keep practicing."
            "She giggles."
            nicole.c "Greg is going to owe you big time."
            change player energy by -energy_short
        elif nicole.strip_count < 3:
            wt_image neighbour_first_visit_8
            "... as she spreads her legs ..."
            wt_image neighbour_outfit_1_3
            "... and pulls her panties aside."
            nicole.c "Did I do a good job?"
            player.c "You can do better.  Keep spreading."
            wt_image neighbour_outfit_1_5
            "She hesitates for a moment ..."
            wt_image neighbour_hypno_outfit_2_6
            "... then pulls her labia apart for your examination."
            player.c "You're wet."
            "She nods in embarrassment."
            #$ nicole.horny_from_dance = True ## not used
            player.c "That's good.  It should make practicing easier."
            change player energy by -energy_short
        else:
            wt_image neighbour_first_visit_8
            "... as she spreads her legs ..."
            wt_image neighbour_outfit_1_5
            "... pulls her panties aside ..."
            wt_image neighbour_hypno_outfit_2_6
            "... and spreads her labia apart for you to see."
            player.c "You're wet."
            wt_image neighbour_outfit_1_3
            nicole.c "I should be embarrassed to admit this, but I'm horny today and taking my clothes off for you just made it worse."
            #$ nicole.horny_from_dance = True ##not here
            $ title = "What do you do?"
            menu:
                "Fuck her":
                    if nicole.beg_count > 0:
                        player.c "What should a horny girl do when she wants cock?"
                        wt_image neighbour_hypno_outfit_2_23
                        "A small shudder passes over Nicole, then she turns and presents her wet pussy to you."
                        nicole.c "She should beg for it.  Please, can I have your cock?  Please, I want you to fuck my pussy and make me cum."
                        $ nicole.beg_count += 1
                    else:
                        wt_image neighbour_hypno_outfit_2_17
                        "Nicole's eyes light up as she sees you pull your clothes off.  She turns and presents her wet pussy to you."
                    wt_image neighbour_sex_10
                    "Nicole moans as you penetrate her ..."
                    nicole.c "ooohhhh"
                    wt_image neighbour_sex_11
                    "... and though you think she's trying to control herself and hold as long as she can while you fuck her ..."
                    nicole.c "oooohhhhh"
                    wt_image neighbour_sex_3
                    "... she's soon spasming to orgasm around your cock."
                    nicole.c "OOOHHHH!!"
                    $ nicole.orgasm_count += 1
                    $ title = "What now?"
                    menu:
                        "It's your turn":
                            wt_image neighbour_sex_13
                            "Her needs met, you can look after your own.  You pound into her wet sex, faster and faster ..."
                            wt_image neighbour_sex_14
                            "... until you flood her insides with your seed."
                            player.c "[player.orgasm_text]"
                            orgasm
                            $ nicole.sex_count += 1

                        "Stop there":
                            wt_image neighbour_sex_12
                            "Nicole looks at you in shock as she realizes you're stopping."
                            nicole.c "How do you do that?  I've never known a guy who could fuck me and than stop without wanting to cum himself."
                            player.c "I'm a professional."
                            change player energy by -energy_short

                "Tell her to play with herself":
                    player.c "Do something about it, then."
                    nicole.c "While you watch?"
                    player.c "Yes"
                    wt_image neighbour_hypno_outfit_2_15
                    "She rubs her fingers across her wet and tender labia ..."
                    wt_image neighbour_hypno_outfit_2_16
                    "... then pushes a finger inside ..."
                    nicole.c "oohhh"
                    wt_image neighbour_hypno_outfit_2_24
                    "... and frigs herself to climax."
                    nicole.c "ooohhhhh  ...  OOOHHHH!!"
                    wt_image neighbour_first_visit_19
                    "When she recovers her breath, Nicole grins up at you."
                    nicole.c "I hope you liked the show."
                    player.c "I did, though maybe not as much as you did."
                    "She giggles at your teasing."
                    change player energy by -energy_short
                    $ nicole.masturbation_count += 1
                    $ nicole.orgasm_count += 1

                "Send her home":
                    player.c "Sounds like Greg's going to have fun when he gets home."
                    wt_image neighbour_outfit_1_6
                    nicole.c "You're mean.  I didn't know being trained by you meant I was going to be sent home horny."
                    player.c "If it was easy, you wouldn't need training, would you?"
                    change player energy by -energy_short
                    $ nicole.horny_from_dance = True
        if not nicole.horny_from_dance:
            call forced_movement(living_room) from _call_forced_movement_292
            summon nicole to living_room
            wt_image neighbour_outfit_1_4
            nicole.c "Thanks for the training!"
        else:
            $ nicole.horny_from_dance = False
    elif nicole.visit_outfit == 2:
        wt_image neighbour_outfit_2_11
        player.c "Cute outfit.  Did you come straight here after grocery shopping?"
        nicole.c "Funny.  I figured you'd have me naked soon anyway, so why dress?  I snuck in around the back way."
        player.c "You guessed right.  Show me how your strip tease skills are coming along."
        nicole.c "Out of this?"
        player.c "Sure.  Why not?"
        nicole.c "It'll be boring.  Wait here."
        call forced_movement(living_room) from _call_forced_movement_293
        summon nicole to living_room
        wt_image living_room.image
        "She disappears before you can stop her."
        wt_image neighbour_inside_1
        "A few minutes later, she returns."
        player.c "You went home and got dressed?"
        wt_image neighbour_inside_2
        nicole.c "Yes.  I wasn't going to show myself off for you in an old tank top and panties."
        player.c "It's your body I'm interested in, not your clothes.  A strip tease is about acting sexy."
        wt_image neighbour_inside_5
        nicole.c "Which I can't do if I don't feel good about what I'm wearing.  Do you want me to take my clothes off for you or not?"
        player.c "If you're finally ready, yeah.  Please proceed."
        wt_image neighbour_strip_practice_2_1
        "She begins swaying gently to some imaginary music ..."
        wt_image neighbour_strip_practice_2_2
        "... pulling down her top as she dances ..."
        wt_image neighbour_hypnotized_inside_2
        "... showing off her decidedly erect nipples."
        wt_image neighbour_strip_practice_2_3
        "... then she wriggles out of her skirt ..."
        if nicole.strip_count < 2:
            wt_image neighbour_strip_practice_2_4
            "... and looks at you."
            nicole.c "Was that good?"
            player.c "You're not done yet.  Show me more."
            wt_image neighbour_strip_practice_2_5
            "She resumes turning and swaying, this time wearing only her panties."
            player.c "That's good, Nicole.  Now show me more of you."
            wt_image neighbour_strip_practice_2_6
            "Hooking a finger in the sides of her panties ..."
            wt_image neighbour_strip_practice_2_7
            "... she slowly slides them down her long legs ..."
            wt_image neighbour_strip_practice_2_8
            "... then turns and gives her butt a little wiggle, sending her panties tumbling the rest of the way to the ground ..."
            wt_image neighbour_strip_practice_2_9
            "... as she sits and spreads her legs."
            nicole.c "Was that better?"
            player.c "You're learning.  Remember to keep practicing."
            "She giggles."
            nicole.c "Greg is going to owe you big time."
            change player energy by -energy_short
        elif nicole.strip_count < 3:
            wt_image neighbour_strip_practice_2_5
            "... turns and sways wearing just her panties ..."
            wt_image neighbour_strip_practice_2_7
            "... then pulls those down ..."
            wt_image neighbour_strip_practice_2_8
            "... wiggling her butt to finish removing them ..."
            wt_image neighbour_strip_practice_2_9
            "... then sits and spreads her legs."
            nicole.c "Did I do a good job?"
            player.c "You can do better.  Keep spreading."
            wt_image neighbour_strip_practice_2_10
            "She hesitates for a moment ..."
            wt_image neighbour_hypnotized_inside_5
            "... then pulls her labia apart for your examination."
            wt_image neighbour_strip_practice_2_11
            player.c "You're wet."
            wt_image neighbour_hypnotized_inside_5
            "She just nods in embarrassment."
            #$ nicole.horny_from_dance = True ##not needed
            player.c "That's good.  It should make practicing easier."
            change player energy by -energy_short
        else:
            wt_image neighbour_strip_practice_2_5
            "... turns and sways wearing just her panties ..."
            wt_image neighbour_strip_practice_2_7
            "... then pulls those down ..."
            wt_image neighbour_strip_practice_2_8
            "... wiggling her butt to finish removing them."
            wt_image neighbour_strip_practice_2_9
            "She sits and spreads her legs ..."
            wt_image neighbour_hypnotized_inside_5
            "... then pulls her labia apart for your examination."
            wt_image neighbour_strip_practice_2_11
            player.c "You're wet."
            wt_image neighbour_hypnotized_inside_5
            nicole.c "I should be embarrassed to admit this, but I was horny coming over here and taking my clothes off for you just made it worse."
            #$ nicole.horny_from_dance = True ##not here
            $ title = "What do you do?"
            menu:
                "Fuck her":
                    if nicole.beg_count > 0:
                        player.c "What should a horny girl do when she wants cock?"
                        wt_image neighbour_strip_practice_2_10
                        "A small shudder passes over Nicole as she looks up at you."
                        nicole.c "She should beg for it.  Please, can I have your cock?  Please, I want you to fuck my pussy and make me cum."
                        $ nicole.beg_count += 1
                    else:
                        pass
                    wt_image neighbour_strip_practice_2_16
                    "Nicole trembles with excitement as you take your cock out.  She walks over to the ottoman ..."
                    wt_image neighbour_strip_practice_2_17
                    "... lies down, and lifts her leg, allowing you access."
                    nicole.c "ooohhhh"
                    wt_image neighbour_strip_practice_2_18
                    "Even though you think she's trying to control herself and hold as long as she can while you fuck her ..."
                    nicole.c "oooohhhhh"
                    wt_image neighbour_strip_practice_2_19
                    "... she's soon spasming to orgasm around your cock."
                    nicole.c "OOOHHHH!!"
                    $ nicole.orgasm_count += 1
                    $ title = "What now?"
                    menu:
                        "It's your turn":
                            wt_image neighbour_strip_practice_2_20
                            "Her desire sated, you can look after your own.  You thrust into your contented neighbor, faster and faster ..."
                            wt_image neighbour_strip_practice_2_21
                            "... until you flood her insides with your seed."
                            player.c "[player.orgasm_text]"
                            $ nicole.sex_count += 1
                            orgasm

                        "Stop there":
                            wt_image neighbour_strip_practice_2_22
                            "Nicole`s disappointed as you stop thrusting and pull out of her."
                            nicole.c "How do you do that?  I've never known a guy who could fuck me and than stop without wanting to cum himself."
                            player.c "I'm a professional."
                            change player energy by -energy_short
                "Tell her to play with herself":
                    player.c "Do something about it, then."
                    nicole.c "While you watch?"
                    player.c "Yes"
                    wt_image neighbour_strip_practice_2_11
                    "She slides her fingers across her wet and tender labia ..."
                    wt_image neighbour_strip_practice_2_13
                    "... rubs her clit ..."
                    nicole.c "oohhh"
                    wt_image neighbour_strip_practice_2_14
                    "... then inserts a finger and frigs herself to climax."
                    nicole.c "ooohhhhh  ...  OOOHHHH!!"
                    wt_image neighbour_strip_practice_2_15
                    "When she recovers her breath, Nicole grins at you."
                    nicole.c "I hope you liked the show."
                    player.c "I did, though maybe not as much as you did."
                    "She giggles at your teasing."
                    change player energy by -energy_short
                    $ nicole.masturbation_count += 1
                    $ nicole.orgasm_count += 1
                "Send her home":
                    player.c "Sounds like Greg's going to have fun when he gets home."
                    wt_image neighbour_inside_13
                    nicole.c "Ouch.  That's mean.  I didn't know being trained by you meant I was going to be sent home horny."
                    player.c "If it was easy, you wouldn't need training, would you?"
                    change player energy by -energy_short
                    $ nicole.horny_from_dance = True
        if not nicole.horny_from_dance:
            wt_image neighbour_inside_13
            nicole.c "Thanks for the training!"
        else:
            $ nicole.horny_from_dance = False
    else:
        wt_image neighbour_outfit_3_1
        player.c "Laundry day?"
        wt_image neighbour_outfit_3_7
        nicole.c "Ha ha.  Don't you like looking at me in my underwear?"
        player.c "I'd like looking at you getting out of your underwear even better. Let's see how your strip tease skills are coming along."
        nicole.c "I'll go change into something."
        player.c "No.  What you're wearing now is fine.  Show me how seductively you can take them off."
        wt_image neighbour_outfit_3_2
        "She sits down and gives you a coy smile ..."
        wt_image neighbour_outfit_3_8
        "... then spins around in the chair ..."
        wt_image neighbour_outfit_3_9
        " ... and slowly slips the bra strap off her shoulder."
        wt_image neighbour_outfit_3_10
        "Flashing you a seductive look .."
        if nicole.strip_count < 2:
            wt_image neighbour_outfit_3_11
            "... she turns back to face you."
            nicole.c "Was that good?"
            player.c "For what it was, yes.  You still have one more piece of clothing to lose."
            wt_image neighbour_outfit_3_12
            "She stands up and pushes her panties down ..."
            wt_image neighbour_outfit_3_13
            "... stepping out of them as gracefully as she can ..."
            wt_image neighbour_outfit_3_14
            "... then wiggles her butt at you ..."
            wt_image neighbour_outfit_3_15
            "... as she climbs back on the chair."
            nicole.c "Was that better?"
            player.c "You're learning.  Remember to keep practicing."
            "She giggles."
            nicole.c "Greg is going to owe you big time."
            change player energy by -energy_short
        elif nicole.strip_count < 3:
            wt_image neighbour_outfit_3_12
            "... turns around to remove her panties ..."
            wt_image neighbour_outfit_3_13
            "... stepping out of them as gracefully as she can ..."
            wt_image neighbour_outfit_3_14
            "... then wiggles her butt at you ..."
            wt_image neighbour_outfit_3_15
            "... as she climbs back on the chair."
            nicole.c "Did I do a good job?"
            player.c "You can do better.  You're hiding something I want you to give me a good view of."
            wt_image neighbour_outfit_3_16
            "She blushes and hesitates for a moment ..."
            wt_image neighbour_outfit_3_17
            "... then lifts her leg ..."
            wt_image neighbour_outfit_3_18
            "... flashes you a smile ..."
            wt_image neighbour_outfit_3_19
            "... and spreads herself open for your viewing pleasure."
            player.c "That's better.  Think you can practice that?"
            "She nods."
            change player energy by -energy_short
        else:
            wt_image neighbour_outfit_3_12
            "... turns around to remove her panties ..."
            wt_image neighbour_outfit_3_13
            "... stepping out of them as gracefully as she can."
            wt_image neighbour_outfit_3_14
            "Then she wiggles her butt at you ..."
            wt_image neighbour_outfit_3_16
            "... climbs back on the chair ..."
            wt_image neighbour_outfit_3_17
            "... and lifts her leg ..."
            wt_image neighbour_outfit_3_19
            "... to spread herself open for you."
            #$ nicole.horny_from_dance = False ##not needed
            player.c "Not wet from stripping for me today?"
            nicole.c "I'm not always horny, you know."
            player.c "I didn't, actually."
            "She giggles."
            $ title = "What do you do?"
            menu:
                "Fuck her":
                    wt_image neighbour_outfit_3_18
                    "She may not be horny after her strip tease, but you are.  She grins as you remove your clothes."
                    wt_image neighbour_outfit_3_20
                    "A few strokes of your fingers along her sex moisten her enough to allow you entry.  She coos softly as you penetrate her."
                    nicole.c "oooooo"
                    wt_image neighbour_outfit_3_21
                    "Her body warms quickly to the fucking, letting you pound her faster and faster ..."
                    wt_image neighbour_outfit_3_22
                    "... until you empty your load inside her."
                    $ nicole.sex_count += 1
                    player.c "[player.orgasm_text]"
                    orgasm
                "Send her home":
                    "Turns out, you're not horny today either."
                    change player energy by -energy_short
        wt_image neighbour_outfit_3_10
        nicole.c "Thanks for the training!"
    $ nicole.strip_count += 1
    call character_location_return(nicole) from _call_character_location_return_111
    notify
    wt_image living_room.image
    return

label nicole_practice_bj:
    $ nicole.training_session()
    rem tags 'available_today' from nicole
    if nicole.visit_outfit == 1:
        call forced_movement(boudoir) from _call_forced_movement_294
        summon nicole to boudoir
        wt_image neighbour_hypno_outfit_2_2
        player.c "You look nice today.  Very classy."
        wt_image neighbour_shopping_1
        nicole.c "Thank you!"
        player.c "I enjoy watching classy women suck my cock. Show me how fast you can transform from princess to dick sucking slut."
        wt_image neighbour_outfit_1_6
        "She puts down her purse ..."
        if not nicole.slut_discussion:
            $ nicole.slut_discussion = True
            wt_image neighbour_first_visit_31
            "... and takes a seat on the bed."
            nicole.c "You don't really think of me as a slut, do you?"
            player.c "When you're sucking my cock I do.  Does that surprise you?"
            wt_image neighbour_outfit_1_7
            nicole.c "Sort of, yeah."
            player.c "Spread your legs."
            wt_image neighbour_outfit_1_8
            player.c "Take off the dress."
            wt_image neighbour_outfit_1_9
            player.c "This isn't a strip tease, you don't have to go slow."
            wt_image neighbour_first_visit_7
            player.c "Remove the bra, too."
            wt_image neighbour_first_visit_28
            player.c "Are you going to suck my cock now?"
            "She hesitates a moment before answering."
            wt_image neighbour_hypno_outfit_2_4
            nicole.c "I guess.  Yes."
            player.c "Why?  Am I making you do so?  Did you undress because you're afraid of me?"
            wt_image neighbour_first_visit_21
            nicole.c "No"
            player.c "Am I your husband?"
            "She shakes her head."
            player.c "So you're going to willingly suck the cock of a man you're not married to, just because he wants you to. What does that make you?"
            wt_image neighbour_kneel_8
            nicole.c "A slut, I guess."
            player.c "A woman who knows what she wants, sexually, and isn't afraid to admit it. You want to be sucking my cock right now, don't you?"
            "She nods."
            player.c "Say it.  And be proud about it.  It's your sexuality.  Embrace it."
            wt_image neighbour_kneel_7
            nicole.c "I would enjoy sucking your cock. I'm looking forward to it."
            player.c "Then get on your knees and start sucking my cock, slut, and no more silly hang ups."
            wt_image neighbour_first_visit_11
            "It's not the best blow job you've ever had, but it's one of the most energetic. Nicole throws herself into an enthusiastic pleasuring of your dick ..."
            wt_image neighbour_first_visit_12
            "... which soon earns her a mouthful of jizz."
            player.c "[player.orgasm_text]"
            $ nicole.swallow_count += 1
        else:
            wt_image neighbour_outfit_1_1
            "... climbs onto the bed ..."
            wt_image neighbour_first_visit_8
            "... and strips."
            if nicole.blowjob_practice < 4:
                wt_image neighbour_first_visit_37
                "She starts to take your cock into her mouth when you stop her."
                player.c "Balls first. Warm them up."
                wt_image neighbour_first_visit_23
                nicole.c "Oops. Sorry."
            wt_image neighbour_first_visit_10
            "She warms up your balls with her soft hands ..."
            wt_image neighbour_hypno_outfit_2_11
            "... then takes your cock into her mouth."
            if nicole.blowjob_practice < 2:
                wt_image neighbour_first_visit_22
                "She tackles your cock a little more eagerly than you're in the mood for."
                wt_image neighbour_first_visit_23
                player.c "Slow down.  Take your cue from the guy.  He'll let you know when you should go fast.  Until then, take it slow."
                wt_image neighbour_first_visit_15
                "She takes your cock back in her mouth, this time licking and sucking at a more leisurely pace ..."
            else:
                wt_image neighbour_first_visit_15
                "It's a nice, leisurely blow job ..."
            wt_image neighbour_first_visit_22
            "... until the thrusting of your hips and the change in the pace of your breathing lets her know it's time to go faster."
            if nicole.blowjob_practice > 3:
                wt_image neighbour_hypno_outfit_2_19
                "Nicole, look at me."
                $ title = "Where do you want to cum?"
                menu:
                    "On her face":
                        if nicole.facial_count == 0:
                            player.c "It's time for your next lesson.  I want you to finish the blow job a different way, today."
                            "She hesitates a moment."
                            nicole.c "You want to cum on my face?"
                            player.c "Yes"
                            wt_image neighbour_bj_6
                            player.c "[player.orgasm_text]"
                            wt_image neighbour_bj_7
                            player.c "How does that feel?"
                            nicole.c "Sticky"
                        elif nicole.facial_count == 1:
                            player.c "Ready to take my cum on your face again?"
                            "She nods."
                            wt_image neighbour_bj_6
                            player.c "[player.orgasm_text]"
                            wt_image neighbour_bj_8
                            player.c "Still find the sensation just sticky?"
                            nicole.c "It's actually kind of sexy.  In a sticky sort of way."
                        else:
                            wt_image neighbour_bj_9
                            player.c "[player.orgasm_text]"
                            nicole.c "Mmmm.  That's hot when you get used to it."
                        $ nicole.facial_count += 1
                    "In her mouth":
                        wt_image neighbour_bj_5
                        player.c "[player.orgasm_text]"
                        $ nicole.swallow_count += 1
            else:
                wt_image neighbour_first_visit_15
                player.c "[player.orgasm_text]"
                $ nicole.swallow_count += 1
        wt_image neighbour_first_visit_2
    elif nicole.visit_outfit == 2:
        wt_image neighbour_outfit_2_11
        player.c "Were you in a rush?"
        nicole.c "I figured you'd rather I come over quickly, rather than wasting time getting dressed."
        player.c "I love it when a woman's in a rush to be a dick sucking slut."
        if not nicole.slut_discussion:
            $ nicole.slut_discussion = True
            wt_image neighbour_outfit_2_12
            nicole.c "You don't really think of me as a slut, do you?"
            player.c "When you're sucking my cock I do.  Does that surprise you?"
            nicole.c "Sort of, yeah."
            wt_image neighbour_outfit_2_13
            player.c "Turn around so I can look at you."
            wt_image neighbour_outfit_2_12
            player.c "Give me your hand."
            wt_image neighbour_outfit_2_14
            "You place her hand on your cock.  She instinctively starts stroking it."
            player.c "You ran over here without even bothering to put on pants or a skirt. Did I make you do that? Did you do so because you're afraid of me?"
            wt_image neighbour_outfit_2_15
            nicole.c "No"
            player.c "Look at my cock."
            wt_image neighbour_outfit_2_14
            player.c "Am I your husband?  Is that your husband's cock?"
            "She shakes her head."
            player.c "You willingly ran over here without even stopping to get dressed so you can fondle the cock of a man you're not married to.  What does that make you?"
            nicole.c "A slut, I guess."
            player.c "A woman who knows what she wants, sexually, and isn't afraid to admit it.  You want to be sucking my cock right now, don't you?"
            "She nods."
            player.c "Say it."
            wt_image neighbour_outfit_2_16
            nicole.c "I would enjoy sucking your cock.  I'm looking forward to it."
            player.c "Then start sucking my dick, slut, and no more silly hang ups."
            wt_image neighbour_outfit_2_17
            "It's not the best blow job you've ever had ..."
            wt_image neighbour_outfit_2_18
            "... but it's one of the most energetic."
            wt_image neighbour_outfit_2_19
            "Nicole throws herself into an enthusiastic pleasuring of your dick ..."
            wt_image neighbour_outfit_2_2
            "... which soon earns her a mouthful of jizz."
            player.c "[player.orgasm_text]"
            $ nicole.swallow_count += 1
        else:
            wt_image neighbour_outfit_2_15
            "She steps up to you ..."
            wt_image neighbour_outfit_2_20
            "... removes your cock ..."
            if nicole.blowjob_practice < 4:
                wt_image neighbour_outfit_2_17
                "... and puts your cock into her mouth when you stop her."
                wt_image neighbour_outfit_2_21
                nicole.c "What's wrong?"
                player.c "Balls first.  Warm them up before you start sucking."
                nicole.c "Shoot. I forgot."
                wt_image neighbour_outfit_2_22
                "She shifts her attention to your balls, rubbing her soft hands gently across them."
            else:
                wt_image neighbour_outfit_2_22
                "... and rubs her soft hands gently across your balls."
            wt_image neighbour_outfit_2_14
            "When your balls are warmed and your cock throbbing, she lowers her head ..."
            if nicole.blowjob_practice < 2:
                wt_image neighbour_outfit_2_17
                "... and tackles your cock, a little more eagerly than you're in the mood for."
                wt_image neighbour_outfit_2_21
                player.c "Slow down.  Take your cue from the guy.  He'll let you know when you should go fast.  Until then, take it slow."
                nicole.c "Okay.  Sorry."
                wt_image neighbour_outfit_2_23
                "She takes your cock back in her mouth, this time licking and sucking at a more leisurely pace ..."
            else:
                wt_image neighbour_outfit_2_23
                "... and begins a nice, leisurely blow job ..."
            wt_image neighbour_outfit_2_18
            "... until the thrusting of your hips and the change in the pace of your breathing ..."
            wt_image neighbour_outfit_2_19
            "... lets her know it's time to go faster."
            if nicole.blowjob_practice > 3:
                $ title = "Where do you want to cum?"
                menu:
                    "On her face":
                        if nicole.facial_count == 0:
                            wt_image neighbour_outfit_2_21
                            player.c "Nicole, look at me.  It's time for your next lesson.  Put your face down close to my cock."
                            wt_image neighbour_outfit_2_16
                            player.c "I want you to finish the blow job a different way, today."
                            "She hesitates a moment."
                            nicole.c "You want to cum on my face?"
                            player.c "Yes"
                            wt_image neighbour_bj_3
                            "She closes her eyes and positions her face in front of your cock."
                            wt_image neighbour_bj_4
                            player.c "[player.orgasm_text]"
                            wt_image neighbour_bj_10
                            player.c "How does that feel?"
                            nicole.c "Sticky"
                        elif nicole.facial_count == 1:
                            wt_image neighbour_outfit_2_21
                            player.c "Ready to take my cum on your face again?"
                            wt_image neighbour_outfit_2_16
                            "She nods ..."
                            wt_image neighbour_bj_3
                            "... and positions her face in front of your cock."
                            wt_image neighbour_bj_4
                            player.c "[player.orgasm_text]"
                            wt_image neighbour_bj_10
                            player.c "Still find the sensation just sticky?"
                            nicole.c "It's actually kind of sexy.  In a sticky sort of way."
                        else:
                            wt_image neighbour_bj_3
                            "A touch on her shoulder is enough to tell her what you want."
                            wt_image neighbour_bj_4
                            player.c "[player.orgasm_text]"
                            wt_image neighbour_bj_11
                            nicole.c "Mmmm.  That's hot when you get used to it."
                        $ nicole.facial_count += 1

                    "In her mouth":
                        wt_image neighbour_outfit_2_2
                        player.c "[player.orgasm_text]"
                        $ nicole.swallow_count += 1

            else:
                wt_image neighbour_outfit_2_2
                player.c "[player.orgasm_text]"
                $ nicole.swallow_count += 1
        wt_image neighbour_outfit_2_13
    else:
        wt_image neighbour_outfit_3_1
        player.c "Do you have an exhibitionist fetish you'd like to tell me about?"
        nicole.c "I was careful.  No one saw me coming over here."
        player.c "Just as well.  You might've been embarrassed to explain you were rushing over to be a dick sucking slut."
        if not nicole.slut_discussion:
            $ nicole.slut_discussion = True
            wt_image neighbour_outfit_3_23
            nicole.c "You don't really think of me as a slut, do you?"
            player.c "When you're sucking my cock I do.  Does that surprise you?"
            nicole.c "Sort of, yeah."
            wt_image neighbour_outfit_3_24
            player.c "Spread your legs."
            wt_image neighbour_outfit_3_25
            player.c "Remove your bra."
            wt_image neighbour_outfit_3_26
            player.c "Are you going to suck my cock now?"
            "She hesitates a moment before answering."
            nicole.c "I guess.  Yes."
            player.c "Why? Am I making you do so? Did you prance over here in your underwear and display yourself for me because you're scared of me?"
            nicole.c "No"
            player.c "Am I your husband?"
            "She shakes her head."
            player.c "So you're going to willingly suck the cock of a man you're not married to, just because he wants you to. What does that make you?"
            wt_image neighbour_outfit_3_11
            nicole.c "A slut, I guess."
            wt_image neighbour_outfit_3_27
            player.c "A woman who knows what she wants, sexually, and isn't afraid to admit it. Take my cock in your hand."
            wt_image neighbour_outfit_3_28
            player.c "You're wet.  You want to be sucking my cock right now, don't you?"
            "She nods."
            player.c "Say it."
            nicole.c "I would enjoy sucking your cock.  I'm looking forward to it."
            wt_image neighbour_outfit_3_29
            player.c "Then start sucking my dick, slut, and no more silly hang ups."
            wt_image neighbour_outfit_3_3
            "She rubs her pussy as she sucks you. It's not the best blow job you've ever had ..."
            wt_image neighbour_outfit_3_30
            "... but watching her touch herself as she pleasures your dick is fun ..."
            wt_image neighbour_outfit_3_31
            "... and when you're ready to cum ..."
            wt_image neighbour_outfit_3_6
            "... she sinks to her knees to receive your load."
            player.c "[player.orgasm_text]"
            $ nicole.swallow_count += 1
        else:
            wt_image neighbour_outfit_3_10
            "She smiles as she removes her bra and takes a seat in front of you ..."
            wt_image neighbour_outfit_3_32
            "... and takes your cock in her hand."
            if nicole.blowjob_practice < 4:
                wt_image neighbour_outfit_3_31
                "She's about to put your cock into her mouth when you stop her."
                wt_image neighbour_outfit_3_33
                player.c "Balls first.  Warm them up."
                nicole.c "Oh. Right."
            wt_image neighbour_outfit_2_22
            "Nicole cups your balls in her soft hands and rubs them gently ..."
            wt_image neighbour_outfit_3_29
            "... then takes your cock into her mouth ..."
            if nicole.blowjob_practice < 2:
                wt_image neighbour_outfit_3_33
                "... a little more eagerly than you're in the mood for."
                player.c "Slow down.  Take your cue from the guy.  He'll let you know when you should go fast.  Until then, take it slow."
                wt_image neighbour_outfit_3_31
                "She takes your cock back in her mouth, this time licking and sucking at a more leisurely pace ..."
            else:
                wt_image neighbour_outfit_3_31
                "... licking and sucking it gently.  It's a nice, leisurely blow job ..."
            wt_image neighbour_outfit_3_34
            "... until the thrusting of your hips and the change in the pace of your breathing lets her know it's time to drop to her knees to finish you off."
            if nicole.blowjob_practice > 3:
                $ title = "Where do you want to cum?"
                menu:
                    "On her face":
                        if nicole.facial_count == 0:
                            wt_image neighbour_outfit_3_35
                            player.c "Nicole, look at me.  It's time for your next lesson.  I want you to finish the blow job a different way, today."
                            "She hesitates a moment."
                            nicole.c "You want to cum on my face?"
                            player.c "Yes"
                            wt_image neighbour_outfit_3_36
                            "She closes her eyes and positions her face in front of your cock."
                            player.c "[player.orgasm_text]"
                            player.c "How does that feel?"
                            nicole.c "Sticky"
                        elif nicole.facial_count == 1:
                            wt_image neighbour_outfit_3_35
                            player.c "Ready to take my cum on your face again?"
                            "She nods ..."
                            wt_image neighbour_outfit_3_36
                            player.c "[player.orgasm_text]"
                            wt_image neighbour_outfit_3_37
                            player.c "Still find the sensation just sticky?"
                            nicole.c "It's actually kind of sexy.  In a sticky sort of way."
                        else:
                            wt_image neighbour_outfit_3_35
                            player.c "Nicole, look at me."
                            wt_image neighbour_shower_6
                            player.c "[player.orgasm_text]"
                            wt_image neighbour_outfit_3_38
                            nicole.c "Mmmm.  That's hot when you get used to it."
                        $ nicole.facial_count += 1
                    "In her mouth":
                        wt_image neighbour_outfit_3_6
                        player.c "[player.orgasm_text]"
                        $ nicole.swallow_count += 1
            else:
                wt_image neighbour_outfit_3_6
                player.c "[player.orgasm_text]"
                $ nicole.swallow_count += 1
        wt_image neighbour_outfit_3_10
    nicole.c "Am I getting better?"
    player.c "I'll let you know after you give me head a few more times."
    "She giggles as she leaves."
    $ nicole.blowjob_count += 1
    $ nicole.blowjob_practice += 1
    if not living_room.is_here:
        call forced_movement(living_room) from _call_forced_movement_295
    call character_location_return(nicole) from _call_character_location_return_112
    orgasm notify
    wt_image living_room.image
    return

label nicole_practice_fuck:
    $ nicole.training_session()
    rem tags 'available_today' from nicole
    if nicole.visit_outfit == 1:
        call forced_movement(boudoir) from _call_forced_movement_296
        summon nicole to boudoir
        wt_image neighbour_hypno_outfit_2_2
        player.c "Do you know what men think when they see a pretty woman in a little black dress?"
        wt_image neighbour_first_visit_1
        nicole.c "How nice she looks?"
        player.c '"I wonder how good she is in the sack?"'
        wt_image neighbour_hypno_outfit_2_3
        nicole.c "Really?  A little black dress has that effect?"
        player.c "Nope, that's just what men think whenever they see a pretty woman."
        wt_image neighbour_first_visit_30
        "She giggles."
        nicole.c "Let me guess.  You want me to show you how good I am in the sack?"
        player.c "I can't have a teaching aide who isn't an expert."
        wt_image neighbour_outfit_1_1
        nicole.c "You've already had sex with me.  Don't you think I'm pretty good?"
        player.c "You could get better."
        wt_image neighbour_first_visit_8
        nicole.c "Really?  You think I still need practice?"
        wt_image neighbour_first_visit_9
        "She doesn't, actually, as your rock hard cock knows well ..."
        wt_image neighbour_sex_7
        "... but that doesn't stop you from giving her instructions anyway."
        nicole.c "oohhh"
        wt_image neighbour_first_visit_14
        player.c "Slower"
        nicole.c "oohhh ... okay"
        wt_image neighbour_first_visit_20
        player.c "Turn around"
        nicole.c "All right ..."
        wt_image neighbour_sex_8
        nicole.c "... like this?"
        wt_image neighbour_sex_4
        player.c "Faster"
        nicole.c "ooohhhh"
        wt_image neighbour_sex_15
        nicole.c "OOOHHHH!!"
        player.c "Don't stop moving your hips.  Keep riding me as you cum."
        wt_image neighbour_sex_9
        player.c "[player.orgasm_text]"
        wt_image neighbour_first_visit_14
        nicole.c "Is my fucking getting better?"
        player.c "A few more lessons and you'll be okay."
        call forced_movement(living_room) from _call_forced_movement_297
    elif nicole.visit_outfit == 2:
        wt_image neighbour_outfit_2_11
        player.c "Nice outfit.  I really like the invisible pants.  Shows off your legs."
        wt_image neighbour_outfit_2_1
        nicole.c "You like my legs?"
        player.c "I do.  I'm looking forward to learning whether you've figured out what to do when you spread them."
        wt_image neighbour_outfit_2_24
        nicole.c "You've already had sex with me.  Don't you think I'm pretty good?"
        player.c "You could get better."
        wt_image neighbour_outfit_2_8
        nicole.c "Really?"
        wt_image neighbour_outfit_2_21
        nicole.c "You think I still need practice?"
        wt_image neighbour_outfit_2_25
        "She doesn't, actually, but that doesn't stop you from giving her instructions anyway."
        nicole.c "oohhh"
        wt_image neighbour_outfit_2_26
        player.c "Slower"
        nicole.c "oohhh ... okay"
        wt_image neighbour_outfit_2_27
        player.c "Move your hips back and forth, not just up and down."
        nicole.c "o ... okay ... ooohhhh"
        wt_image neighbour_outfit_2_3
        player.c "Faster"
        nicole.c "ooohhhh ... oooohhhhh"
        wt_image neighbour_outfit_2_28
        nicole.c "OOOHHHH!!"
        player.c "Keep moving.  Don't stop riding me as you cum."
        wt_image neighbour_outfit_2_29
        player.c "[player.orgasm_text]"
        wt_image neighbour_outfit_2_26
        nicole.c "Is my fucking getting better?"
        player.c "A few more lessons and you'll be okay."
        call forced_movement(living_room) from _call_forced_movement_298
    else:
        wt_image neighbour_outfit_3_1
        player.c "Trouble picking out a dress to wear?"
        wt_image neighbour_outfit_3_7
        nicole.c "Funny.  Do I need a dress today?"
        player.c "Not unless you want to protect your modesty while you practice fucking me."
        wt_image neighbour_outfit_3_25
        nicole.c "You've already had sex with me."
        wt_image neighbour_outfit_3_13
        nicole.c "Don't you think I'm pretty good?"
        wt_image neighbour_outfit_3_33
        player.c "You could get better."
        nicole.c "Really?"
        wt_image neighbour_outfit_3_41
        nicole.c "You think I still need practice?"
        wt_image neighbour_outfit_3_39
        "She doesn't, actually ..."
        nicole.c "oohhh"
        wt_image neighbour_outfit_3_40
        "... but that doesn't stop you from giving her instructions anyway."
        nicole.c "ooohhhh"
        wt_image neighbour_outfit_3_4
        player.c "Slower"
        nicole.c "oohhh ... okay"
        wt_image neighbour_outfit_3_42
        player.c "Turn around"
        nicole.c "All right."
        wt_image neighbour_outfit_3_5
        player.c "Faster"
        nicole.c "ooohhhh"
        wt_image neighbour_outfit_3_43
        player.c "Wilder.  Ride me like a horny slut."
        nicole.c "oooohhhhh ... ooooohhhhhh"
        wt_image neighbour_outfit_3_44
        nicole.c "OOOHHHH!!"
        player.c "Don't stop.  Fuck my cock as you cum."
        wt_image neighbour_outfit_3_45
        player.c "[player.orgasm_text]"
        wt_image neighbour_outfit_3_46
        nicole.c "Is my fucking getting better?"
        player.c "A few more lessons and you'll be okay."
    $ nicole.sex_count += 1
    $ nicole.orgasm_count += 1
    call character_location_return(nicole) from _call_character_location_return_113
    orgasm notify
    wt_image living_room.image
    return

label nicole_practice_anal:
    $ nicole.training_session()
    rem tags 'available_today' from nicole
    if nicole.visit_outfit == 1:
        call forced_movement(boudoir) from _call_forced_movement_299
        summon nicole to boudoir
        wt_image neighbour_hypno_outfit_2_2
        player.c "I appreciate you taking the time to dress up for me."
        wt_image neighbour_shopping_1
        nicole.c "What, did you think I wore this just to impress you?"
        player.c "Who else would you want to impress before they fuck your ass?"
        if nicole.anal_count == 0:
            wt_image neighbour_hypno_outfit_2_3
            nicole.c "My ass?  Really??"
            player.c "It's a part of your training I've neglected for too long."
            wt_image neighbour_outfit_1_7
            if nicole.has_tag('natalie_used_dildo_before'):
                nicole.c "I've only tried it once, with Greg.  Not counting what Natalie did to me.  It was uncomfortable."
                player.c "What Natalie did wasn't uncomfortable, was it?"
                nicole.c "A little.  A lot actually."
                player.c "And yet you still came buckets while she was doing it.  You told me you wanted me to treat you like one of my clients.  If you think anal is uncomfortable, I think we've identified a weakness in your sexual repertoire, don't you agree?"
            else:
                nicole.c "I've only tried it once, with Greg.  It was uncomfortable."
                player.c "You told me that on your first visit.  You also told me you wanted me to treat you like one of my clients and teach you what you should be doing.  I think we've identified a weakness in your sexual repertoire, don't you agree?"
            nicole.c "I guess so."
            wt_image neighbour_first_visit_7
            player.c "Then let's deal with that weakness.  Remove your clothes."
            wt_image neighbour_first_visit_21
            nicole.c "How do we do this?"
            player.c "That's adorable.  How do you think we do this?"
            wt_image neighbour_anal_18
            player.c "Good guess."
            if player.has_tag('dominant'):
                 "There's a submissive quality to the way Nicole offers her ass to you.  It's clear anal sex is something she's been waiting for you to 'make' her do."
                 "Your natural instinct is to stimulate her submissive feelings.  On the other hand, you could just get on with fucking her ass."
                 $ title = "What do you do?"
                 menu:
                    "Tell her to beg for it":
                        "You can't help yourself.  You like it when women humiliate themselves for you."
                        player.c "Before I put my cock in you, Nicole, you're going to ask me to fuck you in the ass.  In fact, you're going to beg me to fuck your ass."
                        wt_image neighbour_first_visit_17
                        "Your neighbor looks back at you, wide eyed."
                        nicole.c "Wh ... what??"
                        player.c "You heard me.  You as much as told me you wanted your ass fucked on your first visit.  It's possible the idea of having your ass fucked is the main reason you wanted me to train you in the first place."
                        nicole.c "No ... no, I just ..."
                        player.c "It's time to be honest, Nicole.  You want me to fuck your ass. You're longing to find out what it feels like to have your ass stretched around my cock."
                        player.c "Be honest, with me and with yourself.  Ask me for what you want, Nicole.  And since you haven't been honest up to now, don't just ask.  Beg.  Beg me for what you want, Nicole."
                        wt_image neighbour_anal_4
                        "Nicole's voice quivers as she speaks, so softly that you can barely hear her.  What you hear, though, is music to your ears."
                        nicole.c "Please ... please fuck me ... I'm begging you."
                        "You could leave it there, but that's not in your nature.  Besides, Nicole's as close to sub space as she's ever likely been before."
                        "Why not give her a taste of what its likely to be in submissive bliss?  It'll be a memory she can jill off to later, should she ever masturbate to submissive thoughts."
                        player.c "What are you begging me for, Nicole?  Say it clearly."
                        wt_image neighbour_first_visit_18
                        "Nicole lowers her head and closes her eyes when she replies.  She's still very quiet, but the quiver is almost gone."
                        nicole.c "I'm begging you to fuck my ass.  I want you to fuck my ass, please.  I want to feel your cock inside my ass."
                        player.c "Good girl, Nicole.  Of course, I'd be happy to."
                        add tags 'begged_for_anal' to nicole
                        $ nicole.beg_count += 1
                    "Just fuck her ass":
                        pass
            wt_image neighbour_anal_9
            "You lube up your cock and position it at Nicole's bottom.  Her only reaction is a soft moan as you apply gentle but steady pressure against her rear hole."
            nicole.c "ooooo"
            wt_image neighbour_anal_10
            "It takes patience and a second application of lube, but eventually her sphincter widens enough to allow the head of your cock to pass through."
            nicole.c "OH"
            player.c "Does that feel good?"
            wt_image neighbour_anal_4
            if nicole.has_tag('begged_for_anal'):
                nicole.c "Yeessss"
                player.c "Should I fuck your ass hard now, girl?"
                nicole.c "Yes.  Please.  Please fuck my ass hard."
                wt_image neighbour_anal_1
                "You thrust in and out of her tight ass.  It only takes a few strokes to bring your neighbor to the first anal orgasm of her life."
                nicole.c "OOHH!!"
                $ nicole.orgasm_count += 1
            else:
                nicole.c "nnnnn ... I ... I'm not sure what it feels like."
                wt_image neighbour_anal_1
                "There's no question about how it feels for you.  It feels great as you thrust in and out of her tight ass."
            wt_image neighbour_anal_11
            player.c "[player.orgasm_text]"
            nicole.c "Oh, wow!!!"
        elif nicole.anal_count == 1:
            wt_image neighbour_hypno_outfit_2_3
            nicole.c "My ass?  We've already done that."
            wt_image neighbour_first_visit_7
            player.c "That hardly makes you an expert."
            nicole.c "You want me to be an expert at ... anal?"
            wt_image neighbour_anal_18
            player.c "You were going to say 'ass fucking', weren't you?"
            "She nods."
            if nicole.has_tag('begged_for_anal'):
                wt_image neighbour_first_visit_17
                player.c "You'd like to be an expert ass fucker, wouldn't you Nicole?"
                nicole.c "What??  No ... I mean, I don't know ..."
                player.c "You do know, and I want you to tell me."
                nicole.c "I ... I can't ... You don't expect me to ..."
                player.c "Say it.  I'm not putting my dick in your ass until you say it."
                wt_image neighbour_anal_4
                "You could almost cum listening to the sexy quiver in Nicole's voice as she closes her eyes and admits what she wants."
                nicole.c "I want you to make me an expert ass fucker.  Please train me to pleasure you with my ass.  Please teach me how to be good at anal.  Please, I'm begging you."
                wt_image neighbour_anal_10
                "She's far from that stage, yet.  Her ass is still so tight, it takes a lot of lube and a lot of patience to get even the head of your cock fully inside her."
                nicole.c "OH!"
                wt_image neighbour_anal_1
                "Once you finally do, you slowly and carefully fuck her ass, giving it a chance to adjust properly to having your girth inside it, an experience she seems to enjoy ..."
                nicole.c "oohhhh"
                wt_image neighbour_anal_20
                "... before releasing your load inside her butt, an experience that takes her over the edge with you as she experience her first anal orgasm."
                player.c "[player.orgasm_text]"
                nicole.c "OOHHH!!"
                $ nicole.beg_count += 1
                $ nicole.orgasm_count += 1
            else:
                wt_image neighbour_anal_9
                player.c "Would you like to be an expert ass fucker, Nicole?"
                nicole.c "ooooo ... no ... I mean, I don't know ..."
                wt_image neighbour_anal_10
                "She's far from that stage, yet.  Her ass is still so tight, it takes a lot of lube and a lot of patience to get even the head of your cock fully inside her."
                nicole.c "OH!"
                wt_image neighbour_anal_1
                "Once you finally do, you slowly and carefully fuck her ass, giving it a chance to adjust properly to having your girth inside it ..."
                nicole.c "ooooo"
                wt_image neighbour_anal_19
                "... before giving her a chance to experience your seed shooting inside it."
                player.c "[player.orgasm_text]"
                nicole.c "mmmmm"
        elif nicole.anal_count < 4:
            wt_image neighbour_hypno_outfit_2_3
            nicole.c "My ass?  Again?"
            wt_image neighbour_first_visit_7
            player.c "You're not an expert ass fucker yet, are you?"
            wt_image neighbour_anal_18
            nicole.c "I guess not."
            player.c "So I still need to train you, don't I?"
            if nicole.has_tag('begged_for_anal'):
                wt_image neighbour_anal_4
                nicole.c "Yes. Please train me to pleasure you with my ass. I want to be a good ass fucker. Please, teach me how."
                wt_image neighbour_anal_10
                "She's not there, yet, but it doesn't take as long for her sphincter to relax as it did last time.  With a lot of lube, patience, and constant pressure, you get your cock inside her as she moans."
                nicole.c "oohhh"
                wt_image neighbour_anal_1
                "After that, you start stroking your cock in and out of her, giving her ass a chance to adjust before you pick up the speed ..."
                nicole.c "oohhhh"
                wt_image neighbour_anal_20
                "... and empty your load inside her butt, an experience that takes her over the edge with you."
                player.c "[player.orgasm_text]"
                nicole.c "OOHHH!!"
                $ nicole.beg_count += 1
                $ nicole.orgasm_count += 1
            else:
                wt_image neighbour_anal_9
                nicole.c "Yes, it seems so."
                "Her tight butt still clenches up as the head of your cock pokes against it ..."
                wt_image neighbour_anal_10
                "... but it doesn't take as long for her sphincter to relax as it did last time.  With a lot of lube, patience, and constant pressure, you get your cock inside her as she moans."
                nicole.c "oooo"
                wt_image neighbour_anal_1
                "After that, you start stroking your cock in and out of her, giving her ass a chance to adjust before you pick up the speed ..."
                nicole.c "ooooo"
                wt_image neighbour_anal_19
                "... and empty your load inside her butt."
                player.c "[player.orgasm_text]"
                nicole.c "mmmmm"
        else:
            wt_image neighbour_first_visit_5
            nicole.c "Is that the only way I can impress you?  With my clothes?"
            player.c "What else did you have in mind?"
            wt_image neighbour_first_visit_16
            nicole.c "I was hoping to impress you with how well I take your cock up my ass."
            wt_image neighbour_first_visit_24
            if nicole.has_tag('begged_for_anal'):
                nicole.c "Or do you need me to beg, so you know how much I want it?  Please put your cock in my ass and fuck me.  I want you to teach me to pleasure you with my ass."
                wt_image neighbour_anal_9
                "It hardly counts as begging when she says it like that, but it's fun to listen to her dirty talk anyway.  It's even more fun to feel her ass open up when you press your cock head against it."
            else:
                player.c "No protests today?"
                nicole.c "None.  I'm actually looking forward to it."
                player.c "You want my cock in your ass?"
                nicole.c "I actually do, yes.  Please put your big, hard cock in my ass and fuck me."
                wt_image neighbour_anal_9
                "It's fun listening to her dirty talk. It's even more fun to feel her ass open up when you press your cock head against it."
            wt_image neighbour_anal_10
            "Her ass is still super tight, but she's much better now at letting her sphincter relax.  With a bit of lube and some pressure, your cock head pops through, a sexy sensation for both of you ..."
            nicole.c "oohhh"
            wt_image neighbour_anal_1
            "... a sensation that gets even better as you fuck her."
            nicole.c "oohhhh"
            wt_image neighbour_anal_20
            player.c "[player.orgasm_text]"
            nicole.c "OOHHH!!"
            $ nicole.orgasm_count += 1
        call forced_movement(living_room) from _call_forced_movement_300
        wt_image neighbour_outfit_1_4
        nicole.c "I'm glad not all your training leaves my ass this sore."
        player.c "Sore in a bad way?"
        nicole.c "I didn't say that."
    elif nicole.visit_outfit == 2:
        wt_image neighbour_outfit_2_11
        player.c "Wearing your sexy undies today, I see."
        nicole.c "They're comfortable."
        wt_image neighbour_outfit_2_13
        nicole.c "Plus my ass doesn't look that bad in them, does it?"
        player.c "I'd say your ass looks good enough to fuck."
        if nicole.anal_count == 0:
             wt_image neighbour_outfit_2_11
             nicole.c "That's a figure of speech, right?  You don't really plan to fuck my ass?"
             player.c "It's a part of your training I've neglected for too long."
             wt_image neighbour_outfit_2_12
             nicole.c "I've only tried it once, with Greg.  It was uncomfortable."
             player.c "You told me that on your first visit. You also told me you wanted me to treat you like one of my clients and teach you what you should be doing."
             player.c "I think we've identified a weakness in your sexual repertoire, don't you agree?"
             nicole.c "I guess so."
             player.c "So let's deal with that weakness."
             nicole.c "Okay, I guess.  How do we do this?"
             wt_image neighbour_outfit_2_15
             player.c "Lie on your back and lift your legs."
             if player.has_tag('dominant'):
                 "There's a submissive quality to the way Nicole accepts that you're going to take her ass. It's clear anal sex is something she's been waiting for you to 'make' her do."
                 "Your natural instinct is to stimulate her submissive feelings. On the other hand, you could just get on with fucking her ass."
                 $ title = "What do you do?"
                 menu:
                    "Tell her to beg for it":
                        wt_image neighbour_outfit_2_32
                        "You can't help yourself. You like it when women humiliate themselves for you. You position yourself over her, your cockhead pressing against her rosebud, then stop."
                        player.c "Before I put my cock in you, Nicole, you're going to ask me to fuck you in the ass. In fact, you're going to beg me to fuck your ass."
                        wt_image neighbour_outfit_2_30
                        "Your neighbor looks up at you, wide eyed."
                        nicole.c "Wh ... what??"
                        player.c "You heard me. You as much as told me you wanted your ass fucked on your first visit. It's possible the idea of having your ass fucked is the main reason you wanted me to train you in the first place."
                        nicole.c "No ... no, I just ..."
                        player.c "It's time to be honest, Nicole. You want me to fuck your ass. You're longing to find out what it feels like to have your ass stretched around my cock."
                        player.c "Be honest, with me and with yourself. Ask me for what you want, Nicole. And since you haven't been honest up to now, don't just ask. Beg. Beg me for what you want, Nicole."
                        "Nicole's voice quivers as she speaks, so softly that you can barely hear her. What you hear, though, is music to your ears."
                        nicole.c "Please ... please fuck me ... I'm begging you."
                        "You could leave it there, but that's not in your nature. Besides, Nicole's as close to sub space as she's ever likely been before."
                        "Why not give her a taste of what its likely to be in submissive bliss? It'll be a memory she can jill off to later, should she ever masturbate to submissive thoughts."
                        player.c "What are you begging me for, Nicole?  Say it clearly."
                        wt_image neighbour_outfit_2_31
                        "Nicole half closes her eyes when she replies.  She's still very quiet, but the quiver is almost gone."
                        nicole.c "I'm begging you to fuck my ass. I want you to fuck my ass, please. I want to feel your cock inside my ass."
                        player.c "Good girl, Nicole.  Of course, I'd be happy to."
                        add tags 'begged_for_anal' to nicole
                        $ nicole.beg_count += 1
                    "Just fuck her ass":
                        pass
             wt_image neighbour_outfit_2_5
             "You lube up your cock and position it at Nicole's bottom. Her only reaction is a soft moan as you apply gentle but steady pressure against her rear hole."
             nicole.c "ooooo"
             wt_image neighbour_outfit_2_33
             "It takes patience and a second application of lube, but eventually her sphincter widens enough to allow the head of your cock to pass through."
             nicole.c "OH"
             player.c "Does that feel good?"
             if nicole.has_tag('begged_for_anal'):
                 wt_image neighbour_outfit_2_31
                 nicole.c "Yeessss"
                 player.c "Should I fuck your ass hard now, girl?"
                 nicole.c "Yes.  Please.  Please fuck my ass hard."
                 wt_image neighbour_outfit_2_35
                 "You thrust in and out of her tight ass ..."
                 wt_image neighbour_outfit_2_36
                 "... as Nicole reaches a hand down and starts playing with her clit."
                 wt_image neighbour_outfit_2_37
                 "It only takes a few strokes of your cock, combined with the frantic rubbing of her fingers, to bring your neighbor to the first orgasm of her life."
                 nicole.c "OOHH!!"
                 $ nicole.orgasm_count += 1
                 wt_image neighbour_outfit_2_38
             else:
                 nicole.c "nnnnn ... I ... I'm not sure what it feels like."
                 wt_image neighbour_outfit_2_35
                 "There's no question about how it feels for you.  It feels great as you thrust in and out of her tight ass."
                 wt_image neighbour_outfit_2_34
             player.c "[player.orgasm_text]"
             nicole.c "Oh, wow!!!"
        elif nicole.anal_count == 1:
             wt_image neighbour_outfit_2_11
             nicole.c "My ass?  We've already done that."
             player.c "That hardly makes you an expert."
             wt_image neighbour_outfit_2_12
             nicole.c "You want me to be an expert at ... anal?"
             wt_image neighbour_outfit_2_15
             player.c "You were going to say 'ass fucking', weren't you?"
             "She nods."
             if nicole.has_tag('begged_for_anal'):
                 wt_image neighbour_outfit_2_32
                 player.c "You'd like to be an expert ass fucker, wouldn't you Nicole?"
                 nicole.c "What??  No ... I mean, I don't know ..."
                 player.c "You do know, and I want you to tell me."
                 wt_image neighbour_outfit_2_30
                 nicole.c "I ... I can't ... You don't expect me to ..."
                 player.c "Say it.  I'm not putting my dick in your ass until you say it."
                 wt_image neighbour_outfit_2_31
                 "You could almost cum listening to the sexy quiver in Nicole's voice as she half closes her eyes and admits what she wants."
                 nicole.c "I want you to make me an expert ass fucker. Please train me to pleasure you with my ass. Please teach me how to be good at anal. Please, I'm begging you."
                 wt_image neighbour_outfit_2_5
                 "She's far from that stage, yet.  Her ass is still so tight, it takes a lot of lube and a lot of patience ..."
                 wt_image neighbour_outfit_2_33
                 "... before you can even fit the head of your cock fully inside her."
                 nicole.c "OH!"
                 wt_image neighbour_outfit_2_35
                 "Once you finally do, you slowly and carefully fuck her ass, giving it a chance to adjust properly to having your girth inside it ..."
                 wt_image neighbour_outfit_2_36
                 "... an experience she seems to enjoy as she reaches a hand between her legs to start playing with herself ..."
                 nicole.c "oohhhh"
                 wt_image neighbour_outfit_2_37
                 "... the combination of your cock in her ass and her fingers on her clit bringing her to her first anal orgasm ..."
                 nicole.c "OOHHH!!"
                 wt_image neighbour_outfit_2_38
                 "... just a moment before you shoot your seed into her butt."
                 player.c "[player.orgasm_text]"
                 $ nicole.beg_count += 1
                 $ nicole.orgasm_count += 1
             else:
                 wt_image neighbour_outfit_2_32
                 player.c "Would you like to be an expert ass fucker, Nicole?"
                 wt_image neighbour_outfit_2_30
                 nicole.c "ooooo ... no ... I mean, I don't know ..."
                 wt_image neighbour_outfit_2_5
                 "She's far from that stage, yet.  Her ass is still so tight, it takes a lot of lube and a lot of patience ..."
                 wt_image neighbour_outfit_2_33
                 "... before you can even fit the head of your cock fully inside her."
                 nicole.c "OH!"
                 wt_image neighbour_outfit_2_35
                 "Once you finally do, you slowly and carefully fuck her ass, giving it a chance to adjust properly to having your girth inside it ..."
                 nicole.c "ooooo"
                 wt_image neighbour_outfit_2_34
                 "... before giving her a chance to experience your seed shooting inside it."
                 player.c "[player.orgasm_text]"
                 nicole.c "mmmmm"
        elif nicole.anal_count < 4:
             wt_image neighbour_outfit_2_11
             nicole.c "My ass?  Again?"
             wt_image neighbour_outfit_2_15
             player.c "You're not an expert ass fucker yet, are you?"
             nicole.c "I guess not."
             wt_image neighbour_outfit_2_32
             player.c "So I still need to train you, don't I?"
             if nicole.has_tag('begged_for_anal'):
                 wt_image neighbour_outfit_2_31
                 nicole.c "Yes. Please train me to pleasure you with my ass. I want to be a good ass fucker. Please, teach me how."
                 wt_image neighbour_outfit_2_5
                 "She's not there, yet, but it doesn't take as long for her sphincter to relax as it did last time. With a lot of lube, patience, and constant pressure ..."
                 wt_image neighbour_outfit_2_33
                 "... you get your cock inside her as she moans."
                 nicole.c "oohhh"
                 wt_image neighbour_outfit_2_35
                 "After that, you start stroking your cock in and out of her, giving her ass a chance to adjust ..."
                 wt_image neighbour_outfit_2_36
                 "... while she plays with herself ..."
                 nicole.c "oohhhh"
                 wt_image neighbour_outfit_2_37
                 "... bringing herself to climax ..."
                 nicole.c "OOHHH!!"
                 wt_image neighbour_outfit_2_38
                 "... just before you empty your load inside her butt."
                 player.c "[player.orgasm_text]"
                 $ nicole.beg_count += 1
                 $ nicole.orgasm_count += 1
             else:
                 wt_image neighbour_outfit_2_30
                 nicole.c "Yes, it seems so."
                 wt_image neighbour_outfit_2_5
                 "Her tight butt still clenches up as the head of your cock pokes against it ..."
                 wt_image neighbour_outfit_2_33
                 "... but it doesn't take as long for her sphincter to relax as it did last time.  With a lot of lube, patience, and constant pressure, you get your cock inside her as she moans."
                 nicole.c "oooo"
                 wt_image neighbour_outfit_2_35
                 "After that, you start stroking your cock in and out of her, giving her ass a chance to adjust before you pick up the speed ..."
                 nicole.c "ooooo"
                 wt_image neighbour_outfit_2_34
                 "... and empty your load inside her butt."
                 player.c "[player.orgasm_text]"
                 nicole.c "mmmmm"
        else:
             wt_image neighbour_outfit_2_1
             nicole.c "Then I suppose I'd better let you fuck it."
             if nicole.has_tag('begged_for_anal'):
                 wt_image neighbour_outfit_2_24
                 nicole.c "Or do you need me to beg, so you know how much I want it? Please put your cock in my ass and fuck me. I want you to teach me to pleasure you with my ass."
                 "It hardly counts as begging when she says it like that, but it's fun to listen to her dirty talk anyway."
             else:
                 player.c "No protests today?"
                 nicole.c "None.  I'm actually looking forward to it."
                 player.c "You want my cock in your ass?"
                 wt_image neighbour_outfit_2_24
                 nicole.c "I actually do, yes.  Please put your big, hard cock in my ass and fuck me."
                 "It's fun listening to her dirty talk."
             wt_image neighbour_outfit_2_5
             "It's even more fun to feel her ass open up when you press your cock head against it."
             wt_image neighbour_outfit_2_33
             "Her ass is still super tight, but she's much better now at letting her sphincter relax. With a bit of lube and some pressure, your cock head pops through, a sexy sensation not just for you, but for her too ..."
             nicole.c "oohhh"
             wt_image neighbour_outfit_2_39
             "... as demonstrated by her hand that reaches between her legs and rubs herself as you penetrate her."
             nicole.c "oohhhh"
             wt_image neighbour_outfit_2_6
             "She keeps rubbing herself as you fuck her, slowly at first ..."
             nicole.c "ooohhhhh"
             wt_image neighbour_outfit_2_40
             "... then faster and faster as her ass continues to stretch."
             nicole.c "oooohhhhh"
             wt_image neighbour_outfit_2_37
             "Between the feeling of your cock stretching her open and her own fingers working furiously at hr clit, she cums first ..."
             nicole.c "OOHHH!!"
             wt_image neighbour_outfit_2_38
             "... but not by much."
             player.c "[player.orgasm_text]"
             nicole.c "OOHHH!!"
             $ nicole.orgasm_count += 1
        wt_image neighbour_outfit_2_13
        nicole.c "It's nice to know you find my ass sexy, even when I'm wearing boring underwear."
        call forced_movement(living_room) from _call_forced_movement_301
    else:
        wt_image neighbour_outfit_3_1
        player.c "That underwear is sexier than the pair you wore on your last visit. Are you trying to turn me on?"
        wt_image neighbour_outfit_3_2
        nicole.c "That depends. What happens if I turn you on?"
        player.c "I bend you over that chair and fuck your ass."
        if nicole.anal_count == 0:
             wt_image neighbour_outfit_3_23
             nicole.c "My ass?  Really??"
             player.c "It's a part of your training I've neglected for too long."
             wt_image neighbour_outfit_3_24
             nicole.c "I've only tried it once, with Greg.  It was uncomfortable."
             player.c "You told me that on your first visit. You also told me you wanted me to treat you like one of my clients and teach you what you should be doing."
             player.c "I think we've identified a weakness in your sexual repertoire, don't you agree?"
             nicole.c "I guess so."
             wt_image neighbour_outfit_3_25
             player.c "Then let's deal with that weakness.  Remove your clothes."
             wt_image neighbour_anal_21
             if player.has_tag('dominant'):
                 "There's a submissive quality to the way Nicole offers her ass to you. It's clear anal sex is something she's been waiting for you to 'make' her do."
                 "Your natural instinct is to stimulate her submissive feelings. On the other hand, you could just get on with fucking her ass."
                 $ title = "What do you do?"
                 menu:
                    "Tell her to beg for it":
                        "You can't help yourself.  You like it when women humiliate themselves for you."
                        player.c "Before I put my cock in you, Nicole, you're going to ask me to fuck you in the ass. In fact, you're going to beg me to fuck your ass."
                        nicole.c "Wh ... what??"
                        player.c "You heard me. You as much as told me you wanted your ass fucked on your first visit. It's possible the idea of having your ass fucked is the main reason you wanted me to train you in the first place."
                        nicole.c "No ... no, I just ..."
                        player.c "It's time to be honest, Nicole. You want me to fuck your ass. You're longing to find out what it feels like to have your ass stretched around my cock."
                        player.c "Be honest, with me and with yourself. Ask me for what you want, Nicole. And since you haven't been honest up to now, don't just ask. Beg. Beg me for what you want, Nicole."
                        wt_image neighbour_anal_22
                        "Nicole's voice quivers as she speaks, so softly that you can barely hear her. What you hear, though, is music to your ears."
                        nicole.c "Please ... please fuck me ... I'm begging you."
                        "You could leave it there, but that's not in your nature. Besides, Nicole's as close to sub space as she's ever likely been before."
                        "Why not give her a taste of what its likely to be in submissive bliss? It'll be a memory she can jill off to later, should she ever masturbate to submissive thoughts."
                        player.c "What are you begging me for, Nicole?  Say it clearly."
                        wt_image neighbour_anal_23
                        "Nicole lowers her head as she replies.  She's still very quiet, but the quiver is almost gone."
                        nicole.c "I'm begging you to fuck my ass. I want you to fuck my ass, please. I want to feel your cock inside my ass."
                        player.c "Good girl, Nicole.  Of course, I'd be happy to."
                        add tags 'begged_for_anal' to nicole
                        $ nicole.beg_count += 1
                    "Just fuck her ass":
                        pass
             wt_image neighbour_anal_17
             "You lube up your cock and position it at Nicole's bottom. Her only reaction is a soft moan as you apply gentle but steady pressure against her rear hole."
             nicole.c "ooooo"
             wt_image neighbour_anal_24
             "It takes patience and a second application of lube, but eventually her sphincter widens enough to allow the head of your cock to pass through."
             nicole.c "OH"
             player.c "Does that feel good?"
             if nicole.has_tag('begged_for_anal'):
                 nicole.c "Yeessss"
                 player.c "Should I fuck your ass hard now, girl?"
                 nicole.c "Yes.  Please.  Please fuck my ass hard."
                 wt_image neighbour_anal_5
                 "You thrust in and out of her tight ass. It only takes a few strokes to bring your neighbor to the first anal orgasm of her life."
                 nicole.c "OOHH!!"
                 $ nicole.orgasm_count += 1
             else:
                 nicole.c "nnnnn ... I ... I'm not sure what it feels like."
                 wt_image neighbour_anal_16
                 "There's no question about how it feels for you.  It feels great as you thrust in and out of her tight ass."
             wt_image neighbour_anal_6
             player.c "[player.orgasm_text]"
             nicole.c "Oh, wow!!!"
        elif nicole.anal_count == 1:
             wt_image neighbour_outfit_3_23
             nicole.c "My ass?  We've already done that."
             player.c "That hardly makes you an expert."
             wt_image neighbour_outfit_3_24
             nicole.c "You want me to be an expert at ... anal?"
             wt_image neighbour_outfit_3_25
             player.c "You were going to say 'ass fucking', weren't you?"
             "She nods."
             wt_image neighbour_anal_21
             if nicole.has_tag('begged_for_anal'):
                 player.c "You'd like to be an expert ass fucker, wouldn't you Nicole?"
                 nicole.c "What??  No ... I mean, I don't know ..."
                 player.c "You do know, and I want you to tell me."
                 wt_image neighbour_anal_22
                 nicole.c "I ... I can't ... You don't expect me to ..."
                 player.c "Say it.  I'm not putting my dick in your ass until you say it."
                 wt_image neighbour_anal_23
                 "You could almost cum listening to the sexy quiver in Nicole's voice as she closes her eyes and admits what she wants."
                 nicole.c "I want you to make me an expert ass fucker. Please train me to pleasure you with my ass. Please teach me how to be good at anal.  Please, I'm begging you."
                 wt_image neighbour_anal_17
                 "She's far from that stage, yet. Her ass is still so tight, it takes a lot of lube and a lot of patience ..."
                 wt_image neighbour_anal_24
                 "... but eventually you get the head of your cock fully inside her."
                 nicole.c "OH!"
                 wt_image neighbour_anal_16
                 "Once you finally do, you slowly and carefully fuck her ass, giving it a chance to adjust properly to having your girth inside it, an experience she seems to enjoy ..."
                 nicole.c "oohhhh"
                 wt_image neighbour_anal_6
                 "... before releasing your load inside her butt, an experience that takes her over the edge with you as he experiences her first anal orgasm."
                 player.c "[player.orgasm_text]"
                 nicole.c "OOHHH!!"
                 $ nicole.beg_count += 1
                 $ nicole.orgasm_count += 1
             else:
                 player.c "Would you like to be an expert ass fucker, Nicole?"
                 nicole.c "What?  No ... I mean, I don't know ..."
                 wt_image neighbour_anal_17
                 "She's far from that stage, yet. Her ass is still so tight, it takes a lot of lube and a lot of patience ..."
                 wt_image neighbour_anal_24
                 "... but eventually you get the head of your cock fully inside her."
                 nicole.c "OH!"
                 wt_image neighbour_anal_16
                 "Once you finally do, you slowly and carefully fuck her ass, giving it a chance to adjust properly to having your girth inside it ..."
                 nicole.c "ooooo"
                 wt_image neighbour_anal_6
                 "... before giving her a chance to experience your seed shooting inside it."
                 player.c "[player.orgasm_text]"
                 nicole.c "mmmmm"
        elif nicole.anal_count < 4:
             wt_image neighbour_outfit_3_24
             nicole.c "My ass?  Again?"
             player.c "You're not an expert ass fucker yet, are you?"
             wt_image neighbour_outfit_3_25
             nicole.c "I guess not."
             player.c "So I still need to train you, don't I?"
             if nicole.has_tag('begged_for_anal'):
                 wt_image neighbour_anal_23
                 nicole.c "Yes. Please train me to pleasure you with my ass. I want to be a good ass fucker. Please, teach me how."
                 wt_image neighbour_anal_17
                 "She's not there, yet, but it doesn't take as long for her sphincter to relax as it did last time."
                 wt_image neighbour_anal_24
                 "With a lot of lube, patience, and constant pressure, you get your cock inside her as she moans."
                 nicole.c "oohhh"
                 wt_image neighbour_anal_16
                 "After that, you start stroking your cock in and out of her, giving her ass a chance to adjust before you pick up the speed ..."
                 nicole.c "oohhhh"
                 wt_image neighbour_anal_6
                 "... and empty your load inside her butt, an experience that takes her over the edge with you."
                 player.c "[player.orgasm_text]"
                 nicole.c "OOHHH!!"
                 $ nicole.beg_count += 1
                 $ nicole.orgasm_count += 1
             else:
                 wt_image neighbour_anal_21
                 nicole.c "Yes, it seems so."
                 wt_image neighbour_anal_17
                 "Her tight butt still clenches up as the head of your cock pokes against it, but it doesn't take as long for her sphincter to relax as it did last time."
                 wt_image neighbour_anal_24
                 "With a lot of lube, patience, and constant pressure, you get your cock inside her as she moans."
                 nicole.c "oooo"
                 wt_image neighbour_anal_16
                 "After that, you start stroking your cock in and out of her, giving her ass a chance to adjust before you pick up the speed ..."
                 nicole.c "ooooo"
                 wt_image neighbour_anal_6
                 "... and empty your load inside her butt."
                 player.c "[player.orgasm_text]"
                 nicole.c "mmmmm"
        else:
             wt_image neighbour_outfit_3_8
             nicole.c "Really?  In that case, does seeing me wiggling my butt in these panties turn you on?"
             wt_image neighbour_outfit_3_47
             nicole.c "Or do I have to take my underwear off ..."
             wt_image neighbour_anal_22
             if nicole.has_tag('begged_for_anal'):
                 nicole.c "... and beg, so you know how much I want it? Please put your cock in my ass and fuck me. I want you to teach me to pleasure you with my ass."
                 "It hardly counts as begging when she says it like that, but it's fun to listen to her dirty talk anyway."
             else:
                 nicole.c "... and wiggle my naked butt at you?"
                 player.c "No protests today?"
                 nicole.c "None.  I'm actually looking forward to it."
                 player.c "You want my cock in your ass?"
                 nicole.c "I actually do, yes. Please put your big, hard cock in my ass and fuck me."
                 "It's fun listening to her dirty talk."
             wt_image neighbour_anal_17
             "It's even more fun to feel her ass open up when you press your cock head against it."
             wt_image neighbour_anal_24
             "Her ass is still super tight, but she's much better now at letting her sphincter relax. With a bit of lube and some pressure, your cock head pops through, a sexy sensation for both of you."
             nicole.c "oohhh"
             wt_image neighbour_anal_25
             "Your dick is moving freely enough in and out of her ass now that you turn her around ..."
             wt_image neighbour_anal_26
             "... and let her ride your cock ..."
             wt_image neighbour_anal_27
             "... until first you climax ..."
             player.c "[player.orgasm_text]"
             wt_image neighbour_outfit_4_6
             "... and then she does."
             nicole.c "OOHHH!!"
             $ nicole.orgasm_count += 1
        wt_image neighbour_outfit_3_47
        nicole.c "So that's what happens when I turn you on.  Good to know."
    $ nicole.anal_count += 1
    call character_location_return(nicole) from _call_character_location_return_114
    orgasm notify
    wt_image living_room.image
    return

label nicole_practice_submission:
    if boudoir.has_item(fluffy_cuffs):
        $ nicole.training_session()
        rem tags 'available_today' from nicole
        if nicole.submission_count == 0:
            wt_image neighbour_cuffs_1
            nicole.c "What are we doing today?"
            player.c "Something different."
            nicole.c "What sort of different?"
            player.c "Take off your clothes and have a seat and I'll show you."
            if not living_room.is_here:
                call forced_movement(living_room) from _call_forced_movement_302
                summon nicole
            wt_image neighbour_cuffs_2
            nicole.c "Okay, I'm naked but you're still dressed.  What now?"
            player.c "I'll go get your surprise."
            "You bring out the pink handcuffs from the bedroom."
            wt_image neighbour_cuffs_3
            nicole.c "What are those?"
            player.c "Love cuffs"
            nicole.c "Love cuffs?  For what?"
            player.c "For you.  Put them on."
            wt_image neighbour_cuffs_4
            nicole.c "What happens after I put them on?"
            player.c "You do whatever I tell you to."
            wt_image neighbour_cuffs_5
            nicole.c "Is this how you deal with recalcitrant clients?"
            player.c "It's part of the process.  Once those are fastened, turn around."
            wt_image neighbour_cuffs_6
            nicole.c "What are you doing?"
            player.c "Showing you how I deal with clients who don't listen to me."
            "You bring your hand down hard on her ass ... *smack*"
            wt_image neighbour_cuffs_7
            nicole.c "Ouch!  Hey!!  I listen to you."
            player.c "Let's make sure you keep doing so. I can't have a disobedient teaching aide. Turn around."
            nicole.c "But I already obey you!"
            player.c "Then why haven't you turned around yet?"
            wt_image neighbour_cuffs_8
            "She turns back into position and you resume spanking her ... *smack* ... *smack* ... *smack* ... as she whimpers in protest."
            nicole.c "ouch ... ouch ... ouch! ... that stings!!"
            wt_image neighbour_cuffs_9
            "It isn't a hard spanking, but when you uncuff her, she lies down and rubs her butt in overly dramatic fashion."
            nicole.c "I didn't like that."
            player.c "When you told me you wanted me to train you like one of my clients, did you think I would only ask you to do things you enjoyed?"
            wt_image neighbour_cuffs_10
            nicole.c "Maybe? I guess not. But you don't have to spank me to train me."
            player.c "I train. You learn. Understood?"
            wt_image neighbour_cuffs_3
            nicole.c "Yeah, yeah.  Okay."
            $ player.submission_action_count += 1
            $ nicole.submission_count = 1
            $ nicole.spank_count += 1
            change player energy by -energy_short
        elif nicole.submission_count == 1:
            wt_image neighbour_spank_1
            player.c "Take off your clothes."
            nicole.c "Gee, you're in a romantic mood today."
            if not living_room.is_here:
                call forced_movement(living_room) from _call_forced_movement_303
                summon nicole
            wt_image neighbour_spank_2
            nicole.c "Okay, I'm naked and waiting. You're still dressed?"
            player.c "Turn around."
            wt_image neighbour_spank_3
            nicole.c "Aren't you going to warm me up first?"
            player.c "I'm about to warm you up. Your bottom, anyway."
            "You rub the palm of your hand across her butt cheek, then bring it down with a hard *smack*"
            wt_image neighbour_spank_4
            nicole.c "Ouch!  Hey!!  Not this again."
            player.c "No, this time I want you to take the spanking without your hands being bound."
            wt_image neighbour_spank_5
            nicole.c "Hang on.  When did we agree that you could spank me?"
            player.c "When you told me you wanted me to treat you like any of my other clients and train you to please me."
            nicole.c "Spanking me pleases you?  Why??"
            $ title = "Why do you want to spank her?"
            menu:
                "It's part of training her to be your submissive":
                    player.c "It shows me that you accept my authority over you. That you're willing to be subservient to me, and accept things you don't enjoy in order to please me."
                    nicole.c "Why would you want that?  We both know there are things I'm happy to do that would please you."
                    player.c "I enjoy it when you allow me to do what I want with you. If I only do things that you want to do, you haven't demonstrated true submission, and that's what I want from you."
                    nicole.c "You want to train me to be submissive to you?"
                    player.c "Yes"
                    wt_image neighbour_spank_6
                    nicole.c "Is it going to hurt a lot?"
                    player.c "I'll send you home to Greg in one piece."
                    $ nicole.temporary_count = 1
                "I find it fun":
                    player.c "It turns me on to spank you. I enjoy how it feels to have your ass under my hand. I enjoy listening to your yelps, and watching you twitch in discomfort."
                    nicole.c "It excites you to hurt me?  Is that part of how you want to train me to please you?"
                    player.c "Yes"
                    wt_image neighbour_spank_6
                    nicole.c "Not too much pain, okay.  If it hurts a lot, I'm stopping this."
                    player.c "I'll send you home to Greg in one piece."
                    $ nicole.temporary_count = 1
                    add tags 'spanking_only' to nicole
                "It's the only way I can be sure you'll do what I tell you":
                    player.c "It's the only way I can be sure you'll listen to my instructions."
                    nicole.c "That's crap. I'll listen. I've been listening. I'll continue to listen to what you teach me. But no spanking, understood?"
                    "She's serious, and a bit miffed.  You let her go home.  Best to wait for another visit before continuing her training."
                    $ nicole.temporary_count = 0
                    add tags 'no_spanking' to nicole
                    $ nicole.submission_count = 0
            if nicole.temporary_count == 1:
                wt_image neighbour_spank_7
                "As she moves into position, you bring your hand down on her ass ... *SMACK*"
                nicole.c "Ouch!  That was harder than before."
                player.c "The last time was love taps to get you used to the concept. Today's going to be a proper spanking. Remove your hand."
                wt_image neighbour_spank_8
                "You begin a steady, rhythmic tattooing of her butt ... *smack* ... *smack* ... *smack* ... moving back and forth from cheek to cheek and changing the angle of impact as she whimpers."
                nicole.c "ouch ... ouch ... oooo ... ouch!  .... OW!  .... oooo .... oh ouch!"
                wt_image neighbour_spank_9
                "Eventually, the heat in her ass cheeks becomes too much, and she reaches a hand back to defend herself."
                player.c "Remove your hand."
                nicole.c "It's really hurting now."
                player.c "That's just the blood rushing to the surface. Your skin's a bit tender but you're ready for some harder blows now, ones that you'll feel in the muscles."
                nicole.c "I'm not sure ..."
                player.c "Remove your hand, Nicole."
                wt_image neighbour_spank_8
                "The next set of blows are spaced further apart, and are intended to bruise, not sting ... *SMACK* ... ... *SMACK* ... ... *SMACK*"
                nicole.c "OW!   OWW!!!   Oohhh OWWW!!!"
                wt_image neighbour_spank_10
                nicole.c "Holy shit!  Greg is going to wonder what you're doing with me."
                player.c "Better not show him your bruise collection. He may be inclined to add to it."
                nicole.c "I don't think so."
                "She giggles, and you wonder if she's wishing that maybe he would."
                nicole.c "So, ummm ... if that turned you on, should I be doing something for you?"
                $ title = "What do you want?"
                menu:
                    "Blow job":
                        wt_image neighbour_hypno_outfit_1_6
                        "She's right. The spanking did turn you on. So does watching her sink to her knees to take your cock in her mouth."
                        wt_image neighbour_bj_1
                        "It's a simple but sweetly submissive blow job, as she finishes her spanking by taking your load in her mouth."
                        wt_image neighbour_bj_2
                        player.c "[player.orgasm_text]"
                        $ nicole.blowjob_count += 1
                        $ nicole.swallow_count += 1
                        orgasm
                    "Send her home":
                        player.c "I enjoyed that just fine as it was.  You can go home now."
                        nicole.c "You're an interesting guy. I've never known a man who was more interested in spanking me than in getting off."
                        change player energy by -energy_short
                wt_image neighbour_spank_1
                nicole.c "When do I come back, after the bruises heal?"
                player.c "When I tell you to come back, of course."
                "She giggles as she leaves."
                $ nicole.spank_count += 1
                $ nicole.temporary_count = 0
                $ nicole.submission_count = 2
                $ player.submission_action_count += 1
        elif nicole.has_tag('spanking_only'):
            wt_image neighbour_spank_1
            player.c "How are your bruises?"
            nicole.c "They've healed."
            player.c "Let me see."
            if not living_room.is_here:
                call forced_movement(living_room) from _call_forced_movement_304
                summon nicole
            wt_image neighbour_spank_3
            nicole.c "I'm a fast healer."
            player.c "That's good. I'm going to put them back."
            wt_image neighbour_spank_2
            nicole.c "Can't I convince you to do something else you'd enjoy?"
            player.c "Not today.  Turn around."
            wt_image neighbour_spank_6
            nicole.c "Awwww ... why do you have to be a sadist?"
            player.c "Why do you have to have a firm and perfectly spankable bum?"
            wt_image neighbour_spank_7
            nicole.c "So you're saying this is my bum's fault?"
            player.c "Don't worry, I'm about to punish it for you."
            wt_image neighbour_spank_8
            "She takes the spanking fairly well ... *smack* ... *smack* ... *smack* ..."
            nicole.c "ouch ... ouch ... oooo ... ouch!  .... OW!  .... oooo .... oh ouch!"
            wt_image neighbour_spank_9
            "... only a couple of times reaching back instinctively with her hand to give her butt some protection ..."
            player.c "Remove your hand, Nicole."
            nicole.c "But it hurts!"
            player.c "It's supposed to.  Remove your hand."
            wt_image neighbour_spank_8
            "... which only succeeds in bringing out more of your sadist, causing you to intensify the spanking ... *SMACK* ... ... *SMACK* ... ... *SMACK*"
            nicole.c "OW!   OWW!!!   Oohhh OWWW!!!"
            wt_image neighbour_spank_10
            nicole.c "I'm bruised again. I suppose that means you're turned on again? Do you want me to ... you know?"
            $ title = "What do you want?"
            menu:
                "Blow job":
                    wt_image neighbour_hypno_outfit_1_6
                    "She's right. The spanking did turn you on. So does watching her sink to her knees to take your cock in her mouth."
                    wt_image neighbour_bj_1
                    "It's a simple but sweetly submissive blow job, as she finishes her spanking by taking your load in her mouth."
                    wt_image neighbour_bj_2
                    player.c "[player.orgasm_text]"
                    $ nicole.blowjob_count += 1
                    $ nicole.swallow_count += 1
                    orgasm
                "Send her home":
                    player.c "I enjoyed that just fine as it was.  You can go home now."
                    nicole.c "You're an interesting guy. I've never known a man who was more interested in spanking me than in getting off."
                    change player energy by -energy_short
            wt_image neighbour_spank_1
            nicole.c "You know, black looks okay on me, but blue isn't really my color."
            player.c "I think your butt looks just fine in black and blue."
            "She giggles as she leaves."
            $ nicole.spank_count += 1
        elif nicole.submission_count == 2:
            wt_image neighbour_spank_1
            player.c "It's time for your next lesson in submission, Nicole. Remove your clothes."
            if not living_room.is_here:
                call forced_movement(living_room) from _call_forced_movement_305
                summon nicole
            wt_image neighbour_hypno_outfit_1_10
            nicole.c "Is this going to hurt as much as the last lesson?"
            player.c "No.  Kneel down."
            wt_image neighbour_kneel_2
            nicole.c "Good, because my ass has only finally healed up from that spanking. What are you going to do?"
            player.c "Put your head down, then raise your ass."
            wt_image neighbour_kneel_3
            nicole.c "Okay, now what?"
            player.c "Now you wait."
            wt_image living_room.image
            "You leave her and go on with your day."
            wt_image neighbour_kneel_4
            "From time to time you check back on her and she looks at you expectingly. Eventually, she breaks the silence."
            nicole.c "When are we going to do something?"
            player.c "You are doing something. You're waiting."
            nicole.c "Why?"
            player.c "Because that's what I want from you. Do so quietly from now on."
            wt_image living_room.image
            "You go back to keeping busy while ignoring her."
            wt_image neighbour_kneel_4
            "When you return to her, she's clearly not happy, but holds her tongue until you speak to her."
            player.c "How do you feel?"
            nicole.c "Stupid"
            player.c "Why? I wanted you to do something for me, and you did it. Why is that stupid?"
            nicole.c "I've just been kneeling here waiting for you. It makes me feel more like your pet than your lover."
            player.c "You told me you wanted me to train you in how to please me. I told you that included you being subservient to me. Are you subservient to me?"
            nicole.c "I want to say no, but I've just spent the last hour kneeling naked with my ass up waiting for you while you ignore me. So I guess I'm being pretty damn subservient."
            player.c 'Why would you want to say "no"?'
            nicole.c "Because it's not ... I don't know."
            player.c "Not what? Not what women are supposed to do?"
            nicole.c "Exactly"
            player.c "You're a bright woman, Nicole. You're liberated enough to admit to your husband that you wanted to have sex with me, and you're confident enough to let him sleep with other women without worrying about losing him."
            player.c "I train women for a living. Part of the reason you're attracted to me is that the idea of being trained turned you on, didn't it?"
            nicole.c "Yes, but kneeling here while you ignored me ... it was humiliating."
            player.c "It was submissive. It was subservient. Are you worried that makes you seem weak in my eyes?"
            "She nods."
            player.c "It doesn't. You could have got up and walked out of here at any time and denied what you really want. That would have made you seem weak to me. This is what you want."
            nicole.c "I'm not sure it is."
            player.c "You're fighting this, Nicole. Put your hands between your legs. Both of them. Make yourself cum while I watch."
            nicole.c "What?  I can't ..."
            player.c "Do it."
            wt_image neighbour_kneel_5
            nicole.c "oohhh ... OOHHH!!"
            wt_image neighbour_kneel_6
            player.c "You don't normally come that quick when you masturbate, do you Nicole?"
            nicole.c "Masturbation isn't something I do a lot.  Even before I was married I never ..."
            player.c "Answer the question, Nicole."
            nicole.c "No, I don't normally cum that quick when masturbating. Being told to do so while you watched really got me off."
            player.c "Especially after spending an hour with your ass in the air wondering if I was ever going to touch you."
            nicole.c "Especially after that."
            wt_image neighbour_kneel_7
            nicole.c "The only thing is, I don't want to be subservient to you all the time, okay?"
            player.c "You'll be subservient to me when I tell you to, understood?  Head down when you answer."
            wt_image neighbour_kneel_8
            nicole.c "Okay"
            player.c "Not like that. Tell me exactly what you're going to be."
            nicole.c "I'll be subservient to you whenever you tell me to do."
            $ title = "What now?"
            menu:
                "Have her suck your cock":
                    player.c "Good girl. You've earned the opportunity to suck my cock."
                    wt_image neighbour_hypno_outfit_1_6
                    "She kneels down to take your cock in her mouth."
                    player.c "No hands today."
                    wt_image neighbour_hypno_outfit_1_17
                    player.c "Good girl.  Show me how much you enjoy doing what I tell you to do."
                    wt_image neighbour_bj_1
                    "Quite a bit it seems ..."
                    wt_image neighbour_bj_2
                    "... and she also seems to enjoy the reward you give her for a job a well done."
                    player.c "[player.orgasm_text]"
                    $ nicole.blowjob_count += 1
                    $ nicole.swallow_count += 1
                    orgasm
                "Send her home":
                    player.c "Good girl. Go home to your husband. I'll let you know the next time I want you."
                    "She hurries home, embarrassed at her behavior and more than a little wet between her legs despite her recent orgasm."
                    change player energy by -energy_short
            $ player.submission_action_count += 1
            $ nicole.submission_count = 3
            $ nicole.masturbation_count += 1
            $ nicole.orgasm_count += 1
        else:
            wt_image neighbour_spank_1
            player.c "You look nice."
            nicole.c "Thank you!"
            player.c "You'll look nicer with your top off."
            if not living_room.is_here:
                call forced_movement(living_room) from _call_forced_movement_306
                summon nicole
            wt_image neighbour_kneel_7
            nicole.c "Like this?"
            player.c "Not quite.  You'll look even nicer with your head bowed."
            wt_image neighbour_kneel_8
            player.c "That's better."
            $ title = "What do you want from her?"
            menu:
                "Spank her":
                    wt_image neighbour_spank_6
                    player.c "Turn around."
                    wt_image neighbour_spank_8
                    "She tries to stay quiet during the spanking, but can only hold out so long ... *smack* ... *smack* ... *smack* ..."
                    nicole.c "oooo ... ouch!  .... OW!"
                    wt_image neighbour_spank_9
                    "... and though she tries hard not to, eventually her hand reaches back to give her butt some protection ..."
                    player.c "Remove your hand."
                    "She hesitates."
                    player.c "Now"
                    wt_image neighbour_spank_8
                    "It's a only a small act of defiance, but it's enough to justify, i both her mind and yours, increasing the intensity the spanking ... *SMACK* ... ... *SMACK* ... ... *SMACK*"
                    nicole.c "OW!   OWW!!!   Oohhh OWWW!!!"
                    wt_image neighbour_hypno_outfit_1_10
                    "Trying hard not to rub her sore ass, she looks at you, to see if anything more is required of her."
                    $ title = "What do you want?"
                    menu:
                        "Blow job":
                            wt_image neighbour_hypno_outfit_1_11
                            "She sinks to her knees and opens her mouth to accept your cock, wrapping her lips tightly around your dick as you insert it."
                            wt_image neighbour_bj_1
                            "It's a slow and submissive blow job, exactly what she knew you would be in the mood for after hurting her."
                            wt_image neighbour_bj_2
                            player.c "[player.orgasm_text]"
                            $ nicole.blowjob_count += 1
                            $ nicole.swallow_count += 1
                            orgasm
                        "Send her home":
                            player.c "Go home now."
                            nicole.c "Thank you."
                            "You're not sure whether the 'thank you' is for the spanking or for stopping the spanking. She may not be sure either."
                            change player energy by -energy_short
                    $ nicole.spank_count += 1
                "Have her kneel":
                    player.c "On your knees."
                    wt_image neighbour_spank_6
                    nicole.c "Are you going to ..."
                    player.c "No talking."
                    wt_image neighbour_kneel_4
                    "She waits, quietly, as you go about your business."
                    wt_image neighbour_kneel_3
                    "She smiles when you approach to check on her, thinking you're ready to make use of her ..."
                    wt_image neighbour_kneel_4
                    "... and if she's disappointed when you continue on to do other things, she doesn't say so."
                    "Eventually, she's been there long enough, and it's time to decide what to do with her."
                    $ title = "What do you do with her?"
                    menu:
                        "Use her mouth":
                            player.c "Turn around and open your mouth."
                            wt_image neighbour_first_visit_24
                            "She smiles as she scrambles around ..."
                            wt_image neighbour_bj_12
                            "... to take your cock between her lips."
                            wt_image neighbour_bj_14
                            if nicole.blowjob_practice < 2:
                                "Waiting has made her eager, and she attacks your dick enthusiastically."
                            else:
                                "Waiting has made her eager, but you've trained her to take her time.  She tries to control herself and take it slow."
                            wt_image neighbour_bj_13
                            "Watching her wait has made you pretty eager, too, and you're soon ready to cum."
                            if nicole.facial_count > 0:
                                $ title = "Where do you want to cum?"
                                menu:
                                    "In her mouth":
                                        wt_image neighbour_bj_12
                                        player.c "[player.orgasm_text]"
                                        wt_image neighbour_bj_15
                                        "She swallows your load and the licks your cock clean, just the way a subservient woman would be expected to behave."
                                        $ nicole.swallow_count += 1
                                    "On her face":
                                        wt_image neighbour_bj_16
                                        player.c "Put your face in front of my cock."
                                        wt_image neighbour_bj_17
                                        player.c "[player.orgasm_text]"
                                        wt_image neighbour_bj_18
                                        "She waits for permission to clean herself up, just as a subservient woman should do."
                                        $ nicole.facial_count += 1
                            else:
                                wt_image neighbour_bj_12
                                player.c "[player.orgasm_text]"
                                wt_image neighbour_bj_15
                                "She swallows your load and the licks your cock clean, just the way a subservient woman would be expected to behave."
                                $ nicole.swallow_count += 1
                            $ nicole.blowjob_count += 1
                            orgasm
                        "Fuck her":
                            player.c "Turn around. I'm going to fuck you."
                            wt_image neighbour_first_visit_24
                            "She beams happily as she scrambles around."
                            wt_image neighbour_sex_2
                            "If you needed proof that she finds being made to wait hot, she provides it ..."
                            nicole.c "ooohhhhh"
                            wt_image neighbour_sex_13
                            "... by cumming almost as soon as you penetrate her."
                            nicole.c "OOHHH!!"
                            wt_image neighbour_sex_14
                            "You didn't mind watching her wait yourself, but fucking her eager pussy afterwards, is even better."
                            $ title = "Where do you want to cum?"
                            menu:
                                "In her":
                                    wt_image neighbour_shower_16
                                "On her":
                                    wt_image neighbour_sex_5
                            player.c "[player.orgasm_text]"
                            wt_image neighbour_sex_16
                            nicole.c "That was worth waiting for.  Should I be going now?"
                            wt_image neighbour_sex_17
                            player.c "Not yet.  Lie there with your legs spread for the next half hour.  I want to watch my cum drip out of you before you go home."
                            orgasm
                            $ nicole.sex_count += 1
                            $ nicole.orgasm_count += 1
                        "Fuck her ass" if nicole.anal_count > 2:
                            wt_image neighbour_kneel_2
                            player.c "Offer me your ass."
                            nicole.c "ooooo"
                            wt_image neighbour_anal_7
                            if nicole.has_tag('begged_for_anal'):
                                nicole.c "Please fuck my ass.  Please put your hard dick up my butt and fuck me.  Please!"
                                $ nicole.beg_count += 1
                                wt_image neighbour_anal_28
                                "She begins rubbing her clit as you position your cockhead against her rear opening.  If you needed proof that being made to wait makes her hot, you get it in the orgasm that wracks her as you push your way inside."
                                nicole.c "OOHHH!!"
                                $ nicole.orgasm_count += 1
                            else:
                                "She spreads her butt cheeks and tries to control the little wiggle of anticipation in her hips."
                                if nicole.anal_count > 4:
                                    wt_image neighbour_anal_28
                                    "She begins rubbing her clit as you position your cockhead against her rear opening.  If you needed proof that being made to wait makes her hot, you get it in the orgasm that wracks her as you push your way inside."
                                    nicole.c "OOHHH!!"
                                    $ nicole.orgasm_count += 1
                            wt_image neighbour_anal_13
                            "She groans as you get your dick fully inside her ..."
                            nicole.c "ooooo"
                            wt_image neighbour_anal_14
                            "... the friction between her tight ass and your hard cock is creating an intense sensation for both of you ..."
                            wt_image neighbour_anal_29
                            "... that soon takes you over the edge."
                            player.c "[player.orgasm_text]"
                            wt_image neighbour_anal_30
                            "She holds that position as your balls pump their load into her, content to be a receptacle for your semen until you're finished with her."
                            orgasm
                            $ nicole.anal_count += 1
                        "Tell her to pleasure herself":
                            player.c "Are you horny, girl?"
                            nicole.c "What?"
                            player.c "You heard me. Has kneeling there waiting for me left you horny?"
                            nicole.c "I ... that's not ..."
                            player.c "Not something a strong independent woman should get wet about?"
                            "She blushes."
                            player.c "Finger fuck yourself."
                            wt_image neighbour_kneel_5
                            nicole.c "ooohhhh ... OOHHH!!"
                            wt_image neighbour_kneel_6
                            player.c "Do you have something you want to say before you go?"
                            nicole.c "Waiting on my knees for you made me horny.  I have no idea why, but thank you.  I enjoyed that."
                            $ nicole.masturbation_count += 1
                            $ nicole.orgasm_count += 1
                            change player energy by -energy_very_short
                        "Send her home":
                            player.c "Go home now."
                            nicole.c "Didn't you want to ..."
                            player.c "Watch you kneel there for another hour?  Not today.  Maybe next time."
                            change player energy by -energy_very_short
                "Make a spectacle of her" if not nicole.spectacle_yet:
                    wt_image neighbour_show_1
                    player.c "Have a seat on the counter."
                    wt_image neighbour_show_2
                    player.c "Not like that.  Spread your legs."
                    wt_image neighbour_show_3
                    player.c "Now put your cunt to use."
                    nicole.c "How?"
                    player.c "Put something in it."
                    wt_image neighbour_show_4
                    player.c "Good"
                    wt_image neighbour_show_5
                    nicole.c "Now what?"
                    player.c "Now you stay there and look pretty like a good little ornament."
                    wt_image neighbour_show_4
                    "She's not sure what to make of being put on display like this, but she stays in position, finger in her sex, as you go about your business."
                    wt_image neighbour_show_6
                    "Eventually you take a closer look at her."
                    player.c "How do you feel?"
                    nicole.c "Stupid"
                    player.c "Why?  Because I'm objectifying you?"
                    nicole.c "Yes.  I feel like a piece of furniture."
                    player.c "Give yourself some credit.  You're more art than furniture.  Spread your pussy lips."
                    wt_image neighbour_show_7
                    player.c "Wet art, but I'd rather see you wetter.  Finger fuck yourself."
                    wt_image neighbour_masturbate_1
                    "She reinserts her finger and starts moving it back and forth.  The smell of her arousal rises quickly."
                    player.c "That should be enough.  Show me your cunt again."
                    wt_image neighbour_show_8
                    player.c "That's a good object.  Nice and wet.  You can put your finger back in."
                    wt_image neighbour_show_9
                    nicole.c "You want me to just stay like this?"
                    player.c "Why not? Artwork doesn't need to cum, does it? Strong independent women certainly don't need to cum while they're being objectified."
                    if nicole.beg_count > 0:
                        $ nicole.beg_count += 1
                        nicole.c "I ... I'd like to. Can I cum, please?"
                        player.c "Not 'I'. You're being objectified, remember?  If you're going to beg, beg effectively."
                        nicole.c "Can this artwork please cum? It's surprisingly horny and would really, really like to go back to finger fucking itself."
                        $ title = "Let her cum?"
                        menu:
                            "Go ahead":
                                player.c "Okay, artwork. Put on a show."
                                wt_image neighbour_masturbate_2
                                "It's a quick show, and an intense one."
                                nicole.c "OOHHH!!"
                                wt_image neighbour_show_9
                                player.c "Can my ornament go back to looking pretty now and stop being such a needy decoration?"
                                "She blushes and resumes her position, staying there until you're ready to send her home."
                                $ nicole.masturbation_count += 1
                                $ nicole.orgasm_count += 1
                            "Not today":
                                player.c "Not today.  I want my decorations to be horny today."
                                wt_image neighbour_show_6
                                nicole.c "That's mean."
                                player.c "Not to Greg. Think how happy he'll be when he sees how horny you are when you get home. I wonder what he'll make you do before he lets you cum?"
                                wt_image neighbour_show_9
                                "Probably nothing, but the whirlwind of emotions playing across Nicole's face make you think that on some level, she'd love it if her husband made her earn the right to cum."
                    else:
                        "She's at a loss as to how to respond."
                        $ title = "What do you do?"
                        menu:
                            "Tell her to beg":
                                $ nicole.beg_count += 1
                                wt_image neighbour_show_6
                                player.c "Of course if I'm wrong, and my artwork does want to cum, it could tell me that and maybe convince me I'm wrong."
                                nicole.c "I ... I'd like to cum."
                                player.c "That's not very convincing."
                                nicole.c "I really want to cum.  Please?"
                                player.c "What you're doing right now is called begging, Nicole, and it works best when you admit that you're begging.  One more time, and say it like you mean it."
                                nicole.c "Please?  Please, I want to cum. Please let me cum. I ... I'm begging you."
                                player.c "A bit better. Go on artwork. Put on a show."
                                wt_image neighbour_masturbate_2
                                "It's a quick show, and an intense one."
                                nicole.c "OOHHH!!"
                                wt_image neighbour_show_9
                                player.c "Can my ornament go back to looking pretty now and stop being such a needy decoration?"
                                "She blushes and resumes her position, staying there until you're ready to send her home."
                                $ nicole.masturbation_count += 1
                                $ nicole.orgasm_count += 1
                            "Leave her like this":
                                "It's fun watching the conflicting emotions crossing her face. She's sexually frustrated and she's not sure why. She just knows you're not going to do anything about it, and she both hates and is turned on by that."
                                wt_image neighbour_show_3
                                "Eventually, it's time for her to go."
                                player.c "Try not to tackle Greg as soon as you walk in the door."
                                "She says nothing, as you're pretty sure that's exactly what she's going to do."
                    $ nicole.spectacle_yet = True
                    $ player.submission_action_count += 1
                    change player energy by -energy_very_short
                "Turn her into artwork again" if nicole.spectacle_yet:
                    wt_image neighbour_show_1
                    player.c "Have a seat on the counter."
                    nicole.c "You want me up here again?"
                    wt_image neighbour_show_2
                    player.c "Show me what a pretty piece of artwork you can be."
                    wt_image neighbour_show_3
                    player.c "Not bad, but less generic nude, more attention grabber."
                    wt_image neighbour_show_5
                    player.c "There you go.  Now you're sprucing up the look of my house."
                    wt_image neighbour_show_4
                    "You leave her there, paying her no more attention than you would a painting or sculpture you've seen a hundred times before."
                    wt_image neighbour_show_6
                    "When you finally take the time to pay closer attention to her, you can smell her arousal."
                    player.c "Show me."
                    wt_image neighbour_show_7
                    player.c "Most of my artwork doesn't get so aroused just sitting around."
                    "She blushes, but says nothing."
                    $ title = "What now?"
                    menu:
                        "Tell her to get wetter":
                            player.c "Masturbate"
                            wt_image neighbour_masturbate_1
                            "She reinserts her finger and starts moving it back and forth. The smell of her arousal rises quickly."
                            player.c "That's enough. Show me your cunt again."
                            wt_image neighbour_show_8
                            player.c "That's a good object. Nice and wet. You can put your finger back in."
                            wt_image neighbour_show_9
                            if nicole.beg_count > 0:
                                $ nicole.beg_count += 1
                                nicole.c "Please?"
                                player.c "Please what?"
                                nicole.c "Please, can we do something? I'd like to cum."
                                player.c "What could we do that you would cum from?"
                                nicole.c "Almost anything. Please, I'm really horny right now. I'm begging you, please, I really want to cum."
                                $ title = "What should she do?"
                                menu:
                                    "Finger herself":
                                        player.c "Okay, artwork. Since you're so eager to put on a show for me, go ahead and frig yourself."
                                        wt_image neighbour_masturbate_2
                                        "It's a quick show, and an intense one."
                                        nicole.c "OOHHH!!"
                                        wt_image neighbour_show_9
                                        player.c "Can my ornament go back to looking pretty now and stop being such a needy decoration?"
                                        "She blushes and resumes her position, staying there until you're ready to send her home."
                                        $ nicole.masturbation_count += 1
                                        $ nicole.orgasm_count += 1
                                    "Blow you":
                                        player.c "Can you come from blowing me. No touching yourself, just my cock in your mouth."
                                        nicole.c "I'm not sure, but I'll try."
                                        wt_image neighbour_bj_1
                                        "She sinks to her knees and takes your cock in her mouth."
                                        wt_image neighbour_bj_2
                                        "She twitches as she blows you, her hips rolling and writhing, and you can tell she's trying to create some pressure on her clit ..."
                                        wt_image neighbour_hypno_outfit_1_7
                                        "... but it's not enough, and she rolls her eyes in frustration as you cum."
                                        player.c "[player.orgasm_text]"
                                        wt_image neighbour_bj_7
                                        player.c "Did you cum?"
                                        nicole.c "No.  Can I ..."
                                        player.c "Go home and wait for Greg, and find out if he'll let you cum? Sure. No touching yourself until he says you can."
                                        nicole.c "But ..."
                                        "Whatever she was going to say, she thinks better of it.  Meekly she gets dressed and heads home."
                                        $ nicole.blowjob_count += 1
                                        $ nicole.swallow_count += 1
                                        orgasm
                                    "Just stay like that":
                                        player.c "Not today. I want my decoration to be horny today."
                                        wt_image neighbour_show_6
                                        nicole.c "Nnnnn.  That's not nice."
                                        player.c "I like seeing you horny. Greg may, too. I wonder what he'll make you do before he lets you cum?"
                                        wt_image neighbour_show_9
                                        "Probably nothing, but the whirlwind of emotions playing across Nicole's face make you think that on some level, she'd love it if her husband made her earn the right to cum."
                                        change player energy by -energy_very_short
                            else:
                                "She stays like this until it's time to go, breathing hard and clearly frustrated, but uncertain about what to do about it."
                                wt_image neighbour_show_3
                                player.c "You can go now.  No playing with yourself when you get home. If you're horny, you need to wait and ask Greg for relief."
                                nicole.c "Are you serious?"
                                player.c "Yes"
                                change player energy by -energy_very_short
                        "Send her home":
                            wt_image neighbour_show_3
                            player.c "You can go now. No playing with yourself when you get home. If you're horny, you need to wait and ask Greg for relief."
                            nicole.c "Are you serious?"
                            player.c "Yes"
                            change player energy by -energy_very_short
        call character_location_return(nicole) from _call_character_location_return_115
        notify
        wt_image living_room.image
    else:
        "Nicole's not into BDSM or dungeons. To introduce her to submission, perhaps you should invest in something innocent looking but effective."
    return

## Showgirl Content

#label nicole_activate_dancing:
  ## replaced by standard club label _stage_notice
  #if nicole.has_tag('showgirl') and not nicole.dancing_at_club:
    #"This would be the perfect place for your neighbor Nicole to take her clothes off. You'll make arrangements when you get home."
    #$ nicole.dancing_at_club = True
    #call convert(nicole, 'showgirl')
    #rem tags 'waiting_for_club' from nicole
  #return

label nicole_watch_her_dance:
    $ nicole.training_session()
    rem tags 'available_today' from nicole
    $ nicole.dance_outfit += 1
    # scroll from 4 to 1
    if nicole.dance_outfit > 4:
        $ nicole.dance_outfit = 1
    if nicole.dance_outfit == 1:
        wt_image neighbour_strip_1_1
        "Nicole peeks out coyly from behind the curtains ..."
        wt_image neighbour_strip_1_11
        "... then walks out onto stage ..."
        wt_image neighbour_strip_1_2
        "... and gives the audience a big beaming smile."
        wt_image neighbour_strip_1_12
        "She begins to lose her clothes."
        wt_image neighbour_strip_1_3
        "First her bra ..."
        wt_image neighbour_strip_1_4
        "... then her panties ..."
        wt_image neighbour_strip_1_5
        "... as her audience watches with approval."
        wt_image neighbour_strip_1_6
        "Soon she's sitting nude on the stage."
        wt_image neighbour_strip_1_9
        "All pretext of being shy is dropped, as she rubs her nipples ..."
        wt_image neighbour_strip_1_10
        "... and then her clit ..."
        wt_image neighbour_strip_1_7
        "... before inserting a finger into herself ..."
        wt_image neighbour_strip_1_8
        "... and frigging herself to orgasm as the whole room watches."
        nicole.c "OOHHH!!!"
        wt_image neighbour_strip_1_13
        "She feigns shyness again as the audience claps, but the hint of smile playing across her lips belies how much she loves exposing herself in this way."
    elif nicole.dance_outfit == 2:
        wt_image neighbour_strip_2_7
        "Nicole come out on the stage in a pretty pink outfit ..."
        wt_image neighbour_strip_2_1
        "... that she perhaps doesn't like very much ..."
        wt_image neighbour_strip_2_4
        "... as she promptly gets rid of it."
        wt_image neighbour_strip_2_3
        "Nicole seems much happier with her clothes neatly laid aside."
        wt_image neighbour_strip_2_6
        "Of course, the shoes have to go."
        wt_image neighbour_strip_2_5
        "And the panties are an absolute 'no no'."
        wt_image neighbour_strip_2_9
        "Now she's in the state she wants to be in, and can show the audience something more interesting than her outfit."
        wt_image neighbour_strip_2_8
        "Something sufficiently interesting that Nicole herself can't keep her hands off of it."
        wt_image neighbour_strip_2_10
        "She feels compelled to rub it and rub it ..."
        wt_image neighbour_strip_2_11
        "... a process that has inevitable consequences."
        nicole.c "OOHHH!!!"
        wt_image neighbour_strip_2_13
        "Nicole seems genuinely overwhelmed by the ensuing applause.  She grins at the audience as if to say, 'They like me, they really like me!'"
    elif nicole.dance_outfit == 3:
        wt_image neighbour_strip_3_1
        "You catch Nicole just as she's about to start a private dance."
        wt_image neighbour_strip_3_2
        "Your neighbor is a very enthusiastic lapdancer."
        wt_image neighbour_strip_3_3
        "Her patron is pretty enthusiastic himself."
        wt_image neighbour_strip_3_4
        "Nicole tries to show him her body, but he's more interested in touching than looking."
        wt_image neighbour_strip_3_9
        "This level of contact with the entertainer would be frowned on in most establishments, but The Club allows as much contact as the showgirl is comfortable with."
        wt_image neighbour_strip_3_5
        "Which in Nicole's case is quite a lot ..."
        wt_image neighbour_strip_3_10
        "... as long as he's getting an up close look at her attributes as he touches her."
        wt_image neighbour_strip_3_6
        "He makes sure to let her know how much he appreciates the private showing ..."
        wt_image neighbour_strip_3_7
        "... and Nicole is quick to reciprocate the appreciation."
        wt_image neighbour_strip_3_8
        "Another successful show and another happy audience."
    else:
        wt_image neighbour_strip_4_1
        "Nicole's hair is done and she's classily dressed.  She looks like a Club Member, not one of the entertainers."
        wt_image neighbour_strip_4_2
        "She lifts her knees, revealing that under that classy dress ..."
        wt_image neighbour_strip_4_3
        "... are matching panties that are already soaked straight through."
        wt_image neighbour_strip_4_4
        "The dress isn't needed for the rest of her show, so off it comes."
        wt_image neighbour_strip_4_5
        "She gives the audience a sly look ..."
        wt_image neighbour_strip_4_6
        "... then retrieves a vibrator she has stashed in the sofa.  She gives it a lick ..."
        wt_image neighbour_strip_4_7
        "... and rubs the toy across her wet panties ..."
        wt_image neighbour_strip_4_8
        "... before finding a better place to stash it."
        wt_image neighbour_strip_4_9
        nicole.c "ooohhhh"
        "How many orgasms she has becomes a matter of some debate amongst onlookers ..."
        wt_image neighbour_strip_4_10
        "... as it's difficult to tell when one climax finishes and the next one begins."
        nicole.c "OOHHH ... OOHHH ... OOOHHHH ... OOHHH"
        wt_image neighbour_strip_4_10
        "When she's finally sated - or the batteries have worn out, it's hard to tell which - she happily receives the applause of her appreciative audience."
    add tags 'watched_today' to nicole
    change player energy by -energy_very_short notify
    wt_image stage.image
    return

## Slavegirl Content
label nicole_rename:
    wt_image nicole.image
    "As her owner, it's your prerogative to change [nicole.full_name]'s name, if you want to."
    $ title = "Do you want to change her name?"
    menu:
        "Yes":
            $ title = "What would you like her name to be?"
            $ nicole.name = renpy.input(_("What is her new name?"))
            $ nicole.suffix = renpy.input(_("What is her new title, if you want to give her one?"))
            $ title = "Does she get a prefix?"
            menu:
                "Yes":
                    $ nicole.prefix = renpy.input(_("What is her prefix?"))
                "No":
                    $ nicole.prefix = ""
            $ nicole.change_full_name(nicole.prefix, nicole.name, nicole.suffix)
            $ title = "Are you sure you want her new name to be [nicole.full_name]?"
            menu:
                "Yes":
                    pass
                "No, choose something else":
                    $ nicole.change_full_name("", "Nicole", "the Neighbor")
                    jump nicole_rename
        "No":
            pass
    return

# Tell her how to address you
label nicole_your_name:
    "[nicole.name] currently refers to you as '[nicole.your_name]'"
    $ title = "Change how she should address you?"
    menu:
        "Yes":
            $ title = "How should she address you?"
            $ nicole.your_name = renpy.input(_("What does she call you?"))
        "No":
            pass
    return

label nicole_slavegirl_entertain:
    #$ nicole.training_session() ## don;t think any these should count as daily activities
    wt_image nicole.image
    player.c "Entertain me, [nicole.name]"
    nicole.c "Yes, [nicole.your_name].  What would you like me to do?"
    $ title = "How do you want her to entertain you?"
    menu:
        "Bark like a dog":
            player.c "Bark like a dog."
            $ nicole.temporary_count = 1
            while nicole.temporary_count == 1:
                wt_image neighbour_slavegirl_1
                nicole.c "Rrufff!!  Ruff Ruff Ruff!  Rrrrufff!!!  Ruff Ruff Ruff Ruff Ruff Ruff!"
                $ title = "Keep listening?"
                menu:
                    "Listen to her bark":
                        pass
                    "That's enough":
                        $ nicole.temporary_count = 0
        "Beg for something" if nicole.beg_count > 0:
            if nicole.begged_slave:
                player.c "Beg for me again."
                wt_image neighbour_slavegirl_1
                nicole.c "Please do whatever you want with your property, [nicole.your_name]. Please, [nicole.your_name], I want you to do whatever you want to do with me."
            else:
                player.c "I've always enjoyed listening to you beg.  Beg for me."
                wt_image neighbour_slavegirl_1
                nicole.c "What would property beg for, [nicole.your_name]?"
                player.c "Beg me to give you something you want. Better yet, beg me to give you something you don't want."
                nicole.c  "I'm sorry, [nicole.your_name]. I don't understand. I only want what you want me to want. If you give me something, it'll be something I want."
                player.c 'Just say "please" and then tell me something you want me to do to you.'
                nicole.c "Please do whatever you want with your property, [nicole.your_name]. Please, [nicole.your_name], I want you to do whatever you want to do with me."
                $ nicole.begged_slave = True
            $ nicole.beg_count += 1
        "Be artwork" if nicole.spectacle_yet and not nicole.has_tag('artwork_now'):
            add tags 'artwork_now' to nicole
            player.c "I'd like some art on my wall.  You should look nice there."
            wt_image neighbour_slavegirl_9
            nicole.c "Thank you, [nicole.your_name]."
            wt_image neighbour_slavegirl_4
            player.c "You don't mind being used as a decorative ornament for the remainder of the day, do you?"
            wt_image neighbour_slavegirl_8
            nicole.c "Of course not, [nicole.your_name].  This possession is happy you want to decorate your house with it."
            $ nicole.change_image('neighbour_slavegirl_8')
        "Get back on the floor" if nicole.has_tag('artwork_now'):
            rem tags 'artwork_now' from nicole
            player.c "I'm tired of that view. Get back into your normal position."
            wt_image neighbour_slavegirl_4
            nicole.c "Yes, [nicole.your_name]."
            wt_image neighbour_slavegirl
            "If she's disappointed that you don't want her as your decoration any longer, the feeling is fleeting.  She quickly rediscovers the joy of being back on the floor, looking up at you."
            $ nicole.change_image('neighbour_slavegirl')
        "Dance":
            player.c "Dance for me."
            if not nicole.has_tag('artwork_now'):
                nicole.c "Yes, [nicole.your_name]."
                wt_image neighbour_slavegirl_11
                "She starts wiggling to imaginary music."
                wt_image neighbour_slavegirl_6
                "With no clothes to remove, she instead wiggles her way to the floor ..."
                wt_image neighbour_slavegirl_7
                "... and 'dances' on her knees, shaking her butt as she gyrates."
                wt_image neighbour_slavegirl_12
                "She keeps moving, wiggling rhythmically back and forth in front of you, for as long as you watch.  And the closer you watch her, the happier she seems."
            else:
                wt_image neighbour_slavegirl_2
                nicole.c "Yes, [nicole.your_name]."
                wt_image neighbour_slavegirl_5
                "She gives her best attempt at a seductive dance ..."
                wt_image neighbour_slavegirl_10
                "... wiggling to imaginary music ..."
                wt_image neighbour_slavegirl_4
                "... as she removes her already-see-through outfit."
                wt_image neighbour_slavegirl_3
                "She seems happy to have your attention."
                wt_image neighbour_slavegirl_6
                "Presumably even property likes to be appreciated.  She keeps dancing, wiggling back and forth in front of you, until you eventually tire of the show."
            change player energy by -energy_very_short notify
    return

label nicole_slavegirl_blowjob:
    $ nicole.training_session()
    wt_image nicole.image
    player.c "Mouth"
    if nicole.has_tag('artwork_now'):
        wt_image neighbour_hypno_outfit_1_6
        nicole.c "Yes, [nicole.your_name]."
        wt_image neighbour_hypno_outfit_1_17
        "[nicole.name] lets you use her mouth like you'd use any other of your toys. Fast, slow, rough, gentle. Whatever you're in the mood for."
        $ title = "Where are you in the mood to cum?"
        menu:
            "In her mouth":
                wt_image neighbour_hypno_outfit_1_11
                $ nicole.swallow_count += 1
            "On her face":
                wt_image neighbour_bj_6
                $ nicole.facial_count += 1
    else:
        wt_image neighbour_slavegirl_5
        nicole.c "Yes, [nicole.your_name]."
        wt_image neighbour_slavegirl_bj_3
        "[nicole.name] lets you use her mouth like you'd use any other of your toys. Fast, slow, rough, gentle. Whatever you're in the mood for."
        $ title = "Where are you in the mood to cum?"
        menu:
            "In her mouth":
                wt_image neighbour_slavegirl_bj_2
                $ nicole.swallow_count += 1
            "On her face":
                wt_image neighbour_slavegirl_bj_4
                $ nicole.facial_count += 1
    player.c "[player.orgasm_text]"
    $ nicole.blowjob_count += 1
    orgasm notify
    return

label nicole_slavegirl_sex:
    $ nicole.training_session()
    wt_image nicole.image
    player.c "On the bed."
    if not nicole.has_tag('artwork_now'):
        wt_image neighbour_slavegirl_5
    nicole.c "Yes, [nicole.your_name]."
    $ nicole.slave_sex_outfit += 1
    if nicole.slave_sex_outfit > 2:
        $ nicole.slave_sex_outfit = 1
    if nicole.slave_sex_outfit == 1:
        wt_image neighbour_slavegirl_sex_2
        "[nicole.name] loves it when you take her missionary style."
        nicole.c "ooohhhh"
        wt_image neighbour_slavegirl_sex_4
        "You expect it reminds her of prior days, when she was a married woman with a loving husband.  Does property find it kinky to imagine being married?"
        wt_image neighbour_slavegirl_sex_1
        "If so, maybe it's the kinkiness of giving her owner an orgasm the same way she used to give them to her husband that gets her off as soon as she's looked after you."
        player.c "[player.orgasm_text]"
        nicole.c "OOHHH!!"
    else:
        wt_image neighbour_slavegirl_sex_5
        "[nicole.name] used to be of service to her husband like this, before she became property."
        wt_image neighbour_slavegirl_sex_3
        "Perhaps it's memories of those strange days that trigger the orgasm that washes over her, after she's looked after your needs."
        player.c "[player.orgasm_text]"
        nicole.c "OOHHH!!"
    $ nicole.sex_count += 1
    $ nicole.orgasm_count += 1
    orgasm notify
    return

label nicole_slavegirl_anal:
    $ nicole.training_session()
    wt_image nicole.image
    player.c "Ass"
    if nicole.has_tag('artwork_now'):
        wt_image neighbour_slavegirl_11
        "Eagerly she spins around to give you access."
        player.c "Not standing up.  Get on the bed where you can do more of the work."
    else:
        wt_image neighbour_slavegirl_7
        "Eagerly she spins around to give you access."
        player.c "Not here.  The hard floor's for your knees, not mine. Get up on the bed."
    wt_image neighbour_slavegirl_6
    nicole.c "Yes, [nicole.your_name]."
    $ nicole.slave_anal_outfit += 1
    if nicole.slave_anal_outfit > 3:
        $ nicole.slave_anal_outfit = 1
    if nicole.slave_anal_outfit == 1:
        wt_image neighbour_slavegirl_anal_1
        "[nicole.name]'s ass seems to enjoy her new life more than any other part of her."
        nicole.c "oohhh"
        wt_image neighbour_slavegirl_anal_10
        "Being used this way makes her feel so much like property, she starts trembling almost uncontrollably as you fuck her butt."
        nicole.c "oooohhhhh"
        wt_image neighbour_slavegirl_anal_2
        "Even pulling her hair, hard, isn't enough to keep her from cumming before you do."
        wt_image neighbour_slavegirl_anal_9
        nicole.c "OWWW!!!  OOHHH!!"
        player.c "[player.orgasm_text]"
    elif nicole.slave_anal_outfit == 2:
        wt_image neighbour_slavegirl_anal_4
        player.c "Property doesn't need to cum, just because it has a dick up it's ass.  Understood?"
        nicole.c "oohhh ... yes, [nicole.your_name]"
        wt_image neighbour_slavegirl_anal_5
        "Property may not need to cum ..."
        nicole.c "ooohhhh"
        wt_image neighbour_slavegirl_anal_6
        "... but it still manages to, just before you do."
        nicole.c "OOHHH!!"
        player.c "[player.orgasm_text]"
    else:
        wt_image neighbour_slavegirl_anal_7
        "You put [nicole.name] on top."
        wt_image neighbour_slavegirl_anal_11
        "The awkward angle and strain on her legs should slow down her body's response to the feel of your cock in her ass."
        nicole.c "ooohhhh"
        wt_image neighbour_slavegirl_anal_8
        "It does, but still not enough to keep her from cumming before you do."
        nicole.c "OOHHH!!"
        player.c "[player.orgasm_text]"
    $ nicole.anal_count += 1
    $ nicole.orgasm_count += 1
    orgasm notify
    return

label nicole_slavegirl_pleasure:
    $ nicole.training_session()
    wt_image nicole.image
    if nicole.has_tag('artwork_now'):
        player.c "You look good enough to eat, [nicole.name]."
        nicole.c "Thank you, [nicole.your_name].  Should I lie down to make that more comfortable for you?"
    else:
        player.c "Are your nipples hard and your cunt wet, [nicole.name]?"
        wt_image neighbour_slavegirl_1
        nicole.c "Not right now they aren't, [nicole.your_name]."
        player.c "Get on the bed and let's change that."
        wt_image neighbour_slavegirl_2
        nicole.c "Yes, [nicole.your_name]."
    wt_image neighbour_slavegirl_pleasure_1
    "She may be property, but her nipple hardening in your mouth still feels good ..."
    wt_image neighbour_slavegirl_pleasure_2
    "... and her cunt flooding your mouth as she cums still tastes great."
    wt_image neighbour_slavegirl_pleasure_3
    nicole.c "OOHHH!!"
    $ nicole.orgasm_count += 1
    change player energy by -energy_short notify
    return

label nicole_slavegirl_spanking:
    $ nicole.training_session()
    wt_image nicole.image
    "[nicole.name] is always completely obedient to you. You never have to punish her to keep her in line. That means you get to save her spankings for times when you just feel like spanking her."
    player.c "I'm going to hurt you."
    if nicole.has_tag('artwork_now'):
        nicole.c "Yes, [nicole.your_name]."
        wt_image neighbour_slavegirl_11
    else:
        wt_image neighbour_slavegirl_1
        nicole.c "Yes, [nicole.your_name]."
        wt_image neighbour_slavegirl_7
    "She turns to give you easier access to her bare butt."
    wt_image neighbour_slavegirl_spanked_1
    nicole.c "oww ... ow ... oowww ... ow ow ... OW! ... OW OW OWW!! ... OOWWWW ... OOOWWWW"
    wt_image neighbour_slavegirl_sore
    "When you finally finish, the little tremor in [nicole.name]'s voice as she thanks you for her punishment is so cute, it makes you want to do it again."
    nicole.c "Thank you, [nicole.your_name]."
    $ nicole.spank_count += 1
    change player energy by -energy_short notify
    return

# Lend to Master M
label nicole_lend_to_master_m:
    $ nicole.training_session()
    rem tags 'available_today' from nicole
    wt_image neighbour_slavegirl
    player.c "[nicole.name], get dressed. I'm sending you to another man."
    nicole.c "Another man?  But, I belong to you, [nicole.your_name]."
    player.c "And you're mine to do what I want with. Today, what I want is for you to visit Master M and let him do whatever he wants with you. Dress nice for him."
    wt_image neighbour_slavegirl_2
    nicole.c "Yes, [nicole.your_name]."
    wt_image neighbour_mm_16
    "It's a few hours later before she returns."
    player.c "How did it go?"
    wt_image neighbour_mm_15
    nicole.c "Good, I think, [nicole.your_name]."
    player.c "Was he pleased with you?"
    wt_image neighbour_mm_11
    "She undresses as she answers you."
    nicole.c "I hope so, [nicole.your_name]."
    $ title = "Ask for details?"
    menu:
        "Yes":
            player.c "What did he do with you?"
            wt_image neighbour_mm_12
            nicole.c "{i}When I got there, he told me to sit.{/i}"
            wt_image neighbour_mm_13
            nicole.c "{i}He left me there, waiting ...{/i}"
            wt_image neighbour_mm_1
            nicole.c "{i}... until I'd thought he'd forgotten me.{/i}"
            wt_image neighbour_mm_2
            nicole.c "{i}Then, suddenly, his hands were on me, undressing me.{/i}"
            wt_image neighbour_mm_14
            nicole.c "{i}He spun me around ...{/i}"
            wt_image neighbour_mm_17
            nicole.c "{i}... shoved his fingers in my mouth ...{/i}"
            wt_image neighbour_mm_18
            nicole.c "{i}... and tested my gag reflex as he wrapped me in chains.{/i}"
            wt_image neighbour_mm_4
            nicole.c "{i}Just as I was afraid I was going to throw up, he stopped and checked between my legs.{/i}"
            wt_image neighbour_mm_19
            nicole.c "{i}He seemed surprised that my body wasn't wet for him, but I'm not sure why.  I'm your slavegirl, not his.  I was worried that he was disappointed and that you would be too ...{/i}"
            wt_image neighbour_mm_20
            nicole.c "{i}... when put me to work sucking his cock.{/i}"
            player.c "{i}What happened next?{/i}"
            wt_image neighbour_mm_5
            nicole.c "{i}Nothing, [nicole.your_name].  At least, not for a long, long time. He kept me there, sucking his cock, until my jaw ached and the muscles in my neck and shoulders were screaming at me.{/i}"
            nicole.c "{i}Then he kept me there some more. And some more. Then ... I'm sorry, [nicole.your_name]. I wanted to be a good slavegirl and make you proud of me, but ... then I started to cry.{/i}"
            wt_image neighbour_mm_6
            nicole.c "{i}I couldn't help myself. The agony in my sore muscles was unlike anything I'd experienced before. It was constant and unrelenting. And I knew that I wasn't allowed to make him cum until he was ready.{/i}"
            nicole.c "{i}I'm not sure I could have, even if I was allowed to.  I didn't know how long he would keep me doing this and I ...{/i}"
            nicole.c "{i}I felt the tears starting to run down my face and no matter how hard I tried to stop them, they just kept coming.{/i}"
            player.c "{i}Did you pull away from his cock?{/i}"
            nicole.c "{i}No, [nicole.your_name]. I think he thought I might, because he kept a firm grip on my head once I started to cry.{/i}"
            wt_image neighbour_mm_7
            nicole.c "{i}I think I may have spaced out after that, [nicole.your_name]. The next thing I remember he had removed my chains and was pushing me backwards, his cock still in mouth.{/i}"
            player.c "{i}Did he finally cum?{/i}"
            wt_image neighbour_mm_21
            nicole.c "{i}Yes, [nicole.your_name], but not in my mouth. He finally removed his cock from my mouth, and I thought my jaw was going to fall off ...{/i}"
            wt_image neighbour_mm_22
            nicole.c "{i}Then pushed himself inside me and filled me with his seed.  But not my cunt, [nicole.your_name].  Maybe he was still disappointed that I wasn't wet for him, because he used my ass instead.{/i}"
            player.c "{i}Did you cum, too?{/i}"
            wt_image neighbour_mm_8
            nicole.c "{i}No, [nicole.your_name]. Why would I have? I did start crying again, though, this time in happiness. I belong to you, [nicole.your_name], and I always will, but feeling him cum inside me, knowing that I had finally pleased him, it filled me with a sense of joy.{/i}"
            wt_image neighbour_spank_5
            nicole.c "I did my best to please your friend, [nicole.your_name]. I hope he wasn't disappointed with me or my crying. I hope even more that you aren't disappointed in me, [nicole.your_name]."
            $ title = "What do you do?"
            menu:
                "Punish her":
                    wt_image neighbour_kneel_8
                    player.c "You're a slavegirl, not a little child. If he'd whipped you raw and bleeding, then maybe you would have had a reason to cry."
                    nicole.c "I know, [nicole.your_name]. I'm sorry, [nicole.your_name]."
                    player.c "Get into position."
                    wt_image neighbour_slavegirl_3
                    nicole.c "Yes, [nicole.your_name].  Thank you, [nicole.your_name].  I deserve to be punished."
                    wt_image neighbour_slavegirl_spanked_1
                    "You make it a hard spanking, one of the hardest, if not the hardest, you've ever given her ... *SMACKKK* *SMACKKK* *SMACKKK* *SMACKKK* *SMACKKK*"
                    "It's almost unheard of for [nicole.name] to do anything deserving of a punishment, and she seems to genuinely crave correction for her self-perceived failing. The more painful you make it, the more grateful she seems to be."
                    wt_image neighbour_slavegirl_sore
                    nicole.c "Thank you, [nicole.your_name]!  Thank you so much for punishing me!!  I know it will make me be a better slave for you.  Thank you!!"
                    "The transformation really did a number on your former neighbor, but seeing her respond to correction, you wonder whether there wasn't always a part of her brain that craved domestic discipline. Greg may have missed out on the opportunity to settle disputes by placing his wife over his lap."
                    $ nicole.spank_count += 1
                    change player energy by -energy_short notify
                "Fuck her":
                    wt_image neighbour_slavegirl_sex_2
                    "If she was filled with joy when Master M came inside her, she's absolutely giddy and beside herself with happiness when you take her ..."
                    wt_image neighbour_slavegirl_sex_1
                    "... and fill her with your seed."
                    player.c "[player.orgasm_text]"
                    nicole.c "Ohhh [nicole.your_name]!!!!"
                    $ nicole.sex_count += 1
                    orgasm notify
                "Make her blow you":
                    player.c "Get on your knees."
                    wt_image neighbour_hypno_outfit_1_6
                    "Her jaw has had some rest, but you know it must still be very sore. Despite that, she obediently drops to her knees and takes you into her mouth."
                    wt_image neighbour_hypno_outfit_1_17
                    "She's in agony, and no matter how hard she tries not to let that show, the simple act of sucking you off after the ordeal Master M put her through may be the most intense torture you've inflicted on her."
                    wt_image neighbour_bj_2
                    "Before long, her whole body is trembling as her muscles rebel against overuse."
                    wt_image neighbour_bj_1
                    "Fortunately for her, you can't hold out for much longer, not while watching her try to ignore the tremors in her own body and focus exclusively on pleasuring your cock, no matter how much it hurts."
                    wt_image neighbour_hypno_outfit_1_7
                    player.c "[player.orgasm_text]"
                    "As you release your load into her mouth, she slips into a state of deep subspace.  She's spent most of the day as a mouth for fucking, first by Master M, then by you, and she's rarely if ever been happier."
                    $ nicole.blowjob_count += 1
                    $ nicole.swallow_count += 1
                    orgasm notify
                "Go on with your day":
                    wt_image neighbour_slavegirl_4
                    player.c "I'm sure you did fine, [nicole.name]."
                    nicole.c "Thank you, [nicole.your_name]."
                    wt_image neighbour_slavegirl
                    "She gets back into position, waiting for you to give her future instructions."
        "No, just go on with your day":
            wt_image neighbour_slavegirl_4
            "[nicole.full_name] gets dressed into her normal attire and you go back to your day."
    $ master_m.experience_with_your_slave = "I enjoyed making use of her, although there was something a bit ... off with her. I couldn't quite put my finger on it. Anyway, I enjoyed myself."
    $ master_m.name_of_your_slave_loaned = nicole.name
    $ nicole.training_session()
    add tags 'master_m_visit' to nicole
    call master_m_lend from _call_master_m_lend_4
    return

## Character Events
label nicole_dinner_invite:
    $ nicole.dinner_invite_open = False
    $ nicole.event_count = 3
    call forced_movement(nicole_house) from _call_forced_movement_207
    summon nicole
    wt_image neighbours_door
    "As you approach your neighbor's house ..."
    wt_image neighbour_dinner_1
    "... Nicole sees you coming and greets you at the door."
    nicole.c "Come on in!"
    wt_image neighbour_husband_1
    nicole.c "This is my husband, Greg."
    nicole_husband "Nice to meet you!"
    wt_image dinner_party_1
    "The three of you enjoy the dinner Nicole and Greg have prepared."
    if player.has_item(nicole_bottle_of_wine):
        wt_image dinner_party_2
        "After dinner, you break out the wine and the three of you chat as you sip it."
        rem 1 nicole_bottle_of_wine from player notify
        wt_image neighbour_husband_1
        "Eventually Greg asks what you do for a living."
        nicole_husband "How do you pay the bills?  Are you independently wealthy, or do you have to work like the rest of us poor slobs?"
        $ title = "What do you tell him?"
        menu:
            "I work the odd job here and there.":
                pass
            "I train wives for a living.":
                $ nicole.event_count = 4
                $ nicole.revealed_to_neighbour = 1
                wt_image neighbour_dinner_1
                nicole.c "What?  Seriously??  How does that work?"
                player.c "I train women on behalf of their husbands.  If they have a problem that they can't fix themselves, they send their wife to me, and I fix it for them."
                wt_image neighbour_husband_1
                nicole_husband "They send you their wives and you do what with them??"
                player.c "It depends on the issue.  Whatever they aren't happy with, I work with them to fix it.  Usually that's through hands on, motivational training."
                wt_image neighbour_dinner_1
                nicole.c "Hands on?  How hands on?"
                player.c "As much as you can imagine."
                "Nicole blushes, and not just from the wine."
                nicole.c "And the women put up with that?"
                player.c "I only work with willing participants, yes.  If they're not interested in being trained, there isn't much I can do for them."
                player.c "If they have a hang up they want to get over, or something they want to be better at ... something important enough to affect their marriage, then they'll accept my authority for the duration of their training."
                "Nicole looks at you with something close to wonder."
                wt_image neighbour_husband_1
                nicole_husband "And you get paid for this???"
                "Greg's looking at you with something close to wonder, too."
                if player.test('hypnosis_level', 0):
                    player.c "Yes, I get paid.  I'm worth it.  The hypnosis alone is worth my fee."
                    wt_image neighbour_dinner_1
                    nicole.c "Hypnosis?  You can hypnotize people?"
                    "Nicole sounds skeptical."
                    player.c "Yes, I can.  Would you like me to show you?"
                    wt_image neighbour_husband_1
                    "Nicole looks hesitant but her husband jumps in."
                    nicole_husband "Let's do it!  Come on Nicole, let him hypnotize you.  He's a professional, after all."
                    "Nicole nods her head in agreement."
                    call focus_image from _call_focus_image_80
                    "With her husband looking on in amusement, you put your neighbor under your trance."
                    wt_image neighbour_dinner_hypnotized
                    "You're just about to tell her to bare her breasts, when you catch yourself.  You're not sure Greg is ready to watch his wife strip for you."
                    player.c "Greg, tell me something about Nicole.  What sort of person is she?  What are her hobbies.  That sort of thing."
                    nicole_husband "Does shopping count as a hobby?"
                    player.c "Nicole, you have shopping to do, and it's very important. You can't shop in what you're wearing, and you don't have time to put on something else."
                    player.c "Take off your clothes and go shopping in your underwear. It'll be quicker that way."
                    wt_image neighbour_hypnotized_shopping
                    "Without a word, Nicole stands up and strips down to her bra and panties, then grabs her purse and heads toward the door."
                    nicole_husband "Whoa!  Whoa!  Better stop her!"
                    "It seems you've gone as far as Greg is comfortable with.  You instruct Nicole to dress and sit back down"
                    wt_image neighbour_dinner_hypnotized
                    "As you bring her out of the trance, you subtly reinforce her willingness to follow your instructions in future sessions. It's nothing Greg would be able to follow, but it should be enough to render her more compliant, should the opportunity to hypnotize her arise again."
                    wt_image neighbour_dinner_1
                    nicole.c "So, did it work?  Were you able to hypnotize me?  Why are you grinning like that, Greg?  What was I doing that was so funny?"
                    $ nicole.hypno_session() # deducts energy and records she was hypno'd
        wt_image dinner_party_2
        "The rest of the evening passes in idle chit chat, although you can't help but notice that Nicole seems a bit preoccupied.  Eventually you say your goodbyes, and head home."
    else:
        "With no wine to drink, you say your goodbyes after dinner, and head home."
    call character_location_return(nicole) from _call_character_location_return_116
    call forced_movement(living_room) from _call_forced_movement_208
    change player energy by -energy_short notify
    end_day
    return

label nicole_first_message:
    nicole.c "{i}Hi, it's me, Nicole, your neighbor.{/i}"
    nicole.c "{i}Is this you?  I found this profile online.  From what you told me, it sounded like you.{/i}"
    $ title = "How do you respond?"
    menu:
        "Yes, this is me":
            "You send a quick reply to Nicole:"
            player.c "{i}Yes, this is me.{/i}"
            "Now you wait to see what she does with this information."
            $ nicole.revealed_to_neighbour = 2
        "Delete without replying":
            "No good can come from your nosy neighbor poking around in your work. You delete her message. If she asks about it later, you'll deny receiving it.  Hopefully she'll decide the profile she found isn't you."
    $ nicole.event_count = 5
    $ nicole.message_one_available = False
    return

label nicole_second_message:
    nicole.c "{i}Hi, it's me again. Greg and I have been chatting, about you and what you do. And we've been reading some of the positive comments about you online.{/i}"
    nicole.c "{i}The thing is, I don't really have any issues that I need to be 'trained' about.{/i}"
    nicole.c "{i}Unless you count - and this is really embarrassing, which is why I'm sending this message instead of talking to you - unless you count that I want to sleep with you.{/i}"
    nicole.c "{i}Wow, you can't believe how hard that was for me to write. And now I'm not sure how I'll ever face you the next time I see you on the street.{/i}"
    nicole.c "{i}But there. It's done. I've said it. Or at least, written it.{/i}"
    nicole.c "{i}But okay, there's one more thing. And this is pretty embarrassing, too. I know you usually get paid for your 'training'.{/i}"
    nicole.c "{i}Greg and I can't afford to pay you. So, does that make me a charity case, because I'd like you to fuck me for free?{/i}"
    nicole.c "{i}So I think that last sentence is likely the most pathetic thing I've ever written in my life. I'll wait anxiously for your reply.  ~ N{i}"
    $ title = "How do you respond?"
    menu:
        "You don't do charity.":
            $ nicole.revealed_to_neighbour = 0
            if nicole.hypno_count >0:
                player.c "{i}Nicole, it makes me happy just to see you as my neighbor.  I wouldn't want anything to interfere with that.{/i}"
                "That should keep Greg and Nicole out of your business, without interfering with Nicole's hypnotic inclination to visit you."
                if nicole.has_item(dildo):
                    $ nicole.event_count = 6
                else:
                    $ nicole.event_count = 5
            else:
                player.c "{i}Nicole, I'm sure that was a difficult message for you to send. You're a lovely woman, and as flattered as I am by your offer, this is my work.{/i}"
                player.c "{i}For the health of our relationship, as neighbors, I think it would be best if we not complicate matters between us.{/i}"
                "That should keep Greg and Nicole out of your business."
        "Perhaps you can come to an arrangement.":
            $ nicole.event_count = 8
            player.c "{i}Nicole, thank you for your kind offer. As you point out, I normally get paid for my work. However, I think we may be able to come to an arrangement.{/i}"
            player.c '{i}From time to time I could use the assistance of a woman in my work, to act as a type of "teaching aide".{/i}'
            player.c "{i}As you live next door, you're ideally suited to join me in client sessions to help demonstrate the behavior I'm looking for from my client.{/i}"
            player.c "{i}If this arrangement is of interest to you, have Greg contact me. For the health of your marriage, and for the health of our relationship as neighbors, I need to know he consents before we go any further.{/i}"
            "Now you wait to hear what they say."
    $ nicole.message_two_available = False
    return

########### OBJECTS ###########
## Common Objects
# Put Into Character Specific Content

## Character Specific Objects
# Bottle of Wine
label bow_examine:
  wt_image wine_bottle
  "A bottle of wine you selected from your reserve for your dinner with your neighbors, Greg and Nicole."
  wt_image current_location.image
  return

## Items
# Give Butt Plug
label give_bp_nicole:
    if nicole.has_tag('slavegirl'):
        "Her ass is yours already. Save this for someone whose ass needs training."
    elif nicole.has_tag('showgirl'):
        "Maybe she could work it into her show, but you're better off saving this for someone else."
    else:
        "You don't have to buy her own. Depending on how things go, she may buy one for herself."
    return

# Give Chastity Belt
label give_cb_nicole:
    if nicole.has_tag('slavegirl'):
        "Putting this on her is just making more work for yourself."
    elif nicole.has_tag('showgirl'):
        "Wearing this would be hard for her to explain to her husband Greg."
    else:
        "Save this for someone else."
    return

# Give Dildo
label give_di_nicole:
    if nicole.has_tag('slavegirl'):
        "She doesn't need that.  She has you.  When you want her."
    elif nicole.has_tag('showgirl'):
        "That's a sweet gesture, but she seems quite satisfied already."
    else:
        "Not the right time or place for that."
    return

# Use Fetch Toy
label use_ft_nicole:
    if nicole.has_tag('slavegirl'):
        "She's your slave, not your puppy."
    elif nicole.has_tag('showgirl'):
        "You must be thinking of a different type of show."
    else:
        "You shouldn't try to play fetch with someone who isn't your pet."
    return

# Give Jewelry
label give_jwc_nicole:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_nicole:
    if nicole.has_tag('slavegirl'):
        "She's your slave, not your puppy."
    elif nicole.has_tag('showgirl'):
        "You must be thinking of a different type of show."
    else:
        "You shouldn't try to take someone for a walk who isn't your pet.  At least, not on the end of your leash."
    return

# Give Lingerie
label give_li_nicole:
    if nicole.has_tag('slavegirl'):
        "She has all the clothes she needs for her new life."
    elif nicole.has_tag('showgirl'):
        "That's a sweet thought, but she likes to choose her own dancing clothes."
    else:
        "Save this for someone else."
    return

# Give Love Potion
label give_lp_nicole:
    if nicole.has_tag('slavegirl'):
        "She's already completely devoted to you."
    elif nicole.has_tag('showgirl') and current_location == stage:
        wt_image nicole.image
        nicole.c "Thanks, but I'm about to go on stage.  I don't have time for a drink."
    else:
        "Not the right time or place.  Possibly not even the right person."
    return

# Give Transformation Potion
label give_tp_nicole:
    if nicole.has_tag('transformed'):
        "Your neighbor has already been transformed.  The potion can do nothing more to her now."
    elif nicole.has_tag('waiting_for_club_access'):
        "Your neighbor has already been transformed.  You just need to find her a place where she can safely take her clothes off."
    elif nicole.has_tag('available_today') and nicole.in_area('house'):
        "Once a transformation has occurred, it cannot be undone. Only one transformation can ever occur with any one person."
        # showgirl possible?
        if (nicole.hypnosis_visits_post_dildo and nicole.hypno_count > 4) or nicole.strip_count > 3:
            $ nicole.showgirl_possible = True
        # slavegirl_possible?
        if (nicole.hypnosis_visits_post_dildo and nicole.hypno_count > 5 and nicole.anal_count > 0) or nicole.submission_count > 1 or nicole.beg_count > 1:
            $ nicole.slavegirl_possible = True
        if nicole.showgirl_possible and nicole.slavegirl_possible:
            "Nicole's been introduced to as many possibilities as you can. The potion should have lots of options for you."
        elif nicole.showgirl_possible and not nicole.slavegirl_possible:
            "Nicole's learned to show off her body. That may be something the potion could work with. And it could adjust her sexuality."
            "Alternatively, you may prefer to wait until you're introduced her to more possibilities."
        elif nicole.slavegirl_possible and not nicole.showgirl_possible:
            "Nicole's become used to doing things she wouldn't normally do, in order to please you. That may be something the potion could work with. And it could adjust her sexuality."
            "Alternatively, you may prefer to wait until you're introduced her to more possibilities."
        else:
            "Nicole's not been introduced to many possibilities yet. The potion may be able to adjust her sexuality, but that's it."
        $ title = "Give her the potion?"
        menu:
            "Not now":
                $ nicole.temporary_count = 0
            "Yes, proceed (consumes the potion)":
                $ nicole.temporary_count = 1
        if nicole.temporary_count == 1:
            call forced_movement(kitchen) from _call_forced_movement_307
            summon nicole no_follows
            wt_image neighbour_transformation_1
            "You offer Nicole a freshly made cup of coffee."
            player.c "I hope you like it.  It's my own special blend."
            nicole.c "Mmmm ... thank you!"
            wt_image neighbour_transformation_2
            "The potion takes effect quickly.  Nicole becomes distracted and confused."
            wt_image neighbour_conflicted
            "Soon she's a mass of confusion, struggling to cope as the potion opens her up to the possibility of great change."
            "Once a transformation has occurred, it cannot be undone. Only one transformation can ever occur with any one person."
            "You now need to focus and devote some energy into sculpting the changes the potion will make in Nicole. What do you want to turn your neighbor into?"
            $ title = "What to you want to change Nicole into?"
            menu:
                "Bi-Sexual":
                    "Although she never speaks of it, Nicole harbors a mild curiosity about what it would be like to sleep with another woman.  It isn't a lot to work with, but its all the transformation potion needs."
                    "It latches on to this curiosity and amplifies it until it becomes a burning desire, a major unmet need in your neighbor's life."
                    player.c "Nicole, I have a friend I would like you to meet. A female friend. She's very pretty. I've told her about you.  She said she would like to meet you. I think she's attracted to you Nicole. Would you like me to ask her to come over sometime?"
                    "Still recovering from the effect of the potion, Nicole is unable to speak. She nods her head gratefully at your offer, thankful beyond belief that you are offering her an opportunity to finally fulfill her lifetime desire to touch and be touched by another woman."
                    $ nicole.transformed_via_object = True
                    call nicole_convert_lesbian from _call_nicole_convert_lesbian
                "Showgirl" if nicole.showgirl_possible:
                    "Even if she won't admit it, Nicole has always been proud of her body.  You've introduced her to the experience of using her body to put on a show, and part of her liked it."
                    "The transformation potion grabs hold of this experience and the exhibitionist thrill it inspired, and amplifies it, until it's a core part of her personality."
                    "She loves her body, she loves showing off her body. She wants men to see her body. It's a consuming need inside her, to show herself to as many appreciative men as possible."
                    wt_image neighbour_transformation_3
                    "She hasn't yet recovered enough from the effect of the potion to speak, but she shakily gets to her feet, pulling off her clothes. She needs to show her body to you."
                    wt_image neighbour_transformation_4
                    "She's far too weak from the transformation to put on any kind of a dance. It's all she can do to balance herself precariously on the edge of the table and open herself up for you - or anyone - to see."
                    wt_image neighbour_transformation_6
                    "You don't want her to think that her efforts are unappreciated.  You guide the woozy woman to your bed ..."
                    wt_image neighbour_transformation_7
                    "... and demonstrate how much you enjoyed her attempted dance."
                    wt_image neighbour_transformation_8
                    "Unfortunately, she's too exhausted by the transformation to truly appreciate, or even participate, in your 'thank you'."
                    wt_image neighbour_transformation_5
                    "So you roll her over and finish demonstrating your appreciation ..."
                    wt_image neighbour_transformation_9
                    "... as she gets her much needed rest."
                    nicole.c "*snore*"
                    player.c "[player.orgasm_text]"
                    $ nicole.sex_count += 1
                    orgasm
                    if player.has_tag('club_access') and player.has_tag('club_first_visit_complete'):
                        "When she wakes up, you'll give her directions to the Club.  She should do well there."
                    else:
                        "You'll need to keep an eye out for somewhere she can safely take her clothes off.  Without an outlet for her urges, who knows where she'll get naked?"
                    $ nicole.transformed_via_object = True
                    call nicole_convert_showgirl from _call_nicole_convert_showgirl
                "Slavegirl" if nicole.slavegirl_possible:
                    "Nicole has never consciously thought of herself as submissive, but you've inspired enough submissive feelings in her for the transformation potion to have something to work with."
                    "It latches on to these feelings and amplifies them until they become the center and the core of your neighbor's being. They become who she is, a mere possession. Property. Your property. Nothing more, nothing less."
                    wt_image neighbour_transformation_3
                    "Shakily, she removes her clothes ..."
                    wt_image neighbour_transformation_10
                    "... and sinks to the floor, uncertain about where she is and what she should be doing."
                    wt_image neighbour_transformation_11
                    "Still woozy from the potion, she crawls after you as you guide your new slavegirl into your bedroom. This will be her place from now on."
                    $ nicole.transformed_via_object = True
                    call nicole_convert_slavegirl from _call_nicole_convert_slavegirl
                "Nothing (undo)":
                    $ nicole.temporary_count = 0
                    "Let's just pretend that didn't happen.  That's easier than reloading an old save."
            if nicole.temporary_count == 1:
                $ nicole.temporary_count = 0
                $ nicole.training_session()
                rem tags 'available_today' from nicole
                rem 1 transformation_potion from player
                change player energy by -energy_long notify
                call character_location_return(nicole) from _call_character_location_return_117
                call forced_movement(living_room) from _call_forced_movement_308
            else:
                call forced_movement(living_room) from _call_forced_movement_309
                summon nicole no_follows
    else:
        "Not the right time or place."
    return

# Give Ring of Secuality
label give_rs_nicole:
    "This may work, but there's no content for her.  You should save this for someone else."
    return

# Use Water Bowl
label use_wb_nicole:
  "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

# Use Will Tamer
label use_wt_nicole:
    if nicole.has_tag('transformed'):
        "Your neighbor has already been transformed.  The Will-Tamer can do nothing more to her now."
    elif nicole.has_tag('will_tamer_this_week'):
        "You've already used the Will_Tamer on her this week.  The re-wiring of her brain it has started will take some time to complete.  Try again next week."
    elif nicole.has_tag('available_today') and nicole.in_area('house') and nicole.has_tag('teaching_aide'):
        if nicole.spectacle_yet:
            if nicole.will_tamer_count == 0:
                $ nicole.training_session()
                add tags 'will_tamer_this_week' to nicole
                if current_location != living_room:
                    call forced_movement(living_room) from _call_forced_movement_310
                $ nicole.will_tamer_count = 1
                wt_image neighbour_show_1
                player.c "Ready to be artwork for me?"
                nicole.c "I suppose.  Do you want me on the counter again?"
                player.c "No, I've something else in mind for today."
                wt_image neighbour_kneel_7
                nicole.c "What is that?"
                player.c "A collar for my ornament to wear."
                nicole.c "I'm not a slavegirl."
                player.c "Do you think me putting this on you will make you one?"
                nicole.c "No.  Obviously not.  But why do you want me to wear a collar?"
                player.c "You'll make a nice decoration for my house while you're wearing it. Bow your head while I put it on you."
                wt_image neighbour_kneel_8
                nicole.c "They're going to take away my strong, independent women's membership card if anyone finds out about this."
                player.c "You can exchange it for membership in the slavegirls' club."
                nicole.c "Ha ha. Funny.  Okay, put it on and make me look like a slavegirl."
                wt_image neighbour_will_tamer
                "She doesn't so much look like a slavegirl as she looks like a woman struggling with the confusion of having her brain rewired. Which it is."
                "Every pleasurable moment she's had while submitting to you is amplified and intensified in her memory bank. Making decisions is hard and unsatisfying. Obeying is easy and natural."
                wt_image neighbour_transformation_6
                "You don't leave it on very long, as prolonged exposure could fry the poor girl's brain. When the Will-Tamer comes off, Nicole seems distracted, unable to look you in the eyes - and horny."
                nicole.c "oohhh ... why does being artwork for you turn me on so much?"
                player.c "Do you want to play with yourself?"
                nicole.c "Badly, but ... I don't know why, but I'm exhausted. I think I need to lie down."
                "It'll take a few days for the Will-Tamer to complete the changes it's making to her brain.  She'll be ready for another session in the collar next week."
                call character_location_return(nicole) from _call_character_location_return_118
            elif nicole.will_tamer_count == 1:
                $ nicole.training_session()
                add tags 'will_tamer_this_week' to nicole
                $ nicole.will_tamer_count = 2
                if current_location != living_room:
                    call forced_movement(living_room) from _call_forced_movement_311
                wt_image neighbour_spank_1
                player.c "Off with your clothes, Nicole. It's time for you to wear your collar again."
                wt_image neighbour_kneel_7
                nicole.c "My collar?  Since when did this become my collar?"
                player.c "That's how I think of it when you're wearing it here, for me. When it's just the two of us. You don't mind the idea of wearing your collar for me, do you?"
                wt_image neighbour_kneel_8
                "Your neighbor looks at the collar with a mixture of dread and curiosity - and longing. Since her first session in the Will-Tamer, she's found herself fantasizing about being someone's possession."
                "She's not sure she likes these new found thoughts. Her pussy, on the other hand, is getting sopping wet at the thought of you locking her collar around her neck. The conflict inside her lasts only a moment, then her pussy wins."
                nicole.c "I ... I suppose not."
                player.c "Good girl. You'll be a proper slavegirl in no time."
                wt_image neighbour_will_tamer
                "The Will-Tamer picks up and amplifies the submissive thoughts it's previously stimulated in Nicole. You can see it breaking down her resistance, replacing her previous personality with a new one, centered solely on the joy of being a mere possession."
                "You can't leave it on very long, or her brain will turn to mush. When you see her eyes start to glaze over, you know that's enough for today."
                wt_image neighbour_transformation_6
                nicole.c "I ... I ... May I please have permission to lie down and rest, [nicole.your_name]?"
                "One more session in the collar, and the neighbor you knew will be no more. You can decide next week whether you want that."
                call character_location_return(nicole) from _call_character_location_return_119
            else:
                "The Will-Tamer has had enough time now that one more session will be enough to convince your neighbor to give up her current life and devote herself exclusively to serving you."
                "If you do this, there will be no going back. Nicole as you know her now will no longer exist. You'll also lose the Will-Tamer, as it'll become a part of your new possession."
                $ title = "Proceed?"
                menu:
                    "Transform her with the Will-Tamer":
                        $ nicole.training_session()
                        add tags 'will_tamer_this_week' to nicole
                        if current_location != living_room:
                            call forced_movement(living_room) from _call_forced_movement_312
                        wt_image neighbour_kneel_8
                        "Nicole strips and meekly bows her head as you approach with the collar."
                        player.c "What is this, girl?"
                        "She hesitates before responding in a shaky voice."
                        nicole.c "It's my collar, Sir."
                        player.c "What should I do with it?"
                        "The part of her brain that is still the strong, independent woman she was born makes one last, desperate attempt to take control, but to no avail. The wetness between her legs is too strong."
                        nicole.c "You should put it on me, Sir."
                        player.c "Look at me."
                        wt_image neighbour_face_2
                        player.c "Do you enjoy your current life?"
                        nicole.c "Yes, Sir."
                        player.c "Do you understand why you're calling me 'Sir'?"
                        nicole.c "No, Sir. Not exactly. But I know it has to do with my collar."
                        player.c "What happens when I tell you that you can either turn around and go back to your current life or bow your head?"
                        wt_image neighbour_conflicted
                        player.c "Do you understand why your head is bowed?"
                        "Tears run down her cheeks as she chokes out her answer."
                        nicole.c "No, Sir."
                        player.c "It's okay, girl. Everything's about to become a lot simpler."
                        "Patting her head tenderly, you wrap the collar around her neck."
                        wt_image neighbour_will_tamer
                        "It takes only a moment for the Will-Tamer to fuse with her, becoming a permanent part of her."
                        wt_image neighbour_transformation_10
                        "She sinks to the floor, uncertain about where she is and what she should be doing."
                        wt_image neighbour_transformation_11
                        "Still woozy from the transformation, she crawls after you as you guide your new slavegirl into your bedroom.  This will be her place from now on."
                        rem 1 will_tamer from player
                        $ nicole.transformed_via_object = True
                        call nicole_convert_slavegirl from _call_nicole_convert_slavegirl_1
                    "Not yet":
                        pass
        else:
            "She's not ready to be introduced to wearing a collar yet."
    elif nicole.has_tag('hypnosis_visit_today') and not nicole.has_tag('teaching_aide'):
        "You're not going to be able to convince her to wear the Will-Tamer through hypnosis."
    else:
        "Not the right time or place."
    return

########### TIMERS ###########
## Common Timers
# Start Day Timers
label nicole_start_day_early_am_events:
    # check for early am Nicole visits
    if day == 2 and nicole.event_count > 0:
        # Nicole sneaks into your bed (Playboy)
        if nicole.event_count == 9:
            call forced_movement(bedroom) from _call_forced_movement_313
            summon nicole
            wt_image neighbour_bedroom_1
            "You wake to the sound of someone climbing into your bed."
            wt_image neighbour_bedroom_2
            "It's your neighbor, Nicole.  When did she steal a key?"
            wt_image neighbour_bedroom_3
            "Without a word, she takes out your cock and sucks you hard."
            wt_image neighbour_bedroom_4
            "Then she climbs on top of you and starts fucking herself on your cock, rocking back and forth."
            wt_image neighbour_bedroom_5
            "She soon brings herself to a quiet but seemingly enjoyable climax ..."
            nicole.c "Mmmmm"
            wt_image neighbour_bedroom_6
            "... then turns her attention to you."
            wt_image neighbour_bedroom_7
            "It doesn't take her long to bring you to orgasm."
            player.c "[player.orgasm_text]"
            orgasm notify
            wt_image neighbour_bedroom_8
            "And then with a quick peck on your cheek she's gone, without saying a word."
            "You've had worse starts to your day, but you just know this is going to end oh so very badly."
            wt_image living_room.image
            $ nicole.event_count = 10
            add tags 'event_9_today' to nicole
            call character_location_return(nicole) from _call_character_location_return_120
        # Nicole and Greg move out
        elif nicole.event_count == 11:
            add tags 'neighbours_lost' to player
            wt_image moving_van
            "You wake to the sounds of a moving van being packed at Greg and Nicole's house. Whether they left the neighborhood together, or went their separate ways, you never find out."
            $ nicole.event_count = 0
            # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
            # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
            # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
            call convert(nicole, "unavailable") from _call_convert_117
    return

label nicole_start_day_normal_events:
    # Showgirl Nicole goes to Stage if you have sent her there
    if nicole.dancing_at_club:
        summon nicole to stage no_follows
    # Teaching Aide Nicole is available to visit once per week
    if nicole.neighbour_arrangement and nicole.can_be_interacted:
        add tags 'available_today' to nicole
    # Greg comes looking for Slave Nicole
    if nicole.has_tag('slavegirl') and not nicole_husband.searched_for_slavenicole:
        $ nicole_husband.searched_for_slavenicole = True
        wt_image front_door
        "There's a knock on your door."
        wt_image neighbour_husband_1
        "It's your neighbor, Greg."
        nicole_husband "Hi, do you know where Nicole is?  She hasn't come home."
        summon nicole
        wt_image neighbour_slavegirl
        nicole.c "I'm not coming home.  I belong to my Master now."
        wt_image neighbour_husband_1
        nicole_husband "What are you talking about???  You belong to your Master?  Is this some kind of game, Nicole?  Why are you down on your knees like that??"
        wt_image neighbour_slavegirl_1
        nicole.c "It's not a game, Greg.  It's my new life. It's what I always wanted.  I just didn't know it before."
        nicole.c "I'm a possession.  It's what I was meant to be. And a possession can't be your wife.  A possession can't be anyone's wife."
        wt_image neighbour_slavegirl
        nicole.c "I'm sorry, Greg.  It's over between us.  But don't worry.  I don't want anything.  You can keep the house, the car, everything.  I have everything I need here."
        "Greg is so shaken, he turns around and goes home without another word."
        wt_image moving_van
        "The next morning Greg will call again.  He'll call three times in all.  Every time, Nicole tells him the same thing.  Eventually, he accepts Nicole's new reality.  Shortly thereafter, he moves out of the neighborhood."
        "Other husbands may create more of a fuss than Greg did, and a transformed mind wouldn't do well under intense questionning.  Best to be more careful in the future of who you transform and when."
        call character_location_return(nicole) from _call_character_location_return_121
    # check for normal Nicole visits
    if day == 2 and nicole.event_count > 0:
        # First Event: Welcome to the Neighbourhood
        if nicole.event_count == 1:
            wt_image front_door
            "In the morning there's a knock at your door."
            summon nicole
            wt_image neighbour_door_2
            "An attractive young woman stands on your front step."
            nicole.c "Hi, my name's Nicole. My husband Greg and I live across the street. I just wanted to drop by and welcome you to the neighborhood."
            wt_image housewarming_gift
            nicole.c "I brought you this house warming gift. I hope you like it."
            wt_image neighbour_door_2
            $ title = "What do you say?"
            menu:
                "It's lovely, thank you.":
                    nicole.c "I'm glad you like it. So, do you live here alone?  I didn't see anyone with you when you moved in."
                    player.c "It's just me."
                    nicole.c "Oh, well, it's nice to meet you.  I'm sure you'll like it here.  It's a very friendly neighborhood."
                    wt_image living_room.image
                    "Nicole smiles and leaves.  You put the bonsai tree in your living room for the time being."
                    $ nicole.event_count = 2
                "Living and sculptable - how perfect.":
                    nicole.c "I'm glad you like it. So, do you live here alone?  I didn't see anyone with you when you moved in."
                    player.c "It's just me."
                    nicole.c "Oh, well, it's nice to meet you.  I'm sure you'll like it here.  It's a very friendly neighborhood."
                    wt_image living_room.image
                    "Nicole smiles and leaves.  You put the bonsai tree in your living room for the time being."
                    $ nicole.event_count = 2
                "I'd prefer a more personal gift.":
                    wt_image front_door
                    "Nicole leaves, taking her gift with her and slamming your door behind her."
                    $ nicole.event_count = 0
            if nicole.event_count == 2:
                add tags 'bonsai_allowed' to living_room
                add tags 'bonsai_allowed' to boudoir
                add tags 'bonsai_allowed' to dungeon
                add tags 'bonsai_allowed' to basement
                add tags 'bonsai_allowed' to bedroom
                add 1 nicole_bonsai to living_room
                notify
            call character_location_return(nicole) from _call_character_location_return_122
        # Second event: Dinner Invitation
        elif nicole.event_count == 2:
            wt_image front_door
            "In the morning there's a knock at your door."
            summon nicole
            wt_image neighbour_door_2
            "It's your neighbor, Nicole."
            nicole.c "Hi!  I just wanted to ask if you'd like to come over for supper tonight with my husband Greg and I?"
            nicole.c "We're not making anything fancy - just pasta.  I thought it might be a nice opportunity for us to get to know each other."
            $ title = "What do you say?"
            menu:
                "I'd love to":
                    $ living_room.action_dinner_nicole = living_room.add_action("Join Nicole and Greg for Dinner", label = "nicole_dinner_invite", context = '_contact_other', condition = "nicole.dinner_invite_open", ends_day = True)
                    $ nicole.dinner_invite_open = True
                    nicole.c "Great!  I'll see you tonight."
                    wt_image living_room.image
                    "Nicole smiles and leaves.  If you don't plan on standing them up, you'll need to join them for dinner before ending the day.  That means no client session tonight."
                    $ nicole.event_count = 0 # will get set to either 3 or 4 if you attend the dinner
                "I'll bring some wine (costs 5)":
                    if player.money - player.min_money >= 5:
                        $ living_room.action_dinner_nicole = living_room.add_action("Join Nicole and Greg for Dinner", label = "nicole_dinner_invite", context = '_contact_other', condition = "nicole.dinner_invite_open", ends_day = True)
                        $ nicole.dinner_invite_open = True
                        nicole.c "Great!  I'll see you tonight."
                        wt_image living_room.image
                        "Nicole smiles and leaves.  If you don't plan on standing them up, you'll need to join them for dinner before ending the day.  That means no client session tonight.  In the meantime, you grab a bottle of wine, just in case."
                        change player money by -5
                        add 1 nicole_bottle_of_wine to player notify
                        $ nicole.event_count = 0 # will get set to either 3 or 4 if you attend the dinner
                    else:
                        player.c "I'd love to, but not tonight.  I'd like to bring some wine, and I don't have any right now.  Maybe we could do this another time?"
                        nicole.c "Sure!  That'd be fine.  I'll let you know the next time Greg and I are available."
                        wt_image living_room.image
                "Not tonight":
                    player.c "I'd love to, but not tonight.  I'd like to bring some wine, and I don't have any right now.  Maybe we could do this another time?"
                    nicole.c "Sure!  That'd be fine.  I'll let you know the next time Greg and I are available."
                    wt_image living_room.image
                "Perhaps sometime when your husband isn't home":
                    wt_image front_door
                    "Nicole leaves, slamming your door behind her."
                    $ nicole.event_count = 0
            call character_location_return(nicole) from _call_character_location_return_123
        # Third event: Visit from Curious Nicole
        elif nicole.event_count == 3:
            # Curious Yet?  Event repeats until she is
            #$ nicole.temporary_count = player.submission_action_count + player.desire_action_count
            #if nicole.temporary_count > 6:
            if player.client_visits_count > 6:
                wt_image front_door
                "In the morning there's a knock at your front door."
                summon nicole
                wt_image neighbour_door_4
                "A concerned looking Nicole is at your doorstep."
                nicole.c "Can I come in?"
                wt_image neighbour_inside_1
                nicole.c "I'm sorry to be a butt-in-ski, but I have to ask you something."
                wt_image neighbour_inside_2
                nicole.c "I see these women coming and going from your house. Are they just girlfriends of yours, or is there something else going on?"
                $ title = "What do you tell her?"
                menu:
                    "They're just women I'm dating.":
                        $ nicole.event_count = 5
                        player.c "They're just women I'm dating."
                        wt_image neighbour_inside_11
                        "Nicole nods, but looks sceptical."
                        nicole.c "Okay.  Well, your personal life is none of my business. I'm sorry for disturbing you. I shouldn't be butting my nose in where it doesn't belong."
                        wt_image neighbour_inside_2
                        nicole.c "I was just curious.  You seem to have a very ... active ... social life.  Not that I'm keeping track of you."
                    "There's something else going on.":
                        $ nicole.event_count = 4
                        $ nicole.revealed_to_neighbour = 1
                        player.c "You're very perceptive, Nicole. Yes, there's something more going on. I run a business from here in my home."
                        nicole.c "What type of business?"
                        player.c "I'm a wife trainer."
                        wt_image neighbour_inside_11
                        nicole.c "A what?  Did you say wife trainer?"
                        player.c "Yes. I train women on behalf of their husbands. If they have a problem that they can't fix themselves, they send their wife to me, and I fix it for them."
                        wt_image neighbour_inside_12
                        nicole.c "And the women put up with that?"
                        player.c "I only work with willing participants, yes. If they're not interested in being trained, there isn't much I can do for them."
                        "If they have a hang up they want to get over, or something they want to be better at ... something important enough to affect their marriage, then they'll accept my authority for the duration of their training."
                        wt_image neighbour_inside_5
                        "Nicole looks at you with something close to wonder."
                        nicole.c "That's ... interesting, I guess."
                wt_image neighbour_inside_13
                "After some awkward small talk, Nicole heads home."
                if player.test('hypnosis_level', 0):
                    $ title = "Stop her?"
                    menu:
                        "Hypnotize her":
                            call focus_image from _call_focus_image_81
                            player.c "Before you go, Nicole, look at this for me. Look at this and listen to me. Listen to me, Nicole. Only me. Just the sound of my voice."
                            wt_image neighbour_hypnotized_inside_1
                            player.c "You want to be neighborly, Nicole.  A good way to be neighborly is to help me be comfortable around you."
                            wt_image neighbour_inside_12
                            player.c "Help me be comfortable around you by relaxing and taking off your top.  Showing me your breasts is the friendly, neighborly thing to do."
                            wt_image neighbour_hypnotized_inside_2
                            "She willingly complies ..."
                            wt_image neighbour_hypnotized_inside_9
                            "... removing her top and then framing her breasts for you using her clothes to provide a view of her bare breasts."
                            "Nicole seems more comfortable than most women showing her body to you, so you ask her to show you everything."
                            player.c "That's very neighborly of you, Nicole. I'm feeling more comfortable with you now. If only you weren't hiding so much from me."
                            wt_image neighbour_hypnotized_inside_6
                            player.c "If you weren't hiding so much of who you are and showed me everything, that would be so much more neighborly of you, and I'd be so much more comfortable around you."
                            wt_image neighbour_hypnotized_inside_10
                            player.c "That's better, Nicole.  That's much more neighborly.  If only you weren't still hiding things from me."
                            wt_image neighbour_hypnotized_inside_7
                            player.c "I'd be so much more comfortable around you if I knew you were completely open to me and showing me everything."
                            wt_image neighbour_hypnotized_inside_4
                            "... before sitting back down in front of you, completely naked."
                            player.c  "That's very neighborly of you, Nicole. I'm feeling so much more comfortable with you now."
                            player.c "It would be best, though, if you were an open book, spread open to show me everything. That's what a good neighbor would be for me."
                            if nicole.hypno_count > 0:
                                wt_image neighbour_hypnotized_inside_5
                                "Your neighbor's willingness to share bodes well for your future relationship."
                            else:
                                wt_image neighbour_hypnotized_inside_8
                                "She keeps her legs firmly closed. You haven't hypnotized her often enough to lower her resistance to you enough for that.  Not yet, anyway."
                            "For the moment, you've taken her as far as she can go. You enjoy the view for a while, then instruct her to get dressed."
                            wt_image neighbour_inside_2
                            "Once she's respectable again, you take her out of her trance and let her return home."
                            nicole.c "It was great chatting with you.  Bye!"
                            $ nicole.hypno_session()
                        "Let her go":
                            pass
                wt_image living_room.image
                call character_location_return(nicole) from _call_character_location_return_124
        # Fourth event: Email from Nicole
        elif nicole.event_count == 4:
            $ nicole.event_count = 0
            "You received a new message."
            $ nicole.message_one_available = True
        # Fifth event:  initial Playboy or continuing Hypnosis Events
        elif nicole.event_count == 5:
            if nicole.hypno_count > 0 or player.has_tag('supersexy'):
                rem tags 'no_hypnosis' from nicole
                wt_image front_door
                "In the morning there's a knock at your door."
                summon nicole
                wt_image neighbour_door_2
                "It's your neighbor, Nicole."
                nicole.c "Hi!  Can I come in?"
                wt_image neighbour_inside_9
                nicole.c "I hope you don't mind me dropping by unannounced like this."
                wt_image neighbour_inside_10
                if player.has_tag('supersexy'):
                    nicole.c "I was wondering if you were ... well, doing anything ... and I guess ... wondered if maybe ..."
                    "Women have been throwing themselves at you since you hit puberty. As cute as it is to watch Nicole stumble her way around asking if you'd like to make out with her, letting this go any further is a bad idea."
                    if player.short_name == 'pb':
                        "It was situations like this that caused you to leave your old life behind, move to a new city, and become the Wife Trainer. If you let this happen, it'll end badly. It always does."
                    "On the other hand, Nicole is crazy hot, and the thought of her lips on your body is making it hard for you to think of anything else. Very hard."
                else:
                    nicole.c "So ... ummm ... Greg is away today ... out of town actually. I was wondering if you wanted to ... talk or something?"
                    if not nicole.has_tag('hypno_visit_message_given'):
                        add tags 'hypno_visit_message_given' to nicole
                        "Your past hypnosis of Nicole has opened up her mind to the idea of pleasing you, and she's taken the first step towards making herself available to you."
                wt_image neighbour_inside_3
                $ title = "What do you do?"
                menu:
                    "Hypnotize her" if player.can_hypno(nicole):
                        "That's a lovely idea, Nicole. Let's talk."
                        call focus_image from _call_focus_image_82
                        player.c "To start, I'll do the talking while you look at this. I'll do the talking, and you'll do the listening.  You will listen, Nicole.  You'll listen and learn."
                        wt_image neighbour_hypnotized_house_12
                        player.c "You'll do this because you want to please me.  You will listen and learn and obey me because you want to be a good neighbor and please me.  Please me now, Nicole.  Show me your breasts and please me."
                        wt_image neighbour_hypnotized_house_1
                        "The hypnotized woman raises her top for your approval."
                        player.c "That's a good start, Nicole.  You're very beautiful.  Far too beautiful to hide so much of your body from me.  Show me how beautiful the rest of you is.  Show me your body and please me."
                        wt_image neighbour_hypnotized_house_3
                        player.c  "That's better, Nicole.  You have a beautiful ass.  You have other beautiful body parts, though.  Show me the rest of your body to please me, Nicole."
                        wt_image neighbour_hypnotized_house_2
                        player.c "Yes, your pussy would be beautiful, Nicole.  It would please me to look at your pussy.  Show it to me, Nicole.  Show it to me to please me."
                        wt_image neighbour_hypnotized_house_4
                        player.c "Very good, Nicole.  Your body is very pleasing to me.  You like to please me.  You like to please me with your body.  Use your body to please me, Nicole."
                        wt_image neighbour_hypnotized_house_13
                        "She hesitates.  She loves her husband.  She wants to please you, but she isn't ready to have sex with you yet."
                        $ title = "What now?"
                        menu:
                            "Give her a dildo" if player.has_item(dildo):
                                give 1 dildo from player to nicole notify
                                wt_image neighbour_hypnotized_house_9
                                "You go to your toy chest and bring out a new vibrator. You can sense Nicole's relief as she takes the toy from you. She sees this as is the perfect way for her to please you with her body without cheating on her husband."
                                wt_image neighbour_hypnotized_house_5
                                "She wets the toy eagerly with her mouth ..."
                                wt_image neighbour_hypnotized_house_6
                                "... then slides it into herself."
                                player.c "That's good, Nicole.  Show me how you're going to use your body to please me, Nicole."
                                wt_image neighbour_hypnotized_house_10
                                "The hypnotized woman strokes the dildo in and out of her rapidly wetting pussy."
                                player.c "Very good, Nicole.  That feels good.  It feels great.  It feels right.  If only that was my cock.  If it was my cock, it would feel so good.  It would feel so great.  It would be fucking you hard and fast and it would feel so right."
                                wt_image neighbour_hypnotized_house_14
                                "She jams the dildo in and out of herself, faster and faster.  Her breathing quickens and she begins to moan."
                                player.c "It's right that you enjoy yourself with me.  It's right that you please me with your body, Nicole.  And it's right that you cum when you're with me."
                                wt_image neighbour_hypnotized_house_15
                                "Under your gaze and the influence of your words, an orgasm ripples through your neighbor."
                                nicole.c "OOOHHHH!!!!"
                                wt_image neighbour_hypnotized_house_8
                                "You give her some time to enjoy the sensation and associate it with you before instructing her to dress and bringing her out of her trance."
                                $ nicole.event_count = 6
                                $ nicole.hypnosis_visits_post_dildo = True

                            "Wait":
                                "Nicole's at a road block about how to please you without cheating on her husband, and you're not going to get past it with hypnosis alone."
                                "If you had a suitable toy to give her, you may be able to take her further, but for today, you've taken her as far as you can.  You have her dress and bring her out of her trance."

                        wt_image neighbour_inside_3
                        player.c  "That was fun, Nicole.  I'm so glad you dropped by to talk. I enjoyed it greatly."
                        wt_image neighbour_inside_9
                        nicole.c "So did I!  I can't believe how lucky I am to have a neighbor like you!"
                        wt_image living_room.image
                        if nicole.event_count == 6:
                            "Nicole is still smiling as she heads home.  The next time you get her alone, you should be able to convince her to go further towards pleasing you."
                        else:
                            "Nicole is still smiling as she heads home.  She may not recall what you talked about, but she knows she had a great time.  She'll be back."
                        $ nicole.hypno_session() # deletes energy and records she was hypnotized
                    "Engage in idle chit chat" if not player.has_tag('supersexy'):
                        wt_image neighbour_inside_3
                        "You don't feel like hypnotizing Nicole today.  The two of you talk about the weather and share some neighborhood gossip for a while, then she  heads home.  She'll be back."
                        wt_image living_room.image
                    "Tell her to stop bothering you" if not player.has_tag('supersexy'):
                        player.c "You need to stop bothering me like this."
                        wt_image neighbour_inside_3
                        nicole.c "What do you mean?"
                        player.c "You dropping by the house like this every Tuesday.  It's getting annoying."
                        wt_image neighbour_inside_6
                        nicole.c "Fine.  I'll be going."
                        wt_image living_room.image
                        "She storms out.  You shouldn't have to worry about her dropping by again."
                        $ nicole.event_count = 0
                        # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
                        # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
                        # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
                        # call convert(nicole, "unavailable") ## not needed as setting event to 0 stops contact with her
                    "Tell her only with her husband's consent" if player.has_tag('supersexy'):
                        player.c "Nicole, this isn't right.  Not without Greg's knowledge and consent."
                        if nicole.revealed_to_neighbour > 0:
                            wt_image neighbour_inside_3
                            nicole.c "Not without Greg's consent? What do you mean, like as if I was one of your clients? I'm not paying you to have sex with me, if that's what you mean?"
                            player.c "No, that's not what I mean.  Tell me, Nicole.  Honestly.  Why are you here?"
                            nicole.c "I'm ... I'm not sure.  Maybe I thought I was going to seduce you."
                            nicole.c "Which is ridiculous, because you have so many women who want to sleep with you, you only bother with the ones who can afford to pay ... you even make their husbands pay you for the privilege."
                            player.c "They don't pay me for the privilege of sleeping with me. They pay me to solve problems with their relationship. And yes, usually I sleep with them, too. And their husband knows. And he's okay with it."
                            player.c "Tell me, Nicole.  Have you and Greg talked about me?  What does he think about what I do?"
                            nicole.c "He thinks you have the best gig ever. He even asked me if I could imagine him sending me to be with a man like you."
                            player.c "And how did you respond?"
                            nicole.c "I didn't. I laughed at him and changed the subject."
                            player.c "So why are you here now?"
                            wt_image neighbour_inside_10
                            nicole.c "Because I'm attracted to you. Because I would love to sleep with you. But I don't want to leave Greg. I love him. And things are good between us. Great even!  But ... "
                            wt_image neighbour_inside_3
                            nicole.c "The sex with Greg is great, but I still think about other men. And I'm sure Greg thinks about other women, I'm not stupid. He practically drooled talking about what you do."
                            player.c "Then why don't you talk to him? Tell him what you want, honestly. And ask him what he wants. And decide what you want to do, together, as a couple."
                            "Nicole nods."
                            nicole.c "Okay. I will. But whatever we decide, we can't afford to pay you. We're barely making ends meet now."
                            player.c "Perhaps we can come to an arrangement. There are times when I could use some assistance ... a woman's assistance in particular."
                            nicole.c "You want me to be your assistant?"
                            player.c "I was thinking more of a teaching aide, if you get my meaning."
                            wt_image neighbour_inside_10
                            nicole.c "Oooh ... I like the sound of that!"
                            wt_image neighbour_inside_9
                            "Nicole stands, gives you a quick hug, and practically skips out of your house. You wonder how her conversation with Greg will go."
                            $ nicole.event_count = 8
                            wt_image living_room.image
                        else:
                            wt_image neighbour_inside_6
                            nicole.c "What are you talking about? Did you think I was here for ... Whoa! Get over yourself."
                            wt_image neighbour_inside_8
                            nicole.c "I'm not sure why you think I'm here, but obviously, this was a mistake. I'm not the sort of woman who would cheat on her husband."
                            wt_image living_room.image
                            "Nicole slams your door on the way out.  Rejection is often painful."
                            $ nicole.event_count = 0
                            # WARNING: be very careful with the convert(p, 'unavailable') command, as it deletes all tags from the character and deletes all character name actions before setting status to 'unavailable'
                            # it also runs the equivalent of unconvert on all standard tracked states such as 'slavegirl', 'girlfriend', 'whore', but if she had a different state safest to run unconvert on it first to make sure the _count on that state is calculated correctly
                            # if she can every come back, may be better to use $ p.status = 'unavailable' instead of convert('unavailable')
                            call convert(nicole, "unavailable") from _call_convert_118
                    "Kiss her" if player.has_tag('supersexy'):
                        $ nicole.event_count = 7
                        wt_image neighbour_kiss_1
                        "You reach for Nicole and pull her close. Her eyes close and her hands caress you. As you kiss, she slides your shirt off without breaking the embrace."
                        wt_image neighbour_bj_1
                        "After a few minutes she pulls away from your kiss and sinks to her knees. Removing your pants, she takes you into her mouth."
                        wt_image neighbour_bj_2
                        "You're not sure who's enjoying this more. You let her continue until you see her hips start to squirm ..."
                        wt_image neighbour_sex_1
                        "... then you pull her up onto the bed ..."
                        nicole.c "oooo"
                        wt_image neighbour_sex_2
                        "... push yourself into her ..."
                        nicole.c "OHH!!"
                        wt_image neighbour_sex_3
                        "... and fuck her until she cums, her tight pussy squeezing your cock as her orgasm sweeps over her."
                        nicole.c "Ohhh ... Oohhhhh ...  OOOOHHHH!!"
                        "Now its your turn."
                        $ title = "Where do you want to cum?"
                        menu:
                            "Ass":
                                wt_image neighbour_shower_16
                                "Her tight pussy feels nice, but it's her even tighter other hole that has your interest."
                                wt_image neighbour_anal_4
                                "She trembles as you position the head of your cock against her butt hole, but doesn't object."
                                wt_image neighbour_anal_17
                                "It takes a bit of patience and a lot of lube ..."
                                wt_image neighbour_anal_5
                                "... but eventually you work your way past her sphincter and fully penetrate her butt."
                                nicole.c "oooooo"
                                wt_image neighbour_anal_6
                                "After that, it only takes a few minutes of fucking your neighbor's cute, tight ass to the sounds of her moans before you're ready to cum."
                                nicole.c "oooooo"
                                wt_image neighbour_anal_2
                                $ nicole.anal_count += 1
                            "Mouth":
                                wt_image neighbour_hypno_outfit_1_6
                                "Nicole scrambles around to get her mouth back on your cock."
                                wt_image neighbour_bj_1
                                "A moment later, she's gulping down your hot cum."
                                $ nicole.blowjob_count += 1
                                $ nicole.swallow_count += 1
                            "Pussy":
                                wt_image neighbour_sex_7
                                "You re-position Nicole on top of you ..."
                                wt_image neighbour_sex_4
                                "... then turn her around and enjoy the view as she happily rides your cock."
                                wt_image neighbour_sex_5
                                $ nicole.sex_count += 1
                        player.c "[player.orgasm_text]"
                        orgasm notify
                        wt_image neighbour_inside_7
                        "Nicole gives you a quick kiss, then dresses, grinning like a schoolgirl after her first kiss."
                        nicole.c "That was great!  I'll see you around ... lover!"
                        "This is not going to end well."
                        $ player.desire_action_count += 1
                        $ nicole.orgasm_count += 1
                        wt_image living_room.image
                add tags 'no_hypnosis' to nicole
                call character_location_return(nicole) from _call_character_location_return_125
            else:
                $ nicole.event_count = 6
        # Sixth event: 2nd email to profile and continuing hypno
        elif nicole.event_count == 6:
            # email about you if revealed Rep 1 or better
            if nicole.revealed_to_neighbour > 1 and player.satisfied_client_count >= 1:
                $ nicole.event_count = 0
                "You received a new message today."
                $ nicole.message_two_available = True
            # remind that she's available if continuing hypno
            elif nicole.hypnosis_visits_post_dildo:
                wt_image neighbour_outside_2
                "You see your neighbor, Nicole, taking a walk this morning. She seems to be alone today. You could summon her for a hypno session, if you want."
                wt_image living_room.image
                add tags 'available_today' to nicole
            # delay non hypno if not yet Rep 1
            elif nicole.revealed_to_neighbour > 1 and player.satisfied_client_count < 1:
                wt_image neighbour_outside_2
                "You see your neighbor, Nicole, taking a walk this morning. She smiles at you then continues on her way."
                wt_image living_room.image
        # Seventh event: shower scene
        elif nicole.event_count == 7:
            wt_image phone_1
            "Your phone is ringing."
            wt_image neighbour_cuffs_1
            nicole.c "Hi, its me. Nicole. Can you come over right away? There's a problem in our bathroom and Greg's not home."
            call forced_movement(nicole_house) from _call_forced_movement_314
            wt_image neighbours_door
            "Their front door is unlocked, so you go in."
            summon nicole to nicole_house
            wt_image neighbour_shower_1
            "You find Nicole in her shower, waiting for you."
            nicole.c "Oh, there you are! There's a problem with the water."
            wt_image neighbour_shower_2
            nicole.c "It turns on okay ..."
            wt_image neighbour_shower_10
            nicole.c "... and it seems like it's getting me clean."
            wt_image neighbour_shower_7
            nicole.c "Most of me, anyway."
            wt_image neighbour_shower_3
            nicole.c "But no matter how much water I use down here ..."
            wt_image neighbour_shower_9
            nicole.c "... I stay hot and sticky."
            wt_image neighbour_shower_3
            nicole.c "Do you think you can help with my problem?"
            $ title = "What do you do?"
            menu:
                "Tell her to rinse more vigorously":
                    player.c "I see the problem. You're not using the water the right way. Aim it at your nipple."
                    wt_image neighbour_shower_8
                    nicole.c "Okay ... mmmmm, that feels tingly."
                    player.c "You're holding the water too far away.  Move it closer."
                    wt_image neighbour_shower_11
                    nicole.c "oohhh"
                    player.c "Now do the same where you're sticky."
                    wt_image neighbour_shower_4
                    nicole.c "ooohhhh"
                    "The stream of water gets her close ..."
                    wt_image neighbour_shower_12
                    "... a few strokes of her finger quickly finishes the job."
                    nicole.c "OOHHH!!"
                    wt_image neighbour_shower_13
                    nicole.c "My plumbings available anytime you want to use it, lover. There's no one I'd rather have probing my pipes."
                    "This is so going to end badly."
                    $ nicole.masturbation_count += 1
                    $ nicole.orgasm_count += 1
                    $ nicole.event_count = 9
                    change player energy by -energy_very_short notify
                "Help her with her plumbing":
                    wt_image neighbour_shower_5
                    "She gives you a closer look at her problem ..."
                    wt_image neighbour_shower_14
                    "... then she turns over to give you room to work."
                    wt_image neighbour_shower_15
                    "You apply the right tool for the job ..."
                    nicole.c "ooohhhh"
                    wt_image neighbour_shower_16
                    "... and plunge her piping until it's flowing properly."
                    nicole.c "OOHHH!!"
                    wt_image neighbour_shower_6
                    "She finds a suitable way to thank you."
                    player.c "[player.orgasm_text]"
                    nicole.c "Thanks for fixing my plumbing problem, lover.  I'll be around to clean your pipe again soon."
                    "This is so going to end badly."
                    $ nicole.sex_count += 1
                    $ nicole.orgasm_count += 1
                    $ nicole.event_count = 9
                    orgasm notify
                "Leave before this goes any further":
                    "She's throwing herself at you in the shower she shares with her husband. Time to cut this off now, before someone gets hurt."
                    wt_image neighbour_shower_8
                    "Nicole's not be happy at the rejection, but its for her own good."
                    $ nicole.event_count = 0
            wt_image living_room.image
            call character_location_return(nicole) from _call_character_location_return_126
            call forced_movement(living_room) from _call_forced_movement_315
        # Eighth event: Greg consents
        elif nicole.event_count == 8:
            wt_image front_door
            "In the morning there's a knock at your door."
            wt_image neighbour_husband_1
            "It's your neighbor, Greg."
            nicole_husband "Hi! Nicole and I have been talking. She says she wants to set up an arrangement with you."
            nicole_husband "What she means is she wants to sleep with you. And I guess help you with your clients if you need her."
            nicole_husband "I want you to know I'm cool with all that. We've talked it out. In return, she's okay with me sleeping with other women, as long as I let her know, and there's no running around behind each other's back."
            nicole_husband "So, like, have fun! She's a great gal, with a great body. I'm incredibly lucky to have her as my wife. I hope you know how lucky you are to get to spend time with her now."
            wt_image living_room.image
            "You can now call on your neighbor Nicole once per week. After her first visit, she'll be available to help out in client sessions when you need a teaching aide."
            $ nicole.event_count = 0
            $ nicole.teaching_aide_training_available = True
            $ nicole.neighbour_arrangement = True
            add tags 'available_today' to nicole
        # Ninth event: morning visit
        elif nicole.event_count == 9:
            # implemented in early am visits
            pass
        # Tenth event: Nicole ends it
        elif nicole.event_count == 10:
            if nicole.has_tag('event_9_today'):
                rem tags 'event_9_today' from nicole #this is because early am events fire before regular start day events, keeps both 9 and 10 from happening same day
            else:
                wt_image phone_1
                "Your phone is ringing."
                wt_image neighbour_face_3
                "A distraught Nicole is on the other end of the line."
                nicole.c "It's me. He found out. Greg found out. I'm not sure how ... I don't know if it was something I said or something he saw ... oh god, he's so upset!"
                nicole.c "This was such a mistake. I was such an idiot. I can't see you again. I have to try and save my marriage."
                wt_image living_room.image
                "Sobbing, Nicole hangs up the phone."
                $ nicole.event_count = 11
        # Eleventh event: Moving van
        elif nicole.event_count == 11:
            # implemented in early am visits
            pass
        else:
            pass
    # check for Nicole buttplug visit event
    if day == 2 and nicole.event_count == 0 and nicole.has_tag('available_today') and nicole.anal_count > 4 and week > nicole.buttplug_visit_week and nicole.buttplug_visits_allowed and not nicole.has_tag('slavegirl'):
        wt_image front_door
        "In the morning there's a knock at your door."
        summon nicole
        wt_image neighbour_outfit_4_1
        "It's your neighbour, dressed rather slutty."
        wt_image neighbour_outfit_4_9
        nicole.c "I have a problem."
        if nicole.buttplug_visits_first_complete:
            wt_image neighbour_outfit_4_10
            player.c "Let me guess. Butt plug issues?"
            nicole.c "Uh huh"
            wt_image neighbour_outfit_4_3
        else:
            $ nicole.buttplug_visits_first_complete = True
            player.c "Not from this angle you don't."
            wt_image neighbour_outfit_4_10
            nicole.c "Thanks, but I can show you more easily once I get these pants off."
            wt_image neighbour_outfit_4_2
            "She removes everything but her panties and positions herself over your chair."
            player.c "I'm still not seeing a problem."
            wt_image neighbour_outfit_4_3
            nicole.c "The problem is this butt plug I bought. It doesn't feel as good as your hard cock does."
        if nicole.beg_count > 0:
            $ nicole.beg_count += 1
            nicole.c "Please take the plug out of my ass and replace it with your hard cock. I want to feel your big cock stretching my ass. I'm desperate to feel it inside. Please, I'm begging you to fuck my ass."
        else:
            nicole.c "Would you do me a favour? Would you mind taking this plug out of my ass, and replace it with your hard cock?"
        $ title = "What do you do?"
        menu:
            "Tell her not today":
                player.c "Not today, Nicole  I'm busy."
                nicole.c "Seriously?"
                wt_image neighbour_outfit_4_8
                nicole.c "Maybe I need you to train me on my seduction skills?"
            "Tell her not to bother you like this again":
                player.c "That's not how this works, Nicole. You come over when I invite you, not otherwise."
                nicole.c "So you get to call me when you want sex, but I don't get to let you know when I want sex?"
                player.c "Exactly"
                wt_image neighbour_outfit_4_9
                nicole.c "It's tough on the self esteem when you throw yourself at someone and they reject you."
                player.c "You'll survive."
                $ nicole.buttplug_visits_allowed = False
            "Fuck her ass":
                wt_image neighbour_outfit_4_4
                "The toy exits her tight ass with a little *pop*."
                wt_image neighbour_anal_17
                "Wearing the plug has stretched her ass enough that with a little lube you're able to enter her easily."
                nicole.c "ooohhh"
                wt_image neighbour_outfit_4_11
                "She reaches a hand between her legs and strokes her clit, clearly excited by the feeling of you inside her."
                wt_image neighbour_outfit_4_5
                "She soon cums with your cock deep in her ass."
                nicole.c "OOHHH!!"
                wt_image neighbour_outfit_4_12
                "The twitching of her body as she orgasms brings you over the edge too, and you release your hot seed inside her."
                player.c "[player.orgasm_text]"
                wt_image neighbour_outfit_4_8
                nicole.c "Mmmm ... thanks for helping me out!  Hope I see you again soon!"
                $ nicole.anal_count += 1
                $ nicole.orgasm_count += 1
                orgasm notify
        $ nicole.buttplug_visit_week = week + renpy.random.randint(4,8)
        wt_image living_room.image
        call character_location_return(nicole) from _call_character_location_return_127
    return

# End Day
label nicole_end_day:
    $ nicole.dinner_invite_open = False
    if player.has_item(nicole_bottle_of_wine):
        rem 1 nicole_bottle_of_wine from player
    if nicole.has_tag('available_today'):
        rem tags 'available_today' from nicole
    if nicole.has_tag('on_stage_now'):
        rem tags 'on_stage_now' 'watched_today' from nicole

    if nicole.has_tag('slavegirl'):
        rem tags 'artwork_now' from nicole
        $ nicole.change_image('neighbour_slavegirl')
    call character_location_return(nicole) from _call_character_location_return_128
    return

# End Week
label nicole_end_week:
    pass
    return

## Club and Stage Labels
label nicole_stage_notice:
    "This would be the perfect place for your neighbor Nicole to take her clothes off. You'll make arrangements when you get home."
    $ nicole.dancing_at_club = True
    return

label nicole_stage_call:
    # this runs when has tag 'showgirl' and you visit the Club
    if player.has_tag('stage_visited_today'):
        pass # as doesn't get dismissed from Club when you leave it, only at end of day
    else:
        $ nicole.location = stage
        add tags 'on_stage_now' to nicole
    return

label nicole_stage_send_home:
    call character_location_return(nicole) from _call_character_location_return_129
    return

## Lawyer Content
label nicole_janice_talk_option:
    if nicole.has_tag('likes_girls') and not janice.has_tag('discuss_neighbor_lesbian') and janice.has_tag('asked_about_hiring'):
        "You discuss Nicole's newfound interest in other women with Janice."
        janice.c "Sorry. She doesn't sound like my type. Get back to me when you've found someone blonder."
        player.c "That's a strangely specific compulsion you have, you know?"
        add tags 'discuss_neighbor_lesbian' to janice
        $ janice.temporary_count = 0
    return

## Marilyn Content
label nicole_marilyn_talk_option:
    if nicole.has_tag('likes_girls') and not marilyn.has_tag('discuss_neighbor_lesbian'):
        "You discuss Nicole's newfound interest in other women with Marilyn."
        marilyn.c "She sounds cute, but I've had more brunettes than I care to think about recently.  Let me know when you've found someone fairer."
        add tags 'discuss_neighbor_lesbian' to marilyn
    return

## Frigid Content:
label nicole_elsa_ta_blowjob:
  $ elsa.used_neighbour_ta += 2
  wt_image neighbour_teach_strip_9
  "You invite Nicole to join you."
  player.c "Nicole, I'd like you to show Elsa how to give a blowjob."
  wt_image neighbour_teach_strip_2
  "Your neighbor smiles, happy to comply.  She turns to Elsa and starts stripping."
  nicole.c "First, you should make yourself comfortable.  I prefer to be nude, but you should do what feels right to you."
  wt_image neighbour_teach_bj_1
  "Nicole kneels down in front of you and takes out your cock.  Her attention, however, is on Elsa."
  nicole.c "You can use your hand to get him hard first, if you want.  Just seeing you kneel in front of him will likely have him hard in no time."
  wt_image neighbour_teach_bj_4
  nicole.c "You don't have to take him deep into your mouth.  That can come in time, as you get more comfortable with the feeling."
  wt_image neighbour_teach_bj_2
  nicole.c "For starters, you can just put the tip in your mouth and suck gently.  Use your tongue on the underside of the head of his cock, its a very sensitive area.  You can use your hand to stroke the rest of his cock."
  wt_image neighbour_teach_bj_3
  nicole.c "Be sure to make eye contact with him while you're sucking him.  That gets a man off every time!  Plus, when you see his face and see how excited you're making him, it's a huge turn on.  It never fails to get me wet."
  wt_image neighbour_teach_bj_5
  nicole.c "When he's ready to cum, don't panic."
  wt_image neighbour_teach_bj_6
  if nicole.facial_count > 1:
    nicole.c "My husband Greg likes to cum on my face and I've learned that can be pretty hot, but if you're uncomfortable with that you can just let him cum in your mouth or do what I used to do and keep your lips open so he can watch as he cums in your mouth."
    wt_image neighbour_teach_bj_7
    nicole.c "I'm going to take this load on my face, though, to show it's nothing to be scared of.  Play around with him and you'll soon find out what turns him, and you, on most."
    player.c "[player.orgasm_text]"
    wt_image neighbour_teach_bj_9
    $ nicole.facial_count += 1
  else:
    nicole.c "My husband Greg would like to cum on my face, but that seems weird so I just keep my lips open and let him watch as he cums in my mouth, then let a little dribble out over my lips."
    wt_image neighbour_teach_bj_7
    player.c "[player.orgasm_text]"
    wt_image neighbour_teach_bj_8
    $ nicole.swallow_count += 1
  nicole.c "I've taken his edge off, now it's your turn to practice.  You should be able to take your time and go slow, as it'll be a little while before he's ready to cum again."
  $ nicole.blowjob_count += 1
  orgasm
  add tags 'watched_teaching_aide_blowjob' to elsa
  return

label nicole_elsa_ta_blowjob_first_comment:
    nicole.c "Ummm, maybe go a little slower to start?  You might gag if you try to fit him all inside your mouth at once.  Try licking him first."
    return

label nicole_elsa_ta_blowjob_second_comment:
    nicole.c "I hope so.  Being able to pleasure your guy with your mouth is fun, once you get used to it.  I'd hate for you to miss out on that, or for him to."
    return

label nicole_elsa_ta_blowjob_third_comment:
    nicole.c "When you're ready, you can put him back in your mouth.  Start with just the tip, at first, then you can go deeper once that feels okay to you."
    return

label nicole_elsa_ta_blowjob_end:
    nicole.c "I thought you did amazing!  It even turned me on."
    wt_image frigid_hypnotized_desire_1_3
    elsa.c "Thanks, Nicole.  I appreciate you teaching me how to do that!  It felt nice to finally be able to do that for a guy."
    player.c "Don't I get to comment on how she did?"
    nicole.c "How quickly you came after I'd already blown you was comment enough, I think."
    return

label nicole_elsa_ta_strip:
    if current_target.has_tag('teaching_aide'):
        wt_image neighbour_teach_strip_9
        "You invite Nicole to join you."
        player.c "Nicole, I'd like you to show Elsa how you take your clothes off."
        wt_image neighbour_teach_strip_1
        "Your neighbor smiles.  As you put some music on for her, she begins to dance a little dance while watching Elsa."
        nicole.c "Teasing your guy with your body can be a lot of fun.  Imagine you're in a dance club and just start swaying to the music."
        wt_image neighbour_teach_strip_10
        nicole.c "You'll have his attention pretty much right away."
        wt_image neighbour_teach_strip_6
        nicole.c "Especially when you start playing with your clothes."
        wt_image neighbour_teach_strip_2
        nicole.c "Take your time removing them ..."
        wt_image neighbour_teach_strip_11
        nicole.c "... and don't stop dancing as you do."
        wt_image neighbour_teach_strip_12
        nicole.c "You're not just getting naked for him ..."
        wt_image neighbour_teach_strip_13
        nicole.c "... you're getting him ready."
        wt_image neighbour_teach_strip_14
        nicole.c "And if you're like me, watching the lust in his eyes as you become more and more naked for him ..."
        if nicole.strip_count > 2:
            wt_image neighbour_teach_strip_5
            nicole.c "... will have you ready for him, too."
            wt_image neighbour_teach_strip_8
            nicole.c "Your turn now, sweetie.  I know you can do this.  You don't have to be as bold as me.  Just do what you're comfortable with.  You're sexy and beautiful.  Show us how beautiful and sexy you can be, and feel it yourself, inside."
            add tags 'ta_strip_bold' to elsa
        else:
            wt_image neighbour_teach_strip_8
            nicole.c "... will be fun for you, too."
            "You would have liked Nicole to be a little bolder, but Elsa was fascinated by the show anyway."
            nicole.c "Your turn now, sweetie.  I know you can do this.  Just do what you're comfortable with.  You're sexy and beautiful.  Show us how beautiful and sexy you can be, and feel it yourself, inside."
        add tags 'watched_teaching_aide_strip_nicole' 'watched_teaching_aide_strip' to elsa
    else:
        $ current_target = None
    return

label nicole_elsa_ta_strip_end:
    wt_image neighbour_teach_strip_8
    nicole.c "I thought you were great!  I think I'm a little turned on now, too."
    elsa.c "Thanks, Nicole!  I really appreciate you teaching me."
    return


## Good Girlfriend Content
label nicole_terri_ta_blowjob:
    if current_target.has_tag('teaching_aide'):
        wt_image neighbour_teach_strip_9
        "You invite Nicole to join you."
        player.c "Nicole, Terri is trying to learn how to be a better girlfriend for her boyfriend. I'd like you to show Terri how to give a proper blow job."
        wt_image neighbour_teach_strip_2
        "Your neighbor smiles, happy to comply. She turns to Terri and starts stripping."
        nicole.c "First, you should make yourself comfortable. I prefer to be nude, but you should do what feels right to you."
        wt_image neighbour_teach_bj_1
        "Nicole kneels down in front of you and takes out your cock. Her attention, however, is on Terri."
        nicole.c "You can use your hand to get him hard first, if you want. Just seeing you kneel in front of him will likely have him hard in no time."
        wt_image neighbour_teach_bj_4
        nicole.c "You don't have to take him deep into your mouth. That can come in time, as you get more comfortable with the feeling."
        wt_image neighbour_teach_bj_2
        nicole.c "For starters, you can just put the tip in your mouth and suck gently. Use your tongue on the underside of the head of his cock, its a very sensitive area.  You can use your hand to stroke the rest of his cock."
        wt_image neighbour_teach_bj_3
        nicole.c "Be sure to make eye contact with him while you're sucking him. That gets a man off every time! Plus, when you see his face and see how excited you are making him, it's a huge turn on. It never fails to get me wet."
        wt_image neighbour_teach_bj_5
        nicole.c "When he's ready to cum, don't panic.  It tastes great, and it feels great on your skin too."
        wt_image neighbour_teach_bj_6
        nicole.c "Take as much in your mouth as you're comfortable with, or let it spill out, it doesn't matter."
        if nicole.facial_count > 1:
            wt_image neighbour_teach_bj_7
            nicole.c "Or just let him shoot all over your face.  You'd be amazed at how hot that feels.  Play around with him and you'll soon find out what turns him, and you, on most."
            wt_image neighbour_teach_bj_9
            $ nicole.facial_count += 1
        else:
            wt_image neighbour_teach_bj_8
            $ nicole.swallow_count += 1
        player.c "[player.orgasm_text]"
        nicole.c "Now, I've taken his edge off. It's your turn to practice. You should be able to take your time and go slow, as it'll be a little while before he's ready to cum again."
        $ nicole.blowjob_count += 1
        orgasm
        add tags 'watched_teaching_aide_blowjob' to terri
    else:
        $ current_target = None
    return

label nicole_terri_ta_strip:
    if current_target.has_tag('teaching_aide'):
        wt_image neighbour_teach_strip_9
        "You invite Nicole to join you."
        player.c "Nicole, Terri is trying to learn how to be a better girlfriend for her boyfriend. Could you please show Terri how you take your clothes off when you're trying to excite a man?"
        wt_image neighbour_teach_strip_1
        "Your neighbor smiles.  As you put some music on for her, she begins to dance a little dance while watching Terri, whose cheeks are blushing furiously."
        nicole.c "Teasing your guy with your body can be a lot of fun.  Imagine you're in a dance club and just start swaying to the music."
        wt_image neighbour_teach_strip_10
        nicole.c "You'll have his attention pretty much right away."
        wt_image neighbour_teach_strip_6
        nicole.c "Especially when you start playing with your clothes."
        wt_image neighbour_teach_strip_2
        nicole.c "Take your time removing them ..."
        wt_image neighbour_teach_strip_11
        nicole.c "... and don't stop dancing as you do."
        wt_image neighbour_teach_strip_12
        nicole.c "You're not just getting naked for him ..."
        wt_image neighbour_teach_strip_13
        nicole.c "... you're getting him ready."
        wt_image neighbour_teach_strip_14
        nicole.c "And if you're like me, watching the lust in his eyes as you become more and more naked for him ..."
        if nicole.strip_count > 2:
            wt_image neighbour_teach_strip_5
            nicole.c "... will have you ready for him, too."
            "You enjoy Nicole's finale, but Terri's turned so red, you're afraid she may catch fire. Perhaps it's embarrassment at witnessing Nicole's display, or perhaps it's something else?"
            wt_image neighbour_teach_strip_8
            nicole.c "Your turn now, sweetie.  I know you can do this.  You don't have to be as bold as me.  Just do what you're comfortable with.  You're sexy and beautiful.  Show us how beautiful and sexy you can be, and feel it yourself, inside."
            add tags 'ta_strip_bold' to terri
        else:
            wt_image neighbour_teach_strip_8
            nicole.c "... will be fun for you, too."
            "You would have liked Nicole to be a little bolder, but Terri seemed to find the experience intense regardless. She's turned so red, you're afraid she may catch fire. Perhaps it's embarrassment at witnessing Nicole's display, or perhaps it's something else?"
            nicole.c "Your turn now, sweetie.  I know you can do this.  Just do what you're comfortable with.  You're sexy and beautiful.  Show us how beautiful and sexy you can be, and feel it yourself, inside."
        "Terri takes a deep breath as Nicole settles in beside you to watch the show."
        add tags 'watched_teaching_aide_strip_nicole' 'watched_teaching_aide_strip' to terri
    else:
        $ current_target = None
    return

## Loving Wife Content
label nicole_sarah_positive_role_talk_teaching_aide:
    if current_target.has_tag('teaching_aide') and not sarah.has_tag(tag_expression):
        wt_image neighbour_inside_9
        "Nicole comes right over."
        wt_image lw_visit_2_2
        if current_target.has_tag('sarah_positive_role_sex_done'):
            player.c "Nicole, you remember Sarah."
            sarah.c "Hi!"
            nicole.c "Hi again!"
            wt_image neighbour_inside_3
            player.c "I thought you could tell Sarah about how your relationship with your husband has been since you started having sex with me."
        else:
            player.c "Nicole, this is Sarah."
            sarah.c "Hi!  Nice to meet you."
            nicole.c "Nice to meet you, too!"
            wt_image neighbour_inside_3
            player.c "Sarah's husband wants her to have sex with his friends.  I thought you could tell her about how your relationship with your husband has been since you started having sex with me."
        wt_image lw_visit_2_11
        sarah.c "Your husband doesn't think you're a ... you know, slut?"
        wt_image neighbour_inside_3
        nicole.c "Oh, no!  He's totally fine with it.  He knows it's just sex.  And he likes that I let him sleep with other women, too."
        wt_image lw_visit_2_12
        sarah.c "Doesn't that worry you?  I mean, what if he finds someone he wants to be with more than you?"
        wt_image neighbour_inside_3
        nicole.c "Couldn't that happen anyway?  I figure, anything that makes the two of us happier makes our marriage stronger. It's not like Greg couldn't find someone to sleep with behind my back, if he wanted to.  He's a good looking guy."
        wt_image lw_visit_2_12
        sarah.c "I guess you're right.  Mine is, too."
        wt_image neighbour_inside_3
        "The two of them fall into a long conversation about their husbands, their marriages, and Greg's feelings towards Nicole since she started sleeping with you."
        wt_image lw_visit_2_4
        "Eventually, it gets late, and Nicole leaves."
        sarah.c "Thanks for asking Nicole to chat with me.  It helped a lot."
        add tags 'met_teaching_aide_nicole' 'positive_teaching_aide_resolution_today' to sarah
    else:
        $ current_target = None
    return

label nicole_sarah_positive_role_talk_slavegirl:
    if current_target.has_tag('slavegirl') and not sarah.has_tag(tag_expression):
        wt_image neighbour_slavegirl_9
        "You order [nicole.full_name] to join you."
        nicole.c "Yes, [nicole.your_name]?"
        wt_image lw_visit_2_2
        player.c "[nicole.name], I'd like you to meet Sarah."
        sarah.c "Hi.  Wouldn't you be more comfortable on a chair?"
        wt_image neighbour_slavegirl_9
        player.c "She can talk perfectly well from her knees.  [nicole.name], Sarah's husband wants her to have sex with his friends.  She has concerns.  I thought speaking to another woman could help her."
        nicole.c "I'll try, [nicole.your_name]."
        add tags 'met_slavegirl_nicole' 'positive_transformed_slavegirl_resolution_today' to sarah
        ## remainder of transformed_slavegirl content is back in Sarah's script
    else:
        $ current_target = None
    return

label nicole_sarah_positive_role_sex_teaching_aide:
    if current_target.has_tag('teaching_aide'):
        wt_image neighbour_outfit_4_1
        if not current_target.has_tag('sarah_positive_role_talk_done'):
            player.c "Sarah, this is my friend Nicole."
            wt_image lw_visit_4_8
            sarah.c "Hi"
            nicole.c "Hi!"
        else:
            player.c "You remember Nicole?"
            wt_image lw_visit_4_8
            sarah.c "Of course!"
            nicole.c "Hi again!"
        wt_image neighbour_outfit_4_1
        player.c "Nicole and I are going to have sex together while you watch."
        wt_image lw_visit_4_2
        sarah.c "You can't be serious?"
        wt_image lw_visit_4_3
        player.c "I am.  You've never watched two people make love.  Now you will.  It'll give you a chance to see that sex doesn't have to be private to be fun.  Have a seat and make yourself comfortable."
        wt_image neighbour_teach_sex_1
        "Nicole slips out of her clothes and snuggles up to you while Sarah watches.  She wastes no time freeing your cock."
        wt_image lw_visit_4_6
        sarah.c "Isn't this embarrassing, having me here watching?"
        wt_image neighbour_teach_sex_1
        nicole.c "Not at all.  It's hot, actually.  Look how hard his cock is.  It's such a thrill when you can get a guy excited so easily.  He wants it inside me, and I'm already wet enough that I want him inside me, too."
        wt_image neighbour_strip_practice_2_16
        "Nicole pulls off her panties and kneels in front of you."
        nicole.c "Go ahead.  Put it in me."
        wt_image neighbour_teach_sex_2
        nicole.c "oohhh! ... that feels so good!!  You can see, Sarah, that my body's not having any trouble responding with you here.  Neither is his."
        wt_image lw_visit_4_9
        sarah.c "Yes, I can see that."
        wt_image neighbour_teach_sex_3
        nicole.c "Do you want me to teach her how to pleasure you in this position?"
        player.c "Not in detail.  Today's lesson is that it can be fun to watch and be watched.  Just get the two of us off, Nicole, and I'm sure Sarah will pick up some pointers on the way."
        wt_image neighbour_teach_sex_6
        nicole.c "Okay"
        "Nicole rocks her hips back against you, twisting them side to side while gradually increasing the pace at which she thrusts backwards towards you."
        wt_image lw_visit_4_6
        "Sarah watches intently as Nicole's breathing and yours gets faster and faster as you near orgasm."
        sarah.c "Are you sure it's okay for me to be watching?"
        wt_image neighbour_teach_sex_6
        nicole.c "It's totally fine.  Just give me a moment."
        wt_image neighbour_teach_sex_7
        "Nicole closes her eyes and bucks her hips back hard against you, shuddering to an orgasm around your cock."
        wt_image neighbour_teach_sex_4
        nicole.c "Oooooohhh!!!"
        wt_image lw_visit_4_5
        sarah.c "You actually came?  Even with me here?"
        wt_image neighbour_teach_sex_3
        nicole.c "I did, but he hasn't yet.  Do you want to get him off?"
        wt_image lw_visit_4_4
        sarah.c "No!"
        wt_image neighbour_teach_sex_8
        nicole.c "Okay.  Is it alright if I do?"
        wt_image lw_visit_4_6
        sarah.c "I suppose."
        wt_image neighbour_teach_sex_9
        player.c "[player.orgasm_text]"
        wt_image neighbour_teach_sex_5
        nicole.c "There.  See?  You being here didn't keep him from cumming, either."
        player.c "I think Nicole had fun, don't you?"
        wt_image lw_visit_4_5
        "Sarah nods."
        player.c "And she didn't look ridiculous having sex, did she?"
        wt_image lw_visit_4_9
        sarah.c "No.  Not at all.  You've made your point.  For some people, sex doesn't always have to be in private for it to be fun.  I need to go home and think about this."
        wt_image lw_visit_4_10
        "Sarah looks at you with a little more interest than she has before.  You can't help yourself from teasing her."
        player.c "You can take your panties off while you think about it, if you want."
        $ nicole.sex_count += 1
        $ nicole.orgasm_count += 1
        orgasm
        add tags 'met_teaching_aide_nicole_sex' 'watched_teaching_aide_this_weekend' to sarah
    else:
        $ current_target = None
    return

label nicole_sarah_positive_role_sex_slavegirl:
    if current_target.has_tag('slavegirl'):
        wt_image neighbour_lw_visit_8
        "You put your arm around [nicole.name] and bring her to the living room."
        player.c "Do you know why I let you wear this pretty dress today, [nicole.name]?"
        nicole.c "No, [nicole.your_name], but thank you, [nicole.your_name]."
        player.c "Because I want you to look nice while you help my friend Sarah. You remember Sarah?"
        nicole.c "Yes, [nicole.your_name]."
        player.c "You know Sarah's worried about having her husband watch her have sex. It's hard for her to imagine what that will be like, in part because she's never even seen two people have sex together. I'm going to fuck you in this pretty blue dress, [nicole.name], while Sarah watches us."
        nicole.c "Yes, [nicole.your_name]."
        wt_image lw_visit_4_2
        sarah.c "You can't be serious?"
        wt_image lw_visit_4_4
        player.c "I am.  You've never watched two people have sex.  Now you will.  It'll give you a chance to see that sex doesn't have to be private to be fun. Have a seat and make yourself comfortable."
        wt_image neighbour_strip_3_2
        player.c "Climb up here and kiss me, [nicole.name]."
        nicole.c "Yes, [nicole.your_name]."
        wt_image neighbour_strip_3_4
        "Taking her breast in your mouth, you bite down on it, hard, as she winces and groans."
        nicole.c "oohhh"
        wt_image lw_visit_4_4
        sarah.c "Maybe I should go? I don't want to be intruding on your personal time together."
        player.c "Nonsense. [nicole.name] doesn't mind you being here.  She's happy to service me anytime, regardless of whether anyone's watching.  Aren't you?"
        wt_image neighbour_strip_3_9
        nicole.c "Of course, [nicole.your_name].  [nicole.your_name] wants you to watch, Sarah, so I don't mind.  I'm happy with whatever [nicole.your_name] wants."
        wt_image neighbour_lw_visit_4
        player.c "What I want now, [nicole.name], is for you to be ready for my cock.  Wet my fingers."
        nicole.c "Yes, [nicole.your_name]."
        "She wraps her mouth around your fingers and gently sucks them while spreading her legs."
        wt_image neighbour_strip_3_10
        "She moistens quickly as you stroke your fingers into her."
        nicole.c "ooohhhh"
        wt_image neighbour_strip_3_8
        player.c "Get my cock ready to fuck you, girl."
        nicole.c "Yes, [nicole.your_name]."
        wt_image neighbour_lw_visit_6
        "[nicole.name] slides down to her knees and gently suckles your balls until you're fully erect."
        player.c "Good girl. Now ride my cock until I cum."
        nicole.c "Yes, [nicole.your_name]."
        wt_image neighbour_lw_visit_7
        "[nicole.full_name] rides your dick with enthusiasm.  She loves serving and pleasing you, and this manifests in a deep groan as she feels you cum inside her."
        player.c "[player.orgasm_text]"
        nicole.c "oooohhhhh"
        wt_image lw_visit_4_5
        sarah.c "You've made your point.  Men can enjoy sex even when it's not in private.  Some women, too, I guess ..."
        player.c "And did [nicole.full_name] look ridiculous while I was fucking her?"
        wt_image lw_visit_4_8
        sarah.c "No, not at all.  I mean, the whole submissive thing is kinda weird."
        player.c "You should try it sometime."
        wt_image lw_visit_4_7
        sarah.c "I think I'll just go home and maybe think about this some more, later."
        player.c "Sure.  Don't be afraid to ask your husband how you can serve him while you're thinking about it."
        $ nicole.sex_count += 1
        orgasm
        add tags 'watched_transformed_slavegirl_this_weekend' to sarah
    else:
        $ current_target = None
    return

## Trailer Trash Content
label nicole_becky_sue_fix_clothes_message:
    "Nicole has good taste in clothes and is a sex kitten at heart, but manages to come across as sweet and innocent. She'd likely direct Becky Sue towards something nice but modest."
    return

label nicole_becky_sue_fix_clothes_help:
    wt_image neighbour_shopping_1
    player.c "Nicole, Becky Sue needs some new clothes. Would you take her shopping and help her pick out something nice?"
    wt_image neighbour_hypno_outfit_2_2
    nicole.c "Girls shopping night!! This is going to be so much fun!  What type of clothes are you looking for?"
    "You interject before Becky Sue can reply."
    player.c "Help her find something she could wear in polite company, like a formal dinner or evening soirée."
    wt_image neighbour_outfit_1_4
    nicole.c "I know the perfect places! Come on, Becky Sue. Grab your purse and lets get going."
    nicole.c "Just don't tell Greg how much I spend today, okay? If you're getting some nice new clothes, I think I'll get some for myself, too."
    wt_image tt_fix_clothes_1
    "Nicole's an easy person to make friends with, and Becky Sue takes to her right away. She grabs her handbag and follows Nicole out the door."
    "Nicole has good taste, and her easy charm soon helps Becky Sue feel comfortable wearing the same type of clothes Nicole wears. In fact, Becky Sue enjoys her time shopping with her new friend enough that she'll be more open to future suggestions from you."
    "Becky Sue also picks up on Nicole's understated approach to sexuality. Her time spent with your neighbor reinforces in Becky Sue's mind the idea that her worth is not dependent on her body."
    $ becky_sue.slut_level -= 1
    change becky_sue sos by 15
    change becky_sue resistance by -10
    return

## Character Specific Timers
# Convert Character to Lesbian
label nicole_convert_lesbian:
    call convert(nicole, 'lesbian') from _call_convert_120
    add tags 'janice_talk_option_possible' 'marilyn_talk_option_possible' to nicole
    return

# Convert Character to Showgirl
label nicole_convert_showgirl:
    if player.has_tag('club_access') and player.has_tag('club_first_visit_complete'):
        $ nicole.training_regime = 'daily'
        call convert(nicole, "showgirl") from _call_convert_121
        $ nicole.dancing_at_club = True
    else:
        add tags 'waiting_for_club_access' to nicole
    return

# Convert Character to Slavegirl
label nicole_convert_slavegirl:
    $ nicole.training_regime = 'daily'
    call unconvert(nicole, "teaching_aide") from _call_unconvert_76
    call convert(nicole, "slavegirl") from _call_convert_122
    $ nicole.neighbour_arrangement = False
    $ nicole.teaching_aide_training_available = False
    $ nicole.change_image('neighbour_slavegirl')
    $ nicole.fixed_location = bedroom
    $ nicole.location = bedroom
    add tags 'neighbours_lost' to player
    rem tags 'follows' from nicole
    return

########### ROOMS ###########
# Nicole's House
label nh_examine:
    pass
    return

label nh_no_access:
  return

label nh_enter:
  return

label nh_exit:
  return

########### OTHER ###########
# Bonsai Labels
# NOTE:  consider modifying bonsai coding to make it more modder friendly re additional rooms to put it in
label bt_examine:
  "A gift from your neighbor, [nicole.name].{nw}"

  if 'radiant' in nicole_bonsai.tags:
    extend '\n\nThe tree is truly radiant, almost mesmerizing in its beauty, inspiring a mix of emotions and feelings in all who are near it.{nw}'

  else:
    if living_room.is_here and 'living_room' in nicole_bonsai.tags:
      extend'\n\nThe tree conveys a sense of trust, inspiring the viewer to relax and lower their defenses.{nw}'

    if boudoir.is_here and 'boudoir' in nicole_bonsai.tags:
      extend '\n\nThe tree conveys sexual energy, inspiring passion in the viewer.{nw}'

    if dungeon.is_here and 'dungeon' in nicole_bonsai.tags:
      extend '\n\nThe tree radiates authority, inspiring a sense of pleasurable submission in the viewer.{nw}'

    if bedroom.is_here and 'bedroom' in nicole_bonsai.tags:
      extend '\n\nThe tree looks like what it was always meant to be, inspiring the viewer to embrace their own sense of self.{nw}'

  extend ""
  wt_image current_location.image
  return

label bt_move_it:
  $ title = "Move the plant to another room?"
  $ new_location = renpy.display_menu([(l.name, l) for l in locations_in_area('house') if l != current_location and l.has_tag('bonsai_allowed')] + [("Back", False)])
  if new_location:
    give 1 nicole_bonsai from current_location to new_location notify
    "You think the bonsai would look better in the [new_location.name] and move it there."
    call forced_movement(new_location) from _call_forced_movement_316
  else:
    "You decide to leave the bonsai where it is."
  wt_image current_location.image
  return

label bt_tend_to:
  wt_image bt_image
  add tags 'tended_bonsai' to player # note: this is removed in bt's start day on day 1
  change player energy by 5 notify
  "Sculpting the bonsai tree with some judicious trimming is surprisingly soothing."

  if not 'radiant' in nicole_bonsai.tags:

    if living_room.is_here and 'living_room' not in nicole_bonsai.tags:
      if nicole_bonsai.step_stat('tended_at_living_room', 1, 5)[0]:
        $ nicole_bonsai.resistance_mod = 5
        add tags 'living_room' to nicole_bonsai

    elif boudoir.is_here and 'boudoir' not in nicole_bonsai.tags:
      if nicole_bonsai.step_stat('tended_at_boudoir', 1, 5)[0]:
        $ nicole_bonsai.desire_mod = 5
        add tags 'boudoir' to nicole_bonsai

    elif dungeon.is_here and 'dungeon' not in nicole_bonsai.tags:
      if nicole_bonsai.step_stat('tended_at_dungeon', 1, 5)[0]:
        $ nicole_bonsai.submission_mod = 5
        add tags 'dungeon' to nicole_bonsai

    elif bedroom.is_here and 'bedroom' not in nicole_bonsai.tags:
      if nicole_bonsai.step_stat('tended_at_bedroom', 1, 5)[0]:
        $ nicole_bonsai.sos_mod = 5
        add tags 'bedroom' to nicole_bonsai

    if nicole_bonsai.has_tags('living_room', 'boudoir', 'dungeon', 'bedroom'):
      add tags 'radiant' to nicole_bonsai
      $ nicole_bonsai.add_stats_with_value('desire_mod', 'submission_mod', 'sos_mod', 'resistance_mod', force = True)
      day_label rem from start bt_start_day

      python:
        for location in locations_in_area('house'):
          for stat in ['desire_mod', 'submission_mod', 'sos_mod']:
            location.stats[stat] += 5
          location.stats['resistance_mod'] -= 5
  wt_image current_location.image
  return

label bt_start_day:
  if day == 1:
    if basement.has_item(nicole_bonsai):
        if 'no_light' in nicole_bonsai.tags:
          add tags 'dead_bonsai' to basement
          rem 1 nicole_bonsai from basement no_message
        else:
          add tags 'no_light' to nicole_bonsai
    else:
      rem tags 'no_light' from nicole_bonsai
  return

label bt_throw_away:
    $ title = "Do you really want to get rid of your housewarming gift?"
    menu:
        "Yes, get rid of it":
            "This plant is cluttering up your house.  You decide to throw it away.{w=1.0}"
            extend "\n\n Shame on you\n           - DigitalBonsai"
            rem 1 nicole_bonsai from current_location notify
            python:
                if 'radiant' in nicole_bonsai.tags:
                    for location in locations_in_area('house'):
                        for stat in ['desire_mod', 'submission_mod', 'sos_mod']:
                            location.stats[stat] -= 5
                        location.stats['resistance_mod'] += 5
        "No, keep it":
            "It's such a soothing plant. Why would you get rid of it?"
    return

################################## TO DOS ##################################
# make bonsai tree coding more modder-friendly

################################### NOTES ###################################
## Minor Character Status
#0 = not yet prospect
#1 = prospect, .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = completed, .status = "post_training"
#4 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#5 = dead, rem tags 'continuing_actions' and .status = "post_training"
