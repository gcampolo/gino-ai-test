# Package Register
register_package king_tut name "King Tut" author "Tristimdorion" description "Enhanced Game Experience" dependencies core
register king_tut_init 10 in king_tut as "King Tut"

init 10 python:
    config.label_overrides["club_swingers_watch_girlfriend"] = "king_tut_club_swingers_watch_girlfriend"

    # disable default auto-save
    config.autosave_frequency = None
    config.autosave_on_choice = False
    config.autosave_on_quit = True

    global king_tut_current_version
    king_tut_current_version = "v0.25.1" # Release 0.7R

    # make sure we get the correct location for the auto_image file, if not found, use default image.
    def get_auto_image_location():
        for file in renpy.list_files():
            if "king_tut_" in file:
                return file.replace("idle", "%s")
        return "gui/button/wip_%s.png"

    # add new features to mod after initial release, remove when game version updates (incompatible saves)
    def update_mod():
        # if not has_mod_action("king_tut_retry_gloria"):
        #     living_room.add_action("Retry to impress Gloria", context = "king_tut", label = "king_tut_retry_gloria", order = 91, condition = "gloria.session == 3", unseen = False, seen_result = True)
        # if not has_mod_action("king_tut_retry_diamond"):
        #     living_room.add_action("Retry Diamond Training", context = "king_tut", label = "king_tut_retry_diamond", order = 92, condition = "diamond.training_result < 7 and master_m.current_message == 1", unseen = False, seen_result = True)
        # if not has_mod_action("king_tut_retry_fairyn"):

        #update_mod_condition("king_tut_jasmine_downtown", "not jasmine.status == 'unavailable' and jasmine.downtown_week > 0 and jasmine.has_tag('satisfied') and jasmine.downtown_countdown > 0")

        # update mod version number
        version_action = get_mod_action_by_order_number(999)
        if version_action:
            version_action.name = "{color=#0000aa}----- " + king_tut_current_version + " -----{/color}"

        player.add_tags('whores_once')  # some events are locked out when this is not set
        return

    def has_mod_action(label_name):
        for a in living_room.actions:
            if a.context == "king_tut" and a.label == label_name:
                return True
        return False

    def get_mod_action_by_order_number(number):
        for a in living_room.actions:
            if a.context == "king_tut" and a.order == number:
                return a
        return

    def update_mod_condition(label_name, new_condition):
        for a in living_room.actions:
            if a.context == "king_tut" and a.label == label_name:
                a.condition = new_condition
        return

    def set_client_maximum_results(client):
        if client.sos < 100:
            client.sos = 100
        if client.submission < 200:
            client.submission = 200
        if client.resistance > -50:
            client.resistance = -50

        if not client is chelsea:
            if client.desire < 100:
                client.desire = 100
            if client.sos * 2 > client.desire:
                client.desire = (client.sos * 2) + 10
        return

    def add_client_items(client, items):
        for item in items:
            if not client.has_item(item):
                client.add_item(item, with_message = False)
        return

    def set_client_optimal_end_state(client):
        global title
        client.clear_training_session()
        if not client.has_tag("love_potion_used"):
            client.add_tag("love_potion_used")  # this tags prevents many bad results in continuing actions
        if client is alexis:
            add_client_items(alexis, [chastity_belt, dildo, butt_plug])

            alexis.remove_tags('no_slavery')
            alexis.add_tags('accepts_domination', 'discussed_dildo')
            alexis.sex_skill_level = 6
            alexis.daisy_event = 2
            alexis.anal_training_count = 5
            alexis.boxing_complete = 1
        if client is becky_sue:
            title = "Training result?"
            becky_sue.tt_status = renpy.display_menu(items = [("Trashy Slut", 3), ("Trashy Virtuous", 4), ("Wholesome", 6), ("Wholesome Slut", 9), ("Wholesome Virtuous", 10), ("Classy Lady", 12), ("Classy Slut", 14), ("Classy Virtuous", 15)])

            if becky_sue.tt_status in [11, 12, 13, 14]:
                title = "Will she stay with her sugar daddy?"
                is_sugar_baby = renpy.display_menu(items = [("Yes", True), ("No", False)])
                if not is_sugar_baby:
                    becky_sue.submission = 75   # lower her submission, so she leaves her sugar daddy

            add_client_items(becky_sue, [dildo])
            # remove all lingerie tags so you can give them again as girlfriend
            becky_sue.remove_item(lingerie, with_message = False)
            becky_sue.remove_tags('lingerie_whorish', 'lingerie_classy_slut', 'lingerie_classy_demure', 'lingerie_sweet', 'lingerie_wholesome_whore', 'lingerie_trashy_whore', 'lingerie_corset_classy', 'lingerie_corset_slutty')
            becky_sue.add_tags('ready_for_exhibitionist_outfit', 'accepts_domestic_discipline', 'says_fuck_during_orgasm', 'fixed_clothes', 'fixed_hair')
            becky_sue.orgasm_count = 5
            becky_sue.dungeon_pleasure_count = 4
            becky_sue.language = 2
            becky_sue.sex_count = 3
            becky_sue.slut_level = 4
            becky_sue.fix_count = 4
            becky_sue.language = 2
            becky_sue.tennis_doubts = 0 # best outcome
        if client is chelsea:
            title = "Training result?"
            is_toned = renpy.display_menu(items = [("Toned", True), ("BBW", False)])
            if is_toned:
                chelsea.desire_c = 200
            else:
                chelsea.desire_c = 50

            chelsea.sex_status = 2
            chelsea.youth_status = 0
            chelsea.dominate_status = 1
            chelsea.lesbian_status = 1
        if client is donna:
            title = "Is Donna a cum-slut?"
            is_cum_slut = renpy.display_menu(items = [("Yes", True), ("No", False)])
            if is_cum_slut and not donna.has_tag('cum_slut'):
                donna.add_tag('cum_slut')
            if not is_cum_slut and donna.has_tag('cum_slut'):
                donna.remove_tag('cum_slut')

            add_client_items(donna, [lingerie, dildo, butt_plug])

            donna.add_tags('stripped')
            donna.hobby_count = 3
            donna.bimbo_training_count = 4
            donna.ready_for_julia = 1
            donna.sex = 3
            donna.state = 4
            donna.sex_type = 2
            donna.son_event_discussion = 5
            donna.daughter_lust_revealed = 2
            if dee.ready_for_mom < 2:
                donna.daughter_investigation_triggered = 3
                dee.visit_week = week + 1

        if client is elsa:
            add_client_items(elsa, [butt_plug, dildo])
            elsa.sex_count = 10
            elsa.handjob_count = 2
            elsa.footjob_count = 1
            elsa.anal_count = 3
            elsa.fuck_machine_count = 2
            # elsa.anal_training = 1    # can be trained when gf
            elsa.masturbate_training = 3
            elsa.blowjob_training = 5
            elsa.domme_clues = 3
        if client is jasmine:
            jasmine.publicshow_level = 8
            jasmine.officeshow_count = 5
        if client is ivy:
            add_client_items(ivy, [lingerie, dildo, butt_plug])

            ivy.anal_count = 3
            ivy.serve_count = 2
            ivy.crawl_count = 3
            ivy.orgasm_count = 5
            ivy.add_tags('gave_her_sexy_lingerie', 'dommed_you', 'stripped_for_you', 'bj_training', 'had_adventurous_sex', 'spanking_orgasm', 'anal_orgasm', 'first_dungeon_visit_complete')
            ivy.remove_tags('will_not_strip')
        if client is lauren:
            add_client_items(lauren, [lingerie, chastity_belt, dildo, butt_plug])

            lauren.add_tags('accepts_anal', 'lingerie_classy')
            lauren.remove_tags('no_anal')
            lauren.blowjob_count = 3
            lauren.sex_count = 3
            lauren.punishment_count = 3
            title = "Blackmail Status:"
            was_blackmailed = renpy.display_menu(items = [("Blackmailed", True), ("No Blackmail", False)])
            if was_blackmailed and not lauren.has_tag('blackmailed'):
                renpy.call("lauren_blackmail_choices")  # we have not seen the black mail choices, so let player choose
            if not was_blackmailed and lauren.has_tag('blackmailed'):
                lauren.remove_tag('blackmailed')
        if client is sarah:
            add_client_items(lauren, [lingerie, butt_plug])

            #sarah.remove_tags()
            sarah.add_tags('lingerie_geisha', 'accepts_spanking')
            sarah.sex_with_guest = 1
            sarah.home_practice_level = 5
            sarah.weekend_watched_level = 4
            sarah.anal_count = 3
            sarah.massage_level = 3
            sarah.lingerie_level = 5
        if client is terri:
            if hannah.letter_re_terri < 7:  # entire storylines are hidden behind this gate
                title = "School event handled by?"
                principal = renpy.display_menu(items = [("Janice (Lawyer)", 8), ("Yourself", 7), ("Marilyn", 0)])
                if principal == 0:
                    hannah.marilyn_solution_thank_you == 1
                else:
                    hannah.letter_re_terri = principal

            terri.boobjob_interest = 2
            terri.orgasm_with_you = 3
            terri.blowjob_training_count == 3
            terri.sex_training_count = 3
            terri.anal_count = 1
            terri.ass_lick_count = 1
            terri.youth_interest = 5
            terri.state = 5
            terri.bondage_sex_count = 1
            terri.footjob_count = 1
            terri.add_tag('titfuck_attempted')

            if terri.ready_for_marilyn == 0 and terri.ready_for_domme == 0 and not terri.has_tag('likes_girls'):
                title = "Final Training?"
                items = [
                    ("Slave for Cassandra (lesbian slave)", 0),
                    ("Young girl for Marilyn (lesbian daughter)", 1),
                    ("Random Lesbian", 2),
                    ("Adult Baby", 3),
                    ("Just finish training as is", 99)
                ]
                if player.has_tag('hypnotist'):
                    items.insert(4, ("Assistant", 4))

                final_training = renpy.display_menu(items)

                # make sure lingerie tags have associated item
                if final_training < 10 and not terri.has_item(lingerie):
                    terri.add_item(lingerie, with_message = False)

                if final_training == 0:
                    terri.ready_for_domme = 2
                    cassandra.independent_encounter_status = 2
                    terri.add_tags('likes_girls', 'lingerie_sexy')
                    renpy.call("terri_calling") # use default scene to end training
                if final_training == 1:
                    terri.ready_for_marilyn = 2
                    marilyn.independent_encounter_status = 2
                    terri.add_tags('likes_girls', 'lingerie_sexy')
                    renpy.call("terri_calling") # use default scene to end training
                if final_training == 2:
                    terri.add_tags('likes_girls', 'lingerie_cheerleader')
                if final_training == 3:
                    terri.youth_interest = 6
                    renpy.call("terri_calling") # use default scene to end training
                if final_training == 4:
                    terri.add_tags('hypnosis_revealed')
                    if terri.has_tag('discussed_assistant_role'):
                        terri.remove_tag('discussed_assistant_role')
                    if terri.sos <= 20:
                        terri.sos = 30
                    renpy.call("terri_calling") # use default scene to end training

        return


