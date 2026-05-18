label E5_SHI_01:
    scene hotspringBGA with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "As a result of the lottery, I was put on bath cleaning duty with Totsuka. I rode the good fortune of being with him and tired to get the cleaning done as quickly as possibly."
    show totsuka home mid_center happy at center with dissolve:
        xoffset 10 yoffset 75
    play music "audio/bgm/BGM13.ogg"
    voice "audio/voice/E5/SHI/01/HA/HA000.ogg"
    hachiman "Alright, let's get started."
    hachiman "(I knew we'd be in groups for cleaning, but who would have thought I'd be alone with Totsuka...!)"
    show totsuka vhappy with dissolve
    voice "audio/voice/E5/SHI/01/SI/SI000.ogg"
    totsuka "Sure!"
    voice "audio/voice/E5/SHI/01/HA/HA001.ogg"
    hachiman "I'll take the mop and handle things over here, you cover that side."
    voice "audio/voice/E5/SHI/01/SI/SI001.ogg"
    totsuka "Roger~!"
    window auto hide dissolve
    hide totsuka with dissolve
    $renpy.pause(delay=0.5, hard=False)
    play sound "audio/sfx/SE01/SE01_24.ogg"
    $renpy.pause(delay=0.25, hard=False)
    show totsuka home far_right vhappy at left with dissolve:
        xoffset 365 yoffset 80
    voice "audio/voice/E5/SHI/01/SI/SI002.ogg"
    totsuka "Ehehe..."
    voice "audio/voice/E5/SHI/01/HA/HA002.ogg"
    hachiman "W-What's up?"
    "Totsuka turned and showed me a happy smile. That angle-like smile almost made me slip and fall on my ass."
    show totsuka happy with dissolve
    voice "audio/voice/E5/SHI/01/SI/SI003.ogg"
    totsuka "I just remembered the field trip we went on."
    voice "audio/voice/E5/SHI/01/HA/HA003.ogg"
    hachiman "The field trip?"
    hachiman "(If I'm being honest, I have nothing but bitter memories from it.)"
    voice "audio/voice/E5/SHI/01/SI/SI004.ogg"
    totsuka "What's wrong, Hachiman?"
    voice "audio/voice/E5/SHI/01/HA/HA004.ogg"
    hachiman "Ah, um... it's nothing."
    voice "audio/voice/E5/SHI/01/SI/SI005.ogg"
    totsuka "The bath here is so big. I bet it feels really good, too."
    voice "audio/voice/E5/SHI/01/HA/HA005.ogg"
    hachiman "Yeah, it does look pretty promising."
    show totsuka blush with dissolve
    voice "audio/voice/E5/SHI/01/SI/SI006.ogg"
    totsuka "I thought we could maybe get in together this time around."
    window auto hide dissolve
    stop voice
    hide totsuka with dissolve
    $renpy.pause(delay=0.5, hard=False)
    play sound "audio/sfx/SE01/SE01_24.ogg"
    $renpy.pause(delay=0.25, hard=False)
    window auto show dissolve
    hachiman "(Holy...! He's being s-s-so assertive! Are you really okay with that, Totsuka?!)"
    show totsuka home far_center happy at right with dissolve:
        xoffset -325 yoffset 75
    voice "audio/voice/E5/SHI/01/SI/SI007.ogg"
    totsuka "You know, we really don't get to do it during summer break or on the field trip."
    voice "audio/voice/E5/SHI/01/HA/HA006.ogg"
    hachiman "T-That's true..."
    show totsuka vhappy with dissolve
    voice "audio/voice/E5/SHI/01/SI/SI008.ogg"
    totsuka "......"
    voice "audio/voice/E5/SHI/01/HA/HA007.ogg"
    hachiman "......"
    show totsuka surprised with dissolve
    voice "audio/voice/E5/SHI/01/SI/SI009.ogg"
    totsuka "Ah, but..."
    voice "audio/voice/E5/SHI/01/HA/HA008.ogg"
    hachiman "Hm?"
    show totsuka pout with dissolve
    voice "audio/voice/E5/SHI/01/SI/SI010.ogg"
    totsuka "...It's nothing. Hiratsuka-sensei and the others are probably already drinking, huh..."
    voice "audio/voice/E5/SHI/01/HA/HA009.ogg"
    hachiman "I bet they are..."
    voice "audio/voice/E5/SHI/01/SI/SI011.ogg"
    totsuka "I just thought because you're so popular, you'll be surrounded by them, you know."
    voice "audio/voice/E5/SHI/01/HA/HA010.ogg"
    hachiman "......"
    window auto hide dissolve
    stop voice
    hide totsuka with dissolve
    $renpy.pause(delay=0.5, hard=False)
    play sound "audio/sfx/SE01/SE01_24.ogg"
    $renpy.pause(delay=0.25, hard=False)
    window auto show dissolve
    "Totsuka's words brought me back to reality in one fell swoop."
    hachiman "(Those guys, at night - drinking! I have a really bad feeling about this...)"
    voice "audio/voice/E5/SHI/01/HA/HA011.ogg"
    hachiman "I'm not really popular, though. I'll make sure I don't get captured."
    show totsuka home mid_center vhappy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/SHI/01/SI/SI012.ogg"
    totsuka "Ahaha, you do that."
    hachiman "(The elder Yukinoshita sister will be a real pain in the ass... Hiratsuka-sensei will probably be frolicking around, too.)"
    hachiman "(Worring her students like this... She acts more like a kid sometimes...)"
    show totsuka happy with dissolve
    voice "audio/voice/E5/SHI/01/SI/SI013.ogg"
    totsuka "You look like you're having fun, Hachiman."
    voice "audio/voice/E5/SHI/01/HA/HA012.ogg"
    hachiman "Oh, me? No, not really."
    hachiman "(Probably.)"
    window auto hide dissolve
    stop music fadeout 0.5
    jump E5_HAR_03

