## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: Wifetrainer

# Package Register
# register_package bree name "Bree the Bondage Store Clerk" description "This package adds Bree the Store Clerk to The Steel Trap" dependencies core
register bree_pregame 10 in core as "Bree the Bondage Store Clerk"

label bree_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('support', "Bree the Bondage Store Clerk (Veruca James)")]
    model_credits += [('bit', 'Elaine for Bree (Francesca Le)')]
    model_credits += [('bit', 'Club Member for Bree (Katrina Jade)')]


    ## Character Definition
    bree = Person(Character("Bondage Store Clerk", who_color = "#800000", what_color = "#800000", window_background = gui.dialogue_background_dark_font_color), "bree", cut_portrait = True, prefix = "", suffix = "")
    #breemaid = Person(Character("Bree the Club Maid", who_color = "#800000", what_color = "#800000"), "breemaid", cut_portrait = True, prefix = "", suffix = "") # changed to single character

    # Other Characters
    elaine = Character("Elaine", who_color = "#804000", what_color = "#804000", window_background = gui.dialogue_background_dark_font_color)
    breeclubman = Character("Club Member", who_color = "#000066", what_color = "#000066", window_background = gui.dialogue_background_dark_font_color)
    breeclubwoman = Person(Character("Club Member", who_color = "#400080", what_color = "#400080", window_background = gui.dialogue_background_dark_font_color), "breeclubwoman", cut_portrait = True, prefix = "", suffix = "")

    ## Actions
    # Item demonstrations when Bree is clerk
    steel_trap.add_action_to_store_items("Ask for a demonstration", label = "_demonstration", condition = "bree.location == steel_trap", unseen = False, seen_result = True)

    # Bree actions
    bree.action_ask_about_nipple_clips = bree.add_action("Ask about nipple clips", label = "_ask_about_nipple_clips", condition = "jasmine.whore_play_status == 7 and bree.location == steel_trap and not bree.has_tag('discussed_jasmine_nipple_clips')")
    bree.action_bad_habit_training = bree.add_action("Deal with her bad habit", label = "_bad_habit_training", condition = "bree.can_be_interacted and bree.has_tag('slavegirl') and bree.bad_habit_status < 4 and not bree.has_tag('bad_habit_trained_this_week') and bree.location == bedroom")
    bree.action_choose_position = bree.add_action("Choose her position", label = "_choose_position", condition = "bree.has_tag('slavegirl') and bree.location == bedroom")
    bree.action_dominate = bree.add_action("Dominate her", label = "_dominate", condition = "bree.can_be_interacted and player.has_tag('dominant') and bree.name == 'Bree' and bree.location == steel_trap and not bree.has_tag('slavegirl')")
    bree.action_give_her_things_to_do = bree.add_action("Give her things to do", label = "_give_her_things_to_do", condition = "bree.has_tag('slavegirl') and bree.location == bedroom")
    bree.action_let_her_cum_degraded = bree.add_action("Let her cum", label = "_let_her_cum_degraded", condition = "bree.can_be_interacted and bree.has_tag('degraded')")
    bree.action_provide_rules = bree.add_action("Provide rules", label = "_provide_rules", condition = "bree.has_tag('slavegirl') and bree.location == bedroom")
    bree.action_relieve_yourself_degraded = bree.add_action("Relieve yourself", label = "_relieve_yourself_degraded", condition = "bree.can_be_interacted and bree.has_tag('degraded')")
    bree.action_rename = bree.add_action("Rename her", label = "_rename", condition = "bree.has_tag('slavegirl') or bree.has_tag('petgirl') or bree.has_tag('degraded')")
    bree.action_slapping_first = bree.add_action("Talk to her about slapping", label = "_slapping_first", condition = "bree.can_be_interacted and bree.has_tag('slavegirl') and not bree.has_tag('accepts_slapping') and bree.location == bedroom")
    bree.action_slapping_subsequent = bree.add_action("Slap her", label = "_slapping_subsequent", condition = "bree.can_be_interacted and bree.has_tag('slavegirl') and bree.has_tag('accepts_slapping') and bree.location == bedroom")
    bree.action_spank = bree.add_action("Spank her", label = "_spank", condition = "bree.can_be_interacted and bree.has_tag('slavegirl') and bree.location == bedroom")
    bree.action_hurt_her = bree.add_action("Hurt her", label = "_hurt_her", condition = "bree.can_be_interacted and bree.has_tag('slavegirl') and bree.location == bedroom")
    bree.action_use_fuck_machine = bree.add_action("Use fuck machine", label = "_use_fuck_machine", condition = "bree.can_be_interacted and bree.has_tag('slavegirl') and dungeon.has_item(fuck_machine) and bree.location == bedroom")
    bree.action_use_her = bree.add_action("Use her", label = "_use_her", condition = "bree.can_be_interacted and bree.has_tag('slavegirl') and bree.location == bedroom")
    bree.action_use_her_degraded = bree.add_action("Use her", label = "_use_her_degraded", condition = "bree.can_be_interacted and bree.has_tag('degraded')")
    bree.action_use_suspension_gear = bree.add_action("Use suspension gear", label = "_use_suspension_gear", condition = "bree.can_be_interacted and bree.has_tag('slavegirl') and dungeon.has_item(suspension_gear) and bree.location == bedroom")
    bree.action_whip_her_degraded = bree.add_action("Whip her", label = "_whip_her_degraded", condition = "bree.can_be_interacted and bree.has_tag('degraded') and dungeon.has_item(floggers)")
    bree.action_play_fetch = bree.add_action("Play fetch", label = "_play_fetch", condition = "bree.can_be_interacted and bree.has_tag('petgirl') and bree.has_item(fetch_toy)")
    bree.action_watch_her = bree.add_action("Watch her", label = "_watch_her", condition = "bree.has_tag('club_maid') and not bree.has_tag('watched_today') and bree.location == club")
    bree.action_talk_friendly = bree.add_action("Talk to her", label = "_talk_friendly", condition = "bree.can_be_interacted and bree.location == steel_trap and bree.hypno_count > 2")
    bree.action_lend_to_master_m = bree.add_action("Lend to Master M", label = "_lend_to_master_m", condition = "bree.has_tag('slavegirl') and player.has_tag('m_waiting_for_slave')")
    bree.action_your_name = bree.add_action("Tell her how to address you", label="_your_name", condition="bree.has_tag('slavegirl')")

    bree.action_alexis = None # note: purposefully none until converted to slave to avoid circle issue with Alexis' name in the action
    bree.action_elsa = None # note: purposefully none until converted to slave to avoid circle issue with Elsa's name in the action

    bree.relationship_action = bedroom.add_action("[bree.full_name]", label = bree.short_name + "_relationship_status", context = "_relationship_status", condition = "bree.has_tag('slavegirl')")


    ## Tags
    # Common Character Tags
    bree.add_tags('no_hypnosis', 'likes_boys', 'likes_girls', 'tst_store_content', 'working_at_store')
    breeclubwoman.add_tags('no_hypnosis', 'likes_girls')

    # Character Specific Tags
    # N/A

    ## Locations
    bree.location = steel_trap

    ## Other
    bree.change_status("minor_character")

    # Start Day Events
    start_day_labels.append('bree_start_day')

    ########### VARIABLES ###########
    # Common Character Variables
    bree.add_stats_with_value('hypno_blowjob_count', 'hypno_swallow_count', 'maintain_week_sg', 'random_number')

    # Character Specific Variables
    bree.add_stats_with_value('bad_habit_status', 'club_reward_counter', 'date_count', 'maintain_week_sg', 'position', 'submit_count', 'work_intro_outfit')
    bree.position = 1 ## starting position for her as slavegirl
    #bree.slap_action_name = "Talk to her about slapping" #changed into two different actions

    bree.description = "The bored looking store clerk ignores you."
    bree.note_left = False
    bree.asked_limits = False
    bree.tookoutcock = False
    bree.storefuck = False
    bree.choice_needed = False
    bree.left_to_suffer = False
    bree.talk_rules = "She is allowed to talk."
    bree.cum_rules = "She is allowed to orgasm."
    bree.your_respect_name = "Sir"
    # bree.work_description = "{} has not been assigned any work.".format(bree.name) ## this dynamic naming is not working, so replaced for now with the below
    bree.work_description = "She has not been assigned any work."

    ## Character Specific Objects
    note_from_bree = Item('Note from Bree', 'notefrombree', with_examine = True)
    note_from_bree.action_read = note_from_bree.add_action("Read the Note", label = '_read')

    ######## EXPANDABLE MENUES #######
    bree_give_her_work_menu = ExpandableMenu("What work do you want to assign to her?", cancelable = False)
    # note: these don't have to be defined in pregame, can be added in game; some of these would ideally be in the script for the content that opens them up, rather than here
    bree.choice_give_her_work_maid =  bree_give_her_work_menu.add_choice("Work as a maid for the Club", "bree_give_her_work_menu_maid", condition = "player.has_tag('club_access') and player.has_tag('club_first_visit_complete') and not bree.has_tag('club_maid')")
    bree.choice_give_her_work_stop_maid  =  bree_give_her_work_menu.add_choice("Stop working as a maid for the Club", "bree_give_her_work_menu_maid_stop", condition = "bree.has_tag('club_maid')")
    bree.choice_give_her_work_no_change  =  bree_give_her_work_menu.add_choice("No changes right now", "bree_give_her_work_no_change")
  return

# Display Portrait
# CHARACTER: Display Portrait
label bree_update_media:
    if bree.has_tag('hypno_now'):
        $ bree.description = "Still in a trance, Bree waits for you to finish shopping."
    elif bree.has_tag('club_maid') and current_location == club:
        if bree.has_tag('maid_exposed_today'):
            $ bree.change_image('b_clerk_maid_1_5')
        else:
            $ bree.change_image('b_clerk_maid_1_1')
    elif bree.has_tag('submitting_now'):
        $ bree.description = "As you instructed, Bree is waiting where you left her, in case you need her."
    elif bree.has_tag('slavegirl') and current_location == bedroom:
        # $ bree.change_image('b_clerk_position_[bree.position]')
        if bree.position == 1:
            $ bree.change_image('b_clerk_position_1')
        elif bree.position == 2:
            $ bree.change_image('b_clerk_position_2')
        elif bree.position == 3:
            $ bree.change_image('b_clerk_position_3')
        elif bree.position == 4:
            $ bree.change_image('b_clerk_position_4')
        elif bree.position == 5:
            $ bree.change_image('b_clerk_position_5')
    elif bree.has_tag('degraded'):
        $ bree.change_image('b_clerk_degraded_1')
    elif bree.has_tag('petgirl'):
        $ bree.change_image('b_clerk_cage')
    elif current_location == steel_trap and bree.submit_count == 0 and bree.hypno_count == 0:
        $ bree.work_intro_outfit += 1
        if bree.work_intro_outfit > 4:
            $ bree.work_intro_outfit = 1
        if bree.work_intro_outfit == 1:
            $ bree.change_image('b_clerk_working_11')
        elif bree.work_intro_outfit == 2:
            $ bree.change_image('b_clerk_working_12')
        elif bree.work_intro_outfit == 3:
            $ bree.change_image('b_clerk_working_1')
        else:
            $ bree.change_image('b_clerk_working_16')
    else:
        pass
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label bree_examine:
    if not bree.has_tag('examined'):
        add tags 'examined' to bree
        $ bree.action_talk = bree.add_action("Talk to her", label ="_talk", condition = "bree.hypno_count == 0 and bree.submit_count == 0 and not bree.has_any_tag('shut_off_store_talk', 'slavegirl', 'petgirl', 'degraded') and bree.location == steel_trap")
    if bree.has_tag('degraded'):
        "[bree.full_name] no longer feels human. She can't stand anyone trying to treat her like one. She needs to be treated as ... nothing. It's the only way she feels anything."
        "For her own safety, you keep her in a straightjacket. For the peace of the household, you keep her gagged. She's fed and watered regularly and her litter box - when she chooses to use it - is kept clean."
        "It's the best you can do for her. That, and treat her the way she craves to be treated."
    elif bree.has_tag('petgirl'):
        "[bree.full_name] is still partially feral, and you need to keep her in a cage.  The process of turning her into your puppygirl destroyed not only her sense of humanity, but also all understanding of what it is to live with humans.  Fortunately, she does understand the need to obey a firm hand."
    elif bree.has_tag("club_maid") and current_location == club:
        "She's not happy being assigned menial labor around the Club. [bree.name] has a bit of a lazy streak that was evident the first time you saw her working at the Steel Trap."
        "She doesn't get to exercise it here at the Club. Too many members are keeping an eye on her and making sure she isn't slacking off. You can watch her from afar, but you have to keep your distance."
        "One of the Club rules is that when you assign someone to work at the Club, you can't interrupt their work or sneak off to a private room with them. They're Club property while they're here. Other Club members, however, can take liberties with them, if their owner allows it."
    elif bree.has_tag('slavegirl'):
        "[bree.full_name] waits for you as you have instructed."
        "[bree.talk_rules] [bree.cum_rules]"
    else:
        "[bree.description]"
    return

#label breemaid_examine:
    #wt_image b_clerk_maid_1_1
    #"She's not happy being assigned menial labor around the Club.  [bree.name] has a bit of a lazy streak that was evident the first time you saw her working at the Steel Trap.  She doesn't get to exercise it here at the Club.  Too many members are keeping an eye on her and making sure she isn't slacking off.  You can watch her from afar, but you have to keep your distance.  One of the Club rules is that when you assign someone to work at the Club, you can't interrupt their work or sneak off to a private room with them.  They're Club property while they're here.  Other Club members, however, can take liberties with them, if their owner allows it."
    #return

label breeclubwoman_examine:
    wt_image b_clerk_maid_2_15
    "The Club member who had been chastising [bree.name] is making a spectacle of herself, especially whenever another female Club member walks by."
    wt_image b_clerk_maid_2_16
    breeclubwoman.c "My pussy is prettier than your pussy."
    "You'll release her from her trance later today.  In the meantime, she's doing a great job of resetting her position within the Club's social cliques."
    return


# Talk to Character
label bree_talk:
  wt_image b_clerk_working_11
  player.c "Hello"
  wt_image b_clerk_working_1
  "She glances up at you, then goes back to doing nothing."
  $ title = "Ask her name?"
  menu:
    "Yes":
      rem tags 'no_hypnosis' from bree
      if player.has_tag('dominant'):
        player.c "What's your name?"
        wt_image b_clerk_working_2
        "The store clerk looks at you more closely.  She hesitates for a moment before answering."
        bree.c "Bree.  My name is Bree."
        $ bree.change_full_name("", "Bree", "the Bondage Store Clerk")
        $ bree.description = "Bree, the clerk at The Steel Trap BDSM store."
        add tags 'shut_off_store_talk' to bree
      else:
        player.c "What's your name?"
        wt_image b_clerk_working_2
        "The store clerk looks at you for a moment, then goes back to doing nothing."
        wt_image b_clerk_working_11
        bree.c "You're not my type."
        if player.has_tag('supersexy'):
            "Not the reaction you normally get from women. I guess good looks and natural charm don't work on everyone"
        add tags 'shut_off_store_talk' to bree
    "No":
      pass
  return

label bree_talk_friendly:
    player.c "You're being friendly today."
    bree.c "Yes, [bree.your_respect_name].  I pride myself on being helpful and friendly with all of our customers.  Please let me know if I can assist you with your shopping."
    return

# Hypno Actions
label bree_hypnosis_start:
    if bree.location == steel_trap:
        $ bree.training_session()
        # Initial Scene Dialog
        "The two of you are alone in the store.  You decide to make use of this opportunity."
        # change art for 1st and 2nd hypno session only
        if bree.hypno_count < 3:
            wt_image b_clerk_working_16
        player.c "Look at this for me"
        # First Hypno Session
        if bree.hypno_count == 0:
            call focus_image from _call_focus_image_35
            player.c "You've been acting very rude. You should not be rude to your customers. You should be polite and friendly."
            wt_image b_clerk_hypno_1
            player.c "You want to be polite and friendly. You don't want to be rude. I'm going to ask you that question again. This time, you'll answer me politely. What's your name?"
            bree.c  "Bree.  My name is Bree."
            $ bree.change_full_name("", "Bree", "the Store Clerk")
            player.c "That's better, Bree. You want to be friendly, Bree. It's friendly to show me your breasts while we are talking.  Be friendly now, Bree.  Show me your breasts."
            wt_image b_clerk_hypno_breasts_1
            if not player.has_tag('first_hypno_breasts_message'):
                add tags 'first_hypno_breasts_message' to player
                "[player.first_hypno_breasts_message_text]"
            "Bree steps out from behind the counter. She's not very tall. Even standing, she needs to look up to meet your eyes as she raises her top."
            wt_image b_clerk_hypno_breasts_2
            player.c "From now on, Bree, you'll be friendly to me. You will not be rude. You don't want to be rude."
            "You've taken her as far as you can for this first session.  You work on lowering her resistance, then instruct her to cover herself up when you leave."
            $ bree.change_image('b_clerk_hypno_breasts_2')
            add tags 'hypno_now' to bree
        # Second Hypno Session
        elif bree.hypno_count == 1:
            call focus_image from _call_focus_image_36
            player.c "Bree, you want to be polite to me.  Polite and friendly and helpful."
            wt_image b_clerk_hypno_1
            player.c "The friendly thing to do is to show me your breasts, Bree."
            wt_image b_clerk_hypno_breasts_1
            "Bree steps out from behind the counter again and lifts her top."
            wt_image b_clerk_hypno_breasts_2
            # only progress if hypnosis level high enough or dominant
            if player.test('hypnosis_level', 9) or player.has_tag('dominant'):
                player.c "You've been rude and inconsiderate to me, Bree.  You're sorry that you've been rude.  You should not have been rude when you should have been helpful."
                player.c "You've been bad.  You know you've been bad, and you're sorry.  In the future, you'll be polite and friendly with me.  And you'll be helpful."
                player.c "Apologize to me now, Bree.  Tell me you're sorry that you were rude. Tell me you've been a bad girl and that you should not have been rude to me when you should have been polite."
                player.c "Tell me that you'll be friendly and helpful in the future.  Tell me now, Bree."
                wt_image b_clerk_hypno_breasts_3
                bree.c "I ... I'm sorry I was rude to you.  I should not have been rude.  I've been a bad girl.  I'll be polite, friendly and helpful with you in the future."
                "You've lowered her resistance as much as you can for now.  You instruct her to stay as is she is until you leave."
                $ bree.change_image('b_clerk_hypno_breasts_3')
            else:
                "You'd like to take Bree further, but even under hypnosis she doesn't see you as someone she respects."
                "If you were a stronger hypnotist or if you were someone she was attracted to, you might be able to break down her resistance to you, but as it is you'll need to be satisfied with a view of her pretty breasts."
                "You instruct her to cover herself up when you leave and return to browsing the store"
                $ bree.hypno_count -=1
                $ bree.change_image('b_clerk_hypno_breasts_2')
            add tags 'hypno_now' to bree
        # Third Hypno Session
        elif bree.hypno_count == 2:
            call focus_image from _call_focus_image_37
            player.c "Bree, you want to be polite to me.  Polite and friendly and helpful."
            wt_image b_clerk_hypno_2
            player.c "The friendly thing to do is to show me your breasts, Bree."
            wt_image b_clerk_hypno_breasts_5
            "Bree removes her top.  She seems to becoming more comfortable with you."
            wt_image b_clerk_hypno_breasts_6
            player.c "From now on, you'll be helpful to me when I'm shopping. If I want something, you'll assist me with it. You'll be friendly and helpful to me, Bree"
            wt_image b_clerk_hypno_breasts_4
            bree.c "Yes, I'll be friendly and helpful to you."
            $ bree.change_image('b_clerk_hypno_breasts_4')
            add tags 'hypno_now' to bree
        # Additional Hypno Sessions
        else:
            call focus_image from _call_focus_image_38
            player.c "Bree, you want to be polite to me.  Polite and friendly and helpful."
            wt_image b_clerk_hypno_2
            player.c "The friendly thing to do is to show me your breasts, Bree."
            wt_image b_clerk_hypno_breasts_5
            "Bree removes her top for your inspection."
            wt_image b_clerk_hypno_breasts_6
            player.c "Bree, you want to be helpful and friendly. I'm a good customer. I'm a good customer, but you've been rude to me. You feel bad that you were rude to me. You were bad. You should not have been rude. You want to make it up to me for being rude before."
            $ title = "How should she make it up to you?"
            menu:
                "Store discount" if steel_trap.discount_ratio > 0.8:
                    wt_image b_clerk_hypno_breasts_4
                    player.c "You should treat me as a good customer, Bree.  A good customer does not have to pay full price.  When I release you from the trance, you'll get me a store discount card, Bree."
                    wt_image b_clerk_working_10
                    "You tell her to dress, then bring her out of the trance."
                    bree.c "I have something for you.  It's a store discount card.  It'll get you 20 percent off all regularly priced items.  Please accept this as my way of saying 'thank you 'for being such a good customer."
                    $ steel_trap.discount_ratio = 0.8
                "Apology":
                    player.c "Apologize to me, Bree.  Tell me you're sorry that you were rude. Tell me that you're a bad girl who should not have been rude to me."
                    wt_image b_clerk_hypno_breasts_3
                    bree.c "I'm very sorry I was rude to you.  I should not have been rude.  I've been a very bad girl."
                    $ bree.change_image('b_clerk_hypno_breasts_3')
                    add tags 'hypno_now' to bree
                "Proper apology (blowjob)":
                    player.c "You're going to give me an apology, Bree.  A proper apology.  You'll show me how sorry you are that you were rude. You'll show me how sorry you are that you were a bad girl.  You'll make it up to me for being bad before, by being good to me now. Show me now, Bree."
                    wt_image b_clerk_hypno_breasts_3
                    bree.c "I'm very sorry I was rude to you ..."
                    wt_image b_clerk_hypno_breasts_7
                    player.c "No, Bree.  I don't want to hear your apology.  I want to feel your apology.  Show me that you're sorry with a proper apology.  Get on your knees, Bree."
                    wt_image b_clerk_hypno_bj_1
                    "Whatever her background is, it's not a prudish or naive one.  She understands what you mean. She sinks to her knees as you instructed.  When you unzip your pants, she opens her mouth without prompting."
                    wt_image b_clerk_hypno_bj_2
                    "She keeps her eyes on you as she takes you into her warm mouth. You place your hand on her head to control the speed at which she bobs up and down on your hard member. Other than that, she needs no further instructions. In her hypnotized state, she's rationalized the need to blow you to make up for her past transgressions."
                    wt_image b_clerk_bj_3
                    player.c "Tell me you're sorry for being rude, Bree.  Then keep your mouth open."
                    wt_image b_clerk_hypno_bj_3
                    bree.c "I'm sorry I was rude to you."
                    "As she finishes her apology, you release your load down the back of her throat."
                    wt_image b_clerk_bj_13
                    player.c "[player.orgasm_text]"
                    $ bree.change_image('b_clerk_hypno_breasts_7')
                    $ bree.hypno_blowjob_count += 1
                    $ bree.hypno_swallow_count += 1
                    orgasm
                    add tags 'hypno_now' to bree
                "Punishment":
                    player.c "When you're bad, you should be punished.  Being punished reminds you not to be bad in the future. You want me to punish you, Bree."
                    player.c "You want me to punish you for being rude, so that you won't be rude in the future.  You want to remember to be polite, friendly and helpful.  Being punished will help you to remember.  Tell me you want me to punish you, Bree."
                    wt_image b_clerk_hypno_breasts_3
                    bree.c "I'm sorry I was rude to you.  I've been bad.  I should be punished.  Please punish me for being bad."
                    player.c "I don't believe you yet, Bree.  You mean what you're saying, Bree.  Let me hear in your voice that you mean it."
                    wt_image b_clerk_hypno_3
                    "She looks at you contritely and begins to plead more earnestly."
                    bree.c "Please punish me.  Please, I've been so bad.  I've been such a bad girl, I need to be punished.  Please, I want you to punish me.  Please punish this bad girl."
                    wt_image b_clerk_backside_2
                    "Without further prompting, she turns and lowers her panties, offering you her backside."
                    wt_image b_clerk_spank_2
                    "You bend Bree forward and begin to tattoo her ass a pretty shade of red ... *smack*"
                    wt_image b_clerk_pain_1
                    "She whimpers as you spank her ... *smack*"
                    bree.c "ow"
                    wt_image b_clerk_spank_2
                    "*smack*"
                    wt_image b_clerk_pain_1
                    bree.c "ow"
                    wt_image b_clerk_spank_2
                    "Those whimpers turn to soft cries, then louder cries as you increase the intensity of the spanking, but she never tries to escape your grip or avoid the punishment ... *SMACK*"
                    wt_image b_clerk_pain_1
                    bree.c "Ow!"
                    wt_image b_clerk_spank_2
                    "*SMACK*"
                    wt_image b_clerk_pain_1
                    bree.c "OW!!"
                    wt_image b_clerk_hypno_3
                    "When your hand begins to hurt, you finally let go of her.  She slumps to the floor beside you."
                    bree.c "Thank you for punishing me.  I'm sure the spanking will help me remember to be polite, friendly and helpful in the future."
                    $ bree.change_image('b_clerk_hypno_breasts_3')
                    add tags 'hypno_now' to bree
                    change player energy by -energy_short
                "Be polite":
                    player.c "You will make it up to me by being polite and friendly.  Show me how polite and friendly you can be, Bree."
                    wt_image b_clerk_hypno_breasts_4
                    bree.c "I'm very sorry I was rude to you before.  Thank you for coming back to the store.  Please let me know if there's anything I can do to help you with your shopping."
                    $ bree.change_image('b_clerk_hypno_breasts_4')
                    add tags 'hypno_now' to bree

        $ bree.hypno_session() # deducts energy and records she was hypnotized
        notify
    else:
        "Not here."
    ## note: following three lines are correct way to halt hypnosis sequence if backing up to the hypnosis context menu, but not for a pure halt that goes back to player action options
    #$ bree.hypno_action.backtrack = True
    #$ context = "bree_hypnosis"
    #break_sequence
    $ ignore_context_change = True # this breaks the hypno sequence before calling hypnosis_context menu, which is not used for bree;
    # note: the above command also means the normal hypno trigger implant sequence doesn't occur, which is fine as Bree doesn't get a trigger
    return