label king_tut_init:
    python:
        global king_tut_accept_weeks
        king_tut_accept_weeks = 4

        living_room.add_button("King Tut", new_context = "king_tut", auto_image = get_auto_image_location(), cut_portrait = True, button_weight = -10)

        # player stats
        living_room.add_action("{color=#ffff00}-- Player Style --{/color}", context = "king_tut", label = "king_tut_dummy_label", order = 0,  unseen = False, seen_result = True)
        living_room.add_action("Learn Hypnosis", context = "king_tut", label = "king_tut_learn_hypnosis", order = 1, condition = "not player.has_tag('hypnotist')", unseen = False, seen_result = True)
        living_room.add_action("Unlearn Hypnosis", context = "king_tut", label = "king_tut_unlearn_hypnosis", order = 1, condition = "player.has_tag('hypnotist')", unseen = False, seen_result = True)
        living_room.add_action("Learn Dominance", context = "king_tut", label = "king_tut_learn_dominance", order = 2, condition = "not player.has_tag('dominant')", unseen = False, seen_result = True)
        living_room.add_action("Unlearn Dominance", context = "king_tut", label = "king_tut_unlearn_dominance", order = 2, condition = "player.has_tag('dominant')", unseen = False, seen_result = True)
        living_room.add_action("Learn Seduction", context = "king_tut", label = "king_tut_learn_seduction", order = 3, condition = "not player.has_tag('supersexy')", unseen = False, seen_result = True)
        living_room.add_action("Unlearn Seduction", context = "king_tut", label = "king_tut_unlearn_seduction", order = 3, condition = "player.has_tag('supersexy')", unseen = False, seen_result = True)
        living_room.add_action("Enhanced Hypnosis", context = "king_tut", label = "king_tut_enhanced_hypnosis", order = 4, condition = "player.has_tag('hypnotist') and not player.has_tag('enhanced_hypnosis')", unseen = False, seen_result = True)
        living_room.add_action("Change Hypnosis Triggers", context = "king_tut", label = "king_tut_change_hypnosis_triggers", order = 5, condition = "player.has_tag('hypnotist')", unseen = False, seen_result = True)

        # training
        living_room.add_action("{color=#ffff00}-- Client Actions --{/color}", context = "king_tut", label = "king_tut_dummy_label", order = 29,  unseen = False, seen_result = True)
        living_room.add_action("Normal Energy", context = "king_tut", label = "king_tut_default_energy", order = 30, condition = "player.has_tag('unlimited_energy')", unseen = False, seen_result = True)
        living_room.add_action("Unlimited Energy", context = "king_tut", label = "king_tut_unlimited_energy", order = 30, condition = "not player.has_tag('unlimited_energy')", unseen = False, seen_result = True)
        living_room.add_action("Normal Sessions", context = "king_tut", label = "king_tut_normal_sessions", order = 31, condition = "player.has_tag('unlimited_sessions')", unseen = False, seen_result = True)
        living_room.add_action("Unlimited Sessions", context = "king_tut", label = "king_tut_unlimited_sessions", order = 31, condition = "not player.has_tag('unlimited_sessions')",unseen = False, seen_result = True)
        living_room.add_action("Client Accept Weeks", context = "king_tut", label = "king_tut_client_accept_weeks", order = 32, unseen = False, seen_result = True)
        living_room.add_action("Extend Training Period", context = "king_tut", label = "king_tut_extend_training_period", order = 33, condition = "any([x for x in all_clients if x.status == 'on_training' and not x.has_tag('first_visit')])", unseen = False, seen_result = True)
        living_room.add_action("End Client Training", context = "king_tut", label = "king_tut_end_client_training", order = 34, condition = "any([x for x in all_clients if x.status == 'on_training' and not x.has_tag('first_visit')])", unseen = False, seen_result = True)
        living_room.add_action("Give another Transformation Potion", context = "king_tut", label = "king_tut_give_another_tp", order = 35, condition = "any([x for x in get_people(include_minor_characters = True, tagged_with_any = ['transformed'])])", unseen = False, seen_result = True)

        # client actions
        living_room.add_action("{color=#ffff00}-- Story Line Actions --{/color}", context = "king_tut", label = "king_tut_dummy_label", order = 40, unseen = False, seen_result = True)
        living_room.add_action("Becky Sue accepts other girls", context = "king_tut", label = "king_tut_convert_becky_sue", order = 41, condition = "becky_sue.has_tag('exclusive_girlfriend') and ((becky_sue.boyfriend_trip == 0 and becky_sue.has_any_tag('submissive_to_sugar_daddy_visits_open', 'sugar_baby', 'concerned_about_boyfriend_relationship')) or becky_sue.has_tag('continuing_actions') or becky_sue.has_tag('girlfriend'))", unseen = False, seen_result = True)
        living_room.add_action("Make Becky Sue bi-sexual", context = "king_tut", label = "king_tut_becky_sue_likes_girls", order = 42, condition = "(becky_sue.has_tag('continuing_actions') or becky_sue.has_tag('girlfriend')) and not becky_sue.has_tag('likes_girls')", unseen = False, seen_result = True)
        living_room.add_action("Set Becky Sue relationship to maximum", context = "king_tut", label = "king_tut_becky_sue_max_relation", order = 43, condition = "(becky_sue.has_tag('continuing_actions') or becky_sue.has_tag('girlfriend')) and becky_sue.relationship_counter < 10", unseen = False, seen_result = True)
        living_room.add_action("Set Chelsea relationship to maximum", context = "king_tut", label = "king_tut_chelsea_max_relation", order = 44, condition = "(chelsea.has_tag('continuing_actions') or chelsea.has_tag('girlfriendO')) and chelsea.relationship_counter < 10", unseen = False, seen_result = True)
        living_room.add_action("Set Jasmine Flashing Downtown", context = "king_tut", label = "king_tut_jasmine_downtown", order = 45, condition = "not jasmine.status == 'unavailable' and jasmine.downtown_week > 0 and jasmine.has_tag('satisfied') and jasmine.downtown_countdown != 0", unseen = False, seen_result = True)
        living_room.add_action("Activate Ivy Submissive Visit", context = "king_tut", label = "king_tut_ivy_submission_visit", order = 46, condition = "ivy.has_tag('continuing_actions') and ivy.has_tag('first_dungeon_visit_complete') and ivy.submissive_visit_timer != 0", unseen = False, seen_result = True)
        living_room.add_action("Unlock Sarah controlled orgasms", context = "king_tut", label = "king_tut_sarah_controlled_orgasms", order = 47, condition = "sarah.has_tag('girlfriend') and not sarah.has_tag('controlled_orgasms')", unseen = False, seen_result = True)

        # side character actions
        living_room.add_action("Rae accepts other girls", context = "king_tut", label = "king_tut_convert_rae", order = 61, condition = "rae.has_tag('talked') and rae.has_tag('exclusive_girlfriend')", unseen = False, seen_result = True)
        living_room.add_action("Cassandra have sex in club", context = "king_tut", label = "king_tut_reset_cassandra", order = 63, condition = "cassandra.independent_encounter_status == 3", unseen = False, seen_result = True)
        living_room.add_action("Marilyn have sex in club", context = "king_tut", label = "king_tut_marilyn_have_sex_in_club", order = 64, condition = "marilyn.sex_count > 0 and marilyn.independent_encounter_status > 2", unseen = False, seen_result = True)
        living_room.add_action("Dee visits next week", context = "king_tut", label = "king_tut_force_dee_visit", order = 65, condition = "donna.status == 'on_training' and donna.daughter_investigation_triggered > 0 and dee.visit_week == week + 1", unseen = False, seen_result = True)
        living_room.add_action("Hire Janice the Lawyer", context = "king_tut", label = "king_tut_hire_lawyer", order = 66, condition = "janice.has_tag('asked_about_hiring') and not player.has_tag('lawyer_on_retainer')", unseen = False, seen_result = True)
        living_room.add_action("Hannah unlock Bethany Solution", context = "king_tut", label = "king_tut_hannah_unlock_bethany", order = 67, condition = 'hannah.lost_money_and_no_fix in [1, 2] and bethany.ready_to_help_school == 0', unseen = False, seen_result = True)
        living_room.add_action("Unlock Marilyn special reward", context = "king_tut", label = "king_tut_unlock_marilyn_special_reward", order = 68, condition = 'marilyn.rewards_pending > 0 and marilyn.sex_count == 0', unseen = False, seen_result = True)

        # quick actions
        living_room.add_action("{color=#ffff00}-- Other Actions --{/color}", context = "king_tut", label = "king_tut_dummy_label", order = 90, unseen = False, seen_result = True)
        living_room.add_action("Add $1000 Money", context = "king_tut", label = "king_tut_increase_money", order = 91, unseen = False, seen_result = True)
        # items
        living_room.add_action("Open Locations", context = "king_tut", label = "king_tut_unlock_locations", order = 92, condition = "not player.has_tag('das_access') or not player.has_tag('club_access')", unseen = False, seen_result = True)
        living_room.add_action("Radiant Bonsai's", context = "king_tut", label = "king_tut_radiant_bonsais", order = 93, condition = "nicole_bonsai in items_in_area('house') and not nicole_bonsai.has_tag('radiant')", unseen = False, seen_result = True)
        living_room.add_action("Stock up on items", context = "king_tut", label = "king_tut_stock_up", order = 94, condition = "not player.has_tag('large_inventory')", unseen = False, seen_result = True)



        # minor characters retry after failure
        living_room.add_action("Retry to impress Gloria", context = "king_tut", label = "king_tut_retry_gloria", order = 91, condition = "gloria.session == 3", unseen = False, seen_result = True)
        living_room.add_action("Retry Diamond Training", context = "king_tut", label = "king_tut_retry_diamond", order = 92, condition = "diamond.training_result < 7 and master_m.current_message == 1", unseen = False, seen_result = True)
        living_room.add_action("Retry Fairyn Training", context = "king_tut", label = "king_tut_retry_fairyn", order = 93, condition = "fairyn.initial_outcome <= 1 and master_m.current_message == 2", unseen = False, seen_result = True)


        living_room.add_action("{color=#0000aa}----- " + king_tut_current_version + " -----{/color}", context = "king_tut", label = "king_tut_dummy_label", order = 999, unseen = False, seen_result = True)

        # reveal sens of self detailed stats to player
        player.add_tags('show_sos')
        player.add_tags('show_desire_c')

        # store girl hypno threshholds
        for person in all_clients + all_minor_characters:
            if person.has_stat("hypno_trigger_sessions_threshold"):
                person.add_stat("original_hypno_trigger_sessions_threshold", person.stats["hypno_trigger_sessions_threshold"])
            if person.has_stat("hypno_trigger_resistance_threshold"):
                person.add_stat("original_hypno_trigger_resistance_threshold", person.stats["hypno_trigger_resistance_threshold"])
            if person.has_stat("hypno_trigger_level_threshold"):
                person.add_stat("original_hypno_trigger_level_threshold", person.stats["hypno_trigger_level_threshold"])

    day_label add to end king_tut_daily_update
    return