label E5_SHI_02:
    scene slopesA with dissolve:
        zoom 3.2 yoffset -2350 xcenter 0.23
    $renpy.pause(delay=1.0, hard=True)
    stop ambient fadeout 0.5
    stop music fadeout 0.5
    play sound "audio/sfx/SE01/SE01_47.ogg"
    show hiratsuka heavy_coat near_left at center:
        zoom 2.0 xoffset 935 yoffset 160 alpha 0
        parallel:
            easein 0.5 xoffset 435
        parallel:
            linear 0.5 alpha 1.0
    $renpy.pause(delay=1.0, hard=True)
    hide hiratsuka
    show hiratsuka heavy_coat near_center at center:
        zoom 2.0 xoffset 60 yoffset 160 alpha 1.0
    with dissolve
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E5/SHI/02/SZ/SZ000.ogg"
    mystery "Well, if it isn't Hikigaya. What are you doing here?"
    window auto hide dissolve
    stop voice
    $renpy.pause(delay=0.5, hard=True)
    scene slopesA
    hide hiratsuka
    show hiratsuka heavy_coat mid_center surprised at center:
        xoffset 10 yoffset 75
    with dissolve
    $renpy.pause(delay=0.25, hard=True)
    play music "audio/bgm/BGM26.ogg"
    window auto show dissolve
    voice "audio/voice/E5/SHI/02/HA/HA000.ogg"
    hachiman "Ah, Sensei."
    "Sliding coolly (as expected) up to me was Hiratsuka-sensei."
    hachiman "(Why are you always so cool?)"
    show hiratsuka happy with dissolve
    voice "audio/voice/E5/SHI/02/SZ/SZ001.ogg"
    hiratsuka "What's the matter? You don't get to go skiing often, so why don't you enjoy it?"
    voice "audio/voice/E5/SHI/02/HA/HA001.ogg"
    hachiman "Well, I can't actally ski, so..."
    "\"Even if I could, I probably won't do it.\" - or so I nearly blurted out."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E5/SHI/02/SZ/SZ002.ogg"
    hiratsuka "Well, it can't be helped then. How about I teach you... and your little sister~?"
    voice "audio/voice/E5/SHI/02/HA/HA002.ogg"
    hachiman "You really don't need to..."
    hide hiratsuka with dissolve
    show hiratsuka heavy_coat mid_center vhappy at left:
        xoffset 110 yoffset 75
    show komachi heavy_coat mid_left happy at right:
        xoffset -270 yoffset 75
    with dissolve
    hachiman "(Hey! You called over Komachi and she came over in high spirits, so I can't back out now!)"
    show komachi vhappy with dissolve
    voice "audio/voice/E5/SHI/02/KO/KO000.ogg"
    komachi "Waa~. You won't mind?"
    show hiratsuka happy with dissolve
    voice "audio/voice/E5/SHI/02/SZ/SZ003.ogg"
    hiratsuka "Yeah, of course I won't. That's what we're here for."
    voice "audio/voice/E5/SHI/02/KO/KO001.ogg"
    komachi "Yay~! Yes, please! Let's do it~."
    show hiratsuka angry with dissolve
    voice "audio/voice/E5/SHI/02/SZ/SZ004.ogg"
    hiratsuka "However! Just so you know, I can be a bit harsh, so be ready for that."
    voice "audio/voice/E5/SHI/02/HA/HA003.ogg"
    hachiman "Say what?"
    show komachi angry with dissolve
    voice "audio/voice/E5/SHI/02/KO/KO002.ogg"
    komachi "Ready and waiting! Please let me call you Master!"
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E5/SHI/02/SZ/SZ005.ogg"
    hiratsuka "That's the spirit! Let's get started right away!"
    hachiman "(Guh, Komachi you're being so extra... you're on fire! I wish I could've just stayed under the \"people bad at skiing\" classification...)"
    show hiratsuka happy with dissolve
    voice "audio/voice/E5/SHI/02/SZ/SZ006.ogg"
    hiratsuka "Let's start with the basics. First, spread your legs in a ハ-shape."
    voice "audio/voice/E5/SHI/02/HA/HA004.ogg"
    hachiman "Like this?"
    show komachi heavy_coat mid_center surprised at right with dissolve:
        xoffset -200 yoffset 75
    voice "audio/voice/E5/SHI/02/KO/KO003.ogg"
    komachi "Like this?"
    voice "audio/voice/E5/SHI/02/SZ/SZ007.ogg"
    hiratsuka "Yeah, that's good enough. Now, try shifting your weight from left to right."
    show komachi pout with dissolve
    voice "audio/voice/E5/SHI/02/KO/KO004.ogg"
    komachi "Like... this?"
    voice "audio/voice/E5/SHI/02/HA/HA005.ogg"
    hachiman "L-Like that?"
    hachiman "(Oh, I really feel like I'm gliding.)"
    show hiratsuka angry with dissolve
    voice "audio/voice/E5/SHI/02/SZ/SZ008.ogg"
    hiratsuka "Now keep doing it until your body gets used to it."
    hachiman "(You're surprisingly gentle...)"
    "Going left and right as I was told, I ended up thinking it was kind of fun."
    show hiratsuka happy with dissolve
    voice "audio/voice/E5/SHI/02/SZ/SZ009.ogg"
    hiratsuka "Yes, this is pretty much it. Those were the basics, and both of you got the hang of it, it seems. Especially your sister, she seems to have a knack for it."
    show komachi mid_left vhappy with dissolve:
        xoffset -270 yoffset 75
    voice "audio/voice/E5/SHI/02/KO/KO005.ogg"
    komachi "Yeah, I think Komachi's got down! Onii-chan, I'll go slide around a bit over there!"
    voice "audio/voice/E5/SHI/02/HA/HA006.ogg"
    hachiman "Sure, don't go too far."
    hide komachi
    hide hiratsuka
    with dissolve
    hachiman "(Komachi, you seem pretty excited... and you're a really fast learner, unlike me.)"
    show hiratsuka heavy_coat mid_center happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/SHI/02/SZ/SZ010.ogg"
    hiratsuka "What's up? You can go ski now."
    voice "audio/voice/E5/SHI/02/HA/HA007.ogg"
    hachiman "Sure, but... I don't see the point of skiing beyond this point."
    "To tell the truth, it's not that I don't enjoy skiing at all, but this is a bad habit of mine and I tend to get stubborn."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E5/SHI/02/SZ/SZ011.ogg"
    hiratsuka "Well, this is just part of your life experience. Next time I see you, I hope you'll have grown into a man to be reckoned with!"
    voice "audio/voice/E5/SHI/02/HA/HA008.ogg"
    hachiman "Right..."
    hachiman "(That's like a line straight out of a shounen...)"
    image hiratsuka_ski_flat = Flatten("hiratsuka heavy_coat mid_left vhappy")
    hide hiratsuka
    show hiratsuka_ski_flat at center:
        xoffset 140 yoffset 80
        on hide:
            parallel:
                linear 0.5 xoffset 0
            parallel:
                linear 0.5 alpha 0
    with dissolve
    voice "audio/voice/E5/SHI/02/SZ/SZ012.ogg"
    hiratsuka "Well then, until next we meet!"
    hide hiratsuka_ski_flat
    play sound "audio/sfx/SE01/SE01_45.ogg"
    $renpy.pause(delay=0.5, hard=True)
    hachiman "(And there she goes... Must've flipped her switch or something.)"
    "After watching Hiratsuka-sensei gallantly glide away in silence, I started sliding around."
    hachiman "(They look like they're having so much fun...)"
    "To be honest, I'm still learning how to enjoy this, but having Hiratsuka-sensei teach me was pretty fun at least."
    hachiman "(I'm pretty tired... I had myself a pretty good workout if I do say so myself. Well, time to go back to the lodge...)"
    play sound "<to 1.0>audio/sfx/SE01/SE01_47.ogg" fadeout 0.5
    show komachi heavy_coat mid_left happy flat at center:
        xoffset 500 yoffset 75 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.5 xoffset 5
    $renpy.pause(delay=0.5, hard=True)
    stop sound fadeout 0.5
    hide komachi
    show komachi heavy_coat mid_center happy at center:
        xoffset -75 yoffset 75
    with dissolve
    voice "audio/voice/E5/SHI/02/KO/KO006.ogg"
    komachi "Huh? Onii-chan, are you going back already?"
    voice "audio/voice/E5/SHI/02/HA/HA009.ogg"
    hachiman "Yeah, that's right. About time I head back and get some sleep."
    show komachi unimpressed with dissolve
    voice "audio/voice/E5/SHI/02/KO/KO007.ogg"
    komachi "Man... talk about pathetic~."
    show komachi happy with dissolve
    voice "audio/voice/E5/SHI/02/KO/KO008.ogg"
    komachi "Well, Komachi will ski around a bit more, okay~?"
    voice "audio/voice/E5/SHI/02/HA/HA010.ogg"
    hachiman "Sure. Have fun. Don't get hurt, alright?"
    show komachi heavy_coat mid_left happy flat with dissolve:
        xoffset 5 alpha 1.0
        on hide:
            parallel:
                linear 0.5 alpha 0
            parallel:
                easeout 0.5 xoffset -400
    hide komachi
    play sound "audio/sfx/SE01/SE01_45.ogg"
    $renpy.pause(delay=0.5, hard=True)
    hachiman "(Let's head back, then...)"
    window auto hide dissolve
    stop sound fadeout 0.5
    stop music fadeout 0.5
    scene lodgeB
    show skyB
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "Honestly, I did pretty good for myself. By the time I got back to the lodge, the sun had gone down. The rest should be coming back soon."
    hide skyB with dissolve
    voice "audio/voice/E5/SHI/02/HA/HA011.ogg"
    hachiman "Man, I'm tired... Huh!?"
    window auto hide dissolve
    scene lodgeB with dissolve:
        zoom 1.9 xoffset -1680 yoffset -450
    play music "audio/bgm/BGM20.ogg"
    window auto show dissolve
    "There, on the sofa, lie Hiratsuka-sensei, sprawled out like she'd been through the wringer."
    voice "audio/voice/E5/SHI/02/HA/HA012.ogg"
    hachiman "Wh-what happened?"
    show hiratsuka heavy_coat_sunset mid_center sad at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/SHI/02/SZ/SZ013.ogg"
    hiratsuka "Ah, Hikigaya... It's been a while since I used up all my power."
    "When she noticed me, Hiratsuka-sensei slowly gave me a thumb up. Her expression like one of a satisfied boxer who had burnt to white ash."
    voice "audio/voice/E5/SHI/02/HA/HA013.ogg"
    hachiman "It would be best if you changed and got some rest before you catch a cold, won't it?"
    show hiratsuka happy with dissolve
    voice "audio/voice/E5/SHI/02/SZ/SZ014.ogg"
    hiratsuka "Fuu... I'll do just that in a bit."
    hachiman "(She's actually the one who wanted to ski the most, wasn't she...?)"
    "A naive thought like \"Why the hell would she do that?\" arose in my mind, but if there was ever a \"Hiratsuka-sensei thing to do\", this was it. I felt like it was charming in its own way."
    window auto hide dissolve
    stop music fadeout 0.5
    jump E5_CMM_03

