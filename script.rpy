# Declare character (Vio)
define e = Character("Vio", color="#cca625")
define s = Character("Stikman", color="#ffffff") # For Stikman dialogue
define s = Character("Shiver", color="#a7c6e7") # For Shiver dialogue
define n = Character(None, color="#ffffff") # For unassigned narrator text

# Solid black background definition
image bg black = "#000000"
image bg white = "#ffffff"

# Position and scale for 1080p canvas
transform vio_scale:
    zoom 0.58
    xalign 0.5
    yalign 1.0

# Position for left side of the screen
transform vio_left:
    zoom 0.58
    xalign 0.2
    yalign 1.0

# Positions for the outdoor Stikman encounter
transform stikman_left:
    zoom 0.58
    xalign 0.2
    yalign 1.0

transform vio_right:
    zoom 0.58
    xalign 0.8
    yalign 1.0

# Default player name variable
default player_name = "Player"

label start:

    # 1. Opening Warning / Disclaimer
    scene bg makename:
        xysize (1920, 1080)
    with dissolve

    "hi, welcome to Date Vio."
    "Before you say something dumb dumb dumb"
    "la la la la la lala"
    "sorry"
    "just know this game is SATIRE, and a JOKE. and is NOT canon."
    "okay, what's-your-name, enter ya name."
    "the narrator dies"

    # Name Input Prompt
    python:
        name_input = renpy.input("you know what to do, bud.", default="Player")
        name_input = name_input.strip()
        if not name_input:
            name_input = "Player"
        player_name = name_input

    # 2. Scene One Intro - The Search for Employment
    scene bg black
    with dissolve

    n "You [player_name], have been looking for your place of employment all day, but couldn't find it."
    n "Then you see it."

    scene bg outsidegym:
        xysize (1920, 1080)
    with dissolve

    n "You think \"wait... is that my workplace?\"..."

    scene bg gym:
        xysize (1920, 1080)
    with dissolve

    n "You walk in, you look around. Yep. This was it."
    n "Your role was just to watch the gymgoers, to make sure they don't kill themselves or something."
    n "You see your assigned bench and walk over to it, then you sit on it."
    n "Then someone, a pokemon looks at you, then walks over to you. The first thing you notice is that this person isn't wearing clothes, but you look around, notice that this is a POKEMON GYM. Anthro Pokemon don't wear clothes. Well, some do, but Anthro Pokemon don't have reproductive organs, so you settle a bit."

    # 3. Vio Appears
    show vio netural at vio_scale
    with dissolve

    e "...Oh. Hey...?- Oh wait! You must be that new guy here..."

    "Vio thinks"

    show vio bored at vio_scale
    e "hmm...uhhh...."

    show vio shocked at vio_scale
    e ""

    show vio worried at vio_scale
    e "Your name was....uh... [player_name], right?"

    menu:
        "Yes":
            pass

        "No":
            scene bg youlied:
                xysize (1920, 1080)
            with dissolve
            n ""
            return

    # Continuing if player chose "Yes":
    show vio worriedright at vio_scale
    e "Okay! - I-i didn't think you were gonna be so...."

    show vio ehh at vio_scale
    e "DIRECT about that..."

    show vio confused at vio_scale
    e "I'm usually pretty shy when I tell people I don't know my name..."

    show vio happy at vio_scale
    e "But...if you're feeling confident...."

    e "...My name's Vio."

    show vio veryhappy at vio_scale
    e "Yours is [player_name], but I already knew that."


    # --- SCENE TWO ---

    show vio smug at vio_scale
    with dissolve

    e "Watch me lift this dumbbell."

    n "Vio attempts to lift the dumbbell, which is a rock. A really BIG one. It slips out of her hand and falls onto her."

    show vio scaredleft at vio_scale
    e "GAH!!!"

    show vio scaredtwyou at vio_scale
    e "......I-i think my legs are broken....?"

    e "C-could you push this off of me....?"

    show vio sad at vio_scale
    e "......Please...?"

    menu:
        "Push rock off of her":
            pass

        "Use your camera to take a picture to blackmail her":
            jump vio_pissed_ending

        "Stare":
            jump vio_pissed_ending


    # If player chose to push the rock:
    n "You, [player_name] push the rock off of her, somehow."

    show vio suprisedwithelect at vio_scale
    e "H-how did you DO that?!"

    # Dialogue options hub (one-time choice)
    menu:
        "Never mind that. Can you stand?":
            show vio worried at vio_scale
            e "...U-uh...let's see...."

        "Are you hurt or bleeding anywhere??":
            show vio scareddown at vio_scale
            e "...Nope."
            
            show vio scaredtwyou at vio_scale
            e "Let's see If I can stand..."
            
            # Moves directly into the standing sequence automatically!
            show vio worried at vio_scale
            e "...U-uh...let's see...."

    # This part runs no matter which option you picked above
    n "Vio attempts to stand"
    
    show vio scaredleft at vio_scale
    e "Catchmecatchmecatchme"
    
    menu:
        "Catch Vio":
            jump vio_caught

        "Don't catch Vio":
            jump vio_pissed_ending