label king_tut_dummy_label:
    return

label king_tut_unlimited_energy:
    python:
        player.add_tag('unlimited_energy')

        player.max_energy = 2000
        player.energy = 2000

    "You now have virtually unlimited energy per week."
    return

label king_tut_default_energy:
    python:
        player.remove_tag('unlimited_energy')

        player.max_energy = 100
        player.energy = 100

    "Your energy levels have been reset."
    return

label king_tut_unlock_locations:
    $ player.add_tags('das_access', 'club_access')

    "You now have access to the Club and the Dark Arts store."
    return

label king_tut_learn_hypnosis:
    wt_image hy_image
    python:
        player.add_tags('hypnotist', 'show_resistance')
        player.hypnosis_level += 10

    "You are now an accomplished hypnotist."
    wt_image player.location.short_name + "_image"
    return

label king_tut_enhanced_hypnosis:
    wt_image hy_image
    python:
        player.add_tag('enhanced_hypnosis')
        player.hypnosis_level += 10

    "You are now a master hypnotist, to further enhance your strength visit the Dark Arts store."
    wt_image player.location.short_name + "_image"
    return

label king_tut_unlearn_hypnosis:
    python:
        if player.has_tag("enhanced_hypnosis"):
            player.hypnosis_level -= 10

        if player.has_tag('hypnotist'):
            player.hypnosis_level -= 10

        player.remove_tags('hypnotist', 'enhanced_hypnosis', 'show_resistance')

    "You are no longer capable of performing hypnosis."
    return