label E5_SHI_03:
    scene lodgeC:
        zoom 2.0 yoffset -350
    show meguri home mid vhappy at left:
        xoffset 145 yoffset 75
    show haruno sweater mid_left sly at right:
        xoffset -110 yoffset 75
    show hiratsuka home mid_center unimpressed at center:
        xoffset 40 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/SHI/03/HR/HR000.ogg"
    haruno "So, Shizuka-chan, have you still not found a boyfriend~?"
    show hiratsuka angry with dissolve
    voice "audio/voice/E5/SHI/03/SZ/SZ000.ogg"
    hiratsuka "None of your business."
    "Haruno-san and Hiratsuka-sensei are chatting away with glasses in hand. Sipping her oolong tea, Meguri-senpai was acting as a refreshment amongst them, listening to their conversation with a "
    "smile on her face."
    show haruno angry with dissolve
    voice "audio/voice/E5/SHI/03/HR/HR001.ogg"
    haruno "Men these days haev no taste. You're so cute, Shizuka-chan~."
    show hiratsuka mid_left with dissolve:
        xoffset 110 yoffset 80
    voice "audio/voice/E5/SHI/03/SZ/SZ001.ogg"
    hiratsuka "Well, I'm tired from skiing, so I guess I'll retire for now. Young people should enjoy company among themselves."
    show haruno vhappy with dissolve
    voice "audio/voice/E5/SHI/03/HR/HR002.ogg"
    haruno "Ah, you're sulking~."
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    scene lodge2A with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "Getting some distance from Haruno-san and sensei, I headed straight to the outdoor bath."
    hachiman "(Totsuka wasn't in the living room, so I wonder where he went... Mybe he's in the bath? We promised we'd go in together, didn't we!?)"
    show totsuka home near_center surprised at center with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E5/SHI/03/SI/SI000.ogg"
    totsuka "Hachiman!"
    voice "audio/voice/E5/SHI/03/HA/HA000.ogg"
    hachiman "To-Totsuka. Did you just..."
    show totsuka sad with dissolve
    play music "audio/bgm/BGM46.ogg"
    voice "audio/voice/E5/SHI/03/SI/SI001.ogg"
    totsuka "Sorry. You didn't come for a while, so I went in."
    hachiman "(Are you... serious...)"
    voice "audio/voice/E5/SHI/03/HA/HA001.ogg"
    hachiman "...I see."
    show totsuka vhappy with dissolve
    voice "audio/voice/E5/SHI/03/SI/SI002.ogg"
    totsuka "The bath was so good! You should take your time and enjoy it!"
    voice "audio/voice/E5/SHI/03/HA/HA002.ogg"
    hachiman "Y-Yeah..."
    hide totsuka with dissolve
    hachiman "(This was the only thing I was looking forward to on this camp... Damn...)"
    window auto hide dissolve
    play sound ["<silence 1.0>", "audio/sfx/SE04/SE04_08.ogg"]
    scene hotspringBGB with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    voice "audio/voice/E5/SHI/03/HY/HY000.ogg"
    hayama "Ah, Hikigaya."
    hachiman "(Bathing... with Hayama...)"
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_31.ogg"
    show hachimanBatha with dissolve
    $renpy.pause(delay=1.0, hard=True)
    window auto show dissolve
    voice "audio/voice/E5/SHI/03/HA/HA003.ogg"
    hachiman "......"
    hachiman "(Why is it him I have to take a bath with and not Totsuka...)"
    voice "audio/voice/E5/SHI/03/HY/HY001.ogg"
    hayama "Were you trying to get away from Haruno-san and the others?"
    voice "audio/voice/E5/SHI/03/HA/HA004.ogg"
    hachiman "I guess. You are, too, I'm guessing."
    voice "audio/voice/E5/SHI/03/HY/HY002.ogg"
    hayama "Yeah. I didn't want to get invovlved in that unnecessarily."
    voice "audio/voice/E5/SHI/03/HA/HA005.ogg"
    hachiman "Same."
    hide hachimanBatha with dissolve
    hachiman "(Wait, I passed by Totsuka on the way here, which means... he got to bathe with Totsuka! U-Unforgivable!)"
    voice "audio/voice/E5/SHI/03/HY/HY003.ogg"
    hayama "Hehe."
    voice "audio/voice/E5/SHI/03/HA/HA006.ogg"
    hachiman "What's so funny?"
    show hachimanBatha with dissolve
    voice "audio/voice/E5/SHI/03/HY/HY004.ogg"
    hayama "I just thought you hide your true feelings. You seem to be very popular with older women."
    voice "audio/voice/E5/SHI/03/HA/HA007.ogg"
    hachiman "I'm really not."
    voice "audio/voice/E5/SHI/03/HY/HY005.ogg"
    hayama "Bt you are. If you're talking to them, they get pretty excited, don't they?"
    voice "audio/voice/E5/SHI/03/HA/HA008.ogg"
    hachiman "What?"
    voice "audio/voice/E5/SHI/03/HY/HY006.ogg"
    hayama "Well, better get out now."
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    play sound "audio/sfx/SE01/SE01_30.ogg"
    hide hachimanBatha with dissolve
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    "Hayama quickly got out of the bath, never losing that fresh expression."
    voice "audio/voice/E5/SHI/03/EB/EB000.ogg"
    mystery "Fufufu...."
    play music "audio/bgm/BGM45.ogg"
    voice "audio/voice/E5/SHI/03/HA/HA009.ogg"
    hachiman "Uwa!?"
    hachiman "(I-Is that Ebina-san?)"
    voice "audio/voice/E5/SHI/03/EB/EB001.ogg"
    ebina "I was expecting a good TotsuHachi scene, but got an unexpectedly excellent HayaHachi one instead...!"
    play sound "audio/sfx/SE01/SE01_36.ogg"
    "That last sound she made was obcoiusly her going underwater."
    voice "audio/voice/E5/SHI/03/HA/HA010.ogg"
    hachiman "H-Hey, are you alright?"
    "No matter how many times I called for her, she didn't respond."
    voice "audio/voice/E5/SHI/03/HA/HA011.ogg"
    hachiman "E-Ebina-san?"
    hachiman "(Was she listening to the whole thing and got a little too excited?)"
    "In the end, I couldn't relax, so I ended up getting out of the bath and going over to the women's bath in a hurry to seek help."
    window auto hide dissolve
    stop music fadeout 0.5
    call loading_screen(duration="short") from _call_loading_screen_31
    jump E5_SHI_04