label bree_hypnosis_end:
    pass
    #break_sequence # no
    return

## Character Specific Actions
# Dominate Her Action
label bree_dominate:
  $ bree.add_tags('trained_today', 'trained_this_week', 'submitting_now')
  $ bree.submit_count += 1
  $ player.submission_action_count += 1

  if bree.submit_count == 1:
      wt_image b_clerk_working_2
      "It's not difficult for you to identify submissive women under normal circumstances.  When they wear a collar while working at a BDSM store, it's really not difficult to identify them."
      "That doesn't mean she's available or attracted to you, but it doesn't hurt to try."
      player.c "Is that how you should be standing, Bree?"
      bree.c "No"
      wt_image b_clerk_working_3
      "She replies quietly and moves out from behind the counter. Nervously she fingers her collar as she stands up straight and looks at you."
      "That answers the question of whether she's attracted to you.  You haven't decided whether you will act on that attraction or not.  Either way, the correct course is to make her wait."
      player.c "Better.  Stay there while I shop. If I need you, I'll let you know.  When I leave, you can go back about your business."
      wt_image b_clerk_working_15
      "Bree nods and waits."
      $ bree.change_image('b_clerk_working_15')

  elif bree.submit_count == 2:
      $ bree.submit_count -= 1
      wt_image b_clerk_working_3
      player.c "Hello, Bree.  Your posture is better today."
      bree.c "Thank you.  Is there anything I can help you with today?"
      $ title = "How do you respond?"
      menu:
          "Ask if she enjoys helping":
              $ bree.submit_count += 1
              player.c "Do you enjoy helping people, Bree?"
              wt_image b_clerk_working_15
              "She hesitates for a moment."
              bree.c "Honestly?  Not really. Not most people anyway.  This job it ... kinda sucks."
              player.c "Were you being honest when you asked if you could help me?"
              wt_image b_clerk_hypno_2
              bree.c "Yes!  You're not most people.  I don't think you are, anyway."
              $ title = "How do you respond?"
              menu:
                  "Do you want to help or serve?":
                      player.c "Are you looking for someone to help, Bree?  Or are you looking for someone to serve?"
                      wt_image b_clerk_working_10
                      "She fidgets awkwardly before answering quietly."
                      wt_image b_clerk_working_14
                      bree.c "I'd like to serve.  If I could find the right man to serve."
                      "The look on her face makes it clear she's wondering if you might be that right man."
                      wt_image b_clerk_working_15
                      "Best to leave this lie for the moment.  She's made her interest clear.  If you intend to proceed, you should take things slowly."

                  "Do you want to help with my hard on?":
                      player.c "I do have a something you could help me with, Bree.  I've been hard ever since I walked in here and saw you again.  Would you like to help me with this problem?"
                      wt_image b_clerk_working_13
                      "Her face falls."
                      bree.c "I thought maybe you might want something more than just a quick fuck.  Silly me.  There's a washroom back there you can jerk off in, if you're that horny."
                      dismiss bree
                      wt_image current_location.image
                      rem tags 'submitting_now' from bree
                      "She makes herself scarce, avoiding contact with you until you leave the store."
                      call convert(bree,'unavailable') from _call_convert_46  ## WARNING: be very careful with this command as it deletes all of her tags, except for permanent story tags
                      #add tags 'lost' to bree
                      rem tags 'submitting_now' from bree
                  "That's enough for today":
                      wt_image b_clerk_working_10
                      player.c "Thank you Bree.  That's very kind.  I'll let you know if I think of anything."
                      wt_image b_clerk_working_15
                      "A small smile creeps onto her face."

          "Ask her to demonstrate the store's equipment":
              player.c "Please show me how some of these items work, Bree."
              wt_image b_clerk_working_10
              bree.c "I think they're all pretty self-explanatory."
              player.c "I was hoping for a personal demonstration.  By you."
              wt_image b_clerk_hypno_2
              "She fidgets uncomfortably for a moment before answering."
              bree.c "I don't think that's appropriate.  I don't even know you."

          "Nothing for today":
              wt_image b_clerk_working_10
              player.c "Not today, Bree.  Thank you.  I'll just take a look around."
              bree.c "Okay"

  elif bree.submit_count == 3:
      wt_image b_clerk_working_15
      player.c "Hello, Bree.  Your posture is good again today."
      wt_image b_clerk_working_3
      bree.c "Thank you"
      player.c "It could, however, be improved.  Are you willing to accept my instructions, Bree?"
      wt_image b_clerk_working_14
      "She nods, nervously."
      player.c "Good girl. You're wearing more clothes than I prefer a submissive to wear in my presence."
      wt_image b_clerk_working_10
      player.c "Please remove your top, bra and skirt, then wait here for me to finish my shopping.  I'll let you know if I need you for anything."
      wt_image b_clerk_hypno_2
      bree.c "Bree glances anxiously at the door.  The store is still open."
      player.c "You may hold your breasts in your hands while I shop.  Anyone coming in will see no more than they would if you were at the beach."
      wt_image b_clerk_working_4
      "Bree nods, and lifts up her top."
      wt_image b_clerk_working_5
      "She sneaks a peek as she removes her bra.  If she was hoping to see approval on your face, she's disappointed."
      wt_image b_clerk_working_18
      "Stoically, you keep your face expressionless as she undresses.  It won't do to let a sub girl think she can impress you simply by flashing her breasts."
      wt_image b_clerk_working_6
      "She lowers her gaze as she finishes stripping to her panties.  As you suggested, she holds her breasts in her hands to protect her modesty from anyone who enters the store."
      player.c "Good girl.  You can go back to your work when I leave."
      $ bree.change_image('b_clerk_working_6')

  elif bree.submit_count == 4:
      wt_image b_clerk_working_6
      player.c "You addressed me when I entered the store.  Did I tell you you could speak, girl?"
      wt_image b_clerk_working_18
      "Bree shakes her head."
      player.c "From now on, you don't speak unless I give you permission.  Is that understood?"
      wt_image b_clerk_working_6
      "She nods, biting her lip with nervous excitement.  You look around at the sight lines in the store."
      player.c "Follow me into the change room."
      wt_image b_clerk_working_20
      player.c "Remove your panties and kneel down."
      wt_image b_clerk_working_22
      "Head bowed, Bree does as you say."
      wt_image b_clerk_working_7
      player.c "From the door, when you're kneeling only your top half is visible.  If someone else comes in, you can duck into the change booth and dress.  Otherwise, you'll wait here.  I'll tell you if I need you.  You may dress and return to your work when I leave."
      $ bree.change_image('b_clerk_working_7')

  elif bree.submit_count == 5:
      wt_image b_clerk_head_bowed_1
      "Bree waits silently for your instructions."
      wt_image b_clerk_working_22
      "You pat her gently on the head and she sighs contentedly."
      wt_image b_clerk_working_7
      "You can try taking her submission deeper next time.  For today, it's enough to have her prove she's learned your previous lesson about waiting silently until she's called upon."

  else:
      wt_image b_clerk_working_7
      "Bree waits silently for your instructions."
      $ title = "What do you want to do?"
      menu:
          "Take out your cock":
              call bree_takeoutcock from _call_bree_takeoutcock

          "Ask about limits" if not bree.asked_limits:
              wt_image b_clerk_head_bowed_1
              player.c "Tell me, girl.  You're an experienced submissive, I believe?"
              wt_image b_clerk_working_22
              bree.c "Somewhat, [bree.your_respect_name].  I've played with a number of Doms.  I haven't found the right one, yet."
              player.c "From what you've learned about yourself, what are your limits?"
              wt_image b_clerk_head_bowed_1
              "Bree pauses a moment to collect her thoughts."
              wt_image b_clerk_working_22
              bree.c "No markings, [bree.your_respect_name].  Not unless or until I was in a committed relationship.  No cutting.  No children or animals, obviously."
              wt_image b_clerk_working_7
              bree.c "I have a conflicted relationship with pain.  I'm not a masochist, I don't get off on pain.  But if you enjoy hurting me, I would enjoy pleasing you, if that makes any sense."
              wt_image b_clerk_working_22
              bree.c "No face slapping, though.  That feels like abuse, not submission to me."
              $ bree.asked_limits = True
              $ title = "What do you do?"
              menu:
                  "Take out your cock":
                      call bree_takeoutcock from _call_bree_takeoutcock_1

                  "Invite her to your house (sends you home)" if bree.tookoutcock:
                      call bree_date from _call_bree_date

                  "Slap her face":
                      wt_image b_clerk_slap_1
                      "Before she can react, you reach out and slap Bree hard across the face. Tears spring immediately to her eyes as she looks at you in pain and disbelief."
                      player.c "I don't accept limits from subs, Bree.  Especially silly limits."
                      wt_image b_clerk_angry_1
                      "She grabs her clothes and starts to dress, stopping only long enough to give you the finger."
                      bree.c "Get the fuck out of my store, you jerk, before I call the cops!"
                      $ player.add_tags('tst_barred')
                      call forced_movement(downtown) from _call_forced_movement_74
                      "You can hear Bree still screaming at you as she locks the door behind you."
                      bree.c "Asshole!!!"

                  "Nothing more for today":
                      wt_image b_clerk_head_bowed_1
                      player.c "Thank you.  That'll be all for today.  Stay here while I shop.  If I need you, I'll let you know.  You may go back to your work when I leave."
                      wt_image b_clerk_working_7
                      "Bree nods contentedly."
                      $ bree.change_image('b_clerk_working_7')

          "Fuck her" if bree.tookoutcock and bree.asked_limits:
              $ bree.storefuck = True
              wt_image current_location.image
              "You lock the door and put up the 'Back Soon' sign. Then you return to Bree."
              wt_image b_clerk_sex_1
              "Standing her up, you lift one leg to give you easy access.  She's already wet, and moans softly as you slide into her."
              bree.c "oohhh"
              wt_image b_clerk_sex_7
              "She clearly enjoys being of service like this.  She closes her eyes as you fuck her ..."
              wt_image b_clerk_sex_2
              "... and as she gets close to orgasm, shoves a finger in her ass.  That takes her over the edge, as she shudders and cries out."
              bree.c "OOHHHH!!"
              wt_image b_clerk_sex_8
              player.c "[player.orgasm_text]"
              wt_image b_clerk_working_21
              "You pat her head as you dress.  You should probably teach her not to touch herself when she's pleasuring you, but otherwise she did fine.  She's definitely trainable."
              $ bree.change_image('b_clerk_sex_9')
              $ bree.description = "Bree kneels on the floor, savoring the feel of your cum dripping out of her pussy."
              rem tags 'submitting_now' from bree
              $ bree.orgasm_count += 1
              $ bree.sex_count += 1
              orgasm notify

          "Fuck her ass" if bree.tookoutcock and bree.asked_limits and bree.storefuck:
              wt_image current_location.image
              "You lock the door and put up the Back Soon sign. Then you return to Bree."
              wt_image b_clerk_anal_7
              "She's demonstrated a willingness to stick her own fingers up her butt, so you're not surprised that she offers no objection as you position yourself at her rear entrance ..."
              wt_image b_clerk_anal_8
              "... and push yourself inside."
              bree.c "oohhh"
              wt_image b_clerk_anal_2
              "She reaches a hand between her legs and plays with herself as you fuck her ass ..."
              wt_image b_clerk_anal_9
              "... making you wonder which of you'll cum first?"
              wt_image b_clerk_anal_10
              "To slow her down, you pull her down on top of you ..."
              wt_image b_clerk_anal_11
              "... making her do the work of riding you."
              wt_image b_clerk_anal_3
              "Despite that, she still cums first.  Barely."
              bree.c "OOHHHH!!"
              player.c "[player.orgasm_text]"
              wt_image b_clerk_anal_12
              "You pat her head as you dress.  You should probably teach her not to touch herself, but her ability to cum with your cock in her ass makes you think controlling her pleasure response will always be a challenge."
              $ bree.change_image('b_clerk_anal_12')
              $ bree.description = "Bree kneels on the floor, savoring the feel of your cum dripping out of her ass."
              rem tags 'submitting_now' from bree
              $ bree.orgasm_count += 1
              $ bree.anal_count += 1
              orgasm notify

          "Invite her to your house (sends you home)" if bree.asked_limits and bree.tookoutcock and bree.date_count != 4:
              call bree_date from _call_bree_date_1

          "Talk about becoming your slave (sends you home)" if bree.date_count == 4:
              player.c "Bree, I believe you've enjoyed our time together.  In fact, I believe you've been thinking about what it would be like if we formed a deeper relationship.  Am I right?"
              wt_image b_clerk_working_22
              "She nods her head, and you think she's holding her breath in anticipation of what you may say next."
              player.c "There are a few things you must know."
              wt_image b_clerk_head_bowed_1
              player.c "First, if I take you as my slavegirl, that is the exact role you will have in my life.  A slave.  That is to say, a possession.  An item of property for me to use as I please."
              player.c "Second, I will not be exclusive to you.  There are other women in my life, and that will remain the case.  I will sleep with other women when and as I choose."
              player.c "I will keep you safe by protecting myself and you from communicable diseases. But if you think you will be jealous, this will not be the right situation for you."
              player.c "Third, as my property, I will protect you and keep you safe.  But I will also use you as I see fit."
              player.c "And I may choose to use you with other people, or even lend you to others from time to time.  Men or women. If I do, you will be required to obey them as you do me."
              player.c "This is not a decision to be made lightly.  I don't expect an answer right now.  Take your time.  If you have any questions, you may ask them now."
              wt_image b_clerk_hypno_3
              bree.c "I don't need any time, [bree.your_respect_name].  And I don't have any questions.  I accept your offer.  I want to belong to you."
              bree.c "I agree that you may do with me whatever you want, even lend me out if that pleases you."
              bree.c "And I'll try very hard, [bree.your_respect_name], not to be jealous of the other women in your life.  I don't think I can promise anything more on that front other than that I will try.  And if I fail, I hope you'll punish me and train me not to be jealous."
              "You nod."
              wt_image b_clerk_head_bowed_1
              player.c "Very well, girl.  Then I have a test for you today, to see if this can work.  When you finish your shift, you'll come to my house.  I won't be alone.  I'll be with another woman."
              wt_image b_clerk_working_22
              player.c "You'll serve me while she watches, you'll watch while I have sex with her, and if it amuses me, I'll have you serve her.  If after that you still feel as you do now, I'll accept you as my slavegirl."
              wt_image b_clerk_hypno_3
              bree.c "Yes, [bree.your_respect_name].  Thank you, [bree.your_respect_name]!!  I'll be there."
              call forced_movement(living_room) from _call_forced_movement_75
              summon bree
              wt_image b_clerk_test_1
              "Elaine and you are already naked when Bree arrives. At your command, Bree strips too. Once Bree is naked, Elaine goes and stands beside her."
              elaine "So, you think you want to be his slavegirl?"
              wt_image b_clerk_test_2
              elaine "Come on, then.  Let's see how useful you are with your mouth."
              wt_image b_clerk_test_3
              "You don't play with Elaine very often.  She's a no nonsense, take charge kind of gal, though, when it comes to other women.  You knew she'd be a good test, to see if Bree could really be happy in your lifestyle."
              wt_image b_clerk_test_4
              elaine "Come on, you can do better than that.  Push out your tongue and your lips.  Get your teeth out of the way.  He wants to fuck your mouth, not your incisors."
              wt_image b_clerk_test_5
              elaine "That's enough."
              "Elaine roughly pulls Bree's mouth off your cock."
              elaine "Thanks for getting him hard, little slavegirl.  I'm going to enjoy riding that nice thick cock you've worked up on him."
              wt_image b_clerk_test_6
              "As you enter Elaine, she pulls out a butt plug, and starts jamming it in and out of Bree's ass."
              elaine "God that feels good!  You did such a nice job getting him hard for me, I should reward you.  Stick out that ass, slavegirl.  I have a present for you."
              wt_image b_clerk_test_7
              "Elaine shifts on top of you and directs Bree to kneel in front of her."
              elaine "That's it, lick his balls, slavegirl.  You want your owner to enjoy fucking other women, don't you?"
              wt_image b_clerk_test_8
              "Bree doesn't shy away.  In fact, you catch her playing with herself as she licks you.  You let it pass for today, but after she becomes your slavegirl, you'll decide when and how her pussy gets touched."
              wt_image b_clerk_test_10
              elaine "Mmmmm  ... make me cum while your owner fucks my ass, slavegirl ...  AAAOOOOOO!!!!"
              wt_image b_clerk_test_11
              elaine "Now him."
              player.c "[player.orgasm_text]"
              wt_image b_clerk_test_9
              "After you and Elaine are finished, Bree prostrates herself on the floor in front of you."
              bree.c "[bree.your_respect_name], may I have permission to speak?"
              "You nod."
              bree.c "[bree.your_respect_name], if you will have me, I still want to be owned by you."
              $ title = "Do you take her as your slavegirl?"
              menu:
                  "Yes":
                      player.c "Yes, girl, I will have you.  Go to the bedroom and wait for me.  I'll call on you when it's time for your real training to begin."
                      call bree_convert_slavegirl from _call_bree_convert_slavegirl
                  "No":
                      player.c "No, girl.  I won't.  Our time together ends now."
                      wt_image b_clerk_looking_up
                      "Bree looks at you in disbelief.  When she sees you're serious, she gets up and gathers her clothes.  Tears streaming down her face, she flees your house as fast as she can."
                      wt_image current_location.image
                      "You never see her again.  Whether she quits her job and leaves town, or just becomes very good at avoiding you, you never learn."
                      call convert(bree,'unavailable') from _call_convert_47  ## WARNING: be very careful with this command as it deletes all of her tags, except for permanent story tags
              orgasm
              change player energy by -energy_short notify
              call character_location_return(bree) from _call_character_location_return_210

  return

# Take out cock during store sex
label bree_takeoutcock:
  $ bree.tookoutcock = True
  wt_image b_clerk_working_8
  "You put a 'Back Soon' sign on the store door, then take off your clothes and present your cock to the kneeling Bree. She looks somewhat surprised, but doesn't object."
  $ title = "What do you want?"
  menu:
      "Blow job":
          wt_image b_clerk_bj_1
          "Bree opens her mouth and begins to gently lick the underside of your cock.  Cutely, she rubs herself between her legs as she licks."
          wt_image b_clerk_bj_2
          "You let her lick you tenderly for a few minutes, then place your hand on the back of her head and guide her onto your shaft."
          wt_image b_clerk_bj_3
          "As the pressure in your balls mounts, you move her head faster and faster along your cock.  Eventually you grip her firmly and hold her head still as you thrust harder and harder between her lips."
          wt_image b_clerk_bj_13
          "As you cum, you hold her head in place, letting each spurt empty into her warm mouth."
          "[player.orgasm_text]"
          wt_image b_clerk_working_9
          player.c "Good girl."
          "You pat her head as you dress.  You should probably teach her not to touch herself when she's pleasuring you, but otherwise she did fine.  She's definitely trainable."
          $ bree.change_image('b_clerk_working_9')
          $ bree.description = "Bree kneels on the floor, savoring the taste of your cum in her mouth."
          $ bree.blowjob_count += 1
          $ bree.swallow_count += 1

      "Tit job":
          wt_image b_clerk_breast_job_1
          "Bree places your cock between her breasts, then squeezes them tight."
          wt_image b_clerk_breast_job_2
          "She keeps her head bowed, watching your cock as you thrust up and down against her soft, warm mounds."
          wt_image b_clerk_breast_job_3
          "As your balls reach the boiling point, you turn her sideways, and release your seed across her beautiful chest.  Cutely, she plays with herself as your cum splatters on her."
          "[player.orgasm_text]"
          wt_image b_clerk_breast_job_4
          player.c "Good girl."
          "You pat her head as you dress.  You should probably teach her not to touch herself when she's pleasuring you, but otherwise she did fine.  She's definitely trainable."
          $ bree.change_image('b_clerk_breast_job_4')
          $ bree.description = "Bree kneels on the floor, savoring the feeling of your cum on her chest."
          $ bree.titfuck_count += 1

  rem tags 'submitting_now' from bree
  orgasm notify

  return