# Catch route continuation
label vio_caught:
    show vio sad at vio_scale
    e "I think I can walk... I might have to be trained to walk again though... It's really numb."
    
    show vio tired at vio_scale
    e "...Umm...-"

    n "Vio's phone dings"
    n "Vio checks her phone."

    show vio worried at vio_scale
    e ""

    n "her phone dings again"

    show vio shocked at vio_scale
    e ""

    show vio scaredtwyou at vio_scale
    e "...[player_name].........."

    e ".......my house......."

    n "vio snifs sadly"

    show vio sad at vio_scale
    e "....It's gone...."

    e "...I-i don't know what to do...."

    e "...Could you let me stay at your place?"

    menu:
        "Yeah. It's alright. It's late too, better late than never.":
            pass

        "...It's uh.... too messy?":
            jump vio_left_her_ending

    show vio tiredhappy at vio_scale
    e "...T-thank you..."

    show vio extremelyhappy at vio_scale
    e ""

    scene bg playerhousenight:
        xysize (1920, 1080)
    with dissolve

    show vio tired at vio_left
    with dissolve

    e "Is...that your house?"

    show vio tiredhappy at vio_left
    e "Looks nice....."

    show vio sleeping at vio_left
    e "zzz....! HUH?"

    show vio shocked at vio_left
    e ""

    show vio tired at vio_left
    e "...S-sorry........I-i'm so tired..."

    e "....Could you carry me inside.......? ...I'm really tired."

    menu:
        "Yes":
            pass

    scene bg insidehouse:
        xysize (1920, 1080)
    with dissolve

    show vio tired at vio_scale
    with dissolve

    e "...I-it's wonderful..."

    show vio tiredhappy at vio_scale
    e "...hehehe......"

    n "Vio collapses due to overexaustion"

    show vio sleepinghappy at vio_scale
    e ""

    $ couch_button_text = "Put her on the couch"

    label carry_choice_loop:
        menu:
            "Carry Vio to bedroom":
                pass

            "[couch_button_text]":
                $ couch_button_text = "She's cold. The bed's better."
                jump carry_choice_loop

    scene bg insidehousethree:
        xysize (1920, 1080)
    with dissolve

    n "You carefully tuck her into your bed. Then you get in next to her. Being sure not to wake her, not that you would."

    scene bg playerhousenight:
        xysize (1920, 1080)
    with dissolve

    $ renpy.pause(3.0, hard=True)

    scene bg playerhouse:
        xysize (1920, 1080)
    with dissolve


    # --- SCENE THREE ---

    scene bg insidehousefour:
        xysize (1920, 1080)
    with dissolve

    show vio sleepinghappy at vio_scale
    e ""

    # Quick eye-opening animation sequence (smug -> happy)
    show vio smug at vio_scale
    $ renpy.pause(0.15)
    show vio happy at vio_scale
    e ""

    e "...Morning."

    n "You're awake"

    show vio happy at vio_scale
    e "T-thank you for...last night..."

    e "Could I hug you?"

    menu:
        "Yes":
            show vio veryhappy at vio_scale
            e "R-REALLY?"

            show vio extremelyhappy at vio_scale
            e "T-thank you!"

            n "Vio hugs you, tight."
            n "This is when you realize she kinda smells like cinnamon."

            menu:
                "Why do you smell like cinnamon?":
                    pass

            show vio happy at vio_scale
            e "...It's natural!!"

            show vio ehh at vio_scale
            e "Why...don't we go out somewhere?"

        "No":
            show vio sad at vio_scale
            e "A-alright..."

            n "Vio leans against you."
            n "This is when you realize she kinda smells like cinnamon."

            menu:
                "Why do you smell like cinnamon?":
                    pass

            show vio disappointed at vio_scale
            e "...It's natural...!"

            show vio disappointedtwo at vio_scale
            e "Why don't we go out somewhere......?"

            menu:
                "Yeah, we should.":
                    pass

                "I'm tired" (disable=True):
                    pass

    show vio happy at vio_scale
    e "...Yeah...."

    n "You, [player_name] and Vio both walk outside."

    scene bg grass:
        xysize (1920, 1080)
    with dissolve

    # Stikman on left, Vio on right
    show stikman happy at stikman_left
    show vio extremelyhappy at vio_right
    with dissolve

    s "...HEY KID."
    s "COME HERE~"

    n "Vio steps closer."

    show stikman reallyhappy at stikman_left
    s "YIPPEEE"

    show stikman pulloutknife at stikman_left
    s ""

    show stikman holdoutknife at stikman_left
    s ""

    show stikman stab at stikman_left
    s "HEHEHEHEHHEHEHE"

    show vio staretwyouwhilestabbed at vio_right
    e "AAH!!!!!!!"

    show stikman joy at stikman_left
    s "HEHEHEHEHEHEHEHEHAHAHAHAHAHAHAHA"

    show vio looksatstabwound at vio_right
    e "....OWWW.....FUCK."

    menu:
        "PUNCH STIKMAN IN FACE":
            pass

        "ECAF NI NAMKITS HCNUP":
            pass

    show stikman tired at stikman_left
    s "HOLY COW!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    show stikman shout at stikman_left
    s "WHY"
    s "YOU"
    s "LITTLE"
    s "PEICE"
    s "OF"
    s "SHIT."

    show stikman thumbsup at stikman_left
    s "THAT WAS JUST AMAZINGGGG!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    show stikman hehe at stikman_left
    s "NOW, [player_name]. GO ███ YOURSELF."

    show stikman illalwaysbehere at stikman_left
    s "LOOK KID, I'LL ALWAYS BE HERE. HEHEHHEAHHEHE..."

    show stikman angry at stikman_left
    s "AND LOOK, [player_name]. YOU SHOULD GO ████████████████."

    show stikman byebye at stikman_left
    s "BYE BYEE"

    show stikman byby at stikman_left
    s ""

    show stikman bb at stikman_left
    s ""

    show stikman yy at stikman_left
    s ""

    hide stikman with Pixellate(0.3, 5)

    n "Stikman ████es out of reality."

    n "Vio grabs your leg."

    show vio dizzy at vio_scale
    e "...Call someone....anyone..."

    n "You pull out your phone, and call emergency services."

    scene bg black:
        xysize (1920, 1080)
    with dissolve

    n "Eventually, the ambulance came. You were able to stop her wound from bleeding out too much, Vio herself is too weak to say anything. She feels stupid."
    n "After getting the discharge papers, you two were allowed to go home, so you did."

    scene bg insidehousetwo:
        xysize (1920, 1080)
    with dissolve

    show vio cryingbandaged at vio_scale
    e ""

    n "You walk over to Vio, and put your hand on her shoulder, patting it softly."

    show vio lookawayfromyoubandaged at vio_scale
    e ""

    menu:
        "Vio, you need rest.":
            pass

        "Vio. Sleep. Now.":
            pass

    show vio cryingbandaged at vio_scale
    e ""

    n "Vio nods, then hugs you, then winces."
    n "She wanted to show you more affection but was too sore to DO anything more."
    n "You hold Vio in your arms as she falls asleep. You then go to your bedroom and tuck her in carefully."

    scene bg insidehousefour:
        xysize (1920, 1080)
    with dissolve

    show vio lookawayfromyoubandaged at vio_scale
    e ""

n "Vio hugs you really tightly, then kisses you, very lightly on the cheek."
n "Vio falls asleep."

jump true_ending
n ""
n "Hey, [player_name] could you help me out?"
n "...Yeah, me the text."

    menu:
        "Yes":
            pass

        "No":
            return

# Shiver test
    scene bg white:
    show shiver uwu
    e "This is a test."
return


# Bad ending handler for when you leave her
label vio_left_her_ending:
    scene bg youlefther:
        xysize (1920, 1080)
    with dissolve
    n ""
    return


# Bad ending handler for when Vio gets pissed
label vio_pissed_ending:
    scene bg viopissed:
        xysize (1920, 1080)
    with dissolve
    n ""
    return

# Bad ending handler for the true ending
label true_ending:
    scene bg true:
        xysize (1920, 1080)
    with dissolve
    n ""
    return