label E5_SHI_04:
    scene lodgeroomC with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    hachiman "(I can't fall asleep for some reason...)"
    "It was already pretty late, but I wasn't sleepy at all. However, I didn't feel like going to the living room and getiing involved with the drunks."
    hachiman "(So much for that... Guess I'll go for a walk.)"
    window auto hide dissolve
    scene lodge2A with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    voice "audio/voice/E5/SHI/04/HA/HA000.ogg"
    hachiman "Hm?"
    show hiratsuka coat near_center surprised at center with dissolve:
        xoffset 30 yoffset 75
    play music "audio/bgm/BGM26.ogg"
    voice "audio/voice/E5/SHI/04/SZ/SZ000.ogg"
    hiratsuka "Ah, it's you, Hikigaya. Where are you going in the middle of the night?"
    voice "audio/voice/E5/SHI/04/HA/HA001.ogg"
    hachiman "Ah, sensei... I just couldn't sleep is all."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ001.ogg"
    hiratsuka "Then I've got just the thing for you. Why don't you come with me for a bit?"
    voice "audio/voice/E5/SHI/04/HA/HA002.ogg"
    hachiman "Did you want to have ramen by any chance?"
    show hiratsuka happy with dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ002.ogg"
    hiratsuka "Fu... You've got some good intuition on ya."
    hachiman "(I'm getting better at reading patterns her patterns, which makes me both sad and happy.)"
    voice "audio/voice/E5/SHI/04/HA/HA003.ogg"
    hachiman "You had a drink earlier, so you shouldn't drive drunk."
    show hiratsuka near_left vhappy with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E5/SHI/04/SZ/SZ003.ogg"
    hiratsuka "That was just oolong tea. I didn't have a single drop of alcohol just so I can do this!"
    hachiman "(Really? Not a single drop? You sound pretty pretty proud of that for some reason...)"
    voice "audio/voice/E5/SHI/04/HA/HA004.ogg"
    hachiman "Right..."
    window auto hide dissolve
    stop voice
    scene ramenShop with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    "She brought me to a famous local ramen restaurant. Every time I go out with her, I'm always amazed at the depth of her ramen knowledge"
    hachiman "(This place is amazing... how did you even know about it? As expected of sensei...)"
    window auto hide dissolve
    scene ramenShop:
        zoom 2.0 xalign .5 ypos -425
    show hiratsuka home mid_center vhappy at center:
        xoffset 40 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ004.ogg"
    hiratsuka "Pretty good, right?"
    voice "audio/voice/E5/SHI/04/HA/HA005.ogg"
    hachiman "Yeah, the noodles and the soup were made for each other. How did you find this place."
    hide hiratsuka
    $url = ["hiratsuka home mid_center happy", "hiratsuka home mid_center sad"]
    $multiImagePara = [40, 75, 0, 0, 2.0]
    call multiImage() from _call_multiImage_83
    voice "audio/voice/E5/SHI/04/SZ/SZ005.ogg"
    hiratsuka "It's a hobby of mine. It's sad to say, but you're the only person who is even remotely as interested in this as I am."
    call finishmultiImage from _call_finishmultiImage_87
    show hiratsuka home mid_center sad at center:
        xoffset 40 yoffset 75
    "As we talked, we sipped our noodles side to side. The ramen warmed us up nicely."
    voice "audio/voice/E5/SHI/04/HA/HA006.ogg"
    hachiman "At any rate, I think you're overlooking her..."
    show hiratsuka unimpressed with dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ006.ogg"
    hiratsuka "Haruno isn't the type of person to hang out at a ramen place for dinner. When I told her about my passion, she was exasperated."
    voice "audio/voice/E5/SHI/04/HA/HA007.ogg"
    hachiman "I can see that happening..."
    show hiratsuka angry with dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ007.ogg"
    hiratsuka "The only thing she cares about right now is herself. She doesn't care who she's drinking with as long as it entertains her."
    voice "audio/voice/E5/SHI/04/SZ/SZ008.ogg"
    hiratsuka "She has yet to find someone she's really interested in."
    "As she made this assertion, Hiratsuka-sensei's expression and tone of voice showed a hint of loneliness. This  was supposed to be a casual conversation, so it caught me off guard and I stopped eating."
    hiratsuka "(So sensei was worried about Haruno-san in her own way...)"
    voice "audio/voice/E5/SHI/04/HA/HA008.ogg"
    hachiman "I don't know if she ever will. Find someone to measure up to her that is."
    show hiratsuka happy with dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ009.ogg"
    hiratsuka "Who knows? It all depends on her."
    voice "audio/voice/E5/SHI/04/HA/HA009.ogg"
    hachiman "Well, I suppose that's true..."
    "As sensei said this with a chuckle, she cut the topic short. I agreed we should leave it at that."
    show hiratsuka unimpressed with dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ010.ogg"
    hiratsuka "Honestly, those sisters should be more straightforward with each other."
    voice "audio/voice/E5/SHI/04/HA/HA010.ogg"
    hachiman "If the could really do that, they probably wouldn't be like this, would they?"
    show hiratsuka angry with dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ011.ogg"
    hiratsuka "No need to be so pessimistic. That was just an idealistic perspective. Would you be willing to intervene for Yukinoshita's sake in the first place?"
    voice "audio/voice/E5/SHI/04/HA/HA011.ogg"
    hachiman "......"
    "I couldn't reply. It's not like I haven't thought about it, whether I intend to do it or not aside. Rather, everytime I think about it, it gets harder to reach an answer."
    voice "audio/voice/E5/SHI/04/SZ/SZ012.ogg"
    hiratsuka "Anyway, this isn't enough for me... I need more liquor. Hey, can I get some--"
    voice "audio/voice/E5/SHI/04/HA/HA012.ogg"
    hachiman "You shouldn't. You have to drive back lodge."
    show hiratsuka frown with dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ013.ogg"
    hiratsuka "Ah, yeah... there was that. I'll hold back for now."
    hachiman "(What do you mean \"hold back for now\"? That carelessness of hers...)"
    voice "audio/voice/E5/SHI/04/HA/HA013.ogg"
    hachiman "It sounds heartless, but isn't this an issue between sisters? Yukinoshita wouldn't like it if I just butted in."
    show hiratsuka angry with dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ014.ogg"
    hiratsuka "Her feeling aside, how do you feel about it?"
    voice "audio/voice/E5/SHI/04/HA/HA014.ogg"
    hachiman "I feel exactly as I said, her feelings aside."
    "After I said that, I was a little surprised I didn't want to hurt Yukinoshita. I didn't want to step into her situation."
    show hiratsuka happy with dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ015.ogg"
    hiratsuka "I see... so that's your answer."
    "As if she can see through me, Hiratsuka-sensei just smiled gently. Her expression seemed to be a bit sad and showing mixed feelings."
    voice "audio/voice/E5/SHI/04/HA/HA015.ogg"
    hachiman "Well... that's where I'm at right now."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ016.ogg"
    hiratsuka "Well, that's fine for now."
    "Right now, I was just wondering what kind of emotion was hiding behind that complicated expression."
    window auto hide dissolve
    scene ramenShop
    show hiratsuka coat mid_center vhappy at center:
        xoffset 40 yoffset 75
    with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ017.ogg"
    hiratsuka "For a local ramen shop, this place is really good!"
    voice "audio/voice/E5/SHI/04/HA/HA016.ogg"
    hachiman "True. I'm thoroughly satisfied."
    show hiratsuka happy with dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ018.ogg"
    hiratsuka "Well, better get going, then."
    voice "audio/voice/E5/SHI/04/HA/HA017.ogg"
    hachiman "Sure."
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    scene skyC with Fade(0.5, 0.5, 0.5)
    play ambient "audio/sfx/SE06/SE06_06L.ogg"
    window auto show dissolve
    "Even though we were in a rental car, Hiratsuka-sensei's driving was always pleasant. I couldn't help but start falling asleep."
    "As we were headed back, I savoured the lingering taste of the ramen, thinking I would be able to get some sleep now for sure."
    $renpy.pause(delay=0.5,hard=True)
    stop ambient
    play sound "audio/sfx/SE06/SE06_07.ogg"
    "The car suddenly started losing speed before coming to complete stop shortly after."
    voice "audio/voice/E5/SHI/04/SZ/SZ019.ogg"
    hiratsuka "Huh?"
    voice "audio/voice/E5/SHI/04/HA/HA018.ogg"
    hachiman "Hm?"
    play sound "audio/sfx/SE06/SE06_08.ogg"
    voice "audio/voice/E5/SHI/04/SZ/SZ020.ogg"
    hiratsuka "......"
    voice "audio/voice/E5/SHI/04/HA/HA019.ogg"
    hachiman "What's going on?"
    stop sound
    play music "audio/bgm/BGM21.ogg"
    voice "audio/voice/E5/SHI/04/SZ/SZ021.ogg"
    hiratsuka "Yep... looks like the engine's stalled."
    voice "audio/voice/E5/SHI/04/HA/HA020.ogg"
    hachiman "Really?"
    voice "audio/voice/E5/SHI/04/SZ/SZ022.ogg"
    hiratsuka "Seriously, in a place like this... yeah, we're screwed."
    voice "audio/voice/E5/SHI/04/HA/HA021.ogg"
    hachiman "A-are we really?"
    play sound "audio/sfx/SE06/SE06_08.ogg"
    hachiman "(It's snowing as far as the eye can see...)"
    "We were on a snow covered road in the middle of nowhere. I don't think getting rescued is an option at this point."
    stop sound
    voice "audio/voice/E5/SHI/04/SZ/SZ023.ogg"
    hiratsuka "No other way. I'll have to fix this myself somehow."
    play sound "audio/sfx/SE06/SE06_10.ogg"
    "Saying that, Hiratsuka-sensei dashingly exited the car and began cluttering about under the hood."
    stop sound
    hachiman "(I'd better go and help her...)"
    "It didn't sit right with me to let a woman work alone in this cold weather. I jumped outisde."
    window auto hide dissolve
    scene skyC
    show hiratsuka coat_night near_center surprised at center:
        xoffset 30 yoffset 75
    with Fade(0.5, 0.5, 0.5)
    play sound "audio/sfx/SE06/SE06_10.ogg"
    $renpy.pause(delay=1.0,hard=True)
    play sound "audio/sfx/SE06/SE06_11.ogg"
    $renpy.pause(delay=0.5,hard=True)
    stop sound
    window auto show dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ024.ogg"
    hiratsuka "What's the matter, Hikigaya? You should wait inside."
    voice "audio/voice/E5/SHI/04/HA/HA022.ogg"
    hachiman "I can't really do that now, can I? I'll help you."
    show hiratsuka blush with dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ025.ogg"
    hiratsuka "I-I see. Thank you. Even though I dragged you all the way here..."
    voice "audio/voice/E5/SHI/04/HA/HA023.ogg"
    hachiman "Well, I don't know much about cars, but if there's anything I can do to help, let me know."
    show hiratsuka happy with dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ026.ogg"
    hiratsuka "That's very kind of you... It's surprising."
    voice "audio/voice/E5/SHI/04/HA/HA024.ogg"
    hachiman "Now's not the time to be talking about that. We should focus on fixing this."
    show hiratsuka blush with dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ027.ogg"
    hiratsuka "Y-Yes, you're right. We should..."
    hachiman "(This is somehow really embarrassing! Focus on repairing, focus, repairing...)"
    window auto hide dissolve
    scene skyC
    show hiratsuka coat_night near_left pout at center:
        xoffset 250 yoffset 75
    with Fade(0.5, 0.5, 0.5)
    play sound "audio/sfx/SE01/SE01_87.ogg"
    window auto show dissolve
    "After that, we struggled together to get this car working, but it showed no sign of doing so. In all seriousness, we might actually be stranded."
    stop sound
    voice "audio/voice/E5/SHI/04/SZ/SZ028.ogg"
    hiratsuka "Yeah... it seems we're done for."
    voice "audio/voice/E5/SHI/04/HA/HA025.ogg"
    hachiman "It certainly... seems that way..."
    show hiratsuka near_center angry with dissolve:
        xoffset 30 yoffset 75
    voice "audio/voice/E5/SHI/04/SZ/SZ029.ogg"
    hiratsuka "No other way. We'll spend the night in the car. If the temperature rises, it might work. If not, we'll call for help."
    voice "audio/voice/E5/SHI/04/HA/HA026.ogg"
    hachiman "Huh?"
    show hiratsuka happy with dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ030.ogg"
    hiratsuka "Fortunately, there's a spare blanket in the trunk. We won't freeze to death at least."
    hachiman "(That might be true, but that's not the issue here...)"
    "I don't know how sensei felt about spending the night together in a closed space, but it was pretty troubling for me."
    window auto hide dissolve
    stop music fadeout 1.0
    scene hiratsukaHachimanCar
    with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ031.ogg"
    hiratsuka "......"
    voice "audio/voice/E5/SHI/04/HA/HA027.ogg"
    hachiman "......"
    hachiman "(What am I supposed to do here...)"
    "Hiratsuka-sensei didn't expect there to be only one blanket and... neither did I. We were huddled in the car, so close we're practically glued together."
    "There was the cold of course, but... there was another sort of discomfort in the air, that's for sure."
    voice "audio/voice/E5/SHI/04/SZ/SZ032.ogg"
    hiratsuka "Hikigaya, don't go to sleep. You'll die if you do."
    voice "audio/voice/E5/SHI/04/HA/HA028.ogg"
    hachiman "You just had to try and say that, didn't you?"
    voice "audio/voice/E5/SHI/04/SZ/SZ033.ogg"
    hiratsuka "Uh... Well, nevermind that. I'm getting a craving for something sweet."
    window auto hide dissolve
    stop voice
    image hiratsukaHachimanCarDup = "images/BG/EV33a.jpg"
    show hiratsukaHachimanCarDup at top with dissolve:
        zoom 1.5 xoffset 30 yoffset -30
    window auto show dissolve
    voice "audio/voice/E5/SHI/04/HA/HA029.ogg"
    hachiman "Like chocolate? Sorry to say, I don't have any..."
    play music "audio/bgm/BGM18.ogg"
    voice "audio/voice/E5/SHI/04/SZ/SZ034.ogg"
    hiratsuka "Speaking of chocolate, it reminds me of the Valentine's Day event..."
    voice "audio/voice/E5/SHI/04/HA/HA030.ogg"
    hachiman "What, is your life flashing before your eyes or something?"
    voice "audio/voice/E5/SHI/04/SZ/SZ035.ogg"
    hiratsuka "Sorry, but I'm not dying that easily."
    voice "audio/voice/E5/SHI/04/HA/HA031.ogg"
    hachiman "Me neither."
    "I try to hide my embarrassment by making jokes and light-hearted remarks, but my heart was still racing. I don't know about you, sensei, but at least for me, this situation is too stimulating."
    voice "audio/voice/E5/SHI/04/SZ/SZ036.ogg"
    hiratsuka "This ski camp was fun..."
    voice "audio/voice/E5/SHI/04/HA/HA032.ogg"
    hachiman "There's still one day left to go, so let's not use past tense."
    voice "audio/voice/E5/SHI/04/SZ/SZ037.ogg"
    hiratsuka "Haha, I guess you're right. Are you having fun, Hikigaya?"
    voice "audio/voice/E5/SHI/04/HA/HA033.ogg"
    hachiman "......"
    hide hiratsukaHachimanCarDup with dissolve
    hachiman "(You're getting straight to the point and it's throwing me off...)"
    voice "audio/voice/E5/SHI/04/HA/HA034.ogg"
    hachiman "It's not all bad. I'm seriously tired, though..."
    voice "audio/voice/E5/SHI/04/SZ/SZ038.ogg"
    hiratsuka "That's because you're so serious about everyting."
    voice "audio/voice/E5/SHI/04/HA/HA035.ogg"
    hachiman "I guess so."
    voice "audio/voice/E5/SHI/04/SZ/SZ039.ogg"
    hiratsuka "Being serious about bothering or hurting others... Well, it's probably the only thing you can do right now."
    voice "audio/voice/E5/SHI/04/HA/HA036.ogg"
    hachiman "......"
    "Honestly, I couldn't say anything to that. There are some things you can't reach without having to destroy first. However, destroying said thing won't necessarily yield the result you seek."
    "That said, is it really courageous to simply destroy what you have right now, completely in the dark, just because you hate deception? I felt like I was having a Zen dialogue in my mind."
    window auto hide dissolve
    show hiratsukaHachimanCarDup at top with dissolve:
        zoom 1.5 xoffset 30 yoffset -30
    window auto show dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ040.ogg"
    hiratsuka "Hah..."
    "As if she could see through my inner confilct, Hiratsuka-sensei smiled at me."
    voice "audio/voice/E5/SHI/04/SZ/SZ041.ogg"
    hiratsuka "Still, you don't have to be so afraid of causing trouble for or hurting others."
    voice "audio/voice/E5/SHI/04/HA/HA037.ogg"
    hachiman "I think that's a bit reckless."
    voice "audio/voice/E5/SHI/04/SZ/SZ042.ogg"
    hiratsuka "Reckless, huh? But if you can't do anything out of fear of what might happen, you might regret it more than just breaking what you have."
    hide hiratsukaHachimanCarDup with dissolve
    "She said this in an unusually serious tone. It's a little different from her usual admonishing one. It had this strange... earnestness that I'd never heard from her before."
    voice "audio/voice/E5/SHI/04/HA/HA038.ogg"
    hachiman "Are you speaking from personal experience?"
    voice "audio/voice/E5/SHI/04/SZ/SZ043.ogg"
    hiratsuka "It's just a common parable. However..."
    hachiman "(...However?)"
    "As she was about to say something, sensei suddenly smiled. Perhaps it was because we were so close that I couldn't miss the obvious sadness in her expression."
    voice "audio/voice/E5/SHI/04/SZ/SZ044.ogg"
    hiratsuka "Well, after all, there isn't a single person who hasn't thought \"I wish I had done this instead.\". That's all I'm saying."
    voice "audio/voice/E5/SHI/04/HA/HA039.ogg"
    hachiman "What was your youth like, sensei?"
    "\"You're capable. I know because I've been there, too.\" - Her words came to mind."
    "What did sensei destroy, who did she hurt, and what did she gain? What did she find in the end?"
    "If there is something to be found after that destruction, will I be able to find it? And just who will be standing before me when I do?"
    window auto hide dissolve
    show hiratsukaHachimanCarDup at top with dissolve:
        zoom 1.5 xoffset 30 yoffset -30
    window auto show dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ045.ogg"
    hiratsuka "Don't go and poke fun at me now. Let's see... it was so long ago, I forgot."
    voice "audio/voice/E5/SHI/04/HA/HA040.ogg"
    hachiman "I want to hear... what your days in highschool were like."
    "I genuinly wanted to hear about it. Maybe it was because I'd been remembering and reflecting upon every single word that sensei had said more than I thought I would."
    voice "audio/voice/E5/SHI/04/SZ/SZ046.ogg"
    hiratsuka "My highschool years are nothing worth mentioning. We all have times like that in our lives."
    voice "audio/voice/E5/SHI/04/SZ/SZ047.ogg"
    hiratsuka "It's just that sometimes when I look at you and the others, I think of things that could've happened, but didn't."
    hachiman "(\"Things that could've happened\"? Like what?)"
    "Those words stuck with me in a strange way."
    voice "audio/voice/E5/SHI/04/SZ/SZ048.ogg"
    hiratsuka "Honestly, it's embarrassing how long ago it was."
    voice "audio/voice/E5/SHI/04/HA/HA041.ogg"
    hachiman "Is that... so?"
    window auto hide dissolve
    stop voice
    hide hiratsukaHachimanCarDup with dissolve
    window auto show dissolve
    "Saying that, Hiratsuka-sensei smiled softly as if she had lost her strength and leaned against me. At that moment, I couldn't help but feel the urge to snuggle up to her."
    "It must be because of the cold. That's what I told myself. But somehow, despite myself, my heart was beating faster and faster."
    hachiman "(She's always watching over me... but then who's watching over you, sensei?)"
    "If I could, maybe I... I don't know why I feel this way. I don't understand why, but now... I feel like I want to know her better than I did before."
    voice "audio/voice/E5/SHI/04/HA/HA042.ogg"
    hachiman "I want to hear about your story sometime..."
    voice "audio/voice/E5/SHI/04/SZ/SZ049.ogg"
    hiratsuka "........."
    "She must have been very tired, because she seemed to be completely asleep. Her sleeping face was more innocent, cute and beautiful than I'd ever seen her before."
    hachiman "(Well... I don't mind this, either...)"
    "As I listened to sensei's calm breathing, I felt as if the strand of tension I had was broken and my eyelids suddenly grew heavy."
    window auto hide dissolve
    stop music fadeout 0.5
    scene black with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ050.ogg"
    hiratsuka "Hikigaya. Wake up, Hikigaya!"
    voice "audio/voice/E5/SHI/04/HA/HA043.ogg"
    hachiman "........."
    voice "audio/voice/E5/SHI/04/SZ/SZ051.ogg"
    hiratsuka "The car came back to normal apparently. Rejoice, we can finally go back!"
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    scene lodgeoutA with dissolve
    play sound "audio/sfx/SE06/SE06_09.ogg"
    window auto show dissolve
    "An odd 10 minutes later and we were back at the lodge. Fortunately, it looked like the place was quiet and no one had woken up yet."
    show hiratsuka home mid_center angry at center with dissolve:
        xoffset 40 yoffset 75
    stop sound
    play sound "audio/sfx/SE06/SE06_11.ogg"
    $renpy.pause(delay=0.5,hard=True)
    voice "audio/voice/E5/SHI/04/SZ/SZ052.ogg"
    hiratsuka "Okay, we'll go in sneaky-like. Don't let anyone spot you."
    voice "audio/voice/E5/SHI/04/HA/HA044.ogg"
    hachiman "Um, right..."
    hachiman "(Any way you look at it, a teacher and a student coming back together in the moring after being out all night doesn't exactly look good... We were just eating ramen and got stranded, though...)"
    window auto hide dissolve
    scene lodge2A
    show hiratsuka coat near_left happy at center:
        xoffset 250 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ053.ogg"
    hiratsuka "Alright, looks like the coast is clear."
    voice "audio/voice/E5/SHI/04/HA/HA045.ogg"
    hachiman "Roger."
    hachiman "(I'm a ninja, a shinobi... making sound is a foreign concept to me... real quiet now...)"
    voice "audio/voice/E5/SHI/04/IR/IR000.ogg"
    iroha "Ah, it's senpai... and Hiratsuka-sensei. Good morning~"
    show hiratsuka surprised with dissolve
    play music "audio/bgm/BGM45.ogg"
    voice "audio/voice/E5/SHI/04/MI/MIX000.ogg"
    hachiandhira "......!"
    "And so, just as I let my guard down, Isshiki popped up from behind me. It seems that when you're startled to death, you can't even speak."
    hachiman "(The one person I didn't want finding us had found us...)"
    voice "audio/voice/E5/SHI/04/IR/IR001.ogg"
    iroha "...Say, what are you two doing together in the morning? And wearing coats while trying to sneak around... you're so suspicious."
    voice "audio/voice/E5/SHI/04/HA/HA047.ogg"
    hachiman "No, this isn't anything suspicious at all..."
    window auto hide dissolve
    scene lodgeA
    show yukino home mid_center happy at left:
        xoffset 25 yoffset 75
    show iroha home mid_center unimpressed at right:
        xoffset -315 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/SHI/04/YK/YK000.ogg"
    yukino "Good morning."
    hachiman "(Damn! She's someone I want finding me like this even less!)"
    voice "audio/voice/E5/SHI/04/HA/HA048.ogg"
    hachiman "M-Morning..."
    show yukino angry with dissolve
    voice "audio/voice/E5/SHI/04/YK/YK001.ogg"
    yukino "I see you two have been going somewhere together, but where would that be?"
    voice "audio/voice/E5/SHI/04/HA/HA049.ogg"
    hachiman "This really isn't what it looks like..."
    show iroha happy with dissolve
    voice "audio/voice/E5/SHI/04/IR/IR002.ogg"
    iroha "You're not denying it, so... you guys obviously went somewhere together."
    voice "audio/voice/E5/SHI/04/HA/HA050.ogg"
    hachiman "......"
    show yukino sly with dissolve
    voice "audio/voice/E5/SHI/04/YK/YK002.ogg"
    yukino "Don't worry, I won't question you too much. I'm sure I'll regret it if I heard it all."
    voice "audio/voice/E5/SHI/04/HA/HA051.ogg"
    hachiman "No, wait a minute. You've got it all wrong."
    show iroha surprised with dissolve
    voice "audio/voice/E5/SHI/04/IR/IR003.ogg"
    iroha "Huh? You two together... all night?"
    voice "audio/voice/E5/SHI/04/HA/HA052.ogg"
    hachiman "......"
    hachiman "(Don't give me that look of genuine surprised! Nothing happened!)"
    window auto hide dissolve
    scene lodge2A
    show hiratsuka coat near_center happy at center:
        xoffset 20 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/SHI/04/SZ/SZ055.ogg"
    hiratsuka "Yeah, we went together to get ramen, but our car broke down on the way back. We were in deep waters, but we managed to come back this morning."
    "Sensei immediately explained the situation in a calm and concise manner. There must be a big difference in persuasiveness between what I say and what sensei says. I was relieved, but not for long."
    voice "audio/voice/E5/SHI/04/IR/IR004.ogg"
    iroha "You were in deep...? All night!?"
    voice "audio/voice/E5/SHI/04/YK/YK003.ogg"
    yukino "I'm not fond of the idea that a student and a teacher go out for dinner together and stay up all night."
    show hiratsuka coat near_left vhappy at center with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E5/SHI/04/SZ/SZ056.ogg"
    hiratsuka "Ah, don't be such a stickler. We couldn't resist the allure of local ramen. Right, Hikigaya?"
    voice "audio/voice/E5/SHI/04/HA/HA053.ogg"
    hachiman "T-That's right..."
    "Sensei threw me the lowkey glance of a rascal. I commited to memory the embarrassing feeling I got from seemingly sharing a secret with sensei."
    window auto hide dissolve
    stop music fadeout 0.5
    jump E5_CMM_04

