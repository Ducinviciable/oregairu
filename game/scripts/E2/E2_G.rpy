label E2_G04_01:
    scene black with Fade(1.0, 1.5, 0)
    play sound "audio/sfx/SE04/SE04_06.ogg"
    scene outsideA
    with Fade(0, 2, 1.0)
    play music "audio/bgm/BGM06.ogg"
    window auto show dissolve
    voice "audio/voice/E2/G04/01/HA/HA000.ogg"
    hachiman "Did you lock the door?"
    show komachi coat mid_left sad at center with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E2/G04/01/KO/KO000.ogg"
    komachi "It's locked. It's cold...!"
    voice "audio/voice/E2/G04/01/HA/HA001.ogg"
    hachiman "It's winter after all. Okay, ready to go?"
    show komachi coat mid_center happy at center with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E2/G04/01/KO/KO001.ogg"
    komachi "Yup, so where are we going?"
    voice "audio/voice/E2/G04/01/HA/HA002.ogg"
    hachiman "Let's see..."
    menu outside_menu:
        with dissolve
        hachiman "(Somewhere Komachi will be able to take her mind off things...)"
        "Do you want to go see the high school?":
            $komachiHelpFlag = "saki"
            voice "audio/voice/E2/G04/01/HA/HA003.ogg"
            hachiman "Wanna go see the school?"
            show komachi surprised with dissolve
            voice "audio/voice/E2/G04/01/KO/KO002.ogg"
            komachi "Your school?"
            voice "audio/voice/E2/G04/01/HA/HA004.ogg"
            hachiman "Yeah. You were there during the festival, so it might be nothing new to you, but it's good scope out your school of choice. I think it's a good way to renew your vigour..."
            "Immediately after I made the suggestion, I regretted it. I wonder if I cornered Komachi. She looks anxious..."
            # google translated ^
            show komachi mid_left frown with dissolve:
                xoffset 5 yoffset 75
            voice "audio/voice/E2/G04/01/KO/KO003.ogg"
            komachi "Hmm... Should we ride the bike there?"
            voice "audio/voice/E2/G04/01/HA/HA005.ogg"
            hachiman "Well, it's a bit far, but let's try walking there."
            voice "audio/voice/E2/G04/01/HA/HA006.ogg"
            hachiman "We can use the bus on the way home. The streets aren't really crowded today."
            show komachi happy with dissolve
            voice "audio/voice/E2/G04/01/KO/KO004.ogg"
            komachi "You're right. Walking is a nice change of pace... Let's get a move on then."
            voice "audio/voice/E2/G04/01/HA/HA007.ogg"
            hachiman "Okay then, we're now departing for school."
            show komachi unimpressed with dissolve
            voice "audio/voice/E2/G04/01/KO/KO005.ogg"
            komachi "What was that? Onii-chan, if you want to become a tour guide or anything similar, forget about it. You'll suck the excitement out of everyone straight away."
            voice "audio/voice/E2/G04/01/HA/HA008.ogg"
            hachiman "I'm not interested in any job that requires that level of communication skills, and, more importantly, I will never work."
            show komachi vhappy with dissolve
            voice "audio/voice/E2/G04/01/KO/KO006.ogg"
            komachi "Yeah, I knew about that already."
            window auto hide dissolve
            stop voice
            stop music fadeout 1.0
            jump E2_SAK_01
        "Do you want to go up to the front of the station?": #yukino
            $komachiHelpFlag = "yukino"
            hachiman "(Okay, where to go... Somewhere that will take her mind off the exams.)"
            hachiman "(But I can't think of a place except for Saize... But no, it can't be Saize...)"
            voice "audio/voice/E2/G04/01/HA/HA009.ogg"
            hachiman "Don't you have anywhere you want to go?"
            hide komachi
            $url = ["komachi coat mid_center angry", "komachi coat mid_center surprised2"]
            $multiImagePara = [-75, 75, 0, 0, 3.75]
            call multiImage() from _call_multiImage_23
            voice "audio/voice/E2/G04/01/KO/KO007.ogg"
            komachi "Somewhere I want to go? Not really...? Ah!"
            call finishmultiImage from _call_finishmultiImage_24
            show komachi coat mid_center angry at center:
                xoffset -75 yoffset 75
            with dissolve
            voice "audio/voice/E2/G04/01/KO/KO008.ogg"
            komachi "I wanna eat taiyaki sweets."
            voice "audio/voice/E2/G04/01/HA/HA010.ogg"
            hachiman "Taiyaki Sweets?"
            show komachi mid_left vhappy at center with dissolve:
                xoffset 0 yoffset 75
            voice "audio/voice/E2/G04/01/KO/KO009.ogg"
            komachi "Yup! Those taiyaki that look like parfaits with soft cream or ice cream in them!"
            voice "audio/voice/E2/G04/01/HA/HA011.ogg"
            hachiman "That's not even a taiyaki anymore but just a parfait... so, where can you get them?"
            show komachi happy with dissolve
            voice "audio/voice/E2/G04/01/KO/KO010.ogg"
            komachi "I heard they're in a shop at Kaihin-makuhari station."
            voice "audio/voice/E2/G04/01/HA/HA012.ogg"
            hachiman "Oh..."
            hachiman "(Well, I do like sweet stuff too...)"
            voice "audio/voice/E2/G04/01/HA/HA013.ogg"
            hachiman "Then wanna get going?"
            show komachi mid_center vhappy at center with dissolve:
                xoffset -75 yoffset 75
            voice "audio/voice/E2/G04/01/KO/KO011.ogg"
            komachi "Hooray!!"
            window auto hide dissolve
            stop voice
            stop music fadeout 1.0
            jump E2_YUK_01

