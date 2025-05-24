# register_package playboy_trainer name "Trainer Type Playboy" description "This package adds the Playboy as a trainer type" dependencies core

register playboy_trainer_pregame 1 in core as "Playboy"

label playboy_trainer_pregame:
    $ pb = TrainerType("Playboy", "pb", bg = 'aroused', tags = ["supersexy", "show_desire"], desire_mod = 10, desire_gain_mod = 5)
    return

label pb_introduction:
    wt_image pb_image
    "The hurt look in his eyes will haunt you forever.  He was your friend.  Your best friend.  He asked you to be his best man.  She said it was her last chance at a fling before marriage.  She said it didn't count if you aren't married yet.  It counts.  You knew it counts.  She threw herself at you, like women always do.  You let her, like you always do.  You knew better."
    "They say its bad luck to see your bride on your wedding day.  What is it when you see your bride with her arms and legs wrapped around your best man, riding his cock in her wedding dress?  From over her shoulder you saw him walk in on you.  Saw the hurt in his eyes.  You've never felt worse.  It cost you your best friend.  It cost them their marriage."
    "Now you've moved to a new town to start over. You couldn't be celibate even if you wanted to.  So to give you a distraction from other women throwing themselves at you, you’re going to stick to women whose husbands approve of you sleeping with them."
    "And to help you start to feel better about yourself, you’re going to help those women become happier with the person they are, not sabotage their lives for the enjoyment of a brief fling.  You set up a profile online, offering your services."
    "You become The Wife Trainer.\n\nSkills: You raise Desire faster, and you can see a client's exact Desire score."
    return
