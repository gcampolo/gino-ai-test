## Author
# Questions/Comments/Suggestions/Bugfixes can be directed to: wifetrainer

# Package Register
## register_package
register dee_pregame 20 in core as "Dee the Daughter"

# Pregame
label dee_pregame:
  python:
  ## Constants
    ## Credits
    model_credits += [('support', "Dee the Daughter (Alexa Lynn)")]
    model_credits += [('bit', "Snow (Aurora Snow)")]

    ## Character Definition
    # Lime
    dee = Person(Character("Dee", who_color="#00FF00", what_color="#00FF00"), "dee", prefix = "", suffix = "the Protective Daughter")

    # Other Characters
    # Blue
    dee_prof = Character("Dr. Jameson", who_color="#0000FF", what_color="#0000FF", window_background=gui.dialogue_background_dark_font_color)

    # Light Blue
    dee_ra = Character("Snow", who_color="#0080FF", what_color="#0080FF")

    ## Actions
    dee.action_talk_professor = dee.add_action("Talk about her professor", label="_talk_professor", condition = "dee.can_be_interacted and dee.professor_event_status == 0 and dee.in_area('house')")
    dee.action_talk_women_authority = dee.add_action("Talk about women in authority", label="_talk_women_authority", condition = "dee.can_be_interacted and dee.marilyn_event_status == 0 and player.marilyn_building_visit_count > 0 and dee.in_area('house')")
    dee.action_talk_sex_life = dee.add_action("Talk about her sex life", label="_talk_sex_life", condition = "dee.can_be_interacted and dee.in_area('house') and not dee.has_tag('sex_talk_today')")
    dee.action_talk_mother = dee.add_action("Talk about her mother", label="_talk_mother", condition = "dee.can_be_interacted and donna.daughter_lust_revealed == 2 and dee.in_area('house')")
    dee.action_invoke_hypno_trigger = dee.add_action("Invoke her hypno trigger", label = "_invoke_hypno_trigger", condition = "dee.can_be_interacted and dee.has_tag('trigger_implanted') and dee.in_area('house')")
    dee.action_sex = dee.add_action("Offer to have sex with her", label="_sex", condition = "dee.can_be_interacted and dee.in_area('house')")
    dee.action_dominate = dee.add_action("Take her to your dungeon", label="_dominate_her", condition = "dee.can_be_interacted and dee.dom_discussion_count > 0 and not dee.has_tag('talked_domination_today') and dee.in_area('house')")
    dee.action_end_session = dee.add_action("Send her home", label="_end_session", condition = "dee.in_area('house')")

    # Add Actions to Hypnosis Actions
    dee.trigger_phrase = "Feminists fuck when ordered"
    # hypno_trigger_sessions_threshold sets when the _implant_trigger label runs
    dee.hypno_trigger_sessions_threshold = 5
    # hypno actionss
    dee.bj_hypno_action = dee.add_action("Getting a blow job", label = "_bj_hypnosis", context = "_hypnosis", condition = "dee.in_area('house')")
    dee.sex_hypno_action = dee.add_action("Having sex with her", label = "_sex_hypnosis", context = "_hypnosis", condition = "dee.in_area('house') and dee.hypno_blowjob_count > 0")
    dee.submission_hypno_action = dee.add_action("Exploring a woman's traditional role in society", label = "_submission_hypnosis", context = "_hypnosis", condition = "dee.in_area('house') and dee.dom_discussion_count == 0")
    dee.resistance_hypno_action = dee.add_action("Just lower her resistance", label = "_resistance_hypnosis", context = "_hypnosis", condition = "dee.in_area('house') and not dee.has_tag('trigger_implanted')")
    dee.nothing_hypno_action = dee.add_action("Nothing in particular", label = "_nothing_hypnosis", context = "_hypnosis", condition = "not dee.in_area('house') or dee.has_tag('trigger_implanted')")

    # Continuing Visits Actions
    dee.action_contact = living_room.add_action("Contact [dee.full_name]", label = dee.short_name + "_contact", context = "_contact_other", condition = "dee.can_be_interacted and dee.has_tag('contact_open')")
    # Special Contact
    dee.action_contact = living_room.add_action("Contact [dee.name]'s RA", label = "dee_ra_contact", context = "_contact_other", condition = "dee.talk_sex_life_status == 2 or dee.talk_sex_life_status == 4")

    ## Tags
    # Common Character Tags
    dee.add_tags('first_visit', 'no_hypnosis', 'likes_boys', 'likes_girls')

    # Character Specific Tags
    # N/A

    ## Locations
    # N/A

    ## Other
    dee.change_status("minor_character")

    # Start Day Events
    start_day_labels.append('dee_start_day')

    ########### VARIABLES ###########
    # Common Character Variables
    dee.add_stats_with_value('hypno_blowjob_count', 'hypno_facial_count', 'hypno_swallow_count', 'hypno_sex_count', 'visit_count', 'visit_week')

    # Character Specific Variables
    dee.add_stats_with_value('dom_discussion_count', 'fuck_machine_ride_count', 'marilyn_event_status', 'professor_event_status', 'ready_for_mom', 'talk_sex_life_status')
    # key for dee.dom_discussion_count: 0 = not yet discussed, 1 = discussed, 2 = will offer herself to you next time, 3 = has offered herself to you, 4 = you have dominated her before
    # key for dee.ready_for_mom: 0 = not discussed, 1 = event pending, 2 = didn't go through with it, 3 = went through with it, 4 = went through with it and let you know it was one time thing only
    # key for dee.talk_sex_life_status: 0 = hasn't disclosed anything to you, 1 = told you about her relatonship with her RA, 2 = talked about being in a rut with her RS, 3 = you convinced her RA to by a dildo,
    # 4 = follow up scene with dildos if storyline not advanced yet, 5 = you told RA about Dee's experience with Marilyn, 6 = follow up strap-on scenes if story-line not advanced yet,
    # 7 = first scene of Dee dominating Snow if storyline ends with Dee in control, # 8 = second scene if sotryline ends with Dee in control, # 9 = follow up scene if storyline ends with Dee in control of her RA,
    # 10 = first public domination scene if you told Dee to be her RA's bitch, # 11 = follow up scene if storyline ends with Dee as the RA's bitch
    # key for dee.marilyn_event_status: 0 = no event yet, 1 = event pending, 2 = heard about event

    ######## EXPANDABLE MENUS #######

  return

# Initial Contact Message

# Character Rejected

# Arrange Character Session

# Display Portrait
# CHARACTER: Display Portrait
label dee_update_media:
    pass # no changes currently
    return

########### CHARACTER ACTIONS ###########
## Common Character Actions
# Examine Character
label dee_examine:
    if dee.has_tag('sex_before'):
        "She sees you as a casual sex partner."
    elif player.has_tag('supersexy'):
        "She's interested in you, sexually, but hasn't yet admitted that."
    else:
        "She's not interested in having sex with you."
    if dee.dom_discussion_count > 4:
        "She lets you take her to your dungeon and train her.  She says it's because she wants to learn how to dominate other women, but she seems to become aroused easily when submitting to you, even though that doesn't fit her vision of herself."
    elif dee.dom_discussion_count == 4:
        "She let you dominate her once, to see what it was like.  You told her there's more she could learn and although she's hesitant, she seems open to additional sessions in your dungeon."
    elif dee.dom_discussion_count == 2 or dee.dom_discussion_count == 3:
        "She's willing to let you dominate her once, to see what it's like."
    elif dee.dom_discussion_count == 1:
        "She's not interested in letting you dominate her."
    if dee.ready_for_mom > 2:
        "Thanks to your intervention, she now has a very special relationship with her Mom."
    if dee.has_tag('trigger_implanted'):
        "You have implanted a hypnotic trigger in her.  It doesn't do much right now, but it's there."
    return

# Talk to Character
label dee_talk_professor:
    player.c "This professor of yours, the enlightened one who wouldn't exchange his position of authority for sex, is he in a relationship?"
    wt_image daughter_house_1_1
    dee.c "Not that I know of."
    player.c "I take it he's not gay, either."
    wt_image daughter_house_1_2
    dee.c "How would you know that?"
    player.c "How many men are in your classes?"
    dee.c "I ... I don't think there are any."
    player.c "That's why I know he's not gay.  He could have specialized in anything. Instead, he chose to teach women in society, a topic that's guaranteed to deliver him a class full of young women every year."
    wt_image daughter_house_1_22
    dee.c "Or he could just be interested in rectifying the oppression imposed on women by a traditionally patriarchal society!"
    wt_image daughter_house_1_25
    dee.c "Besides, he can't have a relationship with any of the women in his class. The school has a strict no fraternization policy that prevents professors from having any sexual relationship with their students. That was the first topic Dr. Jameson discussed with us at the start of the class, a history of the policy and why it's necessary to protect the women at the university from abuse."
    player.c "Oh, this guy's clever."
    wt_image daughter_house_1_22
    dee.c "What do you mean?"
    player.c "So on day one in front of his new class of nubile young women, he immediately sets himself up as forbidden fruit."
    wt_image daughter_house_1_24
    dee.c "That's not what he was doing!  He was educating us."
    player.c "Educating you on why he couldn't make the first move, knowing damn well that out of a class of horny first year college students, there's going to be more than a few attracted to the idea of seducing the man they're not allowed to sleep with."
    wt_image daughter_house_1_21
    dee.c "That's not true!  He wouldn't sleep with one of his students.  It would be contrary to everything he's taught us about the need for women to be valued in society regardless of their sexual attractiveness to men."
    player.c "Prove it.  When you get back to school, ask him for some extra help with your studies. Offer to thank him for his help and for being such an amazing professor. Find out for yourself whether he's indifferent to the opportunity his authority as a professor creates for him to gain access to potential sexual partners."
    wt_image daughter_house_1_1
    dee.c "That's just you projecting your own needs and insecurities onto someone else.  A truly secure man is capable of accepting women as equals without 'conquering' them sexually in an imbalanced power relationship."
    if dee.has_tag('first_visit'):
        player.c "It's late, kid,  I'm too tired to debate human nature with you tonight.  You want to understand what people are really like, drop by again sometime when it isn't so late and we can chat."
    else:
        player.c "It's nice seeing you, kid, but I don't have time to chat any more today. Perhaps we could continue our conversation at another time."
    $ dee.professor_event_status = 1
    call dee_visit_end from _call_dee_visit_end
    return

label dee_talk_women_authority:
    player.c "How much contact have you had with powerful women?  I mean women who've made it to the top in what is a traditionally male industry?"
    wt_image daughter_house_1_2
    dee.c "I ... I haven't really.  I've read about them in my studies, though."
    player.c "Would you like to meet one?"
    wt_image daughter_house_1_25
    dee.c "You could do that?"
    player.c "Yes.  I'll set up a meeting between you and my friend, Marilyn.  It may give you a chance to test your theory about what women do with the power they achieve."
    wt_image daughter_house_1_22
    dee.c "What do you mean?  Are you saying that gender is irrelevant and that humans behave according to the socio-economic role they fill, and that perceived gender differences are actually differences in socio-economic needs and functions that are independent of the actor's gender identity?"
    if dee.has_tag('first_visit'):
        player.c "It's late, kid,  I'm too tired to debate human nature with you tonight.  You want to understand what people are really like, drop by again sometime when it isn't so late and we can chat."
    else:
        player.c "It's nice seeing you, kid, but I don't have time to chat any more today. Perhaps we could continue our conversation at another time."
    $ dee.marilyn_event_status = 1
    call dee_visit_end from _call_dee_visit_end_1
    return

label dee_talk_sex_life:
    add tags 'sex_talk_today' to dee
    # if hasn't talked to you about her RA yet
    if dee.talk_sex_life_status == 0:
        wt_image daughter_house_1_2
        dee.c "I'm not about to start talking to you about what I do or don't do with guys at college."
        player.c "What about the girls at college?  I understand from your Mom that you're not picky."
        wt_image daughter_house_1_21
        dee.c "I'm not going to talk to you about any part of my sex life.  Perv!"
        if dee.marilyn_event_status > 1 or dee.professor_event_status > 1:
            if dee.marilyn_event_status > 1 and dee.professor_event_status > 1:
                player.c "You told me about your adventures with Marilyn and Dr. Jameson.  What's the difference?  Is there a girl you really like you're embarrassed to talk to me about?"
            elif dee.marilyn_event_status > 1:
                player.c "You told me about your adventures with Marilyn.  What's the difference?  Is there a girl you really like you're embarrassed to talk to me about?"
            else:
                player.c "You told me about your adventures Dr. Jameson.  What's the difference?  Is there a girl you really like you're embarrassed to talk to me about?"
            wt_image daughter_house_1_2
            dee.c "No, there's no one I'm embarrassed about.  No one I really like, either.  I mean, there is one girl, but I wouldn't say I 'like like' her."
            player.c "Do you 'like like' the way she fucks you on a regular basis?"
            wt_image daughter_house_1_21
            dee.c "Would you fucking stop!  You're worse than Mom."
            player.c "I suspect the details I'm interested in are slightly different than the ones your Mom wants to know about.  Then again, now that I think about it, maybe not.  Anyway, if the sex is so good between the two of you, what's the problem?"
            wt_image daughter_house_1_22
            dee.c "I never said the sex was so good and I never said there was a problem."
            player.c "Well, at least one of those two statements must be true."
            wt_image daughter_house_1_24
            dee.c "You're just not going to give up, are you?  Fine, you win.  I'll feed your pervy fantasies."
            wt_image daughter_ra_1_1
            dee.c "{i}Her name is [dee_ra.name] and she's the RA for my floor at my college dorm.  We met the first day I moved in.{/i}"
            wt_image daughter_ra_1_2
            dee.c "{i}We hit it off right away, or maybe I should say she started hitting on me right away.  Both, I guess.{/i}"
            wt_image daughter_ra_1_3
            dee.c "{i}I wouldn't say she's my 'type', exactly, but I like her and think she's sexy.  She's 4 or 5 years older than me and knows what she wants, which apparently includes me.  And if I'm being honest, I'm horny on a regular basis, like a lot of freshmen I guess.  I masturbated that night, thinking about the blatant interest she showed in me, and the night after that, too.{/i}"
            wt_image daughter_ra_1_4
            dee.c "{i}A couple of days later, we're alone in the TV room late at night, when she suddenly leans over and starts to remove my hoodie.{/i}"
            dee_ra "I'd like to get a better view of what you look like, freshee.  I hope that's okay?  You're so pretty, but you're always covered up in these baggy clothes when you're hanging around the dorm."
            wt_image daughter_ra_1_5
            dee.c "What if someone walks in??"
            wt_image daughter_ra_1_6
            dee_ra "Then I wouldn't be the only one getting to enjoy this amazing view.  You're really beautiful, did you know that?  You have nothing to be embrassed about."
            wt_image daughter_ra_1_7
            dee.c "It would be humiliating.  Can you image the reputation I'd get if one of the other girls walk in and finds me sitting naked beside you?"
            wt_image daughter_ra_1_8
            dee_ra "Then I guess you'll either have to put your clothes back on or invite me back to your room so I can continue to undress you in private."
            wt_image daughter_ra_1_9
            dee.c "{i}Like I said before, I'm a horny college freshman.  Of course, I invited her back to my room and got naked for her.  I was happy to watch as she got naked for me, too.{/i}"
            wt_image daughter_ra_1_10
            dee_ra "Do you like what you see, freshee?  I know I do."
            wt_image daughter_ra_1_11
            dee.c "{i}I wasn't sure I could answer her without my voice cracking, so I decided to answer in a way that didn't risk me sounding like an idiot ...{/i}"
            wt_image daughter_ra_1_12
            dee.c "{i}... by licking her nipple and hoping that made me seem cool and confident, not nervous and horny, which is how I was actually feeling.{/i}"
            wt_image daughter_ra_1_13
            dee_ra "Mmmm, an eager freshee.  I like that.  You and I are going to have a lot of fun this semester."
            wt_image daughter_ra_1_14
            dee.c "{i}I liked the sound of that, because it meant this wasn't just a one-night stand.  Not that I have a problem with those, but I didn't want to have one with my RA the first week I got there.  A girl can get a reputation really easy around a dorm and I didn't want to be known as the floor slut before I'd even gotten to know most of my dorm-mates.{/i}"
            wt_image daughter_ra_1_15
            dee.c "{i}A moment later, her tongue was on my clit and I couldn't think of anything other than how good that felt ...{/i} Ohhh FUCCKKKK!!!!"
            wt_image daughter_ra_1_16
            dee_ra "Mmmm, you cum quickly, freshee.  That's flattering.  Also tasty."
            wt_image daughter_ra_1_10
            dee_ra "Would you like to find out what I taste like?"
            wt_image daughter_ra_1_17
            dee.c "{i}To be honest, I felt more like pushing her head back between my legs and making her lick me some more, but she was my RA and this was a new fling, so I decided it made more sense to reciprocate and make sure she enjoyed herself.  Which she did, maybe a little bit too much.{/i}"
            wt_image daughter_ra_1_18
            dee_ra "You look good down there, freshee.  How'd you like to spend the rest of the semester in this position?"
            wt_image daughter_ra_1_19
            dee.c "{i}I liked the idea of an on-going relationship with her, but I could see she was sizing me up for a pet collar I had no intention of wearing.{/i}"
            wt_image daughter_ra_1_20
            dee.c "{i}Fortunately, there's a foolproof way to restore the power balance with girls like her, and boys, too.  I turned her to jelly with my tongue and when she started making puppy-dog eyes at me, I made her cum, hard.{/i}"
            dee_ra "Shit, freshee, that feels so good!  Oh, wow!  Oh, I'm going to ... OOHHHH!!!!"
            wt_image daughter_ra_1_21
            dee.c "I'd love to do this again sometime, [dee_ra.name].  Anytime you feel like having an orgasm like that again, I'm sure you can figure out a way to earn one from me."
            dee_ra "Look at you with the big balls!  Silly me thinking a little wisp of a thing like you would be a pushover.  Okay, freshee, we'll do this on your terms.  I lick your itches, you lick mine.  This is going to be a fun term!"
            wt_image daughter_house_1_2
            dee.c "Can we stop talking about my sex life now?  That wasted all of my time.  It's time for me to go."
            "For now.  If you want to influence her relationship with [dee_ra.name], ask her about her sex life again on another visit"
            change player energy by -energy_very_short notify
            $ dee.talk_sex_life_status = 1
            add tags 'talked_ra_today' to dee
            call dee_visit_end from _call_dee_visit_end_2
    # shares RA sex scene for first time
    elif dee.talk_sex_life_status == 1:
        player.c "How are things with your RA?"
        wt_image daughter_house_1_1
        dee.c "Good.  Can we not talk about that?"
        player.c "After you tell me what's wrong."
        wt_image daughter_house_1_21
        dee.c "Nothing's wrong.  I just told you things are good!"
        player.c "Which they aren't, or you'd be more enthusiastic about telling me about your lover.  What's wrong?"
        wt_image daughter_house_1_2
        dee.c "You're just going to keep hammering away at this, aren't you?"
        wt_image daughter_ra_1_2
        dee.c "{i}We don't see each other a lot during the day, but when we do she's super nice and flirty.{/i}"
        wt_image daughter_ra_1_9
        dee.c "{i}I see her more often at night.  If she hasn't hooked up with anyone, she comes by to see if I'm alone.  If I am, she climbs into bed with me and says the same thing.{/i}"
        dee_ra "Put your head between my legs and eat me out, freshee."
        wt_image daughter_ra_1_10
        dee.c "{i}Every time I have the same answer ...{/i} Earn it."
        wt_image daughter_ra_1_22
        dee.c "{i}I spread my legs and she puts her mouth where it belongs.{/i}"
        player.c "{i}But it leaves you unsatisfied.{/i}"
        wt_image daughter_ra_1_15
        dee.c "{i}No, not at all!  She's really good with her mouth and I cum every time.{/i}"
        player.c "{i}But you're still unsatisfied.{/i}"
        wt_image daughter_ra_1_23
        dee.c "{i}Sort of.  I want her to stay there.  Some nights I'd like to fall asleep with my thighs wrapped around her head.{/i}"
        player.c "{i}Have you told her that?{/i}"
        wt_image daughter_ra_1_15
        dee.c "{i}Yes, and sometimes she'll indulge me for a little while, but never as long as I'd like.{/i}"
        wt_image daughter_ra_1_16
        dee_ra "That's enough attention for you, freshee.  Reciprocation time."
        wt_image daughter_ra_1_17
        player.c "{i}Do you enjoy eating her out?{/i}"
        dee.c "{i}I do, but not as much as she'd like me to.  I'm leaving her unsatisfied, too.  Sometimes she reminds me of that.{/i}"
        wt_image daughter_ra_1_19
        dee_ra "It's so good having you like this, feeling your tongue on my cunt, watching you between my legs.  I'd love to come back to my room sometime and find you kneeling there, naked, waiting to serve me like this."
        wt_image daughter_ra_1_20
        dee.c "{i}She never lasts long after she starts talking like that, the fantasy of having me as her pet gets to her and she starts to cum.{/i}"
        wt_image daughter_ra_1_8
        dee.c "{i}It's always awkward when she leaves, each of us enjoying what we've both done together, but wishing it was something other than it is.{/i}"
        wt_image daughter_house_1_2
        dee.c "Maybe I should break it up, I don't know.  It's convenient having a fuck buddy on the same floor and the orgasms are great.  It's just never going to work for both us in the long run.  Let's talk about something else now, this was depressing."
        "You can leave things at that, if you want.  Or you could give [dee_ra.name] a call sometime.  It shouldn't be too hard to track down [dee.name]'s dorm and then pass a message to her RA."
        $ dee.talk_sex_life_status= 2
    # follow up after initial RA sex scene, if you haven't spoken to her RA yet
    elif dee.talk_sex_life_status == 2:
        player.c "How are things with your RA?"
        wt_image daughter_house_1_1
        dee.c "Good.  I have nothing more to say than I told you last time, so you might as well drop this topic now."
        "You can leave things at that, if you want.  Or you could give [dee_ra.name] a call sometime.  It shouldn't be too hard to track down [dee.name]'s dorm and then pass a message to her RA."
    # first dildo scene after you speak to her RA
    elif dee.talk_sex_life_status == 3:
        player.c "How are things with your RA?"
        wt_image daughter_house_1_1
        dee.c "Good.  Interesting, actually.  She surprised me the other night."
        wt_image daughter_ra_1_9
        dee.c "{i}She came looking for me in my room after all the other girls were asleep, but this time she brought some things with her.{/i}"
        wt_image daughter_ra_1_25
        dee.c "What are those?"
        dee_ra "How naive are you, freshee?  Get on your knees and I'll show you what they are."
        wt_image daughter_ra_1_26
        dee.c "{i}She had two sex toys with her.  One was a vibrator.  She put that one inside me and turned it on.  It soon turned my knees to jelly.{/i}  *bzzzzzt*"
        wt_image daughter_ra_1_27
        dee_ra "Cum for me, freshee.  Let me hear those cute orgasm sounds of yours."
        player.c "{i}So it was another power thing for her.  Did you hold out and make her work for your orgasm?{/i}"
        wt_image daughter_ra_1_28
        dee.c "{i}I wish.  That infernal buzzing device felt so good, I came with only the tip of it inside me ...{/i}  Ohhh FUCCKKKK!!!!"
        wt_image daughter_ra_1_29
        dee.c "{i}The second toy was for me to use on her.  It was a regular dildo.{/i}"
        wt_image daughter_ra_1_30
        dee.c "{i}It wasn't lost on me that this meant I was going to have to work a lot harder and a lot longer to get her off than she had to work on me.{/i}"
        wt_image daughter_ra_1_31
        dee.c "{i}I tried to get her off using the toy alone, but I couldn't quite get her there ...{/i}"
        wt_image daughter_ra_1_32
        dee.c "{i}... and had to use my tongue on her clit to finish her off, which was clearly what she'd wanted all along.{/i}"
        dee_ra "Oh, what a good freshee!  Just like that, freshee!  Oh, I'm going to ... OOHHHH!!!!"
        wt_image daughter_ra_1_21
        dee.c "{i}I'd eaten her out without her having to do the same for me.  She was pretty pleased with herself, but at least she didn't gloat.  She just gave me a kiss and went back to her room without saying anything.{/i}"
        wt_image daughter_house_1_1
        player.c "Were you mad at her afterwards?  Or at yourself?"
        dee.c "No, not really.  It was actually pretty sexy the way she tilted the power dynamics in her favor and in a way that I wanted to go along with it.  I'd like to get her back sometime, though."
        if dee.dom_discussion_count < 2:
            player.c "I could teach you how to take control of her, if you'd like?  You'd need to agree to submit to me in my dungeon, though, so I can train you."
            wt_image daughter_house_1_2
            dee.c "I don't even want her dominating me, why would I want you to do so?"
            if dee.marilyn_event_status > 1:
                $ title = "Convince her?"
                menu:
                    "Yes":
                        player.c "Have you forgotten about your experience with Marilyn?"
                        wt_image daughter_house_1_24
                        dee.c "What does Marilyn have to do with it?"
                        player.c "You remember how she made you feel. 'Putty in her hands' were your words.  You're not naturally submissive, but you were with her, and you liked it.  I can help you recapture that feeling.  It would be a great learning experience for you.  If you're not sure you want to explore your submissive side, what about using it as a way to explore your dominant side.  You'd like to be able to make people feel what Marilyn made you feel, wouldn't you?"
                        wt_image daughter_house_1_22
                        dee.c "You could teach me to take control of others as easily as Marilyn took control of me?  Even though I'm not a powerful woman like she is?"
                        player.c "You'll teach yourself, I'll just be the role model.  The more experiences you have as a submissive, the better you'll understand how the person you're trying to control is feeling."
                        wt_image daughter_house_1_1
                        player.c "I can see you're not ready to say 'yes' right now, but think about it.  There's no need to rush, we can do this when you're ready."
                        $ dee.dom_discussion_count = 2
                    "Not today":
                        "You can raise this with her again on a future visit, if you want."
                        $ dee.dom_discussion_count = 1
            else:
                "If you're interested in pursuing this, you can offer some reasons on a future visit, ideally after she's had an enjoyable submissive experience with a powerful woman."
                $ dee.dom_discussion_count = 1
        else:
            "You can convince her to take control over her RA after you've trained her enough in your dungeon."
        if dee.marilyn_event_status == 0:
            "You could also give [dee_ra.name] another call and plant an idea about how she could better dominate [dee.name].  You need [dee.name] to have a submissive experience with a powerful woman, first, though, in order to prepare her for further domination from her RA."
        elif dee.has_tag('strapon_story_told'):
            "You could also give [dee_ra.name] another call and tell her about [dee.name]'s experience with Marilyn.  That should give her some ideas about how she can better dominate [dee.name], if you'd like to hear about that."
        add tags 'talked_domination_today' to dee
        $ dee.talk_sex_life_status = 4
    # follow up dildo scene if you haven't spoken to her RA a second time or taught her how to take control of her RA
    elif dee.talk_sex_life_status == 4:
        player.c "How are things with your RA?"
        wt_image daughter_ra_1_26
        dee.c "{i}Good.  She drops by my room to use the vibrator on me on a regular basis.{/i}  *bzzzzzt*"
        wt_image daughter_ra_1_27
        dee.c "{i}She still teases me about how easily I'm going to cum for her ...{/i}"
        wt_image daughter_ra_1_28
        dee.c "{i}... and she continues to be right ...{/i}  Ohhh FUCCKKKK!!!!"
        wt_image daughter_ra_1_29
        dee.c "{i}When I recover, I reciprocate.{/i}"
        wt_image daughter_ra_1_30
        dee.c "{i}She enjoys watching me use the dildo on her.  It gets her excited.{/i}"
        wt_image daughter_ra_1_31
        dee.c "{i}I can get her really close to cumming using the toy alone, but somehow she always manages to hold out on me ...{/i}"
        wt_image daughter_ra_1_32
        dee.c "{i}... until I give in and use my tongue on her clit to finish her off.{/i}"
        dee_ra "Oh, what a good freshee!  Just like that, freshee!  Oh, I'm going to ... OOHHHH!!!!"
        wt_image daughter_ra_1_21
        dee.c "{i}I'd still love to wipe that smug look off her face, though.  She loves the fact that I had to lick her after I came without her touching me.  She's not mean about it or anything, she just has the upper hand and we both know it.  I'd love to flip the situation, but I guess I love the way she makes me feel when she uses the vibrator on her even more.{/i}"
        wt_image daughter_house_1_1
        player.c "You could buy a vibrator to use on her, you know."
        dee.c "Then I'd just be copying her.  That wouldn't change the way she's tilted the power dynamics in her favor, if anything it'd be more like throwing in the towel."
        if dee.dom_discussion_count < 2:
            player.c "I could teach you how to take control of her, if you'd like?  You'd need to agree to submit to me in my dungeon, though, so I can train you."
            wt_image daughter_house_1_2
            dee.c "I don't even want her dominating me, why would I want you to do so?"
            if dee.marilyn_event_status > 1:
                $ title = "Convince her?"
                menu:
                    "Yes":
                        player.c "Have you forgotten about your experience with Marilyn?"
                        wt_image daughter_house_1_24
                        dee.c "What does Marilyn have to do with it?"
                        player.c "You remember how she made you feel. 'Putty in her hands' were your words.  You're not naturally submissive, but you were with her, and you liked it.  I can help you recapture that feeling.  It would be a great learning experience for you.  If you're not sure you want to explore your submissive side, what about using it as a way to explore your dominant side.  You'd like to be able to make people feel what Marilyn made you feel, wouldn't you?"
                        wt_image daughter_house_1_22
                        dee.c "You could teach me to take control of others as easily as Marilyn took control of me?  Even though I'm not a powerful woman like she is?"
                        player.c "You'll teach yourself, I'll just be the role model.  The more experiences you have as a submissive, the better you'll understand how the person you're trying to control is feeling."
                        wt_image daughter_house_1_1
                        player.c "I can see you're not ready to say 'yes' right now, but think about it.  There's no need to rush, we can do this when you're ready."
                        $ dee.dom_discussion_count = 2
                    "Not today":
                        "You can raise this with her again on a future visit, if you want."
                        $ dee.dom_discussion_count = 1
            else:
                "If you're interested in pursuing this, you can offer some reasons on a future visit, ideally after she's had an enjoyable submissive experience with a powerful woman."
                $ dee.dom_discussion_count = 1
        else:
            "You can convince her to take control over her RA after you've trained her enough in your dungeon."
        if dee.marilyn_event_status == 0:
            "You could also give [dee_ra.name] another call and plant an idea about how she could better dominate [dee.name].  You need [dee.name] to have a submissive experience with a powerful woman, first, though, in order to prepare her for further domination from her RA."
        elif dee.has_tag('strapon_story_told'):
            "You could also give [dee_ra.name] another call and tell her about [dee.name]'s experience with Marilyn.  That should give her some ideas about how she can better dominate [dee.name], if you'd like to hear about that."
        add tags 'talked_domination_today' to dee
    # first RA strap-on scene if you spoke to her RA about Dee's experience with Marilyn
    elif dee.talk_sex_life_status == 5:
        add tags 'ra_used_strapon' to dee
        player.c "How are things with your RA?"
        wt_image daughter_house_1_23
        "She hangs her head and replies quietly."
        dee.c "You talked to her, didn't you?"
        player.c "Why?  What happened?"
        wt_image daughter_ra_1_25
        dee.c "{i}She made me her bitch is what happened, the same way Marilyn did.{/i}"
        dee_ra "You know, freshee, I know you'd like me to use this vibrator on you again, but I think I've been making things too easy on you."
        wt_image daughter_ra_1_10
        dee_ra "You probably think it's unfair that I use a vibrator on you, but you have to use a regular dildo on me."
        dee.c "A little.  I have to work a lot harder to get you off."
        wt_image daughter_ra_1_8
        dee_ra "Let's make things more fair, then.  I'm not going to use the vibrator today, I'm going to use a plain old, non-vibrating dildo on you.  But you're going to find it means you'll need to work even harder to earn your orgasm."
        dee.c "What do you mean?"
        wt_image daughter_ra_1_33
        dee_ra "It means I've learned about your weakness, freshee.  Turn around."
        wt_image daughter_ra_1_34
        dee.c "{i}She pushed the strap-on inside me and it felt good ...{/i} oohhhh!"
        wt_image daughter_ra_1_35
        dee_ra "You like the new toy I bought for you, don't you, freshee?  I knew you would.  Start fucking yourself on it now."
        wt_image daughter_ra_1_36
        dee.c "Hold on, you're supposed to be fucking me.  You need to get me off, before I return the favor."
        wt_image daughter_ra_1_37
        dee_ra "Oh, this is too much fun!  That was our old deal, freshee.  I'm changing our deal.  The new deal is that I'll give you the opportunity to get yourself off, then as a 'thank you' you'll eat me out until I'm tired of seeing your pretty face between my legs."
        dee.c "I'm not going along with that."
        wt_image daughter_ra_1_38
        dee_ra "Oh yes you are, freshee.  I set the timer on my phone to 5 minutes when I put on the strap-on.  There's four-and-a-half minutes left.  That's how long I'm going to let you enjoy the dildo inside you, then you're my bitch for the rest of the evening."
        wt_image daughter_ra_1_36
        dee.c "{i}I knew then that you'd ratted me out about my experience with Mariyn, although I didn't know why.{/i}"
        wt_image daughter_ra_1_37
        dee_ra "Look at you, trying to hold yourself still.  Quit fighting it, freshee.  You want this, I want this.  Give in and use my strap-on to make yourself cum.  Only four minutes left for you to enjoy it."
        player.c "{i}You held out, of course.  You wouldn't give her the satisfaction of knowing that she'd won.{/i}"
        wt_image daughter_ra_1_39
        dee.c "{i}I couldn't help myself.  I kept thinking of Marilyn and how small I'd felt near her and yet how lucky to have been given even a few minutes of her time.  I kept thinking about the timer on [dee_ra.name]'s phone and the audacity of her offering me 5 minutes in return for the rest of my evening.  And I kept thinking about how good the strap-on felt inside me, until I found myself rocking back on it, fucking myself on it.{/i}"
        wt_image daughter_ra_1_38
        dee_ra "That's good, freshee.  That's very good.  You have three-and-a-half minutes left to enjoy my strap-on, then you're my bitch for the rest of the night."
        wt_image daughter_ra_1_40
        dee.c "{i}I came at the thought of that, that I was trading less than 5 minutes of my own pleasure for an evening of pleasuring her.  It was so hot how she'd manipulated me, I didn't even have to picture it as being Marilyn behind me, I was starting to see [dee_ra.name] as the same sort of powerful authority figure ...{/i}  Ohhh FUCCKKKK!!!!"
        wt_image daughter_ra_1_41
        dee.c "{i}I don't think I stopped cumming until her damn phone started beeping.{/i}"
        dee_ra "Time's up, freshee.  Get off my dildo, you know where you belong now."
        wt_image daughter_ra_1_17
        dee.c "{i}I wasn't allowed to use a toy on her anymore, it was my mouth only.{/i}"
        wt_image daughter_ra_1_20
        dee.c "{i}I still knew how to puch her buttons - or lick them, I guess - so I made her cum quickly, but it didn't do much to restore the power balance betwen us."
        dee_ra "Shit, freshee, that feels so good!  Oh, wow!  Oh, I'm going to ... OOHHHH!!!!"
        wt_image daughter_ra_1_18
        dee.c "{i}Yes, she was now making puppy-dog eyes at me, but it was from a position of control.{/i}"
        dee_ra "I love that you're eager to please me, freshee, but you don't need to rush.  You're going to be between my legs until I'm ready to go to sleep.  I'll let you drink lots of my juices before I leave."
        wt_image daughter_ra_1_19
        player.c "{i}You could have just stopped and kicked her out.{/i}"
        dee.c "{i}That wouldn't have been fair.  She'd told me what the deal was and I'd accepted, I was going to hold up my end of the bargain.  This was what she'd wanted from the first night she crept into my room.  It took you interfering to help her get it, but I could tell she was happy now.  With herself, and also with me.{/i}"
        wt_image daughter_ra_1_18
        dee_ra "This is so nice, freshee.  You really made me work for this, didn't you?  But you're finally where you belong now.  We're going to have so much fun now for the rest of the semester."
        wt_image daughter_ra_1_17
        dee.c "{i}I still had some resistence left, though.{/i}  This is just for tonight."
        wt_image daughter_ra_1_19
        dee_ra "No, freshee, this is now for whenever I want it.  But don't worry, I'll still let you ride my strap-on whenever you need to be reminded about why you're my bitch."
        call dee_talk_sex_life_final_question from _call_dee_talk_sex_life_final_question
    # follow up RA strap-on scene if you haven't taught Dee to take control or convinced her to be the RA's bitch
    elif dee.talk_sex_life_status == 6:
        player.c "How are things with your RA?"
        wt_image daughter_house_1_23
        dee.c "Pretty much the same.  I keep letting her take control of me."
        wt_image daughter_ra_1_9
        dee.c "{i}When she feels horny, she sneaks into my room and demands I service her.{/i}"
        dee_ra "Time to lick my cunt, freshee."
        wt_image daughter_ra_1_10
        dee.c "I've got a better idea, why don't you lick mine instead?"
        wt_image daughter_ra_1_42
        dee_ra "No, freshee.  You're my bitch, not the other way around.  But since you seem to be having trouble remembering that, let me set the timer on my phone again."
        wt_image daughter_ra_1_37
        dee_ra "There, freshee.  The strap-on's in place.  All you need to do is back up and you can enjoy five minutes on my cock before you spend the rest of the evening with your head between my legs."
        wt_image daughter_ra_1_36
        dee.c "{i}She'll put the head of the dildo against me, but she'll never put it inside.  I have to do that myself.{/i}"
        wt_image daughter_ra_1_34
        dee_ra "Time's ticking, freshee.  Only four-and-a-half minutes to go.  We both know you're going to spend the night licking me out, regardless.  I would have thought you'd want as much time with the dildo inside you as you can, but if you want to waste most of your five minutes pretending you're not my bitch, that's up to you."
        wt_image daughter_ra_1_35
        dee.c "{i}I swear, sometimes I'm not even aware that I've started to fuck her dildo until I feel it inside me ...{/i}  oohhh!"
        wt_image daughter_ra_1_38
        dee_ra "Good, you remember your place.  Fuck yourself silly on the strap-on while you can, freshee, because when the timer goes, you're mine for the rest of the night."
        wt_image daughter_ra_1_39
        dee.c "{i}I do exactly that, bucking back on her strap-on as hard as I can.  Sometimes I imagine it's Marilyn back there, but most of the time now I just enjoy the experience.{/i}"
        wt_image daughter_ra_1_40
        dee.c "Ohhh FUCCKKKK!!!!"
        wt_image daughter_ra_1_41
        dee.c "{i}All too soon, though, her phone starts beeping and the experience ends.{/i}"
        dee_ra "Time's up, freshee.  Assume the position."
        wt_image daughter_ra_1_19
        dee.c "{i}I don't mind licking her out, and it's a good thing, too.{/i}"
        wt_image daughter_ra_1_20
        dee.c "{i}It's not difficult for me to make her cum ...{/i}"
        dee_ra "Good, freshee!  That feels so good!  Oh, wow!  Oh, I'm going to ... OOHHHH!!!!"
        wt_image daughter_ra_1_17
        dee.c "{i}... but satisfying her to the point where she'll let me get up is a whole different matter.{/i}"
        wt_image daughter_ra_1_18
        dee_ra "I don't have classes tomorrow morning, freshee, so I can stay up late.  I'm going to listen to some podcasts on my phone.  Show me how many times you can make me cum while I'm listening to them."
        wt_image daughter_ra_1_20
        player.c "{i}How many times was it?{/i}"
        wt_image daughter_ra_1_19
        dee.c "{i}I have no idea, all I know is it was enough to make my tongue so tired it ached.{/i}"
        call dee_talk_sex_life_final_question from _call_dee_talk_sex_life_final_question_1
    # first scene if you taught Dee to take control of her RA
    elif dee.talk_sex_life_status == 7:
        player.c "How are things with your RA?"
        wt_image daughter_house_1_25
        dee.c "Amazing!  I thought about your advice and spent a lot of time thinking about how I could put it into action.  It went better than I thought it possibly could."
        wt_image daughter_ra_1_2
        dee.c "{i}I took the initiative for a change, and approached her in the common room.{/i}  You are so beautiful, [dee_ra.name].  I want to spend some time alone with you, in private.  Preferably with your clothes off."
        if dee.has_tag('ra_used_strapon'):
            dee_ra "That's so sweet of you!  And sassy.  I like this new, more forward you.  Are you going to kneel down and service my pussy when we get to your room or are you angling to get a ride on my strap-on, first?"
        else:
            dee_ra "That's so sweet of you!  And sassy.  I like this new, more forward you.  Are you going to kneel down and service my pussy when we get to your room or do you want me to use the vibrator on you, first?"
        wt_image daughter_ra_1_3
        dee.c "I know how much you love my touch, and I do love watching you make puppy-dog eyes when I make you cum.  But, yes, when I said I wanted to see you naked, I was thinking about you using your toy on me.  Come back to my room and show me what you can do with it."
        if dee.has_tag('ra_used_strapon'):
            wt_image daughter_ra_1_9
            dee_ra "Okay, [dee.name], turn over and I'll put on the strap-on and set the timer on my phone."
            dee.c "Instead of the strap-on today, why don't you show me what you can do with your vibrator, instead."
        wt_image daughter_ra_1_25
        dee_ra "Okay, I have the vibrator.  Get on your knees and I'll use it on you."
        dee.c "I love how eager you are to please me, but I'm going to stay like this.  I want to watch you put the toy inside me."
        wt_image daughter_ra_1_50
        dee.c "No, don't turn it on.  Just fuck me with it."
        wt_image daughter_ra_1_51
        dee_ra "But you like how the vibrator feels inside you when it's buzzing."
        dee.c "You promised me you'd show me what you can do with your sex toy.  You don't need to use the batteries to make me feel good, do you?"
        wt_image daughter_ra_1_50
        dee_ra "I guess not.  Do you like this, when I twist and turn it around inside you?"
        dee.c "Keep going and let's find out."
        wt_image daughter_ra_1_52
        dee.c "Mmmm, good girl, [dee_ra.name].  You're make me wet.  Can you see my arousal?  Can you smell it?"
        wt_image daughter_ra_1_50
        dee.c "It smells good, doesn't it?  Get your nose closer to my pussy and smell how sexy it is."
        wt_image daughter_ra_1_52
        dee_ra "You're dripping, [dee.name].  And yes, it does smell good.  I'm going to turn the vibrator on now."
        dee.c "Not yet.  I want you to show me that you can get me off without turning the vibrator on.  And I want you to get your nose closer to my pussy.  Hold the vibrator in your mouth."
        wt_image daughter_ra_1_51
        dee_ra "What?"
        wt_image daughter_ra_1_50
        dee.c "Don't be shy.  You promised to show me what you can do with the toy.  Hold it between your teeth and fuck me with it.  Or don't you think you're hot enough to get me off like that?"
        wt_image daughter_ra_1_53
        dee.c "{i}Awkwardly, she put the toy in her mouth and held it between her teeth as she continued to fuck me with it.{/i}"
        dee.c "Do you know what I like best about this, [dee_ra.name]?  Other than seeing your pretty head between my legs?  You can't talk back to me now, not with the toy held in your mouth."
        wt_image daughter_ra_1_54
        dee.c "I can see you want to say something to me, probably a snide remark.  But you can't, not without letting go of the vibrator.  And you're too stubborn to do that, because you know that would mean I've won this little game we're playing.  So be a good, obedient girl and show me if you can bring to climax like this."
        wt_image daughter_ra_1_55
        dee.c "Drive it all the way in, [dee_ra.name].  I know you want to.  It'll put your nose right up against my sexy cunt.  You'll like that.  You'll like having your nose pressed up against my clit, smelling my arousal while you fuck me with the sextoy in your mouth."
        wt_image daughter_ra_1_56
        dee.c "Oh, [dee_ra.name].  You're such a good girl.  That's so hot, I feel like I should reward you.  Do you want to watch and smell me cum on the toy in your mouth?  Look at me and nod if you want that, [dee_ra.name]."
        wt_image daughter_ra_1_53
        dee.c "{i}That was the moment when I had the hardest time controlling myself.  I almost came as she nodded her head obediently.  It took everything I had to hold my climax back until she had her nose pressed up against my sex again.{/i}"
        wt_image daughter_ra_1_56
        dee.c "Ohhh FUCCKKKK!!!!"
        wt_image daughter_ra_1_13
        dee_ra "Okay, freshee, I admit it, that was hot.  Time for you to get me off, now."
        wt_image daughter_ra_1_10
        dee.c "Get you off?  That wasn't part of our deal.  I said I wanted to see you naked in my room, and I have.  I said I wanted you to show me what you can do with your sex toy and you have.  That's all I offered you, [dee_ra.name]."
        wt_image daughter_ra_1_8
        dee_ra "But you also said ..."
        dee.c "That I enjoy seeing the puppy-dog eyes you make at me when I make you cum?  I do enjoy that, [dee_ra.name], but I didn't say I wanted to see you make those puppy-dog eyes at me tonight.  I tell you what, though.  If you're a good, obedient girl for me tomorrow, I'll give you an orgasm for a reward."
        wt_image daughter_ra_1_49
        dee.c "{i}The conflict on her face was one of the sexiest things I've ever seen.  She didn't exactly say 'yes', but she definitely didn't say 'no', either.{/i}"
        wt_image daughter_house_1_25
        dee.c "I can't wait to lead her deeper into my control."
        $ dee.talk_sex_life_status = 8
    # second scene if you taught Dee to take control of her RA
    elif dee.talk_sex_life_status == 8:
        player.c "How are things with your RA?  Are you having any luck exerting contorl over her?"
        wt_image daughter_house_1_25
        dee.c "More than I thought I would!  Things are getting pretty intense.  She's more into me than I realized, and she's willing to take increasingly lopsided deals in order to spend time with me."
        wt_image daughter_ra_1_2
        dee.c "{i}What really changed our relationship, though, was when I convinced her to demonstrate to the whole floor that she was in a subordinate relationship with me.{/i}"
        dee.c "You're looking particularly pretty today, [dee_ra.name].  I think I'll take you back to my room and eat your pussy until I see that pretty face of yours cum.  You'd like that, wouldn't you?"
        dee_ra "You know I would!"
        wt_image daughter_ra_1_3
        dee.c "Good, so you won't mind doing something for me to earn that orgasm, will you?"
        dee_ra "That depends.  What exactly do you want?"
        wt_image daughter_ra_1_4
        dee.c "Something you'll enjoy.  Take my top off."
        wt_image daughter_ra_1_57
        dee.c "Now put your head between my legs.  You're going to eat me out here, in the TV Room, before I take you back to my room to let you have your reward."
        wt_image daughter_ra_1_8
        dee_ra "But the other girls?"
        dee.c "The other girls need to know who your mouth and pussy belong to.  You like to fool around, you're not shy about it, and I can't be around all the time to make sure you're not playing with someone besides me.  But the other girls can keep an eye on you for me when I'm not here."
        wt_image daughter_ra_1_49
        dee.c "Oh, hi Sharon!  Can you ask the other girls to come in?  [dee_ra.name] has something she wants to show everyone."
        wt_image daughter_ra_1_42
        dee.c "{i}Once everyone had gathered, I gave [dee_ra.name] her instructions.  I wasn't sure she'd follow them, but I was so turned on when she did.{/i}"
        wt_image daughter_ra_1_49
        dee_ra "[dee.name] wants all of you to know that if you catch me trying to sneak someone into my room, you should report me to her."
        dee.c "Explain why to them, [dee_ra.name]."
        wt_image daughter_ra_1_57
        dee_ra "Because [dee.name] gives me the best orgasms, but I need to earn them from her, and I want to be a good girl for her so she'll keep giving them to me."
        wt_image daughter_ra_1_48
        dee.c "I'm going to let [dee_ra.name] earn an orgasm now, to prove that she's serious.  Let the girls know you want them to stay so that you have an audience, and why."
        wt_image daughter_ra_1_6
        dee.c "{i}It wasn't easy for [dee_ra.name] to reply, but evenutally she did.{/i}"
        wt_image daughter_ra_1_43
        dee_ra "I'm going to eat [dee.name] out here in the TV Room so that she'll give me an orgasm when she takes me back to her room.  I have to do this here in public with an audience so that you all understand the nature of our relationship and won't hesitate to report me to [dee.name] if you catch me trying to be with someone else."
        wt_image daughter_ra_1_58
        dee.c "{i}Some of the girls left, of course, either in disgust or out of embarrassment, but enough stayed to make the situation incredibly hot.  If it wasn't my best orgasm ever, it was definitely top three ...{/i}  Ohhh FUCCKKKK!!!!"
        wt_image daughter_ra_1_20
        dee.c "{i}The orgasm I gave her when I got her back to my room was definitely one of the best [dee_ra.name]'s ever had, too.{/i}"
        dee_ra "Oh, thank you, [dee.name]!  That feels so good!!  Oh, wow!!  Oh, I'm going to ... OOHHHH!!!!"
        wt_image daughter_ra_1_8
        dee_ra "I can't believe I'm in a submissive relationship and enjoying it."
        wt_image daughter_ra_1_16
        dee.c "Put your head between my legs and say that again."
        wt_image daughter_ra_1_14
        dee_ra "I'm your submissive, [dee.name], and I like it."
        wt_image daughter_ra_1_15
        dee.c "{i}She spends a lot of time between my legs now, usually in my room, sometimes in her room, occasionally in the common areas of the dorm when I feel like subjecting her to some pleasurable humiliation.{/i}"
        wt_image daughter_house_1_25
        if dee.ready_for_mom > 2:
            dee.c "Thank you for helping me get to this point with [dee_ra.name].  I don't think it would have happened without your help.  Between her and Mom, you've really helped me become comfortable taking control of other women."
            sys "There are no other women in the game for [dee.name] to take control of, but if you locate any appropriate artwork between [dee.name] and other characters in the game, let Wifetrainer know and he'll try to work it into the game."
        else:
            dee.c "Thank you for helping me get to this point with [dee_ra.name].  I don't think it would have happened without your help."
        $ dee.talk_sex_life_status = 9
    # follow up scene if you taught Dee to take control of her RA
    elif dee.talk_sex_life_status == 9:
        player.c "How's life with your submissive RA?"
        wt_image daughter_house_1_25
        dee.c "Hot!"
        wt_image daughter_ra_1_57
        dee.c "{i}When we're together in the common room, I have her curl up on my lap like a cat.{/i}"
        wt_image daughter_ra_1_48
        dee.c "{i}Sometimes I have her worship my tits while we're watching TV together.{/i}"
        wt_image daughter_ra_1_58
        dee.c "{i}Occasionally, when I feel like giving her some pleasurable humiliation, I have her eat me out where other girls can watch her, if they want.{/i}"
        wt_image daughter_ra_1_14
        dee.c "{i}Most often, I have her pleasure me when we're alone in my room or hers.{/i}"
        wt_image daughter_ra_1_15
        dee.c "{i}She gives me lots of orgasms ...{/i}  Ohhh FUCCKKKK!!!!"
        wt_image daughter_ra_1_20
        dee.c "{i}Once or twice a week, I let her have one of her own.{/i}"
        dee_ra "Oh, thank you, [dee.name]!  That feels so good!!  Oh, wow!!  Oh, I'm going to ... OOHHHH!!!!"
        wt_image daughter_ra_1_10
        dee.c "{i}I wasn't sure how she'd respond to me expecting her to be exclusive to me, but she's taken to it really well.{/i}"
        wt_image daughter_ra_1_23
        dee.c "If I ask the girls if they've seen you bringing anyone into your room when I'm not around, or sneaking around campus with someone else, what are they going to tell me, [dee_ra.name]."
        wt_image daughter_ra_1_22
        dee_ra "There's been no one, [dee.name].  I know I need to keep my mouth and pussy available for you alone or you won't play with me and make me cum ever again."
        wt_image daughter_ra_1_23
        dee.c "Tell me how hot it is that I've been with two other girls and a boy already this week, but you're only allowed to be with me?"
        wt_image daughter_ra_1_16
        dee_ra "Mmmm, [dee.name], that is so hot!  I've had less sex this semester than in any year before, but enjoyed the sex I have had more than ever!  I love being your submissive exclusive."
        wt_image daughter_ra_1_15
        dee.c "{i}She means it, too.  When she first let me take control of her, I know she thought it was just going to be a short-term experiment.  I'm sure it's a shock to her how turned on she gets when I have her service me after I've been with someone else.{/i}"
        dee_ra "Oh, [dee.name]!  The boy you were with, that was today wasn't it?  I can taste him on you!!"
        wt_image daughter_ra_1_22
        dee.c "There's more of him inside me."
        wt_image daughter_ra_1_23
        dee.c "{i}At moments like that, watching her hips twitching in excitement, I wonder if maybe this will end up being a longer relationship than I expected.{/i}"
        player.c "{i}So it's love, is it?{/i}"
        wt_image daughter_ra_1_8
        dee.c "{i}Still mostly lust, but there are moments that make me think maybe this is love, or could become love.{/i}"
        wt_image daughter_house_1_25
        if dee.ready_for_mom > 2:
            dee.c "Thank you for helping us get together like this.  I don't think it would have happened without you.  Between [dee_ra.name] and Mom, you've really helped me improve my relationships with the women in my life."
        else:
            dee.c "Thank you for helping us get togther like this.  I don't think it would have happened without you."
    # first scene of RA dominating Dee if you told Dee to accept being her bitch
    elif dee.talk_sex_life_status == 10:
        wt_image daughter_house_1_23
        player.c "How's life as your RA's bitch?"
        wt_image daughter_ra_1_3
        dee.c "{i}Interesting.  As you expected, she wasn't content to dominate me in the privacy of our rooms.  She wanted control over me in the public area of our dorm, too.{/i}"
        wt_image daughter_ra_1_4
        dee.c "What are you doing?"
        wt_image daughter_ra_1_5
        dee_ra "Taking a look at my property."
        wt_image daughter_ra_1_7
        dee_ra "You don't object to being naked while we watch TV together, freshee?"
        wt_image daughter_ra_1_6
        dee.c "The other girls ..."
        wt_image daughter_ra_1_43
        dee_ra "The other girls are not to be allowed to look at you while I'm not around, understood?  But when I am around, I'll decide how much of you they get to see."
        wt_image daughter_ra_1_44
        dee.c "Hi Sharon, hi Tatiana.  [dee.name]'s going to be licking my nipples while we watch TV.  If that makes you feel awkward, we'll be done in about an hour, but if it doesn't you're welcome to join us to watch the show."
        wt_image daughter_ra_1_11
        dee.c "{i}She didn't ask if licking her tits in front of an audience made me feel awkward, she just presented her breasts to me.{/i}"
        wt_image daughter_ra_1_12
        dee.c "{i}I tried to watch the show as best I could as I licked her nipples, in some sort of vain attempt to keep up the pretense in front of the other girls that this was a normal way to spend time with a girlfriend.  Somehow, all I managed to do was turn myself on almost as much, if not more than, I was turning [dee_ra.name] on.{/i}"
        wt_image daughter_ra_1_45
        dee_ra "Girls, [dee.name] is getting horny.  I'm going to let her lick my cunt while we finish the show.  Don't worry, we'll be quiet."
        wt_image daughter_ra_1_42
        dee.c "Wait, no.  I can't."
        wt_image daughter_ra_1_46
        dee_ra "Sharon, can you mute the TV for a minute?  I need to discipline, [dee.name]."
        wt_image daughter_ra_1_47
        dee.c "{i}As soon as the TV was muted, she addressed me sternly.{/i}"
        dee_ra "When I tell you to lick my cunt, you either drop to your knees or you ask permission to service me in private, freshee."
        wt_image daughter_ra_1_42
        dee.c "{i}I leaned in close and whispered ...{/i}  May I please have permission to service you in private?"
        dee_ra "Louder, freshee.  Speak up!"
        wt_image daughter_ra_1_47
        dee.c "{i}Humiliated and surprisingly wet, I croaked out my request as loudly as I could ...{/i}  May I please be allowed to service you in private!"
        wt_image daughter_ra_1_46
        dee_ra "Looks like the TV Room's all yours, girls.  [dee.name] and I will be in my room if anybody needs me, otherwise I'll see you tomorrow."
        wt_image daughter_ra_1_19
        dee.c "{i}It was a long night, but not an unpleasant one.{/i}"
        wt_image daughter_ra_1_18
        dee_ra "You have three minutes to play with yourself.  Feel free to cum while you're doing so, as long as your tongue never leaves my cunt."
        wt_image daughter_ra_1_17
        dee.c "Ohhh FUCCKKKK!!!!"
        wt_image daughter_ra_1_21
        dee_ra "I told you this is where you belong.  You're so silly for taking so long to figure that out."
        wt_image daughter_house_1_23
        player.c "Is it where you belong?"
        wt_image daughter_house_1_2
        dee.c "I don't think so, no.  Not long term.  But I'm doing as you suggested and embracing the situation, and getting as much as I can out of being her bitch for at least the rest of the semester.  College is for learning stuff, right?  And I'm certainly learning a lot from [dee_ra.name], about myself and about domination and submission."
        $ dee.talk_sex_life_status = 11
    # follow up scene of RA dominating Dee if you told Dee to accept being her bitch
    elif dee.talk_sex_life_status == 11:
        wt_image daughter_house_1_23
        player.c "How's life as your RA's bitch?"
        wt_image daughter_ra_1_4
        dee.c "{i}Interesting.  I'm kept in various states of undress in the dorm when she's around, regardless of whether there are other girls around or not.{/i}"
        wt_image daughter_ra_1_48
        dee.c "{i}Sometimes she keeps my nipples hard.  She says it's because she likes seeing them sticking out, but I think it's mostly because she likes the other girls seeing how aroused I am near her.{/i}"
        wt_image daughter_ra_1_11
        dee.c "{i}More often, I'm the one required to pleasure her nipples while we're sitting together.  It's surprising how quickly it's become normal for me to be licking and suckling on [dee_ra.name]'s breasts while the girls on our floor are all sitting around watching TV.{/i}"
        wt_image daughter_ra_1_44
        dee.c "{i}[dee_ra.name] sets the tone for that.  She acts like there's nothing out of the ordinary and the other girls go along with that.  I do, too.{/i}"
        wt_image daughter_ra_1_45
        dee_ra "Hi Sharon, hi Tatiana.  That is such a cute skirt!  [dee.name], don't you like Tatiana's outfit?"
        wt_image daughter_ra_1_12
        dee.c "It's really cute, Tatiana.  It looks really nice on you."
        wt_image daughter_ra_1_8
        dee.c "{i}The only times there's any discussion of our relationship is when I balk at one of her instructions.{/i}"
        dee_ra "My pussy is a little wet.  Use your tongue to clean it off."
        wt_image daughter_ra_1_42
        dee.c "{i}Then I'm expected to address the whole room when I offer an alternative to what she wanted.{/i}"
        dee_ra "Girls, mute the TV for a moment.  I think [dee.name] has something she wants to say."
        wt_image daughter_ra_1_47
        dee.c "May I please be allowed to lick your pussy clean in private, rather than here in front of everyone."
        player.c "{i}Have you ever considered it might be less humiliating just to lick her pussy there in public?  It seems like the other girls are pretty much inured to yours and [dee_ra.name]'s antics, anyway.{/i}"
        wt_image daughter_house_1_23
        "[dee.name] blushes a fierce shade of red as she replies."
        wt_image daughter_ra_1_21
        dee.c "Yes, lately I have been.  The other girls don't say anything and thankfully with my head between [dee_ra.name]'s legs I can't see what sort of looks they may be giving me.  The only look I can see is on [dee_ra.name]'s face, and I can tell I'm making her very happy, which weirdly makes me very wet, despite the humiliation I feel."
        wt_image daughter_house_1_22
        if dee.ready_for_mom > 2:
            dee.c "Thank you for arranging things such that I ended up in this situation.  I would never have voluntarily gone down this path on my own, but it's made my first year in university something I'll never forget.  I doubt I'll ever be a submissive in an on-going relationship again, but it's helped me to better understand and give Mom what she's looking for.  Maybe it will help with future relationships, too."
        else:
            dee.c "Thank you for arranging things such that I ended up in this situation.  I would never have voluntarily gone down this path on my own, but it's made my first year in university something I'll never forget.  I doubt I'll ever be a submissive in an on-going relationship again, but it's helped me to better understand why it can be enjoyable to give up control to someone else.  Maybe that will help me with future relationships."
    return

label dee_talk_sex_life_final_question:
    wt_image daughter_house_1_23
    dee.c "What should I do?"
    player.c "What do you mean?"
    wt_image daughter_house_1_2
    if dee.has_tag('help_her_turn_tables_ra'):
        dee.c "What I mean is, you made this happen.  I don't know why you did, other than you enjoy manipulating women and their sex-lives, but you did.  You said you'd help me turn the tables on her, but I'm not sure you meant it.  So how does this end?"
    else:
        dee.c "What I mean is, you made this happen.  I don't know why you did, other than you enjoy manipulating women and their sex-lives, but you did.  So how does this end?"
    $ title = "What do you say to her?"
    menu menu_dee_sex_life_final_question:
        "How do you want it to end?":
            wt_image daughter_house_1_22
            dee.c "I want her to be spending her nights between my legs, not the other way around.  But I don't know how to do that, because she's become too good at putting me under her thumb and making me enjoy being there."
            jump menu_dee_sex_life_final_question
        "Embrace being [dee_ra.name]'s bitch":
            wt_image daughter_house_1_24
            player.c "I suggest you enjoy the situation while it lasts.  She's going to find a new playtoy when the next batch of freshmen arrive, isn't she?"
            wt_image daughter_house_1_22
            dee.c "Probably"
            player.c "Not probably, definitely.  Get as much out of the experience as you can.  She's a sexy, dominant young woman.  You can learn from her, either how to be a sexy, dominant woman yourself or how to please the Dommes that come into your life.  Have you let her play with you in the public areas of your dorm, yet?"
            wt_image daughter_house_1_2
            dee.c "What??  No!  I'd get a reputation."
            player.c "A reputation as what?  [dee_ra.name]'s bitch?  Don't you think the other girls on the floor have figured that out by now?  She owns you for the rest of this term.  Embrace the situation, [dee.name].  When she wants control over you, let her have it, regardless of where that is.  It will make her happy, and you'll find that will make you happy, too."
            wt_image daughter_house_1_23
            if dee.has_tag('help_her_turn_tables_ra'):
                rem tags 'help_her_turn_tables_ra' from dee
                dee.c "I guess.  This isn't going to be easy for me.  Does this mean you're not going to help me turn the tables on [dee_ra.name] after all?"
                player.c "Sometimes the hottest situations are the most difficult ones.  As challenging as you're going to find it, with what I've learned about you, I've come to realize this is a better path for you."
            else:
                dee.c "I guess.  This isn't going to be easy for me."
                player.c "Sometimes the hottest situations are the most difficult ones."
            $ dee.talk_sex_life_status = 10
        "I'll teach you to turn the tables on her":
            if dee.dom_discussion_count < 2:
                player.c "I could teach you how to take control of her, if you'd like?  You'd need to agree to submit to me in my dungeon, though, so I can train you."
                wt_image daughter_house_1_2
                dee.c "I don't even want her dominating me, why would I want you to do so?"
                $ title = "Convince her?"
                menu:
                    "Yes":
                        add tags 'help_her_turn_tables_ra' to dee
                        player.c "Have you forgotten about your experience with Marilyn?"
                        wt_image daughter_house_1_24
                        dee.c "What does Marilyn have to do with it?"
                        player.c "You remember how she made you feel. 'Putty in her hands' were your words.  You're not naturally submissive, but you were with her, and you liked it.  I can help you recapture that feeling.  It would be a great learning experience for you.  If you're not sure you want to explore your submissive side, what about using it as a way to explore your dominant side.  You'd like to be able to make people feel what Marilyn made you feel, wouldn't you?"
                        wt_image daughter_house_1_22
                        dee.c "You could teach me to take control of others as easily as Marilyn took control of me?  Even though I'm not a powerful woman like she is?"
                        player.c "You'll teach yourself, I'll just be the role model.  The more experiences you have as a submissive, the better you'll understand how the person you're trying to control is feeling."
                        wt_image daughter_house_1_1
                        player.c "I can see you're not ready to say 'yes' right now, but think about it.  There's no need to rush, we can do this when you're ready."
                        $ dee.dom_discussion_count = 2
                    "Not today":
                        "You can raise this with her again on a future visit, if you want."
                        $ dee.dom_discussion_count = 1
            elif dee.has_tag('help_her_turn_tables_ra'):
                player.c "I said I'd help you turn the tables on her and I will.  Keep spending time with me in my dungeon and I'll teach you what you need to know to start taking control of [dee_ra.name]."
            else:
                add tags 'help_her_turn_tables_ra' to dee
                player.c "Keep spending time with me in my dungeon and I'll teach you what you need to know to start taking control of [dee_ra.name]."
                dee.c "Okay.  I'll try to make myself available more often.  I'm anxious to learn what you have to teach me."
            $ dee.talk_sex_life_status = 6
        "Nothing right now":
            $ dee.talk_sex_life_status = 6
    return

label dee_talk_mother:
    if dee.marilyn_event_status == 0:
        "Before talking about her mother's fantasy, wait until [dee.name]'s had an experience that will help her understand how her mother feels."
    elif dee.ready_for_mom == 0:
        add tags 'talked_mom_today' to dee
        player.c "Tell me, [dee.name].  What did you learn from your time with Marilyn and your professor?"
        wt_image daughter_house_1_2
        dee.c "People in power will use their power to obtain access to sexual partners, regardless of whether they are good people or not, and regardless of whether they're a man or a woman."
        player.c "Right, I remember.  The subject for your new thesis.  More generally, though.  What does it tell you about the nature of power?"
        wt_image daughter_house_1_25
        dee.c "That it's sexy. That people are attracted to it."
        player.c "Do you think there's anything wrong with being attracted to someone because of their perceived power. If a woman, for example, fantasizes about someone strong and confident, do you think it's wrong for her to have those fantasies?"
        wt_image daughter_house_1_24
        dee.c "No, there's nothing wrong with that."
        player.c "What if it's someone she shouldn't fantasize about?  Forbidden fruit, for example."
        wt_image daughter_house_1_22
        dee.c "Like my professor and I?  Or a secretary and her boss?  Sure, I can understand that.  She shouldn't have a relationship with him, but I can understand why she may fantasize about it."
        player.c "And if she could have that relationship without hurting anybody, do you think that would be okay?"
        wt_image daughter_house_1_25
        dee.c "Sure, if no one gets hurt. Why not?"
        player.c "What if I told you somebody was having those fantasies about you?"
        wt_image daughter_house_1_21
        dee.c "Me?  I don't have any power over anyone."
        player.c "Are you sure?  You know what you want and you're not afraid to go after it.  You're confident in yourself intellectually and sexually. You may not have acquired any of the external trappings of power yet, but you behave like someone accustomed to and conformable with exercising authority.  Someone close to you could easily grow to see you the same way you saw Marilyn when you met her."
        "[dee.name] looks puzzled for a moment, then her face goes white. Very quietly, she replies:"
        wt_image daughter_house_1_22
        dee.c "You're talking about my Mom, aren't you?"
        wt_image daughter_house_1_23
        "There's silence for a while. You let the thought sink in, and let [dee.name] process the conflicting emotions that pass over her."
        player.c "Are you angry at her?"
        wt_image daughter_house_1_22
        "[dee.name] shakes her head."
        dee.c "If ... if she feels that way, I'm sure she can't help it."
        player.c "No, I don't think she can.  I'm sure she would make those thoughts go away if she possibly could.  She can't, and it eats at her."
        wt_image daughter_house_1_23
        dee.c "What ... What do you think I should do?"
        player.c "What does your gut tell you?"
        wt_image daughter_house_1_22
        dee.c "That I should tell her it's okay, Mom. I know and I'm not upset with you."
        player.c "That would be a great first start. What else do you think you could do for her?"
        wt_image daughter_house_1_23
        "[dee.name] sits quietly for quite a while.  You let her think and process as long as she needs before she can respond."
        dee.c "You're suggesting I should have sex with my Mom."
        player.c "I'm not suggesting anything.  I'm giving you information.  Your mother has been struggling with her sexual desire for you. She knows it's wrong, but she can't help herself. She's drawn to the authority and self-confidence you project.  If you wanted to, you could seduce her as easily as Marilyn seduced you.  The question is, do you want to? What does your pussy tell you?"
        wt_image daughter_house_1_22
        dee.c "My pussy is pretty messed up right now.  I've never had anyone see me the way you say Mom sees me. The idea of having that kind of power over someone, it's pretty exciting.  I just wish it was somebody..."
        player.c "Somebody what?  Safe?  I bet your professor wishes he attracted women who weren't his students as easily as he does those who aren't supposed to sleep with him. Every student he has sex with is one more chance that someone blows the whistle on him and creates a lot of trouble.  Forbidden lust isn't safe, but it's often the more powerful for that."
        wt_image daughter_house_1_23
        "[dee.name] nods and then exhales deeply."
        dee.c "I really don't know what I want to do with this information, but I do know something."
        wt_image daughter_house_1_10
        dee.c "I desperately need to fuck right now.  Will you please fuck me?"
        wt_image daughter_house_1_4
        "[dee.name] slides off the sofa and out of her clothes. You can smell her pussy juices from here as she pulls her panties aside."
        $ title = "What do you want to do?"
        menu:
            "Fuck her":
                add tags 'sex_before' to dee
                wt_image daughter_house_1_16
                dee.c "Climb up here with me.  I'm so wet.  I need you inside me right now."
                wt_image daughter_house_1_47
                "You sit on the sofa and [dee.name] climbs on top of you.  She wasn't kidding about her pussy being wet.  Her juices drip onto your cock as she lowers herself onto you."
                wt_image daughter_house_1_17
                dee.c "Oohhhhh  That feels good!"
                wt_image daughter_house_1_50
                "[dee.name] starts riding you, faster and faster, grinding herself onto your cock."
                wt_image daughter_house_1_51
                "It's clear she wants to be in control.  You're just a hard cock to her right now, an instrument for her to use to cleanse the dirty desires the conversation about her mother has stirred up in her head.  Not that you're complaining."
                wt_image daughter_house_1_52
                dee.c "Oohhh!  Oh yeah!!  Give me that hard cock!"
                wt_image daughter_house_1_102
                dee.c "More!  Take my tit in your mouth and suck!"
                wt_image daughter_house_1_18
                "She pushes her breast forward, unwilling to take 'no' for an answer.  You take her pert nipple between your lips, then suckle it and as much of her tit as you can fit into your mouth.  She gasps and picks up the speed at which she's riding you."
                wt_image daughter_house_1_103
                dee.c "Ohhh!  Ohh, that feels good!"
                wt_image daughter_house_1_50
                "It certainly does, and her wet pussy sliding up and down your cock feels awfully good, too."
                wt_image daughter_house_1_104
                dee.c "Ohhh FUCCKKKK!!!!"
                wt_image daughter_house_1_13
                "As her orgasm washes over her - and before you can climax yourself - she climbs off of you."
                dee.c "Thanks.  I really needed that."
                $ title = "What do you do?"
                menu:
                    "Remind her you haven't cum yet":
                        wt_image daughter_house_1_46
                        dee.c "What?  Oh right.  Here, I'll look after that for you."
                        wt_image daughter_house_1_53
                        "If she has any reservations about tasting her own cum juices, she doesn't let on ..."
                        wt_image daughter_house_1_54
                        "... as she licks your dick clean of all residue from having been inside her pussy ..."
                        wt_image daughter_house_1_55
                        "... before taking you inside her mouth."
                        wt_image daughter_house_1_56
                        "As blowjobs go, it's a typical college girl effort ..."
                        wt_image daughter_house_1_57
                        "... long on enthusiasm and effort, short on subtlety or technique ..."
                        wt_image daughter_house_1_55
                        "... but more than pleasurable enough to get the job done."
                        wt_image daughter_house_1_58
                        $ title = "Where do you want to cum?"
                        menu:
                            "In her":
                                add tags 'failed_swallow' to dee
                                wt_image daughter_house_1_59
                                player.c "[player.orgasm_text]"
                                wt_image daughter_house_1_60
                                if donna.has_tag('cum_slut'):
                                    "Unlike her mother, it seems [dee.name] hasn't acquired a taste for cum ..."
                                else:
                                    "It seems [dee.name] doesn't enjoy, or at least doesn't have much experience with, the taste of cum ..."
                                wt_image daughter_house_1_61
                                "... but she diligently pumps as much seed out of your balls as they have to give."
                                wt_image daughter_house_1_62
                                "When you finally finish, she gags slightly as she swallows your load."
                                player.c "You okay?"
                                wt_image daughter_house_1_27
                                dee.c "Yeah, I'm fine.  It's not easy catching your cum without choking when your cock is spurting like that.  I need to run now, okay?  My mind's all over the place."
                                player.c "I take it you don't have a lot of experience with giving blowjobs."
                                wt_image daughter_house_1_26
                                dee.c "I have a little, but most of the guys I've been with seemed to prefer facials.  I haven't had to try and catch a full load like that in my mouth very often.  It's trickier than it sounds."
                                player.c "Maybe you should ask your Mom for tips on how she does it?"
                                wt_image daughter_house_1_21
                                dee.c "Ewww!!  That conversation's not happening!"
                                player.c "Then I guess I'll just have to teach you how to swallow."
                                wt_image daughter_house_1_22
                                dee.c "Great!  Next time I'll bring a guy with me and you can show me how you swallow his load.  Shhh!  Don't try to explain yourself, I know what I heard."
                                $ dee.swallow_count += 1
                            "On her":
                                add tags 'facial_before' to dee
                                wt_image daughter_house_1_63
                                player.c "[player.orgasm_text]"
                                wt_image daughter_house_1_64
                                dee.c "I'm going to get cleaned up and go now, okay?  My mind's all over the place."
                                $ dee.facial_count += 1
                        player.c "Sure, kid.  You have a lot to think about.  Go take some time and think."
                        $ dee.blowjob_count += 1
                        orgasm notify
                    "Submissively ask permission to cum":
                        wt_image daughter_house_1_46
                        dee.c "What?  Oh right.  Here, I'll ..."
                        wt_image daughter_house_1_41
                        dee.c "Wait, you know what?  If you want to cum, go ahead."
                        $ title = "What do you do?"
                        menu:
                            "Jerk off while she's watching":
                                wt_image daughter_house_1_40
                                "[dee.name] lets you look at her body, but refrains from touching you.  She does, however, watch intently as you get yourself off, and provides instructions as you start to cum."
                                dee.c "Dump your load on the floor at my feet!"
                                player.c "[player.orgasm_text]"
                                wt_image daughter_house_1_29
                                dee.c "I really need to get going.  That was hot, but my mind's all over the place right now.  You can clean that mess up after I leave, okay?"
                                orgasm notify
                            "Let yourself be edged":
                                wt_image daughter_house_1_29
                                dee.c "You'd rather stay blue-balled?  That's kind of hot, actually.  Sorry, my mind's all over the place right now.  I need to get going.  I'll look after you another time, okay?"
                        player.c "Of course, [dee.name].  You have a lot to think about.  Go take some time and think."
                    "Let her go home":
                        player.c "TI'm glad you had fun.  You have a lot to think about.  Go take some time and think."
                wt_image daughter_house_1_26
                "She nods, then gets herself dressed and leaves."
                $ dee.orgasm_count += 1
            "Send her home":
                player.c "I think it would be more productive for you to channel that sexual tension into your thinking."
                wt_image daughter_house_1_32
                dee.c "You think being horny is going to help me make better decisions?"
                player.c "Yes, if you're honest with yourself about why you're so horny."
        $ dee.ready_for_mom = 1
        call dee_visit_end from _call_dee_visit_end_3
    else:
        add tags 'talked_mom_follow_up_today' to dee
        player.c "How are things with your Mom?"
        if dee.ready_for_mom == 1:
            wt_image daughter_house_1_22
            dee.c "Surprisingly good, considering I'm a nervous wreck around her.  I want to do this for her.  I want to bring my Mom's fantasy to life, but I'm not brave enough to do it on my own.  I hope you'll be ready to help me the next time I'm available to visit?"
        elif dee.ready_for_mom == 2:
            wt_image daughter_house_1_24
            dee.c "Surprisingly good.  Obviously you're right and going through with making her fantasy a reality would have been a big mistake.  But I boss her around a bit more than I used to, in a loving sort of way, and she seems to respond really well to it."
            wt_image daughter_house_1_25
            dee.c "I try not to think about what she does, though, when she goes to bed after I spend an evening having her cater to my every whim."
            "The look on her face suggests she does think about it, a lot, and it turns her on."
        elif dee.ready_for_mom > 2:
            wt_image daughter_house_1_22
            "She grins."
            dee.c "Wouldn't you like to know?  All I'll tell you is that things are good.  Very good.  I'm sure your imagination can do the rest."
            wt_image daughter_house_1_25
            dee.c "I wonder if you're going to jerk off tonight, thinking about my Mom and me?  Don't tell me, I'll make up my own mind about what I think you'll be up to."
    return


# Hypno Actions
label dee_hypnosis_start:
    if dee.in_area('house'):
        call focus_image from _call_focus_image_64
        player.c "Look at this for me, [dee.name].  Look and listen.  Listen to my voice.  Listen to my voice.  Only my voice now.  Only my voice."
        wt_image daughter_house_1_2
        "She falls under your trance."
        if dee.hypno_count == 0:
            player.c "We'll have a chat now, [dee.name].  We should be comfortable for our chat.  You want to be comfortable for our chat and you want me to be comfortable for our chat.  Take your top off and bare your breasts so that we can both be comfortable."
            wt_image daughter_house_1_22
            dee.c "That's an unusual request."
            player.c "Do you think women's breasts are something dirty that need to be hidden away?"
            wt_image daughter_house_1_2
            dee.c "No"
            player.c "Do you think they're inherently sexual organs whose only purpose is to titillate and excite men?"
            wt_image daughter_house_1_21
            dee.c "No, of course not."
            player.c "Do you think women should have the right to bare their breasts wherever and whenever they want?"
            wt_image daughter_house_1_24
            dee.c "Yes, absolutely."
            player.c "As a liberated woman yourself, you're probably feeling oppressed by the expectation that you should keep your breasts hidden while we talk."
        else:
            player.c "We'll have a chat now, [dee.name].  We should be comfortable for our chat.  You want to be comfortable for our chat and you want me to be comfortable for our chat.  Of course, since the patriarchy is forcing you to keep your breasts covered up, it must be difficult for you to be comfortable.  You'd like to do something about that."
        wt_image daughter_house_1_26
        dee.c "I want to take off my top.  There's no reason why a woman can't have a normal conversation with her breasts out.  Men do it all the time."
        wt_image daughter_house_1_75
        player.c "Of course, [dee.name].  You and you alone should decide what you do with your body.  Since you want to have your breasts out, you should take them out."
        wt_image daughter_house_1_3
        dee.c "I'm more comfortable, now.  What did you want to talk to me about?"
        $ dee.training_session()
        $ dee.hypno_session() # deducts energy and records she was hypno'd
        # system now automatically goes on to the menu of hypnosis options, i.e. actions with the context _hypnosis for this client
    else:
        "Not here."
        $ ignore_context_change = True # this breaks the hypno sequence before calling hypnosis_context menu
    return

label dee_bj_hypnosis:
    if dee.hypno_blowjob_count == 0:
        wt_image daughter_house_1_3
        player.c "Now that you're comfortable, we should talk more about why you react poorly when I tell you I want to sleep with you."
        wt_image daughter_house_1_130
        dee.c "Isn't that obvious?  You're treating me like a sex object."
        player.c "I see you as a potential sex partner.  It's not the same thing.  Don't women have sexual urges, too?"
        wt_image daughter_house_1_129
        dee.c "Of course they do."
        player.c "Shouldn't they be allowed to act on those sexual urges without being judged negatively by society?"
        dee.c "Yes"
        player.c "Do women always have to wait for men to make the first move, or should they be free to express their interests by making the first move?"
        dee.c "They should be free to express their sexual interests."
        player.c "So if you wanted to take my cock out and suck it, is there any reason why you shouldn't just say so?"
        wt_image daughter_house_1_130
        dee.c "No.  But I don't want to suck your cock."
        player.c "That's what society teaches young women.  Society says it's wrong to have those types of urges, but it's not.  You like sucking cock, but you've been taught to suppress that urge."
        wt_image daughter_house_1_128
        dee.c "I do like sucking cock.  I like the power it gives me.  I love how men turn into kittens as soon as you take their cock in your mouth."
        player.c "You shouldn't feel bad about having those feelings.  Isn't it okay for women to have power over men?"
        wt_image daughter_house_1_3
        dee.c "Yes.  I'd like to have power over men."
        player.c "Would you like to have power over me?"
        wt_image daughter_house_1_129
        dee.c "Yes.  I'd like to wipe that smug confident look off of your face."
        player.c "That's very understandable, [dee.name].  You're a smart woman.  How could you have power over me, [dee.name]?"
        wt_image daughter_house_1_130
        dee.c "I could suck your cock.  You'd look like a helpless kitten if I started to lick your dick.  But if I did that now, you'd think I was easy."
        player.c "Are men viewed negatively when they have sex with someone they've just met?"
        wt_image daughter_house_1_129
        dee.c "No"
        player.c "Should women be viewed negatively when they have sex with someone they've just met?"
        wt_image daughter_house_1_129
        dee.c "No"
        player.c "Isn't it important for women to do what they want regardless of how other people view them?"
        wt_image daughter_house_1_130
        dee.c "Yes"
        player.c "Are you going to let how I view you dictate how you act?"
        wt_image daughter_house_1_3
        dee.c "No, no I'm not."
        player.c "So why shouldn't you take power over me, if that's what you want to do?"
    else:
        wt_image daughter_house_1_3
        player.c "It's too bad the patriarchy oppresses women like you and gives all the power to men like me.  You'd like to have power over me.  If only there was some way you could exert your power over me."
        wt_image daughter_house_1_130
        dee.c "I could suck your cock.  That would wipe that smug confident look off of your face.  You'd look like a helpless kitten if I started to lick your dick.  But I don't want to suck your cock."
        player.c "I understand, [dee.name].  Society has taught you that it's wrong to suck men's cocks.  Society doesn't want you to take power over me by sucking my cock.  Society wants to make sure you stay powerless, doesn't it? "
        wt_image daughter_house_1_129
        dee.c "Yes.  Society exerts multiple axes of control over women to control their behavior and prevent them from exercising their innate power."
        wt_image daughter_house_1_3
        dee.c "I shouldn't let society dictate when and how I exert power over a man."
    wt_image daughter_house_1_128
    "[dee.name] grins mischievously as she slides down out of the sofa."
    dee.c "You look pretty composed and pulled together.  I bet you'll look a lot different once I have your dick in my hand."
    wt_image daughter_house_1_131
    dee.c "And when I take out your cock and start sucking it, you're going to be putty in my hands."
    wt_image daughter_house_1_132
    "As she predicted, you make no move to stop her as she unceremoniously pops your cock in her mouth and starts sucking on the head of it."
    wt_image daughter_house_1_133
    "She watches you as she sucks on your cock, a satisfied look on her face.  If she stopped now, she probably could get you to do a lot of things in return for her putting your cock back in her mouth."
    wt_image daughter_house_1_5
    "Happily for you, she doesn't stop sucking you.  She keeps her warm lips wrapped around the head of your cock and suckles enthusiastically."
    wt_image daughter_house_1_101
    "It's a weird blow job, as the hypnotized woman seems to be trying to exert dominance over you by extracting an orgasm from you using the power of suction alone, her lips never straying past the head of your cock."
    wt_image daughter_house_1_133
    "Despite the lack of subtlety, the technique works in this situation, as you watch the mind-controlled young feminist attempt to assert power in your relationship on her knees with your dick in your mouth."
    wt_image daughter_house_1_86
    "When the pleasure inside you builds to the point that you begin to spurt, she removes your cock from her mouth at points it at herself"
    wt_image daughter_house_1_134
    player.c "[player.orgasm_text]"
    wt_image daughter_house_1_14
    player.c "I suppose you're pleased with yourself?"
    wt_image daughter_house_1_135
    dee.c "Yes, I am.  You made puppy eyes when you were cumming.  Not so powerful now, are you?"
    wt_image daughter_house_1_65
    player.c "Do you really think it's appropriate to exert authority over men by sucking their cocks and making them cum on your face?"
    wt_image daughter_house_1_9
    dee.c "I think men do lots of things to exert power and control over women.  Women shouldn't be afraid to do the same."
    $ dee.hypno_blowjob_count += 1
    $ dee.hypno_facial_count += 1
    orgasm
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_39
    return

label dee_sex_hypnosis:
    # intro
    if dee.hypno_sex_count == 0:
        player.c "I suppose you know that women can restore the power balance in their relationships with men by taking the man's cock into their mouth?"
        wt_image daughter_house_1_128
        dee.c "Yes, I have some familiarity with that."
        player.c "I'm not surprised.  You're an intelligent young feminist, so no doubt you're aware of many ways you can use your body to assert influence over men."
        wt_image daughter_house_1_130
        dee.c "I shouldn't do that.  If I use my beauty to get ahead, I advance myself but I oppress all women as a gender by linking my value to how attractive I am."
        player.c "Of course, you should never rely on your beauty.  You should only assert yourself using techniques available to all women, regardless of their body type or what they look like.  Having sex with a man, for example, is a time-tested way that any woman can maintain the power balance in a relationship."
        wt_image daughter_house_1_129
        dee.c "You should only have sex with someone who you're attracted to, in a consensual relationship where you both enjoy the sex."
        player.c "Men would like you to think that, yes.  But the reality is when you have sex with a man you're not attracted to, at a time when you're not in the mood for intimacy, you gain a lot of power over him, as he wants the sex, but you don't."
        wt_image daughter_house_1_130
        dee.c "So if I had sex with you, that might cause you to stop acting like the alpha in our relationship, because suddenly you'd want to keep getting access to something I don't care whether you get or don't get?"
        player.c "I knew an intelligent woman like you would find a way to rationalize why you've suddently decided to spread your legs for me."
        wt_image daughter_house_1_4
        dee.c "Oh, there's no rationalizing required.  I know exactly what I'm doing.  I'm going to let you fuck me because I'm tired of you behaving like you have all the power in our relationship.  Come over here and fuck me so that we can both see that I'm really the one in control."
    else:
        player.c "It's too bad that the best way for you to assert control in our relationship is to fuck me.  You want to fuck me, of course, to keep me in my place.  If you enjoy asserting control over me, of course, then I suppose you would enjoy fucking me, too."
        wt_image daughter_house_1_128
        dee.c "I love fucking you.  I love being able to decide when or if you get to have sex with me.  I love asserting my power over you."
        wt_image daughter_house_1_4
        dee.c "I want you to fuck me right now so that we can both see that I'm the one in control."
    # middle part
    wt_image daughter_house_1_46
    "As you remove your clothes, the hypnotized woman does the same."
    wt_image daughter_house_1_136
    "Slowly you work your way inside her, careful not to do anything to disrupt the trance she's in."
    wt_image daughter_house_1_137
    dee.c "You're lucky that I'm letting you fuck me.  You don't have as much control over me as you thought you did, do you?  If you want this to continue, you should show me some respect."
    wt_image daughter_house_1_138
    # ending
    if dee.hypno_sex_count == 0:
        "A soft kiss on her shoulder is enough to reinforce the narrative she's woven in her own mind, as she interprets it as a display of submission."
        wt_image daughter_house_1_139
        "Now convinced that 'her' plan is working, she lies back and lets you use her tight pussy to get yourself off."
        wt_image daughter_house_1_140
        "As you fuck her, [dee.name]'s body becomes more and more aroused.  Not enough to cum, today, but enough to suggest she might be able to in the future.  You, of course, are ready now."
        wt_image daughter_house_1_137
        player.c "I'm going to fill your cunt with sperm."
        dee.c "Do it.  That'll just confirm that you'll do what I want you to."
        wt_image daughter_house_1_145
        player.c "[player.orgasm_text]"
        wt_image daughter_house_1_141
        player.c "That was very clever of you, [dee.name], luring me into fucking you until I filled you with sperm, when you didn't even want to fuck me."
        wt_image daughter_house_1_76
        dee.c "I know!  And men are so easy, you fell for it."
    else:
        "As you softly kiss her shoulder again, her hips wiggle in excitement.  This small gesture is enough to reinforce the narrative she's woven in her own mind, and it turns her on as she interprets it as a display of submission."
        wt_image daughter_house_1_140
        "Her body is now fully aroused from the combination of the fucking and her own imagination about what's going on here.  You can still influence her, though, if you want."
        $ title = "What do you do?"
        menu:
            "Convince her she gets more control by not cumming":
                wt_image daughter_house_1_141
                player.c "You're not going to enjoy this too much.  If you cum while I'm fucking you, it will seem like you wanted this just as much as I did.  You'd lose all leverage over me if that happened."
                wt_image daughter_house_1_137
                dee.c "oohhhh ... Of course.  I'm not going to cum.  If I let you know how good your cock feels moving inside me, you might think I'm doing this for me, rather than to control you."
                wt_image daughter_house_1_141
                player.c "That's very smart, [dee.name].  You're such an intelligent young woman.  Hold back that orgasm you're on the verge of experiencing.  If you don't cum even when you really, really want to, you'll definitely show me who has the power in our relationship.  If you play with yourself without cumming while we're fucking, you'll really show me how in control you are."
                wt_image daughter_house_1_142
                dee.c "oohhhh ... ohh fuck!!  Do you see how in control I am?  I'm playing with my throbbing clit, but I'm not going to let myself cum while you're fucking me, even though it feels so incredibly good!  Just please, please, please finish soon!!"
                player.c "Are you sure?  You'd be displaying even more control if I take my time and you keep edging yourself like that, hovering on the brink, but not letting yourself cum."
                wt_image daughter_house_1_143
                "She's unable to reply.  It takes everything she has to fight back both tears and her orgasm.  Fortunately for her, the sensation of her body trembling in frustration triggers the onset of your own orgasm as you watch her deny her own."
                wt_image daughter_house_1_145
                player.c "[player.orgasm_text]"
                dee.c "Oh thank fuck!!"
                wt_image daughter_house_1_144
                dee.c "I ... I showed you I was in control, didn't I?"
                wt_image daughter_house_1_137
                player.c "Of course, [dee.name].  You clearly demonstrated who has the power in our relationship."
                wt_image daughter_house_1_76
                dee.c "Good!  That was exactly what I wanted to do."
            "Allow her to cum":
                wt_image daughter_house_1_141
                player.c "Are you going to cum while I'm fucking you, [dee.name]?"
                wt_image daughter_house_1_140
                dee.c "Oh fuck am I ever!!"
                wt_image daughter_house_1_142
                "As you continue to thrust in and out of she, she rubs her clit, bringing herself to a loud, trembling climax that brings you along with her."
                dee.c "Ohhh FUCCKKKK!!!!"
                wt_image daughter_house_1_145
                player.c "[player.orgasm_text]"
                wt_image daughter_house_1_144
                if not dee.has_any_tag('sex_before', 'post_hypno_sex_interest', 'no_post_hypno_sex_interest'):
                    "As your balls finish pumping their contents into her, she gasps for air, still recovering from her orgasm.  She's vulnerable right now, you can use this opportunity to break down her resistence to having sex with you when she's not hypnotized, if you want."
                    $ title = "What do you want to do?"
                    menu:
                        "Open up non-hypnotic sex content":
                            add tags 'post_hypno_sex_interest' to dee
                            wt_image daughter_house_1_140
                            player.c "What you just experienced, [dee.name], you will remember as a dream.  A pleasant dream, an arousing dream.  A wet dream that aroused you so much you came in your sleep.  Do you understand?"
                            wt_image daughter_house_1_137
                            dee.c "Yes, I will remember having a dream about fucking you.  The sex was so good, I came in my sleep."
                        "Not now":
                            wt_image daughter_house_1_146
                            "Why worry about fucking her while she has all her mental faculties, when you can already enjoy her as a manipulated hypno-sex toy."
                        "Never (shuts off question)":
                            add tags 'no_post_hypno_sex_interest' to dee
                            wt_image daughter_house_1_146
                            "Why worry about fucking her while she has all her mental faculties, when you can already enjoy her as a manipulated hypno-sex toy."
                else:
                    "As your balls finish pumping their contents into her, she gasps for air, still recovering from her orgasm, but clearly pleased with herself."
                    wt_image daughter_house_1_76
                    dee.c "I guess I showed you who's in charge in this relationship."
    $ dee.hypno_sex_count += 1
    orgasm
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_40
    return

label dee_submission_hypnosis:
    # Note: only available as an option when dom_discussion_count == 0
    player.c "You'd like to better understand how the patriarchy controls women, [dee.name].  You'd like the opportunity to explore a woman's traditional role in society to that you can better understand the challenges women have had to face."
    wt_image daughter_house_1_130
    dee.c "Yes, that would be helpful to my studies."
    player.c "I can be very helpful to your studies, [dee.name].  You would like me to take you to my dungeon and show you what it's like to be dominated by a man, so you can understand how it feels to be a submissive woman."
    wt_image daughter_house_1_129
    dee.c "No, I don't want you to dominate me.  I don't want anyone to dominate me.  That isn't something I'm interested in.  Not even for my studies."
    if dee.marilyn_event_status > 1:
        player.c "What about when Marilyn dominated you.  Didn't you enjoy that?"
        wt_image daughter_house_1_130
        dee.c "I did enjoy that.  I don't think it would feel the same if you dominated me, though.  I'm not normally submissive.  I'd much rather be the one taking control."
        player.c "You will enjoy it, [dee.name].  You will enjoy it when I dominate you, because submitting to me will be exciting and submitting to me will help you learn how to dominate others."
        wt_image daughter_house_1_128
        "She responded positively to those thoughts, but she still needs time to accept the suggestion.  You let her remember that you had this conversation, though not the circumstances.  By her next visit, she should be ready to let you take her to your dungeon."
        $ dee.dom_discussion_count = 2
    else:
        "You spend the rest of the evening trying to convince her that this is something she'd like to explore, but you're not going to succeed until she has a real work experience that reinforces your hypnotic suggestion."
        $ dee.dom_discussion_count = 1
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_41
    return

label dee_resistance_hypnosis:
    wt_image daughter_house_1_130
    if player.has_tag('hypnotist'):
        "You spend the rest of the evening lowering [dee.name]'s resistance to you, getting you closer to being able to implant a hypnotic trigger in her mind."
    else:
        "You spend the rest of the evening attempting to lower [dee.name]'s resistance, but because you're not a natural hypnotist, it's unlikely to help you influence her behavior in the future."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_42
    return

label dee_nothing_hypnosis:
    # note: if in house, only get here if trigger already implanted
    if dee.in_area('house'):
        wt_image daughter_house_1_46
        "There's nothing much to do with her right now and you've already implanted a hypnotic trigger in her mind, so you simply have her display her body for your enjoyment until you're ready to go to bed."
    else:
        "There's nothing for you to do with the hypnotized woman in this location."
    call custom_hypnosis_action_end from _call_custom_hypnosis_action_end_43
    return

label dee_implant_trigger:
    # _implant_trigger runs if hypno_count >= hypno_trigger_sessions_threshold; in order for hypno_count to be up to date, hypno_session() needs to be applied before getting here; if hypno_session() runs afterward, such as in hypnosis_end, adjust hypno_trigger_sessions_threshold accordingly
    if player.has_tag('hypnotist'):
        add tags 'trigger_implanted' to dee
        "[dee.name]'s mind is very open to you now, allowing you to implant a hypnotic trigger.  It won't do very much right now, but it's now there, you just need to pick a trigger phrase."
        $ title = "What trigger phrase do you want to use?"
        menu menu_dee_implant_trigger:
            "[dee.trigger_phrase]" if dee.trigger_phrase != "":
                pass
            "Choose something else":
                $ dee.trigger_phrase = renpy.input("What do you want her trigger phrase to be?")
                jump menu_dee_implant_trigger
        player.c "[dee.name], I have something important to tell you. When you hear the phrase \"[dee.trigger_phrase]\", you will immediately fall into a trance and obey the speaker of the phrase, and do everything that they tell you.  Do you understand?"
        if dee.in_area('house'):
            wt_image daughter_house_1_29
        dee.c "Yes.  When I hear \"[dee.trigger_phrase]\" I will fall into a trance and do everything I am told."
        player.c "You will not remember anything you do while you are in a trance.  Everything you do in the trance will seem normal, and you will not mind doing it.  You will stay in the trance until the speaker of the phrase releases you.  Do you understand?"
        dee.c "Yes.  I will forget everything I do in a trance.  I won't mind doing it because it will seem normal.  I'll stay in the trance until I'm released."
    return

label dee_hypnosis_end:
    notify
    wt_image daughter_house_1_1
    "You release [dee.name] from her trance and tell her it's time to go home."
    call dee_visit_end from _call_dee_visit_end_4
    return

# End Session
label dee_end_session:
    if dee.has_tag('first_visit'):
        player.c "It's late, kid,  I'm too tired to debate human nature with you tonight.  You want to understand what people are really like, drop by again sometime when it isn't so late and we can chat."
    else:
        player.c "It's nice seeing you, kid, but I don't have time to chat today.  Perhaps we could continue our conversation at another time."
    call dee_visit_end from _call_dee_visit_end_5
    return

label dee_invoke_hypno_trigger:
    player.c "It was nice of you to rush over here to be my sex toy for the evening."
    wt_image daughter_house_1_2
    if dee.has_tag('sex_before'):
        dee.c "Your sex toy?   I had a more balanced sexual relationship in mind."
    else:
        dee.c "Are you delusional?  I'm not here to have sex with you, let alone to be your sex toy."
    wt_image daughter_house_1_21
    player.c "'[dee.trigger_phrase]', [dee.name].  Let's not waste any more time on what you had in mind, your mind is now a complete blank.  Remove your clothes."
    wt_image daughter_house_1_3
    player.c "What do you have in mind now?"
    wt_image daughter_house_1_29
    dee.c "Nothing"
    player.c "Correct, sex toys don't have thoughts.  Stay like that while I decide what I want to do with you."
    wt_image daughter_house_1_46
    $ title = "What do you want?"
    menu menu_dee_trigger_options:
        "Tell her to offer herself to you":
            if dee.has_tag('cum_face_now'):
                wt_image daughter_house_1_66
            elif dee.has_tag('cock_face_now'):
                wt_image daughter_house_1_148
            else:
                wt_image daughter_house_1_40
            dee.c "Your sex toy is available for use."
            jump menu_dee_trigger_options
        "Rub your cock on her face":
            add tags 'cock_face_now' to dee
            if dee.has_tag('cum_face_now'):
                rem tags 'cum_face_now' from dee
                wt_image daughter_house_1_147
                "You rub your cock across her face, smearing your cum into her skin as you do so."
            else:
                wt_image daughter_house_1_146
                "The entranced woman says nothing, she just looks up at you vacantly as you rub your cock back and forth across her pretty face."
            jump menu_dee_trigger_options
        "Leave her like this for a while":
            if dee.has_tag('cum_face_now'):
                wt_image daughter_house_1_8
            else:
                wt_image daughter_house_1_46
            "You go about your business while the triggered woman waits mindlessly for you."
            rem tags 'cock_face_now' from dee
            jump menu_dee_trigger_options
        "Use her mouth":
            wt_image daughter_house_1_149
            player.c "Open your mouth, sex toy."
            wt_image daughter_house_1_5
            player.c "Now suck."
            wt_image daughter_house_1_101
            "She does so, steadily, consistently and without thinking about what she'sdoing.  Just an obedient automaton with no other purpose than to suck on your cock for your enjoyment."
            wt_image daughter_house_1_133
            "As the pre-cum drizzles out of you cock, she opens her eyes, awaiting further instructions."
            wt_image daughter_house_1_5
            $ title = "Where do you want to cum?"
            menu:
                "On her":
                    wt_image daughter_house_1_149
                    player.c "[player.orgasm_text]"
                    wt_image daughter_house_1_8
                    "There's no obvious reaction from the entranced woman as you spray her with your seed."
                    $ dee.hypno_facial_count += 1
                    add tags 'cum_face_now' to dee
                "In her":
                    wt_image daughter_house_1_101
                    player.c "[player.orgasm_text]"
                    wt_image daughter_house_1_132
                    player.c "Swallow"
                    wt_image daughter_house_1_95
                    "She obediently shows off a now empty mouth."
                    wt_image daughter_house_1_46
                    $ dee.hypno_swallow_count += 1
                    rem tags 'cum_face_now' from dee
            $ dee.hypno_blowjob_count += 1
            orgasm notify
            add tags 'sex_today' to dee
            rem tags 'cock_face_now' from dee
            jump menu_dee_trigger_options
        "Use her pussy":
            wt_image daughter_house_1_15
            "With a vacant stare, she holds herself open for you."
            $ title = "How do you want to do this?"
            menu:
                "Tell her to be wet":
                    wt_image daughter_house_1_33
                    player.c "Good sex toys are wet on command.  Rub your clit and be a wet toy for me."
                    wt_image daughter_house_1_39
                    "Honestly, it's more enjoyable for you this way.  You can fuck her as long and as hard as you'd like, enjoying her tight, moist snatch gripping your cock firmly."
                    wt_image daughter_house_1_12
                    "You take your time, enjoying the experience, until the pressure in your balls builds to the point where you need relief, and you empty your seed into the entranced woman."
                    wt_image daughter_house_1_38
                    player.c "[player.orgasm_text]"
                    wt_image daughter_house_1_15
                    "When your balls finish pumping their load, you extract yourself.  She watches as you pull out, waiting for further instructions."
                "Tell her to stay dry":
                    add tags 'dry_fucked_today' to dee
                    wt_image daughter_house_1_11
                    "Fucking her like this is uncomfortable for you, but even more uncomfortable for her."
                    wt_image daughter_house_1_37
                    "You can feel her body bruising, even tearing, from the painful friction.  In her entranced state, she can't take steps to protect herself, but she'll be sore, possibly even bleeding, by the time you're finished."
                    wt_image daughter_house_1_36
                    "The dry fuck doesn't feel great around your cock, either, but watching her suffer while you fuck her more than makes up for it, and you can feel your balls boil over as you coat her damaged insides with your seed."
                    wt_image daughter_house_1_38
                    player.c "[player.orgasm_text]"
                    wt_image daughter_house_1_15
                    "When your balls finish pumping their load, you extract yourself.  She winces as you pull out, her pussy now thoroughly battered and sore."
            $ dee.hypno_sex_count += 1
            orgasm notify
            rem tags 'cock_face_now' 'cum_face_now' from dee
            add tags 'sex_today' to dee
            jump menu_dee_trigger_options
        "Nothing else":
            wt_image daughter_house_1_10
            "You instruct her to clean herself up and dress before releasing her from her trance."
            wt_image daughter_house_1_21
            if dee. has_tag('dry_fucked_today'):
                dee.c "Oh, wow!  Is that the time?"
                wt_image daughter_house_1_23
                "Suddenly aware of the pain between her legs, she reaches a hand down, then catches herself."
                wt_image daughter_house_1_2
                dee.c "I'm not feeling well, I'd better head home."
                call dee_visit_end from _call_dee_visit_end_6
            elif dee.has_tag('sex_today'):
                dee.c "Oh, wow!  Is that the time?  I should probably get going."
                call dee_visit_end from _call_dee_visit_end_7
            else:
                dee.c "Oh, wow!  Is that the time?  I should probably get going soon."
    return


# Weekend Actions

## Character Specific Actions

# Sex Actions
label dee_sex:
    if dee.has_tag('sex_before'):
        $ dee.temporary_count = 1
        if dee.has_any_tag('sex_talk_today', 'talked_domination_today', 'talked_mom_follow_up_today'):
            player.c "I think that's enough chatting for today.  How about we go into the bedroom and fuck?"
        else:
            player.c "I'm glad you came over, kid.  I don't have a lot of time to chat, but I do have just enough time to fuck you.  Shall we retire to the bedroom?"
        if dee.has_tag('insulting_you'):
            wt_image daughter_house_1_25
            dee.c "No, old man.  I don't have time to waste on you making yourself comfortable.  I'm in a generous mood so I'll let you have another pity fuck, but if you want to fuck my hot young body, you'll need to show me you can get your pathetic cock up right here and now or I'm leaving."
            $ title = "What do you do?"
            menu:
                "Get your pathetic cock up":
                    $ dee.temporary_count = 0 # shuts off regular sex menu below because choice already made
                    wt_image daughter_house_1_40
                    dee.c "God, what a pathetic limp dick you are.  Are you even going to be able to get that hard enough to get it into my tight pussy, old man?"
                    call dee_sex_insulting_you_repeat from _call_dee_sex_insulting_you_repeat
                    $ dee.orgasm_count += 1
                    $ dee.sex_count += 1
                    orgasm notify
                "Worship her pussy":
                    $ dee.temporary_count = 0  # shuts off regular sex menu below because choice already made
                    wt_image daughter_house_1_24
                    player.c "Could I please you in a different way, instead?"
                    dee.c "You pathetic limp dick.  Can't give me a proper fucking so you want to try and make it up to me some other way, huh?  Get on your knees."
                    wt_image daughter_house_1_30
                    dee.c "Is this what you want?  Access to my sweet young pussy?"
                    $ title = "How do you respond?"
                    menu:
                        "Beg for access":
                            player.c "Yes, please."
                            wt_image daughter_house_1_31
                            dee.c "You can beg better than that, can't you?"
                            player.c "Please may I be allowed to worship your sweet young pussy."
                            wt_image daughter_house_1_30
                            dee.c "Will you do a good job?  I'm not sure a pathetic limp dick like you deserves access to my pussy."
                            player.c "Please, I'll make you feel good.  Please may be allowed to lick your pussy and make you feel good?"
                        "Nod silently":
                            pass
                    wt_image daughter_house_1_16
                    dee.c "Okay, but tongue only, no fingers.  You'll get me off with your mouth alone and you'll stay on your knees while you're doing it."
                    wt_image daughter_house_1_41
                    "She leans back and presents her cunt to you.  Still on your knees, you shuffle forward ..."
                    wt_image daughter_house_1_45
                    "... and start to lick.  She's already wet and you lap up her delicious nectar."
                    wt_image daughter_house_1_44
                    dee.c "Is that the best you can do?  The girls in college are way better at eating me out.  Try harder, limp dick, or I'm taking my pussy away."
                    wt_image daughter_house_1_45
                    "You pick up the pace, licking at her frantically like an unskilled college kid might eat her.  Insulting you has already turned her on and she doesn't need subtlty to arouse her, just contact on her clit.  Once she gets it, she cums quickly and hard."
                    wt_image daughter_house_1_68
                    dee.c "Ohhh FUCCKKKK!!!!"
                    wt_image daughter_house_1_41
                    dee.c "Shit, that felt nice.  Not as good as the girls at school, but not bad for an old man who can't get it up."
                    wt_image daughter_house_1_40
                    dee.c "I'd like you to stay on your knees while I dress, limp dick.  Will you do that?"
                    $ title = "Will you?"
                    menu:
                        "Yes, stay on your knees":
                            wt_image daughter_house_1_69
                            "From your knees, you watch as the beautiful young woman dresses."
                            wt_image daughter_house_1_27
                            if dee.ready_for_mom > 2:
                                dee.c "I really like seeing you down there.  It's a good place for older men, on their knees in front of me.  Mom likes being in that position, too.  I wonder if you taught her that, or maybe she taught it to you?"
                            else:
                                dee.c "I really like seeing you down there.  It's a good place for older men, on their knees in front of me."
                            if not dee.has_tag('no_ass_sniffing'):
                                wt_image daughter_house_1_70
                                dee.c "I feel like I should reward you.  Would you like to sniff my ass before I go?"
                                $ title = "What do you say?"
                                menu:
                                    "Yes, please":
                                        wt_image daughter_house_1_72
                                        dee.c "Get your nose right in there.  No touching, though, other than your nose against my butt crack."
                                        wt_image daughter_house_1_73
                                        "You press your nose up against her tightly closed anus, inhaling the basest scent of her body."
                                        wt_image daughter_house_1_74
                                        dee.c "Okay, that's enough.  You got a good whiff."
                                        wt_image daughter_house_1_26
                                        dee.c "Thanks for the fun time.  See you again soon, I hope!"
                                    "Only if that's something you'd enjoy":
                                        wt_image daughter_house_1_71
                                        dee.c "You don't really want to, but you'll do it to please me?  That makes it even hotter.  Hell yeah, I want you to!"
                                        wt_image daughter_house_1_72
                                        dee.c "Get your nose right in there.  No touching, though, other than your nose against my butt crack."
                                        wt_image daughter_house_1_73
                                        "You press your nose up against her tightly closed anus, inhaling the basest scent of her body."
                                        wt_image daughter_house_1_74
                                        dee.c "That was so hot!  Thanks for doing that, you're a really good play partner."
                                        wt_image daughter_house_1_26
                                        dee.c "See you again soon, I hope!"
                                    "Not today":
                                        wt_image daughter_house_1_26
                                        dee.c "Maybe next time, then.  See you again soon, I hope!"
                                    "Never (shuts off question)":
                                        add tags 'no_ass_sniffing' to dee
                                        wt_image daughter_house_1_26
                                        dee.c "Too bad, that would have been really hot.  See you again soon, I hope!"
                        "No, get back up":
                            wt_image daughter_house_1_26
                            player.c "Fun time's over, [dee.name]."
                            dee.c "Oh well, I enjoyed it while it lasted.  See you again soon, I hope!"
                    $ dee.orgasm_count += 1
                    $ dee.pleasure_her_count += 1
                    change player energy by -energy_short notify
                "Ask her to stop insulting you":
                    rem tags 'insulting_you' from dee
                    wt_image daughter_house_1_22
                    dee.c "Oh, are you tired of that game?  What did you want to do instead"
                "Suggest something else for today":
                    wt_image daughter_house_1_26
                    dee.c "Okay, I could be up for something different.  What did you have in mind?"
        elif dee.has_tag('talking_dirty'):
            wt_image daughter_house_1_25
            dee.c "Mmmm, I can't wait for the bedroom.  I want that big, sexy cock of yours in me right here, right now!"
            $ title = "What do you do?"
            menu:
                "Fuck her with your big, sexy cock":
                    $ dee.temporary_count = 0 # shuts off regular sex menu below because choice already made
                    wt_image daughter_house_1_33
                    dee.c "Oh yeah!  Stick that sexy man-meat inside me!"
                    call dee_sex_dirty_talk_repeat from _call_dee_sex_dirty_talk_repeat
                    $ dee.orgasm_count += 1
                    $ dee.sex_count += 1
                    orgasm notify
                "Ask her to stop talking dirty":
                    rem tags 'talking_dirty' from dee
                    wt_image daughter_house_1_26
                    dee.c "No problem!  What did you want to do instead"
                "Suggest something else for today":
                    wt_image daughter_house_1_26
                    dee.c "Sure.  What did you have in mind?"
        elif dee.has_tag('insulting_herself'):
            wt_image daughter_house_1_25
            dee.c "A stupid blonde cum dump like me doesn't need to be taken to a nice bed.  You can just have your way with my scrawny body right here."
            $ title = "What do you do?"
            menu:
                "Fuck the cum dump":
                    $ dee.temporary_count = 0 # shuts off regular sex menu below because choice already made
                    wt_image daughter_house_1_23
                    player.c "Get your clothes off, skank, and tell me what you are."
                    call dee_sex_insulting_herself_repeat from _call_dee_sex_insulting_herself_repeat
                    $ dee.orgasm_count += 1
                    $ dee.sex_count += 1
                    orgasm notify
                "Tell her to stop insulting herself":
                    rem tags 'insulting_herself' from dee
                    wt_image daughter_house_1_26
                    dee.c "Thanks!  I was starting to get tired of that game, too.  What did you want to do instead"
                "Suggest something else for today":
                    wt_image daughter_house_1_26
                    dee.c "That sounds good to me.  What did you have in mind?"
        else:
            wt_image daughter_house_1_25
            dee.c "Why?  Didn't you enjoy fucking me here in the living room before?  How do you want to do this?"
        # if another sex option not chosen earlier, go to default sex menu
        if dee.temporary_count > 0:
            $ title = "What do you want?"
            menu:
                "Eat her out" if not dee.has_tag('insulting_you'):
                    wt_image daughter_house_1_10
                    player.c "Why don't you spread your legs and get those panties off and I'll make you feel good."
                    wt_image daughter_house_1_16
                    if dee.pleasure_her_count > 0:
                        dee.c "Please say that means you're going to eat me out again?"
                        wt_image daughter_house_1_40
                        player.c "You like it when I lick your cunt?"
                        wt_image daughter_house_1_41
                        dee.c "I love it!  Stop talking, I don't want to listen to your mouth, I want to feel it between my legs."
                        wt_image daughter_house_1_45
                        "She's already wet as your tongue touches her, and gets wetter still as you lick gently along her labia."
                        wt_image daughter_house_1_44
                        dee.c "Stop being a fucking tease and get your mouth on my clit!"
                        wt_image daughter_house_1_45
                        "With a hand on the back of your head, she forces your face back onto her pussy.  You wrap your lips around her clit and start sucking.  For most women, that would be too intense, too fast, but not for [dee.name]."
                        wt_image daughter_house_1_68
                        dee.c "Ohhh FUCCKKKK!!!!"
                        wt_image daughter_house_1_41
                        dee.c "Holy shit!  That was intense."
                        player.c "Better than the kids at college?"
                        wt_image daughter_house_1_28
                        dee.c "Better than the boys, that's for sure.  Probably better than most of the girls, too!"
                    else:
                        if dee.has_tag('talking_dirty'):
                            dee.c "If you're not planning on fucking me silly with your hard, sexy cock, how exactly are you going to make me feel good?"
                        else:
                            dee.c "You still have your pants on.  How exactly are you planning on making me feel good?"
                        wt_image daughter_house_1_40
                        player.c "With my mouth and tongue.  Any objections?"
                        wt_image daughter_house_1_41
                        dee.c "Absolutely not!"
                        wt_image daughter_house_1_45
                        "She's already wet as your tongue touches her, and gets wetter still as you lick gently along her labia."
                        wt_image daughter_house_1_41
                        dee.c "What the fuck are you doing?  Aren't you going to lick my clit?"
                        player.c "I'm getting to that."
                        wt_image daughter_house_1_44
                        dee.c "Get to it fucking now!"
                        wt_image daughter_house_1_45
                        "With a hand on the back of your head, she forces your face back onto her pussy.  You wrap your lips around her clit and start sucking.  For most women, that would be too intense, too fast, but not for [dee.name]."
                        wt_image daughter_house_1_68
                        dee.c "Ohhh FUCCKKKK!!!!"
                        wt_image daughter_house_1_41
                        player.c "That's not your first time getting head."
                        wt_image daughter_house_1_28
                        dee.c "I'm a pretty, bi-sexual college girl on a campus full of horny students, what do you think?"
                        player.c "I think maybe next time we should take things slower.  You might enjoy things more if you let me gradually work you up."
                        wt_image daughter_house_1_27
                        dee.c "I don't know.  I like it fast and intense.  Some of the shy girls fumble around down there not sure what to do.  I've come to appreciate the direct approach."
                    wt_image daughter_house_1_26
                    dee.c "Thanks for showing me a great time!  You sure know how to convince a girl to come back."
                    $ dee.orgasm_count += 1
                    $ dee.pleasure_her_count += 1
                    change player energy by -energy_short notify
                "Tell her to masturbate":
                    wt_image daughter_house_1_24
                    dee.c "What?  How is that fun?  I could have stayed home in my room if I wanted to masturbate."
                    player.c "Do you normally have men watching you masturbate when you're in your room?  Do you have a camgirl business you want to tell me about?"
                    wt_image daughter_house_1_25
                    dee.c "No, but masturbating while you watch still sounds like masturbation, just creepier."
                    player.c "How about I tell you what to do, then?  Would that be more participatory?  Stand up and remove your panties and skirt."
                    wt_image daughter_house_1_110
                    dee.c "This seems like more work for less fun than just fucking."
                    wt_image daughter_house_1_111
                    player.c "We haven't reached the fun part, yet.  Bend over and start touching yourself."
                    wt_image daughter_house_1_112
                    "With her bare ass turned towards you, [dee.name] reaches a hand back between her legs and begins running the tips of her finger nails along her sex."
                    player.c "How's that?  A little more fun now?"
                    wt_image daughter_house_1_113
                    dee.c "A little more fun, yeah."
                    player.c "Let's make it a lot more fun.  Turn over and rub your clit."
                    wt_image daughter_house_1_114
                    "For a lot of women, that would be escalating things too quickly.  Not [dee.name], though.  Once she starts to get aroused, she peaks fast."
                    dee.c "Oh, this is good!  Oh!!  Oh fuck I'm going to cum!!"
                    $ title = "What do you do?"
                    menu menu_dee_masturbation_menu:
                        "Watch her cum" if not dee.has_any_tag('slowed_now', 'fingering_now'):
                            if not dee.has_tag('topless_now'):
                                wt_image daughter_house_1_115
                            elif dee.has_tag('facedown_now'):
                                wt_image daughter_house_1_127
                            else:
                                wt_image daughter_house_1_118
                            dee.c "Ohhh FUCCKKKK!!!!"
                            wt_image daughter_house_1_110
                            player.c "Nice show.  You should seriously consider a camgirl business."
                            wt_image daughter_house_1_25
                            dee.c "No way.  Once stuff's on the internet, it's there forever."
                            wt_image daughter_house_1_21
                            dee.c "Oh my god!  You don't have a camera set up in here, do you?  If you do, I swear I will seriously fuck you up!"
                            wt_image daughter_house_1_1
                            player.c "Relax, tiger cub.  Nobody got to see your show except me and all the members of my Discord page."
                            change player energy by -energy_very_short notify
                        "Tell her to take her top off first" if not dee.has_tag('topless_now'):
                            add tags 'topless_now' to dee
                            wt_image daughter_house_1_13
                            dee.c "Can't resist the opportunity to ogle my massive tits, huh?"
                            wt_image daughter_house_1_116
                            "Still smiling at the joke she made at her own expense, she resumes rubbing herself."
                            wt_image daughter_house_1_117
                            "It's not long before she's on the verge of climax again."
                            jump menu_dee_masturbation_menu
                        "Tell her to slow down" if dee.has_tag('topless_now') and not dee.has_any_tag('slowed_now', 'facedown_now'):
                            add tags 'slowed_now' to dee
                            rem tags 'fingering_now' from dee
                            wt_image daughter_house_1_13
                            dee.c "Why??  I was just about ready to cum!  What else do you want me to do??"
                            jump menu_dee_masturbation_menu
                        "Tell her to rub herself again" if dee.has_any_tag('slowed_now', 'fingering_now') and not dee.has_tag('facedown_now'):
                            rem tags 'slowed_now' 'fingering_now' from dee
                            wt_image daughter_house_1_116
                            "You don't have to tell her twice.  With a satisfied smile, she resumes rubbing herself."
                            wt_image daughter_house_1_117
                            "It's not long before she's on the verge of climax again."
                            jump menu_dee_masturbation_menu
                        "Tell her to finger herself" if dee.has_tag('slowed_now') and not dee.has_any_tag('fingering_now', 'facedown_now'):
                            add tags 'fingering_now' to dee
                            wt_image daughter_house_1_119
                            dee.c "Okay, but it would feel better if I just rubbed myself."
                            wt_image daughter_house_1_120
                            "Her finger makes sexy squelching sounds as she pumps it in and out of her wet hole, but she seems to be right.  She doesn't look like she's going to be able to cum like this."
                            jump menu_dee_masturbation_menu
                        "Tell her to flip over" if dee.has_tag('fingering_now'):
                            wt_image daughter_house_1_121
                            "Impressively, she manages to keep her finger inside herself as she does so."
                            dee.c "I'm still not going to be able to cum from just fingering myself."
                            wt_image daughter_house_1_122
                            player.c "Engage your brain, [dee.name].  Think of something sexy that's happened when you're on your knees, something that makes you want to cum?  Can you find that moment or fantasy?"
                            if dee.marilyn_event_status > 1 or dee.has_tag('fuck_machine_used_from_behind'):
                                rem tags 'fingering_now' 'slowed_now' from dee
                                add tags 'facedown_now' to dee
                                wt_image daughter_house_1_123
                                "She bites her lip and softly nods ..."
                                wt_image daughter_house_1_124
                                "... then resumes frigging herself, faster now, a somewhat glazed look on her face."
                                player.c "What is it?  What are you picturing?"
                                wt_image daughter_house_1_125
                                if dee.marilyn_event_status > 1 and not dee.has_tag('strapon_story_told'):
                                    dee.c "It's Marilyn.  Something she did to me after she took me back to her hotel.  You didn't want to hear about it, but it was really fucking hot."
                                    $ title = "Ask about it now?"
                                    menu:
                                        "Yes":
                                            add tags 'strapon_story_told' to dee
                                            wt_image daughter_marilyn_15
                                            dee.c "{i}After I are her out in the limo, her chauffer pulled up in front of a fancy hotel.  Marilyn told me to dress, then I nervously followed her up to her room.{/i}"
                                            wt_image daughter_marilyn_23
                                            dee.c "{i}When we got upstairs, she kissed me and told me that since I'd been a good girl, she'd reward me now.{/i}"
                                            player.c "{i}By letting you cum, I presume?{/i}"
                                            wt_image daughter_marilyn_8
                                            dee.c "{i}That's what I assumed, too, but no. She told me we could continue our interview and she'd give me more information for my studies about women in authority.  First, though, she made me get down on my knees and eat her out some more.{/i}"
                                            player.c "{i}Made you?{/i}"
                                            wt_image daughter_marilyn_23
                                            dee.c "{i}Asked me, I guess.{/i}"
                                            player.c "{i}Did she really ask you?{/i}"
                                            wt_image daughter_marilyn_24
                                            dee.c "{i}No.  She told me to get on the floor and eat her out and I did.  She didn't ask and she didn't make me.  She just expected me to and I went along with it.{/i}"
                                            wt_image daughter_marilyn_9
                                            dee.c "{i}And so I knelt there, lapping at her pussy, as she talked to me about real-life challenges faced by women trying to succeed in a male-dominated industry.{/i}"
                                            wt_image daughter_marilyn_25
                                            dee.c "{i}I even got to ask her questions.  I was careful not to pry too much, as I could sense there were things about her past it was best not to ask about, but as long as I kept my tongue busy in her sex, she was happy to answer questions about her experiences without sharing too many details.{/i}"
                                            wt_image daughter_marilyn_10
                                            dee.c "{i}I lost track of how many times she came in my mouth while we talked, but eventually she said we needed to wrap things up.  She asked if there was one more thing I wanted to know before I left.{/i}"
                                            player.c "{i}What did you ask her?{/i}"
                                            wt_image daughter_marilyn_26
                                            dee.c "{i}I asked if I would be permitted to have another orgasm before I left.{/i}"
                                            player.c "{i}Did she agree?{/i}"
                                            wt_image daughter_marilyn_14
                                            dee.c "{i}Sort of.  She told me it was cute how I came in her limo without even having my clit touched.  She said she would fuck me for five minutes, and that I could have as many orgasms as I wanted in that time, as long as I kept my hands away from my clit.{/i}"
                                            wt_image daughter_marilyn_11
                                            dee.c "{i}Then she put on a strap-on and bent me over and started fucking me, but not before setting the alarm on the hotel clock to ring in exactly five minutes.  She had really meant it when she said that was all of her time I could have.{/i}"
                                            wt_image daughter_marilyn_12
                                            player.c "{i}And how many times were you able to cum in the time she gave you?{/i}"
                                            wt_image daughter_marilyn_13
                                            dee.c "{i}Just once, I think.  But it started almost as soon as she penetrated me and it didn't stop until the alarm rang.  And the whole time I was kneeling there, convulsing, the only thing I could think of - to the extent I could think at all - was how lucky I was that she taking time from her busy day to do this for me.{/i}"
                                        "No":
                                            pass
                                elif dee.has_tag('fuck_machine_used_from_behind'):
                                    dee.c "The fuck machine.  I'm imagining it ramming into me, so hard, so fast."
                                else:
                                    dee.c "It's Marilyn.  She's set her alarm and she's fucking me from behind with her strap-on and she's going to make me cum before the alarm goes!"
                                wt_image daughter_house_1_126
                                "Lost in the memory, [dee.name] soon has herself ready to cum."
                            else:
                                wt_image daughter_house_1_121
                                dee.c "Nope.  All my favorite sexy moments have happened when someone's kneeling between my knees, not behind me."
                                wt_image daughter_house_1_120
                                "She turns back over, her finger still moving in and out of her pussy, but not getting her any closer to cumming."
                            jump menu_dee_masturbation_menu
                        "Tell her to turn back to face you" if dee.has_tag('facedown_now'):
                            add tags 'slowed_now' 'fingering_now' to dee
                            rem tags 'facedown_now' from dee
                            wt_image daughter_house_1_121
                            dee.c "Damn it!  I was so close.  Would you quit re-positioning me?"
                            wt_image daughter_house_1_120
                            "She turns back over, her finger still moving in and out of her pussy, but you've disrupted her fantasy now, and she's not getting her any closer to cumming."
                            jump menu_dee_masturbation_menu
                        "Tell her to stop (ends scene)" if dee.has_tag('topless_now') and not dee.has_any_tag('slowed_now', 'fingering_now'):
                            if dee.has_tag('facedown_now'):
                                wt_image daughter_house_1_121
                            else:
                                wt_image daughter_house_1_13
                            dee.c "Stop?  Why??"
                            player.c "That's as much of your show as I want to watch."
                            wt_image daughter_house_1_40
                            dee.c "But I was so close!  I was right on the ..."
                            wt_image daughter_house_1_29
                            player.c "Edge?  Yes, I could tell.  It was fun to watch.  If you don't have the willpower to keep from touching yourself, you can finish yourself off before you go.  I won't stop you.  Are you such a horny girl, you can't leave without finishing what you started?"
                            wt_image daughter_house_1_46
                            dee.c "If I keep going, I humiliate myself in front of you because I can't control my urges.  If I stop, I've let you edge me, which is giving you control of my body in a different way.  You win either way."
                            player.c "Is that so bad?"
                            if dee.has_tag('insulted_herself_before'):
                                wt_image daughter_house_1_23
                                dee.c "I guess not.  You just showed me that sometimes you can turn me into a stupid blonde cunt.  I don't like that you can have that effect on me, but I can't deny that it turns me on in a perverse way."
                            elif dee.dom_discussion_count > 3:
                                wt_image daughter_house_1_23
                                dee.c "I guess not.  You've demonstrated that you're good at taking control, so I shouldn't be suprised by you doing so.  And I can't deny that this side of you turns me on a little bit."
                            else:
                                wt_image daughter_house_1_22
                                dee.c "I like winning power games in relationships, not losing them, but I can't deny that it's a bit of a turn on knowing that you're a challenge."
                    rem tags 'topless_now' 'fingering_now' 'facedown_now' 'slowed_now' from dee
                "Hand job":
                    if not dee.has_tag('hj_intro_complete'):
                        add tags 'hj_intro_complete' to dee
                        wt_image daughter_house_1_24
                        player.c "I presume you've learned how to please boys using just your hands?"
                        wt_image daughter_house_1_75
                        dee.c "If this is where you plan to ask 'how old was I when I gave my first handjob?', forget it.  I'm not going to answer."
                        player.c "How about I ask you to show off your skills, then, so I can give you some pointers if you need them?"
                        wt_image daughter_house_1_76
                        dee.c "Wow!  Even my first boyfriend had a better line than that to get my hands on his cock."
                        player.c "Really?  What was it?"
                        wt_image daughter_house_1_77
                        dee.c "Something along the lines of 'You're so pretty, could you jerk me off before my Mom gets home?'"
                        player.c "No way that was a better line than mine!"
                        wt_image daughter_house_1_78
                        dee.c "Well, his included a compliment.  Plus he was feeling up my tits at the time, which was making me horny.  And I was curious about what a boy's penis feels like when it's hard."
                    elif dee.has_tag('hj_trained'):
                        wt_image daughter_house_1_75
                        player.c "How about you show me that you've learned how to give a good hand job."
                        wt_image daughter_house_1_76
                        dee.c "I already knew how to give a good hand job."
                        player.c "Who told you that, the former boyfriend who was feeling up your tits while his Mom was out of the house?"
                        wt_image daughter_house_1_77
                        dee.c "The first guy who told me I was beautiful?  Yes, him and a few others."
                    else:
                        wt_image daughter_house_1_75
                        player.c "Remind me what that trick was to get you to give a hand job?  Something about feeling up your tits?"
                        wt_image daughter_house_1_76
                        dee.c "Jerk!  If you're talking about my first boyfriend, he told me I was beautiful."
                        player.c "While he was feeling up your tits, right?"
                        wt_image daughter_house_1_77
                        dee.c "So?  It was still a nice moment."
                    wt_image daughter_house_1_79
                    $ title = "How do you reply?"
                    menu:
                        "Compliment her":
                            player.c "I think you're beautiful, too, and what you're doing with your hands feels amazing."
                            wt_image daughter_house_1_80
                            if dee.has_tag('hj_trained'):
                                dee.c "So I guess I don't really need any more lessons in how to give a hand job, do I?  You're liking what I'm doing."
                                wt_image daughter_house_1_85
                                dee.c "You like my hand playing with your balls ..."
                                wt_image daughter_house_1_79
                                dee.c "... you like my fingers stroking along your shaft ..."
                                wt_image daughter_house_1_80
                                dee.c "... you like everything I'm doing for you, don't you?"
                                player.c "I'm loving what you're doing.  I'm really close, [dee.name].  If you keep going, I'm going to cum on you."
                            else:
                                dee.c "So I guess I don't really need lessons in how to give a hand job, do I?  You're liking what I'm doing."
                                player.c "I'm loving what you're doing.  I'm really close, [dee.name].  If you keep going, I'm going to cum on you."
                            wt_image daughter_house_1_81
                            dee.c "Do it!  I want that!  Show me how much you loved my hand job!"
                            wt_image daughter_house_1_82
                            "You do exactly that.  She tilts her head back, her hand moving more quickly on your shaft as the first drops of pre-cum land on her face."
                            wt_image daughter_house_1_83
                            player.c "[player.orgasm_text]"
                            wt_image daughter_house_1_66
                            dee.c "Pretty good hand job, huh?"
                            wt_image daughter_house_1_65
                            player.c "Absolutely amazing, [dee.name]."
                            "She preens with pride at the compliment.  Despite her self-confidence, she seems to relish having an older, more experienced man compliment her on her sexual skills."
                        "Insult her":
                            player.c "I'm surprised he could even find those tiny bee-stings of yours."
                            wt_image daughter_house_1_78
                            dee.c "Rude!  Do you want me to continue this hand job or are you going to keep insulting me?"
                            wt_image daughter_house_1_79
                            player.c "I want you to continue the hand job while I insult you, you stupid, tiny-titted blonde slut."
                            dee.c "And why the fuck should I do that?  Your cock is hard and throbbing in my hand, I should walk away and leave you blue-balled."
                            wt_image daughter_house_1_80
                            player.c "No, you're going to keep stroking my cock, because your feminist brain is turned on by the thought of a man who's showing you no respect painting your face with his hot cum, you dumb cunt."
                            dee.c "You think so, huh?  I think I should stop right now."
                            wt_image daughter_house_1_81
                            player.c "And I think you should tilt your face back while you pump my cock, cum dump."
                            wt_image daughter_house_1_82
                            "She does as directed, her hand moving more quickly on your shaft as the first drops of pre-cum land on her face."
                            wt_image daughter_house_1_83
                            player.c "[player.orgasm_text]"
                            wt_image daughter_house_1_66
                            if dee.has_tag('insulted_herself_before'):
                                player.c "Which did you prefer, me insulting you or you insulting yourself?"
                                wt_image daughter_house_1_67
                                dee.c "Honestly, I hated the tone you were taking with me, but it was kinda hot continuing to pleasure you while you insulted me.  But not quite as hot as humiliating myself while you fuck me."
                            elif dee.has_tag('open_to_being_insulted'):
                                player.c "I see you still enjoy being insulted.  We should try something more intense sometime."
                                wt_image daughter_house_1_67
                                dee.c "Honestly, I hated the tone you were taking with me, but it was kinda hot continuing to pleasure you while you insulted me.  So, yeah, if you want to try something like that again, I'd be up for it."
                            else:
                                player.c "You enjoyed being insulted.  We should try something more intense sometime."
                                wt_image daughter_house_1_67
                                dee.c "Honestly, I hated the tone you were taking with me, but it was kinda hot continuing to pleasure you while you insulted me.  So, yeah, if you want to try something like that again, I'd be up for it."
                                add tags 'open_to_being_insulted' to dee
                        "Be submissive towards her":
                            $ dee.temporary_count = 0
                            player.c "I'm sorry, [dee.name].  My cock probably isn't as nice as his, but please play with it anyway.  I'm grateful that you're touching me."
                            if dee.has_tag('insulted_you_before'):
                                wt_image daughter_house_1_78
                                dee.c "You need to be more than grateful, you worthless worm.  If you want me to keep touching your pathetic cock, you need to beg."
                                player.c "Please, [dee.name], please!  Please keep touching my pathetic cock with your beautiful, sexy hands.  I know I don't deserve your touch, but please take pity on me make me feel good."
                                wt_image daughter_house_1_79
                                dee.c "I'll make you hard, but I'm probably going to blue-ball you.  How do you feel about that?"
                                $ title = "What do you do?"
                                menu:
                                    "Thank her for blue-balling you":
                                        wt_image daughter_house_1_80
                                        dee.c "You like that idea, huh?  You like having a pretty, young college girl play with your cock but not let you cum?"
                                        player.c "I love it!  Thank you, [dee.name]!"
                                        wt_image daughter_house_1_79
                                        dee.c "You're getting close to cumming aren't you?"
                                        player.c "Really, really close!"
                                        wt_image daughter_house_1_80
                                        dee.c "But you're going to hold it back aren't you?  You're going to deny yourself the pleasure that's building in your balls."
                                        player.c "I'm going to try!"
                                        if dee.has_tag('hj_trained'):
                                            wt_image daughter_house_1_84
                                            dee.c "If I tug on your balls, will it help?"
                                            player.c "Uggh!!  It hurts, but it also feels good."
                                            wt_image daughter_house_1_85
                                            dee.c "What if I tug on them lightly, is that better?  You're not going to cum from having your balls pulled, are you?"
                                            player.c "I'm trying not to!"
                                        wt_image daughter_house_1_79
                                        dee.c "Don't try, do.  Keep yourself from cumming."
                                        player.c "Yes, [dee.name].  I am, but it's really, really difficult!"
                                        wt_image daughter_house_1_78
                                        dee.c "How much would you like me to keep stroking you until you cum all over my face!"
                                        player.c "So much!!"
                                        wt_image daughter_house_1_79
                                        dee.c "But you want me to blue-ball you, don't you?"
                                        player.c "Uggh!!  Yes!  I want both!!  If you keep doing that, I'll need to cum."
                                        wt_image daughter_house_1_80
                                        dee.c "Five more strokes, count them down and control yourself while you take them."
                                        player.c "Aagghhh ... five!  four!  three!!  two!!  one!!!"
                                        wt_image daughter_house_1_78
                                        dee.c "There!  I'll stop there.  What would like to say to me?"
                                        $ title = "What do you say?"
                                        menu:
                                            "That was amazing!":
                                                wt_image daughter_house_1_28
                                                dee.c "That was really hot, wasn't it?"
                                            "That was cruel":
                                                wt_image daughter_house_1_27
                                                dee.c "It was, wasn't it?  And I really enjoyed watching you put up with it."
                                            "I'd like permission to eat your cunt":
                                                wt_image daughter_house_1_44
                                                dee.c "Fuck yes!  Get your mouth down here, blue-balls."
                                                wt_image daughter_house_1_45
                                                "She's drenched even before you touch her.  Blue-balling you has clearly turned her on.  Her hand pressing at the back your head leaves you no options in how to eat her.  You're just a mouth for her to grind her clit against, and she does so hard, smearing your face with her juices as she cums."
                                                wt_image daughter_house_1_68
                                                dee.c "Ohhh FUCCKKKK!!!!"
                                                wt_image daughter_house_1_41
                                                dee.c "Fuck, that was so hot!  I didn't let you cum, but then you got me off anyway.  I could enjoy that type of relationship."
                                                $ dee.pleasure_her_count += 1
                                                $ dee.orgasm_count += 1
                                        wt_image daughter_house_1_26
                                        dee.c "No touching yourself after I leave.  I want you to enjoy those blue-balls until morning."
                                        change player energy by -energy_short notify
                                    "Tell her you want whatever she wants to do with you":
                                        wt_image daughter_house_1_80
                                        dee.c "Whatever I want, huh?  So I'm in charge, aren't I?"
                                        player.c "Yes, [dee.name]!"
                                        wt_image daughter_house_1_79
                                        dee.c "So if I want to stroke your cock faster and faster without you cummig, you'll hold your orgasm back, won't you?"
                                        player.c "Yes, [dee.name], but it's really, really difficult!"
                                        wt_image daughter_house_1_78
                                        dee.c "I can see that.  Even when I stop stroking you to give you a break, your cock is still twitching.  Would you like me to let you cum, now?"
                                        player.c "Yes, [dee.name]!  Please!"
                                        wt_image daughter_house_1_79
                                        dee.c "But if I don't want you to cum, if I want to just keep teasing you until I stop and leave you horny, you'll hold your orgasm back for me, won't you?"
                                        player.c "Uggh!  Yes, [dee.name], if that's what you want, I'll do my best to please you.  But if you keep doing that, I'll need to cum.  I won't be able to hold back."
                                        if dee.has_tag('hj_trained'):
                                            wt_image daughter_house_1_84
                                            dee.c "If I tug on your balls, will it help?"
                                            player.c "Uggh!!  It hurts, but it also feels good."
                                            wt_image daughter_house_1_85
                                            dee.c "What if I tug on them lightly, is that better?  You're not going to cum from having your balls pulled, are you?"
                                            player.c "If you keep stroking my cock while you tug on them I will!  I don't think I can hold back any longer!!"
                                        wt_image daughter_house_1_80
                                        dee.c "I think you can.  Five more strokes, count them down and control yourself while you take them."
                                        player.c "Aagghhh ... five!  four!  three!!  two!!  one!!!"
                                        wt_image daughter_house_1_78
                                        dee.c "There!  I'll stop there."
                                        player.c "Thank you, [dee.name]!  I hope I pleased you."
                                        wt_image daughter_house_1_40
                                        dee.c "You did.  Would you like an opportunity to please me some more?"
                                        $ title = "What do you do?"
                                        menu:
                                            "Get on your knees between her legs":
                                                wt_image daughter_house_1_44
                                                dee.c "I'm still not going to let you cum, even after you get me off.  Understood?"
                                                player.c "Yes, [dee.name]."
                                                wt_image daughter_house_1_45
                                                dee.c "Good.  Start licking."
                                                "She's drenched even before you touch her.  Blue-balling you has clearly turned her on.  Her hand pressing at the back your head doesn't even give you the opportunity to properly lick her.  You're just a mouth for her to grind her clit against, and she does so hard, smearing your face with her juices as she cums."
                                                wt_image daughter_house_1_68
                                                dee.c "Ohhh FUCCKKKK!!!!"
                                                wt_image daughter_house_1_41
                                                dee.c "Fuck, that was so hot!  I didn't let you cum, but then you got me off anyway.  I could enjoy that type of relationship."
                                                $ dee.pleasure_her_count += 1
                                                $ dee.orgasm_count += 1
                                            "Tell her that took too much out of you":
                                                wt_image daughter_house_1_27
                                                dee.c "I guess I was a little cruel to you.  It was fun watching you control yourself for me, though.  Okay, we can stop things there."
                                        wt_image daughter_house_1_26
                                        dee.c "No touching yourself after I leave.  I want you to experience the sensation of being blue-balled until morning."
                                        change player energy by -energy_short notify
                                    "Demean yourself and hope she'll let you cum":
                                        player.c "Please, [dee.name].  Please don't do that.  I know I'm worthless and pathetic and don't deserve it, but I'd really like it if you let me cum."
                                        wt_image daughter_house_1_80
                                        dee.c "I'm not sure.  What did you say you were?"
                                        player.c "Worthless and pathetic and not worthy of your touch!"
                                        wt_image daughter_house_1_78
                                        dee.c "You're right, you are a worthless, pathetic old man and you don't deserve to have a pretty girl playing with your cock do you?"
                                        player.c "I don't, [dee.name].  I really don't"
                                        wt_image daughter_house_1_79
                                        dee.c "Tell me how special I am and maybe I'll take pity on you."
                                        player.c "You're amazing, [dee.name]!  You're beautiful and sexy and I'm so lucky to have you touching me!"
                                        wt_image daughter_house_1_80
                                        dee.c "Now remind me how pathetic you are."
                                        player.c "I'm worthless, [dee.name]!  I'm a pathetic, useless old man who doesn't deserve to have your beautiful hands on his cock."
                                        if dee.has_tag('hj_trained'):
                                            wt_image daughter_house_1_84
                                            dee.c "Thank me for pulling on your balls and making them hurt."
                                            player.c "Thank you, [dee.name]!  Thank you for hurting my useless balls!"
                                            wt_image daughter_house_1_85
                                            dee.c "Okay, you can cum on the floor now, but you need to cum while you're having your balls pulled."
                                        else:
                                            wt_image daughter_house_1_78
                                            dee.c "Okay, you can cum on the floor now."
                                        wt_image daughter_house_1_86
                                        player.c "[player.orgasm_text]"
                                        wt_image daughter_house_1_28
                                        dee.c "That's quite the mess you made on the floor."
                                        $ title = "What do you do?"
                                        menu:
                                            "Get it cleaned up later":
                                                wt_image daughter_house_1_26
                                                dee.c "I like it when you demean yourself.  I'm not sure why, but it's hot.  Maybe we can do more of that the next time I come by?"
                                            "Kneel down and lick it clean now":
                                                wt_image daughter_house_1_27
                                                "While she dresses, [dee.name] watches with interest as you lick your own cum off of your floor.  She's clearly aroused by the scene."
                                                wt_image daughter_house_1_87
                                                dee.c "If I made a mess on your floor, would you lick that up, too?  I'm not talking about cum, though, just so we're clear."
                                                $ title = "Would you lick up the type of mess she's talking about?"
                                                menu:
                                                    "Yes":
                                                        wt_image daughter_house_1_4
                                                        "Squatting down, she releases a stream of golden fluid onto your floor ... *pzzzzzztttt*"
                                                        wt_image daughter_house_1_114
                                                        "As you lick up her mess, she spreads her legs and plays with herself."
                                                        wt_image daughter_house_1_115
                                                        dee.c "Ohhh FUCCKKKK!!!!"
                                                        wt_image daughter_house_1_75
                                                        dee.c "Watching you demean yourself is such a turn on, but I guess I made that obvious.  I can't wait to come see you again!"
                                                        $ dee.orgasm_count += 1
                                                    "No":
                                                        wt_image daughter_house_1_26
                                                        dee.c "It's good to know you have some limits!  I like it when you demean yourself, though.  I'm not sure why, but it's hot.  Maybe we can do more of that the next time I come by?"
                                        $ dee.handjob_count += 1
                                        orgasm notify
                            else:
                                wt_image daughter_house_1_78
                                dee.c "You're grateful, are you?  What exactly are you grateful for?"
                                if dee.has_tag('hj_trained'):
                                    wt_image daughter_house_1_85
                                    dee.c "Are you grateful for me playing with your balls?"
                                    player.c "Yes, [dee.name].  Thank you!"
                                wt_image daughter_house_1_80
                                dee.c "Are you grateful to have a pretty college girl like me stroking your cock?"
                                player.c "Yes, [dee.name].  Thank you!"
                                wt_image daughter_house_1_79
                                dee.c "Are you grateful that my hands are making your cock hard and throbbing?"
                                player.c "Yes, [dee.name].  Very grateful!"
                                wt_image daughter_house_1_78
                                dee.c "I'd bet you'd like to cum now.  Ask nicely and maybe I'll let you."
                                $ title = "How do you want to ask?"
                                menu:
                                    "Demean yourself":
                                        wt_image daughter_house_1_79
                                        player.c "Please let this pathetic, worthless old man cum, [dee.name]!  Please take pity on me and let me cum!!"
                                        wt_image daughter_house_1_78
                                        dee.c "Holy fuck!  That was hot!  Do it again."
                                        wt_image daughter_house_1_79
                                        player.c "Please let this pathetic, worthless old man cum, [dee.name]!  Please take pity on me and let me cum!!"
                                        wt_image daughter_house_1_80
                                        dee.c "Fuck, that turns me on hearing you insult yourself like that!  Do you really think I should let you cum on me?"
                                    "Beg pitifully":
                                        wt_image daughter_house_1_79
                                        player.c "Please, [dee.name], please let me cum?  Please??  I'm begging you, please let me cum!  Please?!"
                                        wt_image daughter_house_1_80
                                        dee.c "Mmmmm, that was nice, but I'm not sure.  Do you really think I should let you cum on me?"
                                    "Ask nicely":
                                        wt_image daughter_house_1_79
                                        player.c "Please let me cum, [dee.name].  What you're doing feels so nice, I'd really like to cum."
                                        wt_image daughter_house_1_80
                                        dee.c "You'd like to cum, would you?  I don't know, do you really think I should let you cum on me?"
                                $ title = "Should she let you cum on her?"
                                menu:
                                    "Yes":
                                        wt_image daughter_house_1_79
                                        dee.c "I suppose you are being very obedient.  And it's hot having you talk like that."
                                        wt_image daughter_house_1_81
                                        dee.c "Okay, you can cum on me."
                                        wt_image daughter_house_1_82
                                        "She tilts her head back, her hand moving more quickly on your shaft as the first drops of pre-cum land on her face."
                                        wt_image daughter_house_1_83
                                        player.c "[player.orgasm_text]"
                                        wt_image daughter_house_1_66
                                        dee.c "It's fun having you act that way.  We should do that more often."
                                    "No":
                                        wt_image daughter_house_1_78
                                        dee.c "You're right, it would make an awful mess and I don't think you deserve the right to cum on me.  Cum on the floor."
                                        wt_image daughter_house_1_86
                                        player.c "[player.orgasm_text]"
                                        wt_image daughter_house_1_75
                                        dee.c "It's fun having you act that way.  We should do that more often."
                                        $ dee.temporary_count = 0
                                        $ dee.handjob_count += 1
                                        orgasm notify
                                sys "If you get [dee.name] used to insulting you, she'll make future submissive hand job sessions more intense."
                        "Focus on instructing her":
                            if dee.has_tag('hj_trained'):
                                player.c "Let's continue your lessons."
                                wt_image daughter_house_1_78
                                dee.c "Continue them?  What are you talking about?  Giving a hand job isn't that complicated."
                                wt_image daughter_house_1_79
                                dee.c "You already told me to start with soft, gentle strokes ..."
                                wt_image daughter_house_1_85
                                dee.c "... and to play gently with your balls while I'm rubbing your shaft."
                                wt_image daughter_house_1_80
                                dee.c "And I know to watch for the signs of pre-cum, which by the way you're already dripping lots of."
                                wt_image daughter_house_1_79
                                dee.c "Which means you're ready for me to take a firmer grip and pump you faster now."
                                wt_image daughter_house_1_80
                                dee.c "I can tell you're trying to hold back and make this last, but I've got you now.  You're going to cum for me."
                                player.c "I can hold out quite long, you don't have me that excited, yet."
                                wt_image daughter_house_1_78
                                dee.c "Then I guess I'll need to use the last technique you taught me ..."
                                wt_image daughter_house_1_81
                                dee.c "... and offer my face as a target.  Are you going to hold out now?"
                                wt_image daughter_house_1_82
                                "For as long as you can, yes, but her hand pumping you faster and faster above her pretty, upturned face eventually overcomes your resistance."
                                wt_image daughter_house_1_83
                                player.c "[player.orgasm_text]"
                                wt_image daughter_house_1_9
                                player.c "You look rather pleased with yourself."
                                dee.c "I know when a teacher has to give me an 'A'."
                            else:
                                add tags 'hj_trained' to dee
                                player.c "I'm sure what you're doing felt good to your teenage first boyfriend, and probably to the boys at your college, but you really should learn how to please a grown man.  For starters, you're trying to pleasure my cock, not pull it off me."
                                wt_image daughter_house_1_78
                                dee.c "What do you mean?  Doesn't a firm grip feel good?"
                                player.c "At the end, right before the guy cums, yes.  Before then, a softer touch is better.  Tease him, make his cock feel good."
                                wt_image daughter_house_1_80
                                dee.c "I thought a firm grip would feel good.  I know that's what I like.  But I'll try being more gentle.  How is that?"
                                player.c "Not bad, but you're ignoring an important part of my anatomy."
                                wt_image daughter_house_1_78
                                dee.c "What do you mean?  You wanted a hand job, I'm giving you a hand job."
                                player.c "You're only playing with my shaft.  I have balls, too, hanging right there.  You should pleasure them, too."
                                wt_image daughter_house_1_84
                                dee.c "Like this?"
                                player.c "Ow!!  What happened to gentle?  Play with them, don't try to pull them off me."
                                wt_image daughter_house_1_85
                                dee.c "Sorry.  Geez, you're sensitive.  What if I tickle them like this?"
                                player.c "Much better.  Keep stroking my shaft while you're caressing them."
                                wt_image daughter_house_1_80
                                dee.c "Are you sure you don't just like giving orders?  No guy has ever complained about a hand job I've given him."
                                player.c "No shit.  They all want to get another one, or a blow job, or into your pants.  They're not going to risk hurting your feelings.  Do you want to just keep tugging on men's cocks like a deranged ape, or do you want to learn how to give a mind-blowing hand job?"
                                wt_image daughter_house_1_78
                                dee.c "I want to learn how to give mind-blowing hand jobs."
                                player.c "Then stop fighting me and do what I say."
                                wt_image daughter_house_1_85
                                "[dee.name] shuts up after that and concentrates on your instructions, pleasuring your balls ..."
                                wt_image daughter_house_1_79
                                "... and your shaft with intense concentration.  You make her work at it as long as you can, but her soft hands and dutiful behavior combine to eventually wear down your resistance."
                                wt_image daughter_house_1_80
                                player.c "Has anything changed?"
                                dee.c "Your cock is dripping!"
                                wt_image daughter_house_1_78
                                player.c "That's pre-cum.  What should you be doing now?"
                                dee.c "Taking a firmer grip?"
                                wt_image daughter_house_1_79
                                player.c "Yes, now you can take a firmer grip, and you can start pumping faster, too.  Where should your face be?"
                                wt_image daughter_house_1_80
                                dee.c "Directly in front of your cock?"
                                wt_image daughter_house_1_81
                                player.c "Good girl.  Tilt your head back and keep pumping."
                                wt_image daughter_house_1_82
                                "She does as directed, her hand moving more quickly on your shaft as the first spurts of cum land on her face."
                                wt_image daughter_house_1_83
                                player.c "[player.orgasm_text]"
                                wt_image daughter_house_1_66
                                dee.c "So, how'd I do?"
                                player.c "Not bad.  You have potential."
                                wt_image daughter_house_1_65
                                dee.c "The load of cum dripping down my face says I have more than potential, mister.  You enjoyed that, even if you won't admit it."
                    # if hand job completed
                    if dee.temporary_count > 0:
                        $ dee.handjob_count += 1
                        $ dee.facial_count += 1
                        orgasm notify
                "Blow job":
                    wt_image daughter_house_1_75
                    if dee.has_tag('insulting_herself'):
                        player.c "Why don't you show me what an obedient, giving cum dump you can be by getting your tits out and getting down on your knees to suck my cock?"
                    else:
                        player.c "Why don't you show me what a generous, giving soul you can be by getting your tits out and getting down on your knees to suck my cock?"
                    wt_image daughter_house_1_76
                    dee.c "I think we both know I'm not really anything of the sort."
                    wt_image daughter_house_1_77
                    dee.c "But I do enjoy playing with men's cocks sometimes."
                    wt_image daughter_house_1_78
                    dee.c "And I especially like the idea of seeing you make puppy-dog eyes at me once I have your cock hard and throbbing."
                    $ title = "How do you respond?"
                    menu:
                        "Just enjoy the blow job":
                            player.c "I'm looking forward to that, too."
                            wt_image daughter_house_1_90
                            dee.c "I bet you are.  You're going to love feeling my wet lips around your cock."
                            wt_image daughter_house_1_92
                            "She's not wrong.  Her mouth does feel great."
                            if dee.has_tag('bj_trained'):
                                wt_image daughter_house_1_91
                                "She remembers that you like the feel of her tongue licking at the underside of your cock head ..."
                                wt_image daughter_house_1_93
                                "... and she remembers that you like to feel her tongue continually swirling along your cock as she blows you."
                                wt_image daughter_house_1_100
                                "She also remembers to stroke your cock with her lips, using her hand just to hold your cock steady."
                                if dee.has_tag('can_use_teeth_during_bjs'):
                                    wt_image daughter_house_1_92
                                    "You told her that love bites were okay ..."
                                    wt_image daughter_house_1_98
                                    "... so you're not surprised to feel her teeth bite down on the head of your cock, as she seems to enjoy inflicting a little pain when she gives head ..."
                                    wt_image daughter_house_1_96
                                    player.c "Ow!"
                                    wt_image daughter_house_1_7
                                    "... but she soon switches back to gentle mode, using her soft lips to soothe the pain emitting from the bite marks."
                                else:
                                    wt_image daughter_house_1_7
                                    "You told her not to use her teeth and she respects your wishes, sucking gently on the head of your cock without biting."
                                wt_image daughter_house_1_6
                                "As your excitement builds, she locks eyes on you and she watches your face as she bobs her head faster and faster along your shaft."
                            else:
                                wt_image daughter_house_1_94
                                "It's a college girl blow job - lots of enthusiasm, lots of hand pumping, not much technique, but pleasurable regardless ..."
                                wt_image daughter_house_1_98
                                "... at least until she scrapes her teeth along the head of your cock."
                                wt_image daughter_house_1_96
                                player.c "Ow!"
                                wt_image daughter_house_1_91
                                dee.c "I like to give love bites.  I bet you love this, too."
                                wt_image daughter_house_1_92
                                "Taking the head of your cock back between her teeth, she bites down."
                                wt_image daughter_house_1_98
                                player.c "Oww!!"
                                wt_image daughter_house_1_7
                                "As quickly as it starts, the painful moment is over, and her teeth are replaced by her soft lips, gently sucking on and soothing your sore cock head."
                                wt_image daughter_house_1_94
                                "Then she goes back to pumping your shaft with her hand while she tries to suction the cum out of your balls with her mouth.  It's not subtle, but it works."
                            wt_image daughter_house_1_91
                            dee.c "Mmmmm, puppy-dog eyes.  I'm going to make you cum now."
                            wt_image daughter_house_1_97
                            $ title = "Where do you want to cum?"
                            menu:
                                "In her":
                                    wt_image daughter_house_1_94
                                    player.c "[player.orgasm_text]"
                                    wt_image daughter_house_1_92
                                    if dee.has_tag('successful_swallow'):
                                        "She starts to choke and pull back as your sperm shoots into the back of her throat ..."
                                        wt_image daughter_house_1_101
                                        "... but stays in place once she feels your hand on the back of her head, again."
                                        wt_image daughter_house_1_95
                                        "When you finish cumming, she shows you her empty mouth."
                                        player.c "Is that getting easier?"
                                        wt_image daughter_house_1_78
                                        dee.c "A little maybe?  I'm not sure why you won't just cum on my face, though, like a normal guy."
                                    elif dee.has_tag('failed_swallow'):
                                        "She starts to choke and pull back as your sperm shoots into the back of her throat ..."
                                        wt_image daughter_house_1_90
                                        "What little cum makes it into her mouth, she spits out."
                                        player.c "Still haven't talked to your Mom about how to swallow, huh?"
                                        wt_image daughter_house_1_26
                                        if dee.ready_for_mom > 2:
                                            dee.c "Nope, and if you think I'm going to bring her over again so we can both blow you at the same time, forget it.  That was a one time deal."
                                        else:
                                            dee.c "Ewww!  Would you quit suggesting that?  I'm sure you think you can convince me to bring my mother over so we can both blow you, but it's not going to happen."
                                    else:
                                        add tags 'failed_swallow' to dee
                                        "She starts to choke and pull back as your sperm shoots into the back of her throat."
                                        wt_image daughter_house_1_90
                                        if donna.has_tag('cum_slut'):
                                            "Unlike her mother, it seems [dee.name] hasn't acquired a taste for cum."
                                        else:
                                            "It seems [dee.name] doesn't enjoy, or at least doesn't have much experience with, the taste of cum."
                                        player.c "You okay?"
                                        wt_image daughter_house_1_27
                                        dee.c "Yeah, I'm fine.  It's not easy catching your cum without choking when your cock is spurting like that."
                                        player.c "I take it you don't have a lot of experience with giving blowjobs."
                                        wt_image daughter_house_1_26
                                        dee.c "I have a little, but most of the guys I've been with seemed to prefer facials.  I haven't had to try and catch a full load like that in my mouth very often.  It's trickier than it sounds."
                                        player.c "Maybe you should ask your Mom for tips on how she does it?"
                                        wt_image daughter_house_1_21
                                        dee.c "Ewww!!  That conversation's not happening!"
                                        player.c "Then I guess I'll just have to teach you how to swallow."
                                        wt_image daughter_house_1_22
                                        dee.c "Great!  Next time I'll bring a guy with me and you can show me how you swallow his load.  Shhh!  Don't try to explain yourself, I know what I heard."
                                    $ dee.swallow_count += 1
                                "On her":
                                    wt_image daughter_house_1_82
                                    "[dee.name] tilts her head back as she jerks your load onto her waiting face."
                                    wt_image daughter_house_1_83
                                    player.c "[player.orgasm_text]"
                                    if dee.has_tag('facial_before'):
                                        wt_image daughter_house_1_65
                                        player.c "You know, those boys in college are onto something.  You do look good like that."
                                    else:
                                        add tags 'facial_before' to dee
                                        wt_image daughter_house_1_65
                                        if dee.professor_event_status > 1:
                                            dee.c "So I guess it's not just college boys and Dr. Jameson who like to see me like this."
                                        else:
                                            dee.c "So I guess it's not just college boys who like to see me like this."
                                        player.c "Have many of the boys from your school been able to admire you in this condition?"
                                        wt_image daughter_house_1_66
                                        dee.c "I'm not a slut, if that's what you're trying to imply.  And even if I were, there's nothing wrong with a woman having a healthy libido and multiple consensual partners at the same time, as long as she hasn't made a monogamous commitment to any of them."
                                        wt_image daughter_house_1_67
                                        player.c "Well, the next time your non-monogamous libido is in the mood for another facial, drop by and see me."
                                    $ dee.facial_count += 1
                        "Be submissive to her":
                            player.c "Thank you, [dee.name].  I like it when you take control."
                            wt_image daughter_house_1_91
                            dee.c "I bet you do.  Typical man, all tough and blustery until a pretty woman offers to take him into her mouth, then you turn into my bitch, don't you?"
                            wt_image daughter_house_1_92
                            player.c "Yes, [dee.name].  I'm lucky to be your bitch."
                            wt_image daughter_house_1_7
                            "Taking the head of your cock between her teeth, she bites down on it."
                            wt_image daughter_house_1_96
                            player.c "Ow!!"
                            wt_image daughter_house_1_91
                            if dee.has_tag('insulted_you_before'):
                                dee.c "Thank me for biting your cock, you pathetic worm, and ask me to bite if again."
                                player.c "Thank you, [dee.name].  Please bite and hurt my worthless cock."
                                wt_image daughter_house_1_92
                                player.c "Owww!!"
                                wt_image daughter_house_1_91
                                dee.c "You're still hard, you pathetic old man.  Are you so grateful to have a sexy young woman pay attention to you that you can stay hard even when she's hurting you?"
                                player.c "Yes, [dee.name].  I'm so grateful to have your mouth on my cock, I'm happy with whatever you want to do with it."
                                wt_image daughter_house_1_96
                                "The sensation of her teeth clamping down on you is as much psychological terror as pain, but the pain is still real."
                                wt_image daughter_house_1_98
                                player.c "OOWWW!!"
                                wt_image daughter_house_1_100
                                "Fortunately, she immediately soothes the pain with the far more pleasurable sensation of her soft lips sliding back and forth along your shaft."
                                wt_image daughter_house_1_91
                                dee.c "Those are the puppy eyes I wanted to see.  Tell me how little you deserve this blow job."
                                wt_image daughter_house_1_93
                                player.c "I don't deserve this at all, [dee.name].  I'm so lucky to have a beautiful young woman take pity on me and suck my worthless cock."
                                wt_image daughter_house_1_95
                                dee.c "You're right, you don't serve this.  You don't deserve to give me a facial, either, and I don't like the taste of your cum, so you're going to spill your seed on the floor.  Thank me for that."
                                wt_image daughter_house_1_97
                                player.c "Thank you, [dee.name], for letting me cum on the floor!"
                                wt_image daughter_house_1_99
                                "As your balls start to boil over, she removes your cock from her mouth and directs onto the floor beside her."
                                wt_image daughter_house_1_86
                                player.c "[player.orgasm_text]"
                                wt_image daughter_house_1_40
                                dee.c "You made a mess.  Get in it while you thank me for the blowjob by licking my cunt."
                                $ title = "What do you do?"
                                menu:
                                    "Kneel in the mess you made":
                                        wt_image daughter_house_1_41
                                        dee.c "Don't just kneel in it.  Lie right down so it gets all over your belly."
                                        wt_image daughter_house_1_44
                                        dee.c "Much better.  Now lick."
                                        wt_image daughter_house_1_45
                                        "She's already wet and gets wetter quickly as you lick her clit.  Her hand is soon at the back of your head, pressing mouth onto her clit."
                                        wt_image daughter_house_1_68
                                        dee.c "Ohhh FUCCKKKK!!!!"
                                        wt_image daughter_house_1_41
                                        dee.c "That was hot!  Kneel up so I can look at your cum smeared over your belly before I go."
                                        wt_image daughter_house_1_75
                                        dee.c "You're fun to play with.  I'm looking forward to doing this again."
                                        $ dee.pleasure_her_count += 1
                                        $ dee.orgasm_count += 1
                                        change player energy by -energy_very_short
                                    "Refuse":
                                        wt_image daughter_house_1_75
                                        dee.c "And here I thought you were an adventurous playmate.  Have it your way, I still enjoyed hearing you call yourself down.  That was fun."
                            else:
                                dee.c "What's wrong, don't you like a little pain with your blowjob."
                                wt_image daughter_house_1_93
                                player.c "I guess?"
                                wt_image daughter_house_1_91
                                dee.c "Don't just guess.  You're my bitch, remember?  Ask me to bite you."
                                wt_image daughter_house_1_92
                                player.c "Please bite my cock, [dee.name]."
                                wt_image daughter_house_1_98
                                player.c "Oww!!"
                                wt_image daughter_house_1_91
                                dee.c "You're still hard.  You liked that more than you're willing to admit, bitch."
                                wt_image daughter_house_1_100
                                "You certainly like what happens next, as she starts sliding her soft lips back and forth along your shaft ..."
                                wt_image daughter_house_1_93
                                "... pumping and sucking on your cock ..."
                                wt_image daughter_house_1_97
                                "... until you feel your balls start to boil over."
                                wt_image daughter_house_1_99
                                "As you start to cum, she removes your cock from her mouth and directs it onto the floor."
                                wt_image daughter_house_1_86
                                player.c "[player.orgasm_text]"
                                wt_image daughter_house_1_28
                                dee.c "I don't like the taste of your cum and I didn't think you deserved a facial, but it was fun watching my bitch make a mess on his floor.  Hope you don't mind the mess.  I'll be going now."
                                sys "If you get [dee.name] used to insulting you, she'll make future submissive blow job sessions more intense."
                        "Insult her":
                            player.c "Keep telling yourself that, slut.  The reality is you love being on your knees, serving a man."
                            dee.c "Ha!  Keep up that attitude and your cock won't be going into my mouth after all."
                            wt_image daughter_house_1_90
                            player.c "Yes, it will, because there's nothing that would turn your feminist brain on more than sucking off a man who treats her like a stupid cum dump.  Now get your mouth around my cock, you dumb cunt."
                            wt_image daughter_house_1_94
                            "Despite your cock in her mouth, you catch the sound of an involuntary moan arising from the back of [dee.name]'s throat."
                            wt_image daughter_house_1_93
                            dee.c "nnnnn"
                            wt_image daughter_house_1_6
                            player.c "Look at the educated feminist college girl, now.  Down on her knees, serving a man the way nature intended her to be.  It feels good to be treated as a mouth-to-fuck, doesn't it, slut?"
                            wt_image daughter_house_1_91
                            dee.c "You know, outside of porn, most feminists don't actually get off on being humiliated by a man."
                            wt_image daughter_house_1_94
                            player.c "Get your mouth back on my cock, you dumb cunt.  I'm not treating 'most feminists' like dirt, I'm treating you like dirt because you're the only girl in your college stupid enough and pathetic enough to come over here tonight hoping that I'd put you on your knees where you belong."
                            wt_image daughter_house_1_100
                            player.c "Look at you working so hard to please me.  A silly little tiny-titted whore spending her break sucking cock, just the way they teach you in gender equality classes, don't they?"
                            wt_image daughter_house_1_94
                            "Another moan escapes from the back of [dee.name]'s throat."
                            wt_image daughter_house_1_93
                            dee.c "nnnnn"
                            wt_image daughter_house_1_97
                            player.c "What's that, slut?  You're looking forward to earning my cum?  Okay, I suppose I could empty my load, now."
                            wt_image daughter_house_1_6
                            $ title = "Where do you want to cum?"
                            menu:
                                "In her":
                                    wt_image daughter_house_1_94
                                    player.c "[player.orgasm_text]"
                                    wt_image daughter_house_1_92
                                    "She starts to choke and pull back as your sperm shoots into the back of her throat ..."
                                    wt_image daughter_house_1_101
                                    "... but with a firm hand on the back of her head, you hold her in place."
                                    player.c "I don't care whether you like the taste of my cum, slut.  Swallow it all."
                                    wt_image daughter_house_1_90
                                    "Once your balls are empty you let go of her head."
                                    player.c "Show me you swallowed it all."
                                    wt_image daughter_house_1_95
                                    player.c "Good girl.  You're wet between the legs now, aren't you?"
                                    wt_image daughter_house_1_40
                                    if dee.has_tag('insulted_herself_before'):
                                        dee.c "Yes.  I hated the things you were saying to me, but it was hot continuing to blow you while you insulted me.  Not quite as hot as humiliating myself, though, while you fuck me."
                                    else:
                                        dee.c "Yes.  I hated the things you were saying to me, but it was hot continuing to blow you while you insulted me.  If you want to try something like that again, I'd be okay with it."
                                    $ dee.swallow_count += 1
                                "On her":
                                    wt_image daughter_house_1_90
                                    player.c "Offer me a target, cum dump."
                                    wt_image daughter_house_1_82
                                    "You didn't specify what target.  She could have offered you her tits, but she tilts her head back and offers her face, instead."
                                    wt_image daughter_house_1_83
                                    player.c "[player.orgasm_text]"
                                    wt_image daughter_house_1_66
                                    player.c "Good girl.  You're wet between the legs now, aren't you?"
                                    wt_image daughter_house_1_67
                                    if dee.has_tag('insulted_herself_before'):
                                        dee.c "Yes.  I hated the things you were saying to me, but it was hot continuing to blow you while you insulted me.  Not quite as hot as humiliating myself, though, while you fuck me."
                                    elif dee.has_tag('open_to_being_insulted'):
                                        dee.c "Yes.  I hated the things you were saying to me, but it was hot continuing to blow you while you insulted me."
                                    else:
                                        dee.c "Yes.  I hated the things you were saying to me, but it was hot continuing to blow you while you insulted me.  If you want to try something like that again, I'd be okay with it."
                                        add tags 'open_to_being_insulted' to dee
                                    $ dee.facial_count += 1
                        "Train her":
                            if not dee.has_tag('bj_trained'):
                                add tags 'bj_trained' to dee
                                player.c "If you expect me to make puppy-dog eyes, you'd better know what you're doing."
                                dee.c "I do.  Guys are easy."
                                wt_image daughter_house_1_100
                                "[dee.name] takes your cock in her mouth and starts to blow you."
                                wt_image daughter_house_1_94
                                "It's a college girl effort, not bad, but not really good, either."
                                wt_image daughter_house_1_98
                                "Then she unexpectedly scrapes her teeth along the head of your cock."
                                wt_image daughter_house_1_96
                                player.c "Ow!  Careful!"
                                wt_image daughter_house_1_78
                                dee.c "Most guys like it when I do that."
                                player.c "More likely some guys like that and the rest put up with it because you like doing it.  Unless you mostly hook up with submissive guys, which wouldn't surprise me."
                                wt_image daughter_house_1_90
                                dee.c "Well, at least you like the rest of my blow job."
                                wt_image daughter_house_1_6
                                player.c "It's okay, but not great."
                                wt_image daughter_house_1_78
                                dee.c "What do you mean?  What's wrong with it??"
                                player.c "You've got no technique.  You're just sucking on my cock and waiting for me to blow, when you aren't scratching me with your teeth like a she-devil.  Try a little subtlety, lick the underside of my cock head for starters."
                                wt_image daughter_house_1_91
                                dee.c "Like this?"
                                wt_image daughter_house_1_92
                                player.c "Yeah.  Now close your lips around my cock but keep teasing the underside with your tongue."
                                wt_image daughter_house_1_93
                                player.c "That's a bit better.  Keep moving your tongue while you take me deeper."
                                wt_image daughter_house_1_94
                                player.c "Less hands, [dee.name].  When I want a hand job, I'll ask for one.  Pumping's okay when I'm ready to cum, but until then I want you to get me excited with your lips and tongue, not your fingers."
                                wt_image daughter_house_1_100
                                player.c "That's more like it.  Can you take me deeper?"
                                wt_image daughter_house_1_95
                                dee.c "I'm not sure.  I'll try."
                                wt_image daughter_house_1_7
                                "Slowly, she takes you back into her mouth ..."
                                wt_image daughter_house_1_97
                                "... trying to work her way down your shaft as far as she can ..."
                                wt_image daughter_house_1_100
                                "... which isn't very far before she starts gagging and has to pull off, choking."
                                wt_image daughter_house_1_99
                                dee.c "Fuck, you're big.  Was that okay?"
                                wt_image daughter_house_1_78
                                player.c "Honestly, not really.  You're going to need to learn to control your gag reflex if you want to be able to give good deep throat.  For today, let's just focus on making my cock feel good with your lips and tongue."
                                wt_image daughter_house_1_91
                                dee.c "Okay, lips and tongue.  No hands, no teeth."
                                wt_image daughter_house_1_92
                                "This time when she takes you into her mouth, it's much better."
                                wt_image daughter_house_1_93
                                "Her tongue dances along your shaft as she bobs her head back and forth."
                                wt_image daughter_house_1_100
                                player.c "Much better, [dee.name].  Now look at me as you suck me off."
                                wt_image daughter_house_1_6
                                "Her eyes locked on yours, she tries to please you following the instrucitons you've given, and succeeds."
                                wt_image daughter_house_1_91
                                dee.c "I like this part.  You've got puppy-dog eyes now."
                                wt_image daughter_house_1_97
                                "Eyes still locked on yours, she starts sliding her mouth faster and faster along your shaft, urging the cum out of your balls."
                            else:
                                player.c "If you expect me to make puppy-dog eyes, you'd better demonstrate that you've learned how to suck cock properly."
                                wt_image daughter_house_1_91
                                dee.c "I remember.  You like to feel my tongue on the underside of your cock head ..."
                                wt_image daughter_house_1_92
                                dee.c "... and you want me to keep tonguing you as I use my lips on you, like this."
                                wt_image daughter_house_1_93
                                "Her tongue is indeed active, swirling around your cock as she blows you."
                                wt_image daughter_house_1_91
                                dee.c "And you want me to stroke your cock with just my lips, not my hands, not until you're ready to cum, anyway."
                                wt_image daughter_house_1_100
                                "Her lips slide up and down your shaft, while her hand holds you place, not pumping, at least not yet."
                                wt_image daughter_house_1_95
                                if dee.has_tag('can_use_teeth_during_bjs'):
                                    dee.c "And you like it when I hurt you a little bit with my teeth while I'm blowing you."
                                else:
                                    dee.c "And you don't want me to use my teeth, even though I think it's hot when I hurt you a little bit while I'm sucking you."
                                $ title = "What do you say?"
                                menu:
                                    "That's correct":
                                        pass
                                    "A little teeth is okay"  if not dee.has_tag('can_use_teeth_during_bjs'):
                                        add tags 'can_use_teeth_during_bjs' to dee
                                        wt_image daughter_house_1_78
                                        dee.c "Mmmm, that's what I like to hear."
                                    "No more teeth" if dee.has_tag('can_use_teeth_during_bjs'):
                                        rem tags 'can_use_teeth_during_bjs' from dee
                                        wt_image daughter_house_1_78
                                        dee.c "Too intense?"
                                        player.c "A little.  Mostly too scary and distracting."
                                        wt_image daughter_house_1_90
                                        dee.c "Maybe this will feel better."
                                if dee.has_tag('can_use_teeth_during_bjs'):
                                    wt_image daughter_house_1_92
                                    "[dee.name] takes the head of your cock between her teeth ..."
                                    wt_image daughter_house_1_98
                                    "... and scrapes them against your sensitive skin before biting down and finishing with a painful nip."
                                    wt_image daughter_house_1_96
                                    player.c "Ow!"
                                    wt_image daughter_house_1_91
                                    dee.c "Should I bite you again, or would you rather I make it feel better."
                                    $ title = "What do you want?"
                                    menu menu_dee_bj_bite_another_menu:
                                        "Another bite":
                                            wt_image daughter_house_1_96
                                            "She takes your cock back between her teeth and bites down harder this time."
                                            wt_image daughter_house_1_98
                                            player.c "Oww!!!"
                                            jump menu_dee_bj_bite_another_menu
                                        "Something to make your sore cock feel better":
                                            wt_image daughter_house_1_92
                                            "[dee.name] takes the now tender head of your cock gently between her lips ..."
                                            wt_image daughter_house_1_7
                                            "... and sucks and licks at it gently, soothing the sore spots left by her teeth."
                                else:
                                    wt_image daughter_house_1_7
                                    "[dee.name] takes the head of your cock gently between her lips ..."
                                    wt_image daughter_house_1_98
                                    "... and swirls around it, licking with her tongue, but using no teeth."
                                wt_image daughter_house_1_6
                                "Then she locks her eyes on yours and picks up the pace, sucking and licking at your cock."
                                wt_image daughter_house_1_97
                                player.c "That's nice, but have you learned to take me deeper, yet?"
                                wt_image daughter_house_1_95
                                dee.c "I'm not sure, but I'll try."
                                wt_image daughter_house_1_7
                                "Slowly, she takes you back into her mouth ..."
                                wt_image daughter_house_1_97
                                "... trying to work her way down your shaft as far as she can ..."
                                wt_image daughter_house_1_100
                                "... which isn't very far before she starts gagging and has to pull off, choking."
                                wt_image daughter_house_1_99
                                dee.c "Fuck, you're big.  Was that any better?"
                                player.c "Honestly, not really.  You're tensing up.  You need to learn to relax if you're going to control your gag reflex."
                                wt_image daughter_house_1_90
                                dee.c "I'm not sure I can, but hopefully I can still give you puppy eyes."
                                wt_image daughter_house_1_97
                                "She goes back to work on your cock, combining both enthusiasm and a fun, teasing technique."
                                wt_image daughter_house_1_91
                                dee.c "There are the puppy-dog eyes I love to see.  I'm going to make you cum, now."
                                wt_image daughter_house_1_6
                                $ title = "Where do you want to cum?"
                            $ title = "Where do you want to cum?"
                            menu:
                                "In her":
                                    wt_image daughter_house_1_94
                                    player.c "[player.orgasm_text]"
                                    wt_image daughter_house_1_92
                                    if dee.has_tag('successful_swallow'):
                                        "She starts to choke and pull back as your sperm shoots into the back of her throat ..."
                                        wt_image daughter_house_1_101
                                        "... but stays in place once she feels your hand on the back of her head, again."
                                        wt_image daughter_house_1_95
                                        "When you finish cumming, she shows you her empty mouth."
                                        player.c "Is that getting easier?"
                                        wt_image daughter_house_1_78
                                        dee.c "A little maybe?  I'm not sure why you won't just cum on my face, though, like a normal guy."
                                    elif dee.has_tag('failed_swallow'):
                                        add tags 'successful_swallow' to dee
                                        "She starts to choke and pull back as your sperm shoots into the back of her throat ..."
                                        wt_image daughter_house_1_101
                                        "... but with a firm hand on the back of her head, you hold her in place."
                                        player.c "No, not this time.  I don't care whether you like the taste of my cum.  You need to learn how to swallow."
                                        wt_image daughter_house_1_90
                                        "Once your balls are empty you let go of her head."
                                        player.c "Show me you swallowed it all."
                                        wt_image daughter_house_1_95
                                        player.c "Good girl.  Other than not being able to deep throat, you're on your way towards becoming a talented little fellatrix."
                                    else:
                                        add tags 'failed_swallow' to dee
                                        "She starts to choke and pull back as your sperm shoots into the back of her throat."
                                        wt_image daughter_house_1_90
                                        if donna.has_tag('cum_slut'):
                                            "Unlike her mother, it seems [dee.name] hasn't acquired a taste for cum."
                                        else:
                                            "It seems [dee.name] doesn't enjoy, or at least doesn't have much experience with, the taste of cum."
                                        player.c "You okay?"
                                        wt_image daughter_house_1_27
                                        dee.c "Yeah, I'm fine.  It's not easy catching your cum without choking when your cock is spurting like that."
                                        player.c "I could tell you didn't have a lot of experience with giving blowjobs."
                                        wt_image daughter_house_1_26
                                        dee.c "I had a little, although none of the guys I've been with before ever tried to teach me how to suck a cock.  And they all seemed to prefer facials.  I haven't had to try and catch a full load like that in my mouth very often.  It's trickier than it sounds."
                                        player.c "Maybe you should ask your Mom for tips on how she does it?"
                                        wt_image daughter_house_1_21
                                        dee.c "Ewww!!  That conversation's not happening!"
                                        player.c "Then I guess I'll just have to teach you how to swallow."
                                        wt_image daughter_house_1_22
                                        dee.c "Great!  Next time I'll bring a guy with me and you can show me how you swallow his load.  Shhh!  Don't try to explain yourself, I know what I heard."
                                    $ dee.swallow_count += 1
                                "On her":
                                    wt_image daughter_house_1_82
                                    "[dee.name] tilts her head back as she jerks your load onto her waiting face."
                                    wt_image daughter_house_1_83
                                    player.c "[player.orgasm_text]"
                                    if dee.has_tag('facial_before'):
                                        wt_image daughter_house_1_65
                                        player.c "You know, those boys in college are onto something.  You do look good like that."
                                    else:
                                        add tags 'facial_before' to dee
                                        wt_image daughter_house_1_66
                                        player.c "I see you don't need any training on offering facials."
                                        wt_image daughter_house_1_65
                                        if dee.professor_event_status > 1:
                                            dee.c "The boys in college like seeing me like this. So did Dr. Jameson.  I figured you would, too."
                                        else:
                                            dee.c "The boys in college like seeing me like this. I figured you would, too."
                                    $ dee.facial_count += 1
                    $ dee.blowjob_count += 1
                    orgasm notify
                "Have her ride you":
                    wt_image daughter_house_1_75
                    player.c "Have you been getting enough workouts in?  You look like you might have been skipping your legs days."
                    dee.c "Is that your way of saying my legs look skinny?  I'm not a gym rat, I don't work out every day."
                    wt_image daughter_house_1_76
                    player.c "So you have been skipping your legs days.  Good thing I have a pole you can exercise on right here."
                    wt_image daughter_house_1_28
                    dee.c "That has to be the lamest line ever!"
                    player.c "Quit stalling, you have a workout ahead of you.  My cock's not going to ride itself."
                    wt_image daughter_house_1_47
                    "If there's anything more enjoyable than watching a petite spinner position herself on top of your cock ..."
                    wt_image daughter_house_1_17
                    "... it could only be the sensation of her young pussy stretching to accommodate your girth as she settles herself onto your erection."
                    wt_image daughter_house_1_48
                    "When she reaches the bottom, she reaches her hands behind you ..."
                    wt_image daughter_house_1_49
                    "... and caresses your balls, as if seeking to assure herself that she does, indeed, finally have you all the way inside her."
                    wt_image daughter_house_1_50
                    "Now satisfied that that's the case, she starts to show off her fitness ..."
                    wt_image daughter_house_1_51
                    "... lifting herself up ..."
                    wt_image daughter_house_1_52
                    "... then slamming herself down."
                    wt_image daughter_house_1_17
                    "It's a tremendous workout for her legs, but one she seems to be enjoying ..."
                    wt_image daughter_house_1_18
                    "... just not quite enough to get herself off, yet."
                    wt_image daughter_house_1_102
                    dee.c "I need more stimulation."
                    $ title = "What do you?"
                    menu:
                        "Take her breast in your mouth":
                            wt_image daughter_house_1_18
                            "Leaning forward, you take her pert nipple into your mouth.  She gasps and picks up the speed at which she's riding you."
                            wt_image daughter_house_1_103
                            dee.c "Ohhh!  Ohh, that feels good!"
                            wt_image daughter_house_1_50
                            "It certainly does, and not just to her."
                            wt_image daughter_house_1_104
                            dee.c "Ohhh FUCCKKKK!!!!"
                            wt_image daughter_house_1_52
                            player.c "[player.orgasm_text]"
                            wt_image daughter_house_1_28
                            dee.c "That was amazing!  A great orgasm and I have an excuse to skip legs day this week!"
                            $ dee.orgasm_count += 1
                        "Spank her" if dee.dom_discussion_count > 3:
                            wt_image daughter_house_1_105
                            "Taking hold of her ass, you give it a squeeze, followed by a sharp slap."
                            wt_image daughter_house_1_106
                            "*SMACK*"
                            wt_image daughter_house_1_109
                            dee.c "OW!  Hey, what the hell?!"
                            wt_image daughter_house_1_108
                            player.c "Shut up and ride me."
                            wt_image daughter_house_1_106
                            "*SMACK*  *SMACK*  *SMACK*"
                            wt_image daughter_house_1_19
                            dee.c "Owww!  Oh!!  Oh fuck!!"
                            wt_image daughter_house_1_107
                            dee.c "Ohhh FUCCKKKK!!!!"
                            wt_image daughter_house_1_106
                            "She continues to buck her hips up-and-down on your cock as she climaxes.  If anything, she rides you faster, milking the cum from your balls."
                            wt_image daughter_house_1_105
                            player.c "[player.orgasm_text]"
                            wt_image daughter_house_1_16
                            dee.c "Jerk!  Don't you think you should ask permission before spanking someone's ass."
                            player.c "What?  You asked for it.  You said you needed more stimulation, I gave it to you."
                            wt_image daughter_house_1_21
                            dee.c "I didn't mean spank my ass!"
                            wt_image daughter_house_1_75
                            player.c "Why not?  You enjoy it when I spank your ass.  I think we should set a rule that I can spank you whenever the mood strikes me."
                            wt_image daughter_house_1_1
                            dee.c "No, definitely not.  But it deal feel good today, so I guess I won't stay mad at you."
                            $ dee.orgasm_count += 1
                        "Just let yourself go":
                            wt_image daughter_house_1_51
                            "She may need more stimulation, but you don't."
                            wt_image daughter_house_1_52
                            player.c "[player.orgasm_text]"
                            wt_image daughter_house_1_46
                            dee.c "That wasn't very nice.  We both should have gotten some from this."
                            wt_image daughter_house_1_75
                            player.c "We both did.  I got an orgasm and you got a workout.  Wasn't that more fun than hitting the gym?"
                            wt_image daughter_house_1_1
                            dee.c "Okay, you got me there.  Hitting you was more fun than hitting the leg machines.  See you next time!"
                    $ dee.sex_count += 1
                    orgasm notify
                "Normal missionary sex":
                    wt_image daughter_house_1_33
                    "[dee.name] watches with interest as you push yourself inside her ..."
                    wt_image daughter_house_1_15
                    "... holding herself open to make the entry easier."
                    wt_image daughter_house_1_12
                    "As you move yourself slowly inside her, her body warms to the sensation ..."
                    wt_image daughter_house_1_39
                    "... getting wetter around your cock as her breath quickens."
                    wt_image daughter_house_1_12
                    "Now you can pick up the pace, bringing her along with you."
                    wt_image daughter_house_1_11
                    dee.c "Oh my God!  Oh!!  Oh fuck I'm going to cum!!"
                    wt_image daughter_house_1_36
                    dee.c "Ohhh FUCCKKKK!!!!"
                    wt_image daughter_house_1_35
                    "As she spasms around your cock, you can't help but let yourself go."
                    wt_image daughter_house_1_38
                    player.c "[player.orgasm_text]"
                    wt_image daughter_house_1_26
                    dee.c "That was fun!  I like having casual sex with you."
                    $ dee.orgasm_count += 1
                    $ dee.sex_count += 1
                    orgasm notify
                "Have her talk dirty to you" if not dee.has_tag('talking_dirty'):
                    add tags 'talking_dirty' to dee
                    if dee.has_tag('talked_dirty_before'):
                        wt_image daughter_house_1_40
                        dee.c "Oh, yeah?  You want me to tell you how much my hot, dripping pussy is looking forward to having your big, sexy cock inside it?"
                        wt_image daughter_house_1_33
                        dee.c "Go on, then.  Stick that sexy man-meat inside me!"
                        call dee_sex_dirty_talk_repeat from _call_dee_sex_dirty_talk_repeat_1
                    else:
                        add tags 'talked_dirty_before' to dee
                        wt_image daughter_house_1_46
                        dee.c "Uh, okay.  I want you to fuck me."
                        player.c "With what?"
                        wt_image daughter_house_1_29
                        dee.c "Uh, your cock?"
                        wt_image daughter_house_1_33
                        player.c "Okay, you want my cock inside you?  Okay, how does that feel?"
                        wt_image daughter_house_1_15
                        dee.c "It feels good.  Really good.  Your cock feels really good inside me."
                        player.c "Does it?  Why?"
                        wt_image daughter_house_1_39
                        dee.c "Mmmm, because you have a big, fat sexy cock."
                        player.c "And what am I doing with it?"
                        wt_image daughter_house_1_12
                        dee.c "Ohh ... you're fucking me with it.  You're fucking me with your fat, hard sexy cock."
                        wt_image daughter_house_1_11
                        "As her words excite you, you fuck her harder and harder.  She finds her body responding, and that encourages her to continue with growing enthusiasm."
                        dee.c "Oh yeah.  Slam that fucking cock of yours into me.  Fuck me with your giant dick and make me cum!"
                        wt_image daughter_house_1_37
                        player.c "Is this what you like?  Getting fucked hard and fast?"
                        dee.c "Yes!!  I love it!  I love your big cock inside me!  Fuck me with it!  Fuck me silly with your giant dick!"
                        wt_image daughter_house_1_36
                        dee.c "Oh my God!  Oh!!  Oh fuck I'm going to cum!!"
                        wt_image daughter_house_1_35
                        dee.c "Ohhh FUCCKKKK!!!!"
                        "As she spasms around your cock, you can't help but let yourself go."
                        wt_image daughter_house_1_38
                        player.c "[player.orgasm_text]"
                        wt_image daughter_house_1_42
                        dee.c "Holy shit!  Now that was a fucking!"
                        player.c "Drop by again some time for another round."
                        wt_image daughter_house_1_40
                        dee.c "If I do, will you pound my pretty pink pussy with your big sexy dick?"
                        player.c "You're getting into this dirty talk thing."
                        wt_image daughter_house_1_28
                        dee.c "It's kinda fun.  We should do it again some time."
                    $ dee.orgasm_count += 1
                    $ dee.sex_count += 1
                    orgasm notify
                "Have her insult you" if not dee.has_tag('insulting_you'):
                    add tags 'insulting_you' to dee
                    if dee.has_tag('insulted_you_before'):
                        wt_image daughter_house_1_40
                        dee.c "God, what a pathetic limp dick you are.  A hot young pussy like mine and you need to be insulted in order to get it up.  Are you even going to be able to get hard enough to get that into my tight pussy, old man?"
                        call dee_sex_insulting_you_repeat from _call_dee_sex_insulting_you_repeat_1
                    else:
                        add tags 'insulted_you_before' to dee
                        wt_image daughter_house_1_29
                        dee.c "Insult you?  What the fuck's wrong with you?  Why would you want me to insult you?"
                        wt_image daughter_house_1_40
                        dee.c "Oh, I get it.  You want me to tell you how ridiculously small your cock is.  Is that what you need to get it up?"
                        wt_image daughter_house_1_33
                        dee.c "Seriously, I can barely even feel you inside me.  This is just going to be a pity fuck, isn't it?  Me letting a small dicked wonder like you have access to my sexy pussy."
                        wt_image daughter_house_1_15
                        dee.c "You're a complete joke, you know that?  You have a tight young body like mine to fuck and you need insults to get you off."
                        wt_image daughter_house_1_42
                        dee.c "That's fucking pathetic.  You can't keep this little limp dick of yours hard without me reminding you of what a loser you are?"
                        wt_image daughter_house_1_15
                        dee.c "Come on, old man.  Pick up the pace.  The guys at my college dick me three times as good as this."
                        wt_image daughter_house_1_34
                        dee.c "Jesus fuck, do you even know what to do with that thing?  I said go faster, loser.  Fuck me like you like girls, assuming you even do."
                        wt_image daughter_house_1_11
                        "As her words excite you, you fuck her harder and harder.  She finds her body responding, and that encourages her to continue with growing enthusiasm."
                        dee.c "God you're pathetic.  A real man would have made me cum three times by now.  Just finish up loser and dribble your little seed into me so I can go find a proper college bull to breed me."
                        wt_image daughter_house_1_37
                        dee.c "Ohh ... is that all you've got?  Quit fumbling around down there and squirt out your little jizz into me already!"
                        wt_image daughter_house_1_11
                        dee.c "Oh fuck ... are you still going?  What's wrong, loser?  Can't get off even when you have a sexy young goddess to fuck?"
                        wt_image daughter_house_1_36
                        dee.c "Oh my God!  Oh!!  Oh fuck I'm going to cum!!"
                        wt_image daughter_house_1_35
                        dee.c "Ohhh FUCCKKKK!!!!"
                        "As she spasms around your cock, you can't help but let yourself go."
                        wt_image daughter_house_1_38
                        player.c "[player.orgasm_text]"
                        wt_image daughter_house_1_28
                        dee.c "Shit, that was fun!  I loved seeing how excited you got when I insulted you.  I think I like this side of you."
                        wt_image daughter_house_1_40
                        dee.c "And I like that you're in touch with your pathetic worm side.  Do you want to lick your spunk out of my pussy before I go?"
                        menu:
                            "Yes, please":
                                wt_image daughter_house_1_44
                                "She lies back and spreads her legs as you get on your knees ..."
                                wt_image daughter_house_1_45
                                "... and suck your own cum out of her just-fucked cunt."
                                wt_image daughter_house_1_41
                                dee.c "That was hot!  I guess it's time for me to go, but I'll definitely be back."
                            "No":
                                wt_image daughter_house_1_27
                                dee.c "Too bad, that would have been hot to watch.  Well I guess my pussy and I are going away, at least for today.  I may come back sometime, when I feel in the mood to let you have another pity fuck."
                            "Never (shuts question off)":
                                add tags 'no_licking_spunk_from_her' to dee
                                wt_image daughter_house_1_27
                                dee.c "Too bad, that would have been hot to watch.  Well I guess my pussy and I are going away, at least for today.  I may come back sometime, when I feel in the mood to let you have another pity fuck."
                    $ dee.orgasm_count += 1
                    $ dee.sex_count += 1
                    orgasm notify
                "Have her insult herself" if dee.has_any_tag('insulted_herself_before', 'open_to_being_insulted') and not dee.has_tag('insulting_herself'):
                    if dee.has_tag('insulted_herself_before'):
                        wt_image daughter_house_1_23
                        dee.c "Do we have to do it like this?  Can't we just have sex like normal people?"
                        wt_image daughter_house_1_29
                        player.c "But you're not a normal girl, are you [dee.name]?  A normal girl doesn't drop by looking for sex from a man who's going to make her insult herself.  Tell me what you really are."
                        call dee_sex_insulting_herself_repeat from _call_dee_sex_insulting_herself_repeat_1
                    else:
                        wt_image daughter_house_1_21
                        dee.c "What?  I'm not going to do that!"
                        player.c "Yes, you are.  It turned you on when I pointed out what a stupid cum dump you are.  Now you're going to let me know you see yourself the same way."
                        wt_image daughter_house_1_2
                        dee.c "But I don't see myself that way."
                        player.c "Then why are you getting wet, thinking about being treated as a cum dump?"
                        wt_image daughter_house_1_10
                        dee.c "I don't know.  I must just be horny, I guess."
                        player.c "A horny what, [dee.name]?  What exactly are you?  Describe yourself to me."
                        wt_image daughter_house_1_16
                        dee.c "I'm a horny college girl who wants you to fuck my scrawny body."
                        player.c "That's an okay start, but you can run yourself down more than that, can't you, you dumb cunt?"
                        wt_image daughter_house_1_42
                        dee.c "Yes, I can.  I'm just a dumb, skinny blonde.  Fuck me like the stupid slut I am."
                        wt_image daughter_house_1_15
                        player.c "You're going too easy on yourself.  Tell me what you or I take my cock away."
                        dee.c "I'm a skinny, tiny-titted tramp who should have her stupid feminist thoughts fucked out of her by a hard cock."
                        wt_image daughter_house_1_37
                        "As you start to fuck her, she finds her body responding, and that encourages her to insult herself with growing enthusiasm."
                        dee.c "Oh yeah.  Fuck some sense into this stupid slut!  Treat me like your scrawny, tiny-titted blonde whore."
                        wt_image daughter_house_1_11
                        dee.c "Fill me!  Fill this stupid cunt with your seed!!"
                        player.c "Do you know what a stupid slut begging for a man's cum is?"
                        wt_image daughter_house_1_39
                        dee.c "A cum dump!  Use me as your scrawny, small-titted blonde cum dump."
                        player.c "I don't know.  A young whore like you, I think the whole feminist bit was just an act.  I think you're just trying to trap me into filling your belly with my baby so I'll look after you.  It won't work, you know?  I'll kick you to the curb, barefoot and pregnant, and never think of you again.  You know that, right?  Do you still want my cum?"
                        wt_image daughter_house_1_12
                        dee.c "Yes!  Please!  I'm such a stupid young cunt I want you use me as your cum dump, I don't care about the consequences!!"
                        wt_image daughter_house_1_37
                        dee.c "Please!!  Please, use me as your cum dump!  Fill this scrawny skank with your seed!"
                        wt_image daughter_house_1_36
                        dee.c "Oh my God!  Oh!!  Oh fuck I'm going to cum!!!"
                        wt_image daughter_house_1_35
                        dee.c "Ohhh FUCCKKKK!!!!"
                        "As she spasms around your cock, you can't help but let yourself go."
                        wt_image daughter_house_1_38
                        player.c "[player.orgasm_text]"
                        wt_image daughter_house_1_29
                        "When you finish pumping your load into her, she looks at you with a combination of bewilderment and mortification."
                        player.c "You okay, kid?"
                        wt_image daughter_house_1_41
                        dee.c "Yeah, I guess.  It's just ... "
                        player.c "Relax.  It was just sex.  Kinky sex.  Hot, too, wasn't it?"
                        wt_image daughter_house_1_40
                        dee.c "Very!  But just to set the record straight, I'm not a cunt, a slut or a whore.  I don't care what I just said.  And I really am on birth control."
                        player.c "Not a cunt, slut or whore.  Got it.  Just a scrawny blonde cum dump, then, I guess?"
                        wt_image daughter_house_1_28
                        "She punches you playfully on the arm."
                        dee.c "Stop it!  Don't call me that, either.  Not unless you're fucking me silly while you're doing it."
                        add tags 'insulted_herself_before' 'insulting_herself' to dee
                    $ dee.sex_count += 1
                    $ dee.orgasm_count += 1
                    orgasm notify
                "Nothing, just send her home":
                    wt_image daughter_house_1_22
                    dee.c "Seriously?  What happened?  Is it suddenly past your bedtime?  I guess I'd better leave and let you have your beauty sleep, huh?"
            $ dee.temporary_count = 0
        call dee_visit_end from _call_dee_visit_end_8
    elif dee.has_tag('post_hypno_sex_interest'):
        player.c "It's late, kid.  I'm too tired to debate human nature with you tonight.  Let's you and I go into the bedroom before I'm too tired to fuck you."
        wt_image daughter_house_1_25
        dee.c "Funny you should mention being tired.  I had the weirdest dream after one of our visits.  I must have been super tired when I got home because ..."
        wt_image daughter_house_1_23
        "Suddenly her cheeks blush and she averts her eyes."
        player.c "Because what?  Did you have a dream about me or something?"
        wt_image daughter_house_1_21
        dee.c "How did you know?!"
        player.c "Lucky guess.  It must have been a good dream.  Do you want to tell me about it?"
        wt_image daughter_house_1_20
        dee.c "Not really.  I think I'm going to keep this one a secret."
        player.c "A secret?  Why?  What did you dream about."
        wt_image daughter_house_1_24
        dee.c "It was about you and it's embarrassing."
        player.c "Embarrassing?  What were we doing?  Fucking?"
        wt_image daughter_house_1_21
        dee.c "Yes!  How did you know?!"
        player.c "It's a pretty obvious guess, don't you think?  But why would us having sex in your dream be embrassing?"
        wt_image daughter_house_1_25
        dee.c "Wow, you're determined.  Because it was a wet dream, okay?  I actually came while I was sleeping?  Satisfied?"
        player.c "No.  If the dream was that good, imagine how good the reality would be."
        wt_image daughter_house_1_24
        dee.c "It was just a dream, okay?  I don't actually want to have sex with you."
        player.c "Really?  How about we test that theory.  You lift up your skirt.  If you're dry, I'll agree, it was just a silly dream and I'll drop the subject.  If you're wet, though, then we fuck, and we'll see if we can make real life even more exciting than your wet dream."
        wt_image daughter_house_1_25
        "[dee.name] sits there and for a moment you think she's about to tell you off.  Then her expression softens and she lifts her skirt."
        call dee_first_sex from _call_dee_first_sex
    elif dee.dom_discussion_count == 3 and dee.ready_for_mom < 3:
        wt_image daughter_house_1_22
        dee.c "I said I was ready to let you dominate me, I didn't say anything about sleeping with you."
        player.c "Really?  And you don't think I'm going to have my way with you after I've dominated you?"
        wt_image daughter_house_1_2
        dee.c "I guess that will depend on whether you're just all talk or if you can make it as interesting an experience as you promised."
    elif dee.has_tag('bound_sex_before'):
        player.c "It's late, kid.  I'm too tired to debate human nature with you tonight.  Let's you and I go into the bedroom before I'm too tired to fuck you."
        wt_image daughter_house_1_22
        dee.c "Whoa, where is that coming from?  I'm not about to go to bed with you."
        player.c "Okay, you can take your clothes off here and I'll fuck you on the sofa."
        wt_image daughter_house_1_21
        dee.c "I'm not about to do that either!"
        wt_image daughter_house_1_24
        player.c "Really?  If I pull you over my lap on the sofa, flip your skirt up and spank your bare ass, I could have you ready to spread your legs for me in no time.  Couldn't I?"
        "She looks at you in disbelief for a moment, then slowly lowers her head."
        wt_image daughter_house_1_23
        dee.c "Yes, Sir.  Probably."
        player.c "Is that what you want, a relationship where I need to tie you up and spank you everytime I want to fuck you?"
        wt_image daughter_house_1_22
        dee.c "No, I guess not."
        player.c "You guess not or you know not?  Spread your legs and pull up your skirt.  Let's see what your body has to say on the subject."
        call dee_first_sex from _call_dee_first_sex_1
    elif dee.has_tag('sex_discussion_before') or dee.ready_for_mom > 2:
        wt_image daughter_house_1_2
        if dee.ready_for_mom > 2:
            dee.c "Whoa!  What we did together with Mom was about fulfilling her fantasy.  I'm not interested in starting a sexual relationship with you."
        else:
            dee.c "I already told you 'no', before."
        if dee.dom_discussion_count == 1 and dee.marilyn_event_status > 1 and not dee.has_tag('talked_domination_today'):
            player.c "And you haven't reconsidered?  Not even after your experience with Marilyn?"
            wt_image daughter_house_1_24
            dee.c "What does Marilyn have to do with it?"
            player.c "You remember how she made you feel. 'Putty in her hands' were your words.  You're not naturally submissive, but you were with her, and you liked it.  I can help you recapture that feeling.  Who knows?  There may be a whole new side of your sexuality you'd enjoy exploring."
            wt_image daughter_house_1_22
            dee.c "And you're volunteering to help me experience it?  How generous of you.  I can guess what you're hoping to get out of that, but what would I get out of it?"
            if dee.talk_sex_life_status > 2:
                player.c "A good time, better than you're expecting.  A learning experience, too.  If you're not sure you want to explore your submissive side, what about using it as a way to explore your dominant side.  You'd like to be able to make people feel what Marilyn made you feel, wouldn't you?  Your RA, for example?"
            else:
                player.c "A good time, better than you're expecting.  A learning experience, too.  If you're not sure you want to explore your submissive side, what about using it as a way to explore your dominant side.  You'd like to be able to make people feel what Marilyn made you feel, wouldn't you?"
            wt_image daughter_house_1_2
            dee.c "You could teach me to take control of others as easily as Marilyn took control of me?  Even though I'm not a powerful woman like she is?"
            player.c "You'll teach yourself, I'll just be the role model.  The more experiences you have as a submissive, the better you'll understand how the person you're trying to control is feeling."
            wt_image daughter_house_1_1
            player.c "I can see you're not ready to say 'yes' right now, but think about it.  There's no need to rush, we can do this when you're ready."
            add tags 'talked_domination_today' to dee
            $ dee.dom_discussion_count = 2
    else:
        player.c "It's late, kid.  I'm too tired to debate human nature with you tonight.  Let's you and I go into the bedroom before I'm too tired to fuck you."
        wt_image daughter_house_1_21
        dee.c "See?  That's what I'm talking about.  You see me as a sexual object."
        $ title = "How do you respond?"
        menu:
            "Rely on your charm" if player.has_tag('supersexy'):
                "You shrug."
                player.c "Women who show up unexpectedly at my house usually want to sleep with me.  If you don't, no big deal.  I'm just telling you it's late, and if we're going to do this, let's get started."
                wt_image daughter_house_1_24
                dee.c "Seriously?  That's your pick up line?  You're not making any effort at all."
                player.c "Effort to what?  Make you feel special?  You're not.  But you're cute, and you're here, and I'm telling you I'm available if you want to.  You want flowers and romance and a guy to win you over, I'm sure they'll come along, not that you'll give them the time of day. I thought you were a liberated woman comfortable with her sexual side who's not afraid to act on her urges."
                wt_image daughter_house_1_22
                dee.c "And you just assume one of my urges is to fuck you?"
                player.c "You tell me.  Instead of talking, I could have my fingers in your cunt right now.  If that thought doesn't make you wet, go home.  If it does make you wet, you need to decide what you're going to do about it."
                wt_image daughter_house_1_25
                "[dee.name] sits there and for a moment you think she's about to storm off.  Then her expression softens and she lifts her skirt."
                call dee_first_sex from _call_dee_first_sex_2
            "Dominate her" if player.has_tag('dominant'):
                add tags 'sex_discussion_before' to dee
                player.c "I see you as a potential sex partner. It's not the same thing."
                wt_image daughter_house_1_2
                dee.c "But you asked me to go to bed with you without knowing anything about me or what I like, and without me giving you any indication that I was interested in you."
                player.c "I'm old enough and experienced enough to figure out what my sex partners like without conducting a pre-sex survey, especially at this hour of the night.  And if you weren't interested, you'd say no."
                wt_image daughter_house_1_22
                dee.c "So you just tell every woman who comes to your house to come to your bedroom with you, just in case they're interested?"
                player.c "No, just some of them.  Some I tell to come into my dungeon with me."
                wt_image daughter_house_1_24
                dee.c "Your dungeon?  Are you serious?"
                player.c "Yes.  Would you like to see it?"
                wt_image daughter_house_1_21
                dee.c "No!  Is that what you do with Mom?"
                player.c "Do you think she'd like that?"
                wt_image daughter_house_1_24
                dee.c "No!  I don't know.  I don't think so."
                player.c "Are you sure?  She is rather submissive, as you know very well and no doubt take advantage of, like with your laundry.  You on the other hand aren't, at least not in your daily life.  Have you wondered what it would be like?"
                wt_image daughter_house_1_2
                dee.c "What would be like?"
                player.c "Giving up control.  Letting someone else tell you what to do.  Giving them the authority to do whatever they want to you, whatever would make them happy, with no consideration as to what you want."
                wt_image daughter_house_1_21
                dee.c "No!  Why would I do that?"
                player.c "To experiment.  To understand other people better.  Your mother, for example.  Or maybe just for the naughty thrill of it.  Have you ever had a boyfriend or girlfriend spank you?"
                wt_image daughter_house_1_24
                dee.c "No, never.  And I haven't wanted them to."
                player.c "Then you're not dating a wide enough range of people."
                wt_image daughter_house_1_22
                dee.c "I suppose you think I should start dating you?"
                player.c "No, but you should visit me in my dungeon sometime.  You'll learn some things about yourself, and maybe some skills you can use with others, too.  Are you going to sleep with me tonight?  Or lie across my lap and let me spank you?"
                wt_image daughter_house_1_21
                if dee.has_tag('first_visit'):
                    dee.c "No!  I don't even know you."
                else:
                    dee.c "No!  I hardly even know you."
                player.c "Perhaps next time, then.  It's late, kid.  I'm too tired to debate human nature with you tonight.  You want to understand what people are really like, drop by again some time when it isn't so late and we can chat."
                $ dee.dom_discussion_count = 1
                call dee_visit_end from _call_dee_visit_end_9
            "Hypnotize her" if player.can_hypno(dee):
                $ queue_action(donna.hypno_action)
            "Just talk with her" if not player.has_any_tag('supersexy', 'dominant'):
                add tags 'sex_discussion_before' to dee
                player.c "I see you as a potential sex partner. It's not the same thing."
                wt_image daughter_house_1_2
                dee.c "But you asked me to go to bed with you without knowing anything about me or what I like, and without me giving you any indication that I was interested in you."
                player.c "I'm old enough and experienced enough to figure out what my sex partners like without conducting a pre-sex survey, especially at this hour of the night.  And if you weren't interested, you'd say no."
                wt_image daughter_house_1_22
                dee.c "So you just tell every woman who comes to your house to come to your bedroom with you, just in case they're interested?"
                player.c "Just the ones I'm attracted to."
                wt_image daughter_house_1_25
                dee.c "Which is probably all of them.  No, I'm not interested in sleeping with you."
                player.c "Fine.  You don't have to be snarky about it. It's late, kid.  I'm too tired to debate human nature with you tonight.  You want to understand what people are really like, drop by again some time when it isn't so late and we can chat."
                call dee_visit_end from _call_dee_visit_end_10
            "Try something else":
                pass
    return

label dee_sex_dirty_talk_repeat:
    wt_image daughter_house_1_34
    dee.c "Ohh ... you're fucking me with it!  You're fucking me with your fat, hard sexy cock!"
    wt_image daughter_house_1_11
    dee.c "That's it!  Pound my pretty pink pussy with your big sexy dick!!"
    wt_image daughter_house_1_39
    dee.c "Ohhh, you're making me so wet!"
    player.c "Is this what you like?  My big cock splitting you open?"
    wt_image daughter_house_1_15
    dee.c "Yes!!  I love it!  I love your big cock inside me!  Fuck me with it!  Make me cum on your dick!!"
    wt_image daughter_house_1_12
    dee.c "Ohhh, you're doing it!!  You're using your giant meat-stick to make me cum!!"
    wt_image daughter_house_1_37
    dee.c "Oh my God!  Oh!!  Oh fuck, you're going to fuck an orgasm out of me!!!"
    wt_image daughter_house_1_36
    dee.c "Ohhh FUCCKKKK!!!!"
    wt_image daughter_house_1_35
    "As she spasms around your cock, it's hard to hold back, but you wait for her to recover her breath, so she can dirty talk you through to orgasm, too."
    wt_image daughter_house_1_15
    dee.c "Oh yeah!  Don't hold back!!  Slam that fucking cock of yours into me."
    wt_image daughter_house_1_37
    dee.c "Yes!  Just like that!!  Fuck me with your giant dick and fill me with your seed!"
    wt_image daughter_house_1_38
    player.c "[player.orgasm_text]"
    wt_image daughter_house_1_42
    dee.c "Holy shit!  Now that was a fucking!  I think my pussy's going to be sore for a week."
    player.c "Should I apologize?"
    wt_image daughter_house_1_28
    dee.c "No way!  I love how riled up you get from dirty talk.  I can't wait to do this with you again."
    return

label dee_sex_insulting_you_repeat:
    wt_image daughter_house_1_33
    "You are, and relatively easily, too, as she's already wet, seemingly excited from insulting you."
    wt_image daughter_house_1_34
    dee.c "It's a fucking miracle.  You managed to get it up and inside me.  Now show me you know how to use that worthless cock of yours."
    wt_image daughter_house_1_15
    "You start to fuck her, but she's not impressed."
    dee.c "Seriously, is that the best you can do?  Pick up the pace, limp dick."
    wt_image daughter_house_1_39
    "You thrust faster, but she's still not happy."
    dee.c "Are you even doing anything down there?  I'm used to being fucked hard by young college studs, this is fucking embarrassing."
    wt_image daughter_house_1_12
    "You keep going and despite her insults - or maybe because of them - you can tell her excitement is growing."
    dee.c "What a fucking loser you are.  A tight sexy college girl to fuck and this is all you can muster?  Go faster already."
    wt_image daughter_house_1_11
    "As she continues to insult you, you can tell she's getting more and more excited, and so are you."
    dee.c "Jesus fuck, do you even know what to do with that thing?  I said go faster, loser.  Fuck me like you like girls, assuming you even do."
    wt_image daughter_house_1_37
    "Egged on by her taunting, you give her as hard a pounding as you've ever given anyone, and her body responds accordingly even as she continues to insult you."
    dee.c "Pathetic, fucking, loser!  I would have cum three times by now if a real man had been doing this to me."
    wt_image daughter_house_1_36
    dee.c "Harder!  Harder you fucking limp dick!!  Harder!!!"
    wt_image daughter_house_1_35
    dee.c "Ohhh FUCCKKKK!!!!"
    wt_image daughter_house_1_12
    dee.c "Mmmmm, you haven't cum, yet.  Limp dick like you probably can't even get off, but if you think you can, loser, do it."
    wt_image daughter_house_1_36
    dee.c "Oh shit, that's it!  Show me that you like girls after all and fill me with your sad little trickle of cum, old man!!"
    wt_image daughter_house_1_38
    player.c "[player.orgasm_text]"
    if dee.has_tag('no_licking_spunk_from_her'):
        wt_image daughter_house_1_41
        dee.c "That was hot!  You are such a fun sex partner!"
    else:
        wt_image daughter_house_1_46
        dee.c "Fuck that was fun.  You know what would be even more fun, loser?"
        wt_image daughter_house_1_40
        dee.c "Lick your spunk out of my pussy before I go."
        $ title = "Do it?"
        menu:
            "Yes":
                wt_image daughter_house_1_44
                "She lies back and spreads her legs as you get on your knees ..."
                wt_image daughter_house_1_45
                "... and suck your own cum out of her just-fucked cunt."
                wt_image daughter_house_1_41
                dee.c "That was so fucking hot!  You are such a fun sex partner!"
            "No":
                wt_image daughter_house_1_26
                dee.c "Too bad, that would have been so hot.  I had fun anyway, though.  Thanks for being such a great sex partner."
            "Never (shuts question off)":
                add tags 'no_licking_spunk_from_her' to dee
                wt_image daughter_house_1_26
                dee.c "Too bad, that would have been so hot.  I had fun anyway, though.  Thanks for being such a great sex partner."
    return

label dee_sex_insulting_herself_repeat:
    wt_image daughter_house_1_46
    dee.c "A dumb cunt for you to fuck."
    player.c "Should you be proud of your body, slut?"
    wt_image daughter_house_1_41
    dee.c "No.  I'm too skinny and I have tiny tits."
    player.c "So why should I fuck a tit-less whore like you?"
    wt_image daughter_house_1_40
    dee.c "Because I can be a cock-sleeve and a cum dump for you."
    wt_image daughter_house_1_33
    player.c "Is this what you're good for?  A place for men to stick their dicks into?"
    wt_image daughter_house_1_15
    dee.c "This is all I'm good for.  A hole for fucking."
    wt_image daughter_house_1_39
    player.c "I thought you were a feminist?  An educated woman?  That's what you pretend to be.  But that's not what you really are, is it?  What are you really?"
    wt_image daughter_house_1_12
    dee.c "I'm a dumb cunt!  A meat-bag for you to fuck!!"
    player.c "That's right, fuck toy.  That's all you are.  How does that make you feel?"
    wt_image daughter_house_1_11
    dee.c "Turned on!  I'm so fucking wet right now!"
    player.c "What does that say about you, whore?  What does it say that being my fuck toy turns you on?"
    wt_image daughter_house_1_37
    dee.c "That I'm a dumb fucking cunt who loves being treated like a piece of meat!!"
    wt_image daughter_house_1_36
    dee.c "Ohhh FUCCKKKK!!!!"
    wt_image daughter_house_1_35
    "As she spasms around your cock, it's hard to hold back, but you wait for her to recover so she can resume insulting herself before you cum."
    wt_image daughter_house_1_12
    player.c "What's going to happen now, slut?"
    wt_image daughter_house_1_15
    dee.c "You're going to fill me with your cum."
    player.c "What does that make you?"
    wt_image daughter_house_1_11
    dee.c "Your cum dump!  Your scrawny, tiny-titted blonde cum dump!!"
    wt_image daughter_house_1_38
    player.c "[player.orgasm_text]"
    if not dee.has_tag('insulting_herself_reflection_complete'):
        add tags 'insulting_herself_reflection_complete' to dee
        wt_image daughter_house_1_41
        "When you finish, [dee.name] looks at you, an uncertain expression on her face."
        dee.c "The things I said ... you don't really think of me like that, do you?"
        player.c "Does it matter?  Which do you think would be hotter, if that was just role-play or if I really do think of you as a stupid slut with no value other than as a place for me to dump my cum?"
        wt_image daughter_house_1_29
        dee.c "I mean, if you did see me like that ... if this wasn't us just playing a kinky game ..."
        wt_image daughter_house_1_40
        dee.c "... then you'd be looking at me right now and thinking what a dumb cunt I am, and you'd be right.  I'd be nothing but a dumb cunt."
        player.c "Let's run with that for a moment.  Does it change whether you'd be willing to come visit me?"
        wt_image daughter_house_1_29
        dee.c "Well, yeah!  I mean I wouldn't want to ..."
        player.c "Wouldn't want to what?  Have hot casual sex that gives you intense orgasms?"
        wt_image daughter_house_1_27
        dee.c "The sex is really hot.  But if I knew you really thought that way and it wasn't just role-play, I don't think I could respect myself if I kept returning."
        player.c "And if we leave it ambiguous, so you don't know whether I really see you as a stupid tiny-titted cum dump?"
        wt_image daughter_house_1_26
        dee.c "Then the sex will probably be even hotter.  Okay, as long as you keep the insults to when we're having sex, I'll be back."
    else:
        wt_image daughter_house_1_27
        dee.c "You know, I still can't figure out whether the things you say about me, the things you want me to say about myself, whether that's just kinky sex play or the way you really see me."
        wt_image daughter_house_1_26
        dee.c "Please keep your mouth shut and don't enlighten me. I've decided you were right with what you said before, the casual sex is actually hotter when I don't really know."
    return

label dee_first_sex:
    wt_image daughter_house_1_10
    dee.c "You win, I'm wet.  See?"
    wt_image daughter_house_1_30
    "She pulls her panties to the side to give you a clearer look.  Then a nervous, conflicted look passes her face."
    wt_image daughter_house_1_31
    if dee.has_tag('first_visit'):
        dee.c "Before we do this, I just need to know. Did you just ... you know, finish doing this with my Mom?"
    else:
        dee.c "Before we do this, I just need to know. Have you ... you know, done this with my Mom?"
    $ title = "How do you reply?"
    menu:
        "Yes, I did":
            player.c "Yes, I did.  Do you think you can get me off better than your Mom did?"
            wt_image daughter_house_1_32
            "[dee.name] is uncharacteristically silent."
            player.c "No response?  You think you're better than your Mom at most things, don't you?"
            wt_image daughter_house_1_31
            dee.c "I never said that."
            player.c "I'm not talking about what you've said.  I'm talking about what you think.  You view yourself as being more competent than your Mom, don't you?"
            "She nods."
            wt_image daughter_house_1_32
            player.c "So now I'm going to judge you, to see if you know how to fuck as good as she does.  Do you think you can?"
            wt_image daughter_house_1_4
            "She nods again."
            dee.c "Yes, I'm going to fuck you better than my mother did."
            add tags 'will_fuck_better_than_mom' to dee
        "What does it matter?":
            player.c "What does it matter?  You could have fucked five guys on the way over here.  I could have had seven women through here earlier today.  Does it matter if one of them was your Mom?"
            wt_image daughter_house_1_30
            dee.c "I guess not.  It's weird, though, isn't it?"
            player.c "Is it weird, or does it turn you on?"
            wt_image daughter_house_1_32
            dee.c "I don't know."
            player.c "The wetness on your pussy tells me it doesn't turn you off."
            wt_image daughter_house_1_4
            dee.c "No, I guess it doesn't."
        "I don't kiss and tell":
            player.c "What I did or didn't do with your mother is between her and me, just like what I do or don't do with you is between you and me.  If you really want to know, you can ask her, but I'm not saying."
            wt_image daughter_house_1_4
            dee.c "That's fair.  It makes me feel better about this, actually.  I'm ready to fuck you now."
    wt_image daughter_house_1_16
    "[dee.name] stares lustfully at your body - especially your cock - as you remove your clothes and prepare to fuck her."
    wt_image daughter_house_1_33
    "She's wet, warm, and tight as you push into her, and it feels great - to both of you."
    wt_image daughter_house_1_11
    dee.c "Oh, yeah.  Fuck that feels good!"
    wt_image daughter_house_1_34
    dee.c "That's it.  Fuck me.  Harder.  Oh yeah.  Fuck!   That's it.  Right like that."
    wt_image daughter_house_1_35
    dee.c "Oh my God!  Oh!!  Oh fuck I'm going to cum!!!"
    wt_image daughter_house_1_36
    dee.c "Ohhh FUCCKKKK!!!!"
    wt_image daughter_house_1_37
    if dee.professor_event_status > 1 or dee.marilyn_event_status > 1:
        player.c "You really do have a hair trigger."
        wt_image daughter_house_1_12
        dee.c "What do you mean?"
        if dee.professor_event_status > 1 and dee.marilyn_event_status > 1:
            player.c "I mean with your professor and with Marilyn and now with me, you cum quickly when you're excited."
        elif dee.professor_event_status > 1:
            player.c "I mean with your professor and now with me, you cum quickly after penetration when you're excited."
        else:
            player.c "I mean with Marilyn and now with me, you cum quickly when you're excited."
        wt_image daughter_house_1_42
        dee.c "So?  Nobody ever complains when men cum quickly."
        player.c "That's definitely not true, but regardless I didn't mean anything bad by it.  A lot of women your age aren't able to let themselves cum, especially not with a new partner.  It's great that you are able to."
        wt_image daughter_house_1_15
        dee.c "Thanks, I guess.  Is there anything I can do to help you relax so that you can let yourself cum, to?"
    else:
        player.c "Before I get flattered, are you always that responsive and quick to cum?"
        wt_image daughter_house_1_12
        dee.c "No, you can go ahead and feel flattered.  I'm not normally that excited."
        player.c "Maybe knowing that your Mom has also spent time with me is a turn on for you."
        wt_image daughter_house_1_15
        "She blushes and quickly changes the topic."
        dee.c "You haven't come yet.  Is there anything I can do?"
    $ title = "What do you want?"
    menu menu_dee_first_sex_menu:
        "Have her suck you off":
            wt_image daughter_house_1_41
            player.c "Why don't you show me what you can do with your mouth?"
            wt_image daughter_house_1_53
            "If she has any reservations about tasting her own cum juices, she doesn't let on ..."
            wt_image daughter_house_1_54
            "... as she licks your dick clean of all residue from having been inside her pussy ..."
            wt_image daughter_house_1_55
            "... before taking you inside her mouth."
            wt_image daughter_house_1_56
            "As blowjobs go, it's a typical college girl effort ..."
            wt_image daughter_house_1_57
            "... long on enthusiasm and effort, short on subtlety or technique ..."
            wt_image daughter_house_1_55
            "... but more than pleasurable enough to get the job done."
            wt_image daughter_house_1_58
            $ title = "Where do you want to cum?"
            menu:
                "In her":
                    add tags 'failed_swallow' to dee
                    wt_image daughter_house_1_59
                    player.c "[player.orgasm_text]"
                    wt_image daughter_house_1_60
                    if donna.has_tag('cum_slut'):
                        "Unlike her mother, it seems [dee.name] hasn't acquired a taste for cum ..."
                    else:
                        "It seems [dee.name] doesn't enjoy, or at least doesn't have much experience with, the taste of cum ..."
                    wt_image daughter_house_1_61
                    "... but she diligently pumps as much seed out of your balls as they have to give."
                    wt_image daughter_house_1_62
                    "When you finally finish, she gags slightly as she swallows your load."
                    player.c "You okay?"
                    wt_image daughter_house_1_27
                    dee.c "Yeah, I'm fine.  It's not easy catching your cum without choking when your cock is spurting like that."
                    player.c "I guess you don't have a lot of experience with giving blowjobs."
                    wt_image daughter_house_1_26
                    dee.c "I have a little, but most of the guys I've been with seemed to prefer facials.  I haven't had to try and catch a full load like that in my mouth very often.  It's trickier than it sounds."
                    player.c "Maybe you should ask your Mom for tips on how she does it?"
                    wt_image daughter_house_1_21
                    dee.c "Ewww!!  That conversation's not happening!"
                    player.c "Then I guess I'll just have to teach you how to swallow."
                    wt_image daughter_house_1_22
                    dee.c "Great!  Next time I'll bring a guy with me and you can show me how you swallow his load.  Shhh!  Don't try to explain yourself, I know what I heard."
                    $ dee.swallow_count += 1
                "On her":
                    add tags 'facial_before' to dee
                    wt_image daughter_house_1_63
                    player.c "[player.orgasm_text]"
                    wt_image daughter_house_1_64
                    if dee.professor_event_status > 1:
                        dee.c "So I guess it's not just college boys and Dr. Jameson who like to see me like this."
                    else:
                        dee.c "So I guess it's not just college boys who like to see me like this."
                    wt_image daughter_house_1_65
                    player.c "Have many of the boys from your school been able to admire you in this condition?"
                    wt_image daughter_house_1_66
                    dee.c "I'm not a slut, if that's what you're trying to imply.  And even if I were, there's nothing wrong with a woman having a healthy libido and multiple consensual partners at the same time, as long as she hasn't made a monogamous commitment to any of them."
                    wt_image daughter_house_1_67
                    player.c "Well, the next time your non-monogamous libido is in the mood for another facial, drop by and see me."
                    $ dee.facial_count += 1
            $ dee.blowjob_count += 1
            orgasm notify
        "Have her ride you":
            wt_image daughter_house_1_46
            player.c "A young thing like you should be keeping herself in good shape.  Climb up on top of me and let's find out how fit you are."
            wt_image daughter_house_1_47
            "If there's anything more enjoyable than watching a petite spinner position herself on top of your cock ..."
            wt_image daughter_house_1_17
            "... it could only be the sensation of her young pussy stretching to accommodate your girth as she settles herself onto your erection."
            wt_image daughter_house_1_48
            "When she reaches the bottom, she reaches her hands behind you ..."
            wt_image daughter_house_1_49
            "... and caresses your balls, as if seeking to assure herself that she does, indeed, finally have you all the way inside her."
            wt_image daughter_house_1_50
            "Now satisfied that that's the case, she starts to show off her fitness ..."
            wt_image daughter_house_1_51
            "... lifting herself up ..."
            wt_image daughter_house_1_52
            "... then slamming herself down."
            wt_image daughter_house_1_17
            "It's a tremendous workout for her legs ..."
            wt_image daughter_house_1_18
            "... but one she seems to be enjoying ..."
            wt_image daughter_house_1_51
            "... although not quite so much as you are."
            wt_image daughter_house_1_52
            player.c "[player.orgasm_text]"
            if dee.has_tag('will_fuck_better_than_mom'):
                wt_image daughter_house_1_42
                dee.c "I bet I was able to ride you a lot faster than Mom could."
                wt_image daughter_house_1_29
                player.c "You might be surprised.  But I did enjoy that, yes."
            else:
                wt_image daughter_house_1_41
                dee.c "Was that okay?  I mean, I'm pretty sure it was, but - that was good for you, right?"
                player.c "Yes, [dee.name].  I enjoyed that."
            wt_image daughter_house_1_28
            dee.c "Good.  I enjoyed that, too.  And now I have an excuse to skip legs day this week.  I guess I'd better be going."
            $ dee.sex_count += 1
            orgasm notify
        "Have her talk dirty to you":
            add tags 'talked_dirty_before' 'talking_dirty' to dee
            wt_image daughter_house_1_15
            dee.c "Uh, okay.  Your cock feels really good inside me."
            player.c "Does it?  Why?"
            wt_image daughter_house_1_39
            dee.c "Mmmm, because you have a big, fat sexy cock."
            player.c "And what am I doing with it?"
            wt_image daughter_house_1_12
            dee.c "Ohh ... you're fucking me with it.  You're fucking me with your fat, hard sexy cock."
            wt_image daughter_house_1_11
            "As her words excite you, you fuck her harder and harder.  She finds her body responding, and that encourages her to continue with growing enthusiasm."
            dee.c "Oh yeah.  Slam that fucking cock of yours into me.  Fuck me with your giant dick and fill me with your seed!"
            $ title = "What do you?"
            menu:
                "Oblige her":
                    wt_image daughter_house_1_37
                    player.c "Is this what you like?  Getting fucked hard and fast until your insides are blsted with spunk."
                    dee.c "Yes!!  I love it!  Do it, fill me up!"
                "Hold off and see if she'll cum":
                    wt_image daughter_house_1_37
                    player.c "Is this what you like?  Getting fucked hard and fast?"
                    dee.c "Yes!!  I love it!  I love your big cock inside me!  Fuck me with it!  Fuck me silly with your giant dick!"
                    wt_image daughter_house_1_36
                    dee.c "Oh my God!  Oh!!  Oh fuck I'm going to cum again!!!"
                    wt_image daughter_house_1_35
                    dee.c "Ohhh FUCCKKKK!!!!"
                    "As she spasms around your cock, you can't help but let yourself go."
                    $ dee.orgasm_count += 1
            wt_image daughter_house_1_38
            player.c "[player.orgasm_text]"
            wt_image daughter_house_1_42
            dee.c "Holy shit!  Now that was a fucking!"
            player.c "Drop by again some time for another round."
            wt_image daughter_house_1_40
            dee.c "If I do, will you pound my pretty pink pussy with your big sexy dick?"
            player.c "You're getting into this dirty talk thing."
            wt_image daughter_house_1_28
            if dee.has_tag('will_fuck_better_than_mom'):
                dee.c "It's kinda fun.  I bet Mom doesn't have as a big a potty mouth as me."
            else:
                dee.c "It's kinda fun.  You'd never be able to get Mom to go along with it, though, I bet."
            player.c "You'd be surprised."
            $ dee.sex_count += 1
            orgasm notify
        "Have her insult you":
            add tags 'insulted_you_before' 'insulting_you' to dee
            wt_image daughter_house_1_15
            dee.c "Seriously?  You have a tight young body like mine to fuck and you need insults to get you off?"
            wt_image daughter_house_1_42
            dee.c "That's fucking pathetic.  You can't keep this little limp dick of yours hard without me reminding you of what a loser you are?"
            wt_image daughter_house_1_15
            dee.c "Come on, old man.  Pick up the pace.  The guys at my college dick me three times as good as this."
            wt_image daughter_house_1_34
            dee.c "Jesus fuck, do you even know what to do with that thing?  I said go faster, loser.  Fuck me like you like girls, assuming you even do."
            wt_image daughter_house_1_11
            "As her words excite you, you fuck her harder and harder.  She finds her body responding, and that encourages her to continue with growing enthusiasm."
            dee.c "God you're pathetic.  A real man would have made me cum three times by now.  Just finish up loser and dribble your little seed into me so I can go find a proper college bull to breed me."
            $ title = "What do you?"
            menu:
                "Finish up":
                    wt_image daughter_house_1_37
                    dee.c "Ohh ... is that all you've got?  Quit fumbling around down there and squirt out your little jizz into me already!"
                "Hold off and see if she'll cum":
                    wt_image daughter_house_1_37
                    dee.c "Ohh ... is that all you've got?  Quit fumbling around down there and squirt out your little jizz into me already!"
                    wt_image daughter_house_1_11
                    dee.c "Oh fuck ... are you still going?  What's wrong, loser?  Can't get off even when you have a sexy young goddess to fuck?"
                    wt_image daughter_house_1_36
                    dee.c "Oh my God!  Oh!!  Oh fuck I'm going to cum again!!!"
                    wt_image daughter_house_1_35
                    dee.c "Ohhh FUCCKKKK!!!!"
                    "As she spasms around your cock, you can't help but let yourself go."
                    $ dee.orgasm_count += 1
            wt_image daughter_house_1_38
            player.c "[player.orgasm_text]"
            wt_image daughter_house_1_28
            dee.c "Shit, that was fun!  I loved seeing how excited you got when I insulted you.  I think I like this side of you."
            wt_image daughter_house_1_29
            dee.c "Hang on.  When Mom comes over, there's no way she does that with you.  She wouldn't have it in her."
            player.c "Probably not, no.  But I like that you do."
            wt_image daughter_house_1_40
            if dee.has_tag('will_fuck_better_than_mom'):
                dee.c "So I did fuck you better than Mom!  Not that there was any doubt about that.  Do you want to lick your spunk out of my pussy before I go?"
            else:
                dee.c "And I like that you're in touch with your pathetic worm side.  Do you want to lick your spunk out of my pussy before I go?"
            menu:
                "Yes, please":
                    wt_image daughter_house_1_44
                    "She lies back and spreads her legs as you get on your knees ..."
                    wt_image daughter_house_1_45
                    "... and suck your own cum out of her just-fucked cunt."
                    wt_image daughter_house_1_41
                    dee.c "That was hot!  I guess it's time for me to go, but I'll definitely be back."
                "No":
                    wt_image daughter_house_1_27
                    dee.c "Too bad, that would have been hot to watch.  Well I guess my pussy and I are going away, at least for today.  I may come back sometime."
                "Never (shuts question off)":
                    add tags 'no_licking_spunk_from_her' to dee
                    wt_image daughter_house_1_27
                    dee.c "Too bad, that would have been hot to watch.  Well I guess my pussy and I are going away, at least for today.  I may come back sometime."
            $ dee.sex_count += 1
            orgasm notify
        "Have her insult herself":
            wt_image daughter_house_1_15
            dee.c "What?  I'm not going to do that!"
            if dee.has_tag('will_fuck_better_than_mom'):
                add tags 'insulted_herself_before' 'insulting_herself' to dee
                player.c "Really?  And here I thought you said you'd be a better fuck than your Mom."
                wt_image daughter_house_1_29
                dee.c "Wait?  Does Mom do that ..."
                wt_image daughter_house_1_42
                dee.c "No, don't tell me!  Just fuck my scrawny body."
                player.c "That's an okay start, but you can run yourself down more than that, can't you, you dumb cunt?"
                wt_image daughter_house_1_15
                dee.c "Yes, I can.  I'm just a dumb, skinny blonde.  Fuck me like the stupid slut I am."
                wt_image daughter_house_1_37
                "As her words excite you, you fuck her harder and harder.  She finds her body responding, and that encourages her to insult herself with growing enthusiasm."
                dee.c "Oh yeah.  Fuck some sense into this stupid slut!  Treat me like your scrawny, tiny-titted blonde whore."
                wt_image daughter_house_1_11
                dee.c "Fill me!  Fill this stupid cunt with your seed!!"
                $ title = "What do you?"
                menu:
                    "Oblige her":
                        wt_image daughter_house_1_15
                        player.c "Do you know what a stupid slut begging for a man's cum is?"
                        wt_image daughter_house_1_39
                        dee.c "A cum dump!  Use me as your scrawny, small titted blonde cum dump."
                    "Hold off and see if she'll cum":
                        wt_image daughter_house_1_15
                        player.c "I don't know.  A young whore like you, I don't think you're depraved enough to deserve my seed.  I think I'll go dump it in your mother instead."
                        wt_image daughter_house_1_12
                        dee.c "I am!  I'm such a stupid young cunt I want you use me as your cum dump, not Mom!"
                        wt_image daughter_house_1_37
                        dee.c "Please!!  Please, use me as your cum dump!  Fill this scrawny skank with your seed!"
                        wt_image daughter_house_1_36
                        dee.c "Oh my God!  Oh!!  Oh fuck I'm going to cum again!!!"
                        wt_image daughter_house_1_35
                        dee.c "Ohhh FUCCKKKK!!!!"
                        "As she spasms around your cock, you can't help but let yourself go."
                        $ dee.orgasm_count += 1
                wt_image daughter_house_1_38
                player.c "[player.orgasm_text]"
                wt_image daughter_house_1_29
                "When you finish pumping your load into her, she looks at you with a combination of bewilderment and mortification."
                player.c "You okay, kid?"
                wt_image daughter_house_1_41
                dee.c "Yeah, I guess.  It's just ... "
                player.c "Relax.  It was just sex.  Kinky sex.  Hot, too, wasn't it?"
                wt_image daughter_house_1_40
                dee.c "Very!  But just to set the record straight, I'm not a cunt, a slut or a whore.  I don't care what I just said."
                player.c "Not a cunt, slut or whore.  Got it.  Just a scrawny blonde cum dump, then, I guess?"
                wt_image daughter_house_1_28
                "She punches you playfully on the arm."
                dee.c "Stop it!  Don't call me that, either.  Not unless you're fucking me silly while you're doing it."
                $ dee.sex_count += 1
                orgasm notify
            else:
                jump menu_dee_first_sex_menu
        "Just fuck her":
            wt_image daughter_house_1_12
            player.c "Just lie back and look sexy, [dee.name]."
            wt_image daughter_house_1_37
            "That's easy for her to do ..."
            wt_image daughter_house_1_11
            "... just like cumming inside her tight cunt is easy for you."
            wt_image daughter_house_1_38
            player.c "[player.orgasm_text]"
            if dee.has_tag('will_fuck_better_than_mom'):
                wt_image daughter_house_1_42
                dee.c "I bet my tight, young pussy felt better around your cock than Mom's."
                wt_image daughter_house_1_29
                player.c "You might be surprised.  But I did enjoy that, yes."
            else:
                wt_image daughter_house_1_41
                dee.c "Was that okay?  I mean, I'm pretty sure it was, but - that was good for you, right?"
                player.c "Yes, [dee.name].  I enjoyed that."
            wt_image daughter_house_1_28
            dee.c "Good.  I enjoyed that, too.  I guess I'd better be going, though."
            $ dee.sex_count += 1
            orgasm notify
        "Stop there and have her go home":
            player.c "That's okay, kid.  I'm glad you had fun."
            if dee.has_tag('will_fuck_better_than_mom'):
                wt_image daughter_house_1_29
                dee.c "Wait, does that mean Mom was ..."
                wt_image daughter_house_1_40
                dee.c "I'm sorry I came so quickly, but give me another chance.  Put your cock back in my pussy and I promise I'll make it feel good."
                player.c "Maybe another time, kid.  Don't worry, I'm sure you can get as good at sex as your mother is, once you've had some practice."
            else:
                wt_image daughter_house_1_41
                dee.c "Yeah, but I don't want to seem ungrateful.  I know women do it all the time, getting a man off without expecting an orgasm in return, so I know it's all right if I'm the only one who came.  I just don't want to perpetuate an imbalanced power relationship even if I was the one to garner the benefits."
                player.c "That was an awful lot of words when you could have just said it'll be my turn next time."
    $ dee.orgasm_count += 1
    add tags 'sex_before' to dee
    return

# Domination Actions
label dee_dominate_her:
    add tags 'talked_domination_today' to dee
    if dee.dom_discussion_count == 1:
        player.c "Ready to visit my dungeon?"
        wt_image daughter_house_1_2
        dee.c "I already told you 'no', before."
        if dee.marilyn_event_status > 1:
            player.c "And you haven't reconsidered?  Not even after your experience with Marilyn?"
            wt_image daughter_house_1_24
            dee.c "What does Marilyn have to do with it?"
            player.c "You remember how she made you feel. 'Putty in her hands' were your words.  You're not naturally submissive, but you were with her, and you liked it.  I can help you recapture that feeling.  Who knows?  There may be a whole new side of your sexuality you'd enjoy exploring."
            wt_image daughter_house_1_22
            dee.c "And you're volunteering to help me experience it?  How generous of you.  I can guess what you're hoping to get out of that, but what would I get out of it?"
            if dee.talk_sex_life_status > 2:
                player.c "A good time, better than you're expecting.  A learning experience, too.  If you're not sure you want to explore your submissive side, what about using it as a way to explore your dominant side.  You'd like to be able to make people feel what Marilyn made you feel, wouldn't you?  Your RA, for example?"
            else:
                player.c "A good time, better than you're expecting.  A learning experience, too.  If you're not sure you want to explore your submissive side, what about using it as a way to explore your dominant side.  You'd like to be able to make people feel what Marilyn made you feel, wouldn't you?"
            wt_image daughter_house_1_2
            dee.c "You could teach me to take control of others as easily as Marilyn took control of me?  Even though I'm not a powerful woman like she is?"
            player.c "You'll teach yourself, I'll just be the role model.  The more experiences you have as a submissive, the better you'll understand how the person you're trying to control is feeling."
            wt_image daughter_house_1_1
            player.c "I can see you're not ready to say 'yes' right now, but think about it.  There's no need to rush, we can do this when you're ready."
            $ dee.dom_discussion_count = 2
    # note: can never get here while dom_discussion_count == 2
    # first domination session
    elif dee.dom_discussion_count == 3:
        if not current_location == dungeon:
            call forced_movement(dungeon) from _call_forced_movement_1004
            wt_image daughter_dungeon_1_1
            "You lead [dee.name] into your dungeon and instruct her to undress."
        else:
            wt_image daughter_dungeon_1_1
            player.c "Undress"
        wt_image daughter_dungeon_1_2
        "She strips down to her underwear as she looks around, seemingly more curious than nervous."
        $ dungeon.added_submission = dungeon.added_by_items('submission_mod')
        if dungeon.added_submission >= 30:
            dee.c "Wow, this is an elaborate set up."
        elif dungeon.added_submission >= 15:
            dee.c "You have quite a bit of stuff in here."
        elif dungeon.added_submission >= 5:
            dee.c "There's not much in here."
        else:
            dee.c "This is just an empty room."
        wt_image daughter_dungeon_1_3
        if dungeon.added_submission >= 15:
            player.c "If you're lucky, I'll show you how I use everything in here someday, but for today we're keeping things simple.  Give me your hands."
        else:
            player.c "It has everything we need for today.  Give me your hands."
        wt_image daughter_dungeon_1_4
        dee.c "I've never seen anyone tie a knot like that before."
        wt_image daughter_dungeon_1_5
        player.c "You really don't have any experience with proper BDSM, do you?  This is a very simple technique, easy to tie, but safe and secure."
        wt_image daughter_dungeon_1_6
        dee.c "I like the safe part."
        wt_image daughter_dungeon_1_7
        player.c "You'll come to appreciate the secure part, too, pretty soon."
        wt_image daughter_dungeon_1_8
        dee.c "That sounds ominous.  Is this how you dominate someone, put them in a scary situation where they're helpless?"
        wt_image daughter_dungeon_1_9
        player.c "It's one way, yes, but mostly what we're doing is changing the power dynamics between us and getting out of our normal, everyday routine.  Tying you up is just one method of transferring power from you to me.  There are others."
        wt_image daughter_dungeon_1_10
        player.c "Taking away your sight, for example, reinforces your sense of helplessness, doesn't it?"
        wt_image daughter_dungeon_1_11
        dee.c "Oh shit, does it ever!"
        wt_image daughter_dungeon_1_12
        player.c "And leaving you unable to close your legs leaves you feeling both physically and mentally open to me."
        wt_image daughter_dungeon_1_13
        dee.c "I guess that's a good way to describe how I'm feeling.  Thank you, by the way, for letting me keep my underwear on.  I wasn't sure you would."
        wt_image daughter_dungeon_1_14
        player.c "That's cute.  Do you really think I'm not going to strip you naked, now that I have you tied up."
        wt_image daughter_dungeon_1_15
        dee.c "I guess not."
        wt_image daughter_dungeon_1_16
        player.c "Definitely not.  But here's a more difficult question.  Do I have your permission to touch you?"
        dee.c "I ... I guess I assumed that went along with agreeing to allow you to dominate me."
        wt_image daughter_dungeon_1_17
        player.c "Good, but it's always better to confirm.  Besides, it feels different, re-confirming your consent once you're tied up, doesn't it?"
        dee.c "Yes.  I feel ... smaller, somehow."
        wt_image daughter_dungeon_1_18
        player.c "It feels different, too, having your tit squeezed when you can't bring your hands down to push mine away."
        dee.c "Ohhh ... yes."
        wt_image daughter_dungeon_1_19
        player.c "You've had lovers pinch your nipples before, but I bet the pain has never felt as intense as now, knowing you can't control how long or hard I pinch them."
        dee.c "Oww!!!  Ohhh ... yes, this feels more intense."
        wt_image daughter_dungeon_1_17
        player.c "And how about this?  Is this more intense, too?"
        wt_image daughter_dungeon_1_20
        "Taking her now sore nipple between your lips, you suckle it gently as she gasps from the unexpectedly pleasant sensation."
        wt_image daughter_dungeon_1_21
        dee.c "Oohhhh ... that does feel surprisingly good!"
        wt_image daughter_dungeon_1_16
        player.c "You're going to enjoy the next part, too.  I'm going to spank you."
        wt_image daughter_dungeon_1_17
        dee.c "I don't think I'll enjoy being spanked."
        player.c "Tell you what, I'm going to check to see how wet you are now and then I'll check again after I spank you.  If you don't want me to be able to keep constant tabs on how wet you are, you could always try closing your legs."
        wt_image daughter_dungeon_1_22
        "She lets out a moan at the touch of your fingers, a combination of arousal, embarrassment at being aroused, and both embarrassment and arousal from being helpless to prevent you from checking between her legs whenever you want."
        dee.c "Ooohhhh"
        player.c "Reasonably wet, but you're going to be a lot wetter when I'm finished spanking you."
        wt_image daughter_dungeon_1_23
        "You make it a 'good girl' spanking - hard enough to sting, but with plenty of attention to the sensitive undersides of her buttocks and more than a few slaps that finish with your fingers making contact with her sex ... *smack*  *smack*  *smack*  *smack*  *smack*"
        dee.c "Ow!  Ohh!  OW!!  Ow, ohhh!!!"
        wt_image daughter_dungeon_1_24
        "You don't stop until she's breathing hard and her butt has turned a pleasing shade of red."
        player.c "What am I going to find when I touch your pussy, [dee.name]?"
        wt_image daughter_dungeon_1_25
        dee.c "Ooohhhh ... I'm wetter now.  I didn't like being spanked, I swear I didn't!  It hurt!  But the way you did it was so sensual, and being tied like this, unable to protect my sore ass as you spanked it, it turned me on even though I didn't want it to."
        if dungeon.has_item(floggers):
            $ title = "Flog her tits now?"
            menu:
                "Yes, give her the full experience":
                    wt_image daughter_dungeon_1_26
                    if dungeon.added_submission >= 15:
                        player.c "I said I wasn't going to show you everything I have in here today, but there is one item I'd like you to experience.  Turn around."
                    else:
                        player.c "I know you think there's not much in my dungeon, but there is one item I'd like you to experience.  Turn around."
                    wt_image daughter_dungeon_1_27
                    "With the blindfold on, she can't see what you have in your hand, but as she finishes turning slowly in her bonds to face you, she feels it as you crack the flogger across her exposed breasts ... *thwappp*"
                    wt_image daughter_dungeon_1_28
                    dee.c "Ow!  What is that??"
                    wt_image daughter_dungeon_1_27
                    player.c "A flogger.  Do you like it?"
                    "*thwappp*"
                    wt_image daughter_dungeon_1_28
                    dee.c "Ow!  No!!"
                    wt_image daughter_dungeon_1_27
                    player.c "Are you sure?  Your nipples look hard."
                    "*thwappp*"
                    wt_image daughter_dungeon_1_28
                    dee.c "Ow!  No!  Yes?  Maybe?  I'm not sure."
                    wt_image daughter_dungeon_1_27
                    player.c "Do you really not know or are you just not listening to what your body is telling you?  I think this is turning you on.  Don't you agree?"
                    "*thwapp"
                    wt_image daughter_dungeon_1_28
                    dee.c "Oohhh!  Yes, you're right!  I'm not sure why, but yes, this is turning me on!"
                    $ title = "What now?"
                    menu menu_dee_dungeon_visit_1_flog_menu:
                        "Flog her again":
                            wt_image daughter_dungeon_1_27
                            "*thwapp"
                            wt_image daughter_dungeon_1_28
                            dee.c "Oohhh!!"
                            jump menu_dee_dungeon_visit_1_flog_menu
                        "Spank her pussy, now":
                            pass
                "No, go straight to spanking her pussy":
                    pass
        wt_image daughter_dungeon_1_22
        player.c "You're so wet you're dripping.  Do you think I could make you cum now, [dee.name], just by spanking you?"
        wt_image daughter_dungeon_1_16
        dee.c "No.  I'm turned on, but spanking my ass isn't going to make me cum, no matter how sensual your spankings are."
        wt_image daughter_dungeon_1_17
        player.c "Oh, but I didn't say I was going to make you cum by spanking your ass."
        wt_image daughter_dungeon_1_29
        "You bring your hand down sharply on her sex, making sure that most of the force reverberates directly on her clit."
        wt_image daughter_dungeon_1_30
        dee.c "Oww!!"
        player.c "That's hot isn't it?"
        wt_image daughter_dungeon_1_29
        "*smack*"
        wt_image daughter_dungeon_1_30
        dee.c "Oww!!  No, it's scary!"
        player.c "Yes, and ...?"
        wt_image daughter_dungeon_1_29
        "*smack*"
        wt_image daughter_dungeon_1_30
        dee.c "Oww!!  And painful!"
        player.c "Yes, and ...?"
        wt_image daughter_dungeon_1_29
        "*smack*"
        wt_image daughter_dungeon_1_30
        dee.c "And ... Ohhh FUCCKKK!!!"
        wt_image daughter_dungeon_1_17
        player.c "And what else, [dee.name]?"
        wt_image daughter_dungeon_1_16
        dee.c "Hot.  Being spanked on my pussy until I came was hot.  Scary and painful and hot."
        wt_image daughter_dungeon_talk_1
        if dee.has_tag('help_her_turn_tables_ra'):
            dee.c "That was ... interesting.  I'm not sure it really helps me turn the tables on [dee_ra.name], though.  She's not going to agree to join me in your dungeon and in any event hers and Marilyn's form of domination is more natural, not ropes and chains stuff.  That's more what I'm interested in."
        else:
            dee.c "That was ... interesting.  I'm not sure it really helps me take control of other women the way Marilyn controlled me, though.  Her form of domination was more natural, not ropes and chains stuff.  That's more what I'm interested in.."
        player.c "Right now I'm trying to broaden the experiences you've had as a submissive.  The more situations you've been in, the better you'll understand how the person you're trying to control is feeling.  I must warn you, though, the next time what I put you through will be much more intense."
        wt_image daughter_dungeon_talk_2
        dee.c "Next time?"
        wt_image daughter_dungeon_talk_3
        player.c "If you want to learn what I have to teach you, there'll need to be a next time."
        wt_image daughter_dungeon_talk_4
        if dee.has_tag('help_her_turn_tables_ra'):
            dee.c "Well, I didn't think a woman could cum from having her pussy spanked - any woman, let alone me - so I guess I could put up with something more intense to learn what else you can teach me.  I'll try to make myself available more often.  I'm anxious to learn how to turn the tables on [dee_ra.name]."
        else:
            dee.c "Well, I didn't think a woman could cum from having her pussy spanked - any woman, let alone me - so I guess I could put up with something more intense to learn what else you can teach me."
        $ dee.orgasm_count += 1
        change player energy by -energy_long notify
        $ dee.dom_discussion_count = 4
        call forced_movement(living_room) from _call_forced_movement_1005
        call dee_visit_end from _call_dee_visit_end_11
    # second domination session
    elif dee.dom_discussion_count == 4:
        if not current_location == dungeon:
            call forced_movement(dungeon) from _call_forced_movement_1006
        wt_image daughter_dungeon_1_1
        player.c "Am I going to be tied up again?"
        wt_image daughter_dungeon_1_2
        player.c "Yes, and there's no need for modesty.  Remove your underwear then give me your hands."
        wt_image daughter_dungeon_2_1
        player.c "The anticipation of being tied up again is making you wet, isn't it?"
        wt_image daughter_dungeon_2_2
        dee.c "No, just nervous.  Why are you wearing a mask?"
        wt_image daughter_dungeon_2_10
        player.c "Because I'm not going to blindfold you today.  I want you to see what's happening to you, but I don't want you to be distracted by this being 'me' doing this to you.  It could be any dominant man - or woman, if your imagination is strong enough."
        wt_image daughter_dungeon_2_4
        dee.c "Wouldn't it be better to personalize the domination?"
        wt_image daughter_dungeon_2_3
        player.c "See?  I told you by putting you in the position of a sub, you'd teach yourself.  This wouldn't be as frightening if it was someone you know and trust doing it.  In fact, just by letting me tie you up, you find yourself trusting me more.  You must trust me to let me do this, therefore you do trust me more than you did.  It's a fun circle as long as the Dom doesn't mess it up."
        wt_image daughter_dungeon_2_11
        dee.c "What would mess it up?"
        wt_image daughter_dungeon_2_12
        player.c "Abusing that trust is an obvious way.  Less obvious is letting the sub lie and get away with it.  It makes her think she has power when what you want is for her to realize she's wholly dependent on you and needs to be completely honest with you."
        wt_image daughter_dungeon_2_5
        player.c "Why did you tell me you weren't getting wet when you clearly are?"
        wt_image daughter_dungeon_2_13
        dee.c "I didn't realize I was!  I swear!  All I felt was nervous.  I wasn't trying to lie to you."
        wt_image daughter_dungeon_2_6
        "*SMACK*"
        wt_image daughter_dungeon_2_7
        dee.c "OWW!"
        wt_image daughter_dungeon_2_14
        player.c "Okay, [dee.name].  I believe you.  But I can't let you inadvertently lie because you're not aware of what your body is doing.  Do you know why?"
        wt_image daughter_dungeon_2_6
        "*SMACK*"
        wt_image daughter_dungeon_2_7
        dee.c "OWW!  Why??"
        wt_image daughter_dungeon_2_12
        player.c "Because you should never let a sub be unaware of what her body's doing."
        wt_image daughter_dungeon_2_5
        player.c "When she's excited, it's a wasted chance to put her mind in tune with how her body's responding to being dominated.  Yours likes being tied up more than you expected.  Admit it."
        wt_image daughter_dungeon_2_13
        dee.c "Yes, my body is turned on.  I'm turned on."
        wt_image daughter_dungeon_2_12
        player.c "Good girl.  But there's a more important reason why I need to punish you for not being in tune with your body.  To keep you safe, I need you to be aware of what your body is feeling, so you can let me know if there's a problem, either with the bindings or the position I've put you in or anything else."
        wt_image daughter_dungeon_2_6
        "*SMACK*"
        wt_image daughter_dungeon_2_7
        dee.c "OWW!  I understand!  I'll pay closer attention to my body's reactions for you."
        wt_image daughter_dungeon_2_15
        player.c "Good girl.  Would you care to share how your body responds to my fingers penetrating you?"
        wt_image daughter_dungeon_2_8
        dee.c "Oohhhh ... it's gearing up to have an orgasm!"
        wt_image daughter_dungeon_2_9
        player.c "So quickly?  You really are a responsive minx.  Control yourself, you are not allowed to cum, I just want you soaking wet, it'll make what happens next more interesting."
        wt_image daughter_dungeon_2_16
        dee.c "Oohhhh, but ..."
        wt_image daughter_dungeon_2_17
        player.c "But nothing, that's enough back talk.  My fingers are going away now and so is your voice."
        if dungeon.has_item(gags):
            wt_image daughter_dungeon_2_18
            "[dee.name] watches apprehensively as you select a ballgag to use on her."
            dee.c "How will I be able to tell you what my body's feeling if I can't talk?"
            player.c "A very good question.  You've been paying attention.  Shake your head vigorously from side to side or grunt three times if you need me to remove the gag.  Open wide."
            wt_image daughter_dungeon_2_19
            "You fasten the gag in place and buckle it behind her head."
        else:
            wt_image daughter_dungeon_2_14
            "[dee.name] watches apprehensively as you pick up the cloth you used to blindfold her last session and fold it until it will serve as a gag for her mouth."
            dee.c "How will I be able to tell you what my body's feeling if I can't talk?"
            player.c "A very good question.  You've been paying attention.  Shake your head vigorously from side to side or grunt three times if you need me to remove the gag.  Open wide."
            wt_image daughter_dungeon_2_20
            "You fasten the gag in place and tie it behind her head."
        if dungeon.has_item(floggers):
            $ title = "Flog her now?"
            menu:
                "Yes, redden her butt":
                    if dungeon.has_item(gags):
                        wt_image daughter_dungeon_2_21
                        player.c "You look very cute tied up and gagged, but you'll look even cuter with a red butt."
                        wt_image daughter_dungeon_2_22
                    else:
                        wt_image daughter_dungeon_2_22
                        player.c "You look very cute tied up and gagged, but you'll look even cuter with a red butt."
                    "*thwappp*  *thwappp*  *thwappp*"
                    if dungeon.has_item(gags):
                        wt_image daughter_dungeon_2_23
                    dee.c "nnnnnnn"
                    wt_image daughter_dungeon_2_24
                    "The increased blood flow shows up quickly on her pale skin.  Her ass is soon glowing a pleasing shade of red."
                    $ title = "What now?"
                    menu menu_dee_dungeon_visit_2_flog_menu:
                        "Flog her again":
                            wt_image daughter_dungeon_2_22
                            "*thwappp*"
                            if dungeon.has_item(gags):
                                wt_image daughter_dungeon_2_23
                            dee.c "nnnnnnn"
                            wt_image daughter_dungeon_2_24
                            jump menu_dee_dungeon_visit_2_flog_menu
                        "Move on the main event":
                            pass
                "No, move on to the main event":
                    pass
        wt_image daughter_dungeon_2_25
        player.c "This next part is going to be intense, as promised.  If you want to get as much out of it as you can, I want you to pay close attention and be honest with yourself about how you're feeling, mentally and physically."
        wt_image daughter_dungeon_2_26
        dee.c "NNNN??!!"
        wt_image daughter_dungeon_2_27
        player.c "Yes, I know, the rope is rough against your tender sex and scary once I tie it off like this."
        wt_image daughter_dungeon_2_28
        player.c "Do you see now why I wanted you good and wet before we got to this part?  The rope is uncomfortable now, but just think how uncomfortable it would be if your natural lubricants weren't protecting it?  Especially after I tighten the line."
        wt_image daughter_dungeon_2_29
        dee.c "NNNNNN!!!"
        wt_image daughter_dungeon_2_30
        player.c "I know, it feels like the rope is going to split you in two, but it won't.  What it will do is apply constant, intense pressure on your sex, especially your clit."
        wt_image daughter_dungeon_2_31
        player.c "You can keep trying to pull away, but it won't help.  There's not enough slack to relieve the prssure.  I recommend you lean into the experience - literally.  Some women would find that too intense, but I think you'll like it, if you let yourself."
        wt_image daughter_dungeon_2_29
        player.c "When you've had as much of this experience as you want, let me know and I'll let you sit down.  If I were you, I'd give yourself an orgasm first, but it's up to you."
        wt_image daughter_dungeon_2_32
        "You watch as she experiments in her bonds, alternating between trying to alleviate and intensify the sensation between her legs.  After a few minutes, she's had enough and grunts three times into her gag."
        dee.c "nnnhh - nnnhh - nnnhh"
        wt_image daughter_dungeon_2_33
        player.c "Not ready to let yourself cum?  Okay, let's get you down so you can have a seat, as promised."
        wt_image daughter_dungeon_2_34
        "She's so focussed on the flood of relief from no longer feeling the pressure between her legs, she seems barely to notice or care about you tying her to the chair ..."
        wt_image daughter_dungeon_2_35
        "... until you begin tightening the crotch rope again."
        wt_image daughter_dungeon_2_36
        dee.c "NNNN??!!"
        wt_image daughter_dungeon_2_37
        player.c "You're a stubborn young woman, [dee.name], refusing to accept what your body wants.  Giving you the freedom to adjust the intensity of the sensation between your legs was a mistake.  You'll have no such freedom in this position."
        wt_image daughter_dungeon_2_38
        "She groans as you tighten the rope, the pressure lifting her off the chair."
        dee.c "NNNNNN!!"
        wt_image daughter_dungeon_2_39
        player.c "Forget the fear, forget the pain, [dee.name].  Focus on how hard your clit is, on how hard your nipples are.  Maybe this would be easier if I drew more of your attention to your nipples."
        wt_image daughter_dungeon_2_40
        "You wind some twine around her right nipple ..."
        wt_image daughter_dungeon_2_41
        "... then the left ..."
        wt_image daughter_dungeon_2_42
        "... then pull them both taut."
        wt_image daughter_dungeon_2_43
        player.c "You'd like me to untie you, wouldn't you?"
        wt_image daughter_dungeon_2_44
        "She nods her head emphatically, then grits her teeth as even this amount of motion increases the pressure on her sex and breasts."
        player.c "Good girl.  Then all you need to do is cum and I'll let you go."
        wt_image daughter_dungeon_2_45
        "Her head slumps back.  Likely she can't believe she can cum in this position, but you suspect she can, if she lets herself slip into the right headspace."
        wt_image daughter_dungeon_2_46
        "After a few minutes, she proves you right.  Despite the pain and discomfort, her body tenses up as you watch ..."
        wt_image daughter_dungeon_2_47
        "... and she screams an orgasm into her gag."
        wt_image daughter_dungeon_2_48
        dee.c "nnnn NNNNNNN!!!"
        wt_image daughter_dungeon_2_43
        player.c "Good girl.  Would you like me to untie you now?"
        wt_image daughter_dungeon_2_34
        "She nods meekly as you remove the twine from around her nipples, release the pressure on her crotch rope, and untie her from her chair."
        wt_image daughter_dungeon_talk_1
        "Once her bonds are removed, you wait silently until she's recovered enough to speak."
        dee.c "You undersold it when you said this would be intense."
        wt_image daughter_dungeon_talk_4
        dee.c "At times I hated you, and at other times I was willing to do anything you wanted if you'd only take the pain away."
        wt_image daughter_dungeon_talk_3
        dee.c "What surprised me most was how fluid the border between pain and pleasure was.  Even when I was fighting it - you told me not to, but I couldn't help myself - I was aware that the pain was turning me on and I kind of hated myself and you for that, because I don't want to be a masochist and I don't want you trying to turn me into one."
        wt_image daughter_dungeon_talk_2
        player.c "I don't think that would be possible, either you enjoy pain or you don't.  What you were feeling wasn't pure pain, though.  It was sensual pain, intended to both arouse you, much the same was as spanking your pussy, but leaving you feeling even more helpless and controlled."
        wt_image daughter_dungeon_talk_1
        dee.c "Well, in that you succeeded.  I think I get why being dominated can be such a rush for a submissive person. Everything was about you.  What are you going to do to me next, how long are you going to leave me here, what can I do to make you happy so you'll take that damn rope away?  My whole world was reduced to you."
        wt_image daughter_dungeon_talk_3
        if dee.has_tag('help_her_turn_tables_ra'):
            dee.c "I don't think it really helped me understand how to turn the tables on [dee_ra.name], though.  She's not going to agree to join me in your dungeon and in any event hers and Marilyn's form of domination is more natural, not ropes and chains stuff.  That's more what I'm interested in."
        else:
            dee.c "I don't think it really helped me understand how to take control of other women the way Marilyn controlled me, though.  Her form of domination was more natural, not ropes and chains stuff.  That's more what I'm interested in.."
        wt_image daughter_dungeon_talk_2
        player.c "Like I told you last time, I'm trying to broaden the experiences you've had as a submissive.  How you want to control someone is less important than understanding how you need to behave in order to control them.  For that, you need to understand what's in their head at least as much, if not more, than what's in yours."
        wt_image daughter_dungeon_talk_1
        dee.c "And if I want to control them with words alone, how do I tell what they're feeling?  Or know what I need to say or how I need to say it to convince them to submit to me?"
        player.c "Patience.  You'll spend the next few days thinking about and learning more about your experience today, including things that are applicable to all forms of domination.  You'll learn even more from our next session."
        wt_image daughter_dungeon_talk_3
        dee.c "So I have to submit to you again?"
        player.c "You don't have to, you want to."
        wt_image daughter_dungeon_talk_2
        dee.c "Only to continue to learn from you.  I don't want you to get the wrong idea."
        player.c "Relax, tiger cub.  I get it.  You're a dominant personality.  I'm not trying to turn you into something you're not."
        wt_image daughter_dungeon_talk_3
        dee.c "Okay, good.  Then in that case, I'm looking forward to learning more from you about how to control women."
        player.c "By being a good girl and doing everything I tell you to."
        wt_image daughter_dungeon_talk_1
        dee.c "Yeah, yeah, by being a good girl and doing everything you tell me to.  Don't rub it in!"
        $ dee.dom_discussion_count = 5
        call forced_movement(living_room) from _call_forced_movement_1007
        call dee_visit_end from _call_dee_visit_end_12
    # third domination session
    elif dee.dom_discussion_count == 5:
        if not current_location == dungeon:
            call forced_movement(dungeon) from _call_forced_movement_1008
        wt_image daughter_dungeon_3_1
        player.c "Get naked for me, good girl."
        wt_image daughter_dungeon_3_2
        dee.c "Good girl?  Is that how you plan to address me now?"
        wt_image daughter_dungeon_3_3
        "You bring your hand down on her bottom, more playfully than viciously ... *smack*"
        player.c "Unless I hear back talk or you disobey me, in which case you'll wish I was still calling you 'good girl'.  Hand me your panties and kneel down."
        wt_image daughter_dungeon_3_4
        dee.c "I didn't take you for a panty-collector.  Actually, I kind of did.  Took you a while to decide to collect mine, though.  What changed?"
        wt_image daughter_dungeon_3_5
        "She hands you her panties then kneels down, letting you push them into her mouth."
        player.c "You wanted to learn how to control women.  Here's an easy way to shut up one who's trying to hide her nervousness by talking smart."
        wt_image daughter_dungeon_3_6
        player.c "Feeling more obedient, aren't you?  As soon as you decided not to spit those panties out, you made a choice to let me humiliate and control you.  That means your brain is already preparing itself for what I might ask you to do next, isn't it?"
        "She nods gently."
        wt_image daughter_dungeon_3_5
        player.c "Each small act of submission prepares you for another, deeper step.  If I told you when you arrived at my house today that you'd be crawling naked for me with your panties in your mouth, it would have been difficult for your brain to imagine or accept that.  It's much easier to picture yourself crawling for me now, isn't it?  Even though it's still not something you want to do."
        "She hesitates slightly before nodding gently again."
        wt_image daughter_dungeon_3_6
        player.c "Here's a trick.  Make the acts of submission seem as normal as possible.  I look at you and I see you exactly where you should be, doing exactly what you should be doing.  You can see that in my face, don't you?"
        "She nods again."
        wt_image daughter_dungeon_3_5
        player.c "And when you crawl across the floor to pick up the ropes on the other side of the room and bring them back to me, that's going to be normal as well.  A natural extension of you kneeling obediently at my feet."
        wt_image daughter_dungeon_3_6
        player.c "Here's another trick.  Letting your submissive know in advance what's going to happen helps to make it seem normal when it happens.  Surprises are good sometimes, but when convincing someone to give up control, it's usually better to give their brain time to acclimatize to the idea.  For example, after you crawl over to those ropes and bring them back to me, I'm going to tie you with them, then take you across my lap and spank you."
        wt_image daughter_dungeon_3_5
        player.c "Final trick for today.  Giving the submissive some agency within the bounds of your control can be good for securing their obedience.  For example, how many times I spank you is going to be based on how long it takes you to crawl over to the ropes and bring them to me.  Too slow, and I increase the number of spanks.  Too fast, and I increase them as well.  I want time to enjoy watching you crawl, but I don't want you to procastinate."
        wt_image daughter_dungeon_3_6
        player.c "You can see what that's doing to your head, can't you?  If I'd pushed you too far, you'd get up and leave, but I've been watching your face and you're now ready for this.  There's no longer any question about whether you'll crawl over and get the ropes for me, the only question is whether you please or disappoint me by crawling at the correct pace.  Sixty seconds, that's how long I want you to take, starting now."
        wt_image daughter_dungeon_3_7
        "With only the slightest hesitation, [dee.name] turns and heads towards the ropes."
        wt_image daughter_dungeon_3_8
        "She crawls at a slow, steady pace, no doubt trying to count the seconds off in her head."
        wt_image daughter_dungeon_3_9
        player.c "You can drop the panties now and carry one of the ropes back in your mouth."
        wt_image daughter_dungeon_3_8
        "Obediently she does, crawling a little faster on the way back, presumably because collecting the ropes took longer than she had budgetted for in her mental clock."
        wt_image daughter_dungeon_3_10
        "When she reaches you, you stand her up and begin tying her.  The look on her face tells you she's struggling to hold something back."
        player.c "You clearly have something you want to say, so out with it."
        dee.c "How did I do?"
        wt_image daughter_dungeon_3_11
        player.c "Competitive women make such great submissives.  Tell me, are you asking because you're worried about how many extra spanks you earned or do you just want to know how well you did at the task I gave you?"
        dee.c "Both?"
        wt_image daughter_dungeon_3_12
        player.c "You did extremely well.  You took 55 seconds, so you earned 5 extra spanks for getting back too soon, but I'm pleased with your performance.  Most women would have been off by more."
        wt_image daughter_dungeon_3_11
        dee.c "Shoot!  I rushed at the end.  I thought I was running out of time, but I wasn't."
        player.c "And that's why competitive women make such good subs.  You're happy to receive my praise, you're probably surprised yourself at how good my praising you made you feel.  But you're also disappointed because you wanted to do even better.  If I brought another sub out here now and made it a competition as to who could suck my cock best, you'd go all out to win it, wouldn't you?"
        wt_image daughter_dungeon_3_13
        "She laughs, a combination of nervous energy and genuine amusement at herself."
        dee.c "I'm not going to answer that because I really don't want to find myself in that competition.  But I will admit that I was surprised at how good it felt when you praised me, even though I was mad at myself for not doing better."
        if dungeon.has_item(gags):
            wt_image daughter_dungeon_3_14
            player.c "Understandable, but I'm sure you understand that if you're not going to answer my questions fully and openly, I'm going to take away your voice until you're feeling more submissive and compliant.  I will, however, put your mind at ease regarding having failed at my test."
        wt_image daughter_dungeon_3_15
        player.c "One of the great things about being a sub is that you never need to dwell on what you could have done better.  Transgressions are punished and then forgotten.  Just make sure that any punishments you give come with complete absolution.  If you expect your sub to accept your punishments willingly, you must truly forgive her afterwards and never ever use it against her again later."
        wt_image daughter_dungeon_3_16
        if dungeon.has_item(gags):
            player.c "When you're ready to earn my forgiveness, lie across my lap."
            wt_image daughter_dungeon_3_17
            "With only a slight hesitation born out of nervousness, she puts herself across your lap.  She finds it a little awkward with her hands and arms bound behind her back, but eventually she gets herself into proper position."
            player.c "Fifteen spanks.  Ten that you were going to get, anyway, just because I felt like giving them to you, then five hard ones at the end, as punishment for not completing my task properly."
            wt_image daughter_dungeon_3_18
            "The first 10 spanks are firm but sensual, stimulating the sensitive underside of her buttocks and reverberating directly into her pussy, leaving her moaning into her gag more in arousal than pain ...  *smack*  *smack*  *smack*  *smack*  *smack*  *smack*  *smack*  *smack*  *smack*  *smack*"
            wt_image daughter_dungeon_3_19
            dee.c "nnnnnnn"
            wt_image daughter_dungeon_3_20
            player.c "You like that.  You remember from our first session how arousing a spanking can be for a good girl who obeys me.  You won't like the next part so much.  This is for failing at my task."
            wt_image daughter_dungeon_3_21
            "It's only five swats, but you make them hard ones.  By the time they're over, her ass is a flaming red and she's screaming into her gag ... *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*"
            wt_image daughter_dungeon_3_22
            dee.c "NNN!  NNN!  NNNNNN!!!"
            wt_image daughter_dungeon_3_20
            player.c "It's okay, [dee.name].  Punishment's over.  I know that was painful, but you took it very well.  I'm going to reward you now, for being such a good girl."
            wt_image daughter_dungeon_3_23
            "Carefully moving her off your lap, you lay her face down beside you ..."
            wt_image daughter_dungeon_3_24
            "... and increase her helplessness by winding a rope around her feet ..."
            wt_image daughter_dungeon_3_25
            "... leaving her fully hog-tied and immobilized."
            wt_image daughter_dungeon_3_26
            "Then you place your hand between her bound legs and begin finger-fucking her."
            wt_image daughter_dungeon_3_27
            player.c "That feels nice, doesn't it?  Even better than the 'good girl spanking'."
            wt_image daughter_dungeon_3_28
            dee.c "nnnnnnn"
            wt_image daughter_dungeon_3_29
            player.c "Ah right, your gag.  You don't need that anymore.  I want to hear you when you cum, a nice loud scream so I know how much you enjoy being tied up by me.  You are going to cum loudly for me, aren't you, good girl?"
        else:
            player.c "When you're ready to earn my forgiveness, lie down."
            wt_image daughter_dungeon_3_23
            "With only a slight hesitation born out of nervousness, she stretches out beside you."
            wt_image daughter_dungeon_3_24
            "You increase her helplessness by winding a rope around her feet ..."
            wt_image daughter_dungeon_3_25
            "... leaving her fully hog-tied and immobilized."
            wt_image daughter_dungeon_3_31
            player.c "Fifteen spanks.  Ten that you were going to get, anyway, just because I felt like giving them to you, then five hard ones at the end, as punishment for not completing my task properly."
            wt_image daughter_dungeon_3_32
            "The first 10 spanks are firm but sensual, stimulating the sensitive underside of her buttocks and reverberating directly into her pussy, leaving her moaning more in arousal than pain ...  *smack*  *smack*  *smack*  *smack*  *smack*  *smack*  *smack*  *smack*  *smack*  *smack*"
            wt_image daughter_dungeon_3_33
            dee.c "oooooo"
            wt_image daughter_dungeon_3_34
            player.c "You like that.  You remember from our first session how arousing a spanking can be for a good girl who obeys me.  You won't like the next part so much.  This is for failing at my task."
            wt_image daughter_dungeon_3_32
            "It's only five swats, but you make them hard ones.  By the time they're over, her ass is a flaming red and she's calling out in pain ... *SMACK*  *SMACK*  *SMACK*  *SMACK*  *SMACK*"
            wt_image daughter_dungeon_3_35
            dee.c "OWW!  OWW!  OOWWWW!!!"
            wt_image daughter_dungeon_3_36
            player.c "It's okay, [dee.name].  Punishment's over.  I know that was painful, but you took it very well.  I'm going to reward you now, for being such a good girl."
            wt_image daughter_dungeon_3_26
            "Placing your hand between her bound legs, you begin finger-fucking her."
            wt_image daughter_dungeon_3_27
            player.c "That feels nice, doesn't it?  Even better than the 'good girl spanking'."
            wt_image daughter_dungeon_3_33
            dee.c "oooohhhh ... yes"
            wt_image daughter_dungeon_3_34
            player.c "I want to hear you when you cum, a nice loud scream so I know how much you enjoy being tied up by me.  You are going to cum loudly for me, aren't you, good girl?"
        wt_image daughter_dungeon_3_30
        dee.c "ooohhhh ... if you keep doing that with your fingers, yes!"
        wt_image daughter_dungeon_3_37
        "You do indeed keep thrusting your fingers in and out of her as the orgasm builds inside her ..."
        wt_image daughter_dungeon_3_38
        "... until it suddenly explodes out."
        dee.c "Ohhh FUCCKKK!!!"
        wt_image daughter_dungeon_3_39
        player.c "Good girl, you screamed nice and loud when you came.  No need for me to punish you with another hard spanking.  If you'd like another good girl spanking, though, you can have one now as a reward."
        wt_image daughter_dungeon_3_40
        dee.c "No, no more stimulation, please.  That's enough for today.  That was intense.  I need time to process."
        player.c "What's going through your head right now?"
        wt_image daughter_dungeon_3_41
        dee.c "A lot of things.  Aren't you going to untie me?"
        $ title = "Untie her to chat?"
        menu:
            "Yes":
                wt_image daughter_dungeon_talk_2
                dee.c "You've really conditioned me to go along with whatever you want me to do."
                player.c "That's what you wanted, wasn't it?  To learn how to control others?  I've shown you how I've taken control of you.  Have you taken any lessons from that?"
                wt_image daughter_dungeon_talk_3
                if dee.ready_for_mom > 2 and dee.has_tag('help_her_turn_tables_ra'):
                    dee.c "I think I will, from today's session in particular.  Thank you for the hints, by the way.  I think I'd be very comfortable with a woman who's naturally submissive, like Mom.  I'm not sure I could bring out the submissive tendencies in someone like [dee_ra.name], though."
                elif dee.ready_for_mom > 2:
                    dee.c "I think I will, from today's session in particular.  Thank you for the hints, by the way.  I think I'd be very comfortable with a woman who's naturally submissive, like Mom.  I'm not sure I could bring out the submissive tendencies in someone who's not already aware of them, though."
                elif dee.has_tag('help_her_turn_tables_ra'):
                    dee.c "I think I will, from today's session in particular.  Thank you for the hints, by the way.  I think I'd be very comfortable with a woman who's naturally submissive.  I'm not sure I could bring out the submissive tendencies in someone like [dee_ra.name], though."
                else:
                    dee.c "I think I will, from today's session in particular.  Thank you for the hints, by the way.  I think I'd be very comfortable with a woman who's naturally submissive.  I'm not sure I could bring out the submissive tendencies in someone who's not already aware of them, though."
                if dee.has_tag('help_her_turn_tables_ra'):
                    player.c "You're not going to be able to bring out submissive tendencies in everyone, I hope you realize that?  Some people just aren't going to respond to being dominated, no matter what approach you take.  Your RA, though, I'm pretty sure you can handle."
                else:
                    player.c "You're not going to be able to bring out submissive tendencies in everyone, I hope you realize that?  Some people just aren't going to respond to being dominated, no matter what approach you take.  With more experience, though, you should become better able to assess who is and who isn't open to giving up control to you."
                wt_image daughter_dungeon_talk_1
                dee.c "Will you continue to help me with that?"
                wt_image daughter_dungeon_talk_2
                player.c "Are you asking me to continue to training you?  You know I normally charge money for that.  If you expect to continue to get lessons from me, you'd best ask politely."
                wt_image daughter_dungeon_talk_3
                "She takes a deep breath before replying."
                wt_image daughter_dungeon_talk_4
                dee.c "Please, Sir, will you continue training me?"
                wt_image daughter_dungeon_talk_2
                player.c "We'll see.  Continue to make yourself available to me and if I'm in the mood and think that you'll be a good girl for me, I'll take you back to my dungeon and give you more lessons."
                wt_image daughter_dungeon_talk_1
                dee.c "Thank you, Sir.  I'll be a good girl for you, I promise.  I'm going to head home now, I have a lot to think about."
            "No, chat with her like this":
                wt_image daughter_dungeon_3_40
                player.c "I enjoy seeing you tied up.  Relax and gather your thoughts.  We'll chat when you're ready, no rush."
                wt_image daughter_dungeon_3_42
                "She nods and rests quietly for a few minutes while you enjoy the view."
                wt_image daughter_dungeon_3_43
                dee.c "You've really conditioned me to accept your orders.  I'm lying naked and tied up while we're chatting and I'm not even fighting it."
                player.c "That's what you wanted, wasn't it?  To learn how to control others?  I've shown you how I've taken control of you.  Have you taken any lessons from that?"
                wt_image daughter_dungeon_3_41
                if dee.ready_for_mom > 2 and dee.has_tag('help_her_turn_tables_ra'):
                    dee.c "I think I will, from today's session in particular.  Thank you for the hints, by the way.  I think I'd be very comfortable with a woman who's naturally submissive, like Mom.  I'm not sure I could bring out the submissive tendencies in someone like [dee_ra.name], though."
                elif dee.ready_for_mom > 2:
                    dee.c "I think I will, from today's session in particular.  Thank you for the hints, by the way.  I think I'd be very comfortable with a woman who's naturally submissive, like Mom.  I'm not sure I could bring out the submissive tendencies in someone who's not already aware of them, though."
                elif dee.has_tag('help_her_turn_tables_ra'):
                    dee.c "I think I will, from today's session in particular.  Thank you for the hints, by the way.  I think I'd be very comfortable with a woman who's naturally submissive.  I'm not sure I could bring out the submissive tendencies in someone like [dee_ra.name], though."
                else:
                    dee.c "I think I will, from today's session in particular.  Thank you for the hints, by the way.  I think I'd be very comfortable with a woman who's naturally submissive.  I'm not sure I could bring out the submissive tendencies in someone who's not already aware of them, though."
                if dee.has_tag('help_her_turn_tables_ra'):
                    player.c "You're not going to be able to bring out submissive tendencies in everyone, I hope you realize that?  Some people just aren't going to respond to being dominated, no matter what approach you take.  Your RA, though, I'm pretty sure you can handle."
                else:
                    player.c "You're not going to be able to bring out submissive tendencies in everyone, I hope you realize that?  Some people just aren't going to respond to being dominated, no matter what approach you take.  With more experience, though, you should become better able to assess who is and who isn't open to giving up control to you."
                wt_image daughter_dungeon_3_43
                dee.c "Will you continue to help me with that?"
                wt_image daughter_dungeon_3_41
                player.c "Are you asking me to continue to training you?  You know I normally charge money for that.  If you expect to continue to get lessons from me, you'd best ask politely."
                wt_image daughter_dungeon_3_40
                "She takes a deep breath before replying."
                dee.c "Please, Sir, will you continue training me?"
                wt_image daughter_dungeon_3_39
                player.c "We'll see.  Continue to make yourself available to me and if I'm in the mood and think that you'll be a good girl for me, I'll take you back to my dungeon and give you more lessons."
                wt_image daughter_dungeon_3_43
                dee.c "Thank you, Sir.  I'll be a good girl for you, I promise.  May I please go home now, I have a lot to think about."
                wt_image daughter_dungeon_3_42
                player.c "Of course, let me get these ropes off you.  Be careful when you sit up.  You've been tied in that position for a while, give yourself a moment before you try and stand and get dressed."
        $ dee.orgasm_count += 1
        change player energy by -energy_long notify
        $ dee.dom_discussion_count = 6
        call forced_movement(living_room) from _call_forced_movement_1009
        call dee_visit_end from _call_dee_visit_end_13
    # continuing domination sessions
    elif dee.dom_discussion_count == 6:
        player.c "Ready to continue your training?"
        wt_image daughter_house_1_23
        if dee.has_tag('help_her_turn_tables_ra'):
            dee.c "Yes, Sir.  I'm looking forward to learning more from you.  Especially on how to turn the tables on [dee_ra.name]."
        elif dee.fuck_machine_ride_count > 0:
            dee.c "Yes, Sir.  If you'd like to train me on the fuck machine again, I wouldn't mind."
        else:
            dee.c "Yes, Sir.  I'm looking forward to learning more from you."
        $ dee.temporary_count = 1
        $ title = "What do you want to do with her?"
        menu menu_dee_continuing_domination_menu:
            "Trade her to the slaver" if samantha.slaver_events == 9:
                "This won't just cause you to lose access to [dee.name].  It will cause her mother to devote her life to finding her, costing you access to [donna.name] as well.  Do you still want to proceed?"
                $ title = "Proceed?"
                menu:
                    "Yes, trade [dee.name] to the slavers for Sam":
                        if not current_location == dungeon:
                            call forced_movement(dungeon) from _call_forced_movement_1010
                            summon dee no_follows
                        wt_image daughter_dungeon_1_1
                        player.c "Once you have your clothes off, turn around."
                        wt_image daughter_dungeon_1_3
                        dee.c "Yes, Sir."
                        wt_image daughter_slaver_1_1
                        player.c "You won't be able to see in this head harness, [dee.name]."
                        wt_image daughter_slaver_1_2
                        player.c "You won't be able to speak, either, but you can amuse me with the sight of your body.  Remove your bra and panties."
                        wt_image daughter_slaver_1_3
                        player.c "Good girl.  Kneel down."
                        wt_image daughter_slaver_1_4
                        "Carefully, she lowers herself to the floor ..."
                        wt_image daughter_slaver_1_5
                        "... where you complete her immobilization by connecting a chain to the head harness."
                        wt_image daughter_slaver_1_6
                        "No one knows she's here.  Sadly, the disappearance of yet another college girl, especially one with a promisicuous reputation like [dee.name], won't lead to more than a cursory search by the police.  Her fate is about to be sealed."
                        call forced_movement(living_room) from _call_forced_movement_1011
                        wt_image phone_1
                        "She can still hear, though, and so to not cause her any more distress than necessary, you step out of the room to place a call to the slaver."
                        wt_image barista_slaver_1
                        player.c "I'm ready to make a trade.  It would be easiest if you come collect her."
                        samantha_whore_client_3 "Okay, but this needs to be done quickly.  Make sure the product is ready and in no condition to resist."
                        call forced_movement(dungeon) from _call_forced_movement_1012
                        wt_image daughter_slaver_1_6
                        "Already taken care of, you think.  You wait with her, enjoying the sight of her body for the last time, until they come to collect her."
                        wt_image daughter_slaver_1_7
                        "It doesn't take long.  [dee.name] startles at the sound of someone else entering the room, but doesn't try to move.  She still thinks this is a new training lesson you have planned for her."
                        $ title = "What do you say to her?"
                        menu:
                            "Thank you for being a good girl":
                                player.c "Thank you for being such a good girl, [dee.name].  This man is going to take you away and look after you, now.  Be a good girl for him, too.  It will make what comes next easier for you."
                            "Time to be de-clawed, tiger cub":
                                player.c "You were such a fierce, protective tiger cub when I first met you.  Too bad you couldn' protect yourself.  I de-fanged you, but now this man is about to remove your claws."
                            "I never did like you":
                                player.c "I never did like you, you mouthy, domineering feminist bitch.  Too bad for you that your college didn't teach you to be a better judge of character.  This man is going to make you pay dearly for your lack of good judgment."
                            "Nothing":
                                "You watch quietly as the man steps behind [dee.name]."
                        wt_image daughter_slaver_1_8
                        "She has no time to react before the man plunges a needle into her neck."
                        wt_image daughter_slaver_1_9
                        "Attaching weighted clamps to her nipples as [dee.name] slumps into his arms seems cruel, but the man advises it's actually a kindness.  Apparently the stimulation speeds up her body's absorption of the drug he injected into her."
                        wt_image daughter_slaver_1_10
                        "Indeed, as the man binds her into a folded position for easier transport, she already seems more relaxed and you can smell the scent of her arousal.  Whatever fate awaits her, it seems her pussy will be wet for it."
                        dismiss dee
                        call forced_movement(living_room) from _call_forced_movement_1013
                        wt_image current_location.image
                        "There's nothing more for you to now except wait for Sam to be returned to you. [donna.name] will be distraught when she finds out her daughter has gone missing, but that's a small price to pay to get Sam back."
                        rem tags 'contact_open' from dee
                        $ donna.daughter_investigation_triggered == 2
                        $ dee.visit_week = 0
                        call convert(dee, 'unavailable') from _call_convert_192
                        call convert(donna, 'unavailable') from _call_convert_193
                        $ current_target = samantha
                        $ samantha.slaver_events = 10
                        $ samantha.doll_return_week = week + 1
                        add tags 'trade_complete' to samantha
                        change player energy by -energy_short notify
                    "No, not now":
                        $ title = "What do you want to do with her?"
                        jump menu_dee_continuing_domination_menu
            "Help her turn the tables on her RA" if dee.has_tag('help_her_turn_tables_ra'):
                if not current_location == living_room:
                    call forced_movement(living_room) from _call_forced_movement_1014
                wt_image daughter_house_1_23
                player.c "What have you learned so far that could be helpful to you with [dee_ra.name]?"
                wt_image daughter_house_1_2
                dee.c "A few things.  Some of those hints you gave me are probably useful, like acting as if her submitting to me is perfectly normal.  I'm not quite sure how to do that with [dee_ra.name], though."
                player.c "You have to be feeling confident yourself.  That means it needs to be a situation where you're feeling comfortable and in charge.  How often have you initiated sex with [dee_ra.name]?"
                wt_image daughter_house_1_22
                dee.c "Almost never.  You're right, I can't be passive, I need to initiate things.  That's part of how she's gotten the upper hand on me, isn't it?"
                player.c "Probably.  What else has she done that's worked with you?"
                wt_image daughter_house_1_2
                dee.c "She's definitely acted as if me submitting to her is normal.  You mentioned how important that can be.  She also hasn't been shy about telling me in advance what I'll be doing for her soon.  That was another of your tricks you shared."
                player.c "Anything else I told you that you can recognize [dee_ra.name] doing to you?"
                "[dee.name] thinks for a moment before responding."
                wt_image daughter_house_1_21
                dee.c "She was using my competitive nature against me!  Not quite the same way you were, but she made our encounters into a game she knew I'd play even though she'd stacked the rules against me."
                player.c "That wouldn't have worked by itself, though.  There must have been something else that kpt you playing her game."
                wt_image daughter_house_1_24
                dee.c "The sex.  It was good, even when I was taking a submissive role.  You did that to me, too, making sure I came when I was submitting to you, conditioning me to be willing to submit again."
                player.c "You're almost there.  Anything else you can think of?"
                wt_image daughter_house_1_22
                dee.c "Agency.  I thought about that hint for a while, trying to figure out what you meant.  When you set conditions for me to make a choice, even if it was a false choice, you still engaged my brain in actively choosing my own submission.  By making a choice, any choice, I was conditioning myself to justify my choice and my submission."
                player.c "Each small act of submission prepares you for another, [dee.name].  Don't forget that.  As long as she wants the carrot you're holding out to her, you may be able to get her to do things she'd never agree to immediately, by building up to them one act of submission at a time."
                wt_image daughter_house_1_25
                dee.c "Thank you!  I feel better about this now.  I still need to think about how to approach [dee_ra.name], but your advice makes a lot of sense.  I think I can do this."
                $ title = "What now?"
                menu:
                    "Tell her to suck your cock":
                        add tags 'bj_thank_you' to dee
                        if dee.has_any_tag('bound_bj_before', 'sex_before'):
                            wt_image daughter_house_1_75
                            dee.c "Yes, Sir."
                        else:
                            wt_image daughter_house_1_21
                            dee.c "What?"
                            player.c "If you're really thankful for the help I've given you, remove your clothes, get on your knees and suck my cock."
                            wt_image daughter_house_1_1
                            "She looks at you for a moment, debating in her head whether she's ready to change her relationship with you this way ..."
                            wt_image daughter_house_1_75
                            "... then decides she is."
                            dee.c "Yes, Sir."
                        wt_image daughter_house_1_53
                        "You take a seat on the sofa beside her and watch ..."
                        if dee.has_tag('bj_trained'):
                            wt_image daughter_house_1_54
                            "... as she spends time licking at the underside of your cock head, just the way you told her you liked it."
                            wt_image daughter_house_1_56
                            "She continues to swirl her tongue along your cock as she blows you ..."
                            wt_image daughter_house_1_59
                            "... stroking your cock with her lips, keeping her hands out of the way except when needed to hold your cock steady."
                            wt_image daughter_house_1_55
                            if dee.has_tag('can_use_teeth_during_bjs'):
                                "You told her that love bites were okay, but she keeps her teeth out of the way, today, perhaps feeling like they wouldn't be appropriate under the circumstances for which she's blowing you."
                            else:
                                "As instructed, she keeps her teeth out of the way, careful not to catch you with them as she blows you."
                            wt_image daughter_house_1_59
                            "You hold for a while, enjoying her efforts to please you, but eventually you need release."
                        else:
                            wt_image daughter_house_1_54
                            "... as she licks up and down your dick ..."
                            wt_image daughter_house_1_55
                            "... before taking you inside her mouth."
                            wt_image daughter_house_1_56
                            "As blowjobs go, it's a typical college girl effort ..."
                            wt_image daughter_house_1_57
                            "... long on enthusiasm and effort, short on subtlety or technique ..."
                            wt_image daughter_house_1_55
                            "... but more than pleasurable enough to get the job done."
                        wt_image daughter_house_1_58
                        $ title = "Where do you want to cum?"
                        menu:
                            "In her":
                                wt_image daughter_house_1_57
                                player.c "[player.orgasm_text]"
                                wt_image daughter_house_1_60
                                if dee.has_tag('successful_swallow'):
                                    "She starts to choke and pull back as your sperm shoots into the back of her throat ..."
                                    wt_image daughter_house_1_61
                                    "... but then catches herself and diligently pumps as much seed out of your balls as they have to give."
                                    wt_image daughter_house_1_62
                                    player.c "Show me how much you swallowed."
                                    wt_image daughter_house_1_63
                                    "She opens her lips, showing off an empty mouth."
                                    player.c "Good girl."
                                elif dee.has_tag('failed_swallow'):
                                    "She starts to choke and pull back as your sperm shoots into the back of her throat ..."
                                    wt_image daughter_house_1_61
                                    "... but then catches herself and diligently pumps as much seed out of your balls as they have to give."
                                    wt_image daughter_house_1_62
                                    "When you finally finish, she gags slightly as she swallows your load."
                                    player.c "Still haven't talked to your Mom about how to swallow, huh?"
                                    wt_image daughter_house_1_76
                                    if dee.ready_for_mom > 2:
                                        dee.c "Nope, and if you think I'm going to bring her over again so we can both blow you at the same time, forget it.  That was a one time deal."
                                    else:
                                        dee.c "Ewww!  Would you quit suggesting that?  I'm sure you think you can convince me to bring my mother over so we can both blow you, but it's not going to happen."
                                else:
                                    add tags 'failed_swallow' to dee
                                    if donna.has_tag('cum_slut'):
                                        "Unlike her mother, it seems [dee.name] hasn't acquired a taste for cum ..."
                                    else:
                                        "It seems [dee.name] doesn't enjoy, or at least doesn't have much experience with, the taste of cum ..."
                                    wt_image daughter_house_1_61
                                    "... but she diligently pumps as much seed out of your balls as they have to give."
                                    wt_image daughter_house_1_62
                                    "When you finally finish, she gags slightly as she swallows your load."
                                    player.c "You okay?"
                                    wt_image daughter_house_1_27
                                    dee.c "Yeah, I'm fine.  It's not easy catching your cum without choking when your cock is spurting like that."
                                    player.c "I guess you don't have a lot of experience with giving blowjobs."
                                    wt_image daughter_house_1_26
                                    dee.c "I have a little, but most of the guys I've been with seemed to prefer facials.  I haven't had to try and catch a full load like that in my mouth very often.  It's trickier than it sounds."
                                    player.c "Maybe you should ask your Mom for tips on how she does it?"
                                    wt_image daughter_house_1_21
                                    dee.c "Ewww!!  That conversation's not happening!"
                                    player.c "Then I guess I'll just have to teach you how to swallow."
                                    wt_image daughter_house_1_22
                                    dee.c "Great!  Next time I'll bring a guy with me and you can show me how you swallow his load.  Shhh!  Don't try to explain yourself, I know what I heard."
                                $ dee.swallow_count += 1
                            "On her":
                                wt_image daughter_house_1_63
                                player.c "[player.orgasm_text]"
                                wt_image daughter_house_1_64
                                if dee.has_tag('facial_before'):
                                    player.c "You know, those boys in college are onto something.  You do look good like that."
                                    wt_image daughter_house_1_65
                                    dee.c "As compliments go, that's a bit of a mixed one, but I'm going to take the high road and say 'thank you'."
                                else:
                                    add tags 'facial_before' to dee
                                    if dee.professor_event_status > 1:
                                        dee.c "So I guess it's not just college boys and Dr. Jameson who like to see me like this."
                                    else:
                                        dee.c "So I guess it's not just college boys who like to see me like this."
                                    wt_image daughter_house_1_65
                                    player.c "Have many of the boys from your school been able to admire you in this condition?"
                                    wt_image daughter_house_1_66
                                    dee.c "I'm not a slut, if that's what you're trying to imply.  And even if I were, there's nothing wrong with a woman having a healthy libido and multiple consensual partners at the same time, as long as she hasn't made a monogamous commitment to any of them."
                                    wt_image daughter_house_1_67
                                    player.c "Well, the next time your non-monogamous libido is in the mood for another facial, drop by and see me."
                                $ dee.facial_count += 1
                        $ dee.blowjob_count += 1
                        orgasm
                    "Send her home":
                        pass
                rem tags 'help_her_turn_tables_ra' from dee
                change player energy by -energy_very_short notify
                $ dee.talk_sex_life_status = 7
            "Bound blowjob":
                if not current_location == dungeon:
                    call forced_movement(dungeon) from _call_forced_movement_1015
                wt_image daughter_dungeon_4_1
                "You have [dee.name] strip, then use ropes to immobilize her, leaving her balancing on her knees."
                wt_image daughter_dungeon_4_2
                if dee.has_tag('bound_bj_before'):
                    dee.c "Would you like me to blow you again, Sir?"
                    wt_image daughter_dungeon_4_3
                    player.c "There's no need to use words to make that offer, is there?"
                    wt_image daughter_dungeon_4_7
                    "As you stand in front of her, she opens her mouth."
                else:
                    dee.c "This is awkward."
                    wt_image daughter_dungeon_4_3
                    player.c "I'm sure you'll manage."
                    wt_image daughter_dungeon_4_4
                    dee.c "Manage what?"
                    wt_image daughter_dungeon_4_5
                    player.c "Manage to suck me off to thank me for training you."
                    wt_image daughter_dungeon_4_6
                    if dee.has_tag('bj_thank_you'):
                        dee.c "I seem to be expected to thank you with my mouth a lot."
                        wt_image daughter_dungeon_4_7
                        player.c "I've been very helpful to you.  Open your mouth and show me where my cock is going to go."
                    elif dee.has_tag('sex_before'):
                        dee.c "Wouldn't it be better if you untied me and we could have sex normally on the sofa?"
                        wt_image daughter_dungeon_4_7
                        player.c "But I like seeing you tied up, you know that, and I'm going to enjoy watching you blow me while you're tied up.  Open your mouth and show me where my cock is going to go."
                    else:
                        dee.c "You expect me to look after you sexually now?"
                        wt_image daughter_dungeon_4_8
                        player.c "You're not stupid, [dee.name].  I've been tying you up naked for a while now.  You knew this was coming, didn't you?"
                        wt_image daughter_dungeon_4_9
                        "She hesitates for just a moment before she nods."
                        wt_image daughter_dungeon_4_7
                        player.c "Good, because I've been very patient with you, but now I'm going to start enjoying you.  Open your mouth and show me where my cock is going to go."
                wt_image daughter_dungeon_4_10
                player.c "Good girl.  Stay like that."
                wt_image daughter_dungeon_4_11
                "She dutifully keeps her mouth open as you take out your cock ..."
                wt_image daughter_dungeon_4_12
                "... and put it inside."
                if dee.has_tag('bj_trained'):
                    wt_image daughter_dungeon_4_13
                    "Remembering what you taught her, when you step back she locks her eyes on you and licks submissively at the underside of your cock head."
                    wt_image daughter_dungeon_4_14
                    "And when you step forward again, she keeps her tongue active in her mouth, swirling it around your cock ..."
                    wt_image daughter_dungeon_4_15
                    "... as she bobs her head up and down your shaft, stroking your cock with her lips as best she can within the confines of her bounds."
                    wt_image daughter_dungeon_4_16
                    if dee.has_tag('can_use_teeth_during_bjs'):
                        "She keeps her teeth out of the way, perhaps sensing that these are not the circumstances for love bites."
                    else:
                        "As instructed, she keeps her teeth out of the way, careful not to catch you with them as her head slides up and down your shaft."
                else:
                    wt_image daughter_dungeon_4_20
                    "As you pull back, she sucks as hard as she can on the head of your cock ..."
                    wt_image daughter_dungeon_4_15
                    "... and continues to suck firmly as she follows you ..."
                    wt_image daughter_dungeon_4_21
                    "... her head moving back and forth as she seeks out as much of your dick as she can reach."
                wt_image daughter_dungeon_4_17
                "Watching the bound, young college girl pleasuring your cock is highly stimulating ..."
                wt_image daughter_dungeon_4_18
                "... and while you make this last as long as you can, eventually the warm wetness of her mouth wins out."
                wt_image daughter_dungeon_4_19
                $ title = "Where do you want to cum?"
                menu:
                    "In her":
                        wt_image daughter_dungeon_4_22
                        player.c "[player.orgasm_text]"
                        if dee.has_tag('successful_swallow'):
                            wt_image daughter_dungeon_4_23
                            "She starts to choke and pull back as your sperm shoots into the back of her throat ..."
                            wt_image daughter_dungeon_4_26
                            "... but moves back in place once she feels your hand on the back of her head ..."
                            wt_image daughter_dungeon_4_27
                            "... and stays there until your balls are empty."
                            wt_image daughter_dungeon_4_25
                            player.c "Show me how much you swallowed."
                            wt_image daughter_dungeon_4_10
                            player.c "Good girl.  Your throat makes a lovely cum dump."
                        elif dee.has_tag('failed_swallow'):
                            add tags 'successful_swallow' to dee
                            wt_image daughter_dungeon_4_24
                            "She starts to choke and pull back as your sperm shoots into the back of her throat ..."
                            wt_image daughter_dungeon_4_26
                            "... but with a firm hand on the back of her head, you hold her in place."
                            wt_image daughter_dungeon_4_27
                            player.c "No, not this time.  I don't care whether you like the taste of my cum.  You need to learn how to swallow."
                            wt_image daughter_dungeon_4_23
                            "Once your balls are empty you let go of her head."
                            wt_image daughter_dungeon_4_25
                            player.c "Show me you swallowed it all."
                            wt_image daughter_dungeon_4_10
                            player.c "Good girl.  I expect your throat to be available as a cum dump for me from now on."
                        else:
                            add tags 'failed_swallow' to dee
                            wt_image daughter_dungeon_4_24
                            if donna.has_tag('cum_slut'):
                                "She starts to choke and pull back as your sperm shoots into the back of her throat.  Unlike her mother, it seems [dee.name] hasn't acquired a taste for cum."
                            else:
                                "She starts to choke and pull back as your sperm shoots into the back of her throat.  It seems [dee.name] doesn't enjoy, or at least doesn't have much experience with, the taste of cum."
                            wt_image daughter_dungeon_4_25
                            "When you finally finish, she gags slightly as she swallows your load."
                            player.c "You okay?"
                            wt_image daughter_dungeon_4_6
                            dee.c "Yeah, I'm fine.  It's not easy catching your cum without choking when your cock is spurting like that."
                            player.c "I guess you don't have a lot of experience with giving blowjobs."
                            wt_image daughter_dungeon_4_8
                            dee.c "I have a little, but most of the guys I've been with seemed to prefer facials.  I haven't had to try and catch a full load like that in my mouth very often.  It's trickier than it sounds."
                            if donna.has_tag('cum_slut'):
                                player.c "Maybe you should ask your Mom for tips on how she does it?  These days she doesn't even spill a drop, or if she does she scoops it back into her mouth to swallow it."
                            else:
                                player.c "Maybe you should ask your Mom for tips on how she does it?  She doesn't let as much dribble out as you do."
                            wt_image daughter_dungeon_4_4
                            dee.c "Ewww!!  That conversation's not happening!"
                        $ dee.swallow_count += 1
                    "On her":
                        wt_image daughter_dungeon_4_28
                        "As you pull out of her mouth she looks up at you, waiting for what comes next."
                        wt_image daughter_dungeon_4_29
                        player.c "[player.orgasm_text]"
                        wt_image daughter_dungeon_4_30
                        if dee.has_tag('facial_before'):
                            player.c "You look good tied-up, but you look even better tied-up with cum on your face."
                            wt_image daughter_dungeon_4_31
                            dee.c "That might be the weirdest compliment I've ever received, but 'thank you', I guess?"
                        else:
                            add tags 'facial_before' to dee
                            if dee.professor_event_status > 1:
                                dee.c "So I guess it's not just college boys and Dr. Jameson who like to see me like this."
                            else:
                                dee.c "So I guess it's not just college boys who like to see me like this."
                            wt_image daughter_dungeon_4_31
                            player.c "Have many of the boys from your school been able to admire you in this condition?"
                            dee.c "I'm not a slut, if that's what you're trying to imply.  And even if I were, there's nothing wrong with a woman having a healthy libido and multiple consensual partners at the same time, as long as she hasn't made a monogamous commitment to any of them."
                            wt_image daughter_dungeon_4_32
                            player.c "That's an impressive speech delivered bound on your knees with my cum dripping down your face.  Lick my cock clean then I'll let you go get back to your non-monogmous life."
                        $ dee.facial_count += 1
                add tags 'bound_bj_before' to dee
                $ dee.blowjob_count += 1
                orgasm notify
                call forced_movement(living_room) from _call_forced_movement_1016
            "Bound sex" if dee.has_any_tag('bound_bj_before', 'bound_sex_before', 'bj_thank_you', 'sex_before'):
                if not current_location == dungeon:
                    call forced_movement(dungeon) from _call_forced_movement_1017
                wt_image daughter_dungeon_5_1
                "You have [dee.name] strip, then use ropes to immobilize her arms."
                if dee.has_tag('bound_sex_before'):
                    player.c "I'm going to fuck you now, [dee.name], and you're going to let me."
                elif dee.has_tag('sex_before') or dee.ready_for_mom > 2:
                    player.c "I've been enjoying the sight of you tied up on our little trips to my dungeon.  It's time I enjoy the feel of your cunt around my cock while you're tied up."
                else:
                    player.c "I've been enjoying the sight of you tied up on our little trips to my dungeon, but it's time to change the nature of our relationship.  I don't just want to enjoy the sight of your body, I want to enjoy using it while you're tied up."
                    wt_image daughter_dungeon_5_2
                    dee.c "You're not talking about me using my mouth on you again, are you?"
                    player.c "No, [dee.name], I'm not.  I'm going to fuck you and you're going to let me."
                    "She hesitates for a moment, contemplating where this is taking your relationship, then replies."
                wt_image daughter_dungeon_5_3
                dee.c "Yes, Sir."
                wt_image daughter_dungeon_5_4
                player.c "A horny college girl like you doesn't need any more warm up than that, does she?  When I bend you over and press the head of my cock against your cunt, it's going to be wet for me, isn't it?"
                dee.c "oohhh ... Yes, Sir."
                wt_image daughter_dungeon_5_5
                "A little bit of dirty talk and the anticipation of penetration really is all it takes for her body to be ready for penetration."
                wt_image daughter_dungeon_5_6
                dee.c "oohhhhh"
                wt_image daughter_dungeon_5_7
                $ dee.temporary_count = 0
                $ title = "Enjoy her body"
                menu menu_dee_bound_sex_menu:
                    "Fuck her":
                        $ dee.temporary_count += 1
                        wt_image daughter_dungeon_5_9
                        "Gripping her firmly by her bound arms, you thrust into her as she moans.  The harder and faster you fuck her, the louder she moans."
                        dee.c "oohhhhh ... oohhhhh!!"
                        wt_image daughter_dungeon_5_7
                        jump menu_dee_bound_sex_menu
                    "Spank her":
                        wt_image daughter_dungeon_5_8
                        "Her whole body jolts and she yelps - more in surprise than pain - as you bring your hand down on her ass with your cock still inside her ... *smack*"
                        dee.c "Ohh, ow!"
                        wt_image daughter_dungeon_5_7
                        jump menu_dee_bound_sex_menu
                    "Make her cum" if dee.temporary_count > 0:
                        wt_image daughter_dungeon_5_11
                        if dee.sex_count == 0:
                            "Some women, particularly young women, find it challenging to reach orgasm, especially with a new sex partner."
                        else:
                            "Some women, particularly young women, find it challenging to reach orgasm."
                        wt_image daughter_dungeon_5_12
                        "[dee.name] is not one of those women.  A small change in the angle at which you're fucking her quickly has her creaming around your cock."
                        wt_image daughter_dungeon_5_13
                        dee.c "Ohhh FUCCKKK!!!"
                        wt_image daughter_dungeon_5_14
                        "There may be more enjoyable sensations than a bound young woman spasming in orgasm on your cock, but there aren't many, and they would all trigger your balls to empty, too."
                        wt_image daughter_dungeon_5_11
                        player.c "[player.orgasm_text]"
                        wt_image daughter_dungeon_5_3
                        if dee.has_tag('bound_sex'):
                            dee.c "Well that was kinky and weird, but kind of fun."
                        elif dee.has_tag('sex_before'):
                            dee.c "I think I would have enjoyed that more without my arms being tied up in these ropes, but it was fun anyway."
                        else:
                            dee.c "You're pretty good at this bondage thing."
                        $ dee.orgasm_count += 1
                    "Cum before she does" if dee.temporary_count > 0:
                        wt_image daughter_dungeon_5_9
                        "With three final, hard thrusts you empty your load inside her."
                        wt_image daughter_dungeon_5_6
                        player.c "[player.orgasm_text]"
                        wt_image daughter_dungeon_5_10
                        "Shit!  I was so close."
                        wt_image daughter_dungeon_5_5
                        player.c "Good thing you enjoy pleasing me enough not to worry about your own pleasure."
                        wt_image daughter_dungeon_5_3
                        dee.c "Yeah, sure.  You can go with that if it turns your crank."
                add tags 'bound_sex_before' to dee
                $ dee.temporary_count = 1
                $ dee.sex_count += 1
                orgasm notify
                call forced_movement(living_room) from _call_forced_movement_1018
            "Intense crotch rope ordeal":
                if not current_location == dungeon:
                    call forced_movement(dungeon) from _call_forced_movement_1019
                wt_image daughter_dungeon_3_12
                "Once [dee.name] is naked, you tie her elbows together behind her back ..."
                wt_image daughter_dungeon_6_1
                "... then use the elbow tie as leverage to lift her heels off the ground."
                wt_image daughter_dungeon_6_2
                "A rope gag comes next ..."
                wt_image daughter_dungeon_6_3
                "... followed by the crotch rope."
                wt_image daughter_dungeon_6_4
                "Then you hobble her ..."
                wt_image daughter_dungeon_6_5
                "... before relaxing the rope supporting her weight by her elbows, forcing her to keep her balance herself."
                wt_image daughter_dungeon_6_6
                "It's a challenging position.  If she lowers her heels, she increases the pressure of the rope digging into her sex.  If she keeps her heels high, she exhausts her calf muscles and sways back and forth slightly, causing the crotch rope to rub against her sex."
                wt_image daughter_dungeon_6_7
                "As you step back to watch, her eyes follow you, pleading silently for release."
                player.c "Don't look at me, keep your focus on the rope between your legs."
                wt_image daughter_dungeon_6_8
                "You enforce your command by looping a rope behind her neck and tying it to the crotch rope.  Now she has to keep her head down, looking at the rope digging into her sex.  Any attempt to lift her head just amplifies the sensation of being sawed in two."
                wt_image daughter_dungeon_6_9
                "It's important that she be aroused, so that her natural lubricants prevent the friction of the rope from damaging her skin.  A quick check between her legs confirms that she's thoroughly wet from the intense pressure on her clit.  She's closer to cumming than she is to suffering injury."
                wt_image daughter_dungeon_6_10
                "That doesn't mean she's comfortable.  She's anything but.  The crotch rope might be arousing her, but it's also agonizing and scary.  After a while, her leg muscles start to tire and she begins to shake, which makes it feel like she's sawing herself in half against the rope."
                dee.c "NNNNNN!!"
                player.c "Intense isn't it?  Scary, too.  Do you find this scary, [dee.name]?  Are you worried about what happens once your legs are too tired to hold your heels off the ground?"
                wt_image daughter_dungeon_6_8
                "She nods vigorously.  She's safe, but it doesn't feel safe to her."
                $ title = "What do you do?"
                menu menu_dee_intense_crop_rope_menu:
                    "Watch her for a little longer":
                        wt_image daughter_dungeon_6_10
                        "She's beautiful, scared, helpless and intensely turned on despite the ordeal she finds herself in.  You'll have to let her go soon, but it's hard not to watch her struggle for a few more minutes, bouncing gently up and down and swaying slightly from side to side as she tries to hold herself steady but can't as the fatigue in her legs increases."
                        wt_image daughter_dungeon_6_8
                        dee.c "NNNNNN!!"
                        jump menu_dee_intense_crop_rope_menu
                    "Let her down after she cums":
                        wt_image daughter_dungeon_6_8
                        player.c "I'm going to let you down, but only after you cum on the rope."
                        dee.c "nnnn????"
                        wt_image daughter_dungeon_6_9
                        player.c "Was that confusion, [dee.name]?  Your cunt is soaked.  Didn't you realize how much your body is turned on right now?"
                        wt_image daughter_dungeon_6_11
                        "She hadn't actually, she'd been too preoccupied with the scariness of the situation and the unpleasant sensations to notice her underlying arousal.  But now that you've pointed it out, she starts grinding her hips forward against your fingers."
                        wt_image daughter_dungeon_6_6
                        player.c "No, [dee.name].  You're going to cum by grinding your sore pussy against the crotch rope ..."
                        wt_image daughter_dungeon_6_5
                        player.c "... and I'm going to remove your rope gag so I can hear you scream loudly as you do it."
                        wt_image daughter_dungeon_6_12
                        "She spent most of the ordeal struggling to ease the pressure between her legs.  Hesitantly at first, she now leans into it, pressing her sore pussy against the rope until she finds the right angle at which to grind her hard clit against it.  Then she starts rocking her hips back and forth as she makes herself cum by humping the crotch rope."
                        dee.c "Ohhh FUCCKKK!!!"
                        wt_image daughter_dungeon_talk_2
                        "When she finishes cumming, you help her down into a sitting position."
                        dee.c "That was embarrassing."
                        player.c "What was?"
                        wt_image daughter_dungeon_talk_3
                        dee.c "Humping the rope like that.  I must have looked like an animal, or an idiot."
                        $ title = "What do you tell her?"
                        menu:
                            "She looked sexy":
                                wt_image daughter_dungeon_talk_1
                                dee.c "Thank you.  Even if you're just saying that, it makes me feel better.  That was a weird orgasm, I'm not sure I completely enjoyed it, but it was crazy intense."
                            "She looked like a slut":
                                wt_image daughter_dungeon_talk_2
                                dee.c "I guess I did, cumming on a rope like that.  It was a weird orgasm, too.  I'm not sure I even really enjoyed it, although it was crazy intense."
                            "She looked desperate":
                                wt_image daughter_dungeon_talk_4
                                dee.c "I was feeling desperate!  Desperate to cum, desperate to get off that rope.  It was such a weird orgasm, too.  I'm not sure I even completely enjoyed it, I was mostly just relieved the ordeal was over."
                        $ dee.orgasm_count += 1
                    "Let her down in return for a blowjob":
                        wt_image daughter_dungeon_6_8
                        if dee.has_any_tag('bound_bj_before', 'bj_thank_you', 'sex_before'):
                            "She nods vigorously, happy to take your cock in her mouth in return for removing the rope between her legs."
                        else:
                            "You thought she might hesitate at this change in your relationship, but she doesn't.  She nods vigorously, prepared to have your cock in her mouth in return for removing the rope between her legs."
                        wt_image daughter_dungeon_4_32
                        "After you let her down, she attacks your cock.  There's no technique, just desperate cocksucking, fueled both by relief from the end of her ordeal and sexual tension from the arousal she felt during the ordeal."
                        wt_image daughter_dungeon_4_33
                        "She's not the only one who's intensely aroused.  Watching her struggle on the crotch rope turned you on, too, so much so that you find yourself releasing your load soon after she takes you into her eager mouth."
                        player.c "[player.orgasm_text]"
                        wt_image daughter_dungeon_4_34
                        if dee.has_tag('successful_swallow'):
                            "She looks up at you in surprise, not having expected you to cum so quickly, and instinctively pulls back as your jizz shoots into the back of her throat ..."
                            wt_image daughter_dungeon_4_26
                            "... but quickly moves back in place once she feels your hand on the back of her head and stays there until your balls are empty."
                            wt_image daughter_dungeon_4_10
                            "Unprompted, she opens her mouth to show you she swallowed your entire load."
                            player.c "Good girl.  How does your cunt feel?"
                            wt_image daughter_dungeon_4_9
                            dee.c "Honestly, I have no idea what to make of that experience.  You clearly enjoyed it, though."
                        elif dee.has_tag('failed_swallow'):
                            add tags 'successful_swallow' to dee
                            "She looks up at you in surprise, not having expected you to cum so quickly, and instinctively pulls back as your jizz shoots into the back of her throat ..."
                            wt_image daughter_dungeon_4_26
                            "... but with a firm hand on the back of her head, you hold her in place."
                            wt_image daughter_dungeon_4_27
                            player.c "No, not this time.  I don't care whether you like the taste of my cum.  You need to learn how to swallow."
                            wt_image daughter_dungeon_4_34
                            "Once your balls are empty you let go of her head."
                            player.c "Show me you swallowed it all."
                            wt_image daughter_dungeon_4_10
                            player.c "Good girl.  I expect your throat to be available as a cum dump for me from now on."
                        else:
                            add tags 'failed_swallow' to dee
                            if donna.has_tag('cum_slut'):
                                "She starts to choke and pull back as your sperm shoots into the back of her throat.  Unlike her mother, it seems [dee.name] hasn't acquired a taste for cum."
                            else:
                                "She starts to choke and pull back as your sperm shoots into the back of her throat.  It seems [dee.name] doesn't enjoy, or at least doesn't have much experience with, the taste of cum."
                            wt_image daughter_dungeon_4_18
                            "When you finally finish, she gags slightly as she swallows your load."
                            player.c "You okay?"
                            wt_image daughter_dungeon_4_9
                            dee.c "Yeah, I'm fine.  It's not easy catching your cum without choking when your cock is spurting like that."
                            player.c "I guess you don't have a lot of experience with giving blowjobs."
                            dee.c "I have a little, but most of the guys I've been with seemed to prefer facials.  I haven't had to try and catch a full load like that in my mouth very often.  It's trickier than it sounds."
                            wt_image daughter_dungeon_4_31
                            if donna.has_tag('cum_slut'):
                                player.c "Maybe you should ask your Mom for tips on how she does it?  These days she doesn't even spill a drop, or if she does she scoops it back into her mouth to swallow it."
                            else:
                                player.c "Maybe you should ask your Mom for tips on how she does it?  She doesn't let as much dribble out as you do."
                            dee.c "Ewww!!  That conversation's not happening!"
                        add tags 'bound_bj_before' to dee
                        $ dee.swallow_count += 1
                        $ dee.blowjob_count += 1
                        orgasm
                    "Just let her down":
                        wt_image daughter_dungeon_6_5
                        "[dee.name] sighs in relief as you release her."
                        wt_image daughter_dungeon_talk_3
                        player.c "How's your cunt?"
                        wt_image daughter_dungeon_talk_4
                        dee.c "Sore.  Aroused.  The center of my being right now, it's hard to focus or think about anything else."
                        player.c "So pretty much normal for you, then."
                        wt_image daughter_dungeon_talk_1
                        dee.c "Ha ha.  I'm not a slut, I just like sex."
                        player.c "And you like being tied up with a rope torturing your crotch."
                        wt_image daughter_dungeon_talk_4
                        dee.c "I'm not sure I did enjoy it, but it was intense and it did leave me horny.  So I guess I kind of enjoyed parts of it, but the overall experience was bizarre."
                call forced_movement(living_room) from _call_forced_movement_1020
                change player energy by -energy_very_short notify
            "Gag and bind her on her back" if dungeon.has_item(gags):
                if not current_location == dungeon:
                    call forced_movement(dungeon) from _call_forced_movement_1021
                wt_image daughter_dungeon_7_1
                "You gag [dee.name] and lay her on her back ..."
                wt_image daughter_dungeon_7_2
                "... tying her feet into the air ..."
                wt_image daughter_dungeon_7_3
                "... leaving her in a helpless and vulnerable position."
                wt_image daughter_dungeon_7_4
                $ title = "What do you do with her?"
                menu menu_dee_gagged_back_menu:
                    "Look at her":
                        wt_image daughter_dungeon_7_5
                        "She watches apprehensively as you admire her bound form from different angles ..."
                        wt_image daughter_dungeon_7_3
                        "... enjoying the view from the side ..."
                        wt_image daughter_dungeon_7_6
                        "... above ..."
                        wt_image daughter_dungeon_7_7
                        "... and below."
                        if dee.has_tag('came_today'):
                            wt_image daughter_dungeon_7_10
                            "Her cunt is still wet and puffy from her prior orgasm."
                        elif dee.has_tag('aroused_now'):
                            wt_image daughter_dungeon_7_10
                            "Your prior attention has left her aroused.  It would be easy to make her cum, if you wanted to."
                        wt_image daughter_dungeon_7_4
                        jump menu_dee_gagged_back_menu
                    "Tease her" if dee.has_tag('aroused_now'):
                        wt_image daughter_dungeon_7_13
                        if dee.has_tag('came_multiple_times_today'):
                            player.c "You cum so easily like this, [dee.name].  Tied up, gagged and cumming like a fountain every time I play with your clit.  Are you sure you don't want to stay like this?  Just nod your head and I'll take you as my permanent slave."
                            wt_image daughter_dungeon_7_1
                            "She shakes her head 'no', but it's a surprisingly feeble effort.  She doesn't really want to be a slave, but her body's so exhausted from the bondage and the orgasms that she can barely bring herself to express her preference."
                        elif dee.has_tag('came_today'):
                            player.c "Such a good girl.  Tied up, gagged and still able to cum for me.  I think you like this more than you let on.  Are you sure you don't want to become my slavegirl."
                            wt_image daughter_dungeon_7_1
                            "She shakes her head 'no', but doesn't try to give her safe signal or convince you to remove her from her bonds."
                        elif dee.has_tag('aroused_now'):
                            player.c "You're wet, [dee.name].  Tied up, gagged and dripping wetness from between your legs onto my dungeon equipment.  Are you hoping I'll make you gush even more fluids onto my bench and floor?"
                            wt_image daughter_dungeon_7_11
                            "She nods and her pussy puckers at the thought."
                        else:
                            player.c "Wife Trainer fucked up.  We shouldn't be able to be having this conversation with the tags attached to you right now."
                        wt_image daughter_dungeon_7_4
                        jump menu_dee_gagged_back_menu
                    "Pleasure her with your mouth":
                        if dee.has_tag('came_today') and dee.has_tag('aroused_now'):
                            "Her cunt is wet and sensitive from her prior orgasm.  She probably doesn't feel any particular urge to cum again, but you expect you could make her cum anyway."
                        elif dee.has_tag('aroused_now'):
                            wt_image daughter_dungeon_7_10
                            "[dee.name] is wet and aroused from your prior attention, but you can make her wetter still."
                        else:
                            wt_image daughter_dungeon_7_5
                            "[dee.name] doesn't seem to be enjoying herself too much, but you can change that."
                        wt_image daughter_dungeon_7_8
                        "You lower your head between her legs ..."
                        wt_image daughter_dungeon_7_9
                        "... and kiss, lick, nibble and tease her sex while she moans into her gag."
                        dee.c "nnnnnn"
                        wt_image daughter_dungeon_7_10
                        if dee.has_tag('came_today'):
                            "She thrashes in her bounds.  It's not clear if she's trying to avoid or increase the contact on her sensitive sex."
                        elif dee.has_tag('aroused_now'):
                            "She strains at her bounds, trying to thrust her mound up against your mouth, desperate to cum."
                        else:
                            "Soon her sex is puffy and wet and she's on the verge of cumming."
                        $ title = "What now?"
                        menu:
                            "Make her cum again" if dee.has_tag('came_today'):
                                add tags 'came_multiple_times_today' to dee
                                wt_image daughter_dungeon_7_9
                                "You put your head back between her legs and flick your tongue hard against her engorged clit.  At first she tries to twist her hips away, but the bonds she's in don't let her escape.  As you keep flicking her clit with your tongue, she suddenly stops tying to pull away and thrusts her hips up towards you."
                                wt_image daughter_dungeon_7_12
                                dee.c "nnnn NNNNNNN!!!"
                                $ dee.orgasm_count += 1
                                $ dee.pleasure_her_count += 1
                            "Make her cum" if not dee.has_tag('came_today'):
                                add tags 'came_today' to dee
                                wt_image daughter_dungeon_7_9
                                "You put your head back between her legs and flick your tongue hard against her engorged clit.  It barely takes three licks before she's lifting her hips and grinding her sex against your mouth in climax."
                                wt_image daughter_dungeon_7_12
                                dee.c "nnnn NNNNNNN!!!"
                                $ dee.orgasm_count += 1
                                $ dee.pleasure_her_count += 1
                            "Stop there":
                                add tags 'aroused_now' to dee
                                wt_image daughter_dungeon_7_11
                                if dee.has_tag('came_today'):
                                    "She groans into her gag as you stop.  You're not sure if it's a groan of relief or a groan of disappointment, and you suspect she doesn't know, either."
                                else:
                                    "She groans in disappointment as she realizes you're stopping, when she's so close."
                                dee.c "nnnnn"
                        wt_image daughter_dungeon_7_4
                        jump menu_dee_gagged_back_menu
                    "Spank her pussy":
                        wt_image daughter_dungeon_7_14
                        if dee.has_tag('aroused_now'):
                            "You bring your hand down sharply on her aroused cunt ... *SMACK*"
                            wt_image daughter_dungeon_7_11
                            if dee.has_tag('came_multiple_times_today'):
                                "Her whole body trembles as and groans into the gag.  She's exhausted from the prior orgasms.  She probably can't cum again just from having her pussy spanked, but you could try anyway, if you want."
                            elif dee.has_tag('came_today'):
                                "She closes her eyes and groans into the gag.  She's already cum once today, but you might be able to make her cum again if you spank her clit."
                            else:
                                "She closes her eyes and groans into the gag.  She's so turned on you could likely make her cum just by spanking her clit, if you wanted to."
                            $ title = "Try and make her cum?"
                            menu:
                                "Yes, try and spank her to orgasm":
                                    wt_image daughter_dungeon_7_11
                                    "You strike the flat of your hand fully against her sex, sending shock waves up through her clit ... *smack*  *smack*  *smack*"
                                    wt_image daughter_dungeon_7_1
                                    if dee.has_tag('came_multiple_times_today'):
                                        "She strains in her bonds, her head shaking from side to side."
                                        wt_image daughter_dungeon_7_14
                                        "You increase the intensity of the spanks as her whole body bucks and thrashes, including some blows directly on her erect and throbbing clit ... *SMACK*  *SMACK*  *SMACK*"
                                        wt_image daughter_dungeon_7_1
                                        "[dee.name] continues to shake.  The spanking has left her on the brink of another climax, but after the orgasms she's already experienced today, it's not enough to take her over the edge."
                                    else:
                                        "She starts to strain in her bonds.  She hates this sensation, but her body is responding anyway."
                                        wt_image daughter_dungeon_7_14
                                        "You increase the intensity of the spanks as her whole body bucks and thrashes, then you take over the edge with three hard slaps in quick succession, directly on her erect and throbbing clit ... *SMACK*  *SMACK*  *SMACK*"
                                        wt_image daughter_dungeon_7_12
                                        dee.c "nnnn NNNNNNN!!!"
                                        $ dee.orgasm_count += 1
                                "No, leave her aroused":
                                    pass
                        else:
                            "You slap her exposed sex with the palm of your hand, softly at first, then gradually harder and harder ... *smack*  *smack*  *smack*  *SMACK*  *SMACK*"
                            wt_image daughter_dungeon_7_11
                            "It's a scary experience for her, but you could probably make it an arousing one, too, if you want?"
                            $ title = "Try and turn her on?"
                            menu:
                                "Yes, try and spank her to arousal":
                                    add tags 'aroused_now' to dee
                                    wt_image daughter_dungeon_7_14
                                    "You continue spanking her pussy, mixing shap slaps with more gentle swats ... *smack*  *smack*  *SMACK*  *smack*  *smack*  *SMACK* ..."
                                    wt_image daughter_dungeon_7_10
                                    "... increasing the stimulation and blood-flow until her pussy is throbbing, wet and aroused."
                                "No, move on to something else":
                                    pass
                        wt_image daughter_dungeon_7_4
                        jump menu_dee_gagged_back_menu
                    "Crop her pussy" if dungeon.has_item(floggers) and not dee.has_tag('cropped_pussy_today'):
                        add tags 'cropped_pussy_today' to dee
                        wt_image daughter_dungeon_7_15
                        "Picking up a crop, you smack it sharply on her exposed sex ...  *THWACCKK*"
                        wt_image daughter_dungeon_7_16
                        if dee.has_tags('aroused_now'):
                            rem tags 'aroused_now' from dee
                            "[dee.name] is no masochist.  Whatever arousal she had been feeling is brought to a quick end by the intense pain.  She screams into her gag and shakes her head from side-to-side."
                        else:
                            "[dee.name] is no masochist.  She screams into her gag and shakes her head from side-to-side at the intense pain."
                        dee.c "NNNNN!!"
                        wt_image daughter_dungeon_7_11
                        "[dee.name] breathes heavily, trying to calm herself from the pain radiating through her cunt.  Unless she's aroused first, she won't be able to tolerate another cropping between her legs without tapping out."
                        wt_image daughter_dungeon_7_4
                        jump menu_dee_gagged_back_menu
                    "Crop her pussy again" if dungeon.has_item(floggers) and dee.has_tag('cropped_pussy_today') and dee.has_tag('aroused_now'):
                        rem tags 'aroused_now' from dee
                        wt_image daughter_dungeon_7_15
                        "Picking the crop back up, you bring it down again on her wet and aroused pussy ...  *THWACCKK*"
                        wt_image daughter_dungeon_7_16
                        dee.c "NNNNN!!"
                        wt_image daughter_dungeon_7_11
                        "That dried her up quickly.  [dee.name] breathes heavily, trying to calm herself from the pain radiating through her cunt.  She's no longer feeling aroused, only sore."
                        wt_image daughter_dungeon_7_4
                        jump menu_dee_gagged_back_menu
                    "Flog her pussy" if dungeon.has_item(floggers):
                        if not dee.has_tag('flogged_today'):
                            add tags 'flogged_today' to dee
                            wt_image daughter_dungeon_7_13
                            player.c "I have a treat for your pussy, [dee.name]."
                            wt_image daughter_dungeon_7_17
                            "She looks at you in terror as you swing the flogger down towards her exposed sex ..."
                        else:
                            "[dee.name] looks at you in terror as you pick up the flogger and swing it down again towards her exposed sex ..."
                        wt_image daughter_dungeon_7_18
                        "*THWACCKK* ... [dee.name] grunts into her gag at the intense sensation."
                        dee.c "NNNNNN"
                        wt_image daughter_dungeon_7_17
                        "Again you swing the flogger down on her exposed sex ..."
                        wt_image daughter_dungeon_7_18
                        "*THWACCKK* ... and again [dee.name] grunts into her gag."
                        dee.c "NNNNNN"
                        wt_image daughter_dungeon_7_17
                        "One more swing ..."
                        wt_image daughter_dungeon_7_18
                        if dee.has_tag('aroused_now') and dee.has_tag('came_multiple_times_today') and not dee.has_tag('flogged_to_orgasm_today'):
                            add tags 'flogged_to_orgasm_today' to dee
                            "*THWACCKK* ... and instead of a grunt you hear the unmistakable sounds of [dee.name] cumming from the flogging."
                            wt_image daughter_dungeon_7_12
                            dee.c "nnnn NNNNNNN!!!"
                            wt_image daughter_dungeon_7_13
                            player.c "Well, well, well.  Look at you cumming from being flogged like a proper pain slut.  Are you sure you don't want to be my slavegirl?  We could experiment with all the different ways I could make you cum."
                            wt_image daughter_dungeon_7_1
                            "She shakes her head 'no'.  That isn't the life she wants.  She's not even sure she even really enjoyed the orgasm from being flogged, it felt more like something that happened to her, rather than something she participated in."
                            $ dee.orgasm_count += 1
                        elif dee.has_tag('aroused_now') and dee.has_tag('came_multiple_times_today'):
                            "*THWACCKK* ... and she trembles and grunts, but doesn't climax this time."
                            dee.c "NNNNNN"
                            wt_image daughter_dungeon_7_1
                            "It seems you've flogged as many orgasms out of her today as her body is capable of giving.  She stares ahead, her eyes almost vacant, as she struggles to deal with the combination of pain and pleasure radiating from her wet and beaten cunt out to every part of her body."
                        elif dee.has_tag('aroused_now'):
                            "*THWACCKK* ... and she groans not in pain, but in pleasure ..."
                            dee.c "nnnnnn"
                            wt_image daughter_dungeon_7_10
                            "... as her wet and puffy sex throbs from the stimulation of the flogging."
                        else:
                            "*THWACCKK* ... and she grunts once more."
                            dee.c "NNNNNN"
                            wt_image daughter_dungeon_7_11
                            "You let her sore, flogged cunt rest for a moment while you decide what to do with her next."
                        wt_image daughter_dungeon_7_4
                        jump menu_dee_gagged_back_menu
                    "Fuck her (ends session)" if dee.sex_count > 0:
                        wt_image daughter_dungeon_7_5
                        "You've fucked her before and she makes no sign of objecting as you step up between her bound legs ..."
                        wt_image daughter_dungeon_7_19
                        "... and prepare to fuck her again."
                        wt_image daughter_dungeon_7_20
                        if dee.has_tag('aroused_now'):
                            "She's slick with arousal and her pussy opens easily to accept your cock."
                        elif dee.has_tag('came_multiple_times_today'):
                            "She's still wet inside from her prior orgasms and her pussy opens easily to accept your cock."
                        elif dee.has_tag('came_today'):
                            "She's still wet inside from her prior orgasm and her pussy opens easily to accept your cock."
                        else:
                            "Carefully and slowly you push your cock gently against her opening until her body warms up enough to let you inside."
                        wt_image daughter_dungeon_7_21
                        if dee.has_tag('aroused_now') and dee.has_tag('came_multiple_times_today'):
                            "The inside of her cunt is warm and tight and feels great around your cock.  Your cock probably feels good to her, too, but she's exhausted from her prior orgasms and doesn't seem to have capacity for another today.  She just lies there and moans softly into her gag as you grip her by the tits and fuck her bound body ..."
                            wt_image daughter_dungeon_7_22
                            "... until you fill her with your seed."
                            player.c "[player.orgasm_text]"
                        elif dee.has_tag('aroused_now') and dee.has_tag('came_today'):
                            add tag 'came_multiple_times_today' to dee
                            "The inside of her cunt is warm and tight and feels great around your cock.  It seems your cock feels great to her, as well.  Even though she's alrady cum once today, as you grip her by the tits and fuck her bound body, you feel her tense up ..."
                            wt_image daughter_dungeon_7_22
                            "... and cum, groaning into her gag just as you're filling her with your seed."
                            dee.c "nnnn NNNNNNN!!!"
                            player.c "[player.orgasm_text]"
                            $ dee.orgasm_count += 1
                        elif dee.has_tag('aroused_now'):
                            add tag 'came_today' to dee
                            "The inside of her cunt is warm and tight and feels great around your cock.  It seems your cock feels great to her, as well.  As you grip her by the tits and fuck her bound body, you feel her tense up ..."
                            wt_image daughter_dungeon_7_22
                            "... and cum, groaning into her gag just as you're filling her with your seed."
                            dee.c "nnnn NNNNNNN!!!"
                            player.c "[player.orgasm_text]"
                            $ dee.orgasm_count += 1
                        elif dee.has_tag('came_multiple_times_today'):
                            "The inside of her cunt is warm and tight and feels great around your cock.  Her sex is sensitive from the prior orgasms and she moans softly into her gag as lies there while you grip her by the tits and fuck her bound body ..."
                            wt_image daughter_dungeon_7_22
                            "... until you fill her with your seed."
                            player.c "[player.orgasm_text]"
                        elif dee.has_tag('came_today'):
                            "The inside of her cunt is warm and tight and feels great around your cock.  Her sex is sensitive from the prior orgasm and she moans softly into her gag as lies there while you grip her by the tits and fuck her bound body ..."
                            wt_image daughter_dungeon_7_22
                            "... until you fill her with your seed."
                            player.c "[player.orgasm_text]"
                        else:
                            "The inside of her cunt is warm and tight and feels great around your cock.  Gripping her firmly by the tits, you fuck her bound body ..."
                            wt_image daughter_dungeon_7_22
                            "... until you fill her with your seed."
                            player.c "[player.orgasm_text]"
                        add tags 'bound_sex_before' to dee
                        $ dee.sex_count += 1
                        orgasm
                    "Nothing else (ends session)":
                        if dee.has_any_tag('aroused_now', 'came_today', 'came_multiple_times_today'):
                            change player energy by -energy_short
                        else:
                            change player energy by -energy_very_short
                if dee.has_tag('came_multiple_times_today'):
                    wt_image daughter_dungeon_talk_1
                    "After release her from her bonds, [dee.name] smiles at you while she catches her breath."
                    wt_image daughter_dungeon_talk_4
                    dee.c "That was intense.  You certainly know how to give a girl interesting experiences."
                elif dee.has_tag('came_today'):
                    wt_image daughter_dungeon_talk_1
                    "After release her from her bonds, [dee.name] smiles at you while she catches her breath."
                    wt_image daughter_dungeon_talk_4
                    dee.c "I'll give you this, a visit to your dungeon is rarely boring!"
                else:
                    wt_image daughter_dungeon_talk_2
                    "After you release her from her bonds, [dee.name] takes a moment before she dresses and leaves."
                    dee.c "You really seem to enjoy having me helpless.  It's kind of creepy, but it's definitely a learning experience about what goes on in the mind when you're subjected to that sort of domination."
                rem tags 'aroused_now' 'came_today' 'came_multiple_times_today' 'cropped_pussy_today' 'flogged_today' 'flogged_to_orgasm_today' from dee
                notify
                call forced_movement(living_room) from _call_forced_movement_1022
            "Suspension bondage" if dungeon.has_item(suspension_gear):
                if not current_location == dungeon:
                    call forced_movement(dungeon) from _call_forced_movement_1023
                wt_image daughter_dungeon_8_1
                if not dee.has_tag('suspended_before'):
                    "[dee.name] doesn't seem concerned about you tying her up ..."
                    wt_image daughter_dungeon_8_2
                    "... until you hoist her into the air."
                    wt_image daughter_dungeon_8_3
                    dee.c "Holy shit!!  Is this safe??!!"
                    wt_image daughter_dungeon_8_4
                    $ title = "What do you tell her?"
                    menu:
                        "It is as long as you don't squirm around too much":
                            pass
                        "I don't know, this is the first time I've done this":
                            pass
                        "Hopefully it is now that I've made a few adjustments":
                            pass
                    wt_image daughter_dungeon_8_3
                    dee.c "Are you serious???"
                    wt_image daughter_dungeon_8_5
                    player.c "I'm kidding, [dee.name].  You're perfectly safe.  Relax and just enjoy the sensation."
                    wt_image daughter_dungeon_8_6
                    "She tries, but you can't help but notice that she seems to be trying hard not to move, just in case she accidentally causes herself to fall."
                    wt_image daughter_dungeon_8_8
                    "You let her hang there long enough to become comfortable with the idea that she isn't about to plummet helplessly to the hard floor, then proceed."
                else:
                    "[dee.name] tries to remain calm, but she's breathing quickly as you tie her to the suspension gear ..."
                    wt_image daughter_dungeon_8_2
                    "... and comes close to hyper-ventilating as you hoist her into the air."
                    wt_image daughter_dungeon_8_5
                    player.c "Relax, [dee.name].  You're safe, remember?"
                    wt_image daughter_dungeon_8_7
                    "You hear taking slow, deep breaths to calm herself.  It works.  Soon she's hanging peacefully while you eye her up and decide what you want to do with her."
                wt_image daughter_dungeon_8_9
                $ title = "What do you want to do with her?"
                menu menu_dee_suspension_bondage_menu:
                    "Give her a spin":
                        wt_image daughter_dungeon_8_8
                        "Taking hold of one knee ..."
                        wt_image daughter_dungeon_8_4
                        "... you spin her as she hangs helplessly."
                        wt_image daughter_dungeon_8_3
                        dee.c "Oh fuck!!"
                        wt_image daughter_dungeon_8_5
                        "She spins around ..."
                        wt_image daughter_dungeon_8_4
                        "... and around ..."
                        wt_image daughter_dungeon_8_6
                        if dee.has_tag('aroused_now'):
                            "... until her momentum slows and she comes to rest, a little dizzy but otherwise none the worst for wear ..."
                            wt_image daughter_dungeon_8_14
                            "... and still pleasingly wet and aroused."
                        else:
                            "... until her momentum slows and she comes to rest, a little dizzy but otherwise none the worst for wear."
                        wt_image daughter_dungeon_8_9
                        jump menu_dee_suspension_bondage_menu
                    "Crop her" if dungeon.has_item(floggers):
                        wt_image daughter_dungeon_8_10
                        if dee.has_tag('cropped_today'):
                            dee.c "Oh no!  Not again?"
                        else:
                            "[dee.name] gasps in nervous anticipation as you pick up the crop."
                        $ title = "Where do you want to crop her?"
                        menu menu_dee_suspension_cropping_menu:
                            "Thigh":
                                add tags 'cropped_today' to dee
                                wt_image daughter_dungeon_8_11
                                "*thwackkk*"
                                wt_image daughter_dungeon_8_10
                                dee.c "Ow!"
                                jump menu_dee_suspension_cropping_menu
                            "Foot":
                                add tags 'cropped_today' to dee
                                wt_image daughter_dungeon_8_12
                                "*thwackkk*"
                                wt_image daughter_dungeon_8_10
                                dee.c "OW!!"
                                jump menu_dee_suspension_cropping_menu
                            "Breast":
                                add tags 'cropped_today' to dee
                                wt_image daughter_dungeon_8_13
                                "*thwackkk*"
                                wt_image daughter_dungeon_8_10
                                dee.c "OW!!"
                                jump menu_dee_suspension_cropping_menu
                            "Pussy" if not dee.has_tag('cropped_pussy_today'):
                                add tags 'cropped_today' 'cropped_pussy_today' to dee
                                wt_image daughter_dungeon_8_14
                                "*thwackkk*"
                                wt_image daughter_dungeon_8_15
                                if dee.has_tags('aroused_now'):
                                    rem tags 'aroused_now' from dee
                                    dee.c "OOWWW!!!"
                                    "[dee.name] is no masochist.  Whatever arousal she had been feeling is brought to a quick end by the intense pain.  Best not to try that when she's not aroused, she's unlikely to be able to tolerate it."
                                else:
                                    dee.c "OOWWW!!!  No, not there!!"
                                    "[dee.name] is no masochist.  Best not to try that when she's not aroused, she's unlikely to be able to tolerate it."
                                wt_image daughter_dungeon_8_10
                                jump menu_dee_suspension_cropping_menu
                            "Aroused pussy" if dee.has_tag('cropped_pussy_today') and dee.has_tag('aroused_now'):
                                rem tags 'aroused_now' from dee
                                wt_image daughter_dungeon_8_14
                                "*thwackkk*"
                                wt_image daughter_dungeon_8_15
                                dee.c "OOWWW!!!"
                                wt_image daughter_dungeon_8_10
                                "That killed the arousal she had been feeling."
                                jump menu_dee_suspension_cropping_menu
                            "That's enough for now":
                                wt_image daughter_dungeon_8_8
                                "[dee.name] watches with relief as you put the crop down."
                                wt_image daughter_dungeon_8_9
                                jump menu_dee_suspension_bondage_menu
                    "Choke her" if not dee.has_tag('choked_max_today'):
                        add tags 'choked_today' to dee
                        wt_image daughter_dungeon_8_19
                        "It's so easy to cut off her breath when she's suspended like this.  A little upward pressure on her throat and she loses all access to air."
                        "You hold her like this until she starts to squirm ..."
                        wt_image daughter_dungeon_8_20
                        "... then remove your hand and watch as she gasps for air."
                        wt_image daughter_dungeon_8_21
                        player.c "What do you say?  Should we do that again, only longer this time?"
                        "She's too focussed on catching her breath to say anything.  You don't think she enjoyed that, but she's not tappig out, either."
                        $ title = "What now?"
                        menu:
                            "Choke her again":
                                wt_image daughter_dungeon_8_19
                                "This time you maintain your grip, continuing to cut off her breath even after she starts squirming ..."
                                "... waiting until you see her start to panic ..."
                                wt_image daughter_dungeon_8_20
                                "... before you remove your hand and watch as she gasps for air."
                                wt_image daughter_dungeon_8_21
                                player.c "You look so cute when you start to turn blue.  How long can you go without breathing?  Shall we find out?"
                                "Still she says nothing, just sucks in as much air as she can."
                                menu:
                                    "Choke her again":
                                        add tags 'choked_max_today' to dee
                                        wt_image daughter_dungeon_8_19
                                        "She starts to squirm as soon as she feels your hand on her throat ..."
                                        "... as she fights for breath she can't get, her whole body shakes in her bonds.  She tries to move away, tries to remove her throat from your hand, but she can't."
                                        "It takes longer this time, but as she continues to go without air she panics again."
                                        wt_image daughter_dungeon_8_20
                                        "You immediately remove your hand and watch as she gasps for air, trembling in her bonds as she does so."
                                        wt_image daughter_dungeon_8_21
                                        player.c "This is fun.  Do you think you could go at least another 15 seconds?"
                                        dee.c "No, no more.  It's too scary."
                                        wt_image daughter_dungeon_8_8
                                        "You'll have to stop there for today."
                                    "Move on to something else":
                                        pass
                            "Move on to something else":
                                pass
                        wt_image daughter_dungeon_8_9
                        jump menu_dee_suspension_bondage_menu
                    "Pleasure her with your mouth":
                        if dee.has_tag('came_today') and dee.has_tag('aroused_now'):
                            wt_image daughter_dungeon_8_14
                            "Her cunt is wet and sensitive from her prior orgasm.  She probably doesn't feel any particular urge to cum again, but you expect you could make her cum anyway."
                        elif dee.has_tag('aroused_now'):
                            wt_image daughter_dungeon_8_14
                            "[dee.name] is wet and aroused from your prior attention, but you can make her wetter still."
                        else:
                            wt_image daughter_dungeon_8_16
                            "[dee.name] doesn't seem to be enjoying herself too much, but you can change that."
                        wt_image daughter_dungeon_8_7
                        "You pull her towards you ..."
                        wt_image daughter_dungeon_8_17
                        "... and bury your face in her sex, kissing, licking, nibbling and teasing her as she moans."
                        dee.c "oohhhhh"
                        wt_image daughter_dungeon_8_18
                        if dee.has_tag('came_today'):
                            "Soon her sex is puffy and wet and she's on the verge of cumming again."
                        elif dee.has_tag('aroused_now'):
                            "She wriggles side-to-side as best she can in suspension, trying to generate more contact with your mouth, desperate to cum."
                        else:
                            "Soon her sex is puffy and wet and she's on the verge of cumming."
                        $ title = "What now?"
                        menu:
                            "Make her cum again" if dee.has_tag('came_today'):
                                add tags 'came_multiple_times_today' to dee
                                wt_image daughter_dungeon_8_17
                                "You bury your face back between her legs and take her hard clit between your lips, sucking gently on it as you flick the tip of your tonue against it."
                                wt_image daughter_dungeon_8_15
                                dee.c "ohhh FUCCKKK!!!"
                                $ dee.orgasm_count += 1
                                $ dee.pleasure_her_count += 1
                            "Make her cum" if not dee.has_tag('came_today'):
                                add tags 'came_today' to dee
                                wt_image daughter_dungeon_8_17
                                "You bury your face back between her legs and take her hard clit between your lips, sucking gently on it as you flick the tip of your tonue against it."
                                wt_image daughter_dungeon_8_15
                                dee.c "ohhh FUCCKKK!!!"
                                $ dee.orgasm_count += 1
                                $ dee.pleasure_her_count += 1
                            "Stop there":
                                add tags 'aroused_now' to dee
                                wt_image daughter_dungeon_8_6
                                if dee.has_tag('came_today'):
                                    "She groans as you stop.  You're not sure if it's a groan of relief or a groan of disappointment, and you suspect she doesn't know, either."
                                else:
                                    "She groans in disappointment as she realizes you're stopping, when she's so close."
                                dee.c "oohhhh"
                        wt_image daughter_dungeon_8_9
                        jump menu_dee_suspension_bondage_menu
                    "Have her blow you (ends session)" if dee.has_any_tag('bound_bj_before', 'bj_thank_you', 'sex_before'):
                        wt_image daughter_dungeon_8_22
                        "She doesn't hesitate when you present your cock to her.  She opens her mouth to take you inside."
                        wt_image daughter_dungeon_8_23
                        "In this position she can't so much blow you as simply hang there and keep her soft lips formed in the shape of an 'O' ..."
                        wt_image daughter_dungeon_8_24
                        "... as you push and pull her head back and forth along your cock ..."
                        wt_image daughter_dungeon_8_25
                        "... until your balls fill her mouth with their spunk."
                        wt_image daughter_dungeon_8_26
                        player.c "[player.orgasm_text]"
                        if dee.has_tag('successful_swallow'):
                            wt_image daughter_dungeon_8_25
                            "She knows how to swallow, now, without making a fuss.  She slurps down the load ..."
                            wt_image daughter_dungeon_8_2
                            "... then waits patiently as you slowly lower her ..."
                            wt_image daughter_dungeon_8_1
                            "... until she's safely - and gratefully - back on the ground."
                            dee.c "Thank you for letting me down."
                            player.c "Did you think I wouldn't?"
                            if dee.has_tag('came_multiple_times_today'):
                                wt_image daughter_dungeon_talk_1
                                dee.c "No, but I think time works differently when you're suspended.  It felt like I was up there a lot longer than I actually was, and I'm happy to be back on the ground.  While I'm at it, thank you for the orgasms, too.  They felt nice."
                            elif dee.has_tag('came_today'):
                                wt_image daughter_dungeon_talk_1
                                dee.c "No, but I think time works differently when you're suspended.  It felt like I was up there a lot longer than I actually was, and I'm happy to be back on the ground.  While I'm at it, thank you for the orgasm, too.  It felt nice."
                            elif dee.has_tag('choked_today'):
                                wt_image daughter_dungeon_talk_3
                                dee.c "No, but I think time works differently when you're suspended.  It felt like I was up there a lot longer than I actually was.  Especially when you were choking me, that felt like it went on forever.  I'm happy to be back on the ground."
                            elif dee.has_tag('cropped_today'):
                                wt_image daughter_dungeon_talk_3
                                dee.c "No, but I think time works differently when you're suspended.  It felt like I was up there a lot longer than I actually was.  It probably felt like you were cropping me a lot longer than you actually were, too.  Regardless, I'm happy to be back on the ground."
                            else:
                                wt_image daughter_dungeon_talk_4
                                dee.c "No, but I think time works differently when you're suspended.  It felt like I was up there a lot longer than I actually was.  I'm happy to be back on the ground."
                        elif dee.has_tag('failed_swallow'):
                            wt_image daughter_dungeon_8_27
                            "... she still struggles to swallow your load, choking as your balls spurt into her ..."
                            wt_image daughter_dungeon_8_15
                            "... and then spitting out what she can after you finish cumming and remove your cock."
                            wt_image daughter_dungeon_8_2
                            "This isn't the right position to teach her to swallow, it's too awkward an angle, so you slowly lower her ..."
                            wt_image daughter_dungeon_8_1
                            "... until she's safely back on the ground."
                            wt_image daughter_dungeon_talk_3
                            player.c "Still haven't talked to your Mom about how to swallow, huh?"
                            wt_image daughter_dungeon_talk_2
                            if dee.ready_for_mom > 2:
                                dee.c "Nope, and if you think I'm going to bring her over again so we can both blow you at the same time, forget it.  That was a one time deal."
                            else:
                                dee.c "Ewww!  Would you quit suggesting that?  I'm sure you think you can convince me to bring my mother over so we can both blow you, but it's not going to happen."
                        else:
                            add tags 'failed_swallow' to dee
                            wt_image daughter_dungeon_8_27
                            if donna.has_tag('cum_slut'):
                                "She starts to choke and tries to pull back - unsuccessfully - as your sperm shoots into the back of her throat.  Unlike her mother, it seems [dee.name] hasn't acquired a taste for cum."
                            else:
                                "She starts to choke and tries to pull back  - unsuccessfully - as your sperm shoots into the back of her throat.  It seems [dee.name] doesn't enjoy, or at least doesn't have much experience with, the taste of cum."
                            wt_image daughter_dungeon_8_15
                            "When you finally finish, she gags slightly as she spits out as much of your load as she can."
                            wt_image daughter_dungeon_8_2
                            "Carefully you lower her back to the floor."
                            player.c "You okay?"
                            wt_image daughter_dungeon_8_1
                            dee.c "Yeah, I'm fine.  It's not easy catching your cum without choking when your cock is spurting like that."
                            player.c "I guess you don't have a lot of experience with giving blowjobs."
                            wt_image daughter_dungeon_talk_1
                            dee.c "I have a little, but most of the guys I've been with seemed to prefer facials.  I haven't had to try and catch a full load like that in my mouth very often.  It's trickier than it sounds."
                            if donna.has_tag('cum_slut'):
                                player.c "Maybe you should ask your Mom for tips on how she does it?  These days she doesn't even spill a drop, or if she does she scoops it back into her mouth to swallow it."
                            else:
                                player.c "Maybe you should ask your Mom for tips on how she does it?  She doesn't let as much dribble out as you do."
                            wt_image daughter_dungeon_talk_2
                            dee.c "Ewww!!  That conversation's not happening!"
                        $ dee.blowjob_count += 1
                        $ dee.swallow_count += 1
                        orgasm notify
                    "Fuck her (ends session)" if dee.sex_count > 0:
                        wt_image daughter_dungeon_8_28
                        "You've fucked her before and she makes no objection as you press the head of your cock against her sex and prepare to fuck her again."
                        wt_image daughter_dungeon_8_29
                        "Taking hold of her bound arms, you pull the hanging woman backwards onto your waiting shaft."
                        wt_image daughter_dungeon_8_30
                        if dee.has_tag('aroused_now'):
                            "She's slick with arousal and slides easily onto your cock with a moan."
                            wt_image daughter_dungeon_8_31
                            dee.c "oohhhh"
                        elif dee.has_tag('came_multiple_times_today'):
                            "She's still wet inside from her prior orgasms and slides easily onto your cock."
                        elif dee.has_tag('came_today'):
                            "She's still wet inside from her prior orgasm and slides easily onto your cock."
                        else:
                            "Carefully and slowly you pull her onto your cock as her sex stretches to accommodate you."
                        wt_image daughter_dungeon_8_32
                        "The inside of her cunt is warm and tight and feels great around your cock as you pull her back and forth along your shaft."
                        if dee.has_tag('aroused_now') and dee.has_tag('came_multiple_times_today'):
                            wt_image daughter_dungeon_8_33
                            "Your cock seems to feel good to her, too, but she's exhausted from her prior orgasms and doesn't seem to have capacity for another today."
                            wt_image daughter_dungeon_8_36
                            "Her wet, young cunt wrapped tightly around your dick, however, is more than enough stimulation to allow you to enjoy an intense, ball-emptying orgasm."
                        elif dee.has_tag('aroused_now') and dee.has_tag('came_today'):
                            add tag 'came_multiple_times_today' to dee
                            wt_image daughter_dungeon_8_33
                            "Your cock seems to feel great to her, as well."
                            wt_image daughter_dungeon_8_34
                            "Even though she's already cum once today, she tenses up and then spasms around your cock in another orgasm."
                            wt_image daughter_dungeon_8_35
                            dee.c "ohhh FUCCKKK!!!"
                            wt_image daughter_dungeon_8_36
                            "Her cunt felt great before, it feels almost unbearably great around your cock now, as it continues to twitch and spasm, sucking the sperm out of your balls."
                            $ dee.orgasm_count += 1
                        elif dee.has_tag('aroused_now'):
                            add tag 'came_today' to dee
                            wt_image daughter_dungeon_8_33
                            "Your cock seems to feel great to her, as well."
                            wt_image daughter_dungeon_8_34
                            "She tenses up and then spasms around your cock in orgasm."
                            wt_image daughter_dungeon_8_35
                            dee.c "ohhh FUCCKKK!!!"
                            wt_image daughter_dungeon_8_36
                            "Her cunt felt great before, it feels almost unbearably great around your cock now, as it continues to twitch and spasm, sucking the sperm out of your balls."
                            $ dee.orgasm_count += 1
                        elif dee.has_tag('came_multiple_times_today'):
                            wt_image daughter_dungeon_8_33
                            "Her sex is sensitive from the prior orgasms and she bites her lip in pleasure while you fuck her bound body ..."
                            wt_image daughter_dungeon_8_36
                            "... until her wet, young cunt milks the sperm from your balls."
                        elif dee.has_tag('came_today'):
                            wt_image daughter_dungeon_8_33
                            "Her sex is sensitive from her prior orgasm and she bites her lip in pleasure while you fuck her bound body ..."
                            wt_image daughter_dungeon_8_36
                            "... until her wet, young cunt milks the sperm from your balls."
                        else:
                            wt_image daughter_dungeon_8_36
                            "Her soft, young cunt wrapped tightly around your dick is soon triggers an intense, ball-emptying orgasm."
                        wt_image daughter_dungeon_8_37
                        player.c "[player.orgasm_text]"
                        wt_image daughter_dungeon_8_2
                        "When you've finished filling her young womb with seed, you slowly lower her ..."
                        wt_image daughter_dungeon_8_1
                        "... until she's safely - and gratefully - back on the ground."
                        dee.c "Thank you for letting me down."
                        player.c "Did you think I wouldn't?"
                        if dee.has_tag('came_multiple_times_today'):
                            wt_image daughter_dungeon_talk_1
                            dee.c "No, but I think time works differently when you're suspended.  It felt like I was up there a lot longer than I actually was, and I'm happy to be back on the ground.  While I'm at it, thank you for the orgasms, too.  They felt nice."
                        elif dee.has_tag('came_today'):
                            wt_image daughter_dungeon_talk_1
                            dee.c "No, but I think time works differently when you're suspended.  It felt like I was up there a lot longer than I actually was, and I'm happy to be back on the ground.  While I'm at it, thank you for the orgasm, too.  It felt nice."
                        elif dee.has_tag('choked_today'):
                            wt_image daughter_dungeon_talk_3
                            dee.c "No, but I think time works differently when you're suspended.  It felt like I was up there a lot longer than I actually was.  Especially when you were choking me, that felt like it went on forever.  I'm happy to be back on the ground."
                        elif dee.has_tag('cropped_today'):
                            wt_image daughter_dungeon_talk_3
                            dee.c "No, but I think time works differently when you're suspended.  It felt like I was up there a lot longer than I actually was.  It probably felt like you were cropping me a lot longer than you actually were, too.  Regardless, I'm happy to be back on the ground."
                        else:
                            wt_image daughter_dungeon_talk_4
                            dee.c "No, but I think time works differently when you're suspended.  It felt like I was up there a lot longer than I actually was.  I'm happy to be back on the ground."
                        add tags 'bound_sex_before' to dee
                        $ dee.sex_count += 1
                        orgasm
                    "Let her down (ends session)":
                        wt_image daughter_dungeon_8_2
                        "That's enough fun with her for today.  You slowly lower her ..."
                        wt_image daughter_dungeon_8_1
                        "... until she's safely - and gratefully - back on the ground."
                        dee.c "Thank you for letting me down."
                        player.c "Did you think I wouldn't?"
                        if dee.has_tag('came_multiple_times_today'):
                            wt_image daughter_dungeon_talk_1
                            dee.c "No, but I think time works differently when you're suspended.  It felt like I was up there a lot longer than I actually was, and I'm happy to be back on the ground.  While I'm at it, thank you for the orgasms, too.  They felt nice."
                        elif dee.has_tag('came_today'):
                            wt_image daughter_dungeon_talk_1
                            dee.c "No, but I think time works differently when you're suspended.  It felt like I was up there a lot longer than I actually was, and I'm happy to be back on the ground.  While I'm at it, thank you for the orgasm, too.  It felt nice."
                        elif dee.has_tag('choked_today'):
                            wt_image daughter_dungeon_talk_3
                            dee.c "No, but I think time works differently when you're suspended.  It felt like I was up there a lot longer than I actually was.  Especially when you were choking me, that felt like it went on forever.  I'm happy to be back on the ground."
                        elif dee.has_tag('cropped_today'):
                            wt_image daughter_dungeon_talk_3
                            dee.c "No, but I think time works differently when you're suspended.  It felt like I was up there a lot longer than I actually was.  It probably felt like you were cropping me a lot longer than you actually were, too.  Regardless, I'm happy to be back on the ground."
                        else:
                            wt_image daughter_dungeon_talk_4
                            dee.c "No, but I think time works differently when you're suspended.  It felt like I was up there a lot longer than I actually was.  I'm happy to be back on the ground."
                        if dee.has_any_tag('aroused_now', 'came_today', 'came_multiple_times_today'):
                            change player energy by -energy_short
                        else:
                            change player energy by -energy_very_short
                add tags 'suspended_before' to dee
                rem tags 'aroused_now' 'came_today' 'came_multiple_times_today' 'choked_today' 'choked_max_today' 'cropped_today' 'cropped_pussy_today' 'flogged_today' 'flogged_to_orgasm_today' from dee
                notify
                call forced_movement(living_room) from _call_forced_movement_1024
            "Fuck machine" if dungeon.has_item(fuck_machine):
                if not current_location == dungeon:
                    call forced_movement(dungeon) from _call_forced_movement_1025
                if dee.fuck_machine_ride_count == 0:
                    wt_image fm_image
                    "She looks at you suspiciously as you set up the fuck machine."
                    dee.c "What is that?"
                    player.c "You're in university, I'm sure you can guess.  Go on, lie down and take off your clothes."
                    wt_image daughter_machine_1_1
                    "She hesitates for a moment, then her curiosity gets the better of her.  She pulls off her skirt and lies down."
                    wt_image daughter_machine_1_2
                    player.c "Take off your top, too.  You get a ride, I want a show."
                    wt_image daughter_machine_1_3
                    "She pulls off her top and takes the dildo in her hand."
                    dee.c "Do I just put it inside me?"
                    wt_image daughter_machine_1_4
                    "She proceeds to do just that, pushing the dildo inside herself with surprising ease.  The whole situation is arousing her."
                    player.c "Lie back.  I'll adjust it for you."
                    wt_image daughter_machine_1_5
                    "She watches with curiousity as you adjust the dildo to the right position."
                    player.c "Ready?"
                    wt_image daughter_machine_1_6
                    dee.c "Ready for what?  What happens now?"
                    player.c "Now I turn it on."
                    wt_image daughter_machine_1_5
                    dee.c "Ohhh!!"
                    "[dee.name] startles as the machine begins to fuck her with a steady rhythm of *thump* ... *thump* ... *thump*"
                    player.c "Feels nice, huh?"
                    wt_image daughter_machine_1_6
                    dee.c "uh huh"
                    player.c "Kind of like being fucked by one of your college guys?"
                    wt_image daughter_machine_1_5
                    dee.c "A little."
                    "[dee.name] lies back, clearly enjoying the sensation as the machine continues to fuck her with a slow and steady *thump* ... *thump* ... *thump*"
                    player.c "How about now?"
                    wt_image daughter_machine_1_9
                    "You speed the machine up and watch as it stimulates the flow of fluids dripping out of the young woman's cunt ...  *thump*  *thump*  *thump*"
                    wt_image daughter_machine_1_7
                    dee.c "Oh shit!!  Ohhh!!!!"
                    wt_image daughter_machine_1_8
                    player.c "Still feel like some college guy fucking you?"
                    dee.c "Nooo ... oohhhh"
                    wt_image daughter_machine_1_9
                    "You crank the machine up another notch ... *THUMP* *THUMP* *THUMP*"
                    wt_image daughter_machine_1_10
                    dee.c "Ohhh FUCCKKKK!!!!"
                    wt_image daughter_machine_1_11
                    player.c "Do you need a minute?"
                    dee.c "Mmm hmmm"
                    "You give her some time to compose herself before she heads home, her knees still wobbly."
                elif dee.fuck_machine_ride_count == 1:
                    wt_image fm_image
                    "Her eyes sparkle when you bring out the fuck machine."
                    player.c "Looking forward to another ride?"
                    dee.c "Maybe a little."
                    wt_image daughter_machine_2_1
                    player.c "You need to say 'thank you' to the machine before you can ride it again."
                    dee.c "What do you mean?"
                    wt_image daughter_machine_2_2
                    player.c "You say 'thank you' to the machine.  With your mouth.  The way a woman should say 'thank you' for receiving pleasure."
                    dee.c "You want me to give head to a machine?"
                    wt_image daughter_machine_2_3
                    player.c "To thank it for the pleasure it gave you last time, and the pleasure you'll get today if it lets you mount it for another ride.  Yes."
                    "For a while, she tries to say 'no'. The memory of the intensity of her orgasm from the last ride, however, keeps flooding back into her head and soaking her pussy."
                    dee.c "Okay.  Fine."
                    wt_image daughter_machine_2_4
                    "She looks at the machine and gathers her resolve."
                    dee.c "You know this is humiliating, right?  Is that why you're doing it?"
                    player.c "Say 'thank you' to the machine, [dee.name]."
                    wt_image daughter_machine_2_5
                    "She kneels down in front of the dildo."
                    dee.c "Is this turning you on?"
                    player.c "I suggest you worry less about me and more about making the machine feel like you appreciate it."
                    wt_image daughter_machine_2_6
                    dee.c "Maybe it just wants a handjob?  That works for most guys."
                    player.c "College guys, maybe.  This machine knows how good it can make you feel and won't be satisfied unless you show it how grateful you truly are for the opportunity to be with it."
                    wt_image daughter_machine_2_7
                    "[dee.name] finally stops stalling and takes the dildo into her mouth, blowing it as if it were a real cock."
                    wt_image daughter_machine_2_8
                    "She keeps at it for an impressively long time, until you're sure her jaw must be aching.  It occurs to you that she's probably used to giving blowjobs as the main event, since college boys likely don't need any help to get hard, and so she isn't sure how long a warm up blowjob should last."
                    wt_image daughter_machine_2_6
                    "Eventually she stops to ask for guidance."
                    dee.c "Is it ready to fuck me, yet?"
                    wt_image daughter_machine_2_5
                    player.c "It will be once you spread your legs and show it how wet you are for it.  You are dripping wet and ready to impale yourself on it now, aren't you?"
                    wt_image daughter_machine_2_9
                    "She says nothing, just presses herself against the phallus ..."
                    wt_image daughter_machine_2_10
                    "... until it slips inside her sopping wet cunt."
                    wt_image daughter_machine_2_11
                    player.c "Ready?"
                    dee.c "Fuck yes!  Give it to me!!"
                    wt_image daughter_machine_2_12
                    "You flick the machine on, and it starts thrusting in and out of [dee.name]'s pussy ... *thump* ... *thump* ... *thump*"
                    wt_image daughter_machine_2_13
                    dee.c "Ohhh ... shit that feels good!"
                    player.c "Don't cum, yet.  It's about to feel better."
                    wt_image daughter_machine_2_14
                    "You speed up the machine and it starts thrusting more forcefully into her, pumping more and more wetness out of her ... *thump*  *thump*  *thump*"
                    wt_image daughter_machine_2_15
                    dee.c "Ohhhhh!!!  Shit that's fucking amazing!!  I'm going to ..."
                    player.c "Not yet.  It gets better"
                    wt_image daughter_machine_2_16
                    "You turn the speed up one more notch, sending the dildo pounding into her sex at full speed ... *THUMP* *THUMP* *THUMP*"
                    wt_image daughter_machine_2_17
                    dee.c "Ohhh FUCCKKKK!!!!"
                    wt_image daughter_machine_2_18
                    dee.c "This thing may ruin me for men.  Are women allowed to marry machines?"
                    player.c "You're the women's studies major, you tell me.  I'll leave the two of you alone to share your moment."
                elif dee.fuck_machine_ride_count > 1:
                    wt_image fm_image
                    "Her eyes sparkle when you bring out the fuck machine."
                    wt_image daughter_machine_2_3
                    dee.c "My favorite lover.  Most intense lover, anyway."
                    $ title = "What now?"
                    menu:
                        "Tell her to thank the machine":
                            wt_image daughter_machine_2_4
                            "She drops to her knees in front of the machine."
                            wt_image daughter_machine_2_6
                            dee.c "Just so you know, I still find this humiliating."
                            wt_image daughter_machine_2_7
                            player.c "I know.  The machine appreciates your submissiveness towards it.  So do I."
                            "You pat her on the head, stroking her hair as she pleasures the phallus."
                            wt_image daughter_machine_2_8
                            "When she's humiliated herself to your satisfaction, you let her lie back and take the dildo inside her."
                        "Just let her fuck it":
                            pass
                    wt_image daughter_machine_2_9
                    "Spreading her legs, she presses against the phallus ..."
                    wt_image daughter_machine_2_12
                    "... until it slips inside her already-wet cunt."
                    wt_image daughter_machine_2_11
                    "She trembles with excitement as she anticipates what comes next."
                    $ dee.temporary_count = 1
                    $ title = "What now?"
                    menu menu_dee_fuck_machine_menu:
                        "Tell her to turn over":
                            rem tags 'machine_slow' 'machine_medium' 'machine_fast' from dee
                            # note: stays above 1 so as to align with visit_end call
                            if dee.temporary_count > 1:
                                $ dee.temporary_count -= 1
                            if dee.has_tag('on_knees_now'):
                                wt_image daughter_machine_2_9
                                if dee.has_tag('turned_last'):
                                    dee.c "Make up your mind, already."
                                else:
                                    "She turns over and spreads her legs."
                                wt_image daughter_machine_2_12
                                "The dildo slides easily back into her wet cunt."
                                wt_image daughter_machine_2_11
                                rem tags 'on_knees_now' from dee
                                add tags 'turned_last' to dee
                            else:
                                wt_image daughter_machine_2_19
                                if dee.has_tag('turned_last'):
                                    dee.c "Make up your mind, already."
                                else:
                                    "Head down and ass up, she gets on all fours."
                                wt_image daughter_machine_2_20
                                "Reaching back with her hand, she guides the dildo back inside her."
                                wt_image daughter_machine_2_22
                                add tags 'on_knees_now' 'turned_last' to dee
                            jump menu_dee_fuck_machine_menu
                        "Set the machine to slow" if not dee.has_tag('machine_slow'):
                            add tags 'machine_slow' to dee
                            rem tags 'machine_medium' 'machine_fast' from dee
                            jump dee_fuck_machine_content
                        "Set the machine to medium" if not dee.has_tag('machine_medium'):
                            add tags 'machine_medium' to dee
                            rem tags 'machine_slow' 'machine_fast' from dee
                            jump dee_fuck_machine_content
                        "Set the machine to fast" if not dee.has_tag('machine_fast'):
                            add tags 'machine_fast' to dee
                            rem tags 'machine_slow' 'machine_medium' from dee
                            jump dee_fuck_machine_content
                        "Just watch" if dee.has_any_tag('machine_slow', 'machine_medium', 'machine_fast'):
                            jump dee_fuck_machine_content
                        "Stop (ends session)" if dee.has_any_tag('machine_slow', 'machine_medium', 'machine_fast'):
                            if dee.has_tag('came_today'):
                                wt_image daughter_machine_2_18
                                dee.c "Wow!!  I really think I should ask this machine to marry me.  I can't imagine anyone else could ever fuck me like that."
                            else:
                                wt_image daughter_machine_2_2
                                dee.c "But I haven't cum, yet?"
                                player.c "Sometimes finishing before you do is just part of the machine's boyfriend-experience."
                    rem tags 'came_today' 'came_multiple_times_today' 'machine_slow' 'machine_medium' 'machine_fast' 'on_knees_now' 'turned_last' from dee
                call forced_movement(living_room) from _call_forced_movement_1026
                $ dee.fuck_machine_ride_count += 1
                change player energy by -energy_very_short notify
            "Nothing (change your mind)":
                $ dee.temporary_count = 0
                wt_image daughter_house_1_1
                rem tags 'talked_domination_today' from dee
        if dee.temporary_count > 0:
            if donna.daughter_investigation_triggered == 3:
                "That's enough for her for today."
            call dee_visit_end from _call_dee_visit_end_14
    return

label dee_fuck_machine_content:
    # note: temporary_count starts at 1 when not excited (to align with visit_end test), drops to 2 after orgasm, she cums when reaches 5 or above
    rem tags 'turned_last' from dee
    if dee.has_tag('machine_slow'):
        $ dee.temporary_count += 1
        if dee.has_tag('on_knees_now'):
            wt_image daughter_machine_2_21
        else:
            wt_image daughter_machine_2_10
        "*thump* ... *thump* ... *thump*"
        # if not orgasm
        if dee.temporary_count < 5:
            if dee.has_tag('on_knees_now'):
                wt_image daughter_machine_2_22
            else:
                wt_image daughter_machine_2_11
            dee.c "ohhh"
    elif dee.has_tag('machine_medium'):
        $ dee.temporary_count += 2
        if dee.has_tag('on_knees_now'):
            wt_image daughter_machine_2_21
        else:
            wt_image daughter_machine_2_14
        "*thump*  *thump*  *thump*"
        # if not orgasm
        if dee.temporary_count < 5:
            if dee.has_tag('on_knees_now'):
                wt_image daughter_machine_2_22
            else:
                wt_image daughter_machine_2_13
            dee.c "Ohhhh!"
    else:
        $ dee.temporary_count += 3
        if dee.has_tag('on_knees_now'):
            wt_image daughter_machine_2_21
        else:
            wt_image daughter_machine_2_16
        "*THUMP* *THUMP* *THUMP*"
        # if not orgasm
        if dee.temporary_count < 5:
            if dee.has_tag('on_knees_now'):
                wt_image daughter_machine_2_22
            else:
                wt_image daughter_machine_2_15
            dee.c "Ohhhhh!!!"
    # if orgasm
    if dee.temporary_count > 4:
        $ dee.temporary_count = 2
        if dee.has_tag('on_knees_now'):
            add tags 'fuck_machine_used_from_behind' to dee
            wt_image daughter_machine_2_23
        else:
            wt_image daughter_machine_2_17
        dee.c "Ohhhh FUUCCKKK!!!"
        if dee.has_tag('came_multiple_times_today'):
            wt_image daughter_machine_2_18
            dee.c "No more!!  No more!  It's too intense.  I need to stop there."
            "You give her some time to recover, then send her home and go on with your day."
        elif dee.has_tag('came_today'):
            add tags 'came_multiple_times_today' to dee
            jump menu_dee_fuck_machine_menu
        else:
            add tags 'came_today' to dee
            jump menu_dee_fuck_machine_menu
    else:
        jump menu_dee_fuck_machine_menu
    return

## Post-Training Character Actions
# N/A

########### OBJECTS ###########
## Common Objects
# Contact Character
label dee_contact:
    rem tags 'contact_open' from dee
    if dee.ready_for_mom == 1:
        wt_image daughter_phone_1
        dee.c "I'll be right over and I'm bringing my Mom.  I'm going to do this, but I want your help.   Will you help me bring my Mom's fantasy to life?  I don't think I'm brave enough to try and do it on my own."
        $ dee.drop_idea = False
        $ title = "What do you tell her?"
        menu menu_dee_contact:
            "I'll be waiting for the two of you":
                $ dee.training_session()
                $ donna.training_session()
                summon donna
                summon dee
                wt_image daughter_donna_1_1
                "[donna.name] looks confused as [dee.name] brings her into your house."
                donna.c "[dee.name], why are we here?  How do you even know about this place?"
                dee.c "I know all about your training, Mom."
                wt_image daughter_donna_1_2
                donna.c "[dee.name], let me explain ..."
                dee.c "It's okay, Mom.  I understand why Dad arranged it for you.  I get what he was trying to do. You've always been a bit repressed, sexually. I think your time in training has been good for you.  I've been getting some training, too."
                wt_image daughter_donna_1_3
                donna.c "You have?  But you've always been so confident and ... well, I don't mean this in a bad way, sweetheart, but your sex life seems pretty active to me already.  And how could you afford the cost of the training?"
                dee.c "That's why we're here, Mom.  Mr. Wife Trainer hasn't been charging me for all the lessons he's been giving me. I guess it's some sort of family plan or student discount.  I wanted to thank him for all the help he's been giving me.  And as my mother, I knew you'd want to thank him, too, once you knew how much help he's been to me."
                wt_image daughter_donna_1_4
                donna.c "I ... I'm not entirely sure what to say.  But if my daughter feels like you've been helping her, especially helping her for free, then of course, I'm very grateful to you.  Thank you!"
                dee.c "Mom, it's really important to me that Mr. Wife Trainer feel appreciated."
                wt_image daughter_donna_1_5
                donna.c "Sweetheart, I just finished thanking him."
                dee.c "It wasn't much of a 'thank you', Mom.  You're going to do something special for him.  We both are."
                wt_image daughter_donna_1_6
                donna.c "[dee.name], you're embarrassing me.  I don't understand what you mean."
                dee.c "What I mean, Mom, is that you're going to take your top off and I'm going to do the same, and we're going to let him look at us together, mother and daughter."
                if donna.has_tag('bimbo'):
                    wt_image daughter_donna_1_8
                    donna.c "Oh, of course he'd enjoy that!  Should we take our skirts off, too?"
                    dee.c "I'm impressed, Mom.  I thought you'd be more nervous about this.  Yes, let's take our skirts off, too."
                    wt_image daughter_donna_1_11
                    donna.c "I'm not nervous taking my clothes off any more, [dee.name].  Mr. Wife Trainer taught me that.  I should be naked as often as possible.  Being naked with you feels even better than being naked on my own, and I bet this is the best 'thank you' we could give our trainer."
                    dee.c "Not the best 'thank you', Mom.  Can you guess what the really special thing is we're going to do together?"
                    wt_image daughter_donna_1_12
                    donna.c "I'm not good at guessing, [dee.name].  Can you do the guessing and the thinking for me?"
                    dee.c "I'd like that, Mom.  I'd like to make all the decisions for you."
                    wt_image daughter_donna_1_13
                    donna.c "I'd like that, too!  What should I do now?"
                    dee.c "Get on your knees, Mom.  I'll do the thinking from now on, but you have to help me with the sucking."
                    wt_image daughter_donna_1_12
                    donna.c "Sucking what?  Oh!  You mean ... [dee.name], I'm not sure that's appropriate.  I'm still your mother and ..."
                    dee.c "And you're going to stop trying to think for yourself and let me decide what's right and wrong from now on.  Let's finish our special thank you to Mr. Wife Trainer.  Get on your knees and open your mouth, Mom."
                else:
                    wt_image daughter_donna_1_3
                    if donna.has_tag('stripped'):
                        donna.c "[dee.name], I don't know if that's appropriate ..."
                        dee.c "Hush, Mom.  I want to do something special for Mr. Wife Trainer, so he feels appreciated. You'd like to see us with our tops off, wouldn't you?"
                        player.c "Yes, I would."
                        wt_image daughter_donna_1_6
                        "[donna.name] blushes."
                        dee.c "There, that's settled."
                        donna.c "[dee.name] ..."
                        wt_image daughter_donna_1_7
                        dee.c "I'm not taking 'no' for an answer, Mom.  You need to start listening to me more often.  Take your top off."
                    else:
                        donna.c "[dee.name], sweetheart, I'm not comfortable taking off my clothes."
                        dee.c "Don't be silly, Mom, you're beautiful."
                        wt_image daughter_donna_1_6
                        "[donna.name] blushes."
                        donna.c "I'm an old woman and I have an old woman's body.  You wouldn't understand."
                        dee.c "Don't be silly.  I want to see your body.  You want to see her body, too, don't you?"
                        player.c "Yes, I do."
                        wt_image daughter_donna_1_7
                        dee.c "There, that's settled.  I'm not taking 'no' for an answer, Mom. You need to start listening to me more ofte.  Take your top off."
                    donna.c "I'm going to look so ugly compared to you ..."
                    wt_image daughter_donna_1_9
                    dee.c "Mom, you're beautiful."
                    donna.c "Except for my ..."
                    dee.c "Mom, shut up now and say 'thank you' to Mr. Wife Trainer."
                    wt_image daughter_donna_1_10
                    donna.c "Oh [dee.name], you always make me feel comfortable, even when I'm doing something ridiculous.  Thank you, Mr. Wife Trainer, for helping my daughter and me."
                    dee.c "Good, Mom.  Now let's take our skirts off."
                    wt_image daughter_donna_1_12
                    donna.c "[dee.name], how far are you planning on going with this?"
                    dee.c "Just smile and do what I tell you to do, Mom."
                    wt_image daughter_donna_1_11
                    donna.c "Okay, [dee.name], I trust you.  I'll do as you say."
                    dee.c "That's the deferential Mom I love.  See how much easier things are when you're obedient?  Let's finish our special thank you to Mr. Wife Trainer.  Get on your knees and open your mouth, Mom."
                wt_image daughter_donna_1_14
                "As you remove your clothes, [dee.name] guides her mother to her knees in front of you.  [donna.name] looks nervous, but allows her daughter to place your cock in her mouth."
                dee.c "That's it, Mom.  Don't think, don't question.  Just trust me and do as I tell you.  Suck his cock, Mom."
                if donna.sex_experience < 2:
                    call donna_first_bj_with_you from _call_donna_first_bj_with_you_11
                wt_image daughter_donna_1_15
                "As [donna.name] suckles gently on you and slides her lips up and down your shaft, her daughter joins in and licks and suckles your balls."
                wt_image daughter_donna_1_16
                "Then they both lick your shaft as they change positions ..."
                wt_image daughter_donna_1_17
                "... and [dee.name] sucks your cock while her mother licks your balls.  As incredible as this feels, it's time to push [donna.name] to go further."
                wt_image daughter_donna_1_18
                player.c "Look at your daughter, [donna.name].  She's so beautiful and has such a sexy mouth.  And her tongue is so talented.  Can you imagine how hard her nipples get when you squeeze her soft her tits?  How good her hot tongue feels when it licks you?"
                wt_image daughter_donna_1_19
                "Emboldened by your encouragement of her mother's fantasy, [dee.name] takes over from there."
                wt_image daughter_donna_1_20
                dee.c "Lie down while I do the sucking for a few minutes, Mom."
                wt_image daughter_donna_1_21
                "[donna.name] closes her eyes and caresses her daughter's hair as [dee.name] sucks your cock between her mother's wide-spread legs.  You can see [donna.name]'s sex open and moisten in excitement and you're confident that has more to do with the proximity of her daughter's mouth than your cock."
                wt_image daughter_donna_1_22
                player.c "Don't be shy, [donna.name].  Tell your daughter what you want."
                donna.c "oohhh  ooohhhh"
                wt_image daughter_donna_1_20
                dee.c "What is it Mom?  Say it.  Say what you want."
                donna.c "Ummm, his cock?"
                wt_image daughter_donna_1_23
                dee.c "Really?  Is that what those moans were about?  I'd better let you suck on him for a while, then."
                "As [donna.name] does so, [dee.name] positions her wet pussy directly above her mother's face."
                wt_image daughter_donna_1_24
                dee.c "Make him hard for me, Mom, I'm going to let him fuck me.  If you do a good job, I might let you fluff some of my other lovers in the future."
                wt_image daughter_donna_1_25
                "You pull your cock out of [donna.name]'s mouth and push it inside her daughter's waiting sex.  [dee.name]'s pussy stretches easily to take you in, but it's her mother that moans as you penetrate [dee.name], sending some of her pussy juice dripping onto her mother's face."
                donna.c "oohhh  ooohhhh"
                wt_image daughter_donna_1_26
                dee.c "Oh Mom, his cock feels so good inside me.  See how excited my pussy is?  I'm so wet my cunt juices are leaking everywhere."
                "[donna.name] looks up at, and then away from, her daughter's pussy, embarrassed and ashamed at her own body's response to the sight of her daughter's arousal."
                wt_image daughter_donna_1_27
                dee.c "Goodness, Mom!  I'm not the only one getting excited, am I?  His cock must look even better than I realized, because your cunt is so wet I can smell it from here.  Why don't you get out from under there and sit in front of me."
                wt_image daughter_donna_1_28
                "Anxious to avoid embarrassing herself further, [donna.name] scrambles away as directed.  Her hopes of avoiding more shame are crushed, however, when [dee.name] grabs her by the hips and positions her face over [donna.name]'s sex."
                dee.c "Let me help you with that dripping cunt, Mom.  I've decided I'm going to keep Mr. Wife Trainer's cock for myself this evening, I don't want him fucking you after he's been inside me.  But don't worry, I'll take care of you myself."
                wt_image daughter_donna_1_29
                donna.c "[dee.name]!  No!!"
                wt_image daughter_donna_1_30
                dee.c "Hush, Mom.  It's okay."
                wt_image daughter_donna_1_31
                "As [dee.name] brings her mother's fantasy to life, you pound in and out of her, trying hard to control your excitement.  You don't want to cum and bring your participation to a premature end."
                wt_image daughter_donna_1_32
                "Delaying your orgasm becomes more and more difficult, as [dee.name] brings her mother to one climax after another at the end of her talented tongue."
                donna.c "oohhh  oh!  OH!  oohhh  Gaawwdddd!!!  OH!!  Oh Gaaawwddd!!!!"
                wt_image daughter_donna_1_33
                dee.c "Your turn, Mom."
                wt_image daughter_donna_1_34
                donna.c "[dee.name], I ... mmpphhh"
                "[dee.name] ignores her mother's protests and pulls her head between her legs as she takes your cock into her mouth."
                wt_image daughter_donna_1_35
                dee.c "Ohhh FUCCKKKK!!!!"
                wt_image daughter_donna_1_36
                "The sight of [donna.name] licking her daughter to a quick orgasm eliminates everything that was left of your self-control.  As you cum, she pushes your cock out of her mouth ..."
                player.c "[player.orgasm_text]"
                wt_image daughter_donna_1_37
                "... swallowing some of your load while the rest spurts onto her face."
                dee.c "Shit, I thought I was going to choke when you started cumming with my head hanging back like that."
                if donna.has_tag('cum_slut'):
                    wt_image emp_nest_hypno_bj_4
                    donna.c "Cum  Cum"
                    dee.c "Mom, are you okay?"
                    player.c "Your Mom gets intense cravings for sperm sometimes.  It'll pass, but it's hard for her to see sperm without wanting to taste it."
                    wt_image daughter_donna_1_38
                    dee.c "Here, Mom.  It's okay, I have sperm for you."
                    donna.c "Cum!  Cum!"
                    wt_image daughter_donna_1_39
                    "[donna.name] leans over and licks your cum off her daughter's face."
                    dee.c "Is that better, Mom?"
                    wt_image daughter_donna_1_40
                    "[donna.name] keeps licking, her tongue slipping between her daughter's lips in the search for more of your sperm."
                    donna.c "Cum.  Cum."
                    wt_image daughter_donna_1_41
                    dee.c "That's all the sperm I have for you, Mom, but I have something else you can lick up."
                    wt_image daughter_donna_1_42
                    donna.c "Cum?  Cum?"
                    wt_image daughter_donna_1_43
                    dee.c "Yes, Mom.  It's girl cum and I want you to get used to the taste of it, because you're going to be drinking a lot of it whenever I'm home and feeling horny."
                    $ donna.cum_slut_visit_week += 1
                else:
                    player.c "It's okay, you look good like that.  Doesn't she, [donna.name]?"
                    wt_image daughter_donna_1_44
                    donna.c "You always looks beautiful, [dee.name], but I'm sorry about what just happened.  I should never have done that with you.  I should never have let things go this far."
                    dee.c "That's enough with the self-doubts, Mom.  What happend today is something I wanted to happen.  Clean the sperm off my face and kiss me."
                    wt_image daughter_donna_1_45
                    "[donna.name] blushes as she dutifully cleans your cum off her daughter's face and then kisses her on the lips."
                    wt_image daughter_donna_1_41
                    donna.c "You're really not mad at me?"
                    dee.c "No, Mom.  If I was, I'd punish you, but I'm never going to be mad at you for doing what you're told.  Speaking of which, put your head back between my legs, Mom."
                    wt_image daughter_donna_1_44
                    donna.c "[dee.name], we shouldn't ..."
                    dee.c "Stop talking, Mom.  Put your mouth between my legs and keep it there until I'm finished with you."
                    wt_image daughter_donna_1_42
                    dee.c "You need practice in eating cunt, Mom.  When I'm home and feeling horny, I'm going to expect you to provide me with relief, and I expect you to do so at least as well as the girls in my dorm."
                    wt_image daughter_donna_1_43
                    "It's exactly the way [donna.name] imagined it.  Her flat on her belly, following the instructions of her talented, amazing, self-confident daughter.  And if it's not exactly the fantasy [dee.name] had growing up, she at least now has something else to look forward to on her trips home from university.  A way for her and her Mom to spend some quality time together while her laundry is getting done."
                if not donna.has_tag('stripped'):
                    "Through all the excitement, you forgot to ask [donna.name] about the piercing through her clit hood.  That seems out of character for a suburban housewife. But then, not many suburban housewives engage in her current behavior, either.  You give her and her daughter some alone time."
                    add tags 'stripped' to donna
                else:
                    "You give [donna.name] and her daughter some alone time to explore their new relationship."
                $ dee.sex_count += 1
                $ dee.facial_count += 1
                $ dee.ready_for_mom = 3
                if not donna.has_tag('likes_girls'):
                    call convert(donna, 'lesbian') from _call_convert_194
                    "Having sex with her daughter for the first time makes [donna.name] realize she enjoys sexual contact with women just as much as she does with men, at least when it's with the right woman."
                call character_location_return(donna) from _call_character_location_return_746
                call character_location_return(dee) from _call_character_location_return_747
                orgasm notify
                wt_image current_location.image
            "Maybe this isn't a great idea" if not dee.drop_idea:
                player.c "I'm not sure this is a great idea, [dee.name].  I know I encouraged you to think about it, but perhaps you should let your Mom's fantasy stay exactly that - a fantasy."
                dee.c "But ... it's kind of becoming my fantasy, too.  Ever since you told me about it, it's the most intense sexual thought I've ever had in my entire life.  I need to do this.  Please, won't you help me?"
                $ dee.drop_idea = True
                $ title = "What do you tell her?"
                jump menu_dee_contact
            "Drop the idea" if dee.drop_idea:
                $ dee.training_session()
                player.c "I'm glad you've found a new fantasy to get yourself wet over, but having sex with your Mom for real is just going to mess things up.  If I were you, I'd drop the whole idea."
                dee.c "I guess you're right.  I think I'll take some time and think about it some more.  I'll catch up with you some other time."
                $ dee.ready_for_mom = 2
                wt_image current_location.image
            "Come over alone today":
                player.c "Let's hold off on bringing your Mom over.  How about you just come visit on your own for today?"
                dee.c "Okay"
                call dee_visit from _call_dee_visit_2
            "Cancel her visit":
                player.c "Right now isn't good for me.  I'll let you know when I'm ready for the two of you."
                add tags 'contact_open' to dee
                $ dee.drop_idea = False
                wt_image current_location.image
    elif dee.ready_for_mom == 3:
        if donna.has_tag('post_continuing_actions'):
            $ title = "Suggest a threesome with her Mom?"
        else:
            $ title = "Ask her to bring her Mom?"
        menu:
            "Yes, arrange a threesome":
                if not dee.has_tag('continuing_mom_threesomes'):
                    wt_image daughter_phone_1
                    if donna.has_tag('post_continuing_actions'):
                        player.c "Come on over, [dee.name].  I'd like to spend some time with you and your Mom together."
                    else:
                        player.c "Come on over, [dee.name].  Feel free to bring your Mom with you."
                    dee.c "That was a one time deal.  What Mom and I do together now is strictly between her and me.  But I will drop by to see you."
                    if dee.talk_sex_life_status > 9:
                        add tags 'continuing_mom_threesomes' to dee
                        player.c "Is that how [dee_ra.name] would see it, I wonder?  I bet she'd love to have your mother visit the dorm.  Do you think you could dom your Mom while [dee_ra.name] doms you, or would [dee_ra.name] figure out how to control both of you?"
                        dee.c "I don't want to find out.  I'll get Mom and we'll both be right over."
                        call dee_visit_continuing_mom_threesome from _call_dee_visit_continuing_mom_threesome
                    elif dee.talk_sex_life_status > 6:
                        add tags 'continuing_mom_threesomes' to dee
                        player.c "Now, now.  Don't get possessive.  I helped you take control of [dee_ra.name].  The least you can do is give me access to you and your Mom when I'm in the mood."
                        dee.c "I guess.  Okay, I'll get Mom and we'll both be right over."
                        call dee_visit_continuing_mom_threesome from _call_dee_visit_continuing_mom_threesome_1
                    else:
                        $ title = "Have [dee.name] visit you alone?"
                        menu:
                            "Yes, have [dee.name] visit you":
                                call dee_visit from _call_dee_visit_3
                            "No, not today":
                                pass
                else:
                    call dee_visit_continuing_mom_threesome from _call_dee_visit_continuing_mom_threesome_2
            "No, just have [dee.name] visit":
                call dee_visit from _call_dee_visit_4
            "Never ask for a threesome (shuts this menu off)":
                $ dee.ready_for_mom = 4
                call dee_visit from _call_dee_visit_5
    else:
        call dee_visit from _call_dee_visit
    return

label dee_ra_contact:
    if dee.talk_sex_life_status == 2:
        "[dee.name]'s relationship with her RA is clearly going nowhere, so messing around with it isn't going to cost her true love or anything.  It might even help the two women.  The question is how to approach it."
        "There's no point is just telling them 'take turns being switches', because that's not what either wants.  You're going to need to push one or the other to accept and enjoy a submissive role, but that's not going to be easy, either, as their power struggle has fallen into a predictable stalemate."
        "The first thing you'll need to do is to shake them out of the routine they're in.  If you call [dee.name]'s RA, you may be able to prod her into changing things up a bit."
        $ title = "Call [dee.name]'s RA?"
        menu:
            "Yes":
                wt_image phone_1
                "Tracking down the dorm where [dee.name] lives and leaving a message for the RA on her floor proves relatively easy.  You have to wait a few minutes for her to reply, but eventually she does."
                wt_image daughter_ra_1_24
                dee_ra "You called about [dee.name]?  Am I supposed to know who you are?"
                player.c "A friend of the family.  I know all about you, [dee_ra.name], and your relationship with [dee.name]."
                dee_ra "What's that supposed to mean?"
                player.c "It means I think you like her and she likes you, too.  But she's thinking about putting an end to the little arrangement the two of you have and I thought you'd want to know.  If you don't want to lose her, I'd suggest you make some changes."
                "There's a long pause as the young woman decides whether and how to respond."
                dee_ra "I don't know what you're talking about, but say I did.  What sort of change are you talking about?"
                player.c "Anything other than what the two of you have been doing everytime you sleep together.  You're both too young to fall into a boring routine so fast.  You're the older one in this relationship, find something new and exciting to do with her, or she'll move on to someone else who will."
                wt_image current_location.image
                "You hang up.  The next time [dee.name] comes to visit, you can ask about their relationship again and find out if [dee_ra.name] acted on your advice or not."
                $ dee.talk_sex_life_status = 3
            "Not now":
                pass
    elif dee.talk_sex_life_status == 4:
        if dee.marilyn_event_status == 0:
            "Wait until [dee.name] has a submissive experience with another woman that you can tell her RA about."
        elif dee.has_tag('strapon_story_told'):
            $ title = "Do you want to tell her RA how she can better dominate [dee.name]?"
            menu:
                "Yes":
                    wt_image daughter_ra_1_24
                    "[dee_ra.name] returns your call much quicker today."
                    player.c "I hear you've spiced things up with [dee.name].  Are you enjoying your relationship the way it is now?"
                    dee_ra "It's nice, yes.  Did you have an idea of how it could be better?"
                    player.c "What would be better for you?  Are you hoping to marry her someday or are you just intersted in having her as your submissive sextoy for the semester?"
                    "The young woman hesitates, unsure about how to respond."
                    dee_ra "You said you were a friend of her family?"
                    player.c "Relax.  You showed you could get the upper hand on [dee.name], which isn't easy.  You know she'd like to turn the tables on you.  I'm sure she fights you every time you try to dominate her.  Here's some advice.  Buy a strap-on and give her a time limit on how long has to cum while you're using it on her."
                    wt_image current_location.image
                    "Be sure to talk to [dee.name] about her sex life the next time she visits, to find out whether her RA followed through on your suggestion or not."
                    $ dee.talk_sex_life_status = 5
                "Not today":
                    pass
        else:
            "You didn't learn enough about [dee.name]'s time with Marilyn to have any secrets to share with her RA.  Maybe you'll get an opportunity later to hear more."
    return

label dee_visit:
    summon dee
    rem tags 'no_hypnosis' from dee # to allow hypnosis while she's visiting you
    $ dee.visit_count += 1
    # first visit
    if dee.visit_count == 1:
        call dee_first_visit from _call_dee_first_visit
    # subsequent visits
    elif dee.visit_count > 1:
        wt_image daughter_house_1_1
        "[dee.name] comes right over."
        # Marilyn event described
        if dee.marilyn_event_status == 1:
            player.c "Tell me how your meeting with Marilyn went."
            wt_image daughter_house_1_2
            dee.c "Ummm.  What did she tell you?"
            player.c "Nothing.  Why, what happened?"
            wt_image daughter_marilyn_1
            dee.c "{i}She met up with me on campus, in a pretty fancy limo. I think she was traveling between business meetings. I didn't pry. Anyway, it was really kind of her to drop by the university and make time to meet with me.{/i}"
            "[dee.name] has good instincts.  Not prying is a good policy when it comes to Marilyn, which is why you didn't ask why she was visiting [dee.name]'s university town in the first place, or why she had dyed her hair blonde while she was there."
            player.c "{i}Did the two of you hit it off right away?{/i}"
            wt_image daughter_marilyn_2
            dee.c "{i}Sort of. I felt a bit ... maybe a little star struck meeting her? She's this important powerful business woman pulling up to meet me in an expensive limousine. I must have seemed like the most awkward foolish kid overwhelmed at the opportunity to chat with her.{/i}"
            player.c "{i}Did you have lots of questions for her?{/i}"
            wt_image daughter_marilyn_15
            dee.c "{i}I had a bunch planned, yes. But, she's rather ... intimidating.  I felt I was flustered the whole time I was with her, especially ...{/i}"
            player.c "{i}Especially when?{/i}"
            "[dee.name] hesitates for a moment before continuing."
            wt_image daughter_marilyn_3
            dee.c "{i}Especially when she kept putting her hand on my knee. I think she was doing it to reassure me, but I found it rather distracting.{/i}"
            player.c "{i}Not in a bad way, I don't think?{/i}"
            wt_image daughter_house_1_2
            dee.c "I guess not.  But after I'd managed to stutter out a bunch of questions that she answered, she said she had a question to ask me.  Then she asked if I wanted to touch her."
            wt_image daughter_house_1_23
            "[dee.name] blushes and looks down before continuing."
            wt_image daughter_marilyn_4
            dee.c "{i}I don't know why I said yes.{/i}"
            player.c "{i}You said yes because a powerful, authoritative woman who you admired offered you a chance to connect with her on a personal level.{/i}"
            wt_image daughter_house_1_2
            dee.c "I guess, yeah."
            player.c "{i}That plus your pussy was sopping wet by that point.{/i}"
            wt_image daughter_house_1_23
            "[dee.name]'s blush deepens."
            wt_image daughter_marilyn_4
            dee.c "{i}All we were doing was talking about the obstacles faced by women, and the moment she touched my leg my stomach turned to jelly.  When she told me to touch her tit I thought I was going to cum on the spot.{/i}"
            player.c "{i}How long did it actually take before she made you cum?{/i}"
            wt_image daughter_marilyn_16
            dee.c "{i}Can I retain some dignity and let's just say I made her work to get me off?{/i}"
            player.c "{i}No, tell the truth.{/i}"
            wt_image daughter_marilyn_17
            dee.c "{i}Fine.  She made me demonstrate how needy I was first.{/i}"
            marilyn.c "Make a mess on the limo seat, dirty girl.  I want to see how big a puddle you can make for me."
            wt_image daughter_marilyn_5
            marilyn.c "Mmmm, that is a big, wet mess.  Clean that up, dirty girl.  Once it's all gone I'll let you feel my tongue on your cunt."
            player.c "{i}I suppose she gave you some tissues to clean it up with?{/i}"
            wt_image daughter_house_1_23
            dee.c "You know damn well that wsn't what she meant."
            player.c "Licking your own fluids off a car seat?  Surely you wouldn't do that just because she told you to?"
            wt_image daughter_marilyn_18
            dee.c "{i}You know damn well I did so you can wipe that smirk off your face.  And yes, I did it fast.  And I did it with my ass in the air like a needy slut.{/i}"
            wt_image daughter_marilyn_19
            dee.c "{i}And yes, I came even faster when she ran her tongue along my slit.{/i}"
            wt_image daughter_marilyn_20
            dee.c "{i}She never even reached my clit.  It was like a premature ejactulation for a woman, I came just from her licking my outer labia.  I was so embarrassed.{/i}"
            player.c "{i}Don't worry, I bet she was flattered.  Did she tell you to lick that mess clean, too?{/i}"
            wt_image daughter_marilyn_7
            dee.c "{i}She didn't have to.  Just like she didn't have to tell me what to do with her pussy when she pushed it into my face while I knelt on the floor of the limousine licking my cum off her leather seat."
            player.c "{i}Did you touch yourself while you were eating her out?{/i}"
            wt_image daughter_marilyn_21
            dee.c "{i}Damn you, you really aren't going to let me keep any dignity, are you?  Yes, I started playing with myself while I ate her out.  The whole situation was so intense, I couldn't help myself.{/i}"
            player.c "{i}Did you cum again while you were eating her out?{/i}"
            wt_image daughter_marilyn_6
            dee.c "{i}No{/i}"
            player.c "{i}Why not?{/i}"
            wt_image daughter_house_1_23
            "[dee.name] blushes again."
            dee.c "She told me not to."
            player.c "Why did you obey her?"
            wt_image daughter_marilyn_6
            dee.c "{i}I don't know.  I just sat there on the floor of her limo as we drove along, licking her pussy and edging myself and it was the most intense sexual experience of my life.{/i}"
            player.c "{i}How did it feel when she came on your mouth?{/i}"
            wt_image daughter_marilyn_22
            dee.c "{i}Like I wanted more.{/i}"
            player.c "{i}Sounds like a memorable meeting.{/i}"
            wt_image daughter_house_1_24
            dee.c "It wasn't over."
            $ title = "What do you tell her?"
            menu:
                "Continue (may open some future content)":
                    add tags 'strapon_story_told' to dee
                    wt_image daughter_marilyn_15
                    dee.c "{i}The limo pulled up in front of a fancy hotel.  Marilyn told me to dress, then I nervously followed her up to her room.{/i}"
                    wt_image daughter_marilyn_23
                    dee.c "{i}When we got upstairs, she kissed me and told me that since I'd been a good girl, she'd reward me now.{/i}"
                    player.c "{i}By letting you cum, I presume?{/i}"
                    wt_image daughter_marilyn_8
                    dee.c "{i}That's what I assumed, too, but no. She told me we could continue our interview and she'd give me more information for my studies about women in authority.  First, though, she made me get down on my knees and eat her out some more.{/i}"
                    player.c "{i}Made you?{/i}"
                    wt_image daughter_marilyn_23
                    dee.c "{i}Asked me, I guess.{/i}"
                    player.c "{i}Did she really ask you?{/i}"
                    wt_image daughter_marilyn_24
                    dee.c "{i}No.  She told me to get on the floor and eat her out and I did.  She didn't ask and she didn't make me.  She just expected me to and I went along with it.{/i}"
                    wt_image daughter_marilyn_9
                    dee.c "{i}And so I knelt there, lapping at her pussy, as she talked to me about real-life challenges faced by women trying to succeed in a male-dominated industry.{/i}"
                    wt_image daughter_marilyn_25
                    dee.c "{i}I even got to ask her questions.  I was careful not to pry too much, as I could sense there were things about her past it was best not to ask about, but as long as I kept my tongue busy in her sex, she was happy to answer questions about her experiences without sharing too many details.{/i}"
                    wt_image daughter_marilyn_10
                    dee.c "{i}I lost track of how many times she came in my mouth while we talked, but eventually she said we needed to wrap things up.  She asked if there was one more thing I wanted to know before I left.{/i}"
                    player.c "{i}What did you ask her?{/i}"
                    wt_image daughter_marilyn_26
                    dee.c "{i}I asked if I would be permitted to have another orgasm before I left.{/i}"
                    player.c "{i}Did she agree?{/i}"
                    wt_image daughter_marilyn_14
                    dee.c "{i}Sort of.  She told me it was cute how I came in her limo without even having my clit touched.  She said she would fuck me for five minutes, and that I could have as many orgasms as I wanted in that time, as long as I kept my hands away from my clit.{/i}"
                    wt_image daughter_marilyn_11
                    dee.c "{i}Then she put on a strap-on and bent me over and started fucking me, but not before setting the alarm on the hotel clock to ring in exactly five minutes.  She had really meant it when she said that was all of her time I could have.{/i}"
                    wt_image daughter_marilyn_12
                    player.c "{i}And how many times were you able to cum in the time she gave you?{/i}"
                    wt_image daughter_marilyn_13
                    dee.c "{i}Just once, I think.  But it started almost as soon as she penetrated me and it didn't stop until the alarm rang.  And the whole time I was kneeling there, convulsing, the only thing I could think of - to the extent I could think at all - was how lucky I was that she taking time from her busy day to do this for me.{/i}"
                    player.c "{i}So what did you learn from your time with Marilyn?{/i}"
                "That's enough":
                    player.c "That's enough, I get the point.  You can save the rest of your dignity and keep the remaining details to yourself.  So what did you learn from your time with Marilyn?"
            wt_image daughter_house_1_23
            dee.c "That I was putty in her hands."
            player.c "Do you think you'll see her again?"
            wt_image daughter_house_1_2
            "[dee.name] shakes her head."
            dee.c "It was just a fling.  She's not interested in me."
            player.c "Do you feel exploited?"
            wt_image daughter_house_1_1
            dee.c "Not really."
            player.c "Power is sexy, isn't it?"
            "[dee.name] nods."
            wt_image daughter_house_1_25
            dee.c "Marilyn knows that, too. She knew I was going to sleep with her the moment I stepped into her limo. You knew that, too, when you set this up."
            player.c "Do you think things would have gone differently if she'd been a man?"
            wt_image daughter_house_1_24
            dee.c "No.  If a man had picked me up in his limo and treated me the same way, I probably would have slept with him, too.  Willingly."
            player.c "So what did you really learn from your time with Marilyn?"
            wt_image daughter_house_1_2
            if dee.professor_event_status > 0:
                dee.c "That I was wrong that women in power won't use their authority to satisfy their sexual desires. Maybe that's a human thing, not a male thing."
                player.c "So the distinguishing feature then is the character of the person?"
                wt_image daughter_house_1_22
                dee.c "No, not based on what happened with Dr. Jameson.  I guess I have to amend my thinking.  People in power will use their power to obtain access to sexual partners, regardless of whether they are good people or not, and regardless of whether they're a man or a woman."
                player.c "That sounds about right.  You don't have a statistically significant data set to go on, but that's probably not needed for an arts degree."
                wt_image daughter_house_1_24
                dee.c "This could be the subject of my thesis!  The use of authority for sexual conquest."
                player.c "That sounds like an interesting paper to research."
            else:
                dee.c "That I was wrong that women in power won't use their authority to satisfy their sexual desires.  Maybe that's a human thing, not a male thing."
                wt_image daughter_house_1_22
                dee.c "That shouldn't happen, however. I didn't feel exploited or anything, but using a position of power to gain sexual access is inherently abusive. Good people in authority wouldn't let that happen."
                "You can probably disavow her of that notion by talking to her more about her professor."
            $ dee.marilyn_event_status = 2
            $ marilyn.rewards_pending += 1
            add tags 'dee_reward_pending' to marilyn
            add tags 'marilyn_talk_option_possible' 'janice_talk_option_possible' to dee
        # Professor event described
        elif dee.professor_event_status == 1:
            player.c "Have you spent some 'quality time' with your professor, yet?"
            wt_image daughter_house_1_2
            dee.c "Yes, and it went down pretty much the way you thought it would."
            wt_image daughter_prof_10
            dee.c "{i}I waited for him after class to ask him some questions.{/i}"
            wt_image daughter_prof_11
            dee.c "{i}He closed the door and the two of us had a great chat.  He explained some of the more difficult details of that day's readings.  He was kind and patient and charming, and listened to my perspectives before sharing his own.{/i}"
            wt_image daughter_prof_2
            dee.c "{i}At the end, I told him how much I appreciated him sharing his time and his knowledge with me, and I really meant it. I was grateful, and more than a little attracted to him. Then I did what you suggested.{/i}"
            dee.c "I wish I could show you how much I appreciate having you as my professor."
            dee_prof "What do you mean?"
            wt_image daughter_prof_1
            dee.c "You know.  I just wouldn't want to get you in trouble with the university.  I should go."
            dee_prof "Hold up.  Wait a minute.  What would you be getting me in trouble for?"
            wt_image daughter_prof_12
            dee.c "For having sexual contact with a student."
            dee.c "{i}I was sure he'd toss me out of the room right then.  I was already thinking about how I was going to explain my behavior to the dean.  Mr. Jameson, however, was clearly thinking about something else.{/i}"
            dee_prof "That's a very important rule to prevent professors from preying on students."
            wt_image daughter_prof_10
            dee.c "I know.  It just seems a shame that I can't show you how I really feel about you.  I should go."
            dee_prof "And how is that, [dee.name]?  How do you really feel about me?"
            wt_image daughter_prof_1
            dee.c "That you're an amazing man and I'm really grateful to be able to learn from you.  And that I'd love to show you how grateful I am."
            dee_prof "I'm not sure I follow you.  You've just told me you're grateful.  What more would you want to do?"
            wt_image daughter_prof_10
            dee.c "Dr. Jameson, are you really going to make me say it?"
            dee_prof "Say what, [dee.name]?"
            wt_image daughter_prof_12
            dee.c "That I'd like to suck your cock, Dr. Jameson.  That's wrong of me.  A man like you wouldn't want a student doing that for him.  I should go."
            dee_prof "Hold up, [dee.name].  I'd like you to think very carefully about what you're saying.  The university put the 'no fraternization' rule in place to protect you.  It prevents me from abusing my authority over you."
            wt_image daughter_prof_1
            dee.c "I don't need to be protected from you, do I?"
            dee_prof "Of course not.  My only interest is in helping you and your classmates to get the best education possible and prepare you for your future studies or career."
            wt_image daughter_prof_12
            dee.c "So would that change if I sucked your cock?"
            dee_prof "Not at all. I wouldn't treat you or any of your classmates any differently regardless of whether you do or don't suck my cock."
            wt_image daughter_prof_10
            dee.c "So, it would be okay with you if I sucked your cock?"
            dee_prof "Put your books down and listen, [dee.name].  This is very important.  You need to understand the university policy and why it exists.  Do you understand it?"
            wt_image daughter_prof_15
            dee.c "I think I do understand it.  You've explained it very well.  The rule is intended to protect me, but what it's really doing is preventing me from expressing how I feel, out of a fear that I'll get you in trouble.  That seems so unfair."
            wt_image daughter_prof_3
            dee_prof "The last thing we want to do at this school is prevent our female students from expressing themselves freely.  You must understand, though, that if you act on those feelings, I won't treat you any differently, or favor you in any way, over any of your classmates?  That wouldn't be fair to them."
            dee.c "Of course, Mr. Jameson.  You know I'm at the top of my class anyway.  This isn't about my grades.  It's about showing you how thankful I am for your tutelage and guidance."
            wt_image daughter_prof_15
            dee_prof "If I promise not to tell anybody, would you still like to suck my cock, [dee.name]?"
            wt_image daughter_prof_13
            dee.c "{i}I really did.  When he came around from behind his desk, I didn't hesitate.  I pulled down his pants and took him into my mouth.  This had started out as a test, one I was sure he would pass because I was sure you were wrong about him.  And when I found out you were right, I didn't care.{/i}"
            wt_image daughter_prof_14
            dee.c "{i}I wanted to see the puppy-dog eyes I knew he'd get when he felt my mouth on his cock and he didn't disappoint me.  Here was this beautiful, intelligent, amazing man, and the only thought he had in the world was about me and the pleasure I was bringing him.{/i}"
            wt_image daughter_prof_16
            player.c "{i}Did you feel exploited?{/i}"
            wt_image daughter_prof_4
            dee.c "{i}No, I felt powerful.  And I felt wet.{/i}"
            wt_image daughter_prof_5
            dee.c "{i}I stood up and took my clothes off.{/i}"
            dee.c "I want to feel you inside me."
            wt_image daughter_prof_6
            dee.c "{i}When I saw his hard dick approaching me, I almost came from the sheer excitement of the situation.{/i}"
            wt_image daughter_prof_17
            dee.c "{i}When he shoved himself inside me, I did cum - almost instantly.{i}"
            wt_image daughter_prof_7
            dee.c "Ohh Fucckkk!!!!"
            wt_image daughter_prof_8
            dee.c "{i}He fucked me for a little while and I could tell he was getting close.  I wanted to feel him let go inside me, so I started bucking back against him, but I could sense him resisting.{/i}"
            wt_image daughter_prof_18
            dee.c "It's okay, I'm on birth control."
            dee_prof "No, I have a policy.  I don't cum inside my students.  Not in their pussies."
            wt_image daughter_prof_19
            dee.c "{i}I already knew I wasn't his first, but this confirmed it.  I probably wasn't even his first this term.  I may not even have been his first today.{/i}"
            player.c "{i}Did that hurt?{/i}"
            wt_image daughter_prof_20
            dee.c "{i}I wouldn't say hurt, no.  But it did make me jealous.  And competitive.  I didn't want him grading me as a worse fuck than other students he'd had, I wanted to be the best in the class, ideally the best he'd ever had.  I rolled off his desk and got back on my knees.{/i}"
            wt_image daughter_prof_9
            dee.c "{i}I went back to work on his cock like a mad woman and when he was ready to cum, I happily jerked him off all over my face and glasses, figuring that the sight of me coated in his jizz would be something he'd think about again and again in the days ahead.{/i}"
            wt_image daughter_prof_21
            dee_prof "That was really something, [dee.name].  I hope you feel in the mood to do that agains someday soon.  Thank you for being so understanding about my 'no cumming inside' rule, but if you wouldn't mind licking my cock clean, I'd appreciate it.  I have another class starting in a few minutes."
            wt_image daughter_house_1_1
            player.c "So what did you learn from this?"
            wt_image daughter_house_1_2
            dee.c "That you were right.  The professor I admire really is like other men and happy to use his position to gain sexual access to women."
            player.c "Do you think you'll fuck him again?"
            wt_image daughter_house_1_22
            dee.c "I don' t know. I feel like I should say 'no', because it's wrong.  But then I think about how hard I came when he was fucking me, and I think of the look on his face when he came on me, and I'm so tempted to do it again."
            player.c "Do you feel exploited?"
            wt_image daughter_house_1_2
            dee.c "Not really."
            player.c "Fucking an authority figure is sexy, isn't it?"
            wt_image daughter_house_1_25
            "[dee.name] nods."
            dee.c "Dr. Jameson knows that, too. He probably knew I was going to have sex with him the moment he saw me waiting for him after class. That's why he closed the door for our chat."
            player.c "Do you still think he's a good, respectable man who views women as equals and has their best interests at heart?"
            wt_image daughter_house_1_1
            dee.c "Oddly, yes.  Maybe it is true that men just can't help themselves from taking advantage of their power to have sex with women, no matter how good a man they are."
            player.c "So you think it would have been different if he had been a woman?"
            if dee.marilyn_event_status > 1:
                wt_image daughter_house_1_22
                dee.c "No, not based on what happened with Marilyn.  I guess I have to amend my statement.  People in power will use their power to obtain access to sexual partners, regardless of whether they are good people or not, and regardless of whether they're a man or a woman."
                player.c "That sounds about right.  You don't have a statistically significant data set to go on, but that's probably not needed for an arts degree."
                wt_image daughter_house_1_24
                dee.c "This could be the subject of my thesis!  The use of authority for sexual conquest."
                player.c "That sounds like an interesting paper to research."
            else:
                wt_image daughter_house_1_24
                dee.c "Absolutely!  Women wouldn't use their power to gain sexual access.  They know that's inherently abusive and they'd be careful not to let that happen."
                "You can probably disavow her of that notion by introducing her to a powerful woman."
            $ dee.professor_event_status = 2
        # agrees to domination session
        elif dee.dom_discussion_count == 2:
            wt_image daughter_house_1_2
            dee.c "Okay"
            player.c "Okay, what?"
            wt_image daughter_house_1_22
            dee.c "Okay, I'm ready to let you take me to your dungeon.  But this is a one-time offer.  I'll let you 'dominate' me once, just to see what it's like.  That's all."
            $ dee.dom_discussion_count = 3
        # asks about domination session if deferred last time
        elif dee.dom_discussion_count == 3:
            wt_image daughter_house_1_2
            dee.c "So are you going to take me to your dungeon today?"
            player.c "Still eager, that's good.  That's not exactly the proper way to ask though, is it?"
            wt_image daughter_house_1_22
            dee.c "What do you mean?"
            player.c "I mean that wasn't very deferential.  It was barely even polite.  If you want to learn about submission, you can start now with how you ask me."
            "She stares at you, clearly waging an internal debate with herself."
            wt_image daughter_house_1_23
            "Finally she lowers her head."
            dee.c "I would like it if you took me to your dungeon and taught me about power exchange in a consensual relationship."
            player.c "There, that wasn't so hard, was it?"
            wt_image daughter_house_1_1
            dee.c "Are you kidding?  That was crazy hard.  And also a little bit stimulating.  You're good at this, aren't you?"
            player.c "If you're a good girl, I might give you the chance to find out."
        # when being trained to turn tables on Snow
        elif dee.has_tag('help_her_turn_tables_ra'):
            dee.c "I'm ready for my next lesson on how to turn the tables on [dee_ra.name]."
        # when you've taught her to dominate Snow but she hasn't told you about it yet
        elif dee.talk_sex_life_status == 7 or dee.talk_sex_life_status == 8:
            "There's a spring to [dee.name]'s step as she arrives today.  She seems even more confident than usual.  Things must be going well with her and [dee_ra.name].  You should ask her about her sex life."
        # default intro
        else:
            dee.c "So I learned a lot of interesting things about the patriarchy in my gender studies class.  If you have some time, I can enlighten you on the ways you objectify and debase women."
    return

label dee_visit_end:
    if dee.has_tag('first_visit'):
        wt_image daughter_house_1_2
        dee.c "Fine.  Just remember.  I don't really understand what your relationship is with Mom - or Dad.  But if you hurt either of them, I know where you live."
        player.c "I get it.  You're a protective little tiger cub."
    elif dee.has_tag('dry_fucked_today'):
        wt_image daughter_house_1_23
        "She leaves quietly, confused about the pain between her legs, but too embarrassed to mention it."
    elif dee.has_tag('talked_ra_today'):
        pass
    elif dee.has_tag('talked_mom_today'):
        wt_image current_location.image
        "She leaves quietly, preoccupied by the thoughts in her head."
    elif dee.dom_discussion_count == 3:
        wt_image daughter_house_1_25
        dee.c "Aren't you going to take me to your dungeon?"
        $ title = "What do you do?"
        menu:
            "Take her to your dungeon":
                call dee_dominate_her from _call_dee_dominate_her
            "Tell her next time":
                wt_image daughter_house_1_2
                player.c "You're eager, I like that in a submissive.  However, I also like patience.  I'll teach you about domination when I'm ready.  Offer yourself to me again the next time you drop by, and maybe I'll oblige.  You're dismissed now."
    $ dee.training_session()
    add tags 'no_hypnosis' to dee
    rem tags 'first_visit' 'hypnotized_now' 'cock_face_now' 'cum_face_now' 'dry_fucked_today' 'sex_today' 'sex_talk_today' 'talked_mom_today' 'talked_mom_follow_up_today' 'talked_ra_today' 'talked_domination_today' from dee
    call character_location_return(dee) from _call_character_location_return_748
    if dee.marilyn_event_status == 1 and donna.daughter_investigation_triggered == 3:
        wt_image marilyn_office_24
        "After [dee.name] leaves, you contact Marilyn."
        marilyn.c "What do you want?"
        player.c "I have someone you'll be interested in."
        wt_image marilyn_office_25
        marilyn.c "Young?  Fair-skinned?"
        player.c "Yes to both. She's a women's studies major. She jumped at the chance to meet a successful woman in a traditionally male business. She's been taught that unlike men, women in authority won't use their power to advance their sexual agenda."
        wt_image marilyn_office_24
        marilyn.c "So she's not even interested in sleeping with me?  Why are you bothering me with this?"
        player.c "When's the last time you were sent somebody who wasn't already prepped to sleep with you?  This one's a naive little cutie who's eager to learn from you.  You're the sort of woman she's been reading about and admires.  Plus I have it on good authority she doesn't mind the taste of pussy juice."
        wt_image marilyn_office_2
        marilyn.c "Hmmm.  I do need to be up near the university in a couple of weeks.  I could arrange to meet with her on campus."
        player.c "Have fun seducing her!"
    wt_image current_location.image
    return

label dee_visit_continuing_mom_threesome:
    $ dee.training_session()
    $ donna.training_session()
    summon donna
    summon dee
    wt_image daughter_donna_1_4
    if donna.has_tag('post_continuing_actions'):
        "[donna.name] greets her daughter warmly when [dee.name] arrives."
        dee.c "I can't stay long, Mom.  I need you to come home with me and do my laundry."
        donna.c "Of course, dear!  Is there anything you want me to do with you and my boyfriend first, before we go?"
    else:
        "[dee.name] shows up with mother in tow."
    if donna.has_tag('bimbo'):
        wt_image daughter_donna_1_6
        donna.c "Should we be naked?  The way he's looking at us, I feel like we should be naked."
    wt_image daughter_donna_1_5
    $ title = "What do you want?"
    menu menu_dee_mom_threesome_menu:
        "Have them strip" if not dee.has_tag('naked_now'):
            add tags 'naked_now' to dee
            wt_image daughter_donna_1_7
            if donna.has_tag('bimbo'):
                donna.c "Yay!  I knew we were supposed to be naked!!"
            else:
                donna.c "This is both exciting and humiliating, being naked beside my gorgeous daughter."
            wt_image daughter_donna_1_10
            "Mother and daughter remove their tops ..."
            wt_image daughter_donna_1_8
            "... followed by their skirts ..."
            wt_image daughter_donna_1_13
            "... then await further instructions."
            wt_image daughter_donna_1_11
            jump menu_dee_mom_threesome_menu
        "Let [dee.name] take charge":
            wt_image daughter_donna_1_14
            dee.c "Make his cock hard for me, Mom."
            "[donna.name] sucks gently on your cock under her daughter's supervision."
            wt_image daughter_donna_1_46
            dee.c "Okay, that should be enough fluffing.  I want to watch the two of you make out while I test and see how hard you made."
            wt_image daughter_donna_1_47
            "As [donna.name] leans in to kiss you, [dee.name] settles onto your cock, letting out a contented moan as her wet pussy stretches open to let you inside."
            dee.c "oohhhh"
            wt_image daughter_donna_1_48
            dee.c "More tongue, you two.  Kiss like you're excited to be my sex toys."
            wt_image daughter_donna_1_49
            dee.c "Fuck, Mom!  You did such a good job making him hard, you deserve a reward.  Sit on his face while I ride him."
            wt_image daughter_donna_1_50
            dee.c "Lick my Mom out, but don't let her cum until I say she can.  Don't you cum, either."
            wt_image daughter_donna_1_51
            "[dee.name] resumes riding your shaft while her mother grinds her damp sex against your mouth."
            dee.c "Are you enjoying this, Mom?  Are you hoping I'll let you cum?"
            donna.c "Yes, [dee.name], I'm enjoying this.  And yes, I'm excited enough to cum if you'd like me to."
            wt_image daughter_donna_1_52
            dee.c "Cover his face with your juices, Mom, but nobody cums until I say so."
            "[dee.name] rides you faster and faster, her tight young cunt milking your cock to the point that you can barely hold back.  Her mother is in a similar state, her cunt leaking fluids steadily onto your lapping tongue."
            $ title = "Hold out?"
            menu:
                "Yes, do as you're told":
                    wt_image daughter_donna_1_54
                    "It's not easy for you to control your orgasm, and from the amount of fluids she's spilled onto your face, it's not easy for [donna.name], either.  Fortunately, [dee.name] is close to orgasm herself."
                    dee.c "Oohhhh ...  Quick!  Change positions, Mom!!"
                    wt_image daughter_donna_1_55
                    "[dee.name] straddles your face, pressing her dripping-wet cunt against your mouth as her mother takes her place on your cock."
                    dee.c "If you make me cum, the two of you can cum, too."
                    wt_image daughter_donna_1_56
                    "Making [dee.name] cum is as easy as flicking your tongue hard against her clit three times. As you taste the spurt of juices you releases into your mouth, you let yourself go, groaning into her cunt as you empty your load in her mother's cunt.  You thought [donna.name] might find it harder to cum, but you feel her spasming on your cock as your balls empty themselves inside her."
                    dee.c "Ohhh FUCCKKKK!!!!"
                    player.c "[player.orgasm_text]"
                    donna.c "oooohhhhhh  ooohh  Oh Gaawwwddd!!"
                    if donna.has_tag('cum_slut'):
                        wt_image daughter_donna_1_2
                        donna.c "Cum?  Cum?"
                        dee.c "It's inside you, Mom.  Scope it out and eat it up, if you want."
                        wt_image daughter_donna_1_1
                        donna.c "Cum!  Cum!"
                        dee.c "It's so weird seeing her like this.  I wonder if she's always been like this?"
                        "You don't bother answering.  Once [donna.name] has eaten as much of your sperm as she can locate, she and her daughter dress and leave."
                    else:
                        wt_image daughter_donna_1_8
                        dee.c "Not bad.  Not as good as the girls at my dorm, but not bad.  Did he do a good job of eating your pussy, too, Mom?"
                        donna.c "Yes, [dee.name].  Thank you for letting me cum on his cock afterwards."
                        wt_image daughter_donna_1_4
                        dee.c "No problem, Mom.  I know Dad can't look after you like he used to, and you've been doing as I say without questioning really well.  I figured you deserved a reward for your obedience.  Let's head home and I'll let you thank me more intimately before we go to bed."
                        donna.c "That sounds wonderful, [dee.name]."
                        "The two women leave, smiling, clearly both enjoying the new form their mother-daughter relationship now takes."
                    $ donna.sex_count += 1
                    $ dee.pleasure_her_count += 1
                "No, let yourself cum now":
                    wt_image daughter_donna_1_53
                    "You groan into [donna.name]'s cunt as you let go deep inside her daughter's cunt."
                    player.c "[player.orgasm_text]"
                    dee.c "Somebody's a naughty boy.  You're going to have to look after me now, Mom."
                    donna.c "Of course, [dee.name]!"
                    wt_image daughter_donna_1_42
                    if dee.has_tag('cum_slut'):
                        donna.c "Cum!!  Cum!!"
                        dee.c "Yes, Mom.  You eat his cum out of me, just make sure you make me cum, too."
                    else:
                        donna.c "I can taste his cum inside you."
                        dee.c "Lick it out of me, Mom.  I want you to make me cum by licking his load out of my cunt."
                    wt_image daughter_donna_1_43
                    dee.c "Ohhh FUCCKKKK!!!!"
                    "[dee.name] enjoys the feel of her mother's tongue on her for a little while longer, then the two of them dress and leave."
                    $ dee.sex_count += 1
            orgasm
        "Mother and daughter blow job":
            wt_image daughter_donna_1_46
            dee.c "Come on, Mom.  Let's show him a good time."
            wt_image daughter_donna_1_14
            "[dee.name] watches her mother blow you for a while ..."
            wt_image daughter_donna_1_16
            "... then joins [donna.name] in licking along your shaft ..."
            wt_image daughter_donna_1_15
            "... before switching to licking and suckling on your balls while [donna.name] takes you deep in her mouth."
            wt_image daughter_donna_1_18
            "Then they switch, and [dee.name] takes you deep into her mouth ..."
            wt_image daughter_donna_1_17
            "... while her mother pleasures your balls."
            wt_image daughter_donna_1_16
            $ title = "What now?"
            menu menu_dee_donna_bj_menu:
                "Have [dee.name] blow you":
                    wt_image daughter_donna_1_18
                    "[donna.name] joins you in watching her daughter suck your cock for a few minutes ..."
                    wt_image daughter_donna_1_17
                    "... before joining in."
                    wt_image daughter_donna_1_16
                    jump menu_dee_donna_bj_menu
                "Have [donna.name] blow you":
                    wt_image daughter_donna_1_14
                    if dee.has_tag('bj_trained'):
                        if dee.has_tag('can_use_teeth_during_bjs'):
                            dee.c "Keep working your tongue along the underside of his shaft as you blow him, Mom.  He likes it like that.  You can use your teeth a little bit, but mostly you should be pleasuring him with your lips and tongue."
                        else:
                            dee.c "Lips and toogue only, Mom.  Keep working your tongue along the underside of his shaft as you blow him.  He likes it like that."
                    else:
                        dee.c "Do a good job for him, Mom.  Make his cock hard and throbby."
                    wt_image daughter_donna_1_15
                    "When she tires of instructing her mother on how to suck your cock, [dee.name] joins in, helping out by licking and suckling your balls."
                    wt_image daughter_donna_1_16
                    jump menu_dee_donna_bj_menu
                "Cum in [dee.name]'s mouth":
                    wt_image daughter_donna_1_17
                    player.c "[player.orgasm_text]"
                    wt_image daughter_donna_1_19
                    if dee.has_tag('successful_swallow'):
                        "[dee.name] crinkles her nose, but swallows your load without complaint."
                    else:
                        "[dee.name] starts to choke, struggling to swallow your load without gagging.  Eventually she gets most of it down, but it seems to be a struggle for her."
                    if donna.has_tag('cum_slut'):
                        donna.c "Cum?  Cum?"
                        wt_image daughter_donna_1_41
                        dee.c "Here, Mom.  I saved some for you."
                        wt_image daughter_donna_1_40
                        "[donna.name] licks your sperm out of her daughter's mouth, then the two of you dress and head home."
                        $ donna.cum_slut_visit_week += 1
                    else:
                        wt_image daughter_donna_1_8
                        dee.c "He looks satisfied, Mom.  We should get going now."
                    $ dee.swallow_count += 1
                "Cum in [donna.name]'s mouth":
                    wt_image daughter_donna_1_15
                    player.c "[player.orgasm_text]"
                    wt_image daughter_donna_1_14
                    "[dee.name] pumps the last drops of sperm out of your balls and into her mother's waiting mouth."
                    if donna.has_tag('cum_slut'):
                        wt_image daughter_donna_1_29
                        donna.c "Cum!  Cum!"
                        wt_image daughter_donna_1_10
                        donna.c "Cum  Cum"
                        dee.c "I think she might have enjoyed that just as much as you did.  Come on, Mom, let's get you back home."
                        $ donna.cum_slut_visit_week = week + 3
                    else:
                        wt_image daughter_donna_1_8
                        dee.c "He looks satisfied, Mom.  We should get going now."
                    $ donna.swallow_count += 1
                "Cum on both their faces":
                    wt_image daughter_donna_1_57
                    player.c "[player.orgasm_text]"
                    wt_image daughter_donna_1_58
                    if donna.has_tag('cum_slut'):
                        donna.c "Cum!  Cum!"
                        wt_image daughter_donna_1_9
                        "[donna.name] licks her daughter's face clean, then her own."
                        donna.c "Cum?  Cum?"
                        dee.c "That's all he has for now, Mom.  Let's get you home."
                        $ donna.cum_slut_visit_week = week + 3
                    else:
                        dee.c "He looks satisfied, Mom.  We should get ourselves cleaned up and get going."
                    $ dee.facial_count += 1
                    $ donna.facial_count += 1
            $ dee.blowjob_count += 1
            $ donna.blowjob_count += 1
            orgasm
        "Fuck [dee.name] while her mother watches":
            wt_image daughter_donna_1_23
            dee.c "Fluff him up good, Mom.  I want him rock hard when he enters me."
            wt_image daughter_donna_1_27
            "She does and you are.  [dee.name]'s tight, young pussy stretches wide as you extract yourself from her mother's mouth and push penetrate her."
            wt_image daughter_donna_1_26
            dee.c "Fuck, Mom!  His cock feels so good inside me.  I'm getting so wet.  Can you see that?  Am I dripping on you?"
            donna.c "Yes, [dee.name]!"
            wt_image daughter_donna_1_27
            dee.c "Good.  Watch close, Mom, because his cock feels so good I think I'm going to cum."
            wt_image daughter_donna_1_59
            "[dee.name]'s body is incredibly responsive.  You can feel her already tight pussy tightening even more around your cock as she near climax."
            wt_image daughter_donna_1_25
            dee.c "Ohhh FUCCKKKK!!!!"
            "[donna.name] moans and nearly cums herself at the sight of her daughter being fucked to orgasm.  You don't just nearly cum, you thrust hard into the college girl, emptying your load inside her."
            wt_image daughter_donna_1_26
            player.c "[player.orgasm_text]"
            if donna.has_tag('cum_slut'):
                wt_image daughter_donna_1_59
                donna.c "Cum?  Cum?"
                wt_image daughter_donna_1_24
                dee.c "There's a bit still left in his cock, you can drink that, Mom ..."
                wt_image daughter_donna_1_41
                dee.c "... but there's even more down here."
                wt_image daughter_donna_1_42
                donna.c "Cum!  Cum!"
                wt_image daughter_donna_1_43
                dee.c "That's right, Mom.  Drink all of his cum out of my pussy."
                wt_image daughter_donna_1_8
                "Once [donna.name] has licked as much of your sperm out of her daughter as she can get, the two of them dress and head home happy."
            else:
                wt_image daughter_donna_1_24
                dee.c "Clean his cock for him, Mom."
                wt_image daughter_donna_1_42
                dee.c "Clean my pussy, too."
                wt_image daughter_donna_1_10
                dee.c "Okay, Mom.  Time for us to dress and head home."
                donna.c "I'm glad I was able to help the two of you enjoy yourselves."
            $ dee.orgasm_count += 1
            $ dee.sex_count += 1
            orgasm
        "Fuck [donna.name] while her daughter watches":
            wt_image daughter_donna_1_60
            dee.c "You were worried that men won't find you attractive anymore, Mom, and yet he wants to fuck your pussy instead of mine."
            wt_image daughter_donna_1_61
            "[dee.name] moves closer to get an even better view as you use her mother's cunt to get yourself off."
            $ title = "Where do you want to cum?"
            menu:
                "In [donna.name]":
                    wt_image daughter_donna_1_62
                    player.c "[player.orgasm_text]"
                    if donna.has_tag('cum_slut'):
                        donna.c "Cum!  Cum!"
                        wt_image daughter_donna_1_63
                        dee.c "No, Mom, I'm not going to suck his cum out of you just so you can eat it.  You'll survive until the urge passes."
                        wt_image daughter_donna_1_9
                        donna.c "Cum?  Cum?"
                        dee.c "No, Mom, not today.  Let's get you home"
                    else:
                        "As you empty your load inside her, you're amused to see [donna.name] trying to push her daughter's head between her legs."
                        wt_image daughter_donna_1_63
                        dee.c "Quit pushing on my head, Mom.  I'm not getting you off today.  If being fucked left you horny, you can ask for permission to play with yourself later."
                        donna.c "Yes, [dee.name].  I'm sorry, I got carried away."
                        wt_image daughter_donna_1_9
                        dee.c "For that, I'm going to spank you when we get home, Mom."
                        donna.c "Of course, [dee.name].  I deserve it."
                "In her daughter's mouth":
                    wt_image daughter_donna_1_20
                    "When you pull out of [donna.name] and push your cock into her daughter's mouth, you're not sure that either of them are quite sure what you're up to."
                    wt_image daughter_donna_1_21
                    "As you start to cum, though, you're amused to see [donna.name] hold her daughter's head in place, forcing her to take your load into her mouth."
                    player.c "[player.orgasm_text]"
                    wt_image daughter_donna_1_22
                    if donna.has_tag('cum_slut'):
                        donna.c "Cum!  Cum!"
                        wt_image daughter_donna_1_20
                        dee.c "Okay, okay, Mom.  Just wait a second."
                        wt_image daughter_donna_1_39
                        "A second is about as long as [donna.name] does wait, before leaning over and happily sucking your cum out of her daughters mouth."
                        wt_image daughter_donna_1_9
                        donna.c "Cum?  Cum?"
                        dee.c "That's all there was, Mom.  Let's get you home, now."
                        $ donna.cum_slut_visit_week += 1
                    else:
                        donna.c "That's so hot, [dee.name]!  Lick my juices off his cock."
                        wt_image daughter_donna_1_20
                        if dee.has_tag('successful_swallow'):
                            dee.c "You can let go now, Mom.  I swallowed it all.  Since when are you in cahoots with him about making me drink his cum?"
                        else:
                            "[dee.name] gags a little and spits up some of your cum, unable to easily swallow the full load."
                            dee.c "Shit, Mom!  Ease up!  He was spurting so much I almost choked."
                        donna.c "Sorry, [dee.name].  I got excited and a little carried away."
                        wt_image daughter_donna_1_9
                        dee.c "For that, I'm going to spank you when we get home, Mom."
                        donna.c "Yes, [dee.name].  I deserve it."
                        $ dee.swallow_count += 1
            if donna.sex_type == 1:
                "[donna.name]'s first experience having sex with you was certainly a memorable one."
                $ donna.sex_type = 2
                change donna sos by 10
            $ donna.sex_count += 1
            orgasm
        "Fuck them both" if donna.sex_type > 1:
            wt_image daughter_donna_1_64
            "[dee.name] yelps as you skip the warm up and go straight to stretching her young cunt with your cock."
            dee.c "Ohh!!"
            wt_image daughter_donna_1_65
            "Then you do the same to her mother's, older cunt ..."
            donna.c "OH!"
            wt_image daughter_donna_1_64
            "... before switching back to the younger woman."
            dee.c "Oh, shit!!  You were just inside Mom!"
            wt_image daughter_donna_1_66
            $ dee.temporary_count = 0
            $ donna.temporary_count = 0
            $ title = "What now?"
            menu menu_dee_donna_fuck_both_menu:
                "Fuck [dee.name]":
                    if dee.has_tag('came_today'):
                        wt_image daughter_donna_1_67
                        "Her pussy is slick from her prior orgasm, but still feels tight and warm around your cock as you fuck her."
                        wt_image daughter_donna_1_66
                    elif dee.temporary_count == 0:
                        wt_image daughter_donna_1_67
                        "Despite the lack of foreplay, [dee.name]'s body responds quickly to the sensation of your cock thrusting in and out of her, and she moans in excitement."
                        wt_image daughter_donna_1_66
                        dee.c "oohhhh"
                    else:
                        add tag 'came_today' to dee
                        wt_image daughter_donna_1_67
                        "As you pound into her, [dee.name] stiffens up, then her body starts to tremble as she cums on your cock."
                        wt_image daughter_donna_1_68
                        dee.c "Ohhh FUCCKKKK!!!!"
                        wt_image daughter_donna_1_66
                        $ dee.orgasm_count += 1
                    $ dee.temporary_count += 1
                    jump menu_dee_donna_fuck_both_menu
                "Fuck [donna.name]":
                    wt_image daughter_donna_1_69
                    if donna.has_tag('came_today'):
                        "Your cock slides easily in and out of her pussy, which is still dripping wet from her orgasm."
                    elif donna.temporary_count == 0:
                        "She's ready for your cock this time and though her body isn't completely warmed up, yet, after a few thrusts in and out she lets out a soft moan."
                        donna.c "oohhh"
                    elif donna.temporary_count == 1:
                        "She's fully warmed up now and clearly enjoying the experience of being naked beside her daughter with your cock thrusting in and out of her."
                        donna.c "ooohhhh  oooohhhhhh"
                    else:
                        add tags 'came_today' to donna
                        "As your cock stretches and probes the inside of her sex, [donna.name] leans against her daughter and spasms to an intense climax while her daughter moans in excitement beside her."
                        wt_image daughter_donna_1_65
                        donna.c "oohhh  oohhh  Oh Gaawwwdddd!!! "
                        if dee.has_tag('came_today'):
                            dee.c "Oh shit, Mom!!  You came on his cock after I came on it, too!"
                        else:
                            dee.c "Oh shit, Mom!!  You came on his cock after it had been inside me!"
                        if not donna.has_tag('sex_orgasm'):
                            "Cumming from sex with a man who isn't her husband is a new experience for [donna.name]."
                            add tags 'sex_orgasm' to donna
                            change donna sos by 5 notify
                        wt_image daughter_donna_1_69
                        $ donna.orgasm_count += 1
                    $ donna.temporary_count += 1
                    jump menu_dee_donna_fuck_both_menu
                "Finish inside [dee.name]" if (dee.temporary_count + donna.temporary_count) > 1:
                    wt_image daughter_donna_1_68
                    if dee.has_tag('came_today'):
                        player.c "[player.orgasm_text]"
                        if donna.has_tag('came_today'):
                            if donna.has_tag('cum_slut'):
                                wt_image daughter_donna_1_29
                                donna.c "Cum?  Cum?"
                                wt_image daughter_donna_1_9
                                dee.c "Not now, Mom.  Now we're going home, but I'll show you where the cum went while we're on our way.  Thanks for showing my Mom and I a good time!"
                            else:
                                wt_image daughter_donna_1_8
                                dee.c "Thanks for showing my Mom and I a good time.  That was fun!  See you next time."
                        else:
                            wt_image daughter_donna_1_9
                            dee.c "That was fun.  Are you feeling left out, Mom?  We both came, but you didn't."
                            if donna.has_tag('cum_slut'):
                                donna.c "Cum?  Cum?"
                                dee.c "Not now, Mom.  Now we're going home, but I'll show you where the cum went while we're on our way."
                            else:
                                wt_image daughter_donna_1_10
                                donna.c "Not at all, [dee.name].  I'm just glad you wanted me here to participate in your fun.  That's more satisfying than cumming myself."
                                dee.c "We've trained her well, haven't we?  See you next time!"
                    elif dee.temporary_count == 1:
                        "[dee.name] moans in frustration as she hears you cum, leaving her hanging."
                        player.c "[player.orgasm_text]"
                        wt_image daughter_donna_1_67
                        dee.c "Mom, mouth between my legs.  Right now!"
                        wt_image daughter_donna_1_42
                        if donna.has_tag('cum_slut'):
                            donna.c "Cum!  Cum!"
                            dee.c "Yes, Mom.  Suck his cum out of me and drink my girl cum, too."
                        else:
                            dee.c "Suck every drop of his cum out of me, Mom, and drink all of my cum, too."
                            donna.c "Yes, [dee.name]."
                        wt_image daughter_donna_1_43
                        "After being warmed up by your cock inside her, it doesn't take her mother long to get [dee.name] off."
                        dee.c "Ohhh FUCCKKKK!!!!"
                        if donna.has_tag('cum_slut'):
                            wt_image daughter_donna_1_9
                            dee.c "Okay, now we can head home."
                            donna.c "Cum  Cum"
                            $ donna.cum_slut_visit_week = week + 1
                        else:
                            wt_image daughter_donna_1_10
                            dee.c "Okay, now we can head home."
                            donna.c "Yes, [dee.name].  I'm glad I could help make that a good experience for you."
                    elif donna.has_tag('came_today'):
                        player.c "[player.orgasm_text]"
                        wt_image daughter_donna_1_9
                        dee.c "Well, I guess I'm the only one who doesn't cum today.  Did the two of you enjoy yourselves?"
                        if donna.has_tag('cum_slut'):
                            donna.c "Cum?  Cum?"
                            dee.c "Don't worry, Mom, I'll show you where his cum went on our drive home."
                        else:
                            donna.c "[dee.name], I'm happy to look after you."
                            wt_image daughter_donna_1_10
                            dee.c "I know that, Mom.  I'm good for right now.  It was nice, though, getting to see you enjoy yourself."
                            donna.c "Thank you.  The both of you make me feel so desired, it's a really nice feeling, even better than the orgasm."
                    else:
                        player.c "[player.orgasm_text]"
                        wt_image daughter_donna_1_9
                        dee.c "Well, I guess the patriarchy is in full force.  Only people with testicles get to cum today."
                        if donna.has_tag('cum_slut'):
                            donna.c "Cum?  Cum?"
                            dee.c "Don't worry, Mom, I'll show you where his cum went on our drive home."
                        else:
                            donna.c "[dee.name], I'm happy to look after you."
                            wt_image daughter_donna_1_8
                            dee.c "I know that, Mom.  I'll find a use for you once we get home."
                "Finish inside [donna.name]" if (dee.temporary_count + donna.temporary_count) > 1:
                    wt_image daughter_donna_1_65
                    if dee.has_tag('came_today'):
                        if donna.has_tag('came_today'):
                            player.c "[player.orgasm_text]"
                            if donna.has_tag('cum_slut'):
                                wt_image daughter_donna_1_29
                                donna.c "Cum?  Cum?"
                                wt_image daughter_donna_1_9
                                dee.c "Not now, Mom.  Now we're going home, but I'll show you where the cum went while we're on our way.  Thanks for showing my Mom and I a good time!"
                            else:
                                wt_image daughter_donna_1_8
                                dee.c "Thanks for showing my Mom and I a good time.  That was fun!  See you next time."
                        else:
                            "[donna.name] moans submissively as you use her as a cum dump after pleasuring her daughter."
                            player.c "[player.orgasm_text]"
                            wt_image daughter_donna_1_9
                            dee.c "That's so hot that we both came, but all Mom got was a creampie.  Did you enjoy that, Mom?"
                            if donna.has_tag('cum_slut'):
                                donna.c "Cum?  Cum?"
                                dee.c "Not now, Mom.  Now we're going home, but I'll show you where the cum went while we're on our way."
                            else:
                                wt_image daughter_donna_1_10
                                donna.c "Honestly?  I kind of did.  Helping the two of you have a fun experience is more satisfying than cumming myself."
                                dee.c "We've trained her well, haven't we?  See you next time!"
                    elif dee.temporary_count == 1:
                        "[dee.name] moans in frustration as she hears you cum inside her mother, leaving her hanging."
                        player.c "[player.orgasm_text]"
                        wt_image daughter_donna_1_69
                        dee.c "Mom, mouth between my legs.  Right now!"
                        wt_image daughter_donna_1_42
                        if donna.has_tag('cum_slut'):
                            donna.c "Cum?  Cum?"
                            dee.c "Not now, Mom.  I'll show you where his cum went after, right now you're going to drink my girl cum."
                        else:
                            donna.c "Yes, [dee.name]."
                        wt_image daughter_donna_1_43
                        "After being warmed up by your cock inside her, it doesn't take her mother long to get [dee.name] off."
                        dee.c "Ohhh FUCCKKKK!!!!"
                        if donna.has_tag('cum_slut'):
                            wt_image daughter_donna_1_9
                            dee.c "Okay, now we can head home.  I'll show you where his cum went on the way."
                            donna.c "Cum  Cum"
                        else:
                            wt_image daughter_donna_1_10
                            dee.c "Okay, now we can head home."
                            donna.c "Yes, [dee.name].  I'm glad I could help make that a good experience for you."
                    elif donna.has_tag('came_today'):
                        player.c "[player.orgasm_text]"
                        wt_image daughter_donna_1_9
                        dee.c "Well, I guess I'm the only one who doesn't cum today.  Did the two of you enjoy yourselves?"
                        if donna.has_tag('cum_slut'):
                            donna.c "Cum?  Cum?"
                            dee.c "Don't worry, Mom, I can show you where his cum went on our drive home."
                        else:
                            donna.c "[dee.name], I'm happy to look after you."
                            wt_image daughter_donna_1_10
                            dee.c "I know that, Mom.  I'm good for right now.  It was nice, though, getting to see you enjoy yourself."
                            donna.c "Thank you.  The both of you make me feel so desired, it's a really nice feeling, even better than the orgasm."
                    else:
                        player.c "[player.orgasm_text]"
                        wt_image daughter_donna_1_9
                        dee.c "Well, I guess the patriarchy is in full force.  Only people with testicles get to cum today."
                        if donna.has_tag('cum_slut'):
                            donna.c "Cum?  Cum?"
                            dee.c "Don't worry, Mom, I can show you where his cum went on our drive home."
                        else:
                            donna.c "[dee.name], I'm happy to look after you."
                            wt_image daughter_donna_1_8
                            dee.c "I know that, Mom.  I'll find a use for you once we get home."
                "Finish on their faces" if (dee.temporary_count + donna.temporary_count) > 1:
                    wt_image daughter_donna_1_57
                    player.c "[player.orgasm_text]"
                    wt_image daughter_donna_1_58
                    if dee.has_tag('came_today'):
                        if donna.has_tag('came_today'):
                            dee.c "Thanks for showing my Mom and I a good time.  That was fun!  See you next time."
                            if donna.has_tag('cum_slut'):
                                donna.c "Cum!  Cum!"
                        else:
                            dee.c "That's so hot that we both came, but all Mom got was a load in the face.  Did you enjoy that, Mom?"
                            if donna.has_tag('cum_slut'):
                                donna.c "Cum!  Cum!"
                                wt_image daughter_donna_1_5
                                dee.c "Sounds like she's happy.  See you next time!"
                            else:
                                donna.c "Honestly?  I kind of did.  Helping the two of you have a fun experience is more satisfying than cumming myself."
                                wt_image daughter_donna_1_4
                                dee.c "We've trained her well, haven't we?  See you next time!"
                    elif dee.temporary_count == 1:
                        dee.c "That's him looked after, now it's my turn.  Get your mouth between my legs, Mom."
                        wt_image daughter_donna_1_42
                        if donna.has_tag('cum_slut'):
                            donna.c "Cum?  Cum?"
                            dee.c "There's some on your face you can lick off later.  Right now you're going to drink my girl cum."
                        else:
                            donna.c "Yes, [dee.name]."
                        wt_image daughter_donna_1_43
                        "After being warmed up by your cock inside her, it doesn't take her mother long to get [dee.name] off."
                        dee.c "Ohhh FUCCKKKK!!!!"
                        if donna.has_tag('cum_slut'):
                            wt_image daughter_donna_1_8
                            dee.c "Okay, now we can head home."
                            donna.c "Cum  Cum"
                        else:
                            wt_image daughter_donna_1_10
                            dee.c "Okay, now we can head home."
                            donna.c "Yes, [dee.name].  I'm glad I could help make that a good experience for you."
                    elif donna.has_tag('came_today'):
                        dee.c "Well, I guess I'm the only one who doesn't cum today.  Did the two of you enjoy yourselves?"
                        if donna.has_tag('cum_slut'):
                            donna.c "Cum!  Cum!"
                        else:
                            donna.c "[dee.name], I'm happy to look after you."
                            wt_image daughter_donna_1_8
                            dee.c "I know that, Mom.  I'll find a use for you once we get home."
                    else:
                        dee.c "Well, I guess the patriarchy is in full force.  Only people with testicles get to cum today."
                        if donna.has_tag('cum_slut'):
                            donna.c "Cum!  Cum!"
                        else:
                            donna.c "[dee.name], I'm happy to look after you."
                            wt_image daughter_donna_1_8
                            dee.c "I know that, Mom.  I'll find a use for you once we get home."
                    if donna.has_tag('cum_slut'):
                        $ donna.cum_slut_visit_week = week + 3
                    $ dee.facial_count += 1
                    $ donna.facial_count += 1
            $ dee.temporary_count = 0
            $ donna.temporary_count = 0
            rem tags 'came_today' from dee
            rem tags 'came_today' from donna
            $ dee.sex_count += 1
            $ donna.sex_count += 1
            orgasm
        "Nothing else" if dee.has_tag('naked_now'):
            wt_image daughter_donna_1_8
            dee.c "Wow, I know some guys are easy, but that was ridiculous.  Come on, Mom, I guess he must have already creamed his pants at the sight of the two of us naked.  Let's head home."
            change player energy by -energy_very_short
    rem tags 'naked_now' from dee
    call character_location_return(donna) from _call_character_location_return_749
    call character_location_return(dee) from _call_character_location_return_750
    notify
    wt_image current_location.image
    return

label dee_first_visit:
    wt_image front_door
    "Before you settle for the night, there's a knock at your door."
    wt_image daughter_door_1
    "A wisp of a girl shivers in the waning evening light.  She looks cold, but angry."
    dee.c "Who are you?"
    player.c "Who am I?  I'm the owner of this house.  Who are you?"
    wt_image daughter_door_2
    if donna.status == 'on_training':
        dee.c "I'm the daughter of the woman who just left.  Why was she here?  What have you been doing with her?"
        player.c "How long have you been out here?"
    else:
        dee.c "I'm the daughter of the woman who was here earlier.  Why was she here?  What have you been doing with her?"
        player.c "You mean [donna.name]?  How long have you been out here?"
    wt_image daughter_door_3
    if donna.status == 'on_training':
        dee.c "Long enough to wonder whether I should call the cops and report you.  Then I finally saw Mom leave.  Answer my questions.  What have you been doing with my Mom and why?"
    else:
        dee.c "Long enough to wonder whether I should call the cops and report you.  Answer my questions.  What have you been doing with my Mom and why?"
    # "She has an annoying squeaky little girl voice, the type some women keep long after they should have moved on to an adult's voice. It's rather irritating, almost like trying to read lime green on white, but otherwise she's fairly cute."
    $ title = "Invite her in?"
    menu:
        "Invite her in":
            wt_image daughter_door_1
            player.c "You're shivering. Come in and we'll talk inside."
            wt_image daughter_door_3
            dee.c "Oh no.  I'm not going inside with you.  You could be some kind of pervert preying on my Mom."
            player.c "I'm not preying on your Mom.  I'm helping her."
            wt_image daughter_door_2
            dee.c "Helping her?  What do you even know about her?  What do you know about our family or about me?"
            player.c "I know all about your family."
            wt_image daughter_door_3
            dee.c "Really?  Go on then.  What has Mom told you about me?"
            if donna.has_tag('discussed_children'):
                $ donna.daughter_investigation_triggered = 3
                player.c "I know your Mom is very proud of you, [dee.name].  She says you're doing well at university with your women in society studies."
                wt_image daughter_door_2
                player.c "I know you take advantage of her easy going nature, dragging your dirty laundry home for her to do when you're perfectly capable of doing it yourself.  I also know your Mom doesn't mind, because that's the type of person she is."
                wt_image daughter_door_1
                player.c "What she would mind is seeing you standing there shivering trying to catch a cold instead of coming in so we can continue this conversation inside."
                "She glowers at you but steps inside."
                wt_image daughter_house_1_1
                dee.c "Okay, so Mom has told you about me.  Why hasn't she told me about you?"
                if donna.has_tag('stripped'):
                    player.c "Parents don't tell their children everything.  For example, I bet your mother hasn't told you she has a clit ring."
                    wt_image daughter_house_1_21
                    dee.c "Oh my god!  She does not!!  And how would you even know!!!"
                    player.c "I know because I've seen it."
                    wt_image daughter_house_1_20
                    dee.c "Shut up!  I can't even handle that thought right now.  My mother does not have a pierced ... anything."
                    player.c "Why is that so hard to believe?"
                    wt_image daughter_house_1_21
                    dee.c "Because she's ... Mom!"
                    player.c "Is that what they teach you in your women in society classes? That women are defined by their family relationships?"
                    wt_image daughter_house_1_22
                    dee.c "No! I mean, yes, in a patriarchal society. But no they shouldn't be, but ..."
                    player.c "But you want her to be."
                    wt_image daughter_house_1_24
                    dee.c "No, I don't want her to be defined just as a 'mom', but ...  a clit ring?  Seriously?  You have her mixed up with someone else."
                    player.c "There's more to your mother than you may realize.  She's just 'Mom' to you, but she's her own woman, with her own needs and desires."
                else:
                    player.c "Parents don't tell their children everything.  There's more to your mother than you may realize. She's just 'Mom' to you, but she's her own woman, with her own needs and desires."
                wt_image daughter_house_1_25
                dee.c "I'm not sure you're talking about my mother.  Mom doesn't have those desires.  She's different."
                player.c "Then why do you think she was here, with me?"
                wt_image daughter_house_1_22
                dee.c "I really don't know."
                player.c "Because your father sent her here."
                wt_image daughter_house_1_2
                dee.c "Why?"
                player.c "To train her."
                wt_image daughter_house_1_22
                dee.c "Train her for what?"
                player.c "To be ready to go out and enjoy her life, and find a new man.  One who can give her the things your father no longer can."
                wt_image daughter_house_1_21
                dee.c "That's not possible.  Dad ..."
                player.c "Dad what?  Doesn't love your mother?  Wouldn't do whatever he could to make sure that she's happy?"
                wt_image daughter_house_1_24
                dee.c "No.  I mean, yes.  He would do exactly those things.  But there's no way Mom wouldn't tell me.  She tells me everything and I tell her everything."
                player.c "So I've heard.  Your mom is a bit concerned about your proclivity to spread your legs for every good-looking guy or gal who catches your eye."
                wt_image daughter_house_1_21
                dee.c "What the hell business is that of yours??  I like sex.  It's not wrong for a woman to like sex."
                wt_image daughter_house_1_2
                player.c "No, it's not.  It's also not wrong for a woman to be a bit more discerning about who she sleeps with.  If your Mom chose not to tell you that your father sent her to me to train her to be ready to have sex with another man now that he can't have sex with her, perhaps you can respect and understand why she chose to keep that secret from you?"
                wt_image daughter_house_1_21
                player.c "Unlike you, your Mom isn't naturally inclined to spread her legs for every cute guy or girl who walks by. That doesn't mean she shouldn't have an enjoyable sex life.  It does mean she may want to be a little more secretive about it, especially with a hyper-confident daughter who's likely to judge her whatever decisions she makes."
                dee.c "I don't judge her!"
                wt_image daughter_house_1_22
                player.c "Yes, you do.  You judge everyone.  It's in your nature."
                "She sits quietly for a moment."
                dee.c "How did you know that?  That I judge people."
                wt_image daughter_house_1_2
                player.c "I know women.  It's my thing.  Why do you judge people, [dee.name]?"
                "She shrugs."
                wt_image daughter_house_1_1
                dee.c "I don't know. Maybe I just have high expectations?"
                player.c "And when people turn out to be human, you're disappointed."
                wt_image daughter_house_1_2
                dee.c "That's a cop out. People excuse their actions by saying they're 'just human' instead of taking responsibility. Men have been justifying the oppression for women for years by saying it's 'human nature'. That's their excuse to treat women as sex objects and abuse their power to gain sexual favors. 'It's just boys being boys.' 'They're not doing anything wrong, they just have urges.' Blah blah blah."
                player.c "And women don't have those urges?"
                wt_image daughter_house_1_24
                dee.c "No!  Women do.  Women just control themselves.  We don't abuse our power for sex when we get into positions of authority.  Men do.  At least some of them.  Not all."
                player.c "Which men won't trade authority for sex?"
                wt_image daughter_house_1_1
                dee.c "Well, my professor at university, for example.  He's totally enlightened and a good man. He teaches us all sorts of things about the oppression of women in a patriarchal society and how to create real change."
                "She's given you some topics to discuss, if you want to.  Or you could check to see if she's open to an intimate relationship."
            else:
                player.c "I know about the important aspects of your family, like your Dad's illness.  I don't know anything about you, your Mom doesn't talk about you."
                wt_image daughter_door_2
                dee.c "Fuck you!  I'm the most important thing in Mom's life, besides Dad's health.  If you were a friend she'd have told you about me."
                sys "You don't know enough about her to progress this story line.  If you want, however, you can re-set this event until you've been able to learn more about [donna.name]'s family."
                $ title = "What now?"
                menu:
                    "Reset this event and try later":
                        wt_image front_door
                        "It's been a long day.  Maybe you were imagining this conversation."
                        $ donna.daughter_investigation_triggered = 0
                        $ dee.visit_count = 0
                    "Tell her that her Mom has the hots for her" if donna.daughter_lust_revealed > 0:
                        player.c "Well, I do know that your Mom has the hots for you."
                        wt_image daughter_door_3
                        dee.c "Ewwww!!! You're gross!"
                        wt_image front_door
                        "She storms off. That should be the last you see of her. From the revolted look on her face as she left, you'd guess she won't even tell her Mom about your conversation."
                        $ donna.daughter_investigation_triggered = 2
                    "Get rid of her":
                        player.c "Maybe you're not as important as you think.  Your Mom needs something more in her life than looking after spoiled children and a sick husband."
                        wt_image daughter_door_3
                        dee.c "And you're that something? She's a happily married woman. Why would she be spending time with you?"
                        player.c "Talk to your parents if you want answers. Or keep your nose out of their business, if you want to be a good daughter. I don't care one way or the other. If you're not coming in, then I'm going to bed."
                        wt_image front_door
                        "You leave her fuming on your doorstep."
                        $ donna.daughter_investigation_triggered = 2
                call character_location_return(dee) from _call_character_location_return_751
        "Tell her to get lost":
            player.c "Get lost, kid.  You have questions, ask your mother.  Or your father."
            wt_image daughter_door_2
            dee.c "Dad knows Mom was here?"
            player.c "Like I said, talk to your parents if you want answers. Or keep your nose out of their business, if you want to be a good daughter.  I don't care one way or the other, I'm going to bed."
            $ donna.daughter_investigation_triggered = 2
            call character_location_return(dee) from _call_character_location_return_752
    return


# View Relationship Status

# Review Files

# Description Display

## Character Specific Objects
# N/A

## Items
# Give Butt Plug
label give_bp_dee:
    if dee.has_tag('sex_before'):
        dee.c "Let's just stick to front door activities, okay?"
    elif dee.dom_discussion_count > 2:
        dee.c "Oh, no!  I may be up to visiting your dungeon with you, but I'm not letting you use that on me."
    else:
        dee.c "There is something seriously wrong with you.  Put that away."
    return

# Give Chastity Belt
label give_cb_dee:
    if dee.ready_for_mom > 2:
        dee.c "Even Mom doesn't want me wearing one of those these days.  Although maybe I'll fit her for one sometime."
    else:
        dee.c "Did my Mom put you up to this?  Tell her 'ha ha, but no', I like my sex life and I'm keeping it, thank you very much."
    return

# Give Dildo
label give_di_dee:
    if dee.talk_sex_life_status > 2:
        dee.c "I get enough of that sort of play with [dee_ra.name], thanks."
    elif dee.has_tag('sex_before'):
        dee.c "No thanks.  I don't have any trouble getting access to the real thing, when I'm in the mood for it."
    else:
        dee.c "Ewww. It's all kinds of messed up that you'd think I'd want that as a gift from you."
    return

# Use Fetch Toy

# Give Jewelry

# Use Leash

# Give Lingerie
label give_li_dee:
    dee.c "Are you trying to turn me into your sugar baby?  Save the lingerie for someone who will model it for you."
    return

# Give Love Potion
label give_lp_dee:
    dee.c "No way.  Who knows what kind of weird drug you might have put in there."
    return

# Give Transformation Potion
label give_tp_dee:
    dee.c "No way.  Who knows what kind of weird drug you might have put in there."
    return

# Give Ring of Secuality
label give_rs_dee:
    "She already likes both boys and girls."
    return

# Use Water Bowl

# Use Will Tamer
label use_wt_dee:
    if dee.dom_discussion_count > 2:
        dee.c "No way.  I may be up to visiting your dungeon with you, but I draw the line at wearing a collar."
    else:
        dee.c "Ewww.  Keep that away from me."
    return


########### TIMERS ###########
## Common Timers
# End Training Permanently
# TIMER: Check Character Engagement Ends

# Start Day
label dee_start_day:
    # normal contact
    if donna.daughter_investigation_triggered == 3 and dee.visit_week == week:
        if day == 1:
            wt_image phone_1
            "You receive a message from [dee.full_name]."
            if dee.has_tag('father_dead'):
                dee.c "{i}I'm around this week.  Let me know if you have time for us to meet.{/i}"
            else:
                dee.c "{i}I'm around home this week, visiting my parents.  Let me know if you have time for us to meet.{/i}"
            add tags 'contact_open' to dee
    # accelerated contact while you are supposed to be training her to turn the tables on her RA
    elif donna.daughter_investigation_triggered == 3 and dee.has_tag('help_her_turn_tables_ra') and dee.dom_discussion_count > 3 and dee.talk_sex_life_status < 7:
        if day == 1:
            wt_image phone_1
            "You receive a message from [dee.full_name]."
            dee.c "{i}Let me know if you have time for me to visit this week.  I'm anxious to learn how you think I can turn the tables on [dee_ra.name].  It's a long drive in to the city to meet, but a friend will let me borrow his car so I can make it, just tell me when.{/i}"
            add tags 'contact_open' to dee
    else:
        rem tags 'contact_open' from dee
        if week > dee.visit_week and dee.visit_week > 0:
            $ dee.visit_week += 4
    return

# End Day
label dee_end_day:
    ## End Day - Daughter 1st Visit
    if donna.daughter_investigation_triggered == 1:
        call dee_visit from _call_dee_visit_1
    ## Cancel contact options if Donna is lost
    if donna.daughter_investigation_triggered == 3 and donna.status == 'unavailable':
        rem tags 'contact_open' from dee
        $ donna.daughter_investigation_triggered == 2
        $ dee.visit_week = 0
        call convert(dee, 'unavailable') from _call_convert_195
        sys "When you lost access to [donna.name], you lost access to her daughter, [dee.name], as well, who is too concerned about her Mom to think about contacting you."
    return

# End Week
label dee_end_week:
    pass
    return


## Lawyer Content
label dee_janice_talk_option:
    if janice.has_tag('asked_about_hiring') and not janice.has_tag('discuss_dee_lesbian'):
        player.c "I've met a sexually adventurous blonde college girl.  Marilyn seems to have had a lot of fun with her, would you like me to send her your way, too?"
        janice.c "A college girl?  She could be a gold-digger.  I'd better not risk it."
        player.c "That's a strangely specific compulsion you have, you know?"
        add tags 'discuss_dee_lesbian' to janice
        $ janice.temporary_count = 0
    return

## Marilyn Content
label dee_marilyn_talk_option:
    if dee.marilyn_event_status == 2:
        marilyn.c "Young, sexually confused university students are so fun.  Drop by to see me to collect your finder's fee."
    return

## Loving Wife Content
# none

## Character Specific Timers
# none

# Will-Tamer Timer
# none


########### ROOMS ###########
# N/A

################################### NOTES ###################################
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