label king_tut_learn_dominance:
    wt_image nd_image
    python:
        player.add_tags('dominant', 'show_submission')
        player.submission_mod += 10
        player.submission_gain_mod += 5

    "You now have a natural dominant aura."
    wt_image player.location.short_name + "_image"
    return

label king_tut_unlearn_dominance:
    python:
        player.remove_tags('dominant', 'show_submission')
        player.submission_mod -= 10
        player.submission_gain_mod -= 5

    "You lost your natural dominant aura."
    return

label king_tut_learn_seduction:
    wt_image pb_image
    python:
        player.add_tags('supersexy', 'show_desire')
        player.desire_mod += 10
        player.desire_gain_mod += 5

    "You are now proficient at seducing woman."
    wt_image player.location.short_name + "_image"
    return

label king_tut_unlearn_seduction:
    python:
        player.remove_tags('supersexy', 'show_desire')
        player.desire_mod -= 10
        player.desire_gain_mod -= 5

    "You have lost your enigmatic charm."
    return

label king_tut_stock_up:
    python:
        player.add_tag('large_inventory')
        lingerie.max_quantity = 30
        dildo.max_quantity = 30
        butt_plug.max_quantity = 30
        chastity_belt.max_quantity = 30
        transformation_potion.max_quantity = 30
        love_potion.max_quantity = 30
        will_tamer.max_quantity = 10
        ring_sexuality.max_quantity = 10
        suggestion_pills.max_quantity = 99
        fetch_toy.max_quantity = 10

    add 20 dildo to player
    add 20 love_potion to player
    add 20 transformation_potion to player
    add 20 lingerie to player
    add 20 butt_plug to player
    add 20 chastity_belt to player
    add 4 suggestion_pills to player

    add 3 will_tamer to player
    add 3 ring_sexuality to player

    add 5 fetch_toy to player
    add 1 leash to player
    add 1 water_bowl to player

    notify
    "Your inventory has been filled up with all items you need."
    return

