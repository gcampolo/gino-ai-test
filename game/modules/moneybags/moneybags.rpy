register_package moneybags name "Moneybags" author "Digital Bonsai" description "New trainer type demo based around having more money. Mind that, besides its perks, it has no special content in game."
register moneybags_trainer_pregame 1 in moneybags as "Moneybags Trainer Type"

label moneybags_trainer_pregame:
    $ monb = TrainerType("Moneybags", "monb", bg = 'pearls', chosen_label = "_chosen", tags = ['wealthy'], money = 600)
    return

label monb_chosen:
    day_label add to start monb_start_day priority 999
    return

label monb_start_day:
    if day == 1 and week > 1:
        notify "Your various investments net you 30."
        notify
        change player money by 30 no_message
    return

label monb_introduction:
    wt_image monb_image
    "You were always the black sheep of your very respected family. Longing to find the freedom your lastname denied you, you moved to a different country, and left all that behind. Except, of course, a decent amount of money to help you start over."
    "You always had a knack to convince people to do what you wanted, even before using your money as a way to grease the wheels. But you are determined to use your gifts to do good... or at least what you consider to be good."
    "By mere happenstance a friend of yours asked you to talk to his wife to convince her to try to save their marriage. You succeded and felt good doing it. It wasn't exactly the outcome that draw you in but the journey. Molding someone into what you want."
    "Now you need to see how far you can go in influencing others. You use your connections to setup a discrete online profile advertising your services."
    "You become The Wife Trainer.\n\nSkills: You start with significally more money, and recieve a small extra sum weekly."
    sys "There is very little unique in game content for the Moneybags trait.  At least for now."
    return
