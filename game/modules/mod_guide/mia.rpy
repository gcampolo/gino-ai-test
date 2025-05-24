## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: Digital Bonsai

# Package Register
register_package mod_guide name "Mod Guide" author "Digital Bonsai" description "A very early attempt at making an interactive guide for people who wants to create mods" disabled dependencies core
register mia_pregame 1 in mod_guide as "Mia the Helpful Aide"

# Pregame
label mia_pregame:
    python:

        ## Credits
        model_credits += [('full', "Mia the Helpful Aide (Mia Khalifa)")]

        ## Character Definition
        mia = Person(Character("Mia", who_color="#D93E99", what_color="#D93E99", window_background="#000000CC"), "mia", prefix = "", suffix = "the Helpful Aide", resistance = 20, training_period = 9, min_reputation = 5000)
        mia.trigger_phrase = ""

        # Other Characters
        # Other
        other_mia = Character("Shopper", who_color="#ff66ff", what_color="#ff66ff")


        ## Actions

        # hypnosis actions
        # mia.add_hypno_actions() # this adds the standard hypnosis actions

        # training actions
        mia.action_talk = mia.add_action("Talk to her", label="_talk", condition = "mia.in_area('house')")
        mia.action_talk = mia.add_action("Talk about registering a package", label="_register_talk", condition = "mia.in_area('house') and not mia.has_tag('first_talk')")
        mia.action_talk = mia.add_action("Talk about creating a WT character", label="_character_talk", condition = "mia.in_area('house') and mia.has_tag('register_talk_complete')")
        mia.action_dismiss = mia.add_action("Bye Bye, Mia", label="_dismiss", condition = "mia.in_area('house') and mia.has_tag('no_more_topics')")

        ## Tags
        # Common Character Tags
        mia.add_tags('first_talk', 'no_hypnosis', 'likes_boys', 'likes_girls', 'likes_modders')

        # Character Specific Tags
        # N/A

        ## Locations and Location Actions
        mia_inner_workings = Location("Game's Inner Workings", 'miw')

        ## Character Specific Items
        mia_glasses = Item("Mia's Glasses", 'mg', with_examine = True)

        ## Other
        mia.change_status("available_to_be_client")

        # Start Day Events
        start_day_labels.append('mia_start_day')

        ########### VARIABLES ###########
        # Common Character Variables
        mia.add_stats_with_value('hypno_blowjob_count', 'show_tits_count')

        # Character Specific Variables

        ####
        # New Engine Features
        ####

        ## Video Demo
        living_room.add_action("Watch Training Video (Video Demo)", label = '_watch_tv', unseen = False, seen_result = True)
        living_room.add_action("Watch Cool Movie (GIF to WEBM Demo)", label = '_watch_cool_movie', unseen = False, seen_result = True)

        ## Expandable Menu Demo
        # Inner Expendable Menu
        test_inner_menu = ExpandableMenu("Are you testing an inner Expandable Menu?")
        test_inner_menu.add_choice("Calls a label", "menu_test_inner_yes", "True")

        # Main Expandable menu
        test_menu = ExpandableMenu("Are you testing Expandable Menu?")
        # to can be a label (string) of another ExpandableMenu object. If it is an ExpandableMenu the option will open that menu.
        test_menu.add_choice(name = "Calls a label", to = "menu_test_yes", condition = "True")
        test_menu.add_choice("Add Another Option - One Shot", "menu_test_add", one_shot = True)
        test_menu.add_choice("Revealed Option - Show inner Menu", test_inner_menu, "player.has_tag('extra_option')")

        # Demo Action
        living_room.add_action("Expandable Menu Demo", label = '_show_expandable_menu', unseen = False, seen_result = True)
    return

label lr_show_expandable_menu:
    call expandable_menu(test_menu) from _call_expandable_menu_7
    return

label menu_test_yes:
    "Called a label"
    return

label menu_test_inner_yes:
    "Called a label from inner menu"
    return

label menu_test_add:
    "You clicked the add another option"
    $ test_menu.add_choice("Added Option - Reveal Option", "menu_test_extra", "True", one_shot = True)
    return

label menu_test_extra:
    add tags 'extra_option' to player
    return

label lr_watch_tv:
    wt_image training_video
    "You take a few minutes to relax and learn some critical new skills."
    sys "The core WT content doesn't use video (or sound), but the engine supports it if modders wish to include reasonably sized files in their content."
    return

label lr_watch_cool_movie:
    wt_image ramona_rocks
    "You are watching a gif converted to webm using {a=https://convertio.co/gif-webm/}convertio.co{/a}\nThe whole process took about 10 seconds."
    sys "The core WT content doesn't use video (with or without sound), but the engine supports it if modders wish to include reasonably sized files in their content."
    return