label king_tut_radiant_bonsais:
    python:
        nicole_bonsai.sos_mod = 5
        nicole_bonsai.resistance_mod = 5
        nicole_bonsai.desire_mod = 5
        nicole_bonsai.submission_mod = 5
        nicole_bonsai.add_tag('bedroom')
        nicole_bonsai.add_tag('living_room')
        nicole_bonsai.add_tag('boudoir')
        nicole_bonsai.add_tag('dungeon')
        nicole_bonsai.add_tag('radiant')
        nicole_bonsai.remove_action(nicole_bonsai.action_move) # it's already in every room, so discard move action
        nicole_bonsai.add_stats_with_value('desire_mod', 'submission_mod', 'sos_mod', 'resistance_mod', force = True)

    add 1 nicole_bonsai to bedroom
    add 1 nicole_bonsai to living_room
    add 1 nicole_bonsai to basement
    add 1 nicole_bonsai to dungeon
    add 1 nicole_bonsai to boudoir

    day_label rem from start bt_start_day

    python:
        for location in locations_in_area('house'):
            for stat in ['desire_mod', 'submission_mod', 'sos_mod']:
                location.stats[stat] += 5
            location.stats['resistance_mod'] -= 5

    notify

    "The Bonsai Tree is now radiant and available in all house rooms."
    return