# Training Dates
label bree_date:
    player.c "Bree, I'd like you to visit me at my house.  Will you join me there after your work is done?"
    wt_image b_clerk_working_22
    "She nods, perhaps a little too eagerly."
    $ bree.date_count += 1
    $ player.submission_action_count += 1
    call forced_movement(living_room) from _call_forced_movement_76
    summon bree

    if bree.date_count == 1:
        wt_image b_clerk_date_1_1
        'Bree arrives for your "date" in a beautiful body hugging outfit that shows off her gorgeous curves. Silently you take in the view as she watches you nervously.'
        wt_image b_clerk_date_1_3
        "She can tell you're impressed, but you're careful not to let her know just how impressed. Obediently, she waits quietly, not saying anything until you give her permission."
        wt_image b_clerk_date_1_1
        player.c "Remove your clothes.  Keep the stockings and shoes on.  Then kneel down, head on the floor."
        wt_image b_clerk_date_1_4
        "Bree quickly complies, happy that you want to see more of her body."
        wt_image b_clerk_date_1_5
        player.c "Stay in that position for the next two hours.  I recommend you shift your body weight to your arms.  It'll help keep the position from becoming too uncomfortable."
        wt_image b_clerk_date_1_2
        "You go about your business, stepping around and over the woman kneeling on your floor.  You use the opportunity to observe her from every angle, but you do not touch her."
        wt_image b_clerk_date_1_9
        "When the two hours are up, you stand beside Bree and give her permission to shift her aching limbs."
        player.c "Is submission about whips and chains and leather, Bree?"
        wt_image b_clerk_date_1_7
        bree.c "No, [bree.your_respect_name]."
        player.c "Then what is submission?"
        "She thinks for a moment before answering."
        bree.c "Submission is giving up control.  It's letting someone else decide what you do and what is done to you."
        player.c "Did you enjoy our time together this afternoon?"
        "Bree collects her thoughts before replying."
        wt_image b_clerk_date_1_6
        bree.c "[bree.your_respect_name], may I ask a question before I answer you?"
        player.c "Yes, go ahead."
        bree.c "Did you enjoy having me kneel on your floor this afternoon?"
        player.c "Yes, girl, I did."
        wt_image b_clerk_date_1_8
        bree.c "Then I enjoyed our time together."
        "You stand her up, supporting her until she can get her legs underneath her."
        wt_image b_clerk_date_1_3
        "After she dresses, you get her a glass of water, then send her home."
        player.c "I'll look forward to seeing you at the store again, Bree."
        bree.c "So will I, [bree.your_respect_name]!"
        change player energy by -energy_short

    elif bree.date_count == 2:
        wt_image b_clerk_date_2_1
        "Bree arrives for your second date much more down dressed than the first.  Perhaps she thinks if she looks more available, you'll avail yourself of more of her than you did the last time."
        player.c "Hello, Bree.  Please lower your top."
        wt_image b_clerk_date_2_2
        player.c "Thank you.  Now, take the top off all the way and remove your pants too.  Once you're finished undressing, kneel."
        wt_image b_clerk_date_2_3
        "You catch her glancing at you as she undresses, looking for signs of approval.  You ignore her for the moment.  There'll be plenty of time later to demonstrate how much she pleases you."
        wt_image b_clerk_date_2_4
        "For now, you want to know whether she can enjoy submission simply for its own sake, devoid of sex, spankings, and the trappings of BDSM."
        player.c "Take your hands out of your panties.  You will not touch yourself without permission.  Place your hands on the floor in front of you."
        wt_image b_clerk_date_2_5
        player.c "Better.  Turn around, still on your knees."
        wt_image b_clerk_date_2_6
        player.c "Head on the floor, bottom up, then look at me."
        wt_image b_clerk_date_2_7
        player.c "Which of your holes are available for my use, girl?"
        bree.c "All of them, [bree.your_respect_name]."
        wt_image b_clerk_date_2_14
        player.c "Remove your panties and show me."
        wt_image b_clerk_date_2_15
        player.c "That looks like you expect me to work for access to your holes.  Do you expect me to have to earn access?"
        bree.c "No, [bree.your_respect_name]"
        wt_image b_clerk_date_2_16
        "She rolls onto her back and lifts her legs."
        player.c "And still your legs are closed."
        wt_image b_clerk_date_2_8
        player.c "Better.  Hold that position until I decide what I want to do with you."
        "You leave her there.  Five minutes later, you return with a pillow that you slide under her lower back to support her neck.  Then you go about your business."
        wt_image b_clerk_date_2_17
        "You don't ignore her, you regularly check her out from different angles.  But you don't speak to her, and you don't touch her."
        wt_image b_clerk_date_2_8
        "After an hour passes, you stand beside her."
        player.c "Very good, Bree.  You can get dressed now."
        wt_image b_clerk_date_2_9
        "The conflict is obvious on Bree's face as she dresses."
        player.c "Did you want to ask me something?"
        wt_image b_clerk_date_2_10
        bree.c "[bree.your_respect_name] ... did you not want to make use of me?"
        "You pause for a moment before replying."
        player.c "Bree, do you think I find you attractive?"
        wt_image b_clerk_date_2_1
        "She reflects for a moment on your behavior with her in the store."
        bree.c  "Yes, [bree.your_respect_name].  I think you find me attractive."
        wt_image b_clerk_date_2_11
        player.c "Do you think I'm unhappy with you?"
        bree.c "I hope not, [bree.your_respect_name]."
        wt_image b_clerk_date_2_1
        player.c "Don't worry.  When I'm unhappy with you, I'll tell you, plain and simple.  If you fail to please me in any way, I will tell you."
        "She nods."
        wt_image b_clerk_date_2_11
        bree.c "Thank you, [bree.your_respect_name]."
        player.c "So what do you think it means that I'm sending you home now?"
        "Bree thinks for a moment."
        wt_image b_clerk_date_2_12
        bree.c "Perhaps ... Perhaps you're showing me that you'll have sex with me when you want to have sex with me, and not necessarily when I'm hoping you'll have sex with me?"
        "You smile."
        player.c "I'll see you at the store, Bree."
        wt_image b_clerk_date_2_13
        bree.c "Yes, [bree.your_respect_name].  I look forward to it!"
        change player energy by -energy_short

    elif bree.date_count == 3:
        wt_image b_clerk_date_3_11
        "Bree shows up for your third date in a simple red dress.  No attempt to look sultry or 'available'.  Just stunning."
        wt_image b_clerk_date_3_1
        player.c "We're going to use my dungeon today."
        "Bree beams."
        call forced_movement(dungeon) from _call_forced_movement_77
        summon bree no_follows
        wt_image b_clerk_date_3_2
        "Bree is all smiles as you show her into your play room.  Nothing here scares here. Rather, she's clearly excited."
        wt_image b_clerk_date_3_17
        "You place a blindfold around her eyes ...."
        wt_image b_clerk_date_3_3
        "... then fasten her wrists behind her, and connect them to a pulley."
        wt_image b_clerk_date_3_4
        "As you raise her wrists, it forces her into a bent forward position.  You leave her like this."
        call forced_movement(living_room) from _call_forced_movement_411
        "For the next hour, you go about your business.  Then you return to check on her."
        call forced_movement(dungeon) from _call_forced_movement_412
        wt_image b_clerk_date_3_4
        $ bree.choice_needed = True
        while bree.choice_needed:
            $ title = "What do you do with her now?"
            menu:
                "That's enough for today" if bree.left_to_suffer:
                    $ bree.choice_needed = False
                    wt_image b_clerk_date_3_3
                    "You decide she's had enough.  As you lower her arms, lets out a small moan as the pressure is released and blood returns to previously constricted areas."
                    wt_image b_clerk_date_3_14
                    "She slumps to the floor, covered in her own drool.  You remove her blindfold and she blinks at the light. She looks at you briefly, then looks away."
                    bree.c "May I ask you something, [bree.your_respect_name]?"
                    player.c "Go ahead."
                    wt_image b_clerk_date_3_13
                    bree.c "Did you enjoy our time together today?"
                    player.c "Yes, Bree.  I did.  And you don't have to ask me that anymore.  I'll tell you if I'm ever not enjoying what you're doing for me."
                    wt_image b_clerk_date_3_1
                    "You let her clean herself up and tell her you'll see her soon.  She leaves happy."
                    change player energy by -energy_short

                "Leave her to suffer" if not bree.left_to_suffer:
                    $ bree.left_to_suffer = True
                    call forced_movement(living_room) from _call_forced_movement_413
                    "You continue to go about your business, checking in on her every few minutes, but saying nothing, and leaving her untouched."
                    call forced_movement(dungeon) from _call_forced_movement_414
                    wt_image b_clerk_date_3_12
                    "The strain on her shoulders after the first hour becomes quite uncomfortable.  She begins to emit small moans."
                    bree.c "nnnnn ... nnnnnn"
                    call forced_movement(living_room) from _call_forced_movement_415
                    "As the end of the second hour approaches, her moans are becoming louder and more frequent, and can be heard throughout the house."
                    call forced_movement(dungeon) from _call_forced_movement_416
                    wt_image b_clerk_date_3_10
                    "Drool is running from her mouth, drenching herself, as she can no longer focus on anything except trying to relieve the pain in her shoulders."
                    bree.c "NNNNN ... NNNNNNN"
                    "You can't safely leave her in this position much longer."

                "Leave her to suffer more" if bree.left_to_suffer and not bree.has_tag('date_3_suffered_more'):
                    add tags 'date_3_suffered_more' to bree
                    wt_image b_clerk_date_3_12
                    "Bree's shoulders are screaming at her now, and there's no position she can shift to make the pain go away, even briefly."
                    wt_image b_clerk_date_3_4
                    "She knows you're there, watching her suffer.  She starts to tremble, waiting for you to help her, release her, do anything other than just watch."
                    wt_image b_clerk_date_3_10
                    "Soon she bursts into tears from the frustration and pain."

                "Leave her there" if bree.has_tag('date_3_suffered_more'):
                    $ bree.choice_needed = False
                    wt_image b_clerk_date_3_18
                    bree.c "Mercy!  Mercy!  Release me.  Let me down!  Let me down!!!  I'm sorry, I can't do this.  I'm not the right sub for you.  Let me go!!"
                    wt_image b_clerk_date_3_13
                    "Unfortunately, things didn't work out between you and Bree.  You never again see her at the store.  Whether she moved, or was just very good at avoiding you, you never find out."
                    wt_image current_location.image
                    call convert(bree,'unavailable') from _call_convert_48  ## WARNING: be very careful with this command as it deletes all of her tags, except for permanent story tags
                    #$ bree.add_tags('lost')
                    $ player.submission_action_count -= 1
                    change player energy by -energy_short

                "Use her mouth":
                    $ bree.choice_needed = False
                    wt_image b_clerk_date_3_14
                    "You unhook Bree and pull off her blindfold.  As the pressure in her shoulders is released, she sinks to the ground in relief, covered in her own drool and blinking from the light."
                    wt_image b_clerk_date_3_15
                    "She understands your intent as you take her by the hair, and opens her mouth."
                    wt_image b_clerk_date_3_5
                    "Gripping her firmly by the back of the head, you guide her onto your hard cock and ease the full length of your shaft into her."
                    wt_image b_clerk_date_3_6
                    "She starts to gag as you reach the back of her throat, then catches herself, and relaxes enough for you to push her head right down to your balls. You hold her there, as she tries her best to suck on you."
                    wt_image b_clerk_date_3_15
                    "The sensation is incredible.  When you can hold back no longer, you pull her head off of your cock ..."
                    wt_image b_clerk_date_3_16
                    "... and shoot your load over her, covering her face with your hot jizz."
                    player.c "[player.orgasm_text]"
                    wt_image b_clerk_date_3_9
                    bree.c "Oh my god, [bree.your_respect_name]!  That was amazing!!"
                    "In her excitement, Bree forgets herself and speaks without permission.  You let it slide, this time."
                    wt_image b_clerk_date_3_1
                    "You let her clean herself up and tell her you'll see her soon.  She leaves happy."
                    change player energy by -energy_short
                    orgasm notify
                    $ bree.blowjob_count += 1
                    $ bree.facial_count += 1

                "Use her for sex":
                    $ bree.choice_needed = False
                    wt_image b_clerk_date_3_7
                    "You step behind Bree and lift her dress.  She moans as she feels you behind her, and not just because of the pain in her shoulders.  You don't need to check if she's wet.  You can smell her pussy juices as you position yourself."
                    wt_image b_clerk_date_3_8
                    bree.c "oooooooaaaaaggggg"
                    "Bree half moans, half screams as you enter her.  A few minutes later, half moans, half grunts start escaping from her mouth."
                    wt_image b_clerk_date_3_18
                    bree.c "Please, [bree.your_respect_name].  May I cum?  Please, may I cum [bree.your_respect_name]?"
                    "You haven't taught her to do that.  It must be something she's fantasized about.  That being the case, it's likely she enjoys the thought of being denied.  The two tend to go hand in hand."
                    wt_image b_clerk_date_3_8
                    player.c "Not yet"
                    "She struggles to hold back her orgasm as you fuck her, but that's a battle she quickly loses."
                    wt_image b_clerk_date_3_18
                    bree.c "Please ... please ... please ..."
                    wt_image b_clerk_date_3_12
                    "She tries to control her body by focusing on the pain in her shoulders instead of the burning between her legs, but that only helps her so long."
                    wt_image b_clerk_date_3_18
                    bree.c "PLEASE!  PLEASE!  I'M BEGGING YOU!!  MAY I PLEASE CUM????"
                    "You know she can't hold back any longer."
                    wt_image b_clerk_date_3_8
                    player.c "Cum for me, girl.  Cum on my cock."
                    wt_image b_clerk_date_3_18
                    bree.c "OOOOOHHHHHHHH!!"
                    wt_image b_clerk_date_3_14
                    "As the orgasm sweeps over her, its everything you can do hold back your own.  You pull out and unhook her.  As she slumps to the floor, covered in her own drool and sweat, you pull off the blindfold and she blinks in the light."
                    wt_image b_clerk_date_3_16
                    "Grabbing her by the hair, you position her face to receive the hot load of cum that has been building inside you.  Instinctively, she opens her mouth."
                    player.c "[player.orgasm_text]"
                    wt_image b_clerk_date_3_9
                    bree.c "Oh my god, [bree.your_respect_name]!  That was amazing!!"
                    "In her excitement, Bree forgets herself and speaks without permission.  You let it slide, this time."
                    wt_image b_clerk_date_3_1
                    "You let her clean herself up and tell her you'll see her soon.  She leaves happy."
                    $ bree.sex_count += 1
                    $ bree.orgasm_count += 1
                    change player energy by -energy_short
                    orgasm notify

    else:
        "You instruct Bree to wear something classy for your 'date'."
        call forced_movement(dungeon) from _call_forced_movement_417
        summon bree no_follows
        wt_image b_clerk_date_4_1
        "It's the first time you've told her what to wear.  She looks nervous when she arrives, worried about whether her choice of clothes will meet with your approval.  You spend a few minutes looking her over."
        player.c "Very nice.  Kneel and place your hands on your legs."
        wt_image b_clerk_date_4_2
        "You can see the tension release from her body at the knowledge that her choice has pleased you.  She sinks to the floor, half contented, half nervous about what you have in store."
        player.c "Lean forward.  Place your head on the floor and your hands out in front of you."
        wt_image b_clerk_date_4_3
        "She does as you instruct.  You spend a few minutes enjoying the sight of her before you continue."
        player.c "When I asked you about your limits, you told me that if I enjoyed hurting you, you would enjoy pleasing me in that way.  I'm going to hurt you today, Bree.  Do you consent?"
        wt_image b_clerk_date_4_4
        "She nods. You pull up to her knees and tie ropes around each wrist.  She nuzzles back against you, breathing hard from the excitement of your touch and anticipation of what comes next."
        wt_image b_clerk_date_4_5
        "You position her over the table and remove her panties.  The ropes from each wrist you loop around her thighs, and then tie off.   You wrap another rope around her ankles and fasten it to the far end of the table.  She cannot stand, she cannot roll off, and she cannot protect her bottom in any way.  Her ass is now yours to do with as you please."
        $ title = "What do you punish her with?"
        menu:
            "Your hand":
                "You spank Bree with your bare hand.  You start the spanking slow *smack* *smack* *smack*..."
                wt_image b_clerk_date_4_6
                "... then work up to hard steady smacks that soon have her calling out in pain. *SMACK*  *SMACK*  *SMACK*"
                bree.c "OOWWWW!!!!"

            "Purchases from The Steel Trap" if dungeon.has_item(floggers):
                "You begin beating Bree with some of the instruments you purchased from the store she works at."
                wt_image b_clerk_date_4_11
                "You start with a paddle ... *smack*  *smack*  *smack*"
                wt_image b_clerk_date_4_12
                "... then work up to something decidedly more painful ... *thwappp*  *thwappp*  *thwappp*."
                wt_image b_clerk_date_4_6
                "It doesn't take long before Bree's screaming at the top of her lungs."
                bree.c "AAAHHHOOWWWW!!!!"

        $ title = "Gag her?"
        menu:
            "No":
                "You listen to Bree cry out as you beat her ass."
                bree.c "OOWWW!!!  OOOWWW!!!!  OOOWWWW!!!!!"

            "Yes" if dungeon.has_item(gags):
                add tags 'gagged_now' to bree
                wt_image b_clerk_gag_1
                "You take one of the gags you bought from Bree's store and place it in her mouth."
                wt_image b_clerk_gag_3
                "You continue to beat her in relative silence as the ball gag muffles her screams.  All you can hear is a loud 'Mmmmppphhh ... Mmmmmppphhh' after each new blow lands."
                wt_image b_clerk_date_4_7
                "Soon Bree's drool is flowing over the ball gag and down the side of her face as she breathes heavily, trying to deal with the pain you're inflicting."

        wt_image b_clerk_date_4_8
        "Once Bree's ass is a consistent, glowing shade of red, you stop.  It wouldn't do to leave marks, not at this point anyway."

        if bree.has_tag('gagged_now') and dungeon.has_item(fuck_machine):
            $ title = "Do you want to put Bree on the fuck machine?"
            menu:
                "No":
                    pass

                "Yes":
                    wt_image b_clerk_gag_2
                    "You pull Bree up and make sure her gag is firmly in place.  This is about to get noisy enough, even with the gag."
                    wt_image b_clerk_date_4_9
                    "Taking some nipple clamps, you attach them to her sensitive buds.  She'll need the distraction in a moment."
                    wt_image b_clerk_date_4_14
                    "Then you put her in position over the fuck machine and turn it on.  It doesn't take her long to cum."
                    bree.c "mmmpphhh"
                    "When she does, you increase the speed.  She cums again and again.  After each orgasm, you increase the speed at which the automated vibrator slams into her."
                    bree.c "MMMPPHHH  ...  MMMMPPPHHHH"
                    wt_image b_clerk_date_4_10
                    "Soon she's digging her fingers into her own skin and frothing at the mouth, her eyes rolling back in her head as she experiences the best-worst fifteen minutes of her life."
                    bree.c "MMMPPHHH  ...  MMMMPPPHHHH"
                    $ bree.orgasm_count += 5

        $ title = "What do you do with her now?"
        menu:
            "Fuck her mouth":
                wt_image b_clerk_bj_4
                "You grip Bree firmly by the hair and pull her mouth onto your cock.  It only takes a moment before you shoot your load down the back of her throat."
                player.c "[player.orgasm_text]"
                $ bree.blowjob_count += 1
                $ bree.swallow_count += 1
                orgasm

            "Fuck her ass":
                wt_image b_clerk_anal_5
                "You re-tie Bree into a more comfortable position for you ..."
                wt_image b_clerk_anal_6
                "... then you pound into her tight ass to the sound of her moaning on every thrust."
                wt_image b_clerk_anal_1
                "When you can hold back no longer, you release your seed deep inside her."
                player.c "[player.orgasm_text]"
                $ bree.anal_count += 1
                orgasm

            "That's enough for today":
                if bree.has_tag('gagged_now'):
                    wt_image b_clerk_date_4_7
                else:
                    wt_image b_clerk_date_4_6
                "You give Bree a chance to recover before untying her and helping her to her feet."

        wt_image b_clerk_date_4_13
        "Once she's pulled herself together, Bree looks like she has something she wants to say."
        player.c "Go ahead."
        bree.c "No one has ever made me feel like that before, [bree.your_respect_name]."
        "If she was interested in you before, she's totally smitten now."
        rem tags 'gagged_now' from bree
        change player energy by -energy_short
        if player.short_name == 'nd':
            "You need to think long and hard about whether to continue this.  You started this new life to avoid the complications that come with taking care of a slavegirl."
            "On the other hand, you've grown tremendously over the past few weeks.  You're not the same man you were when you came here."
            "Perhaps you are ready to risk heartache again for the right slavegirl.  Is Bree the right one for you?  You'll need to think about that before the next time you see her."

    call character_location_return(bree) from _call_character_location_return_211
    wt_image current_location.image
    notify
    return

# Ask Her About Nipple Clips
label bree_ask_about_nipple_clips:
    player.c "Do you have any clip on nipple jewelry?  Something slutty, like a whore would wear?"
    bree.c "Not really. Just some toy stuff that doesn't look very good. Our customers go in for real nipple jewelry, the piercing stuff."
    "You're not ready to get Jasmine's nipples pierced. That requires a trip to a professional shop, and you need to break her resistance down yourself, first. Perhaps there's another store you could check?"
    add tags 'discussed_jasmine_nipple_clips' to bree
    return


## Slavegirl Actions
# Rename Her
label bree_rename:
    wt_image bree.image
    "As her owner, it's your prerogative to change [bree.full_name]'s name, if you want to."
    $ title = "Do you want to change her name?"
    menu:
        "Yes":
            call bree_rename_change from _call_bree_rename_change
        "No":
            pass
    return

label bree_rename_change:
    $ title = "What would you like her name to be?"
    $ bree.name = renpy.input(_("What is her new name?"))
    $ bree.suffix = renpy.input(_("What is her new title, if you want to give her one?"))
    $ title = "Does she get a prefix?"
    menu:
        "Yes":
            $ bree.prefix = renpy.input(_("What is her prefix?"))
        "No":
            $ bree.prefix = ""
    $ bree.change_full_name(bree.prefix, bree.name, bree.suffix)
    $ title = "Are you sure you want her new name to be [bree.full_name]?"
    menu:
        "Yes":
            pass
        "No, choose something else":
            jump bree_rename_change
    return

# Tell her how to address you
label bree_your_name:
    "[bree.name] currently refers to you as '[bree.your_respect_name]'."
    $ title = "Change how she should address you?"
    menu:
        "Yes":
            call bree_your_name_change from _call_bree_your_name_change
        "No":
            pass
    return

label bree_your_name_change:
    $ title = "How should she address you?"
    $ bree.your_respect_name = renpy.input(_("How should she address you?"))
    $ title = "Are you sure you want her to call you '[bree.your_respect_name]'?"
    menu:
        "Yes":
            pass
        "No, choose something else":
            jump bree_your_name_change
    return


# Choose her position
label bree_choose_position:
    wt_image bree.image
    $ title = "What position do you want [bree.name] to adopt while she waits for you?"
    menu:
        "Her current position is fine":
            pass
        "Relaxed" if bree.position != 1:
            $ bree.position = 1
            $ bree.change_image('b_clerk_position_1')
            wt_image b_clerk_position_1
            "You tell [bree.name] she can dress and relax. She only needs to kneel and present herself when you come into the room."
            jump bree_choose_position
        "Kneeling palms up" if bree.position != 2:
            $ bree.position = 2
            $ bree.change_image('b_clerk_position_2')
            wt_image b_clerk_position_2
            "You tell [bree.name] to kneel and wait for you with her hands on knees, palms facing up."
            jump bree_choose_position
        "Kneeling hands behind head" if bree.position != 3:
            $ bree.position = 3
            $ bree.change_image('b_clerk_position_3')
            wt_image b_clerk_position_3
            "You tell [bree.name] to kneel and wait for you with her hands behind her head."
            jump bree_choose_position
        "Kneeling head on floor" if bree.position != 4:
            $ bree.position = 4
            $ bree.change_image('b_clerk_position_4')
            wt_image b_clerk_position_4
            "You tell [bree.name] to kneel and wait for you with her head on the floor, hands stretched out in front of her."
            jump bree_choose_position
        "Tie her in place" if bree.position != 5:
            $ bree.position = 5
            $ bree.change_image('b_clerk_position_5')
            wt_image b_clerk_position_5
            "You position [bree.name] kneeling with her back against a cot, pull her arms back behind her and lash her in place.  She'll wait for you like this until you're ready for her."
            jump bree_choose_position
        "Forced deep throat" if bree.has_tag('master_m_visit') and bree.position != 6:
            "Her time with Master M has given you an idea for a new position for her to hold."
            wt_image b_clerk_bound_1
            "You lock [bree.name] in place ..."
            wt_image b_clerk_position_6
            "... and impale her mouth on a dildo.  She'll wait for you like this until you're ready for her."
            $ bree.position = 6
            $ bree.change_image('b_clerk_position_6')
            jump bree_choose_position
    return

# Provide Rules
label bree_provide_rules:
    wt_image bree.image
    "[bree.talk_rules] [bree.cum_rules]"
    $ title = "What rules should she be following?"
    menu:
        "Her current rules are fine":
            pass
        "Allow her to talk" if not bree.has_tag('allowed_to_talk'):
            $ bree.add_tags('allowed_to_talk')
            $ bree.talk_rules = "She is allowed to talk."
            jump bree_provide_rules
        "No talking without permission" if bree.has_tag('allowed_to_talk'):
            rem tags 'allowed_to_talk' from bree
            $ bree.talk_rules = "She is not allowed to talk without permission."
            jump bree_provide_rules
        "Allow her to have orgasms" if not bree.has_tag('allowed_to_cum'):
            if bree.has_tag('allowed_to_beg'):
                rem tags 'allowed_to_beg' from bree
            $ bree.add_tags('allowed_to_cum')
            $ bree.cum_rules = "She is allowed to orgasm."
            jump bree_provide_rules
        "Allow her to beg for orgasms" if not bree.has_tag('allowed_to_beg'):
            if bree.has_tag('allowed_to_cum'):
                rem tags 'allowed_to_cum' from bree
            $ bree.add_tags('allowed_to_beg')
            $ bree.cum_rules = "She is allowed to beg for orgasms."
            jump bree_provide_rules
        "No orgasms" if bree.has_tag('allowed_to_cum') or bree.has_tag('allowed_to_beg'):
            if bree.has_tag('allowed_to_cum'):
                rem tags 'allowed_to_cum' from bree
            if bree.has_tag('allowed_to_beg'):
                rem tags 'allowed_to_beg' from bree
            $ bree.cum_rules = "She is not allowed to have orgasms."
            jump bree_provide_rules
    return