label E5_SHI_05:
    hachiman "(I couldn't even finish my breakfast, did I really catch a cold?)"
    voice "audio/voice/E5/SHI/05/HA/HA000.ogg"
    hachiman "I can clean at least. Today... It looks like I'll be taking the bath again today..."
    voice "audio/voice/E5/SHI/05/YI/YI000.ogg"
    yui "No, Hikki, you don't have to! I'll have Tobechi help out with that."
    voice "audio/voice/E5/SHI/05/HA/HA001.ogg"
    hachiman "That's just be a bother, though..."
    show yukino angry with dissolve
    voice "audio/voice/E5/SHI/05/YK/YK000.ogg"
    yukino "No, what will be a bother is you slugging around in that state. You might get someone else sick."
    show iroha mid_center unimpressed with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E5/SHI/05/IR/IR000.ogg"
    iroha "This is a weird time to be stubborn like this, senpai..."
    voice "audio/voice/E5/SHI/05/YI/YI001.ogg"
    yui "She's right, Hikki. You better go to bed and keep warm. Do you want me to walk you?"
    show yukino sly with dissolve
    voice "audio/voice/E5/SHI/05/YK/YK001.ogg"
    yukino "Yuigahama-san. It's just a cold. You don't have to baby him."
    voice "audio/voice/E5/SHI/05/IR/IR001.ogg"
    iroha "True... if you can stay out all night, you can go to your room by yourself."
    hachiman "(She's being pretty harsh...)"
    show yui mid_left surprised with dissolve:
        xoffset -145 yoffset 75
    voice "audio/voice/E5/SHI/05/YI/YI002.ogg"
    yui "Huh!? He stayed out all night!?"
    show yukino unimpressed with dissolve
    voice "audio/voice/E5/SHI/05/YK/YK002.ogg"
    yukino "Yuigahama-san, there are things that you are better off not knowing."
    show yui pout with dissolve
    voice "audio/voice/E5/SHI/05/YI/YI003.ogg"
    yui "But I wanna know~..."
    voice "audio/voice/E5/SHI/05/HA/HA002.ogg"
    hachiman "It was just a misunderstanding."
    show yukino angry with dissolve
    voice "audio/voice/E5/SHI/05/YK/YK003.ogg"
    yukino "Enough out of you. Now go and get some sleep."
    voice "audio/voice/E5/SHI/05/HA/HA003.ogg"
    hachiman "......"
    "Feeling unreasonabley treated by them, I staggered back to my room and laid down."
    window auto hide dissolve
    stop music fadeout 0.5
    jump E5_SHI_06