label king_tut_convert_rae:
    add tag 'no_club_visit' to rae
    rem tag 'exclusive_girlfriend' from rae

    wt_image rae.image
    "Rae will no longer complain about other girlfriends."
    wt_image player.location.short_name + "_image"
    return

label king_tut_convert_becky_sue:
    add tag 'no_club_visit' to becky_sue
    rem tag 'exclusive_girlfriend' from becky_sue

    wt_image becky_sue.image
    "Becky Sue will no longer complain about other girlfriends."
    wt_image player.location.short_name + "_image"
    return

label king_tut_becky_sue_likes_girls:
    add tag 'likes_girls' to becky_sue

    wt_image becky_sue.image
    "Becky Sue will now be open to having sex with other women."
    wt_image player.location.short_name + "_image"
    return

label king_tut_becky_sue_max_relation:
    $ becky_sue.relationship_counter = 10

    wt_image becky_sue.image
    "Your relationship with Becky Sue is now perfect."
    wt_image player.location.short_name + "_image"
    return

label king_tut_chelsea_max_relation:
    python:
        chelsea.relationship_counter = 10
        chelsea.visit_talk_count = 6
        chelsea.visit_sex_count = 6

    wt_image chelsea.image
    "Your relationship with Chelsea is now perfect."
    wt_image player.location.short_name + "_image"
    return

label king_tut_increase_money:
    $ player.money += 1000
    return

label king_tut_change_hypnosis_triggers:
    $ title = "Hypnosis Trigger Implants Difficulty:"
    menu:
        "Easy":
            # increase threshold by 20 (check is person.resistance < threshold -> implement trigger)
            python:
                for person in all_clients + all_minor_characters:
                    if person.has_stat("hypno_trigger_sessions_threshold"):
                        person.set_stat("hypno_trigger_sessions_threshold", int(person.stats["original_hypno_trigger_sessions_threshold"] / 2.0))
                    if person.has_stat("hypno_trigger_resistance_threshold"):
                        person.set_stat("hypno_trigger_resistance_threshold", int(person.stats["original_hypno_trigger_resistance_threshold"] / 2.0))
                    if person.has_stat("hypno_trigger_level_threshold"):
                        person.set_stat("hypno_trigger_level_threshold", int(person.stats["original_hypno_trigger_level_threshold"] / 2.0))

            "You can now implant hypnosis triggers sooner."
        "Default":
            python:
                for person in all_clients + all_minor_characters:
                    if person.has_stat("hypno_trigger_sessions_threshold"):
                        person.set_stat("hypno_trigger_sessions_threshold", person.stats["original_hypno_trigger_sessions_threshold"])
                    if person.has_stat("hypno_trigger_resistance_threshold"):
                        person.set_stat("hypno_trigger_resistance_threshold", person.stats["original_hypno_trigger_resistance_threshold"])
                    if person.has_stat("hypno_trigger_level_threshold"):
                        person.set_stat("hypno_trigger_level_threshold", person.stats["original_hypno_trigger_level_threshold"])

            "Hypnosis trigger implant set to default values."
        "Cancel":
            pass
    return