# Deal With Her Bad Habit
label bree_bad_habit_training:
    $ bree.training_session()
    add tags 'bad_habit_trained_this_week' to bree
    if bree.bad_habit_status == 0:
        wt_image b_clerk_bj_train_1_1
        player.c "[bree.name], come over here and blow me."
        if bree.has_tag('allowed_to_talk'):
            bree.c "Yes, [bree.your_respect_name].  Thank you, [bree.your_respect_name]!"
        else:
            "Silently she moves into position."
        wt_image b_clerk_bj_train_1_2
        player.c "That's not where your hand belongs."
        bree.c "I'm sorry, [bree.your_respect_name]."
        "She puts her right hand on your cock and starts stroking it as she blows you, but leaves her left hand in place between her legs."
        player.c "I didn't mean that hand."
        bree.c "[bree.your_respect_name]?"
        "She seems genuinely unaware that she's touching herself as she blows you. Maybe she's been doing this since the first time she blew a guy, and it's become an ingrained habit she doesn't even think about."
        $ title = "What do you do?"
        menu:
            "Accept her little quirk":
                $ bree.bad_habit_status = 4
                "There are worse things in the world than a slavegirl who touches herself instinctively when she services you. You decide to ignore her little quirk and enjoy the pleasure her mouth brings you."
                wt_image b_clerk_bj_train_1_3
                player.c "[player.orgasm_text]"

            "Teach her to leave her pussy alone when she's serving you":
                player.c "When you blow me, the only thing you are to pay attention to is my cock.  Not your pussy.  Turn around."
                wt_image b_clerk_bj_train_1_4
                "You bind her arms behind her back."
                player.c "Now, let's see you blow me without touching yourself."
                wt_image b_clerk_lw_visit_3
                "She does a good job, the ropes preventing her from reaching her sex as she pleasures you. Hopefully that will break her of her bad habit."
                player.c "[player.orgasm_text]"
                $ bree.bad_habit_status = 1
                $ player.submission_action_count += 1

    elif bree.bad_habit_status == 1:
        wt_image b_clerk_bj_train_1_1
        player.c "[bree.name], come over here and blow me."
        if bree.has_tag('allowed_to_talk'):
            bree.c "Yes, [bree.your_respect_name].  Thank you, [bree.your_respect_name]!"
        else:
            "Silently she moves into position."
        "As soon as her tongue touches your cock, her hand slips between her legs."
        $ title = "What do you do?"
        menu:
            "Accept her little quirk":
                $ bree.bad_habit_status = 4
                "There are worse things in the world than a slavegirl who touches herself instinctively when she services you. You decide to ignore her little quirk and enjoy the pleasure her mouth brings you."
                wt_image b_clerk_bj_train_1_3
                player.c "[player.orgasm_text]"

            "Teach her to leave her pussy alone when she's serving you":
                player.c "Who owns you?"
                bree.c "You do, [bree.your_respect_name]"
                player.c "What do I own of you?"
                bree.c "All of me, [bree.your_respect_name]"
                player.c "Those hands, do they belong to me?"
                bree.c "Yes, [bree.your_respect_name]"
                player.c "That pussy, is that mine?"
                bree.c "Yes, [bree.your_respect_name]"
                player.c "Did I tell you that I want those hands touching that pussy?"
                "She blushes."
                bree.c "No, [bree.your_respect_name]"
                player.c "Then you don't deserve the freedom to move those hands until you learn to use them only as I instruct you to."
                if dungeon.has_item(gags):
                    wt_image b_clerk_bj_train_2_1
                    "You take away the use of her hands and bind her in place.  Then you leave her alone for a while to let her think about her transgression."
                    if dungeon.has_item(floggers):
                        wt_image b_clerk_bj_train_2_2
                        "To reinforce how serious you are about this, you interrupt her alone time with periodic beatings."
                        "{i}thwapppp{/i}"
                        bree.c "nnnnnnn"
                        "{i}thwapppp{/i}"
                        bree.c "nnnnnnnnnnn"
                        "{i}thwapppp{/i}"
                        bree.c "nnnnnnnnnnnnnn"
                else:
                    wt_image b_clerk_bj_train_2_5
                    "You take away the use of her hands and bind her in place.  Then you leave her alone for a while to let her think about her transgression."
                wt_image b_clerk_bj_train_2_3
                "When you think she's had enough time to process the lesson, you have her blow you, with her hands immobilized, ropes preventing her from reaching her sex as she pleasures you."
                "Hopefully that will break her of her bad habit."
                wt_image b_clerk_bj_train_2_4
                player.c "[player.orgasm_text]"
                if bree.has_tag('allowed_to_talk'):
                    "As she finishes swallowing your load, she looks up at you thanks you as best she can with your cock in her mouth."
                    bree.c "Thank you, Thir, for cowecting me and twaining me to be a bettuh thwave."
                    player.c "Don't talk with your mouth full."
                    bree.c "Yeth, Thir."
                else:
                    "As she finishes swallowing your load, she looks up at you.  She's not allowed to speak, which is just as well with your cock in her mouth."
                    'But she does her best to say "thank you" with her eyes,'
                    extend " and you know she's grateful to you for correcting her behavior and teaching her to be the slave you want."
                $ bree.bad_habit_status = 2
                $ player.submission_action_count += 1

    elif bree.bad_habit_status == 2:
        wt_image b_clerk_bj_train_1_1
        player.c "[bree.name], come over here and blow me."
        if bree.has_tag('allowed_to_talk'):
            bree.c "Yes, [bree.your_respect_name].  Thank you, [bree.your_respect_name]!"
        else:
            "Silently she moves into position."
        "Infuriatingly, as soon as her tongue touches your cock, her hand slips between her legs."
        wt_image b_clerk_looking_up
        player.c "What are you doing???"
        bree.c "[bree.your_respect_name]?"
        player.c "What have I taught you?"
        bree.c "Oh!!  [bree.your_respect_name], I am so so so very sorry!!!  I don't know what's wrong with me!"
        $ title = "What do you do?"
        menu:
            "Give up":
                wt_image b_clerk_bj_train_1_2
                $ bree.bad_habit_status = 4
                "There are worse things in the world than a slavegirl who touches herself instinctively when she services you. You decide to ignore her little quirk and enjoy the pleasure her mouth brings you."
                wt_image b_clerk_bj_train_1_3
                player.c "[player.orgasm_text]"

            "Get angry":
                player.c "This is ridiculous, [bree.name]."
                bree.c "Yes, [bree.your_respect_name].  I know, [bree.your_respect_name]."
                player.c "Shut up.  No speaking until you're spoken to."
                "She nods."
                player.c "Is this difficult, what I've asked of you?"
                bree.c 'She shakes her "no".'
                player.c "Yet you continue to disobey me."
                "Pitifully, she nods, ashamed of herself."
                wt_image b_clerk_bj_train_3_1
                "Marching her into the dungeon, you bind her in place, immobilizing her hands."
                "You leave her there while you give yourself a chance to cool down.  It wouldn't be safe to punish her while you're angry."
                wt_image b_clerk_bj_train_3_2
                "When you've composed yourself, and given her time to absorb the seriousness of the situation, you return and shove your fingers into her mouth."
                player.c "When I'm enjoying your mouth, all you are is a mouth.  Your entire being and essence is mouth.  You do not have hands to place between your legs.  You do not have a pussy to rub."
                player.c "You are a mouth.  Nothing more.  Nothing less."
                wt_image b_clerk_bj_train_3_3
                player.c "Are you ready to be a mouth?"
                bree.c "Yes, [bree.your_respect_name].  Thank you, [bree.your_respect_name]!"
                wt_image b_clerk_bj_train_3_4
                "The blow job is desperate, frantic, almost animal like.  She throws everything she has into it, doing everything she can to please you within the limits imposed on her by her bonds."
                "You need to place your hands on her head to slow her down, giving you a moment to enjoy the sensation before you empty your load into and on her."
                player.c "[player.orgasm_text]"
                wt_image b_clerk_bj_train_3_1
                "When you've recovered, she looks up at you imploringly."
                bree.c "[bree.your_respect_name], may I speak?"
                $ title = "Let her speak?"
                menu:
                    "Yes":
                        player.c "Go ahead."
                        bree.c "Thank you for taking the time to correct me, [bree.your_respect_name]!!  I am so so sorry."
                        bree.c "I promise you, I wasn't trying to be disobedient.  I would never purposefully disobey you, [bree.your_respect_name].  I hope you know that!"
                        bree.c "I don't understand why I'm being so stupid about this.  I'll do better next time.  I promise, [bree.your_respect_name]!"

                    "No":
                        player.c "No, you may not speak.  What you can do is obey my instructions in the future."
                        "She nods frantically."

            "Stay patient":
                player.c "Why are you disobeying me?"
                bree.c "I don't know, [bree.your_respect_name]!!  I'm not trying to.  I've never purposefully disobeyed you.  Not even when you're not around and wouldn't know.  Certainly not while you're sharing your precious time with me."
                player.c "Are you trying to get punished?"
                bree.c "No, [bree.your_respect_name]!  I'm not a brat!!  I want you to punish me when it amuses you, not because you need to. I'm trying to be the best slave possible for you.  I don't understand why I can't do this simple thing for you."
                "Tears are welling up in the corners of her eyes, and she's about to break down and bawl."
                $ title = "What now?"
                menu:
                    "Give up":
                        wt_image b_clerk_bj_train_1_2
                        "There are worse things in the world than a slavegirl who touches herself instinctively when she services you. You decide to ignore her little quirk and enjoy the pleasure her mouth brings you."
                        wt_image b_clerk_bj_train_1_3
                        player.c "[player.orgasm_text]"
                        $ bree.bad_habit_status = 4

                    "Get angry":
                        player.c "This is ridiculous, [bree.name]."
                        bree.c "Yes, [bree.your_respect_name].  I know, [bree.your_respect_name]."
                        player.c "Shut up.  No speaking until you're spoken to."
                        "She nods."
                        player.c "Is this difficult, what I've asked of you?"
                        bree.c 'She shakes her "no".'
                        player.c "Yet you continue to disobey me."
                        "Pitifully, she nods, ashamed of herself."
                        wt_image b_clerk_bj_train_3_1
                        "Marching her into the dungeon, you bind her in place, immobilizing her hands."
                        "You leave her there while you give yourself a chance to cool down.  It wouldn't be safe to punish her while you're angry."
                        wt_image b_clerk_bj_train_3_2
                        "When you've composed yourself, and given her time to absorb the seriousness of the situation, you return and shove your fingers into her mouth."
                        player.c "When I'm enjoying your mouth, all you are is a mouth.  Your entire being and essence is mouth.  You do not have hands to place between your legs.  You do not have a pussy to rub."
                        player.c "You are a mouth.  Nothing more.  Nothing less."
                        wt_image b_clerk_bj_train_3_3
                        player.c "Are you ready to be a mouth?"
                        bree.c "Yes, [bree.your_respect_name].  Thank you, [bree.your_respect_name]!"
                        wt_image b_clerk_bj_train_3_4
                        "The blow job is desperate, frantic, almost animal like.  She throws everything she has into it, doing everything she can to please you within the limits imposed on her by her bonds."
                        "You need to place your hands on her head to slow her down, giving you a moment to enjoy the sensation before you empty your load into and on her."
                        player.c "[player.orgasm_text]"
                        wt_image b_clerk_bj_train_3_1
                        "When you've recovered, she looks up at you imploringly."
                        bree.c "[bree.your_respect_name], may I speak?"
                        $ title = "Let her speak?"
                        menu:
                            "Yes":
                                player.c "Go ahead."
                                bree.c "Thank you for taking the time to correct me, [bree.your_respect_name]!!  I am so so sorry."
                                bree.c "I promise you, I wasn't trying to be disobedient.  I would never purposefully disobey you, [bree.your_respect_name].  I hope you know that!"
                                bree.c "I don't understand why I'm being so stupid about this.  I'll do better next time.  I promise, [bree.your_respect_name]!"

                            "No":
                                player.c "No, you may not speak.  What you can do is obey my instructions in the future."
                                "She nods franticly."

                    "Stay patient":
                        player.c "Kneel beside me on your knees and elbows and try blowing me again."
                        bree.c "Yes, [bree.your_respect_name].  Thank you, [bree.your_respect_name]."
                        wt_image b_clerk_bj_train_4_1
                        "Sniffling back the tears, she moves into position ..."
                        wt_image b_clerk_bj_train_4_2
                        "... and begins pleasuring you with her mouth."
                        wt_image b_clerk_bj_train_4_1
                        "Suddenly, she lifts her head and looks at you in surprise."
                        bree.c "Oh!  [bree.your_respect_name], I caught myself trying to reach between my legs!!"
                        player.c "How did you notice?"
                        bree.c "I had to shift my weight to move my arm.  Otherwise, I don't think I would've been aware of what I was doing.  I was so busy concentrating on your cock I was oblivious to everything else."
                        player.c "So you've been trying so hard ... get your mouth back on my cock.  Did I say you could stop blowing me?"
                        bree.c "No, [bree.your_respect_name].  Sorry, [bree.your_respect_name]."
                        wt_image b_clerk_bj_train_4_2
                        "Her mouth back where it belongs, you continue your thought."
                        player.c "You've been trying so hard to focus exclusively on my cock and giving me pleasure, you weren't aware of the habit your hand had gotten into."
                        player.c "You haven't been a bad slave for me, [bree.name].  You just need to learn how to be a better one.  In this position, will you notice if that hand tries to sneak away again?"
                        "She nods."
                        player.c "Good. Pay attention when that happens and learn how to break the habit by moving it further away from your legs.  We'll make this a long, leisurely session, so you have lots of time to re-train yourself."
                        "She seems totally happy with the idea of sucking your cock for an extended period, and you're hardly upset by the prospect.  You settle back and let her worship you."
                        wt_image b_clerk_bj_train_4_3
                        "When you've let her practice long enough and you're finally ready to cum, she slides down and kneels at your feet, as if to demonstrate that she can finish you off and take your load without touching herself."
                        player.c "[player.orgasm_text]"
                        $ bree.bad_habit_status = 3
                        $ player.submission_action_count += 1

    else:
        wt_image b_clerk_looking_up
        player.c "[bree.name], come over here and blow me."
        if bree.has_tag('allowed_to_talk'):
            pass
        else:
            bree.c "[bree.your_respect_name], may I speak?"
            "That's a rare request for her just before you use her, so it must be something important."
            player.c "Go ahead."
        bree.c "[bree.your_respect_name], may I kneel beside you one more time, instead of in front you?  I'm worried that if I don't, I might relapse."
        "She's probably right, and there's no point in prolonging her training by pushing her before she's ready."
        player.c "Okay"
        wt_image b_clerk_bj_train_4_1
        "Happily, she scrambles up beside you on her elbows and knees, and takes you into her mouth."
        wt_image b_clerk_bj_train_4_2
        "It's an enjoyable blow job, and this time there are no interruptions by revelations part way through."
        wt_image b_clerk_bj_train_4_3
        "Just like last time, however, when you're ready to cum, she slides down and kneels at your feet, as if to demonstrate that she can finish you off and take your load without touching herself."
        player.c "[player.orgasm_text]"
        "She absolutely glows as you shower her with your jizz."
        if bree.has_tag('allowed_to_talk'):
            bree.c "[bree.your_respect_name], I can control myself now.  I won't ever touch this pussy without permission ever again.  Thank you so much!!"
            bree.c "I'll never be able to explain how happy you've made me, knowing that you would take the time and effort to turn me into the type of slave you want.  It means more than I could ever explain."
            "Well, that went well."
        else:
            bree.c "[bree.your_respect_name], I know I'm only supposed to speak when spoken to, but I can't keep this inside!"
            bree.c "I can control this hand now, and I won't ever touch this pussy without permission ever again.  Thank you so much!!"
            bree.c "I'll never be able to explain how happy you've made me, knowing that you would take the time and effort to turn me into the type of slave you want.  It means more than I could ever explain."
            bree.c "And I'm sorry that I just broke your rule to say it, but I just couldn't keep it inside, no matter how hard I tried.  If you need to punish me, I understand."
            "Who has the energy to punish her after that blow job?"
            player.c "Maybe later."
            "She nods happily.  Not even the prospect of future discipline can dampen her good mood."
        $ bree.bad_habit_status = 5
        $ player.submission_action_count += 1

    $ bree.maintain_week_sg = week + 4
    $ bree.blowjob_count += 1
    $ bree.swallow_count += 1
    orgasm notify
    return

# Give Her Things To Do
label bree_give_her_things_to_do:
    "[bree.work_description]"
    call expandable_menu(bree_give_her_work_menu) from _call_expandable_menu_33
    return

label bree_give_her_work_menu_maid:
    wt_image b_clerk_unhappy
    if bree.has_tag('allowed_to_talk'):
        player.c "I have work for you."
        bree.c "[bree.your_respect_name]?"
        player.c "My private Club is looking for volunteers to keep the place neat and tidy. I volunteered you. The Club President or his wife will let you know when your shifts are. They'll also provide a suitable uniform for you to wear."
        bree.c "[bree.your_respect_name], you want me to be a common maid?"
        player.c "I'd prefer you were an uncommon maid.  Can you do a great job and make me proud?"
        bree.c "Yes, [bree.your_respect_name].  I'll try."
        "Clearly she hates the idea, but she's obedient enough to do it anyway, which is quite adorable."
    else:
        player.c "I have work for you. My private Club is looking for volunteers to keep the place neat and tidy. I volunteered you."
        player.c "The Club President or his wife will let you know when your shifts are. They'll also provide a suitable uniform for you to wear. Do a great job and make me proud."
        "You haven't given her permission to speak, so she can't tell you how much she hates the idea, but that's clear from her face. Despite that, she's obedient enough to do it anyway, which is quite adorable."
    # $ bree.work_description = "{} currently works as a volunteer maid at the Club. She doesn't like it, but she puts up with it to please you.".format(bree.name)
    $ bree.work_description = "She currently works as a volunteer maid at the Club. She doesn't like it, but she puts up with it to please you."
    add tags 'club_maid' 'can_be_in_club' to bree
    return

label bree_give_her_work_menu_maid_stop:
    wt_image b_clerk_lw_visit_11
    if bree.has_tag('allowed_to_talk'):
        player.c "I've decided you don't need to work at the Club anymore."
        bree.c "If that's what you think is best, [bree.your_respect_name]."
        "There's no doubt that's what she thinks is best.  That made her happy."
    else:
        player.c "I've decided you don't need to work at the Club anymore."
        "That made her happy."
    # $ bree.work_description = "{} has not been assigned any work.".format(bree.name)
    $ bree.work_description = "She has not been assigned any work."
    rem tags 'club_maid' 'can_be_in_club' from bree
    return

label bree_give_her_work_no_change:
    pass
    return

# Slapping
label bree_slapping_first:
    $ bree.training_session()
    add tags 'accepts_slapping' to bree
    wt_image b_clerk_date_1_3
    "You tell [bree.name] to dress and come sit beside you."
    player.c "When we first met, and I asked you about your limits, you told me that you did not want to be slapped, that that feels more like abuse than submission to you."
    "[bree.name] nods."
    player.c "You've accepted me as your owner and ceded control of your body to me.  Do you think it is appropriate to keep this limit on my authority?"
    player.c "If I choose to slap my property, should that not be my right?  If I think this is something you should experience, as my slavegirl, is it not something I should do to you?"
    player.c "Will the experience of being slapped by me do you harm, emotionally, do you think?  Will it feel like abuse to you, now, coming from me?"
    "[bree.name] shakes her head.  Very softly, she replies."
    bree.c "No, [bree.your_respect_name]"
    player.c "So you accept my authority to slap you?"
    bree.c "Yes, [bree.your_respect_name]"
    player.c "Kneel down, girl.  I'm going to slap you now."
    wt_image b_clerk_slap_2
    "She keeps her eyes fixed on yours as you hold her face in place with your left hand and bring back your right."
    wt_image b_clerk_slap_3
    "She doesn't flinch as you slap your hand hard against her cheek ...  SLAP!"
    wt_image b_clerk_slap_5
    "As the sting and the shame of the slap hits her, however, she twists away and lets out a cry."
    bree.c "oooooo"
    wt_image b_clerk_slap_4
    "You move behind her and bring her back into position."
    player.c "Hold still."
    "She does as she's told as you slap her ... SLAP  SLAP  SLAP.  She cringes and cries out from the sting of each slap, but no longer twists away from you."
    bree.c "oooooo"
    wt_image b_clerk_head_bowed_1
    if bree.has_tag('allowed_to_talk'):
        "When you finish, [bree.name] bows her head. Even though you've given her permission to talk, she hesitates."
    else:
        "When you finish, [bree.name] bows her head. Its clear that she's anxious to say something to you, and eventually she asks for permission."
    bree.c "May I speak, [bree.your_respect_name]?"
    player.c "Go ahead."
    wt_image b_clerk_looking_up
    "She looks up at you, meeting your eyes as her voice quivers."
    bree.c "Thank you, [bree.your_respect_name], for the slapping.  Thank you for making the effort to take me past my limits and help me to be a better submissive for you."
    player.c "You're welcome, [bree.name].  Now, go resume your position.  I'll let you know the next time I feel like slapping you."
    $ player.submission_action_count += 1
    $ bree.maintain_week_sg = week + 4
    change player energy by -energy_long notify
    return

label bree_slapping_subsequent:
    $ bree.training_session()
    wt_image b_clerk_head_bowed_1
    player.c "I'm going to slap you, [bree.name]."
    "She bows her head."
    wt_image b_clerk_slap_6
    player.c "Lift your head."
    "She does so, nervously, as you touch her cheek."
    wt_image b_clerk_slap_1
    "You caress [bree.name]'s face, then slap her hard across the cheek ... SLAP!"
    if bree.has_tag('allowed_to_talk'):
        bree.c "Thank you, [bree.your_respect_name]."
    else:
        "You haven't given her permission to talk, so she holds her tongue and accepts the slap silently."
    $ bree.choice_needed = True
    while bree.choice_needed:
        $ title = "Again?"
        menu:
            "Slap her again":
                wt_image b_clerk_slap_6
                "You stroke her face gently for a moment, then pull your hand back ... "
                wt_image b_clerk_slap_1
                "SLAP!"
                if bree.has_tag('allowed_to_talk'):
                    bree.c "ooooo ... thank you, [bree.your_respect_name]."
                else:
                    bree.c "ooooo"

            "That's enough for today":
                $ bree.choice_needed = False
    if bree.maintain_week_sg < week + 2:
        $ bree.maintain_week_sg = week + 2
    change player energy by -energy_very_short notify
    return

# Spank Her
label bree_spank:
    $ bree.training_session()
    wt_image b_clerk_spank
    "Sometimes the simplest activities are the most enjoyable."
    bree.c "ow  ... ow ... OW ... OW  ...  OW!  ... OW!  ... OWWW!! ...  OWWW!!"
    wt_image b_clerk_pain_4
    if bree.has_tag('allowed_to_talk'):
        bree.c "Thank you, [bree.your_respect_name].  Thank you for taking the time to amuse yourself by hurting me."
    else:
        "[bree.name] remembers her rules and stays silent after the spanking.  She's physically uncomfortable but emotionally satisfied by the experience."
    $ bree.maintain_week_sg = week + 4
    change player energy by -energy_short notify
    return