label E5_SHI_06:
    scene lodgeroomA with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    "With a foggy head, I closed my eyes in bed. Perhaps I was more seriously ill than I thought, and found myself breathing more heavily than usual."
    hachiman "(I caught a cold on a school trip and now I have to lay down and sleep... way to go me. I can get some rest...)"
    "I muttered to myself in my mind, but alone in a room, I actually did start to feel lonely."
    window auto hide dissolve
    play sound "audio/sfx/SE04/SE04_13.ogg"
    $renpy.pause(delay=0.75,hard=True)
    window auto show dissolve
    voice "audio/voice/E5/SHI/06/SZ/SZ000.ogg"
    hiratsuka "Hikigaya, are you in there? It's me... Hiratsuka."
    voice "audio/voice/E5/SHI/06/HA/HA000.ogg"
    hachiman "Yeah... come in."
    "Hiratsuka-sensei's voice make me kind of nervous. I wonder if she was worried about me."
    voice "audio/voice/E5/SHI/06/SZ/SZ001.ogg"
    hiratsuka "I'm coming in, then."
    window auto hide dissolve
    $renpy.pause(delay=0.25,hard=True)
    play sound "audio/sfx/SE04/SE04_05.ogg"
    $renpy.pause(delay=0.75,hard=True)
    stop sound
    show hiratsuka home mid_center sad at center with dissolve:
        xoffset 40 yoffset 75
    play music "audio/bgm/BGM18.ogg"
    window auto show dissolve
    voice "audio/voice/E5/SHI/06/SZ/SZ002.ogg"
    hiratsuka "Are you okay?"
    window auto hide dissolve
    hide hiratsuka with dissolve
    play sound "audio/sfx/SE04/SE04_06.ogg"
    $renpy.pause(delay=0.5,hard=True)
    stop sound
    show lodgeroomADup at truecenter:
        zoom 2.0 xalign 0 ypos 740
    show hiratsuka home near_center sad at center:
        xoffset 30 yoffset 75
    with dissolve
    window auto show dissolve
    "Hiratsuka-sensei said with a concerned look on her face, and gently put her hand on my forehead. Her soft, cool touch felt good."
    hachiman "(Wasn't there a myth about people with cool hands having warm hearts?)"
    show hiratsuka angry with dissolve
    voice "audio/voice/E5/SHI/06/SZ/SZ003.ogg"
    hiratsuka "Hmm... you're not too hot, but you still have a fever."
    hachiman "(Being so nice to me... it's not fair...)"
    show hiratsuka near_left happy with dissolve:
        xoffset 200 yoffset 80
    voice "audio/voice/E5/SHI/06/SZ/SZ004.ogg"
    hiratsuka "Hold on a second, I'll get a wet towel."
    voice "audio/voice/E5/SHI/06/HA/HA001.ogg"
    hachiman "Thanks... for doing this."
    show hiratsuka sad with dissolve
    voice "audio/voice/E5/SHI/06/SZ/SZ005.ogg"
    hiratsuka "Don't sweat it. It's partly my fault, after all."
    "Hiratsuka-sensei looked unusually apologetic. Truthfully, it wasn't her fault at all. I went along with her out of my own volition."
    voice "audio/voice/E5/SHI/06/HA/HA002.ogg"
    hachiman "Are you alright, sensei? You might catch a cold."
    show hiratsuka near_center vhappy with dissolve:
        xoffset 30 yoffset 75
    voice "audio/voice/E5/SHI/06/SZ/SZ006.ogg"
    hiratsuka "Fu... Well, maybe that would be a good way to atone for my sins."
    voice "audio/voice/E5/SHI/06/HA/HA003.ogg"
    hachiman "that's going a bit overboard."
    show hiratsuka sad with dissolve
    voice "audio/voice/E5/SHI/06/SZ/SZ007.ogg"
    hiratsuka "I'm grateful to you. For coming along with me to eat ramen and... for last night. I'm... so sorry to have let you catch a cold."
    voice "audio/voice/E5/SHI/06/HA/HA004.ogg"
    hachiman "......"
    show hiratsuka happy with dissolve
    voice "audio/voice/E5/SHI/06/SZ/SZ008.ogg"
    hiratsuka "So why don't you at least let me take care of you?"
    voice "audio/voice/E5/SHI/06/HA/HA005.ogg"
    hachiman "T-Then... I'll take you up on that."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E5/SHI/06/SZ/SZ009.ogg"
    hiratsuka "Thank you."
    "Sensei's not the kind of person who would say something lke that out of lies or flattery. She always has been diligent with me. Not only as a teacher, but also as a human being."
    "Just when I was drifting off, I thought that maybe that's why I feel so at ease even though I'm in such a bad shape."
    window auto hide dissolve
    stop music fadeout 0.5
    jump E5_CMM_06