label king_tut_client_accept_weeks:
    $ title = "Set number of weeks for accepting clients to:"
    menu:
        "One year":
            $ king_tut_accept_weeks = 52
            call king_tut_daily_update from _call_king_tut_daily_update_1
        "Six months":
            $ king_tut_accept_weeks = 26
            call king_tut_daily_update from _call_king_tut_daily_update_2
        "Default (4 weeks)":
            $ king_tut_accept_weeks = 4
            call king_tut_daily_update from _call_king_tut_daily_update_3
        "Cancel":
            pass
    return

label king_tut_extend_training_period:
    python:
        title = "Select client:"
        client = renpy.display_menu(items = [(p.name, p) for p in get_people(include_minor_characters = False, with_status = "on_training")] + [("Cancel", False)])
        if client:
            title = "Select # weeks:"
            weeks = renpy.display_menu(items = [("2 Weeks", 2), ("3 Weeks", 3), ("4 Weeks", 4), ("Cancel", False)])
            if weeks:
                client.stats["training_period"] += weeks
                renpy.say("", "[client.name] training period extended by [weeks] weeks.")
    return

label king_tut_end_client_training:
    python:
        title = "Select client:"
        client = renpy.display_menu(items = [(p.name, p) for p in get_people(include_minor_characters = False, not_tagged_with_any = ["first_visit", "satisfied", "unsatisfied"])] + [("Cancel", False)])
        if client:
            title = "Select status:"
            success = renpy.display_menu(items = [("Only end training", 1), ("Maximize Stats / Optimum", 2), ("Cancel", False)])
            if success:
                if success == 2:
                    set_client_maximum_results(client)
                    set_client_optimal_end_state(client)
                renpy.call(client.short_name + "_end_training")
    return

label king_tut_give_another_tp:
    python:
        title = "Select client:"
        client = renpy.display_menu(items = [(p.name, p) for p in get_people(include_minor_characters = True, tagged_with_any = ["transformed"])] + [("Cancel", False)])
        if client:
            client.tags.remove("transformed")
            for c_tag in ['girlfriend', 'hypno_girlfriend', 'bimbo', 'showgirl', 'whore', 'assistant', 'sugar_baby', 'domme', 'degraded', 'lesbian', 'puppy_girl', 'puppygirl', 'adult_baby']:
                if client.has_tag(c_tag):
                    renpy.call("unconvert", client, c_tag)

    python:
        if client:
            renpy.call("give_tp_" + client.short_name)
    return

label king_tut_normal_sessions:
    rem tag 'unlimited_sessions' from player
    "You are limited to one hypnosis and session per client per week."
    return

label king_tut_unlimited_sessions:
    add tag 'unlimited_sessions' to player
    "You now have daily hypnosis and session per client."
    return

label king_tut_jasmine_downtown:
    python:
        jasmine.downtown_week = week - 1
        if jasmine.downtown_week <= 0:
            jasmine.downtown_week = 1
        jasmine.downtown_countdown = 0
        jasmine.downtown_follow_count = 3
        jasmine.downtown_outfit = 5

    wt_image exhi_downtown_1_1
    "Jasmine is flashing downtown."
    wt_image player.location.short_name + "_image"
    return

label king_tut_ivy_submission_visit:
    python:
        ivy.submissive_visit_timer = 0

    wt_image intro_wife_dungeon_1_1
    "Ivy will now allow a visit where you take her to the dungeon."
    wt_image player.location.short_name + "_image"
    return

label king_tut_sarah_controlled_orgasms:
    python:
        if sarah.edged_since_o < 4:
            sarah.edged_since_o = 4
        if sarah.edged_weeks < 2:
            sarah.edged_weeks = 2

    add tag 'controlled_orgasms' to sarah

    wt_image lw_gf_event_2_1
    "Sarah can now be edged, prevent her from getting orgasms and she will start to beg. A chastity belt might help."
    wt_image player.location.short_name + "_image"
    return

label king_tut_fix_chelsea_lesbian_route:
    python:
        chelsea.lesbian_status += 1
        chelsea.lesbian_club_count = 2

    wt_image chubby_swinging_22
    "[chelsea.name] didn't respond the way you'd hoped she would, but she demonstrated an awareness of what the woman was looking for, as opposed to being completely oblivious to it like she was last time.  That's progress, in a way, and may affect her thinking once she's had a chance to absorb her own feelings about the woman's attraction to her."
    wt_image player.location.short_name + "_image"
    return