# Use Suspension Gear
label bree_use_suspension_gear:
    $ bree.training_session()
    call forced_movement(dungeon) from _call_forced_movement_418
    summon bree
    wt_image b_clerk_suspend_1
    "You bring [bree.name] to your dungeon."
    player.c "Eyes down.  Arms outstretched."
    "She obeys as you wrap first your arm, then the rope around her."
    wt_image b_clerk_suspend_2
    "You carefully wind the rope around her body, creating a secure harness."
    wt_image b_clerk_suspend_10
    "When the ropes are secure, and can hold her weight ..."
    wt_image b_clerk_suspend_3
    "... you winch her into the air ..."
    wt_image b_clerk_suspend_4
    "... then you flip her over, and complete the tie. [bree.name] hangs helplessly, her arms bound behind her, one leg straight up, the other tied tight to her ass."
    $ title = "What do you do with her now?"
    menu:
        "Flog her" if dungeon.has_item(floggers):
            wt_image b_clerk_suspend_5
            "Her helplessness brings out the sadist in you. Picking up a flogger, you begin to whip her with it."
            wt_image b_clerk_suspend_6
            "Her breasts are particularly sensitive.  Perhaps it's the position, bringing more blood than normal into her tits.  She start screaming earlier, and louder, than she normally does when you beat them."
            bree.c "Oooowwwww!!!!"
            wt_image b_clerk_suspend_7
            "So, of course, you concentrate on her breasts, flogging them back and forth, one blow after another until she's taken as much as you think she can safely take."
            bree.c "nnnnnnnnnnnnnnnn!!!!"
            wt_image b_clerk_suspend_12
            "Then you relax to the sounds of her pitiful whimpers."
            bree.c "ooooo ... oooooooo"
            change player energy by -energy_short

        "Torture her with electricity" if bethany.torture_count >0:
            "Watching Bethany be tortured by Hannah put you in the mood to try something similar with [bree.name]."
            wt_image b_clerk_suspend_13
            player.c "I have a toy for you."
            wt_image b_clerk_suspend_14
            "zzzzapppp"
            bree.c "OOOWWWWW!!!!!"
            player.c "Too intense on your tender feet?"
            wt_image b_clerk_suspend_15
            player.c "How about your tongue?"
            "zzzzapppp"
            bree.c "OOOOOOOWWWWW!!!!!"
            wt_image b_clerk_suspend_16
            player.c "That sounded worse.  Let's stick to your feet."
            "zzzzapppp  ...  zzzzapppp  ...  zzzzapppp"
            bree.c "OOOWWWWW ...  OOWWWWW ....  OOOWWWWOOWWWOOOWWWOOWWWWW!!!!!"
            wt_image b_clerk_suspend_12
            "She told you upfront she had a conflicted relationship with pain.  You're not making it any easier for her to resolve that conflict."
            bree.c "OOOWWWWOOWWWOOOWWWOOWWWWW!!!!!"
            change player energy by -energy_short

        "Play with her breasts":
            wt_image b_clerk_suspend_8
            "You grip her firmly by the tit.  Her breasts seem fuller and more sensitive than normal.  Perhaps the position she is in is increasing the blood flow to her breasts."
            wt_image b_clerk_suspend_9
            "To test her sensitivity, you pinch one of her nipples hard.  She doesn't usually scream this loud when you pinch her like this."
            bree.c "Oowww!!"
            "This position has made her more sensitive."
            wt_image b_clerk_suspend_10
            "So, of course, you concentrate exclusively on this area of her body, amusing yourself by experimenting with her to see what sounds you can get her to make just by squeezing and pinching her engorged tits."
            bree.c "Oowww!!  Oohhhh!!!  Ooooo!!!!  OOOWWWWW!!!!"
            change player energy by -energy_short

        "Just let her hang there":
            "She looks so cute hanging there, it seems a shame to disturb her.  The ropes carry her weight evenly around her hips.  She can safely stay in this position for a couple of hours."
            "So that's where you leave her, going about your business while she hangs there, providing an enjoyable backdrop to your day."
            change player energy by -energy_very_short

    $ bree.maintain_week_sg = week + 4
    call character_location_return(bree) from _call_character_location_return_212
    notify
    return

# Use Fuck Machine
label bree_use_fuck_machine:
    $ bree.training_session()
    call forced_movement(dungeon) from _call_forced_movement_419
    summon bree
    wt_image b_clerk_machine_2
    "You place [bree.name] on a bench in front of the fuck machine and adjust the settings so that each stroke will penetrate her fully."
    if bree.has_tag('allowed_to_cum'):
        "She smiles eagerly in anticipation of what the machine will do to her."
    elif bree.has_tag('allowed_to_beg'):
        "She resolves herself to the certainty that the machine will soon have her begging for release, hoping that you won't make her beg too long."
    else:
        "She trembles in trepidation of what the machine will do to her, remembering that she's not allowed to cum and worried about whether she'll be able to hold off when the machine starts working on her."
    wt_image b_clerk_machine_3
    "Her look is soon replaced by a grimace as the intensity of the fucking borders between pain and pleasure."
    bree.c "ooohhhh ... nnnnnnnn"
    wt_image b_clerk_machine_14
    "When she gets close to orgasm, you stop the machine and order her to turn over.  You replace the business end with a double-headed dildo that's soon ramming both of her holes."
    if bree.has_tag('allowed_to_cum'):
        wt_image b_clerk_machine_15
        "When she gets close again, you slow the strokes, leaving her on edge before speeding the machine up again.  You continue to tease and torture her this way until she's beyond the point of holding back."
        wt_image b_clerk_machine_4
        bree.c "ooohhhh .... ooooohhhhh"
        $ bree.temporary_count = 1
    elif bree.has_tag('allowed_to_beg'):
        wt_image b_clerk_machine_15
        if bree.has_tag('allowed_to_talk'):
            "When she gets close again, you slow the strokes, leaving her on edge before speeding the machine up again.  You continue to tease and torture her this way until she asks for permission to cum."
        else:
            "When she gets close again, you slow the strokes, leaving her on edge before speeding the machine up again.  You continue to tease and torture her this way until she asks for permission to beg."
            wt_image b_clerk_machine_16
            bree.c "ooohhhh ... ooooohhhhh ... Please, [bree.your_respect_name], may I have permission to beg?"
            player.c "Go ahead."
        wt_image b_clerk_machine_4
        bree.c "oooohhhh ... ooooohhh ... May I please cum, [bree.your_respect_name]?  Please??? I need to cum so bad,  I can't hold it back ...  please?? ... please???"
        $ title = "Give her permission to cum?"
        menu:
            "Yes, tell her she can cum":
                wt_image b_clerk_machine_17
                "You listen to her begging until you think she's going to explode in frustration. Only then do you relent."
                player.c "You may cum now, [bree.name]."
                $ bree.temporary_count = 1

            "No, tell her to fight it":
                wt_image b_clerk_machine_17
                "Keeping a woman who's not allowed to cum on the machine is intensely cruel.  When you see her struggle to hold off her orgasm, you slow the strokes, giving her a chance to control herself before speeding the machine up again."
                wt_image b_clerk_machine_18
                "You continue to tease and torture her this way until she's almost at the breaking point of being unable to hold back a climax."
                bree.c "PLLEEAAASE, [bree.your_respect_name]!   I CAN'T HOLD BACK!!  MAY I PLEASE CUM????"
                $ title = "What do you do?"
                menu:
                    "Tell her she can cum":
                        wt_image b_clerk_machine_17
                        "You listen to her begging until you think she's going to explode in frustration. Only then do you relent."
                        player.c "You may cum now, [bree.name]."
                        $ bree.temporary_count = 1

                    "Turn off the machine":
                        $ bree.temporary_count = 2

                    "Let it keep fucking her":
                        $ bree.temporary_count = 3
    else:
        wt_image b_clerk_machine_15
        "Putting a woman who's not allowed to cum on the machine is cruel, but you're about to be crueler still.  When you see her struggle to hold off her orgasm, you slow the strokes, giving her a chance to control herself before speeding the machine up again."
        wt_image b_clerk_machine_16
        bree.c "ooohhhh .... ooooohhhhh"
        wt_image b_clerk_machine_17
        "You continue to tease and torture her this way until she's almost at the breaking point of being unable to hold back a climax."
        $ title = "What do you do?"
        menu:
            "Turn off the machine":
                $ bree.temporary_count = 2

            "Let it keep fucking her":
                $ bree.temporary_count = 3
    if bree.temporary_count == 1:
        wt_image b_clerk_machine_13
        "[bree.name]'s body shakes from her head to her feett as the climax rips though her."
        if bree.has_tag('allowed_to_talk'):
            bree.c "OOOHHHH!!!!!!   THANK YOU!!!"
        else:
            bree.c "OOOHHHH!!!!!!"
        $ bree.maintain_week_sg = week + 4
        $ bree.orgasm_count += 1
    elif bree.temporary_count == 2:
        wt_image b_clerk_machine_6
        "You flip the switch to off.  As the dildo stops moving in and out of her, [bree.name] slumps forward in relief."
        if bree.has_tag('allowed_to_talk'):
            bree.c "Thank you for turning off the machine, [bree.your_respect_name].  I wasn't sure I could hold back much longer."
        else:
            "She's not allowed to talk, but the look on her face suggests she's grateful you shut the machine down when you did, before she came without permission."
        $ bree.maintain_week_sg = week + 4
    elif bree.temporary_count == 3:
        wt_image b_clerk_machine_4
        "You leave the machine running.  Soon [bree.name]'s trembling from head to foot."
        wt_image b_clerk_machine_13
        "A moment later, and every muscle in her body tenses up as she's helpless to prevent the orgasm from ripping through her."
        bree.c "Noooooo!!!  OOOOHHHHH!!!!!"
        wt_image b_clerk_machine_6
        "She slumps forward, mortified at her transgression.  Tears run freely down her cheeks.  You can punish her for her disobedience later. For the moment, she's doing a good job of chastising herself."
        bree.c "I'm sorry [bree.your_respect_name]!!!  I'm so sorry.  I didn't want to cum!  I tried not to.  I couldn't help myself.  I'm so so sorry!!!"
        if bree.maintain_week_sg < week + 2:
            $ bree.maintain_week_sg = week + 2
        $ bree.orgasm_count += 1
    change player energy by -energy_very_short notify
    call character_location_return(bree) from _call_character_location_return_213
    call forced_movement(bedroom) from _call_forced_movement_420
    return

# Hurt Her
label bree_hurt_her:
    $ bree.training_session()
    call forced_movement(dungeon) from _call_forced_movement_421
    summon bree
    wt_image bree.image
    "[bree.name] has come to adore having you hurt her.  Nothing else makes her feel so ... submitted ... to you."
    "Not that she doesn't still experience an intense sense of fear and apprehension when you tell her you want to watch her experience pain."
    $ title = "How do you want to hurt her?"
    menu:
        "Clamps":
            wt_image b_clerk_clamps_1
            "You make [bree.name] watch as you place the clamps over her nipples ..."
            wt_image b_clerk_clamps_2
            "... and begin to add weights."
            wt_image b_clerk_clamps_3
            "Once you reach the maximum weight she can tolerate, you leave them pulling on her nipples and breasts for the next fifteen minutes."
            bree.c "nnnnnnn"
            wt_image b_clerk_crop_3
            "As you finally take the clamps off, she screams."
            bree.c "Ooowwww!!"
            wt_image b_clerk_clamps_4
            "When she recovers from having the weighted clamps removed, you re-tie [bree.name], bind her breasts to trap the blood flow, and re-attach the clamps to her already painful nipples, this time without weights."
            "You blindfold and leave her there, watching the waves of emotion passing across her face as she deals with the sensations emanating from her tortured breasts."
            bree.c "nnnnnnnnnnn"
        "Clothespins":
            wt_image b_clerk_pins_1
            "You warm [bree.name] up with two lines of clothespins along each side of her body."
            wt_image b_clerk_pins_2
            'The "zippers" hurt when you remove them, but you quickly distract her with pins on both nipples.'
            bree.c "Ooowwww!!!!"
            wt_image b_clerk_pins_3
            "You leave [bree.name] in this position until her jagged breaths tell you she's reaching the limit of her pain tolerance."
            wt_image b_clerk_pins_4
            "Unfortunately for her, the pain when you remove the pins is far more intense than the feeling of the pins themselves, as the blood rushes back in to the tortured flesh."
            bree.c "Oooowwwww!!!!"
            "Again, you distract her with a new, strategically placed clothespin placed firmly around her engorged clit."
            bree.c "oooooo"
            wt_image b_clerk_pins_5
            "Taking deep breaths, [bree.name] concentrates on absorbing the intense sensation, hovering on the border between pain and pleasure ..."
            wt_image b_clerk_pins_6
            "... until she sees how you intend to remove the last clothespin, at which point her resolve fails her and she starts screaming even before the crop strikes."
            bree.c "Aaaaahh .. OOOWWWW!!!!"
        "Wax":
            wt_image b_clerk_wax_1
            "You prepare [bree.name] for her waxing."
            wt_image b_clerk_wax_2
            "You can't resist teasing her.  The extra blood flow will make her even more sensitive to what is to come."
            wt_image b_clerk_wax_3
            "You light the candle and begin dripping wax over [bree.name]'s belly and breasts."
            bree.c "oooooo"
            wt_image b_clerk_wax_4
            "The closer the candle is to her skin, the hotter the wax is when it lands."
            "You move the candle up and down, alternating drops of pleasantly warm with drops that are excruciatingly hot as [bree.name] struggles to hold back her screams."
            bree.c "nnnnn ... nnnnnnn"
            wt_image b_clerk_wax_5
            "You light a second candle, and place both of them directly above [bree.name]'s exposed groin."
            bree.c "Oohhhh!"
            wt_image b_clerk_wax_6
            "She watches helplessly as the candles drip ... drip ... drip."
            "By moving her hips, she can keep the heat on any one area from getting unbearable, but she can't prevent the overall discomfort from growing, and soon she's screaming despite herself."
            bree.c "Oohhh  ... Ooohhhh  ... Ooowwwww!!"
            wt_image b_clerk_wax_7
            "Soon, the wax has formed a solid cake around and over her tender labia.  She's sore but unmistakably aroused, too."
            bree.c "nnnnnnnnnn  ooohhhh  oohhh  ooowwww  ooooooo!!"
            wt_image b_clerk_wax_8
            "When the candles have burned out, you watch and listen with amusement as [bree.name] recovers from the waxing."
            "The wax wasn't hot enough to burn her skin, but it feels that way to her poor, overloaded pain receptors.  Still, you have the sense she'd like her sore parts touched, despite the pain."
            bree.c "ooooo ... ooooooo"
        "Riding Crop" if dungeon.has_item(floggers):
            wt_image b_clerk_crop_1
            "[bree.name] steels her resolve as you position her for her cropping."
            wt_image b_clerk_crop_2
            "You warm her up by cropping the soles of her feet ... *smack*  *smack*  *smack*"
            wt_image b_clerk_crop_3
            "The sting of the leather against her sensitive soles soon brings tears to her eyes."
            bree.c "ooooo"
            wt_image b_clerk_crop_4
            "The pain becomes worse when you shift to her breasts, and she cries out."
            bree.c "Oowww!!"
            wt_image b_clerk_crop_5
            "The true agony, however, only begins when you start cropping her sex."
            bree.c "OOOWWWW!!!"
            wt_image b_clerk_crop_6
            "Just when she thinks she can take no more, you replace the riding crop with your hand."

            if bree.has_tag('allowed_to_cum'):
                "[bree.name] is no painslut, but the hard slapping of your hand against her already tortured clit and pussy lips soon rips an intense orgasm out of her. The experience is somewhat pleasurable, but it is mostly something to be endured."
                bree.c "Ooohhhhh!!!"

            elif bree.has_tag('allowed_to_beg'):
                "[bree.name] is no painslut, but the hard slapping of your hand against her already tortured clit and pussy lips soon has her on the brink of orgasm."
                bree.c "Please [bree.your_respect_name]!!  May I be allowed to cum, [bree.your_respect_name]???"
                $ title = "Give her permission to cum?"
                menu:
                    "Let her cum":
                        player.c "Go ahead.  Cum for me."
                        "Your hand slapping on her already tortured clit and pussy lips soon rips an intense orgasm out of her. The experience is somewhat pleasurable, but it is mostly something to be endured."
                        bree.c "Ooohhhhh!!!"

                    "No, tell her to control herself":
                        player.c "Don't be silly.  I'm doing this to watch you suffer, not to watch you enjoy yourself."
                        "She grits her teeth and tries to ignore both the pleasurable and painful sensations radiating from her center until your hand eventually stops slapping her tender sex."

            else:
                "[bree.name] is no painslut, but the hard slapping of your hand against her already tortured clit and pussy lips soon has her on the brink of orgasm."
                "Knowing that she's not allowed to cum, she grits her teeth and tries to ignore both the pleasurable and painful sensations radiating from her center until your hand eventually stops slapping her tender sex."
    $ bree.maintain_week_sg = week + 4
    call character_location_return(bree) from _call_character_location_return_214
    call forced_movement(bedroom) from _call_forced_movement_422
    change player energy by -energy_short notify
    return

# Use Her
label bree_use_her:
    $ bree.training_session()
    wt_image bree.image
    "The time you spend fucking [bree.name] is always her favorite time of the week."
    $ title = "What part of her do you want to use?"
    menu:
        "Ass":
            call forced_movement(dungeon) from _call_forced_movement_423
            summon bree to dungeon
            wt_image b_clerk_anal_4
            "You strap [bree.name] down and prepare her to receive you, using the buttplug she bought before she met you."
            wt_image b_clerk_anal_5
            "Once the butt plug has her stretched open, you remove it and insert yourself."
            bree.c "Oohhh!!"
            wt_image b_clerk_anal_6
            if bree.has_tag('allowed_to_cum'):
                "It's always a race to see if you can finish before [bree.name] gets herself off on the feeling of your cock ramming her open."
                wt_image b_clerk_anal_5
                $ bree.random_number = renpy.random.randint(1, 10)
                if bree.random_number < 6:
                    "And even when you win, the feel of your seed shooting inside her brings her over the edge shortly after."
                    player.c "[player.orgasm_text]"
                    bree.c "OOOHHH!!!"
                else:
                    "Not that you can really lose, because even she cums first, the feeling of her body climaxing around your cock in her ass always brings you over the edge shortly after."
                    bree.c "OOOHHH!!!"
                    player.c "[player.orgasm_text]"
                $ bree.orgasm_count += 1

            elif bree.has_tag('allowed_to_beg'):
                "The feel of your cock ramming her open has [bree.name] begging for relief quickly."
                bree.c "Please [bree.your_respect_name]!  Your cock feels sooo good in my ass, [bree.your_respect_name].  Can I please cum, [bree.your_respect_name]?  Pleaassse?  I need to cum so bad, [bree.your_respect_name]!"
                $ title = "Give her permission to cum?"
                menu:
                    "Yes, let her cum":
                        if bree.has_tag('allowed_to_talk'):
                            "When you give her permission, she's very grateful."
                            bree.c "OOOHHH!!!  Thank you [bree.your_respect_name]!!"
                        else:
                            "When you give her permission, she's very grateful, not that she's allowed to express that with words."
                            bree.c "OOOHHH!!!"
                        "Not that you need much more in the way of thanks than the feeling of her body climaxing around your cock in her ass, a feeling that always brings you over the edge, too."
                        player.c "[player.orgasm_text]"
                        $ bree.orgasm_count += 1

                    "No, tell her to control herself":
                        player.c "Not today.  Control yourself.  This is about my pleasure, not yours."
                        "She grits her teeth and focuses on getting you off as quick as she can, while you do your best to make it last as long as you can before you fill her bowels with your sperm."
                        player.c "[player.orgasm_text]"

            else:
                "The feel of your cock ramming her open fills [bree.name] with a sense of purpose, and not being allowed to cum herself, she knows the purpose is to please you."
                "She grits her teeth and focuses on getting you off as quick as she can, while you do your best to make it last as long as you can before you fill her bowels with your sperm."
                player.c "[player.orgasm_text]"

            $ bree.anal_count += 1

        "Mouth":
            # option if bad habit training completed or abandoned
            if bree.bad_habit_status > 3:
                $ title = "How do you want to enjoy her mouth?"
                menu:
                    "Bound":
                        $ bree.temporary_count = 0

                    "Unbound":
                        $ bree.temporary_count = 1
            else:
                $ bree.temporary_count = 0

            #Bound
            if bree.temporary_count == 0:
                call forced_movement(dungeon) from _call_forced_movement_424
                summon bree to dungeon
                wt_image b_clerk_bj_5
                player.c "Open your mouth, [bree.name].  Stick out your tongue."
                wt_image b_clerk_bj_6
                "You tie her firmly in place, then roughly shove your cock into her open, waiting mouth."
                "She's learned to swallow you whole without gagging.  Without missing a beat, she immediately sets to work sucking and pleasuring you with her tongue."
                wt_image b_clerk_bj_7
                player.c "Look at me while I cum."
                "[bree.name] keeps her eyes on you as you fill her mouth and throat with your load."
                player.c "[player.orgasm_text]"

            #Unbound
            if bree.temporary_count == 1:
                call forced_movement(living_room) from _call_forced_movement_425
                summon bree to living_room
                wt_image b_clerk_bj_train_4_4
                player.c "Open your mouth, [bree.name].  Stick out your tongue."
                # if cured:
                if bree.bad_habit_status == 5:
                    wt_image b_clerk_bj_train_5_1
                    "She keeps her hands on you as she takes your cock into her mouth."
                    wt_image b_clerk_bj_train_5_2
                    "Even when you tell her to use only her mouth, she keeps her hands where you can see them."
                    wt_image b_clerk_bj_train_5_3
                    "She's proud of herself for changing to please you better, and you're pretty pleased with that blow job."
                    player.c "[player.orgasm_text]"
                # if not cured
                else:
                    wt_image b_clerk_bj_train_1_1
                    "Your dick has no sooner touched the tip of her tongue, than her hand sneaks down between her legs."
                    "Is she even aware that she's doing it?  At this point, you honestly have no idea."
                    wt_image b_clerk_bj_train_1_3
                    "What you do know is it doesn't impact the quality of her blow job.  In fact, it's kind of fun, watching your slave girl surreptitiously rubbing her clit while she pleasures you."
                    player.c "[player.orgasm_text]"
                    wt_image b_clerk_bj_train_1_2
                    player.c "Did you enjoy that?"
                    bree.c "Yes, [bree.your_respect_name].  I love when you use my mouth."
                    player.c "I meant did you enjoy the feeling of your hand?"
                    bree.c "On your cock when it came?  Oh yes, [bree.your_respect_name]!  It felt amazing."

            $ bree.blowjob_count += 1
            $ bree.swallow_count += 1

        "Pussy":
            call forced_movement(dungeon) from _call_forced_movement_426
            summon bree to dungeon
            wt_image b_clerk_sex_3
            "You prefer to bind [bree.name] tightly before having sex.  It prevents her from shifting her body to enhance or reduce her pleasure as you fuck her."
            wt_image b_clerk_sex_4
            "Despite that, she's always dripping wet in anticipation before you enter her ..."
            if bree.has_tag('allowed_to_cum'):
                wt_image b_clerk_sex_6
                "... and loves the feeling of your cock inside her so much she invariably cums, loudly ..."
                bree.c "OOOHHHHH!!!!"
                wt_image b_clerk_sex_5
                "... as soon as you fill her with your seed, if not before then."
                player.c "[player.orgasm_text]"
                $ bree.orgasm_count += 1

            elif bree.has_tag('allowed_to_beg'):
                "... and loves the feeling of your cock inside her so much she invariably begs for permission to cum shortly after you start stroking into her."
                bree.c "Please [bree.your_respect_name]!  Please, may I cum for you [bree.your_respect_name]?? Your cock feels so good inside me.  Please may I cum, [bree.your_respect_name]?"
                $ title = "Give her permission to cum?"
                menu:
                    "Yes, let her cum":
                        wt_image b_clerk_sex_6
                        "When she gets permission, she cums, loudly ..."
                        bree.c "OOOHHHHH!!!!"
                        wt_image b_clerk_sex_5
                        "... as soon as you fill her with your seed, if not before then."
                        player.c "[player.orgasm_text]"
                        $ bree.orgasm_count += 1

                    "No, tell her to control herself":
                        player.c "No.  This is about me, not you."
                        wt_image b_clerk_sex_5
                        "Any disappointment she feels at not getting to cum is soon replaced with a feeling of intense satisfaction when you fill her with your seed."
                        player.c "[player.orgasm_text]"
                        bree.c "oooooo ... mmmmmm"

            else:
                "... even though she knows she's not allowed to cum, and that this is all about your pleasure."
                wt_image b_clerk_sex_5
                "That doesn't keep her from feeling a sense of deep satisfaction, especially when you fill her with your seed."
                player.c "[player.orgasm_text]"
                bree.c "oooooo ... mmmmmm"

    $ bree.sex_count += 1
    $ bree.maintain_week_sg = week + 4
    orgasm notify
    call character_location_return(bree) from _call_character_location_return_215
    return