label E5_SHI_07:
    scene lodgeroomC with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    voice "audio/voice/E5/SHI/07/HA/HA000.ogg"
    hachiman "Nn... huh?"
    "The ceiling felt unfamiliar to me, but gradually coming to my senses, I remembered my current situation."
    hachiman "(Ah, that's right... I caught a cold. I fell asleep without realizing again...)"
    hachiman "(Looks like I still have a fever...)"
    window auto hide dissolve
    play sound "audio/sfx/SE04/SE04_13.ogg"
    $renpy.pause(delay=0.75,hard=True)
    window auto show dissolve
    hachiman "(Mm? Who's that?)"
    voice "audio/voice/E5/SHI/07/HA/HA001.ogg"
    hachiman "Yes...?"
    voice "audio/voice/E5/SHI/07/SZ/SZ000.ogg"
    hiratsuka "It's me. I'm coming in."
    window auto hide dissolve
    $renpy.pause(delay=0.25,hard=True)
    play sound "audio/sfx/SE04/SE04_05.ogg"
    $renpy.pause(delay=0.75,hard=True)
    stop sound
    show hiratsuka home mid_center happy at center with dissolve:
        xoffset 40 yoffset 75
    play music "audio/bgm/BGM42.ogg"
    window auto show dissolve
    voice "audio/voice/E5/SHI/07/HA/HA002.ogg"
    hachiman "Sensei... What's up?"
    show hiratsuka blush with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ001.ogg"
    hiratsuka "Even though it's a cold, you need to eat. I made porridge, would you like some?"
    voice "audio/voice/E5/SHI/07/HA/HA003.ogg"
    hachiman "Huh?"
    window auto hide dissolve
    image lodgeroomCDup = "images/bg/BG59C.jpg"
    hide hiratsuka with dissolve
    $renpy.pause(delay=0.25,hard=True)
    show lodgeroomCDup at truecenter:
        zoom 2.0 xalign 0 ypos 740
    show hiratsuka home near_center happy at center:
        xoffset 30 yoffset 75
    with dissolve
    window auto show dissolve
    "The porrridge that Hiratsuka-sensei brought to me smelled delicious. To be honest, I don't have much of an appetite, but I can't let her kindness go to waste."
    voice "audio/voice/E5/SHI/07/HA/HA004.ogg"
    hachiman "Can I?"
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ002.ogg"
    hiratsuka "Don't know if you'll like it, though."
    voice "audio/voice/E5/SHI/07/HA/HA005.ogg"
    hachiman "I'll have some, thank you."
    show hiratsuka near_left happy with dissolve:
        xoffset 200 yoffset 80
    "When I tried to take the bowl of porridge that was offered to me, sensei suddenly lifted it up."
    show hiratsuka blush with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ003.ogg"
    hiratsuka "Don't push yourself. I-I'll... feed it to you."
    voice "audio/voice/E5/SHI/07/HA/HA006.ogg"
    hachiman "Huh..."
    show hiratsuka near_center with dissolve:
        xoffset 30 yoffset 75
    voice "audio/voice/E5/SHI/07/SZ/SZ004.ogg"
    hiratsuka "You don't want to?"
    hachiman "(How could I say no...?)"
    voice "audio/voice/E5/SHI/07/HA/HA007.ogg"
    hachiman "I-I do..."
    voice "audio/voice/E5/SHI/07/SZ/SZ005.ogg"
    hiratsuka "I see. Then... Here."
    "An embarrassed Hiratsuka-sensei awkwardly scoops up a spoonful of porridge, blows on it so it's easier to eat, and lifts it up to my mouth."
    "This sweet and sour sitation makes me feel like my fever's about to go up not down."
    hachiman "(L-Look... when you offer it up to me like this...)"
    show hiratsuka sad with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ006.ogg"
    hiratsuka "What's wrong? Are you not going to have any after all?"
    voice "audio/voice/E5/SHI/07/HA/HA008.ogg"
    hachiman "N-No, I will... Here goes."
    "When I timidly opened my mouth, a spoon was gently inserted."
    hachiman "(Wait a minute! I haven't even had Komachi feed me like this...!)"
    voice "audio/voice/E5/SHI/07/HA/HA009.ogg"
    hachiman "It's... delicious."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ007.ogg"
    hiratsuka "That's good to hear. Looks like my cooking skills are up to par."
    voice "audio/voice/E5/SHI/07/HA/HA010.ogg"
    hachiman "Sure are."
    "She said with a considerable amount of pride, and it's kind of cute. And yet she is pretty manly. I suddenly thought about her irregularity."
    hachiman "(She looks like she's having fun... and I somehow feel pretty bad.)"
    show hiratsuka surprised with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ008.ogg"
    hiratsuka "What's wrong?"
    voice "audio/voice/E5/SHI/07/HA/HA011.ogg"
    hachiman "It looks like you're getting in a good mood, so why not join the others downstairs?"
    "Sensei huffed and shook her head."
    show hiratsuka happy with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ009.ogg"
    hiratsuka "Normally, I'd probably do that, but surprisingly, I feel more at home here, doing this."
    voice "audio/voice/E5/SHI/07/HA/HA012.ogg"
    hachiman "...Really?"
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ010.ogg"
    hiratsuka "Here, have one more."
    voice "audio/voice/E5/SHI/07/HA/HA013.ogg"
    hachiman "Ah... thanks."
    show hiratsuka sad with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ011.ogg"
    hiratsuka "As a teacher, I can't feel any piece of mind just leaving you like this..."
    voice "audio/voice/E5/SHI/07/HA/HA014.ogg"
    hachiman "Eh, that bad?"
    voice "audio/voice/E5/SHI/07/SZ/SZ012.ogg"
    hiratsuka "Have you experience first-hand fun you can have with other people, is what I wanted to do, but..."
    hachiman "(Have fun with other people, huh...?)"
    voice "audio/voice/E5/SHI/07/HA/HA015.ogg"
    hachiman "There's no point in forcing anybody."
    "To tell the truth, I'm much relaxed and at ease in this situation, but it's hard to say that when looking at sensei's complicated expression."
    show hiratsuka happy with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ013.ogg"
    hiratsuka "Well, I knew you would say that, but... there are some things you can experience only in the present."
    voice "audio/voice/E5/SHI/07/HA/HA016.ogg"
    hachiman "......"
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ014.ogg"
    hiratsuka "Now, another bite..."
    "Hiratsuka-sensei made a break in our conversation to bring me a spoonful of porridge. As expected, I felt bad and refused."
    voice "audio/voice/E5/SHI/07/HA/HA017.ogg"
    hachiman "Ah, I think I can eat by myself now..."
    show hiratsuka blush with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ015.ogg"
    hiratsuka "Don't say that. Doing this is actually pretty fun."
    voice "audio/voice/E5/SHI/07/HA/HA018.ogg"
    hachiman "I-Is that so? Alrigth then..."
    "Gratefully, I accepted the porridge. I was actually starting to feel better with every spoonful. The human body is a strange thing."
    show hiratsuka happy with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ016.ogg"
    hiratsuka "You've lost the whole day, but I hope there's something about this camp that you'll look back someday and feel a little nostalgic about."
    voice "audio/voice/E5/SHI/07/HA/HA019.ogg"
    hachiman "I'd look back on it and miss it probably because it's something I've lost."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ017.ogg"
    hiratsuka "Well, that sounds like something you'd say, but..."
    show hiratsuka happy with dissolve
    "When I said this, sensei looked somewhat sad. I wondered if there was something she had lost. I wondered if she was looking back on it right now and feeling nostalgic."
    "If that's the case, I want to know about it someday. Maybe the fever's impairing me, but for some reason, I find myself thinking so."
    show hiratsuka blush with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ018.ogg"
    hiratsuka "I... honestly had fun."
    voice "audio/voice/E5/SHI/07/HA/HA020.ogg"
    hachiman "Huh?"
    voice "audio/voice/E5/SHI/07/SZ/SZ019.ogg"
    hiratsuka "Yet, I ended up causing you trouble in the process."
    voice "audio/voice/E5/SHI/07/HA/HA021.ogg"
    hachiman "If you had fun, then it's fine."
    "I wondered what kind of experience sensei wold look back on last night as. I didn't dare venture to find out, though."
    voice "audio/voice/E5/SHI/07/HA/HA022.ogg"
    hachiman "It might become something... to look back fondly on."
    "Maybe I don't want yesterday's event to be \"lost\" after all. Maybe I can't think clearly right now because of the fever, but I'm sure that's true."
    hachiman "(Oh, no... now I've gone and said that...)"
    show hiratsuka surprised with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ020.ogg"
    hiratsuka "......"
    voice "audio/voice/E5/SHI/07/HA/HA023.ogg"
    hachiman "What's wrong...?"
    show hiratsuka blush with dissolve
    voice "audio/voice/E5/SHI/07/SZ/SZ021.ogg"
    hiratsuka "Huh? Ah, n-no... it's nothing."
    "Looking at a, slightly embarrassed, Hiratsuka-sensei, I felt strange, like I was getting a little hot, yet I was completely at ease."
    show hiratsuka near_left blush with dissolve:
        xoffset 200 yoffset 80
    voice "audio/voice/E5/SHI/07/SZ/SZ022.ogg"
    hiratsuka "Anyway, why don't we go out for ramen again when you get better?"
    voice "audio/voice/E5/SHI/07/HA/HA024.ogg"
    hachiman "Ah... I'd like that."
    "Such an innocuous promise was a great relief. Rather than looking back and worring about this and that, maybe that's all we need for now."
    window auto hide dissolve
    stop music fadeout 0.5
    call loading_screen(28) from _call_loading_screen_32
    jump E6_CMM_01
