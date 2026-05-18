label E2_HAR_01:
    play sound "audio/sfx/SE07/SE07_02a.ogg"
    $renpy.pause(delay=0.5, hard=True)
    hachiman "(Oh! They're all gathered together! It's a cat get together! It's cold so they're all bunched up, huh...)"
    window auto hide dissolve
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE03/SE03_06.ogg"
    scene khstationA with Fade(0.1, 0.0, 0.5, color="#fff")
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    hachiman "(There, I'll that to Komachi later.)"
    hachiman "(Well then, I'll go look in the station's building for now....)"
    stop music fadeout 0.5
    voice "audio/voice/E2/HAR/01/HR/HR000.ogg"
    mystery "Hikigaya-kun! Yahallo!"
    voice "audio/voice/E2/HAR/01/HA/HA000.ogg"
    hachiman "............"
    play music ["<silence 0.5>", "audio/bgm/BGM35.ogg"]
    show haruno coat far_center happy at center with dissolve:
        xoffset 15 yoffset 75
    voice "audio/voice/E2/HAR/01/HR/HR001.ogg"
    haruno "To think I'd meet you here. Is this fate at work?"
    voice "audio/voice/E2/HAR/01/HA/HA001.ogg"
    hachiman "Ah, I'm just here to buy something for my sister."
    hide haruno with dissolve
    show haruno coat near_left vhappy at center with dissolve:
        xoffset 195 yoffset 75
    voice "audio/voice/E2/HAR/01/HR/HR002.ogg"
    haruno "Oh, I see. Then let Onee-san help you with that."
    hachiman "(Ah! She grabbed my arm! Something soft is pressing up against me, but I'm more scared than anything!)"
    hachiman "(I-It's not like I'm getting all excited, alright!?)"
    show haruno happy with dissolve
    voice "audio/voice/E2/HAR/01/HR/HR003.ogg"
    haruno "Now, where should we go, I wooonder~"
    voice "audio/voice/E2/HAR/01/HA/HA002.ogg"
    hachiman "Ah, well...."
    show haruno vhappy with dissolve
    voice "audio/voice/E2/HAR/01/HR/HR004.ogg"
    haruno"I got it! That one seems perfect!"
    window auto hide dissolve
    scene cakeShopA with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E2/HAR/01/HA/HA003.ogg"
    hachiman "Huh... This seems like a fancy cafe."
    window auto hide dissolve
    scene cakeShopA with dissolve:
        zoom 2.0 xalign 0 ypos -505
    show haruno sweater near_center vhappy at center with dissolve:
        xoffset -20 yoffset 75
    window auto show dissolve
    voice "audio/voice/E2/HAR/01/HR/HR005.ogg"
    haruno "The cakes here are delicious. You like sweet things, don't you?"
    voice "audio/voice/E2/HAR/01/HA/HA004.ogg"
    hachiman "Well, sure..."
    "I know full well that this person is not the pleasant older sister she appears to be. That's why, to be honest, I don't want to face her right now."
    "Even more so with the events from the New Year still lingering in my mind..."
    voice "audio/voice/E2/HAR/01/HA/HA005.ogg"
    hachiman "...By the way, how was your New Year?"
    show haruno happy with dissolve
    voice "audio/voice/E2/HAR/01/HR/HR006.ogg"
    haruno "Hmm~. Thanks to Yukino-chan joining, it was fun~"
    voice "audio/voice/E2/HAR/01/HA/HA006.ogg"
    hachiman "I think even Yukinoshita would be overwhelmed if she was abducted like that."
    show haruno annoyed with dissolve
    voice "audio/voice/E2/HAR/01/HR/HR007.ogg"
    haruno "That's a strange way of putting it. It's not like we were restraining her. And if she really didn't want to come, she could've refused, you know?"
    show haruno sly with dissolve
    voice "audio/voice/E2/HAR/01/HR/HR008.ogg"
    haruno "Besides, if you really wanted to help Yukino-chan, why didn't you just abduct her instead?"
    voice "audio/voice/E2/HAR/01/HA/HA007.ogg"
    hachiman "...Like in \"The Graduate\"? You're kidding. Me and her are not like that anyway."
    show haruno happy with dissolve
    voice "audio/voice/E2/HAR/01/HR/HR009.ogg"
    haruno"You're right. That's not very much like you... Because you won't be able to forgive someone, not even yourself, for running away."
    voice "audio/voice/E2/HAR/01/HA/HA008.ogg"
    hachiman "...That's not true. I often try to run away. Actually, I'd love to run away right now."
    voice "audio/voice/E2/HAR/01/HR/HR010.ogg"
    haruno "That's no good~. Oh, I know. How about we exchange contact information so you can't get away? We haven't done that yet, have we?"
    window auto hide dissolve
    stop voice
    stop voice fadeout 1.0
    stop music fadeout 1.0
    scene sidewalkB with Fade(1.0, 2.0, 1.0)
    play footsteps "<from 0 to 6.0>audio/sfx/SE00/SE00_07.ogg"
    window auto show dissolve
    hachiman "(...In the end, we exchanged our contact information.)"
    hachiman "(Now she can contact me anytime... Scary!)"
    voice "audio/voice/E2/HAR/01/HA/HA009.ogg"
    hachiman "............"
    stop footsteps
    hachiman "(Even so, I wonder if she enjoys messing with me.)"
    window auto hide dissolve
    stop voice
    scene cafeC
    show hayama school near_center pout at center:
        xoffset -15 yoffset 75
    with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    voice "audio/voice/E2/HAR/01/HY/HY000.ogg"
    hayama "That person wouldn't mess with people she had no interest in. ...Instead, she would ignore them. She would either smother the ones she likes, or destroy the ones she doesn't."
    window auto hide dissolve
    stop voice
    scene sidewalkB with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    voice "audio/voice/E2/HAR/01/HA/HA010.ogg"
    hachiman "............"
    voice "audio/voice/E2/HAR/01/HA/HA011.ogg"
    hachiman "Bet it's rather fun for her then..."
    window auto hide dissolve
    play footsteps "audio/sfx/SE00/SE00_03.ogg"
    $renpy.pause(delay=1.5, hard=True)
    stop footsteps fadeout 0.5
    $renpy.pause(delay=0.5, hard=True)
    call loading_screen(14, "35") from _call_loading_screen_22
    jump E3_CMM_01
