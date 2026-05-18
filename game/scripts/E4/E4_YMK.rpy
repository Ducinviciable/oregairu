label E4_YMK_07:
    $hayamaTalk = True
    scene black with Fade(0.5, 0.5, 0)
    play sound "audio/sfx/SE04/SE04_18.ogg"
    scene parkA with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    hachiman "(Hmm? Hayama is here, too...)"
    stop sound
    show hayama school mid_center surprised at center with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E4/YMK/07/HY/HY000.ogg"
    hayama "Ah, Hikigaya..."
    voice "audio/voice/E4/YMK/07/HA/HA000.ogg"
    hachiman "Yo."
    hachiman "(Too bad it was Hayama. Not that I wanted to see anyone else in particular...)"
    window auto hide dissolve
    show hayama happy with dissolve
    play sound "audio/sfx/SE01/SE01_77.ogg"
    $renpy.pause(delay=1.0, hard=False)
    window auto show dissolve
    voice "audio/voice/E4/YMK/07/HY/HY001.ogg"
    hayama "Here."
    play sound "audio/sfx/SE01/SE01_74.ogg"
    $renpy.pause(delay=0.5, hard=False)
    "Hayama, who had been here first, took a drink that came out of the vending machine and tossed it my way."
    play sound "audio/sfx/SE01/SE01_75.ogg"
    $renpy.pause(delay=0.5, hard=False)
    hachiman "(Black coffee, huh? Your taste isn't terible, at least...)"
    $renpy.pause(delay=0.5, hard=False)
    play music "audio/bgm/BGM10.ogg"
    voice "audio/voice/E4/YMK/07/HA/HA001.ogg"
    hachiman "Ah, thanks."
    voice "audio/voice/E4/YMK/07/HY/HY002.ogg"
    hayama "I thought I'd go with the sugar-free one. Or maybe the sweeter one would've been better?"
    voice "audio/voice/E4/YMK/07/HA/HA002.ogg"
    hachiman "Are you being sarcastic? I thought I was careful going to that cake shop, but apparently not."
    voice "audio/voice/E4/YMK/07/HY/HY003.ogg"
    hayama "Well.. I really admire you capability to deal with something like that the way you did."
    voice "audio/voice/E4/YMK/07/HA/HA003.ogg"
    hachiman "If we're talking about capability, I bet you can handle everything from sweet making to actual cooking perfectly. It won't even surprise me if that's the case."
    show hayama relieved with dissolve
    voice "audio/voice/E4/YMK/07/HY/HY004.ogg"
    hayama "No, of course I can't. Though I may look like I can, I'm just a run of the mill soccer player."
    hachiman "(To be able to dumb all his attributes like that... As expected of him)"
    "While I was having a meaningless conversation with Hayama, I thought about the sisters with universal attributes"
    show hayama school mid_right happy at center with dissolve:
        xoffset -25 yoffset 65
    voice "audio/voice/E4/YMK/07/HY/HY005.ogg"
    hayama "...At any rate, you've thought it through."
    voice "audio/voice/E4/YMK/07/HA/HA005.ogg"
    hachiman "What~?"
    "Because of how nonchalantly he just cut right into the topic, I wasn't able to respond with more than a little squeek, to which Hayama showed a relieved smile."
    voice "audio/voice/E4/YMK/07/HY/HY006.ogg"
    hayama "Because of what you did, everyone is able to act naturally. Even so as far as Tobe, who is able to stuff himself with chocolates now, is delighted about it."
    voice "audio/voice/E4/YMK/07/HA/HA006.ogg"
    hachiman "............"
    voice "audio/voice/E4/YMK/07/HA/HA007.ogg"
    hachiman "So... Are you able to, too?"
    "Hayama says \"everyone\". But does he really mean everyone? When I asked, Hayama smiled a bittersweet smile."
    show hayama relieved with dissolve
    voice "audio/voice/E4/YMK/07/HY/HY007.ogg"
    hayama "I'm always going to be the me I am now, you know."
    voice "audio/voice/E4/YMK/07/HA/HA008.ogg"
    hachiman "That person said it, didn't she? That you don't have any demands of your own."
    "After those words left my mouth, I wondered if I had overstepped my boundaries. But since she is truly the main source of strain in this event, I guess I had no choice but to say what I did."
    show hayama happy with dissolve
    voice "audio/voice/E4/YMK/07/HY/HY008.ogg"
    hayama "Haruno-san is very observant and takes in a lot of the world around her, but she's incredibly cold when it comes to things she's not interested in."
    hachiman "(Well, that's true...)"
    show hayama school mid_center happy at center with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E4/YMK/07/HY/HY009.ogg"
    hayama "She's taken quite the liking to you, you know."
    voice "audio/voice/E4/YMK/07/HA/HA009.ogg"
    hachiman "Making fun of me is all she's doing, not that I ever asked for it."
    show hayama relieved with dissolve
    voice "audio/voice/E4/YMK/07/HY/HY010.ogg"
    hayama "............"
    "Hayama responded with a small chuckle to my crude remark."
    show hayama frown with dissolve
    voice "audio/voice/E4/YMK/07/HY/HY011.ogg"
    hayama "I've told you before that I don't like that about you."
    voice "audio/voice/E4/YMK/07/HA/HA010.ogg"
    hachiman "I think we're equal in that regard."
    voice "audio/voice/E4/YMK/07/HY/HY012.ogg"
    hayama "............"
    hachiman "(I don't know why I can't stay away from talking about her after all, even though I brush her off everytime. I pity Miura and Isshiki, whose names aren't even mentioned.)"
    voice "audio/voice/E4/YMK/07/HA/HA011.ogg"
    hachiman "Well, go do your job, Mr. Taste-Tester."
    show hayama school mid_right frown at center with dissolve:
        xoffset -25 yoffset 65
    voice "audio/voice/E4/YMK/07/HY/HY013.ogg"
    hayama "...You truly do not know your own value."
    hide hayama with dissolve
    play sound "audio/sfx/SE04/SE04_18.ogg"
    $renpy.pause(delay=1.0, hard=False)
    "Hayama seemed to dissmiss our conversation with that and returned to the venue. The aftertaste of the black coffee, which I usually didn't drink much of, was bitter in my mouth."
    "When I think about it, my conversations with Hayama always seem to take place in such a way to avoid the central point."
    "I sometimes wonder what the point of our conversations really is? Is it really just nothingness? I dont know."
    "Just as Hayato Hayama is doing his best to be \"insincere\", I've been swept up in my own self-consciousness, not knowing what the \"real thing\" is, and not being able to find it."
    window auto hide dissolve
    show hallwayB
    show ebina school_sunset mid_center angry at center:
        xoffset 65 yoffset 75
    with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    voice "audio/voice/E4/YMK/07/EB/EB000.ogg"
    ebina "You can pretend to accept everyone and not left anyone get close, or you can pretend to reject everyone and peacefully live in the status quo. What's the difference, I wonder?"
    voice "audio/voice/E4/YMK/07/HA/HA012.ogg"
    hachiman "It's... the difference in motive, I guess."
    voice "audio/voice/E4/YMK/07/EB/EB001.ogg"
    ebina "I feel like I understand both sides of that."
    hachiman "(I guess we're kind of alike...)"
    window auto hide dissolve
    stop music fadeout 1.0
    hide ebina
    hide hallwayB
    with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    play music "audio/bgm/BGM44.ogg"
    hachiman "(Oh no, this isn't supposed to be the world of HayaHachi! It might be Ebina-sans's poisonous mid waves! Scary!)"
    window auto hide dissolve
    play sound ["<silence 0.6>", "audio/sfx/SE02/SE02_19.ogg"]
    show totsukaClassroom with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    voice "audio/voice/E4/YMK/07/SI/SI000.ogg"
    totsuka "I think it's a wonderful thing to be able to get closer to someone."
    stop sound
    hachiman  "(If the distance between Totsuka and me shortens, I'm totally fine with that. In fact, I'd welcome it.)"
    window auto hide dissolve
    stop music fadeout 1.0
    hide totsukaClassroom with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    hachiman "(W-well, it's time I get back...)"
    window auto hide dissolve
    jump E4_G02_01