# Lend to Master M
label bree_lend_to_master_m:
  wt_image b_clerk_looking_up
  player.c "[bree.name], get dressed.  I'm sending you to another man."
  bree.c "Another man?  But, I belong to you, [bree.your_respect_name]."
  player.c "And you are mine to do what I want with.  Today, what I want is for you to go visit Master M and let him do whatever he wants with you. Until he sends you back to me, you will obey him as you would me."
  bree.c "Yes, [bree.your_respect_name]."
  if bree.has_tag('allowed_to_talk'):
    bree.c "Another man, [bree.your_respect_name]?"
    player.c "We discussed this before you agreed to become my slave.  You are my property and I will do with you what I choose, including lending you to others if the mood strikes me."
    player.c "Today I'm sending you to please Master M.  Until he sends you back to me, you will obey him as you would me."
    bree.c "Yes, [bree.your_respect_name]."
    "She's not happy about this, but she obeys."
  else:
    "You can see panic in her eyes.  She wants to say something, but remembering her rules, bites her tongue."
    player.c "We discussed this before you agreed to become my slave.  You are my property and I will do with you what I choose, including lending you to others if the mood strikes me."
    player.c "Today I'm sending you to please Master M.  Until he sends you back to me, you will obey him as you would me."
    "She nods. She's not happy about this, but she obeys."
  wt_image b_clerk_mm_10
  "It's a few hours later before she returns and undresses."
  player.c "How did it go?"
  bree.c "Good, I hope, [bree.your_respect_name]."
  player.c "Was he pleased with you?"
  bree.c "I hope so."
  $ title = "Ask for details?"
  menu:
    "Yes":
      player.c "What did he do with you?"
      wt_image b_clerk_mm_2
      bree.c "{i}He had me strip ...{/i}"
      wt_image b_clerk_mm_3
      bree.c "{i}... and lie down on a table ...{/i}"
      wt_image b_clerk_mm_4
      bree.c "{i}... where he tied me in place and placed his cock in my mouth.{/i}"
      player.c "{i}Then what?{/i}"
      bree.c "{i}He ...   He ...{/i}"
      player.c "{i}Go on.{/i}"
      wt_image b_clerk_mm_5
      bree.c "{i}He placed his hand between my legs and played with the wetness dripping out of me. He didn't say anything.  He didn't need to.  He wasn't trying to arouse me.  I was wet simply because he'd tied me down and stuck his cock in my mouth, and he knew it.  He knew even before he touched me.  He just touched me to make me acknowledge it.{/i}"
      bree.c "{i}I'm so sorry, [bree.your_respect_name]!!  I belong to you and you're the only Master I want.  I'm not a slut.  I don't want to be with other men.  I'm so sorry my body betrayed me and betrayed you!{/i}"
      wt_image b_clerk_mm_6
      bree.c "{i}I was so humiliated.  He chuckled softly under his breath at me as he re-tied me into a kneeling position. I was thankful, at first, when he put me to work sucking him, because it meant I didn't have to look at him and see his amusement at how easy I was.{/i}"
      bree.c "{i}But then he just kept me there, kneeling and sucking on him, for what seemed like forever.{/i}"
      wt_image b_clerk_mm_7
      bree.c "{i}It went on and on until my jaw ached and every muscle in my shoulders are neck was screaming at me. You've put me through more intense suffering, [bree.your_respect_name], but this was agonizing in it's own, unique way.  My entire being was focused on his cock, which had become an instrument of torture, and my only role was to give it pleasure.{/i}"
      player.c "{i}And did you?{/i}"
      bree.c "{i}I tried, [bree.your_respect_name].  When the pain got so bad I could hardly bear it, I tried so hard to get him to cum, but he would have none of it.  He was in control and he made sure I knew it.  I was just a mouth and he was going to use me as one until he had finished amusing himself with me.{/i}"
      wt_image b_clerk_mm_8
      bree.c "{i}I must have spaced out, because I lost all track of time.  The next thing I remember is that his cock was finally, mercifully  removed from my mouth and I was being pulled up, into the air.  Then I felt his cock enter me, and I could feel him cumming inside me.{/i}"
      player.c "{i}Did you cum, too?{/i}"
      wt_image b_clerk_mm_9
      bree.c "{i}No, [bree.your_respect_name].  But, [bree.your_respect_name] ... I'm so sorry, [bree.your_respect_name].  The only reason I didn't cum is because he told me I wasn't allowed to.  My body wanted to, so much, hanging there, feeling his seed spurting inside me, but he wouldn't let me.{/i}"
      wt_image b_clerk_mm_11
      bree.c "I hope you can forgive me, [bree.your_respect_name].  I didn't mean to betray you and respond to another man.  I don't want to be his slave, I want to be yours.  If you decide to punish me, I'll understand, [bree.your_respect_name]."
      $ title = "What do you do?"
      menu:
        "Punish her":
          call forced_movement(dungeon) from _call_forced_movement_427
          summon bree
          wt_image b_clerk_whip_10
          "She needs punishment for her body's response, and you give it to her.  You bind her on her back with her legs in the air ..."
          wt_image b_clerk_whip_8
          "... then shove a big, black dildo into her mouth."
          wt_image b_clerk_whip_9
          player.c "Is this what you like, you dirty slut?  A big black cock in your mouth that you can't make cum no matter how hard you suck on it?  Is that what turns your whore cunt on?"
          if dungeon.has_item(floggers):
            wt_image b_clerk_whip_11
            player.c "Let's see if I can teach this whore cunt not to get wet every time a strange man shoves his dick in your mouth."
            "There's no need to spread this whipping around.  There's one part of her body that earned this punishment, and that's what you rain the blows down on ... *thwappp* ... *thwappp* ... *thwappp*"
            bree.c "Ooowwww!! ... Ooowwww!!!! ... OOOWWWW!!!!"
          else:
            wt_image b_clerk_spank_3
            player.c "Let's see if I can teach this whore cunt not to get wet every time a strange man shoves his dick in your mouth."
            "There's no need to spread this spanking around.  There's one part of her body that earned this punishment, and that's what you rain the blows down on ... *slappp* ... *slappp* ... *slappp*"
            bree.c "Oooww! ... Oooowww!! ... Ooooowwww!!!"
          wt_image b_clerk_pain_3
          "[bree.name] can take a lot of pain.  Today she needs to, as you make her pussy regret that she was turned on by being dominated by Master M.  Eventually, though, you finally reach her pain tolerance limit.  She screams like an animal when you take her to the point where she can take no more."
          bree.c "YOOAAAWWWW!!!!"
          wt_image b_clerk_gratitude
          if bree.has_tag('allowed_to_talk'):
            "It takes a long time before [bree.name] is able to again form words.  When she can, she looks up at you with gratitude and devotion."
            bree.c "Thank you for correcting me, [bree.your_respect_name]."
          else:
            "It takes a long time before [bree.name] recovers enough to focus.  When she can, she looks up at you with gratitude and devotion.  She's too obedient to talk without your permission, but does her best to say 'thank you' with her eyes."
          change player energy by -energy_short notify
          call forced_movement(bedroom) from _call_forced_movement_428
          call character_location_return(bree) from _call_character_location_return_216
        "Fuck her":
          wt_image b_clerk_mm_12
          player.c "Stand up, [bree.name]."
          bree.c "Yes, [bree.your_respect_name]."
          wt_image b_clerk_mm_13
          "When you lay her on her back and place the tip of your cock inside her, she literally trembles with delight."
          if bree.has_tag('allowed_to_cum'):
            wt_image b_clerk_mm_14
            "And when you push yourself into her, she cums, loudly and almost instantaneously."
            bree.c "OOOHHHHH!!!!"
            "It doesn't take you much longer."
            player.c "[player.orgasm_text]"
            $ bree.orgasm_count += 1
          elif bree.has_tag('allowed_to_beg'):
            wt_image b_clerk_mm_15
            "And when you push yourself into her, she starts to shake uncontrollably."
            bree.c "Please, [bree.your_respect_name]!!!   Please, may I be allowed to cum, [bree.your_respect_name]????   Please!!!!"
            $ title = "Give her permission to cum?"
            menu:
              "Let her cum":
                wt_image b_clerk_mm_14
                player.c "Go ahead, [bree.name].  Cum for me."
                "She does, loudly and instantaneously."
                bree.c "OOOHHHHH!!!!"
                "It doesn't take you much longer."
                $ bree.orgasm_count += 1
              "No, tell her to control herself":
                wt_image b_clerk_mm_16
                player.c "No.   Control yourself."
                "She does, barely.  Long enough for you to take your pleasure from her.  Fortunately for her, that doesn't take long and you're soon instructing her to pump your cock while you shower her with your seed."
            player.c "[player.orgasm_text]"
          else:
            wt_image b_clerk_mm_15
            "And when you push yourself into her, she starts to shake uncontrollably."
            "She knows she's not allowed to cum, but it takes every ounce of self-control she has not to disobey you as you take your pleasure from her."
            wt_image b_clerk_mm_16
            "Fortunately for her, that doesn't take long and you're soon instructing her to pump your cock while you shower her with your seed."
            player.c "[player.orgasm_text]"
          wt_image b_clerk_mm_17
          if bree.has_tag('allowed_to_talk'):
            bree.c "Thank you for using me, [bree.your_respect_name]!"
            bree.c "You're the only Master I want.  No other Master could make me feel the way you do.  If you choose to lend me out to other men, I'll obey them absolutely, but I'll only be thinking about you and my obedience to you when I do so."
          else:
            "She looks up at you with big, puppy dog eyes."
            "You know she wants to say something sappy and emotional, but she's too obedient to talk without permission, and there's no need to give her that permission.  The look on her face says enough."
          $ bree.sex_count += 1
          orgasm notify
        "Make her blow you":
          if bree.bad_habit_status == 5 or bree.bad_habit_status == 3:
            wt_image b_clerk_bj_8
            player.c "I'm going to use your mouth."
            "Her jaw has had some rest, but you know it must still be very sore."
            "Despite that, she obediently takes you into her mouth, making sure to keep her hands where you can see them."
            wt_image b_clerk_bj_9
            "She's in agony, and no matter how hard she tries not to let that show, the simple act of sucking you off after the ordeal Master M put her through is one of the most intense tortures you've inflicted on her."
            "Before long, her whole body is trembling as her muscles rebel against overuse."
          else:
            wt_image b_clerk_bj_11
            player.c "I'm going to use your mouth."
            "Her jaw has had some rest, but you know it must still be very sore.  Despite that, she obediently takes you into her mouth."
            wt_image b_clerk_bj_12
            "She's in agony, and no matter how hard she tries not to let that show, the simple act of sucking you off after the ordeal Master M put her through is one of the most intense tortures you've inflicted on her.  Before long, her whole body is trembling as her muscles rebel against overuse. Not even her hand furiously frigging away between her legs is enough to distract her body from the suffering it's going through."
          wt_image b_clerk_bj_10
          "Fortunately for her, you can't hold out for much longer, not while watching her try to ignore the tremors in her own body and focus exclusively on pleasuring your cock, no matter how much it hurts."
          player.c "[player.orgasm_text]"
          "As you release your load into her mouth, she slips into a state of deep subspace.  She's spent most of the day as a mouth for fucking, first by Master M, then by you, and she's rarely if ever been happier."
          $ bree.blowjob_count += 1
          $ bree.swallow_count += 1
          orgasm notify
        "Go on with your day":
          player.c "I'm sure you did fine, [bree.full_name]."
          "Perhaps, but she doesn't look happy with herself."
    "No, just go on with your day":
      player.c "I'm sure you did fine, [bree.full_name]."
      "Perhaps, but she doesn't look happy with herself."
  $ master_m.experience_with_your_slave = "She's a natural submissive, that one.  You're lucky to have her."
  $ master_m.name_of_your_slave_loaned = bree.name
  $ bree.training_session()
  add tags 'master_m_visit' to bree
  call master_m_lend from _call_master_m_lend_1
  return

# with Alexis
label bree_alexis:
    call alexis_sg_bree from _call_alexis_sg_bree
    return

# with Elsa
label bree_elsa:
    call elsa_sg_bree from _call_elsa_sg_bree
    return

## Degraded Actions
# Whip Her
label bree_whip_her_degraded:
    $ bree.training_session()
    wt_image b_clerk_whip_1
    "[bree.name] grins manically as you take out her gag and string her up. Is she looking forward to the whipping?"
    wt_image b_clerk_whip_2
    "You flog her back ..."
    bree.c "nnnn"
    wt_image b_clerk_whip_3
    "... and her belly and breasts."
    bree.c "nnnn"
    wt_image b_clerk_whip_4
    "But she doesn't really react until you pay particular attention to her ass and sex ..."
    wt_image b_clerk_pain_2
    "... at which point she screams like an animal as the leather cuts into the tender flesh between her legs."
    bree.c "YOOAAAWWWW!!!!"
    wt_image b_clerk_whip_5
    "When you first met her, you needed to worry about not marking her.  No longer."
    wt_image b_clerk_whip_12
    "Her skin is rendered tender and raw by the flogger, ready to be ripped open when you switch to the whip."
    bree.c "nnnn"
    wt_image b_clerk_whip_13
    "{i}thwippp{/i}"
    bree.c "Aaaaaahhh!!"
    "{i}thwippp{/i}"
    bree.c "Aiiieeeeee!!!"
    "{i}thwippp{/i}"
    bree.c "YOOAAAWWWW!!!!"
    wt_image b_clerk_whip_7
    "You'll treat her wounds when you're finished, to make sure she doesn't get an infection."
    "For the moment, you can simply enjoy torturing a creature that exists for no other purpose than to suffer for your amusement."
    change player energy by -energy_short notify
    return

# Relieve Yourself
label bree_relieve_yourself_degraded:
    $ bree.training_session()
    wt_image b_clerk_degraded_1
    "[bree.name] watches warily as you approach."
    wt_image b_clerk_degraded_5
    "You free her mouth and wrap a rope around her neck ..."
    wt_image b_clerk_degraded_2
    "... which you use to lash her neck to the floor, turning her face so that she's looking up at you."
    "She's now ready for you to relieve yourself on her, however you see fit."
    return

# Use Her Degraded
label bree_use_her_degraded:
    $ bree.training_session()
    wt_image b_clerk_degraded_1
    "It may say something about you that in her current condition, you can still see [bree.name] as a possible source of sexual satisfaction."
    wt_image b_clerk_degraded_3
    "The only part of her you enter any more is her ass.  You turn her around to unchain her.  She's always docile as you do so, perhaps anticipating the perverted mating to come."
    wt_image b_clerk_anal_13
    "She growls as you penetrate her, either in discomfort or satisfaction, or perhaps both."
    bree.c "rrrrrhhh"
    wt_image b_clerk_degraded_4
    "You turn her around before you cum. She doesn't look away, doesn't even close her eyes, as you cover her face with your sperm. Her open mouth happily swallows everything that lands inside it."
    player.c "[player.orgasm_text]"
    $ bree.sex_count += 1
    $ bree.facial_count += 1
    orgasm notify
    return

# Let Her Cum Degraded
label bree_let_her_cum_degraded:
    $ bree.training_session()
    wt_image b_clerk_stick_4
    "[bree.name] gets highly agitated when she goes too long between orgasms. To help deal with her in this condition, you attached a thick dildo to the end of a large stick.  A calm comes over her face as soon as you bring it out.  She happily lets you tie her into position ..."
    wt_image b_clerk_stick_1
    "... so that you can insert the stick inside her."
    bree.c "nnnn"
    wt_image b_clerk_stick_5
    "Using both hands, you ram the stick dildo in and out of [bree.name]'s cunt as she grunts and pants ..."
    wt_image b_clerk_stick_2
    "... deep guttural sounds escape from her throat every time you slam the instrument into her ..."
    bree.c "uuuggghhh  ...  uuuggghhh"
    wt_image b_clerk_stick_3
    "... but the most animal like sounds she makes are the growls she lets loose as she reaches orgasm."
    bree.c "YOOAAAWWWW!!!!"
    wt_image b_clerk_stick_6
    "It's hard work on your part getting her to this point, but it's worth it for the docile and content look on her face as the orgasm subsides and you re-chain her into her normal position."
    change player energy by -energy_short notify
    return

## petgirl Actions
# Fetch
label bree_play_fetch:
    $ bree.training_session()
    wt_image b_clerk_fetch_2
    "[bree.name] happily chases the ball."
    wt_image b_clerk_fetch_3
    "You were worried she might run off with it, but the joy of the chase is so strong she happily brings it back for you to throw again."
    wt_image b_clerk_fetch_1
    "Soon, she's so exhausted from chasing the ball she curls up in a ball herself, watching you happily from the basket.  You'll put her back in her cage in a little while - you don't yet trust her around the house unsupervised - but for now its nice to give her some quiet time with you."
    change player energy by -energy_very_short notify
    return


## Club Actions
# Bree Watch Her
label bree_watch_her:
    add tags 'watched_today' to bree
    $ bree.random_number = renpy.random.randint(1,10)
    if bree.random_number < 5:
        wt_image b_clerk_maid_1_2
        "None of the Club members are paying much attention to [bree.name] today.  She goes about her cleaning, glancing back at you from time to time."
        "It's hard to know exactly what she's thinking.  She may have a hard time explaining it herself."
        "She doesn't like being made to do menial work, yet she likes that you make her do something she doesn't like because it amuses you.  She hates that you're putting her on display, yet she likes that you'll publicly show off that she belongs to you."
        "All relationships can be complicated and weird sometimes, D/s relationships particularly so."
    elif bree.random_number < 8:
        wt_image b_clerk_maid_1_3
        "One of the Club members has taken an interest in [bree.name], although she clearly has no interest in him."
        "She's quite capable of handling unwanted attention. She's been doing it since she reached puberty. There's no need for you to intervene - unless you want him to get a better show."
        $ title = "Intervene?"
        menu:
            "Tell her to show him what he wants to see":
                wt_image b_clerk_maid_1_1
                player.c "He's trying to see your tits. Give him a proper look."
                "She looks at you for a moment ..."
                wt_image b_clerk_maid_1_4
                "... then pulls her top down, exposing her breasts."
                $ title = "What now?"
                menu:
                    "She can get back to work":
                        "That's enough.  Get back to work."
                        wt_image b_clerk_maid_1_2
                        "She does so, humiliated at being exposed, and a little bit pleased that you made her expose herself for your amusement."

                    "She should finish cleaning like this":
                        "Finish your shift like this. That way you don't need to waste time pulling your top down for the next member who wants to see your tits."
                        wt_image b_clerk_maid_1_5
                        "She's humiliated at being exposed like this, and a little bit pleased that you made her expose herself for your amusement."
                        $ bree.change_image('b_clerk_maid_1_5')
                        add tags 'maid_exposed_today' to bree

                    "Let him touch her":
                        wt_image b_clerk_maid_1_5
                        "Ignoring her, you turn to the Club member."
                        player.c "You can touch them if you want."
                        wt_image b_clerk_maid_1_6
                        "He gives them a thorough examination and a good squeeze before letting [bree.name] get back to her work."

                    "Tell her to blow him":
                        wt_image b_clerk_maid_1_5
                        "He might like your tits.  Get on your knees and offer to blow him, in case you've turned him on."
                        wt_image b_clerk_maid_1_7
                        bree.c "My owner wants to know if you would like me to suck your dick?"
                        breeclubman "Okay, but make it quick.  You have work to do, and I don't want Gloria mad at me because you're slacking off."
                        wt_image b_clerk_maid_1_8
                        "[bree.name] knew that serving other men was part of the deal.  You made that quite clear before she offered you her submission.  She might not have expected you to offer her services in quite so public a location, but at least she was told to make it quick."
                        "That she is quite capable of doing, using her talented mouth to extract his sperm in short order."
                        breeclubman "Mmmmm.  Nice."
                        wt_image b_clerk_maid_1_7
                        player.c "Get back to work, [bree.name], and don't turn on any other members today."
                        wt_image b_clerk_maid_1_2
                        "There's nothing quite so chauvinistic as blaming a woman for the way a man responds to her body.  Since you'd also chastise her for not wearing the skimpy outfit or looking sexy, your instruction is also hypocritical, putting her in a no win situation that her submissive brain finds ridiculously arousing."
            "Do nothing":
                wt_image b_clerk_maid_1_1
                "After she sends him away, she looks at you, as if to say 'this is what you're making me put up with'."
    else:
        $ breeclubwoman.location = club
        wt_image b_clerk_maid_2_1
        "Whatever their other qualities, some women are drawn to putting themselves at the top of the social pecking order at the expense of other women.  Dressed as a maid, [bree.name] is usually ignored by such women, who are more concerned about their status vis-a-vis the other Club members than they are with a servant who's already clearly at the bottom of the social order."
        "Every once in a while, however, one of the women takes liberties with [bree.name], either because it gives them a little ego boost, or they find her cute and it makes them wet between the legs to put her in her place.  [bree.name] isn't as good at handling herself around these women as she is with men.  Maybe it's because she hasn't had as much experience fending off unwanted female attention.  Or maybe it's because she gets a taboo thrill at being dominated by a woman she just met."
        "Either way, right now she's caught like a deer in the headlights as a Club member chastises her for sloppy cleaning.  Nothing's going to happen if you leave them alone, other than the Club member will have the satisfaction of making [bree.name] feel small and [bree.name] will have the humiliating satisfaction of being made to feel small."
        $ title = "Intervene?"
        menu:
            "Ask what's wrong":
                wt_image b_clerk_maid_2_2
                player.c "Is there a problem with her work?"
                breeclubwoman.c 'She was supposed to clean the table I was sitting at, and she left almost as much dust on it when she was "finished" as there was when she started.'
                wt_image b_clerk_maid_1_9
                player.c "Is this true?"
                bree.c "I missed a spot, [bree.your_respect_name].  I was rushing because I didn't want to disturb her and her friend.  I'm sorry, [bree.your_respect_name]."
                $ title = "What now?"
                menu:
                    "Turn the tables" if player.test('hypnosis_level', 1):
                        wt_image b_clerk_maid_2_2
                        "Perhaps my slave can make amends. Let's you and I discuss in private how she could make it up to you."
                        wt_image b_clerk_maid_2_17
                        breeclubwoman.c "Okay"
                        wt_image b_clerk_maid_2_18
                        "You accompany her to a private room, where you take out your focus."
                        wt_image b_clerk_maid_2_19
                        player.c "Look at this, please."
                        breeclubwoman.c "What is ..."
                        call focus_image from _call_focus_image_39
                        player.c "Just look at this and listen to my voice. You and I are going to talk. We are going to talk and you are going to listen to me. Listen to me. Listen to my voice. Only my voice. Only my voice now."
                        wt_image b_clerk_maid_2_11
                        player.c "There's no need for you to wear so many clothes, you're proud of your body."
                        breeclubwoman.c "Yes"
                        wt_image b_clerk_maid_2_12
                        player.c "Show it off to me. You want to show me your bare breasts and sexy body while we talk. You want me to be impressed by how beautiful you are."
                        breeclubwoman.c "Yes"
                        wt_image b_clerk_maid_2_13
                        player.c "You're beautiful, aren't you?"
                        breeclubwoman.c "Yes"
                        player.c "Beauty is one of the ways women judge each other, isn't it?"
                        breeclubwoman.c "Yes"
                        player.c "You like it when other women accept you as their social superior."
                        breeclubwoman.c "Yes"
                        player.c "You should use your beauty to show other women they are inferior to you."
                        breeclubwoman.c "I do."
                        player.c "You should do more. You should show them just how beautiful you really are. Your pussy is beautiful. Its more beautiful than the pussies of other women. You should show the other women in the Club how beautiful your pussy is. You should tell them how much prettier your pussy is than theirs."
                        breeclubwoman.c "Should I?"
                        player.c "If you want them to recognize you as their social superior, yes, you should."
                        wt_image b_clerk_maid_2_14
                        breeclubwoman.c "Okay"
                        "She leaves, heading back to the common area of the Club. You follow a few minutes later."
                        wt_image current_location.image
                        notify
                    "Tell her to get back to work":
                        player.c "Get back to work, and do better next time."
                        wt_image b_clerk_maid_1_10
                        bree.c "Yes, [bree.your_respect_name]"
                        "You can't criticize another Club member in front of the serving staff. This is as much as you can do to let [bree.name] know you're taking her side. She understands that, and does her best to stifle a grin as she leaves."
                        call character_location_return(breeclubwoman) from _call_character_location_return_217
                    "Suggest she be punished":
                        wt_image b_clerk_maid_1_4
                        player.c "Sorry's not good enough.  Strip, then turn around and present your bare ass."
                        wt_image b_clerk_maid_1_11
                        "Part of the Club rule against fraternizing with your own partner when you've assigned her to serve is that you also can't discipline her.  You turn to the other woman."
                        wt_image b_clerk_maid_2_2
                        player.c "Would you care to do the honors?"
                        breeclubwoman.c "My pleasure."
                        wt_image b_clerk_maid_1_11
                        "*smack* ... *smack* ... *smack*  ...  The woman probably thinks she's being hard on [bree.name], but compared to the punishments you put her through, this is a walk in the park.  Still, punishment is less about the physical and much more about the mental. Being spanked in public by a strange woman because she couldn't properly clean a table is intensely humiliating in a way a truly sore bottom could never be."
                        call character_location_return(breeclubwoman) from _call_character_location_return_218
                    "Suggest they kiss and make up":
                        player.c "Tell the lady you're sorry."
                        bree.c "I'm sorry, Ma'am.  I should have done a better job."
                        player.c "Tell her you'll do better next time."
                        bree.c "I promise I'll do a better job of cleaning your table the next time, Ma'am."
                        player.c "Now kiss her to show you're grateful she took the time to point out your flaws."
                        wt_image b_clerk_maid_2_3
                        "Satisfied by [bree.name]'s show of subordination, the Club member seems ready and willing to accept the kiss."
                        $ title = "Is this right?"
                        menu:
                            "Let them make out":
                                wt_image b_clerk_maid_2_4
                                "[bree.name] doesn't dare break the kiss until the other woman does or you tell her she's allowed to."
                                "Since the Club member isn't in any rush to end things, you settle back and watch your slave make out with the woman who just finished humiliating her."

                            "Remind your slave of her place":
                                player.c "Not like that.  You're not her equal."
                                wt_image b_clerk_maid_2_5
                                "[bree.name] lowers her head and obsequiously licks at the other woman's neck and chin, like a puppy seeking forgiveness."
                                "The Club member isn't quite sure what to make of it, but you get the impression she'd like to receive [bree.name]'s kisses lower still.  Perhaps another time."
                        call character_location_return(breeclubwoman) from _call_character_location_return_219
                    "Suggest she serve the Club member":
                        player.c "Tell the lady you're sorry and offer to make it up to her."
                        bree.c "I'm sorry, Ma'am.  What can I do to make it up to you?"
                        wt_image b_clerk_maid_2_2
                        breeclubwoman.c "What are you offering? I'm not interested in more of your cleaning. Unless, that is, you intend to do the cleaning with your mouth?"
                        wt_image b_clerk_maid_1_9
                        bree.c "Yes, Ma'am. That's what my owner would like me to offer to you."
                        wt_image b_clerk_maid_2_2
                        breeclubwoman.c "Interesting. How big of a slut are you? Is it just my pussy you're hoping to clean, or are you prepared to clean my other hole?"
                        "A shocked [bree.name] looks to you for guidance. You ignore her while you size up the Club member."
                        $ title = "What do you decide?"
                        menu:
                            "Pussy only":
                                wt_image b_clerk_maid_2_19
                                player.c "I don't think it was that big an offense."
                                wt_image b_clerk_maid_2_20
                                "The Club member chuckles."
                                breeclubwoman.c "I wasn't sure how depraved she is. Okay, I'll accept a pussy licking as your apology for being a sloppy maid. Come here and lie down."
                                wt_image b_clerk_maid_2_7
                                "The woman straddles [bree.name]'s face, her position a physical manifestation of the dominant social status she so enjoys demonstrating."
                                "[bree.name] makes no objection to being used this way. You made it clear, before you accepted her submission, that you would make her available to women when the mood strikes you. Her own sexuality in this regard is a bit of a mystery. She doesn't seem to respond physically to other women, but she responds to domination. You don't think she would ever be happy belonging to a Domme, but she responds well to being shown that she's below other women in your eyes."
                                "Right now, the Club member is responding well to it as well, flooding your slave's face with her pussy juice as she bucks to an orgasm."
                                breeclubwoman.c "Oh, yes!  Lick me, you fucking whore!!  Aaahhhhhh!!!"
                            "Ass cleaning it is":
                                wt_image b_clerk_maid_2_17
                                player.c "Let's do this in private."
                                "Asking [bree.name] to rim someone where anyone walking through the Club could see her is a bit more humiliation than even she's ready for."
                                breeclubwoman.c "Of course."
                                wt_image b_clerk_maid_2_18
                                "The Club member leads the way, with [bree.name] following behind."
                                wt_image b_clerk_maid_2_8
                                "Once you're in a private room, the Club member strips. A close up view of her tits seems to be her 'thank you' to you for the use of her slave."
                                wt_image b_clerk_maid_1_9
                                "You turn to [bree.name]."
                                wt_image b_clerk_maid_1_12
                                player.c "You don't get to wear clothes when another woman has removed hers around you."
                                wt_image b_clerk_maid_2_9
                                "A now naked [bree.name] positions herself behind the other woman. You made it clear, before you accepted her submission, that you would make her available to women when the mood strikes you. You didn't clarify how those women could use her, but you know she'll accept anything that doesn't cause her harm. In some ways, the more humiliating the use the better. She responds well to being shown that you view her as ranking below other women."
                                "A quick glance back at your face before she buries her tongue in the Club member's ass confirms that you're enjoying seeing her humiliating this way, and that's enough for [bree.name] to feel good about being made to feel so insignificant."
                                wt_image b_clerk_maid_2_10
                                "You're not sure how often the Club member has had her ass eaten, but you suspect she'll be looking for more such opportunities in the future.  She doesn't quite cum from the feel of your slave's tongue in her ass, but she gets really close. Close enough that it takes only a small touch on her sex to take her over the edge."
                                breeclubwoman.c "Fingers, you fucking whore!!  Rub my cunt with your fingers.  Oh, yes!  Aaahhhhhh!!!"
                                wt_image b_clerk_maid_1_11
                                player.c "You have more cleaning to do back in the public area."
                                wt_image b_clerk_maid_1_2
                                "A thoroughly humiliated and unmistakably aroused [bree.name] dresses and returns to her maid's duties."
                                if bree.maintain_week_sg < week + 2:
                                    $ bree.maintain_week_sg = week + 2
                        call character_location_return(breeclubwoman) from _call_character_location_return_220
            "Do nothing":
                wt_image b_clerk_maid_1_2
                "When the tongue lashing is finished, [bree.name] gets back to work."
                "It's hard to know exactly what she's thinking.  She'd like you to believe that she's only doing this for you, and that's true, to the extent that she wouldn't be dressed this way and accepting verbal discipline from women she doesn't know if you hadn't put her in this situation."
                "How much she enjoys being at the bottom of the female pecking order is harder to ascertain.  She may not truly know herself."
                call character_location_return(breeclubwoman) from _call_character_location_return_221
    return

