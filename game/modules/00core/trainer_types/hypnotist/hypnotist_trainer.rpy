# register_package hypnotist_trainer name "Trainer Type Hypnotist" description "This package adds the Hypnotist as a trainer type" dependencies core

register hypnotist_trainer_pregame 1 in core as "Hypnotist"

label hypnotist_trainer_pregame:
    $ hy = TrainerType("Hypnotist", "hy", bg = 'hypnotized', tags = ["hypnotist", "show_resistance"], hypnosis_level = 10)

    $ player.add_examine_phrase("player.test('hypnosis_level', 0) and not player.has_tag('hypnotist')", "You have gained a limited hypnotic ability.")
    $ player.add_examine_phrase("player.test('hypnosis_level',10)", "The effectiveness of your hypnosis has improved.", "player.test('hypnosis_level',15)", "The effectiveness of your hypnosis has greatly improved.")
    return

label hy_introduction:
    wt_image hy_image
    "The professional license was too shackling. It carried too much risk of professional sanction, or even arrest. So you left your career as a marriage counselor behind, and moved to a new city, and a new start.  One where you could escape the tedium and frustration of trying to talk people through their irreconcilable differences, and focus on truly helping them."
    "You don't know where your power to hypnotize comes from. Even as a child, you were good at getting people to open up to you. As a teenager, you learned you could influence people's behavior, especially the girls you dated."
    "It was only when you turned to hypnosis as a tool in your marriage counseling, however, that you learned how easily you could bring people into a trance as long as you had a focus for them to look at. And as long as you were alone with them."
    "You soon learned you could achieve better results in a single one-on-one meeting, alone and in private, than you could in a year of traditional counseling."
    "Now you need to see how far this power to influence people can take you. You'll focus on consenting couples who are tackling their problems before they become insurmountable. And you'll focus on the wife, because frankly, changing the behavior of women turns you on. You create an online profile advertising your services."
    "You become The Wife Trainer.\n\nSkills: You can Hypnotize clients when they are alone with you, allowing you to change client statistics directly, and you can see a client's exact Resistance score."
    return
