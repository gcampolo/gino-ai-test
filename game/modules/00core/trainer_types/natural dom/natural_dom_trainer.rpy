# register_package natural_dom_trainer name "Trainer Type Natural Dom" description "This package adds the Natural Dom as a trainer type" dependencies core

register natural_dom_trainer_pregame 1 in core as "Natural Dom"

label natural_dom_trainer_pregame:
    $ nd = TrainerType("Natural Dom", "nd", bg = 'submissive', tags = ["dominant", "show_submission"], submission_mod = 10, submission_gain_mod = 5)
    return

label nd_introduction:
    wt_image nd_image
    "You needed to sell her.  You loved her and she loved you, and you hated the thought of life without her.  The day you signed her sale contract was the worst day of your life.  You swore an oath, however, to give her what she needed.  And what she needed, to become the person she was meant to be, was to experience being treated like property."

    "To obey out of pure submission, not love.  She would never have that if she stayed with you.  So you took her to her new owner's house, accepted his payment for her, and left, quickly, hoping she wouldn't see the tears in your eyes."

    "Now you've moved to a new city to start over.  You’re not ready for the emotional commitment associated with single women.  You're not ready to fall in love again.  You still need opportunities, however, to exert dominance over women, as an outlet for your sexual needs as well as your own emotional healing.  So you create an online profile reaching out to husbands needing help to train their wives."

    "You become The Wife Trainer.\n\nSkills: You raise Submission faster, and you can see a client's exact Submission score."

    return