########### OBJECTS ###########
## Common Objects
# View Relationship Status
label bree_relationship_status:
  wt_image bree.image
  if bree.has_tag('slavegirl'):
    if bree.has_tag('allowed_to_talk'):
      "[bree.full_name] is allowed to talk.{nw}"
    else:
      "[bree.full_name] is not allowed to talk except when spoken to.{nw}"
    if bree.has_tag('allowed_to_cum'):
      extend "\nShe is allowed to have orgasms.{nw}"
    elif bree.has_tag('allowed_to_beg'):
      extend "\nShe has permission to beg for orgasms.{nw}"
    else:
      extend "\nShe is not allowed to cum.{nw}"
    $ bree.temporary_count = bree.maintain_week_sg - week
    if bree.temporary_count > 2:
      extend "\nShe is happy with your relationship."
    elif bree.temporary_count > 0:
      extend "\nShe wishes you would spend more time with her."
    elif bree.has_tag('love_potion_used'):
      extend "\nShe feels like she never gets to spend time with you, but the lingering effects of the love potion make it impossible for her to contemplate leaving and not seeing you again."
    elif bree.temporary_count > -3:
      extend "\nShe's unhappy with your lack of attention and is considering leaving you."
    else:
      extend "\nShe feels ignored and plans to leave you unless you do something with her soon."
  wt_image current_location.image
  return

# Review Files
label bree_review_files:
    call bree_description_display from _call_bree_description_display_1
    wt_image current_location.image
    return

# Description Display
label bree_description_display:
    wt_image b_clerk_working_10
    if bree.status == "unavailable":
        ## main description
            "Bree wants nothing to do with you."
    return

## Character Specific Objects
# Note From Bree
label notefrombree_examine:
    wt_image note_from_bree_1
    "Bree left you a note."
    return

label notefrombree_read:
    wt_image note_from_bree_1
    bree.c "{i}[bree.your_respect_name], I know I'm not to speak without permission, and I don't know if you will give me permission to speak this visit or not.{/i}"
    bree.c "{i}I want you to know that I spoke to my manager about you, and told him what a great customer you are.  He agreed that you can have a 50 percent discount on all future purchases.{/i}"
    bree.c "{i}I hope you're pleased, [bree.your_respect_name]. ~ Bree{/i}"
    if bree.location == steel_trap:
        player.c "Yes girl, I'm pleased.  Thank you for doing this."
        "Bree blushes slightly."
    $ steel_trap.discount_ratio = 0.5
    rem 1 note_from_bree from current_location notify
    return

# Demonstrate - Butt Plug
label bp_tst_demonstration:
  if bree.location == steel_trap:
    if bree.submit_count > 4 or bree.hypno_count > 2:
      wt_image b_clerk_butt_plug_1
      "It's not sanitary to sell plugs that have been used, so Bree gets her bag and retrieves her favorite butt toy.  She must use it frequently, because she lubes it up just with saliva."
      wt_image b_clerk_butt_plug_2
      "She grins when she sees your surprise at how easily she can move it in and out of her rosebud."
    else:
      "[bree.full_name] is not prepared to give you a personal demonstration of how her store's items work.  At least not yet."
  else:
    "[bree.full_name] is not around to give you a demonstration of how her store's items work."
  return

# Demonstrate - Chastity Belt
label cb_tst_demonstration:
  if bree.location == steel_trap:
    if bree.submit_count > 4 or bree.hypno_count > 2:
      wt_image b_clerk_chastity_belt
      "Bree fumbles around trying to put the chastity belt on.  Perhaps this is the one item in the store she hasn't tried out on her own?"
      "Eventually, with your assistance, you're able to lock the belt snugly in place.  A check with your fingers confirms that nobody is getting inside now without the key."
    else:
      "[bree.full_name] is not prepared to give you a personal demonstration of how her store's items work.  At least not yet."
  else:
    "[bree.full_name] is not around to give you a demonstration of how her store's items work."
  return

# Demonstrate - Floggers and Paddles
label fl_tst_demonstration:
  if bree.location == steel_trap:
    if bree.submit_count > 4 or bree.hypno_count > 2:
      wt_image b_clerk_backside
      "Bree gamely offers you her backside as a target for the store's various floggers, paddles and crops."
      wt_image b_clerk_gag_1
      "Just as you're about to start, you tell her you had better gag her so as not to disturb anyone walking by outside."
      wt_image b_clerk_flogged
      "Once you have the ball gag firmly in place, you ignore her ass and move around to her front. She grimaces when she understands your intent, but lets you use her breasts as your target. *thwapp*"
      bree.c "Mmmmppphhh"
    else:
      "[bree.full_name] is not prepared to give you a personal demonstration of how her store's items work.  At least not yet."
  else:
    "[bree.full_name] is not around to give you a demonstration of how her store's items work."
  return

# Demonstrate - Gags
label ga_tst_demonstration:
  if bree.location == steel_trap:
    if bree.submit_count > 4 or bree.hypno_count > 2:
      wt_image b_clerk_gag_1
      "You tell Bree you want to see how well her ball gags work.  She obediently opens her mouth. "
      wt_image b_clerk_gag_2
      "You're able to adjust the straps quite easily.  There's no way she can get the gag out on her own, and while it's in there, she can't make any sound louder than a soft moan."
    else:
      "[bree.full_name] is not prepared to give you a personal demonstration of how her store's items work.  At least not yet."
  else:
    "[bree.full_name] is not around to give you a demonstration of how her store's items work."
  return

# Demonstrate - Fuck Machine
label fm_tst_demonstration:
  if bree.location == steel_trap:
    if bree.submit_count > 4 or bree.hypno_count > 2:
      wt_image b_clerk_machine_1
      "Bree seems to know right away how to adjust the settings to fit her.  You expect this isn't the first time she's used the device, but it may well be the first time she's done so with anyone watching."
      wt_image b_clerk_machine_7
      "She bites her lip and tries not to show any emotion as her pussy is reamed to the sound of the steady *whump* *whump* *whump* of the machine's motor."
      wt_image b_clerk_machine_8
      bree.c "That's enough."
      $ title = "What do you do?"
      menu:
          "Let her get up":
              pass
          "Tell her a few minutes more":
              wt_image b_clerk_machine_9
              player.c  "Just a couple of minutes more."
              "The machine keeps up it's steady *whump* *whump* *whump*."
              wt_image b_clerk_machine_10
              bree.c "oohhh ... I'd better ..."
              player.c "Just another minute, Bree."
              wt_image b_clerk_machine_11
              bree.c "ooohhhh ...  oooohhhhh ..."
              wt_image b_clerk_machine_12
              bree.c "OOOHHHHH!!"
              "The machine seems to do what it says it does, and rather well.  An embarrassed Bree disappears to clean herself up."
              wt_image current_location.image
    else:
      "[bree.full_name] is not prepared to give you a personal demonstration of how her store's items work. At least not yet."
  else:
    "[bree.full_name] is not around to give you a demonstration of how her store's items work."
  return

# Demonstrate - Suspension Gear
label sg_tst_demonstration:
  if bree.location == steel_trap:
    if bree.submit_count > 4 or bree.hypno_count > 2:
      wt_image b_clerk_suspension_gear
      "Bree instructs you on how to use the suspension pulleys to safely lift her up and off the ground. Looking at her dangling helplessly, you understand why some people would want to install this gear in their homes."
    else:
      "[bree.full_name] is not prepared to give you a personal demonstration of how her store's items work.  At least not yet."
  else:
    "[bree.full_name] is not around to give you a demonstration of how her store's items work."
  return

## Items
# Give Butt Plug
label give_bp_bree:
    if bree.has_tag('degraded') or bree.has_tag('petgirl'):
        "She's gone far beyond ass play at this stage.  Better save this for a client."
    elif bree.has_tag('slavegirl'):
        "She already owned one even before she became your slavegirl. You can save this for a client."
    else:
        "She's already bought one for herself.  Save this for someone else."
    return

#label give_bp_breemaid:
    #"Wait until the two of you are home before trying to give her anything."
    #return

# Give Chastity Belt
label give_cb_bree:
    if bree.has_tag('degraded') or bree.has_tag('petgirl'):
        "She's past the point of playing with herself at this stage.  Better save this for someone else."
    elif bree.has_tag('slavegirl'):
        "She's too obedient to touch herself or let someone else touch her when you're not around."
    else:
        "You should save this for a client."
    return

#label give_cb_breemaid:
    #"Wait until the two of you are home before trying to give her anything."
    #return

# Give Dildo
label give_di_bree:
    if bree.has_tag('degraded') or bree.has_tag('petgirl'):
        "She's past the point of playing with herself at this stage. Better save this for someone else."
    elif bree.has_tag('slavegirl'):
        "She's way too sexually stimulated as it is from the act of submitting to you. She doesn't need additional stimulation."
    else:
        "You should save this for a client."
    return

#label give_di_breemaid:
    #"Wait until the two of you are home before trying to give her anything."
    #return

# Use Fetch Toy
label use_ft_bree:
  if bree.has_tag('petgirl'):
    wt_image b_clerk_fetch_2
    "[bree.name] happily chases the ball."
    wt_image b_clerk_fetch_3
    "You were worried she might run off with it, but the joy of the chase is so strong she happily brings it back for you to throw again."
    wt_image b_clerk_fetch_1
    "Soon, she's so exhausted from chasing the ball she curls up in a ball herself, watching you happily from the basket.  You'll put her back in her cage in a little while - you don't yet trust her around the house unsupervised - but for now its nice to give her some quiet time with you."
    change player energy by -energy_very_short
    give 1 fetch_toy from player to bree notify
  else:
    "You shouldn't try to play fetch with someone who isn't your pet."
  return

#label use_ft_breemaid:
    #"Wait until the two of you are home before trying to give her anything."
    #return

# Give Jewelry
label give_jwc_bree:
  "Save this as a gift for [chelsea.name]."
  return

# Use Leash
label use_le_bree:
  if bree.has_tag('petgirl'):
    wt_image b_clerk_cage_2
    "[bree.name] watches warily as you approach her cage. She loves to go for walks, but hates the leash, and hasn't yet reconciled this conflict."
    "You have to be careful opening the cage, or she'll run off before you can attach the leash."
    wt_image b_clerk_walk_1
    "With the leash safely snapped in place, you lead [bree.name] away from her cage."
    "She'll test you at least once on your walk, to see if she can get away.  For the moment, though, she follows docilely behind you."
  elif current_location == club and bree.has_tag('club_maid'):
    "Owners aren't supposed to have contact with their submissives they send to work at the Club. Not even to take them for a walksy."
  else:
    "[bree.name] would probably love it if you took her for a walk on a leash, so let's hope this scene gets added to the game soon."
  return

#label use_le_breemaid:
    #"Owners aren't supposed to have contact with the submissives they send to the Club.  Not even to take them for a walksy."
    #return

# Give Lingerie
label give_li_bree:
    if bree.has_tag('degraded') or bree.has_tag('petgirl'):
        "She's past the point of wearing clothes at this stage.  Better save this for a client."
    elif bree.has_tag('slavegirl'):
        "A cuffs and matching collar are the only lingerie she needs."
    else:
        "You should save this for a client."
    return

#label give_li_breemaid:
    #"Wait until the two of you are home before trying to give her anything."
    #return

# Give Love Potion
label give_lp_bree:
  if bree.has_tag('love_potion_used'):
    "You've already used a love potion on her.  Another one won't have any effect."
  else:
    if bree.has_tag('degraded') or bree.has_tag('petgirl'):
      "Her current mental state isn't susceptible to human notions of love."
    elif bree.has_tag('slavegirl') and current_location == bedroom:
      "[bree.name] is already your devoted slavegirl.  Do you really want to use  love potion on her and deepen her infatuation with you?"
      $ title = "Use love potion on her?"
      menu:
        "Yes":
          wt_image b_clerk_gratitude
          player.c "I brought you something to drink, [bree.name]."
          bree.c "Thank you, [bree.your_respect_name].  I'm not thirsty right now."
          player.c "I didn't ask if you were thirsty.  I said I have something for you to drink."
          bree.c "Yes, [bree.your_respect_name]."
          "She obediently drinks the mixture of potion and water."
          wt_image b_clerk_looking_up
          "The potion takes effect quickly.  You can see her struggling to control herself from speaking without permission.  But the effect of the potion is too strong, and she blurts out her feelings, unable to keep them bottled up."
          bree.c "Thank you for the drink, [bree.your_respect_name]!  Thank you for owning me!!  I'm the luckiest slave in the world!!"
          add tags 'love_potion_used' to bree
          rem 1 love_potion from player notify
        "No, save it":
          pass
    elif bree.has_tag('club_maid') and current_location == club:
      "She's not allowed to have a drink when she's supposed to be working."
    else:
      "Best to save this for a paying client."
  return

#label give_lp_breemaid:
    #"Wait until the two of you are home before trying to give her anything."
    #return

# Give Transformation Potion
label give_tp_bree:
    if bree.has_tag('transformed'):
        "Bree has already been transformed.  The potion can do nothing more to her now."
    elif bree.location == bedroom:
        $ bree.temporary_count = 1
        wt_image b_clerk_gratitude
        "She gave you control over her body, trusting you to keep her safe and sculpt her into the person you think she should be.  You're about to change her more than she anticipated."
        player.c "I brought you something to drink, [bree.name]."
        bree.c "Thank you, [bree.your_respect_name].  I'm not thirsty right now."
        player.c "I didn't ask if you were thirsty.  I said I have something for you to drink."
        bree.c "Yes, [bree.your_respect_name]."
        "She obediently drinks the mixture of potion and water."
        wt_image b_clerk_transform
        "The potion takes effect quickly, opening her up to the potential for great change."
        "Bree dreamed of becoming a treasured submissive, graceful and slutty by turns, depending on what her Master demanded of her.  In her darkest fantasies, however, she also imagined being something ... less.  Less human.  Less worthy of respect or consideration."
        "The potion latches on to these fantasies, ready to inflate them from inspiration for masturbation into the core of her being."
        "You now need to spend some energy, directing the potion on what changes you want it to make in her."
        $ title = "What to you want her to be?"
        menu:
            "Petgirl":
                "On rare occasions, Bree would fantasize about being someone's pet, and masturbate to the thought of being treated like an animal."
                "Those random thoughts have turned into the sole purpose for her existence.  She is an animal, and needs to be treated as one.  It's all she can imagine ever being."
                wt_image b_clerk_cage
                "You lead her over to her new cage.  You'll need to keep her here at least until she's house trained."
                $ bree.transformed_via_object = True
                call bree_convert_petgirl from _call_bree_convert_petgirl
            "Degraded":
                "In her darkest moments, Bree would masturbate to the thought of being treated in ways she could never admit to anyone.  They weren't things she ever wanted to experience, but when she was in a particular mood, the thought of them would make her wet."
                "Now, it's the only thing that gets her wet.  It's the only thing that makes her feel alive.  She doesn't feel human.  She can't stand anyone trying to treat her like one.  She needs to be treated as ... nothing.  It's the only way she feels anything."
                call forced_movement(basement) from _call_forced_movement_78
                summon bree
                wt_image b_clerk_degraded_1
                "You drag her down into the basement."
                "For her own safety, you place her in a straightjacket and chain her in place. Then you gag her to keep her from disturbing the rest of the household.  As an afterthought, you place a litter box beside her.  Now she can decide if she wants to sit in her own filth or not."
                $ bree.transformed_via_object = True
                call bree_convert_degraded from _call_bree_convert_degraded
                call character_location_return(bree) from _call_character_location_return_222
            "Nothing (undo)":
                $ bree.temporary_count = 0
                "Let's just pretend that didn't happen.  That's easier than reloading an old save."
        if bree.temporary_count == 1:
            $ bree.temporary_count = 0
            rem 1 transformation_potion from player
            change player energy by -energy_long notify
    elif bree.has_tag('club_maid') and current_location == club:
        "She's not allowed to have a drink when she's supposed to be working."
    else:
        "Not here.  Not now."
    return

# Give Ring of Secuality
label give_rs_bree:
    "This may work, but there's no content for her.  You should save this for someone else."
    return

# Use Water Bowl
label use_wb_bree:
  if bree.has_tag('petgirl'):
    wt_image b_clerk_cage_2
    "[bree.name] watches you as you approach her cage with the full bowl of water."
    wt_image b_clerk_nuzzle
    "When you let her out of her cage, she nuzzles up against your leg.  She still bites and scratches from time to time, so you've taken to binding her when she's out of her cage, but she's coming to recognize you as her alpha male, and is making an effort to get on your good side."
    wt_image b_clerk_water_bowl_1
    player.c "Stay, girl.  Stay."
    "[bree.name] watches you put the bowl down, her gaze shifting back and forth from the bowl to you.  She wants to run forward to it, but she's learned that makes you unhappy.  She's also learned that when you're unhappy, you discipline her, and she doesn't want that."
    "But she does want to drink from the bowl, so badly that she twitches as she tries to hold herself back."
    wt_image b_clerk_water_bowl_2
    player.c "Drink girl."
    "She dives forward..."
    wt_image b_clerk_water_bowl_3
    "...and starts happily lapping up the water you've brought her."
  elif bree.has_tag('club_maid') and current_location == club:
    "She's not allowed to have a drink when she's supposed to be working. Not even when she's being a good girl."
  else:
    "You shouldn't offer water in a bowl to anyone who isn't your pet."
  return

#label use_wb_breemaid:
    #"Owners aren't supposed to have contact with the submissives they send to the Club."
    #return

