## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: a4hryou

# Package Register
# register_package terri name "Terri, The Good Girlfriend" description "Allows Terri to be client." dependencies core
register terri_pregame 10 in core as "Terri the Good Girlfriend"

# Pregame
label terri_pregame:
    python:
        ## Constants
        ## Credits
        model_credits += [('full', "Terri the Good Girlfriend (Dani Jensen)")]

        ## Character Definition
        terri = Person(Character("Terri", who_color="#FF0000", what_color="#FF0000", window_background=gui.dialogue_background_medium_font_color), "terri", cut_portrait = True, prefix = "", suffix = "the Good Girlfriend", resistance = 20, training_period = 12, min_reputation = 1)
        terri.trigger_phrase = None
        terri.your_respect_name = "Sir"
        terri.your_daddy_name = "Daddy"

        # Other Characters
        # Deep Yellow
        hypno_training_woman_terri_1 = Character("Woman in Park", who_color="#e6b800", what_color="#e6b800")
        # Blue
        hypno_training_woman_terri_2 = Character("Woman in Park", who_color="#0042B2", what_color="#0042B2", window_background = gui.dialogue_background_dark_font_color)
        # Teal
        hypno_training_woman_terri_3 = Character("Woman in Park", who_color="#00c4c4", what_color="#00c4c4")
        # Orangish Brown
        hypno_training_woman_terri_4 = Character("Woman in Coffee Shop", who_color="#c77318", what_color="#c77318", window_background = gui.dialogue_background_dark_font_color)
        # Deep Yellow
        hypno_training_woman_terri_8 = Character("Jogger", who_color="#e6b800", what_color="#e6b800")
        # rose
        hypno_training_woman_terri_9 = Character("Shopper", who_color="#ff66ff", what_color="#ff66ff")


        ## Actions

        # hypnosis actions
        terri.add_hypno_actions(implant = False) # this adds the standard hypnosis actions
        terri.action_hypno_insecurities = terri.add_action("Address her insecurities", label = "_insecurities_hypnosis", context = "_hypnosis", condition = "terri.hypno_insecurities_count <= 2")

        # training actions
        terri.action_talk = terri.add_action("Talk to her", label="_talk", condition = "terri.can_be_interacted and terri.status == 'on_training' and terri.in_area('house') and not terri.has_tag('talked_today')")
        terri.action_make_out = terri.add_action("Make out with her", label="_make_out", condition = "terri.can_be_interacted and terri.status == 'on_training' and terri.in_area('house') and not terri.has_tag('first_visit') and not terri.has_tag('make_out_action_not_available')")
        terri.action_youth_training = terri.add_action("Work on her youthfulness", label="_youth_training", condition = "terri.can_be_interacted and terri.status == 'on_training' and not terri.has_tag('first_visit') and terri.in_area('house')")
        terri.action_skills_training = terri.add_action("Work on her basic sex skills", label="_skills_training", condition = "terri.can_be_interacted and terri.status == 'on_training' and not terri.has_tag('first_visit') and terri.in_area('house')")
        terri.action_variety_training = terri.add_action("Introduce her to new sex acts", label="_variety_training", condition = "terri.can_be_interacted and terri.status == 'on_training' and not terri.has_tag('first_visit') and terri.sex_training_count > 0 and terri.in_area('house')")
        terri.action_strip = terri.add_action("Have her strip for you", label="_strip", condition = "terri.can_be_interacted and terri.status == 'on_training' and not terri.has_tag('first_visit') and terri.strip_masturbate_dildo_options == 0 and terri.in_area('house')")
        terri.action_end_session = terri.add_action("End session", label="_end_session", condition = "not terri.has_any_tag('first_visit', 'post_continuing_actions', 'shut_off_end_session') and terri.in_area('house')")
        terri.action_pleasure_her = terri.add_action("Pleasure her", label="_pleasure_her", condition = "terri.can_be_interacted and terri.status == 'on_training' and not terri.has_tag('first_visit') and terri.pleasure_her_action_used > 0 and terri.pleasure_her_action_used < 3 and terri.in_area('house')")
        terri.action_masturbate_for_you = terri.add_action("Have her masturbate for you", label="_masturbate_for_you", condition = "terri.can_be_interacted and terri.status == 'on_training' and not terri.has_tag('first_visit') and terri.strip_masturbate_dildo_options == 1 and terri.in_area('house')")
        terri.action_dildo_herself = terri.add_action("Have her dildo herself", label="_dildo_herself", condition = "terri.can_be_interacted and terri.status == 'on_training' and not terri.has_tag('first_visit') and terri.strip_masturbate_dildo_options == 2 and terri.in_area('house')")
        terri.action_show_off_lingerie = terri.add_action("Have her show off her lingerie", label="_show_off_lingerie", condition = "terri.can_be_interacted and terri.status == 'on_training' and terri.has_item(lingerie) and terri.lingerie_action_used == 1 and terri.in_area('house')")

        # visit actions
        terri.action_contact_talk = terri.add_action("Talk to her", label="_contact_talk", condition = "terri.can_be_interacted and terri.status == 'post_training' and terri.has_tag('continuing_actions') and terri.in_area('house') and not terri.has_tag('futanari')")

        # adult baby actions
        terri.action_bottle = terri.add_action("Bring her a bottle", label="_bottle", condition="terri.has_tag('adult_baby') and terri.can_be_interacted and terri.in_area('house')")
        terri.action_toy = terri.add_action("Bring her a toy", label="_toy", condition="terri.has_tag('adult_baby') and terri.can_be_interacted and terri.in_area('house')")
        terri.action_crawl = terri.add_action("Let her crawl around", label="_crawl", condition="terri.has_tag('adult_baby') and terri.can_be_interacted and terri.in_area('house')")
        terri.action_daddy_needs = terri.add_action("[terri.your_daddy_name] has needs, too", label="_daddy_needs", condition="terri.has_tag('adult_baby') and terri.can_be_interacted and terri.in_area('house')")
        terri.action_diaper = terri.add_action("Check her diaper", label="_diaper", condition="terri.has_tag('adult_baby') and terri.can_be_interacted and not terri.has_tag('diaper_checked_today') and terri.in_area('house')")
        terri.action_bath = terri.add_action("Give her a bath", label="_bath", condition="terri.has_tag('adult_baby') and terri.can_be_interacted and terri.in_area('house')")
        terri.action_daddy_name = terri.add_action("Tell her how to address you", label="_daddy_name", condition="terri.has_tag('adult_baby')")

        # assistant actions
        terri.action_assistant_training = terri.add_action("Train her", label="_assistant_training", condition = "terri.has_tag('assistant') and not terri.has_tag('assistant_trouble') and terri.can_be_interacted and terri.in_area('house')")

        # doll actions
        terri.action_doll_dress_her = terri.add_action("Dress her", label='_doll_dress_her', condition = "terri.can_be_interacted and terri.has_tag('doll') and terri.in_area('house')")
        terri.action_doll_rearrange_her = terri.add_action("Rearrange her", label='_doll_rearrange_her', condition = "terri.can_be_interacted and terri.has_tag('doll') and terri.doll_dress_state > 0 and terri.in_area('house')")
        terri.action_doll_use_her = terri.add_action("Use her", label='_doll_use_her', condition = "terri.can_be_interacted and terri.has_tag('doll') and terri.doll_dress_state > 0 and terri.in_area('house')")

        # slavegirl actions
        terri.action_hurt_her = terri.add_action("Hurt her",label="_hurt_her", condition="terri.can_be_interacted and terri.has_tag('slavegirl') and terri.in_area('house')")
        terri.action_use_her = terri.add_action("Use her",label="_use_her", condition="terri.can_be_interacted and terri.has_tag('slavegirl') and terri.in_area('house')")
        terri.action_sg_kiss_her = terri.add_action("Kiss her",label="_sg_kiss_her", condition="terri.can_be_interacted and terri.has_tag('slavegirl') and terri.in_area('house')")
        terri.action_let_her_out = terri.add_action("Let her out for a bit",label="_let_her_out", condition="not terri.has_tag('slavegirl_let_out') and terri.can_be_interacted and terri.has_tag('slavegirl') and terri.in_area('house')")
        terri.action_rename = terri.add_action("Rename her",label="_rename", condition="terri.has_tag('slavegirl')")
        terri.action_lend_to_master_m = terri.add_action("Lend her to Master M", label="_lend_to_master_m", condition="terri.has_tag('slavegirl') and player.has_tag('m_waiting_for_slave') and terri.in_area('house')")
        terri.action_your_name = terri.add_action("Tell her how to address you", label="_your_name", condition="terri.has_tag('slavegirl')")

        # futanari actions
        terri.action_futanari_talk = terri.add_action("Talk to her", label="_futanari_talk", condition = "terri.can_be_interacted and terri.status == 'post_training' and terri.has_tag('continuing_actions') and terri.in_area('house') and terri.has_tag('futanari')")

        # terri.action_review_files = None
        # terri.action_relationship_status = None

        terri.relationship_action = bedroom.add_action("[terri.full_name]", label = terri.short_name + "_relationship_status", context = "_relationship_status", condition = "terri.has_tag('adult_baby') or terri.has_tag('assistant') or terri.has_tag('continuing_actions')")

        ## Tags
        # Common Character Tags
        terri.add_tags('first_visit', 'no_hypnosis')
        ## note: Terri does not start with 'likes_girls'; this gets added if you successfully deal with this issue; she also doesn't have 'likes_boys' because she's equivalent to Sam here, will sleep with them but not attracted to them

        # Character Specific Tags
        # N/A

        ## Locations
        # Terri the Assistant's Room
        terri_the_assistant_room = Location("Assistant's Room", 'tar', cut_portrait = True, enter_break_labels = ['tar_no_access'], enter_labels = ['tar_enter'], exit_labels = ['tar_exit'], area = 'house')
        living_room.connection_tar = living_room.add_connection(terri_the_assistant_room, condition = "terri.has_tag('assistant') and living_room.is_empty")
        terri_the_assistant_room.connection_lr = terri_the_assistant_room.add_connections(living_room)

        # Park for Terri's Hypnotist Assistant Training
        terri_secluded_park = Location("Secluded Park", 'tsp', cut_portrait = True, enter_break_labels = ['tsp_no_access'], enter_labels = ['tsp_enter'], exit_labels = ['tsp_exit'])
        # Coffee Shop for Terri's Hypnotist Assistant Training
        terri_quiet_coffee_shop = Location("Quiet Coffee Shop", 'qcs', cut_portrait = True, enter_break_labels = ['qcs_no_access'], enter_labels = ['qcs_enter'], exit_labels = ['qcs_exit'])

        ## Character Specific Items
        lollipop_terri = Item('Lollipop', 'lpt', with_examine = True)
        lollipop_terri.action_buy_it = lollipop_terri.add_action("Buy it", label = '_buy', condition = "player.location == coffee_shop and terri.has_tag('adult_baby') and not player.has_item(lollipop_terri)")
        lollipop_terri.action_give_terri = lollipop_terri.add_action("Give to [terri.name]", label = '_give_terri', condition = "player.has_item(lollipop_terri) and terri.has_tag('adult_baby')")
        lollipop_terri.action_throw_away = lollipop_terri.add_action("Throw away", label = '_throw_away', condition = "player.has_item(lollipop_terri)")


        ## Other
        terri.change_status("available_to_be_client")

        # Start Day Events
        start_day_labels.append('terri_start_day')

        ########### VARIABLES ###########
        # Common Character Variables
        terri.add_stats_with_value('hypno_blowjob_count', 'hypno_facial_count', 'hypno_orgasm_count', 'hypno_sex_count', 'hypno_swallow_count')

        # Character Specific Variables
        terri.add_stats_with_value('adult_baby_outfit', 'adult_baby_toy_outfit', 'adult_baby_crawl_outfit', 'ass_lick_count', 'assistant_must_train_by_week', 'assistant_training_count', 'blowjob_training_count', 'bondage_sex_count', 'cheerleader_outfit_visit', 'diaper_outfit_count', 'diaper_play_preference', 'discussed_transformation', 'futanari_outfit', 'hypno_insecurities_count')
        terri.add_stats_with_value('lesbian_clues', 'lesbian_confronted', 'lesbian_is_pervert_disclosure', 'lingerie_action_used', 'maintain_week_baby', 'orgasm_with_dildo', 'orgasm_with_you', 'pleasure_her_action_used', 'ready_for_domme', 'ready_for_marilyn', 'sex_training_count', 'strip_masturbate_dildo_options', 'youth_interest', 'boobjob_interest', 'sleep_depth', 'visit_sex_count', 'doll_dress_state')
        terri.add_stats_with_value('state',value = 1)

        ######## EXPANDABLE MENUS #######
        ## Weekend Training
        terri_talk_expandable_menu = ExpandableMenu("What do you talk to her about?", cancelable = False)
        # note: these don't have to be defined in pregame, can be added in game
        terri.choice_talk_lesbian_perversion =  terri_talk_expandable_menu.add_choice("Why is lesbianism a perversion?", "terri_talk_lesbian_perversion", condition = "terri.lesbian_is_pervert_disclosure == 1")
        terri.choice_talk_sex_boyfriend =  terri_talk_expandable_menu.add_choice("Do you enjoy sex with your boyfriend?", "terri_talk_sex_boyfriend", condition = "not terri.has_tag('sex_with_boyfriend_discussion') and terri.lesbian_clues > 1")
        terri.choice_talk_orgasm_you =  terri_talk_expandable_menu.add_choice("What were you thinking about when you came on my tongue?", "terri_talk_orgasm_you", condition = "terri.orgasm_with_you == 2")
        terri.choice_talk_orgasm_dildo =  terri_talk_expandable_menu.add_choice("What were you thinking when you came with the dildo?", "terri_talk_orgasm_dildo", condition = "terri.orgasm_with_dildo == 1 or terri.orgasm_with_dildo == 2")
        terri.choice_talk_being_lesbian =  terri_talk_expandable_menu.add_choice("Being a lesbian", "terri_talk_being_lesbian", condition = "terri.lesbian_clues > 3 and terri.lesbian_confronted < 3")
        terri.choice_talk_how_feeling =  terri_talk_expandable_menu.add_choice("How are you feeling?", "terri_talk_how_feeling")
        terri.choice_talk_nothing =  terri_talk_expandable_menu.add_choice("Nothing", "terri_talk_nothing")

    return

# Initial Contact Message
# OBJECT: Check Messages
label terri_message:
    terri.c "{i}Hi. My name is [terri.name].{/i}"
    terri.c "{i}I'm not sure if you can help me or not. My boyfriend doesn't know that I'm doing this, but I want to be a better girlfriend for him. I don't feel like I know how to properly please him.{/i}"
    terri.c "{i}I'm 25, but I don't have a lot of experience with relationships. I'm hoping maybe you could assist me, and show me what I should be doing?{/i}"
    terri.c "{i}I know that technically this would count as cheating on my boyfriend, but I'm doing it to become a better girlfriend for him, so I'm hoping that makes it okay.{/i}"
    terri.c "{i}I can be available to meet any evening during the week, but I'm not around from Friday through Sunday, as I spend that time at my boyfriend's, and I don't want him to know about this.{/i}"
    call consider_contract(terri, "Reply to [terri.full_name]") from _call_consider_contract_7
    if yesno == True:
        sys "You accept the assignment. You have until the end of week [terri.training_limit] to complete it."
        sys "You may hold one evening session each week to complete her training. [terri.name] spends the weekend with her boyfriend and is not available for weekend sessions."
    return

# Client Rejected
label terri_rejected:
    sys "You can no longer train [terri.full_name]."
    return

# Arrange Client Session
# OBJECT: Schedule Client Session
label terri_calling:
    # Check if client has already been trained this week
    if not terri.can_be_interacted:
        "You had an evening session with [terri.name] earlier this week. You need to wait until the weekend or next week for another session."
    else:
        if terri.ready_for_marilyn == 1 or terri.ready_for_domme == 1:
            $ title = "What type of session do you want to have with [terri.name]?"
            menu:
                "Set up meeting with [marilyn.name] (ends training)" if terri.ready_for_marilyn == 1:
                    $ terri.ready_for_marilyn = 2
                "Set up meeting with [cassandra.name] the Domme (ends training)" if terri.ready_for_domme == 1:
                    $ terri.ready_for_domme = 2
                "Normal session":
                    pass
        call forced_movement(living_room) from _call_forced_movement_185
        call terri_state_check from _call_terri_state_check ## sets her image for the visit
        summon terri
        $ terri.visit_count += 1
        if 'first_visit' in terri.tags:
            wt_image terri.image
            "[terri.name] arrives at your door right on time. A short, slim, pretty redhead, you guess she's a little older than she looks. You show her to your living room."
            if not player.has_tag('first_client_visit_message'):
                wt_image current_location.image
                add tags 'first_client_visit_message' to player
                sys "[player.first_client_visit_message_text]"
        # finishing scene with Marilyn, ends training
        elif terri.ready_for_marilyn == 2:
            summon marilyn
            $ terri.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
            wt_image indy_marilyn_1_1
            "[marilyn.name] arrives before [terri.name].  It's strange to see [marilyn.name] with her hair dyed black and wearing a matronly frock, but the ensemble works well for the role she's about to play."
            wt_image indy_marilyn_1_2
            "When [terri.name] arrives, you let her know what's in store for her."
            wt_image indy_marilyn_1_3
            player.c "There's someone very important here to spend some time with you today, [terri.name]."
            wt_image indy_marilyn_1_4
            terri.c "Who is it?"
            wt_image indy_marilyn_1_5
            player.c "It's your Mommy, come to visit you for the day."
            wt_image indy_marilyn_1_1
            marilyn.c "Hello, child.  It's so good to see you."
            wt_image indy_marilyn_1_6
            terri.c "But my Mommy is ..."
            wt_image indy_marilyn_1_1
            marilyn.c "Hush, child, don't be so literal.  Don't you miss your Mommy?  Wouldn't you like to spend today with her?"
            wt_image indy_marilyn_1_7
            terri.c "I miss her terribly."
            wt_image indy_marilyn_1_1
            marilyn.c "And she misses you, child.  Look how beautiful you've become!  How long has it been since Mommy's seen you?"
            wt_image indy_marilyn_1_8
            terri.c "She died when I was 11 years old.  Do you really think she'd think I was beautiful?  I wasn't very pretty as a child, I was awkward and gangly while I was growing up."
            wt_image indy_marilyn_1_1
            marilyn.c "You've always been beautiful to Mommy, now the whole world can see what I've always seen."
            wt_image indy_marilyn_1_9
            terri.c "Thank you, Mo ... Ma'am.  That's sweet of you to say."
            wt_image indy_marilyn_1_10
            marilyn.c "Don't be so formal, you never called me Ma'am growing up.  I want my little girl to call me what she always called me."
            wt_image indy_marilyn_1_11
            terri.c "Yes ... Mommy."
            wt_image indy_marilyn_1_12
            marilyn.c "Doesn't that feel good?"
            terri.c "It feels great.  Thank you for letting me call you, Mommy.  It's nice to be able to spend time with her - with you, I mean - again."
            wt_image indy_marilyn_1_13
            marilyn.c "The pleasure is all mine.  How has your school work been going?"
            wt_image indy_marilyn_1_14
            terri.c "It's going really well, I think.  I've been learning a lot in my training."
            marilyn.c "But you're still having trouble with your feelings about girls, aren't you?"
            wt_image indy_marilyn_1_15
            terri.c "I'm sorry, Mommy.  I try hard not to cause trouble.  Liking girls is a perversion, and I try very hard not to."
            wt_image indy_marilyn_1_16
            marilyn.c "Well of course it is!  Perversions are what get little girls all warm and tingly between their legs.  Doesn't the thought of kissing another girl get you all warm and tingly between your legs?"
            wt_image indy_marilyn_1_17
            "[terri.name] nods in shame."
            terri.c "But I remember what you - I mean, what my real Mommy - taught me.  That I shouldn't kiss girls."
            wt_image indy_marilyn_1_15
            marilyn.c "In public child!  Where other people can see you!!  When your Mommy was still alive, that was still a big thing.  She was just trying to protect you.  That doesn't apply here, in private, where you're nice and safe and comfortable and can just relax and be yourself.  When you're alone at home, you can kiss all the girls you want to!"
            wt_image indy_marilyn_1_18
            terri.c "Really??  Are you saying I misunderstood her?"
            wt_image indy_marilyn_1_19
            marilyn.c "You were only 11 years old, child.  You weren't old enough yet for her to explain everything to you.  She told you what she thought you needed to know to keep you safe.  She would never have let you feel bad about liking girls if she'd been here when you were growing up."
            wt_image indy_marilyn_1_20
            "[terri.name] looks like she's about to cry as years of self-guilt start to wash out of her."
            wt_image indy_marilyn_1_21
            marilyn.c "It's okay, child."
            "[terri.name] moans softly as [marilyn.name] gives her a soft kiss on the cheek."
            wt_image indy_marilyn_1_22
            marilyn.c "Your trainer was right, child.  You really do need Mommy to help you feel better about yourself."
            wt_image indy_marilyn_1_23
            "[terri.name] seems to melt as [marilyn.name] completes her thought by licking the redhead's neck."
            terri.c "oohhhh ... yes, Mommy!"
            wt_image indy_marilyn_1_13
            marilyn.c "Your trainer knows you better than I do.  Let's ask him how best Mommy can help you?"
            $ title = "What does [terri.name] need most?"
            menu menu_terri_marilyn_options_menu:
                "Start with kissing practice" if not terri.has_tag('kissed_marilyn'):
                    add tags'kissed_marilyn' to terri
                    wt_image indy_marilyn_1_24
                    "The two women seem happy with that suggestion."
                    wt_image indy_marilyn_1_25
                    "[marilyn.name] takes the initiative ..."
                    wt_image indy_marilyn_1_26
                    "... showing [terri.name] how to kiss another woman."
                    wt_image indy_marilyn_1_27
                    "The redhead proves an eager student, aggressively extending the kiss as [marilyn.name] pulls back."
                    wt_image indy_marilyn_1_13
                    marilyn.c "I think my little girl is going to be good at kissing women.  What else do you think she needs from Mommy?"
                    jump menu_terri_marilyn_options_menu
                "More kissing practice" if terri.has_tag('kissed_marilyn'):
                    wt_image indy_marilyn_1_12
                    marilyn.c "You heard your trainer, child.  Show him how well you can kiss Mommy."
                    wt_image indy_marilyn_1_27
                    "[terri.name] eagerly seeks out the older woman's mouth."
                    wt_image indy_marilyn_1_26
                    "The two of them kiss ..."
                    wt_image indy_marilyn_1_25
                    "... their lips gradually opening more and more as their tongues probe each other's mouth ..."
                    wt_image indy_marilyn_1_24
                    "... as [terri.name] becomes more and more excited."
                    terri.c "oohhhh"
                    wt_image indy_marilyn_1_13
                    marilyn.c "That was good, little girl.  Mommy enjoyed that, but you liked it even more, didn't you?"
                    terri.c "Yes, Mommy.  I'm very tingly between my legs, now."
                    jump menu_terri_marilyn_options_menu
                "A firm hand":
                    wt_image indy_marilyn_1_29
                    marilyn.c "I'm not surprised.  A girl who lost her mother so young likely didn't get nearly enough discipline growing up.  Get on your knees, child."
                    wt_image indy_marilyn_1_30
                    marilyn.c "I'm not going to have a child of mine trying to have sex with other women without knowing her way around a woman's body.  Lift up my dress."
                    terri.c "But Mommy ..."
                    wt_image indy_marilyn_1_31
                    marilyn.c "No 'buts'.  You're far too old never to have had your tongue inside a woman's snatch before.  Do as you're told and put your face between Mommy's legs."
                    terri.c "Yes, Mommy."
                    wt_image indy_marilyn_1_32
                    marilyn.c "Now follow my lead.  If I pull on your hair, it means you're licking too firmly.  If I push your head in, it means you're not licking firmly enough.  If I pull your head up or down, it means you haven't been paying enough attention to that area of my pussy."
                    wt_image indy_marilyn_1_33
                    "You're pretty sure [marilyn.name] is mostly getting off on bossing [terri.name] around and watching her struggle to follow orders, but even so, [terri.name] gains some valuable experience on how to pleasure another woman."
                    wt_image indy_marilyn_1_34
                    marilyn.c "That's good, child.  You follow directions very well.  Time to teach you how to pleasure women in another way."
                    wt_image indy_marilyn_1_35
                    marilyn.c "Not every woman's going to want you to pleasure her asshole, but some of the dominant ones will before they'll let you make them cum, and I expect my child to know how to please a Domme's anus just as much as she can please her pussy."
                    wt_image indy_marilyn_1_36
                    marilyn.c "Get your clothes off, child, and get over here and stick your tongue in my butt."
                    wt_image indy_marilyn_1_37
                    "As [terri.name] does so, [marilyn.name] reaches a hand back ..."
                    wt_image indy_marilyn_1_38
                    "... and directs the redhead on how to eat ass, the same way she taught her how to eat pussy."
                    wt_image indy_marilyn_1_39
                    "[marilyn.name]'s a patient teacher, and keeps [terri.name] in place until there's no hint of any remaining reluctance to stick her tongue deep into [marilyn.name]'s asshole."
                    wt_image indy_marilyn_1_40
                    marilyn.c "Good girl.  For learning that lesson so well, I'm going to let you make me cum now."
                    wt_image indy_marilyn_1_41
                    "As [marilyn.name] pulls her head forward ..."
                    wt_image indy_marilyn_1_42
                    "... [terri.name] laps enthusiastically at the older woman's pussy, seemingly eager to taste a woman's cum for the first time."
                    wt_image indy_marilyn_1_43
                    "[marilyn.name] doesn't keep her waiting long."
                    wt_image indy_marilyn_1_44
                    marilyn.c "Oohhhhhh"
                    wt_image indy_marilyn_1_45
                    marilyn.c "Good girl.  Keep licking until you're told you can stop.  Did that make you all sticky and tingly between the legs, child, making Mommy cum?"
                    terri.c "Uh huh"
                    wt_image indy_marilyn_1_46
                    marilyn.c "You can stop licking, child.  Since you've been such a good girl, Mommy's going to help you out with that tingling neediness."
                    wt_image indy_marilyn_1_47
                    "As [marilyn.name] fingers her pussy, teases her nipple, and licks her ear, a lifetime of sexual frustration rushes out of [terri.name] in a series of intense orgasms, so continuous you can't tell when one is ending and another one starting."
                    wt_image indy_marilyn_1_48
                    terri.c "Ooooohhhhh  OOOHHH!!!!  Ooooooooohhhhhh OOOHHH OHHH!!!!!  Oooooooohhhh OHHH!!!"
                    wt_image indy_marilyn_1_46
                    "When [terri.name] finally stops cumming, [marilyn.name] removes her fingers."
                    marilyn.c "Your pussy feels good now, doesn't it?"
                    terri.c "Yes, Mommy.  Very good."
                    wt_image indy_marilyn_1_49
                    marilyn.c "It's important to always remember your manners, child.  After a Domme makes you feel better, you need to show her how grateful you are to her."
                    terri.c "Yes, Mommy.  Is there anything I can do for you to thank you for teaching me how to cum from a woman's touch?"
                    wt_image indy_marilyn_1_50
                    marilyn.c "You can lie down while I sit on your face, child.  I have some phone calls to make.  You're going to eat me out while I make them."
                    wt_image indy_marilyn_1_51
                    "[marilyn.name] makes it clear that you're not welcome to listen in on her phone calls - and presumably [terri.name] won't be able to hear them, either, once [marilyn.name] sits on her face - so you step away and give her some privacy until she's finished with her business and with the use of [terri.name]'s mouth."
                    change player energy by -energy_short
                "A gentle hand":
                    wt_image indy_marilyn_1_12
                    marilyn.c "Of course I'll be gentle with her.  She's my little girl, I'm going to treat her right."
                    wt_image indy_marilyn_1_73
                    marilyn.c "Let me take a good look at you, child.  You've grown so much since I saw you last."
                    wt_image indy_marilyn_1_74
                    marilyn.c "Oh, my!  Look at these pretty red panties.  Did you pick these out all by yourself?"
                    wt_image indy_marilyn_1_75
                    "[terri.name] giggles."
                    terri.c "Of course I did!  I'm a big girl, now."
                    wt_image indy_marilyn_1_76
                    marilyn.c "And now that you're a big girl, do you sometimes find yourself getting wet and sticky between your legs?  Especially when you think about pretty girls wth silky-smooth skin?"
                    terri.c "Yes, Mommy.  Sometimes."
                    wt_image indy_marilyn_1_77
                    marilyn.c "Mommy has that same problem, child, especially when she thinks of pretty, fair-haired girls who have never been with another woman.  Here's what I do when that happens."
                    wt_image indy_marilyn_1_54
                    marilyn.c "I find a pretty girl and I take her somewhere private where the two of us can be alone and no one can see us."
                    wt_image indy_marilyn_1_62
                    marilyn.c "Then I have her kiss me, like this, and place her hand between my legs, like this."
                    terri.c "oooohhhh!"
                    wt_image indy_marilyn_1_63
                    marilyn.c "Then I push her head down between my legs ..."
                    wt_image indy_marilyn_1_64
                    marilyn.c "... and I make her lick and finger me ..."
                    wt_image indy_marilyn_1_65
                    marilyn.c "... and I keep her there until the tingly, needy feeling washes away."
                    wt_image indy_marilyn_1_66
                    terri.c "Ooooohhhhh  OOOHHH!!!!  Ooooooooohhhhhh OOOHHH OHHH!!!!!  Oooooooohhhh OHHH!!!"
                    wt_image indy_marilyn_1_67
                    "A lifetime of sexual frustration rushes out of [terri.name] in a series of intense orgasms, so continuous you can't tell when one is ending and another one starting."
                    wt_image indy_marilyn_1_68
                    "[marilyn.name] patiently licks away at the redhead's gushing pussy, swallowing each new flood of juices as the younger woman lets herself experience true sexual gratification for the first time."
                    wt_image indy_marilyn_1_69
                    "When [terri.name] finally stops cumming, [marilyn.name] licks her face possessively."
                    wt_image indy_marilyn_1_70
                    marilyn.c "My little girl's pussy feels good now, doesn't it?"
                    terri.c "Uh huh"
                    wt_image indy_marilyn_1_35
                    marilyn.c "It's important to always remember your manners.  Once someone makes you feel better, you need to thank her properly.  Do you know how to lick a woman's pussy, child?"
                    wt_image indy_marilyn_1_71
                    "[terri.name] shakes her head 'no'."
                    wt_image indy_marilyn_1_72
                    marilyn.c "That's okay, child.  I'll teach you.  Put your mouth down here."
                    wt_image indy_marilyn_1_43
                    marilyn.c "No, not like that.  Lick around the labia first, then stick your tongue into the hole and start probing."
                    wt_image indy_marilyn_1_45
                    marilyn.c "Wait.  Work yourself up slowly towards the clit.  I'll tell you when you can touch that.  Lick down here first."
                    wt_image indy_marilyn_1_41
                    marilyn.c "Here, let me show you.  Follow my lead, I'll show you where your lips and tongue should be and what direction to move them."
                    wt_image indy_marilyn_1_42
                    "It seems [terri.name] isn't any more naturally gifted at orally pleasuring women than she is at orally pleasuring men. Both she and [marilyn.name], however, seem happy to take their time to improve her technique."
                    wt_image indy_marilyn_1_44
                    "This is going to take a while.  You leave them to their training."
                    change player energy by -energy_short
                "An opportunity to nurse":
                    wt_image indy_marilyn_1_52
                    marilyn.c "That's a great idea.  When's the last time you nursed, child?"
                    wt_image indy_marilyn_1_11
                    terri.c "Nursed?  I'm too old to nurse, Mommy."
                    wt_image indy_marilyn_1_53
                    marilyn.c "Nonsense!  You're nervous and confused.  Nursing will comfort you.  Let's make you comfortable and then you can suckle Mommy's breast and everything will be all right."
                    wt_image indy_marilyn_1_54
                    "[terri.name] hesitates at first as [marilyn.name] offers her ample boob ..."
                    wt_image indy_marilyn_1_55
                    "... then opens her mouth ..."
                    wt_image indy_marilyn_1_56
                    "... and starts suckling."
                    wt_image indy_marilyn_1_57
                    marilyn.c "There.  Doesn't that make everything feel better?"
                    wt_image indy_marilyn_1_58
                    "Still suckling happily at [marilyn.name]'s teat, [terri.name] nods."
                    wt_image indy_marilyn_1_57
                    marilyn.c "Good.  No more silly questioning about why you want to kiss girls, okay?  If kissing girls makes my little girl happy, I want you to kiss every girl you like.  Does the thought of that make my little girl's nipples hard and throbby?"
                    wt_image indy_marilyn_1_59
                    "[marilyn.name] doesn't wait for [terri.name] to reply before pinching her nipple and confirming for herself how hard and throbbing it is."
                    terri.c "oohhhh!  Yes, Mommy!"
                    wt_image indy_marilyn_1_60
                    marilyn.c "And when Mommy bites and nibbles on your hard little nipples, does that make you sticky and tingly between your legs?"
                    terri.c "oohhhh!!  Yes, Mommy!!"
                    wt_image indy_marilyn_1_61
                    marilyn.c "Mommy has that same problem, child.  Here's what I do.  I find a pretty, fair-haired girl and I take her somewhere private where the two of us can be alone and no one can see us."
                    wt_image indy_marilyn_1_62
                    marilyn.c "Then I have her kiss me, like this, and place her hand between my legs, like this."
                    terri.c "oooohhhh!"
                    wt_image indy_marilyn_1_63
                    marilyn.c "Then I push her head down between my legs ..."
                    wt_image indy_marilyn_1_64
                    marilyn.c "... and I make her lick and finger me ..."
                    wt_image indy_marilyn_1_65
                    marilyn.c "... and I keep her there until the tingly, needy feeling washes away."
                    wt_image indy_marilyn_1_66
                    terri.c "Ooooohhhhh  OOOHHH!!!!  Ooooooooohhhhhh OOOHHH OHHH!!!!!  Oooooooohhhh OHHH!!!"
                    wt_image indy_marilyn_1_67
                    "A lifetime of sexual frustration rushes out of [terri.name] in a series of intense orgasms, so continuous you can't tell when one is ending and another one starting."
                    wt_image indy_marilyn_1_68
                    "[marilyn.name] patiently licks away at the redhead's gushing pussy, swallowing each new flood of juices as the younger woman lets herself experience true sexual gratification for the first time."
                    wt_image indy_marilyn_1_69
                    "When [terri.name] finally stops cumming, [marilyn.name] licks her face possessively."
                    wt_image indy_marilyn_1_70
                    marilyn.c "My little girl's pussy feels good now, doesn't it?"
                    terri.c "Uh huh"
                    wt_image indy_marilyn_1_35
                    marilyn.c "It's important to always remember your manners.  Once someone makes you feel better, you need to thank her properly.  Do you know how to lick a woman's pussy, child?"
                    wt_image indy_marilyn_1_71
                    "[terri.name] shakes her head 'no'."
                    wt_image indy_marilyn_1_72
                    marilyn.c "That's okay, child.  I'll teach you.  Put your mouth down here."
                    wt_image indy_marilyn_1_43
                    marilyn.c "No, not like that.  Lick around the labia first, then stick your tongue into the hole and start probing."
                    wt_image indy_marilyn_1_45
                    marilyn.c "Wait.  Work yourself up slowly towards the clit.  I'll tell you when you can touch that.  Lick down here first."
                    wt_image indy_marilyn_1_41
                    marilyn.c "Here, let me show you.  Follow my lead, I'll show you where your lips and tongue should be and what direction to move them."
                    wt_image indy_marilyn_1_42
                    "It seems [terri.name] isn't any more naturally gifted at orally pleasuring women than she is at orally pleasuring men. Both she and [marilyn.name], however, seem happy to take their time to improve her technique."
                    wt_image indy_marilyn_1_44
                    "This is going to take a while.  You leave them to their training."
                    change player energy by -energy_short
                "Let them sort it out themselves (skip scene)":
                    wt_image indy_marilyn_1_28
                    "[marilyn.name] is more than capable of handling [terri.name] on her own from here.  You leave them alone and retire early for the evening."
                    change player energy by -energy_very_short
            call character_location_return(marilyn) from _call_character_location_return_700
            call character_location_return(terri) from _call_character_location_return_701
            wt_image phone_1
            "The next morning, [terri.name] calls you."
            wt_image indy_phone_1
            terri.c "Thank you so much for taking the time to set that up yesterday."
            wt_image indy_phone_2
            terri.c "I can't explain why I was being so foolish before, but that setting really helped me to truly hear and accept what she was saying - the same thing you've been saying."
            wt_image indy_phone_3
            terri.c "This is who I am. I need to accept it. Women turn me on. Men don't. I wish it was different, but it isn't, and I have to learn to be okay with that. Hearing Mommy say it was okay really helped. Now I have to do the rest myself."
            wt_image indy_phone_1
            terri.c "Thank you so much. When I hired you, I had no idea you'd be able to help me this much. I hope we can stay in touch."
            wt_image current_location.image
            "She leaves a glowing review on your profile."
            call convert(terri,"satisfied", False, True) from _call_convert_98
            call terri_convert_lesbian from _call_terri_convert_lesbian
            add tags 'continuing_actions' 'janice_talk_option_possible' 'marilyn_talk_option_possible' to terri
            add tags 'terri_reward_pending' to marilyn
            $ marilyn.independent_encounter_status = 2
            $ marilyn.rewards_pending += 1
            sys "You should check in with [marilyn.name] to hear how she felt about the experience."
            notify
            end_day
        # finishing scene with Cassandra, ends training
        elif terri.ready_for_domme == 2:
            summon cassandra
            $ terri.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
            wt_image indy_cassandra_24
            "[cassandra.name] is eager to meet [terri.name].  She joins you at your house before [terri.name] arrives so you can explain to her what to expect."
            wt_image indy_cassandra_25
            cassandra.c "This is going to be fun!  If she really is a suppressed lesbian and as obedient as you say, I'm sure I can help her."
            wt_image indy_cassandra_2
            "You meet [terri.name] at the door and show her in."
            wt_image indy_cassandra_26
            player.c "I have something special arranged for you today, [terri.name]."
            wt_image indy_cassandra_27
            terri.c "Yes, I remember you told me you would have a surprise for today's session.  Should I be nervous?"
            wt_image indy_cassandra_28
            player.c "Not at all.  [terri.name], this is [cassandra.name]."
            wt_image indy_cassandra_29
            terri.c "Oh.  Umm, is she here to help me with my training?"
            wt_image indy_cassandra_30
            player.c "Indeed she is.  I've taught you how important it is to be obedient to your boyfriend in order to please him."
            wt_image indy_cassandra_31
            terri.c "Yes, [terri.your_respect_name]."
            wt_image indy_cassandra_32
            player.c "[cassandra.name] has a lot of experience in teaching girls to be obedient.  She's a Domme, [terri.name], and from now on you will refer to her as 'Mistress'."
            wt_image indy_cassandra_33
            terri.c "Mistress?"
            wt_image indy_cassandra_34
            player.c "That's right.  You'll obey her the way you'd obey your boyfriend, or obey me.  I'm turning you over to her to complete your training."
            wt_image indy_cassandra_35
            cassandra.c "Don't be frightened, child.  Come, sit down on the bed beside me."
            wt_image indy_cassandra_4
            terri.c "Okay, but ..."
            cassandra.c "Okay what?"
            wt_image indy_cassandra_36
            "[terri.name] stares at [cassandra.name], hesitating a moment before resuming."
            wt_image indy_cassandra_37
            terri.c "Okay, Mistress.  But I'm not sure how you're going to be able to train me to please my boyfriend."
            cassandra.c "The first thing you are going to do, child, is to stop thinking so much."
            wt_image indy_cassandra_4
            terri.c "Mistress?  I'm not sure I understand?"
            cassandra.c "You don't need to understand.  You need to obey.  You've been entrusted to me because someone who cares for you believes this is the best thing for you.  And I agree."
            wt_image indy_cassandra_38
            cassandra.c "From now on, I decide what you need and what you'll do.  Your only responsibility is to obey my instructions.  The only thing you need to think about is how to follow my instructions so as to please me.  Can you do that, child?"
            wt_image indy_cassandra_39
            "As [terri.name] hesitates, [cassandra.name] lifts the front of [terri.name]'s dress, showing a clear interest in the redhead's legs.  You can see the blush rising in [terri.name]'s cheeks, but she's too nervous or shocked to say anything."
            wt_image indy_cassandra_40
            "As [terri.name] remains silent, [cassandra.name] grips her firmly but carefully around the neck, securing control but cautious not to hurt [terri.name] as she does so."
            wt_image indy_cassandra_41
            cassandra.c "When I ask you a question, child, you'll answer it.  And you won't take an eternity thinking about it before you do so.  You'll share what's going on in your head.  I can't help you unless you're obedient and honest with me.  I'm only going to ask once more, can you follow my instructions?"
            terri.c "I'll try, Mistress."
            wt_image indy_cassandra_42
            cassandra.c "Trying is a start, but I expect actual obedience, not just attempted obedience.  It gets easier with practice, though.  I'm going to give you a simple order and you're going to follow it without thinking about it, understood?"
            wt_image indy_cassandra_38
            terri.c "Yes, Mistress, I'll try ... I mean, I'll do it."
            cassandra.c "Good.  Lift your dress up so I have a better view of your upper thighs."
            wt_image indy_cassandra_42
            terri.c "Mistress, why would you ..."
            cassandra.c "Stop thinking and lift your dress, child.  Now."
            wt_image indy_cassandra_43
            "Red-faced, [terri.name] does as she's told."
            cassandra.c "Better.  I know it's hard now, but it'll get easier in time.  Let's do something else easy, next.  Stand up.  You have beautiful, sexy legs by the way."
            wt_image indy_cassandra_44
            "[terri.name] gets shakily to her feet, as if her legs are struggling to support her.  She hears the compliment about her legs, but isn't sure how to respond, or even how she feels about it, so she says nothing, eyes downcast, as [cassandra.name] steps closer."
            cassandra.c "That's good, child.  See, you can follow instructions without hesitating.  Stay still, I'm going to kiss you."
            wt_image indy_cassandra_45
            terri.c "But Mistress, that's wrong.  Girls kissing other girls is wrong."
            wt_image indy_cassandra_46
            cassandra.c "Hush.  Your role is to obey, child.  I decide what's right and wrong.  If this is wrong, that's my responsibility, and I'm the one to blame.  You're only following orders.  Now, stand still."
            wt_image indy_cassandra_5
            "[cassandra.name] takes [terri.name]'s head in both hands, trapping it to prevent the younger woman from pulling away.  She then proceeds to give [terri.name] her first kiss with a woman."
            wt_image indy_cassandra_47
            "Held firm by the stronger woman, she can't escape the soft lips and tongue exploring her mouth.  She doesn't want to fight it. Her nipples are hard and her cunt wet, and she's filled with an overwhelming sense of pleasure ... and shame."
            wt_image indy_cassandra_48
            cassandra.c "Don't move child, there's something else I want to do with you."
            wt_image indy_cassandra_49
            terri.c "Mistress, please don't look at me down there right now!"
            wt_image indy_cassandra_50
            cassandra.c "I have no intention of looking, I'm planning on touching, and I like what I feel.  You're wet under those panties."
            terri.c "I'm sorry, Mistress.  I enjoyed kissing you, and I shouldn't have.  Please stop, because I'm afraid I'm going to start enjoying this, too."
            wt_image indy_cassandra_51
            "In one swift motion, [cassandra.name] pulls the gray shift dress up and over [terri.name]'s head and throws her on the bed."
            wt_image indy_cassandra_52
            "Then she removes her own top and pants while keeping [terri.name] pinned ..."
            wt_image indy_cassandra_53
            "... before pulling her back off the bed and down to her knees."
            cassandra.c "Do you think for one moment that I give a rat's ass about what you are or are not enjoying??  When I tell you to do something, it's because I want you to do it.  And what are you supposed to do?"
            terri.c "Obey, Mistress.  I'm supposed to do what you tell me."
            wt_image indy_cassandra_54
            cassandra.c "And if I'm enjoying what you're doing for me or I'm doing with you, what does it matter whether it's making you wet between the legs or making you want to piss in fear?"
            terri.c "It doesn't, Mistress.  It doesn't matter at all as long as you're enjoying yourself."
            wt_image indy_cassandra_55
            cassandra.c "I knew there was a smart, obedient, good girl in there just waiting to be let out.  Show me you understand your role in our relationship."
            wt_image indy_cassandra_56
            "There's no hesitation this time as [terri.name] kisses [cassandra.name]'s feet.  A lifetime of pent-up lesbian desire fuels her eagerness to accept [cassandra.name] as an authority figure, knowing she'll be 'forced' to do things without being held accountable for whether they're 'right' or 'wrong'."
            wt_image indy_cassandra_17
            cassandra.c "I'm going to take you across my knees now and spank you, girl.  Get up here and lie across my lap."
            $ title = "Stay and watch?"
            menu:
                "Yes, watch [cassandra.name] dominate [terri.name]":
                    wt_image indy_cassandra_14
                    cassandra.c "This isn't going to be a gentle spanking, but it's for your own good.  If you ever think about back-sliding, if you ever think about questioning whether you should or shouldn't be doing what I tell you to do, you're going to remember this spanking and remember what I'm willing to do with you to enforce my rules."
                    wt_image indy_cassandra_16
                    cassandra.c "Give me permission to punish you, now and whenever I think you're too slow or too hesitant in following my instructions, or just not doing a good enough job at pleasing me."
                    wt_image indy_cassandra_15
                    terri.c "Yes, Mistress.  Punish me whenever you think I need it."
                    wt_image indy_cassandra_57
                    "[cassandra.name] begins the spanking, and as promised, she's not gentle ... *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*"
                    terri.c "OW!  OW!  OW!  OWW!!  OWW!!"
                    wt_image indy_cassandra_15
                    cassandra.c "How is your ass feeling, child?"
                    terri.c "Sore!  It's sore, Mistress."
                    wt_image indy_cassandra_58
                    "[cassandra.name] resumes the spanking.  It's clear [terri.name] is struggling to deal with the pain ... *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*"
                    terri.c "NNNN!!  NNNNNNNN!!!"
                    wt_image indy_cassandra_59
                    cassandra.c "Now how's your ass?"
                    terri.c "Very sore!!  It's very sore and burning, Mistress."
                    wt_image indy_cassandra_60
                    "Tapping into her reserves, [cassandra.name] makes the next set even harder, energetically swatting [terri.name]'s bruised rear, leaving the redhead too overwhelmed to do anything other than gasp silently ... *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*"
                    terri.c "NNNN!!  NNNNNNNN!!!"
                    wt_image indy_cassandra_61
                    cassandra.c "Now how does your ass feel?"
                    terri.c "HUUUUNNNNHHHHH"
                    wt_image indy_cassandra_62
                    "[terri.name]'s non-communicative state seems to have been what [cassandra.name] was aiming for.  She stops spanking [terri.name] and finishes undressing her ..."
                    wt_image indy_cassandra_63
                    "... and herself ..."
                    wt_image indy_cassandra_64
                    "... then pulls [terri.name] to her plump breasts."
                    wt_image indy_cassandra_65
                    cassandra.c "I know your bum's hurting child, but suckle on Mistress and it'll soothe you."
                    wt_image indy_cassandra_66
                    cassandra.c "Gentle, child!  Mistress' boob isn't going anywhere.  Take your time."
                    wt_image indy_cassandra_9
                    cassandra.c "That's better.  Is nursing on Mistress' nipple helping you feel better?"
                    wt_image indy_cassandra_67
                    terri.c "Yes, Mistress, thank you.  I feel wonderful right now, cared for and safe."
                    wt_image indy_cassandra_68
                    cassandra.c "I promise, I'll take good care of you and keep you safe, child.  But right now I'm horny and I need you to look after Mistress."
                    terri.c "But Mistress, I don't know how."
                    wt_image indy_cassandra_69
                    cassandra.c "I'll teach you.  Stick out your tongue."
                    wt_image indy_cassandra_11
                    cassandra.c "Sometimes beginners shy away too much.  You need to get right in there and worship me with abandon.  Keep your tongue moving."
                    wt_image indy_cassandra_70
                    cassandra.c "What the hell are you doing down there?  Stop.  Just hold your tongue out and your face still for a moment."
                    wt_image indy_cassandra_71
                    "The big breasted Domme presses herself forward onto her pretty new sub's face and grinds herself to orgasm."
                    wt_image indy_cassandra_72
                    cassandra.c "AAHHH!!!!"
                    wt_image indy_cassandra_70
                    cassandra.c "That was absolutely terrible.  You really don't know your way around a pussy do you?"
                    wt_image indy_cassandra_68
                    terri.c "I'm sorry, Mistress."
                    cassandra.c "It's a good thing you're so damn beautiful, I could almost cum just from looking at you.  I won't mind taking the time to teach you to please me properly.  Lie down on the bed, face up.  I'm going to teach you how to do this properly."
                    wt_image indy_cassandra_22
                    terri.c "Yes, Mistress. Thank you, Mistress."
                    wt_image indy_cassandra_10
                    "It seems [terri.name] isn't any more naturally gifted at orally pleasuring women than she is at orally pleasuring men. Somehow, though, you suspect neither [cassandra.name] nor [terri.name] will mind rectifying that situation.  You leave them to their training.  You should check in with [cassandra.name] at the Club later to find out how things are going with her and [terri.name]."
                "No, [cassandra.name] can handle things from here":
                    wt_image indy_cassandra_14
                    "[cassandra.name] seems to have things - namely [terri.name] - well in hand.  You give her some privacy to finish converting [terri.name] into her submissive.  You should check in with [cassandra.name] at the Club later to find out how things are going with her and [terri.name]."
            call character_location_return(cassandra) from _call_character_location_return_702
            call character_location_return(terri) from _call_character_location_return_703
            wt_image phone_1
            "The next morning, [terri.name] calls you."
            wt_image indy_phone_3
            terri.c "Mistress informs me that I'll be under her instruction for quite a while.  I'm to move in with her, in order to better learn from her."
            wt_image indy_phone_2
            terri.c "She's forbidden me from seeing my boyfriend until she's finished with me.  I'm afraid I won't have time to continue my training with you, either, as she's going to be keeping me very busy."
            wt_image indy_phone_1
            terri.c "I just wanted to thank you for your training, and for putting me in Mistress' charge. I learned a lot from you, and I think I'm going to learn lots more from Mistress. Good bye!"
            wt_image current_location.image
            "She leaves a glowing review on your profile, increasing your reputation."
            call convert(terri,"satisfied", False, True) from _call_convert_99
            call terri_convert_lesbian from _call_terri_convert_lesbian_1
            add tags 'continuing_actions' 'janice_talk_option_possible' to terri
            $ cassandra.independent_encounter_status = 2
            change player energy by -energy_short notify
            call character_location_return(terri) from _call_character_location_return_704
            end_day
        # possible finishing scene with adult baby outcome
        elif terri.youth_interest == 6:
            wt_image indy_diaper_33
            "[terri.name] looks both nervous and excited as she arrives for her session."
            terri.c "Can I please show you something?"
            wt_image indy_diaper_1
            "You follow her into the boudoir. She climbs up on the bed and empties out a bag."
            terri.c "You've helped me to see how much I enjoy age play. What we've done has been incredible, but I want to go further."
            wt_image indy_diaper_34
            terri.c "I bought a bottle."
            wt_image indy_diaper_2
            terri.c "I've filled it today, but I'm hoping next time maybe you could fill it and warm it up for me?"
            wt_image indy_diaper_3
            "Without waiting for a response, she starts sucking on the baby bottle."
            wt_image indy_diaper_35
            "She finishes the bottle ..."
            wt_image indy_diaper_4
            "... then she pulls off her clothes to reveal the diaper she's wearing."
            wt_image indy_diaper_5
            "She crawls around for a bit ..."
            wt_image indy_diaper_36
            "... then gathers up the items from her bag."
            wt_image indy_diaper_6
            "Nervously, she sits and sucks on a soother."
            wt_image indy_diaper_7
            "Eventually she gets the courage to look up at you."
            $ title = "What do you tell her?"
            menu:
                "Get out of here weirdo":
                    wt_image indy_diaper_37
                    "You don't actually get the words out. The look on your face is enough for [terri.name]. She quickly gathers up her things, pulls on some clothes and bolts for the door."
                    dismiss terri
                    wt_image current_location.image
                    "You never see her again."
                    call convert(terri, 'unavailable') from _call_convert_100
                    #change player money by -terri.pay # not needed as 'trained_this_week' never added this visit
                "This is a step too far":
                    $ terri.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    player.c "This is a bit too far, [terri.name]. Do you think your boyfriend will enjoy seeing you like this?"
                    "She shakes her head 'no'."
                    player.c "I'm not sure continuing on this path will help you. How about we take a step back, and try again next week?"
                    "From behind the soother, you hear a soft ..."
                    terri.c '"Okay"'
                    wt_image indy_diaper_8
                    "She's clearly disappointed, but likely not surprised by your advice.  She gathers up her stuff.  She's too embarrassed to continue today's session."
                    $ terri.youth_interest = 7
                    wt_image indy_diaper_33
                "We'll find the right partner for you":
                    $ terri.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
                    player.c "This isn't for me, and it's not for your current boyfriend either, is it [terri.name]?"
                    "She shakes her head 'no'."
                    player.c "Don't worry. It is for someone. You're the most beautiful baby I've ever seen. We'll find you a good Mommy or Daddy."
                    wt_image indy_diaper_38
                    terri.c "Will they let me play with my teether?"
                    player.c "I'm sure they will."
                    "There's no point in continuing her sessions. She's found the right path for her. She leaves a glowing review for you."
                    dismiss terri
                    wt_image phone_1
                    "A few days later, she sends you a message telling you about the new life she's found with the best Mommy ever."
                    if terri.has_tag('love_potion_used'):
                        terri.c "{i}I hope we can stay in touch.  Mommy says it's okay, and we have such a connection.  I want you to know everything that's happening in my life, so I'll write often.{/i}"
                    $ player.extra_clients_fee_this_week += terri.pay # because it won't be picked up in normal end of week calcs because she'll already be off training
                    call convert(terri,"satisfied",False,True) from _call_convert_101
                "I need to buy a crib":
                    player.c "It seems I need to get a crib. Fortunately, there's room in my bedroom. Come by tomorrow, and it should be all set up for you."
                    wt_image indy_diaper_38
                    terri.c "Can I bring my teether?"
                    player.c "Of course you can. Now, it looks like you emptied your bottle. Let me fill that up for you with some nice warm milk."
                    wt_image indy_diaper_39
                    "[terri.name] beams at you, a look of pure joy on her face.  That evening, she leaves a glowing review for you.  The next morning she moves in."
                    "She keeps her job and her existing social life, and doesn't seem to want to get involved in yours.  On the weekends she does her own thing, although you're pretty sure her boyfriend is no longer in the picture."
                    "But every weekday evening, when she gets home from work she changes out of her normal clothes and into a diaper and sits in her crib.  When you pay attention to her, and bring her a bottle or let her out of the crib to crawl around, she's ecstatic.  When you don't, she plays quietly by herself. She seems happy."
                    $ player.extra_clients_fee_this_week += terri.pay # because it won't be picked up in normal end of week calcs because she'll already be off training
                    call convert(terri,"satisfied",False,True) from _call_convert_102
                    call terri_convert_adult_baby from _call_terri_convert_adult_baby
            change player energy by -energy_very_short notify
            end_day
        # possible finishing scene with hypnotist's assistant outcome; note, uses check against raw sos score, not 'test' function, as temporary and room modifiers and the like should not apply
        elif terri.has_tag('hypnosis_revealed') and terri.sos > 20 and player.has_tag('hypnotist') and not terri.has_tag('discussed_assistant_role'):
            $ terri.hypno_count = 5
            if terri.state == 1:
                wt_image indy_talk_state_1_1
            elif terri.state == 2:
                wt_image indy_talk_state_2_1
            elif terri.state == 3:
                wt_image indy_talk_state_3_4
            elif terri.state == 4:
                wt_image indy_talk_state_4_7
            elif terri.state == 5:
                wt_image indy_talk_state_5_2
            "[terri.name] arrives for your session with something on her mind."
            terri.c "I have something I need to discuss with you.  That thing you do with the hypnosis.  Getting inside people's heads.  Can you show me how to do that?"
            player.c "I'm not sure.  I have a talent for it.  I don't know if I can teach it to someone else.  Why?  Why do you want me to?"
            if terri.state == 1:
                wt_image indy_bj_1_state_1_1
            elif terri.state == 2:
                wt_image indy_bj_1_state_2_1
            elif terri.state == 3:
                wt_image indy_talk_state_3_3
            elif terri.state == 4:
                wt_image indy_talk_state_4_9
            elif terri.state == 5:
                wt_image indy_talk_state_5_3
            terri.c "You've really helped me.  I feel so much more confident now than when I came to you.  I want to learn how to help other people, help them with the demons in their head."
            player.c "You won't let me fully help you.  Let me hypnotize you again, and I can help with your demons."
            if terri.state == 1:
                wt_image indy_talk_state_1_2
            elif terri.state == 2:
                wt_image indy_hypno_state_2_2
            elif terri.state == 3:
                wt_image indy_hypno_state_3_5
            elif terri.state == 4:
                wt_image indy_hypno_state_4_5
            elif terri.state == 5:
                wt_image indy_hypno_state_5_5
            terri.c "No!  My demons are my own.  I don't want you poking around in my head.  Who knows what you could find?  But I can understand how it could be helpful, to some people.  I'd like to learn how to ease their suffering."
            if terri.state == 1:
                wt_image indy_hypno_state_1_2
            elif terri.state == 2:
                wt_image indy_hypno_state_2_1
            elif terri.state == 3:
                wt_image indy_talk_state_3_5
            elif terri.state == 4:
                wt_image indy_talk_state_4_11
            elif terri.state == 5:
                wt_image indy_portrait_state_5
            terri.c "Can you try teaching me?  Perhaps I could be your apprentice, or assistant or something?"
            "[terri.name] knew she was being hypnotized, when few people do. She may have an innate talent for this. And having her as your assistant may reduce the Energy it takes you to hypnotize people in your home. You may have to take time to train her, however, or she could get herself into trouble, as a little knowledge can be dangerous."
            $ title = "What do you do?"
            menu:
                "Accept her as your assistant":
                    player.c "Okay, I'm willing to give this a try.  I'll set up a room here for you, and you can assist me with my clients. Confidentially. They aren't to know you're here."
                    if terri.state == 1:
                        wt_image indy_bj_1_state_1_1
                    elif terri.state == 2:
                        wt_image indy_talk_state_2_2
                    elif terri.state == 3:
                        wt_image indy_talk_state_3_1
                    elif terri.state == 4:
                        wt_image indy_talk_state_4_3
                    elif terri.state == 5:
                        wt_image indy_bj_1_state_5_1
                    terri.c "And you'll teach me what you know?"
                    player.c "In time, when you're ready.  You'll need to keep your job, though, I'm not paying you."
                    if terri.state == 1:
                        wt_image indy_portrait_state_1
                    elif terri.state == 2:
                        wt_image indy_portrait_state_2
                    elif terri.state == 3:
                        wt_image indy_talk_state_3_2
                    elif terri.state == 4:
                        wt_image indy_talk_state_4_1
                    elif terri.state == 5:
                        wt_image indy_talk_state_5_3
                    terri.c "Thank you!  I can't wait to get started."
                    wt_image current_location.image
                    "That night, she leaves a glowing review for you online, increasing your reputation.  The next day, she moves into your house.  You set her up in her own room, with some books to study.  You're not sure she'll learn anything from them, but they'll keep her out of your hair."
                    wt_image indy_assistant_1
                    "[terri.name]'s eager to assist and does have some knack for hypnosis.  With her help, client hypnosis sessions now use less Energy than before. Of course, sometimes you need to banish her for the more 'sensitive' sessions, but most of the time she's able to observe and learn."
                    wt_image indy_assistant_27
                    "Make sure you spend time with her regularly to advance her studies, or she may get herself into trouble."
                    sys "Energy cost for future hypnosis in your house is reduced thanks to having an assistant."
                    $ player.extra_clients_fee_this_week += terri.pay # because it won't be picked up in normal end of week calcs because she'll already be off training
                    call convert(terri,"satisfied",False,True) from _call_convert_103
                    call terri_convert_assistant from _call_terri_convert_assistant
                    end_day
                "Keep this a client relationship":
                    add tags 'discussed_assistant_role' to terri
                    player.c "I'm sorry, [terri.name]. I don't think I can help you.  Let's just keep this a client relationship.  Shall we get on with our session?"
                    if terri.state == 1:
                        wt_image indy_talk_state_1_2
                    elif terri.state == 2:
                        wt_image indy_hypno_state_2_5
                    elif terri.state == 3:
                        wt_image indy_talk_state_3_9
                    elif terri.state == 4:
                        wt_image indy_talk_state_4_10
                    elif terri.state == 5:
                        wt_image indy_talk_state_5_8
                    terri.c "I suppose so."
        else:
            wt_image terri.image
            "[terri.name] smiles at you as she takes a seat in your living room."
    wt_image current_location.image
    return

# Display Portrait
# CHARACTER: Display Portrait
label terri_update_media:
    if terri.status == "post_training":
        if terri.has_tag('new_man'):
            $ terri.change_image('indy_new_man_1')
        elif terri.has_tag('futanari'):
            if terri.futanari_outfit == 2:
                $ terri.change_image('indy_futanari_2_2')
            else:
                $ terri.change_image('indy_futanari_1_25')
        elif terri.has_tag('adult_baby'):
            $ terri.change_image('indy_crib_1')
        elif terri.has_tag('assistant'):
            $ terri.change_image('indy_assistant_1')
        elif terri.has_tag('slavegirl'):
            if terri.has_tag('slavegirl_let_out'):
                $ terri.change_image('indy_slavegirl_2_3')
            else:
                $ terri.change_image('indy_slavegirl_1_1')
        elif terri.has_tag('doll'):
            $ terri.change_image('indy_doll_[terri.doll_dress_state]_1')
        elif terri.has_tag('cheerleader_visit_now'):
            if terri.has_tag('boob_job'):
                if terri.has_tag('strips_on_visit'):
                    $ terri.change_image('indy_cheerleader_2_5')
                else:
                    $ terri.change_image('indy_cheerleader_2_1')
            else:
                $ terri.change_image('indy_cheerleader_1_16')
        elif terri.has_tag('regular_visit_now'):
            if terri.has_tag('boob_job'):
                if terri.has_tag('strips_on_visit'):
                    $ terri.change_image('indy_boob_job_1_14')
                else:
                    $ terri.change_image('indy_boob_job_1_5')
            else:
                $ terri.change_image('indy_drink_1_19')
        elif terri.has_tag('boob_job'):
            $ terri.change_image('indy_boob_job_1_1')
        else:
            $ terri.change_image('indy_portrait_state_' + str(terri.state))
    else:
        $ terri.change_image('indy_portrait_state_' + str(terri.state))
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label terri_examine:
    if terri.has_tag('assistant_trouble'):
        wt_image indy_mirror_1_2
        "You touch her shoulder and she slumps forward against the mirror.  Was she trying self-hypnosis in front of the mirror?  It looks like she's placed herself into her own hypnotic trance."
        if day > 2:
            call terri_assistant_death from _call_terri_assistant_death
        else:
            wt_image indy_mirror_1_3
            "She's dehydrated from lack of fluids, but still alive.  You get her some water, and pour a bit in her mouth.  Most of it rolls back out."
            $ title = "What do you do?"
            menu menu_terri_examine_1:
                "Try hypnosis" if not terri.has_tag('examine_tried_hypnosis'):
                    wt_image indy_mirror_1_2
                    player.c "[terri.name], I want you to listen to me. Listen to my voice, [terri.name]. Only my voice. [terri.name], I want you to wake up now. Wake up [terri.name]. You are no longer hypnotized. You are wide awake and aware of everything around you."
                    "It doesn't work. You can't reach her. She's too far gone in her own self-induced trance."
                    add tags 'examine_tried_hypnosis' to terri
                    $ title = "What do you do?"
                    jump menu_terri_examine_1
                "Take her to the hospital":
                    wt_image indy_mirror_1_4
                    "She's as light as a feather as you pick her up.  You get her in the car and drive her to the Emergency Room."
                    wt_image indy_hospital_1
                    "They aren't able to revive her, but they get an IV in her and get her re-hydrated. That'll keep her alive. You're not her next-of-kin and you have no authority to provide health care instructions for her. Her care is out of your hands now."
                    wt_image police_interview
                    "The police drop by the next day to ask you some questions. You tell them what you know, except for your theory about self-hypnosis. There's no sign of trauma, so they're treating it as a spontaneous coma. You don't hear anything more on the matter."
                "Call [janice.name] the Lawyer" if player.has_tag('lawyer_on_retainer'):
                    wt_image lawyer_desk_1
                    player.c "[janice.name], I have a problem."
                    janice.c "That's what I'm here for."
                    "You explain the situation."
                    janice.c "Consider the problem solved. No charge. Someone will be by to pick her up in a few minutes."
                    player.c "What will happen to her?"
                    janice.c "If I told you that, I'd have to charge you. This won't come back to you, that's all you need to know."
                    wt_image living_room.image
                    "Two hours later, and there's no sign that [terri.name] had ever been in your house. Perhaps you should have got her medical attention, or tried harder to save her yourself. On the other hand, what's the point of having a high priced lawyer on retainer if you aren't going to rely on her to keep you out of trouble."
        call convert(terri, 'unavailable') from _call_convert_104
        dismiss terri
        call forced_movement(living_room) from _call_forced_movement_186
        wt_image living_room.image
    else:
        call terri_description_display from _call_terri_description_display
        wt_image current_location.image
    return

# Talk to Character
label terri_talk:
    if 'first_visit' in terri.tags:
        add tags 'talked_today' to terri
        wt_image indy_talk_state_1_1
        player.c "Thank you for contacting me, [terri.name].  Tell me a little more about your concerns."
        wt_image indy_talk_state_1_2
        terri.c "Well, it's kind of stupid, I guess.  But as I said in my email, I don't feel like I know how to please my boyfriend.  I don't have much experience with relationships."
        wt_image indy_bj_1_state_1_1
        terri.c "I never had a boyfriend in high school or university.  Now that I have one, I don't want to lose him."
        player.c "Do you love him?"
        wt_image indy_talk_state_1_3
        "She hesitates for just a moment before responding."
        terri.c "Yes, I think so.  He's very nice and treats me well.  I think he's the best chance I'll have to have a normal life. I don't want to mess it up."
        player.c "What do you mean a 'normal life'?"
        wt_image indy_bj_1_state_1_1
        terri.c "You know. A husband, maybe children some day."
        player.c "Is that what you want?"
        wt_image indy_talk_state_1_3
        terri.c "Isn't that what you're supposed to do, when you grow up?"
        player.c "I'm not sure you're 'supposed' to do anything when you grow up."
        wt_image indy_talk_state_1_2
        "She sighs."
        terri.c "Life was so much easier as a child.  I guess I'm a bit lost as an adult.  But I am sure my boyfriend is good for me, and I'm scared I'm going to screw it up."
        player.c "Why do you say that?"
        wt_image indy_talk_state_1_1
        terri.c "I don't know what I should be doing with him.  At any time, really. But especially sexually."
        player.c "Do you think he's unhappy with your sex life?"
        wt_image indy_talk_state_1_3
        terri.c "I can't tell.  He's such a nice guy, he'd never say anything if he thought it would hurt my feelings.  He knows he's my first.  When I ask him if there's anything I should be doing differently, he just says I did great and don't worry about it."
        player.c "Perhaps you shouldn't worry about it?"
        wt_image indy_talk_state_1_2
        "She shakes her head."
        terri.c "I'm sure our sex life could be better.  He doesn't have a lot of experience either.  I don't want some other woman to come along, someone who can give him what he really wants, and then I lose him."
        player.c "What does he really want?"
        wt_image indy_talk_state_1_1
        terri.c "I don't know!  You're the expert on training women to please men.  What do most men want in their woman?"
        $ title = "What do you tell her?"
        menu:
            "Youth and beauty":
                player.c "Youth and beauty rank pretty high for many men."
                "[terri.name] nods."
                wt_image indy_hypno_state_1_2
                terri.c "I get that.  I miss the days of my youth too. Even if I'm an adult now, maybe if I act young, he will see me that way.  Do you think that would help?"
                player.c "Anything that helps you feel more comfortable and relaxed will help.  Which means we also need to work on your comfort level with your sexual experience."
                wt_image indy_bj_1_state_1_1
                "She nods again."
                terri.c "Yes, I want that.  Please teach me how I should be pleasuring him."
                $ terri.youth_interest += 1
                sys "[terri.name] is now more interested in acting young."
            "Variety":
                player.c "Variety is important."
                wt_image indy_hypno_state_1_5
                terri.c "I was afraid you'd say that.  So it's pretty much certain that he will want to be with other women.  What should I do to make sure that he comes back and stays with me?"
                player.c "You can provide the variety, for starters.  What have the two of you done together?"
                wt_image indy_talk_state_1_2
                terri.c "I take him in my mouth, sometimes.  He seems to like that.  Other times, he puts his thing inside me."
                player.c "Inside you how?"
                wt_image indy_hypno_state_1_2
                terri.c "You know.  I lie down and open my legs, and he puts himself inside me."
                player.c "What else do you do together?"
                wt_image indy_bj_1_state_1_1
                terri.c "Oh, well, kiss of course.  And hold hands.  And we cuddle on the sofa together.  And sometimes after sex, he holds me before he falls asleep."
                player.c "I may be able to help you."
                wt_image indy_portrait_state_1
                terri.c "Oh good!  I was hoping you would."
                change terri resistance by -5 notify
            "Great in the sack":
                player.c "Being good in the sack certainly helps."
                wt_image indy_bj_1_state_1_1
                terri.c "I thought that was the case.  That's why I contacted you.  Can you help me get better at sex?"
                change terri resistance by -5 notify
            "Lesbian tendencies":
                player.c "Lesbian tendencies rank surprisingly high."
                wt_image indy_hypno_state_1_1
                terri.c "What?  Why would anyone want their girlfriend to be into something perverted like that? That doesn't even make sense.  If they're a lesbian, they aren't interested in men.  Why would a man want that?"
                player.c "Well, technically perhaps I should have said 'bisexual tendencies', although there are plenty of men who fantasize about sex with pure lesbians.  Perhaps it's the allure of the unattainable?  Lots of people are attracted to things they can't easily get."
                wt_image indy_hypno_state_1_5
                "[terri.name] seems to think for a moment and looks like she's about to say something.  Then she pauses before continuing."
                wt_image indy_talk_state_1_3
                terri.c "So, should I be playing hard to get?"
                player.c "Occasionally, yes, probably.  Although being a tease is likely more effective, especially if you can keep him wanting more for the moment.  Just remember to deliver often enough to leave him satisfied too."
                wt_image indy_bj_1_state_1_1
                terri.c "Can you show me?  How to tease him, and how to satisfy him, too?"
                $ terri.lesbian_is_pervert_disclosure = 1
                sys "[terri.name] had a strong reaction to that topic.  You could discuss it further with her later, if you want."
            "Obedience":
                player.c "Obedience is important for a lot of men."
                wt_image indy_talk_state_1_2
                "She nods."
                terri.c "Yes, I understand.  A lot of men want a woman who will do as he says.  But what should I do when he doesn't tell me what he wants?  Should I just sit around until he tells me he wants me?  Shouldn't I try to make things better for him?"
                player.c "I think that depends on your relationship with him.  Does your boyfriend tell you what he wants very often?"
                wt_image indy_talk_state_1_3
                terri.c "Almost never.  I wish he would sometimes.  Maybe then I wouldn't feel so uncertain about whether I'm truly pleasing him?"
                player.c "If we work on your obedience to me, it may help you to bring out greater decisiveness in your boyfriend.  And if we work on your skills, you'll be better able to please him at whatever he does demand of you.  For this to work, you will need to obey me as you would him.  Do you agree?"
                wt_image indy_hypno_state_1_2
                terri.c "Yes, I agree.  I'll obey you while you train me.  Thank you."
                change terri submission by 10 notify
            "Big boobs":
                player.c "Big boobs are important for a lot of men."
                wt_image indy_bj_1_state_1_1
                terri.c "I know!  Thank goodness my boyfriend doesn't seem to care about that."
                wt_image indy_talk_state_1_1
                terri.c "At least, I don't think he does.  He's never complained about the size of my breasts.  But he's not one to complain about things, generally."
                add tags 'discussed_boobs' to terri
                $ terri.boobjob_interest += 1
                sys "[terri.name] is now more self-conscious about the size of her breasts."
        # Add Client Actions
        rem tags 'no_hypnosis' 'first_visit' from terri
        wt_image current_location.image
    else:
        call expandable_menu(terri_talk_expandable_menu) from _call_expandable_menu_117
        wt_image current_location.image
    return

label terri_talk_lesbian_perversion:
    add tags 'talked_today' to terri
    if terri.state == 1:
        wt_image indy_talk_state_1_2
    elif terri.state == 2:
        wt_image indy_talk_state_2_4
    elif terri.state == 3:
        wt_image indy_talk_state_3_7
    elif terri.state == 4:
        wt_image indy_talk_state_4_10
    elif terri.state == 5:
        wt_image indy_talk_state_5_7
    player.c "[terri.name], you told me that lesbianism is a perversion.  Why do you say that?"
    if terri.state == 1:
        wt_image indy_hypno_state_1_1
    elif terri.state == 2:
        wt_image indy_hypno_state_2_2
    elif terri.state == 3:
        wt_image indy_talk_state_3_8
    elif terri.state == 4:
        wt_image indy_talk_state_4_11
    elif terri.state == 5:
        wt_image indy_talk_state_5_6
    "[terri.name] looks taken aback."
    terri.c "Well, isn't it?  That's what I was taught."
    player.c "Who taught you that?"
    if terri.state == 1:
        wt_image indy_talk_state_1_2
    elif terri.state == 2:
        wt_image indy_talk_state_2_4
    elif terri.state == 3:
        wt_image indy_talk_state_3_7
    elif terri.state == 4:
        wt_image indy_hypno_state_4_1
    elif terri.state == 5:
        wt_image indy_talk_state_5_8
    terri.c "My mother."
    player.c "Why did she say that?"
    if terri.state == 1:
        wt_image indy_talk_state_1_1
    elif terri.state == 2:
        wt_image indy_talk_state_2_5
    elif terri.state == 3:
        wt_image indy_talk_state_3_6
    elif terri.state == 4:
        wt_image indy_talk_state_4_4
    elif terri.state == 5:
        wt_image indy_hypno_state_5_1
    "[terri.name] looks embarrassed."
    terri.c "I did something wrong.  I was just a girl at the time.  My Mom died while I was quite young, only 11 years old.  This was a little before that, just after I started school.  I had a friend over for a sleepover.  Before the two of us went to bed, I kissed her."
    if terri.state == 1:
        wt_image indy_talk_state_1_3
    elif terri.state == 2:
        wt_image indy_hypno_state_2_2
    elif terri.state == 3:
        wt_image indy_hypno_state_3_5
    elif terri.state == 4:
        wt_image indy_talk_state_4_12
    elif terri.state == 5:
        wt_image indy_talk_state_5_6
    terri.c "My Mom was very upset.  She told me that girls who kiss other girls are perverts.  She told me I should only ever kiss boys, and warned me to never forget that.  I haven't."
    if terri.state == 1:
        wt_image indy_talk_state_1_2
    elif terri.state == 2:
        wt_image indy_hypno_state_2_5
    elif terri.state == 3:
        wt_image indy_hypno_state_3_2
    elif terri.state == 4:
        wt_image indy_talk_state_4_10
    elif terri.state == 5:
        wt_image indy_hypno_state_5_2
    "[terri.name] looks like she doesn't want to continue on this topic any longer. Best to move on to something else."
    $ terri.lesbian_is_pervert_disclosure = 2
    $ terri.lesbian_clues += 1
    add tags 'mom_died_young_reveal' to terri
    return

label terri_talk_sex_boyfriend:
    add tags 'talked_today' to terri
    if terri.state == 1:
        wt_image indy_talk_state_1_2
    elif terri.state == 2:
        wt_image indy_hypno_state_2_1
    elif terri.state == 3:
        wt_image indy_portrait_state_3
    elif terri.state == 4:
        wt_image indy_hypno_state_4_1
    elif terri.state == 5:
        wt_image indy_portrait_state_5
    player.c "[terri.name], do you enjoy having sex with your boyfriend?"
    if terri.state == 1:
        wt_image indy_bj_1_state_1_1
    elif terri.state == 2:
        wt_image indy_talk_state_2_1
    elif terri.state == 3:
        wt_image indy_talk_state_3_1
    elif terri.state == 4:
        wt_image indy_talk_state_4_1
    elif terri.state == 5:
        wt_image indy_talk_state_5_1
    terri.c "Of course I do!  He's wonderful.  He's very sweet and he's very good to me."
    player.c "But does it excite you when he touches you, or when you touch him?"
    if terri.state == 1:
        wt_image indy_talk_state_1_3
    elif terri.state == 2:
        wt_image indy_hypno_state_2_2
    elif terri.state == 3:
        wt_image indy_talk_state_3_9
    elif terri.state == 4:
        wt_image indy_talk_state_4_6
    elif terri.state == 5:
        wt_image indy_talk_state_5_2
    terri.c "I ... I'm not sure what you mean?"
    player.c "Have you ever had an orgasm while he's touching you?"
    if terri.state == 1:
        wt_image indy_talk_state_1_1
    elif terri.state == 2:
        wt_image indy_talk_state_2_5
    elif terri.state == 3:
        wt_image indy_talk_state_3_8
    elif terri.state == 4:
        wt_image indy_talk_state_4_7
    elif terri.state == 5:
        wt_image indy_portrait_state_5
    terri.c "I ... I think so."
    player.c "As strong as the orgasms you have when you masturbate?"
    if terri.state == 1:
        wt_image indy_hypno_state_1_1
    elif terri.state == 2:
        wt_image indy_talk_state_2_4
    elif terri.state == 3:
        wt_image indy_hypno_state_3_5
    elif terri.state == 4:
        wt_image indy_talk_state_4_8
    elif terri.state == 5:
        wt_image indy_hypno_state_5_5
    "She blushes, then looks upset."
    terri.c "No, but when he's touching me, it's normal.  And that's better.  Don't try to make it seem like there's something wrong with the two of us being together."
    player.c "I wasn't suggesting that, [terri.name]."
    if terri.state == 1:
        wt_image indy_talk_state_1_2
    elif terri.state == 2:
        wt_image indy_hypno_state_2_5
    elif terri.state == 3:
        wt_image indy_hypno_state_3_2
    elif terri.state == 4:
        wt_image indy_talk_state_4_10
    elif terri.state == 5:
        wt_image indy_hypno_state_5_2
    "[terri.name] looks like she doesn't want to continue on this topic any longer.  Best to move on to something else."
    $ terri.lesbian_clues += 1
    add tags 'sex_with_boyfriend_discussion' to terri
    return

label terri_talk_orgasm_you:
    add tags 'talked_today' to terri
    player.c "[terri.name], what were you thinking about when you came on my tongue?"
    if terri.state == 1:
        wt_image indy_hypno_state_1_2
    elif terri.state == 2:
        wt_image indy_talk_state_2_2
    elif terri.state == 3:
        wt_image indy_talk_state_3_3
    elif terri.state == 4:
        wt_image indy_talk_state_4_1
    elif terri.state == 5:
        wt_image indy_talk_state_5_1
    terri.c "What do you mean?  I was just thinking about how good it felt, that's all."
    player.c "Your eyes were closed.  Who were you thinking about?  Your boyfriend?  Someone else?"
    if terri.state == 1:
        wt_image indy_hypno_state_1_1
    elif terri.state == 2:
        wt_image indy_talk_state_2_4
    elif terri.state == 3:
        wt_image indy_talk_state_3_9
    elif terri.state == 4:
        wt_image indy_talk_state_4_6
    elif terri.state == 5:
        wt_image indy_hypno_state_5_1
    terri.c "What does it matter who I was thinking about?  It was normal, wasn't it?  You're a boy, I'm a girl.  I shouldn't have to feel bad about enjoying that, should I?"
    player.c "I didn't suggest you should feel bad about it.  I just want you to be honest with me, and tell me what you were thinking about while you were enjoying sex."
    if terri.state == 1:
        wt_image indy_talk_state_1_1
    elif terri.state == 2:
        wt_image indy_talk_state_2_5
    elif terri.state == 3:
        wt_image indy_hypno_state_3_5
    elif terri.state == 4:
        wt_image indy_talk_state_4_8
    elif terri.state == 5:
        wt_image indy_hypno_state_5_5
    "She blushes and looks embarrassed."
    terri.c "I don't see how that's relevant.  It was good.  I enjoyed it.  Now I want to get on with my training, so that my boyfriend can enjoy things too."
    $ terri.orgasm_with_you = 3
    $ terri.lesbian_clues += 1
    return

label terri_talk_orgasm_dildo:
    add tags 'talked_today' to terri
    if terri.orgasm_with_dildo == 1:
        player.c "[terri.name], what were you thinking about when you came while you were practicing on the dildo?"
        if terri.state == 1:
            wt_image indy_hypno_state_1_2
        elif terri.state == 2:
            wt_image indy_talk_state_2_2
        elif terri.state == 3:
            wt_image indy_talk_state_3_3
        elif terri.state == 4:
            wt_image indy_talk_state_4_2
        elif terri.state == 5:
            wt_image indy_talk_state_5_1
        terri.c "What do you mean?  I was just thinking about what you said.  About how I should learn how to be a better girlfriend by practicing on the dildo."
        player.c "Your eyes were closed.  Who were you thinking about?  Your boyfriend?  Someone else?"
        if terri.state == 1:
            wt_image indy_hypno_state_1_1
        elif terri.state == 2:
            wt_image indy_talk_state_2_4
        elif terri.state == 3:
            wt_image indy_talk_state_3_8
        elif terri.state == 4:
            wt_image indy_talk_state_4_3
        elif terri.state == 5:
            wt_image indy_hypno_state_5_1
        terri.c "You told me to close my eyes and relax!  What does it matter who I was thinking about?  It was normal, wasn't it? I came with a fake penis inside me, just like a woman is supposed to when she has a penis inside her, isn't she?  I shouldn't have to feel bad about enjoying that, should I?"
        player.c "I didn't suggest you should feel bad about it.  I just want you to be honest with me, and tell me what you were thinking about while you were enjoying sex.  Have you ever cum with a real penis inside you?"
        if terri.state == 1:
            wt_image indy_talk_state_1_1
        elif terri.state == 2:
            wt_image indy_talk_state_2_5
        elif terri.state == 3:
            wt_image indy_hypno_state_3_5
        elif terri.state == 4:
            wt_image indy_talk_state_4_5
        elif terri.state == 5:
            wt_image indy_talk_state_5_5
        "She blushes and looks embarrassed."
        terri.c "No, but I probably just need practice.  Isn't it a good sign that I was able to cum using the dildo? What does it matter what I was thinking about?  Now I want to get on with my training, so that my boyfriend can enjoy things too."
    elif terri.orgasm_with_dildo == 2:
        player.c "[terri.name], what were you thinking about when you came while you were practicing on the dildo?"
        if terri.state == 1:
            wt_image indy_hypno_state_1_2
        elif terri.state == 2:
            wt_image indy_talk_state_2_2
        elif terri.state == 3:
            wt_image indy_talk_state_3_3
        elif terri.state == 4:
            wt_image indy_talk_state_4_2
        elif terri.state == 5:
            wt_image indy_talk_state_5_1
        terri.c "What do you mean?  I was just thinking about what you said.  About how I should learn how to be a better girlfriend by practicing on the dildo."
        player.c "Who were you thinking about?  Your boyfriend?  Someone else?"
        if terri.state == 1:
            wt_image indy_talk_state_1_1
        elif terri.state == 2:
            wt_image indy_hypno_state_2_1
        elif terri.state == 3:
            wt_image indy_talk_state_3_1
        elif terri.state == 4:
            wt_image indy_talk_state_4_1
        elif terri.state == 5:
            wt_image indy_talk_state_5_4
        "She blushes and looks embarrassed."
        terri.c "I was thinking about being a naughty schoolgirl, and what it would have been like if I had been brave enough to get myself a dildo when I was a young girl.  Maybe I would have fantasized about real cocks more."
        player.c "You didn't fantasize about real cocks when you were a girl?  What did you fantasize about?"
        if terri.state == 1:
            wt_image indy_talk_state_1_3
        elif terri.state == 2:
            wt_image indy_talk_state_2_5
        elif terri.state == 3:
            wt_image indy_hypno_state_3_5
        elif terri.state == 4:
            wt_image indy_talk_state_4_5
        elif terri.state == 5:
            wt_image indy_hypno_state_5_2
        "She blushes a deeper shade of red."
        terri.c "That was a long time ago.  Isn't it a good sign that I was able to cum using the dildo?  What does it matter what I was thinking about?  Now I want to get on with my training, so that my boyfriend can enjoy things too."
    $ terri.lesbian_clues += 1
    $ terri.orgasm_with_dildo = 3
    return

label terri_talk_being_lesbian:
    add tags 'talked_today' to terri
    if terri.state == 1:
        wt_image indy_talk_state_1_2
    elif terri.state == 2:
        wt_image indy_talk_state_2_1
    elif terri.state == 3:
        wt_image indy_talk_state_3_8
    elif terri.state == 4:
        wt_image indy_hypno_state_4_1
    elif terri.state == 5:
        wt_image indy_portrait_state_5
    if terri.lesbian_confronted == 0:
        player.c "[terri.name], I think it's time we talk about something very important?"
        if terri.state == 1:
            wt_image indy_talk_state_1_1
        elif terri.state == 2:
            wt_image indy_talk_state_2_3
        elif terri.state == 3:
            wt_image indy_talk_state_3_6
        elif terri.state == 4:
            wt_image indy_talk_state_4_9
        elif terri.state == 5:
            wt_image indy_bj_1_state_5_1
        terri.c "Oh?  What?"
        player.c "Your sexual orientation."
        if terri.state == 1:
            wt_image indy_hypno_state_1_1
        elif terri.state == 2:
            wt_image indy_hypno_state_2_2
        elif terri.state == 3:
            wt_image indy_talk_state_3_7
        elif terri.state == 4:
            wt_image indy_hypno_state_4_5
        elif terri.state == 5:
            wt_image indy_talk_state_5_7
        terri.c "What do you mean?"
        player.c "[terri.name], I think you're a lesbian."
        if terri.state == 1:
            wt_image indy_hypno_state_1_5
        elif terri.state == 2:
            wt_image indy_talk_state_2_4
        elif terri.state == 3:
            wt_image indy_hypno_state_3_1
        elif terri.state == 4:
            wt_image indy_talk_state_4_3
        elif terri.state == 5:
            wt_image indy_hypno_state_5_5
        terri.c "Why would you say something like that!  I can't believe you'd accuse me of something so ... so, perverted."
        player.c "[terri.name], ..."
        if terri.state == 1:
            wt_image indy_hypno_state_1_1
        elif terri.state == 2:
            wt_image indy_hypno_state_2_5
        elif terri.state == 3:
            wt_image indy_hypno_state_3_2
        elif terri.state == 4:
            wt_image indy_talk_state_4_5
        elif terri.state == 5:
            wt_image indy_talk_state_5_5
        terri.c "No.  No, I don't want to talk about this.  Let's just get on with my training.  Tell me what I should be doing to be a better partner for my boyfriend."
        $ terri.lesbian_confronted = 1
        if terri.lesbian_is_pervert_disclosure == 0:
            $ terri.lesbian_is_pervert_disclosure = 1
    elif terri.lesbian_confronted == 1:
        if terri.lesbian_is_pervert_disclosure == 2:
            player.c "[terri.name], I wanted to tell you something about what your Mother told you.  About lesbians."
            if terri.state == 1:
                wt_image indy_talk_state_1_1
            elif terri.state == 2:
                wt_image indy_talk_state_2_2
            elif terri.state == 3:
                wt_image indy_talk_state_3_6
            elif terri.state == 4:
                wt_image indy_talk_state_4_9
            elif terri.state == 5:
                wt_image indy_bj_1_state_5_1
            terri.c "What do you want to tell me?"
            $ title = "What do you tell her?"
            menu:
                "Your Mother was right":
                    player.c "Your mother was right, [terri.name].  Lesbians are perverts.  Women should not touch or be excited by other women.  Only by men."
                    if terri.state == 1:
                        wt_image indy_talk_state_1_2
                    elif terri.state == 2:
                        wt_image indy_hypno_state_2_2
                    elif terri.state == 3:
                        wt_image indy_hypno_state_3_1
                    elif terri.state == 4:
                        wt_image indy_talk_state_4_11
                    elif terri.state == 5:
                        wt_image indy_talk_state_5_6
                    "She nods."
                    terri.c "I know that."
                    player.c "Even though you know that, [terri.name], you're still excited by the idea of touching and being touched by another woman, aren't you.  It's okay, [terri.name].  You can trust your secret to me."
                    if terri.state == 1:
                        wt_image indy_talk_state_1_3
                    elif terri.state == 2:
                        wt_image indy_talk_state_2_5
                    elif terri.state == 3:
                        wt_image indy_hypno_state_3_5
                    elif terri.state == 4:
                        wt_image indy_talk_state_4_12
                    elif terri.state == 5:
                        wt_image indy_hypno_state_5_1
                    "Tears well up in her eyes, and her voice catches as she replies."
                    terri.c "Yes.  I'm so ashamed, but it's true.  I try to suppress the feelings, to make them go away.  But they push themselves back into my head."
                    player.c "Follow my teaching, [terri.name], and I will help you to deal with your demon."
                    if terri.state == 1:
                        wt_image indy_hypno_state_1_2
                    elif terri.state == 2:
                        wt_image indy_hypno_state_2_3
                    elif terri.state == 3:
                        wt_image indy_talk_state_3_7
                    elif terri.state == 4:
                        wt_image indy_talk_state_4_4
                    elif terri.state == 5:
                        wt_image indy_portrait_state_5
                    terri.c "Yes!  Yes, I will!  Anything you tell me.  Just please, help me."
                    $ terri.lesbian_confronted = 3 # shuts off trying to help her via this route
                    change terri submission by 10
                    change terri resistance by -5 notify
                "Your Mother was wrong":
                    player.c "Your mother was wrong, [terri.name].  There's nothing wrong with two women loving each other, or enjoying each other's touch.  It doesn't make you a bad person.  It doesn't make you a pervert."
                    if terri.state == 1:
                        wt_image indy_hypno_state_1_1
                    elif terri.state == 2:
                        wt_image indy_talk_state_2_4
                    elif terri.state == 3:
                        wt_image indy_talk_state_3_8
                    elif terri.state == 4:
                        wt_image indy_hypno_state_4_5
                    elif terri.state == 5:
                        wt_image indy_talk_state_5_8
                    "She shakes her head."
                    terri.c "No.  No, that's not what Mom taught me."
                    player.c "[terri.name], I know you want to honor your mother's memory.  But parents aren't perfect, and they aren't right about everything.  People understand homosexuality better today than they did when she was alive.  If your mother had lived, maybe she might even feel differently now."
                    if terri.state == 1:
                        wt_image indy_hypno_state_1_5
                    elif terri.state == 2:
                        wt_image indy_talk_state_2_5
                    elif terri.state == 3:
                        wt_image indy_hypno_state_3_1
                    elif terri.state == 4:
                        wt_image indy_talk_state_4_3
                    elif terri.state == 5:
                        wt_image indy_hypno_state_5_5
                    player.c "Your happiness is the most important thing.  It's going to be very difficult for you to be truly happy if you don't accept your true feelings."
                    terri.c "I can be happy with my boyfriend.  I know I can!"
                    if terri.state == 1:
                        wt_image indy_hypno_state_1_1
                    elif terri.state == 2:
                        wt_image indy_hypno_state_2_5
                    elif terri.state == 3:
                        wt_image indy_hypno_state_3_2
                    elif terri.state == 4:
                        wt_image indy_talk_state_4_5
                    elif terri.state == 5:
                        wt_image indy_hypno_state_5_2
                    terri.c "Can we please drop this topic now?  I don't want to discuss this any longer.  I am going to be a good girlfriend for my boyfriend and make him happy. That's what I want."
                    $ terri.lesbian_confronted = 2
                    "Best to move on to something else for the moment.  She's upset and a little more resistant to you, but you can revisit this topic later, after she calms down, if you want to."
                    change terri resistance by 5 notify
        else:
            player.c "[terri.name], I really think we should talk about your sexual orientation."
            if terri.state == 1:
                wt_image indy_hypno_state_1_5
            elif terri.state == 2:
                wt_image indy_talk_state_2_4
            elif terri.state == 3:
                wt_image indy_hypno_state_3_2
            elif terri.state == 4:
                wt_image indy_talk_state_4_10
            elif terri.state == 5:
                wt_image indy_hypno_state_5_2
            terri.c "I told you, I'm not a pervert, and I don't intend to talk about it."
            "You're not going to get anywhere on this front without dealing with the perversion issue.  [terri.name] has her back up now, so best to drop the whole topic and move on to something else for this session."
    elif terri.lesbian_confronted == 2:
        $ title = "How do you want to approach this topic?"
        menu:
            "Convince her yourself":
                player.c "[terri.name], we need to address your feelings about women.  You're never going to be truly comfortable in your own skin until you accept who you are."
                if terri.state == 1:
                    wt_image indy_talk_state_1_2
                elif terri.state == 2:
                    wt_image indy_talk_state_2_3
                elif terri.state == 3:
                    wt_image indy_talk_state_3_9
                elif terri.state == 4:
                    wt_image indy_talk_state_4_9
                elif terri.state == 5:
                    wt_image indy_talk_state_5_8
                terri.c "I have accepted it.  You're the one who keeps bringing this subject up.  It doesn't matter what's in my head.  What matters is how I behave."
                if terri.state == 1:
                    wt_image indy_hypno_state_1_5
                elif terri.state == 2:
                    wt_image indy_talk_state_2_4
                elif terri.state == 3:
                    wt_image indy_hypno_state_3_2
                elif terri.state == 4:
                    wt_image indy_talk_state_4_10
                elif terri.state == 5:
                    wt_image indy_talk_state_5_6
                terri.c "Can we please drop this topic now?  I don't want to discuss it any longer.  I am going to be a good girlfriend for my boyfriend and make him happy.  That's what I want."
                "Perhaps it would be best to leave this topic until you have a better way to approach it."
            "She needs a Mother figure in her life" if terri.state > 3 and marilyn.independent_encounter_status == 1:
                player.c "[terri.name], what do you remember about your mother?"
                if terri.state == 1:
                    wt_image indy_portrait_state_1
                elif terri.state == 2:
                    wt_image indy_portrait_state_2
                elif terri.state == 3:
                    wt_image indy_talk_state_3_5
                elif terri.state == 4:
                    wt_image indy_talk_state_4_2
                elif terri.state == 5:
                    wt_image indy_talk_state_5_1
                terri.c "She was beautiful.  Striking dark hair.  Strong.  Not physically strong, I mean a strong personality.  She was like a force of nature.  Nobody messed with my Mom.  I always felt so safe with her."
                player.c "No wonder you miss her.  Do you ever wish you had a mother figure like her still in your life?"
                if terri.state == 1:
                    wt_image indy_hypno_state_1_2
                elif terri.state == 2:
                    wt_image indy_hypno_state_2_1
                elif terri.state == 3:
                    wt_image indy_talk_state_3_3
                elif terri.state == 4:
                    wt_image indy_talk_state_4_4
                elif terri.state == 5:
                    wt_image indy_portrait_state_5
                terri.c "Yes, sometimes I do.  That's silly, isn't it, at my age?"
                player.c "Not at all.  I may be able to help, [terri.name]."
                if terri.state == 1:
                    wt_image indy_bj_1_state_1_1
                elif terri.state == 2:
                    wt_image indy_talk_state_2_2
                elif terri.state == 3:
                    wt_image indy_talk_state_3_6
                elif terri.state == 4:
                    wt_image indy_talk_state_4_3
                elif terri.state == 5:
                    wt_image indy_talk_state_5_2
                terri.c "Really?  Today?"
                player.c "Not today, no.  But give me some time to think about it."
                "If you want, you can set up a meeting between [terri.name] and [marilyn.name] on a future session."
                $ terri.ready_for_marilyn = 1
                add tags 'marilyn_talk_option_possible' to terri
            "She needs a strong woman in her life" if cassandra.independent_encounter_status == 1 and terri.test('submission',40):
                player.c "[terri.name], I've taught you that it's important to be obedient."
                if terri.state == 1:
                    wt_image indy_talk_state_1_1
                elif terri.state == 2:
                    wt_image indy_talk_state_2_5
                elif terri.state == 3:
                    wt_image indy_talk_state_3_9
                elif terri.state == 4:
                    wt_image indy_talk_state_4_12
                elif terri.state == 5:
                    wt_image indy_hypno_state_5_1
                "She nods."
                player.c "If your boyfriend demands something of you, or I demand something of you, could anyone blame you for doing it?"
                if terri.state == 1:
                    wt_image indy_talk_state_1_2
                elif terri.state == 2:
                    wt_image indy_talk_state_2_1
                elif terri.state == 3:
                    wt_image indy_talk_state_3_7
                elif terri.state == 4:
                    wt_image indy_talk_state_4_11
                elif terri.state == 5:
                    wt_image indy_portrait_state_5
                terri.c "No.  I mean, if he asks me to do something, I'm his girlfriend, I'm supposed to obey him.  You're my trainer, I'm supposed to follow your instructions."
                player.c "So you understand that if someone in a position of authority requires something from you, you don't have to feel bad about doing what they want."
                if terri.state == 1:
                    wt_image indy_talk_state_1_3
                elif terri.state == 2:
                    wt_image indy_talk_state_2_5
                elif terri.state == 3:
                    wt_image indy_talk_state_3_8
                elif terri.state == 4:
                    wt_image indy_talk_state_4_9
                elif terri.state == 5:
                    wt_image indy_talk_state_5_6
                terri.c "Yes.  Does this have something to do with my training for today?"
                player.c "Not for today, no.  I just wanted to make sure you were ready for what might come later."
                "If you want, you could set up a meeting between [terri.name] and [cassandra.name] on a future session."
                $ terri.ready_for_domme = 1
            "Talk about a transformation" if player.has_item(transformation_potion):
                player.c "[terri.name], these thoughts you have about women.  Why do you think they're wrong?"
                if terri.state == 1:
                    wt_image indy_hypno_state_1_1
                elif terri.state == 2:
                    wt_image indy_talk_state_2_5
                elif terri.state == 3:
                    wt_image indy_talk_state_3_7
                elif terri.state == 4:
                    wt_image indy_talk_state_4_11
                elif terri.state == 5:
                    wt_image indy_bj_1_state_5_1
                terri.c "Because that's what my mother taught me.  Girls should only let boys touch them, not other girls."
                player.c "Have you ever wondered what it would be like if you were a boy?"
                if terri.state == 1:
                    wt_image indy_talk_state_1_1
                elif terri.state == 2:
                    wt_image indy_talk_state_2_1
                elif terri.state == 3:
                    wt_image indy_hypno_state_3_5
                elif terri.state == 4:
                    wt_image indy_talk_state_4_4
                elif terri.state == 5:
                    wt_image indy_hypno_state_5_1
                "She hesitates a moment."
                terri.c "Not really.  I mean, okay, once in a while when I was younger I used to think that if I was a boy it would be okay to kiss girls.  Those were just foolish young girl thoughts."
                player.c "If there was a way to make that happen, would you be open to it?"
                if terri.state == 1:
                    wt_image indy_talk_state_1_2
                elif terri.state == 2:
                    wt_image indy_talk_state_2_3
                elif terri.state == 3:
                    wt_image indy_talk_state_3_8
                elif terri.state == 4:
                    wt_image indy_talk_state_4_9
                elif terri.state == 5:
                    wt_image indy_talk_state_5_8
                terri.c "Make what happen?  You're not making any sense."
                "If you want to use the transformation potion to help her, she might be open to the idea."
            "Wait until you have another option":
                rem tags 'talked_today' from terri
    return

label terri_talk_how_feeling:
    add tags 'talked_today' to terri
    if terri.state == 1:
        wt_image indy_talk_state_1_2
    elif terri.state == 2:
        wt_image indy_hypno_state_2_1
    elif terri.state == 3:
        wt_image indy_talk_state_3_7
    elif terri.state == 4:
        wt_image indy_hypno_state_4_1
    elif terri.state == 5:
        wt_image indy_portrait_state_5
    player.c "How are you feeling about yourself and my training, [terri.name]?"
    # first, comments on youth angle, if applicable
    if terri.state == 1:
        pass
    elif terri.state == 2:
        wt_image indy_bj_1_state_2_1
        terri.c "I've been trying to dress younger, and it feels good."
    elif terri.state == 3:
        wt_image indy_talk_state_3_1
        terri.c "I'm feeling great, younger and happier than I've felt in years."
    elif terri.state == 4:
        wt_image indy_talk_state_4_2
        terri.c "I feel so young and happy.  I don't have a care in the world when I get to play the schoolgirl around you."
    elif terri.state == 5:
        wt_image indy_talk_state_5_3
        terri.c "You are so good to me.  Nobody has made me feel this safe and cared for in a long time.  I really feel like a little girl around you, and I love it."
    # then more general response based on sos
    if terri.test('sos', 50):
        if terri.state == 1:
            wt_image indy_portrait_state_1
        elif terri.state == 2:
            wt_image indy_portrait_state_2
        elif terri.state == 3:
            wt_image indy_talk_state_3_2
        elif terri.state == 4:
            wt_image indy_talk_state_4_1
        elif terri.state == 5:
            wt_image indy_talk_state_5_4
        terri.c "I can't thank you enough for all of the things you've taught me.  I really feel like I now know how to be a good girlfriend for my boyfriend."
    elif terri.test('sos',10):
        if terri.state == 1:
            wt_image indy_hypno_state_1_2
        elif terri.state == 2:
            wt_image indy_talk_state_2_2
        elif terri.state == 3:
            wt_image indy_talk_state_3_5
        elif terri.state == 4:
            wt_image indy_talk_state_4_9
        elif terri.state == 5:
            wt_image indy_talk_state_5_1
        terri.c "I'm feeling good about the training.  You've taught me a lot and I'm looking forward to learning more about how I can be a better girlfriend for my boyfriend."
    else:
        if terri.state == 1:
            wt_image indy_bj_1_state_1_1
        elif terri.state == 2:
            wt_image indy_talk_state_2_5
        elif terri.state == 3:
            wt_image indy_talk_state_3_6
        elif terri.state == 4:
            wt_image indy_talk_state_4_11
        elif terri.state == 5:
            wt_image indy_talk_state_5_2
        terri.c "I'm looking forward to learning how to be a better girlfriend for my boyfriend."
    return

label terri_talk_nothing:
    pass
    return

# Hypno Actions
label terri_hypnosis_start:
    if terri.status == 'on_training':
        wt_image indy_hypno_state_[terri.state]_1
        if terri.hypno_count < 3:
            $ terri.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
            if terri.hypno_count == 0:
                player.c "[terri.name], I am going to talk with you, and you are going to listen to me."
                call focus_image from _call_focus_image_72
                player.c "Listen to me now, [terri.name]. Listen to me. Listen to my voice and nothing else, [terri.name]. Only my voice. Only my voice now."
                wt_image indy_hypno_state_[terri.state]_2
                "She soon falls under your trance."
            elif terri.hypno_count == 1:
                player.c "[terri.name], I am going to talk with you, and you are going to listen to me."
                "A quizzical look passes across [terri.name]'s face as you start your mantra, but it passes and she drifts under your control."
                call focus_image from _call_focus_image_73
                player.c "Listen to me now, [terri.name]. Listen to me.  Listen to my voice and nothing else, [terri.name].  Only my voice.  Only my voice now."
                wt_image indy_hypno_state_[terri.state]_1
            elif terri.hypno_count == 2:
                player.c "[terri.name], I am going to talk with you, and you are going to listen to me."
                "[terri.name] gets a strange look on her face. You think she's about to say something, then she stops and focuses on your voice."
                call focus_image from _call_focus_image_74
                player.c "Listen to me now, [terri.name].  Listen to me.  Listen to my voice and nothing else, [terri.name].  Only my voice.  Only my voice now."
            wt_image indy_hypno_state_[terri.state]_3
            player.c "[terri.name], I want you to get comfortable for our talk.  Show me your breasts, [terri.name]."
            wt_image indy_hypno_state_[terri.state]_4
            if not player.has_tag('first_hypno_breasts_message'):
                add tags 'first_hypno_breasts_message' to player
                "[player.first_hypno_breasts_message_text]"
            "[terri.name] bares her chest with no hesitation.  She's very small up top, but no less pretty for that."
        else:
            player.c "[terri.name], I am going to talk with you, and you are going to listen to me."
            if terri.state == 1:
                wt_image indy_hypno_state_1_1
            elif terri.state == 2:
                wt_image indy_talk_state_2_5
            elif terri.state == 3:
                wt_image indy_talk_state_3_7
            elif terri.state == 4:
                wt_image indy_hypno_state_4_1
            elif terri.state == 5:
                wt_image indy_talk_state_5_8
            terri.c "Wait.  Stop.  What are you doing?"
            player.c "What do you mean?  I'm talking to you."
            wt_image indy_hypno_state_[terri.state]_5
            terri.c "No, you're doing something.  You're getting inside my head.  How are you doing it?"
            $ title = "What do you tell her?"
            menu:
                "The truth":
                    player.c "I'm hypnotizing you, [terri.name]."
                    wt_image indy_hypno_state_[terri.state]_1
                    terri.c "Why?"
                    player.c "To help you."
                    wt_image indy_hypno_state_[terri.state]_5
                    terri.c "Well, don't.  I don't want you poking around in my brain.  And how are you able to do that without me knowing?"
                    player.c "It's a skill I have.  Don't worry, I can't make you do anything you don't want to do."
                    wt_image indy_hypno_state_[terri.state]_1
                    terri.c "What have you made me do?  Stop, don't answer that.  I don't want to know.  Promise me you won't do it again.  Otherwise I won't come back."
                    $ title = "Promise her?"
                    menu:
                        "Yes":
                            "You wouldn't be able to hypnotize her without her consent anyway, now that she's wary of you."
                            player.c "I promise.  Our sessions could be more effective, though, if you let me continue. I really can help you."
                            terri.c "No.  No, there are things ... I just don't want that."
                            add tags 'hypnosis_revealed' to terri
                        "No (loses [terri.name] as a client)":
                            player.c "I can't promise you that.  This is for your own good and an important part of your training."
                            dismiss terri
                            wt_image current_location.image
                            "She leaves and never comes back."
                            call convert(terri, 'unavailable') from _call_convert_190
                "A lie":
                    player.c "I don't know what you're talking about, [terri.name]."
                    terri.c "Well, stop it anyway."
                    "She clearly doesn't believe you, and her respect for you has fallen.  Now that she's wary of you, you won't be able to hypnotize her again."
                    change terri resistance by 5 notify
                    "You'll need to choose another activity for today."
            add tags 'no_hypnosis' to terri
            $ ignore_context_change = True # this breaks the hypno sequence before calling hypnosis_context menu
    elif terri.status == 'post_training' and terri.has_tag('continuing_actions') and current_location == living_room:
        if terri.has_tag('futanari'):
            if terri.futanari_outfit == 2:
                wt_image indy_futanari_2_5
                player.c "[terri.name], look at this for me."
                wt_image indy_futanari_2_6
                terri.c "Don't do that."
                player.c "What?"
                wt_image indy_futanari_2_2
                wt_image indy_futanari_1_4
                player.c "[terri.name], look at this for me."
                wt_image indy_futanari_1_3
                terri.c "Don't do that."
                player.c "What?"
                wt_image indy_futanari_1_2
            else:
                wt_image indy_futanari_1_4
                player.c "[terri.name], look at this for me."
                wt_image indy_futanari_1_3
                terri.c "Don't do that."
                player.c "What?"
                wt_image indy_futanari_1_2
        elif terri.has_tag('cheerleader_visit_now'):
            if terri.has_tag('boob_job'):
                wt_image indy_cheerleader_2_1
                player.c "[terri.name], look at this for me."
                if terri.has_tag('strips_on_visit'):
                    wt_image indy_cheerleader_2_5
                else:
                    wt_image indy_cheerleader_2_4
            else:
                wt_image indy_cheerleader_1_16
                player.c "[terri.name], look at this for me."
                wt_image indy_cheerleader_1_17
            terri.c "Don't do that."
            player.c "What?"
        elif terri.has_tag('boob_job'):
            wt_image indy_drink_2_1
            player.c "[terri.name], look at this for me."
            wt_image indy_drink_2_3
            terri.c "Don't do that."
            player.c "What?"
            wt_image indy_drink_2_4
        else:
            wt_image indy_drink_1_19
            player.c "[terri.name], look at this for me."
            wt_image indy_drink_1_7
            terri.c "Don't do that."
            player.c "What?"
            wt_image indy_drink_1_19
        terri.c "Whatever it is you're trying to do.  It makes me uncomfortable.  Let's just talk."
        "[terri.name] is unusually attuned to your attempt to hypnotize her, even if she's not quite sure what you're up to.  You won't be able to put her into a trance."
        add tags 'no_hypnosis' to terri
        $ ignore_context_change = True # this breaks the hypno sequence before calling hypnosis_context menu
    else:
        "You can't hypnotize her anymore."
        add tags 'no_hypnosis' to terri
        $ ignore_context_change = True # this breaks the hypno sequence before calling hypnosis_context menu
    return

label terri_insecurities_hypnosis:
    $ terri.hypno_insecurities_count += 1
    if terri.hypno_insecurities_count == 1:
        player.c "[terri.name], are you a happy person?"
        terri.c "No"
        player.c "Why do you think that is?"
        terri.c "I have Mommy issues."
        player.c "What do you mean?"
        terri.c "My Mommy died when I was young. I miss her. I have a lot of messed up thoughts in my head. Probably because I never got over losing her."
        player.c "Tell me about the messed up thoughts in your head."
        terri.c "No"
        player.c "I'm not going to judge you, [terri.name]. I am safe to talk to. You can tell me. It will feel good to share."
        "You see a struggle on her face, but she's not willing to open up yet. You spend the rest of the session working on increasing her trust in you, in the hopes you have more success next time."
        add tags 'mom_died_young_reveal_hypno' to terri
    elif terri.hypno_insecurities_count == 2:
        player.c "[terri.name], I am here to help you. I'm going to help you feel better about yourself."
        terri.c "Okay"
        player.c "Tell me about the thoughts in your head. The ones that bother you."
        "She hesitates for a moment, then replies."
        terri.c "I'm a pervert. I like girls. I want to kiss them. I want them to kiss me. I shouldn't."
        player.c "Why do you say you shouldn't?"
        terri.c "My Mommy told me. She only wanted me to be happy. She said I shouldn't kiss girls. I try to do what she says. I wish I wasn't a pervert. But I'm very smart. I don't let anyone know I'm a pervert. Except you. You want to help me."
        $ terri.lesbian_clues += 3
        $ title = "What do you try to do?"
        menu:
            "Convince her she's not a pervert":
                player.c "[terri.name], it's very important for you to listen to me. Liking girls is not a perversion."
                terri.c "It is when you're a girl."
                player.c "No, [terri.name], it ..."
                terri.c "My Mommy said it was. You're not my Mommy. I'm not going to listen to you."
                "You're not going to get anywhere on this track today. You work some more on increasing her trust in you, in the hopes you can go further next time."
            "Convince her she's not a lesbian":
                player.c "[terri.name], it's very important for you to listen to me. You like boys. You have a boyfriend. You love him and want to be with him. You want to be with boys. You're not a lesbian."
                terri.c "I could be bisexual. Except I don't get hot and tingly when I'm thinking about boys. Only girls."
                player.c "Boys are sexy, [terri.name]. Boys are hard, and lean, and good looking. Thinking about boys makes you hot and tingly."
                terri.c "No, it doesn't. I wish it did."
                "You're not going to get anywhere on this track today. You work some more on increasing her trust in you, in the hopes you can go further next time."
            "Leave this mess alone":
                "Messing with this while she's hypnotized is just asking for trouble. Maybe you can use this information to help her in other ways, but for today, it's best just to end this session."
    elif terri.hypno_insecurities_count == 3:
        player.c "[terri.name], I am here to help you. I'm going to help you feel better about yourself."
        terri.c "Okay"
        player.c "I want to talk to you about the thoughts in your head. Your thoughts about girls."
        terri.c "There are more."
        player.c "More what?"
        terri.c "More messed up thoughts in my head. It's not just liking girls. I never wanted to grow up. I don't like being an adult. I want to be a little girl, not a woman."
        player.c "You sometimes like to dress and act young. Yes, I've noticed that about you."
        terri.c "No, you don't understand. I wish I was really young. It's not sexual, not really. I just fantasize about being back with my Mommy. Nice and safe and cared for."
        "There's too much stuff going on here to try and parse it out right now. You're going to need a plan. For today, you focus on increasing her trust in you, in the hopes it helps for her next session."
    wt_image indy_portrait_state_[terri.state]
    "When you've gone as far as you can for this session, you instruct her to dress and bring her out of the trance. She doesn't exactly remember what the two of you talked about, but you do.  You just need to decide what you want to do with it."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_24
    return

label terri_desire_hypnosis:
    "You try to work on raising [terri.name]'s Desire towards you, but none of the normal approaches seem to work. She likes you, and you can reinforce that sense of friendship. But you can't get her to see you in a romantic way."
    sys "Trying to raise her Desire this way isn't going to work.  You should try something different."
    if not terri.has_tag('hypno_desire_doesnt_work'):
        add tags 'hypno_desire_doesnt_work' to terri
        $ terri.lesbian_clues += 1
    ## this should back things up to the prior menu
    $ terri.desire_hypno_action.backtrack = True
    $ terri.remove_action( terri.desire_hypno_action )
    $ context = "terri_hypnosis"
    break_sequence
    return

label terri_resistance_hypnosis:
    "You begin to work on reducing [terri.name]'s Resistance to you, but soon discover that her Resistance is already quite low. She came to you voluntarily, and she's already willing to follow your instructions."
    sys "Any residual Resistance she has can't be dealt with through hypnosis. You should abandon this approach and try something different."
    ## this should back things up to the prior menu
    $ terri.resistance_hypno_action.backtrack = True
    $ terri.remove_action( terri.resistance_hypno_action )
    $ context = "terri_hypnosis"
    break_sequence
    return

label terri_sos_hypnosis:
    "You work on raising [terri.name]'s Sense of Self, and in particular her confidence in her ability to please men, including her boyfriend.  This can be the most difficult trait to affect directly, but it goes directly to the goal of her training."
    wt_image indy_portrait_state_[terri.state]
    "When you've gone as far as you can for this session, you instruct her to dress and bring her out of the trance. She doesn't exactly remember what the two of you talked about, but she enjoyed the chat and is feeling better about her ability to be a good girlfriend."
    return

label terri_submission_hypnosis:
    "You work on raising [terri.name]'s Submission towards you. If she's willing to obey you, it'll be easier to train her to accept her new role."
    wt_image indy_portrait_state_[terri.state]
    "When you've gone as far as you can for this session, you instruct her to dress and bring her out of the trance. She doesn't exactly remember what the two of you talked about, but she now sees you as more of an authority figure."
    return

label terri_hypnosis_end:
    $ terri.hypno_session() # deducts energy and records she was hypno'd, including increased hypno_count
    call character_location_return(terri) from _call_character_location_return_705
    if terri.status == 'on_training':
        end_day
    return

# End Session
label terri_end_session:
    if terri.status == 'on_training':
        $ terri.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        "You have nothing more you want to do with [terri.name], so you end today's session here."
        ## the two lines below are not needed for Terri as (a) she pays you regardless, and (b) she has no weekend sessions
        #$ player.extra_clients_fee_this_week -= terri.pay # so you don't get paid for training her this week
        #add tags 'failed_regular_training_this_week' to terri # so that if you train her on the weekend, you get paid for training her on the weekend
        change player energy by -energy_very_short notify
        call character_location_return(terri) from _call_character_location_return_706
        end_day
    elif terri.has_tag('continuing_actions'):
        $ terri.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        if terri.has_tag('futanari'):
            if terri.futanari_outfit == 2:
                wt_image indy_futanari_2_3
            else:
                wt_image indy_futanari_1_23
        elif terri.has_tag('cheerleader_visit_now'):
            if terri.has_tag('boob_job'):
                wt_image indy_cheerleader_2_2
            else:
                wt_image indy_cheerleader_1_2
            "The two of you say your good-byes as [terri.name] leaves."
        elif terri.has_tag('boob_job'):
            wt_image indy_boob_job_1_15
            "The two of you say your good-byes as [terri.name] leaves."
        else:
            wt_image indy_drink_1_19
            "The two of you finish up your drinks and say your good-byes as [terri.name] leaves."
        terri.c "I hope we get to catch up again soon!"
        call character_location_return(terri) from _call_character_location_return_707
        wt_image current_location.image
        change player energy by -energy_very_short notify
    else:
        add tags 'shut_off_end_session' to terri
    return

# Weekend Actions
label terri_weekend:
    call character_location_return(terri) from _call_character_location_return_708
    "[terri.name] spends the weekend with her boyfriend. She's only available for evening sessions, Monday through Thursday."
    $ terri.available_on_weekends = False
    reset_menu
    return

## Character Specific Actions
# Make Out With Her
label terri_make_out:
    $ terri.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    if terri.state == 1:
        wt_image indy_talk_state_1_1
    elif terri.state == 2:
        wt_image indy_talk_state_2_1
    elif terri.state == 3:
        wt_image indy_talk_state_3_6
    elif terri.state == 4:
        wt_image indy_talk_state_4_9
    elif terri.state == 5:
        wt_image indy_talk_state_5_8
    player.c "[terri.name], let's spend some time getting comfortable with each other, and you can show me how you make out with your boyfriend."
    if terri.state == 1:
        wt_image indy_hypno_state_1_2
    elif terri.state == 2:
        wt_image indy_talk_state_2_2
    elif terri.state == 3:
        wt_image indy_talk_state_3_4
    elif terri.state == 4:
        wt_image indy_talk_state_4_6
    elif terri.state == 5:
        wt_image indy_bj_1_state_5_1
    terri.c "Like we're on a date?"
    player.c "Exactly."
    wt_image current_location.image
    "[terri.name] may have been anticipating this.  She excuses herself to change ..."
    wt_image indy_kiss_state_1_8
    "... and emerges wearing the sexiest make out outfit you've seen in a while."
    player.c "Do you usually wear something like this when you make out with your boyfriend?"
    wt_image indy_kiss_state_1_1
    terri.c "Yes.  Shouldn't I?"
    player.c "You should, definitely.  It looks great on you."
    wt_image indy_kiss_state_1_9
    terri.c "It doesn't make me look too old?"
    wt_image indy_kiss_state_1_1
    if terri.state < 3:
        player.c "Not at all.  It looks very sexy on you."
    else:
        player.c "Not at all.  It makes you look grown up enough to get your first kiss."
    wt_image indy_kiss_state_1_2
    "You start off by kissing her on the neck. She shivers slightly as you brush your lips across her skin."
    wt_image indy_kiss_state_1_10
    "She stiffens as you kiss your way up her neck, but she doesn't pull away."
    wt_image indy_kiss_state_1_11
    player.c "I'm going to kiss you on the mouth now.  Is that okay?"
    wt_image indy_kiss_state_1_3
    "She nods and opens her lips as you lean in."
    wt_image indy_kiss_state_1_12
    "She stays like that, eyes closed, mouth open but almost unmoving ..."
    wt_image indy_kiss_state_1_13
    "... as you tease her lips and try to provoke a reaction from her."
    wt_image indy_kiss_state_1_3
    player.c "Are you enjoying this?"
    wt_image indy_kiss_state_1_14
    terri.c "Yes, of course.  You're a very good kisser.  Not that I've kissed that many people, other than my boyfriend.  But what you're doing is nice."
    wt_image indy_kiss_state_1_3
    player.c "That's good.  How about you kiss me back, now?"
    wt_image indy_kiss_state_1_4
    "She does, but her kiss is oddly cold and mechanical.  She presses her lips against you and slips the tip of tongue through to play against yours, but it feels like she's going through the motions of a script, rather than spontaneously enjoying the kiss."
    wt_image indy_kiss_state_1_15
    "She may just be nervous, kissing someone other than her boyfriend, so you try to warm her up and lighten the mood by playfully squeezing her butt as the two of you kiss."
    wt_image indy_kiss_state_1_5
    "She giggles, but seems to take your sudden interest in her bum as a sign that the kissing is over, rather than as encouragement to kiss you more intensely."
    wt_image indy_kiss_state_1_2
    "You nibble again at her neck, since she seemed to like that before.  She leans into you as you do so ..."
    wt_image indy_kiss_state_1_6
    "... then startles and pulls away slightly as the stubble on your beard rubs against the side of her chin."
    wt_image indy_kiss_state_1_7
    "You try one more thing, this time to sexualize the kiss.  She lets you put your hand between her legs, but she shows no sign of arousal at all, and she stiffens up when you try to move your fingers along her sex."
    wt_image indy_kiss_state_1_6
    if player.has_tag('supersexy'):
        "Something's odd here.  Women get wet when you kiss them.  Often they get wet just thinking about kissing you. Unless they're post-menopausal or otherwise have a medical condition that impacts their natural lubrication, they certainly don't stay dry after a full on kiss, caress and nuzzle session."
        $ terri.lesbian_clues += 2
        if terri.pleasure_her_action_used == 0:
            $ terri.pleasure_her_action_used = 1 # this opens up the pleasure her action (no idea why variable is called 'pleasure_you' LOL)
    else:
        "You're not her boyfriend, and this whole situation is rather artificial.  Perhaps, despite her willingness to accept your training, she's just not that into you?"
        $ terri.lesbian_clues += 1
    wt_image indy_kiss_state_1_1
    "You end the session for today, to give you some time to think about how to proceed next time."
    wt_image indy_kiss_state_1_9
    terri.c "Was that okay?  Do I kiss well enough for my boyfriend to enjoy it?"
    player.c "I don't think him enjoying the two of you kissing is likely to be a problem, no."
    wt_image indy_kiss_state_1_16
    terri.c "Okay, good.  I'll go get changed."
    "She seems more relieved than happy about this lesson being over."
    add tags 'make_out_action_not_available' to terri
    change player energy by -energy_long notify
    end_day
    return

# Training
label terri_youth_training:
    $ terri.temporary_count = 1
    # Youth training
    if terri.has_tag('youth_first_conversation') and terri.youth_interest > 2 and not terri.has_tag('mom_died_young_reveal'):
        player.c "[terri.name], for today's session, I'd like to work on your youthfulness."
        if terri.state == 2:
            wt_image indy_talk_state_2_5
        elif terri.state == 3:
            wt_image indy_talk_state_3_6
        elif terri.state == 4:
            wt_image indy_talk_state_4_7
        elif terri.state == 5:
            wt_image indy_hypno_state_5_1
        "[terri.name] nods."
        terri.c "There's something important about my youth I need to tell you about first.  Something I haven't mentioned before, because I like to try and forget it."
        if terri.state == 2:
            wt_image indy_hypno_state_2_2
        elif terri.state == 3:
            wt_image indy_talk_state_3_9
        elif terri.state == 4:
            wt_image indy_talk_state_4_4
        elif terri.state == 5:
            wt_image indy_talk_state_5_6
        terri.c "My mother died while I was just a child.  I miss her.  Even now, as an adult, I miss that feeling of safety and security I had before she died.  I've never felt the same since.  I wish I could get that feeling back."
        player.c "I'm very sorry, [terri.name].  I can't imagine what that must have been like for you.  Perhaps, by working together, we can find a way for you to feel more safe and secure?"
        if terri.state == 2:
            wt_image indy_portrait_state_2
        elif terri.state == 3:
            wt_image indy_talk_state_3_5
        elif terri.state == 4:
            wt_image indy_talk_state_4_2
        elif terri.state == 5:
            wt_image indy_talk_state_5_1
        terri.c "I'd like that."
        add tags 'mom_died_young_reveal' to terri
    if terri.youth_interest == 0 or not terri.has_tag('youth_first_conversation'):
        wt_image indy_talk_state_1_2
        player.c "[terri.name], many men associate youth with beauty."
        wt_image indy_hypno_state_1_2
        terri.c "I get that.  I miss the days of my youth too.  Even if I'm an adult now, maybe if I act young, my boyfriend will see me that way?  Do you think that would help?"
        player.c "Yes, I think it might.  I want you to start thinking and feeling more youthful."
        wt_image indy_portrait_state_1
        terri.c "I'd like that."
        player.c "That includes dressing young."
        wt_image indy_talk_state_1_1
        terri.c "Won't I look ridiculous if I don't dress my age?"
        player.c "Not if you also feel young.  The two go hand-in-hand.  Tell me about your youth."
        wt_image indy_hypno_state_1_2
        terri.c "I miss it.  I miss how simple everything was."
        "You spend the rest of the evening talking about her youth.  It's a topic she seems to enjoy."
        if terri.youth_interest < 3:
            $ terri.youth_interest += 1
            sys "[terri.name] is now more interested in acting young."
        add tags 'youth_first_conversation' to terri
    elif terri.youth_interest == 1 and terri.has_tag('youth_first_conversation'):
        wt_image indy_talk_state_1_2
        player.c "[terri.name], I'd like you to tell me more about your youth."
        wt_image indy_hypno_state_1_2
        "She beams.  It's a topic she loves talking about, and she happily recounts her favorite memories.  You use every opportunity to reinforce that she can recapture the joy of youth by keeping herself in a youthful state of mind."
        wt_image indy_talk_state_1_1
        terri.c "So you really think it will be okay if I dress and act younger?"
        player.c "Yes, [terri.name].  It would be okay."
        wt_image indy_talk_state_1_3
        "She seems to be contemplating your conversation as she heads home."
        $ terri.youth_interest += 1
        sys "[terri.name] is now more interested in acting young."
    elif terri.youth_interest == 2 and terri.has_tag('youth_first_conversation'):
        wt_image indy_portrait_state_2
        player.c "[terri.name], have you been giving any thought to acting younger?"
        wt_image indy_hypno_state_2_3
        terri.c "Yes, I've been thinking about it a lot, and I'm trying to dress younger.  I feel better when I dress young.  I feel happier.  Thank you for helping me understand that."
        if not terri.has_tag('completed_youth_2'):
            change terri resistance by -5 notify
            add tags 'completed_youth_2' to terri
        $ title = "What do you tell her?"
        menu:
            "You could go further":
                player.c "You do look good, [terri.name], but you could go further."
                wt_image indy_talk_state_2_1
                terri.c "Really?  You don't think it will be too much?"
                player.c "Not at all.  Your dress is improving, but you could be even more youthful.  Physically, we can transform you a bit too."
                wt_image indy_talk_state_2_2
                terri.c "What do you mean?"
                player.c "I mean between your legs."
                wt_image indy_hypno_state_2_1
                "She blushes."
                wt_image indy_hypno_state_2_2
                terri.c "You want me to shave?"
                player.c "I do.  I'll inspect you afterwards and let you know if it helped you look younger."
                call forced_movement(bathroom) from _call_forced_movement_988
                wt_image indy_shave_1_1
                "You lend her a razor and shaving cream and she goes into your bathroom.  With only a hint of embarrassment she gets naked ..."
                wt_image indy_shave_1_2
                "... and shaves ..."
                wt_image indy_shave_1_3
                "... meticulously removing all signs of hair."
                wt_image indy_shave_1_4
                terri.c "I'll rinse off.  Then I guess I'll be ready for inspection."
                call forced_movement(boudoir) from _call_forced_movement_989
                wt_image indy_shave_1_15
                "When she joins you in the boudoir, she hasn't just rinsed off, she's put her hair in pigtails.  She's really getting into the looking younger idea."
                wt_image indy_shave_1_5
                terri.c "It's weird, not having any hair down there, but it does make me look younger, doesn't it?"
                player.c "It does.  How does it feel?"
                wt_image indy_shave_1_6
                terri.c "A bit itchy.  Kind of scratchy."
                player.c "Let me feel."
                wt_image indy_shave_1_7
                terri.c "Okay.  Do you think my boyfriend will like my pussy like this?"
                "You run your fingers over her soft, slightly damp pussy as you contemplate your answer."
                $ title = "What do you tell her?"
                menu:
                    "All that matters is whether you like it":
                        wt_image indy_shave_1_8
                        terri.c "I'm not sure about the shaving, but I do love the idea of exploring ways I can look and act younger.  Thanks for encouraging me to explore this!  You have good ideas."
                        change terri resistance by -5 notify # additional resistance gain
                        $ terri.temporary_count = 2 # makes time use only short as little training associated with the shaving
                    "All that matters is I like it":
                        wt_image indy_shave_1_8
                        terri.c "Well, you're my trainer, so I suppose I should try and make you happy.  I hope it makes my boyfriend happy, too.  I'm enjoying exploring ways I can look and act younger.  So far following your instructions seems to be working out."
                        change terri submission by 5 notify
                        $ terri.temporary_count = 2 # makes time use only short as little training associated with the shaving
                    "He should, it's very fuckable (have sex with her)" if terri.sex_count > 0 and terri.blowjob_training_count > 0:
                        if terri.sex_training_count == 0:
                            wt_image indy_shave_1_5
                            terri.c "Oh, you want to ..."
                            player.c "See how you do at fucking?  Yes, [terri.name], it's an important skill for a good girlfriend to have, even a young-looking girlfriend like you."
                            wt_image indy_shave_1_6
                            terri.c "Okay.  I hope I don't disappoint you."
                            wt_image indy_shave_1_9
                            "You enter her carefully.  She's a little bit wet, but only a little bit."
                            wt_image indy_shave_1_10
                            "Despite her willingness to do this, she doesn't get any wetter as you gently fuck her."
                            player.c "[terri.name], do you want to be doing this?"
                            wt_image indy_shave_1_11
                            terri.c "Of course!  You said you wanted to see how I have sex."
                            player.c "Is this what it's like with your boyfriend? Are you always this dry, or is it just because you're nervous doing this for the first time with me?"
                            wt_image indy_shave_1_14
                            terri.c "Yes.  Why?  Am I doing something wrong?"
                            player.c "Is it uncomfortable when he fucks you?"
                            wt_image indy_shave_1_13
                            terri.c "A little.  He's not as big as you, so not as much as it is right now."
                            wt_image indy_shave_1_6
                            "You stop and get some lubricant.   That may make things easier."
                            wt_image indy_shave_1_9
                            player.c "Does that feel better?"
                            terri.c "Yes, that's much better.  Thank you!"
                            wt_image indy_shave_1_13
                            "Although she says it's better, and it must be without the discomfort of being dry, there's no evidence that she's enjoying this."
                            wt_image indy_shave_1_9
                            "Some women have difficulties with their natural lubrication, but with the lube you added, you think she should now be responding more than she is. She still isn't moving or participating in the fuck, yet she watches with a seeming hope that this is good for you. For a woman who wants to be good at sex, it doesn't seem to come naturally to her, either physically or instinctually."
                            wt_image indy_shave_1_11
                            terri.c "Am I doing something wrong?  You seem to be thinking a lot."
                            player.c "No, [terri.name].  It's nothing that we can't work on."
                            wt_image indy_shave_1_10
                            "You don't want to undermine her confidence, and she is both beautiful and tight.  You set your thoughts aside and focus on your own pleasure."
                            wt_image indy_shave_1_12
                            player.c "[player.orgasm_text]"
                            wt_image indy_shave_1_6
                            terri.c "Was that all right?  You seemed to enjoy yourself at the end.  Did you learn anything I should be doing differently?"
                            player.c "It was great, [terri.name].  You're great.  We'll pick this up again on a future visit."
                            wt_image indy_shave_1_8
                            terri.c "Okay.  I'm happy to work on anything you think I should be doing differently.  I really want to know how to be the best girlfriend I can be.  Thanks for encouraging me to look and act younger, I'm going to try more of that."
                            if terri.pleasure_her_action_used == 0:
                                $ terri.pleasure_her_action_used = 1 # this opens up the pleasure her action
                            add tags 'make_out_action_not_available' to terri # shuts the make out option off after you've already had sex with her
                            $ terri.lesbian_clues += 1
                            $ terri.sex_training_count += 1
                        elif terri.sex_training_count == 1:
                            wt_image indy_shave_1_6
                            terri.c "You want to fuck me again?"
                            $ title = "What do you want?"
                            menu:
                                "Train her":
                                    wt_image indy_shave_1_5
                                    player.c "I'm not going to fuck you today.  Today, I'm going to teach you how you can fuck me better."
                                    wt_image indy_shave_1_16
                                    terri.c "What do you mean?  Isn't fucking the man's job?"
                                    wt_image indy_shave_1_17
                                    player.c "Not at all.  Get on your hands and knees and open yourself up."
                                    wt_image indy_shave_1_18
                                    "Her pussy's not as dry as it usually is.  Whether that's from the shaving or the youth-play, you're not sure.  From past experience, though, you decide to apply a generous amount of lube to both her pussy and your cock, just to be safe."
                                    wt_image indy_shave_1_19
                                    "Even with lube, she struggles to take you all the way inside.  She'll never be able to fuck a man properly if her body isn't into it."
                                    player.c "Think sexy thoughts while you fuck me, [terri.name].  You're a pretty young girl with a sexy, hairless pussy.  Think about that or whatever makes you wet while you push yourself back against my cock."
                                    wt_image indy_shave_1_20
                                    "Slowly she starts to relax.  Not a lot, but enough to be able to move more easily along your cock.  She's not a natural.  You guide her with your hands on her hips, helping her figure out how to fuck your cock."
                                    wt_image indy_shave_1_21
                                    "You let her keep at it, learning as much as she can about pleasing a man this way until she's getting tired and your balls are aching to burst.  Then you give her a reward for her efforts, in the form of your cum shooting inside her."
                                    wt_image indy_shave_1_22
                                    player.c "[player.orgasm_text]"
                                    wt_image indy_shave_1_17
                                    terri.c "Was that okay?  Did I do better than the first time?"
                                    wt_image indy_shave_1_16
                                    player.c "Yes, you did great, [terri.name].  Another lesson or two, and you'll be a top-grade fucker."
                                    wt_image indy_shave_1_8
                                    terri.c "Oh, good.  Thank you!  And thanks for encouraging me to look and act younger, I'm going to try more of that."
                                    $ terri.sex_training_count += 1
                                    change terri sos by 10
                                "Just enjoy fucking her bald snatch":
                                    wt_image indy_shave_1_10
                                    "Her freshly shaved pussy is too enticing to waste time trying to train her right now.  You position yourself between her legs and shove yourself inside."
                                    call terri_shaved_sex from _call_terri_shaved_sex
                        elif terri.sex_training_count == 2:
                            wt_image indy_shave_1_6
                            terri.c "You want to have sex again?  Should I be on my hands-and-knees like last time?"
                            $ title = "What do you want?"
                            menu:
                                "Train her":
                                    wt_image indy_shave_1_5
                                    player.c "Not today.  Today I'm going to lie down and you're going to straddle me."
                                    wt_image indy_shave_1_16
                                    terri.c "You want me on top?"
                                    player.c "I do.  I'm going to teach you how to bring a man to orgasm by riding his cock."
                                    wt_image indy_shave_1_23
                                    "As usual, despite her willingness to have sex with you and a generous application of lube ..."
                                    wt_image indy_shave_1_24
                                    "... her body struggles to open up enough to fit you inside."
                                    wt_image indy_shave_1_25
                                    player.c "In this position, you control when and how far I go inside you, [terri.name].  Let your mind relax and think sexy thoughts as you relax and play with yourself.    You're a pretty young girl with a sexy, hairless pussy.  Close your eyes and think about that or whatever makes you wet as you settle onto my cock."
                                    wt_image indy_shave_1_26
                                    "It takes a while, but eventually she relaxes enough that she can start to move on you without discomfort."
                                    wt_image indy_shave_1_27
                                    player.c "Fuck me now, [terri.name].  Ride my hard cock up and down.  Start off nice and slow and easy, then pick up the pace."
                                    wt_image indy_shave_1_28
                                    "You help guide her with your hands on her ass, showing her how to slam down on the down thrusts, how far to come up on the up thrusts, and when to move faster."
                                    wt_image indy_shave_1_29
                                    player.c "Use your cunt muscles, too, [terri.name].  Grip me at the top, then relax as you slam down.  Squeeze again at the bottom before rising up again."
                                    wt_image indy_shave_1_30
                                    "This is new to her, but she's getting the hang of it.  She rides you faster and faster, squeezing and milking you as best she can.  When you think her legs muscles are ready to give out from fatigue, you take pity on her and let yourself climax.  She doesn't orgasm herself, but she gives a little moan of satisfaction as she feels you release your seed inside her."
                                    wt_image indy_shave_1_31
                                    player.c "[player.orgasm_text]"
                                    wt_image indy_shave_1_32
                                    terri.c "Oh!"
                                    wt_image indy_shave_1_6
                                    player.c "Keep working on squeezing with your Kegel muscles and pay attention to the man's reactions to know when to go slower and when to go faster.  Keep practicing, and you'll soon be a dream lay for any man."
                                    wt_image indy_shave_1_8
                                    terri.c "Thank you!  Coming from you, that means a lot!  And thanks for encouraging me to look and act younger, I'm going to try more of that."
                                    change terri sos by 10
                                    $ terri.sex_training_count += 1
                                "Just enjoy fucking her bald snatch":
                                    wt_image indy_shave_1_5
                                    player.c "Not today.  Just spread your legs and lie back so I can enjoy looking at your hairless pussy while I fuck you."
                                    wt_image indy_shave_1_10
                                    "You position yourself between her legs and shove yourself inside her enticing bald sex."
                                    call terri_shaved_sex from _call_terri_shaved_sex_1
                        else:
                            wt_image indy_shave_1_6
                            terri.c "You want to have sex again?  Should I climb on top?"
                            wt_image indy_shave_1_5
                            player.c "Not today.  Just spread your legs and lie back so I can enjoy looking at your hairless pussy while I fuck you."
                            wt_image indy_shave_1_10
                            "You position yourself between her legs and shove yourself inside her enticing bald sex."
                            call terri_shaved_sex from _call_terri_shaved_sex_2
                        $ terri.sex_count += 1
                        orgasm
                $ terri.youth_interest += 1
                sys "[terri.name] is now more interested in acting young."
            "What you've done is great":
                wt_image indy_portrait_state_2
                "She smiles happily."
                $ terri.temporary_count = 0 # prevents end_day
    elif terri.youth_interest == 3 and terri.has_tag('youth_first_conversation'):
        wt_image indy_talk_state_3_7
        player.c "[terri.name], have you been giving any thought to behaving younger?"
        wt_image indy_talk_state_3_1
        terri.c "Yes, I've been trying to dress like a young woman and act accordingly.  Do you like my current look?"
        wt_image indy_portrait_state_3
        $ title = "What do you tell her?"
        menu:
            "You could go further":
                player.c "You look great, [terri.name], but you could go further."
                wt_image indy_talk_state_3_3
                terri.c "Really?  You don't think it will be too much?"
                player.c "Not at all.  Do you remember what it was like being a schoolgirl?"
                wt_image indy_talk_state_3_5
                terri.c "Yes!  I loved those days.  Not the studying, of course, but the fun we had."
                wt_image indy_talk_state_3_7
                "You hand her a backpack with clothes."
                wt_image indy_talk_state_3_4
                player.c "Change, then meet me at the high school around the corner."
                if hannah.location == school:
                    dismiss hannah # this removes her from the room for the following scene at the school
                call forced_movement(school) from _call_forced_movement_990
                wt_image indy_school_1_1
                "You watch from a distance as [terri.name] arrives ..."
                wt_image indy_school_1_2
                "... and takes a seat on the school bleachers."
                wt_image indy_school_1_3
                "The school is open, but the students and teachers are all inside.  [terri.name] sits by herself as she waits for you to show yourself."
                wt_image indy_school_1_4
                "She smiles shyly as you approach."
                wt_image indy_school_1_5
                player.c "Class is in, [terri.name]. Follow me."
                if hannah.letter_re_terri < 2 or hannah.letter_re_terri > 7:
                    wt_image indy_school_1_6
                    if hannah.letter_re_terri > 7:
                        "Principal Hannah won't be happy if you're caught in the school, but she's not really in any position to object."
                    else:
                        "You lead her to an empty classroom.  Enrollment is down in this district, and this room isn't being used this year."
                    wt_image indy_school_1_7
                    player.c "Take your seat, young lady."
                    wt_image indy_school_1_8
                    player.c "Did you complete your homework assignment?"
                    wt_image indy_school_1_9
                    terri.c "I didn't know I had homework!"
                    wt_image indy_school_1_10
                    player.c "Your assignment was to practice sucking and fucking, in order to become a better girlfriend.  Remember?"
                    wt_image indy_school_1_11
                    "She giggles."
                    terri.c "Oh, that homework!  Yes, [terri.your_respect_name], I completed all of it."
                    if terri.sex_count > 0 and terri.blowjob_training_count > 0:
                        $ title = "What do you tell her?"
                        menu:
                            "Demonstrate on me how you completed your assignment":
                                wt_image indy_school_1_52
                                terri.c "Demonstrate on you?  Well, okay.  You're the teacher, so if you say so.  First I took off my top, just like you taught me to ..."
                                wt_image indy_school_1_53
                                terri.c "... so he could look at my perky little schoolgirl titties ..."
                                wt_image indy_school_1_54
                                terri.c "... as I got down on my knees and opened his pants, like this."
                                wt_image indy_school_1_55
                                terri.c "His cock isn't as big as yours is ..."
                                wt_image indy_school_1_56
                                terri.c "... but it got nice and hard under my hand, just like yours is getting."
                                wt_image indy_school_1_57
                                terri.c "Before I started sucking on it, I licked up and down his shaft like you taught me to ..."
                                wt_image indy_school_1_58
                                terri.c "... and just like you are, he got even harder.  So that's when I popped him into my mouth and did this."
                                wt_image indy_school_1_59
                                "[terri.name] takes you into her mouth ..."
                                wt_image indy_school_1_60
                                "... and begins an awkward blowjob ..."
                                if terri.blowjob_training_count > 2:
                                    wt_image indy_school_1_62
                                    "... that at least features lots of eye-contact ..."
                                    wt_image indy_school_1_63
                                    "... and ball-cupping, that earns an 'A' for effort, but a 'C-' at best for technique before [terri.name] stops."
                                else:
                                    wt_image indy_school_1_61
                                    "... that earns an 'A' for effort, but a 'D-' at best for technique before [terri.name] stops."
                                wt_image indy_school_1_64
                                terri.c "After I sucked him until he was close to being ready to cum, I pulled off my panties ..."
                                if terri.sex_training_count > 2:
                                    wt_image indy_school_1_75
                                    terri.c "... and asked him to lie down ..."
                                    wt_image indy_school_1_76
                                    terri.c "... so I could lower myself onto his hard dick, like this."
                                    wt_image indy_school_1_77
                                    "She's barely wet, and it takes her a while to work your cock fully inside her, but eventually she manages."
                                    wt_image indy_school_1_78
                                    terri.c "Then I rode him like this, just like you taught me to, until he filled me with his goo."
                                    wt_image indy_school_1_79
                                    "[terri.name] doesn't really get any wetter, but that doesn't stop her from enthusiastically bouncing her tight pussy up and down on your cock until you fill her with your goo, too."
                                    wt_image indy_school_1_80
                                elif terri.sex_training_count == 2:
                                    wt_image indy_school_1_70
                                    terri.c "... and turned around and bent over."
                                    wt_image indy_school_1_71
                                    terri.c "Then I let him put his cock inside me, just like you're doing."
                                    wt_image indy_school_1_72
                                    "She's barely wet, so you have to be careful and slow entering her.  Presumably her boyfriend has learned to do likewise."
                                    wt_image indy_school_1_73
                                    terri.c "After he pushed himself inside me, I started fucking back against him, just like you taught me, until he filled me with his goo."
                                    wt_image indy_school_1_74
                                    "With [terri.name] thrusting her cute butt back and forth as she fucks herself on your cock, it's not long before you fill her with your goo, too."
                                    wt_image indy_school_1_72
                                else:
                                    wt_image indy_school_1_65
                                    terri.c "... and spread my legs for him."
                                    wt_image indy_school_1_66
                                    terri.c "Then I let him put his cock inside me, just like you're doing."
                                    wt_image indy_school_1_67
                                    "She's barely wet, so you have to be careful and slow entering her.  Presumably her boyfriend has learned to do likewise."
                                    wt_image indy_school_1_68
                                    terri.c "Then I laid there like a good girlfriend and waited while he fucked me until he filled me with his goo."
                                    wt_image indy_school_1_69
                                    "As passive as [terri.name] is, it takes a while, but she's pretty enough and her pussy is tight enough that you eventually fill her with your goo, too."
                                player.c "[player.orgasm_text]"
                                wt_image indy_school_1_26
                                terri.c "First my boyfriend, now my teacher.  It's a good thing I'm on birth control, isn't it?  A schoolgirl like me shouldn't get pregnant."
                                wt_image indy_school_1_11
                                terri.c "This is so fun!  I'm just imagining what it would be like to be a schoolgirl again with no care in the world other than to learn how to look after my boyfriend.  I love it!  Thank you for doing this for me."
                                $ terri.sex_count += 1
                                orgasm
                            "Tell me how you completed your assignment":
                                wt_image indy_school_1_10
                                call terri_school_tell_classroom from _call_terri_school_tell_classroom
                    else:
                        wt_image indy_school_1_10
                        "You haven't had sex with her yet, and this is likely not the best way to start her hands-on training."
                        call terri_school_tell_classroom from _call_terri_school_tell_classroom_1
                else:
                    wt_image indy_school_1_32
                    if hannah.letter_re_terri == 2:
                        "You'd like to take [terri.name] into the school, but after the letter you received from the last time you entered school grounds, you decide it would be better not to.  You lead her to the adjacent public park instead."
                    else:
                        "You'd like to take [terri.name] to school, but if Principal Hannah catches you on school grounds again, it could get ugly.  Better not risk that.  You lead her to the adjacent public park instead."
                    wt_image indy_school_1_33
                    player.c "Did you complete your homework assignment?"
                    wt_image indy_school_1_34
                    terri.c "I didn't know I had homework!"
                    wt_image indy_school_1_35
                    player.c "Your assignment was to practice sucking and fucking your boyfriend, in order to become a better girlfriend.  Remember?"
                    wt_image indy_school_1_36
                    "She giggles."
                    terri.c "Oh, that homework!  Yes, [terri.your_respect_name], I completed all of it."
                    wt_image indy_school_1_37
                    player.c "Tell me how you completed your assignment."
                    wt_image indy_school_1_38
                    if terri.blowjob_training_count > 0:
                        terri.c "Well, [terri.your_respect_name], first I took off my top, just like you told me to, so he could look at my perky little schoolgirl titties. Then I got down on my knees and removed his cock from his pants. It's not as big as your cock, but it got nice and hard in my hand."
                        wt_image indy_school_1_39
                        terri.c "Then I put it in my mouth, and it got even harder."
                        if terri.sex_training_count > 2:
                            wt_image indy_school_1_40
                            terri.c "After I sucked him until he was close to being ready to cum, I pulled off my panties ..."
                            wt_image indy_school_1_43
                            terri.c "...and climbed on top of him and lowered myself onto his hard dick."
                            wt_image indy_school_1_44
                            terri.c "Then I rode him just like you taught me to, until he filled me with his goo.  So it's a good thing I'm on birth control, isn't it?"
                        elif terri.sex_training_count == 2:
                            wt_image indy_school_1_41
                            terri.c "After I sucked him until he was close to being ready to cum, I turned around and pulled off my panties."
                            wt_image indy_school_1_42
                            terri.c "When he pushed himself inside me, I started fucking back against him, just like you taught me, until he filled me with his goo.  So it's a good thing I'm on birth control, isn't it?"
                        else:
                            wt_image indy_school_1_40
                            terri.c "After I sucked him until he was close to being ready to cum, I pulled off my panties and lay down on the floor and spread my legs.  Then I let him fuck me until he filled me with his goo.  So it's a good thing I'm on birth control, isn't it?"
                    else:
                        terri.c "Well, [terri.your_respect_name], I knelt down beside him on the couch and took his cock out of his pants."
                        wt_image indy_school_1_39
                        terri.c "After it got hard in my hand, I put it in my mouth and it got even harder."
                        wt_image indy_school_1_40
                        terri.c "After I sucked him until he was close to being ready to cum, I pulled off my panties and spread my legs.  Then I let him fuck me until he came inside me."
                    wt_image indy_school_1_45
                    terri.c "This is so fun!  I'm just imagining what it would be like to be a schoolgirl again with no care in the world other than to learn how to look after my boyfriend.  I love it!  Thank you for doing this for me."
                    $ title = "How did she do on her assignment?"
                    menu:
                        "Very well, praise her":
                            wt_image indy_school_1_46
                            player.c "You make a wonderful schoolgirl.  Any teacher would be happy to have you for their student."
                            wt_image indy_school_1_47
                            terri.c "Thank you!  I feel lucky to have you as my teacher."
                        "Not well enough (punish her)":
                            wt_image indy_school_1_48
                            player.c "Unfortunately, [terri.name], I don't think you've learned the lessons I've been trying to teach you near well enough.  Turn around."
                            wt_image indy_school_1_49
                            player.c "Hopefully this spanking will teach you to take your lessons more seriously in the future, young lady."
                            wt_image indy_school_1_50
                            "You keep the spanking light enough to be playful, but firm enough to still sting a little ... *smack*  *smack*  *smack*  *smack*  *smack*"
                            wt_image indy_school_1_51
                            terri.c "Ow!  I'm sorry I didn't do a better job on my homework.  I promise to be a better student in the future."
                            change terri submission by 5
                if hannah.letter_re_terri == 0:
                    $ hannah.letter_re_terri = 1
                    if day == 1:
                        $ hannah.visit_day = 2
                    elif day == 5:
                        $ hannah.visit_day = 4
                    else:
                        $ hannah.visit_day = day
                    $ hannah.visit_week = week
                $ terri.youth_interest += 1
                sys "[terri.name] is now more interested in acting young."
                call forced_movement(living_room) from _call_forced_movement_991
                call character_location_return(hannah) from _call_character_location_return_709
            "What you've done is great":
                wt_image indy_talk_state_3_2
                "She smiles happily."
                $ terri.temporary_count = 0 # prevents end_day
    elif terri.youth_interest == 4 and terri.has_tag('youth_first_conversation'):
        wt_image indy_talk_state_4_9
        player.c "[terri.name], have you been embracing acting like a schoolgirl?"
        wt_image indy_talk_state_4_2
        terri.c "I have and I really like it!  I feel so young and happy.  I don't have a care in the world when I get to play the schoolgirl around you."
        wt_image indy_portrait_state_4
        $ title = "What do you tell her?"
        menu:
            "You could go further":
                player.c "I'm glad to hear that, [terri.name].  But I think you could look younger still."
                wt_image indy_talk_state_4_3
                terri.c "Really?  I love the idea, but is it really appropriate?  Wouldn't it be weird for a grown woman to be acting like a young girl?"
                wt_image indy_talk_state_4_11
                player.c "No back talk, young lady.  I went through the trouble of setting up a play area for you.  Go make use of it, and I'll tell you when playtime is over."
                wt_image indy_talk_state_4_9
                "You hand her a change of clothing and direct her to the garage."
                wt_image indy_talk_state_4_6
                terri.c "Yes ..."
                wt_image indy_talk_state_4_7
                "She hesitates, then completes her thought in a rush."
                wt_image indy_talk_state_4_8
                terri.c "Yes, [terri.your_daddy_name].  Thank you!"
                call forced_movement(garage) from _call_forced_movement_992
                wt_image indy_pool_1_20
                "[terri.name] changes into the little bikini you bought her and joins you in the garage.  She giggles when she sees the splash pool you've set up."
                wt_image indy_pool_1_1
                terri.c "Is this all for me?"
                wt_image indy_pool_1_10
                player.c "It is, but when I tell you playtime is over, that means it's over.  You need to get out of the pool right away."
                wt_image indy_pool_1_11
                terri.c "Yes, [terri.your_daddy_name]!  I will."
                wt_image indy_pool_1_6
                "[terri.name] happily plays and splashes in the pool.  She looks like she doesn't have a care in the world."
                wt_image indy_pool_1_7
                terri.c "Watch this!  Look at the splash I can make!"
                wt_image indy_pool_1_8
                "As you watch, she bounces the beach ball into the water, laughing as it splashes up over her."
                wt_image indy_pool_1_9
                "You let her play for nearly an hour.  She doesn't show any sign of getting tired."
                wt_image indy_pool_1_2
                player.c "Okay, young lady. Play time is over."
                wt_image indy_pool_1_10
                terri.c "No!  Just five more minutes.  Please?"
                $ title = "What do you tell her?"
                menu:
                    "Time's up":
                        wt_image indy_pool_1_3
                        player.c "I said no fussing when playtime was over. Get out the pool right now, young lady, or next time there will be no pool."
                        wt_image indy_pool_1_5
                        "With a sulk, she puts down the ball and crawls out of the pool."
                        terri.c "Yes, [terri.your_respect_name]."
                        change terri submission by 10 notify
                    "Okay, five more minutes":
                        wt_image indy_pool_1_4
                        player.c "Okay, five more minutes. Then it's time to get out of the pool."
                        wt_image indy_pool_1_21
                        terri.c "Thank you, [terri.your_daddy_name]!"
                        wt_image indy_pool_1_6
                        "She's really getting into this youth play."
                        # note: would add a stat boost here, but there's nothing useful to provide
                $ terri.youth_interest += 1
                sys "[terri.name] is now more interested in acting young."
                call forced_movement(living_room) from _call_forced_movement_993
            "What you've done is great":
                wt_image indy_talk_state_4_1
                "She smiles happily."
                $ terri.temporary_count = 0 # prevents end_day
    elif terri.youth_interest == 5 and terri.has_tag('youth_first_conversation') and not terri.has_tag('completed_youth_5'):
        wt_image indy_talk_state_5_1
        player.c "How is my little girl today?"
        wt_image indy_talk_state_5_4
        terri.c "Great!  You are so good to me.  Nobody has made me feel this safe and cared for in a long time.  I really feel like a little girl around you, and I love it."
        wt_image indy_portrait_state_5
        $ title = "What do you tell her?"
        menu:
            "You could go further":
                add tags 'completed_youth_5' to terri
                wt_image indy_talk_state_5_2
                player.c "I have a new outfit for you, [terri.name].  One even better suited for a little girl.  Go try it on."
                wt_image indy_talk_state_5_3
                terri.c "Yaayyyy!!"
                call terri_youth_5_session from _call_terri_youth_5_session
            "This is as far as we go":
                wt_image indy_hypno_state_5_1
                terri.c "Okay.  Can I play in the splash pool again?"
                $ title = "What do you tell her?"
                menu:
                    "Yes, you can play in the pool":
                        wt_image indy_talk_state_5_4
                        terri.c "Yay!!!  Thank you!!"
                        wt_image current_location.image
                        "You go prepare the splash pool while she changes into her swimsuit."
                        call forced_movement(garage) from _call_forced_movement_994
                        wt_image indy_pool_1_20
                        player.c "Remember, when I tell you playtime is over, that means it's over.  You need to get out of the pool right away."
                        wt_image indy_pool_1_1
                        terri.c "Yes, [terri.your_respect_name]!  I will."
                        wt_image indy_pool_1_2
                        "[terri.name] happily plays and splashes in the pool.  She looks like she doesn't have a care in the world."
                        wt_image indy_pool_1_7
                        terri.c "Watch this!  Look at the splash I can make!"
                        wt_image indy_pool_1_8
                        "As you watch, she bounces the beach ball into the water, laughing as it splashes up over her."
                        wt_image indy_pool_1_6
                        "You let her play for nearly an hour. She doesn't show any sign of getting tired."
                        wt_image indy_pool_1_2
                        player.c "Okay young lady, play time is over."
                        wt_image indy_pool_1_10
                        terri.c "No!  Just five more minutes.  Please?"
                        $ title = "What do you tell her?"
                        menu:
                            "Time is up":
                                wt_image indy_pool_1_3
                                player.c "I said no fussing when playtime was over.  Get out the pool right now, young lady, or next time there will be no pool."
                                wt_image indy_pool_1_5
                                terri.c "Yes, [terri.your_respect_name]."
                                "With a sulk, she puts down the ball and crawls out of the pool."
                                change terri submission by 10
                            "Okay, five more minutes":
                                wt_image indy_pool_1_4
                                player.c "Okay, five more minutes.  Then it's time to get out of the pool."
                                wt_image indy_pool_1_21
                                terri.c "Thank you [terri.your_daddy_name]!"
                                wt_image indy_pool_1_9
                                "She's really getting into this youth play."
                                # note: would add a stat boost here, but there's nothing useful to provide
                        call forced_movement(living_room) from _call_forced_movement_995
                    "No, we have things to do":
                        wt_image indy_hypno_state_5_2
                        terri.c "Awwwww"
                        "She looks disappointed."
                        $ terri.temporary_count = 0
    elif terri.has_tag('completed_youth_5'):
        wt_image indy_talk_state_5_1
        player.c "How is my little girl today?"
        wt_image indy_talk_state_5_4
        terri.c "Great!  You are so good to me.  Nobody has made me feel this safe and cared for in a long time.  I really feel like a little girl around you, and I love it.  Should I change into the little girl outfit you bought me?"
        $ title = "What do you tell her?"
        menu:
            "Yes, go change":
                call terri_youth_5_session from _call_terri_youth_5_session_1
            "No, we have things to do":
                wt_image indy_hypno_state_5_2
                terri.c "Awwwww"
                "She looks disappointed."
                $ terri.temporary_count = 0
    call terri_end_training_session from _call_terri_end_training_session # checks to see if training actually complete and if so, ends_day
    return

label terri_youth_5_session:
    wt_image living_room.image
    "She squeals in delight and runs off to change."
    wt_image indy_lolly_1_14
    terri.c "Look, [terri.your_daddy_name]!  I changed all by myself!"
    wt_image indy_lolly_1_15
    player.c "What a clever girl you are."
    wt_image indy_lolly_1_16
    terri.c "They're a little scratchy.  Do I have to keep all of my clothes on when I play?"
    wt_image indy_lolly_1_17
    player.c "Not when you're playing around the house under my supervision, no, but when you're playing outside where boys can see you, I expect my little girl to keep her clothes on."
    wt_image indy_lolly_1_18
    terri.c "I'm allowed to go outside like this?"
    wt_image indy_lolly_1_19
    player.c "As long as you stay in the yard where I can see you and keep your clothes on, yes, you can go outside and play.  Would you like to go outside to play now?"
    wt_image indy_lolly_1_20
    terri.c "Ummm, what will people think if they see me playing in your yard, dressed like this?"
    wt_image indy_lolly_1_21
    player.c "They'll think I have the prettiest little girl in the neighborhood."
    wt_image indy_lolly_1_15
    terri.c "Thank you, [terri.your_daddy_name], but I think I'll stay inside to play today.  I don't think I'm ready to share this side of me with anyone other than you, just yet."
    wt_image indy_lolly_1_22
    player.c "Not even your boyfriend?"
    wt_image indy_lolly_1_23
    terri.c "Just you, [terri.your_daddy_name]."
    wt_image indy_lolly_1_24
    if terri.youth_interest == 5:
        "She looks at you with admiration as she plays by herself, making quiet 'goo goo ga ga' sounds so softly you can barely make them out."
    else:
        "She looks at you with admiration as she plays by herself, making quiet sounds to herself so softly you can barely make them out."
    wt_image indy_lolly_1_25
    "After a few minutes, she suddenly becomes serious and goes back to using proper words."
    wt_image indy_lolly_1_26
    terri.c "[terri.your_daddy_name], if I take my clothes off to play, will you supervise me and keep me safe?"
    $ title = "What do you do?"
    menu menu_terri_youth_5_menu:
        "Ask if she wants to be a little girl who plays naked":
            wt_image indy_lolly_1_27
            terri.c "Yes, [terri.your_daddy_name].  The thought of being too young to wear clothes makes me tingly down here."
            jump menu_terri_youth_5_menu
        "Tell her to show you her tits, first" if not terri.has_tag('examined_tits_today'):
            add tags 'examined_tits_today' to terri
            wt_image indy_lolly_1_28
            player.c "I want to see your chest, first, before I decide."
            wt_image indy_lolly_1_29
            terri.c "[terri.your_daddy_name], you know your little girl has a very flat chest."
            wt_image indy_lolly_1_30
            terri.c "You don't mind looking at my flat chest, do you [terri.your_daddy_name]?  It's okay for a little girl not to have big tits, right?"
            wt_image indy_lolly_1_31
            $ title = "What do you tell her?"
            menu:
                "Her flat chest is perfect":
                    wt_image indy_lolly_1_34
                    terri.c "Thank you, [terri.your_daddy_name]!  It makes me happy that you like my little girl shape."
                    wt_image indy_lolly_1_26
                    terri.c "Will you supervise me while I play naked, now?"
                    if terri.boobjob_interest > 0:
                        $ terri.boobjob_interest -= 1
                        sys "[terri.name] is now less self-conscious about the size of her breasts."
                "All that matters is that she likes them":
                    wt_image indy_lolly_1_33
                    terri.c "Thank you, [terri.your_daddy_name].  I think having a flat chest is perfect for a little girl like me."
                    wt_image indy_lolly_1_26
                    terri.c "Will you supervise me while I play naked, now?"
                "She should have bigger tits":
                    wt_image indy_lolly_1_32
                    player.c "Even little girls would please their men more if they had big tits."
                    wt_image indy_lolly_1_26
                    terri.c "I'm sorry my breasts are so small, [terri.your_daddy_name].  Would you supervise me while I play naked anyway, even though my chest isn't anything interesting for you to look at?"
                    $ terri.boobjob_interest += 1
                    sys "[terri.name] is now more self-conscious about the size of her breasts."
                    change terri submission by 5 notify
            $ title = "What do you do?"
            jump menu_terri_youth_5_menu
        "Encourage her":
            wt_image indy_lolly_1_34
            player.c "Of course I'll watch over my little girl as she's playing naked."
            wt_image indy_lolly_1_33
            terri.c "Thank you, [terri.your_daddy_name]!"
            wt_image indy_lolly_1_36
            "She pulls off her top ..."
            wt_image indy_lolly_1_37
            "... and bottoms ..."
            wt_image indy_lolly_1_38
            "... and goes back to playing happily by herself."
            wt_image indy_lolly_1_39
            if terri.youth_interest == 5:
                "The 'goo goo ga ga' sounds she makes to herself while she plays are louder and bolder now ..."
                wt_image indy_lolly_1_40
                "... although she scrutinizes your face for signs of a reaction after she makes them."
            else:
                "She makes quiet sounds to herself while she plays ..."
                wt_image indy_lolly_1_40
                "... while scrutinizing your face, perhaps to make sure you can't hear what she's saying."
            wt_image indy_lolly_1_41
            "After a while, she leans in and goes back to using words to address you."
            wt_image indy_lolly_1_42
            terri.c "I'm not so little a girl that [terri.your_daddy_name] can't put his dick inside me, if you need some relief after supervising me."
            wt_image indy_lolly_1_41
            $ title = "Fuck her?"
            menu:
                "Yes, have sex with her":
                    wt_image indy_lolly_1_43
                    "[terri.name] literally 'cooes' as you lift her legs into the air ..."
                    wt_image indy_lolly_1_44
                    "... and spread them wide."
                    wt_image indy_lolly_1_45
                    "She holds herself open for you as you enter her, and you're happy to find her pussy is pleasantly moist and warm around your cock."
                    wt_image indy_lolly_1_46
                    "Despite her body's welcoming response to your cock, [terri.name]'s mostly detached while you're fucking her.  It's clear she wants this to be enjoyable for you and isn't particularly concerned about enjoying it herself ..."
                    wt_image indy_lolly_1_47
                    "... but at least she does sigh contentedly as you empty your load inside her."
                    player.c "[player.orgasm_text]"
                    wt_image indy_lolly_1_48
                    terri.c "It felt really nice, having you fill me up like that, knowing that I can be a little girl and still please you.  This whole visit has been amazing.  Thank you!"
                    $ terri.sex_count += 1
                    orgasm
                "Not today":
                    wt_image indy_lolly_1_42
                    terri.c "Okay, [terri.your_daddy_name].  Just know that your little girl doesn't mind taking care of [terri.your_daddy_name]'s needs."
            if terri.youth_interest == 5:
                $ terri.youth_interest += 1 # takes her to youth_interest = 6, triggering possible adult baby content
                sys "[terri.name] is now more interested in acting young."
        "Discourage her":
            wt_image indy_lolly_1_25
            player.c "I'm worried you're taking this too far, [terri.name].  Just how young do you want to act, anyway?"
            wt_image indy_lolly_1_35
            if terri.youth_interest == 5:
                terri.c "I'm not sure.  Younger than my boyfriend would be comfortable with, that much I know.  I wasn't sure if maybe with you, though ..."
                $ title = "What do you do?"
                menu:
                    "Let her think about what she really wants":
                        wt_image indy_lolly_1_20
                        terri.c "Thank you.  I'll think it over before my next visit."
                        $ terri.youth_interest += 1 # takes her to youth_interest = 6, triggering possible adult baby content
                        sys "[terri.name] is now more interested in acting young."
                    "Tell her 'goo goo ga ga' is too far":
                        wt_image indy_lolly_1_19
                        terri.c "You're right, I was making a fool of myself, making baby sounds.  How about I head home and I won't be so silly on my next visit?"
                $ terri.temporary_count = 2 # sets energy use to short
            else:
                terri.c "Don't worry, [terri.your_daddy_name].  You made it clear I shouldn't take this any further, and I won't.  But can we roleplay you looking after me as your naked little girl?"
                add tags 'discouraged_today' to terri
                jump menu_terri_youth_5_menu
        "End session" if terri.has_tag('discouraged_today'):
            wt_image indy_lolly_1_19
            terri.c "I'm sorry for suggesting something you weren't comfortable with.  I'd best head home now."
            $ terri.temporary_count = 2 # sets energy use to short
    rem tags 'discouraged_today' 'examined_tits_today' from terri
    return

label terri_skills_training:
    $ terri.temporary_count = 1
    # skip if skills training complete
    if terri.blowjob_training_count > 2 and terri.sex_training_count > 2:
        "[terri.name] has learned as much as you can teach her about fucking and giving blow jobs.  It would be better to expand her horizons and try something new with her."
        $ terri.temporary_count = 0 # shuts off end_day
    # first sex step: blowjob
    elif terri.blowjob_training_count == 0:
        if terri.state == 1:
            wt_image indy_talk_state_1_2
        elif terri.state == 2:
            wt_image indy_talk_state_2_4
        elif terri.state == 3:
            wt_image indy_portrait_state_3
        elif terri.state == 4:
            wt_image indy_portrait_state_4
        elif terri.state == 5:
            wt_image indy_portrait_state_5
        player.c "[terri.name], in order to help you to become better at pleasing your boyfriend, I need to understand what you're currently doing well, and where you need help."
        if terri.state == 1:
            wt_image indy_bj_1_state_1_1
            terri.c "I know.  It's okay.  I'm ready to have sex with you.  I know it's cheating on my boyfriend, but I'm doing it for him, so I think that makes it okay."
            player.c "I'm sure it is.  Can you show me how you would please him, if you wanted to do something special for him?"
            wt_image indy_bj_1_state_1_2
            "She says nothing, just leans over and takes your cock out of your pants.  With no hesitation, she puts you in her mouth. Holding you by the base of your cock, she begins vigorously sucking on the head until you stand up and stop her."
            wt_image indy_bj_1_state_1_20
            player.c "That's very nice, and in the right place and time, getting a blow job while you're fully dressed can be very exciting. But usually your boyfriend will prefer to see your body while you're pleasuring him."
            wt_image indy_bj_1_state_1_15
            terri.c "Oh.  Sorry."
            wt_image indy_strip_state_1_3
            "With only a hint of embarrassment, she pulls off her clothes."
            wt_image indy_bj_1_state_1_3
            "A moment later, she's back on your cock, sucking vigorously.  You let her continue for a moment to see if she will change her technique, but she doesn't."
            wt_image indy_bj_1_state_1_16
            player.c "Hold on a moment, [terri.name].  There'll be times when leaning over your boyfriend will be a great way to deliver a blow job. Most of the time, though, men will want to watch you suck their cock and see you looking up at them while you do it.  Get down on the floor and then continue."
            call terri_first_bj_ending from _call_terri_first_bj_ending
        elif terri.state == 2:
            wt_image indy_bj_1_state_2_1
            terri.c "I know. It's okay. I'm ready to have sex with you. I know it's cheating on my boyfriend, but I'm doing it for him, so I think that makes it okay."
            player.c "I'm sure it is. Can you show me how you would please him, if you wanted to do something special for him?"
            wt_image indy_bj_1_state_2_2
            "She says nothing, just kneels down in front of you and takes your cock out of your pants.  With no hesitation, she starts to lick your cock."
            wt_image indy_bj_1_state_2_3
            player.c "That's very nice, and in the right place and time, getting a blow job while you're fully dressed can be very exciting. But usually your boyfriend will prefer to see your body while you're pleasuring him."
            wt_image indy_strip_state_2_7
            terri.c "Oh.  Sorry."
            wt_image indy_strip_state_2_4
            "With no sign of embarrassment, she pulls off her clothes."
            wt_image indy_bj_1_state_1_3
            "A moment later, she's on your cock, sucking vigorously. You let her continue for a moment to see if she will change her technique, but she doesn't."
            wt_image indy_bj_1_state_1_16
            player.c "Hold on a moment, [terri.name]. There'll be times when leaning over your boyfriend will be a great way to deliver a blow job. Most of the time, though, men will want to watch you suck their cock and see you looking up at them while you do it. Get down on the floor and then continue."
            call terri_first_bj_ending from _call_terri_first_bj_ending_1
        elif terri.state == 3:
            wt_image indy_bj_1_state_3_1
            terri.c "I know. It's okay. I'm ready to have sex with you. I know it's cheating on my boyfriend, but I'm doing it for him, so I think that makes it okay."
            player.c "I'm sure it is. Can you show me how you would please him, if you wanted to do something special for him?"
            wt_image indy_bj_1_state_3_2
            "She says nothing, just kneels down in front of you and takes your cock out of your pants. She gasps at the size of you."
            player.c "Don't worry, [terri.name]. The size doesn't matter. It works the same as your boyfriend's. In the right place and time, getting a blow job while you're fully dressed can be very exciting. But usually your boyfriend will prefer to see your body while you're pleasuring him."
            wt_image indy_hypno_state_3_4
            terri.c "Oh.  Sorry."
            wt_image indy_strip_state_3_8
            "With no sign of embarrassment, she pulls off her clothes."
            wt_image indy_bj_1_state_1_3
            "A moment later, she's on your cock, sucking vigorously. You let her continue for a moment to see if she will change her technique, but she doesn't."
            wt_image indy_bj_1_state_1_16
            player.c "Hold on a moment, [terri.name]. There'll be times when leaning over your boyfriend will be a great way to deliver a blow job. Most of the time, though, men like to be able to watch you sucking their cock, and to see you looking up at them while you do it. Get on your knees and then continue."
            call terri_first_bj_ending from _call_terri_first_bj_ending_2
        elif terri.state == 4:
            wt_image indy_strip_state_4_7
            terri.c "I know. It's okay. I'm ready to have sex with you. I know it's cheating on my boyfriend, but I'm doing it for him, so I think that makes it okay."
            wt_image indy_strip_state_4_2
            player.c "I'm sure it is. Can you show me how you would please him, if you wanted to do something special for him?"
            wt_image indy_bj_1_state_4_1
            "She says nothing, just kneels in front of you and takes your cock out of your pants."
            wt_image indy_bj_1_state_4_2
            player.c "That's good, [terri.name]. Usually your boyfriend will prefer to see all of your body while you're pleasuring him, so how about you strip off completely?"
            wt_image indy_strip_state_4_8
            terri.c "Oh.  Sorry."
            wt_image indy_strip_state_4_9
            "With no sign of embarrassment, she pulls off her remaining clothes."
            wt_image indy_bj_1_state_4_4
            "A moment later, she's back on your cock, sucking vigorously. You let her continue for a moment to see if she will change her technique, but she doesn't."
            wt_image indy_bj_1_state_4_3
            player.c "Hold on a moment, [terri.name]. This position is very nice, and there'll be times when leaning over your boyfriend will be a great way to deliver a blow job. Most of the time, though, men like to see you looking up at them while you blow them.  Get down on the floor on your knees and then continue."
            call terri_first_bj_ending from _call_terri_first_bj_ending_3
        elif terri.state == 5:
            wt_image indy_bj_1_state_5_1
            terri.c "I know.  It's okay, I'm ready to have sex with you.  I know it's cheating on my boyfriend, but I'm doing it for him, so I think that makes it okay."
            player.c "I'm sure it is. Can you show me how you would please him, if you wanted to do something special for him?"
            wt_image indy_bj_1_state_5_2
            "She says nothing, just kneels down in front of you as you take your cock out of your pants.  She gasps at the size of you."
            player.c "That's a good start, [terri.name]. In the right place and time, getting a blow job while you're fully dressed can be very exciting. But usually your boyfriend will prefer to see your body while you're pleasuring him."
            wt_image indy_strip_state_5_7
            terri.c "Oh.  Sorry."
            wt_image indy_strip_state_5_4
            "She stands up and with no sign of embarrassment, quickly pulls off her clothes."
            wt_image indy_bj_1_state_1_3
            "A moment later, she's on your cock, sucking vigorously. You let her continue for a moment to see if she will change her technique, but she doesn't."
            wt_image indy_bj_1_state_1_16
            player.c "Hold on a moment, [terri.name]. There'll be times when leaning over your boyfriend will be a great way to deliver a blow job. Most of the time, though, men will want to watch you suck their cock and see you looking up at them while you do it. Get down on the floor and then continue."
            call terri_first_bj_ending from _call_terri_first_bj_ending_4
        $ terri.blowjob_count += 1
        $ terri.blowjob_training_count = 1
        orgasm
        $ terri.temporary_count = 3 # note: very low because you're not really training, just observing
    # second sex step: intercourse
    elif terri.sex_training_count == 0:
        if terri.state == 1:
            wt_image indy_hypno_state_1_5
            player.c "Last time you showed me how you give your boyfriend a blow job, and I promised to help you get better at that.  We will do that, but before we do, I want to see how you do at fucking."
            wt_image indy_hypno_state_1_3
            terri.c "All right."
            wt_image indy_strip_state_1_1
            "[terri.name] immediately undresses ..."
            wt_image indy_sex_1_state_1_6
            "... then leans back and spreads her legs."
            wt_image indy_sex_1_state_1_5
            "You enter her gingerly.  Despite her willingness to do this, she's quite dry."
            wt_image indy_sex_1_state_1_1
            player.c "Are you always this dry, or is it just because you're nervous doing this for the first time with me?"
            wt_image indy_sex_1_state_1_3
            terri.c "What do you mean?"
            player.c "Your pussy.  You're not wet."
            wt_image indy_sex_1_state_1_7
            terri.c "Should I be?"
            player.c "Try playing with your clit.  It'll feel better if your body is excited."
            wt_image indy_sex_1_state_1_8
            "[terri.name] starts stroking her clit, but it doesn't make any difference. She lies there, not moving.  Which is understandable, considering how dry she is.  Any movement would surely be uncomfortable."
            player.c "[terri.name], do you want to be doing this?"
            wt_image indy_sex_1_state_1_4
            terri.c "Of course!  You said you wanted to see how I have sex."
            player.c "Is this what it's like with your boyfriend?"
            wt_image indy_sex_1_state_1_2
            terri.c "Yes.  Why?  Am I doing something wrong?"
            player.c "Is it uncomfortable when he fucks you?"
            wt_image indy_sex_1_state_1_4
            terri.c "A little.  He's not as big as you, so not as much as it is right now."
            wt_image indy_sex_1_state_1_6
            "You stop and get some lubricant.   That may make things easier."
            wt_image indy_sex_1_state_1_7
            player.c "Does that feel better?"
            wt_image indy_sex_1_state_1_5
            terri.c "Yes, that's much better.  Thank you!"
            wt_image indy_sex_1_state_1_7
            "Although she says it's better, and it must be without the discomfort of being dry, there's no evidence that she's enjoying this."
            wt_image indy_sex_1_state_1_1
            "Some women have difficulties with their natural lubrication, but with the lube you added, you think she should now be responding more than she is. She still isn't moving or participating in the fuck, yet she watches with a seeming hope that this is good for you. For a woman who wants to be good at sex, it doesn't seem to come naturally to her, either physically or instinctually."
            wt_image indy_sex_1_state_1_3
            terri.c "Am I doing something wrong?  You seem to be thinking a lot."
            player.c "No, [terri.name].  It's nothing that we can't work on."
            wt_image indy_sex_1_state_1_1
            "You don't want to undermine her confidence, and she is both beautiful and tight.  You set your thoughts aside and focus on your own pleasure."
            wt_image indy_sex_1_state_1_8
            player.c "[player.orgasm_text]"
            wt_image indy_strip_state_1_6
            terri.c "Was that all right?  You seemed to enjoy yourself at the end.  Did you learn anything I should be doing differently?"
            wt_image indy_strip_state_1_12
            player.c "It was great, [terri.name].  You're great.  We'll pick this up again on a future visit."
            wt_image indy_portrait_state_1
            terri.c "Okay.  I'm happy to work on anything you think I should be doing differently.  I really want to know how to be the best girlfriend I can be."
        elif terri.state == 2:
            wt_image indy_hypno_state_2_2
            player.c "Last time you showed me how you give your boyfriend a blow job, and I promised to help you get better at that.  We will do that, but before we do, I want to see how you do at fucking."
            wt_image indy_bj_1_state_2_1
            terri.c "All right."
            wt_image indy_strip_state_2_3
            "[terri.name] immediately undresses ..."
            wt_image indy_sex_1_state_1_6
            "... then leans back and spreads her legs."
            wt_image indy_sex_1_state_1_5
            "You enter her gingerly.  Despite her willingness to do this, she's quite dry."
            wt_image indy_sex_1_state_1_1
            player.c "Are you always this dry, or is it just because you're nervous doing this for the first time with me?"
            wt_image indy_sex_1_state_1_3
            terri.c "What do you mean?"
            player.c "Your pussy.  You're not wet."
            wt_image indy_sex_1_state_1_7
            terri.c "Should I be?"
            player.c "Try playing with your clit.  It'll feel better if your body is excited."
            wt_image indy_sex_1_state_1_8
            "[terri.name] starts stroking her clit, but it doesn't make any difference. She lies there, not moving.  Which is understandable, considering how dry she is.  Any movement would surely be uncomfortable."
            player.c "[terri.name], do you want to be doing this?"
            wt_image indy_sex_1_state_1_4
            terri.c "Of course!  You said you wanted to see how I have sex."
            player.c "Is this what it's like with your boyfriend?"
            wt_image indy_sex_1_state_1_2
            terri.c "Yes.  Why?  Am I doing something wrong?"
            player.c "Is it uncomfortable when he fucks you?"
            wt_image indy_sex_1_state_1_4
            terri.c "A little.  He's not as big as you, so not as much as it is right now."
            wt_image indy_sex_1_state_1_6
            "You stop and get some lubricant.   That may make things easier."
            wt_image indy_sex_1_state_1_7
            player.c "Does that feel better?"
            wt_image indy_sex_1_state_1_5
            terri.c "Yes, that's much better.  Thank you!"
            wt_image indy_sex_1_state_1_7
            "Although she says it's better, and it must be without the discomfort of being dry, there's no evidence that she's enjoying this."
            wt_image indy_sex_1_state_1_1
            "Some women have difficulties with their natural lubrication, but with the lube you added, you think she should now be responding more than she is. She still isn't moving or participating in the fuck, yet she watches with a seeming hope that this is good for you. For a woman who wants to be good at sex, it doesn't seem to come naturally to her, either physically or instinctually."
            wt_image indy_sex_1_state_1_3
            terri.c "Am I doing something wrong?  You seem to be thinking a lot."
            player.c "No, [terri.name].  It's nothing that we can't work on."
            wt_image indy_sex_1_state_1_1
            "You don't want to undermine her confidence, and she is both beautiful and tight.  You set your thoughts aside and focus on your own pleasure."
            wt_image indy_sex_1_state_1_8
            player.c "[player.orgasm_text]"
            wt_image indy_strip_state_2_9
            terri.c "Was that all right?  You seemed to enjoy yourself at the end.  Did you learn anything I should be doing differently?"
            player.c "It was great, [terri.name].  You're great.  We'll pick this up again on a future visit."
            wt_image indy_portrait_state_2
            terri.c "Okay.  I'm happy to work on anything you think I should be doing differently.  I really want to know how to be the best girlfriend I can be."
        elif terri.state == 3:
            wt_image indy_hypno_state_3_1
            player.c "Last time you showed me how you give your boyfriend a blow job, and I promised to help you get better at that.  We will do that, but before we do, I want to see how you do at fucking."
            wt_image indy_portrait_state_3
            terri.c "All right."
            wt_image indy_strip_state_3_10
            "[terri.name] immediately undresses ..."
            wt_image indy_sex_1_state_1_6
            "... then leans back and spreads her legs."
            wt_image indy_sex_1_state_1_5
            "You enter her gingerly.  Despite her willingness to do this, she's quite dry."
            wt_image indy_sex_1_state_1_1
            player.c "Are you always this dry, or is it just because you're nervous doing this for the first time with me?"
            wt_image indy_sex_1_state_1_3
            terri.c "What do you mean?"
            player.c "Your pussy.  You're not wet."
            wt_image indy_sex_1_state_1_7
            terri.c "Should I be?"
            player.c "Try playing with your clit.  It'll feel better if your body is excited."
            wt_image indy_sex_1_state_1_8
            "[terri.name] starts stroking her clit, but it doesn't make any difference. She lies there, not moving.  Which is understandable, considering how dry she is.  Any movement would surely be uncomfortable."
            player.c "[terri.name], do you want to be doing this?"
            wt_image indy_sex_1_state_1_4
            terri.c "Of course!  You said you wanted to see how I have sex."
            player.c "Is this what it's like with your boyfriend?"
            wt_image indy_sex_1_state_1_2
            terri.c "Yes.  Why?  Am I doing something wrong?"
            player.c "Is it uncomfortable when he fucks you?"
            wt_image indy_sex_1_state_1_4
            terri.c "A little.  He's not as big as you, so not as much as it is right now."
            wt_image indy_sex_1_state_1_6
            "You stop and get some lubricant.   That may make things easier."
            wt_image indy_sex_1_state_1_7
            player.c "Does that feel better?"
            wt_image indy_sex_1_state_1_5
            terri.c "Yes, that's much better.  Thank you!"
            wt_image indy_sex_1_state_1_7
            "Although she says it's better, and it must be without the discomfort of being dry, there's no evidence that she's enjoying this."
            wt_image indy_sex_1_state_1_1
            "Some women have difficulties with their natural lubrication, but with the lube you added, you think she should now be responding more than she is.  She still isn't moving or participating in the fuck, yet she watches you, seemingly hoping that this feels good to you.  For a woman who wants to be good at sex, it doesn't seem to come naturally to her, either physically or instinctually."
            wt_image indy_sex_1_state_1_3
            terri.c "Am I doing something wrong?  You seem to be thinking a lot."
            player.c "No, [terri.name].  It's nothing that we can't work on."
            wt_image indy_sex_1_state_1_1
            "You don't want to undermine her confidence, and she is both beautiful and tight.  You set your thoughts aside and focus on your own pleasure."
            wt_image indy_sex_1_state_1_8
            player.c "[player.orgasm_text]"
            wt_image indy_strip_state_3_4
            terri.c "Was that all right?  You seemed to enjoy yourself at the end.  Did you learn anything I should be doing differently?"
            player.c "It was great, [terri.name].  You're great.  We'll pick this up again on a future visit."
            wt_image indy_talk_state_3_2
            terri.c "Okay.  I'm happy to work on anything you think I should be doing differently.  I really want to know how to be the best girlfriend I can be."
        elif terri.state == 4:
            wt_image indy_hypno_state_4_1
            player.c "Last time you showed me how you give your boyfriend a blow job, and I promised to help you get better at that.  We will do that, but before we do, I want to see how you do at fucking."
            wt_image indy_strip_state_4_7
            terri.c "All right."
            wt_image indy_hypno_state_4_3
            "[terri.name] immediately undresses."
            wt_image indy_sex_1_state_4_7
            "She lies down on her back and you enter her gingerly.  Despite her willingness to do this, she's quite dry."
            wt_image indy_sex_1_state_4_1
            player.c "Are you always this dry, or is it just because you're nervous doing this for the first time with me?"
            wt_image indy_sex_1_state_4_3
            terri.c "What do you mean?"
            player.c "Your pussy.  You're not wet."
            wt_image indy_sex_1_state_4_8
            terri.c "Should I be?"
            wt_image indy_sex_1_state_4_9
            player.c "Try playing with your clit.  It'll feel better if your body is excited."
            wt_image indy_sex_1_state_4_2
            "[terri.name] starts stroking her clit, but it doesn't make any difference. She lies there, not moving.  Which is understandable, considering how dry she is.  Any movement would surely be uncomfortable."
            player.c "[terri.name], do you want to be doing this?"
            wt_image indy_sex_1_state_4_10
            terri.c "Of course!  You said you wanted to see how I have sex."
            player.c "Is this what it's like with your boyfriend?"
            wt_image indy_sex_1_state_4_9
            terri.c "Yes.  Why?  Am I doing something wrong?"
            player.c "Is it uncomfortable when he fucks you?"
            wt_image indy_sex_1_state_4_8
            terri.c "A little.  He's not as big as you, so not as much as it is right now."
            wt_image indy_sex_1_state_4_5
            "You stop and get some lubricant for her to apply to herself and you.   That may make things easier."
            wt_image indy_sex_1_state_4_4
            player.c "Does that feel better?"
            terri.c "Yes, that's much better.  Thank you!"
            wt_image indy_sex_1_state_4_11
            "Although she says it's better, and it must be without the discomfort of being dry, there's no evidence that she's enjoying this."
            wt_image indy_sex_1_state_4_6
            "Some women have difficulties with their natural lubrication, but with the lube you added, you think she should now be responding more than she is. She still isn't moving or participating in the fuck, yet she watches you with a look that says she clearly hopes that this is good for you. For a woman who wants to be good at sex, it doesn't seem to come naturally to her, either physically or instinctually."
            wt_image indy_sex_1_state_4_12
            terri.c "Am I doing something wrong?  You seem to be thinking a lot."
            player.c "No, [terri.name].  It's nothing that we can't work on."
            wt_image indy_sex_1_state_4_6
            "You don't want to undermine her confidence, and she is both beautiful and tight.  You set your thoughts aside and focus on your own pleasure."
            wt_image indy_sex_1_state_4_13
            player.c "[player.orgasm_text]"
            wt_image indy_strip_state_4_8
            terri.c "Was that all right?  You seemed to enjoy yourself at the end.  Did you learn anything I should be doing differently?"
            player.c "It was great, [terri.name].  You're great.  We'll pick this up again on a future visit."
            wt_image indy_hypno_state_4_4
            terri.c "Okay.  I'm happy to work on anything you think I should be doing differently.  I really want to know how to be the best girlfriend I can be."
        elif terri.state == 5:
            wt_image indy_hypno_state_5_1
            player.c "Last time you showed me how you give your boyfriend a blow job, and I promised to help you get better at that.  We will do that, but before we do, I want to see how you do at fucking."
            wt_image indy_hypno_state_5_3
            terri.c "All right."
            wt_image indy_strip_state_5_4
            "[terri.name] immediately undresses ..."
            wt_image indy_sex_1_state_5_1
            "... then leans back and spreads her legs."
            wt_image indy_sex_1_state_5_2
            "You enter her gingerly.  Despite her willingness to do this, she's quite dry."
            wt_image indy_sex_1_state_4_1
            player.c "Are you always this dry, or is it just because you're nervous doing this for the first time with me?"
            wt_image indy_sex_1_state_4_3
            terri.c "What do you mean?"
            player.c "Your pussy.  You're not wet."
            wt_image indy_sex_1_state_4_8
            terri.c "Should I be?"
            wt_image indy_sex_1_state_4_9
            player.c "Try playing with your clit.  It'll feel better if your body is excited."
            wt_image indy_sex_1_state_4_2
            "[terri.name] starts stroking her clit, but it doesn't make any difference. She lies there, not moving.  Which is understandable, considering how dry she is.  Any movement would surely be uncomfortable."
            player.c "[terri.name], do you want to be doing this?"
            wt_image indy_sex_1_state_4_10
            terri.c "Of course!  You said you wanted to see how I have sex."
            player.c "Is this what it's like with your boyfriend?"
            wt_image indy_sex_1_state_4_9
            terri.c "Yes.  Why?  Am I doing something wrong?"
            player.c "Is it uncomfortable when he fucks you?"
            wt_image indy_sex_1_state_4_8
            terri.c "A little.  He's not as big as you, so not as much as it is right now."
            wt_image indy_sex_1_state_5_3
            "You stop and get some lubricant for her to apply to herself and you.   That may make things easier."
            wt_image indy_sex_1_state_5_4
            player.c "Does that feel better?"
            terri.c "Yes, that's much better.  Thank you!"
            wt_image indy_sex_1_state_5_5
            "Although she says it's better, and it must be without the discomfort of being dry, there's no evidence that she's enjoying this."
            wt_image indy_sex_1_state_5_6
            "Some women have difficulties with their natural lubrication, but with the lube you added, you think she should now be responding more positively than she is. She still isn't moving or participating in the fuck, yet she watches you with a look that says she clearly hopes that this is good for you. For a woman who wants to be good at sex, it doesn't seem to come naturally to her, either physically or instinctually."
            wt_image indy_sex_1_state_5_5
            terri.c "Am I doing something wrong?  You seem to be thinking a lot."
            player.c "No, [terri.name].  It's nothing that we can't work on."
            wt_image indy_sex_1_state_5_6
            "You don't want to undermine her confidence, and she is both beautiful and tight.  You set your thoughts aside and focus on your own pleasure."
            wt_image indy_sex_1_state_5_7
            player.c "[player.orgasm_text]"
            wt_image indy_strip_state_5_4
            terri.c "Was that all right?  You seemed to enjoy yourself at the end.  Did you learn anything I should be doing differently?"
            player.c "It was great, [terri.name].  You're great.  We'll pick this up again on a future visit."
            wt_image indy_talk_state_5_4
            terri.c "Okay.  I'm happy to work on anything you think I should be doing differently.  I really want to know how to be the best girlfriend I can be."
        if terri.pleasure_her_action_used == 0:
            $ terri.pleasure_her_action_used = 1 # this opens up the pleasure her action
        add tags 'make_out_action_not_available' to terri # shuts the make out option off after you've already had sex with her
        $ terri.lesbian_clues += 1
        $ terri.sex_count += 1
        $ terri.sex_training_count += 1
        orgasm
        $ terri.temporary_count = 3 # note: very low because you're not really training, just observing
    # additional training
    else:
        if terri.state == 1:
            wt_image indy_talk_state_1_2
        elif terri.state == 2:
            wt_image indy_talk_state_2_1
        elif terri.state == 3:
            wt_image indy_talk_state_3_8
        elif terri.state == 4:
            wt_image indy_talk_state_4_10
        elif terri.state == 5:
            wt_image indy_bj_1_state_5_1
        player.c "Have you been practicing your skills, [terri.name]?"
        if terri.state == 1:
            wt_image indy_talk_state_1_1
        elif terri.state == 2:
            wt_image indy_talk_state_2_5
        elif terri.state == 3:
            wt_image indy_talk_state_3_6
        elif terri.state == 4:
            wt_image indy_talk_state_4_11
        elif terri.state == 5:
            wt_image indy_hypno_state_5_1
        terri.c "I tried, with my boyfriend, yes.  I'm not sure I'm getting better though."
        player.c "Let's see if I can help."
        $ title = "What do you want to work on?"
        menu menu_terri_sex_skills:
            "Her oral skills":
                if terri.blowjob_training_count > 2:
                    "[terri.name] has learned as much as you can teach her about giving blow jobs.  Try something else."
                    jump menu_terri_sex_skills
                else:
                    if terri.blowjob_training_count == 1:
                        $ title = "What do you want to do?"
                        menu menu_terri_oral_skills_2:
                            "Have her practice on your finger":
                                player.c "Remove your clothes and come sit on the edge of the bed with your mouth open."
                                wt_image indy_mouth_1_1
                                player.c "It looks like a healthy female mouth.  Good teeth, pink tongue, soft lips.  There's no reason why you can't learn to please a man with it."
                                wt_image indy_mouth_1_2
                                player.c "However, you're not getting my cock in there again until you learn some technique."
                                wt_image indy_mouth_1_3
                                player.c "Let's see how you can do with my finger, and when I think you know what you're doing, you can graduate back to my cock."
                                wt_image indy_mouth_1_4
                                "[terri.name] starts sucking on your finger, much the same way she sucked on your cock the first time."
                                wt_image indy_mouth_1_5
                                player.c "Stop.  The goal is not to pull the semen out using suction alone.  Use your tongue first, swirl and flick it along the cock."
                                wt_image indy_mouth_1_6
                                player.c "Better.  Now wrap your lips gently around the cock as you bob your head back and forth.  Try to stimulate the penis, not overwhelm it."
                                wt_image indy_mouth_1_7
                                player.c "As you're sliding your lips along his shaft, pay particular attention to the tip.  It's the most sensitive area."
                                wt_image indy_mouth_1_8
                                player.c "When he starts to get excited, you can pick up the pace.  But remember, you're still trying to coax the sperm out of his balls, not to suck it out forcefully."
                                wt_image indy_mouth_1_9
                                "It takes time, but eventually [terri.name] starts to get it.  She watches you carefully as you instruct, teaching her when to go faster, when slower, when to apply pressure, and when to tease."
                                wt_image indy_mouth_1_10
                                "When her jaw is aching, you remove your finger and bring the lesson to a close.  She seems genuinely grateful for the lesson."
                                wt_image indy_mouth_1_11
                                terri.c "Thank you for teaching me.  I hope I learned enough that you'll let me practice on your cock next time?"
                                change terri submission by 10
                            "Use a Teaching Aide" if player.teaching_aide_count > 0:
                                $ current_target = None
                                call choose_person_with_tags(tagged_with_any = ['teaching_aide']) from _call_choose_person_with_tags_10
                                if current_target is not None and renpy.has_label(current_target.short_name + '_terri_ta_blowjob'):
                                    summon current_target
                                    call expression current_target.short_name + '_terri_ta_blowjob' from _call_expression_27
                                    if terri.has_tag('watched_teaching_aide_blowjob'):
                                        player.c "Your turn, [terri.name].  Come over here and let's see if you learned anything. Don't worry, I'll give you pointers as needed."
                                        call terri_second_bj_ending from _call_terri_second_bj_ending
                                        "[current_target.name] jumps in before you have a chance to respond."
                                        wt_image indy_bj_2_state_1_6
                                        current_target.c "I thought you did great, [terri.name]!  You'll be a champion cocksucker in no time."
                                        player.c "Yes, you did fine, [terri.name].  You're starting to get the hang of it.  We'll work on improving your skills more soon."
                                        terri.c "Oh good.  Thank you!  And thank you so much for demonstrating for me, [current_target.name]. You're a great teacher!  I really feel more confident, having been able to watch and learn from you."
                                        call character_location_return(current_target) from _call_character_location_return_710
                                        $ current_target = terri
                                        change terri sos by 10
                                        $ terri.temporary_count = 3 # reducing energy for work with TA
                                elif current_target is not None:
                                    sys "Missing label: [current_target.short_name]_terri_ta_blowjob. Choose someone else as content here is not properly defined."
                                    $ current_target = terri
                                    $ title = "What do you want to do?"
                                    jump menu_terri_oral_skills_2
                                if current_target is None:
                                    $ current_target = terri
                                    $ title = "What do you want to do?"
                                    jump menu_terri_oral_skills_2
                            "Just have her blow you":
                                player.c "Let's work on your oral skills, [terri.name]. Come over here, and I'll guide you through how to give a proper blow job."
                                call terri_second_bj_ending from _call_terri_second_bj_ending_1
                                wt_image indy_bj_2_state_1_6
                                player.c "You did fine, [terri.name].  You're starting to get the hang of it.  We'll work on improving your skills more soon."
                                terri.c "Oh good.  Thank you!"
                                change terri sos by 5
                                $ terri.temporary_count = 2
                            "Choose something else":
                                jump menu_terri_sex_skills
                    elif terri.blowjob_training_count == 2:
                        player.c "Let's see if you remember what you were taught last time, [terri.name]."
                        wt_image indy_bj_2_state_1_2
                        "The gentle licks she starts with suggest she does.  She runs her tongue up and down your cock ..."
                        wt_image indy_bj_3_state_1_1
                        "... paying extra attention to your cockhead."
                        wt_image indy_bj_2_state_1_3
                        "Soon she's swirling her tongue along the underside of your shaft as she bobs her pretty head up and down."
                        wt_image indy_bj_3_state_1_7
                        player.c "Good, you do remember your last lesson. Let's add something new to your repertoire. Giving a blow job isn't all about the penis. The balls should get attention, too. Use your tongue to warm up my balls, [terri.name]."
                        wt_image indy_bj_3_state_1_4
                        "Without hesitation, she starts licking your balls."
                        wt_image indy_bj_3_state_1_8
                        player.c "Once you have them warmed up, take them into your mouth."
                        wt_image indy_bj_3_state_1_3
                        player.c "Suck on them gently, [terri.name]."
                        wt_image indy_bj_3_state_1_9
                        player.c "Good.  Now take my balls in your hand and cup them gently while you go back to pleasuring my cock."
                        wt_image indy_bj_3_state_1_5
                        "Her warm hand feels nice on your sack as she resumes licking and sucking on your shaft."
                        wt_image indy_bj_3_state_1_2
                        player.c "Don't forget to keep your eyes on me as you blow me, [terri.name]."
                        wt_image indy_bj_3_state_1_6
                        "She's getting a little better at this. She's still far from the most skilled woman to suck your cock, but she's better than she was when she first hired you. You happily shoot your seed into her now modestly talented mouth."
                        wt_image indy_bj_3_state_1_5
                        player.c "[player.orgasm_text]"
                        wt_image indy_bj_3_state_1_1
                        player.c "That's much better, [terri.name]. Keep sucking cock like that, and any man will be happy to have you take him in your mouth."
                        wt_image indy_bj_2_state_1_6
                        terri.c "Thank you! Coming from you, that means a lot!"
                        $ terri.swallow_count += 1
                        change terri sos by 10
                        change terri resistance by -5
                        orgasm
                    $ terri.blowjob_training_count += 1
            "Her fucking":
                if terri.sex_training_count > 2:
                    "[terri.name] has learned as much as you can teach her about fucking.  Try something else."
                    jump menu_terri_sex_skills
                else:
                    if terri.sex_training_count == 1:
                        if terri.state == 1:
                            wt_image indy_hypno_state_1_1
                            player.c "Let's see if we can improve your skills at fucking."
                            wt_image indy_hypno_state_1_5
                            terri.c "Isn't that really the man's job?  I mean, the fucking part?"
                            wt_image indy_strip_state_1_2
                            player.c "Not at all.  Let's get you naked."
                            wt_image indy_sex_2_state_1_1
                            "Once she's naked, you have [terri.name] kneel down, facing away from you ..."
                            wt_image indy_sex_2_state_1_2
                            "... as you apply lube to your cock and position yourself behind her."
                            wt_image indy_sex_2_state_1_3
                            "Even with lube, she's not comfortable taking you inside her.  She'll never be able to fuck a man properly if her body isn't into it."
                            wt_image indy_sex_2_state_1_4
                            player.c "Play with yourself, [terri.name].  Put your hand between your legs and touch your sex and clit.  Close your eyes and relax and let your body enjoy the sensation."
                            wt_image indy_sex_2_state_1_5
                            "After a few minutes of playing with herself, she starts to relax and get wet.  Not a lot, but enough to be able to move more easily along your cock."
                            wt_image indy_sex_2_state_1_6
                            player.c "Okay, [terri.name].  Time for you to fuck me.  Start moving back against me."
                            wt_image indy_sex_2_state_1_7
                            "She's not a natural.  You guide her with your hands on her hips, helping her figure out how to fuck your cock."
                            wt_image indy_sex_2_state_1_8
                            "You let her keep at it, learning as much as she can about pleasing a man this way until she's getting tired and your balls are aching to burst.  Then you give her a reward for her efforts, in the form of your cum shooting inside her."
                            wt_image indy_sex_2_state_1_9
                            player.c "[player.orgasm_text]"
                            wt_image indy_strip_state_1_7
                            terri.c "Was that okay?  Did I do better than the first time?"
                            player.c "Yes, you did great, [terri.name].  Another lesson or two, and you'll be a top-grade fucker."
                            wt_image indy_portrait_state_1
                            terri.c "Oh, good.  Thank you!"
                        elif terri.state == 2:
                            wt_image indy_hypno_state_2_5
                            player.c "Let's see if we can improve your skills at fucking."
                            wt_image indy_hypno_state_2_2
                            terri.c "Isn't that really the man's job?  I mean, the fucking part?"
                            wt_image indy_strip_state_2_7
                            player.c "Not at all.  Let's get you naked."
                            wt_image indy_sex_2_state_1_1
                            "Once she's naked, you have [terri.name] kneel down, facing away from you ..."
                            wt_image indy_sex_2_state_1_2
                            "... as you apply lube to your cock and position yourself behind her."
                            wt_image indy_sex_2_state_1_3
                            "Even with lube, she's not comfortable taking you inside her.  She'll never be able to fuck a man properly if her body isn't into it."
                            wt_image indy_sex_2_state_1_4
                            player.c "Play with yourself, [terri.name].  Put your hand between your legs and touch your sex and clit.  Close your eyes and relax and let your body enjoy the sensation."
                            wt_image indy_sex_2_state_1_5
                            "After a few minutes of playing with herself, she starts to relax and get wet.  Not a lot, but enough to be able to move more easily along your cock."
                            wt_image indy_sex_2_state_1_6
                            player.c "Okay, [terri.name].  Time for you to fuck me.  Start moving back against me."
                            wt_image indy_sex_2_state_1_7
                            "She's not a natural.  You guide her with your hands on her hips, helping her figure out how to fuck your cock."
                            wt_image indy_sex_2_state_1_8
                            "You let her keep at it, learning as much as she can about pleasing a man this way until she's getting tired and your balls are aching to burst.  Then you give her a reward for her efforts, in the form of your cum shooting inside her."
                            wt_image indy_sex_2_state_1_9
                            player.c "[player.orgasm_text]"
                            wt_image indy_strip_state_2_3
                            terri.c "Was that okay?  Did I do better than the first time?"
                            wt_image indy_strip_state_2_2
                            player.c "Yes, you did great, [terri.name].  Another lesson or two, and you'll be a top-grade fucker."
                            wt_image indy_portrait_state_2
                            terri.c "Oh, good.  Thank you!"
                        elif terri.state == 3:
                            wt_image indy_hypno_state_3_1
                            player.c "Let's see if we can improve your skills at fucking."
                            terri.c "Isn't that really the man's job?  I mean, the fucking part?"
                            wt_image indy_strip_state_3_8
                            player.c "Not at all.  Let's get you naked."
                            wt_image indy_sex_2_state_3_1
                            "Once she's naked, you have [terri.name] bend over, facing away from you ..."
                            wt_image indy_sex_2_state_3_2
                            "... as you apply lube to your cock and position yourself behind her."
                            wt_image indy_sex_2_state_3_3
                            "Even with lube, she's not comfortable taking you inside her.  She'll never be able to fuck a man properly if her body isn't into it."
                            wt_image indy_sex_2_state_3_4
                            player.c "Play with yourself, [terri.name].  Put your hand between your legs and touch your sex and clit.  Close your eyes and relax and let your body enjoy the sensation."
                            wt_image indy_sex_2_state_3_5
                            "After a few minutes of playing with herself, she starts to relax and get wet.  Not a lot, but enough to be able to move more easily along your cock."
                            wt_image indy_sex_2_state_3_6
                            player.c "Okay, [terri.name].  Time for you to fuck me.  Start moving back against me."
                            wt_image indy_sex_2_state_3_7
                            "She's not a natural.  You guide her with your hands on her hips, helping her figure out how to fuck your cock."
                            wt_image indy_sex_2_state_3_8
                            "You let her keep at it, learning as much as she can about pleasing a man this way ..."
                            wt_image indy_sex_2_state_3_2
                            "... until she's getting tired and your balls are aching to burst.  Then you give her a reward for her efforts, in the form of your cum shooting inside her."
                            wt_image indy_sex_2_state_3_9
                            player.c "[player.orgasm_text]"
                            wt_image indy_strip_state_3_9
                            terri.c "Was that okay?  Did I do better than the first time?"
                            wt_image indy_talk_state_3_1
                            player.c "Yes, you did great, [terri.name].  Another lesson or two, and you'll be a top-grade fucker."
                            wt_image indy_talk_state_3_2
                            terri.c "Oh, good.  Thank you!"
                        elif terri.state == 4:
                            wt_image indy_portrait_state_4
                            player.c "Let's see if we can improve your skills at fucking."
                            wt_image indy_hypno_state_4_1
                            terri.c "Isn't that really the man's job?  I mean, the fucking part?"
                            wt_image indy_strip_state_4_11
                            player.c "Not at all.  Let's get you naked."
                            wt_image indy_sex_2_state_4_1
                            "Once she's naked, you have [terri.name] bend over, facing away from you ..."
                            wt_image indy_sex_2_state_4_2
                            "... as you apply lube to your cock and position yourself behind her."
                            wt_image indy_sex_2_state_4_3
                            "Even with lube, she's not comfortable taking you inside her.  She'll never be able to fuck a man properly if her body isn't into it."
                            wt_image indy_sex_1_state_4_9
                            player.c "Play with yourself, [terri.name].  Put your hand between your legs and touch your sex and clit.  Close your eyes and relax and let your body enjoy the sensation."
                            wt_image indy_sex_1_state_4_2
                            "After a few minutes of playing with herself, she starts to relax and get wet.  Not a lot, but enough to be able to move more easily along your cock."
                            wt_image indy_sex_1_state_4_10
                            player.c "Okay, [terri.name].  Time for you to fuck me.  Roll back onto your knees and start moving back against me."
                            wt_image indy_sex_2_state_4_4
                            "She's not a natural."
                            wt_image indy_sex_2_state_4_5
                            "You guide her with your hands on her hips, helping her figure out how to fuck your cock."
                            wt_image indy_sex_2_state_4_4
                            "You let her keep at it, learning as much as she can about pleasing a man this way until she's getting tired and your balls are aching to burst.  Then you give her a reward for her efforts, in the form of your cum shooting inside her."
                            wt_image indy_sex_2_state_4_6
                            player.c "[player.orgasm_text]"
                            wt_image indy_strip_state_4_8
                            terri.c "Was that okay?  Did I do better than the first time?"
                            wt_image indy_talk_state_4_3
                            player.c "Yes, you did great, [terri.name].  Another lesson or two, and you'll be a top-grade fucker."
                            wt_image indy_hypno_state_4_4
                            terri.c "Oh, good.  Thank you!"
                        elif terri.state == 5:
                            wt_image indy_portrait_state_5
                            player.c "Let's see if we can improve your skills at fucking."
                            wt_image indy_hypno_state_5_1
                            terri.c "Isn't that really the man's job?  I mean, the fucking part?"
                            wt_image indy_strip_state_5_1
                            player.c "Not at all.  Let's get you naked."
                            wt_image indy_sex_2_state_3_1
                            "Once she's naked, you have [terri.name] bend over, facing away from you ..."
                            wt_image indy_sex_2_state_3_2
                            "... as you apply lube to your cock and position yourself behind her."
                            wt_image indy_sex_2_state_3_3
                            "Even with lube, she's not comfortable taking you inside her.  She'll never be able to fuck a man properly if her body isn't into it."
                            wt_image indy_sex_2_state_3_4
                            player.c "Play with yourself, [terri.name].  Put your hand between your legs and touch your sex and clit.  Close your eyes and relax and let your body enjoy the sensation."
                            wt_image indy_sex_2_state_3_5
                            "After a few minutes of playing with herself, she starts to relax and get wet.  Not a lot, but enough to be able to move more easily along your cock."
                            wt_image indy_sex_2_state_3_6
                            player.c "Okay, [terri.name].  Time for you to fuck me.  Start moving back against me."
                            wt_image indy_sex_2_state_3_7
                            "She's not a natural.  You guide her with your hands on her hips, helping her figure out how to fuck your cock."
                            wt_image indy_sex_2_state_3_8
                            "You let her keep at it, learning as much as she can about pleasing a man this way ..."
                            wt_image indy_sex_2_state_3_2
                            "... until she's getting tired and your balls are aching to burst.  Then you give her a reward for her efforts, in the form of your cum shooting inside her."
                            wt_image indy_sex_2_state_3_9
                            player.c "[player.orgasm_text]"
                            wt_image indy_strip_state_5_4
                            terri.c "Was that okay?  Did I do better than the first time?"
                            wt_image indy_talk_state_5_1
                            player.c "Yes, you did great, [terri.name].  Another lesson or two, and you'll be a top-grade fucker."
                            wt_image indy_talk_state_5_4
                            terri.c "Oh, good.  Thank you!"
                    elif terri.sex_training_count == 2:
                        if terri.state == 1:
                            wt_image indy_hypno_state_1_1
                            player.c "Time to teach you more about fucking, [terri.name]."
                            wt_image indy_hypno_state_1_3
                            "As she undresses, you do the same, then take a seat."
                            wt_image indy_strip_state_1_8
                            player.c "Once you're naked, climb up here on top of me."
                            wt_image indy_strip_state_1_9
                            terri.c "You want me on top?"
                            wt_image indy_strip_state_1_10
                            player.c "I do.  I'm going to teach you how to bring a man to orgasm by riding his cock."
                            wt_image indy_sex_3_state_1_1
                            "As usual, despite her willingness to have sex with you and a generous application of lube ..."
                            wt_image indy_sex_3_state_1_2
                            "... she struggles with the discomfort of fitting you inside."
                            wt_image indy_sex_3_state_1_3
                            player.c "Remember to play with your clit, [terri.name].  In this position, you control when and how far I go inside you.  Let your mind drift to sexy thoughts as you relax and play with yourself."
                            wt_image indy_sex_3_state_1_4
                            "It takes a while, but eventually she makes herself wet enough that she can start to move on you without discomfort."
                            wt_image indy_sex_3_state_1_3
                            player.c "Fuck me now, [terri.name].  Ride my hard cock up and down.  Start off nice and slow and easy, then pick up the pace."
                            wt_image indy_sex_3_state_1_5
                            "You help guide her with your hands on her ass, showing her how to slam down on the down thrusts, how far to come up on the up thrusts, and when to move faster."
                            wt_image indy_sex_3_state_1_6
                            player.c "Use your cunt muscles, too, [terri.name].  Grip me at the top, then relax as you slam down.  Squeeze again at the bottom before rising up again."
                            wt_image indy_sex_3_state_1_1
                            "This is new to her, but she's getting the hang of it."
                            wt_image indy_sex_3_state_1_7
                            "She rides you faster and faster, squeezing and milking you as best she can.  When you think her legs muscles are ready to give out from fatigue, you take pity on her and let yourself climax.  She doesn't orgasm herself, but she gives a little moan of satisfaction as she feels you release your seed inside her."
                            wt_image indy_sex_3_state_1_2
                            player.c "[player.orgasm_text]"
                            terri.c "Oh!"
                            wt_image indy_strip_state_1_7
                            player.c "Keep working on squeezing with your Kegel muscles and pay attention to the man's reactions to know when to go slower and when to go faster.  Keep practicing, and you'll soon be a dream lay for any man."
                            wt_image indy_portrait_state_1
                            terri.c "Thank you!  Coming from you, that means a lot!"
                        elif terri.state == 2:
                            wt_image indy_hypno_state_2_2
                            player.c "Time to teach you more about fucking, [terri.name]."
                            wt_image indy_strip_state_2_1
                            "As she undresses, you do the same, then take a seat."
                            wt_image indy_strip_state_2_3
                            player.c "Once you're naked, climb up here on top of me."
                            wt_image indy_strip_state_2_9
                            terri.c "You want me on top?"
                            wt_image indy_strip_state_2_4
                            player.c "I do.  I'm going to teach you how to bring a man to orgasm by riding his cock."
                            wt_image indy_sex_3_state_1_1
                            "As usual, despite her willingness to have sex with you and a generous application of lube ..."
                            wt_image indy_sex_3_state_1_2
                            "... she struggles with the discomfort of fitting you inside."
                            wt_image indy_sex_3_state_1_3
                            player.c "Remember to play with your clit, [terri.name].  In this position, you control when and how far I go inside you.  Let your mind drift to sexy thoughts as you relax and play with yourself."
                            wt_image indy_sex_3_state_1_4
                            "It takes a while, but eventually she makes herself wet enough that she can start to move on you without discomfort."
                            wt_image indy_sex_3_state_1_3
                            player.c "Fuck me now, [terri.name].  Ride my hard cock up and down.  Start off nice and slow and easy, then pick up the pace."
                            wt_image indy_sex_3_state_1_5
                            "You help guide her with your hands on her ass, showing her how to slam down on the down thrusts, how far to come up on the up thrusts, and when to move faster."
                            wt_image indy_sex_3_state_1_6
                            player.c "Use your cunt muscles, too, [terri.name].  Grip me at the top, then relax as you slam down.  Squeeze again at the bottom before rising up again."
                            wt_image indy_sex_3_state_1_1
                            "This is new to her, but she's getting the hang of it."
                            wt_image indy_sex_3_state_1_7
                            "She rides you faster and faster, squeezing and milking you as best she can.  When you think her legs muscles are ready to give out from fatigue, you take pity on her and let yourself climax.  She doesn't orgasm herself, but she gives a little moan of satisfaction as she feels you release your seed inside her."
                            wt_image indy_sex_3_state_1_2
                            player.c "[player.orgasm_text]"
                            terri.c "Oh!"
                            wt_image indy_strip_state_2_4
                            player.c "Keep working on squeezing with your Kegel muscles and pay attention to the man's reactions to know when to go slower and when to go faster.  Keep practicing, and you'll soon be a dream lay for any man."
                            wt_image indy_portrait_state_2
                            terri.c "Thank you!  Coming from you, that means a lot!"
                        elif terri.state == 3:
                            wt_image indy_hypno_state_3_1
                            player.c "Time to teach you more about fucking, [terri.name]."
                            wt_image indy_hypno_state_3_4
                            "As she undresses, you do the same, then take a seat."
                            player.c "Once you're naked, climb up here on top of me."
                            wt_image indy_strip_state_3_8
                            terri.c "You want me on top?"
                            player.c "I do.  I'm going to teach you how to bring a man to orgasm by riding his cock."
                            wt_image indy_sex_3_state_3_1
                            "As usual, despite her willingness to have sex with you and a generous application of lube ..."
                            wt_image indy_sex_3_state_3_2
                            "... she struggles with the discomfort of fitting you inside."
                            player.c "Remember to play with your clit, [terri.name].  In this position, you control when and how far I go inside you.  Let your mind drift to sexy thoughts as you relax and play with yourself."
                            wt_image indy_sex_3_state_3_3
                            "It takes a while, but eventually she makes herself wet enough that she can start to move on you without discomfort."
                            wt_image indy_sex_3_state_3_4
                            player.c "Fuck me now, [terri.name].  Ride my hard cock up and down.  Start off nice and slow and easy, then pick up the pace."
                            wt_image indy_sex_3_state_3_5
                            "You help guide her with your hands on her ass, showing her how to slam down on the down thrusts, how far to come up on the up thrusts, and when to move faster."
                            wt_image indy_sex_3_state_3_6
                            player.c "Use your cunt muscles, too, [terri.name].  Grip me at the top, then relax as you slam down.  Squeeze again at the bottom before rising up again."
                            wt_image indy_sex_3_state_3_7
                            "This is new to her, but she's getting the hang of it.  She rides you faster and faster, squeezing and milking you as best she can.  When you think her legs muscles are ready to give out from fatigue, you take pity on her and let yourself climax.  She doesn't orgasm herself, but she gives a little moan of satisfaction as she feels you release your seed inside her."
                            wt_image indy_sex_3_state_3_5
                            player.c "[player.orgasm_text]"
                            terri.c "Oh!"
                            wt_image indy_strip_state_3_8
                            player.c "Keep working on squeezing with your Kegel muscles and pay attention to the man's reactions to know when to go slower and when to go faster.  Keep practicing, and you'll soon be a dream lay for any man."
                            wt_image indy_talk_state_3_1
                            terri.c "Thank you!  Coming from you, that means a lot!"
                        elif terri.state == 4:
                            wt_image indy_portrait_state_4
                            player.c "Time to teach you more about fucking, [terri.name]."
                            wt_image indy_strip_state_4_7
                            "As she undresses, you do the same, then take a seat."
                            wt_image indy_strip_state_4_11
                            player.c "Once you're naked, climb up here on top of me."
                            wt_image indy_strip_state_4_8
                            terri.c "You want me on top?"
                            wt_image indy_strip_state_4_4
                            player.c "I do.  I'm going to teach you how to bring a man to orgasm by riding his cock."
                            wt_image indy_strip_state_4_10
                            "As usual, despite her willingness to have sex with you and a generous application of lube ..."
                            wt_image indy_sex_3_state_4_1
                            "... she struggles with the discomfort of fitting you inside."
                            wt_image indy_sex_3_state_4_2
                            player.c "Remember to play with yourself, [terri.name].  In this position, you control when and how far I go inside you.  Let your mind drift to sexy thoughts as you relax and play with yourself."
                            wt_image indy_sex_3_state_4_3
                            "It takes a while, but eventually she makes herself wet enough that she can start to move on you without discomfort."
                            wt_image indy_sex_3_state_4_4
                            player.c "Fuck me now, [terri.name].  Ride my hard cock up and down.  Start off nice and slow and easy, then pick up the pace."
                            wt_image indy_sex_3_state_4_5
                            "You help guide her with your hands on her ass, showing her how to slam down on the down thrusts, how far to come up on the up thrusts, and when to move faster."
                            wt_image indy_sex_3_state_4_6
                            player.c "Use your cunt muscles, too, [terri.name].  Grip me at the top, then relax as you slam down.  Squeeze again at the bottom before rising up again."
                            wt_image indy_sex_3_state_4_7
                            "This is new to her, but she's getting the hang of it."
                            wt_image indy_sex_3_state_4_8
                            "She rides you faster and faster, squeezing and milking you as best she can.  When you think her legs muscles are ready to give out from fatigue, you take pity on her and let yourself climax.  She doesn't orgasm herself, but she gives a little moan of satisfaction as she feels you release your seed inside her."
                            wt_image indy_sex_3_state_4_9
                            player.c "[player.orgasm_text]"
                            wt_image indy_sex_3_state_4_10
                            terri.c "Oh!"
                            wt_image indy_strip_state_4_8
                            player.c "Keep working on squeezing with your Kegel muscles and pay attention to the man's reactions to know when to go slower and when to go faster.  Keep practicing, and you'll soon be a dream lay for any man."
                            wt_image indy_hypno_state_4_4
                            terri.c "Thank you!  Coming from you, that means a lot!"
                        elif terri.state == 5:
                            wt_image indy_portrait_state_5
                            player.c "Time to teach you more about fucking, [terri.name]."
                            wt_image indy_strip_state_5_1
                            "As she undresses, you do the same, then take a seat."
                            wt_image indy_strip_state_5_7
                            player.c "Once you're naked, climb up here on top of me."
                            wt_image indy_strip_state_5_8
                            terri.c "You want me on top?"
                            wt_image indy_strip_state_5_4
                            player.c "I do.  I'm going to teach you how to bring a man to orgasm by riding his cock."
                            wt_image indy_sex_3_state_5_1
                            "As usual, despite her willingness to have sex with you and a generous application of lube ..."
                            wt_image indy_sex_3_state_5_2
                            "... she struggles with the discomfort of fitting you inside."
                            wt_image indy_sex_3_state_5_3
                            player.c "Remember to play with your clit, [terri.name].  In this position, you control when and how far I go inside you.  Let your mind drift to sexy thoughts as you relax and play with yourself."
                            wt_image indy_sex_3_state_5_4
                            "It takes a while, but eventually she makes herself wet enough that she can start to move on you without discomfort."
                            wt_image indy_sex_3_state_5_5
                            player.c "Fuck me now, [terri.name].  Ride my hard cock up and down.  Start off nice and slow and easy, then pick up the pace."
                            wt_image indy_sex_3_state_5_6
                            "You help guide her with your hands on her ass, showing her how to slam down on the down thrusts, how far to come up on the up thrusts, and when to move faster."
                            wt_image indy_sex_3_state_5_7
                            player.c "Use your cunt muscles, too, [terri.name].  Grip me at the top, then relax as you slam down.  Squeeze again at the bottom before rising up again."
                            wt_image indy_sex_3_state_5_8
                            "This is new to her, but she's getting the hang of it."
                            wt_image indy_sex_3_state_5_9
                            "She rides you faster and faster, squeezing and milking you as best she can.  When you think her legs muscles are ready to give out from fatigue, you take pity on her and let yourself climax.  She doesn't orgasm herself, but she gives a little moan of satisfaction as she feels you release your seed inside her."
                            wt_image indy_sex_3_state_5_10
                            player.c "[player.orgasm_text]"
                            terri.c "Oh!"
                            wt_image indy_strip_state_5_4
                            player.c "Keep working on squeezing with your Kegel muscles and pay attention to the man's reactions to know when to go slower and when to go faster.  Keep practicing, and you'll soon be a dream lay for any man."
                            wt_image indy_talk_state_5_4
                            terri.c "Thank you!  Coming from you, that means a lot!"
                        change terri resistance by -5
                    $ terri.sex_training_count += 1
                    $ terri.sex_count += 1
                    orgasm
                    $ terri.temporary_count = 2
                    change terri sos by 10
            "Do something else instead":
                $ terri.temporary_count = 0 # shuts off end_day
    call terri_end_training_session from _call_terri_end_training_session_1 # checks to see if training actually complete and if so, ends_day
    return

label terri_first_bj_ending:
    wt_image indy_bj_1_state_1_9
    terri.c "I didn't realize that. Thank you."
    wt_image indy_bj_1_state_1_4
    "Once again, she starts sucking on you like a vacuum cleaner. She has no technique whatsoever. You move her hand to your balls and she holds them, but without attempting any form of caress. And she provides no stimulation to any part of your cock except the head, on which she maintains a steady suction. She clearly needs a lot of instruction."
    wt_image indy_bj_1_state_1_17
    "Despite that, the sight of her staring up at you, so eager to please, combined with the sensation of the steady suction, has you at the edge of orgasm. You can work on her technique later, for today you're ready to give her some positive reinforcement. The only decision is whether to let her keep sucking until you fill her mouth, or pull out and see how she handles a facial."
    $ title = "Where do you want to cum?"
    menu:
        "On her face":
            wt_image indy_bj_1_state_1_9
            "[terri.name] looks at you in surprise as you pull yourself out of her mouth."
            wt_image indy_bj_1_state_1_11
            player.c "Hold your hair back and keep looking at me.  Don't move."
            wt_image indy_bj_1_state_1_7
            "She does as you say. As you stroke your cock, she realizes what you're doing, and opens her mouth, perhaps thinking you will deposit your load there. Instead, you let your jizz spurt over her pretty, upturned face."
            wt_image indy_bj_1_state_1_8
            player.c "[player.orgasm_text]"
            wt_image indy_bj_1_state_1_14
            terri.c "Would my boyfriend want to do that?"
            player.c "He's never done that with you?"
            "She shakes her head."
            player.c "If you suggest it, I'm sure he'll take you up on the offer."
            wt_image indy_bj_1_state_1_13
            terri.c "Am I allowed to clean my face?"
            player.c "Only when he tells you. You'll wear my sperm until you're dressed and ready to go. You can clean up just before you leave."
            wt_image indy_bj_1_state_1_12
            terri.c "Okay. Was that good?"
            player.c "Okay, for a beginner. I can teach you to be better, though."
            wt_image indy_bj_1_state_1_14
            terri.c "Would you, please?  I'd like that."
            $ terri.facial_count += 1
            if terri.facial_count == 1:
                change terri submission by 10
        "In her mouth":
            wt_image indy_bj_1_state_1_10
            player.c "[player.orgasm_text]"
            "[terri.name] makes a face as the first spurts strike the back of her throat ..."
            wt_image indy_bj_1_state_1_18
            "... and pulls back, letting the rest of your jizz dribble out of her mouth."
            wt_image indy_bj_1_state_1_19
            player.c "Don't do that.  Swallow it."
            wt_image indy_bj_1_state_1_5
            "She looks at you in surprise, then does as you say. After she's swallowed it all except a small drizzle on her chin, she looks at you quizzically."
            terri.c "Why did you want me to swallow it?  Do men like that?"
            player.c "Usually, yes."
            wt_image indy_bj_1_state_1_6
            terri.c "I didn't know that.  Thank you.  Was that good?"
            player.c "Okay, for a beginner.  I can teach you to be better, though."
            terri.c "Would you, please?  I'd like that."
            $ terri.swallow_count += 1
    return

label terri_second_bj_ending:
    wt_image indy_bj_2_state_1_1
    "[terri.name] puts your cock in her mouth and starts sucking on it immediately."
    wt_image indy_bj_3_state_1_7
    player.c "No.  Stop.  You need to tease my cock first.  Use your tongue and lips, softly, on the shaft."
    wt_image indy_bj_2_state_1_2
    player.c "Better.  That's it.  Lick and tease my dick to get things started."
    wt_image indy_bj_3_state_1_1
    player.c "Now take my cock into your mouth, but don't just start sucking on it. Use your tongue on the underside of the head."
    wt_image indy_bj_2_state_1_4
    player.c "Good, now keep doing that while you wrap your lips gently around me and start bobbing up and down on the shaft."
    wt_image indy_bj_2_state_1_3
    player.c "That's it.  Remember to look at me while you blow me."
    wt_image indy_bj_3_state_1_2
    "She keeps her eyes on you as she follows your instructions.  It's not great, but it's better than her previous effort, and you soon fill her mouth with cum."
    wt_image indy_bj_2_state_1_3
    player.c "[player.orgasm_text]"
    wt_image indy_bj_2_state_1_4
    player.c "Swallow it all, [terri.name]."
    wt_image indy_bj_2_state_1_1
    "She gulps down the load you left in her mouth, and even licks the last bit of cum from the tip of your cock, before looking up at you, nervously."
    wt_image indy_bj_2_state_1_5
    terri.c "Was that better?  Did you enjoy it?  I mean, would my boyfriend enjoy that?"
    $ terri.blowjob_count += 1
    $ terri.swallow_count += 1
    orgasm
    return

label terri_variety_training:
    $ terri.temporary_count = 1
    # skip if variety training complete
    if terri.handjob_count != 0 and terri.footjob_count != 0 and terri.bondage_sex_count != 0 and terri.ass_lick_count != 0 and terri.anal_count != 0 and terri.has_tag('titfuck_attempted'):
        "You've run out of new activities to try with [terri.name].  Select something different to do with her for today's session."
        $ terri.temporary_count = 0
    else:
        if terri.state == 1:
            wt_image indy_talk_state_1_2
        elif terri.state == 2:
            wt_image indy_talk_state_2_1
        elif terri.state == 3:
            wt_image indy_talk_state_3_7
        elif terri.state == 4:
            wt_image indy_hypno_state_4_1
        elif terri.state == 5:
            wt_image indy_bj_1_state_5_1
        player.c "Ready to try something new, [terri.name]?"
        if terri.state == 1:
            wt_image indy_talk_state_1_1
        elif terri.state == 2:
            wt_image indy_hypno_state_2_1
        elif terri.state == 3:
            wt_image indy_talk_state_3_3
        elif terri.state == 4:
            wt_image indy_talk_state_4_11
        elif terri.state == 5:
            wt_image indy_hypno_state_5_1
        "She nods, her face a combination of apprehension and interest at what you may have in mind."
        $ title = "What would you like to try with her?"
        menu:
            "Hand job" if terri.handjob_count == 0:
                call terri_handjob_training from _call_terri_handjob_training
            "Foot job" if terri.footjob_count == 0:
                call terri_footjob_training from _call_terri_footjob_training
            "Tit job" if not terri.has_tag('titfuck_attempted'):
                call terri_titjob_training from _call_terri_titjob_training
            "Bondage sex" if terri.bondage_sex_count == 0:
                call terri_bondage_sex_training from _call_terri_bondage_sex_training
            "Have her lick your ass" if terri.ass_lick_count == 0:
                call terri_asslicking_training from _call_terri_asslicking_training
            "Anal sex" if terri.anal_count == 0:
                if terri.has_item(butt_plug):
                    player.c "[terri.name], have you been wearing the anal plug I gave you?"
                    if terri.state == 1:
                        wt_image indy_talk_state_1_2
                    elif terri.state == 2:
                        wt_image indy_talk_state_2_3
                    elif terri.state == 3:
                        wt_image indy_portrait_state_3
                    elif terri.state == 4:
                        wt_image indy_talk_state_4_7
                    elif terri.state == 5:
                        wt_image indy_talk_state_5_2
                    "She blushes."
                    player.c "You know what that's for, don't you?"
                    if terri.state == 1:
                        wt_image indy_talk_state_1_3
                    elif terri.state == 2:
                        wt_image indy_talk_state_2_5
                    elif terri.state == 3:
                        wt_image indy_talk_state_3_6
                    elif terri.state == 4:
                        wt_image indy_talk_state_4_4
                    elif terri.state == 5:
                        wt_image indy_portrait_state_5
                    terri.c "You want me to get used to having something back there.  In case my boyfriend wants to put his penis there."
                    if terri.state == 1:
                        wt_image indy_strip_state_1_12
                    elif terri.state == 2:
                        wt_image indy_strip_state_2_12
                    elif terri.state == 3:
                        wt_image indy_strip_state_3_3
                    elif terri.state == 4:
                        wt_image indy_strip_state_4_13
                    elif terri.state == 5:
                        wt_image indy_strip_state_5_1
                    player.c "Not if, [terri.name], when.  Get your clothes off and then straddle me.  You're going to put my cock where you've been putting the butt plug."
                    call terri_anal_sex_proceed from _call_terri_anal_sex_proceed
                else:
                    player.c "[terri.name], you want to be able to please your boyfriend with every part of your body, right?"
                    if terri.state == 1:
                        wt_image indy_bj_1_state_1_1
                    elif terri.state == 2:
                        wt_image indy_talk_state_2_2
                    elif terri.state == 3:
                        wt_image indy_talk_state_3_1
                    elif terri.state == 4:
                        wt_image indy_talk_state_4_6
                    elif terri.state == 5:
                        wt_image indy_talk_state_5_1
                    terri.c "Yes, I think so."
                    player.c "You know there are three places in women where men like to put their cocks, right?  We've worked on two of those.  It's time to get you ready to take him in the third."
                    if terri.state == 1:
                        wt_image indy_hypno_state_1_2
                    elif terri.state == 2:
                        wt_image indy_talk_state_2_3
                    elif terri.state == 3:
                        wt_image indy_talk_state_3_6
                    elif terri.state == 4:
                        wt_image indy_talk_state_4_7
                    elif terri.state == 5:
                        wt_image indy_talk_state_5_3
                    "She blushes."
                    terri.c "You're too big for me to take back there."
                    player.c "It stretches, [terri.name]."
                    if terri.state == 1:
                        wt_image indy_talk_state_1_3
                    elif terri.state == 2:
                        wt_image indy_talk_state_2_4
                    elif terri.state == 3:
                        wt_image indy_talk_state_3_7
                    elif terri.state == 4:
                        wt_image indy_talk_state_4_8
                    elif terri.state == 5:
                        wt_image indy_hypno_state_5_1
                    terri.c "Not that much.  It hurts sometimes even when you put it in my pussy.  I'm not ready to try back there."
                    if terri.test('submission', 60):
                        player.c "A little pain is no reason not to be ready to please your man.  I thought I taught you better than that?"
                        if terri.state == 1:
                            wt_image indy_talk_state_1_2
                        elif terri.state == 2:
                            wt_image indy_talk_state_2_5
                        elif terri.state == 3:
                            wt_image indy_talk_state_3_8
                        elif terri.state == 4:
                            wt_image indy_talk_state_4_12
                        elif terri.state == 5:
                            wt_image indy_talk_state_5_6
                        "She hangs her head."
                        terri.c "Yes, you did."
                        if terri.state == 1:
                            wt_image indy_strip_state_1_12
                        elif terri.state == 2:
                            wt_image indy_strip_state_2_7
                        elif terri.state == 3:
                            wt_image indy_strip_state_3_3
                        elif terri.state == 4:
                            wt_image indy_strip_state_4_8
                        elif terri.state == 5:
                            wt_image indy_strip_state_5_7
                        player.c "Then no more silly objections.  Get your clothes off and then straddle me.  You're going to learn how to use your third hole."
                        call terri_anal_sex_proceed from _call_terri_anal_sex_proceed_1
                    else:
                        "You'll either need to get her used to taking something in her butt or increase her submission to you.  For today, choose a different action."
                        $ terri.temporary_count = 0
            "None of these":
                $ terri.temporary_count = 0
    call terri_end_training_session from _call_terri_end_training_session_2 # checks to see if training actually complete and if so, ends_day
    return

label terri_handjob_training:
    player.c "You have a sexy body, [terri.name].  You can use lots of different parts of it to please your boyfriend.  Today we're going to teach you how to please him with your hands.  Take a hold of my cock, [terri.name]."
    # intro content
    if terri.state == 2:
        wt_image indy_hj_1_state_2_1
        "[terri.name] stands up and removes your cock from your pants."
        wt_image indy_hj_1_state_2_7
        player.c "Good.  Now run your hands along it."
        wt_image indy_hj_1_state_2_8
        player.c "Gently.  You're not trying to pull it off me.  Use light touches, teasing touches.  The head is particularly sensitive, so pay it lots of attention, but gentle attention to start."
        wt_image indy_hj_1_state_2_9
        "She runs her soft fingers along your cock, swirling and teasing them lightly against your cockhead."
        wt_image indy_hj_1_state_2_10
        player.c "Feel how it's now throbbing in your hand?  It's ready for you to start using firmer strokes."
        wt_image indy_hj_1_state_2_11
        "She kneels down and starts pumping you vigorously."
        wt_image indy_hj_1_state_2_2
        player.c "Slower than that to start with.  You don't want to rush to get him off, you want him to enjoy the process."
        wt_image indy_hj_1_state_2_12
        player.c "Speaking of which, take off your clothes.  He'll enjoy getting to look at your body while you stroke him."
        wt_image indy_hj_1_state_2_3
        "She removes her clothes ..."
        wt_image indy_hj_1_state_2_4
        "... as you direct her to the sofa."
        wt_image indy_hj_1_state_2_13
        player.c "Finish undressing while I sit down.  You want to make sure your boyfriend is comfortable so he can fully enjoy the sight of your body and the feeling of your hands on him."
    else:
        wt_image indy_hj_1_state_1_1
        "[terri.name] removes your cock from your pants."
        player.c "Good.  Now run your hands along it."
        wt_image indy_hj_1_state_1_2
        "She does so, vigorously, pumping you with a firm grip."
        player.c "Gently.  You're not trying to pull it off me.  Use light touches, teasing touches.  The head and balls are particularly sensitive, so pay them lots of attention, but gentle attention to start."
        wt_image indy_hj_1_state_1_3
        "She runs her soft fingers along your cock, swirling and teasing them lightly against your cockhead, while she cups and plays with your balls with her other hand."
        player.c "Feel how it's now throbbing in your hand?  It's ready for you to start using firmer strokes."
        wt_image indy_hj_1_state_1_4
        "She resumes pumping you vigorously."
        player.c "Slower than that to start with.  You don't want to rush to get him off, you want him to enjoy the process.  Speaking of which, take off your clothes.  He'll enjoy getting to look at your body while you stroke him."
        wt_image indy_hj_1_state_2_13
        "She removes her clothes, then resumes stroking you."
        player.c "Give me some space to sit down.  You want to make sure your boyfriend is comfortable so he can fully enjoy the sight of your body and the feeling of your hands on him."
    # finish scene
    wt_image indy_hj_1_state_2_6
    "As you settle back and make yourself comfortable, [terri.name] lies beside you ..."
    wt_image indy_hj_1_state_2_5
    "... and provides a nice show to go along with the handjob."
    wt_image indy_hj_1_state_2_14
    "As sex skills go, a handjob is about as basic as it gets.  A pretty face, a grip that's not too soft and not too firm, and you're good to go.  It's not long before [terri.name] has the hang of it and you can feel the tension building in your balls."
    wt_image indy_hj_1_state_2_15
    player.c "Pump faster now, [terri.name]."
    wt_image indy_hj_1_state_2_16
    "As she does, you let go onto her pumping hand."
    wt_image indy_hj_1_state_2_17
    player.c "[player.orgasm_text]"
    terri.c "Oh!  I didn't think you'd want to cum that way.  Doesn't a man want to be inside me when he cums?"
    player.c "Often, but this can be nice for a change, or when the time and place doesn't allow for other activities."
    wt_image indy_hj_1_state_2_18
    player.c "Next time, though, don't stop stroking when the man is coming.  Get closer and tighten your grip a little, forming a fist. Then let him spurt on you while you pump the cum out of him. Ideally, aim for your face, to truly show him you belong to him.  Your tits, belly and pussy are all good targets too.  Or if you're out in public, just wrap your lips around him and pump it into your mouth to keep from making a mess."
    wt_image indy_hj_1_state_2_19
    terri.c "All right. I will.  Thank you!"
    "[terri.name] seems happy with herself as she leaves."
    change terri sos by 5
    $ terri.handjob_count = 1
    orgasm
    return

label terri_footjob_training:
    player.c "You can use many different parts of your body to please your boyfriend, [terri.name].  Let's work on one of those now.  Take off your clothes and lie on the sofa."
    wt_image indy_fj_state_1_7
    "As [terri.name] lies down, you place her feet on your cock."
    wt_image indy_fj_state_1_8
    "Instinctively, she grasps it between her insteps."
    wt_image indy_fj_state_1_9
    player.c "Good.  Now move your feet along my shaft to stroke my cock."
    wt_image indy_fj_state_1_1
    "She does as instructed ..."
    wt_image indy_fj_state_1_10
    "... sliding the soft soles of her feet back-and-forth along your shaft."
    wt_image indy_fj_state_1_11
    terri.c "Does this feel good?  Wouldn't my boyfriend rather be inside me?"
    wt_image indy_fj_state_1_8
    player.c "This is about you learning how to please a man, [terri.name], in a way that's fun for both of you.  Just doing the same thing over-and-over again can get boring.  If you want to a great sex partner, you need to learn lots of different ways to excite a man."
    wt_image indy_fj_state_1_2
    player.c "Speaking of which, there's more to your feet than just your soles.  You can use the other parts of your feet to please a man, too."
    wt_image indy_fj_state_1_12
    "[terri.name] starts running her toes along your shaft ..."
    wt_image indy_fj_state_1_13
    "... then shifts her grip ..."
    wt_image indy_fj_state_1_14
    "... and starts stroking you with the tops of her feet."
    wt_image indy_fj_state_1_3
    terri.c "I can apply more pressure this way.  Does it still feel okay?"
    wt_image indy_fj_state_1_13
    player.c "It feels great, [terri.name].  If you keep pumping me like that, you'll make me cum."
    wt_image indy_fj_state_1_15
    terri.c "Really?  Just from me doing this?"
    wt_image indy_fj_state_1_14
    "She seems excited at the prospect and picks up her speed."
    wt_image indy_fj_state_1_16
    player.c "I'm about to let go now, [terri.name], and when I do, it'll be onto your feet.  Are you ready?"
    wt_image indy_fj_state_1_5
    "She nods and relaxes her feet as you finish yourself off on them."
    wt_image indy_fj_state_1_17
    player.c "[player.orgasm_text]"
    wt_image indy_fj_state_1_6
    "You coat her feet with your cum, wiping the head of your cock off on her toes."
    terri.c "Wow.  It feels like you really did enjoy that."
    wt_image indy_fj_state_1_18
    terri.c "I hope my boyfriend enjoys my feet as much as you did!"
    change terri sos by 10
    $ terri.footjob_count = 1
    orgasm
    return

label terri_titjob_training:
    add tags 'titfuck_attempted' to terri
    player.c "A good girlfriend uses every part of her body to please her boyfriend, [terri.name].  Remove your top.  Today you're going to pleasure my cock with your tits."
    if terri.state == 1:
        wt_image indy_hypno_state_1_3
        terri.c "My tits?"
        wt_image indy_strip_state_1_15
        terri.c "They're very small."
    elif terri.state == 2:
        wt_image indy_strip_state_2_7
        terri.c "My tits?"
        wt_image indy_hypno_state_2_4
        terri.c "They're very small."
    elif terri.state == 3:
        wt_image indy_strip_state_3_11
        terri.c "My tits?"
        wt_image indy_hypno_state_3_3
        terri.c "They're very small."
    elif terri.state == 4:
        wt_image indy_strip_state_4_13
        terri.c "My tits?"
        wt_image indy_strip_state_4_14
        terri.c "They're very small."
    else:
        wt_image indy_hypno_state_5_2
        terri.c "My tits?  They're very small."
    player.c "Yes, they are. Hopefully you can still fuck a man's cock with them. Push them together to make a valley for my cock."
    wt_image indy_titfuck_attempt_1_1
    terri.c "I can't!  They're too small for that.  They won't even reach each other, let alone form a valley."
    wt_image indy_titfuck_attempt_1_11
    terri.c "What if I do this?"
    wt_image indy_titfuck_attempt_1_12
    "She presses your cock against her breast ..."
    wt_image indy_titfuck_attempt_1_13
    "... then spits on it."
    wt_image indy_titfuck_attempt_1_3
    "... and rubs the head of your cock against her tiny breasts."
    wt_image indy_titfuck_attempt_1_14
    terri.c "Does that feel good?"
    player.c "That's just teasing, [terri.name]."
    wt_image indy_titfuck_attempt_1_4
    terri.c "Well, I'm sorry.  I don't know what else I can do?  I have small breasts.  Really small breasts.  I can't help it."
    $ title = "What do you tell her?"
    menu:
        "You could help it":
            player.c "Having small tits is a choice, [terri.name].  You could help it, if you wanted to."
            wt_image indy_titfuck_attempt_1_10
            terri.c "You think I should get a boob job?"
            player.c "That's up to you, [terri.name].  All I know is you can't give your boyfriend a nice titfuck with a flat chest.  Get dressed, we'll do something else today."
            if terri.state == 1:
                wt_image indy_strip_state_1_9
            elif terri.state == 2:
                wt_image indy_strip_state_2_8
            elif terri.state == 3:
                wt_image indy_strip_state_3_12
            elif terri.state == 4:
                wt_image indy_strip_state_4_14
            else:
                wt_image indy_hypno_state_5_2
            terri.c "Okay.  Thank you.  I'm sorry I have a flat chest.  It must be more enjoyable for you to train your other clients.  Better endowed ones."
            $ terri.boobjob_interest += 1
            sys "[terri.name] is now more self-conscious about the size of her breasts."
            $ terri.temporary_count = 0
            change terri sos by -5 notify
        "Teasing can be okay":
            player.c "I guess you'll need to do your best with what you have.  Get back to teasing my dick."
            wt_image indy_titfuck_attempt_1_3
            terri.c "Like this?"
            player.c "That'll get me hard, but it won't get me off."
            wt_image indy_titfuck_attempt_1_5
            terri.c "What if I do this?"
            wt_image indy_titfuck_attempt_1_15
            player.c "Remember, I want to get off on your tits today, [terri.name]."
            "She looks at you for a moment, thinking."
            if terri.handjob_count > 0 and terri.facial_count > 0:
                wt_image indy_titfuck_attempt_1_16
                terri.c "You seemed to enjoy when I jerked you off ..."
                wt_image indy_titfuck_attempt_1_15
                terri.c "... and when you came on my face."
                wt_image indy_titfuck_attempt_1_6
                terri.c "What if I jerked you off onto my tits?"
                wt_image indy_titfuck_attempt_1_7
                terri.c "Does that feel good?"
                player.c "Tits, remember?  Get me off on them."
                wt_image indy_titfuck_attempt_1_2
                player.c "[player.orgasm_text]"
                wt_image indy_titfuck_attempt_1_8
                terri.c "Oh, wow!  Look how much cum you sprayed on me!"
                wt_image indy_titfuck_attempt_1_9
                terri.c "Even though my tits are tiny, do you think my boyfriend would enjoy cumming on them like that?"
                player.c "I'm sure he would, [terri.name]."
                change terri sos by 10
                $ terri.handjob_count += 1
                orgasm notify
            else:
                wt_image indy_titfuck_attempt_1_4
                terri.c "I'm sorry, I'm not experienced enough with men.  I don't know how to please you.  Can we do something else?"
                if terri.state == 1:
                    wt_image indy_strip_state_1_9
                elif terri.state == 2:
                    wt_image indy_strip_state_2_8
                elif terri.state == 3:
                    wt_image indy_strip_state_3_12
                elif terri.state == 4:
                    wt_image indy_strip_state_4_7
                else:
                    wt_image indy_hypno_state_5_2
                player.c "Okay, [terri.name].  Get dressed and we'll start again.  Don't get discouraged, everyone has to learn."
                terri.c "I guess."
                change terri sos by -5 notify
                $ terri.temporary_count = 0
        "They help you look young":
            player.c "It's okay.  Small tits help you to look young."
            if terri.state == 1:
                wt_image indy_strip_state_1_9
            elif terri.state == 2:
                wt_image indy_hypno_state_2_4
            elif terri.state == 3:
                wt_image indy_strip_state_3_9
            elif terri.state == 4:
                wt_image indy_strip_state_4_12
            else:
                wt_image indy_hypno_state_5_2
            terri.c "They do?  But that's not good, right?  Men want to fuck a woman, not someone who looks like a little girl."
            player.c "Some men like the little girl look."
            if terri.state == 1:
                wt_image indy_hypno_state_1_2
            elif terri.state == 2:
                wt_image indy_strip_state_2_12
            elif terri.state == 3:
                wt_image indy_strip_state_3_7
            elif terri.state == 4:
                wt_image indy_hypno_state_4_4
            else:
                wt_image indy_hypno_state_5_2
            if terri.youth_interest < 3:
                $ terri.youth_interest += 1
                "She looks pleased as she contemplates that remark."
                sys "[terri.name] is now more interested in acting young."
            else:
                terri.c "Really?  So I guess I have the right type of body to dress and act young."
                change terri sos by 5 notify
    wt_image current_location.image
    return

label terri_bondage_sex_training:
    player.c "[terri.name], sometimes a man enjoys the sight of his woman helpless and vulnerable in front of him.  Has your boyfriend ever tied you up before sex?"
    if terri.state == 1:
        wt_image indy_talk_state_1_2
    elif terri.state == 2:
        wt_image indy_hypno_state_2_2
    elif terri.state == 3:
        wt_image indy_talk_state_3_7
    elif terri.state == 4:
        wt_image indy_hypno_state_4_5
    elif terri.state == 5:
        wt_image indy_talk_state_5_7
    terri.c "No, never."
    player.c "I want to show you what that's like, so that you can encourage him to try it with you."
    if terri.test('submission', 30):
        $ terri.temporary_count = 5 #so it can be used to track submission impact; it gets set back to 1 at end
        if terri.state == 1:
            wt_image indy_talk_state_1_3
        elif terri.state == 2:
            wt_image indy_talk_state_2_5
        elif terri.state == 3:
            wt_image indy_talk_state_3_8
        elif terri.state == 4:
            wt_image indy_talk_state_4_12
        elif terri.state == 5:
            wt_image indy_talk_state_5_8
        "[terri.name] looks like she's about to object."
        player.c "[terri.name], this is something an obedient girlfriend does to please her boyfriend.  Take off your clothes now.  I'm going to tie you up."
        if terri.state == 1:
            wt_image indy_strip_state_1_12
        elif terri.state == 2:
            wt_image indy_strip_state_2_7
        elif terri.state == 3:
            wt_image indy_strip_state_3_3
        elif terri.state == 4:
            wt_image indy_strip_state_4_8
        elif terri.state == 5:
            wt_image indy_strip_state_5_4
        "She's submissive enough to you not to argue.  She stands up and strips, watching nervously as you lay out the ropes you will use to bind her."
        wt_image indy_bondage_1
        "You tie her hands together to start."
        player.c "Get me hard with your hands, [terri.name], before I immobilize you completely."
        wt_image indy_bondage_2
        player.c "Now your mouth, [terri.name]."
        wt_image indy_bondage_3
        player.c "One of the good things about being tied up for your man, [terri.name], is that it encourages him to really take control, and use you the way he wants to use you."
        wt_image indy_bondage_4
        player.c "For example, he may shove himself deeper into your mouth than he normally does. Which means you get the opportunity to please him more completely than you would under other circumstances."
        if terri.ass_lick_count > 0:
            wt_image indy_bondage_5
            player.c "He'll enjoy you licking his ass at any time, but when you're tied up and unable to move away, it may feel that much better to have your little pink tongue probing his anus."
        if dungeon.has_item(gags):
            $ title = "Use a ball gag on her?"
            menu:
                "Yes":
                    wt_image indy_bondage_6
                    player.c "When he's finished having fun with your mouth, he'll move on to other things. You're his right now, so if he doesn't need your mouth, neither do you. A ball gag is a nice way to emphasize the point. You should consider buying him one to use on you as a present."
                    "The experience of having her voice taken away is an intense one for [terri.name]. She reacts more strongly to it than she did to being tied up, trembles passing through her body as you lock the gag in place."
                    wt_image indy_bondage_7
                    player.c "There we go. Feeling helpless yet, [terri.name]?"
                    "A soft murmur from behind the gag might have been a yes, or just a groan. It doesn't really matter. She was obedient before. Now she's pliable putty in your hand as you turn her around."
                    wt_image indy_bondage_8
                    player.c "Open yourself up."
                    wt_image indy_bondage_9
                    "She groans into the gag as you shove yourself into her. She still isn't getting wet before intercourse, and in this position, she can't even play with her clit to try and stimulate herself."
                    "You don't care. This is about bringing out her submissive side. If it hurts a bit while you fuck her, so much the better. Fortunately for her, her body comes to her defense, and starts to moisten as much in self-preservation as excitement as you fuck her and pull her hair."
                    wt_image indy_bondage_16
                    "She still isn't as completely helpless as you'd like, so you pull out of her and position her on the floor. Then you place a blindfold over her eyes, and resume fucking her."
                    wt_image indy_bondage_10
                    "You keep at it for quite a while. Tied, blindfolded and gagged, time begins to lose meaning for [terri.name]. All there is is the floor under her head and knees and your cock pounding into her."
                    "Most submissive women would be fighting the need to orgasm throughout this experience. [terri.name] isn't. She's wet, but barely wet, and putting up with this experience to please you, without getting any deep satisfaction out of it herself."
                    "She may be obedient, but she's not sexually submissive. At least not to you."
                    $ terri.temporary_count += 10
                "No":
                    wt_image indy_bondage_11
                    player.c "When he's finished having fun with your mouth, he'll move on to other things. Put your head down and your ass up."
                    "You circle her while she waits nervously."
                    wt_image indy_bondage_12
                    "When you finally shove yourself into her, she lets out a grunt. She still isn't getting wet before intercourse, and in this position, she can't even play with her clit to try and stimulate herself."
                    "You don't care. This is about bringing out her submissive side. If it hurts a bit while you fuck her, so much the better. Fortunately for her, her body comes to her defense, and starts to moisten as much in self-preservation as excitement as you fuck her."
                    wt_image indy_bondage_13
                    "She still isn't as completely helpless as you'd like, so you place a blindfold over her eyes, and resume fucking her."
                    "You keep at it for quite a while. Tied and blindfolded, time begins to lose meaning for [terri.name]. All there is is the floor under her head and knees and your cock pounding into her."
                    "Most submissive women would be fighting the need to orgasm throughout this experience. [terri.name] isn't. She's wet, but barely wet, and putting up with this experience to please you, without getting any deep satisfaction out of it herself."
                    "She may be obedient, but she's not sexually submissive. At least not to you."
        else:
            wt_image indy_bondage_11
            player.c "When he's finished having fun with your mouth, he'll move on to other things."
            player.c "Put your head down and your ass up."
            "You circle her while she waits nervously."
            wt_image indy_bondage_12
            "When you finally shove yourself into her, she lets out a grunt. She still isn't getting wet before intercourse, and in this position, she can't even play with her clit to try and stimulate herself."
            "You don't care. This is about bringing out her submissive side. If it hurts a bit while you fuck her, so much the better. Fortunately for her, her body comes to her defense, and starts to moisten as much in self-preservation as excitement as you fuck her."
            wt_image indy_bondage_13
            "She still isn't as completely helpless as you'd like, so you place a blindfold over her eyes, and resume fucking her."
            "You keep at it for quite a while. Tied and blindfolded, time begins to lose meaning for [terri.name]. All there is is the floor under her head and knees and your cock pounding into her."
            "Most submissive women would be fighting the need to orgasm throughout this experience. [terri.name] isn't. She's wet, but barely wet, and putting up with this experience to please you, without getting any deep satisfaction out of it herself."
            "She may be obedient, but she's not sexually submissive. At least not to you."
        wt_image indy_bondage_17
        "You pull her back to her knees and finish on her face."
        player.c "[player.orgasm_text]"
        wt_image indy_bondage_14
        player.c "Clean me off [terri.name]."
        "Dutifully, she cleans your cock with her mouth as your cum drips down her cheek and onto her breasts."
        if terri.facial_count == 0:
            $ terri.temporary_count += 10
        wt_image indy_bondage_15
        terri.c "Thank you for showing me that. I'll ask my boyfriend if he'd like to tie me up. I don't think he will, though. He's not really into kinky things."
        $ terri.facial_count += 1
        $ terri.sex_count += 1
        $ terri.bondage_sex_count = 1
        change terri submission by terri.temporary_count
        $ terri.temporary_count = 1
        orgasm
    else:
        if terri.state == 1:
            wt_image indy_hypno_state_1_5
        elif terri.state == 2:
            wt_image indy_hypno_state_2_5
        elif terri.state == 3:
            wt_image indy_talk_state_3_8
        elif terri.state == 4:
            wt_image indy_talk_state_4_10
        elif terri.state == 5:
            wt_image indy_talk_state_5_6
        terri.c "I'm not sure about that.  My boyfriend isn't really into kinky things, and neither am I.  I'd rather learn other ways to please him.  Normal ways."
        "If she were more Submissive towards you, she might let you tie her up.  For today, choose another action."
        $ terri.temporary_count = 0
    return

label terri_asslicking_training:
    player.c "[terri.name], you want to be able to please your boyfriend by pleasuring every part of his body, right?"
    if terri.state == 1:
        wt_image indy_bj_1_state_1_1
    elif terri.state == 2:
        wt_image indy_bj_1_state_2_1
    elif terri.state == 3:
        wt_image indy_talk_state_3_1
    elif terri.state == 4:
        wt_image indy_talk_state_4_9
    elif terri.state == 5:
        wt_image indy_portrait_state_5
    terri.c "Yes, I think so."
    player.c "You've learned some of the ways to please him, but there's one very sensitive area we haven't addressed yet."
    if terri.state == 1:
        wt_image indy_hypno_state_1_2
    elif terri.state == 2:
        wt_image indy_talk_state_2_2
    elif terri.state == 3:
        wt_image indy_talk_state_3_3
    elif terri.state == 4:
        wt_image indy_hypno_state_4_5
    elif terri.state == 5:
        wt_image indy_talk_state_5_2
    terri.c "Where's that?"
    player.c "His anus."
    if terri.state == 1:
        wt_image indy_talk_state_1_3
    elif terri.state == 2:
        wt_image indy_talk_state_2_1
    elif terri.state == 3:
        wt_image indy_talk_state_3_8
    elif terri.state == 4:
        wt_image indy_talk_state_4_3
    elif terri.state == 5:
        wt_image indy_talk_state_5_3
    terri.c "How ... What should I be doing with that?"
    player.c "Using your tongue in it."
    if terri.test('submission', 50):
        if terri.state == 1:
            wt_image indy_talk_state_1_1
        elif terri.state == 2:
            wt_image indy_talk_state_2_4
        elif terri.state == 3:
            wt_image indy_talk_state_3_9
        elif terri.state == 4:
            wt_image indy_talk_state_4_4
        elif terri.state == 5:
            wt_image indy_talk_state_5_8
        terri.c "I ... I'll think about it.  Maybe I'll try using my finger, or even my tongue, on my boyfriend someday.  But ..."
        player.c "No buts, [terri.name].  Okay, that's a bad pun.  No silly objections, [terri.name].  I've told you this is something your boyfriend will enjoy.  That's why you hired me."
        if terri.state == 1:
            wt_image indy_talk_state_1_3
        elif terri.state == 2:
            wt_image indy_hypno_state_2_2
        elif terri.state == 3:
            wt_image indy_talk_state_3_8
        elif terri.state == 4:
            wt_image indy_hypno_state_4_5
        elif terri.state == 5:
            wt_image indy_talk_state_5_7
        player.c "You're going to pleasure my anus as part of your training, and then the next time you see your boyfriend you're going to ask him if he'd like you to do the same for him."
        if terri.state == 1:
            wt_image indy_talk_state_1_2
        elif terri.state == 2:
            wt_image indy_talk_state_2_5
        elif terri.state == 3:
            wt_image indy_hypno_state_3_5
        elif terri.state == 4:
            wt_image indy_talk_state_4_12
        elif terri.state == 5:
            wt_image indy_talk_state_5_6
        "She hangs her head slightly and nods."
        player.c "Get down on your knees, [terri.name]."
        wt_image indy_ass_lick_1
        "You remove your pants and stand over her, then guide her head to your anus."
        wt_image indy_ass_lick_2
        player.c "Get your tongue right in there, [terri.name]. Lick around the rim for a bit, then put your tongue in and lick the inside of my butt."
        wt_image indy_ass_lick_3
        "Once she's figured out what you want, you relax and enjoy the feeling of the pretty redhead's tongue in your anus."
        player.c "Remember, [terri.name], to offer this to your boyfriend this weekend."
        "She nods."
        player.c "Do as good a job for him as you're doing for me and he'll be very happy with you."
        "A smile brightens her face and she burrows deeper into your ass."
        change terri submission by 10
        change terri sos by 10
        change terri resistance by -5
        $ terri.ass_lick_count = 1
    else:
        if terri.state == 1:
            wt_image indy_hypno_state_1_5
        elif terri.state == 2:
            wt_image indy_talk_state_2_4
        elif terri.state == 3:
            wt_image indy_hypno_state_3_1
        elif terri.state == 4:
            wt_image indy_hypno_state_4_1
        elif terri.state == 5:
            wt_image indy_talk_state_5_8
        terri.c "I ... I'll think about it.  Maybe I'll try using my finger, or even my tongue, on my boyfriend someday.  But I'm not doing that right now with you."
        "If she was more submissive towards you, perhaps she'd react differently.  For today, you'll need to choose a different action."
        $ terri.temporary_count = 0
    return

label terri_anal_sex_proceed:
    wt_image indy_anal_1
    "Nervously, [terri.name] climbs up on top of you.  You lube yourself and her up really well, but her rosebud is still very tight."
    if terri.has_item(butt_plug):
        "You're larger even than the butt plug, and much longer. Not that she should be worried about your length. You'll fit in fine once her opening stretches. But she's nervous, and that isn't helping her let her sphincter relax and let you in."
    else:
       "She's nervous, and that isn't helping her let her sphincter relax and let you in."
    wt_image indy_anal_2
    "She lowers herself down and tries to get you in, but her body hasn't opened up enough yet."
    player.c "Relax, [terri.name]. Give your body time. It'll open up naturally."
    wt_image indy_anal_3
    "You turn her around and help support her weight."
    player.c "Let yourself come down slowly, gradually, as your body is ready."
    wt_image indy_anal_4
    "This time it works."
    terri.c "Ohhh!"
    "She gasps as the head of your cock passes through her sphincter ring."
    wt_image indy_anal_5
    "You add some additional lube and shift into position behind her where you can control the pace. She grimaces as you penetrate her again, but it's a lot easier the second time."
    wt_image indy_anal_8
    "To her surprise, you're able to start fucking in and out of her as quickly anally as you do vaginally. Now it's time to show her what her body is really capable of."
    wt_image indy_anal_6
    "You add some more lubricant, then pin her in place and start piledriving her ass."
    terri.c "Uuuugghhhhhh"
    "She groans, but it doesn't really hurt. You fuck her harder than you have before in any position, driving quickly in and out of her tight butt."
    wt_image indy_anal_9
    "There's only so much of that treatment you can give her before your balls boil over. With a deep groan you release your seed deep into her bowels."
    player.c "[player.orgasm_text]"
    wt_image indy_anal_7
    "As your cum drips out of her ass, she grins and gives you a hug."
    terri.c "Wow! I didn't think I was capable of doing that! I think my boyfriend will be really happy when I suggest we try this on the weekend."
    player.c "I'm sure he will be."
    change terri sos by 15
    change terri resistance by -5
    $ terri.anal_count = 1
    orgasm
    return

label terri_school_tell_classroom:
    player.c "Tell me how you completed your assignment."
    wt_image indy_school_1_12
    "Something about this setup seems to have aroused [terri.name], as she gets out of her seat ..."
    wt_image indy_school_1_13
    "... and slinks onto the desk in front of you."
    if terri.blowjob_training_count > 0:
        terri.c "Well, [terri.your_respect_name], first I took off my top, just like you taught me to, so he could look at my perky little schoolgirl titties. Then I got down on my knees and removed his cock from his pants. It's not as big as your cock, but it got nice and hard in my hand.  Then I put it in my mouth, and it got even harder."
        wt_image indy_school_1_14
        if terri.sex_training_count > 2:
            terri.c "After I sucked him until he was close to being ready to cum, I pulled off my panties and climbed on top of him and lowered myself onto his hard dick.  Then I rode him just like you taught me to, until he filled me with his goo.  So it's a good thing I'm on birth control, isn't it?"
        elif terri.sex_training_count == 2:
            terri.c "After I sucked him until he was close to being ready to cum, I turned around and pulled off my panties.  When he pushed himself inside me, I started fucking back against him, just like you taught me, until he filled me with his goo.  So it's a good thing I'm on birth control, isn't it?"
        else:
            terri.c "After I sucked him until he was close to being ready to cum, I pulled off my panties and lay down on the floor and spread my legs.  Then I let him fuck me until he filled me with his goo.  So it's a good thing I'm on birth control, isn't it?"
    else:
        terri.c "Well, [terri.your_respect_name], I knelt down beside him on the couch and took his cock out of his pants.  After it got hard in my hand, I put it in my mouth and it got even harder."
        wt_image indy_school_1_14
        terri.c "After I sucked him until he was close to being ready to cum, I pulled off my panties and spread my legs.  Then I let him fuck me until he came inside me."
    wt_image indy_school_1_13
    terri.c "This is so fun!  I'm just imagining what it would be like to be a schoolgirl again with no care in the world other than to learn how to look after my boyfriend.  I love it!  Thank you for doing this for me."
    $ title = "How did she do on her assignment?"
    menu:
        "Well enough to earn a reward (pleasure her)" if terri.pleasure_her_action_used > 0 and terri.pleasure_her_action_used < 3:
            wt_image indy_school_1_14
            if terri.pleasure_her_action_used == 0:
                "[terri.name] staying dry during activities that make most other women get wet is a puzzle.  It could be a medical condition.  Since she seems to be aroused by the schoolgirl-roleplay, this seems like an opportunity to find out."
            else:
                "Since [terri.name] seems to be aroused by the schoolgirl-roleplay, perhaps you'll have better luck getting her to cum on your fingers today than you did the last time you tried."
            wt_image indy_school_1_15
            player.c "You did so well on your assignment, you've won a reward for getting top marks in your class."
            wt_image indy_school_1_16
            "She gasps as you remove her top."
            wt_image indy_school_1_17
            player.c "Does your boyfriend ever reward you for being a good girl?  Touch you between your legs, for example."
            "She blushes."
            terri.c "No, I've never asked him to do that."
            wt_image indy_school_1_18
            player.c "Today you don't need to ask.  As your reward for being such a dutiful schoolgirl, I'm going to play with your breasts and pussy, [terri.name]."
            wt_image indy_school_1_19
            "Her perky nipples stiffen as you pinch and pull on them, but so does [terri.name] herself.  She may have been into the schoolgirl-roleplay, but she's freezing up now."
            wt_image indy_school_1_20
            player.c "Lie back and let yourself relax, [terri.name].  We're going to take our time.  Make yourself comfortable."
            wt_image indy_school_1_21
            "Her sex is barely moist and gentle teasing with your finger tips isn't improving the situation much."
            player.c "Close your eyes, [terri.name], and don't think of anything except how nice it feels to be touched down there."
            wt_image indy_school_1_22
            "After a bit, her sex opens up enough to allow you to slip a finger inside.  She's slowly becoming aroused, but if you expect her to cum today, you'll need to use your mouth."
            $ title = "Start licking her?"
            menu:
                "Yes, try and make her cum with your mouth":
                    wt_image indy_school_1_23
                    "As the tip of your tongue traces her sex, she moans softly."
                    terri.c "ooohh"
                    wt_image indy_school_1_24
                    "Soon your lapping tongue has her juices flowing enough you can say she's actually enjoying this ...."
                    wt_image indy_school_1_25
                    "... until your cheek touches against the side of her thigh.  It was just a light touch of your beard against her skin, yet it was enough to derail her, and she startles upright."
                    player.c "Close your eyes and lie back down again, [terri.name].  Focus on the sensation of my tongue on your sex."
                    wt_image indy_school_1_23
                    "As she lies back, you resume lapping her pussy.  This time, you're careful not to touch her with anything other than your tongue.  Soon, her juices are flowing again.  A short time later her clit begins to push out from underneath its hood."
                    wt_image indy_school_1_24
                    "You flick and tease around and near but never quite against her clit, alternating between light and firm strokes as her hips buck up towards you, trying to increase the pressure."
                    wt_image indy_school_1_23
                    "Eventually you oblige her with a series of hard direct licks that take her over the edge."
                    wt_image indy_school_1_25
                    terri.c "Oooohhhhhh!!!!"
                    wt_image indy_school_1_26
                    "As much as she enjoyed herself, she seems shaken by the experience.  Perhaps she was okay with pleasing another man to become a better girlfriend, but wasn't expecting to receive orgasms from her trainer?"
                    wt_image indy_school_1_27
                    "Whatever it was, she doesn't seem in the mood to chat now.  You can talk to her about what she's thinking at the start of another session."
                    $ terri.pleasure_her_count += 1
                    $ terri.orgasm_count += 1
                    $ terri.pleasure_her_action_used = 3  # this closes the pleasure her action
                    $ terri.orgasm_with_you = 2 # don't know why this is 2 rather than 1, but this opens up a dialogue option
                "No, stop there":
                    wt_image indy_school_1_26
                    terri.c "What you were doing felt nice.  Thank you."
                    wt_image indy_school_1_27
                    "You can't tell if she's trying not to make you feel bad or trying to convince herself.  Either way, despite your best efforts, she doesn't look like a woman who enjoyed herself today."
                    $ terri.pleasure_her_action_used = 2  # changes next scene
        "Very well, praise her":
            wt_image indy_school_1_10
            player.c "You make a wonderful schoolgirl.  Any teacher would be happy to have you for their student."
            wt_image indy_school_1_11
            terri.c "Thank you!  I feel lucky to have you as my teacher."
        "Not well enough (punish her)":
            wt_image indy_school_1_27
            player.c "Unfortunately, [terri.name], I don't think you've learned the lessons I've been trying to teach you near well enough.  Turn around."
            wt_image indy_school_1_28
            player.c "Hopefully this spanking will teach you to take your lessons more seriously in the future, young lady."
            wt_image indy_school_1_29
            "You keep the spanking light enough to be playful, but firm enough to still sting a little."
            wt_image indy_school_1_30
            "*smack*  *smack*  *smack*  *smack*  *smack*"
            wt_image indy_school_1_31
            terri.c "Ow!  I'm sorry I didn't do a better job on my homework.  I promise to be a better student in the future."
            change terri submission by 5 notify
    return

label terri_shaved_sex:
    wt_image indy_shave_1_13
    "She's a little less dry than she usually is.  Either the shaving or the youth-play has aroused her slightly."
    wt_image indy_shave_1_9
    "Still, she's far from wet, and while she clearly wants you to enjoy yourself, she's not really enjoying this herself."
    wt_image indy_shave_1_10
    "Not that that matters, as you're enjoying yourself enough for the both of you."
    wt_image indy_shave_1_12
    player.c "[player.orgasm_text]"
    wt_image indy_shave_1_14
    terri.c "Oh!  You're still cumming"
    wt_image indy_shave_1_8
    terri.c "I hope that felt as good to you as it seemed.  I'm enjoying exploring ways I can look and act younger.  Thank you for encouraging me to do this."
    $ terri.temporary_count = 2 # makes time use only short as little training associated with the shaving
    return

label terri_end_training_session:
    # End Day if Did Anything
    if terri.temporary_count > 0:
        $ terri.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        if terri.temporary_count == 2:
            change player energy by -energy_short notify
        elif terri.temporary_count == 3:
            change player energy by -energy_very_short notify
        else:
            change player energy by -energy_long notify
        $ terri.temporary_count = 0
        end_day
    return

# Have Her Strip For You
label terri_strip:
    $ terri.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    if terri.state == 1:
        wt_image indy_hypno_state_1_1
    elif terri.state == 2:
        wt_image indy_talk_state_2_1
    elif terri.state == 3:
        wt_image indy_hypno_state_3_1
    elif terri.state == 4:
        wt_image indy_hypno_state_4_1
    elif terri.state == 5:
        wt_image indy_talk_state_5_8
    player.c "[terri.name], one of the nicest things a girlfriend can do for her boyfriend is to take her clothes off for him. Slowly and seductively, gradually unveiling her body as he watches. Have you ever stripped for your boyfriend?"
    if terri.state == 1:
        wt_image indy_talk_state_1_1
    elif terri.state == 2:
        wt_image indy_hypno_state_2_2
    elif terri.state == 3:
        wt_image indy_hypno_state_3_5
    elif terri.state == 4:
        wt_image indy_hypno_state_4_5
    elif terri.state == 5:
        wt_image indy_talk_state_5_6
    terri.c "No, I never thought to do that for him."
    player.c "I want you to strip for me."
    if player.teaching_aide_count > 0:
        $ title = "Do you want to use a Teaching Aide with [terri.name]?"
        menu menu_terri_strip:
            "Yes":
                $ current_target = None
                call choose_person_with_tags(tagged_with_any = ['teaching_aide']) from _call_choose_person_with_tags_11
                if current_target is not None and renpy.has_label(current_target.short_name + '_terri_ta_strip'):
                    summon current_target
                    call expression current_target.short_name + '_terri_ta_strip' from _call_expression_28
                    if terri.has_tag('watched_teaching_aide_strip'):
                        $ terri.lesbian_clues += 1
                elif current_target is not None:
                    sys "Missing label: [current_target.short_name]_terri_ta_strip. Choose someone else as content here is not properly defined."
                    $ current_target = terri
                    $ title = "What do you want to do?"
                    jump menu_terri_strip
                if current_target is None:
                    $ current_target = terri
                    $ title = "What do you want to do?"
                    jump menu_terri_strip
            "No":
                pass
    wt_image indy_strip_state_[terri.state]_1
    "[terri.name] stands up and smiles nervously at you."
    wt_image indy_strip_state_[terri.state]_2
    "Slowly, she begins to take off her clothes."
    wt_image indy_strip_state_[terri.state]_3
    "She's actually quite good at this."
    wt_image indy_strip_state_[terri.state]_4
    "She has the perfect mix of awkwardness and earnestness to make her disrobing feel like a very personal gift."
    wt_image indy_strip_state_[terri.state]_5
    "Soon she's naked.  You wonder how many men have seen her like this?  Not many, from what she's told you."
    if terri.has_tag('watched_teaching_aide_strip'):
        if terri.has_tag('ta_strip_bold'):
            wt_image indy_strip_state_[terri.state]_6
            "Remembering what she was shown, [terri.name] finishes with a flourish, opening herself up completely."
        terri.c "Was that any good?  Would my boyfriend enjoy that?"
        "Before you can answer, [current_target.name] jumps in."
        if current_target.has_tag('likes_girls'):
            current_target.c "That was amazing! Your boyfriend would love seeing you do that!! I loved seeing you do that! I am so wet between my legs right now!!"
            if terri.state == 1:
                wt_image indy_strip_state_1_5
            elif terri.state == 2:
                wt_image indy_strip_state_2_10
            elif terri.state == 3:
                wt_image indy_strip_state_3_7
            elif terri.state == 4:
                wt_image indy_strip_state_4_8
            else:
                wt_image indy_strip_state_5_9
            "[terri.name] blushes furiously, unable to respond to [current_target.name]."
        else:
            current_target.c "That was amazing! Your boyfriend would love seeing you do that!!"
            if terri.state == 1:
                wt_image indy_portrait_state_1
            elif terri.state == 2:
                wt_image indy_strip_state_2_11
            elif terri.state == 3:
                wt_image indy_strip_state_3_7
            elif terri.state == 4:
                wt_image indy_hypno_state_4_4
            else:
                wt_image indy_strip_state_5_9
            terri.c "Oh, great!  Thank you!"
        call character_location_return(current_target) from _call_character_location_return_711
        $ current_target = terri
        change terri sos by 10
        change player energy by -energy_short notify
    else:
        terri.c "Was that any good?  Would my boyfriend enjoy that?"
        player.c "Yes, [terri.name], that was excellent. And yes, I think your boyfriend would enjoy that very much."
        if terri.state == 1:
            wt_image indy_portrait_state_1
        elif terri.state == 2:
            wt_image indy_strip_state_2_11
        elif terri.state == 3:
            wt_image indy_strip_state_3_7
        elif terri.state == 4:
            wt_image indy_hypno_state_4_4
        else:
            wt_image indy_strip_state_5_9
        terri.c "Oh, great!  Thank you!"
        change terri sos by 5
        change player energy by -energy_long notify
    #rem tags 'watched_teaching_aide_strip' from terri ## no need to remove
    $ terri.strip_masturbate_dildo_options = 1 ## opens up masturbation action
    end_day
    return

# Have Her Show Off Her Lingerie
label terri_show_off_lingerie:
    $ terri.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    wt_image terri.image
    if terri.has_tag('lingerie_sexy'):
        player.c "Time to show me what you look like in your new lingerie, [terri.name]."
        wt_image current_location.image
        "She ducks into the bathroom."
        wt_image indy_lingerie_1_1
        "A few minutes later she emerges wearing only the skimpy outfit you bought her."
        wt_image indy_lingerie_1_2
        terri.c "What do you think?  Does it fit me well?"
        wt_image indy_lingerie_1_3
        player.c "Modeling lingerie is less about fit, and much more about attitude, [terri.name].  Turn around and let me see what it looks like from behind."
        wt_image indy_lingerie_1_4
        "She looks great, but completely uncertain of herself."
        wt_image indy_lingerie_1_5
        player.c "Show me a sexy look.  You're trying to seduce him, not have him take pity on you."
        wt_image indy_lingerie_1_6
        "She does her best to strike a pose."
        wt_image indy_lingerie_1_7
        player.c "Better.  Try to look a little happier, though.  You want to look like a woman who's looking for sex."
        wt_image indy_lingerie_1_2
        terri.c "I'm not sure I know how to do that."
        wt_image indy_lingerie_1_3
        player.c "If you're not feeling it or are nervous, you can always just start taking the lingerie off in front of him."
        wt_image indy_lingerie_1_8
        terri.c "What's the point of putting on lingerie for my boyfriend, if I'm just going to take it off?"
        wt_image indy_lingerie_1_9
        player.c "Trust me, [terri.name].  As much as he'll enjoy seeing you wearing the lingerie, he'll enjoy seeing you taking it off just as much."
        wt_image indy_lingerie_1_10
        player.c "That's a good start, but remember what I said before about looking happy?"
        wt_image indy_lingerie_1_11
        "She forces a smile onto her face."
        wt_image indy_lingerie_1_12
        player.c "Better.  Now I want you to convince me that you're so turned on being close to me, you can't wait until we have a chance to fuck."
        if terri.test('submission', 20):
            wt_image indy_lingerie_1_14
            "Submissively, [terri.name] bows her head and spreads her legs."
        else:
            wt_image indy_lingerie_1_13
            "[terri.name] gives her best impression of a sultry look as she spreads her legs."
        player.c "Very good.  Now touch yourself.  Men love when women do that, it's a clear signal you're interested in sex."
        wt_image indy_lingerie_1_15
        player.c "Perfect.  You have his full attention, now you just need to seal the deal.  Show him what you want him to do with you."
        wt_image indy_lingerie_1_16
        "[terri.name] gets on her hands-and-knees and wiggles her bum awkwardly.  She looks more nervous than turned on, but the display is sexy regardless, and you make sure she knows."
        player.c "Very sexy, [terri.name].  I'm rock hard right now, but you still have your panties on.  Is your boyfriend the type who likes to rip your panties off you?"
        wt_image indy_lingerie_1_17
        terri.c "Not really.  Sometimes he takes them off me before we have sex, but not forcefully.  He doesn't rip them."
        wt_image indy_lingerie_1_18
        player.c "Then I suggest you take them off yourself, slow and sexy while he's watching, so he knows how much you want him between your legs."
        if terri.test('submission', 20):
            wt_image indy_lingerie_1_20
            "Head bowed, [terri.name] pulls off the last of her lingerie ..."
        else:
            wt_image indy_lingerie_1_19
            "[terri.name] pulls off the last of her lingerie ..."
        wt_image indy_lingerie_1_21
        "... and turns back around."
        player.c "Perfect, [terri.name].  You've done a great job of teasing with your lingerie and signaling how much you want to have sex.  Sometimes, though, despite your best efforts, he's just not going to be in the mood."
        wt_image indy_lingerie_1_22
        terri.c "I'd be okay with that.  I'm doing this for him, I don't want to force myself on him."
        wt_image indy_lingerie_1_23
        player.c "It's okay to be disappointed, especially if you really are in the mood for sex.  If your goal is to make him happy, though, then you should let him continue to look at your body.  Even if doesn't want sex right now, he'll enjoy that.  Or maybe he does have sex with you, he'll still enjoy looking at you afterwards.  Practice showing your body off for me, [terri.name]."
        if terri.test('submission', 20):
            wt_image indy_lingerie_1_25
        else:
            wt_image indy_lingerie_1_24
        terri.c "Should I put the lingerie back on?"
        player.c "Only if he asks you to.  The general rule to making your man happy is to gradually take clothes off around him, not to cover yourself up.  Make yourself comfortable, we're going to practice you exposing yourself, so it feels natural."
        if terri.test('submission', 20):
            wt_image indy_lingerie_1_27
        else:
            wt_image indy_lingerie_1_26
        terri.c "Thank you for helping me.  I would never have been brave enough to try this on my own.  I can see how wearing lingerie around the house and displaying myself like this would make me a better girlfriend."
    elif terri.has_tag('lingerie_cheerleader'):
        player.c "Time to show me what you look like in your new cheerleader outfit, [terri.name]."
        wt_image current_location.image
        "She ducks into the bathroom."
        wt_image indy_cheerleader_1_1
        "A few minutes later she emerges, a hesitant smile on her face."
        terri.c "What do you think?  Do I look ridiculous?"
        player.c "Not at all.  It looks perfect on you.  Were you a cheerleader in school?"
        wt_image indy_cheerleader_1_10
        terri.c "No.  I always wanted to be, but I wasn't good-looking enough or popular enough to be invited to the squad."
        wt_image indy_cheerleader_1_2
        player.c "You're absolutely good-looking enough. Turn around and show off how you look.  Are you wearing the whole outfit, panties too?"
        "She laughs, then bends over to show you."
        wt_image indy_cheerleader_1_3
        terri.c "Of course!"
        player.c "No bra, though.  That's not part of the outfit."
        wt_image indy_cheerleader_1_4
        terri.c "Well, it wasn't part of the outfit you gave me, but I guess you know I'm not big enough to need one."
        "Her nipples are erect, a rarity for her in your experience.  She's getting off on the cheerleader fantasy."
        wt_image indy_cheerleader_1_11
        player.c "Take the top right off.  I'm sure your boyfriend will prefer his cheerleader topless.  Then show me your best cheerleader moves."
        if terri.test('submission', 20):
            wt_image indy_cheerleader_1_6
            "Submissively, [terri.name] drops to her knees in front of you."
            terri.c "I don't really know any real cheerleader moves.  Maybe I could just ask him what he wants to see me do?"
            player.c "In that case, stand up and take your skirt and panties off.  Everyone enjoys seeing a cheerleader undress."
        else:
            wt_image indy_cheerleader_1_5
            terri.c "I don't really know any cheerleader moves.  Do you think I could do something else to entertain him?"
            wt_image indy_cheerleader_1_12
            player.c "How about you take your skirt and panties off. Everyone enjoys seeing a cheerleader undress."
        wt_image indy_cheerleader_1_13
        terri.c "Okay, but I'm not going to look much like a cheerleader after I take the skirt off."
        wt_image indy_cheerleader_1_7
        player.c "You'll look exactly like a cheerleader, a naked cheerleader, once you pick up your pom poms."
        wt_image indy_cheerleader_1_8
        terri.c "Should I shake them?"
        player.c "You can shake anything you want in that position, [terri.name]."
        wt_image indy_cheerleader_1_14
        "She laughs and gives you a sexy, full-body wiggle."
        terri.c "Are you sure I'm not too old to be pretending to be a cheerleader?  My boyfriend's not going to think I'm foolish or immature, is he?"
        player.c "Does it feel good, being a cheerleader, [terri.name]?"
        wt_image indy_cheerleader_1_9
        "She nods."
        player.c "Then I want you to be a cheerleader.  Wear the outfit around the house whenever the mood strikes you.  Being happy will help make you a better girlfriend."
        wt_image indy_cheerleader_1_15
        terri.c "Thank you!"
        $ terri.youth_interest += 1
        sys "[terri.name] is now more interested in acting young."
        $ terri.cheerleader_outfit_visit = 1
    change terri sos by 10
    change terri resistance by -5
    $ terri.lingerie_action_used = 2 ## closes this action
    change player energy by -energy_long notify
    end_day
    return

# Pleasure Her
label terri_pleasure_her:
    if terri.pleasure_her_action_used == 1:
        $ terri.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        wt_image indy_drink_1_2
        "[terri.name] staying dry during activities that make most other women get wet is a puzzle.  It could be a medical condition.  You decide to focus on her pleasure for this session to see if you can learn more."
        player.c "[terri.name], I'd like you to relax for today's session, because today we're going to focus on you.  Do you drink?"
        terri.c "Sometimes"
        wt_image indy_drink_1_4
        "The drink has enough sweetness in it to mask how strong it is.  After a couple of sips, the alcohol is already hitting her."
        terri.c "What did you mean by focus on me today?"
        player.c "I mean instead of working on how to please your boyfriend, we spend some time letting you enjoy sex."
        wt_image indy_drink_1_3
        terri.c "I enjoy pleasing my boyfriend."
        player.c "I know.  Does he please you back very often?  Touch you between your legs, for example."
        wt_image indy_drink_1_7
        "She blushes."
        terri.c "No, I've never asked him to do that."
        wt_image indy_drink_1_6
        player.c "Today you don't need to ask.  I'm going to touch your pussy, [terri.name].  Your job is to lie back and enjoy it.  Consider it the low-stress part of your training.  Take your hand away and spread your legs."
        wt_image indy_drink_1_10
        "Her sex is dry and gentle teasing with your finger tips isn't improving the situation much."
        player.c "Lie back and let yourself relax, [terri.name].  We're going to take our time.  Make yourself comfortable."
        wt_image indy_drink_1_11
        "After a bit, her sex opens up enough to allow you to slip a finger inside."
        player.c "Close your eyes, [terri.name], and don't think of anything except how nice it feels to be touched down there."
        wt_image indy_drink_1_12
        "She's slowly becoming aroused, but if you expect her to cum today, you'll need to use your mouth."
        $ title = "Start licking her?"
        menu:
            "Yes, try and make her cum with your mouth":
                wt_image indy_drink_1_13
                "As the tip of your tongue traces her sex, she moans softly."
                terri.c "ooohh"
                wt_image indy_drink_1_14
                "Soon your lapping tongue has her juices flowing enough you can say she's actually enjoying this ...."
                wt_image indy_drink_1_15
                "... until your cheek touches against the side of her thigh."
                wt_image indy_drink_1_16
                "It was just a light touch of your beard against her skin, yet it was enough to derail her, and she startles upright."
                wt_image indy_drink_1_17
                player.c "Close your eyes and lie back down again, [terri.name].  Focus on the sensation of my tongue on your sex."
                wt_image indy_drink_1_14
                "As she lies back, you resume lapping her pussy.  This time, you're careful not to touch her with anything other than your tongue.  Soon, her juices are flowing again.  A short time later her clit begins to push out from underneath its hood."
                wt_image indy_drink_1_18
                "You flick and tease around and near but never quite against her clit, alternating between light and firm strokes as her hips buck up towards you, trying to increase the pressure."
                wt_image indy_drink_1_13
                "Eventually you oblige her with a series of hard direct licks that take her over the edge."
                wt_image indy_drink_1_17
                terri.c "Oooohhhhhh!!!!"
                wt_image indy_drink_1_16
                "As much as she enjoyed herself, she seems shaken by the experience.  Perhaps she was okay with pleasing another man to become a better girlfriend, but wasn't expecting to receive orgasms from her trainer?"
                wt_image indy_drink_1_7
                "Whatever it was, she doesn't seem in the mood to chat now.  You can talk to her about what she's thinking at the start of another session."
                $ terri.pleasure_her_count += 1
                $ terri.orgasm_count += 1
                $ terri.pleasure_her_action_used = 3  # this closes this action
                $ terri.orgasm_with_you = 2 # don't know why this is 2 rather than 1, but this opens up a dialogue option
            "No, stop there":
                wt_image indy_drink_1_7
                terri.c "What you were doing felt nice.  Thank you."
                "You can't tell if she's trying not to make you feel bad or trying to convince herself.  Either way, despite your best efforts, she doesn't look like a woman who enjoyed herself today."
                $ terri.pleasure_her_action_used = 2  # changes next scene
        change player energy by -energy_short notify
        end_day
    elif terri.pleasure_her_action_used == 2:
        $ title = "Are you ready to eat her out?"
        menu:
            "Yes":
                $ terri.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
                wt_image indy_pleasure_state_1_2
                "You lead [terri.name] to the bed and undress her.  She offers no resistance as you spread her legs, but she's still nervous."
                wt_image indy_pleasure_state_1_1
                "Gently you stroke the tips of your fingers along her sex, trying to warm her up."
                player.c "We're going to focus on you again today, [terri.name].  Remember what I told you last time, close your eyes and let yourself relax."
                wt_image indy_pleasure_state_1_7
                "She shuts her eyes, but bites her lip nervously as you continue to caress her sex with your fingertips."
                $ title = "Lick her anus?"
                menu:
                    "No, focus to her pussy":
                        wt_image indy_pleasure_state_1_3
                        "You stick with the more vanilla approach of warming her up by licking along her labia.  [terri.name] bites nervously on her finger as you trace the tip of your tongue along her sex, but after a few minutes you can smell and taste the early signs of her becoming aroused."
                    "Yes, put your tongue in her butt":
                        wt_image indy_pleasure_state_1_8
                        if terri.has_item(butt_plug):
                            "Her cute, little rosebud has been sufficiently trained by the butt plug you bought her that you can work your tongue inside it without any difficulty.  This doesn't seem to be helping her relax, though."
                        elif terri.anal_count > 0:
                            "Compared to taking your cock, it's a lot easier for her to relax enough for you to work your tongue into her cute, little rosebud.  This doesn't seem to be helping her relax, though."
                        else:
                            "Her cute little rosebud is so tight, it's difficult to work your tongue inside it.  [terri.name] waits patiently as you try, but this doesn't seem to be helping her relax."
                        wt_image indy_pleasure_state_1_3
                        "You switch to the more vanilla approach of warming her up by licking along her labia.  [terri.name] bites nervously on her finger as you trace the tip of your tongue along her sex, but after a few minutes you can smell and taste the early signs of her becoming aroused."
                wt_image indy_pleasure_state_1_5
                "Soon your lapping tongue has her juices flowing enough you can say she's actually enjoying this ...."
                wt_image indy_pleasure_state_1_4
                "... until your cheek touches against the side of her thigh."
                wt_image indy_pleasure_state_1_9
                "It was just a light touch of your beard against her skin, yet it was enough to derail her, and she startles upright."
                wt_image indy_pleasure_state_1_2
                player.c "Close your eyes and lie back down again, [terri.name].  Focus on the sensation of my tongue on your sex."
                wt_image indy_pleasure_state_1_10
                "As she lies back, you resume lapping her pussy.  This time, you're careful not to touch her with anything other than your tongue.  Soon, her juices are flowing again."
                wt_image indy_pleasure_state_1_11
                "A short time later her nipples stiffen and her clit begins to push out from underneath its hood.  You flick and tease around and near but never quite against her clit, alternating between light and firm strokes as her hips buck up towards you, trying to increase the pressure."
                wt_image indy_pleasure_state_1_5
                "Eventually you oblige her with a series of hard direct licks that take her over the edge."
                wt_image indy_pleasure_state_1_6
                "Her eyes roll back in her head as she groans to a climax."
                terri.c "Oooohhhhhh!!!!"
                wt_image indy_pleasure_state_1_4
                "As much as she enjoyed herself, she seems shaken by the experience.  Perhaps she was okay with pleasing another man to become a better girlfriend, but wasn't expecting to receive orgasms from her trainer?"
                wt_image indy_pleasure_state_1_1
                "Whatever it was, she doesn't seem in the mood to chat now.  You can talk to her about what she's thinking at the start of another session."
                $ terri.pleasure_her_count += 1
                $ terri.orgasm_count += 1
                $ terri.pleasure_her_action_used = 3  # this closes this action
                $ terri.orgasm_with_you = 2 # don't know why this is 2 rather than 1, but this opens up a dialogue option
                change player energy by -energy_short notify
                end_day
            "No":
                "Fingering her again is likely to be a waste of time.  You'll need to try using your mouth on her if you want to try and make her cum."
    return

# Have Her Masturbate For You
label terri_masturbate_for_you:
    if terri.state == 1:
        wt_image indy_hypno_state_1_1
    elif terri.state == 2:
        wt_image indy_hypno_state_2_2
    elif terri.state == 3:
        wt_image indy_talk_state_3_8
    elif terri.state == 4:
        wt_image indy_portrait_state_4
    else:
        wt_image indy_talk_state_5_8
    player.c "[terri.name], one of the things men enjoy is watching women become sexually excited.  Have you ever masturbated while your boyfriend watches?"
    if terri.state == 1:
        wt_image indy_talk_state_1_3
    elif terri.state == 2:
        wt_image indy_talk_state_2_1
    elif terri.state == 3:
        wt_image indy_talk_state_3_7
    elif terri.state == 4:
        wt_image indy_talk_state_4_11
    else:
        wt_image indy_talk_state_5_3
    terri.c "No, never.  I don't think I could do that."
    player.c "Why not?"
    if terri.state == 1:
        wt_image indy_talk_state_1_1
    elif terri.state == 2:
        wt_image indy_talk_state_2_5
    elif terri.state == 3:
        wt_image indy_talk_state_3_9
    elif terri.state == 4:
        wt_image indy_talk_state_4_4
    else:
        wt_image indy_talk_state_5_6
    terri.c "I wouldn't be able to.  Not with someone watching me."
    $ title = "What do you do?"
    menu:
        "Insist that she masturbate":
            if terri.state == 1:
                wt_image indy_strip_state_1_8
            elif terri.state == 2:
                wt_image indy_strip_state_2_7
            elif terri.state == 3:
                wt_image indy_strip_state_3_12
            elif terri.state == 4:
                wt_image indy_strip_state_4_7
            else:
                wt_image indy_strip_state_5_3
            player.c "[terri.name], you came to me to learn how to please your boyfriend.  I'm telling you that this is something you should learn how to do, in order to please him.  Take your clothes off so I can see your genitals."
            if terri.state == 1:
                wt_image indy_strip_state_1_13
            elif terri.state == 2:
                wt_image indy_strip_state_2_5
            elif terri.state == 3:
                wt_image indy_strip_state_3_5
            elif terri.state == 4:
                wt_image indy_strip_state_4_4
            else:
                wt_image indy_strip_state_5_5
            player.c "Now put on a show for me.  Touch yourself and let me see you getting aroused."
            if terri.test('submission', 30):
                if terri.state == 1:
                    wt_image indy_strip_state_1_14
                elif terri.state == 2:
                    wt_image indy_strip_state_2_6
                elif terri.state == 3:
                    wt_image indy_strip_state_3_6
                elif terri.state == 4:
                    wt_image indy_strip_state_4_10
                else:
                    wt_image indy_strip_state_5_6
                "She's clearly uncomfortable with the idea, but she's also become submissive enough to you to try.  Tentatively, she opens herself up while you watch.  Then she freezes."
                if terri.state == 1:
                    wt_image indy_strip_state_1_12
                elif terri.state == 2:
                    wt_image indy_strip_state_2_4
                elif terri.state == 3:
                    wt_image indy_strip_state_3_8
                elif terri.state == 4:
                    wt_image indy_strip_state_4_8
                else:
                    wt_image indy_strip_state_5_4
                terri.c "I'm sorry, I can't.  I know I should be obedient and try hard to please my boyfriend, but I think we need to find some other ways for me to please him.  I'm just not comfortable with this."
            else:
                if terri.state == 1:
                    wt_image indy_strip_state_1_12
                elif terri.state == 2:
                    wt_image indy_strip_state_2_4
                elif terri.state == 3:
                    wt_image indy_strip_state_3_8
                elif terri.state == 4:
                    wt_image indy_strip_state_4_8
                else:
                    wt_image indy_strip_state_5_4
                terri.c "I'm sorry, I can't.  I know I should try hard to please him, but I think we need to find some other ways for me to please him.  I'm just not comfortable with this."
            if terri.state == 1:
                wt_image indy_strip_state_1_11
            elif terri.state == 2:
                wt_image indy_strip_state_2_8
            elif terri.state == 3:
                wt_image indy_strip_state_3_11
            elif terri.state == 4:
                wt_image indy_strip_state_4_13
            else:
                wt_image indy_strip_state_5_7
            "She pulls her clothes back on."
            player.c "Why not, [terri.name]?  You're okay with him seeing your body.  Why get uncomfortable about him seeing you aroused?"
            if terri.state == 1:
                wt_image indy_hypno_state_1_1
            elif terri.state == 2:
                wt_image indy_hypno_state_2_3
            elif terri.state == 3:
                wt_image indy_hypno_state_3_5
            elif terri.state == 4:
                wt_image indy_talk_state_4_4
            else:
                wt_image indy_hypno_state_5_1
            terri.c "I don't know.  It just doesn't seem right, getting aroused by a woman's fingers, even if they're my fingers.  I don't want my boyfriend seeing that."
            $ terri.lesbian_clues += 1
        "Drop the subject":
            player.c "Okay, [terri.name]. We'll do something else this session."
        "You might be able to approach this subject from a different angle.  Perhaps a dildo could be of use."
    $ terri.strip_masturbate_dildo_options = 2 ## shuts off masturbation and opens up dildo
    return

# Have Her Dildo Herself
label terri_dildo_herself:
    if terri.has_item(dildo):
        $ terri.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
        player.c "[terri.name], I'd like you to practice your sex skills on the dildo I gave you."
        if terri.state == 1 or terri.state == 2:
            wt_image indy_dildo_state_1_8
            "Nervously, she removes her clothes."
            wt_image indy_dildo_state_1_9
            player.c "Don't be shy.  Put your dildo inside you.  You're going to practice fucking it like it was a real cock."
            wt_image indy_dildo_state_1_1
            "She's not wet, and struggles to get the dildo inside."
            wt_image indy_dildo_state_1_10
            player.c "It may help if you touch yourself first, [terri.name].  Use your fingers on yourself and think sexy thoughts."
            wt_image indy_dildo_state_1_2
            player.c "When you feel yourself getting wet, put the dildo back in."
            wt_image indy_dildo_state_1_3
            "She does, but the expression on her face makes it clear that if she's wet, she's barely wet."
            wt_image indy_dildo_state_1_11
            player.c "Roll over on your back.  That's the position you and your boyfriend usually fuck in, isn't it?"
            wt_image indy_dildo_state_1_12
            "She nods and re-positions herself ..."
            wt_image indy_dildo_state_1_13
            "... but doesn't seem to be enjoying herself any more like this."
            wt_image indy_dildo_state_1_4
            player.c "Close your eyes and relax, [terri.name].  Stop thinking about anything other than sexy thoughts and the feeling of the dildo moving in and out of you."
            wt_image indy_dildo_state_1_14
            "It takes a while, but after she closes her eyes, she eventually does relax."
            wt_image indy_dildo_state_1_5
            "Amazingly, in time, you can see the tension ease out of her body and the dildo move more easily in and out of her.  You want to instruct her further, explaining how she should be fucking her fake cock, but if you speak you may ruin the spell.  So you just watch, as silently she fucks herself, soft sounds barely escaping her lips, seemingly lost in her own head."
            wt_image indy_dildo_state_1_6
            "She continues like that for some time.  Then almost without warning her legs tremble and her breathing becomes louder.  She slams the dildo into herself more vigorously once, twice, three times, and then groans."
            terri.c "Oooohhhhhhhh!!"
            wt_image indy_dildo_state_1_15
            "So she can cum from fucking, when she's in the proper mindset.  The question is, what was she thinking about to get her into that mindset?"
            player.c "Did you enjoy that?"
            wt_image indy_dildo_state_1_7
            terri.c "Mmmmm, yes.  Did I do it right?"
            wt_image indy_dildo_state_1_16
            player.c "I would have to say 'yes'. Your boyfriend would definitely enjoy that."
            "She seems happy with herself, which is what you want her to feel heading home.  There will be plenty of time to ask her questions at the start of your next session.  For now, let her bask in the glow of a job well done."
            $ terri.orgasm_with_dildo = 1
        elif terri.state >= 3:
            terri.c "I'm just quickly going to change, first."
            wt_image current_location.image
            "She disappears for a few minutes, then reappears wearing a school outfit she's clearly outgrown."
            wt_image indy_dildo_state_3_5
            terri.c "I haven't thought about using a dildo since I was in school.  I didn't dare try to get one then, of course.  When you bought one for me, though, I remembered the thoughts I used to have back then.  Can you believe, I'm still nervous about the thought of actually using it, though?"
            wt_image indy_dildo_state_3_6
            player.c "There's no need to be nervous, but you should be naked.  We're going to use the dildo to practice sex, and most of the time you'll be naked during sex."
            wt_image indy_dildo_state_3_7
            player.c "You don't wear glasses anymore."
            wt_image indy_dildo_state_3_8
            terri.c "I had surgery to correct my vision."
            wt_image indy_dildo_state_3_9
            $ title = "Suggest surgery to correct another problem?"
            menu:
                "No":
                    wt_image indy_dildo_state_3_10
                    "Her little breasts look nice, and besides, [terri.name] has enough issues as it is.  No need to add self-consciousness about her breast size to the list."
                "Yes, breast augmentation":
                    wt_image indy_dildo_state_3_10
                    player.c "You know, you could deal with that physical deficiency through surgery, too."
                    wt_image indy_dildo_state_3_11
                    terri.c "I like the size of my breasts.  I always thought they suit me."
                    player.c "It's not what you like, it's what men like.  You're making it harder on yourself to try pleasing a boyfriend with a flat chest."
                    wt_image indy_dildo_state_3_12
                    if terri.boobjob_interest == 0:
                        terri.c "I hadn't thought about it like that."
                        player.c "That's why you hired me, to teach you things you don't know."
                    else:
                        terri.c "My boyfriend says he likes my breasts just the way they are, but I suppose he might just be saying that to not hurt my feelings."
                        player.c "That's why you hired me, to tell you the truth about what boyfriends want."
                    $ terri.boobjob_interest += 1
                    sys "[terri.name] is now more self-conscious about the size of her breasts."
            wt_image indy_dildo_state_3_13
            "She keeps her school skirt on, but nervously pulls off her panties and sits naked in front of you."
            wt_image indy_dildo_state_3_14
            player.c "As a schoolgirl, did you practice giving blowjobs on a dildo?"
            terri.c "No.  I didn't have one, remember?  And I would have been too nervous to ask a girlfriend to borrow hers."
            wt_image indy_dildo_state_3_15
            player.c "No wonder you need so many lessons now.  We're going to practice fucking, not blowjobs today, but you can still get the dildo wet with your mouth before you put it inside you."
            wt_image indy_dildo_state_3_16
            "Her awkward approach to wetting the dildo with her mouth confirms she still needs help with blowjobs, too, but that's for another day."
            player.c "Okay, I guess that will do.  Put it inside you now and practice fucking it like it was a real cock."
            wt_image indy_dildo_state_3_17
            "She takes her glasses off as she psyches herself up for this next step."
            wt_image indy_dildo_state_3_1
            "Even with a bit of saliva on the sextoy, she's not wet between her legs, and struggles to get the dildo inside."
            wt_image indy_dildo_state_3_18
            player.c "It may help if you touch yourself first, [terri.name].  Use your fingers on yourself and think sexy thoughts.  When you feel yourself getting wet, put the dildo back in."
            wt_image indy_dildo_state_3_19
            "She plays with herself for a few minutes ..."
            wt_image indy_dildo_state_3_2
            "... then tries again."
            wt_image indy_dildo_state_3_20
            "If she's wet now, she's barely wet, and she can barely get the dildo inside her, let alone move it freely."
            wt_image indy_dildo_state_3_21
            player.c "Roll over on your back, [terri.name].  That's the position you and your boyfriend usually fuck in, isn't it?"
            wt_image indy_dildo_state_3_3
            "She nods and re-positions herself."
            wt_image indy_dildo_state_3_22
            player.c "Close your eyes and relax, [terri.name]. Stop thinking about anything other than sexy thoughts and the feeling of the dildo moving in and out of you."
            wt_image indy_dildo_state_3_23
            "It takes a while, but after she closes her eyes, she eventually does relax."
            wt_image indy_dildo_state_3_24
            "Amazingly, in time, you can see the tension ease out of her body and the dildo move more easily in and out of her.  You want to instruct her further, explaining how she should be fucking her fake cock, but if you speak you may ruin the spell.  So you just watch, as silently she fucks herself, soft sounds barely escaping her lips, seemingly lost in her own head."
            wt_image indy_dildo_state_3_25
            "She continues like that for some time.  Then almost without warning her legs tremble and her breathing becomes louder.  She slams the dildo into herself more vigorously once, twice, three times, and then groans."
            wt_image indy_dildo_state_3_26
            terri.c "Oooohhhhhhhh!!"
            wt_image indy_dildo_state_3_27
            "So she can cum from fucking, when she's in the proper mindset.  The question is, what was she thinking about to get her into that mindset?"
            player.c "Did you enjoy that?"
            wt_image indy_dildo_state_3_4
            terri.c "Mmmmm, yes.  Did I do it right?"
            wt_image indy_dildo_state_3_17
            player.c "I would have to say 'yes'. Your boyfriend would definitely enjoy that."
            wt_image indy_dildo_state_3_28
            "She seems happy with herself, which is what you want her to feel heading home.  There will be plenty of time to ask her questions at the start of your next session.  For now, let her bask in the glow of a job well done."
            $ terri.orgasm_with_dildo = 2
        $ terri.masturbation_count += 1
        $ terri.orgasm_count += 1
        $ terri.strip_masturbate_dildo_options = 3 ## shuts off this action
        change terri sos by 10
        change player energy by -energy_long notify
        end_day
    else:
        "You need to gift a dildo to [terri.name] first."
    return

### Post-Training Character Actions
## Adult Baby Actions
# Adult Baby Bring Her a Bottle
label terri_bottle:
    wt_image indy_crib_2
    player.c "Here, baby girl. I brought you a fresh bottle of warm milk."
    wt_image indy_crib_3
    "She must have been thirsty."
    wt_image indy_crib_4
    "She gathers her favorite stuffed animal into her arms and sits contentedly, finishing her bottle."
    if terri.maintain_week_baby < week + 4:
        $ terri.maintain_week_baby = week + 4
    wt_image current_location.image
    return

# Adult Baby Bring Her a Toy
label terri_toy:
    $ terri.adult_baby_toy_outfit += 1
    if terri.adult_baby_toy_outfit > 2:
        $ terri.adult_baby_toy_outfit = 1
    if terri.adult_baby_toy_outfit == 1:
        wt_image indy_crib_6
        "[terri.name] looks a little sad sitting in her crib."
        wt_image indy_crib_7
        "You spot her favorite plush toy lying on the floor beside her crib, pick it up, and pass it to her.  Her bright eyes shine as you hand the toy to her.  She reaches out to take it from you and hugs it tight."
        player.c "Did baby girl lose Piggly Wiggly?  Here you are, baby girl.  Here's Piggly Wiggly."
        wt_image indy_crib_8
        terri.c "Goo goo, ga ga!!"
        "She clutches the toy and rocks herself back and forth.  It takes so little to make her happy."
    if terri.adult_baby_toy_outfit == 2:
        wt_image indy_pool_1_12
        player.c "Baby girl, would you like to play with your ball in the splash pool?"
        wt_image indy_pool_1_13
        "That smile means yes."
        call forced_movement(garage) from _call_forced_movement_996
        summon terri
        wt_image indy_pool_1_20
        "Her eyes light up when you give her the ball to play with as you fill the pool."
        wt_image indy_pool_1_21
        "She splashes and plays happily for a while ..."
        wt_image indy_pool_1_14
        "... then decides her top is getting in the way."
        wt_image indy_pool_1_15
        "She resumes playing topless for a bit ..."
        wt_image indy_pool_1_16
        "... then she decides the bottoms have to go, too."
        wt_image indy_pool_1_17
        "Maybe she figures you'd prefer watching her play this way ..."
        wt_image indy_pool_1_18
        "... or maybe, like lots of babies, she thinks clothes are better for chewing on than wearing."
        wt_image indy_pool_1_19
        "Either way, she spends as much time playing with her swimsuit as she does playing with her ball, until it's time for you to take her out and put her back in her crib."
        change player energy by -energy_very_short notify
        call forced_movement(bedroom) from _call_forced_movement_997
        call character_location_return(terri) from _call_character_location_return_712
    if terri.maintain_week_baby < week + 4:
        $ terri.maintain_week_baby = week + 4
    wt_image current_location.image
    return

# Adult Baby Let Her Crawl Around
label terri_crawl:
    $ terri.adult_baby_crawl_outfit += 1
    if terri.adult_baby_crawl_outfit > 2:
        $ terri.adult_baby_crawl_outfit = 1
    if terri.adult_baby_crawl_outfit == 1:
        wt_image indy_crib_5
        "[terri.name] peers at you from over the top of her crib as you approach."
        wt_image indy_crib_9
        player.c "Time for some play time, baby girl."
        wt_image indy_diaper_37
        "You lay out a sheet and set her down on it ..."
        wt_image indy_diaper_5
        "... and watch as she happily crawls around ..."
        wt_image indy_diaper_5
        "... back and forth."
        wt_image indy_diaper_8
        "When she tires, you give her a rattle ..."
        wt_image indy_diaper_38
        "... which she plays happily with while sucking on her soother."
    elif terri.adult_baby_crawl_outfit == 2:
        wt_image indy_baby_crawl_1_1
        "As you set [terri.name] down on a sheet to let her crawl around, she wriggles out of her diaper ..."
        wt_image indy_baby_crawl_1_2
        "... and starts racing around bare-bummed ..."
        wt_image indy_baby_crawl_1_3
        "... giggling as she does so, because she knows she's being naughty."
        wt_image indy_baby_crawl_1_4
        "After a bit, she calms down and starts rolling around."
        if terri.has_tag('no_toe_sucking'):
            wt_image indy_baby_crawl_1_8
            "She's in a silly mood, but despite the lack of a diaper, she avoids making a mess on the sheets ..."
            wt_image indy_baby_crawl_1_9
            "... and she seems to greatly enjoy having your attention while she crawls around and plays."
        else:
            wt_image indy_baby_crawl_1_5
            "As she does so, she notices her toes ..."
            wt_image indy_baby_crawl_1_6
            "... and starts sucking on them."
            wt_image indy_baby_crawl_1_7
            $ title = "What do you do?"
            menu:
                "Watch her":
                    wt_image indy_baby_crawl_1_13
                    "Encouraged by your attention, [terri.name] licks ..."
                    wt_image indy_baby_crawl_1_14
                    "... and sucks on her own toes ..."
                    wt_image indy_baby_crawl_1_15
                    "... taking each of them into her mouth in turn ..."
                    wt_image indy_baby_crawl_1_16
                    "... then two ..."
                    wt_image indy_baby_crawl_1_17
                    "... and three at a time ..."
                    wt_image indy_baby_crawl_1_18
                    "... until her feet are slick with her own drool."
                    wt_image indy_baby_crawl_1_19
                    $ title = "What next?"
                    menu menu_terri_baby_toe_sucking_menu:
                        "Suck on her toes":
                            wt_image indy_baby_crawl_1_1
                            "[terri.name] giggles ..."
                            wt_image indy_baby_crawl_1_21
                            "... and extends her feet towards you ..."
                            wt_image indy_baby_crawl_1_22
                            "... letting you lick, taste and nibble on her delectable little toes until your cock is rock hard."
                            wt_image indy_baby_crawl_1_19
                            jump menu_terri_baby_toe_sucking_menu
                        "Fuck her feet":
                            wt_image indy_baby_crawl_1_23
                            "[terri.name] coos with happiness as you expose your erection ..."
                            wt_image indy_baby_crawl_1_24
                            "... and wrap her soft feet around it."
                            wt_image indy_baby_crawl_1_25
                            "Her soles are slick with saliva as you pump your cock back and forth between them ..."
                            wt_image indy_baby_crawl_1_26
                            "... until her sexy feet have you ready to cum."
                            wt_image indy_baby_crawl_1_27
                            $ title= "Where do you want to cum?"
                            menu:
                                "In her mouth":
                                    wt_image indy_baby_crawl_1_28
                                    "Your baby girl is flexible enough that she can do that without even taking her feet off your cock."
                                    wt_image indy_baby_crawl_1_29
                                    player.c "[player.orgasm_text]"
                                    wt_image indy_baby_crawl_1_30
                                    "Pleased with herself for having pleased you, she swallows your load ..."
                                    wt_image indy_baby_crawl_1_3
                                    "... then plays quietly by herself until you put her back in her crib."
                                    $ terri.swallow_count += 1
                                "On her soles":
                                    wt_image indy_baby_crawl_1_31
                                    "As you turn [terri.name] over, she reaches back with her feet ..."
                                    wt_image indy_baby_crawl_1_32
                                    "... and pumps your cock until you coat her soles with jizz."
                                    wt_image indy_baby_crawl_1_33
                                    player.c "[player.orgasm_text]"
                                    wt_image indy_baby_crawl_1_34
                                    "Pleased with herself for having pleased you, she licks your cum off the soles of her feet ..."
                                    wt_image indy_baby_crawl_1_9
                                    "... then plays quietly by herself until you put her back in her crib."
                            $ terri.footjob_count += 1
                            orgasm notify
                            $ terri.training_session()
                        "Leave her to her fun":
                            wt_image indy_baby_crawl_1_12
                            "[terri.name] smiles at you as you leave ..."
                            wt_image indy_baby_crawl_1_3
                            "... then goes back to playing quietly by herself until you put her back in her crib."
                "Leave her to her fun":
                    wt_image indy_baby_crawl_1_12
                    "[terri.name] smiles at you as you leave ..."
                    wt_image indy_baby_crawl_1_3
                    "... then goes back to playing quietly by herself until you put her back in her crib."
                "Tell her to stop (shuts off content)":
                    add tags 'no_toe_sucking' to terri
                    wt_image indy_baby_crawl_1_10
                    player.c "No putting your feet in your mouth.  That's dirty and I don't want to see that, understand?"
                    wt_image indy_baby_crawl_1_11
                    "She nods ..."
                    wt_image indy_baby_crawl_1_3
                    "... then goes back to playing, this time keeping her toes out of her mouth."
    if terri.maintain_week_baby < week + 4:
        $ terri.maintain_week_baby = week + 4
    wt_image current_location.image
    return

# Adult Baby Daddy Has Needs Too
label terri_daddy_needs:
    if terri.adult_baby_outfit == 0:
        wt_image indy_pigtails_1_22
        "[terri.name] is happy to go without sex.  Her new role as an adult baby seems to satisfy her in a way sex never did.  She understands, however, that you have needs, and she never objects to looking after them."
    $ terri.adult_baby_outfit += 1
    if terri.adult_baby_outfit > 2:
        $ terri.adult_baby_outfit = 1
    if terri.adult_baby_outfit == 1:
        wt_image indy_pigtails_1_21
        player.c "Time for you to be a big girl for [terri.your_daddy_name]."
        wt_image indy_pigtails_1_1
        $ title = "What do you want?"
        menu:
            "Blow job":
                wt_image indy_pigtails_1_2
                "[terri.name] happily sucks on your dick, but she's never become a truly talented cocksucker."
                wt_image indy_pigtails_1_7
                "She's devoted and attentive, but no matter how often you try to instruct her, there's something about having your penis in her mouth that throws her off."
                wt_image indy_pigtails_1_4
                "In fact, while she'd never admit it, you're pretty sure she gets through the blow jobs by pretending that your cock is her bottle ..."
                wt_image indy_pigtails_1_5
                "... which she works hard to extract the warm milk from."
                player.c "[player.orgasm_text]"
                wt_image indy_pigtails_1_6
                terri.c "mmmm"
                $ terri.blowjob_count += 1
                $ terri.swallow_count += 1
            "Sex":
                wt_image indy_pigtails_1_22
                "[terri.name]'s never learned to enjoy sex."
                wt_image indy_pigtails_1_8
                "With baby play beforehand, she sometimes gets a little wet, but usually you need to use lube."
                wt_image indy_pigtails_1_9
                "Still, she'll willingly get into position to let you satisfy your needs."
                $ title = "How do you want to fuck her?"
                menu:
                    "From behind":
                        wt_image indy_pigtails_1_10
                        "She's warm and tight and beautiful ..."
                        wt_image indy_pigtails_1_11
                        "... and even if she doesn't enjoy the fucking ..."
                        wt_image indy_pigtails_1_12
                        "... she waits patiently as you pound away at her ..."
                        wt_image indy_pigtails_1_13
                        "... until you're finished enjoying yourself."
                        player.c "[player.orgasm_text]"
                    "On her back":
                        wt_image indy_pigtails_1_14
                        "She's warm and tight and beautiful ..."
                        wt_image indy_pigtails_1_3
                        "... and even if she doesn't enjoy the fucking ..."
                        wt_image indy_pigtails_1_15
                        "... she waits patiently as you pound away at her ..."
                        wt_image indy_pigtails_1_16
                        "... until you're finished enjoying yourself."
                        player.c "[player.orgasm_text]"
                    "Her on top":
                        wt_image indy_pigtails_1_17
                        "She's warm and tight and beautiful ..."
                        wt_image indy_pigtails_1_18
                        "... and even if she doesn't enjoy the fucking ..."
                        wt_image indy_pigtails_1_19
                        "... she waits patiently as you bounce her up and down on your cock ..."
                        wt_image indy_pigtails_1_20
                        "... until you're finished enjoying yourself."
                        player.c "[player.orgasm_text]"
                $ terri.sex_count += 1
    elif terri.adult_baby_outfit == 2:
        wt_image indy_pigtails_2_1
        player.c "Time for you to be a big girl for [terri.your_daddy_name]."
        $ title = "What do you want?"
        menu:
            "Blow job":
                wt_image indy_pigtails_2_2
                "Your dick isn't [terri.name]'s favorite thing to put in her mouth."
                wt_image indy_pigtails_2_3
                "She'd rather be sucking on her bottle. Or a lolly, when you let her have one for a treat."
                wt_image indy_pigtails_2_4
                "Still, she loves her [terri.your_daddy_name] and wants him to be happy."
                wt_image indy_pigtails_2_5
                "And besides, your load feels a lot like nice warm milk going down."
                player.c "[player.orgasm_text]"
                $ terri.blowjob_count += 1
                $ terri.swallow_count += 1
            "Fuck her from behind":
                wt_image indy_pigtails_2_6
                "You don't want to hurt your baby girl ..."
                wt_image indy_pigtails_2_7
                "... so you lube her up well ..."
                wt_image indy_pigtails_2_8
                "... before pushing yourself inside her."
                terri.c "Oh!"
                wt_image indy_pigtails_2_9
                "Still, you're quite big and she's quite small ..."
                wt_image indy_pigtails_2_10
                "... and it comes as a relief to her when you finish thrusting ..."
                wt_image indy_pigtails_2_11
                "... and empty your load on her pert little upturned butt."
                player.c "[player.orgasm_text]"
                wt_image indy_pigtails_2_12
                "Now you have to decide whether to put her back in her diaper like this, or clean her up first?"
                $ terri.sex_count += 1
            "Fuck her on her back":
                wt_image indy_pigtails_2_13
                "You don't want to hurt your baby girl, so you lube her up well ..."
                wt_image indy_pigtails_2_14
                "... before pushing yourself inside her."
                terri.c "Oh!"
                wt_image indy_pigtails_2_15
                "Still, you're quite big and she's quite small, and it comes as a relief to her when you finish thrusting ..."
                wt_image indy_pigtails_2_16
                "... and empty your load inside her."
                player.c "[player.orgasm_text]"
                wt_image indy_pigtails_2_17
                "She's going to be a drippy mess in a bit.  Fortunately she'll have her diaper back on by then, to keep her from leaking your cum all over her crib."
                $ terri.sex_count += 1
            "Put her on top of you":
                wt_image indy_pigtails_2_18
                "You lube your baby girl up, then lift her up ..."
                wt_image indy_pigtails_2_19
                "... and lower her onto your shaft."
                $ title = "Fuck her like this?"
                menu:
                    "Yes":
                        wt_image indy_pigtails_2_20
                        "Your baby girl is pretty small, and it's easy to bounce her up and down on your dick ..."
                        wt_image indy_pigtails_2_21
                        "... until you fill her insides with your sticky goo."
                    "No, turn her around":
                        wt_image indy_pigtails_2_22
                        "You spin [terri.name] around ..."
                        wt_image indy_pigtails_2_23
                        "... and play with her barely-there itty bitty tits ..."
                        wt_image indy_pigtails_2_24
                        "... as she rides your pole ..."
                        wt_image indy_pigtails_2_25
                        "... until you fill her insides with your sticky goo."
                player.c "[player.orgasm_text]"
                $ terri.sex_count += 1
    orgasm notify
    if terri.maintain_week_baby < week + 2:
        $ terri.maintain_week_baby = week + 2
    $ terri.training_session()
    wt_image current_location.image
    return

# Adult Baby Check Her Diaper
label terri_diaper:
    add tags 'diaper_checked_today' to terri
    if terri.diaper_play_preference == 0:
        wt_image indy_diaper_1
        player.c "Time for [terri.your_daddy_name] to check your diaper, baby girl."
        "[terri.name]'s face glows for a moment with a combination of contentment, embarrassment, and arousal.  Then she gets serious."
        wt_image indy_diaper_34
        terri.c "Um, [terri.your_daddy_name]?"
        player.c "Yes?"
        terri.c "Would you want the type of baby girl who knows how to go potty?"
        $ title = "What do you tell her?"
        menu:
            "Yes, clean diapers only":
                player.c "Yes. I expect you to keep your diaper clean, baby girl."
                wt_image indy_diaper_1
                terri.c "Okay, [terri.your_daddy_name]."
                wt_image indy_diaper_5
                "She turns around and presents her diaper to you."
                player.c "Very good, a nice clean diaper on my baby girl."
                $ terri.diaper_play_preference = 1
            "Pee is okay":
                player.c "Sometimes baby girls can't hold their pee."
                terri.c "Only their pee, [terri.your_daddy_name]?"
                player.c "Yes"
                wt_image indy_diaper_1
                terri.c "Okay"
                wt_image indy_diaper_5
                "She turns around and presents her diaper to you."
                player.c "Very good, a nice clean diaper on my baby girl."
                "You know it won't always be this clean in the future."
                $ terri.diaper_play_preference = 2
            "Babies don't know how to go potty":
                player.c "Don't be silly. Babies don't know how to go potty."
                wt_image indy_diaper_1
                "She blushes a deep red."
                wt_image indy_diaper_5
                "As if to hide her embarrassment, she turns around and presents her diaper for your inspection."
                player.c "Very good, a nice clean diaper on my baby girl."
                "She's breathing heavily and you know she's contemplating whether she could ever let her diaper be anything other than clean. You don't know for sure if she'll be able to take that step, but her rock hard nipples suggest the idea has triggered a strong response in her."
                $ terri.diaper_play_preference = 3
    else:
        $ terri.diaper_outfit_count += 1
        if terri.diaper_outfit_count > 6:
            $ terri.diaper_outfit_count = 1
        if terri.diaper_outfit_count == 1:
            player.c "Time for [terri.your_daddy_name] to check your diaper."
            if terri.diaper_play_preference > 1:
                wt_image indy_diaper_10
                "Somebody's gone pee pee in her pants, but it's not leaking."
                $ title = "Change her?"
            else:
                wt_image indy_diaper_9
                player.c "Nice and clean!  What a good girl."
                "[terri.name] beams contentedly."
                $ title = "Change her anyway?"
            menu:
                "Change her diaper":
                    wt_image indy_diaper_11
                    player.c "Let's get you changed."
                    player.c "Off with the old diaper."
                    wt_image indy_diaper_12
                    player.c "Give you a wipe."
                    wt_image indy_diaper_13
                    player.c "And add some baby powder."
                    wt_image indy_diaper_10
                    player.c "There.  A nice fresh diaper for my baby girl."
                    "[terri.name] sighs contentedly."
                "Leave this one on her":
                    player.c "This diaper's still good for a while. [terri.your_daddy_name] doesn't have to change you now."
        elif terri.diaper_outfit_count == 2:
            if terri.diaper_play_preference > 1:
                wt_image indy_diaper_14
                player.c "Time for another diaper check."
                player.c "Uh oh, that's a very full diaper, baby girl. It needs to be changed."
                if terri.diaper_play_preference == 3:
                    wt_image indy_diaper_15
                    player.c "Oops. I see somebody had a little accident in her diaper."
                    "[terri.name] flushes a deep shade of red, but the wetness of her pussy tells you this isn't just embarrassing for her, but also arousing."
                    player.c "It's okay. I know my baby girl isn't big enough to go potty all by herself. Let me wipe you up."
                wt_image indy_diaper_16
                player.c "Your bum is all red. You've been in that dirty diaper too long."
                wt_image indy_diaper_17
                player.c "This clean one will feel better."
                wt_image indy_diaper_18
                player.c "There you go. All fixed up."
                "[terri.name] sighs contentedly."
            else:
                $ terri.diaper_outfit_count = 3
        # back to 'If' on purpose
        if terri.diaper_outfit_count == 3:
            if terri.diaper_play_preference > 1:
                wt_image indy_diaper_19
                player.c "Let's take a quick peek at that diaper, baby girl."
                wt_image indy_diaper_20
                player.c "Hmmm, you've definitely peed in your diaper, baby girl, but it isn't too bad. I don't think we need to waste a diaper changing you just yet."
                "[terri.name]'s unable to suppress a moan as you rub her through her urine soaked nappy."
                terri.c "oooooo"
                player.c "My baby girl likes the feel of the wet diaper against her, doesn't she? Especially when I press it against you."
                "[terri.name]'s too ashamed to answer, but her body trembles sweetly as you take a few extra minutes to 'check' her diaper thoroughly."
            else:
              $ terri.diaper_outfit_count = 4
        # back to 'If' on purpose
        if terri.diaper_outfit_count == 4:
            if terri.diaper_play_preference == 3:
                wt_image indy_diaper_21
                player.c "*sniff*  *sniff* ... I think I smell a poopy."
                wt_image indy_diaper_22
                player.c "Let's get you up on the change table."
                wt_image indy_diaper_23
                player.c "Oh! Baby girl!! You've been playing in your crib with that squishy in your diaper?"
                "A humiliated [terri.name] avoids eye contact with you as you examine the mess she's made of herself."
                wt_image indy_diaper_24
                player.c "[terri.your_daddy_name]'ll get you cleaned up."
                wt_image indy_diaper_25
                player.c "Your bum must be sore from playing in a dirty diaper. Let's put some baby powder on it so it feels better."
                wt_image indy_diaper_26
                player.c "There.  There's a nice clean ... Baby girl!  Did you just pee in your clean diaper??"
                "[terri.name] blushes a deeper shade of red."
                player.c "Okay, let's start over again."
            else:
                $ terri.diaper_outfit_count = 5
        # back to 'If' on purpose
        if terri.diaper_outfit_count == 5:
            if terri.diaper_play_preference > 1:
                wt_image indy_diaper_27
                "You're about to check on [terri.name] when you notice she's brought her laptop into her crib. There must be some work she needs to get done, as she's deeply engrossed in it."
                $ title = "Stay or leave?"
                menu:
                    "Wait for her to finish":
                        wt_image indy_diaper_28
                        "As you're watching, she starts shifting her hips. Before long, her bum is twitching more and more insistently."
                        wt_image indy_diaper_29
                        "With a soft sigh, she lifts her hips. You can see the diaper expand as she releases the contents of her bladder into it."
                        if terri.diaper_play_preference == 3:
                            "Her hips, however, haven't stopped twitching."
                            $ title = "Keep watching?"
                            menu:
                                "Yes, keep watching her":
                                    wt_image indy_diaper_30
                                    "With a barely audible grunt, she arches her back."
                                    wt_image indy_diaper_31
                                    "You're going to have a mess to clean up later, but for now your baby girl has big girl work she needs to finish up. Since a poopy diaper doesn't seem to be preventing her from getting that work done, you step away to leave her alone. Baby play can wait."
                                "Go on with your day":
                                    pass
                        else:
                            "It looks like she still has some more work to do. You step away to leave her alone. Baby play can wait."
                    "Go on with your day":
                        pass
            else:
                $ terri.diaper_outfit_count = 6
        # back to 'If' on purpose
        if terri.diaper_outfit_count == 6:
            wt_image indy_diaper_32
            player.c "Let's take a quick peek at that diaper, baby girl.  Wow, perfectly clean.  No need to change that diaper.  Good girl!"
            "[terri.name] beams happily."
    if terri.maintain_week_baby < 4:
        $ terri.maintain_week_baby = week + 4
    wt_image current_location.image
    return

# Adult Baby Give Her a Bath:
label terri_bath:
    wt_image indy_bath_1_1
    player.c "Time for a bath, baby girl."
    wt_image indy_bath_1_2
    terri.c "Ducky?"
    wt_image indy_bath_1_13
    player.c "Yes, you can play with your ducky in the bath, but let me get those shoes off you and test the water temperature, first."
    wt_image indy_bath_1_14
    player.c "Okay, you and ducky can get in the water, now.  I'll help you in so you don't fall."
    wt_image indy_bath_1_3
    "[terri.name] loves being treated as a baby and having your hands all over her as you turn and bathe every part of her."
    wt_image indy_bath_1_5
    "How much she enjoys it is obvious when you tell her to finish cleaning herself up.  Her body responds to being treated like an infant in a way it never did when she was treated as a woman."
    wt_image indy_bath_1_4
    terri.c "Ohhhh!!!"
    $ title = "Your turn now?"
    menu:
        "No, bath time's over":
            wt_image indy_bath_1_6
            player.c "Bath time's over, baby girl.  Did you and ducky enjoy your bath?"
            wt_image indy_bath_1_7
            "She nods and gives the rubber ducky a squeeze ... *squeak* *squeak*"
            change player energy by -energy_very_short
        "No, but clean her pussy up with your mouth":
            wt_image indy_bath_1_24
            player.c "You left a mess between your legs, baby girl.  Let [terri.your_daddy_name] clean that up for you."
            "The taste of her pussy juice after her orgasm, mixed with the soapy bathwater is unusual but arousing."
            wt_image indy_bath_1_17
            player.c "Now you're all clean.  No touching yourself and making yourself sticky again right after your bath.  Let's get you dried off and into your crib."
            change player energy by -energy_very_short
        "Yes, have her blow you":
            wt_image indy_bath_1_8
            "[terri.name]'s not the only one who enjoyed her bath."
            wt_image indy_bath_1_9
            "She's had her fun ..."
            wt_image indy_bath_1_15
            "... she's not about to deny you yours."
            wt_image indy_bath_1_10
            "She knows it takes more than treating her like a baby to get you off ..."
            wt_image indy_bath_1_11
            "... and she's happy to supply her mouth for that purpose.  Besides, since she's already wet and soapy from her bath ..."
            wt_image indy_bath_1_12
            "... it's easy to clean her up after a facial."
            wt_image indy_bath_1_16
            player.c "[player.orgasm_text]"
            $ terri.blowjob_count += 1
            $ terri.facial_count += 1
            orgasm notify
            $ terri.training_session()
        "Yes, fuck her":
            wt_image indy_bath_1_17
            player.c "I'm glad my baby girl made herself nice and wet between the legs ..."
            wt_image indy_bath_1_18
            player.c "... because I have something big I want to put in here."
            wt_image indy_bath_1_19
            "This isn't her favorite activity, and even after her orgasm you have to go slow so as not to hurt her on entry ..."
            wt_image indy_bath_1_20
            "... but she's a good girl who wants her [terri.your_daddy_name] to be happy, so if fucking her tight pussy makes you happy ..."
            wt_image indy_bath_1_21
            "... she'll wait patiently while you fuck it until you cum."
            wt_image indy_bath_1_22
            player.c "[player.orgasm_text]"
            wt_image indy_bath_1_23
            "You've left a mess on your otherwise clean baby girl, but she doesn't seem to mind.  Bath time is still one of the happiest times of her day."
            if not terri.has_tag('no_bath_sex_clean_up'):
                $ title = "Clean her"
                menu:
                    "Yes, lick your cum off of her":
                        wt_image indy_bath_1_24
                        "[terri.name] would have been just as happy if you'd used a cloth, but the heady taste of her just-fucked pussy and your own sperm is an intoxicating end to bath time for you."
                    "No, not today":
                        pass
                    "Never (shuts off question)":
                        add tags 'no_bath_sex_clean_up' to terri
            $ terri.sex_count += 1
            orgasm notify
            $ terri.training_session()
        "Yes, fuck her ass" if terri.anal_count > 0:
            wt_image indy_anal_1
            "Soapy water doesn't make for a very long-lasting lubricant ..."
            wt_image indy_anal_3
            "... but then you're not going to be inside your baby girl's tight ass for very long ..."
            wt_image indy_anal_12
            "... before you fill it with cum."
            wt_image indy_anal_4
            player.c "[player.orgasm_text]"
            wt_image indy_anal_13
            player.c "You were a very good girl, taking that without complaining.  Was it uncomfortable at all?  Show [terri.your_daddy_name] where it hurts"
            wt_image indy_bath_1_25
            player.c "Right in there it hurts?  Does my baby girl love [terri.your_daddy_name] enough to want to do that for him, even though it hurts?"
            wt_image indy_bath_1_26
            "Of course she does, [terri.name] absolutely adores you.  And once she soothes and cleans her bum in the bath water, she'll be ready to let you put her in her crib and use her again tomorrow."
            $ terri.anal_count += 1
            orgasm notify
            $ terri.training_session()
    if terri.maintain_week_baby < 4:
        $ terri.maintain_week_baby = week + 4
    wt_image current_location.image
    return

# Change your Daddy name
label terri_daddy_name:
    wt_image terri.image
    "[terri.name] currently refers to you as '[terri.your_daddy_name]'."
    $ title = "Change how she should address you?"
    menu:
        "Yes":
            call terri_daddy_name_change from _call_terri_daddy_name_change
        "No":
            pass
    return

label terri_daddy_name_change:
    $ title = "How should she address you?"
    $ terri.your_daddy_name = renpy.input(_("How should she address you?"))
    $ title = "Are you sure you want her to call you '[terri.your_daddy_name]'?"
    menu:
        "Yes":
            pass
        "No, choose something else":
            call terri_daddy_name_change from _call_terri_daddy_name_change_1
    return


## Assistant Actions
# Assistant Train Her
label terri_assistant_training:
    $ terri.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
    $ terri.assistant_training_count += 1
    if terri.assistant_training_count == 1:
        wt_image indy_assistant_1
        terri.c "I've been thinking about what I could use for a focus, and I have this old pendant of my mother's."
        wt_image indy_pendant_1
        terri.c "Do you think this would work?"
        wt_image indy_assistant_1
        player.c "It should. Are you ready to try it out on someone?"
        wt_image indy_assistant_22
        terri.c "Right now? I'm not sure I'm ready."
        player.c "You won't be until you start practicing. Get your coat on. We're going to go find you a suitable subject."
        wt_image indy_assistant_23
        terri.c "Are we going to ask for volunteers?"
        player.c "No.  If you want to be effective as a hypnotist, you're going to need to learn how to put someone under without them knowing."
        wt_image indy_assistant_10
        terri.c "Isn't that unethical?"
        player.c "Not if your goal is to help them. Or in your case, learn how to do this so you can help someone else."
        wt_image indy_assistant_23
        "She nods and goes to get her coat. She may not fully agree with your moral position, but her own self-interest in learning hypnosis overrides any qualms she may have."
        call forced_movement(terri_secluded_park) from _call_forced_movement_187
        wt_image indy_park_1
        "You take [terri.name] to a quiet park.  After a bit of walking around, you spot a woman on her own and approach her."
        wt_image indy_training_hypno_1_4
        terri.c "Look at this and listen to me."
        hypno_training_woman_terri_1 "What?"
        player.c "Excuse my friend. She's a bit nervous. She just wants to ask you a few questions."
        wt_image indy_training_hypno_1_1
        hypno_training_woman_terri_1 "Uh, sure?  About what?"
        wt_image indy_training_hypno_1_2
        terri.c "About this pendant. Please look at it. Look at it and listen to me."
        hypno_training_woman_terri_1 "I've never seen that pendant before. Did you find it here in the park?"
        player.c "Let me jump in, [terri.name]. You just watch for a moment. We just have a few simple questions for you. We won't take up much time, but I need you to look at this for me before we can start."
        call focus_image from _call_focus_image_75
        player.c "Listen to me. Listen to my voice. Only my voice now. My friend wants to talk to you. She's very friendly and just wants to talk. Listen to me and listen to my friend."
        wt_image indy_training_hypno_1_1
        player.c "You want to be comfortable ... wait, no. Best if you keep your top on here in the park. Just relax and listen to my friend. Listen to the sound of her voice.  Try talking to her now, [terri.name]. Ask her some questions and see if you can help her."
        terri.c "Okay.  Are you happy?"
        wt_image indy_training_hypno_1_3
        hypno_training_woman_terri_1 "Sometimes"
        terri.c "Would you like to be happier?"
        hypno_training_woman_terri_1 "Sure"
        terri.c "I want you to listen to me. From now on, you're going to be happy. Happy all the time."
        hypno_training_woman_terri_1 "I am?"
        terri.c "Yes"
        "You let [terri.name] stumble around like this for a bit, then instruct the woman to forget she was hypnotized and bring her out of the trance."
        wt_image indy_training_hypno_1_4
        terri.c "Do you feel happy now?"
        hypno_training_woman_terri_1 "Look, I enjoyed chatting with you, but I have to go now."
        "The woman hurries away and you and [terri.name] return home."
        call forced_movement(terri_the_assistant_room) from _call_forced_movement_188
        wt_image indy_assistant_22
        terri.c "That didn't work, did it?"
        player.c "Even after multiple sessions and breaking down her resistance to your influence, just telling someone to be happy is a tall order."
        wt_image indy_assistant_10
        terri.c "So I need to start with something smaller?"
        player.c "You need to start with where they are and move them in the direction you want them to go."
        wt_image indy_assistant_23
        terri.c "Okay. I'm going to do some more studying. You've given me something concrete to work with. Thank you so much!"
        change player energy by -energy_hypnosis
    elif terri.assistant_training_count == 2:
        wt_image indy_assistant_1
        player.c "[terri.name], it's time to continue your training.  Go put your coat on."
        wt_image indy_assistant_23
        terri.c "Okay. I've been studying. Hopefully I can do better than last time."
        call forced_movement(terri_secluded_park) from _call_forced_movement_189
        wt_image indy_park_1
        "You return to the quiet park and look for a new subject for [terri.name] to practice on. Before long, you pass a young woman who smiles and greets you."
        wt_image indy_training_hypno_2_1
        hypno_training_woman_terri_2 "Hi"
        terri.c "Hi.  Could you look at this for me?"
        wt_image indy_training_hypno_2_2
        hypno_training_woman_terri_2 "What is it?"
        terri.c "It's a pendant."
        player.c "Don't explain, [terri.name]. Just swing the pendant while you talk to her."
        terri.c "Look at this and listen to me. Listen to my voice."
        wt_image indy_training_hypno_2_5
        hypno_training_woman_terri_2 "Is this a magic trick of some type?  Are you like a stage performer or something?"
        terri.c "No, I'm a hypnotist. Well, I'm trying to be."
        wt_image indy_training_hypno_2_1
        hypno_training_woman_terri_2 "So you're a student? I don't think this is working. I'm not sure I can be hypnotized, anyway. I was called up on stage once at school and it didn't work then, either."
        player.c "Do you mind if I help?"
        wt_image indy_training_hypno_2_5
        hypno_training_woman_terri_2 "Will it take long?"
        call focus_image from _call_focus_image_76
        player.c "Not at all. Just watch and listen to my voice. Only my voice now. My friend wants to talk to you. She's very friendly and just wants to talk. Listen to me and listen to my friend."
        wt_image indy_training_hypno_2_5
        player.c "You want to be comfortable while we talk. Remove your top so we can all be comfortable while my friend talks to you."
        wt_image indy_training_hypno_2_3
        terri.c "Umm, what if someone walks by and sees her?"
        player.c "Crap, that's such a habit. Make sure no one can see your breasts except me and my friend. Just relax and be comfortable and listen to my friend. Listen to the sound of her voice."
        wt_image indy_training_hypno_2_4
        terri.c "Should I try to help her now?"
        player.c "Yes, but first you need to find out something about her."
        terri.c "Are you enjoying your walk."
        hypno_training_woman_terri_2 "No"
        terri.c "Why not? It's such a beautiful day."
        hypno_training_woman_terri_2 "I'm sad. I used to take my dog on walks on days like today, before he died. Now I just miss him so much, it hurts."
        terri.c "That's terrible! Don't be sad on days like this. Forget about your dog. From now on, you won't remember your dog when you go for a walk. You'll just enjoy the beautiful day and not think about sad things."
        wt_image indy_training_hypno_2_1
        "When [terri.name]'s finished, you tell the woman to cover up and forget about the hypnosis, then bring her out of the trance."
        terri.c "It's a beautiful day for a walk."
        wt_image indy_training_hypno_2_5
        hypno_training_woman_terri_2 "It is. I wish my dog was still with us. It makes me sad, thinking about how much he would have enjoyed going for a walk on a day like today."
        call forced_movement(terri_the_assistant_room) from _call_forced_movement_190
        wt_image indy_assistant_22
        "A forlorn [terri.name] sadly returns home with you. She almost looks like her dog died, too."
        terri.c "Why didn't that work? I found out why she was sad and addressed it."
        player.c "Intensely held beliefs and feelings can't just be washed away with a single suggestion. Sometimes you need to work around the edges, and adjust your subject's thinking indirectly, not head on."
        wt_image indy_assistant_23
        terri.c "Okay. I'm going to do some more studying. You've given me something concrete to work with. Thank you so much!"
        change player energy by -energy_hypnosis
    elif terri.assistant_training_count == 3:
        wt_image indy_assistant_1
        player.c "[terri.name], it's time to continue your training.  Go put your coat on."
        wt_image indy_assistant_23
        terri.c "Okay. I've been studying. Hopefully I can do better than last time."
        call forced_movement(terri_secluded_park) from _call_forced_movement_191
        wt_image indy_park_1
        "You return to the quiet park and look for a new subject for [terri.name] to practice on. A pretty woman walking by herself in the park looks like a good candidate to be [terri.name]'s next subject."
        wt_image indy_training_hypno_3_1
        player.c "Excuse me. Can my friend ask you a few questions?"
        hypno_training_woman_terri_3 "Whatever you're selling or pushing, I'm not interested."
        terri.c "No, it's not like that. I'm a student. I just need to chat with you a moment. It would help with my studies."
        wt_image indy_training_hypno_3_2
        hypno_training_woman_terri_3 "Oh. In that case, sure. What did you want to ask me?"
        terri.c  "Could you look at this for me?"
        wt_image indy_training_hypno_3_3
        hypno_training_woman_terri_3 "What is that?  Some kind of pendant?"
        wt_image indy_training_hypno_3_4
        terri.c "Just watch.  Watch and listen.  Listen to my voice.  Only the sound of my voice."
        wt_image indy_training_hypno_3_3
        hypno_training_woman_terri_3 "Yeah, I can hear you.  But what did you want to ask me?"
        wt_image indy_training_hypno_3_4
        player.c "More swing with the focus, [terri.name].  And keep talking to her.  Don't pause."
        wt_image indy_training_hypno_3_3
        terri.c "Watch.  Watch and listen.  Listen to my voice.  Only the sound of my voice."
        wt_image indy_training_hypno_3_4
        terri.c "Only my voice now. Let everything slip away except the sound of my voice."
        wt_image indy_training_hypno_3_5
        terri.c "Oh my God!  I think I did it!!"
        player.c "That's great, [terri.name]."
        terri.c "Do I have to tell her to take her top off now?"
        player.c "Only if you want to.  That's sort of just my thing.  It's not necessary."
        terri.c "Okay, I'll skip it for now.  What should I do next?"
        player.c "Talk to her.  Find out about her, anything that may be bothering her.  See if you can help her."
        terri.c "All right, here goes.  Are you enjoying your walk?"
        hypno_training_woman_terri_3 "Not really.  It's boring, walking through this same park all the time."
        terri.c "Why do you come here?  There must be something about the park you like?"
        hypno_training_woman_terri_3 "It's close.  And I like the trees."
        terri.c "The trees are amazing!  The most beautiful you've ever seen.  Walking in this park makes you feel great. You love the trees. You love walking in the park and seeing these trees."
        player.c "That's good, [terri.name].  Now have her forget about the hypnosis before you bring her out of it."
        wt_image indy_training_hypno_3_4
        terri.c "Okay.  I'm going to wake you on the count of 3.  When you wake, you'll remember nothing about what we did here or what we talked about.  You'll only remember that we had a lovely chat, and that you love the trees here and walking in this park.  Do you understand?"
        wt_image indy_training_hypno_3_3
        hypno_training_woman_terri_3 "Yes.  I'll remember nothing about what we did or talked about.  I'll only remember our lovely chat and how much I love the trees and walking in this park."
        wt_image indy_training_hypno_3_4
        terri.c "Good.  1 ... 2 ... 3"
        wt_image indy_training_hypno_3_6
        terri.c "Thanks so much for helping me. I hope you have a great walk."
        wt_image indy_training_hypno_3_2
        hypno_training_woman_terri_3 "How could I not?  The trees here are so amazing!  I always feel great every time I come here."
        call forced_movement(terri_the_assistant_room) from _call_forced_movement_192
        wt_image indy_assistant_24
        "[terri.name]'s giddy with excitement as the two of you return home."
        terri.c "Wow!!!  That was so ... so ..."
        player.c "Arousing?"
        wt_image indy_assistant_25
        terri.c "In a way, yeah!  And empowering!!  Having her mind open to me like that.  And the best part is, I really helped her!!  She was bored of her walks, but I helped her be happy with her lot in life."
        wt_image indy_assistant_1
        terri.c "Can anyone learn to do that? Open other people's minds like that?"
        player.c "No. You have a special talent for it, [terri.name]."
        wt_image indy_assistant_24
        terri.c "I've never been special at anything.  Not in a good way, anyway.  Thank you so much for introducing me to this!"
    elif terri.assistant_training_count == 4:
        wt_image indy_assistant_1
        player.c "[terri.name], it's time to continue your training."
        wt_image indy_assistant_25
        terri.c "Oh good!  I can't wait for us to find another subject to practice on."
        player.c "Do you prefer a man or a woman, this time?"
        wt_image indy_assistant_10
        terri.c "How about another woman?  I think you have more experience with them, right?"
        call forced_movement(terri_quiet_coffee_shop) from _call_forced_movement_193
        wt_image indy_coffee_shop_1
        "You forego the park this time, to avoid listening to another tale of why some lonely woman isn't enjoying her walk. This coffee shop is quiet, and you can run interference for [terri.name] if someone tries to interrupt her."
        wt_image indy_training_hypno_4_1
        player.c "Are these seats taken?"
        hypno_training_woman_terri_4 "Uh, no.  But there are plenty of empty tables."
        terri.c "We just wanted to talk to you."
        wt_image indy_training_hypno_4_2
        hypno_training_woman_terri_4 "About what?"
        terri.c "Take a look at this ..."
        player.c "Hold on,  [terri.name].  Things will go a lot easier if you let her get comfortable talking to you first."
        terri.c "Oh, Okay.  I'm studying women and what keeps them from being happy."
        wt_image indy_training_hypno_4_1
        hypno_training_woman_terri_4 "That sounds interesting. How can I help?"
        terri.c "I was hoping to ask you some questions. Is that alright?"
        wt_image indy_training_hypno_4_2
        hypno_training_woman_terri_4 "Sure, but I only have a few minutes before I need to go."
        terri.c "This won't take long.  Please look at this for me ..."
        wt_image indy_training_hypno_4_3
        terri.c "Look and listen.  Listen to my voice.  Only the sound of my voice.  Only the sound of my voice, now."
        wt_image indy_training_hypno_4_4
        terri.c "Oh, wow!!  It worked again!  That's so ... so ..."
        player.c "'Arousing' is the word you're looking for, [terri.name]."
        "She ignores you and starts questioning her subject. There's nothing interesting about the woman's relationship problems or [terri.name]'s hamfisted attempts to solve them ..."
        wt_image indy_assistant_25
        "... but watching [terri.name]'s obvious enjoyment at exercising control over the entranced woman is very interesting."
        wt_image indy_training_hypno_4_4
        terri.c "You're going to forget you were hypnotized and wake on the count of 3.  1 ... 2 ... 3."
        wt_image indy_training_hypno_4_1
        hypno_training_woman_terri_4 "Thanks for talking to me.  I really enjoyed our chat!  Good luck with your study.  I hope my answers to your questions helped."
        call forced_movement(terri_the_assistant_room) from _call_forced_movement_194
        wt_image indy_assistant_22
        terri.c "Did I do okay today?  I couldn't tell from her reaction afterwards if I was able to help her or not?"
        player.c "It takes time for hypnotic suggestions to work their full impact. It'll be next week before the full impact of your influence will have taken hold."
        wt_image indy_assistant_24
        terri.c "So my suggestions are still influencing her brain right now, even though she's no longer hypnotized?"
        player.c "That turns you on, doesn't it?"
        wt_image indy_assistant_27
        terri.c "Maybe a little?  Thanks again for teaching me how to do this."
    elif terri.assistant_training_count == 5:
        wt_image indy_assistant_1
        player.c "[terri.name], it's time to continue your training."
        wt_image indy_assistant_23
        terri.c "Oh good. Let's go find a suitable woman to work on."
        player.c "Did you want to try finding a guy for a change?"
        wt_image indy_assistant_10
        terri.c "I'm really more interested in helping women, so I think it makes sense for me to practice with one."
        call forced_movement(terri_quiet_coffee_shop) from _call_forced_movement_195
        wt_image indy_coffee_shop_1
        "This coffee shop is as quiet as ever.  If [terri.name] was hoping for a follow-up session with her previous subject, she's out of luck, as the woman is nowhere to be seen."
        wt_image indy_training_hypno_5_1
        "A new subject, however, is sitting quietly by herself, reading a book."
        wt_image indy_training_hypno_5_2
        "It takes little help from you for [terri.name] to gain the woman's confidence and then put her under.  She's getting the hang of this."
        wt_image indy_assistant_25
        "The unhappiness in this woman's life is no more interesting than [terri.name]'s previous subject, but that doesn't seem to diminish [terri.name]'s evident enjoyment of the experience"
        wt_image indy_training_hypno_5_3
        "While you make sure no one interrupts, [terri.name]] keeps the woman under, exploring deeper and deeper into the root causes of her life choices, until [terri.name] hits a wall, and nearly collapses from exhaustion."
        wt_image indy_training_hypno_5_4
        "You step in and send the confused woman home, after releasing her from [terri.name]'s trance as best you can.  Then you get [terri.name] back to your place."
        call forced_movement(terri_the_assistant_room) from _call_forced_movement_196
        wt_image indy_assistant_10
        terri.c "What happened?  I've never felt so tired in my life.  Did I pass out?"
        player.c "Almost.  You kept at it too long.  It was too much for your subject, and for you.  You need to pace yourself, and focus each session on making just one change to her thinking."
        wt_image indy_assistant_24
        terri.c  "Thank you.  I'm learning so much from you! I'm totally exhausted, but ..."
    elif terri.assistant_training_count == 6:
        wt_image indy_assistant_1
        player.c "[terri.name], it's time to continue your training."
        wt_image indy_assistant_23
        terri.c "Great!  I'm definitely going to pace myself this time, and focus on just making one change in my subject."
        call forced_movement(terri_quiet_coffee_shop) from _call_forced_movement_197
        wt_image indy_coffee_shop_1
        "A trip back to the quiet coffee shop offers a safe location for [terri.name] to practice, but little choice in the way of subjects today."
        wt_image indy_training_hypno_6_1
        "The only one sitting by herself is a sullen looking young woman who hasn't even bought a coffee to justify taking up a seat."
        wt_image indy_training_hypno_6_2
        "To [terri.name]'s credit, despite the woman's initial instructions to 'fuck off', she eventually gets her under."
        wt_image indy_training_hypno_6_3
        "It's a good thing [terri.name]'s aware of limiting herself today, as this woman's issues could fill a binder.  In the end, [terri.name] simply instructs her to speak up when her boyfriend does something to her she doesn't like."
        call forced_movement(terri_the_assistant_room) from _call_forced_movement_198
        wt_image indy_assistant_10
        terri.c "I see what you mean about pacing yourself. I could've been there all day trying to help her.  I hope I picked the best thing to change to help her be happy."
        player.c "Some people don't know themselves well enough to know what will make them happy.  That woman will speak up more now, but only about the things she thinks she wants."
        wt_image indy_assistant_1
        terri.c "So sometimes the best thing I can do is help the woman understand who she is and what she really wants?"
        player.c "And then if you don't like who she is, you can change her."
        wt_image indy_assistant_24
        terri.c "And get rid of the things that are wrong about her!!  That makes so much sense.  Thank you for teaching me so much!"
    elif terri.assistant_training_count == 7:
        wt_image indy_assistant_1
        player.c "[terri.name], it's time to continue your training."
        wt_image indy_assistant_23
        terri.c "Great!  This time I'm going to get my subject to open up about who she really is."
        call forced_movement(outdoors) from _call_forced_movement_199
        wt_image indy_store_front_1
        "Not wanting to get a reputation at the coffee shop, you look for a new locale.  A boutique home decor store should be a low traffic location."
        wt_image indy_training_hypno_7_1
        "As you suspected, the store clerk's all alone in the store, and naturally inclined to want to please potential client [terri.name]."
        wt_image indy_training_hypno_7_2
        "While you watch the door, [terri.name] easily puts the woman under with little preamble. Then [terri.name] sets in on getting the woman to open up and be honest about who she is and what she wants."
        wt_image indy_assistant_25
        "Despite [terri.name]'s enthusiasm, the woman's a reticent subject, and [terri.name] makes little headway."
        wt_image indy_training_hypno_7_1
        "Eventually, a disappointed [terri.name] gives up, while an equally disappointed store clerk tries to remain positive despite not making a sale."
        call forced_movement(terri_the_assistant_room) from _call_forced_movement_200
        wt_image indy_assistant_22
        terri.c "That was harder than I expected. I couldn't get her to answer honestly, no matter how hard I tried.  She kept citing platitudes, but never anything truly real about herself."
        player.c "Even hypnotized, your subject's reaction is going to be based on how much she trusts you.  Breaking down her resistance to your influence is key if you want to make deep changes."
        wt_image indy_assistant_1
        terri.c "That makes sense.  I'd better spend more time learning how to do that.  Thanks so much for the advice! Before I get back to studying, though ..."
    elif terri.assistant_training_count == 8:
        wt_image indy_assistant_1
        player.c "[terri.name], it's time to continue your training."
        wt_image indy_assistant_23
        terri.c "Great!  I remember what you told me about how I need to break down my subject's resistance before she'll truly open up to me.  I'm going to practice that today."
        call forced_movement(outdoors) from _call_forced_movement_201
        wt_image indy_training_hypno_8_1
        "You haven't yet decided where to take [terri.name], when she notices a woman jogging by."
        wt_image indy_training_hypno_8_2
        "The woman just wants to finish her jog, but [terri.name]'s determined to turn her into her new subject, and before long, [terri.name]'s will wins."
        wt_image indy_assistant_25
        "Then [terri.name] goes to work, convincing the woman that she's her soul mate, the confidante to whom she can confess her innermost thoughts."
        wt_image indy_training_hypno_8_3
        "[terri.name] tries to take her so far, so fast, you're sure it will never work. Then you see the woman's resolve start to waver ..."
        wt_image indy_training_hypno_8_4
        "... and she embraces the idea of [terri.name] as her mentor and advisor, hanging on your assistant's every word."
        wt_image indy_training_hypno_8_5
        "Even after [terri.name] releases her from the trance, her influence on the woman is clear."
        hypno_training_woman_terri_8 "Oh my God!  We have to get together for coffee tomorrow.  I have so many secrets to tell you!!  I can't wait to get your advice."
        call forced_movement(terri_the_assistant_room) from _call_forced_movement_202
        wt_image indy_assistant_10
        terri.c "I think I broke her resistance down, just like you told me to."
        player.c "I think you did, too. That was quite impressive. Once you had her open to your suggestions, were you tempted to have her do anything for you, before you let her go?"
        wt_image indy_assistant_22
        terri.c "Oh, wow ... I was feeling so ... so ..."
        player.c "Turned on?"
        wt_image indy_assistant_24
        terri.c "Yes!  Watching her resistance crumble like that was a real turn on.  But ... well, of course there wasn't anything she could do for me.  She's not a boy."
        wt_image indy_assistant_1
        terri.c "I should be doing something for you, though.  To thank you for teaching me how to do that.  Not just with words, I mean."
    elif terri.assistant_training_count == 9:
        wt_image indy_assistant_1
        player.c "[terri.name], it's time to continue your training."
        wt_image indy_assistant_23
        terri.c "Great!  I think I'm starting to get the hang of this."
        call forced_movement(outdoors) from _call_forced_movement_203
        wt_image indy_shopping_plaza_1
        terri.c "Let's find somebody here."
        player.c "It's a bit busy."
        terri.c "That's okay.  I'll be careful.  I bet there are lots of messed up women here, trying to cover their insecurities with shopping."
        wt_image indy_training_hypno_9_1
        terri.c "Excuse me.  Can I talk with you about your shopping today?"
        hypno_training_woman_terri_9 "Are you doing a product survey or something?"
        terri.c "Not exactly.  I'm looking to set up a business to help women understand what they really want, and it'd be great if I could talk to you about your needs."
        wt_image indy_training_hypno_9_3
        hypno_training_woman_terri_9 "You mean like a personal shopping service?  That's cool, but I could never afford that."
        terri.c "My time today won't cost you anything."
        wt_image indy_training_hypno_9_2
        hypno_training_woman_terri_9 "Okay, then.  What did you want to know?"
        terri.c "Just look at this for me, first."
        wt_image indy_assistant_25
        "[terri.name] takes the woman under, and sets about stripping away her resistance."
        wt_image indy_training_hypno_9_3
        "Soon the woman accepts [terri.name] as an advisor she could never hope to afford, and feels fortunate to have the opportunity to explain her needs to her."
        wt_image indy_training_hypno_9_4
        hypno_training_woman_terri_9 "I'm shopping for a bra.  Again.  I'm always shopping for a bra.  My tits are so tiny and pathetic.  I can't find anything to make them look nice."
        if terri.boobjob_interest > 1:
            terri.c "Your tits are so small, no bra is going to make them interesting to a man, is it?"
            wt_image indy_training_hypno_9_5
            hypno_training_woman_terri_9 "But in the right light, with the right support ..."
            terri.c "They're still tiny tits.  You know that.  It's not a bra you need, it's a boob job."
            wt_image indy_training_hypno_9_9
            hypno_training_woman_terri_9 "But, they're my tits.  I just want guys to find me sexy, the way I am."
            terri.c "They will, after you get your breasts enlarged."
            wt_image indy_training_hypno_9_5
            hypno_training_woman_terri_9 "That'll cost money. I can't afford that."
            terri.c "How much money have you wasted on bras?"
            wt_image indy_training_hypno_9_6
            hypno_training_woman_terri_9 "A lot.  You're right, I'm going to stop wasting money on frivolous things, and save it up for something important.  Making my breasts bigger!"
            wt_image indy_training_hypno_9_7
            "The woman's resolve lasts even after [terri.name] releases her from the trance."
            hypno_training_woman_terri_9 "I want to show you how stupid my tits look right now."
            wt_image indy_training_hypno_9_8
            hypno_training_woman_terri_9 "I hope I get a chance to show them to you again after I've saved my money to fix them with a boob job!"
        else:
            terri.c "Your breasts are beautiful. You don't need anything to make them look nice. They're great the way they are!"
            wt_image indy_training_hypno_9_5
            hypno_training_woman_terri_9 "But if I found the right bra to push them together, they'd look bigger and ..."
            terri.c "You don't really want bigger tits, do you?  If you did, you'd have gotten a boob job."
            wt_image indy_training_hypno_9_9
            hypno_training_woman_terri_9 "No, I don't want bigger breasts.  These are my breasts.  I just want guys to find me sexy, the way I am."
            terri.c "Guys will find you sexy.  Men like breasts no matter what size or shape they are.  You're the one who needs to realize how sexy your breasts are, just like that."
            wt_image indy_training_hypno_9_6
            hypno_training_woman_terri_9 "I want to think that, but everything I hear says that women need big boobs to be sexy."
            terri.c "Is that what your boyfriends have told you?"
            wt_image indy_training_hypno_9_5
            hypno_training_woman_terri_9 "No, but they were probably just being nice."
            terri.c "I'm not your boyfriend, and I think your breasts are super sexy."
            wt_image indy_training_hypno_9_9
            hypno_training_woman_terri_9 "You do?  Really?"
            terri.c "Really. They look like they'd be so nice to touch and squeeze and lick and suckle at ... if I was a guy, of course."
            wt_image indy_training_hypno_9_6
            hypno_training_woman_terri_9 "You're right ..."
            wt_image indy_training_hypno_9_7
            hypno_training_woman_terri_9 "... my tits are beautiful, just like this.  I've always thought it, I just could never let myself truly believe it before now."
            wt_image indy_training_hypno_9_10
            "The woman's new found confidence lasts even after [terri.name] releases her from the trance. And shopping trips in this area just became more interesting."
            hypno_training_woman_terri_9 "I want the whole world to see my tits.  My tiny, sexy, perfectly-me tits.  I've kept them hidden away, ashamed of them, too long.  No more!"
        call forced_movement(terri_the_assistant_room) from _call_forced_movement_204
        wt_image indy_assistant_24
        terri.c "I did it!  I helped her!  I really helped her!!  I can do this. I can fix women who are broken!!  And I have you to thank for that!"
    if terri.assistant_training_count > 2:
        wt_image indy_assistant_2
        terri.c "Did you want me to thank you some more?"
        $ title = "How do you want her to thank you?"
        menu:
            "Sex":
              player.c "Get out of those clothes, and I'll show you how you can thank me."
              wt_image indy_assistant_3
              terri.c "Yes, [terri.your_respect_name]!"
              wt_image indy_assistant_29
              "[terri.name] still requires lube in order to penetrate her easily ..."
              wt_image indy_assistant_7
              "... and even with the lube, it's uncomfortable for her when you're going in."
              wt_image indy_assistant_8
              "When you take her from behind, however, and have her play with her own ass and pussy while you fuck her, she can at least get a little wet."
              wt_image indy_assistant_30
              "It's not enough for her to cum ..."
              wt_image indy_assistant_31
              "... but it makes it easier for you to."
              wt_image indy_assistant_16
              $ title = "Where do you want to cum?"
              menu:
                  "In her pussy":
                      wt_image indy_assistant_17
                      "She struggles to enjoy having your cock inside her, but has no objection to receiving your cum inside her."
                      wt_image indy_assistant_18
                      player.c "[player.orgasm_text]"
                      wt_image indy_assistant_9
                      "She just seems happy knowing she's able to make you happy."
                  "On her pussy":
                      wt_image indy_assistant_32
                      "Flipping her over ..."
                      wt_image indy_assistant_19
                      "... you let her know you want her to finish you off onto her."
                      wt_image indy_assistant_20
                      player.c "[player.orgasm_text]"
                      wt_image indy_assistant_21
                      "She watches with interest as your sperm drips down her, but it's impossible to know what she's thinking, and she won't talk about it."
              $ terri.sex_count += 1
              orgasm
            "Blow Job":
              player.c "A blow job would be nice."
              wt_image indy_assistant_3
              terri.c "Let me get out of these clothes."
              wt_image indy_assistant_4
              "[terri.name] seems happy that you wanted her thanks in the form of her mouth."
              wt_image indy_assistant_11
              "She sees it as recognition of her improving oral skills."
              wt_image indy_assistant_12
              "The reality is that watching [terri.name] hypnotizing that woman turned you on as much if not more than her blow job does.  Regardless, you're soon ready to cum."
              $ title = "Where do you want to cum?"
              menu:
                  "On her face":
                      wt_image indy_assistant_13
                      "Your balls are boiling over, and you don't want to lose this load down her throat.  You pull her off you and put her on her knees."
                      wt_image indy_assistant_6
                      player.c "[player.orgasm_text]"
                      wt_image indy_assistant_14
                      "The pretty upturned face of your assistant receives the evidence of how much you enjoyed her training and her thank you."
                      $ terri.facial_count += 1
                  "Down her throat":
                      wt_image indy_assistant_5
                      "Your balls are boiling over, and her throat seems as good a place as any to empty your load as any."
                      wt_image indy_assistant_28
                      player.c "[player.orgasm_text]"
                      wt_image indy_assistant_15
                      "She chokes slightly, but eventually swallows your demonstration of how much you enjoyed her training and her thank you."
                      $ terri.swallow_count += 1
              $ terri.blowjob_count += 1
              orgasm
            "Words are enough":
              player.c "Words are sufficient, [terri.name]."
              wt_image indy_assistant_26
              terri.c "Okay!  I'm going to go reflect on what I learned today."
    $ terri.assistant_must_train_by_week = week + 5
    call forced_movement(living_room) from _call_forced_movement_205
    wt_image current_location.image
    change player energy by -energy_short notify
    return

## Slavegirl Actions
# Rename Her
label terri_rename:
    wt_image terri.image
    "As her owner, it's your prerogative to change [terri.full_name]'s name, if you want to."
    $ title = "Do you want to change her name?"
    menu:
        "Yes":
            $ title = "What would you like her name to be?"
            $ terri.name = renpy.input(_("What is her new name?"))
            $ terri.suffix = renpy.input(_("What is her new title, if you want to give her one?"))
            $ title = "Does she get a prefix?"
            menu:
                "Yes":
                    $ terri.prefix = renpy.input(_("What is her prefix?"))
                "No":
                    $ terri.prefix = ""
            $ terri.change_full_name(terri.prefix, terri.name, terri.suffix)
            $ title = "Are you sure you want her new name to be [terri.full_name]?"
            menu:
                "Yes":
                    pass
                "No, choose something else":
                    $ terri.change_full_name("", "Terri", "the Good Girlfriend")
                    jump terri_rename
        "No":
            pass
    return

# Tell her how to address you
label terri_your_name:
    wt_image terri.image
    "[terri.name] currently refers to you as '[terri.your_respect_name]'."
    $ title = "Change how she should address you?"
    menu:
        "Yes":
            call terri_your_name_change from _call_terri_your_name_change
        "No":
            pass
    return

label terri_your_name_change:
    $ title = "How should she address you?"
    $ terri.your_respect_name = renpy.input(_("How should she address you?"))
    $ title = "Are you sure you want her to call you '[terri.your_respect_name]'?"
    menu:
        "Yes":
            pass
        "No, choose something else":
            call terri_your_name_change from _call_terri_your_name_change_1
    return

# Hurt Her
label terri_hurt_her:
    $ title = "How do you want to hurt her?"
    menu:
        "Clothespin zipper" if dungeon.has_item(gags):
            wt_image indy_slavegirl_hurt_1_1
            "This only ends one way.  With [terri.name] screaming at the top of her lungs."
            wt_image indy_slavegirl_hurt_1_2
            "With the ball gag in place, the sounds of her screams will be barely tolerable.  Without the gag, the neighbors would have the police here in a moment."
            wt_image indy_slavegirl_hurt_1_3
            "The clothespins sting going on, but that pain is but preamble to the agony of them coming off."
            wt_image indy_slavegirl_hurt_1_4
            "She trembles as she waits, holding the string obediently for you as you fasten each clothespin to increasingly sensitive parts of her body. By the time you fasten a clothespin to her clit, her tears will be welling up in her eyes at the anticipation of what's to come."
            wt_image indy_slavegirl_hurt_1_5
            "You hold her firmly to keep her from falling as you pull the string and rip the clothespins from her skin ... *zzzzzipppppp*"
            wt_image indy_slavegirl_hurt_1_6
            terri.c "NNNNNNNNNNNNNNNNN"
            wt_image indy_slavegirl_hurt_1_5
            player.c "How do you feel, [terri.name]?"
            wt_image indy_slavegirl_hurt_1_1
            terri.c "Happy that I could be of use to you, [terri.your_respect_name].  I hope you enjoyed hurting me."
            change player energy by -energy_very_short notify
        "Electricity and sex":
            wt_image indy_slavegirl_hurt_2_1
            "Setting up electric play is fussy and time-consuming, but can be worth it for [terri.name] ..."
            wt_image indy_slavegirl_hurt_2_2
            "... as the flow of electricity through her genitals affects her body in a way that other pain - and other stimulation - never does ... *zzzzztttttt*"
            wt_image indy_slavegirl_hurt_2_3
            "... causing her labia to swell with blood and her clit to stiffen."
            terri.c "owwww!!  oohhh!"
            wt_image indy_slavegirl_hurt_2_2
            $ title = "What now?"
            menu menu_terri_slavegirl_hurt_electricity:
                "Shock her again":
                    if terri.has_tag('cock_in_mouth_now'):
                        wt_image indy_slavegirl_hurt_2_6
                        "You hold her head and make sure your cock is out of the way of her teeth before you jolt her ... *zzzzztttttt*"
                        wt_image indy_slavegirl_hurt_2_8
                        terri.c "nnnnn!!  nnnnn!"
                        wt_image indy_slavegirl_hurt_2_7
                    elif terri.has_tag('cock_in_cunt_now'):
                        wt_image indy_slavegirl_hurt_2_12
                        "Her body's not actually into being fucked ..."
                        wt_image indy_slavegirl_hurt_2_13
                        "... but the jolts of electricity you send through her makes her body twitch and squirm as if it is ... *zzzzztttttt*"
                        wt_image indy_slavegirl_hurt_2_14
                        if terri.has_tag('came_today'):
                            terri.c "owwww!!"
                        else:
                            terri.c "owwww!!  oohhh!"
                    else:
                        wt_image indy_slavegirl_hurt_2_3
                        "Her pussy spasms and her clit twitches as you send another jolt of electricity through her genitals ... *zzzzztttttt*"
                        terri.c "owwww!!  oohhh!"
                        wt_image indy_slavegirl_hurt_2_2
                    jump menu_terri_slavegirl_hurt_electricity
                "Have her rim you":
                    rem tags 'cock_in_mouth_now' 'cock_in_cunt_now' from terri
                    wt_image indy_slavegirl_hurt_2_4
                    "She sticks her tongue in your butt and starts probing and licking ..."
                    wt_image indy_slavegirl_hurt_2_5
                    "... then her tongue starts twitching inside you when you shock her while she's rimming you ... *zzzzztttttt*"
                    terri.c "nnnnn!!  nnnnn!"
                    jump menu_terri_slavegirl_hurt_electricity
                "Use her mouth" if not terri.has_tag('cock_in_mouth_now'):
                    rem tags 'cock_in_cunt_now' from terri
                    add tags 'cock_in_mouth_now' to terri
                    wt_image indy_slavegirl_hurt_2_6
                    "She's terrible at giving blowjobs, but you can use her mouth to get you hard ..."
                    wt_image indy_slavegirl_hurt_2_7
                    "... while you enjoy the sight of her body twitching as you send electricity coursing through it  ... *zzzzztttttt*"
                    wt_image indy_slavegirl_hurt_2_8
                    terri.c "nnnnn!!  nnnnn!"
                    wt_image indy_slavegirl_hurt_2_7
                    jump menu_terri_slavegirl_hurt_electricity
                "Make her cum" if terri.has_tag('cock_in_cunt_now') and not terri.has_tag('came_today'):
                    add tags 'came_today' to terri
                    wt_image indy_slavegirl_hurt_2_11
                    "Her clit has been so stimulated by the jolts of electricity you've sent coursing through her genitals ..."
                    wt_image indy_slavegirl_hurt_2_15
                    "... that a firm pinch of the engorged nub is sufficient to send an orgasm crashing through her."
                    wt_image indy_slavegirl_hurt_2_14
                    terri.c "Oooohhhhhh!!!!"
                    $ terri.orgasm_count += 1
                    jump menu_terri_slavegirl_hurt_electricity
                "Cum like this" if terri.has_any_tag('cock_in_mouth_now', 'cock_in_cunt_now'):
                    if terri.has_tag('cock_in_mouth_now'):
                        wt_image indy_slavegirl_hurt_2_8
                        "One more shock to her system should take you over the edge ... *zzzzztttttt*"
                        wt_image indy_slavegirl_hurt_2_9
                        terri.c "NNNNNNN"
                        wt_image indy_slavegirl_hurt_2_10
                        player.c "[player.orgasm_text]"
                        wt_image indy_slavegirl_hurt_2_3
                        $ terri.blowjob_count += 1
                        $ terri.swallow_count += 1
                    else:
                        wt_image indy_slavegirl_hurt_2_13
                        "One more shock to her system should take you over the edge ... *zzzzztttttt*"
                        wt_image indy_slavegirl_hurt_2_14
                        if terri.has_tag('came_today'):
                            terri.c "owwww!!"
                        else:
                            terri.c "owwww!!  oohhh!"
                        wt_image indy_slavegirl_hurt_2_12
                        player.c "[player.orgasm_text]"
                        wt_image indy_slavegirl_hurt_2_13
                        $ terri.sex_count += 1
                    if terri.has_tag('came_today'):
                        terri.c "Thank you for making use of me, [terri.your_respect_name].  My whole body feels like it's on fire from the electricity and the orgasm.  I hope my cumming and suffering both pleased you."
                    else:
                        terri.c "Thank you for making use of me, [terri.your_respect_name].  My whole body feels like it's on fire from the electricity.  I hope that pleased you."
                    orgasm notify
                "Fuck her" if not terri.has_tag('cock_in_cunt_now'):
                    rem tags 'cock_in_mouth_now' from terri
                    add tags 'cock_in_cunt_now' to terri
                    wt_image indy_slavegirl_hurt_2_11
                    "It's a nice change to feel [terri.name]'s sex swollen with increased bloodflow as she accepts your cock inside her."
                    wt_image indy_slavegirl_hurt_2_12
                    "She doesn't even involuntarily squirm or try to pull away as you begin to fuck her ..."
                    wt_image indy_slavegirl_hurt_2_13
                    "... although she does squirm and shake as you send another jolt of electricity through her body ... *zzzzztttttt*"
                    wt_image indy_slavegirl_hurt_2_14
                    terri.c "owwww!!  oohhh!"
                    jump menu_terri_slavegirl_hurt_electricity
                "Stop there":
                    wt_image indy_slavegirl_hurt_2_3
                    if terri.has_tag('came_today'):
                        terri.c "My whole body feels like it's on fire from the electricity and the orgasm, [terri.your_respect_name].  I hope my cumming and suffering both pleased you."
                    else:
                        terri.c "My whole body feels like it's on fire from the electricity, [terri.your_respect_name].  I hope that pleased you."
                    change player energy by -energy_very_short notify
            rem tags 'came_today' 'cock_in_mouth_now' 'cock_in_cunt_now' from terri
        "Rough her up":
            $ terri.temporary_count = 0
            wt_image indy_slavegirl_hurt_3_1
            "Growing up, [terri.name] hated the thoughts in her head about receiving gentle touches from soft, feminine hands.  As scared as she is of the pain you're about to inflict, a part of her welcomes being manhandled by rough, masculine hands as a sign that she's rejected her former sickness."
            $ title = "What do you do?"
            menu menu_terri_slavegirl_rough_up:
                "Tell her to humiliate herself while you hurt her" if not terri.has_tag('humiliating_herself_now') and not terri.has_tag('cock_in_mouth_now'):
                    add tags 'humiliating_herself_now' to terri
                    wt_image indy_slavegirl_hurt_3_1
                    terri.c "Yes, [terri.your_respect_name].  Thank you for giving me the opportunity to tell you how pathetic I am."
                    jump menu_terri_slavegirl_rough_up
                "Tell her to shut up" if terri.has_tag('humiliating_herself_now') and not terri.has_tag('cock_in_mouth_now'):
                    rem tags 'humiliating_herself_now' from terri
                    wt_image indy_slavegirl_hurt_3_1
                    "She nods quietly, acknowledging your order."
                    jump menu_terri_slavegirl_rough_up
                "Slap her":
                    rem tags 'cock_in_mouth_now' from terri
                    $ terri.temporary_count += 1
                    wt_image indy_slavegirl_hurt_3_2
                    "You strike her cheek hard with the palm of your hand ... *SLAP*"
                    if terri.has_tag('humiliating_herself_now'):
                        terri.c "Oww!!  I'm sorry, [terri.your_respect_name], for being a worthless slave who deserves to be slapped."
                    else:
                        terri.c "Oww!!"
                    jump menu_terri_slavegirl_rough_up
                "Pull her hair":
                    rem tags 'cock_in_mouth_now' from terri
                    $ terri.temporary_count += 1
                    wt_image indy_slavegirl_hurt_3_3
                    "Wrapping your fingers in her hair, you pull on it until tears form in her eyes."
                    if terri.has_tag('humiliating_herself_now'):
                        terri.c "Oww!!  I'm sorry, [terri.your_respect_name], that I have such ugly red hair."
                    else:
                        terri.c "Oww!!"
                    jump menu_terri_slavegirl_rough_up
                "Squeeze her tit":
                    rem tags 'cock_in_mouth_now' from terri
                    $ terri.temporary_count += 1
                    wt_image indy_slavegirl_hurt_3_4
                    "Taking a firm grip of her tit, you squeeze, twist and pull on the soft flesh as [terri.name] squirms in discomfort."
                    if terri.has_tag('humiliating_herself_now'):
                        terri.c "Oww!!  I'm sorry, [terri.your_respect_name], that I have such tiny breasts."
                    else:
                        terri.c "Oww!!"
                    jump menu_terri_slavegirl_rough_up
                "Spank her ass":
                    rem tags 'cock_in_mouth_now' from terri
                    $ terri.temporary_count += 1
                    wt_image indy_slavegirl_hurt_3_5
                    "Pulling her head down until she's bent over at the waist, you spank her bare butt ... *SMACK*  *SMACK*  *SMACK*"
                    if terri.has_tag('humiliating_herself_now'):
                        terri.c "Oww!!  I'm sorry, [terri.your_respect_name], that I don't have a sexy ass."
                    else:
                        terri.c "Oww!!"
                    jump menu_terri_slavegirl_rough_up
                "Shove your cock in her mouth" if not terri.has_tag('cock_in_mouth_now'):
                    add tags 'cock_in_mouth_now' to terri
                    $ terri.temporary_count += 1
                    wt_image indy_bondage_3
                    "[terri.name] isn't good at giving blowjobs, but this isn't a blowjob.  This is you ramming your cock into her mouth until it hurts her."
                    jump menu_terri_slavegirl_rough_up
                "Cum down her throat" if terri.has_tag('cock_in_mouth_now'):
                    wt_image indy_bondage_4
                    player.c "[player.orgasm_text]"
                    wt_image indy_bondage_2
                    if terri.has_tag('humiliating_herself_now'):
                        "She swallows your load and licks your cock clean before speaking again."
                        wt_image indy_slavegirl_hurt_3_2
                        terri.c "Thank you for finding a way to enjoy the useless mouth of a slavegirl who's too stupid to learn how to suck your cock properly, [terri.your_respect_name]."
                    else:
                        "She silently swallows your load and licks your cock clean before you leave."
                    $ terri.blowjob_count += 1
                    $ terri.swallow_count += 1
                    orgasm notify
                "Cum on her face" if terri.has_tag('cock_in_mouth_now'):
                    wt_image indy_bondage_17
                    player.c "[player.orgasm_text]"
                    if terri.has_tag('humiliating_herself_now'):
                        wt_image indy_bondage_15
                        terri.c "Thank you for making my ugly face prettier with your cum, [terri.your_respect_name]."
                    else:
                        wt_image indy_bondage_14
                        "She silently licks the head of your cock clean before you leave."
                    $ terri.blowjob_count += 1
                    $ terri.facial_count += 1
                    orgasm notify
                "Stop there" if not terri.has_tag('cock_in_mouth_now') and terri.temporary_count > 0:
                    change player energy by -energy_very_short notify
                    $ terri.temporary_count = 0
                "Change your mind" if not terri.has_tag('cock_in_mouth_now') and terri.temporary_count == 0:
                    pass
            rem tags 'cock_in_mouth_now' 'humiliating_herself_now' from terri
        "Change your mind":
            pass
    wt_image current_location.image
    return

# Use Her
label terri_use_her:
    $ terri.temporary_count = 0
    call terri_update_media from _call_terri_update_media
    wt_image terri.image
    $ title = "Where do you want to use her?"
    menu:
        "Mouth out of the cage" if not terri.has_tag('slavegirl_let_out'):
            wt_image indy_slavegirl_bj_3_1
            "You let [terri.full_name] out of her cage and position her at your feet.  She immediately takes your cock into her mouth."
            wt_image indy_slavegirl_bj_3_2
            "Despite your hopes for her, she never became a truly talented cocksucker, but she is good at mindlessly following instructions."
            wt_image indy_slavegirl_bj_3_3
            $ title = "What do you want her to do?"
            $ terri.temporary_count = 0
            menu menu_terri_slavegirl_bj_out_of_cage:
                "Let her do her own thing":
                    $ terri.temporary_count = 1
                    wt_image indy_slavegirl_bj_3_1
                    "She still hasn't grasped how to properly pleasure a cock ..."
                    wt_image indy_slavegirl_bj_3_2
                    "... but she's pretty enough and her mouth is wet enough that you feel your balls tighten anyway as she does her best to blow you."
                    wt_image indy_slavegirl_bj_3_3
                    jump menu_terri_slavegirl_bj_out_of_cage
                "Lick your balls":
                    $ terri.temporary_count = 1
                    wt_image indy_slavegirl_bj_3_6
                    "This she can't mess up.  She takes your balls into her mouth ..."
                    wt_image indy_slavegirl_bj_3_7
                    "... and licks your sack as she strokes your cock."
                    jump menu_terri_slavegirl_bj_out_of_cage
                "Stroke your shaft":
                    $ terri.temporary_count = 1
                    wt_image indy_slavegirl_bj_3_5
                    "Her hand is soft, and if her grip is a little firmer than ideal, it's still hard to mess up a basic handjob, especially with her warm lips wrapped around the head of your cock as she strokes you."
                    wt_image indy_slavegirl_bj_3_3
                    jump menu_terri_slavegirl_bj_out_of_cage
                "Suck the head of your cock":
                    $ terri.temporary_count = 1
                    wt_image indy_slavegirl_bj_3_4
                    "This she can do.  She latches onto the head of your cock and sucks for all she's worth, trying to extract the cum from your balls by pure suction alone."
                    wt_image indy_slavegirl_bj_3_3
                    jump menu_terri_slavegirl_bj_out_of_cage
                "Hold still while you face fuck her":
                    $ terri.temporary_count = 1
                    wt_image indy_slavegirl_bj_3_8
                    "You lean forward to give yourself leverage as you thrust your cock hard and fast between her lips."
                    wt_image indy_slavegirl_bj_3_9
                    "As the force of your thrusts increase, she needs to put her hands back behind her head to hold herself steady and prevent you from cracking her skull open on the cage bars as you fuck her mouth-hole."
                    jump menu_terri_slavegirl_bj_out_of_cage
                "Swallow your load" if terri.temporary_count > 0:
                    wt_image indy_slavegirl_bj_3_3
                    "As you start to spurt ..."
                    wt_image indy_slavegirl_bj_3_10
                    "... her eyes widen ..."
                    wt_image indy_slavegirl_bj_3_1
                    "... and to her credit, she leans forward to receive your load ..."
                    wt_image indy_slavegirl_bj_3_2
                    player.c "[player.orgasm_text]"
                    wt_image indy_slavegirl_bj_3_11
                    "... before showing you that she swallowed it all."
                    $ terri.swallow_count += 1
                "Take a facial" if terri.temporary_count > 0:
                    wt_image indy_slavegirl_bj_3_12
                    player.c "[player.orgasm_text]"
                    wt_image indy_slavegirl_bj_3_13
                    "When your balls stop spurting, she licks the head of your cock ..."
                    wt_image indy_slavegirl_bj_3_14
                    "... and continues to lick it until your cock is clean, even if her face isn't."
                    $ terri.facial_count += 1
            wt_image indy_slavegirl_1_2
            "As you put her back in her cage, she stares searchingly up at you, looking for any hint of having pleased you."
            $ title = "What do you say?"
            menu:
                "Compliment her":
                    player.c "Good girl.  I enjoyed that."
                    wt_image indy_slavegirl_1_1
                    terri.c "Thank you, [terri.your_respect_name].  I know I'm not very good at that, but I'll keep trying to get better, to be a good slavegirl for you."
                "Reprimand her":
                    player.c "That was terrible.  You've learned nothing from my teachings.  Wait here and think about how you can suck my cock better the next time."
                    wt_image indy_slavegirl_1_1
                    "Crestfallen, she nods, determined to suck your cock better in the future."
                "Nothing, stay silent":
                    wt_image indy_slavegirl_1_1
                    "She watches uncertainly as you walk away, hoping that the load of sperm you shot meant that you enjoyed using her mouth, even if you didn't say you did."
            $ terri.blowjob_count += 1
        "Mouth in the cage" if not terri.has_tag('slavegirl_let_out'):
            wt_image indy_slavegirl_1_2
            player.c "Put your head in the neck restraint and open your mouth, [terri.name]."
            wt_image indy_slavegirl_1_3
            "She's never become a talented cocksucker, but bound like this, it doesn't matter."
            wt_image indy_slavegirl_bj_1_1
            "The metal collar around her neck holds her in place, preventing her from backing away as you thrust your cock between her parted lips."
            wt_image indy_slavegirl_bj_1_2
            "Still, even with the collar immobilizing her, it's fun to hold her by the hair as you use her."
            wt_image indy_slavegirl_bj_1_3
            player.c "Suck"
            wt_image indy_slavegirl_bj_1_4
            "That she can do. She begins to literally suck at the end of your cock, creating and maintaining an intense sensation that soon pulls the semen out of your balls, spilling it into the back of her throat."
            wt_image indy_slavegirl_bj_1_5
            player.c "[player.orgasm_text]"
            wt_image indy_slavegirl_bj_1_6
            "She keeps up the suction, even after your balls are empty, until you remove your cock.  She's nothing if not obedient."
            $ terri.blowjob_count += 1
            $ terri.swallow_count += 1
        "Mouth" if terri.has_tag('slavegirl_let_out'):
            wt_image indy_slavegirl_2_5
            player.c "Mouth"
            wt_image indy_bj_1_state_1_16
            "Dutifully but nervously, she opens her mouth and gets down on the floor."
            wt_image indy_bj_1_state_1_17
            "She's not good at sucking cock, and she knows it.  Still, she looks hopefully up at your face as she takes your cock into her mouth, looking for any sign of approval that she's doing this right."
            wt_image indy_bj_1_state_1_4
            "She's eager to please ..."
            wt_image indy_bj_1_state_1_10
            "... but worshiping dick just doesn't come naturally to her."
            wt_image indy_bj_1_state_1_4
            "Fortunately, she's pretty enough and has soft enough lips that you're able to enjoy yourself despite her lack of technique."
            wt_image indy_bj_1_state_1_16
            $ title = "Where do you want to cum?"
            menu:
                "In her":
                    wt_image indy_bj_1_state_1_18
                    player.c "[player.orgasm_text]"
                    wt_image indy_bj_1_state_1_19
                    "She shows you your cum before swallowing it."
                    wt_image indy_bj_1_state_1_9
                    "Then she stares searchingly up at you, looking for any hint of having pleased you."
                    $ terri.swallow_count += 1
                "On her":
                    wt_image indy_bj_1_state_1_7
                    "She waits happily for you to finish on her pretty face."
                    wt_image indy_bj_1_state_1_8
                    player.c "[player.orgasm_text]"
                    wt_image indy_bj_1_state_1_5
                    "She lets you watch your cum drip down her face and chin ..."
                    wt_image indy_bj_1_state_1_6
                    "... before wiping it up with her fingers and swallowing it as she stares searchingly up at you, looking for any hint of having pleased you."
                    $ terri.facial_count += 1
            $ title = "What now?"
            menu:
                "Praise her":
                    wt_image indy_slavegirl_2_5
                    player.c "Good girl.  You're a very obedient cocksucker and that makes me happy."
                    "She may be a lousy fellatrix, but she's otherwise a good slave and she positively glows at the smallest compliments."
                "Insult her":
                    wt_image indy_slavegirl_2_4
                    player.c "You stupid cunt.  How did I end up with the only slavegirl in the world who can't suck a cock properly?"
                    "She cringes at your words, feeling miserable inside at having disappointed you."
                "Ignore her":
                    wt_image indy_slavegirl_2_2
                    "She gets back into position, hoping that the fact you came meant that she was a good slavegirl for you."
            $ terri.blowjob_count += 1
        "Cunt out of the cage" if not terri.has_tag('slavegirl_let_out'):
            wt_image indy_slavegirl_sex_3_1
            "You take [terri.full_name] out of her cage and re-bind her with her legs spread apart."
            $ title = "How do you want to fuck her?"
            menu:
                "Rough":
                    wt_image indy_slavegirl_sex_3_2
                    "Bound like this, she's deliciously helpless.  Unlike some slavegirls, cutting off her oxygen while she's helpless doesn't get her wet, but it does make you hard as a reminder that she belongs to you and is yours to do with as you please."
                    wt_image indy_slavegirl_sex_3_3
                    "What you please right now is to fuck her dry pussy, hard and fast ..."
                    wt_image indy_slavegirl_sex_3_4
                    "... until she's squirming from the pain and you're squirming from the need to empty your balls inside her."
                "Gentle":
                    wt_image indy_slavegirl_sex_3_6
                    "She's dry, of course ..."
                    wt_image indy_slavegirl_sex_3_7
                    "... but a liberal application of lube ..."
                    wt_image indy_slavegirl_sex_3_8
                    "... soon has her pussy glistened up ..."
                    wt_image indy_slavegirl_sex_3_9
                    "... and suitable for fucking."
                    wt_image indy_slavegirl_sex_3_10
                    "Suitably prepared like this, you're pleased at how good it feels to slip between the soft, warm folds of her sex ..."
                    wt_image indy_slavegirl_sex_3_11
                    "... and how enjoyable it is to be able to slide easily in-and-out as you fuck her sexy body until you fill it with your cum."
            wt_image indy_slavegirl_sex_3_5
            player.c "[player.orgasm_text]"
            wt_image indy_slavegirl_sex_3_1
            terri.c "Thank you for letting me be of use to you, [terri.your_respect_name]."
            player.c "Get back in your cage."
            wt_image indy_slavegirl_1_2
            terri.c "Yes, [terri.your_respect_name].  Thank you again, [terri.your_respect_name]!"
            $ terri.sex_count += 1
        "Cunt in the cage" if not terri.has_tag('slavegirl_let_out'):
            wt_image indy_slavegirl_1_2
            player.c "Turn around and spread your knees, [terri.name]."
            wt_image indy_slavegirl_1_3
            "You cuff her wrists and lock her neck in place so she won't be able to squirm away when you enter her.  She doesn't mean to, it's an involuntary reaction by her body to the sensation of your cockhead pressing into her, and it happens whether you use lube or don't."
            wt_image indy_slavegirl_sex_1_1
            "She's dry, of course.  She always is before sex.  And during sex."
            $ title = "Lube her dry pussy?"
            menu:
                "Yes, use lube":
                    wt_image indy_slavegirl_sex_1_10
                    "After a generous application of lube ..."
                    wt_image indy_slavegirl_sex_1_2
                    "... you're able to push into her with little resistance."
                    wt_image indy_slavegirl_sex_1_4
                    "She can tolerate being fucked like this for as long as you want to fuck her, and given how good her lubricated pussy feels around your cock, that's a very long time."
                    wt_image indy_slavegirl_sex_1_5
                    "Eventually, though, the lubricant wears off.  She starts to squirm and groan in pain and her tight cunt starts to feel even tighter and warmer ..."
                    wt_image indy_slavegirl_sex_1_3
                    "... the increased friction making it impossible to hold out any longer."
                "No, don't bother":
                    wt_image indy_slavegirl_sex_1_6
                    "She's going to cry out when you penetrate her dry cunt, regardless, but hooking your fingers into her mouth at least keeps her cries of pain down to a dull roar as your cock splits her open ..."
                    wt_image indy_slavegirl_sex_1_7
                    terri.c "NNNNNNN"
                    wt_image indy_slavegirl_sex_1_8
                    "... letting you pound into her in relative peace, as long and as hard as you want ..."
                    wt_image indy_slavegirl_sex_1_3
                    "... until the friction and warmth of her tight, dry pussy milks the cum from your balls."
            wt_image indy_slavegirl_sex_1_9
            player.c "[player.orgasm_text]"
            wt_image indy_slavegirl_sex_1_2
            terri.c "NNNNN ... Thank you for letting me be of use to you, [terri.your_respect_name]."
            wt_image indy_slavegirl_1_2
            "You could reply to her 'thank you', but it's better to leave her wondering if you're happy with her.  It'll make her all the more eager to please you next time."
            $ terri.sex_count += 1
        "Cunt" if terri.has_tag('slavegirl_let_out'):
            wt_image indy_slavegirl_2_3
            "You could tie her up, but she's kneeling right here in front of you. There hardly seems any need."
            wt_image indy_slavegirl_2_4
            player.c "Open your cunt."
            wt_image indy_slavegirl_sex_2_1
            "She's dry, of course, and even telling her to play with herself doesn't help the situation."
            $ title = "Use lube?"
            menu:
                "Yes, make this less uncomfortable for her":
                    wt_image indy_slavegirl_sex_2_2
                    "She knows you're being kind to her and that seems to make her happy.  You still need to hold her firmly in place to keep her from squirming away from you, but she doesn't mean it.  She's a good girl, her body just naturally avoids cock when not held in place."
                "No, don't bother":
                    add tags 'dry_pussy_today' to terri
                    wt_image indy_slavegirl_sex_2_3
                    "No lube makes entering more difficult, but the little yelps of pain she makes as you penetrate her dry hole are kind of fun."
                    terri.c "oww  oww  oowww"
            $ terri.temporary_count = 0
            $ title = "How do you want to do this?"
            menu menu_terri_slavegirl_sex_let_out:
                "Have her play with herself":
                    $ terri.temporary_count = 1
                    wt_image indy_slavegirl_sex_2_4
                    if terri.has_tag('dry_pussy_today'):
                        "It doesn't help alleviate the discomfort she's experiencing, but it's fun watching her act like she's enjoying the experience."
                    else:
                        "It doesn't help her enjoy the experience, but it's fun watching her act like she's aroused by having your cock inside her."
                    jump menu_terri_slavegirl_sex_let_out
                "Have her play with her ass, too":
                    $ terri.temporary_count = 1
                    wt_image indy_slavegirl_sex_2_7
                    "On your instructions, she rams two fingers into her ass and frigs her butt while she rubs her pussy."
                    wt_image indy_slavegirl_sex_2_8
                    if terri.has_tag('dry_pussy_today'):
                        "It doesn't help alleviate the discomfort she's experiencing, it just adds pain from frigging a dry asshole to the pain of having her dry pussy fucked, but it's exciting watching her suffer as you fuck her."
                    else:
                        "It does nothing to excite her, but it does excite you to see how willing she is to obey you."
                    jump menu_terri_slavegirl_sex_let_out
                "Spank her while you fuck her":
                    $ terri.temporary_count = 1
                    wt_image indy_slavegirl_sex_2_6
                    if terri.has_tag('dry_pussy_today'):
                        "She doesn't seem to mind you swatting her ass while you fuck her.  If anything, it seems to calm her.  She holds her hips still and lets your hand hurt her ass while your cock hurts her dry cunt ... *smack*  *smack*  *smack*  *smack*  *smack*"
                    else:
                        "She doesn't seem to mind you swatting her ass while you fuck her.  If anything, it seems to calm her.  She holds her hips still and lets your hand hurt her ass while your cock plows her cunt ... *smack*  *smack*  *smack*  *smack*  *smack*"
                    terri.c "Ow!  Ow!  Ow ow oww!!"
                    jump menu_terri_slavegirl_sex_let_out
                "Have her bark like a dog":
                    $ terri.temporary_count = 1
                    wt_image indy_slavegirl_sex_2_5
                    if terri.has_tag('dry_pussy_today'):
                        "She wiggles her ass while she barks, but that's probably just an attempt to relieve the discomfort she's feeling while you fuck her."
                    else:
                        "She wiggles her ass while she barks, but that's probably just because the sensation of having your cock inside her remains a strange one to her."
                    terri.c "Ruff!  Ruff!  Ruff ruff ruff!!"
                    jump menu_terri_slavegirl_sex_let_out
                "Just fuck her":
                    $ terri.temporary_count = 1
                    wt_image indy_slavegirl_sex_2_9
                    if terri.has_tag('dry_pussy_today'):
                        "Her cunt is so dry it's hard to slide your cock in and out of it easily, but the extra friction adds a pleasant warmth for you, and a painful burning for her."
                    else:
                        "She's so cute and her cunt is so tight, you don't need any other stimulation to enjoy fucking her."
                    jump menu_terri_slavegirl_sex_let_out
                "Cum now" if terri.temporary_count > 0:
                    pass
            wt_image indy_slavegirl_sex_2_9
            player.c "[player.orgasm_text]"
            if terri.has_tag('dry_pussy_today'):
                wt_image indy_slavegirl_2_5
                "As you pull out, she presses her thighs together, trying to alleviate the pain in her pussy, but she's otherwise seemingly none the worse for wear."
            else:
                wt_image indy_slavegirl_2_2
                "As you pull out, she smiles back at you."
            terri.c "Thank you for letting me be of use to you, [terri.your_respect_name]."
            $ terri.temporary_count = 0
            $ terri.sex_count += 1
            rem tags 'dry_pussy_today' from terri
        "Ass in the cage" if not terri.has_tag('slavegirl_let_out') and not terri.has_item(dildo):
            "You'll need to gift her a dildo first before engaging in this activity."
            $ title = "Set a dildo aside for use on [terri.name]?"
            menu:
                "Yes" if player.has_item(dildo):
                    give 1 dildo from player to terri notify
                    call terri_use_her_anal_in_cage from _call_terri_use_her_anal_in_cage
                "Not now":
                    $ terri.temporary_count = 1
        "Ass in the cage" if not terri.has_tag('slavegirl_let_out') and terri.has_item(dildo):
            call terri_use_her_anal_in_cage from _call_terri_use_her_anal_in_cage_1
        "Ass out of the cage" if not terri.has_tag('slavegirl_let_out') and not terri.has_item(butt_plug):
            "You'll need to gift her a butt plug first before engaging in this activity."
            $ title = "Set a butt plug aside for use on [terri.name]?"
            menu:
                "Yes" if player.has_item(butt_plug):
                    give 1 butt_plug from player to terri notify
                    call terri_use_her_anal_out_cage from _call_terri_use_her_anal_out_cage
                "Not now":
                    $ terri.temporary_count = 1
        "Ass out of the cage" if not terri.has_tag('slavegirl_let_out') and terri.has_item(butt_plug):
            call terri_use_her_anal_out_cage from _call_terri_use_her_anal_out_cage_1
        "Ass" if terri.has_tag('slavegirl_let_out'):
            wt_image indy_sex_2_state_1_2
            "She trembles at your instruction ..."
            wt_image indy_doll_1_24
            "... but dutifully leans forward and gives you access to her backdoor."
            wt_image indy_doll_2_7
            if terri.anal_count == 0:
                if terri.has_item(butt_plug):
                    "You're a lot bigger than the butt plug, which is the only thing she's ever had back there.  You could make losing her anal virginity less painful by using lube, if you want.  Or not."
                else:
                    "She's never had anything back there.  You could make losing her anal virginity less painful by using lube, if you want.  Or not."
            $ title = "Use lube?"
            menu:
                "No, don't bother":
                    wt_image indy_anal_10
                    terri.c "OOWWWW!!!"
                    if terri.anal_count == 0:
                        "She doesn't want to scream, but she can't help it.  This is a terribly painful way to lose her anal virginity, but her screams and squirming just make it feel all that much better to you."
                    else:
                        "She doesn't want to scream, but she can't help it.  Being taken this way hurts her terribly, but her screams and squirming just make it feel all that much better to you."
                "Yes, reduce the friction":
                    wt_image indy_anal_10
                    if terri.anal_count == 0:
                        terri.c "OW!"
                        "Even with the lube, she calls out in pain as your cock penetrates her virgin ass.  After she gets used to the sensation of being filled back there, though, you're able to slide your cock in and out until her tight anus milks the cum from your balls."
                    else:
                        "Even with the lube, her ass grips your cock tightly, but the lubricant reduces the friction enough that you can enjoy sliding your cock in and out until her anus milks the cum from your balls."
            wt_image indy_anal_11
            player.c "[player.orgasm_text]"
            wt_image indy_slavegirl_sex_2_1
            terri.c "Thank you for letting me use all three of my holes to please you, [terri.your_respect_name]."
            $ terri.anal_count += 1
        "Change your mind":
            $ terri.temporary_count = 1
    if terri.temporary_count == 0:
        orgasm notify
    else:
        $ terri.temporary_count = 0
    wt_image current_location.image
    return

label terri_use_her_anal_in_cage:
    wt_image indy_slavegirl_anal_1_1
    "[terri.full_name]'s ass is even tighter than her dry cunt."
    wt_image indy_slavegirl_anal_1_2
    "Using a large dildo on her first serves to both lubricate her and open her up at the same time."
    wt_image indy_slavegirl_anal_1_3
    "It takes some time, and elicits some yelps of pain ..."
    terri.c "Oww!!  OW!"
    wt_image indy_slavegirl_anal_1_4
    "... but eventually the dildo is moving freely in-and-out of her ass."
    wt_image indy_slavegirl_sex_1_2
    "Whether you add more lube as you replace the dildo with your cock depends on how much friction you want to feel ..."
    wt_image indy_slavegirl_anal_1_5
    "... while you're buggering her."
    wt_image indy_slavegirl_sex_1_5
    "It doesn't matter to her.  As long as you enjoy her backhole enough to flood her insides with cum, she's grateful for the opportunity to serve, no matter how much it hurts."
    wt_image indy_slavegirl_anal_1_6
    player.c "[player.orgasm_text]"
    wt_image indy_slavegirl_sex_1_2
    terri.c "Thank you for letting me be of use to you, [terri.your_respect_name]!"
    wt_image indy_slavegirl_1_2
    "Your cum dripping out of her sore ass, she watches as you leave, hopeful that you enjoyed reaming her."
    $ terri.anal_count += 1
    return

label terri_use_her_anal_out_cage:
    wt_image indy_slavegirl_anal_3_1
    "As willing as she is to offer you her ass, you're not easily getting inside there without opening her up."
    wt_image indy_slavegirl_anal_3_2
    "Fortunately, butt plugs are custom-made for preparing the asses of slavegirls ..."
    wt_image indy_slavegirl_anal_3_3
    "... stretching the sphincter that guards her backhole ..."
    wt_image indy_slavegirl_anal_3_4
    "... until it's ready to open wide for you ..."
    wt_image indy_slavegirl_anal_3_5
    "... and it's ready to take you deep."
    wt_image indy_slavegirl_anal_3_1
    "Then you remove the plug ..."
    wt_image indy_slavegirl_anal_3_6
    "... and replace it with your cock."
    wt_image indy_slavegirl_anal_3_7
    "You decide how much or how little lube to use ..."
    wt_image indy_slavegirl_anal_3_8
    "... and how fast or slow to fuck her."
    wt_image indy_slavegirl_anal_3_9
    "She decides nothing, she just accepts, groaning sexily when the discomfort becomes too much ..."
    wt_image indy_slavegirl_anal_3_10
    terri.c "NNNNNNN"
    wt_image indy_slavegirl_anal_3_8
    "... while she waits for you to empty your balls into her bowels."
    wt_image indy_slavegirl_anal_3_11
    player.c "[player.orgasm_text]"
    wt_image indy_slavegirl_anal_3_10
    terri.c "Thank you for letting me be of use to you, [terri.your_respect_name]."
    wt_image indy_slavegirl_anal_3_9
    player.c "Get back in your cage."
    wt_image indy_slavegirl_1_2
    terri.c "Yes, [terri.your_respect_name].  Thank you again, [terri.your_respect_name]!"
    $ terri.anal_count += 1
    return

# Kiss Her
label terri_sg_kiss_her:
    wt_image indy_slavegirl_hurt_3_2
    "[terri.name] shyly approaches you ..."
    wt_image indy_slavegirl_kiss_1_1
    "... and presses her lips to yours."
    wt_image indy_slavegirl_kiss_1_2
    "She doesn't so much kiss you and let you kiss her, but she sits patiently on your lap until you've had your fill of exploring her mouth with your tongue."
    wt_image current_location.image
    return

# Let Her Out For a Bit
label terri_let_her_out:
    add tags 'slavegirl_let_out' to terri
    wt_image indy_strip_state_1_7
    "[terri.full_name] seems disoriented as you remove her from the cage and strip her naked."
    wt_image indy_slavegirl_2_2
    "She's more comfortable when you give her a place to get back on her knees.  It's good for her to be able to move and stretch, and frankly she makes a nice background decoration as you work around the house."
    wt_image indy_slavegirl_2_3
    "She's become used to the confinement of her cage, though, and you'll securely lock her up before going to bed for the night."
    wt_image current_location.image
    return

# Lend to Master M
label terri_lend_to_master_m:
    wt_image indy_strip_state_1_7
    player.c "[terri.name], get dressed. I'm sending you to another man."
    wt_image indy_strip_state_1_9
    terri.c "Another man?  But, I belong to you, [terri.your_respect_name]."
    wt_image indy_strip_state_1_12
    player.c "And you are mine to do what I want with. Today, what I want is for you to go visit Master M and let him do whatever he wants with you. Until he sends you back to me, you will obey him as you would me."
    wt_image indy_hypno_state_1_5
    terri.c "Yes, [terri.your_respect_name]."
    wt_image indy_strip_state_1_11
    "It's a few hours later before she returns and undresses."
    player.c "How did it go?"
    wt_image indy_strip_state_1_2
    terri.c "Good, I hope, [terri.your_respect_name]."
    player.c "Was he pleased with you?"
    wt_image indy_strip_state_1_3
    terri.c "I hope so."
    $ title = "Ask for details?"
    menu:
        "Yes":
            wt_image indy_strip_state_1_4
            player.c "What did he do with you?"
            wt_image indy_mm_1
            terri.c "{i}He didn't do anything with me at first.  One of his slavegirls stripped and gagged me and bound me to a post.  I'm not sure how long he left me waiting there, but it seemed like a long time.{/i}"
            wt_image indy_mm_2
            terri.c "{i}At some point - I'm not sure how when - Master M appeared and asked if I was ready to pleasure him.  I nodded 'yes'.{/i}"
            wt_image indy_mm_8
            terri.c "{i}He removed my gag and put his dick in my mouth. I sucked it just like he told me to, [terri.your_respect_name], but he seemed restless. He kept changing the position of my head and the angle of his dick, as if he was trying to find the most enjoyable way to use me.{/i}"
            wt_image indy_mm_9
            terri.c "{i}We stayed like that for a long, long time while I tried my best to follow his instructions and bring him pleasure.{/i}"
            player.c "{i}Did he cum?{/i}"
            wt_image indy_mm_8
            terri.c "{i}No, [terri.your_respect_name]. Not like this. He kept me there, sucking his cock, until my jaw ached and the muscles in my neck and shoulders were screaming at me. Then he kept me there some more. And some more.{/i}"
            wt_image indy_mm_3
            terri.c "{i}Then ... I'm sorry, [terri.your_respect_name]. I wanted to be a good slavegirl and make you proud of me, but ... then I started to cry. I couldn't help myself. The agony in my sore muscles was unlike anything I'd experienced before. It wasn't harsh, but it was constant and unrelenting. I didn't know how long he would keep me doing this and I ... I felt the tears starting to run down my face."
            player.c "{i}Did you pull away from his cock?{/i}"
            wt_image indy_mm_4
            terri.c "{i}No, [terri.your_respect_name].  I couldn't have even if I wanted to, because he kept a firm grip on my head, moving it around and changing the position of it on his dick.  But I did start to retch, and it took everything I had not to throw up on him.{/i}"
            wt_image indy_mm_10
            terri.c "{i}Shortly after that, everything became a blur.  I think I may have passed out, or come close to doing so.{/i}"
            wt_image indy_mm_5
            terri.c "{i}When my head cleared, I found I'd been tied into a new position.{/i}"
            wt_image indy_mm_11
            terri.c "{i}Then he put his dick in my mouth again.{/i}"
            wt_image indy_mm_6
            terri.c "{i}He was angled more like you usually use me, [terri.your_respect_name], fucking my mouth like it was my pussy.  He seemed more satisfied with this position, and kept at it for a very, very long time.{/i}"
            wt_image indy_mm_12
            terri.c "{i}I'm not sure exactly how long. The pain in my jaw, neck, and shoulders had become even worse, and at some point I must have spaced out again.{/i}"
            wt_image indy_mm_7
            terri.c "{i}The next thing I remember, he was pushing himself into me from behind ...{/i}"
            wt_image indy_mm_13
            terri.c "{i}... and flooding my insides with his cum.{/i}"
            player.c "{i}Did you cum, too?{/i}"
            wt_image indy_sex_2_state_1_2
            "She seems surprised by the question."
            terri.c "No, [terri.your_respect_name].  Why would I have cum?"
            wt_image indy_slavegirl_2_3
            $ title = "What do you do?"
            menu:
                "Punish her":
                    wt_image indy_slavegirl_2_4
                    player.c "Your jaw muscles wouldn't be hurting if you'd pay attention to my instructions and learn how to suck a cock properly."
                    wt_image indy_slavegirl_2_2
                    "It sounds like Master M didn't have any better luck training her to suck cock than you have.  You know it won't do any good, but her inability to master this basic skill is infuriating, and you take it out on her upturned bottom ... *smack* ... *smack* ... *smack* ... *smack* ... *smack*"
                    terri.c "ow!  Ow!  Ooww!!  OOWWW!!!  OOWW OW OWWWW!!  I'M SORRY [terri.your_respect_name]!  I PROMISE I'LL BE A BETTER COCK SUCKER IN THE FUTURE!!"
                    wt_image indy_slavegirl_2_5
                    "You're pretty sure she won't be, but it's not from lack of trying.  She really does want to be a good slave."
                    change player energy by -energy_short notify
                "Fuck her":
                    wt_image indy_slavegirl_sex_2_6
                    "Unlike Master M, you bypass her mouth and go straight for her cunt.  It's the less aggravating way to make use of her body."
                    wt_image indy_slavegirl_sex_2_4
                    "She's dry, as usual, as you enter her, but she doesn't seem to mind.  She looks back at you as you fuck her, seemingly happy to have her owner's cock inside her rather than some other man."
                    wt_image indy_slavegirl_sex_2_6
                    "When you've enjoyed her long enough, you let yourself go, dumping the second load of cum for the day into her waiting pussy."
                    wt_image indy_slavegirl_sex_2_9
                    player.c "[player.orgasm_text]"
                    wt_image indy_slavegirl_sex_2_3
                    terri.c "Thank you for letting me be of use to you, [terri.your_respect_name]."
                    $ terri.sex_count += 1
                    orgasm notify
                "Make her blow you":
                    wt_image indy_slavegirl_2_4
                    player.c "Open your mouth."
                    wt_image indy_bj_state_1_16
                    "Her jaw has had some rest, but you know it must still be very sore. Despite that, she obediently takes you into her mouth."
                    wt_image indy_bj_state_1_4
                    "Master M's efforts weren't any more successful than yours. She's still a lousy cock sucker. She's been told what to do and she's eager to please, but she just has no talent for actually pleasuring a cock."
                    wt_image indy_bj_state_1_10
                    "Today her efforts are further hampered by the pain she's experiencing.  She's in agony, and no matter how hard she tries not to let that show, the simple act of sucking you off after the ordeal Master M put her through may be the most intense torture you've inflicted on her."
                    wt_image indy_bj_state_1_17
                    "Before long, her whole body is trembling as her muscles rebel against overuse, and tears well up in her eyes."
                    wt_image indy_bj_state_1_18
                    "Fortunately for her, watching her try to ignore the tremors in her own body and focus exclusively on pleasuring your cock, no matter how much it hurts, turns you on in a way the blow job itself doesn't, and you soon feel your balls boiling over,"
                    wt_image indy_bj_state_1_19
                    player.c "[player.orgasm_text]"
                    wt_image indy_bj_state_1_5
                    "As she swallows the load you left in her mouth, she looks up at you in adoration, happy with herself for having brought you pleasure, happy with you that you were able to make use of her. All thoughts of the pain she's experienced are pushed aside by a deep sense of satisfaction that she has found her proper role in life."
                    $ terri.blowjob_count += 1
                    $ terri.swallow_count += 1
                    orgasm notify
                "Go on with your day":
                    wt_image indy_strip_state_1_5
                    player.c "I'm sure you did fine, [terri.name].  Let's get you back in your cage."
                    wt_image indy_strip_state_1_7
                    terri.c "Yes, [terri.your_respect_name]."
        "No, just go on with your day":
            wt_image indy_strip_state_1_9
            player.c "I'm sure you did fine, [terri.name]. Let's get you back in your cage."
            wt_image indy_strip_state_1_7
            terri.c "Yes, [terri.your_respect_name]."
    $ master_m.experience_with_your_slave = "I enjoyed making use of her, although there was something a bit .. off with her. I couldn't quite put my finger on it. Anyway, I enjoyed myself."
    $ master_m.name_of_your_slave_loaned = terri.name
    $ terri.training_session()
    add tags 'master_m_visit' to terri
    call master_m_lend from _call_master_m_lend_3
    return

## Doll Actions
# Dress Her
label terri_doll_dress_her:
    wt_image terri.image
    $ title = "How do you want to dress your doll up?"
    menu:
        "Clothed" if not terri.doll_dress_state == 1:
            wt_image indy_doll_1_38
            "Sometimes it's fun to put clothes on your doll.  You can always take them off her again later."
            wt_image indy_doll_1_1
            $ terri.change_image('indy_doll_1_1')
            $ terri.doll_dress_state = 1
        "Naked" if not terri.doll_dress_state == 2:
            wt_image indy_doll_2_1
            "Your doll really only has one purpose now."
            wt_image indy_doll_2_2
            "Stripping it naked seems to show off that purpose to good effect."
            $ terri.change_image('indy_doll_2_1')
            $ terri.doll_dress_state = 2
        "Glasses clothed" if not terri.doll_dress_state == 3:
            wt_image indy_doll_3_1
            "After she enhanced her assets, [terri.name] probably would have done well in the corporate world, either behind a desk or under one."
            $ terri.change_image('indy_doll_3_1')
            $ terri.doll_dress_state = 3
        "Glasses naked" if not terri.doll_dress_state == 4:
            wt_image indy_doll_4_1
            "Putting glasses on your doll makes it look like a slutty secretary or horny librarian."
            $ terri.change_image('indy_doll_4_1')
            $ terri.doll_dress_state = 4
        "Collar clothed" if not terri.doll_dress_state == 5:
            wt_image indy_doll_5_1
            "Dressed up like this, [terri.name] looks like the perfect housewife.  A collared housewife, but perhaps those are the perfect kind."
            $ terri.change_image('indy_doll_5_1')
            $ terri.doll_dress_state = 5
        "Collar naked" if not terri.doll_dress_state == 6:
            wt_image indy_doll_6_1
            "[terri.name] came to you hoping to learn how to be a better girlfriend.  Naked, collared, and with bigger boobs seems like an improvement."
            $ terri.change_image('indy_doll_6_1')
            $ terri.doll_dress_state = 6
        "Lingerie" if not terri.doll_dress_state == 7:
            if not terri.has_tag('doll_lingerie_sexy'):
                if player.has_item(lingerie):
                    "Do you want to give the lingerie to your doll?"
                    $ title = "Give sexy lingerie to [terri.full_name]?"
                    menu:
                        "Yes":
                            rem 1 lingerie from player
                            add tags 'doll_lingerie_sexy' to terri
                        "No":
                            pass
                else:
                    "You'll need to pick up some lingerie of this type to fit your doll's current frame."
            if terri.has_tag('doll_lingerie_sexy'):
                wt_image indy_doll_7_1
                "Your doll looks rather nice dressed up like this.  Sort of like an expensive mistress, or trophy wife."
                $ terri.change_image('indy_doll_7_1')
                $ terri.doll_dress_state = 7
        "Schoolgirl outfit" if not terri.doll_dress_state == 8:
            if not terri.has_tag('doll_lingerie_schoolgirl'):
                if player.has_item(lingerie):
                    "Do you want to give the lingerie to your doll?"
                    $ title = "Give schoolgirl lingerie to [terri.full_name]?"
                    menu:
                        "Yes":
                            rem 1 lingerie from player
                            add tags 'doll_lingerie_schoolgirl' to terri
                        "No":
                            pass
                else:
                    "You'll need to pick up some lingerie of this type to fit your doll's current frame."
            if terri.has_tag('doll_lingerie_schoolgirl'):
                wt_image indy_doll_8_1
                "Terri the Woman enjoyed being treated younger than she was.  You'd like to think [terri.full_name] enjoys being dressed up as a schoolgirl, too."
                $ terri.change_image('indy_doll_8_1')
                $ terri.doll_dress_state = 8
        "Leave her as she is":
            pass
    wt_image current_location.image
    return

# Rerrange Her
label terri_doll_rearrange_her:
    if terri.doll_dress_state == 1:
        wt_image indy_doll_1_2
        "Even clothed, it can be fun to turn your doll around ..."
        wt_image indy_doll_1_3
        "... and look at it from different angles."
        wt_image indy_doll_1_4
        "You can pose it like a pin up ..."
        wt_image indy_doll_1_5
        "... or as a tease."
        wt_image indy_doll_1_39
        "With its skirt pulled up ..."
        wt_image indy_doll_1_40
        "... or its skirt removed."
        wt_image indy_doll_1_41
        "Wearing just underwear ..."
        wt_image indy_doll_1_6
        "... or with its bra removed ..."
        wt_image indy_doll_1_7
        "... and its panties down ..."
        wt_image indy_doll_1_8
        "... or with its panties off completely.  At which point it's not really clothed anymore, but still looks nice."
    elif terri.doll_dress_state == 2:
        wt_image indy_doll_2_2
        "What the doll has to offer is easily displayed when it's naked."
        wt_image indy_doll_2_3
        "You can position it to emphasize one hole ..."
        wt_image indy_doll_2_4
        "... or another."
        wt_image indy_doll_2_5
        "Stand it up ..."
        wt_image indy_doll_2_6
        "... or turn it around."
        wt_image indy_doll_2_7
        "It doesn't care what part of it you want to look at."
        wt_image indy_doll_2_8
        "One position's as good as another to a doll."
    elif terri.doll_dress_state == 3:
        wt_image indy_doll_3_2
        '"Poseable Smart Girl" is a good look for [terri.name].'
        wt_image indy_doll_3_3
        "One part sexy librarian ..."
        wt_image indy_doll_3_4
        "... one part slut ..."
        wt_image indy_doll_3_5
        "... one hundred percent sex toy."
    elif terri.doll_dress_state == 4:
        wt_image indy_doll_4_5
        "What the doll has to offer is already on display."
        wt_image indy_doll_4_2
        "You can position it to emphasize one hole ..."
        wt_image indy_doll_4_3
        "... or another ..."
        wt_image indy_doll_3_43
        "... or another."
        wt_image indy_doll_4_4
        "No matter how you pose it, though ..."
        wt_image indy_doll_4_9
        "... it's purpose and function remain clear."
    elif terri.doll_dress_state == 5:
        wt_image indy_doll_5_2
        "One of the attributes of a perfect housewife - or housedoll in this case ..."
        wt_image indy_doll_5_3
        "... is that it will expose its breasts on demand ..."
        wt_image indy_doll_5_4
        "... and leave them exposed for as long as you feel like looking at them.  With clothes ..."
        wt_image indy_doll_5_18
        "... or without them."
        wt_image indy_doll_5_5
        "On its feet ..."
        wt_image indy_doll_5_6
        "... or on its knees.  Facing towards you ..."
        wt_image indy_doll_5_7
        "... or facing away."
        wt_image indy_doll_5_30
        "The perfect housedoll knows its function is to please ..."
        wt_image indy_doll_5_8
        "... and like the perfect housewife, it patiently awaits opportunities to do so."
    elif terri.doll_dress_state == 6:
        wt_image indy_doll_6_2
        "The natural position for a slave doll is on its knees, of course ..."
        wt_image indy_doll_6_3
        "... but it looks nice in a sitting position, too."
        wt_image indy_doll_6_4
        "Especially when its posture is corrected."
    elif terri.doll_dress_state == 7:
        wt_image indy_doll_7_45
        "The lingerie shows off your doll's body quite nicely ..."
        wt_image indy_doll_7_2
        "... and like a good trophy wfe, its happy to sit and do nothing while you admire its body ..."
        wt_image indy_doll_7_46
        "... from front ..."
        wt_image indy_doll_7_47
        "... and back.  Tits covered ..."
        wt_image indy_doll_7_48
        "... or tits out.  Legs together ..."
        wt_image indy_doll_7_3
        "... or legs apart.  Panties on ..."
        wt_image indy_doll_7_4
        "... or panties pulled aside."
        wt_image indy_doll_7_49
        "Like a good trophy wife, your doll is happy to model the lingerie you bought it however you want ..."
        wt_image indy_doll_7_5
        "... and from whichever angle you want."
        wt_image indy_doll_7_50
        "After all, sitting still and looking pretty is what trophy wives - and dolls - do best."
    elif terri.doll_dress_state == 8:
        wt_image indy_doll_8_2
        "You'd think it'd be easy to re-arrange a schoolgirl doll to the pose you want ..."
        wt_image indy_doll_8_3
        "... but every time you try to adjust its skirt ..."
        wt_image indy_doll_8_4
        "... to give you a more interesting view ..."
        wt_image indy_doll_8_5
        "... it reacts in shock and covers itself up as soon as you leave it alone.  You're not sure why.  The innocent schoolgirl act isn't fooling anyone."
    wt_image current_location.image
    return

# Use Her
label terri_doll_use_her:
    wt_image terri.image
    $ title = "How do you want to use your doll?"
    menu:
        "Hand job":
            if terri.doll_dress_state == 1:
                wt_image indy_doll_1_9
                "Sometimes the sexiest thing to request from a clothed woman ..."
                wt_image indy_doll_1_42
                "... or a clothed doll in this case ..."
                wt_image indy_doll_1_43
                "... is a basic handjob."
                wt_image indy_doll_1_10
                "Especially when, as in this situation ..."
                wt_image indy_doll_1_11
                "... you know how the hand job's going to end."
                wt_image indy_doll_1_12
                $ terri.facial_count += 1
            elif terri.doll_dress_state == 2:
                wt_image indy_doll_2_9
                "Your doll only really has one purpose now.  So when you place it's hand on your cock ..."
                wt_image indy_doll_2_10
                "... it instinctively starts stroking ..."
                wt_image indy_doll_2_11
                "... and continues to stroke ..."
                wt_image indy_doll_2_12
                "... until it fulfills its purpose."
                wt_image indy_doll_2_34
                $ terri.facial_count += 1
            elif terri.doll_dress_state == 3:
                wt_image indy_doll_3_6
                "The stereotypical secretary blows her boss on his lunch break ..."
                wt_image indy_doll_3_45
                "... but a smart secretary saves the time she would otherwise waste fixing her lipstick ..."
                wt_image indy_doll_3_46
                "... by getting you off with her hand, instead ..."
                wt_image indy_doll_3_12
                "... speeding the process up with some judicious boob contact."
                wt_image indy_doll_3_9
            elif terri.doll_dress_state == 4:
                wt_image indy_doll_4_10
                "With those glasses on, [terri.name] looks like the sort of slutty librarian who would give handjobs in the poetry aisle."
                wt_image indy_doll_3_7
                "You need to spit on it to give your doll saliva to dribble on you, but [terri.name] looks like the sort of librarian who'd enjoy that, too."
                wt_image indy_doll_3_8
                "Suitably wetted, your sex toy strokes your cock ..."
                wt_image indy_doll_3_12
                "... to the inevitable conclusion."
                wt_image indy_doll_3_9
            elif terri.doll_dress_state == 5:
                wt_image indy_doll_5_2
                "A good housedoll, like a good housewife, is prepared to give handjobs on request ..."
                wt_image indy_doll_5_9
                "... a perfect housedoll, like a perfect housewife, doesn't shy away from finishing them the right way."
                wt_image indy_doll_5_10
            elif terri.doll_dress_state == 6:
                wt_image indy_doll_6_6
                "Slaves are usually put to more strenuous use ..."
                wt_image indy_doll_6_5
                "... but they're also available to stroke cock on demand ..."
                wt_image indy_doll_6_7
                "... and to suck balls while doing so ..."
                wt_image indy_doll_6_8
                "... and to receive the consequences of their actions."
                wt_image indy_doll_6_9
            elif terri.doll_dress_state == 7:
                wt_image indy_doll_7_7
                "A hand job is an easy way for a trophy wife - or trophy doll - to earn its keep."
                wt_image indy_doll_7_9
                "Once you're soaped up ..."
                wt_image indy_doll_7_51
                "... it'll contentedly stroke you off ..."
                wt_image indy_doll_7_10
                "... for as long as you care to delay ..."
                wt_image indy_doll_7_11
                "... the inevitable conclusion."
                wt_image indy_doll_7_12
            elif terri.doll_dress_state == 8:
                wt_image indy_doll_8_26
                "The hand job is a schoolgirl staple."
                wt_image indy_doll_8_6
                "There's no easier way to keep a boyfriend and still practice safe sex ..."
                wt_image indy_doll_8_7
                "... especially if you don't mind re-doing your makeup between classes."
                wt_image indy_doll_1_12
            player.c "[player.orgasm_text]"
            $ terri.handjob_count += 1
            orgasm notify
        "Tit job":
            if terri.doll_dress_state == 1:
                wt_image indy_doll_1_44
                "These tits cost [terri.name] quite a bit of money, back when she could worry about things like money."
                wt_image indy_doll_1_14
                "If there's anything of [terri.name] still left inside your sex toy ..."
                wt_image indy_doll_1_15
                "... you're sure it'll be happy to know you're getting a benefit from her financial sacrifice."
                wt_image indy_doll_1_16
            elif terri.doll_dress_state == 2:
                wt_image indy_doll_2_13
                "You sit your doll in front of you ..."
                wt_image indy_doll_2_14
                "... lean it forward ..."
                wt_image indy_doll_2_35
                "... tell it to press its recently-enhanced features together ..."
                wt_image indy_doll_2_15
                "... and enjoy the use of those features."
                wt_image indy_doll_2_16
            elif terri.doll_dress_state == 3:
                wt_image indy_doll_3_47
                "The tits [terri.name] paid for look great in this outfit."
                wt_image indy_doll_3_10
                "They look nice coming out of the outfit, too ..."
                wt_image indy_doll_3_11
                "... and look even better wrapped around your cock."
                wt_image indy_doll_3_14
                "They feel nice, too ..."
                wt_image indy_doll_3_13
                "... especially since, like all good secretaries ..."
                wt_image indy_doll_3_15
                "... your doll doesn't shy away from what happens next."
                wt_image indy_doll_3_16
            elif terri.doll_dress_state == 4:
                wt_image indy_doll_4_7
                "Thanks to [terri.name] the Woman's financial investment, [terri.full_name] sports an appealing pair of tits."
                wt_image indy_doll_3_11
                "They look even better wrapped around your cock ..."
                wt_image indy_doll_3_13
                "... and feel better still."
                wt_image indy_doll_3_14
                "Especially since, like all good nerdy sluts ..."
                wt_image indy_doll_3_15
                "... your doll doesn't shy away from what happens next."
                wt_image indy_doll_3_16
            elif terri.doll_dress_state == 5:
                wt_image indy_doll_5_3
                "Your housedoll, like a good housewife, knows its tits aren't just for looking at ..."
                wt_image indy_doll_5_11
                "... and thanks to [terri.name] the Woman's financial investment ..."
                wt_image indy_doll_5_33
                "... like a perfect housewife, [terri.full_name] now has a pair well-suited for your use and enjoyment."
                wt_image indy_doll_5_12
                "And enjoy them, you do."
                wt_image indy_doll_5_13
            elif terri.doll_dress_state == 6:
                wt_image indy_doll_6_10
                "Even though she didn't realize it at the time, [terri.name]'s servitude began when she bought larger breasts for you."
                wt_image indy_doll_6_11
                "Terri the Woman may not have understood the sole purpose for her enhanced chest was to please you, but [terri.name] the Slave Doll certainly does."
                wt_image indy_doll_3_12
                "And please you with it she does."
                wt_image indy_doll_6_12
            elif terri.doll_dress_state == 7:
                wt_image indy_doll_7_13
                "The first step to becoming a trophy wife is to make yourself desirable to men."
                wt_image indy_doll_7_14
                "[terri.name] demonstrated her suitability for the role when she invested in a new pair of tits."
                wt_image indy_doll_7_15
                "It's not a role you can get without a lot of time on your knees."
                wt_image indy_doll_7_16
                "[terri.name] the Woman might have struggled to devote herself so mindlessly to the role of being a tit valley ..."
                wt_image indy_doll_7_17
                "... but [terri.full_name] specializes in providing mindless entertainment."
                wt_image indy_doll_7_18
            elif terri.doll_dress_state == 8:
                wt_image indy_doll_8_2
                "Most schoolgirls don't have tits like your doll."
                wt_image indy_doll_8_8
                "Then again, your doll didn't have tits like this, either, until Terri the Woman bought them for you."
                wt_image indy_doll_2_15
                "You'd thank her for the generous gift, if she was still capable of understanding such matters."
                wt_image indy_doll_2_16
            player.c "[player.orgasm_text]"
            $ terri.titfuck_count += 1
            orgasm notify
        "Blow job":
            if terri.doll_dress_state == 1:
                wt_image indy_doll_1_17
                "You used to admonish [terri.name] for trying to give a blow job without first showing off her tits ..."
                wt_image indy_doll_1_18
                "... but there's something sexy about head from a fully clothed woman ..."
                wt_image indy_doll_1_19
                "... even if that woman is now more sex toy than real girl."
                wt_image indy_doll_1_20
                $ title = "Where do you want to cum?"
                menu:
                    "In its mouth":
                        wt_image indy_doll_1_21
                        $ terri.swallow_count += 1
                    "On its face":
                        wt_image indy_doll_1_22
                        "It has such a pretty face, but you can make it even prettier."
                        wt_image indy_doll_1_12
                        $ terri.facial_count += 1
            elif terri.doll_dress_state == 2:
                wt_image indy_doll_2_17
                "Terri the Woman struggled with the concept, but [terri.full_name] understands its body is for looking at, even when it's being placed on its knees."
                wt_image indy_doll_2_18
                "And if its mouth is no more talented now than it ever was ..."
                wt_image indy_doll_2_19
                "... it can at least now kneel there comfortably for hours until the sight of its body eventually gets you off."
                wt_image indy_doll_2_20
                $ terri.facial_count += 1
            elif terri.doll_dress_state == 3:
                wt_image indy_doll_3_44
                "Like a full service secretary, your doll is available for whatever the boss wants ..."
                wt_image indy_doll_3_17
                "... and is perfectly happy to get on its knees ..."
                wt_image indy_doll_3_18
                "... with its mouth open ..."
                wt_image indy_doll_3_48
                "... and stay there until the boss is finished with it."
                wt_image indy_doll_3_49
                $ title = "Where do you want to cum?"
                menu:
                    "In it":
                        wt_image indy_doll_3_20
                        $ terri.swallow_count += 1
                    "On it":
                        wt_image indy_doll_3_21
                        $ terri.facial_count += 1
            elif terri.doll_dress_state == 4:
                wt_image indy_doll_4_6
                "Like a full service secretary, your doll is available for whatever the boss wants ..."
                wt_image indy_doll_3_17
                "... and is perfectly happy to get on its knees ..."
                wt_image indy_doll_3_18
                "... with its mouth open ..."
                wt_image indy_doll_3_48
                "... and stay there until the boss is finished with it."
                wt_image indy_doll_3_49
                $ title = "Where do you want to cum?"
                menu:
                    "In it":
                        wt_image indy_doll_3_20
                        $ terri.swallow_count += 1
                    "On it":
                        wt_image indy_doll_3_21
                        $ terri.facial_count += 1
            elif terri.doll_dress_state == 5:
                wt_image indy_doll_5_2
                "Like the perfect housewife, your housedoll never asks why you want a blowjob at this hour of the day."
                wt_image indy_doll_5_14
                "It just gets on its knees ..."
                wt_image indy_doll_5_16
                "... and puts its mouth to a more productive use than asking questions."
                wt_image indy_doll_5_31
                $ title = "Where do you want to cum?"
                menu:
                    "In it":
                        wt_image indy_doll_5_32
                        $ terri.swallow_count += 1
                    "On it":
                        wt_image indy_doll_5_17
                        $ terri.facial_count += 1
            elif terri.doll_dress_state == 6:
                wt_image indy_doll_6_13
                "Just like a real slavegirl, your slavedoll considers it natural that you want it on its knees ..."
                wt_image indy_doll_6_14
                "... worshiping your cock ..."
                wt_image indy_doll_6_15
                "... and your balls ..."
                wt_image indy_doll_6_17
                "... for as long as it takes you to decide you want to cum."
                wt_image indy_doll_6_16
                $ title = "Where do you want to cum?"
                menu:
                    "In its mouth":
                        wt_image indy_doll_6_30
                        $ terri.swallow_count += 1
                    "On its face":
                        wt_image indy_doll_6_18
                        $ terri.facial_count += 1
            elif terri.doll_dress_state == 7:
                wt_image indy_doll_7_19
                "Nobody ever became a trophy wife without at least feigning excitement at the opportunity to suck cock."
                wt_image indy_doll_7_20
                "[terri.name] the Woman tried to enjoy worshiping cock ..."
                wt_image indy_doll_7_21
                "... and balls ..."
                wt_image indy_doll_7_22
                "... but it didn't come easily to her."
                wt_image indy_doll_7_23
                "[terri.full_name], on the other hand, looks perfectly natural with your dick in its mouth."
                wt_image indy_doll_7_24
                $ title = "Where do you want to cum?"
                menu:
                    "In its mouth":
                        wt_image indy_doll_7_25
                        $ terri.swallow_count += 1
                    "On its face":
                        wt_image indy_doll_7_26
                        $ terri.facial_count += 1
            elif terri.doll_dress_state == 8:
                wt_image indy_doll_8_2
                "Every schoolgirl's initial reaction to the idea of putting a boy's dick in their mouth is ..."
                wt_image indy_doll_8_9
                '"Eww ... Ick!"'
                wt_image indy_doll_8_10
                "They all end up down here anyway, once the right boy comes along."
                wt_image indy_doll_2_20
                $ terri.facial_count += 1
            player.c "[player.orgasm_text]"
            $ terri.blowjob_count += 1
            orgasm notify
        "Sex":
            if terri.doll_dress_state == 1:
                wt_image indy_doll_1_27
                "You undress the doll to get access to the hole you want."
                wt_image indy_doll_1_46
                $ title = "Where do you put the doll to fuck it?"
                menu:
                    "On its back":
                        wt_image indy_doll_1_8
                        "Lots of real women like to be fucked on their back, a comfortable position where they can see and connect with their partner ..."
                        wt_image indy_doll_1_31
                        "But those things don't matter to dolls, so you can focus on what looks and feels good to you ..."
                        wt_image indy_doll_1_48
                        "... regardless of whether a real woman would find it comfortable ..."
                        wt_image indy_doll_1_32
                        "... uncomfortable ..."
                        wt_image indy_doll_1_33
                        "... or even possible."
                        wt_image indy_doll_1_49
                    "On top of you":
                        wt_image indy_doll_1_34
                        "Your toy never weighed much even when it was a real girl ..."
                        wt_image indy_doll_1_50
                        "... it's even easier now to pick it up and drop it onto your cock ..."
                        wt_image indy_doll_1_35
                        "... and bounce her up and down on your cock ..."
                        wt_image indy_doll_1_36
                        "... for as long as that amuses you."
                        wt_image indy_doll_1_37
                    "Standing up":
                        wt_image indy_doll_1_28
                        "Your toy doesn't get uncomfortable, so you can put it in a position that gives you easy access ..."
                        wt_image indy_doll_1_29
                        "... and it'll hold that position no matter how long ..."
                        wt_image indy_doll_1_30
                        "... or how hard you fuck it."
                        wt_image indy_doll_1_47
            elif terri.doll_dress_state == 2:
                wt_image indy_doll_2_2
                "There's no need for foreplay. [terri.name] won't get wet anyway. Some things haven't changed."
                $ title = "How do you want to fuck the naked doll?"
                menu:
                    "Like this":
                        wt_image indy_doll_2_21
                        "Entering [terri.full_name] feels the same as it did when she was a real girl - tight and dry."
                        wt_image indy_doll_2_22
                        "For old times' sake, you place its hand on its clit and tell it to rub."
                        wt_image indy_doll_2_23
                        "It still doesn't get wet. And you still enjoy fucking it, anyway."
                        wt_image indy_doll_2_27
                    "From behind":
                        wt_image indy_doll_2_24
                        "When she was a real girl, you needed to be careful trying to fuck [terri.name] without lube."
                        wt_image indy_doll_2_25
                        "Now you don't need to worry about causing damage. You can just enjoy how it feels to you. And it feels quite nice."
                        wt_image indy_doll_2_26
                    "With it on top":
                        wt_image indy_doll_2_28
                        "[terri.name] slides on easily ..."
                        wt_image indy_doll_2_29
                        "... and stays in place ..."
                        wt_image indy_doll_2_30
                        "... until you've finished with it."
                        wt_image indy_doll_2_31
                    "Like a doll":
                        wt_image indy_doll_2_6
                        "Dolls don't break as easily as real girls.  So where a real girl would worry about what might happen if she falls ..."
                        wt_image indy_doll_2_32
                        "... your doll has no such worries about the future state of it's face should it lose it's grip as you fuck it hard and rough."
                        wt_image indy_doll_2_33
            elif terri.doll_dress_state == 3:
                wt_image indy_doll_3_50
                "You tell your doll to undress ..."
                wt_image indy_doll_3_22
                "... while you assess your options."
                wt_image indy_doll_4_3
                $ title = "How do you want to fuck your doll?"
                menu:
                    "On its back":
                        wt_image indy_doll_3_23
                        "Dolls don't worry about things like foreplay."
                        wt_image indy_doll_3_24
                        "Slow and gentle ..."
                        wt_image indy_doll_3_25
                        "... fast and rough ..."
                        wt_image indy_doll_3_26
                        "... no matter how you fuck it ..."
                        wt_image indy_doll_3_27
                        "... only one of you is cumming.  It's one of the few things that didn't change for [terri.name] the Woman when she became [terri.full_name]."
                        wt_image indy_doll_3_51
                    "From behind":
                        wt_image indy_doll_3_52
                        "Your doll doesn't care if you'd rather look at its ass than its face ..."
                        wt_image indy_doll_3_53
                        "... or that sometimes you fuck it so hard ..."
                        wt_image indy_doll_3_30
                        "... you knock the glasses right off its head."
                        wt_image indy_doll_3_32
                        "Its primary purpose is to be a cum receptacle ..."
                        wt_image indy_doll_3_54
                        "... and it doesn't need glasses for that."
                        wt_image indy_doll_3_33
                    "Standing up":
                        wt_image indy_doll_3_34
                        "A real girl might find this position awkward ..."
                        wt_image indy_doll_3_35
                        "... but your doll doesn't care."
                        wt_image indy_doll_3_55
                        "If you think it should only have one foot on the ground, that's fine with it ..."
                        wt_image indy_doll_3_56
                        "... and if it falls over ..."
                        wt_image indy_doll_3_57
                        "... you just set it back upright ..."
                        wt_image indy_doll_3_37
                        "... and continue fucking it until you're finished."
                        wt_image indy_doll_3_38
                    "With it on top":
                        wt_image indy_doll_3_39
                        "It's surprising how light your doll is, making it easy to lift her up ..."
                        wt_image indy_doll_3_40
                        "... impale her on your cock ..."
                        wt_image indy_doll_3_58
                        "... and bounce her up and down there until your lust is sated."
                        wt_image indy_doll_3_41
            elif terri.doll_dress_state == 4:
                wt_image indy_doll_4_8
                $ title = "How do you want to fuck the bespectacled slut doll?"
                menu:
                    "On its back":
                        wt_image indy_doll_3_23
                        "Dolls don't worry about things like foreplay."
                        wt_image indy_doll_3_24
                        "Slow and gentle ..."
                        wt_image indy_doll_3_25
                        "... fast and rough ..."
                        wt_image indy_doll_3_26
                        "... no matter how you fuck it ..."
                        wt_image indy_doll_3_27
                        "... only one of you is cumming.  It's one of the few things that didn't change for [terri.name] the Woman when she became [terri.full_name]."
                        wt_image indy_doll_3_51
                    "From behind":
                        wt_image indy_doll_3_52
                        "Your doll doesn't care if you'd rather look at its ass than its face ..."
                        wt_image indy_doll_3_53
                        "... or that sometimes you fuck it so hard ..."
                        wt_image indy_doll_3_30
                        "... you knock the glasses right off its head."
                        wt_image indy_doll_3_32
                        "Its primary purpose is to be a cum receptacle ..."
                        wt_image indy_doll_3_54
                        "... and it doesn't need glasses for that."
                        wt_image indy_doll_3_33
                    "Standing up":
                        wt_image indy_doll_3_34
                        "A real girl might find this position awkward ..."
                        wt_image indy_doll_3_35
                        "... but your doll doesn't care."
                        wt_image indy_doll_3_55
                        "If you think it should only have one foot on the ground, that's fine with it ..."
                        wt_image indy_doll_3_56
                        "... and if it falls over ..."
                        wt_image indy_doll_3_57
                        "... you just set it back upright ..."
                        wt_image indy_doll_3_37
                        "... and continue fucking it until you're finished."
                        wt_image indy_doll_3_38
                    "With it on top":
                        wt_image indy_doll_3_39
                        "It's surprising how light your doll is, making it easy to lift her up ..."
                        wt_image indy_doll_3_40
                        "... impale her on your cock ..."
                        wt_image indy_doll_3_58
                        "... and bounce her up and down there until your lust is sated."
                        wt_image indy_doll_3_41
            elif terri.doll_dress_state == 5:
                wt_image indy_doll_5_18
                "Like a good housewife, your doll undresses and waits obediently while you assess your options."
                $ title = "How do you want to fuck the housewife doll?"
                menu:
                    "On its back":
                        wt_image indy_doll_5_22
                        "Every good housewife knows her most important duty is performed on her back."
                        wt_image indy_doll_5_23
                        "Unlike a perfect housewife, however, your housedoll doesn't respond physically to performing its duty.  Not that [terri.name] ever did when she was a real girl, either."
                        wt_image indy_doll_5_24
                        "For old times' sake, you place its hand on its clit."
                        wt_image indy_doll_5_25
                        "Some things don't change.  [terri.name] still doesn't get wet, and you still enjoy yourself anyway."
                        wt_image indy_doll_5_36
                    "From behind":
                        wt_image indy_doll_5_19
                        "Like all good housewives, your housedoll is happy to be turned around and bent over."
                        wt_image indy_doll_5_34
                        "And like a perfect housewife, there's no need for foreplay or worrying about things like how this feels to her."
                        wt_image indy_doll_5_20
                        "All that matters is how it feels to you ... and it feels quite nice."
                        wt_image indy_doll_5_35
                    "With it on top":
                        wt_image indy_doll_5_26
                        "Like a good housewife, your housedoll welcomes being picked up and impaled on your cock."
                        wt_image indy_doll_5_27
                        "And like a perfect housewife, it lets you bounce it up and down on your cock for however long you find that fun."
                        wt_image indy_doll_5_28
            elif terri.doll_dress_state == 6:
                wt_image indy_doll_6_4
                "Like an obedient slave, your doll waits patiently while you assess your options."
                $ title = "How do you want to fuck the slave doll?"
                menu:
                    "On its back":
                        wt_image indy_doll_6_21
                        "Slaves rarely get to lie down when they're being fucked ..."
                        wt_image indy_doll_6_19
                        "... but once it's on its back, a slavedoll can be fucked even harder and faster than a real slavegirl."
                        wt_image indy_doll_6_20
                        "And if the experience of being sexually dominated by you doesn't make it wet like a natural slavegirl ..."
                        wt_image indy_doll_6_22
                        "... that doesn't diminish your enjoyment any."
                        wt_image indy_doll_6_31
                    "From behind":
                        wt_image indy_doll_6_2
                        "Slaves look more natural on their knees.  Unlike some real slavegirls, however ..."
                        wt_image indy_doll_6_23
                        "... kneeling doesn't make your slavedoll wet."
                        wt_image indy_doll_6_24
                        "That doesn't keep it from behaving like a good slave and focusing exclusively on your pleasure ..."
                        wt_image indy_doll_6_25
                        "... including playing with its ass for your amusement while you fuck it."
                        wt_image indy_doll_6_32
                    "With it on top":
                        wt_image indy_doll_6_26
                        "Like a good slavegirl, your slavedoll makes an attractive cocksleeve ..."
                        wt_image indy_doll_6_27
                        "... and can be bounced up and down your cock ..."
                        wt_image indy_doll_6_33
                        "... facing backwards ..."
                        wt_image indy_doll_6_34
                        "... or forwards ..."
                        wt_image indy_doll_6_35
                        "... never stopping ..."
                        wt_image indy_doll_6_36
                        "... until it serves as a cum recepticle as well as a cocksleeve."
                        wt_image indy_doll_6_37
            elif terri.doll_dress_state == 7:
                wt_image indy_doll_7_6
                "Good mistresses and wanna-be trophy wives are ready to go whenever you are.  So are dolls."
                $ title = "How do you want to fuck the trophy doll?"
                menu:
                    "On its back":
                        wt_image indy_doll_7_27
                        "Like [terri.name] the Woman, [terri.full_name] doesn't get wet at the anticipation of intercourse."
                        wt_image indy_doll_7_28
                        "Also like Terri the Woman, that doesn't interfere with your pleasure one bit."
                        wt_image indy_doll_7_29
                        "Sex with [terri.name] has always been only about the guy ..."
                        wt_image indy_doll_7_30
                        "... turning her into a doll just made things simpler for everyone."
                        wt_image indy_doll_7_31
                    "From behind":
                        wt_image indy_doll_7_5
                        "Trophy wives - and trophy dolls - understand you're at least as interested in how their ass looks as you are in how their face looks ..."
                        wt_image indy_doll_7_32
                        "... and aren't the least bit surprised to be turned around for the purposes of sex."
                        wt_image indy_doll_7_33
                        "Being a cocksleeve is the reason they're kept around ..."
                        wt_image indy_doll_7_34
                        "... and a cocksleeve doesn't care which direction it's facing, regardless of whether it's a trophy wife being treated like an object ..."
                        wt_image indy_doll_7_35
                        "... or a trophy doll that's actually become an object."
                        wt_image indy_doll_7_36
                    "With it on top":
                        wt_image indy_doll_7_37
                        "Trophy wives are traditionally light-weight, but your doll is especially easy to pick up and put where you want it."
                        wt_image indy_doll_7_38
                        "It fits comfortably and securely over your cock ..."
                        wt_image indy_doll_7_39
                        "... where it stays while you bounce it up-and-down ..."
                        wt_image indy_doll_7_40
                        "... and spin it round-and-round ..."
                        wt_image indy_doll_7_41
                        "... until you've had your fun."
                        wt_image indy_doll_7_42
            elif terri.doll_dress_state == 8:
                wt_image indy_doll_8_11
                "Good schoolgirls don't let boys take off their panties, but you're not about to give your doll the opportunity to be good."
                $ title = "How do you want to fuck the schoolgirl doll?"
                menu:
                    "On its back":
                        wt_image indy_doll_8_12
                        "Most schoolgirls have wet dreams about being touched by a boy 'down there'."
                        wt_image indy_doll_8_13
                        "Not [terri.name], of course.  Not even before she became a doll and ceased having dreams of any sort."
                        wt_image indy_doll_8_14
                        "A doll also can't have babies, which means unlike real schoolgirls ..."
                        wt_image indy_doll_8_15
                        "... your doll doesn't care whether you pull out."
                        wt_image indy_doll_2_27
                    "From behind":
                        wt_image indy_doll_8_16
                        "Schoolgirls are too young to appreciate humiliation."
                        wt_image indy_doll_8_17
                        "So unlike your doll, they shouldn't naively let boys roll them over ..."
                        wt_image indy_doll_8_18
                        "... and fuck them like an animal until the boy marks them as his territory."
                        wt_image indy_doll_8_27
                    "With it on top":
                        wt_image indy_doll_8_13
                        "Schoolgirls are light and easily folded into compact packages."
                        wt_image indy_doll_8_19
                        "Your doll is particularly light, and can be lifted up using any convenient hole or holes for a grip ..."
                        wt_image indy_doll_8_20
                        "... and bounced up-and-down on your cock for as long as it amuses you."
                        wt_image indy_doll_2_31
                    "Like a doll":
                        wt_image indy_doll_8_21
                        "Schoolboys are usually the risk takers, not schoolgirls.  Most schoolgirls wouldn't let you pick them up like this ..."
                        wt_image indy_doll_8_22
                        "... and fuck them in such a precarious position."
                        wt_image indy_doll_8_23
                        "Fortunately, unlike a real schoolgirl, your doll won't break if you drop it on its head.  Which you likely will when you cum."
                        wt_image indy_doll_8_24
            player.c "[player.orgasm_text]"
            $ terri.sex_count += 1
            orgasm notify
        "Anal":
            if terri.doll_dress_state == 1:
                wt_image indy_doll_1_39
                "You have to turn your doll around ..."
                wt_image indy_doll_1_23
                "... and disrobe it ..."
                wt_image indy_doll_1_24
                "... to access the hole you're interested in."
                wt_image indy_doll_1_25
                "But once you do, your toy doesn't care which opening you chose to put your dick into ..."
                wt_image indy_anal_10
                "... and unlike a real girl, you can't damage it by fucking it too hard, too fast, or too long."
                wt_image indy_doll_1_26
            elif terri.doll_dress_state == 2:
                wt_image indy_doll_2_6
                "You turn your doll around ..."
                wt_image indy_doll_2_7
                "... to get easy access to the hole you're interested in."
                wt_image indy_anal_10
                "The best thing about ass fucking a doll is that you can't damage it, no matter how hard, how fast, or how long you fuck it."
                wt_image indy_anal_11
            elif terri.doll_dress_state == 3:
                wt_image indy_doll_3_42
                "You reposition your doll ..."
                wt_image indy_doll_3_43
                "... to give you access to the hole you're interested in."
                wt_image indy_anal_10
                "The best thing about ass fucking a doll is that you can't damage it, no matter how hard, how fast, or how long you fuck it."
                wt_image indy_anal_11
            elif terri.doll_dress_state == 4:
                wt_image indy_doll_4_4
                "You reposition your doll ..."
                wt_image indy_doll_3_43
                "... to give you access to the hole you're interested in."
                wt_image indy_anal_10
                "The best thing about ass fucking a doll is that you can't damage it, no matter how hard, how fast, or how long you fuck it."
                wt_image indy_anal_11
            elif terri.doll_dress_state == 5:
                wt_image indy_doll_5_29
                "A good housewife - like a good doll - has three holes that can be used for pleasure."
                wt_image indy_doll_5_37
                "With a perfect housewife, the back hole is always on the menu ..."
                wt_image indy_anal_10
                "... and open to your cock for as often and as long as you want to make use of it."
                wt_image indy_anal_11
            elif terri.doll_dress_state == 6:
                wt_image indy_doll_6_2
                "Like a real slavegirl, your slavedoll is here to please ..."
                wt_image indy_doll_6_28
                "... presenting you with ready access ..."
                wt_image indy_doll_6_29
                "... to whatever hole you want."
                wt_image indy_anal_10
                "And unlike a real slavegirl, you can't damage your doll by ass fucking it, no matter how hard, how fast, or how long you ream it."
                wt_image indy_anal_11
            elif terri.doll_dress_state == 7:
                wt_image indy_doll_7_52
                "Some trophy wives worry that giving up the back door too easily changes them from prospective trophy to easy whore ..."
                wt_image indy_doll_7_43
                "... but your trophy doll doesn't worry about such nonsense."
                wt_image indy_anal_10
                "You can fuck its ass as often as you want ..."
                wt_image indy_doll_7_44
                "... as hard, long, and rough as you want to fuck it, too.  It's not a real girl, you can't break it.  Not like this, anyway."
                wt_image indy_anal_11
            elif terri.doll_dress_state == 8:
                wt_image indy_doll_8_25
                "Smart schoolgirls know it's better to offer a boy their ass than their pussy."
                wt_image indy_anal_10
                "It might hurt a lot more, but no schoolgirl ever got pregnant from a load of sperm up their ass."
                wt_image indy_anal_11
            player.c "[player.orgasm_text]"
            $ terri.anal_count += 1
            orgasm notify
        "Never mind":
            pass
    wt_image current_location.image
    return

########### OBJECTS ###########
## Common Objects
# Contact Former Client
label terri_contact:
    # first check to see if she just had a boob job
    if terri.boobjob_interest == 6 and not terri.has_tag('boob_job'):
        pass #skips cheerleader outfit tests
    # check for cheerleader outfit if you gave her this lingerie and she isn't under Cassandra's control
    elif terri.cheerleader_outfit_visit > 0 and not cassandra.independent_encounter_status > 1 and not terri.has_tag('futanari'):
        $ terri.cheerleader_outfit_visit += 1
        if terri.cheerleader_outfit_visit > 6:
            $ terri.cheerleader_outfit_visit = 4
    # 1st visit in cheerleader outfit
    if terri.cheerleader_outfit_visit == 3 and not terri.has_tag('no_cheerleader_visits') and not cassandra.independent_encounter_status > 1 and not terri.has_tag('futanari'):
        if terri.has_tag('boob_job'):
            call terri_contact_cheerleader_boob_job from _call_terri_contact_cheerleader_boob_job
        else:
            summon terri to living_room
            wt_image indy_cheerleader_1_1
            "[terri.name] shows up at your door, wearing her cheerleader outfit."
            wt_image indy_cheerleader_1_2
            terri.c "I hope you don't mind that I wore this.  During my training you said I should wear it around the house whenever I felt like it, but today I felt like wearing it to visit you."
            wt_image indy_cheerleader_1_16
            "She plunks down on the floor, like a teenager might.  She seems to be imagining herself as a teenager right now."
        add tags 'cheerleader_visit_now' to terri
    # continuing visits in cheerleader outfit
    elif terri.cheerleader_outfit_visit == 6 and not terri.has_tag('no_cheerleader_visits') and not cassandra.independent_encounter_status > 1 and not terri.has_tag('futanari'):
        if terri.has_tag('boob_job'):
            call terri_contact_cheerleader_boob_job from _call_terri_contact_cheerleader_boob_job_1
        else:
            summon terri to living_room
            wt_image indy_cheerleader_1_1
            "[terri.name] shows up wearing her cheerleader outfit."
            wt_image indy_cheerleader_1_2
            terri.c "This outfit is so fun.  Thank you again for getting it for me."
            wt_image indy_cheerleader_1_16
            "She plunks down on the floor, like a teenager might.  She seems to be imagining herself as a teenager right now."
        add tags 'cheerleader_visit_now' to terri
    # futanari content
    elif terri.has_tag('futanari'):
        $ terri.futanari_outfit += 1
        if terri.futanari_outfit > 3:
            $ terri.futanari_outfit = 2
        # first contact post transformation phone call
        if terri.futanari_outfit == 1:
            wt_image indy_futanari_1_1
            player.c "How are you adapting to life with a cock, [terri.name]?"
            terri.c "I'm horny.  Intensely horny.  I can't stop touching my cock."
        # continuing visits, white dress outfit
        elif terri.futanari_outfit == 2:
            wt_image indy_futanari_2_1
            player.c "How are you feeling today, [terri.name]?"
            terri.c "Not bad, actually.  I think I jerked off enough yesterday that I feel more like a normal human today."
        # continuing visits, mini skirt outfit
        else:
            wt_image indy_futanari_1_1
            player.c "How are you feeling today, [terri.name]?"
            terri.c "I'm having a horny day.  All I can think about is getting off."
        $ title = "Invite her over?"
        menu:
            "Yes, ask her to visit":
                summon terri to living_room
                # first visit
                if terri.futanari_outfit == 1:
                    wt_image front_door
                    "[terri.name] arrives quickly."
                    wt_image indy_futanari_1_23
                    terri.c "Thanks for inviting me over.  I haven't been comfortable spending time with other people since ... well, since this happened."
                    wt_image indy_futanari_1_24
                    terri.c "I hope you don't mind me leaving it hanging out like this while we talk?  Sometimes the urge to touch it is so intense, I just need to stroke it a bit to make the urge go away."
                    wt_image indy_futanari_1_25
                # subsequent visit, white dress
                elif terri.futanari_outfit == 2:
                    wt_image front_door
                    "[terri.name] arrives promptly ..."
                    wt_image indy_futanari_2_3
                    "... taking a seat on your couch."
                    wt_image indy_futanari_2_4
                    terri.c "Thanks for inviting me over.  I don't get to socialize as much as I'd like anymore.  I'm looking forward to talking with you."
                # subsequent visit, short skirt
                else:
                    wt_image front_door
                    "[terri.name] arrives quickly."
                    wt_image indy_futanari_1_24
                    "... letting her cock hang loose as soon as she steps inside."
                    wt_image indy_futanari_1_25
                    terri.c "I'm probably going to need to play with myself while we talk.  I hope you don't mind."
            "Not today":
                if terri.futanari_outfit == 1:
                    $ terri.futanari_outfit = 0 ## to make sure first visit is in short skirt
                else:
                    $ terri.training_session() ## to keep her from changing mood in the same day
                wt_image current_location.image
    # continuing post-book job visit
    elif terri.has_tag('boob_job'):
        summon terri to living_room
        if terri.has_tag('strips_on_visit'):
            wt_image indy_boob_job_1_15
            "You invite [terri.name] over for a drink, and she happily joins you."
            wt_image indy_boob_job_1_2
            "As soon as she arrives she pulls open her dress ..."
            wt_image indy_boob_job_1_3
            "... giving you a nice view of her surgically enhanced breasts ..."
            wt_image indy_boob_job_1_14
            "... then sits down and waits while you fix the drinks."
            if terri.has_tag('love_potion_used'):
                terri.c "Thank you so much for inviting me over. I so love when we get to spend time together! You are so amazingly good to me! I never thought I could have a friend like you."
            add tags 'boobs_out_now' to terri
        else:
            wt_image indy_boob_job_1_15
            "You invite [terri.name] over for a drink, and she happily joins you, taking a seat as you fix the drinks."
            wt_image indy_boob_job_1_5
            if terri.has_tag('love_potion_used'):
                terri.c "Thank you so much for inviting me over. I so love when we get to spend time together! You are so amazingly good to me! I never thought I could have a friend like you."
            else:
                terri.c "Mmmmm.  That looks good."
        add tags 'regular_visit_now' to terri
    # 1st post-boob job visit
    elif terri.boobjob_interest == 6:
        summon terri to living_room
        wt_image indy_boob_job_1_1
        "You invite [terri.name] over for a drink, and she happily joins you."
        terri.c "I did it!"
        player.c "Did what?"
        terri.c "The breast enhancement. Just like you suggested. Can't you tell?"
        wt_image indy_boob_job_1_2
        terri.c "Here, I'll show you ..."
        wt_image indy_boob_job_1_3
        terri.c "Quite a difference, isn't it? My boyfriend was really surprised when he saw them."
        wt_image indy_boob_job_1_2
        terri.c "Thanks for convincing me to do this. I don't know why I was so reluctant. I can see now that these are much better for men."
        player.c "Guess that goes along with being an airhead."
        wt_image indy_boob_job_1_4
        "She giggles."
        terri.c "Men are going to call me that more often now, aren't they?"
        wt_image indy_boob_job_1_5
        "[terri.name] has a seat while you fix the two of you a drink."
        add tags 'boob_job' 'regular_visit_now' to terri
    # regular visit
    else:
        summon terri to living_room
        wt_image indy_drink_1_1
        "You invite [terri.name] over for a drink, and she happily joins you."
        wt_image indy_drink_1_2
        if terri.has_tag('love_potion_used'):
            terri.c "Thank you so much for inviting me over.  I so love when we get to spend time together!  You are so amazingly good to me!  I never thought I could have a friend like you."
        else:
            terri.c "Mmmmm.  That looks good."
        wt_image indy_drink_1_4
        add tags 'regular_visit_now' to terri
    return

label terri_contact_cheerleader_boob_job:
    summon terri to living_room
    wt_image indy_cheerleader_2_2
    if not terri.has_tag('cheerleader_boob_job_visit_before'):
        add tags 'cheerleader_boob_job_visit_before' to terri
        "[terri.name] arrives at your door, wearing a new cheerleader dress."
        terri.c "The cheerleader outfit you bought me doesn't fit since I upsized my boobies, so I bought this new one to replace it."
        wt_image indy_cheerleader_2_3
        terri.c "I hope you like it, because I'd like to wear it sometimes when I come to visit you."
        wt_image indy_cheerleader_2_4
        terri.c "I don't look as young as I did in the other outfit, but at least I'm not flat-chested anymore, so hopefully you like me in this look."
    else:
        "[terri.name] arrives at your door in her cheerleader outfit."
        wt_image indy_cheerleader_2_2
        terri.c "Dressing like a cheerleader is so fun, even if I'm now a bouncy, big-boobed cheerleader instead of looking like a just developing, flat-chested cheerleader."
    if terri.has_tag('strips_on_visit'):
        wt_image indy_cheerleader_2_5
        "She doesn't expose her breasts, presumably because she wants to keep the cheerleader outfit intact, but she does spread her legs wide so you can see her thighs and panties as she takes a seat."
    else:
        wt_image indy_cheerleader_2_1
    return

label terri_contact_talk:
    if terri.has_tag('cheerleader_visit_now') and terri.has_tag('boob_job'):
        if terri.has_tag('strips_on_visit'):
            wt_image indy_cheerleader_2_5
        else:
            wt_image indy_cheerleader_2_1
    elif terri.has_tag('cheerleader_visit_now'):
        wt_image indy_cheerleader_1_16
    elif terri.has_tag('boob_job'):
        wt_image indy_drink_2_1
    else:
        wt_image indy_drink_1_3
    $ title = "What do you want to talk to her about?"
    menu menu_terri_contact_talk:
        "Discuss transformation" if player.has_item(transformation_potion) and terri.discussed_transformation == 0 and terri.lesbian_clues > 2:
            call terri_transformation_discussion from _call_terri_transformation_discussion
        "Suggest you have sex":
            if terri.has_tag('cheerleader_visit_now') and terri.has_tag('boob_job'):
                wt_image indy_cheerleader_2_4
                if terri.visit_sex_count > 3:
                    terri.c "Awwww, do I have to pay for a remedial lesson again today?  I was hoping I could just sit here and look pretty in my cheerleader outfit."
                elif terri.visit_sex_count > 0:
                    terri.c "I don't want a remedial lesson today, I just want to sit here and look pretty in my cheerleader outfit.  I hope that's okay?"
                else:
                    terri.c "What?!  No!  I'm just here to look pretty in my cheerleader outfit, that's all."
                $ title = "What do you suggest?"
                menu:
                    "Blow job" if terri.visit_sex_count > 3:
                        player.c "Sorry, [terri.name], but you should practice your blow jobs.  You remember what the first step is, right?"
                        wt_image indy_cheerleader_2_6
                        terri.c "I'm supposed to get naked."
                        wt_image indy_cheerleader_2_7
                        player.c "And once you're naked, what do you do?"
                        wt_image indy_cheerleader_2_18
                        terri.c "Kneel in front of you and make your cock feel good?"
                        wt_image indy_cheerleader_2_19
                        player.c "Not just my cock, airhead.  What else?"
                        wt_image indy_cheerleader_2_20
                        terri.c "Your balls?"
                        wt_image indy_cheerleader_2_21
                        player.c "Normally I'd have said that was obvious, but considering what a ditz you are, congratulations on figuring that out."
                        wt_image indy_cheerleader_2_20
                        terri.c "Thank you"
                        wt_image indy_cheerleader_2_22
                        player.c "Don't talk, suck."
                        wt_image indy_cheerleader_2_23
                        "She does, and although her technique remains horrible, she eventually manages to suction enough stimulation that you're ready to fill the ditz with cum."
                        wt_image indy_cheerleader_2_24
                        $ title = "Where do you want to cum?"
                        menu:
                            "In her":
                                wt_image indy_cheerleader_2_25
                                player.c "[player.orgasm_text]"
                                wt_image indy_cheerleader_2_24
                                player.c "What happens now?"
                                wt_image indy_cheerleader_2_20
                                terri.c "I show you I swallowed?"
                                wt_image indy_cheerleader_2_18
                                player.c "Correct.  Try to remember what you learned, airhead, or you'll need me to charge you for remedial lessons forever."
                                wt_image indy_cheerleader_2_6
                                terri.c "I'll try to remember.  Thanks for the lesson.  I'll send your payment at the end of the week."
                                $ terri.swallow_count +=1
                            "On her":
                                wt_image indy_cheerleader_2_18
                                player.c "Hold still."
                                wt_image indy_cheerleader_2_26
                                player.c "[player.orgasm_text]"
                                wt_image indy_cheerleader_2_27
                                player.c "What happens now?"
                                wt_image indy_cheerleader_2_28
                                terri.c "I clean off your cock?"
                                wt_image indy_cheerleader_2_29
                                player.c "Correct.  Try to remember what you learned, airhead, or you'll need me to charge you for remedial lessons forever."
                                wt_image indy_cheerleader_2_30
                                terri.c "I'll try to remember.  Thanks for the lesson.  I'll send your payment at the end of the week."
                                $ terri.facial_count += 1
                        call character_location_return(terri) from _call_character_location_return_713
                        wt_image current_location.image
                        $ player.extra_clients_fee_this_week += terri.pay
                        $ terri.blowjob_count += 1
                        orgasm notify
                    "Sex" if terri.visit_sex_count > 3:
                        wt_image indy_cheerleader_2_11
                        player.c "Sorry, [terri.name], but I want to make sure you haven't forgotten what I told you about having sex.  Get naked and spread your legs."
                        wt_image indy_cheerleader_2_31
                        "She takes her panties off, but keeps the cheerleader dress on as she lies back and opens her legs for you."
                        wt_image indy_cheerleader_2_32
                        "She's not completely dry when you place the head of your cock against her, which is unusual for her. Wearing the cheerleader outfit seems to have aroused [terri.name], which makes entering her easier than normal. She even moans slightly as you penetrate her."
                        terri.c "ohhh"
                        wt_image indy_cheerleader_2_33
                        "It's strange to be fucking [terri.name] when she's - well, not exactly into it, but not completely divorced from the experience, either."
                        wt_image indy_cheerleader_2_32
                        "She even moves a little while you're fucking her, helping bring you to climax."
                        player.c "[player.orgasm_text]"
                        wt_image indy_cheerleader_2_34
                        terri.c "That was a lot of cum.  I think I might be getting better at fucking.  It even felt better to me today.  Thanks for the lesson!  I'll send your payment at the end of the week."
                        wt_image indy_cheerleader_2_2
                        "She leaves, seemingly happy with herself and you, not realizing that she forgot to put her panties back on and will have a wet mess running down her legs by the time she gets home."
                        call character_location_return(terri) from _call_character_location_return_714
                        wt_image current_location.image
                        $ player.extra_clients_fee_this_week += terri.pay
                        $ terri.sex_count += 1
                        orgasm notify
                    "You'll eat her out" if terri.visit_sex_count > 3:
                        player.c "You still need work learning how to cum, [terri.name].  I think today's a good day for us to work on that.  Get naked and spread your legs."
                        wt_image indy_cheerleader_2_31
                        "She takes her panties off, but keeps the cheerleader dress on as she lies back and opens her legs for you."
                        terri.c "You might be right.  I'm feeling really soaked."
                        wt_image indy_cheerleader_2_35
                        "In reality, she's barely wet as you start, but as she holds herself open for you and closes her eyes, she gets steadily more aroused, until you can taste her juices on your tongue."
                        $ title = "What now?"
                        menu menu_terri_cheerleader_boob_job_eat_her:
                            "Lick her pussy":
                                wt_image indy_cheerleader_2_35
                                "Her cunt is wet and flowing with juices for you to lap up as she moans."
                                terri.c "oohhhhh"
                                jump menu_terri_cheerleader_boob_job_eat_her
                            "Lick her asshole":
                                wt_image indy_cheerleader_2_36
                                if terri.has_item(butt_plug):
                                    "Her cute, little rosebud has been sufficiently trained by the butt plug you bought her that you can work your tongue inside it without any difficulty."
                                elif terri.anal_count > 0:
                                    "Compared to taking your cock, it's a lot easier for her to relax enough for you to work your tongue into her cute, little rosebud."
                                else:
                                    "Her cute little rosebud is so tight, it's difficult to work your tongue inside it, but [terri.name] doesn't seem to mind as you do."
                                terri.c "OH!  oohhh"
                                jump menu_terri_cheerleader_boob_job_eat_her
                            "Make her cum":
                                wt_image indy_cheerleader_2_37
                                "Aroused as she is, [terri.name]'s clit still shirks from direct contact, and you have to tease it out from under its hood before you can apply enough contact to make her cum.  Perhaps involuntarily, she pushes you away as the intensity of the sensation overwhelms her."
                                wt_image indy_cheerleader_2_34
                                terri.c "Oooohhhhhh!!!!"
                                wt_image indy_cheerleader_2_38
                                terri.c "Whew!  Do orgasms always feel like that?"
                                player.c "Good ones do."
                                wt_image indy_cheerleader_2_2
                                terri.c "Thank you for teaching me how to have a good orgasm in my cheerleader outfit!  I'll try to remember to wear this outfit more often.  I'll send your payment at the end of the week."
                                $ terri.cheerleader_outfit_visit = 4 # shortens time until she wears the outfit again by one week
                                $ terri.pleasure_her_count += 1
                                $ terri.orgasm_count += 1
                            "Stop there":
                                wt_image indy_cheerleader_2_38
                                "[terri.name] looks at you with confusion as you stop."
                                player.c "It doesn't seem like you're going to be able to cum today, [terri.name]."
                                wt_image indy_cheerleader_2_31
                                terri.c "Really?  I thought I was getting close."
                                player.c "Do you feel needy between your legs?  Like you need something pressed up against your sex and rubbing it?"
                                wt_image indy_cheerleader_2_34
                                terri.c "Yes!  That's exactly how I feel."
                                wt_image indy_cheerleader_2_31
                                player.c "Take your hand away.  That sensation means you'll need future lessons."
                                terri.c "Okay.  I'll send your payment for this lesson at the end of the week, and then maybe we can work on teaching me how to cum again soon?"
                        call character_location_return(terri) from _call_character_location_return_715
                        wt_image current_location.image
                        $ player.extra_clients_fee_this_week += terri.pay
                        change player energy by -energy_short notify
                    "Spank her":
                        player.c "Turn around and present your bum to me, young lady.  I'm going to spank you."
                        wt_image indy_cheerleader_2_5
                        terri.c "Young lady?  Ummm, okay."
                        wt_image indy_cheerleader_2_8
                        terri.c "I guess I should have been more polite to you.  Is that why I'm being spanked like a little girl?"
                        player.c "Sure, airhead, if that's what you'd like to think.  Stick out your bum."
                        $ title = "Tell her to count?"
                        menu:
                            "Yes, count the spanks":
                                add tags 'counting_now' to terri
                            "No, not today":
                                rem tags 'counting_now' from terri
                        wt_image indy_cheerleader_2_9
                        "*smack*  *smack*  *smack*"
                        if terri.has_tag('counting_now'):
                            terri.c "That's one.  That's two.  Ow!  That's three.  I'm sorry I wasn't more polite!"
                        else:
                            terri.c "Ow!  I'm sorry I wasn't more polite!"
                        wt_image indy_cheerleader_2_8
                        $ terri.temporary_count = 3
                        $ title = "What now?"
                        menu menu_terri_cheerleader_boob_job_spanking:
                            "Spank her again":
                                wt_image indy_cheerleader_2_9
                                "*smack*"
                                $ terri.temporary_count += 1
                                if terri.temporary_count > 9:
                                    if terri.has_tag('counting_now'):
                                        terri.c "Ooowwww!!!  That's [terri.temporary_count.to_s]!  Do I get a safeword or something?  Like 'my bum is so sore I need you to stop now?'"
                                    else:
                                        terri.c "Ooowwww!!!  Do I get a safeword or something?  Like 'my bum is so sore I need you to stop now?'"
                                    "She's had enough and your hand is pretty sore from spanking her, anyway.  Time to stop."
                                else:
                                    if terri.temporary_count < 6:
                                        if terri.has_tag('counting_now'):
                                            terri.c "Oww!!  That's [terri.temporary_count.to_s]!"
                                        else:
                                            terri.c "Oww!!"
                                    elif terri.temporary_count == 6:
                                        if terri.has_tag('counting_now'):
                                            terri.c "Oww!!  That's [terri.temporary_count.to_s]!  I remembered to say I was sorry, didn't I?  In case I didn't, I'm sorry I wasn't polite."
                                        else:
                                            terri.c "Oww!!  I remembered to say I was sorry, didn't I?  In case I didn't, I'm sorry I wasn't polite!"
                                    elif terri.temporary_count == 7:
                                        if terri.has_tag('counting_now'):
                                            terri.c "Oww!!  That's [terri.temporary_count.to_s]!  Oh, wow!  That stings!!"
                                        else:
                                            terri.c "Oww!!  Oh, wow!  That stings!!"
                                    elif terri.temporary_count == 8:
                                        if terri.has_tag('counting_now'):
                                            terri.c "Oowww!!!  That's [terri.temporary_count.to_s]!"
                                        else:
                                            terri.c "Oowww!!!"
                                    elif terri.temporary_count == 9:
                                        if terri.has_tag('counting_now'):
                                            terri.c "Oowww!!!  That's [terri.temporary_count.to_s]!  My bum's really sore now!!"
                                        else:
                                            terri.c "Oowww!!!  My bum's really sore now!!"
                                    wt_image indy_cheerleader_2_8
                                    jump menu_terri_cheerleader_boob_job_spanking
                            "Send her home":
                                pass
                        wt_image indy_cheerleader_2_10
                        if terri.temporary_count < 6:
                            terri.c "Being spanked is no fun, but being treated like a young cheerleader who's earned a spanking is kind of hot, so I'm not sure what to think right now."
                            change player energy by -energy_very_short
                        elif terri.temporary_count < 9:
                            terri.c "Being spanked is no fun, but being treated like a young cheerleader who's earned a spanking is kind of hot, so I'm not sure what to think right now, other than that my bum is sore."
                            change player energy by -energy_short
                        else:
                            terri.c "Being spanked is no fun, but being treated like a young cheerleader who's earned a spanking is kind of hot, so I'm not sure what to think right now, other than that my bum is very sore."
                            change player energy by -energy_short
                        player.c "Try not to think at all, airhead, you're not good at it.  Just try and remember to do what I tell you, like a good, brainless cheerleader."
                        wt_image indy_cheerleader_2_2
                        terri.c "Okay, I'll try.  Bye!"
                        call character_location_return(terri) from _call_character_location_return_716
                        wt_image current_location.image
                        $ terri.temporary_count = 0
                        if terri.submission < 50:
                            change terri submission by 5 notify
                    "She just get naked":
                        wt_image indy_cheerleader_2_11
                        player.c "You can look like a pretty cheerleader with your clothes off.  Take your panties off and I'll show you."
                        wt_image indy_cheerleader_2_12
                        terri.c "Do I really still look pretty in this outfit now, or do I just look slutty?"
                        player.c "Hmmm.  Do a cheer with your pussy exposed and let me see."
                        wt_image indy_cheerleader_2_13
                        "Grabbing her pom poms, she does her best to do a cheer while keeping her sex exposed to your gaze."
                        $ title = "What do you tell her?"
                        menu:
                            "She looks pretty like that":
                                wt_image indy_cheerleader_2_14
                                terri.c "Really?  Thanks!"
                            "She'd be better off naked":
                                wt_image indy_cheerleader_2_6
                                player.c "You'll look less lewd if you take the dress off, too."
                                wt_image indy_cheerleader_2_15
                                terri.c "But now I don't look like a cheerleader, I just look naked."
                                player.c "You'll look like a cheerleader once you do a cheer."
                                wt_image indy_cheerleader_2_16
                                "Picking her pom poms back up, she attempts another cheer, this time completely naked."
                                player.c "Much better.  You're pretty and sexy and showing off your enhanced assets."
                                wt_image indy_cheerleader_2_17
                                terri.c "Really?  Well, as long as I still look like a cheerleader, I guess this is okay."
                        "She stays like that until you're tired of talking with her and send her home."
                        call character_location_return(terri) from _call_character_location_return_717
                        wt_image current_location.image
                    "Nothing":
                        if terri.has_tag('strips_on_visit'):
                            wt_image indy_cheerleader_2_5
                        else:
                            wt_image indy_cheerleader_2_1
                        terri.c "Thanks for being so understanding."
            elif terri.has_tag('cheerleader_visit_now'):
                player.c "You look really hot in that outfit, [terri.name].  It's turning me on, seeing you wear it."
                wt_image indy_cheerleader_1_18
                terri.c "Really?  I'm glad you like it.  It turns me on a little, too, when I wear it.  But I shouldn't cheat on my boyfriend, not now that my training's over."
                $ title = "What do you suggest?"
                menu:
                    "Blow job":
                        wt_image indy_cheerleader_1_19
                        player.c "Cheerleaders blow guys they like, [terri.name].  You know that.  It's part of what makes them so popular."
                        wt_image indy_cheerleader_1_20
                        terri.c "I do like you, and I'm grateful to you for buying me this outfit.  And I can feel that wearing the outfit really has made you hard."
                        wt_image indy_cheerleader_1_21
                        terri.c "I guess it wouldn't hurt anybody if I sucked you off, like if we were kids hiding under the school bleachers."
                        wt_image indy_cheerleader_1_22
                        "She gets into this blowjob more than she normally gets into sex, and you expect it's because she's thinking of a younger version of herself sucking off you - or somebody."
                        wt_image indy_cheerleader_1_23
                        terri.c "You need to cum in my mouth.  I don't want a mess on my outfit the teachers could see."
                        wt_image indy_cheerleader_1_24
                        "That's an easy request to honor, considering how nice her warm, wet mouth feels on your cock."
                        player.c "[player.orgasm_text]"
                        wt_image indy_cheerleader_1_23
                        terri.c "Wow, that was a big load.  You really do like seeing me dressed up as a cheerleader."
                        wt_image indy_cheerleader_1_18
                        terri.c "I enjoyed that.  I know I shouldn't enjoy cheating on my boyfriend, but that was a fun fantasy to act out with you."
                        wt_image indy_cheerleader_1_2
                        "She seems happy as she leaves."
                        call character_location_return(terri) from _call_character_location_return_718
                        wt_image current_location.image
                        $ terri.blowjob_count += 1
                        $ terri.swallow_count += 1
                        orgasm notify
                    "Sex":
                        wt_image indy_cheerleader_1_26
                        player.c "Sexy young cheerleaders sometimes let guys get all the way to home base with them, especially when they've been making out with a boy they like."
                        wt_image indy_cheerleader_1_32
                        "Before she can respond, you kiss her, and she immediately starts kissing you back."
                        wt_image indy_cheerleader_1_28
                        player.c "You're going to let me get to home base with you, aren't you [terri.name]?"
                        terri.c "I guess.  I do like you a lot."
                        wt_image indy_cheerleader_1_33
                        player.c "I like you, too, especially when you use your sexy young cheerleader mouth to get me hard before you put me inside you."
                        wt_image indy_cheerleader_1_34
                        "Once her mouth has you fully erect, [terri.name] climbs on top of you ..."
                        wt_image indy_cheerleader_1_35
                        "... and slowly sinks down, taking your length inside her as her tight pussy gradually stretches to accommodate you."
                        wt_image indy_cheerleader_1_36
                        "Then she turns around, keeping your cock inside her ..."
                        wt_image indy_cheerleader_1_37
                        "... and leans forward, encouraging you to take her from behind."
                        wt_image indy_cheerleader_1_38
                        "That position doesn't seem to be quite what she's looking for either ..."
                        wt_image indy_cheerleader_1_39
                        "... and she turns over to face you, watching you with a strange dispassion as you use her tight pussy to get yourself off."
                        wt_image indy_cheerleader_1_40
                        $ title = "Where do you want to cum?"
                        menu:
                            "In her":
                                wt_image indy_cheerleader_1_39
                                player.c "[player.orgasm_text]"
                                wt_image indy_cheerleader_1_41
                                terri.c "It's a good thing I'm old enough to be on birth control, or that could have got me in a lot of trouble, mister."
                            "On her":
                                wt_image indy_cheerleader_1_42
                                player.c "[player.orgasm_text]"
                                wt_image indy_cheerleader_1_43
                                terri.c "Oh my god, you didn't get any on my clothes, did you?  The teachers might see!"
                                wt_image indy_cheerleader_1_44
                                terri.c "Whew, looks like it all landed on my belly and chest."
                                wt_image indy_cheerleader_1_45
                                terri.c "This is kind of hot, actually.  A slutty young cheerleader wearing a boy's cum under her clothes after she lets him fuck her."
                        wt_image indy_cheerleader_1_2
                        "[terri.name] seems to have enjoyed getting deep into her young cheerleader fantasy with you.  She's in a good mood as she leaves."
                        $ terri.sex_count += 1
                        call character_location_return(terri) from _call_character_location_return_719
                        wt_image current_location.image
                        orgasm notify
                    "You'll eat her out":
                        wt_image indy_cheerleader_1_17
                        terri.c "You don't have to do that!"
                        wt_image indy_cheerleader_1_26
                        player.c "I know, but you said yourself you're a bit turned on.  Let me look after that for you."
                        wt_image indy_cheerleader_1_27
                        terri.c "I didn't say that because I was expecting anything of you.  You don't have to do this."
                        player.c "I know, but I want to.  You're turned on enough that you'd enjoy being licked, wouldn't you?"
                        wt_image indy_cheerleader_1_28
                        terri.c "Yes, I guess I am, but ..."
                        player.c "Shhhh, let me look after that needy pussy of yours."
                        wt_image indy_cheerleader_1_29
                        "Her sexy snatch is pleasantly responsive.  Her lips are wet and her clit gets throbbing hard as you lick her."
                        wt_image indy_cheerleader_1_30
                        "She has to turn her head and look away, though, before she can completely relax, and she keep her face turned away from you as she cums.  Whether that's out of guilt or something else is hard to say."
                        terri.c "Oooohhhhhh!!!!"
                        wt_image indy_cheerleader_1_31
                        terri.c "You really are a good friend.  My pussy feels incredible now."
                        wt_image indy_cheerleader_1_2
                        "She seems really happy as she leaves.  She may wear her cheerleader outfit for you again soon."
                        $ terri.cheerleader_outfit_visit = 4 # shortens time until she wears the outfit again by one week
                        $ terri.pleasure_her_count += 1
                        call character_location_return(terri) from _call_character_location_return_720
                        wt_image current_location.image
                        change player energy by -energy_short notify
                    "Spank her":
                        player.c "Stand up and present your bum to me, young lady.  I'm going to spank you."
                        wt_image indy_cheerleader_1_17
                        terri.c "Spank me?  Like I was a little girl?  A naughty, sexy little cheerleader girl?"
                        player.c "Who's getting naughtier by the minute the longer she delays following my order."
                        wt_image indy_cheerleader_1_3
                        terri.c "I'm sorry I was naughty.  Please don't spank me too hard."
                        $ title = "Tell her to count?"
                        menu:
                            "Yes, count the spanks":
                                add tags 'counting_now' to terri
                            "No, not today":
                                rem tags 'counting_now' from terri
                        wt_image indy_cheerleader_1_46
                        "*smack*  *smack*  *smack*"
                        if terri.has_tag('counting_now'):
                            terri.c "That's one.  That's two.  Ow!  That's three.  I'm sorry I was naughty!"
                        else:
                            terri.c "Ow!  I'm sorry I was naughty!"
                        wt_image indy_cheerleader_1_3
                        $ terri.temporary_count = 3
                        $ title = "What now?"
                        menu menu_terri_cheerleader_spanking:
                            "Spank her again":
                                wt_image indy_cheerleader_1_46
                                "*smack*"
                                $ terri.temporary_count += 1
                                if terri.temporary_count > 9:
                                    if terri.has_tag('counting_now'):
                                        terri.c "Ooowwww!!!  That's [terri.temporary_count.to_s]!  My bum's so sore, I couldn't have been that naughty?!"
                                    else:
                                        terri.c "Ooowwww!!!    My bum's so sore, I couldn't have been that naughty?!"
                                    "She's had enough and your hand is pretty sore from spanking her, anyway.  Time to stop."
                                else:
                                    if terri.temporary_count < 6:
                                        if terri.has_tag('counting_now'):
                                            terri.c "Oww!!  That's [terri.temporary_count.to_s]!"
                                        else:
                                            terri.c "Oww!!"
                                    elif terri.temporary_count == 6:
                                        if terri.has_tag('counting_now'):
                                            terri.c "Oww!!  That's [terri.temporary_count.to_s]!  I remembered to say I was sorry, didn't I?  In case I didn't, I'm sorry I was naughty."
                                        else:
                                            terri.c "Oww!!  I remembered to say I was sorry, didn't I?  In case I didn't, I'm sorry I was naughty!"
                                    elif terri.temporary_count == 7:
                                        if terri.has_tag('counting_now'):
                                            terri.c "Oww!!  That's [terri.temporary_count.to_s]!  Oh, wow!  That stings!!"
                                        else:
                                            terri.c "Oww!!  Oh, wow!  That stings!!"
                                    elif terri.temporary_count == 8:
                                        if terri.has_tag('counting_now'):
                                            terri.c "Oowww!!!  That's [terri.temporary_count.to_s]!"
                                        else:
                                            terri.c "Oowww!!!"
                                    elif terri.temporary_count == 9:
                                        if terri.has_tag('counting_now'):
                                            terri.c "Oowww!!!  That's [terri.temporary_count.to_s]!  My bum's really sore now!!"
                                        else:
                                            terri.c "Oowww!!!  My bum's really sore now!!"
                                    wt_image indy_cheerleader_1_3
                                    jump menu_terri_cheerleader_spanking
                            "Send her home":
                                pass
                        wt_image indy_cheerleader_1_2
                        if terri.temporary_count < 6:
                            terri.c "Being spanked is no fun.  I guess that's why naughty young girls get spanked.  Thanks for stopping before my bum got too sore.  Bye!"
                            change player energy by -energy_very_short
                        elif terri.temporary_count < 9:
                            terri.c "Being spanked is no fun.  I guess that's why naughty young girls get spanked, so that their sore bum reminds them not to be naughty.  Bye!"
                            change player energy by -energy_short
                        else:
                            terri.c "Being spanked is no fun.  I guess that's why naughty young girls get spanked, so that their sore bum reminds them not to be naughty.  I'm not sure you needed to make mine quite that sore to get the message across, though.  Bye!"
                            change player energy by -energy_short
                        call character_location_return(terri) from _call_character_location_return_721
                        wt_image current_location.image
                        $ terri.temporary_count = 0
                        if terri.submission < 50:
                            change terri submission by 5 notify
                    "She just get naked":
                        wt_image indy_cheerleader_1_16
                        terri.c "But then I wouldn't be dressed as a cheerleader."
                        player.c "But I'd get to enjoy watching a cheerleader undress for me."
                        wt_image indy_cheerleader_1_11
                        terri.c "Okay, I guess stripping naked for you isn't really cheating on my boyfriend."
                        wt_image indy_cheerleader_1_4
                        "Her nipples are rock hard as she undresses.  She's enjoying this more than she's trying to let on."
                        wt_image indy_cheerleader_1_25
                        terri.c "Did you want to see my panties?"
                        player.c "Only for a moment, then I want to see them coming off, too."
                        wt_image indy_cheerleader_1_7
                        "She giggles as she removes her underwear, leavnig her naked except for her running shoes."
                        wt_image indy_cheerleader_1_8
                        terri.c "I'd better get my poms poms or I'll just look like a slut sitting here naked in front of you."
                        wt_image indy_cheerleader_1_14
                        terri.c "I suppose you probably like me looking like a slut, though.  That's part of what guys like about cheerleaders, right, that they show off their bodies?"
                        "She punctuates her remarks by shaking her naked tush at you."
                        wt_image indy_cheerleader_1_9
                        terri.c "You do like me like this, don't you?"
                        $ title = "What do you say?"
                        menu:
                            "You look great":
                                wt_image indy_cheerleader_1_15
                                "A pleased looking [terri.name] chats with you like this until it's time for her to go home."
                            "Your boobs could be bigger":
                                if marilyn.independent_encounter_status > 1:
                                    wt_image indy_cheerleader_1_15
                                    terri.c "Mommy liked my small titties.  I think I'll keep them like this."
                                elif terri.boobjob_interest > 1:
                                    if terri.boobjob_interest < 5:
                                        if terri.has_tag('satisfied') and terri.has_tag('continuing_actions'):
                                            terri.c "I know you think I should get them enlarged, but my boyfriend seems really happy with our sex life. I don't think I need to make any additional changes."
                                            player.c "You don't want to get complacent, [terri.name]."
                                            if terri.test('resistance', 20):
                                                terri.c "I should listen to you, shouldn't I?"
                                                player.c "Yes, [terri.name]. I have your best interests at heart."
                                                $ terri.boobjob_interest = 5
                                                sys "[terri.name] is now more self-conscious about the size of her breasts."
                                            else:
                                                "[terri.name] listens politely, but her resistance is too high for you to convince her to get a boob job."
                                        else:
                                            terri.c "I know you think I should get them enlarged, but I don't think that would help things with my boyfriend."
                                            player.c "It might. It's not late for you to turn yourself into a better girlfriend for him."
                                            if terri.test('resistance', 10):
                                                terri.c "I should listen to you, shouldn't I?"
                                                player.c "Yes, [terri.name]. I have your best interests at heart."
                                                $ terri.boobjob_interest = 5
                                                sys "[terri.name] is now more self-conscious about the size of her breasts."
                                            else:
                                                "[terri.name] listens politely, but her resistance is too high for you to convince her to get a boob job."
                                    else:
                                        player.c "You still haven't had that boob job, [terri.name]."
                                        terri.c "I know. My tits are pathetic, but they're my tits. They're small like a little girl's, but somehow that's always been comforting to me. I always felt they suited me."
                                        player.c "Time to be a big girl now, [terri.name].  With a big girl's body."
                                        terri.c "They're not cheap. Boob jobs that is. I was shocked when I found how much it was going to cost me."
                                        player.c "What's more important? Your money or your boyfriend's happiness?"
                                        "[terri.name] nods."
                                        terri.c "You're right. I'll do it. I hope I don't look ridiculous afterwards."
                                        player.c "What's ridiculous about having big breasts?"
                                        terri.c "I don't know. Women who get boob jobs, they're just ... They have a reputation for not being that smart, I guess."
                                        player.c "The dumbest thing you've done, [terri.name], is wait this long to improve your chest. That makes you more of an airhead than having big knockers will."
                                        "She blushes. The next time you see her, you're pretty sure she'll look different."
                                        $ terri.boobjob_interest = 6
                                else:
                                    if not terri.has_tag('discussed_boobs_cheerleader_outfit'):
                                        terri.c "Really?  I like my small breasts.  I think they make me look younger.  They certainly help me feel younger.  AlthoughI guess a lot of guys prefer big boobs."
                                        player.c "They do, [terri.name].  If you're still interested in being a better girlfriend, you should think about enhancing your body."
                                        "[terri.name] seems to give the idea some thought."
                                        add tags 'discussed_boobs_cheerleader_outfit' to terri
                                        $ terri.boobjob_interest += 1
                                        sys "[terri.name] is now more self-conscious about the size of her breasts."
                                    else:
                                        terri.c "I don't know, I kind of like my small breasts.  I think they make me look younger.  They certainly help me feel younger."
                                "[terri.name] chats with you for a little while longer, then it's time for her to go home."
                        call character_location_return(terri) from _call_character_location_return_722
                        wt_image current_location.image
                    "Nothing":
                        wt_image indy_cheerleader_1_16
                        terri.c "Thanks for being so understanding."
            elif terri.has_tag('boob_job'):
                $ terri.training_session()  ## note: this adds the 'trained_today' and 'trained_this_week' tags
                if terri.visit_sex_count == 0:
                    player.c "Now that you've corrected your physical deficiency, we should finish your training."
                    if terri.has_tag('boobs_out_now'):
                        wt_image indy_boob_job_1_14
                    else:
                        wt_image indy_boob_job_1_6
                    terri.c "What do you mean?  My training's already over."
                    player.c "Remember the trouble you had with tit fucks? I wasn't able to show you how to do it properly when you were flat as a board."
                    terri.c "That's okay. I think I've figured that out."
                    player.c "What? With your boyfriend? I don't think he'd tell you if you were doing it wrong, would he?"
                    "She shakes her head, 'no'."
                    player.c "It's only [terri.pay] for my lesson. Even after the cost of the breast enlargement, I'm sure you can afford that."
                    terri.c "Well, okay."
                    wt_image indy_boob_job_1_7
                    player.c "Is that how you put your tits together for your boyfriend?"
                    terri.c "Yes"
                    player.c "Squeeze them together and form a proper valley for my cock."
                    wt_image indy_boob_job_1_13
                    terri.c "Like this?"
                    player.c "Better. Now wrap them tight around my dick."
                    wt_image indy_boob_job_1_8
                    terri.c "Oh! That's rougher than my boyfriend likes it."
                    player.c "Are you sure? Try it sometime and see. You've got proper boobs now. Keep them squeezed as firmly around my cock as you can."
                    wt_image indy_boob_job_1_9
                    terri.c "Does this feel good?"
                    player.c "Lean back and I'll show you."
                    wt_image indy_boob_job_1_10
                    terri.c "Lean back?"
                    player.c "Have you forgotten everything I've taught you, airhead?"
                    wt_image indy_boob_job_1_11
                    player.c "[player.orgasm_text]"
                    terri.c "Was that better than before?"
                    player.c "Much better."
                    wt_image indy_boob_job_1_12
                    terri.c "So my new boobs work? Thank you for teaching me how to use them!"
                    $ terri.titfuck_count += 1
                elif terri.visit_sex_count == 1:
                    player.c "Now that you have a proper woman's body, it's time to teach you how to use it."
                    if terri.has_tag('boobs_out_now'):
                        wt_image indy_boob_job_1_14
                    else:
                        wt_image indy_boob_job_1_6
                    terri.c "You already showed me how to give a tit fuck."
                    player.c "I'm talking about normal fucking. You need to re-learn how to do that properly."
                    terri.c "I think I can still do intercourse the same way I always have."
                    player.c "Your balance will be all off. Just like a young gymnast going through puberty who needs to learn how to deal with a changing center of gravity."
                    player.c "You didn't have to deal with that going through puberty, did you? Your breasts didn't grow large enough to be an issue for you."
                    terri.c "I guess not. Do you really think it would affect me now?"
                    player.c "Yes. Are you wearing panties?"
                    if terri.has_tag('boobs_out_now'):
                        wt_image indy_boob_job_1_17
                        terri.c "Of course."
                        player.c "Hand them to me."
                        terri.c "Why?"
                        player.c "Get with the program, airhead. You can't fuck me with your panties on."
                        wt_image indy_boob_job_1_18
                        player.c "Now climb on top of me."
                    else:
                        wt_image indy_boob_job_1_16
                        terri.c "Of course."
                        player.c "Take them off and climb on top of me."
                        terri.c "Why?"
                        player.c "Get with the program, airhead. You can't fuck me with your panties on."
                    wt_image indy_boob_job_1_19
                    "Slipping back into her old role as your pupil, she lowers herself onto your hard shaft."
                    wt_image indy_boob_job_1_20
                    player.c "Same cost per session for remedial lessons as for your original training, [terri.name]."
                    terri.c "Oh.  Okay, if you think it will help me?"
                    player.c "It will.  Now ride me up and down, [terri.name].  Show me how you're going to pleasure your boyfriend's cock."
                    wt_image indy_boob_job_1_19
                    terri.c "This doesn't feel much different than with my old breasts. Does it feel different to you?"
                    wt_image indy_boob_job_1_21
                    player.c "Your dress is getting in the way. Slide off me and remove it."
                    wt_image indy_boob_job_1_22
                    player.c "Now let's try again. Ride my shaft, [terri.name]."
                    wt_image indy_boob_job_1_23
                    terri.c "Oh!  They're really bouncing!!! Ouch! It doesn't feel very good."
                    wt_image indy_boob_job_1_24
                    player.c "Does it help if I rub your clit while you're riding me?"
                    terri.c "No.  Should it?"
                    player.c "Some women like that. Maybe you should just ride me faster."
                    wt_image indy_boob_job_1_25
                    terri.c "Ouch!!  That's really uncomfortable, having them bounce up and down like this."
                    player.c "Not for me it isn't. Keep going."
                    wt_image indy_boob_job_1_26
                    player.c "[player.orgasm_text]"
                    "[terri.name] breathes a sigh of relief and rolls onto her side as your balls empty their load into her."
                    wt_image indy_boob_job_1_27
                    terri.c "You were right. I guess I do need to learn how to fuck with these new, larger breasts."
                    $ terri.sex_count += 1
                elif terri.visit_sex_count == 2:
                    player.c "Time to learn how to give a blow job with your new breasts, [terri.name]."
                    if terri.has_tag('boobs_out_now'):
                        wt_image indy_boob_job_1_14
                    else:
                        wt_image indy_boob_job_1_6
                    terri.c "Okay, there's no way having bigger boobs means I need to re-learn how to pleasure my boyfriend with my mouth."
                    player.c "Stop talking, airhead, and get on your knees in front of me.  You know the money for my training will be well spent."
                    wt_image indy_boob_job_1_28
                    player.c "See?  You're already doing it wrong."
                    terri.c "I am?"
                    player.c "You are. I can't even see your chest. What's the point of getting a blowjob from a bimbo with big knockers if you can't even see her tits?"
                    wt_image indy_boob_job_1_29
                    terri.c "Is this better?"
                    player.c "Yes, bimbo.  Except you forgot the part where you're supposed to be sucking my cock."
                    wt_image indy_boob_job_1_30
                    terri.c "Getting breast enhancements doesn't make me a bimbo."
                    player.c "Less talking and more cock sucking, airhead, or I'll charge you double for today's lesson."
                    wt_image indy_boob_job_1_31
                    player.c "Passable. You never were much of a cocksucker. At least now you have the physical attributes to provide a nice show while you're giving head."
                    wt_image indy_boob_job_1_32
                    player.c "Show me where a big titted bimbo will direct her boyfriend' seed when he's ready to cum."
                    terri.c "Here?"
                    player.c "Close enough for an airhead. Stay still and I'll show you."
                    wt_image indy_boob_job_1_33
                    player.c "[player.orgasm_text]"
                    wt_image indy_boob_job_1_34
                    terri.c "Did having bigger breasts really improve my blow job?"
                    player.c "Yes, airhead. You're a sexy looking bimbo with a dick in your mouth, now."
                    $ terri.blowjob_count += 1
                    $ terri.facial_count += 1
                elif terri.visit_sex_count == 3:
                    player.c "Time for a remedial lesson."
                    if terri.has_tag('boobs_out_now'):
                        wt_image indy_boob_job_1_14
                    else:
                        wt_image indy_boob_job_1_6
                    terri.c "I'm not sure you need to keep training me."
                    player.c "An airhead like you? You'll forget everything I taught you if I don't make you practice."
                    terri.c "I'm not really a bimbo, you know. Getting breast enhancements doesn't make a woman stupid."
                    player.c "Stand up and take off your clothes, [terri.name]."
                    wt_image indy_boob_job_1_35
                    terri.c "I don't mind showing you my body. I'm glad you like looking at it. That doesn't make me a bimbo."
                    player.c "Lie back and spread your legs."
                    wt_image indy_boob_job_1_36
                    player.c "Is your pussy wet?"
                    terri.c "No.  I don't get wet very easily. You know that."
                    player.c "You never get wet, airhead. But you desperately want to please your boyfriend, even though you don't enjoy having sex with him."
                    terri.c "I want to be a good girlfriend for him! I like knowing my boyfriend enjoyed himself."
                    player.c "What you like is to be sexually pleasing to men, just like every other bimbo. As long as you get him off, you're happy. Right, airhead?"
                    terri.c "I guess, but that's not a bad thing, is it?"
                    player.c "I never said it was a bad thing. Now be a good bimbo and show me you can get me off with your pussy, and I won't charge you extra for wasting my time with this conversation."
                    wt_image indy_boob_job_1_37
                    "[terri.name]'s used to taking a cock with little to no natural lubricant."
                    wt_image indy_boob_job_1_38
                    "It's not comfortable for her, but you're hard, so she hopes that means you're enjoying yourself."
                    wt_image indy_boob_job_1_39
                    player.c "[player.orgasm_text]"
                    terri.c "Was that ... was that okay?"
                    wt_image indy_boob_job_1_40
                    player.c "Yes, airhead. You're almost as good a cock sheath as any bimbo I've ever stuck my dick into."
                    terri.c "So my boyfriend should really enjoy fucking me, because he's not as experienced as you."
                    player.c "As long as you keep paying me to practice with you, you should be fine."
                    $ terri.sex_count += 1
                elif terri.visit_sex_count > 3:
                    $ title = "What type of remedial lesson is [terri.name] paying for today?"
                    menu:
                        "Tit job":
                            wt_image indy_boob_job_1_7
                            terri.c "I think I'm getting better at giving tit jobs."
                            wt_image indy_boob_job_1_10
                            "Amazingly, she is. She wraps her breasts tightly around your dick, and fucks it ..."
                            wt_image indy_boob_job_1_13
                            "... until she senses you're on the edge, when she removes her dress completely to receive your offering."
                            wt_image indy_boob_job_1_11
                            player.c "[player.orgasm_text]"
                            wt_image indy_boob_job_1_12
                            terri.c "I think it's hard to mess up a tit job with my equipment."
                            $ terri.titfuck_count += 1
                        "Blow job":
                            wt_image indy_boob_job_1_41
                            terri.c "Okay, if you think my blow jobs need work."
                            wt_image indy_boob_job_1_28
                            player.c "What are you forgetting, airhead?"
                            wt_image indy_boob_job_1_35
                            terri.c "I'm supposed to get naked first."
                            player.c "Why?"
                            wt_image indy_boob_job_1_29
                            terri.c "So he can look at my body while I blow him."
                            player.c "Which he needs to do why?"
                            wt_image indy_boob_job_1_42
                            terri.c "Because my mouth isn't talented enough to get him excited all on its own."
                            wt_image indy_boob_job_1_43
                            player.c "I'm glad that something's getting through your thick skull, bimbo.  You can start sucking on me now."
                            wt_image indy_boob_job_1_44
                            "It seems no amount of practice is going to teach [terri.name] to be good at giving head, but she's otherwise hot enough that you're soon ready to cum, regardless."
                            $ title = "Where do you want to cum?"
                            menu:
                                "In her mouth":
                                    wt_image indy_boob_job_1_45
                                    player.c "[player.orgasm_text]"
                                    wt_image indy_boob_job_1_46
                                    terri.c "That was more semen than I remember.  I wonder if larger breasts cause a man to ejaculate more sperm?"
                                    $ terri.swallow_count += 1
                                "On her face":
                                    wt_image indy_boob_job_1_32
                                    player.c "Get ready."
                                    wt_image indy_boob_job_1_33
                                    player.c "[player.orgasm_text]"
                                    wt_image indy_boob_job_1_34
                                    terri.c "I think my larger breasts are helping you to enjoy my blow jobs more!"
                                    $ terri.facial_count += 1
                            $ terri.blowjob_count += 1
                        "Cowgirl":
                            if terri.has_tag('boobs_out_now'):
                                wt_image indy_boob_job_1_17
                            else:
                                wt_image indy_boob_job_1_2
                            terri.c "Which way do you want me to face?"
                            $ title = "How do you want her to ride you?"
                            menu:
                                "Facing towards you":
                                    wt_image indy_boob_job_1_19
                                    "[terri.name] climbs on top ..."
                                    wt_image indy_boob_job_1_20
                                    "... and rides you ..."
                                    wt_image indy_boob_job_1_47
                                    "... until you fill her with your cum."
                                    player.c "[player.orgasm_text]"
                                    wt_image indy_boob_job_1_48
                                    "[terri.name] surprises you with a quick kiss as she climbs off you."
                                    player.c "What was that for?"
                                    terri.c "For liking my new breasts so much you'd fill me with such a big load.  I can already feel it dripping out of me."
                                "Facing away from you":
                                    wt_image indy_boob_job_1_25
                                    terri.c "You can't see my new breasts like this."
                                    player.c "That's okay.  I'll hear them bouncing up and down as you ride me."
                                    wt_image indy_boob_job_1_23
                                    "Hear them you can, as [terri.name] tries to ignore the discomfortable feeling while sliding up and down your pole as fast as she can ..."
                                    wt_image indy_boob_job_1_22
                                    "... until she sighs in relief as she brings you to climax."
                                    player.c "[player.orgasm_text]"
                                    wt_image indy_boob_job_1_27
                                    terri.c "So my new breasts even sound sexier?  That's good to know."
                            $ terri.sex_count += 1
                        "Missionary":
                            wt_image indy_boob_job_1_35
                            terri.c "That's kind of the easiest skill, don't you think?  I mean, I mostly just need to lie there, right?"
                            player.c "So you think even an airhead like you can get it right?  Or have you forgotten what I've taught you about making it more enjoyable for the man?"
                            wt_image indy_boob_job_1_36
                            terri.c "I'm supposed to get myself wet, using lube if I need to."
                            player.c "What else, airhead?"
                            wt_image indy_boob_job_1_37
                            terri.c "Not just lie here. I'm supposed to make it interesting for him."
                            player.c "By doing what?"
                            wt_image indy_boob_job_1_38
                            terri.c "Moving, so he doesn't feel like he's fucking an inanimate doll."
                            player.c "You'd make a pretty good sex doll now, though, wouldn't you?"
                            terri.c "Would I?"
                            wt_image indy_boob_job_1_49
                            player.c "It might be easier on you, too. Not having to act like a real girl. Just being an object to be used for sex."
                            terri.c "I don't think my boyfriend would like that. I want to be a good girlfriend for him, not a doll."
                            wt_image indy_boob_job_1_39
                            player.c "[player.orgasm_text]"
                            terri.c "You don't really think I'd make a better doll than woman, do you?"
                            $ title = "What do you say?"
                            menu:
                                "Of course not, airhead":
                                    player.c "Of course not, airhead. What you're best at is being a bimbo."
                                    wt_image indy_boob_job_1_40
                                    terri.c "So my sex skills must be improving, right?  Bimbos are good at sex, I think?"
                                    player.c "Don't think, airhead. It just results in you saying stupid things."
                                    wt_image indy_boob_job_1_39
                                    terri.c "Sorry.  You're right.  It's best if you keep training me."
                                "You make a fine woman, [terri.name]":
                                    player.c "You're just fine as a woman, [terri.name]."
                                    wt_image indy_boob_job_1_40
                                    if terri.has_tag('satisfied'):
                                        terri.c "Thank you!  My boyfriend thinks so, too."
                                    else:
                                        terri.c "Thank you!  I wish I could be sure my boyfriend thinks the same way."
                                "I wouldn't have to keep training you, if you were a doll":
                                    player.c "If you were a sex doll, I wouldn't have to keep training you."
                                    wt_image indy_boob_job_1_40
                                    terri.c "It's okay. I don't mind paying you to keep training me.  I'm sure I can get better at sex."
                            $ terri.sex_count += 1
                        "Nothing (change your mind)":
                            $ title = "What do you want to talk to her about?"
                            jump menu_terri_contact_talk
                wt_image living_room.image
                "[terri.name] fixes herself up and heads home, promising to send your payment to you by the end of the week."
                $ player.extra_clients_fee_this_week += terri.pay
                $ terri.visit_sex_count += 1
                call character_location_return(terri) from _call_character_location_return_723
                orgasm notify
            else:
                player.c "It's nice having you back here. Perhaps the two of us could get naked together again? You know, for old times' sake?"
                "She laughs."
                if cassandra.independent_encounter_status > 1:
                    terri.c "You know Mistress doesn't let me sleep with boys."
                elif terri.has_tag('likes_girls'):
                    terri.c "You know I only like girls. I'm sure with your charms, you don't need a charity fuck from me."
                    player.c "I wouldn't mind one."
                    "She laughs again."
                    terri.c "How about we just chat?"
                else:
                    terri.c "I'm trying to be a good girlfriend for my boyfriend. Now that our training is over, it wouldn't be very good of me to fool around on him. How about we just chat?"
        "Discuss her breasts" if terri.boobjob_interest > 1 and not terri.has_tag('boob_job') and not terri.has_tag('discussed_boobs_today') and not cassandra.independent_encounter_status > 1 and not marilyn.independent_encounter_status > 1:
            if terri.boobjob_interest < 5:
                player.c "Have you given any further thought to your breasts?"
                terri.c "What do you mean?"
                player.c "You know what I mean."
                if terri.has_tag('satisfied') and terri.has_tag('continuing_actions'):
                    terri.c "My boyfriend seems really happy with our sex life. I don't think I need to make any additional changes."
                    player.c "You don't want to get complacent, [terri.name]."
                    if terri.test('resistance', 20):
                        terri.c "I should listen to you, shouldn't I?"
                        player.c "Yes, [terri.name]. I have your best interests at heart."
                        $ terri.boobjob_interest = 5
                        sys "[terri.name] is now more self-conscious about the size of her breasts."
                    else:
                        "[terri.name] listens politely, but her resistance is too high for you to convince her to get a boob job."
                else:
                    terri.c "I don't think that would help."
                    player.c "It might. It's not late for you to turn yourself into a better girlfriend for him."
                    if terri.test('resistance', 10):
                        terri.c "I should listen to you, shouldn't I?"
                        player.c "Yes, [terri.name]. I have your best interests at heart."
                        $ terri.boobjob_interest = 5
                        sys "[terri.name] is now more self-conscious about the size of her breasts."
                    else:
                        "[terri.name] listens politely, but her resistance is too high for you to convince her to get a boob job."
            else:
                player.c "You still haven't had that boob job, [terri.name]."
                terri.c "I know. My tits are pathetic, but they're my tits. They're small like a little girl's, but somehow that's always been comforting to me. I always felt they suited me."
                player.c "Time to be a big girl now, [terri.name]. With a big girl's body."
                terri.c "They're not cheap. Boob jobs that is. I was shocked when I found how much it was going to cost me."
                player.c "What's more important? Your money or your boyfriend's happiness?"
                "[terri.name] nods."
                terri.c "You're right. I'll do it. I hope I don't look ridiculous afterwards."
                player.c "What's ridiculous about having big breasts?"
                terri.c "I don't know. Women who get boob jobs, they're just ... They have a reputation for not being that smart, I guess."
                player.c "The dumbest thing you've done, [terri.name], is wait this long to improve your chest. That makes you more of an airhead than having big knockers will."
                "She blushes and takes a drink. The next time you see her, you're pretty sure she'll look different."
                $ terri.boobjob_interest = 6
            add tags 'discussed_boobs_today' to terri
        "Tell her to show you her breasts" if terri.has_tag('boob_job') and not terri.has_tag('boobs_out_now'):
            if terri.has_tag('cheerleader_visit_now'):
                wt_image indy_cheerleader_2_4
                terri.c "This is a one piece dress.  I'd have to take the whole thing off to show you my boobs."
                player.c "You're confusing me, airhead.  Why is that a problem?  I want to see your body.  You should leap at the chance to show it off."
                wt_image indy_cheerleader_2_6
                terri.c "But I also want to show off my cheerleader outfit.  How about I just take it off for a minute?"
                wt_image indy_cheerleader_2_7
                "She takes off her dress and stares vacuously at you while you ogle her breasts ..."
                wt_image indy_cheerleader_2_6
                "... then puts her clothes back on."
            else:
                wt_image indy_drink_2_4
                terri.c "What?  Why??"
                player.c "I want to see them.  Consider it a fair trade for letting you have a drink."
                wt_image indy_drink_2_5
                terri.c "I'm taking my top off in return for drinks now?"
                player.c "That sounds like something an airhead would do."
                wt_image indy_drink_2_6
                "She takes a swig of her drink to fortify her courage ..."
                wt_image indy_boob_job_1_2
                "... and opens her top."
                terri.c "You don't really think I'm an airhead, do you?"
                wt_image indy_boob_job_1_14
                player.c "Shush.  Don't interrupt while I'm admiring your tits."
                wt_image indy_boob_job_1_3
                if terri.test('submission', 30):
                    $ title = "Do you want her to strip every time she visits?"
                    menu:
                        "Yes, tell her in the future she's to undress as soon as she arrives":
                            player.c "From now on, you're to take out your breasts as soon as you get here."
                            wt_image indy_boob_job_1_14
                            terri.c "What?  Why??"
                            player.c "Stop asking stupid questions, airhead.  Because it pleases me.  You want to please your former trainer, don't you?"
                            wt_image indy_boob_job_1_3
                            "She nods."
                            terri.c "Yes, [terri.your_respect_name].  I'm glad looking at my new tits pleases you."
                            add tags 'strips_on_visit' to terri
                        "No, don't bother":
                            pass
                else:
                    wt_image indy_boob_job_1_3
                    "If she was more Submissive to you, you could likely convince her to strip without the fuss.  Then again, she's not putting up much of a fight as it is."
                add tags 'boobs_out_now' to terri
        "Tell her to stop wearing the cheerleader outfit" if terri.has_tag('cheerleader_visit_now') and not terri.has_tag('no_cheerleader_visits'):
            if terri.has_tag('boob_job'):
                wt_image indy_cheerleader_2_4
            terri.c "I guess it is a little childish of me to dress up like this to come visit a friend.  I won't wear it again."
            add tags 'no_cheerleader_visits' to terri
        "Tell her it's okay to start wearing her cheerleader outfit again" if terri.cheerleader_outfit_visit > 0 and terri.has_tag('no_cheerleader_visits'):
            terri.c "Really?  If you won't mind, I probably will wear it again when I visit you, the next time the mood strikes me."
            rem tags 'no_cheerleader_visits' from terri
        "Just chat":
            player.c "How are things with you?"
            if cassandra.independent_encounter_status > 1:
                terri.c "Mistress keeps me very busy!"
                terri.c "I have a long list of chores I need to complete every day. I'm going to have to work super fast to catch up on the time I'm spending here with you. But I don't mind. I enjoy our time together."
                terri.c "And I don't mind all the chores. It makes me useful. And when Mistress gets home, I get to serve her and be useful to her, too."
                terri.c "She's very good to me. She punishes me a lot. I need that. I still have lots of bad thoughts in my head, and feelings in my body I shouldn't have. The punishments help."
                player.c "Help you not have them, or help you feel better about having them?"
                "She sips her drink quietly, letting your question go unanswered."
            elif terri.has_tag('likes_girls'):
                terri.c "Things are good. I don't have a girlfriend yet, but I've been out on some dates.  They've been fun!  So different than when I was dating boys."
                if marilyn.independent_encounter_status > 1:
                    player.c "Do you ever see Mommy?"
                    terri.c "No.  I'd like to, but she's insanely busy. She said us having sex was a one time thing, which I'm fine with. I think if I ever really needed her, she'd be there for me. But I need to make my own life, and that's what I'm doing."
            elif terri.has_tag('satisfied'):
                if terri.has_tag('boob_job'):
                    terri.c "Things are good. My boyfriend is really happy with our sex life. Especially since I got the new boobs. He says he didn't realize what he was missing until I showed him!"
                    terri.c "I seem to get more attention now when I'm out. Not just men. Women, too, which is really awkward. It's harder, though, to get people to look me in the eyes. Or listen to me."
                else:
                    terri.c "Things are good. My boyfriend is really happy with our sex life. He says he didn't realize what he was missing until I showed him!"
                    terri.c "I haven't told him where I learned to do all the things I know how to do now, but I'll always be thankful to you for your training."
            else:
                terri.c "I'm not sure. My boyfriend hasn't left me, which is good. He says he's happy with me, but I'm still nervous that I'm not as good a girlfriend to him as I should be."
                if terri.has_tag('boob_job'):
                    terri.c "He does seem to like my new breasts, though. So that helps. Thanks again for convincing me to get that boob job."
                    terri.c "I seem to get more attention now when I'm out. Not just men. Women, too, which is really awkward. It's harder, though, to get people to look me in the eyes. Or listen to me."
                else:
                    terri.c "I know you tried your best during my training. I'm afraid I'm just not good at the girlfriend thing."
            wt_image current_location.image
        "Nothing else (send her home)":
            player.c "It was nice seeing you, [terri.name]"
            if terri.has_tag('cheerleader_visit_now'):
                if terri.has_tag('boob_job'):
                    wt_image indy_cheerleader_2_3
                else:
                    wt_image indy_cheerleader_1_2
                terri.c "Thanks!  It was nice seeing you, too.  Bye!"
                rem tags 'cheerleader_visit_now' from terri
            else:
                terri.c "Likewise. Thanks for the drink. Let's do this again!"
            call character_location_return(terri) from _call_character_location_return_724
            wt_image current_location.image
    return

label terri_futanari_talk:
    if terri.futanari_outfit == 2:
        if terri.has_tag('cock_out_now'):
            wt_image indy_futanari_2_15
        elif terri.has_tag('aroused_now'):
            wt_image indy_futanari_2_7
        else:
            wt_image indy_futanari_2_4
    else:
        if terri.has_tag('cock_out_now'):
            wt_image indy_futanari_1_30
        else:
            wt_image indy_futanari_1_25
    $ title = "What do you want to talk to her about?"
    menu menu_terri_futanari_talk:
        "How she likes having a cock":
            if terri.futanari_outfit == 2:
                if terri.has_tag('cock_out_now'):
                    wt_image indy_futanari_2_18
                elif terri.has_tag('aroused_now'):
                    wt_image indy_futanari_2_8
                else:
                    wt_image indy_futanari_2_6
            else:
                if terri.has_tag('cock_out_now'):
                    wt_image indy_futanari_1_28
                else:
                    wt_image indy_futanari_1_2
            terri.c "It's taken away any confidence I might ever have had about dating someone ..."
            if terri.futanari_outfit == 2:
                if terri.has_tag('cock_out_now'):
                    wt_image indy_futanari_2_19
                elif terri.has_tag('aroused_now'):
                    wt_image indy_futanari_2_2
                else:
                    wt_image indy_futanari_2_4
            else:
                if terri.has_tag('cock_out_now'):
                    wt_image indy_futanari_1_27
                else:
                    wt_image indy_futanari_1_5
            if terri.discussed_transformation == 0:
                terri.c "... but it feels so good when I cum these days, it's almost worth it."
            else:
                terri.c "... but it feels so good when I cum these days, I can almost forgive you doing this to me."
        "Her sex life":
            if terri.futanari_outfit == 2:
                if terri.has_tag('cock_out_now'):
                    wt_image indy_futanari_2_18
                elif terri.has_tag('aroused_now'):
                    wt_image indy_futanari_2_2
                else:
                    wt_image indy_futanari_2_5
            else:
                if terri.has_tag('cock_out_now'):
                    wt_image indy_futanari_1_27
                else:
                    wt_image indy_futanari_1_31
            if terri.has_tag('likes_girls'):
                terri.c "I don't have one.  What woman would want me like this?"
                player.c "Lots of women, probably."
            else:
                terri.c "I don't have one.  What guy would want me like this?"
                if terri.has_tag('you_sucked_her_cock'):
                    player.c "You know I'm attracted to you."
                else:
                    player.c "I'm sure some would."
            if terri.futanari_outfit == 2:
                if terri.has_tag('cock_out_now'):
                    wt_image indy_futanari_2_17
                elif terri.has_tag('aroused_now'):
                    wt_image indy_futanari_2_8
                else:
                    wt_image indy_futanari_2_6
            else:
                if terri.has_tag('cock_out_now'):
                    wt_image indy_futanari_1_28
                else:
                    wt_image indy_futanari_1_2
            if terri.has_tag('likes_girls'):
                terri.c "That's sick.  No lesbian should fuck someone with a penis.  It's unnatural."
                "There's no getting around some irrational prejudices, it seems."
            elif terri.has_tag('you_sucked_her_cock'):
                terri.c "That's nice of you to say, but it's still sick.  I appreciated you sucking me off before, but we both have cocks, so we shouldn't be anything more than friends."
            else:
                terri.c "That's sick.  No guy should fuck someone with a penis."
        "Suggest you have sex":
            if terri.futanari_outfit == 2:
                if terri.has_tag('cock_out_now'):
                    wt_image indy_futanari_2_17
                elif terri.has_tag('aroused_now'):
                    wt_image indy_futanari_2_2
                else:
                    wt_image indy_futanari_2_5
            else:
                if terri.has_tag('cock_out_now'):
                    wt_image indy_futanari_1_29
                else:
                    wt_image indy_futanari_1_2
            terri.c "What?  No!  We both have cocks.  That would be wrong."
        "Suggest she get off":
            if terri.futanari_outfit == 2 and not terri.has_any_tag('cock_out_now', 'aroused_now'):
                wt_image indy_futanari_2_4
                terri.c "Actually, I'm okay now, for a change.  I don't need to get off."
            else:
                if terri.futanari_outfit == 2:
                    if terri.has_tag('cock_out_now'):
                        wt_image indy_futanari_2_16
                    elif terri.has_tag('aroused_now'):
                        wt_image indy_futanari_2_2
                    terri.c "Horny as I'm now feeling, I still don't think I can get off right now, not with you watching."
                else:
                    if terri.has_tag('cock_out_now'):
                        wt_image indy_futanari_1_27
                    else:
                        wt_image indy_futanari_1_6
                    terri.c "Horny as I am right now, I still don't think I can get off right now, not with you watching."
                $ title = "What do you suggest?"
                menu menu_terri_futanari_get_off:
                    "Offer one of your women to her" if player.girlfriend_count > 0 or player.hypno_girlfriend_count > 0 or player.slavegirl_count > 0 or player.bimbo_count > 0:
                        if player.slavegirl_count > 0:
                            if player.slavegirl_count == 1:
                                player.c "How about I get my slavegirl to get you off?  She probably won't even like it, so it's not perverted."
                            else:
                                player.c "How about I get one of my slavegirls to get you off?  They probably won't even like it, so it's not perverted."
                            if terri.futanari_outfit == 2:
                                if terri.has_tag('cock_out_now'):
                                    wt_image indy_futanari_2_17
                                elif terri.has_tag('aroused_now'):
                                    wt_image indy_futanari_2_8
                                else:
                                    wt_image indy_futanari_2_6
                            else:
                                if terri.has_tag('cock_out_now'):
                                    wt_image indy_futanari_1_28
                                else:
                                    wt_image indy_futanari_1_2
                            terri.c "No way!  I'm not going to let you force some poor woman to look after me, sexually."
                            if player.bimbo_count > 0:
                                player.c "How about a bimbo, then?  She wouldn't be forced, she'd love to suck on your big cock."
                                terri.c "No!  I don't want you tricking some idiot to service me."
                            if player.girlfriend_count or player.hypno_girlfriend_count > 0:
                                player.c "What about my girlfriend, then?"
                                terri.c "Yuck!  I don't want to be part of your relationship with someone else."
                        elif player.bimbo_count > 0:
                            player.c "I know someone who'd love to suck on your cock.  She's a little ditzy, but she'll happily blow you."
                            if terri.futanari_outfit == 2:
                                if terri.has_tag('cock_out_now'):
                                    wt_image indy_futanari_2_17
                                elif terri.has_tag('aroused_now'):
                                    wt_image indy_futanari_2_8
                                else:
                                    wt_image indy_futanari_2_6
                            else:
                                if terri.has_tag('cock_out_now'):
                                    wt_image indy_futanari_1_28
                                else:
                                    wt_image indy_futanari_1_2
                            terri.c "No way!  I don't want you tricking some idiot to service me."
                            if player.girlfriend_count or player.hypno_girlfriend_count > 0:
                                player.c "What about my girlfriend, then?"
                                terri.c "Yuck!  I don't want to be part of your relationship with someone else."
                        else:
                            player.c "How about I get my girlfriend to look after you?  I'm sure she'd do so if I asked."
                            if terri.futanari_outfit == 2:
                                if terri.has_tag('cock_out_now'):
                                    wt_image indy_futanari_2_17
                                elif terri.has_tag('aroused_now'):
                                    wt_image indy_futanari_2_8
                                else:
                                    wt_image indy_futanari_2_6
                            else:
                                if terri.has_tag('cock_out_now'):
                                    wt_image indy_futanari_1_28
                                else:
                                    wt_image indy_futanari_1_2
                            terri.c "No way!  I don't want to be part of your relationship with someone else."
                        jump menu_terri_futanari_get_off
                    "Offer to find her a woman":
                        if terri.futanari_outfit == 2:
                            if terri.has_tag('cock_out_now'):
                                wt_image indy_futanari_2_17
                            elif terri.has_tag('aroused_now'):
                                wt_image indy_futanari_2_8
                            else:
                                wt_image indy_futanari_2_6
                        else:
                            if terri.has_tag('cock_out_now'):
                                wt_image indy_futanari_1_28
                            else:
                                wt_image indy_futanari_1_2
                        if terri.has_tag('likes_girls'):
                            terri.c "No way!  The only women I like are lesbians and only a perverted lesbian would want to get someone with a penis off.  I don't want you finding me a pervert."
                        else:
                            terri.c "No way!  I'm a woman!  The only women who'd want to have sex with me are perverts.  I don't want you finding me a pervert."
                        jump menu_terri_futanari_get_off
                    "Offer to find her a man":
                        if terri.futanari_outfit == 2:
                            if terri.has_tag('cock_out_now'):
                                wt_image indy_futanari_2_17
                            elif terri.has_tag('aroused_now'):
                                wt_image indy_futanari_2_8
                            else:
                                wt_image indy_futanari_2_6
                        else:
                            if terri.has_tag('cock_out_now'):
                                wt_image indy_futanari_1_28
                            else:
                                wt_image indy_futanari_1_2
                        terri.c "No way!  I have a cock!  I don't want you finding me a pervert man who wants to have sex with someone with a cock."
                        jump menu_terri_futanari_get_off
                    "Suggest you watch porn":
                        if terri.futanari_outfit == 2:
                            if terri.has_tag('cock_out_now'):
                                wt_image indy_futanari_2_15
                            elif terri.has_tag('aroused_now'):
                                wt_image indy_futanari_2_7
                            else:
                                wt_image indy_futanari_2_6
                        else:
                            if terri.has_tag('cock_out_now'):
                                wt_image indy_futanari_1_35
                            else:
                                wt_image indy_futanari_1_3
                        terri.c "You mean watch porn together?  I guess we could do that.  It's no different than watching a movie together, right?  Except we'll both be jerking off while we watch."
                        if terri.futanari_outfit == 2:
                            if terri.has_tag('cock_out_now'):
                                wt_image indy_futanari_2_11
                            else:
                                wt_image indy_futanari_2_9
                            "[terri.name] watches with interest as you flip through your collection of porn, looking for something to watch."
                        else:
                            if terri.has_tag('cock_out_now'):
                                wt_image indy_futanari_1_37
                                "[terri.name] watches with interest as you flip through your collection of porn, looking for something to watch."
                            else:
                                wt_image indy_futanari_1_36
                                "[terri.name] picks up the remote and starts flipping through your collection of porn."
                                terri.c "What did you want to watch?"
                        $ title = "What type of porn do you want to watch with her?"
                        menu menu_terri_futanari_porn_choice:
                            "Straight sex":
                                if terri.futanari_outfit == 2:
                                    if terri.has_tag('cock_out_now'):
                                        wt_image indy_futanari_2_12
                                        "[terri.name] is soon engrossed in the scene playing out in front of her."
                                    else:
                                        wt_image indy_futanari_2_11
                                        "[terri.name] is soon engrossed in the scene playing out in front of her.  She frees her cock from her dress ..."
                                        wt_image indy_futanari_2_12
                                        "... and starts stroking it while she watches."
                                        add tags 'cock_out_now' to terri
                                    wt_image indy_futanari_2_14
                                else:
                                    if terri.has_tag('cock_out_now'):
                                        wt_image indy_futanari_1_40
                                        "[terri.name] is soon engrossed in the scene playing out in front of her."
                                        wt_image indy_futanari_1_35
                                    else:
                                        wt_image indy_futanari_1_38
                                        "[terri.name] is soon engrossed in the scene playing out in front of her."
                                        wt_image indy_futanari_1_39
                                terri.c "Oh yes, pound that pretty pussy of hers!  Fuck that sexy slut hard!"
                            "Gay male":
                                terri.c "I'm not going to be able to get off on this.  Can we watch something else?"
                                "All cocks is the wrong type of stimulation for [terri.name], it seems."
                                jump menu_terri_futanari_porn_choice
                            "Lesbian":
                                if terri.futanari_outfit == 2:
                                    if terri.has_tag('cock_out_now'):
                                        wt_image indy_futanari_2_12
                                        "[terri.name] is soon engrossed in the scene playing out in front of her."
                                    else:
                                        wt_image indy_futanari_2_11
                                        "[terri.name] is soon engrossed in the scene playing out in front of her.  She frees her cock from her dress ..."
                                        wt_image indy_futanari_2_12
                                        "... and starts stroking it while she watches."
                                        add tags 'cock_out_now' to terri
                                    wt_image indy_futanari_2_14
                                else:
                                    if terri.has_tag('cock_out_now'):
                                        wt_image indy_futanari_1_40
                                        "[terri.name] is soon engrossed in the scene playing out in front of her."
                                        wt_image indy_futanari_1_35
                                    else:
                                        wt_image indy_futanari_1_38
                                        "[terri.name] is soon engrossed in the scene playing out in front of her."
                                        wt_image indy_futanari_1_39
                                if terri.has_tag('likes_girls'):
                                    terri.c "Oh, shit!  Look at those two sexy women!!  I wish I was doing that to them!  It's so hot!!"
                                else:
                                    terri.c "Oh, shit!  Look at those two perverts!!  That's so, so wrong.  Those perverted sluts shouldn't be doing that!  It's so hot!!"
                            "Female submissive":
                                if terri.futanari_outfit == 2:
                                    if terri.has_tag('cock_out_now'):
                                        wt_image indy_futanari_2_12
                                        "[terri.name] is soon engrossed in the scene playing out in front of her."
                                    else:
                                        wt_image indy_futanari_2_11
                                        "[terri.name] is soon engrossed in the scene playing out in front of her.  She frees her cock from her dress ..."
                                        wt_image indy_futanari_2_12
                                        "... and starts stroking it while she watches."
                                        add tags 'cock_out_now' to terri
                                    wt_image indy_futanari_2_14
                                else:
                                    if terri.has_tag('cock_out_now'):
                                        wt_image indy_futanari_1_40
                                        "[terri.name] is soon engrossed in the scene playing out in front of her."
                                        wt_image indy_futanari_1_35
                                    else:
                                        wt_image indy_futanari_1_38
                                        "[terri.name] is soon engrossed in the scene playing out in front of her."
                                        wt_image indy_futanari_1_39
                                terri.c "Oh, what a dirty fucking slut she is!  Punish her!  Punish that dirty slut and make her your bitch!!"
                            "Female dominant":
                                if terri.futanari_outfit == 2:
                                    if terri.has_tag('cock_out_now'):
                                        wt_image indy_futanari_2_12
                                        "[terri.name] is soon engrossed in the scene playing out in front of her."
                                    else:
                                        wt_image indy_futanari_2_11
                                        "[terri.name] is soon engrossed in the scene playing out in front of her.  She frees her cock from her dress ..."
                                        wt_image indy_futanari_2_12
                                        "... and starts stroking it while she watches."
                                        add tags 'cock_out_now' to terri
                                    wt_image indy_futanari_2_14
                                else:
                                    if terri.has_tag('cock_out_now'):
                                        wt_image indy_futanari_1_40
                                        "[terri.name] is soon engrossed in the scene playing out in front of her."
                                        wt_image indy_futanari_1_35
                                    else:
                                        wt_image indy_futanari_1_38
                                        "[terri.name] is soon engrossed in the scene playing out in front of her."
                                        wt_image indy_futanari_1_39
                                terri.c "Oh, Mistress, I wish you were doing that to me!  Punish that big cock!  Make it sore and achy like mine!!  Oh, yes, Mistress!  Make me serve your wet pussy like he is!!"
                            "None":
                                if terri.futanari_outfit == 2:
                                    if terri.has_tag('cock_out_now'):
                                        wt_image indy_futanari_2_17
                                    else:
                                        wt_image indy_futanari_2_8
                                else:
                                    if terri.has_tag('cock_out_now'):
                                        wt_image indy_futanari_1_35
                                    else:
                                        wt_image indy_futanari_1_34
                                terri.c "Funny, I would have thought you'd have had some kind of porn you'd want to watch with me."
                                jump menu_terri_futanari_get_off
                        # only get here if don't jump away
                        $ title = "What now?"
                        menu:
                            "Watch her cum":
                                if terri.futanari_outfit == 2:
                                    wt_image indy_futanari_2_19
                                    terri.c "oohhhh ... this scene is so hot, I'm going to cum!"
                                    wt_image indy_futanari_2_20
                                    terri.c "Oooohhhhhh!!!!"
                                    wt_image indy_futanari_2_21
                                    "[terri.name] pumps a ridiculous amount of cum out of her cock and onto your floor."
                                    wt_image indy_futanari_2_22
                                else:
                                    wt_image indy_futanari_1_41
                                    "As her excitement builds, [terri.name] grabs some tissues."
                                    wt_image indy_futanari_1_42
                                    terri.c "oohhhh ... this scene is so hot, I'm going to cum!"
                                    wt_image indy_futanari_1_43
                                    terri.c "Oooohhhhhh!!!!"
                                    wt_image indy_futanari_1_44
                                    "The tissue prove inadequate to prevent [terri.name] from making a mess."
                                    wt_image indy_futanari_1_45
                                    terri.c "Oh shit, I'm still cumming!"
                                    wt_image indy_futanari_1_46
                                    terri.c "oohhhh ... I'm making such a mess."
                                    wt_image indy_futanari_1_11
                                    terri.c "I hope that's all of it."
                                    wt_image indy_futanari_1_12
                                    terri.c "oohhhh ... I think there's more!"
                                    wt_image indy_futanari_1_13
                                    terri.c "Oooohhhhhh!!!!"
                                    wt_image indy_futanari_1_14
                                    "Frantically, [terri.name] grabs more tissues ..."
                                    wt_image indy_futanari_1_15
                                    "... but they're barely enough to hold back the flood."
                                    wt_image indy_futanari_1_16
                                    "Eventually, even her magically-enhanced balls are empty, but not before they leave a mess on her and your floor."
                                    wt_image indy_futanari_1_47
                                $ title = "What do you do about the mess?"
                                menu:
                                    "Tell her to clean it up":
                                        if terri.futanari_outfit == 2:
                                            if terri.test('submission', 60):
                                                wt_image indy_futanari_2_23
                                                terri.c "Yes, [terri.your_respect_name]."
                                                "She dutifully licks the cum off her own cock, then does the same for the cum on the floor."
                                            elif terri.test('submission', 40):
                                                wt_image indy_futanari_2_23
                                                terri.c "Yes, [terri.your_respect_name]."
                                                "She dutifully licks the cum off her own cock, then cleans up the cum on the floor."
                                            else:
                                                wt_image indy_futanari_2_24
                                                terri.c "I will.  Give me a moment to recover and I'll wipe up the mess I made."
                                        else:
                                            if terri.test('submission', 60):
                                                wt_image indy_futanari_1_48
                                                terri.c "Yes, [terri.your_respect_name]."
                                                wt_image indy_futanari_1_49
                                                "She dutifully scoops up and eats all of the cum dripping from her cock ..."
                                                wt_image indy_futanari_1_20
                                                "... then mops up the mess she left on the floor ..."
                                                wt_image indy_futanari_1_50
                                                "... and licks that up, too."
                                                wt_image indy_futanari_1_51
                                                $ title = "What now?"
                                                menu:
                                                    "Tell her to eat the tissues":
                                                        wt_image indy_futanari_1_52
                                                        player.c "Don't waste the tissues, [terri.name]."
                                                        wt_image indy_futanari_1_53
                                                        terri.c "But they can't be re-used ... Oh! You mean ..."
                                                        wt_image indy_futanari_1_54
                                                        "[terri.name] puts the cum-soaked tissues in her mouth ..."
                                                        wt_image indy_futanari_1_55
                                                        "... and slowly chews and swallow them as you watch."
                                                    "That's enough":
                                                        pass
                                            elif terri.test('submission', 40):
                                                wt_image indy_futanari_1_48
                                                terri.c "Yes, [terri.your_respect_name]."
                                                wt_image indy_futanari_1_49
                                                "She dutifully scoops up and eats all of the cum dripping from her cock ..."
                                                wt_image indy_futanari_1_20
                                                "... then mops up the mess she left on the floor."
                                            else:
                                                wt_image indy_futanari_2_11
                                                terri.c "Of course!  Sorry I made such a mess."
                                                wt_image indy_futanari_1_20
                                                "[terri.name] carefully wipes up the mess she left on the floor ..."
                                                wt_image indy_futanari_1_21
                                                "... then cleans up the mess she left on herself."
                                    "Lick it up yourself":
                                        if terri.futanari_outfit == 2:
                                            wt_image indy_futanari_2_25
                                            "[terri.name] watches as you drop to the floor and start licking up the mess she made ..."
                                            wt_image indy_futanari_2_42
                                            "... then moans as you lick her cock clean."
                                            wt_image indy_futanari_2_27
                                            terri.c "oohhhh ... I could have cleaned my cock off myself, but it feels nice when you do it like that."
                                        else:
                                            wt_image indy_futanari_1_57
                                            "[terri.name] watches as you drop to the floor and start licking up the mess she made ..."
                                            wt_image indy_futanari_1_74
                                            "... then moans as you lick her cock clean."
                                            wt_image indy_futanari_1_58
                                            terri.c "oohhhh"
                                            wt_image indy_futanari_1_59
                                            terri.c "I could have cleaned my cock off myself, but it feels nice when you do it like that."
                                    "Ignore it":
                                        if terri.futanari_outfit == 2:
                                            wt_image indy_futanari_2_24
                                        else:
                                            wt_image indy_futanari_1_56
                                        terri.c "oohhh ... That felt good.  Sorry about the mess."
                                        if player.slavegirl_count > 1:
                                            player.c "Don't worry about it.  I'll get one of my slavegirls to clean it up."
                                        elif player.slavegirl_count == 1:
                                            player.c "Don't worry about it.  I'll get one of my slavegirls to clean it up."
                                        else:
                                            player.c "Don't worry about it.  I'm glad you had fun."
                                if terri.futanari_outfit == 2:
                                    wt_image indy_futanari_2_3
                                else:
                                    wt_image indy_futanari_1_23
                                "[terri.name] smiles as she leaves.  It seems she enjoyed her visit."
                                change player energy by -energy_very_short notify
                                call terri_futanari_send_home from _call_terri_futanari_send_home
                            "Flip to something else":
                                if terri.futanari_outfit == 2:
                                    if terri.has_tag('cock_out_now'):
                                        wt_image indy_futanari_2_11
                                    else:
                                        wt_image indy_futanari_2_9
                                else:
                                    if terri.has_tag('cock_out_now'):
                                        wt_image indy_futanari_1_37
                                    else:
                                        wt_image indy_futanari_1_36
                                jump menu_terri_futanari_porn_choice
                    "Offer to suck her off yourself":
                        if terri.has_tag('you_sucked_her_cock'):
                            if terri.futanari_outfit == 2:
                                if terri.has_tag('cock_out_now'):
                                    wt_image indy_futanari_2_18
                                    if terri.has_tag('you_no_ball_licking'):
                                        terri.c "I mean, if you think I need another lesson in receiving blowjobs, you were my trainer, so I guess that's okay."
                                    else:
                                        if terri.has_tag('you_licked_her_balls'):
                                            terri.c "I mean, if you think I need another lesson in receiving blowjobs, you were my trainer, so I guess that's okay.  Will you worship my balls again, too?"
                                        else:
                                            terri.c "I mean, if you think I need another lesson in receiving blowjobs, you were my trainer, so I guess that's okay.  Will you worship my balls this time?  I think I need a lesson in how to have my balls licked, too."
                                        $ title = "What do you tell her?"
                                        menu:
                                            "Yes, I'll worship your balls":
                                                wt_image indy_futanari_2_12
                                                player.c "Lie back and give me access."
                                                wt_image indy_futanari_2_31
                                                "Her cock twitches in anticipation as you kneel between her legs ..."
                                                wt_image indy_futanari_2_32
                                                "... and run your tongue up and down the sensitive underside of her shaft before swirling it back and forth and around her big, sexy balls ..."
                                                wt_image indy_futanari_2_33
                                                "... eventually taking her sack into your mouth and tea-bagging her gently."
                                                wt_image indy_futanari_2_11
                                                terri.c "Oohhhh, I can't take that teasing anymore.  Kneel down in front of me, I want to feel my cock in your mouth."
                                                add tags 'you_licked_her_balls' to terri
                                            "No, I'm just going to suck your cock today":
                                                wt_image indy_futanari_2_26
                                                player.c "For today, just open your knees so I can suck your cock, [terri.name]."
                                            "No, never (shuts off question)":
                                                wt_image indy_futanari_2_26
                                                player.c "Don't be gross, [terri.name].  Just open your knees so I can suck your cock."
                                                add tags 'you_no_ball_licking' to terri
                                else:
                                    wt_image indy_futanari_2_44
                                    if terri.has_tag('you_no_ball_licking'):
                                        terri.c "I mean, if you think I need another lesson in receiving blowjobs, you were my trainer, so I guess that's okay."
                                    else:
                                        if terri.has_tag('you_licked_her_balls'):
                                            terri.c "I mean, if you think I need another lesson in receiving blowjobs, you were my trainer, so I guess that's okay.  Will you worship my balls again, too?"
                                        else:
                                            terri.c "I mean, if you think I need another lesson in receiving blowjobs, you were my trainer, so I guess that's okay.  Will you worship my balls this time?  I think I need a lesson in how to have my balls licked, too."
                                        $ title = "What do you tell her?"
                                        menu:
                                            "Yes, I'll worship your balls":
                                                wt_image indy_futanari_2_46
                                                player.c "Spread your legs and give me access."
                                                wt_image indy_futanari_2_27
                                                "Her cock twitches in anticipation as you kneel between her legs ..."
                                                wt_image indy_futanari_2_47
                                                "... and run your tongue up and down the sensitive underside of her shaft before swirling it back and forth and around her big, sexy balls ..."
                                                wt_image indy_futanari_2_48
                                                "... eventually taking her sack into your mouth and tea-bagging her gently."
                                                wt_image indy_futanari_2_27
                                                terri.c "Oohhhh, I can't take that teasing anymore.  I want to feel my cock in your mouth."
                                                add tags 'you_licked_her_balls' to terri
                                            "No, I'm just going to suck your cock today":
                                                wt_image indy_futanari_2_45
                                                player.c "For today, just give me your cock to suck, [terri.name]."
                                            "No, never (shuts off question)":
                                                wt_image indy_futanari_2_45
                                                player.c "Don't be gross, [terri.name].  Just give me your cock to suck."
                                                add tags 'you_no_ball_licking' to terri
                                wt_image indy_futanari_2_34
                                "She offers her cock to you with both hands and you lick gently around the head and tip ..."
                                wt_image indy_futanari_2_35
                                "... before opening wide and taking her thick dick into your mouth."
                                wt_image indy_futanari_2_36
                                "After a while, you feel a hand on your head ..."
                                wt_image indy_futanari_2_37
                                "... and she starts guiding you around her cock, showing you where she wants you to kiss and lick ..."
                                wt_image indy_futanari_2_36
                                "... before grabbing your head more firmly and vigorously face-fucking you."
                                wt_image indy_futanari_2_38
                                "Just as you're starting to gag, she pulls out of your mouth ..."
                                wt_image indy_futanari_2_39
                                "... and finishes on your face."
                                wt_image indy_futanari_2_40
                                terri.c "Oooohhhhhh!!!!"
                                wt_image indy_futanari_2_41
                                if terri.has_tag('you_cleaned_her_cock'):
                                    terri.c "Oh, wow!  Look what you did.  There's a mess on your face and all over my cock and hands, too."
                                    wt_image indy_futanari_2_23
                                    terri.c "I think you need to clean me off before I leave."
                                    $ title = "What now?"
                                    menu:
                                        "Clean her up with your mouth":
                                            wt_image indy_futanari_2_42
                                            "[terri.name] offers her cock to you and watches as you lick her cum off it and her fingers."
                                            wt_image indy_futanari_2_27
                                            terri.c "Having you clean my cock after you blow me feels so nice.  You should probably wipe the cum off your face, now, it's dripping off your chin and making even more of a mess.  I'll just see myself out.  Thanks for a great visit!"
                                        "Tell her to clean herself off today":
                                            wt_image indy_futanari_2_10
                                            "[terri.name] wipes herself clean with her dress.  Presumably she'll wash it when she gets home."
                                            wt_image indy_futanari_2_43
                                            terri.c "I liked it better when you cleaned my cock off, but I still really enjoyed the blowjob.  Thanks for a great visit!"
                                else:
                                    terri.c "Oh, wow!  Looks like we both need to clean ourselves up, I shot a lot of cum on you and got some on myself, too."
                                    $ title = "What now?"
                                    menu:
                                        "Clean her up with your mouth":
                                            wt_image indy_futanari_2_23
                                            player.c "I'm the one who gave you the blowjob, [terri.name], so really I'm responsible for the mess on your cock and hands.  Don't be afraid to expect me to clean it up."
                                            wt_image indy_futanari_2_42
                                            "[terri.name] offers her cock to you and watches as you lick her cum off it and her fingers."
                                            wt_image indy_futanari_2_27
                                            terri.c "I liked that!  The blowjob felt even better with the after-care of you licking me clean.  You should probably wipe the cum off your face, now, it's dripping off your chin and making even more of a mess.  I'll just see myself out.  Thanks for a great visit!"
                                            add tags 'you_cleaned_her_cock' to terri
                                        "Just clean yourself":
                                            wt_image indy_futanari_2_10
                                            "[terri.name] wipes herself clean with her dress.  Presumably she'll wash it when she gets home."
                                            wt_image indy_futanari_2_43
                                            terri.c "Thanks for a great visit!"
                            else:
                                if terri.has_tag('cock_out_now'):
                                    wt_image indy_futanari_1_37
                                    if terri.has_tag('you_no_ball_licking'):
                                        terri.c "I mean, if you think I need another lesson in receiving blowjobs, you were my trainer, so I guess that's okay."
                                    else:
                                        if terri.has_tag('you_licked_her_balls'):
                                            terri.c "I mean, if you think I need another lesson in receiving blowjobs, you were my trainer, so I guess that's okay.  Will you worship my balls again, too?"
                                        else:
                                            terri.c "I mean, if you think I need another lesson in receiving blowjobs, you were my trainer, so I guess that's okay.  Will you worship my balls this time?  I think I need a lesson in how to have my balls licked, too."
                                        $ title = "What do you tell her?"
                                        menu:
                                            "Yes, I'll worship your balls":
                                                wt_image indy_futanari_1_35
                                                "Her cock twitches in anticipation as you kneel between her legs."
                                                wt_image indy_futanari_1_60
                                                "It twitches even more as you run your tongue up and down the sensitive underside of her shaft, before turning your attention to her balls."
                                                wt_image indy_futanari_1_61
                                                "It's more difficult to pleasure her balls with her panties still on, but the moans that escape her throat as you lick her balls around the edges and through the thin fabric of the panties tell you how much she's enjoying this."
                                                wt_image indy_futanari_1_62
                                                terri.c "Oohhhh, I can't take that teasing anymore.  I want to feel my cock in your mouth."
                                                add tags 'you_licked_her_balls' to terri
                                            "No, I'm just going to suck your cock today":
                                                wt_image indy_futanari_1_62
                                                player.c "For today, just give me your cock to suck, [terri.name]."
                                            "No, never (shuts off question)":
                                                wt_image indy_futanari_1_62
                                                player.c "Don't be gross, [terri.name].  Just give me your cock to suck."
                                                add tags 'you_no_ball_licking' to terri
                                else:
                                    wt_image indy_futanari_1_34
                                    if terri.has_tag('you_no_ball_licking'):
                                        terri.c "I mean, if you think I need another lesson in receiving blowjobs, you were my trainer, so I guess that's okay."
                                    else:
                                        if terri.has_tag('you_licked_her_balls'):
                                            terri.c "I mean, if you think I need another lesson in receiving blowjobs, you were my trainer, so I guess that's okay.  Will you worship my balls again, too?"
                                        else:
                                            terri.c "I mean, if you think I need another lesson in receiving blowjobs, you were my trainer, so I guess that's okay.  Will you worship my balls this time?  I think I need a lesson in how to have my balls licked, too."
                                        $ title = "What do you tell her?"
                                        menu:
                                            "Yes, I'll worship your balls":
                                                wt_image indy_futanari_1_75
                                                "Her cock twitches in anticipation as you kneel at her feet."
                                                wt_image indy_futanari_1_76
                                                "It twitches even more as you run your tongue up and down the sensitive underside of her shaft, before turning your attention to her balls."
                                                wt_image indy_futanari_1_77
                                                "It's more difficult to pleasure her balls with her panties still on, but the moans that escape her throat as you lick her balls around the edges and through the thin fabric of the panties tell you how much she's enjoying this."
                                                wt_image indy_futanari_1_75
                                                terri.c "Oohhhh, I can't take that teasing anymore.  I want to feel my cock in your mouth."
                                                add tags 'you_licked_her_balls' to terri
                                            "No, I'm just going to suck your cock today":
                                                wt_image indy_futanari_1_6
                                                player.c "For today, just give me your cock to suck, [terri.name]."
                                            "No, never (shuts off question)":
                                                wt_image indy_futanari_1_6
                                                player.c "Don't be gross, [terri.name].  Just give me your cock to suck."
                                                add tags 'you_no_ball_licking' to terri
                                wt_image indy_futanari_1_63
                                "[terri.name] stands over you and feeds her thick cock into your waiting mouth."
                                wt_image indy_futanari_1_64
                                "You bob your head back and forth, your lips wrapped tightly around her shaft, your tongue licking at the underside as you suck her.  When you sense she's getting close, you stop and look at her."
                                if terri.has_tag('cock_out_now'):
                                    wt_image indy_futanari_1_59
                                else:
                                    wt_image indy_futanari_1_75
                                player.c "Show me how you want me to suck you."
                                wt_image indy_futanari_1_64
                                "As you resume sucking her, she tentatively places a hand on your head ..."
                                wt_image indy_futanari_1_66
                                "... and starts guiding you around her cock ..."
                                wt_image indy_futanari_1_67
                                "... showing you where she wants you to kiss and lick ..."
                                wt_image indy_futanari_1_65
                                "... before grabbing your head more firmly and vigorously face-fucking you."
                                wt_image indy_futanari_1_68
                                "Just as you're starting to gag, she pulls out of your mouth and sits directly in front of you ..."
                                wt_image indy_futanari_1_69
                                "... and finishes on your face."
                                wt_image indy_futanari_1_70
                                terri.c "Oooohhhhhh!!!!"
                                wt_image indy_futanari_1_71
                                if terri.has_tag('you_cleaned_her_cock'):
                                    terri.c "Oh, wow!  Look what you did.  There's a mess on your face and all over my cock and hands, too."
                                    wt_image indy_futanari_1_78
                                    terri.c "I think you need to clean me off before I leave."
                                    $ title = "What now?"
                                    menu:
                                        "Clean her up with your mouth":
                                            wt_image indy_futanari_1_74
                                            "[terri.name] offers her cock to you and watches as you lick her cum off it and her fingers."
                                            wt_image indy_futanari_1_34
                                            terri.c "Having you clean my cock after you blow me feels so nice.  You should probably wipe the cum off your face, now, it's dripping off your chin and making even more of a mess.  I'll just see myself out.  Thanks for a great visit!"
                                        "Tell her to clean herself off today":
                                            wt_image indy_futanari_1_41
                                            "[terri.name] wipes the cum off her hands and cock with some tissues while you do the same with the cum on your face."
                                            wt_image indy_futanari_1_34
                                            terri.c "I liked it better when you cleaned my cock off, but I still really enjoyed the blowjob.  Thanks for a great visit!"
                                else:
                                    terri.c "Oh, wow!  Looks like we both need to clean ourselves up, I shot a lot of cum on you and got some on myself, too."
                                    $ title = "What now?"
                                    menu:
                                        "Clean her up with your mouth":
                                            wt_image indy_futanari_1_73
                                            player.c "Put the tissue away.  I'm the one who gave you the blowjob, [terri.name], so really I'm responsible for the mess on your cock and hands.  Don't be afraid to expect me to clean it up."
                                            wt_image indy_futanari_1_74
                                            "[terri.name] offers her cock to you and watches as you lick her cum off it and her fingers."
                                            wt_image indy_futanari_1_34
                                            terri.c "I liked that!  The blowjob felt even better with the after-care of you licking me clean.  You should probably wipe the cum off your face, now, it's dripping off your chin and making even more of a mess.  I'll just see myself out.  Thanks for a great visit!"
                                            add tags 'you_cleaned_her_cock' to terri
                                        "Just clean yourself":
                                            wt_image indy_futanari_1_41
                                            "[terri.name] wipes the cum off her hands and cock with some tissues while you do the same with the cum on your face."
                                            wt_image indy_futanari_1_34
                                            terri.c "Thanks for a great visit!"
                        # first time you blow her
                        else:
                            if terri.futanari_outfit == 2:
                                if terri.has_tag('cock_out_now'):
                                    wt_image indy_futanari_2_28
                                    terri.c "What?  No, that would be wrong.  You have a cock, too."
                                    player.c "I'll decide for myself what's right or wrong on that front.  Besides, I'm your trainer and I haven't trained you on how to receive a blowjob, yet, have I?"
                                    wt_image indy_futanari_2_29
                                    terri.c "Well, no, you haven't."
                                    player.c "And that's something you'd like to learn, isn't it?"
                                    wt_image indy_futanari_2_30
                                    terri.c "It is, actually.  My cock's getting even harder, thinking about a pair of lips wrapped around it."
                                    player.c "Sit down and I'll teach you what it's like."
                                    wt_image indy_futanari_2_18
                                    if not terri.has_tag('you_no_ball_licking'):
                                        terri.c "Thank you!  Will you worship my balls, too?"
                                        $ title = "What do you tell her?"
                                        menu:
                                            "Yes, I'll worship your balls":
                                                wt_image indy_futanari_2_12
                                                player.c "Lie back and give me access."
                                                wt_image indy_futanari_2_31
                                                "Her cock twitches in anticipation as you kneel between her legs ..."
                                                wt_image indy_futanari_2_32
                                                "... and run your tongue up and down the sensitive underside of her shaft before swirling it back and forth and around her big, sexy balls ..."
                                                wt_image indy_futanari_2_33
                                                "... eventually taking her sack into your mouth and tea-bagging her gently."
                                                wt_image indy_futanari_2_11
                                                terri.c "Oohhhh, I can't take that teasing anymore.  Kneel down in front of me, I want to feel my cock in your mouth."
                                                add tags 'you_licked_her_balls' to terri
                                            "No, I'm just going to suck your cock today":
                                                wt_image indy_futanari_2_26
                                                player.c "For today, just open your knees so I can suck your cock, [terri.name]."
                                            "No, never (shuts off question)":
                                                wt_image indy_futanari_2_26
                                                player.c "Don't be gross, [terri.name].  Just open your knees so I can suck your cock."
                                                add tags 'you_no_ball_licking' to terri
                                    else:
                                        terri.c "Thank you!"
                                else:
                                    wt_image indy_futanari_2_8
                                    terri.c "What?  No, that would be wrong.  You have a cock, too."
                                    player.c "I'll decide for myself what's right or wrong on that front.  Besides, I'm your trainer and I haven't trained you on how to receive a blowjob, yet, have I?"
                                    wt_image indy_futanari_2_5
                                    terri.c "Well, no, you haven't."
                                    player.c "And that's something you'd like to learn, isn't it?"
                                    wt_image indy_futanari_2_44
                                    terri.c "It is, actually.  I'm getting a stiffer erection, just thinking about a pair of lips wrapped around my cock."
                                    player.c "Show me."
                                    wt_image indy_futanari_2_9
                                    player.c "First lesson about getting a blowjob, [terri.name].  It'll feel better on your bare cock, rather than through your dress.  You do want to feel my lips and tongue on your bare cock, don't you?"
                                    wt_image indy_futanari_2_45
                                    if not terri.has_tag('you_no_ball_licking'):
                                        terri.c "Yes, I do.  Thank you!  Will you worship my balls, too?"
                                        $ title = "What do you tell her?"
                                        menu:
                                            "Yes, I'll worship your balls":
                                                wt_image indy_futanari_2_46
                                                player.c "Spread your legs and give me access."
                                                wt_image indy_futanari_2_27
                                                "Her cock twitches in anticipation as you kneel between her legs ..."
                                                wt_image indy_futanari_2_47
                                                "... and run your tongue up and down the sensitive underside of her shaft before swirling it back and forth and around her big, sexy balls ..."
                                                wt_image indy_futanari_2_48
                                                "... eventually taking her sack into your mouth and tea-bagging her gently."
                                                wt_image indy_futanari_2_27
                                                terri.c "Oohhhh, I can't take that teasing anymore.  I want to feel my cock in your mouth."
                                                add tags 'you_licked_her_balls' to terri
                                            "No, I'm just going to suck your cock today":
                                                wt_image indy_futanari_2_46
                                                player.c "For today, just give me your cock to suck, [terri.name]."
                                            "No, never (shuts off question)":
                                                wt_image indy_futanari_2_46
                                                player.c "Don't be gross, [terri.name].  Just give me your cock to suck."
                                                add tags 'you_no_ball_licking' to terri
                                    else:
                                        terri.c "Yes, I do.  Thank you!"
                                wt_image indy_futanari_2_34
                                "She offers her cock to you with both hands and you lick gently around the head and tip ..."
                                wt_image indy_futanari_2_35
                                "... before opening wide and taking her thick dick into your mouth."
                                if terri.has_tag('cock_out_now'):
                                    wt_image indy_futanari_2_30
                                else:
                                    wt_image indy_futanari_2_46
                                "When you sense she's getting close, you stop and look at her."
                                player.c "Show me how you want me to suck you."
                                wt_image indy_futanari_2_36
                                "As you resume sucking her, she tentatively places a hand on your head ..."
                                wt_image indy_futanari_2_37
                                "... and starts guiding you around her cock, showing you where she wants you to kiss and lick ..."
                                wt_image indy_futanari_2_36
                                "... before grabbing your head more firmly and vigorously face-fucking you."
                                wt_image indy_futanari_2_38
                                "Just as you're starting to gag, she pulls out of your mouth ..."
                                wt_image indy_futanari_2_39
                                "... and finishes on your face."
                                wt_image indy_futanari_2_40
                                terri.c "Oooohhhhhh!!!!"
                                wt_image indy_futanari_2_41
                                terri.c "Oh, wow!  That's the best lesson you've ever taught me.  I guess we both need to clean ourselves up, I shot a lot of cum on you and got some on myself, too."
                                $ title = "What now?"
                                menu:
                                    "Clean her up with your mouth":
                                        wt_image indy_futanari_2_23
                                        player.c "The lesson's not over.  I'm the one responsible for the mess on your cock and hands.  Don't be afraid to expect me to clean it up."
                                        wt_image indy_futanari_2_42
                                        "[terri.name] offers her cock to you and watches as you lick her cum off it and her fingers."
                                        wt_image indy_futanari_2_27
                                        terri.c "That really was an amazing lesson!  I like getting blowjobs a lot more than I ever liked giving them.  You should probably wipe the cum off your face, now, it's dripping off your chin and making even more of a mess.  I'll just see myself out.  Thanks for a great visit!"
                                        add tags 'you_cleaned_her_cock' to terri
                                    "Just clean yourself":
                                        wt_image indy_futanari_2_10
                                        "[terri.name] wipes herself clean with her dress.  Presumably she'll wash it when she gets home."
                                        wt_image indy_futanari_2_43
                                        terri.c "Thanks for the lesson.  I liked getting a blowjob a lot more than I ever liked giving them.  Thanks for a great visit!"
                            else:
                                if terri.has_tag('cock_out_now'):
                                    wt_image indy_futanari_1_29
                                    terri.c "What?  No, that would be wrong.  You have a cock, too."
                                    player.c "I'll decide for myself what's right or wrong on that front.  Besides, I'm your trainer and I haven't trained you on how to receive a blowjob, yet, have I?"
                                    wt_image indy_futanari_1_28
                                    terri.c "Well, no, you haven't."
                                    player.c "And that's something you'd like to learn, isn't it?"
                                    wt_image indy_futanari_1_40
                                    terri.c "It is, actually.  My cock's getting even harder, thinking about a pair of lips wrapped around it."
                                    player.c "Then let me teach you what it's like."
                                    if not terri.has_tag('you_no_ball_licking'):
                                        wt_image indy_futanari_1_37
                                        terri.c "Thank you!  Will you worship my balls, too?"
                                        $ title = "What do you tell her?"
                                        menu:
                                            "Yes, I'll worship your balls":
                                                wt_image indy_futanari_1_35
                                                "Her cock twitches in anticipation as you kneel between her legs."
                                                wt_image indy_futanari_1_60
                                                "It twitches even more as you run your tongue up and down the sensitive underside of her shaft, before turning your attention to her balls."
                                                wt_image indy_futanari_1_61
                                                "It's more difficult to pleasure her balls with her panties still on, but the moans that escape her throat as you lick her balls around the edges and through the thin fabric of the panties tell you how much she's enjoying this."
                                                wt_image indy_futanari_1_62
                                                terri.c "Oohhhh, I can't take that teasing anymore.  I want to feel my cock in your mouth."
                                                add tags 'you_licked_her_balls' to terri
                                            "No, I'm just going to suck your cock today":
                                                wt_image indy_futanari_1_62
                                                player.c "For today, just give me your cock to suck, [terri.name]."
                                            "No, never (shuts off question)":
                                                wt_image indy_futanari_1_62
                                                player.c "Don't be gross, [terri.name].  Just give me your cock to suck."
                                                add tags 'you_no_ball_licking' to terri
                                    else:
                                        wt_image indy_futanari_1_62
                                        terri.c "Thank you!"
                                else:
                                    wt_image indy_futanari_1_2
                                    terri.c "What?  No, that would be wrong.  You have a cock, too."
                                    player.c "I'll decide for myself what's right or wrong on that front.  Besides, I'm your trainer and I haven't trained you on how to receive a blowjob, yet, have I?"
                                    wt_image indy_futanari_1_3
                                    terri.c "Well, no, you haven't."
                                    player.c "And that's something you'd like to learn, isn't it?"
                                    wt_image indy_futanari_1_34
                                    terri.c "It is, actually.  My cock's getting even harder, thinking about a pair of lips wrapped around it."
                                    player.c "Then let me teach you what it's like."
                                    if not terri.has_tag('you_no_ball_licking'):
                                        wt_image indy_futanari_1_33
                                        terri.c "Thank you!  Will you worship my balls, too?"
                                        $ title = "What do you tell her?"
                                        menu:
                                            "Yes, I'll worship your balls":
                                                wt_image indy_futanari_1_75
                                                "Her cock twitches in anticipation as you kneel at her feet."
                                                wt_image indy_futanari_1_76
                                                "It twitches even more as you run your tongue up and down the sensitive underside of her shaft, before turning your attention to her balls."
                                                wt_image indy_futanari_1_77
                                                "It's more difficult to pleasure her balls with her panties still on, but the moans that escape her throat as you lick her balls around the edges and through the thin fabric of the panties tell you how much she's enjoying this."
                                                wt_image indy_futanari_1_75
                                                terri.c "Oohhhh, I can't take that teasing anymore.  I want to feel my cock in your mouth."
                                                add tags 'you_licked_her_balls' to terri
                                            "No, I'm just going to suck your cock today":
                                                wt_image indy_futanari_1_6
                                                player.c "For today, just give me your cock to suck, [terri.name]."
                                            "No, never (shuts off question)":
                                                wt_image indy_futanari_1_6
                                                player.c "Don't be gross, [terri.name].  Just give me your cock to suck."
                                                add tags 'you_no_ball_licking' to terri
                                    else:
                                        wt_image indy_futanari_1_23
                                        terri.c "Thank you!"
                                wt_image indy_futanari_1_63
                                "[terri.name] stands over you and feeds her thick cock into your waiting mouth."
                                wt_image indy_futanari_1_64
                                "You bob your head back and forth, your lips wrapped tightly around her shaft, your tongue licking at the underside as you suck her.  When you sense she's getting close, you stop and look at her."
                                if terri.has_tag('cock_out_now'):
                                    wt_image indy_futanari_1_59
                                else:
                                    wt_image indy_futanari_1_75
                                player.c "Show me how you want me to suck you."
                                wt_image indy_futanari_1_64
                                "As you resume sucking her, she tentatively places a hand on your head ..."
                                wt_image indy_futanari_1_66
                                "... and starts guiding you around her cock ..."
                                wt_image indy_futanari_1_67
                                "... showing you where she wants you to kiss and lick ..."
                                wt_image indy_futanari_1_65
                                "... before grabbing your head more firmly and vigorously face-fucking you."
                                wt_image indy_futanari_1_68
                                "Just as you're starting to gag, she pulls out of your mouth and sits directly in front of you ..."
                                wt_image indy_futanari_1_69
                                "... and finishes on your face."
                                wt_image indy_futanari_1_70
                                terri.c "Oooohhhhhh!!!!"
                                wt_image indy_futanari_1_71
                                terri.c "Oh, wow!  That's the best lesson you've ever taught me.  I guess we both need to clean ourselves up, I shot a lot of cum on you and got some on myself and the chair, too."
                                wt_image indy_futanari_1_72
                                $ title = "What now?"
                                menu:
                                    "Clean her up with your mouth":
                                        wt_image indy_futanari_1_73
                                        player.c "The lesson's not over.  Put the tissue away.  I'm the one responsible for the mess on your cock and hands.  Don't be afraid to expect me to clean it up."
                                        wt_image indy_futanari_1_74
                                        "[terri.name] offers her cock to you and watches as you lick her cum off it and her fingers."
                                        wt_image indy_futanari_1_34
                                        terri.c "That really was an amazing lesson!  I like getting blowjobs a lot more than I ever liked giving them.  You should probably wipe the cum off your face, now, it's dripping off your chin and making even more of a mess.  I'll just see myself out.  Thanks for a great visit!"
                                        add tags 'you_cleaned_her_cock' to terri
                                    "Just clean yourself":
                                        wt_image indy_futanari_1_41
                                        "[terri.name] wipes the cum off her hands and cock with some tissues while you do the same with the cum on your face."
                                        wt_image indy_futanari_1_34
                                        terri.c "Thanks for the lesson.  I liked getting a blowjob a lot more than I ever liked giving them.  Thanks for a great visit!"
                        add tags 'you_sucked_her_cock' to terri
                        change player energy by -energy_very_short notify
                        call terri_futanari_send_home from _call_terri_futanari_send_home_1
                    "Nothing":
                        pass
        "Ask her to show you her cock" if not terri.has_tag('cock_out_now'):
            if terri.futanari_outfit == 2:
                if not terri.has_tag('aroused_now'):
                    wt_image indy_futanari_2_5
                    terri.c "It's not hard, at least not fully, and for a change I'm not horny right now.  I should probably keep it in my dress for this visit."
                    wt_image indy_futanari_2_6
                    $ title = "What do you tell her"
                    menu:
                        "Make it hard for me":
                            if terri.test('submission', 30):
                                wt_image indy_futanari_2_8
                                terri.c "Yes, [terri.your_respect_name], if that's what you want."
                                wt_image indy_futanari_2_7
                                "She rubs the head of her cock through her dress as it stiffens and becomes erect."
                                wt_image indy_futanari_2_2
                                terri.c "Is that better, [terri.your_respect_name]?"
                            else:
                                wt_image indy_futanari_2_5
                                terri.c "Why?  If you're really about my cock, isn't this enough?"
                                wt_image indy_futanari_2_6
                                player.c "I'd like to see you aroused.  Run your hand along your cock.  If you're really not horny, that shouldn't do much."
                                wt_image indy_futanari_2_8
                                terri.c "I don't think you understand how sensitive my cock is."
                                wt_image indy_futanari_2_7
                                terri.c "See?  It's already getting hard."
                                wt_image indy_futanari_2_2
                                terri.c "Happy now?"
                            menu:
                                "I want a better view":
                                    wt_image indy_futanari_2_9
                                    terri.c "This is as erect as it gets."
                                    player.c "Are you sure?  Lie down and stroke it for me."
                                    wt_image indy_futanari_2_10
                                    player.c "Good girl.  Now open your dress and show me how sexy you are."
                                    wt_image indy_futanari_2_11
                                    terri.c "You like seeing me like this?"
                                    wt_image indy_futanari_2_15
                                    player.c "I do, but I like it even better when you touch yourself."
                                    wt_image indy_futanari_2_16
                                    terri.c "I guess you're in luck, then, because I'm going to have a hard time not touching myself now that I'm worked up, again."
                                    add tags 'cock_out_now' to terri
                                "That's good":
                                    wt_image indy_futanari_2_7
                                    terri.c "Good for you, maybe.  Getting erect is making me horny again."
                                    add tags 'aroused_now' to terri
                        "She can keep it in her dress":
                            wt_image indy_futanari_2_4
                            terri.c "Thank you."
                else:
                    wt_image indy_futanari_2_2
                    terri.c "It's pretty obvious already, isn't it?"
                    menu:
                        "I want a better view":
                            wt_image indy_futanari_2_9
                            terri.c "This is as erect as it gets."
                            player.c "Are you sure?  Lie down and stroke it for me."
                            wt_image indy_futanari_2_10
                            player.c "Good girl.  Now open your dress and show me how sexy you are."
                            wt_image indy_futanari_2_11
                            terri.c "You like seeing me like this?"
                            wt_image indy_futanari_2_15
                            player.c "I do, but I like it even better when you touch yourself."
                            wt_image indy_futanari_2_16
                            terri.c "I guess you're in luck, then, because I'm going to have a hard time not touching myself now that I'm worked up, again."
                            add tags 'cock_out_now' to terri
                        "I guess this view is good":
                            wt_image indy_futanari_2_7
                            terri.c "Good for you, maybe.  Getting erect is making me horny again."
            else:
                wt_image indy_futanari_1_23
                terri.c "Well, I'm not exactly hiding it."
                wt_image indy_futanari_1_2
                player.c "You could make it harder for me, though, couldn't you?"
                wt_image indy_futanari_1_3
                terri.c "You wouldn't mind?  I've been fighting the urge to stroke myself too much, because I didn't think you'd want to see me fully erect."
                wt_image indy_futanari_1_4
                player.c "I wouldn't mind at all.  I'd like to see how big your cock gets."
                wt_image indy_futanari_1_5
                terri.c "It gets pretty big."
                wt_image indy_futanari_1_26
                terri.c "Wouldn't you rather see my tits, instead?  They're a lot smaller than my cock, but maybe you'd enjoy the sight of them more?"
                wt_image indy_futanari_1_22
                player.c "Can't I look at both?"
                wt_image indy_futanari_1_27
                terri.c "If that's what you want?"
                wt_image indy_futanari_1_28
                player.c "It is, but I want you to keep your legs spread, so I can see your balls, too."
                wt_image indy_futanari_1_29
                player.c "Much better.  How does that feel?"
                wt_image indy_futanari_1_30
                terri.c "Weird, but I'm horny so keeping my cock hard feels good.  I need to use my dress to stroke myself, though.  Using my hand would feel too intense."
                add tags 'cock_out_now' to terri
        "Chit chat":
            if terri.futanari_outfit == 2:
                if terri.has_tag('cock_out_now'):
                    wt_image indy_futanari_2_16
                    "As the two of you chat, [terri.name] ideally strokes her cock ..."
                    wt_image indy_futanari_2_18
                    "... and keeps closing her legs and squeezing them together."
                    wt_image indy_futanari_2_17
                    player.c "Does squeezing your thighs together feel good against your balls?"
                    wt_image indy_futanari_2_18
                    terri.c "Yes, so fucking good.  I wasn't feeling horny before I came over, but now I am, again."
                    wt_image indy_futanari_2_19
                    terri.c "I don't know how you guys ever get any work done, I feel like I need to play with my cock and balls constantly once I start feeling like this."
                elif terri.has_tag('aroused_now'):
                    wt_image indy_futanari_2_8
                    "As the two of you chat, [terri.name] rubs the head of her cock through her dress."
                    wt_image indy_futanari_2_2
                    terri.c "This is so nice, being able to have a normal conversation like this."
                    wt_image indy_futanari_2_8
                    player.c "Especially while your cock is erect?"
                    wt_image indy_futanari_2_2
                    terri.c "Well, my cock is erect most of the time, to be honest."
                    wt_image indy_futanari_2_7
                    terri.c "What's really nice is to be able to visit and talk with you like two normal friends, while my cock is erect."
                else:
                    wt_image indy_futanari_2_6
                    "As the two of you chat ..."
                    wt_image indy_futanari_2_7
                    "... you notice the front of [terri.name]'s dress rise ..."
                    wt_image indy_futanari_2_4
                    "... and fall."
                    wt_image indy_futanari_2_6
                    player.c "Is this conversation turning you on?"
                    wt_image indy_futanari_2_8
                    terri.c "What?  No, why do you ask?"
                    wt_image indy_futanari_2_5
                    player.c "Your cock keeps getting erect."
                    wt_image indy_futanari_2_2
                    terri.c "I know.  Mine does that all the time.  I thought that was normal."
                    wt_image indy_futanari_2_6
                    player.c "Only if you're excited."
                    wt_image indy_futanari_2_4
                    if terri.discussed_transformation == 0:
                        terri.c "I am really enjoying being able to have a normal conversation with you.  That's probably all it is.  I get excited really easily ever since I got a cock."
                    else:
                        terri.c "I am really enjoying being able to have a normal conversation with you.  That's probably all it is.  I get excited really easily ever since you gave me a cock."
            else:
                if terri.has_tag('cock_out_now'):
                    wt_image indy_futanari_1_27
                    "As the two of you chat, you notice [terri.name] keeps closing her legs and squeezing them together."
                    wt_image indy_futanari_1_28
                    terri.c "Sorry, I know you wanted me to keep my legs apart, it's just ..."
                    wt_image indy_futanari_1_27
                    player.c "Squeezing your thighs together feels good against your balls?"
                    wt_image indy_futanari_1_29
                    terri.c "So fucking good.  I don't know how you guys ever get any work done, it takes all the willpower I have not to play with my cock and balls constantly."
                else:
                    wt_image indy_futanari_1_32
                    "As the two of you chat, [terri.name] ideally strokes her cock ..."
                    wt_image indy_futanari_1_33
                    "... and rubs her balls."
                    wt_image indy_futanari_1_34
                    terri.c "This is so nice, being able to have a normal conversation like this."
                    wt_image indy_futanari_1_4
                    player.c "While you play with yourself?"
                    wt_image indy_futanari_1_5
                    terri.c "Yes, exactly!  My cock and balls need so much attention ..."
                    wt_image indy_futanari_1_33
                    terri.c "... I'm so glad you let me visit and talk with you like two normal friends."
        "Nothing else (send her home)":
            call terri_futanari_send_home from _call_terri_futanari_send_home_2
    return

label terri_futanari_send_home:
    $ terri.training_session()
    rem tags 'aroused_now' 'cock_out_now' from terri
    call character_location_return(terri) from _call_character_location_return_725
    wt_image current_location.image
    return

# View Relationship Status
label terri_relationship_status:
    call terri_description_display from _call_terri_description_display_1
    wt_image current_location.image
    return

# Review Files
label terri_review_files:
    call terri_description_display from _call_terri_description_display_2
    wt_image current_location.image
    return

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_terri:
    if terri.has_item(butt_plug):
        "You've already gifted [terri.name] a butt plug.  She only needs one."
    elif terri.status == "on_training":
        if terri.state == 1:
            wt_image indy_talk_state_1_2
        elif terri.state == 2:
            wt_image indy_talk_state_2_5
        elif terri.state == 3:
            wt_image indy_hypno_state_3_1
        elif terri.state == 4:
            wt_image indy_hypno_state_4_5
        elif terri.state == 5:
            wt_image indy_hypno_state_5_1
        "[terri.name] blushes when she opens your gift."
        terri.c "What is this for?"
        player.c "It's to help prepare you to please your boyfriend. You want to be the best girlfriend possible to him, don't you?"
        if terri.state == 1:
            wt_image indy_hypno_state_1_2
        elif terri.state == 2:
            wt_image indy_hypno_state_2_2
        elif terri.state == 3:
            wt_image indy_hypno_state_3_5
        elif terri.state == 4:
            wt_image indy_talk_state_4_11
        elif terri.state == 5:
            wt_image indy_talk_state_5_6
        "She nods."
        if terri.state == 1:
            wt_image indy_strip_state_1_2
        elif terri.state == 2:
            wt_image indy_strip_state_2_13
        elif terri.state == 3:
            wt_image indy_strip_state_3_13
        elif terri.state == 4:
            wt_image indy_strip_state_4_1
        elif terri.state == 5:
            wt_image indy_strip_state_5_1
        player.c "Turn around then and drop your panties, and I'll show you how it works."
        wt_image indy_butt_plug_1
        "When the plug enters her, she gasps."
        wt_image indy_butt_plug_2
        terri.c "Oohh!  How long should I wear this?"
        player.c "Until having something in there feels natural."
        if terri.state == 1:
            wt_image indy_talk_state_1_2
        elif terri.state == 2:
            wt_image indy_hypno_state_2_2
        elif terri.state == 3:
            wt_image indy_hypno_state_3_5
        elif terri.state == 4:
            wt_image indy_talk_state_4_8
        elif terri.state == 5:
            wt_image indy_talk_state_5_2
        "She nods again, her face blushing even more."
        change terri submission by 10
        give 1 butt_plug from player to terri notify
        wt_image current_location.image
    elif terri.has_tag('slavegirl'):
        "She'll only get to use it when you want her to, and where you want her to, but you set a butt plug aside for your slavegirl."
        give 1 butt_plug from player to terri notify
    else:
        "You should save the butt plug for someone else."
    return

# Give Chastity Belt
label give_cb_terri:
    if terri.status == 'on_training':
        "[terri.name]'s trying to be the best girlfriend she can be for her boyfriend. Locking him out of her pussy isn't going to help."
    else:
        "Save this for someone else."
    return

# Give Dildo
label give_di_terri:
    if terri.has_item(dildo):
        "You've already gifted [terri.name] a dildo.  One is enough."
    elif terri.status == "on_training":
        "It's tough to do your homework without the right tools at home."
        if terri.state == 1:
            wt_image indy_talk_state_1_1
        elif terri.state == 2:
            wt_image indy_talk_state_2_5
        elif terri.state == 3:
            wt_image indy_talk_state_3_8
        elif terri.state == 4:
            wt_image indy_talk_state_4_11
        elif terri.state == 5:
            wt_image indy_talk_state_5_2
        player.c "Remember, [terri.name], practice makes perfect."
        give 1 dildo from player to terri notify
        wt_image current_location.image
    elif terri.has_tag('slavegirl'):
        "She'll only get to use it when you want her to, and where you want her to, but you set a dildo aside for your slavegirl."
        give 1 dildo from player to terri notify
    else:
        "You should save this for someone else."
    return

# Use Fetch Toy
label use_ft_terri:
    "You shouldn't try to play fetch with someone who isn't your pet."
    return

# Give Jewelry
label give_jwc_terri:
    "Save this as a gift for [chelsea.name]."
    return

# Use Leash
label use_le_terri:
    "You shouldn't try to take someone for a walk who isn't your pet."
    return

# Give Lingerie
label give_li_terri:
    if terri.has_item(lingerie):
        if terri.has_tag('doll'):
            "You'll need to dress her in it yourself if you want to see what it looks like on her."
        else:
            "You've already gifted lingerie to [terri.name]. She has enough for now."
    elif terri.status == "on_training":
        $ title = "What type of lingerie do you want to gift to [terri.name]?"
        menu:
            "Cheerleader outfit":
                if terri.state == 1:
                    wt_image indy_hypno_state_1_2
                elif terri.state == 2:
                    wt_image indy_talk_state_2_2
                elif terri.state == 3:
                    wt_image indy_talk_state_3_5
                elif terri.state == 4:
                    wt_image indy_talk_state_4_9
                elif terri.state == 5:
                    wt_image indy_talk_state_5_3
                "Although not strictly lingerie, the cheerleader outfit could serve a similar purpose.  [terri.name]'s eyes light up when she sees it."
                terri.c "Oh!  How cute!!  You don't think I'll look ridiculous wearing it, will I?  I mean, I'm not a teenager anymore, as much as I'd love to be."
                player.c "I think it will look great on you, [terri.name]."
                if terri.state == 1:
                    wt_image indy_portrait_state_1
                elif terri.state == 2:
                    wt_image indy_portrait_state_2
                elif terri.state == 3:
                    wt_image indy_talk_state_3_2
                elif terri.state == 4:
                    wt_image indy_talk_state_4_1
                elif terri.state == 5:
                    wt_image indy_talk_state_5_4
                "She beams."
                add tags 'lingerie_cheerleader' to terri
                #$ terri.action_show_off_lingerie = terri.add_action("Have Her Show Off Her Cheerleader Outfit", label="_show_off_lingerie", condition = "terri.lingerie_action_used == 1")  ## moved to pregame
                $ terri.action_show_off_lingerie.name = "Have show off her cheerleader outfit"
            "Sexy bra and panties":
                if terri.state == 1:
                    wt_image indy_hypno_state_1_2
                elif terri.state == 2:
                    wt_image indy_talk_state_2_2
                elif terri.state == 3:
                    wt_image indy_talk_state_3_5
                elif terri.state == 4:
                    wt_image indy_talk_state_4_9
                elif terri.state == 5:
                    wt_image indy_talk_state_5_3
                "[terri.name] smiles when she sees the outfit."
                terri.c "Do you think this is something I should wear for my boyfriend?"
                player.c "I'll let you know once I've seen you model it."
                add tags 'lingerie_sexy' to terri
                #$ terri.action_show_off_lingerie = terri.add_action("Have Her Show Off Her Lingerie", label="_show_off_lingerie", condition = "terri.lingerie_action_used == 1")
        $ terri.lingerie_action_used = 1 ## opens up show_off action
        give 1 lingerie from player to terri notify
    elif terri.has_tag('doll'):
        "You'll need to dress her in it yourself if you want to see what it looks like on her."
    else:
        "You should save the lingerie for a current client."
    return

# Give Love Potion
label give_lp_terri:
    if terri.has_tag('love_potion_used'):
        "You've already used a love potion on her.  Additional ones won't work."
    elif terri.status == "post_training" and terri.has_tag('adult_baby'):
        wt_image indy_crib_2
        player.c "Hi baby girl.  I brought you a bottle."
        "She takes the bottle from your hands and begins to suckle it."
        wt_image indy_crib_3
        "Soon she's guzzling the whole bottle, as fast as she can suck it through the nipple."
        wt_image indy_crib_7
        "As she finishes drinking, she clutches her favorite toy to her chest and looks up at you with pure adoration."
        terri.c "Goo goo ga ga!!   Goo goo ga ga!!"
        "You're pretty sure that's baby talk for baby girl loves her [terri.your_daddy_name] sooo much."
        add tags 'love_potion_used' to terri
        rem 1 love_potion from player notify
        $ terri.maintain_week_baby = week + 4
        wt_image current_location.image
    elif terri.status == "on_training":
        wt_image indy_drink_1_2
        player.c "Here, [terri.name].  I fixed you a drink."
        terri.c "Oh?  What is it?  It's not strong is it?"
        wt_image indy_drink_1_4
        player.c "No, just some fruit juice and special herbs."
        terri.c "Mmmm.  It looks good."
        wt_image indy_drink_1_5
        "[terri.name] takes a sip, then a second ... then she spaces out for a few minutes as the potion takes effect."
        wt_image indy_drink_1_3
        "A few minutes later she regains her senses, seemingly unaware that time has passed.  She takes a seat beside you."
        terri.c "I really enjoy spending time with you.  You're like my best friend, or the brother I never had.  Which is crazy, I know, because I barely know you.  But I just feel like we have this connection."
        wt_image indy_drink_1_6
        player.c "Like we're meant to be lovers?"
        "She laughs."
        wt_image indy_drink_1_19
        terri.c "No, silly.  I mean like something spiritual, like we're soul mates or something."
        $ terri.lesbian_clues += 2
        add tags 'love_potion_used' to terri
        rem 1 love_potion from player notify
    else:
        "You should save the love potion for someone else."
    return

# Give Transformation Potion
label give_tp_terri:
    if terri.has_tag('transformed'):
        "[terri.full_name] has already been transformed. There's nothing more the potion can do to her now."
    elif terri.has_tag('assistant_trouble'):
        "I don't think she can drink it in this condition."
    elif terri.has_tag('assistant'):
        wt_image indy_assistant_1
        terri.c "No thanks.  I don't like to drink anymore.  I find it interferes with my study and my powers of concentration."
    elif terri.cheerleader_outfit_visit == 3 or terri.cheerleader_outfit_visit == 6:
        terri.c "I shouldn't drink when I'm a cheerleader.  I think that would get me kicked off the squad."
        player.c "Only if you got caught."
        terri.c "I'm too much of a goody-two-shoes to risk it."
    else:
        if terri.boobjob_interest > 1 and not terri.has_tag('boob_job') and not cassandra.independent_encounter_status > 1 and not marilyn.independent_encounter_status > 1:
            "You might gain a different option for [terri.name] if you wait."
            $ title = "Proceed anyway?"
            menu:
                "Yes, proceed":
                    pass
                "No, wait":
                    return
        if terri.lesbian_clues > 2 and terri.discussed_transformation == 0:
            $ title = "Do you want to discuss transformation with [terri.name] first?"
            menu:
                "Yes, discuss with her first":
                    call terri_transformation_discussion from _call_terri_transformation_discussion_1
                "No, just use the potion":
                    call terri_transformation_potion_timer from _call_terri_transformation_potion_timer
        else:
            call terri_transformation_potion_timer from _call_terri_transformation_potion_timer_1
    return

# Give Ring of Secuality
label give_rs_terri:
    "The ring is magic, but not a powerful enough magic to sort out [terri.name]'s messed up sexual feelings."
    return

# Use Water Bowl
label use_wb_terri:
    "You shouldn't offer water in a bowl to anyone who isn't your pet."
    return

# Use Will Tamer
label use_wt_terri:
    if terri.has_tag('assistant_trouble'):
        "Putting this on her in this condition isn't going to work."
    elif terri.has_tag('transformed'):
        "She's already been transformed. The Will-Tamer can do nothing to her now."
    else:
        terri.c "Uh, that kind of weirds me out. How about we do something else?"
    return

label lpt_examine:
    wt_image lpt_image
    if terri.has_tag('adult_baby'):
        "Your baby girl [terri.name] would probably enjoy this treat."
    else:
        "You're not sure how you got this or why, but it's likely more calories than it's worth."
    wt_image current_location.image
    return

label lpt_buy:
    if not player.has_item(lollipop_terri):
        wt_image lpt_image
        "The lollies cost next to nothing, and [terri.name] would likely enjoy one.  Pay 1 for a lollipop?"
        $ title = "Buy one?"
        menu:
            "Yes":
                if player.money - player.min_money >= 1:
                    $ player.money -= 1
                    rem 1 lollipop_terri from coffee_shop
                    add 1 lollipop_terri to player notify
                else:
                    "You can't afford one right now."
            "No":
                pass
    else:
        "The one you have is enough for now."
    wt_image current_location.image
    return

label lpt_give_terri:
    if terri.is_here:
        if current_location == bedroom and terri.has_tag('adult_baby') and terri.can_be_interacted:
            wt_image indy_lolly_1_1
            player.c "Would you like a treat, baby girl?"
            wt_image indy_lolly_1_2
            player.c "It's a lollipop.  You like lollies, don't you?"
            wt_image indy_lolly_1_3
            terri.c "Mmmmm!"
            wt_image indy_lolly_1_4
            "After taking a few licks, [terri.name] places the sticky lolly on her breast ..."
            wt_image indy_lolly_1_5
            "... and gives you a look that makes it clear she's wondering if [terri.your_daddy_name] wants a thank you for the treat?"
            $ title = "Do you want to enjoy her while she enjoys her lollipop"
            menu:
                "No, just let her enjoy the treat":
                    wt_image indy_lolly_1_6
                    "[terri.name]'s bright smile as she enjoys the candy is the only thanks you need, today."
                "Yes, turn her around and fuck her":
                    wt_image indy_lolly_1_7
                    "You turn [terri.name] around and pull down her panties."
                    wt_image indy_lolly_1_8
                    "She goes back to licking her lolly ..."
                    wt_image indy_lolly_1_9
                    "... while you amuse yourself with the things that interest you."
                    wt_image indy_lolly_1_10
                    "[terri.name] pays no attention to you as you plow her ..."
                    wt_image indy_lolly_1_11
                    "... looking back at you only when you flood her insides with your seed."
                    player.c "[player.orgasm_text]"
                    wt_image indy_lolly_1_12
                    "Then she pulls her panties back up ..."
                    wt_image indy_lolly_1_13
                    "... and goes back to her candy, sporting a mischievous grin."
                    $ terri.sex_count += 1
                    orgasm
                    $ terri.training_session()
            $ terri.maintain_week_baby += 4
            add 1 lollipop_terri to coffee_shop
            rem 1 lollipop_terri from player notify
            wt_image current_location.image
        elif current_location == bedroom and terri.has_tag('adult_baby'):
            "She's had enough excitement for today.  Maybe give this to her tomorrow."
        elif not terri.has_tag('adult_baby'):
            "She's no longer interested in those."
        else:
            "Not here."
    else:
        "[terri.name] isn't here."
    return

label lpt_throw_away:
    "It would have been bad for your teeth, anyway."
    if terri.has_tag('adult_baby'):
        add 1 lollipop_terri to coffee_shop
    rem 1 lollipop_terri from player notify
    return

########### TIMERS ###########
## Common Timers
# End Training Permanently
# TIMER: Check Client Engagement Ends
label terri_end_training:
    # bonus to SOS for youth interest
    if terri.youth_interest > 5:
        $ terri.temporary_count = 25
    elif terri.youth_interest < 2:
        $ terri.temporary_count = 0
    else:
        $ terri.temporary_count = terri.youth_interest*5
    change terri sos by terri.temporary_count
    $ terri.temporary_count = 0
    wt_image terri.image
    "Your engagement to train [terri.full_name] has now ended.  She gives you a quick call."
    if terri.sos > 50:
        call convert(terri,"satisfied",False,True) from _call_convert_105
        add tags 'continuing_actions' to terri
        terri.c "Hi! I wanted to give you a call to thank you for all your help."
        terri.c "I really feel like I can be a great girlfriend for my boyfriend now, and it's all thanks to you."
        terri.c "I'll make sure everybody knows what a great job you did. Thanks again!"
        if terri.has_tag('love_potion_used'):
          terri.c "I hope we can still get together, even though my training is over. Maybe for a drink or something? I feel like we have such a connection. I would miss not seeing you and telling you about what's going on in my life."
        $ terri.action_end_session.name = "End visit"
    else:
        terri.c "Hi. I wanted to give you a call to thank you for your training."
        terri.c "I'm not sure I'm really as good a girlfriend to my boyfriend as he deserves. Not yet anyway. I think you tried your best. I'm probably not a very good student."
        terri.c "Anyways, thanks for trying to help me."
        if terri.has_tag('love_potion_used'):
            terri.c "I hope we can still get together, even though my training is over. Maybe for a drink or something? I feel like we have such a connection. I would miss not seeing you and telling you about what's going on in my life."
            $ terri.change_status("post_training")
            add tags 'continuing_actions' to terri
            $ terri.action_end_session.name = "End visit"
        else:
            call convert(terri,"unsatisfied",True,True) from _call_convert_106
    wt_image current_location.image
    return

# Start Day
label terri_start_day:
  ## Assistant Trouble
  if terri.has_tag('assistant_trouble'):
    "You didn't see [terri.name] come out of her room all day yesterday."
  return

# End Day
label terri_end_day:
    if terri.has_tag('sleep_visit_today'):
        rem tags 'aroused_now' 'sleep_visit_today' 'sleep_hypno_today' 'sleep_touched' 'sleep_bra_removed' 'sleep_panties_removed' 'sleep_fingered' from terri
    if terri.status == "on_training" or terri.has_tag('continuing_actions'):
        rem tags 'aroused_now' 'boobs_out_now' 'cock_out_now' 'cheerleader_visit_now' 'discussed_boobs_today' 'regular_visit_now' 'talked_today' from terri
    if terri.has_tag('slavegirl'):
        rem tags 'slavegirl_let_out' from terri
    if terri.has_tag('adult_baby'):
        rem tags 'diaper_checked_today' from terri
    call character_location_return(terri) from _call_character_location_return_726
    return

## Lawyer Content
label terri_janice_talk_option:
    if terri.has_tag('likes_girls') and janice.has_tag('asked_about_hiring') and not janice.has_tag('discussed_terri'):
        "You discuss [terri.name]'s acceptance of her interest in other women with [janice.name]."
        janice.c "Sorry. She doesn't sound like my type. Get back to me when you've found someone blonder and more married."
        player.c "That's a strangely specific compulsion you have, you know?"
        add tags 'discussed_terri' to janice
        $ janice.temporary_count = 0
    return

## Marilyn Content
label terri_marilyn_talk_option:
    if terri.ready_for_marilyn > 0:
        if terri.status == "on_training" and marilyn.independent_encounter_status == 1:
            if not marilyn.has_tag('discussed_terri'):
                "You fill [marilyn.name] in on your discussions with [terri.name]."
                marilyn.c "Well, well.  That is an intriguing scenario.  Let me know the time and place, and I'll be there to give this little girl the Mommy-figure she's looking for."
                add tags 'discussed_terri' to marilyn
            else:
                marilyn.c "Let me know what you want me to play 'Mommy' for your Mommy-issues client."
            sys "You can set up [marilyn.name] to meet [terri.name] on a future training session."
        elif marilyn.independent_encounter_status == 2:
            marilyn.c "You outdid yourself, sending me that little redhead.  Drop by to see me and I'll provide a suitable reward."
    return

## Loving Wife Content
label terri_sarah_positive_role_talk_adult_baby:
    if current_target.has_tag('adult_baby') and not sarah.has_tag(tag_expression):
        "There's too high a chance Sarah gets derailed by the nature of this fetish to listen to the messenger."
        sys "Either that, or Wife Trainer hasn't figured out how to write this scene yet."
        jump sarah_introduce_menu
    else:
        $ current_target = None
    return

label terri_sarah_positive_role_talk_slavegirl:
    if current_target.has_tag('slavegirl') and not sarah.has_tag(tag_expression):
        wt_image indy_lw_visit_1_7
        "You order [terri.full_name] to join you."
        wt_image indy_lw_visit_1_8
        player.c "Take a seat, [terri.name].  I'd like you to meet [sarah.name]."
        wt_image lw_visit_2_2
        sarah.c "Hi.  Shouldn't you be dressed?"
        wt_image indy_lw_visit_1_8
        player.c "She doesn't need clothes to talk.  [terri.name], Sarah's husband wants her to have sex with his friends. She has concerns. I thought speaking to another woman could help her."
        wt_image indy_lw_visit_1_1
        terri.c "I'll try, [terri.your_respect_name]."
        add tags 'met_slavegirl_terri' 'positive_transformed_slavegirl_resolution_today' to sarah
        ## remainder of transformed_slavegirl content is back in sarah's script
    else:
        $ current_target = None
    return

label terri_sarah_positive_role_sex_slavegirl:
    if current_target.has_tag('slavegirl'):
        wt_image indy_lw_visit_1_7
        player.c "[terri.name], come here and join us.  You remember Sarah?"
        wt_image indy_lw_visit_1_1
        terri.c "Yes, [terri.your_respect_name]."
        wt_image indy_lw_visit_1_8
        player.c "You know Sarah's worried about having her husband watch her have sex.  It's hard for her to imagine what that will be like, in part because she's never even seen two people have sex together.  I'm going to fuck you, while Sarah watches us."
        wt_image lw_visit_4_2
        sarah.c "You can't be serious?"
        wt_image lw_visit_4_3
        player.c "I am.  You've never watched two people have sex.  Now you will.  It'll give you a chance to see that sex doesn't have to be private to be fun.  Have a seat and make yourself comfortable."
        wt_image indy_lw_visit_1_9
        player.c "Let's get you prepared, [terri.name].  Turn around."
        wt_image indy_bondage_11
        "You bind [terri.name] into a kneeling position while [sarah.name] watches with a mixture of curiosity and horror."
        wt_image indy_lw_visit_1_10
        player.c "Open your mouth and get me hard."
        wt_image indy_bondage_3
        "She takes you into her mouth and sucks you erect."
        wt_image lw_visit_4_4
        sarah.c "Maybe I should go?  I don't want intrude on your personal time together."
        wt_image indy_lw_visit_1_11
        player.c "Nonsense.  [terri.name] doesn't mind you being here.  She's happy to service me anytime, regardless of whether anyone's watching.  Aren't you?"
        wt_image indy_lw_visit_1_2
        "She tries to answer you and address Sarah as best she can with your dick in her mouth."
        terri.c "Of courthh, Thirr.  Thirr wantth you to watch, Tharah, tho I don't mind.  I'm happy with whatever Thirr wantth."
        wt_image indy_bondage_2
        player.c "What I want, [terri.name], is for you to be ready for my cock.  Open yourself up for me."
        wt_image indy_bondage_11
        "She lowers her head and raises her ass."
        wt_image indy_lw_visit_1_4
        player.c "Open your asshole, too.  I want to look at it while I fuck you."
        wt_image indy_lw_visit_1_3
        "[terri.name] spreads her butthole for your inspection as you approach her. You think you hear a soft moan from Sarah as you get ready to enter your slavegirl."
        sarah.c "ohh"
        wt_image indy_lw_visit_1_5
        "In this position, [terri.name] can't do much more than take the fucking you give her, but she takes it very well, offering a warm sheath for your dick and obediently keeping her asshole spread open for your inspection as you thrust in and out of her."
        wt_image indy_lw_visit_1_6
        player.c "[player.orgasm_text]"
        terri.c "oooohhhhh"
        wt_image lw_visit_4_5
        sarah.c "You've made your point.  Men can enjoy sex even when it's not in private.  Some women, too, I guess."
        player.c "And did [terri.name] look ridiculous while I was fucking her?"
        wt_image lw_visit_4_8
        sarah.c "No.  No, I guess not.  I mean, the whole bondage thing is kinda weird."
        player.c "You should try it sometime."
        wt_image lw_visit_4_7
        sarah.c "I think I'll just go home and maybe think about this some more, later."
        player.c "Sure.  And if your husband wants to borrow some of my equipment to use on you while you're thinking about it, just let me know."
        $ terri.sex_count += 1
        orgasm
        add tags 'watched_transformed_slavegirl_this_weekend' to sarah
    else:
        $ current_target = None
    return

# End Week
label terri_end_week:
    ## Independent Assistant Events
    if terri.has_tag('assistant') or terri.has_tag('assistant_trouble'):
        if terri.assistant_training_count == 9 and not terri.has_tag('assistant_trouble'):
            summon terri no_follows
            wt_image indy_assistant_1
            terri.c "Hey, can we chat for a moment?"
            wt_image indy_assistant_24
            terri.c "I want to thank you for all the training you've provided to me.  You've really been great!  I've learned so much. I'm sure there are more things that you could teach me, but I'm ready to start learning on my own now."
            wt_image indy_assistant_27
            terri.c "I have some ideas I want to try out, so I've quit my job, and I'm moving to my own place.  I'm sorry I can't be your assistant any more, but I really do appreciate everything you've done for me."
            wt_image indy_assistant_23
            sys "This is the last time you'll see [terri.name] in this version of the game.  A future update will continue this story."
            call terri_lose_assistant from _call_terri_lose_assistant
            dismiss terri
            wt_image current_location.image
        else:
            if terri.has_tag('assistant_trouble'):
                rem tags 'assistant_trouble' from terri
                wt_image indy_mirror_1_1
                "You still haven't seen [terri.name], and there's a foul smell coming from her room. You go inside and see [terri.name] sitting in front of the mirror, just staring at it."
                wt_image indy_mirror_1_2
                "You touch her shoulder and she slumps forward against the mirror.  Was she trying self-hypnosis in front of the mirror?  It looks like she's placed herself into her own hypnotic trance."
                call terri_assistant_death from _call_terri_assistant_death_1
            else:
                if terri.assistant_must_train_by_week == week:
                    "You haven't heard any activity from [terri.name]'s room all weekend. You should check to make sure she's all right."
                    add tags 'assistant_trouble' to terri
                else:
                    $ terri.temporary_count = week + 3
                    if terri.assistant_must_train_by_week < terri.temporary_count:
                        wt_image indy_assistant_1
                        terri.c "Hi.  I hope you'll be able to help with my hypnosis training this week?  I've learned as much as I can, I think, from reading books."
                    $ terri.temporary_count = 0
    ## Hypno Girlfriend Maintenance
    if terri.has_tag('assistant') and player.hypno_girlfriend_count > 0 and not terri.has_tag('assistant_asked_about_hypno_girlfriend'):
        add tags 'assistant_asked_about_hypno_girlfriend' to terri
        call random_person_with_tags(tagged_with_any = ['hypno_girlfriend']) from _call_random_person_with_tags
        summon terri no_follows
        wt_image indy_assistant_22
        "[terri.name] comes to see you, a look of concern on her face."
        wt_image indy_assistant_10
        terri.c "Can I ask you a question?  I hope it's not impertinent.  It's about [current_target.name].  Have you done something to her?"
        "[terri.name]'s learning quite a bit about hypnosis.  There's no point in lying to her.  She'll soon figure it out."
        player.c "You mean have I hypnotized her?  Yes, I have."
        wt_image indy_assistant_22
        terri.c "Does she know?"
        player.c "No, she doesn't.  Does that concern you?"
        wt_image indy_assistant_1
        terri.c "A little."
        player.c "What's the first thing you learned about the limitations of hypnosis?"
        wt_image indy_assistant_10
        terri.c "You can't make someone do something unless part of them wants to do it?"
        player.c "Correct.  And does she seem happy to you?"
        wt_image indy_assistant_1
        terri.c "Yes, I think she does."
        player.c "Isn't that the point of hypnosis?  Isn't that what you want to do, help people to be happier with themselves?"
        wt_image indy_assistant_23
        terri.c "Yes, you're right.  I'm sorry I brought it up.  I'm sure you know what's best."
        wt_image current_location.image
    ## Love Potion Weekly Actions
    if terri.has_tag('love_potion_used') and terri.visit_count == 0 and terri.status == "on_training":
        wt_image phone_1
        "Your phone is ringing."
        wt_image indy_phone_1
        terri.c "Oh, hi.  It's me, [terri.name]."
        wt_image indy_phone_2
        terri.c "I'm sorry for disturbing you.  You didn't have me over for training this week.  I know, you were probably busy.  I understand."
        wt_image indy_phone_1
        terri.c "Maybe, if you don't have time to train me again next week, we could still get together for a cup of coffee or something?  Just to catch up.  I feel like we have such a connection, I miss it when I don't get to spend time with you."
        wt_image current_location.image
    ## Relationship Maintenance
    if terri.has_tag('adult_baby') and week >= terri.maintain_week_baby:
        if week == terri.maintain_week_baby:
            wt_image phone_1
            "[terri.name] spends the weekends at her house, and you rarely see or hear from her on Saturday or Sunday, so you're surprised to see a phone message from her."
            wt_image indy_phone_1
            terri.c "{i}Hi, it's me. I just wanted to ask if you were getting tired of our little game?{/i}"
            wt_image indy_phone_2
            terri.c "{i}It's okay if you are.  I'll understand.  I'm just starting to feel a little foolish hanging around in my crib, being ignored.{/i}"
            wt_image indy_phone_1
            terri.c "{i}I hope you still want to play with me and find some time to do so soon, because I miss my [terri.your_daddy_name].{/i}"
            wt_image current_location.image
        $ terri.temporary_count = terri.maintain_week_baby + 2
        if week >= terri.temporary_count:
            wt_image phone_1
            "There's a new message on your phone from [terri.name]."
            wt_image indy_phone_1
            terri.c "{i}Hi. It's me again.  I think you've grown tired of our little game, and that's okay.  I know you're busy and don't have a lot of time to spend with me.{/i}"
            if terri.has_tag('love_potion_used'):
                wt_image indy_phone_2
                terri.c "{i}Part of me thinks I should move on and find a new [terri.your_daddy_name] who has more time to spend on his baby girl, but I know in heart that you're the only daddy for me, and I can't bear the thought of not seeing you again.{/i}"
                wt_image indy_phone_1
                terri.c "{i}Your baby girl misses you, [terri.your_daddy_name].  I hope you spend time with me soon!{/i}"
            else:
                terri.c "{i}Thank you so much for helping me understand this side of me. I will always think fondly of you, and in my heart, you will always be my [terri.your_daddy_name]. But I think I should move on, and try and find a new Daddy who has more time to spend on his baby girl.{/i}"
                wt_image indy_phone_2
                terri.c "{i}Good bye, [terri.your_daddy_name].  I'll miss you always.{/i}"
                call convert(terri, 'unavailable') from _call_convert_107
            wt_image current_location.image
    call character_location_return(terri) from _call_character_location_return_727
    $ terri.visit_count_total += terri.visit_count
    $ terri.visit_count = 0
    return

## Character Specific Timers
# Description Display
label terri_description_display:
    call terri_update_media from _call_terri_update_media_1
    wt_image terri.image
    if terri.status == "post_training":
        # main description
        if terri.has_tag('new_man'):
            "Terry the New Guy.  You made him what he is today."
        elif terri.has_tag('futanari'):
            "[terri.name] the Good Girlfriend is now [terri.full_name].  You've done everything you can for her, physically, to get her ready to pursue her desires, but she's still uncomfortable pursuing women.  On the plus side, she now enjoys playing with cock more than she ever did, as long as it's her cock."
        elif terri.has_tag('doll'):
            "Terri the Good Girlfriend is now [terri.full_name].  She was never happy with her own desires, and hoped to suppress them by learning how to please her man.  You made that happen for her, but not the way she expected."
        elif terri.has_tag('adult_baby'):
            "[terri.name] the Good Girlfriend is now [terri.full_name].  She kept her job and her existing social life - although you're pretty sure her boyfriend is no longer in the picture - and doesn't seem to want to get involved in yours.  When she finishes work, she changes out of her normal clothes and into a diaper, and sits in her crib."
        elif terri.has_tag('slavegirl'):
            if terri.has_tag('slavegirl_let_out'):
                "[terri.full_name]'s old insecurities creep back in when she's let out of her cage. She never seems quite certain what to do with herself, and usually spends her time kneeling somewhere near you until you lock her back up in her cage for the night."
            else:
                "Terri the Good Girlfriend has become [terri.full_name]. She spends her days in the metal cage you built for her. With no freedom of movement and complete dependence on you for food, water, and toilet privileges, she can do nothing but spend her time thinking about how to please you. She no longer has time for self loathing or to worry about her own sexuality. She seems happier this way."
        elif terri.has_tag('assistant'):
            "[terri.name] the Good Girlfriend is now [terri.full_name].  She's keenly interested in all things hypnosis, although she won't ever let you hypnotize her."
        elif terri.has_tag('satisfied') and terri.has_tag('continuing_actions'):
            if terri.has_tag('boob_job'):
                "[terri.name] the Good Girlfriend now has confidence in her ability to please her boyfriend.  She tells anyone who asks that you're the reason she's such a good girlfriend.  She doesn't mention you're also the reason she has a new pair of knockers."
            else:
                "[terri.name] the Good Girlfriend now has confidence in her ability to please her boyfriend.  She tells anyone who asks that you're the reason she's such a good girlfriend."
        elif terri.has_tag('continuing_actions'):
            if terri.has_tag('boob_job'):
                "[terri.name] the Good Girlfriend still worries about whether she's able to properly please her boyfriend.  With her new set of knockers, she really shouldn't worry so much."
            else:
                "[terri.name] the Good Girlfriend still worries about whether she's able to properly please her boyfriend."
        # relationship status
        if terri.has_tag('adult_baby'):
            $ terri.temporary_count = terri.maintain_week_baby - week
            if terri.temporary_count > 2:
                "[terri.full_name] is happy with your relationship."
            elif terri.temporary_count > 0:
                "[terri.full_name] wishes you would spend more time with her."
            elif terri.has_tag('love_potion_used'):
                "[terri.full_name] feels like she never gets to spend time with you, but the lingering effects of the love potion make it impossible for her to contemplate leaving and not seeing you again."
            elif terri.temporary_count > -2:
                "[terri.full_name] is unhappy with your lack of attention and is considering leaving you."
            else:
                "[terri.full_name] feels ignored and plans to leave you unless you do something with her soon."
        elif terri.has_tag('assistant'):
            if terri.assistant_must_train_by_week < week + 3:
                "She's hoping you will train her again soon."
            else:
                "She's happy with your training and is busy studying what you've taught her so far."
        elif terri.has_tag('continuing_actions'):
            if terri.visit_sex_count > 0:
                "[terri.name] sees you as a friend ... and a mentor who she's willing to pay to give her remedial sex lessons."
            elif terri.has_tag('love_potion_used'):
                "Thanks to the effect of the love potion, [terri.name] sees you as her very best friend ... but just a friend."
            else:
                "[terri.name] sees you as a friend, and nothing more."
    elif terri.status == "on_training":
        "[terri.name] came to you on her own initiative and asked you to train her to be a better girlfriend for her boyfriend."
        "You have until the end of week [terri.training_limit] to complete this engagement."
    if not terri.has_any_tag('bimbo', 'degraded', 'doll', 'petgirl', 'transformed_slavegirl', 'whore'):
        if terri.has_tag('trigger_implanted'): # note this should not be possible, included here only for consistency
            "You have implanted a hypnotic trigger in her."
        if terri.has_tag('love_potion_used'):
            "She is under the influence of a love potion."
        "[terri.statblock]"
        $ items = ", ".join(i.name for i in terri.get_items()) if terri.get_items() != [] else ' Nothing'
        "You have given her: [items]"
    return

# State Check
label terri_state_check:
    if terri.youth_interest > 5:
        $ terri.state = 5
    elif terri.youth_interest > 1 and terri.youth_interest < 6:
        $ terri.state = terri.youth_interest
    else:
        $ terri.state = 1
    return

# Transformation Discussion
label terri_transformation_discussion:
    if terri.has_tag('cheerleader_visit_now') and terri.has_tag('boob_job'):
        if terri.has_tag('strips_on_visit'):
            wt_image indy_cheerleader_2_5
        else:
            wt_image indy_cheerleader_2_1
    elif terri.has_tag('cheerleader_visit_now'):
        wt_image indy_cheerleader_1_16
    elif terri.has_tag('adult_baby'):
        wt_image indy_crib_5
    elif terri.has_tag('boob_job'):
        wt_image indy_drink_2_1
    else:
        wt_image indy_drink_1_3
    player.c "I may have a solution to your problem, [terri.name]."
    if terri.has_tag('cheerleader_visit_now') and terri.has_tag('boob_job'):
        if terri.has_tag('strips_on_visit'):
            wt_image indy_cheerleader_2_5
        else:
            wt_image indy_cheerleader_2_4
    elif terri.has_tag('cheerleader_visit_now'):
        wt_image indy_cheerleader_1_18
    elif terri.has_tag('adult_baby'):
        wt_image indy_crib_7
    elif terri.has_tag('boob_job'):
        wt_image indy_drink_2_2
    else:
        wt_image indy_drink_1_19
    terri.c "What problem?"
    player.c "Your lust for women."
    if terri.has_tag('adult_baby'):
        wt_image indy_crib_9
        terri.c "I ... I don't think about that very much anymore.  I'm happy, with you.  Like this.  I don't want anything to change."
        $ terri.discussed_transformation = 2
    elif cassandra.independent_encounter_status > 1:
        terri.c "Mistress is helping me with that. She punishes me every time I feel bad about my feelings. I think it's helping. I don't want to do anything that could mess up what I have now with Mistress."
        $ terri.discussed_transformation = 2
    elif terri.has_tag('likes_girls'):
        if marilyn.independent_encounter_status > 1:
            terri.c "I don't see that as a problem anymore. You and Mommy have helped me to come to terms with who I am. I don't want to change. Maybe at one point I did, but not now."
        else:
            terri.c "I don't see that as a problem anymore. I've come to terms with who I am. I don't want to change. Maybe at one point I did, but not now."
        $ terri.discussed_transformation = 2
    else:
        if terri.has_tag('cheerleader_visit_now') and terri.has_tag('boob_job'):
            if terri.has_tag('strips_on_visit'):
                wt_image indy_cheerleader_2_5
            else:
                wt_image indy_cheerleader_2_4
        elif terri.has_tag('cheerleader_visit_now'):
            wt_image indy_cheerleader_1_17
        elif terri.has_tag('boob_job'):
            wt_image indy_drink_2_4
        else:
            wt_image indy_drink_1_3
        terri.c "Are you telling me you have a way to help me stop fantasizing about women?"
        player.c "I may have a way to make sure that you no longer feel guilty about those thoughts."
        if terri.has_tag('cheerleader_visit_now') and terri.has_tag('boob_job'):
            if terri.has_tag('strips_on_visit'):
                wt_image indy_cheerleader_2_5
            else:
                wt_image indy_cheerleader_2_4
        elif terri.has_tag('cheerleader_visit_now'):
            wt_image indy_cheerleader_1_17
        elif terri.has_tag('boob_job'):
            wt_image indy_drink_2_5
        else:
            wt_image indy_drink_1_7
        "She thinks for a few minutes."
        if terri.has_tag('cheerleader_visit_now') and terri.has_tag('boob_job'):
            if terri.has_tag('strips_on_visit'):
                wt_image indy_cheerleader_2_1
            else:
                wt_image indy_cheerleader_2_1
        elif terri.has_tag('cheerleader_visit_now'):
            wt_image indy_cheerleader_1_18
        elif terri.has_tag('boob_job'):
            wt_image indy_drink_2_3
        else:
            wt_image indy_drink_1_19
        terri.c "Okay. That could be worth trying."
        $ terri.discussed_transformation = 1
    return

# Transformation Potion Timer
label terri_transformation_potion_timer:
    $ terri.temporary_count = 1
    if terri.has_tag('adult_baby'):
        wt_image indy_crib_8
        player.c "I made your bottle from a special formulation today, baby girl."
        wt_image indy_crib_3
        "[terri.name] takes a sip, then a second ..."
        wt_image indy_crib_6
        "... then she spaces out as the potion takes effect.  You now need to spend some energy helping the potion realize a new potential for her."
    else:
        if terri.has_tag('boob_job'):
            wt_image indy_drink_2_1
        else:
            wt_image indy_drink_1_2
        player.c "I poured you another drink."
        if terri.has_tag('love_potion_used'):
            terri.c "Another?  Well ... okay.  I do love your drinks!"
        else:
            terri.c "Another?  Well ... okay.  I guess I have time."
        if terri.has_tag('boob_job'):
            wt_image indy_drink_2_6
        else:
            wt_image indy_drink_1_4
        "[terri.name] takes a sip, then a second ..."
        if terri.has_tag('boob_job'):
            wt_image indy_drink_2_7
        else:
            wt_image indy_drink_1_5
        "... then she spaces out as the potion takes effect.  You now need to spend some energy helping the potion realize a new potential for her."
    $ title = "Transform her into?"
    menu:
        "Man (warning: no content yet)" if terri.lesbian_clues > 2:
            "Growing up, [terri.name] often thought it was unfair that boys were allowed to kiss girls, when she wasn't.  Sometimes she even thought it was unfair that she wasn't a boy."
            "She hasn't had those thoughts in a long while, but the potion hunts them out, and magnifies them.  It IS unfair that she isn't a boy.  She SHOULD have been a boy.  It was what she was meant to be.  It would explain her feelings towards girls.  It would make those feelings okay."
            if terri.has_tag('adult_baby'):
                wt_image indy_crib_9
            elif terri.has_tag('boob_job'):
                wt_image indy_drink_2_3
            else:
                wt_image indy_drink_1_7
            "[terri.name] becomes dizzy under the influence of the potion."
            terri.c "I ... I'm not feeling well.  I need to go home."
            wt_image phone_1
            "The next morning, your phone rings."
            wt_image indy_new_man_1
            "It's [terri.name].  Or perhaps you should say Terry, the New Guy."
            if terri.discussed_transformation == 0:
                terri.c "I don't understand!  Something happened to me yesterday.  Sorry, I sound crazy but ... LOOK AT ME!"
                terri.c "I didn't know who else to call.  I don't know what to say.  I don't know what to do."
                if terri.has_tag('adult_baby'):
                    terri.c "I don't think I can be your baby anymore.  I need time to figure out my life."
                    "It's a big change, but she ... no, he ... will be happier in time, you're certain."
                elif cassandra.independent_encounter_status > 1:
                    terri.c "Mistress is going to be so disappointed!  This is going to break her heart!"
                    terri.c "I don't know how I will tell her.  What will I even say to her??  I'm sorry Mistress, but I woke up with a penis???"
                    "She ... no, he ... breaks into tears as he hangs up. Perhaps in time he'll be happier like this. Perhaps not."
                elif terri.has_tag('likes_girls'):
                    terri.c "I was finally happy as a woman!  After all these years, I finally accept that I'm a lesbian.  Now suddenly ... I have a PENIS????"
                    "She ... no, he ... breaks into tears as he hangs up. Perhaps in time he'll be happier like this. Perhaps not."
                else:
                    terri.c "I don't know how I can explain this to my boyfriend.  I can't even explain it to myself.  What will I even say to him??  I'm sorry honey, but I woke up with a penis???"
                    terri.c "Maybe I can just send him a note.  I need time to myself to figure out my life."
                    "It's a big change, but she ... no, he ... will be happier in time, you're certain."
            elif terri.discussed_transformation == 1:
                terri.c "WHAT HAVE YOU DONE?"
                terri.c "I don't understand how ... but you CHANGED ME somehow ... LOOK AT ME!!"
                if terri.has_tag('adult_baby'):
                    terri.c "I don't think I can be your baby anymore. I need time to figure out my life."
                    "It's a big change, but she ... no, he ... will be happier in time, you're certain."
                elif cassandra.independent_encounter_status > 1:
                    terri.c "Mistress is going to be so disappointed! This is going to break her heart!"
                    terri.c "I don't know how I will tell her. What will I even say to her??  I'm sorry Mistress, but I woke up with a penis???"
                    "She ... no, he ... breaks into tears as he hangs up. Perhaps in time he'll be happier like this. Perhaps not."
                elif terri.has_tag('likes_girls'):
                    terri.c "I was finally happy as a woman!  After all these years, I finally accept that I'm a lesbian. Now suddenly ... I have a PENIS????"
                    "She ... no, he ... breaks into tears as he hangs up. Perhaps in time he'll be happier like this. Perhaps not."
                else:
                    terri.c "How can I explain this to my boyfriend?  What will I even say to him?? I'm sorry honey, but I woke up with a penis???"
                    player.c "Take a deep breath. It's going to be okay. Your boyfriend will be okay. More importantly, you and your girlfriend are going to be okay."
                    terri.c "Girlfriend?  What girlfriend?"
                    player.c "The one you can go out and find now.  With a clear conscience, and no self doubt or guilt.  You're a man now.  Act like one.  Go, chase girls.  Kiss and fuck as many women as you like.  Or find a nice girl and settle down.  It's what you've wanted to do your whole life."
                    terri.c "Yes, but my old life ... I'll need to find a new job. I need to let my boyfriend down softly. I so need to go shopping for new clothes!"
                    "It's a big change, but she ... no, he ... will be happier in time, you're certain."
            elif terri.discussed_transformation == 2:
                terri.c "YOU DID THIS TO ME!"
                terri.c "I don't understand how ... I certainly don't understand why. But even after I asked you not to, you ... you CHANGED ME somehow ... LOOK AT ME!"
                if terri.has_tag('adult_baby'):
                    terri.c "I was happy being your baby!"
                    player.c "A sexless life.  Or at least a life with no enjoyable sex life for you."
                    terri.c "That was my decision to make!!!"
                    player.c "You couldn't accept your sexuality.  Now you can.  Go, chase girls.  Kiss and fuck as many women as you like.  Or find a nice girl and settle down.  It's what you've wanted to do your whole life."
                    terri.c "You had no right!"
                    "It's a big change, but she ... no, he ... will be happier in time, you're certain."
                elif cassandra.independent_encounter_status > 1:
                    terri.c "Mistress is going to be so disappointed!  This is going to break her heart!"
                    terri.c "I don't know how I will tell her.  What will I even say to her??  I'm sorry Mistress, but I woke up with a penis???"
                    terri.c "AND IT'S ALL YOUR FAULT!"
                    "She ... no, he ... breaks into tears as he hangs up. Perhaps in time he will be happier like this. Perhaps not."
                elif terri.has_tag('likes_girls'):
                    terri.c "I was finally happy as a woman!  After all these years, I finally accept that I'm a lesbian.  Now suddenly ... I have a PENIS????"
                    terri.c "Why would you do this???  Help me to accept who I am, then turn around and change me??"
                    terri.c "YOU HAD NO RIGHT!"
                    "She ... no, he ... breaks into tears as he hangs up.  Perhaps in time he will be happier like this.  Perhaps not."
            $ terri.transformed_via_object = True
            call terri_convert_man from _call_terri_convert_man
        "Sort of a man (limited Futanari content)" if terri.lesbian_clues > 2:
            "Growing up, [terri.name] often thought it was unfair that boys were allowed to kiss girls, when she wasn't.  Sometimes she even thought it was unfair that she wasn't a boy."
            "She hasn't had those thoughts in a long while, but the potion hunts them out, and magnifies them.  It IS unfair that she isn't a boy.  She SHOULD have been a boy.  It was what she was meant to be.  It would explain her feelings towards girls.  It would make those feelings okay."
            if terri.has_tag('adult_baby'):
                wt_image indy_crib_9
            elif terri.has_tag('boob_job'):
                wt_image indy_drink_2_3
            else:
                wt_image indy_drink_1_7
            "[terri.name] becomes dizzy under the influence of the potion."
            terri.c "I ... I'm not feeling well.  I need to go home."
            wt_image phone_1
            "The next morning, your phone rings."
            wt_image indy_futanari_1_1
            if terri.discussed_transformation == 0:
                terri.c "I don't understand!  Something happened to me yesterday.  Sorry, I sound crazy but ..."
                wt_image indy_futanari_1_2
                terri.c "I HAVE A COCK!!  I didn't know who else to call.  I don't know what to say.  I don't know what to do.  I don't understand how this could happen??"
                wt_image indy_futanari_1_3
                if terri.has_tag('adult_baby'):
                    terri.c "I don't think I can be your baby anymore.  I need time to figure out my life."
                elif cassandra.independent_encounter_status > 1:
                    terri.c "Mistress is going to be so disappointed!  This is going to break her heart!  I don't know how I will tell her.  What will I even say to her??  I'm sorry Mistress, but I woke up with a penis???"
                elif terri.has_tag('likes_girls'):
                    wt_image indy_futanari_1_3
                    terri.c "I was finally happy as a woman!  After all these years, I finally accept that I'm a lesbian.  Now suddenly ... I have a PENIS????"
                else:
                    terri.c "I don't know how I can explain this to my boyfriend.  I can't even explain it to myself.  What will I even say to him??  I'm sorry honey, but I woke up with a penis???"
            elif terri.discussed_transformation == 1:
                terri.c "WHAT HAVE YOU DONE?"
                player.c "What do you mean?"
                wt_image indy_futanari_1_2
                terri.c "I don't understand how ... but you CHANGED ME somehow ... I HAVE A COCK!!"
                wt_image indy_futanari_1_3
                if terri.has_tag('adult_baby'):
                    terri.c "I don't think I can be your baby anymore. I need time to figure out my life."
                elif cassandra.independent_encounter_status > 1:
                    terri.c "Mistress is going to be so disappointed! This is going to break her heart!  I don't know how I will tell her.  What will I even say to her??  I'm sorry Mistress, but I woke up with a penis???"
                elif terri.has_tag('likes_girls'):
                    terri.c "I was finally happy as a woman!  After all these years, I finally accept that I'm a lesbian.  Now suddenly ... I have a PENIS????"
                else:
                    terri.c "How can I explain this to my boyfriend?  What will I even say to him??  I'm sorry honey, but I woke up with a penis???"
            elif terri.discussed_transformation == 2:
                terri.c "YOU DID THIS TO ME!"
                player.c "What do you mean?"
                wt_image indy_futanari_1_2
                terri.c "I don't understand how ... I certainly don't understand why.  But even after I asked you not to, you ... you CHANGED ME somehow ... I HAVE A COCK!!"
                wt_image indy_futanari_1_3
                if terri.has_tag('adult_baby'):
                    terri.c "I was happy being your baby!"
                    player.c "A sexless life.  Or at least a life with no enjoyable sex life for you."
                    wt_image indy_futanari_1_2
                    terri.c "That was my decision to make!!!  You had no right!"
                elif cassandra.independent_encounter_status > 1:
                    terri.c "Mistress is going to be so disappointed!  This is going to break her heart!  I don't know how I will tell her.  What will I even say to her??  I'm sorry Mistress, but I woke up with a penis???  AND IT'S ALL YOUR FAULT!"
                elif terri.has_tag('likes_girls'):
                    terri.c "I was finally happy as a woman!  After all these years, I finally accept that I'm a lesbian.  Now suddenly ... I have a PENIS????  Why would you do this???  Help me to accept who I am, then turn around and change me??  YOU HAD NO RIGHT!"
            wt_image indy_futanari_1_4
            terri.c "And to make things worse, I'm so fucking horny I can't even think straight.  How do you guys get anything done with this hanging between your legs?  I haven't been able to stop touching it since I woke up this morning."
            wt_image indy_futanari_1_5
            $ title = "What do you do?"
            menu:
                "Encourage her to masturbate":
                    wt_image indy_futanari_1_4
                    player.c "You know you can make your new cock feel even better, right?  The horniness isn't going to go away until you do."
                    wt_image indy_futanari_1_3
                    terri.c "I have to give myself a handjob?"
                    player.c "If you want relief.  Unless you want to ask someone else to do it for you?"
                    wt_image indy_futanari_1_2
                    terri.c "NO!  I don't want anyone else to see me like this."
                    wt_image indy_futanari_1_7
                    if terri.handjob_count > 0:
                        terri.c "I guess it wouldn't hurt if I stroked it a little faster.  It's no different than when I jerked you off, right?  Oh gawd, I had no idea my hand felt so good sliding up-and-down your cock!"
                    else:
                        terri.c "I guess it wouldn't hurt if I stroked it a little faster.  It's no different than jacking off my boyfriend, right?  Oh gawd, I had no idea my hand felt so good sliding up-and-down his cock!"
                    wt_image indy_futanari_1_8
                    terri.c "Oohhhh ... what's that sensation in my balls?  They feel tight and heavy.  I think my panties are too tight.  I need to sit down, I feel light-headed ..."
                    wt_image indy_futanari_1_9
                    terri.c "Ooohhhhh ... I need to stroke it faster!  Faster!!"
                    wt_image indy_futanari_1_10
                    terri.c "Oooohhhhhh!!!!"
                    wt_image indy_futanari_1_11
                    terri.c "I'm making a mess!  Where are the tissues??"
                    wt_image indy_futanari_1_12
                    terri.c "Oohhhh ... why does the tissue feel so good against my cock??"
                    wt_image indy_futanari_1_13
                    terri.c "Oooohhhhhh!!!!  I'm still cumming!!!"
                    wt_image indy_futanari_1_14
                    terri.c "I need more tissue!!"
                    wt_image indy_futanari_1_15
                    terri.c "Oooohhhhhh!!!!  Why am I still cumming???"
                    wt_image indy_futanari_1_16
                    terri.c "Oh gawd, my cock's still hard and my balls still ache."
                    wt_image indy_futanari_1_17
                    terri.c "Need to keep stroking ... keep stroking ..."
                    wt_image indy_futanari_1_18
                    terri.c "Oooohhhhhh!!!!"
                    wt_image indy_futanari_1_19
                    terri.c "Oohhh ... I think I'm finally finished.  I think my balls are finally empty."
                    wt_image indy_futanari_1_20
                    terri.c "I always figured sex must be something like that for you guys.  It would explain why so many of you are so horny all the time."
                    wt_image indy_futanari_1_21
                    "There's absolutely nothing normal about the number of orgasms [terri.name] just had or the amount of sperm her balls produced, but if this is her image of what sex was like for guys, it must have been what the potion fixated on when it transformed her sex organs."
                    if terri.has_tag('boob_job'):
                        "It seems that large breasts were also inconsistent with her vision of what a body with a cock should look like, as the potion also reduced her chest size when it transformed her."
                    wt_image indy_futanari_1_22
                "End the call":
                    wt_image indy_futanari_1_6
            if terri.discussed_transformation == 0:
                terri.c "Please stay in touch.  I don't know how this happened, but you're the only one I feel comfortable talking to about it."
            elif terri.discussed_transformation == 1:
                terri.c "Please stay in touch.  I don't know how or why you did this to me, but please don't abandon me now that you have."
            elif terri.discussed_transformation == 2:
                terri.c "Please stay in touch.  I'm pissed at you for doing this to me, but please don't abandon me now that you have."
            $ terri.transformed_via_object = True
            call terri_convert_futanari from _call_terri_convert_futanari
        "Slavegirl" if terri.submission > 40 or cassandra.independent_encounter_status > 1:
            if terri.has_tag('adult_baby'):
                wt_image indy_crib_9
            elif terri.has_tag('boob_job'):
                wt_image indy_drink_2_5
            else:
                wt_image indy_drink_1_7
            if cassandra.independent_encounter_status > 1:
                "[terri.name] isn't naturally submissive, but she is a mass of conflicted thoughts and has long been torn by self-guilt."
                "The time spent submitting to first yours and now [cassandra.name]'s will has been a comforting time for [terri.name].  In those moments, she's been able to block out the thoughts in her head and focus just on the commands being given to her."
                "The potion latches on to her memories of those moments of peace, and amplifies them. Soon, she needs those moments. Craves those moments. Can think of nothing other than the peace and joy of submission."
            else:
                "[terri.name] isn't naturally submissive, but she is a mass of conflicted thoughts and has long been torn by self guilt."
                "The time spent submitting to your Will has been a comforting time for [terri.name].  In those moments, she's been able to block out the thoughts in her head and focus just on the commands being given to her."
                "The potion latches on to her memories of those moments of peace, and amplifies them.  Soon, she needs those moments. Craves those moments. Can think of nothing other than the peace and joy of submission."
            if terri.has_tag('adult_baby'):
                wt_image indy_diaper_37
                "As you help her out of the crib, she sinks to her knees, but she knows it's not because she's your baby, anymore."
                wt_image indy_diaper_4
            else:
                if terri.has_tag('boob_job'):
                    wt_image indy_doll_2_8
                else:
                    wt_image indy_drink_1_8
                "[terri.name] pulls off her clothes, as if she knows she shouldn't be wearing them.  Then she sinks to the floor, a confused look on her face."
            player.c "You're my slavegirl.  You belong to me."
            if cassandra.independent_encounter_status > 1:
                terri.c "No, [terri.your_respect_name].  I belong to Mistress."
                if terri.has_tag('adult_baby'):
                    wt_image indy_diaper_5
                elif terri.has_tag('boob_job'):
                    wt_image indy_drink_2_9
                else:
                    wt_image indy_drink_1_9
                "She tries to stand, then falls back to the floor, still woozy from the potion.  There's no point in fighting this. Her heart and soul belong to [cassandra.name]. It's likely the potion did nothing more than hasten along the transformation that was already taking place inside her."
                if terri.has_tag('adult_baby'):
                    wt_image indy_diaper_1
                elif terri.has_tag('boob_job'):
                    wt_image indy_drink_2_10
                else:
                    wt_image indy_drink_1_7
                "You help her to her feet and get her dressed.  Then you take her back to [cassandra.name].  If [cassandra.name] notices a change in [terri.name]'s behavior, she'll likely ascribe it to her own skill as a Domme and the depth of [terri.name]'s natural submissiveness.  There's no need to disabuse [cassandra.name] of that notion."
                dismiss terri
            else:
                terri.c "Yes, [terri.your_respect_name]."
                if terri.has_tag('adult_baby'):
                    wt_image indy_drink_1_9
                    "Still woozy from the potion, she pulls off her diapers as you replace her crib with a cage to keep her in."
                else:
                    if not terri.has_tag('boob_job'):
                        wt_image indy_drink_1_9
                    "You lead her, still woozy from the potion, into your bedroom.  She can rest and recover there while you make a cage to keep her in."
                call terri_convert_slavegirl from _call_terri_convert_slavegirl
            wt_image current_location.image
            $ terri.transformed_via_object = True
        "Doll" if terri.has_tag('boob_job'):
            "Deep down, [terri.name]'s been worried about this since she got the breast enlargement. The way people started to look at her, even women - maybe especially women - like all she was now was a set of big tits.  The potion latches on to those thoughts and confirms them for her.  That is all she is.  Tits, mouth, cunt, ass."
            if terri.has_tag('adult_baby'): # Note: shouldn't be possible to be adult_baby with boob_job, but including this to deal with mods or cheats
                wt_image indy_crib_9
                "With her last conscious thought, she glances at you, wondering whether this was your intention for her all along?"
                wt_image indy_drink_2_10
                "Then she stands and puts on big girl clothes - or big girl doll clothes at least ..."
                wt_image indy_doll_0_2
                "... and waits to be used."
            else:
                wt_image indy_drink_2_3
                "With her last conscious thought, she glances at you, wondering whether this was your solution for her all along?"
                wt_image indy_doll_0_2
                "Then she stands and waits to be used."
            wt_image indy_doll_0_1
            "She looks content, you think.  She was always disturbed by her own desires, anyway. Now she just doesn't have any.  You stash her down in the basement, out of sight.  She'll be there when you're ready to play with her."
            $ terri.transformed_via_object = True
            call terri_convert_doll from _call_terri_convert_doll
            wt_image current_location.image
        "Nothing (undo)":
            $ terri.temporary_count = 0
            "Let's just pretend that didn't happen.  That's easier than reloading an old save."
    if terri.temporary_count == 1:
        $ terri.temporary_count = 0
        $ terri.training_session()
        rem 1 transformation_potion from player
        change player energy by -energy_long notify
        if terri.status == "on_training":
            end_day
    return

# Convert Character to Adult Baby
label terri_convert_adult_baby:
    $ terri.training_regime = 'daily'
    call convert(terri,"adult_baby") from _call_convert_108
    add tags 'post_continuing_actions' to terri
    rem tags 'continuing_actions' 'follows' from terri
    $ terri.fixed_location = bedroom
    $ terri.location = bedroom
    $ terri.suffix = "the Adult Baby"
    $ terri.maintain_week_baby = week + 4
    add 1 lollipop_terri to coffee_shop
    return

# Convert Character to Assistant
label terri_convert_assistant:
    # get energy bonus if Terri is your only assistant ## changed
    #if player.assistant_count == 0:  ## changed to now get always, as limited to house; may need to adjust if another assistant is added
    $ energy_hypnosis.add_modifier(flat = -5, condition = "terri.has_tag('assistant') and current_location in locations_in_area('house')")
    call convert(terri,"assistant") from _call_convert_109
    $ terri.suffix = "the Assistant"
    $ terri.assistant_must_train_by_week = week + 5
    $ terri.fixed_location = terri_the_assistant_room
    $ terri.location = terri_the_assistant_room
    add tags 'post_continuing_actions' to terri
    rem tags 'continuing_actions' 'follows' from terri
    return

# Lose Terri as an Assistant
label terri_lose_assistant:
    # if player.assistant_count == 0:
    #     $ energy_hypnosis += 5 ## reverse gain
    # No need to remove this as the modifier requires terri to be an assistant
    # You could capture the modifier in a variable and remove it later if you want using remove_modifier
    call unconvert(terri,'assistant') from _call_unconvert_47
    return

# Deal with Terri the Assistant's Death
label terri_assistant_death:
    "She's gone. Dead from dehydration you guess. This doesn't look good. There's a dead woman in your house, seemingly killed by lack of access to water. You try to remember when you last had sexual contact with her, and whether the DNA evidence of that would still be accessible."
    $ title = "What do you do?"
    menu menu_terri_examine_2:
        "Call the police (ends game)":
            wt_image police_interview
            "The police treat you as suspect number one.  Hardly surprising.  A woman died of thirst in your house, and there's no evidence she's had contact with anybody but you for days."
            wt_image courtroom_1
            "It takes three years for your case to come to trial.  When it does, justice is finally served.  You didn't kill her, and the circumstantial evidence brought against you is rejected by the jury."
            "You're a free man again, but your reputation is ruined.  You'll need to start a new life somewhere else."
            sys "Reload or restart.  Next time, don't leave your assistants so long between training.  Who knows what trouble they could get up to when you're not supervising their learning?"
            ### END THE GAME ###
            jump end_game
        "Bury the evidence (ends game)":
            wt_image digging_1
            "You wait until dark.  Then you put her in a bag and drive as far away as you can.  When you think you're far enough out of the city, you find some woods and start to dig a hole."
            wt_image digging_2
            "'Please let it be only one person', you think as you see the headlights of a vehicle pull off the road close to you."
            "It isn't.  It's two people.  The landowner and his son.  They saw your vehicle drive in, and came to check to make sure you're okay. You can't hypnotize them, and you can't easily explain what you're doing."
            wt_image courtroom_1
            "The trial is over quickly.  There's no concrete evidence that you killed her, but the jury accepts the circumstantial evidence presented against you."
            sys "Bad end."
            ### END THE GAME ###
            jump end_game
        "Flee (ends game)":
            wt_image airport_1
            "You pack just the essentials you need and head for the airport.  You'll need to start a new life somewhere else.  You've done it before."
            sys "Reload or restart.  Next time, don't leave your assistants so long between training. Who knows what trouble they could get up to when you're not supervising their learning."
            ### END THE GAME ###
            jump end_game
        "Call [janice.name] the Lawyer" if player.has_tag('lawyer_on_retainer'):
            wt_image lawyer_desk_1
            player.c "[janice.name], I have a problem."
            janice.c "That's what I'm here for."
            "You explain the situation."
            janice.c "Consider the problem solved.  No charge.  Someone will be by to pick her up in a few minutes."
            player.c "What will happen to her?"
            janice.c "If I told you that, I'd have to charge you.  More than you can afford.  This won't come back to you, that's all you need to know."
            wt_image living_room.image
            "Two hours later, and there's no sign that [terri.name] had ever been in your house.  Perhaps you should have got her medical attention, or tried harder to save her yourself?"
            "On the other hand, what's the point of having a high priced lawyer on retainer if you aren't going to rely on her to keep you out of trouble."
            call terri_lose_assistant from _call_terri_lose_assistant_1
            call convert(terri,'unavailable') from _call_convert_110
            dismiss terri
            wt_image current_location.image
        "Call [marilyn.name]" if marilyn.favour > 0:
            wt_image marilyn_office_22
            player.c "[marilyn.name], I have a problem.  There's a dead woman in my house."
            marilyn.c "So?  What do you expect me to do about it?  Handling dead bodies isn't exactly a safe venture."
            $ title = "What now?"
            menu:
                "Call in your favor":
                    player.c "[marilyn.name], you owe me one.  You have people who can handle this.  I know you do."
                    "There's silence at the end of the line, then finally a sigh."
                    wt_image marilyn_office_24
                    marilyn.c "Fine.  I'll send somebody over."
                    wt_image marilyn_office_25
                    marilyn.c "Don't touch anything until they get there.  Don't do anything.  Don't contact anybody.  Try not even to breathe if you can help it."
                    wt_image marilyn_office_24
                    marilyn.c "And whatever you do, don't make eye contact with who shows up.  You don't want to be able to recognize them.  They wouldn't like that."
                    wt_image living_room.image
                    "Two hours later, and there's no sign that [terri.name] had ever been in your house.  It's much better being on [marilyn.name]'s good side than the alternative."
                    $ marilyn.favour -= 1
                    call terri_lose_assistant from _call_terri_lose_assistant_2
                    call convert(terri,'unavailable', True) from _call_convert_111
                    dismiss terri
                    wt_image current_location.image
                "Try something else":
                    $ title = "What do you do?"
                    wt_image indy_mirror_1_2
                    jump menu_terri_examine_2
    return

# Convert Character to Lesbian
label terri_convert_lesbian:
    # call convert(terri,"satisfied", True, True)
    call convert(terri,"lesbian", False, True) from _call_convert_112
    add tags 'continuing_actions' to terri
    return

# Convert Character to Man
label terri_convert_man:
    call convert(terri,'new_person', False, True) from _call_convert_113
    add tags 'new_man' to terri
    rem tags 'continuing_actions' 'post_continuing_actions' from terri
    sys "There's no additional content for Terry the New Guy yet. Some is planned for a future version of the game."
    dismiss terri
    wt_image current_location.image
    return

# Convert Character to Futanari
label terri_convert_futanari:
    if terri.has_tag('assistant'):
        call terri_lose_assistant from _call_terri_lose_assistant_5
    if terri.has_tag('adult_baby'):
        call unconvert(terri,'adult_baby') from _call_unconvert_50
    if terri.has_tag('slavegirl'):
        call unconvert(terri,'slavegirl') from _call_unconvert_85
    $ terri.training_regime = 'daily'
    call convert(terri,'futanari', False, True) from _call_convert_191
    add tags 'continuing_actions' 'futanari' to terri
    rem tags 'post_continuing_actions' 'follows' from terri
    $ terri.suffix = "the Futanari"
    $ terri.fixed_location = None
    dismiss terri
    wt_image current_location.image
    return

# Convert Character to Slavegirl
label terri_convert_slavegirl:
    if terri.has_tag('assistant'):
        call terri_lose_assistant from _call_terri_lose_assistant_3
    if terri.has_tag('adult_baby'):
        call unconvert(terri,'adult_baby') from _call_unconvert_48
    $ terri.training_regime = 'daily'
    call convert(terri,"slavegirl", False, True) from _call_convert_114
    add tags 'post_continuing_actions' to terri
    rem tags 'continuing_actions' 'follows' from terri
    $ terri.prefix = "Slave"
    $ terri.suffix = ""
    $ terri.fixed_location = bedroom
    $ terri.location = bedroom
    return

# Convert Character to Doll
label terri_convert_doll:
    if terri.has_tag('assistant'):
        call terri_lose_assistant from _call_terri_lose_assistant_4
    if terri.has_tag('adult_baby'):
        call unconvert(terri,'adult_baby') from _call_unconvert_49
    call convert(terri,'doll', False, True) from _call_convert_115
    $ terri.clear_training_session() # removes training tags so can play with the doll immediately
    $ terri.training_regime = 'daily' ## not really necessary, as no doll tags add trained tags
    $ terri.suffix = "the Doll"
    $ terri.change_image('indy_doll_0_1')
    add tags 'post_continuing_actions' to terri
    rem tags 'continuing_actions' 'follows' from terri
    $ terri.fixed_location = basement
    $ terri.location = basement
    return

########### ROOMS ###########
# Terri the Assistant's Room
label tar_examine:
    "[terri.name] decorated the room herself. Her shelves are filled with a clutter of hypnosis books and childish items."
    return

# Location actions
label tar_no_access:
    if terri.has_tag('sleep_visit_today'):
        "Let her sleep."
        break_movement
        #call forced_movement(living_room)  # not needed, as this is what break_movement does
    elif terri.location != terri_the_assistant_room:
        "[terri.name]'s not here now."
        break_movement
    return

label tar_enter:
    if terri.has_tag('assistant_trouble'):
        wt_image indy_mirror_1_1
        "Something's wrong.  [terri.name] is sitting in front of the mirror, just staring at it."
        player.c "[terri.name], are you okay?"
        "There's no response."
    elif terri.location == terri_the_assistant_room and not terri.can_be_interacted:
        add tags 'sleep_visit_today' to terri
        wt_image indy_sleeping_1_1
        "[terri.name]'s asleep, worn out from practicing the hypnosis techniques you've taught her. You'd never guess her age by the little girl underwear she wears to bed."
        $ terri.temporary_count = 1
        while terri.temporary_count == 1:
            $ title = "What do you do?"
            menu:
                "Deepen her slumber" if terri.sleep_depth > 0 and terri.sleep_depth < 5 and not terri.has_tag('sleep_hypno_today'):
                    #note: terri is already your assistant if you've getting this content, which is why no reason to test for hypnosis ability here
                    wt_image indy_sleeping_1_37
                    if terri.sleep_depth == 1:
                        "You can't exactly hypnotize someone who's already asleep, but you think you can help [terri.name] fall more deeply asleep.  Quietly you whisper in her ear."
                        player.c "I'm here to help you, [terri.name].  Follow my voice and I'll lead you to a deeper sleep.  You want to sleep deeply.  You don't want to be restless."
                        player.c "Listen to my voice and follow it to a deeper place, a safer place, [terri.name].  A place where you let go of your worries and sleep.  Sleep deeply, [terri.name]."
                    else:
                        player.c "Follow my voice, [terri.name]. Follow my voice as I lead you to a deeper sleep. A better sleep. A safer sleep. Sleep deeply, [terri.name]."
                    wt_image indy_sleeping_1_11
                    "Your efforts tire you out a bit, but help [terri.name] fall into a deeper slumber."
                    $ terri.sleep_depth += 1
                    add tags 'sleep_hypno_today' to terri
                    change player energy by -energy_very_short notify

                "Quietly watch her":
                    if terri.has_tag('sleep_panties_removed'):
                        wt_image indy_sleeping_1_8
                    elif terri.has_tag('sleep_bra_removed'):
                        wt_image indy_sleeping_1_6
                    elif terri.has_tag('sleep_hypno_today'):
                        wt_image indy_sleeping_1_37
                    else:
                        wt_image indy_sleeping_1_2
                    if terri.sleep_depth < 1:
                        "She tosses restlessly in the dark. It's an uneasy sleep, but you get a better sense of her sleep patterns as you watch her."
                        $ terri.sleep_depth = 1
                    elif terri.sleep_depth == 1:
                        "You've got a sense for [terri.name]'s sleep patterns now."
                    elif terri.sleep_depth == 2:
                        "She's sleeping more soundly now, but still tossing from time to time."
                    elif terri.sleep_depth == 3:
                        "She seems sound asleep."
                    elif terri.sleep_depth == 4:
                        "She's in a deep slumber."
                    else:
                        "She's so sound asleep, she seems dead to the world."

                "Touch her" if not terri.has_tag('sleep_touched'):
                    wt_image indy_sleeping_1_36
                    "You place your hand on [terri.name]'s thigh, running it along her soft skin."
                    if terri.sleep_depth < 1:
                        wt_image indy_sleeping_1_3
                        "She startles at your touch, and sits up, covering herself."
                        terri.c "What?  What is it??  Is something wrong?"
                        call terri_sleep_session_wake from _call_terri_sleep_session_wake
                    elif terri.sleep_depth == 1:
                        "She stirs at your touch, but doesn't wake."
                    else:
                        "She seems oblivious to your touch."
                    add tags 'sleep_touched' to terri

                "Remove her bra" if terri.has_tag('sleep_touched') and not terri.has_tag('sleep_bra_removed'):
                    wt_image indy_sleeping_1_2
                    "When [terri.name] rolls over, you reach out to unfasten her bra."
                    if terri.sleep_depth < 2:
                        wt_image indy_sleeping_1_3
                        "She startles at your touch, and sits up, covering herself."
                        terri.c "What?  What is it?? Is something wrong?"
                        $ terri.sleep_depth -= 1
                        call terri_sleep_session_wake from _call_terri_sleep_session_wake_1
                    elif terri.sleep_depth == 2:
                        wt_image indy_sleeping_1_41
                        "She stirs as you expose her breasts ...."
                        wt_image indy_sleeping_1_6
                        "... and rolls over, but doesn't wake."
                    else:
                        wt_image indy_sleeping_1_41
                        "She doesn't stir as you expose her breasts ..."
                        wt_image indy_sleeping_1_4
                        "... not even when you give her soft flesh a squeeze."
                        wt_image indy_sleeping_1_5
                        "You take advantage of her slumber to pinch her nipples erect, a state you can rarely get them to when she's awake."
                        wt_image indy_sleeping_1_6
                        "She moans slightly as her nipples stiffen and rolls over, but doesn't wake.  You may be able to safely go further, if you want."
                    add tags 'sleep_bra_removed' to terri

                "Remove her panties" if terri.has_tag('sleep_bra_removed') and not terri.has_tag('sleep_panties_removed'):
                    wt_image indy_sleeping_1_7
                    "When she turns over onto her back, you hook your fingers into her panties and slide them down."
                    if terri.sleep_depth < 3:
                        wt_image indy_sleeping_1_3
                        "She startles at your touch, and sits up, covering herself."
                        terri.c "What?  What is it??  Is something wrong?"
                        $ terri.sleep_depth -= 1
                        call terri_sleep_session_wake from _call_terri_sleep_session_wake_2
                    elif terri.sleep_depth == 3:
                        wt_image indy_sleeping_1_8
                        "She stirs at your touch, fidgeting as you pull the panties off her, but doesn't wake."
                    else:
                        wt_image indy_sleeping_1_8
                        "You're able to pull the panties completely off her without her stirring."
                        wt_image indy_sleeping_1_42
                        "You take advantage of her slumber to expose her clit.  It's slightly erect, no doubt thanks to the attention you paid to her nipples earlier.  You may be able to go further, if you want."
                    add tags 'sleep_panties_removed' to terri

                "Finger her" if terri.has_tag('sleep_panties_removed') and not terri.has_tag('sleep_fingered'):
                    wt_image indy_sleeping_1_9
                    "You gently tease her labia open."
                    if terri.sleep_depth < 4:
                        wt_image indy_sleeping_1_3
                        "She startles at your touch, and sits up, covering herself."
                        terri.c "What?  What is it??  Is something wrong?"
                        $ terri.sleep_depth -= 1
                        call terri_sleep_session_wake from _call_terri_sleep_session_wake_3
                    elif terri.sleep_depth == 4:
                        wt_image indy_sleeping_1_26
                        "Before you can insert a finger, she stirs and rolls over, crossing her legs."
                        wt_image indy_sleeping_1_8
                        "After a few minutes, she rolls back, exposing herself again."
                    else:
                        wt_image indy_sleeping_1_10
                        "She doesn't stir, not even when you slide a finger inside her and begin finger fucking her. She's completely out of it. You could do pretty much anything you want with her in this state."
                        wt_image indy_sleeping_1_8
                    add tags 'sleep_fingered' to terri

                "Put your cock in her mouth" if terri.has_tag('sleep_bra_removed') and terri.sleep_depth > 4:
                    wt_image indy_sleeping_1_46
                    "She's not much of a cocksucker even when she's awake, she could hardly do much worse asleep.  As she rolls towards you, her lips part slightly.  It's all the invitation that you need."
                    wt_image indy_sleeping_1_14
                    "You press the head of your cock against her lips and they open wider, letting you inside."
                    wt_image indy_sleeping_1_15
                    "Instinctively she starts suckling, though her technique is more like that used with a teat or a bottle than a cock. Still, it feels good, and with a few strokes of your hand along the underside of your shaft, you're ready to empty your load into her."
                    wt_image indy_sleeping_1_14
                    player.c "[player.orgasm_text]"
                    wt_image indy_sleeping_1_40
                    "She sighs contentedly as she swallows, as if the flood of warm liquid from her suckling wasn't just expected, but wanted."
                    wt_image indy_sleeping_1_45
                    "You slip out of the room, leaving her sleeping peacefully, just the slightest glistening of your cum on her lips."
                    $ terri.hypno_blowjob_count += 1
                    $ terri.hypno_swallow_count += 1
                    $ terri.temporary_count = 0
                    call forced_movement(living_room) from _call_forced_movement_179
                    orgasm notify

                "Arouse her" if terri.has_tag('sleep_fingered') and terri.sleep_depth > 4:
                    wt_image indy_sleeping_1_5
                    "[terri.name] moans softly as you apply a little more stimulation to her nipples ..."
                    terri.c "mmmhh"
                    wt_image indy_sleeping_1_9
                    "... and then moans again, a little louder as you massage her sex ..."
                    wt_image indy_sleeping_1_10
                    "... and resume fingering her."
                    terri.c "oohhh"
                    wt_image indy_sleeping_1_9
                    "Her pussy is now wet."
                    add tags 'aroused_now' to terri

                "Make her cum" if terri.has_tag('aroused_now'):
                    wt_image indy_sleeping_1_10
                    "You finger fuck the sleeping woman a little longer ..."
                    wt_image indy_sleeping_1_42
                    "... then rub her clit."
                    wt_image indy_sleeping_1_43
                    "Suddenly her body stiffens up.  She pushes your hand away and clamps her legs together firmly as she cums."
                    terri.c "Oooohhhhhh!!!!"
                    wt_image indy_sleeping_1_44
                    terri.c "What ... what are you doing here?"
                    player.c "I heard a noise and came in to check on you.  Are you okay, you look flushed?"
                    wt_image indy_sleeping_1_25
                    terri.c "Thanks for checking on me, but I'm fine.  I just had a ... weird dream.  Can you leave?  I need a moment to myself."
                    $ terri.hypno_orgasm_count += 1
                    $ terri.temporary_count = 0
                    call forced_movement(living_room) from _call_forced_movement_206
                    change player energy by -energy_very_short notify

                "Fuck her" if terri.has_tag('sleep_panties_removed') and terri.sleep_depth > 4:
                    wt_image indy_sleeping_1_9
                    if terri.has_tag('aroused_now'):
                        "[terri.name]'s a limp fuck even when she's awake, she could hardly be much worse asleep.  You tease her labia apart and are pleased to see that your earlier stimulation has left her wet enough that you don't need to apply any lubricant."
                    else:
                        "[terri.name]'s a limp fuck even when she's awake, she could hardly be much worse asleep.  You tease her labia apart and apply enough lubricant to let you enter her without waking her."
                    wt_image indy_sleeping_1_17
                    "Placing the head of your cock against her sex and taking a grip of her hip, you insert yourself inside ..."
                    wt_image indy_sleeping_1_18
                    "... and begin fucking the sleeping woman."
                    $ title = "How do you want to fuck her?"
                    menu:
                        "Face up":
                            wt_image indy_sleeping_1_47
                            "She's dead to the world and seemingly oblivious to the liberties you're taking with her body ..."
                            wt_image indy_sleeping_1_16
                            "... or the cum you're pumping inside it."
                            wt_image indy_sleeping_1_47
                            player.c "[player.orgasm_text]"
                            wt_image indy_sleeping_1_26
                            "When you pull out, she closes her legs, unconcerned about the sperm she's trapping inside of her.  By the time she wakes, all evidence of it will be gone."
                        "Face down":
                            wt_image indy_sleeping_1_19
                            "Rolling her over, you fuck her limp body, thrusting into her faster and faster."
                            wt_image indy_sleeping_1_20
                            "When she still doesn't react, you quicken your pace even more, pounding into her until you empty your load into her unstirring form."
                            wt_image indy_sleeping_1_23
                            player.c "[player.orgasm_text]"
                            wt_image indy_sleeping_1_21
                            "She stays asleep in that position, like a baby, head down and bum up, unaware or unconcerned about your sperm dripping out of her.  By the time she wakes, all evidence of it will be gone."
                    $ terri.hypno_sex_count += 1
                    $ terri.temporary_count = 0
                    call forced_movement(living_room) from _call_forced_movement_180
                    orgasm notify

                "Jerk off on her face" if terri.sleep_depth > 3:
                    if terri.has_tag('sleep_panties_removed'):
                        wt_image indy_sleeping_1_8
                    elif terri.has_tag('sleep_bra_removed'):
                        wt_image indy_sleeping_1_6
                    elif terri.has_tag('sleep_hypno_today'):
                        wt_image indy_sleeping_1_37
                    else:
                        wt_image indy_sleeping_1_2
                    "She looks so pretty, so innocent, lying there gently snoring, that your cock gets rock hard watching her."
                    wt_image indy_sleeping_1_45
                    "You take your dick out and stroke it, so close to her face it's a wonder the smell of your arousal doesn't wake her."
                    wt_image indy_sleeping_1_11
                    "When she rolls over towards you, inadvertently positioning herself directly in front of your cock, you feel your balls boiling over and let yourself go."
                    wt_image indy_sleeping_1_12
                    "She flinches as your warm spunk lands on her face, but she's in too deep a slumber to wake."
                    player.c "[player.orgasm_text]"
                    wt_image indy_sleeping_1_13
                    "You milk the last of the cum from your balls, watching as it rolls down her cheek, then leave to let her finish her sleep.  Most of your seed will be wiped off on her pillow or the sheets the next time she turns over, and the remainder will be dry by the time she wakes."
                    $ terri.hypno_facial_count += 1
                    $ terri.temporary_count = 0
                    call forced_movement(living_room) from _call_forced_movement_181
                    orgasm notify

                "Wake her":
                    wt_image indy_sleeping_1_3
                    "She covers herself as she sits up."
                    terri.c "Sorry, I must have been asleep.  I didn't hear you come in."
                    $ terri.temporary_count = 0
                    call terri_sleep_session_wake from _call_terri_sleep_session_wake_4

                "Let her sleep":
                    $ terri.temporary_count = 0
                    "You quietly tip toe out of the room, careful not to wake her.  She needs her rest."
                    call forced_movement(living_room) from _call_forced_movement_182

    else:
        pass
    return

label terri_sleep_session_wake:
    $ terri.temporary_count = 0
    player.c "Were you having a good sleep?"
    wt_image indy_sleeping_1_38
    if terri.sleep_depth < 3:
        terri.c "Not really.  I'm not a good sleeper.  I have a lot of disturbing dreams."
        player.c "Do you want to talk about those dreams?"
        wt_image indy_sleeping_1_39
        terri.c "Definitely not! What did you want?"
    elif terri.sleep_depth < 5:
        terri.c "Not bad, actually.  Better than I usually do.  What did you want?"
    else:
        terri.c "Lately I've been sleeping like a log.  Learning hypnosis seems to be good for me.  Did you want something?"
    $ title = "What do you tell her?"
    menu:
        "I'm horny":
            wt_image indy_sleeping_1_48
            terri.c "Now?  I'm tired.  I just want to go back to sleep."
            $ title = "What should she do?"
            menu:
                "Suck you off":
                    wt_image indy_sleeping_1_32
                    player.c "Do a good job sucking my dick and this won't take long."
                    wt_image indy_sleeping_1_27
                    "She's smart enough to realize this is the fastest route back to sleep.  She takes out your cock ..."
                    wt_image indy_sleeping_1_28
                    "... licks it hard while caressing your balls ..."
                    wt_image indy_sleeping_1_29
                    "... then starts sucking."
                    wt_image indy_sleeping_1_30
                    "She's no better sucking cock half asleep than she is when she's fully awake, but eventually she gets the job done."
                    $ title = "Where do you want to cum?"
                    menu:
                        "On her face":
                            wt_image indy_sleeping_1_34
                            player.c "Face, [terri.name]."
                            wt_image indy_sleeping_1_35
                            player.c "[player.orgasm_text]"
                            wt_image indy_sleeping_1_32
                            "She cleans off her face and looks up at you."
                            terri.c "If you're feeling better now, I'm going to try going back to sleep."
                            player.c "Didn't you want to wear my cum while you slept?"
                            wt_image indy_sleeping_1_48
                            terri.c "Ewww.  No.  It would be sticky and uncomfortable.  I could never sleep like that."
                            $ terri.facial_count += 1
                        "In her mouth":
                            wt_image indy_sleeping_1_31
                            "She wraps her lips tight around you as you fill her mouth."
                            player.c "[player.orgasm_text]"
                            wt_image indy_sleeping_1_33
                            terri.c "If you're feeling better now, I'm going to try going back to sleep."
                            wt_image indy_sleeping_1_45
                            "How could you not be feeling better, with your sperm glistening on your pretty assistant's lips as she drifts back to sleep?  You leave her to get her rest."
                            $ terri.swallow_count += 1
                    $ terri.blowjob_count += 1
                    orgasm notify
                "Turn around":
                    wt_image indy_sleeping_1_49
                    player.c "I don't mind if you go back to sleep, just turn around first.  I'll do all the work."
                    wt_image indy_sleeping_1_22
                    terri.c "Don't be too long, okay?"
                    wt_image indy_sleeping_1_23
                    "It's not the most enthusiastic offer you've ever received, but it'll do.  You lube yourself up and push into her."
                    wt_image indy_sleeping_1_24
                    "She doesn't exactly fall back to sleep while you're fucking her, but she comes close.  Fortunately, that doesn't distract from your enjoyment of her tight pussy."
                    wt_image indy_sleeping_1_23
                    player.c "[player.orgasm_text]"
                    wt_image indy_sleeping_1_21
                    "The load you leave in her is a sticky one."
                    terri.c "I should probably clean that up before I go back to sleep."
                    wt_image indy_sleeping_1_25
                    player.c "Not on my account.  Were you planning on letting someone else between your legs tonight?"
                    terri.c "No, of course not.  You're right, it's okay if I go to bed with your cum inside me."
                    wt_image indy_sleeping_1_26
                    "She's back to sleep before you leave the room.  Being a hypnotist's assistant is tiring work."
                    $ terri.sex_count += 1
                    orgasm notify
                "Let her sleep":
                    wt_image indy_sleeping_1_33
                    terri.c "Thanks.  I really am tired.  I'll look after you some other time, okay?"
                    wt_image indy_sleeping_1_40
                    "You leave her to her beauty sleep."
            call forced_movement(living_room) from _call_forced_movement_183
        "I just wanted to make sure you were okay":
            wt_image indy_sleeping_1_33
            terri.c "Thanks for checking on me, but I'm fine.  Really.  I'm going to try and rest, now."
            wt_image indy_sleeping_1_40
            "You leave her to her beauty sleep."
            call forced_movement(living_room) from _call_forced_movement_184
    return

label tar_exit:
    return

label tsp_examine:
    return

label tsp_no_access:
    return

label tsp_enter:
    return

label tsp_exit:
    return

label qcs_examine:
    return

label qcs_no_access:
    return

label qcs_enter:
    return

label qcs_exit:
    return

################################### NOTES ###################################
##################### TODO #####################
# look for opportunity to add school visit options using Threesome 15 Young 4 and Young 17 sets
# look for opportunity to add post boob job content using Bathroom 3, Bed 9 and 11, Collar 4, Lingerie 8, Sex 7 8 and 13, Sofa 15, Strip 2, and Toys 6 17 and 19 sets


## Character Status
#0 = not yet prospect
#1 = prospect, .status = "available_to_be_client" and .status = "waiting_on_message"
#2 = lost prospect, .status = "rejected"
#3 = client, .status = "on_training"
#4 = unsatisfied former client, add tags 'unsatisfied' and .status = "post_training"
#5 = satisfied former client, add tags 'satisfied' and .status = "post_training"
#6 = continuing_actions, add tags 'continuing_actions' and .status = "post_training"
#7 = satisfied former client not continuing, rem tags 'continuing_actions' and .status = "post_training"
#8 = post continuing actions, add tags 'post_continuing_actions' and .status = "post_training"