label E2_G05_01:
    play sound ["<silence 2.5>", "audio/sfx/SE04/SE04_06.ogg"]
    scene outsideA with Fade(1.0, 1.0, 1.0)
    play sound "audio/sfx/SE02/SE02_01.ogg"
    $renpy.pause(delay=1.0, hard=True)
    window auto show dissolve
    voice "audio/voice/E2/G05/01/HA/HA000.ogg"
    hachiman "God, it's cold..."
    hachiman "(Well, it is winter after all, what are you gonna do? Let's get this over with quickly...)"
    window auto hide dissolve
    stop sound
    scene khstationA
    with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/BGM08.ogg"
    play ambient "audio/sfx/SE05/SE05_01L.ogg"
    window auto show dissolve
    hachiman "(Hmm. Should I buy her pastry or Japanese style candy? Ah, just buying both seems best.)"
    stop ambient fadeout 0.5
    menu E2_G05_01_menu:
        with dissolve
        hachiman "(Hmm? That's...)"
        "A puppy trio.": #yui route
            play sound "audio/sfx/SE07/SE07_00.ogg"
            hachiman "(Oh, it's a puppy trio. They sure are energetic considering the cold.)"
            hachiman "(Dogs are so cute...)"
            stop music fadeout 1.25
            play sound "audio/sfx/SE02/SE02_00.ogg"
            voice "audio/voice/E2/YUI/01/HA/HA000.ogg"
            hachiman "Ah, so cold..."
            stop sound fadeout 1.0
            jump E2_YUI_01
        "The local cat gathering.":
            $komachiHelpFlag = "haruno meguri"
            jump E2_HAR_01
        "It's so crowded in the city...":
            "not done"
            jump E2_G05_01_menu

label E2_G06_01:
    scene houseA with Fade(0.5, 1.5, 0.5)
    play music ["<silence 0.3>", "audio/bgm/BGM06.ogg"]
    window auto show dissolve
    "After Komachi calmed down, the living room was quiet."
    play sound "audio/sfx/SE03/SE03_03.ogg"
    $renpy.pause(delay=1.5, hard=True)
    show komachi athletic mid_center surprised at center with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E2/G06/01/KO/KO002.ogg"
    komachi "Ah that's rare. Onii-chan's phone is ringing."
    voice "audio/voice/E2/G06/01/HA/HA002.ogg"
    hachiman "What... are you trying to say...?"
    "Komachi took the phone I had left on the sofa. She looked at it and..."
    if shrineMeetFlag == "hiratsuka":
        menu:
            hachiman "(There aren't many people who know my number, but the ones who know might call me out of the blue...)"
            with dissolve
            "I have a bad feeling about this...":
                pass
            "I have... a bad feeling about this.":
                $komachiHelpFlag = "hiratsuka"
                voice "audio/voice/E2/G06/01/HA/HA006.ogg"
                hachiman "I shouldn't pick it up! My gut is telling me I shouldn't!"
                voice "audio/voice/E2/G06/01/KO/KO005.ogg"
                komachi "Stop exaggerating... Oh, Onii-chan, you're sweating bullets. Ah, you got a message."
                voice "audio/voice/E2/G06/01/HA/HA007.ogg"
                hachiman "See no evil, hear no evil, pick up no evil..."
                show komachi pout with dissolve
                voice "audio/voice/E2/G06/01/KO/KO006.ogg"
                komachi "It-It's still going... I don't think it's going to stop until you pick up."
                voice "audio/voice/E2/G06/01/HA/HA008.ogg"
                hachiman "This is actually scary."
                show komachi sad with dissolve
                voice "audio/voice/E2/G06/01/KO/KO007.ogg"
                komachi "Komachi is scared too."
                jump E2_SHI_02
    $komachiHelpFlag = "iroha"
    "At that moment, what appeared in my mind was a sly kouhai's face. It's definitely her..."
    voice "audio/voice/E2/G06/01/HA/HA003.ogg"
    hachiman "Okay, you can hang up for me."
    show komachi unimpressed with dissolve
    voice "audio/voice/E2/G06/01/KO/KO003.ogg"
    komachi "What's okay about that..."
    voice "audio/voice/E2/G06/01/HA/HA004.ogg"
    hachiman "No, I mean if someone is calling, that means that person is probably bad news..."
    hide komachi
    $url = ["komachi athletic mid_center pout", "komachi athletic mid_center surprised"]
    $multiImagePara = [-75, 75, 0, 0, 3.25]
    call multiImage(0) from _call_multiImage_89
    voice "audio/voice/E2/G06/01/KO/KO004.ogg"
    komachi "Ah I see, then I'll hang up for you... Oh."
    call finishmultiImage from _call_finishmultiImage_93
    show komachi athletic mid_center surprised at center:
        xoffset -75 yoffset 75
    play sound "audio/sfx/SE03/SE03_02.ogg"
    $renpy.pause(delay=1.0, hard=True)
    voice "audio/voice/E2/G06/01/HA/HA005.ogg"
    hachiman "...What?"
    jump E2_IRO_01