# Use Will Tamer
label use_wt_bree:
    if bree.has_tag('transformed'):
        "Bree has already been transformed.  The potion can do nothing more to her now."
    elif bree.has_tag('will_tamer_this_week'):
        "You've already used the Will_Tamer her on this week.  The re-wiring of her brain it has started will take some time to complete.  Try again next week."
    elif bree.location == bedroom:
        # first use
        if bree.will_tamer_count == 0:
            add tags 'will_tamer_this_week' to bree
            $ bree.will_tamer_count = 1
            wt_image b_clerk_head_bowed_1
            "[bree.name], I have a new collar for you to wear."
            "She trembles a little and bows her head as you show her the Will-Tamer.  The act of being collared always provides her with a combination of excitement and deep contentment."
            "Unknown to her, this particular collar will induce a much deeper submission than she has ever experienced before."
            wt_image b_clerk_collar_1
            "[bree.name]'s eyes widen as you snap the Will-Tamer in place.  She's naturally submissive, and therefore naturally wired to respond to the impulses the Will-Tamer creates."
            wt_image b_clerk_collar_2
            "In a matter of seconds, her jaw is hanging slack, her eyes starting to deaden."
            "She's already a slavegirl.  The Will-Tamer goes to work eroding all sense of independence and humanity that still form a part of her personality."
            "You leave it on for only a few minutes.  Any longer and her brain will be fried.  The changes it has made in her will continue to re-shape her thinking over the next few days."
            "By next week, if you want, you can use the Will-Tamer on her again.  If you do, the slavegirl you know now will be gone, replaced by something ... less human."
        # second and final use
        else:
            "Using the collar on [bree.name] once has left her more docile, less likely to use her own initiative on anything, looking solely to you for direction on nearly every matter."
            "If you put it on her a second time, the slavegirl you know now will be gone, replaced by something ... less human."
            "You will also lose the Will-Tamer, as it will be absorbed into and form part of her new personality."
            $ title = "Use the Will-Tamer on her again?"
            menu:
                "Yes":
                    rem 1 will_tamer from player
                    wt_image b_clerk_head_bowed_1
                    "She gave you control over her body, trusting you to keep her safe and sculpt her into the person she was meant to be.  You're about to change her more than she ever imagined."
                    player.c "[bree.name], it's time to wear your new collar again."
                    "She trembles even more than the first time as you show her the Will-Tamer.  Now its not just the act of being collared.  The changes the Will-Tamer made last time make her long for the feel of it around her neck again."
                    "You can smell her pussy juices as she bows her head, the mere sight of the Will-Tamer bringing her body to the verge of orgasm."
                    wt_image b_clerk_collar_1
                    "As you snap the collar in place, there's a momentary flash of fear in her eyes.  The part of her mind that wants to remain and independent, thinking human being recognizes the danger it is in."
                    wt_image b_clerk_collar_3
                    "Too late.  The feel of the collar wrapping around her neck triggers the most intensive orgasm she's ever experienced."
                    bree.c "OOOOHHHHHH!!!!"
                    "You need to quickly grab the back of her hair to prevent her from falling as the Will-Tamer takes her."
                    wt_image b_clerk_collar_4
                    "You continue to support her head as the Will-Tamer completes its re-wiring of the mind that was once Bree."
                    "Bree had become the treasured submissive she always imagined becoming, graceful and slutty by turns, depending on what you demand of her.  In her darkest fantasies, however, she also imagined being something ... less.  Less human.  Less worthy of respect or consideration."
                    "As the Will-Tamer completes its work, those dark fantasies are all that is left of the former Bree."
                    $ title = "What do you want her to be?"
                    menu:
                        "Petgirl":
                            "On rare occasions, Bree would fantasize about being someone's pet, and masturbate to the thought of being treated like an animal."
                            "Those random thoughts have turned into the sole purpose for her existence.  She is an animal, and needs to be treated as one.  It's all she can imagine ever being."
                            wt_image b_clerk_cage
                            "You lead her over to her new cage.  You'll need to keep her here at least until she's house trained."
                            $ bree.transformed_via_object = True
                            call bree_convert_petgirl from _call_bree_convert_petgirl_1

                        "Degraded":
                            "In her darkest moments, Bree would masturbate to the thought of being treated in ways she could never admit to anyone.  They weren't things she ever wanted to experience, but when she was in a particular mood, the thought of them would make her wet."
                            "Now, it's the only thing that gets her wet.  It's the only thing that makes her feel alive.  She doesn't feel human.  She can't stand anyone trying to treat her like one.  She needs to be treated as ... nothing.  It's the only way she feels anything."
                            call forced_movement(basement) from _call_forced_movement_79
                            summon bree
                            wt_image b_clerk_degraded_1
                            "You drag her down into the basement."
                            "For her own safety, you place her in a straightjacket and chain her in place. Then you gag her to keep her from disturbing the rest of the household.  As an afterthought, you place a litter box beside her.  Now she can decide if she wants to sit in her own filth or not."
                            $ bree.transformed_via_object = True
                            call bree_convert_degraded from _call_bree_convert_degraded_1
                            call character_location_return(bree) from _call_character_location_return_223

                "No":
                    "You decide you'd rather own the [bree.name] you know now, at least for a little while longer."
    elif not bree.has_tag('slavegirl'):
        "Submissives place great significance on collars.  You'll need the right time and place if you want to collar her."
    else:
        "Not here, not now."
    return

#label use_wt_breemaid:
    #"Owners aren't supposed to have contact with the submissives they send to the Club."
    #return

########### TIMERS ###########
## Common Timers
# Start Day
label bree_start_day:
    pass
    return

# End Day
label bree_end_day:
    rem tags 'maid_exposed_today' from bree
    if bree.has_tag('hypno_now'):
        rem tags 'hypno_now' from bree
    if bree.has_tag('submitting_now'):
        rem tags 'submitting_now' from bree
    rem tags 'in_club_now' 'watched_today' from bree
    call character_location_return(bree) from _call_character_location_return_224
    return

#label breemaid_end_day:
    #pass
    #return

label breeclubwoman_end_day:
    $ breeclubwoman.dismiss(False)
    return

# End Week
label bree_end_week:
    # limit bad habit training to once per week
    if bree.has_tag('bad_habit_trained_this_week'):
        rem tags 'bad_habit_trained_this_week' from bree
    # Relationship Maintenance
    if bree.has_tag('slavegirl'):
        # Warning Week
        if bree.maintain_week_sg == week:
            wt_image b_clerk_looking_up
            "[bree.name] approaches you.  It's clear from her face that she has something she wants to ask you."
            if bree.has_tag('allowed_to_talk'):
                 bree.c "You've given me permission to talk, [bree.your_respect_name], so I hope you don't mind if I say something."
                 bree.c "I know my role is to be available when you want to use me, and to wait patiently until that time.  It's just ... it's been so long since you used me."
                 bree.c "I miss your guidance, [bree.your_respect_name].  I hope I can serve you again soon, [bree.your_respect_name]."
            else:
                $ title = "What do you do?"
                menu:
                    "Give her permission to talk":
                        player.c "You have something you want to say?  Say it."
                        bree.c "Thank you, [bree.your_respect_name].  I know my role is to be available when you want to use me, and to wait patiently until that time.  It's just ... it's been so long since you used me."
                        bree.c "I miss your guidance, [bree.your_respect_name].  I hope I can serve you again soon, [bree.your_respect_name]."
                    "Ignore her":
                        "She knows her place.  Without your permission to speak, she waits silently and unhappily until you leave."
        # check for Leaving Week
        $ bree.temporary_count = bree.maintain_week_sg + 3
        if week >= bree.temporary_count:
            # love potion?
            if bree.has_tag('love_potion_used'):
                wt_image b_clerk_looking_up
                "[bree.name] looks at you, silently.  She looks miserable.  She's unhappy and lonely, but the love potion has her too infatuated with you to even think about leaving."
            else:
                wt_image note_from_bree_1
                "You find a note from [bree.name]"
                bree.c "Dear [bree.your_respect_name], I hope you'll forgive me leaving this way, but I couldn't bear to tell you in person.  I'm sorry that I wasn't a more appealing slavegirl for you, and that I couldn't have been of greater use to you."
                bree.c "I'm sorry, too, that I'm not better able to wait for you to give me your attention.  I know that you're a busy man with many responsibilities.  I'll always cherish our time together and the things you've taught me."
                bree.c "You're an amazing owner, and I know that I've been lucky to be able to share any of your time.  I'll always think fondly of you, but I need more frequent guidance and correction than you're able to provide."
                bree.c "I hope you'll wish me well, and think fondly of me from time to time, as I seek out a new owner, one who can spend more time providing me with the training and discipline I so desperately need."
                dismiss bree
                call convert(bree,'unavailable') from _call_convert_49  ## WARNING: be very careful with this command as it deletes all of her tags, except for permanent story tags
                wt_image current_location.image
    return

#label breemaid_end_week:
    #pass
    #return

label breeclubwoman_end_week:
    pass
    return


## Club and Stage Labels

label bree_club_call:
    # this runs when has tag 'can_be_in_club' and you enter the Club
    if player.has_tag('club_visited_today'):
        if bree.has_tag('in_club_now') and bree.has_tag('club_maid'):
            $ bree.location = club # returns her to club
    else:
        if bree.has_tag('club_maid'):
            $ bree.location = club
            add tags 'in_club_now' to bree
            if bree.club_reward_counter < 2:
                $ bree.club_reward_counter += 1
                if bree.club_reward_counter == 2:
                    $ club_president.rewards_pending += 1
    return

label bree_club_send_home:
    call character_location_return(bree) from _call_character_location_return_225
    return


## Loving Wife Content
label bree_sarah_positive_role_talk_slavegirl:
    if current_target.has_tag('slavegirl') and not sarah.has_tag(tag_expression):
        wt_image b_clerk_position_1
        "You order [bree.full_name] to join you.  A mischievous smile plays across her face, as she assumes she's here to join you and Sarah for a threesome."
        if bree.has_tag('allowed_to_talk'):
            bree.c "Yes, [bree.your_respect_name]?"
            wt_image lw_visit_2_2
            player.c "[bree.name], I'd like you to meet Sarah."
            sarah.c "Hi.  Wouldn't you be more comfortable on a chair?"
            wt_image b_clerk_position_1
            player.c "She can talk perfectly well from her knees.  [bree.name], Sarah's husband wants her to have sex with his friends.  She has concerns.  I thought speaking to another woman could help her."
            bree.c "I'll try, [bree.your_respect_name]."
        else:
            wt_image lw_visit_2_2
            player.c "[bree.name], I'd like you to meet Sarah."
            sarah.c "Hi.  Wouldn't you be more comfortable on a chair?"
            player.c "[bree.name], I'd like you to meet Sarah."
            wt_image b_clerk_position_1
            player.c "She can talk perfectly well from her knees.  [bree.name], Sarah's husband wants her to have sex with his friends.  She has concerns.  I thought speaking to another woman could help her."
            "She nods and turns to chat with Sarah, happy for the opportunity to exercise her vocal cords."
        wt_image lw_visit_2_2
        "Sarah has reservations about the conversation, but [bree.name] turns out to be a thoughtful and impassioned advocate of the contentment that comes from listening to and obeying the man you love.  At the same time, she's able to listen and empathize with Sarah's concerns."
        wt_image lw_visit_2_4
        sarah.c "Thank you for taking the time to chat with me.  I'm not sure that what works for you is the right thing for my husband and I, but I'll think about what we've talked about."
        add tags 'met_slavegirl_bree' 'positive_slavegirl_resolution_today' to sarah
    else:
        $ current_target = None
    return

label bree_sarah_positive_role_sex_slavegirl:
    player.c "[bree.name], come here and join us."
    wt_image b_clerk_position_1
    if current_target.has_tag('slavegirl'):
        if bree.has_tag('allowed_to_talk'):
            bree.c "Yes, [bree.your_respect_name]."
            player.c "You remember Sarah?"
            bree.c "Yes, [bree.your_respect_name]."
            player.c "You know Sarah's worried about having her husband watch her have sex. It's hard for her to imagine what that will be like, in part because she's never even seen two people have sex together. I'm going to fuck you, [bree.name], while Sarah watches us."
            bree.c "Yes, [bree.your_respect_name]."
        else:
            "She comes over and waits silently in front of you, awaiting permission to talk."
            player.c "You remember Sarah?"
            "She nods."
            player.c "You know Sarah's worried about having her husband watch her have sex. It's hard for her to imagine what that will be like, in part because she's never even seen two people have sex together. I'm going to fuck you, [bree.name], while Sarah watches us."
            "She nods again."
        wt_image lw_visit_4_2
        sarah.c "You can't be serious?"
        wt_image lw_visit_4_3
        player.c "I am.  You've never watched two people have sex.  Now you will.  It'll give you a chance to see that sex doesn't have to be private to be fun.  Have a seat and make yourself comfortable."
        wt_image b_clerk_lw_visit_1
        player.c "Let's get you prepared, [bree.name]."
        if bree.has_tag('allowed_to_talk'):
            bree.c "Yes, [bree.your_respect_name]."
        "You remove her clothes and wind a rope around her ..."
        wt_image b_clerk_lw_visit_2
        "... tie it off in back ..."
        wt_image b_clerk_lw_visit_3
        "... then roll her onto her side."
        player.c "Get me hard, [bree.name]."
        if bree.has_tag('allowed_to_talk'):
            bree.c "Yes, [bree.your_respect_name]."
        "You let her suck you for a few minutes, then move on to the main event."
        wt_image b_clerk_lw_visit_4
        "[bree.name] loves being used for your pleasure. She lets out a deep, satisfied moan as you penetrate her."
        bree.c "oooooohhhh"
        wt_image b_clerk_lw_visit_5
        if bree.has_tag('allowed_to_beg'):
            player.c "Remember, no cumming without permission, [bree.name].  Don't embarrass yourself or me in front of Sarah by not following orders."
        else:
            if bree.has_tag('allowed_to_cum'):
                player.c "Just for today, as a special treat for Sarah, you're going to control yourself, [bree.name], and not cum until I give you permission.  Don't embarrass yourself or me in front of Sarah by not following orders."
            else:
                player.c "Just for today, as a special treat for Sarah, I may give you the chance to have an orgasm, [bree.name], but no cumming until I give you permission.  Don't embarrass yourself or me in front of Sarah by not following orders."
            if bree.has_tag('allowed_to_talk'):
                bree.c "N ... no, [bree.your_respect_name]."
            else:
                "She nods vigorously in agreement."
        wt_image lw_visit_4_4
        sarah.c "Maybe I should go?  I don't want to be intruding on your personal time together."
        wt_image b_clerk_lw_visit_4
        player.c "Nonsense.  You can see [bree.name] doesn't mind you being here.  She's having a hard enough time controlling her orgasm as it is."
        wt_image b_clerk_lw_visit_6
        player.c "I'm going to switch to your ass, [bree.name], to make this easier on you."
        if bree.has_tag('allowed_to_talk'):
            bree.c "Yes, [bree.your_respect_name]."
        wt_image b_clerk_lw_visit_7
        "[bree.name] groans as you penetrate her ass, and you're pretty sure you hear Sarah groan softly, too."
        bree.c "ooohhhh!"
        sarah.c "ohh"
        wt_image b_clerk_lw_visit_8
        player.c "Keeping that orgasm in check?"
        if bree.has_tag('allowed_to_talk'):
            bree.c "Y ... yes, [bree.your_respect_name]!"
        else:
            "She nods vigorously."
        player.c "Good girl. Cum for me now."
        wt_image b_clerk_lw_visit_9
        "You're pretty sure she would have cum anyway, but your fingers strumming her clit make the orgasm that much more intense.  Her body thrashes wildly as the climax washes over her."
        if bree.has_tag('allowed_to_talk'):
            bree.c "OOOOHHHHH!!!!!   Thank you [bree.your_respect_name]!!!!!"
        else:
            bree.c "OOOOHHHHH!!!!!"
        wt_image b_clerk_lw_visit_10
        "When her tremors subside to the point that she can steady herself, you unload on her face."
        player.c "[player.orgasm_text]"
        "Lovingly, she laps up your seed with a sigh of contentment."
        if bree.has_tag('allowed_to_talk'):
            bree.c "Thank you [bree.your_respect_name]."
        wt_image lw_visit_4_5
        sarah.c "You were able to cum?  You both were, despite my being here?  Were you even thinking about me being here, watching you?"
        wt_image b_clerk_lw_visit_11
        if not bree.has_tag('allowed_to_talk'):
            "[bree.full_name] looks at you."
            player.c "It's okay, go ahead and answer her."
        bree.c "I knew you were watching, but it was taking everything I had not to cum without permission. So I really wasn't thinking about you watching us. I was only really thinking about following [bree.your_respect_name]'s instructions and not disobeying him."
        bree.c "Even if I had been thinking about it, it wouldn't have bothered me.  Not as long as I knew it was what [bree.your_respect_name] wanted."
        wt_image lw_visit_4_9
        sarah.c "I think you've made your point. For some people, sex doesn't always have to be in private for it to be fun.  I need to go home and think about this."
        wt_image lw_visit_4_10
        "Sarah looks at you with more interest than she has before.  You can't help yourself from teasing her."
        player.c "You can take your panties off while you think about it, if you want."
        $ bree.anal_count += 1
        $ bree.orgasm_count += 1
        $ bree.facial_count += 1
        orgasm
        add tags 'watched_slavegirl_this_weekend' to sarah
    else:
        $ current_target = None
    return


## Store Content
label bree_tst_store_enter:
    if bree.has_tag('working_at_store') and not bree.has_tag('trained_this_week'):
        $ bree.location = steel_trap
        rem tags 'follows' from bree
    elif bree.has_tag('working_at_store') and bree.name == 'Bree':
        "[bree.name] is not here at the moment."
    elif not bree.has_tag('working_at_store') and not bree.has_tag('no_longer_working_message'):
        add tags 'no_longer_working_message' to bree
        "[bree.name] no longer works here."
    if bree.location == steel_trap:
        # activate hypnosis action if applicable
        if bree.has_tag('examined'):
            rem tags 'no_hypnosis' from bree
        # submission intro
        if bree.submit_count >= 1:
            $ bree.work_intro_outfit += 1
            if bree.work_intro_outfit > 3:
                $ bree.work_intro_outfit = 1
            if bree.work_intro_outfit == 1:
                wt_image b_clerk_working_11
                "Bree seems to be doing something close to nothing ..."
            elif bree.work_intro_outfit == 2:
                wt_image b_clerk_working_12
                "Bree seems preoccupied with something that has nothing to do with her job ..."
            else:
                wt_image b_clerk_working_16
                "Bree is making a concerted effort to look bored ..."
            wt_image b_clerk_working_2
            "... until she spots you enter the store."
            if bree.submit_count == 1 or bree.submit_count == 2:
                wt_image b_clerk_working_15
                "As she sees you, she moves out from behind her counter and stands in the same place she was on your last visit."
                wt_image b_clerk_working_3
                bree.c "Hello"
                $ bree.change_image('b_clerk_working_15')
                $ bree.description = "Bree stands in the same place you left her last visit.  She's watching you, perhaps hoping you will speak to her."
            elif bree.submit_count == 3:
                wt_image b_clerk_working_4
                "She quickly checks to confirm there's no one else in the store ..."
                wt_image b_clerk_working_17
                "... then strips to her panties ..."
                wt_image b_clerk_working_18
                "... as she greets you ..."
                bree.c "Hello, [bree.your_respect_name]"
                wt_image b_clerk_working_6
                "... and assumes the position you put her in before."
                $ bree.change_image('b_clerk_working_6')
                $ bree.description = "Bree stands with her head bowed, waiting for you to speak to her."
            elif bree.submit_count == 4:
                wt_image b_clerk_working_19
                "She goes directly to the change room, where she strips ..."
                wt_image b_clerk_working_7
                "... then kneels and bows her head."
                if steel_trap.discount_ratio > 0.5 and not bree.note_left:
                    wt_image note_from_bree_1
                    "Then she places a note on the floor in front of her."
                    $ bree.note_left = True
                    add 1 note_from_bree to steel_trap notify
                    wt_image b_clerk_working_7
                    "She stays there silently, waiting for you to read her note or speak to her."
                $ bree.change_image('b_clerk_working_7')
                $ bree.description = "Bree kneels with her head bowed, waiting for you to speak to her."
            else:
                wt_image b_clerk_working_19
                "She goes directly to the change room, where she strips ..."
                wt_image b_clerk_working_7
                "... then kneels and bows her head.  She stays there silently, waiting for you to speak to her."
                $ bree.change_image('b_clerk_working_7')
                $ bree.description = "Bree kneels with her head bowed, waiting for you to speak to her."
        # hypnosis intro
        elif bree.hypno_count >= 1:
            if bree.hypno_count == 1:
                $ bree.work_intro_outfit += 1
                if bree.work_intro_outfit > 3:
                    $ bree.work_intro_outfit = 1
                if bree.work_intro_outfit == 1:
                    wt_image b_clerk_working_11
                elif bree.work_intro_outfit == 2:
                    wt_image b_clerk_working_12
                else:
                    wt_image b_clerk_working_1
                "Bree is goofing off behind the counter again as you enter the store."
                wt_image b_clerk_working_16
                "She stops and looks at you when she sees you."
                player.c "Hello, Bree."
                wt_image b_clerk_working_2
                "She hesitates slightly before responding."
                bree.c "Hello"
                $ bree.change_image('b_clerk_working_2')
                $ bree.description = "Bree watches you as you shop.  She's no longer ignoring you, but not trying to help either."
            elif bree.hypno_count == 2:
                $ bree.work_intro_outfit += 1
                if bree.work_intro_outfit > 3:
                    $ bree.work_intro_outfit = 1
                if bree.work_intro_outfit == 1:
                    wt_image b_clerk_working_11
                elif bree.work_intro_outfit == 2:
                    wt_image b_clerk_working_12
                else:
                    wt_image b_clerk_working_1
                "Bree is goofing off behind the counter again as you enter the store."
                wt_image b_clerk_working_10
                "She straightens up and moves out from behind the counter when she sees you."
                bree.c "Hello"
                $ bree.change_image('b_clerk_working_10')
                $ bree.description = "Bree watches you as you shop.  She's no longer ignoring you."
            else:
                wt_image b_clerk_working_10
                "Bree comes over to greet you when you enter the store."
                bree.c "Hello.  How may I help you today?"
                $ bree.change_image('b_clerk_working_10')
                $ bree.description = "Bree watches you, waiting to see if you need anything as you shop."
    return

label bree_tst_store_exit:
    if bree.location == steel_trap:
        add tags 'no_hypnosis' to bree
        if bree.has_tag('hypno_now'):
            rem tags 'hypno_now' from bree
        if bree.has_tag('submitting_now'):
            rem tags 'submitting_now' from bree
        call character_location_return(bree) from _call_character_location_return_226
    return

## Character Specific Timers
# Convert Character to Degraded
label bree_convert_degraded:
    $ bree.training_regime = 'daily'
    $ bree.change_image('b_clerk_degraded_1')
    call unconvert(bree,"slavegirl") from _call_unconvert_18
    call convert(bree, "degraded") from _call_convert_50
    rem tags 'club_maid' 'working_at_store' 'follows' from bree
    $ bree.fixed_location = basement
    $ bree.location = basement
    return

# Convert Character to petgirl
label bree_convert_petgirl:
    $ bree.training_regime = 'daily'
    $ bree.change_image('b_clerk_cage')
    call unconvert(bree,"slavegirl") from _call_unconvert_19
    call convert(bree, "petgirl") from _call_convert_51
    rem tags 'club_maid' 'working_at_store' 'follows' from bree
    $ bree.fixed_location = bedroom
    $ bree.location = bedroom
    return

# Convert Character to Slavegirl
label bree_convert_slavegirl:
    $ bree.training_regime = 'daily'
    $ bree.change_image('b_clerk_position_1')
    call convert(bree, "slavegirl") from _call_convert_52
    $ bree.add_tags('allowed_to_talk', 'allowed_to_cum', 'no_hypnosis')
    $ bree.action_alexis = bree.add_action("Play with her and [alexis.full_name]", label = "_alexis", condition = "alexis.has_tag('slavegirl') and alexis.can_be_interacted and not alexis.has_tag('holding_position') and bree.in_area('house') and bree.has_tag('slavegirl') and bree.can_be_interacted")
    $ bree.action_elsa = bree.add_action("Watch her play with [elsa.full_name]", label = "_elsa", condition = "elsa.has_tag('slavegirl') and elsa.can_be_interacted and not elsa.has_tag('holding_position') and bree.in_area('house') and bree.has_tag('slavegirl') and bree.can_be_interacted")
    $ bree.maintain_week_sg = week + 4
    rem tags 'working_at_store' 'follows' from bree
    $ bree.fixed_location = bedroom
    $ bree.location = bedroom
    return

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
