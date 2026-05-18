label E1_SHI_01:
    window auto show dissolve
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E1/SHI/01/SZ/SZ000.ogg"
    mystery "Oh? It's the Hikigayas."
    voice "audio/voice/E1/SHI/01/HA/HA000.ogg"
    hachiman "We've been spotted..."
    window auto hide dissolve
    play music "audio/bgm/BGM16.ogg"
    show hiratsukaShootinga with Dissolve(2.0)
    window auto show dissolve
    voice "audio/voice/E1/SHI/01/SZ/SZ001.ogg"
    hiratsuka "Happy New Year. I'm glad to see both of you doing well."
    "There was Hiratsuka-sensei, holding a rifle in an unnecessarily manly way, smiling at us."
    voice "audio/voice/E1/SHI/01/HA/HA001.ogg"
    hachiman "Happy New Year..."
    voice "audio/voice/E1/SHI/01/KO/KO000.ogg"
    komachi "Happy New Year!"
    voice "audio/voice/E1/SHI/01/HA/HA002.ogg"
    hachiman "Anyway, what are you even doing! You've been making a lot of noise here..."
    voice "audio/voice/E1/SHI/01/SZ/SZ002.ogg"
    hiratsuka "Can't you tell by looking? We're at a shooting stall."
    voice "audio/voice/E1/SHI/01/HA/HA003.ogg"
    hachiman "Well, I can see that much, but..."
    voice "audio/voice/E1/SHI/01/KO/KO001.ogg"
    komachi "Hiratsuka-sensei, are you good at this kind of thing?"
    show hiratsukaShootingb with dissolve
    voice "audio/voice/E1/SHI/01/SZ/SZ003.ogg"
    hiratsuka "Well... no... not really."
    voice "audio/voice/E1/SHI/01/KO/KO002.ogg"
    komachi "Ah, onii-chan, Komachi has an exam to prepare for, so I'll just buy some candy apples and yakisoba and go home ahead."
    voice "audio/voice/E1/SHI/01/HA/HA004.ogg"
    hachiman "Huh?"
    voice "audio/voice/E1/SHI/01/KO/KO003.ogg"
    komachi "Well then, Hiratsuka-sensei, see you!"
    hachiman "(Komachi found this too tiresome and went on home...)"
    voice "audio/voice/E1/SHI/01/SZ/SZ004.ogg"
    hiratsuka "...Hikigaya."
    hachiman "(Ah, you want me to try. Alright, alright...)"
    hachiman "(\"Marriage-prayer set\"? That thing is hopeless no matter how you look at it...)"
    voice "audio/voice/E1/SHI/01/HA/HA005.ogg"
    hachiman "Is that the one you want?"
    voice "audio/voice/E1/SHI/01/SZ/SZ005.ogg"
    hiratsuka "...Yeah."
    voice "audio/voice/E1/SHI/01/SZ/SZ006.ogg"
    hiratsuka "Hikigaya, take this gun from me. My arms have become useless."
    voice "audio/voice/E1/SHI/01/HA/HA006.ogg"
    hachiman "Hah..."
    voice "audio/voice/E1/SHI/01/SZ/SZ007.ogg"
    hiratsuka "...Don't worry about the bill, just do it."
    hachiman "(For having such great sense of grim resolve resonating in her voice, she's saying some pretty sad things...)"
    voice "audio/voice/E1/SHI/01/HA/HA007.ogg"
    hachiman "Ah, why don't you ask Yukinoshita to get it for you? She seems pretty good at this stuff, unlike me..."
    voice "audio/voice/E1/SHI/01/SZ/SZ008.ogg"
    hiratsuka "I tried calling out to her earlier, but she just brushed me off like it was only natural."
    voice "audio/voice/E1/SHI/01/HA/HA008.ogg"
    hachiman "Well, yeah, I can totally see why."
    voice "audio/voice/E1/SHI/01/SZ/SZ009.ogg"
    hiratsuka "What do you mean you can \"totally see why\"? Anyway, are you gonna help me or not?"
    hachiman "(Well, it can't be helped. Guess I'll give it a shot...)"
    voice "audio/voice/E1/SHI/01/HA/HA009.ogg"
    hachiman "I'm not really good at this, just so you know."
    hide hiratsukaShootingb with dissolve
    voice "audio/voice/E1/SHI/01/SZ/SZ010.ogg"
    hiratsuka "I'm forever in your debt."
    voice "audio/voice/E1/SHI/01/HA/HA010.ogg"
    hachiman "!!"
    "Hiratsuka-sensei then walked up to me and handed me a cork gun in a needlessly dramatic manner."
    hachiman "(Ah, she's a bit too close...!)"
    voice "audio/voice/E1/SHI/01/SZ/SZ011.ogg"
    hiratsuka "That one! That's our target!"
    hachiman "(\"Marriage-prayer set\", huh...)"
    voice "audio/voice/E1/SHI/01/HA/HA011.ogg"
    hachiman "Roger that."
    window auto hide dissolve
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE01/SE01_62.ogg"
    $renpy.pause(delay=0.5, hard=True)
    stop sound
    window auto show dissolve
    voice "audio/voice/E1/SHI/01/SZ/SZ012.ogg"
    hiratsuka "Looking good. Target's close! Fire at will!"
    window auto hide dissolve
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE01/SE01_62.ogg"
    $renpy.pause(delay=0.5, hard=True)
    stop sound
    window auto show dissolve
    voice "audio/voice/E1/SHI/01/SZ/SZ013.ogg"
    hiratsuka "One more time!"
    voice "audio/voice/E1/SHI/01/HA/HA012.ogg"
    hachiman "On it..."
    window auto hide dissolve
    scene black with fade
    play sound "audio/sfx/SE01/SE01_62.ogg"
    scene market
    show hiratsuka coat mid_center sad at center:
        xoffset 40 yoffset 75
    with Fade(0, 0.5, 1.0)
    $renpy.pause(delay=0.5, hard=True)
    stop sound
    window auto show dissolve
    voice "audio/voice/E1/SHI/01/ZB/ZB000.ogg"
    sk "Man, enough of that. Here you go, lady, on the house."
    show hiratsuka mid_left happy with dissolve:
        xoffset 140 yoffset 80
    voice "audio/voice/E1/SHI/01/SZ/SZ014.ogg"
    hiratsuka "Th-Thank you so much...!"
    show hiratsuka vhappy with dissolve
    "The owner of the stall, who just couldn't ignore the fact that I missed every single shot, handed over the set I was aiming for."
    hachiman "(\"Marraige-prayer set\"...)"
    show hiratsuka mid_center with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E1/SHI/01/SZ/SZ015.ogg"
    hiratsuka "I owe you, Hikigaya! Big time!"
    voice "audio/voice/E1/SHI/01/HA/HA013.ogg"
    hachiman "That's alright, you really don't. I'm just glad you got what you wanted."
    hide hiratsuka
    $url = ["hiratsuka coat mid_center happy", "hiratsuka coat mid_left vhappy"]
    $multiImagePara = [40, 75, 140, 80, 10.2]
    call multiImage(0, False) from _call_multiImage_22
    voice "audio/voice/E1/SHI/01/SZ/SZ016.ogg"
    hiratsuka "Feh. Well, it was a bit immature of me to get so worked up over not being able to get it. Some things truly do require hard work and persistance. {size=35} With this I'll get married for sure...!"
    call finishmultiImage from _call_finishmultiImage_23
    show hiratsuka coat mid_left vhappy at center:
        xoffset 140 yoffset 80
    hachiman "(Someone please marry this woman.)"
    window auto hide dissolve
    stop music fadeout 0.5
    jump E1_CMM_02