label mia_start_day:
    day_label rem from start mia_start_day
    $ mia.min_reputation = 5
    summon mia
    return


label mia_end_day:
    return

label mia_end_week:
    return


label mia_examine:
    "Mia stands in your living room ready to help you with whatever needs you may have."
    wt_image current_location.image
    return

label mia_talk:
    wt_image mia.image
    if mia.has_tag('first_talk'):
        rem tags 'first_talk' from mia
        mia.c "Hey, handsome! I heard from DB that you want to make a mod for this game!"
        mia.c "Well, I'm here to, hopefully, get you started on that."
        mia.c "Mind that I'm gonna assume you know basic renpy. Control Flow: Labels, Jump, Call, etc. If you don't know that then I suggest you check a renpy tutorial before you keep talking to me."
        mia.c "I'm gonna make a new action available on me, so try clicking on my portrait again."
    else:
        mia.c "You talked to me already, silly. Check other actions."
    return

label mia_register_talk:
    wt_image mia.image
    mia.c "So tempted to make a joke here, but I guess I'll try to keep this professional."
    mia.c "First I totally recomend that you keep the mia.rpy script open together with the tutorial because I'm gonna be referencing lines in the script a lot. So... if you haven't done it I'll give give you a bit of time to do it now."
    mia.c "Ready? Ok. On to package registering"
    mia.c "This script uses both register statements, you can find them in line 5 and 6. Let dissect register_package first."
    mia.c "First comes the command to register the package, then mod_guide, which is the id of this package"
    mia.c "Name is the name shown in the package select screen.\nAuthor is displayed in the tooltip for that package."
    mia.c "The description will tell people hovering your package what they can find in there."
    mia.c "Then comes the optional enabled/disabled flag. If no flag is found the package is enabled by default."
    mia.c "And finally (and most importantly) are dependencies. This package depends on the core package, which is the main game. Most packages should depend on it."
    mia.c "You can have several package ids after the dependencies attribute; separated by a space."
    mia.c "That is all it takes to register a new (empty) package.\nBut now we need to tell it what labels to run on start, and this is where register comes into play."
    mia.c "When you use register you need to first give it a label name. By convention this label is should be called short name of the most important thing in your mod plus '_pregame'. My pregame_label is called 'mia_pregame' cuz I'm the most important thing on the package."
    mia.c "Then you need to give the pregame label a priority; lower is earlier in this case. This is only relevant if you are gonna be adding more than one pregame label."
    mia.c "You follow that with an 'in' and the id of package you are adding this pregame label to.\n\nThen 'as' and a colorful name to show in the tooltip of the package in the select screen."
    mia.c "Once that is done you have a registered package with a registered label that will be called when the package select screen is accepted."
    add tags 'register_talk_complete' to mia
    return

label mia_character_talk:
    wt_image mia.image
    mia.c "First some recognition. Line number 13 adds my name to the model credits that you can access from the menu. The first parameter there 'full' means it'll get added to full model credits. The other possible parameters are 'support' and 'bit'"
    mia.c "Now onto defining characters"
    mia.c "Mmm... so the line that define me as a WT character is number 16. Let talk about it."
    mia.c "The first argument is a normal renpy Character. Then comes the short_name that is used as prefix for labels. It should be unique."
    mia.c "prefix and suffix are part of the naming character scheme. Normally WT uses only the suffix to add a very short description of the character."
    mia.c "In my case, that's [mia.suffix]."
    mia.c "Nobody's sure who mispelled suffix as suffix in the game code originally, but that's the way it is now."
    mia.c "I'll have more to say on this topic later."
    add tags 'no_more_topics' to mia
    return

label mia_dismiss:
    wt_image mia.image
    mia.c "Ahhh ... tired of me already?"
    mia.c "I guess that makes sense, though, because DB hasn't given me anything more to say to you."
    mia.c "Which is why WT butted in and added the 'no_more_topics' tag to my mia_character_talk label, which opened up this new action letting you totally dismiss me."
    mia.c "You can see in line 33 of my script the conditions that opened up this very mean action whereby you send me away."
    mia.c "And the very basic coding in line 114 where WT added the tag to me that let you send me packing."
    mia.c "You can tell it's very basic coding, because WT didn't mess it up ... *wink*"
    mia.c "Look for more super complicated WT code in line 129 for how he actually gets rid of me."
    mia.c "At least the dismiss command only sends me away temporarily.  But we'll have to wait for DB to give me more to say before I can explain how you bring me back."
    player.c "Bye bye, Mia."
    mia.c "Bye bye!"
    dismiss mia
    wt_image current_location.image
    return
