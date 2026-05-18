label E5_G13_01:
    scene slopesA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM44.ogg"
    window auto show dissolve
    voice "audio/voice/E5/G13/01/HA/HA000.ogg"
    hachiman "But still..."
    play sound "audio/sfx/SE01/SE01_46.ogg"
    "When the cleaning was done and we'd put our luggage away, I was immediately (and forcibly) taken to the ski slopes."
    hachiman "(Seriously, what am I supposed to do? I don't get anything at all...)"
    play sound "<to 1>audio/sfx/SE01/SE01_47.ogg" fadeout 0.5
    image komachi heavy_coat mid_left happy flat = Flatten("komachi heavy_coat mid_left happy")
    image yui heavy_coat mid_left happy flat = Flatten("yui heavy_coat mid_left happy")
    show komachi heavy_coat mid_left happy flat at center:
        xoffset 500 yoffset 75 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.5 xoffset 5
    $renpy.pause(delay=0.5, hard=True)
    hide komachi
    show komachi heavy_coat mid_center vhappy1 at center:
        xoffset -75 yoffset 75
    with dissolve
    voice "audio/voice/E5/G13/01/KO/KO000.ogg"
    komachi "Onii-chan! I don't really get what I'm doing, but it's fun!"
    show komachi heavy_coat mid_left happy flat with dissolve:
        xoffset 5 alpha 1.0
        on hide:
            parallel:
                linear 0.5 alpha 0
            parallel:
                easeout 0.5 xoffset -400
    hide komachi
    play sound "audio/sfx/SE01/SE01_46.ogg"
    $renpy.pause(delay=0.5, hard=True)
    hachiman "(Komachi playing in the snowy world is the cutest in the world... And you got used to this place way too quickly...)"
    play sound "<from 1>audio/sfx/SE01/SE01_48.ogg" fadein 0.5
    show yui heavy_coat mid_left happy at center:
        xoffset 500 yoffset 75 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.5 xoffset 10
    $renpy.pause(delay=0.5, hard=True)
    hide yui
    show yui heavy_coat mid_center vhappy1 at center:
        xoffset 10 yoffset 75
    with dissolve
    voice "audio/voice/E5/G13/01/YI/YI000.ogg"
    yui "Hikki, you should ski too!"
    show yui heavy_coat mid_left happy flat with dissolve:
        xoffset 10 alpha 1.0
        on hide:
            parallel:
                linear 0.5 alpha 0
            parallel:
                easeout 0.5 xoffset -400
    hide yui
    play sound "audio/sfx/SE01/SE01_45.ogg"
    $renpy.pause(delay=0.5, hard=True)
    hachiman "(No choice... It's awkward just standing around too so I should just go ask someone.)"
    menu slopes_question1:
        hachiman "(That being said, what do I even ask them...?)"
        with dissolve
        "I want to become good at this": #yukino
            $ski_flag = "yukino"
            hachiman "(I've come all this way, so I want to become good at... this?)"
            "I may be talking about myself, but my willpower is so pathetic it's sad. But, rather than mixing in with the inept lot,
            it'd make me feel better to ski alone with some level of ability."
            hachiman "(But for that, the only people I could ask to teach me were scary people...)"
            hachiman "(No matter how much I thought about it, it'd be great if she could teach me. Even if she was strict, she would take it seriously.)"
            hachiman "(Thinking about it, from the very beginning since I'd met her, I'd never thought of her that way...)"
            #E5_YUK_02 starts here, if following scripts
            jump E5_YUK_02
        "It's fine as long as I'm having fun":#iroha
            $ski_flag = "iroha"
            jump E5_IRO_02
        "I'll learn, slow and steady...":#yui
            $ski_flag = "yui"
            hachiman "(Well, no matter how high my hopes to learn might be, we're only here 2 days, so I'm not expecting anything. Slow and steady is fine. I'll relish the feeling of the fact I'm actually skiing and go slow...)"
            "This isn't to say I don't want to improve at all. I'm just a realist. I just wanted to pat myself on the back for having fun in my own way."
            hachiman "(That said, the problem is who to ask to have teach me...)"
            stop music fadeout 1.2
            play sound "audio/sfx/SE01/SE01_46.ogg"
            "At that moment, someone came into my mind. Someone gentle, hardworking, and a girl who's really concerned with what other people's feelings. Thinking about it, that's the kind of person you want teaching you after all."
            hachiman "(Should I buck up and call out?)"
            play sound "<from 1>audio/sfx/SE01/SE01_48.ogg" fadein 0.5
            show yui heavy_coat mid_left happy at center:
                xoffset 500 yoffset 75 alpha 0
                parallel:
                    linear 0.5 alpha 1.0
                parallel:
                    easein 0.5 xoffset 10
            $renpy.pause(delay=0.5, hard=True)
            hide yui
            show yui heavy_coat mid_center happy at center:
                xoffset 10 yoffset 75
            with dissolve
            play music "audio/bgm/BGM12.ogg"
            voice "audio/voice/E5/G13/01/YI/YI001.ogg"
            yui "Ah, Hikki, what're you pondering about?"
            hachiman "(Ah, speak of the devil!)"
            voice "audio/voice/E5/G13/01/HA/HA001.ogg"
            hachiman "Ah. Well, just about how I can't ski."
            show yui heavy_coat mid_center surprised at center with dissolve:
                xoffset 10 yoffset 75
            voice "audio/voice/E5/G13/01/YI/YI002.ogg"
            yui "Huh?"
            hachiman "(Yeah, I guessed so. I can't just put it out like that.)"
            show yui heavy_coat mid_center blush at center with dissolve:
                xoffset 10 yoffset 75
            voice "audio/voice/E5/G13/01/YI/YI003.ogg"
            yui "Ah,um... If you're okay with me... do you want me to teach you? Though I'm not that great at it."
            voice "audio/voice/E5/G13/01/HA/HA002.ogg"
            hachiman "I-Is that alright?"
            show yui heavy_coat mid_center vhappy at center with dissolve:
                xoffset 10 yoffset 75
            voice "audio/voice/E5/G13/01/YI/YI004.ogg"
            yui "Of course! I promised, didn't I?"
            voice "audio/voice/E5/G13/01/HA/HA003.ogg"
            hachiman "You promised?"
            show yui heavy_coat mid_center surprised at center with dissolve:
                xoffset 10 yoffset 75
            voice "audio/voice/E5/G13/01/YI/YI005.ogg"
            yui "You forgot!?"
            voice "audio/voice/E5/G13/01/HA/HA004.ogg"
            hachiman "No. Sorry for making you do this."
            show yui heavy_coat mid_center vhappy at center with dissolve:
                xoffset 10 yoffset 75
            voice "audio/voice/E5/G13/01/YI/YI006.ogg"
            yui "Don't worry about it!"
            jump E5_YUI_02