label king_tut_reset_cassandra:
    python:
        cassandra.independent_encounter_status = 2
        cassandra.location = club
    add tag 'in_club_now' to cassandra
    add tag 'gloria_club_talk_possible' to cassandra # opens a dialogue for Gloria
    call move_to(club) from _call_king_tut_reset_cassandra
    return

label king_tut_marilyn_have_sex_in_club:
    python:
        marilyn.fuck_chance = 2
        marilyn.location = club
    add tag 'in_club_now' to marilyn
    add tag 'gloria_club_talk_possible' to marilyn
    call move_to(club) from _call_king_tut_marilyn_have_sex_in_club
    return

label king_tut_unlock_marilyn_special_reward:
    wt_image marilyn_office_22
    marilyn.c "It's not very often that someone can offer me a new experience.  I think that deserves a suitable reward."
    add tag 'special_reward' to marilyn
    call expandable_menu(marilyn_reward_menu) from _call_marilyn_reward_menu_king_tut
    wt_image player.location.short_name + "_image"
    return

label king_tut_force_dee_visit:
    $ dee.visit_week = week + 1
    $ donna.daughter_investigation_triggered = 3

    wt_image daughter_house_1_2
    "Dee is visiting her mother next week."
    wt_image player.location.short_name + "_image"
    return

label king_tut_hire_lawyer:
    add tag 'lawyer_on_retainer' to player
    wt_image lawyer_desk_1

    "Congratulations!  You now have a high powered lawyer on retainer."
    wt_image player.location.short_name + "_image"
    return

label king_tut_hannah_unlock_bethany:
    python:
        bethany.ready_to_help_school = 1
        bethany.disclosed_pimping = 3

    wt_image banker_test_1
    "Bethany the Banker now can help out school principal Hannah."
    wt_image player.location.short_name + "_image"
    return

label king_tut_retry_gloria:
    python:
        gloria.session = 2
        gloria.first_session_test = 0
    call gloria_contact from _call_gloria_contact_king_tut_retry_gloria
    return

label king_tut_retry_diamond:
    python:
        diamond.training_result = 0
        diamond.training_submission_level = 0
        diamond.training_desire_level = 0
        master_m.current_message = 0
    call master_m_message from _call_master_m_message_king_tut_retry_diamond
    return

label king_tut_retry_fairyn:
    python:
        fairyn.initial_outcome = 0
        master_m.current_message = 1
    call master_m_message from _call_master_m_message_king_tut_retry_fairyn
    return

label king_tut_daily_update:
    python:
        update_mod()

        for person in [x for x in all_clients if x.status == "waiting_on_message"]:
            person.stats["wait_for_message_period"] = person.week_available + king_tut_accept_weeks

        if player.has_tag("unlimited_sessions"):
            for person in all_clients + all_minor_characters:
                person.tags -= person.remove_tags_daily
                person.tags -= person.remove_tags_weekly
                person.stats['hypno_sessions_this_week'] = -5

        # prevent rae ending relation
        rae.strike_count = 0

        # last day of week notifications (so you can handle them on Friday)
        if day == 4:
            check_up_list = []
            # Whore loss warning
            for whore in get_people(tagged_with_all = ['whore']):
                if hasattr(whore, "whore_lost_countdown") and whore.whore_lost_countdown <= 1:
                    check_up_list.append(whore.name)

            if check_up_list:
                renpy.say(sys, "Notice: You should checkup on your whores, if you don't, you might loose her. Whores that need checkup: " + ", ".join(check_up_list) + ".")

            # notify player that he should give girlfriends love potions.
            need_love_potion = []
            for person in get_people(tagged_with_any = ['girlfriend', 'hypno_girlfriend'], not_tagged_with_any = ['love_potion_used']):
                need_love_potion.append(person.name)

            if need_love_potion:
                renpy.say(sys, "Notice: To prevent girlfriends from leaving you, give them a love potion. Girlfriends without love potion given: " + ", ".join(need_love_potion) + ".")

            # cleanup variables
            check_up_list = None
            need_love_potion = None

        # only autosave once per day
        save_name = "End Week {} - Day {} ".format(week, day)
        renpy.force_autosave(take_screenshot = True, block = True)
        save_name = ""
    return

label king_tut_club_swingers_watch_girlfriend:
    $ title = "Watch Your Girlfriend"
    $ selected_girlfriend = renpy.display_menu(items = [(p.name, p) for p in get_people(tagged_with_any = ['club_date_night', 'in_swingers_room_now', 'swingers_room_possible'], not_tagged_with_any = ['no_club_visit'])] + [('Cancel', False)])

    if selected_girlfriend:
        $ current_target = selected_girlfriend
        if renpy.has_label(current_target.short_name + "_watch"):
            call expression (current_target.short_name + "_watch") from _call_king_tut_watch_girlfriend
        else:
            "WifeTrainer has not implemented scenes for [current_target.name]."
    return
