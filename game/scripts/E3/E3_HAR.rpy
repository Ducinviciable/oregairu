label E3_HAR_01:
    play sound "audio/sfx/SE04/SE04_00.ogg"
    scene black with CropMove(0.5, mode="wipeleft")
    $renpy.pause(delay=0.5, hard=True)
    scene hallwayA with CropMove(0.5, mode="wipeleft")
    window auto show dissolve
    hachiman "(Ahh, right, the toilet...)"
    voice "audio/voice/E3/HAR/01/HY/HY000.ogg"
    mystery "Hikigaya, do you have a moment?"
    show hayama school mid_center pout at center with dissolve:
        xoffset 5 yoffset 75
    hachiman "(To be honest, I don't really want to talk to him right now...)"
    voice "audio/voice/E3/HAR/01/HA/HA000.ogg"
    hachiman "What is it? Is this about the rumors..."
    show hayama relieved with dissolve
    voice "audio/voice/E3/HAR/01/HY/HY001.ogg"
    hayama "No. Well... that too."
    show hayama pout with dissolve
    voice "audio/voice/E3/HAR/01/HY/HY002.ogg"
    hayama "All these rumors must be bothering Yukinoshita. I'm sorry, I should apologize."
    voice "audio/voice/E3/HAR/01/HA/HA001.ogg"
    hachiman "...It's not like it's your fault."
    show hayama happy with dissolve
    voice "audio/voice/E3/HAR/01/HY/HY003.ogg"
    hayama "...That's awfully fair of you."
    voice "audio/voice/E3/HAR/01/HA/HA002.ogg"
    hachiman "I wouldn't call it fair. It's not your fault they've been spreading, and it's a situation that's messing with the both of you."
    voice "audio/voice/E3/HAR/01/HY/HY004.ogg"
    hayama "...That's just like you."
    show hayama pout with dissolve
    voice "audio/voice/E3/HAR/01/HY/HY005.ogg"
    hayama "Although I think Yukinoshita has had it worse than me, so..."
    "That's quite an arrogant way of thinking Hayama..."
    "Well, I don't have the heart to point it out. Besides, his voice is really getting on my nerves."
    voice "audio/voice/E3/HAR/01/HA/HA003.ogg"
    hachiman "Well... I'll let her know... see ya."
    hide hayama with dissolve
    if shrineMeetFlag != "haruno meguri":
        window auto hide dissolve
        stop music fadeout 0.5
        call loading_screen from _call_loading_screen_14
        jump E3_CMM_06
    voice "audio/voice/E3/HAR/01/HY/HY006.ogg"
    hayama "...Hikigaya."
    show hayama school mid_center pout at center with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E3/HAR/01/HA/HA004.ogg"
    hachiman "What? Did you need something else?"
    hachiman "(I was just about to escape as well... *sigh*)"
    show hayama relieved with dissolve
    voice "audio/voice/E3/HAR/01/HY/HY007.ogg"
    hayama "Were you with Haruno the other day?"
    hachiman "(Oh, over winter vacation. Well, I did say I was busy, but it's a little creepy he saw me.)"
    voice "audio/voice/E3/HAR/01/HY/HY008.ogg"
    hayama "Ah... I didn't mean it in a weird way..."
    hachiman "(Well, it definitely sounded weird.)"
    voice "audio/voice/E3/HAR/01/HA/HA005.ogg"
    hachiman "We ran into each other outside of the station, that's all."
    show hayama happy with dissolve
    voice "audio/voice/E3/HAR/01/HY/HY009.ogg"
    hayama "Oh... Well, I thought it was something like that."
    voice "audio/voice/E3/HAR/01/HA/HA006.ogg"
    hachiman "Then why ask?"
    show hayama sad with dissolve
    voice "audio/voice/E3/HAR/01/HY/HY010.ogg"
    hayama "I was just a little worried...... especially after New Years."
    voice "audio/voice/E3/HAR/01/HA/HA007.ogg"
    hachiman "............"
    show hayama pout with dissolve
    voice "audio/voice/E3/HAR/01/HY/HY011.ogg"
    hayama "If you're not up for it, I'd get out while you still can."
    voice "audio/voice/E3/HAR/01/HA/HA008.ogg"
    hachiman "Ahh... if I could, I would have done so already."
    hachiman "(What's with this guy? I can't figure out if he likes me or not. Maybe he likes Haruno? Either way, it isn't funny...)"
    voice "audio/voice/E3/HAR/01/HY/HY012.ogg"
    hayama "I've already told you. She chases and chases after whoever she's interested in, but that's it. Feelings don't matter to her."
    voice "audio/voice/E3/HAR/01/HA/HA009.ogg"
    hachiman "...I guess."
    hachiman "(I wonder why she wants to mess with me in the first place? Well, I am one of the people involved with her sister.)"
    hachiman "(I wish she'd mess with Hayama instead though, he seems to want the attention.)"
    hachiman "(However, unfortunately for him, that seems to be the exact opposite of what she's interested in. Source: Me.)"
    voice "audio/voice/E3/HAR/01/HY/HY013.ogg"
    hayama "Well, if you're ever feeling down don't hesitate to contact me. I'll do my best to help."
    voice "audio/voice/E3/HAR/01/HY/HY014.ogg"
    hayama "I don't know to what extent I can help, though..."
    voice "audio/voice/E3/HAR/01/HA/HA010.ogg"
    hachiman "I probably won't, but well, uh, thanks for the offer."
    show hayama school mid_right happy at center with dissolve:
        xoffset -25 yoffset 65
    voice "audio/voice/E3/HAR/01/HY/HY015.ogg"
    hayama "...I see. It's a little strange being thanked by you."
    hide hayama with dissolve
    voice "audio/voice/E3/HAR/01/HA/HA011.ogg"
    hachiman "Feel weird to me, too."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    call loading_screen(filename="02_09") from _call_loading_screen_15
    jump E3_HAR_02

label E3_HAR_02:
    scene black with Fade(1.0, 1.0, 1.0)
    play ambient "audio/sfx/SE06/SE06_14L.ogg"
    scene skyB with dissolve
    $renpy.pause(delay=1.5, hard=False)
    window auto show dissolve
    hachiman "(Ahh, I've been so tired lately.... I want to go home and sleep...)"
    play sound ["audio/sfx/SE03/SE03_00L.ogg", "audio/sfx/SE03/SE03_00L.ogg"]
    $renpy.pause(delay=0.5, hard=False)
    stop ambient
    play ambient "audio/sfx/SE06/SE06_15.ogg" noloop
    hachiman "(...Oh? A text?)"
    window auto hide dissolve
    stop sound
    scene sidewalkB with dissolve
    play sound "audio/sfx/SE03/SE03_02.ogg"
    stop ambient
    call mail_function("haruno", "haruno", "", "Yahallo! Where are you?") from _call_mail_function_19
    show black with dissolve:
        alpha 0.3
    show haruno coat_sunset mid_center happy flat at center behind black:
        xoffset -20 yoffset 75
        alpha 0
        parallel:
            linear 1.0 alpha 1.0
    window auto show dissolve
    voice "audio/voice/E3/HAR/02/HR/HR000.ogg"
    haruno "\"Yahallo! Where are you?\""
    call mail_clear from _call_mail_clear_4
    hide black with dissolve
    hide haruno
    show haruno coat_sunset mid_center happy at center:
        xoffset -20 yoffset 75
    voice "audio/voice/E3/HAR/02/HA/HA000.ogg"
    hachiman "............"
    play music "audio/bgm/BGM35.ogg"
    hachiman "(Where to say... Just around...?)"
    show haruno vhappy with dissolve
    voice "audio/voice/E3/HAR/02/HR/HR001.ogg"
    haruno "Hehe, did I surprise you?"
    hachiman "(Not really, you practically forced me to give you my number.)"
    voice "audio/voice/E3/HAR/02/HA/HA001.ogg"
    hachiman "So, what are you doing ambushing me on my way home?"
    show haruno coat_sunset mid_left happy at center with dissolve:
        xoffset -20 yoffset 75
    voice "audio/voice/E3/HAR/02/HR/HR002.ogg"
    haruno "Hmm, your big sis had some free time and I was feeling a little bored..."
    voice "audio/voice/E3/HAR/02/HA/HA002.ogg"
    hachiman "Well, I probably have more free time than you...but, isn't it boring hanging out with me?"
    show haruno vhappy with dissolve
    voice "audio/voice/E3/HAR/02/HR/HR003.ogg"
    haruno "Of course not... you know, I really do enjoy spending time with you."
    voice "audio/voice/E3/HAR/02/HA/HA003.ogg"
    hachiman "............"
    hachiman "(I'm honestly pretty scared of you when you're like that.)"
    window auto hide dissolve
    scene cakeShopB with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    hachiman "(And so I was abducted toward the station.)"
    window auto hide dissolve
    scene cakeShopB with dissolve:
        zoom 2.0 xalign 0 ypos -505
    window auto show dissolve
    voice "audio/voice/E3/HAR/02/HR/HR004.ogg"
    haruno "So, how are you doing?"
    "Haruno-san has an awfully innocent smile, but I can't help but feel it's a little ominous."
    voice "audio/voice/E3/HAR/02/HA/HA004.ogg"
    hachiman "Why do you ask?"
    voice "audio/voice/E3/HAR/02/HR/HR005.ogg"
    haruno "It's a new semester after all. A lot is happening, don't you think?"
    hachiman "(I feel like I recognize that expression... but I'm afraid to know why. Then again, I don't think I'm supposed to know...)"
    voice "audio/voice/E3/HAR/02/HA/HA005.ogg"
    hachiman "Well, thanks to someone or other there are rumors that Yukinoshita and Hayama are dating."
    show haruno sweater near_center vhappy at center with dissolve:
        xoffset -20 yoffset 75
    voice "audio/voice/E3/HAR/02/HR/HR006.ogg"
    haruno "Heh. I'm not sure what to make of that... Well, I don't think they're like that."
    hachiman "(Is she trying to trick me? Agh, it's a trap.)"
    show haruno sly with dissolve
    voice "audio/voice/E3/HAR/02/HR/HR007.ogg"
    haruno "Oh, hey, how's Hayato taking it?"
    voice "audio/voice/E3/HAR/02/HA/HA006.ogg"
    hachiman "He said he'll do something. Not that he's done anything yet."
    show haruno annoyed with dissolve
    voice "audio/voice/E3/HAR/02/HR/HR008.ogg"
    haruno "Hmm."
    show haruno happy with dissolve
    voice "audio/voice/E3/HAR/02/HR/HR009.ogg"
    haruno "...And Yukino?"
    voice "audio/voice/E3/HAR/02/HA/HA007.ogg"
    hachiman "I've dealt with this kind of situation before, but I don't think anything can be done... or so she said."
    voice "audio/voice/E3/HAR/02/HR/HR010.ogg"
    haruno "So that's what she said? Hmm, she used to make an awful lot of excuses, though."
    voice "audio/voice/E3/HAR/02/HA/HA008.ogg"
    hachiman "Didn't you help her back then?"
    show haruno sly with dissolve
    voice "audio/voice/E3/HAR/02/HR/HR011.ogg"
    haruno "Why should I have to help? It's Yukino's problem after all."
    "As a cold smile flickers across her face, I had the sudden realisation that I was probably being tested. But, what is she trying...?"
    hachiman "(This girl is bad news.)"
    window auto hide dissolve
    stop music fadeout 0.5
    call loading_screen(15) from _call_loading_screen_23
    jump E3_CMM_06


label E3_HAR_03:
    show yui school_sunset mid_center vhappy at center:
        xoffset -430 yoffset 75
    show meguri school_sunset mid happy at center:
        xoffset 430 yoffset 75
    with dissolve
    $renpy.pause(delay=1.0, hard=True)
    play music "audio/bgm/BGM07.ogg"
    voice "audio/voice/E3/HAR/03/MG/MG000.ogg"
    meguri "Have you all decided on your career path?"
    "While the battle between Yukinoshita and Haruno-san was raging, Meguri-senpai turned and peered at us with with a robotic turn. You could almost hear a bleep."
    show yui pout with dissolve
    voice "audio/voice/E3/HAR/03/YI/YI000.ogg"
    yui "Ah, well... Not yet. I wanted to think about it a bit more."
    show meguri vhappy with dissolve
    voice "audio/voice/E3/HAR/03/MG/MG001.ogg"
    meguri "I can give you a consultation anytime, Yuigahama-san!"
    voice "audio/voice/E3/HAR/03/YI/YI001.ogg"
    yui "Th-Then, when I gather my thoughts, I'll give it a shot!"
    voice "audio/voice/E3/HAR/03/MG/MG002.ogg"
    meguri "Yep! You can count on me!"
    show meguri happy with dissolve
    voice "audio/voice/E3/HAR/03/MG/MG003.ogg"
    meguri "So, what about you, Hikigaya-kun?"
    voice "audio/voice/E3/HAR/03/HA/HA000.ogg"
    hachiman "Uhm, I... think I know."
    hachiman "(It's not that I find it hard to talk to Meguri-senpai, in fact I find her quite comforting, but I can't help but feel self-conscious.)"
    show meguri frown with dissolve
    voice "audio/voice/E3/HAR/03/MG/MG004.ogg"
    meguri "*pout* I thought I could give you advice like a senpai would."
    voice "audio/voice/E3/HAR/03/HA/HA001.ogg"
    hachiman "I'm sorry."
    hide yui
    hide meguri
    with dissolve
    voice "audio/voice/E3/HAR/03/IR/IR000.ogg"
    iroha "Good job, everyone! All alumni, over here, please!"
    show haruno sweater_sunset far_left vhappy at center:
        xoffset 225 yoffset 75
    show yukino school_sunset far_center annoyed at center:
        xoffset -285 yoffset 75
    with dissolve
    voice "audio/voice/E3/HAR/03/HR/HR000.ogg"
    haruno "Ah, preparations are all done~"
    voice "audio/voice/E3/HAR/03/YK/YK000.ogg"
    yukino "That's right. Shouldn't you hurry over there?"
    show yukino stare with dissolve
    voice "audio/voice/E3/HAR/03/YK/YK001.ogg"
    yukino "Now then, we're done here."
    stop voice
    hide yukino with dissolve
    hide haruno with dissolve
    show yui school_sunset mid_center pout at center:
        xoffset -430 yoffset 75
    show meguri school_sunset mid happy at center:
        xoffset 430 yoffset 75
    with dissolve
    hide yui
    $url = ["yui school_sunset mid_center pout", "yui school_sunset mid_right pout"]
    $multiImagePara = [-430, 75, -515, 75, 2.1]
    call multiImage(0, False) from _call_multiImage_21
    voice "audio/voice/E3/HAR/03/YI/YI002.ogg"
    yui "Ah, Yukino! Wait up! S-see you later."
    call finishmultiImage from _call_finishmultiImage_22
    hide yui
    with dissolve
    show meguri sad with dissolve
    voice "audio/voice/E3/HAR/03/MG/MG005.ogg"
    meguri "Aw~ You guys should've tried it out."
    show haruno sweater_sunset mid_center happy at center with dissolve:
        xoffset -395 yoffset 75
    show meguri happy with dissolve
    voice "audio/voice/E3/HAR/03/MG/MG006.ogg"
    meguri "Alright, Haru-san, let's go shall we?"
    voice "audio/voice/E3/HAR/03/HR/HR001.ogg"
    haruno "Yep. Let's go."
    show meguri vhappy with dissolve
    voice "audio/voice/E3/HAR/03/MG/MG007.ogg"
    meguri "See you later, Hikigaya-kun."
    voice "audio/voice/E3/HAR/03/HA/HA002.ogg"
    hachiman "Ah, see ya."
    hide meguri
    hide haruno
    with dissolve
    stop music fadeout 2.0
    hachiman "(Aah, I'm finally set free...)"
    show haruno sweater_sunset near_center happy at center with dissolve:
        xoffset -260 yoffset 75
    voice "audio/voice/E3/HAR/03/HR/HR002.ogg"
    haruno "When this is over, come hang out with big sis."
    voice "audio/voice/E3/HAR/03/HA/HA003.ogg"
    hachiman "............"
    voice "audio/voice/E3/HAR/03/HR/HR003.ogg"
    haruno "I have something I want to talk to you about."
    hide haruno with dissolve
    play music "audio/bgm/BGM46.ogg"
    menu E3_HAR_03_menu:
        with dissolve
        hachiman "At any rate, that doesn't sound like it'll do me any good."
        "I'm curious":
            $totsukaTalkFlag = "meguri"
            "I'd be lying if I said I wasn't curious at all though."
            "I don't know whether it was due to the elusive nature of Haruno Yukinoshita or her irresistible charm that has the tendency to captivate people."
            hachiman "(Irresistable charm? Yeah, no shot... or so I'd like to think. After all, I know how scary she can be.)"
            jump E3_CMM_07
        "Don't bother":
            $totsukaTalkFlag = "haruno"
            hachiman "(I'll just go back and pretend I didn't hear anything.)"
            hachiman "(I should have consulted with Meguri-senpai now that I had the chance. I probably wouldn't have gotten anything out of it, but it would've healed me for sure.)"
            window auto hide dissolve
            stop music fadeout 1.0
            jump E3_CMM_07

label E3_HAR_04:
    scene cakeShopC with Fade(1.5,1.5,0.5)
    play music "audio/bgm/BGM35.ogg"
    window auto show dissolve
    hachiman "(...I know it's probably a bad idea, but I can't refuse. Besides, I'm too lazy to go home right away. I'll wait for her as she asks.)"
    show haruno coat mid_center vhappy at center with dissolve:
        xoffset -20 yoffset 75
    voice "audio/voice/E3/HAR/04/HR/HR000.ogg"
    haruno "Sorry I kept you waiting, my future brother-in-law!"
    voice "audio/voice/E3/HAR/04/HA/HA000.ogg"
    hachiman "...I'm not your brother-in-law."
    window auto hide dissolve
    hide haruno with dissolve
    scene cakeShopC with dissolve:
        zoom 2.0 xalign 0 ypos -505
    window auto show dissolve
    "Ignoring my futile protests, Haruno made her way over and slipped into the seat opposite me. I followed each of her movements a little too closely, unable to help myself. I wasn't really sure what else to think, other than \"she's beautiful\"."
    show haruno sweater near_center annoyed at center with dissolve:
        xoffset -20 yoffset 75
    voice "audio/voice/E3/HAR/04/HR/HR001.ogg"
    haruno "Huhhh, I suppose so."
    voice "audio/voice/E3/HAR/04/HA/HA001.ogg"
    hachiman "Hmm? What?"
    show haruno vhappy with dissolve
    voice "audio/voice/E3/HAR/04/HR/HR002.ogg"
    haruno "Brother-in-law would be a waste, don't you think?"
    voice "audio/voice/E3/HAR/04/HA/HA002.ogg"
    hachiman "That again? And here I was thinking you actually had something to say."
    show haruno happy with dissolve
    voice "audio/voice/E3/HAR/04/HR/HR003.ogg"
    haruno "Hmm? Oh! About that."
    voice "audio/voice/E3/HAR/04/HR/HR004.ogg"
    haruno "What path did you choose, Hikigaya-kun?"
    voice "audio/voice/E3/HAR/04/HA/HA003.ogg"
    hachiman "Well... I guess I'm going into the humanities."
    show haruno vhappy with dissolve
    voice "audio/voice/E3/HAR/04/HR/HR005.ogg"
    haruno "I see, you're always reading books after all. That's a literary young man for sure."
    voice "audio/voice/E3/HAR/04/HA/HA004.ogg"
    hachiman "Oh, no, that's... well..."
    "It's true that we met outside before whilst I was reading a book, but that was only because it was awkward."
    "It was my special book defence shield! Well, the reason was pretty uncool, so I tried my best not to look away. In response, Haruno-san leant forward across the table and peered at me with a devilish look "
    "upon her face."
    show haruno happy with dissolve
    voice "audio/voice/E3/HAR/04/HR/HR006.ogg"
    haruno "What kind of books do you read?"
    voice "audio/voice/E3/HAR/04/HA/HA005.ogg"
    hachiman "...Pretty much anything. Well, I don't read that many foreign books..."
    show haruno annoyed with dissolve
    voice "audio/voice/E3/HAR/04/HR/HR007.ogg"
    haruno "Hm. Akutagawa or Dazai, then?"
    voice "audio/voice/E3/HAR/04/HA/HA006.ogg"
    hachiman "Ah, I don't really read either of them... I tend to go for more general fiction."
    show haruno happy with dissolve
    voice "audio/voice/E3/HAR/04/HR/HR008.ogg"
    haruno "In that case, I'm not sure literature would work. You might enjoy something like sociology, don't you think?"
    "I wasn't sure what to make of that. Before I knew it she'd already began to give me advice."
    "I didn't have any intention of doing what she says, so it wasn't all that helpful, but still. I should be grateful for her kindness, at the least."
    voice "audio/voice/E3/HAR/04/HA/HA007.ogg"
    hachiman "...Thanks for the advice."
    show haruno vhappy with dissolve
    voice "audio/voice/E3/HAR/04/HR/HR009.ogg"
    haruno "You're welcome."
    "Haruno-san smiles and clears her throat."
    show haruno happy with dissolve
    voice "audio/voice/E3/HAR/04/HR/HR010.ogg"
    haruno "...So, have you heard anything about what Yukino-chan is going to study?"
    hachiman "(Damn, she's moving on to the main subject. I lost the chance to show my gratitude.)"
    voice "audio/voice/E3/HAR/04/HA/HA008.ogg"
    hachiman "No, nothing really. I guess she hasn't decided yet."
    show haruno worried with dissolve
    voice "audio/voice/E3/HAR/04/HR/HR011.ogg"
    haruno "If that's so, why doesn't she come consult big sis about it~?"
    voice "audio/voice/E3/HAR/04/HA/HA009.ogg"
    hachiman "Sometimes, you want to figure things out for yourself... I dunno."
    show haruno happy with dissolve
    voice "audio/voice/E3/HAR/04/HR/HR012.ogg"
    haruno "\"By yourself\"... as Yukino-chan would say."
    voice "audio/voice/E3/HAR/04/HA/HA010.ogg"
    hachiman "I think it's something she has to decide for herself regardless."
    voice "audio/voice/E3/HAR/04/HR/HR013.ogg"
    haruno "Well, if deciding \"by yourself\" is even possible."
    hachiman "(Didn't she say that she went to a local University because her parents wanted her to...?)"
    show haruno annoyed with dissolve
    voice "audio/voice/E3/HAR/04/HR/HR014.ogg"
    haruno "If she doesn't make her own decision here, she'll end up regretting it."
    voice "audio/voice/E3/HAR/04/HA/HA011.ogg"
    hachiman "Is that because you regret it yourself?"
    voice "audio/voice/E3/HAR/04/HR/HR015.ogg"
    haruno "You really do know everything, don't you, Hikigaya-kun?"
    stop music fadeout 2.0
    "It's almost like she's ridiculing my shallowness. Yet, at the same time, there was a worrying sharpness to her voice that makes it difficult to disagree. The pressure oozing from Yukinoshita Haruno's smile"
    "caused my hairs to stand on end."
    voice "audio/voice/E3/HAR/04/HA/HA012.ogg"
    hachiman "............"
    "Haruno-san lowered her eyes at me, her gaze all of a sudden much softer."
    play music "audio/bgm/BGM35.ogg"
    show haruno happy with dissolve
    voice "audio/voice/E3/HAR/04/HR/HR016.ogg"
    haruno "...Just kidding. Don't be so scared Hikigaya-kun! It's too cute."
    hachiman "(Uhm... Can you stop digging around in my head?)"
    voice "audio/voice/E3/HAR/04/HR/HR017.ogg"
    haruno "But, you know... you're the first one who's ever said that to me."
    window auto hide dissolve
    stop voice
    call loading_screen(3) from _call_loading_screen_24
    jump E3_G10_01

label E3_HAR_05:
    scene gatesB with Fade(1.0,1.0,1.0)
    hachiman "(Well, time to go home...)"
    voice "audio/voice/E3/HAR/05/MG/MG000.ogg"
    mystery "Ah, it's Hikigaya-kun."
    voice "audio/voice/E3/HAR/05/HA/HA000.ogg"
    hachiman "Hm?"
    show meguri school_sunset mid happy at center with dissolve:
        xoffset 25 yoffset 75
    play music "audio/bgm/BGM42.ogg"
    voice "audio/voice/E3/HAR/05/HA/HA001.ogg"
    hachiman "Oh, hi... did you finish your consultations?"
    voice "audio/voice/E3/HAR/05/MG/MG001.ogg"
    meguri "It's way too early for that. A lot of people came. I'm just taking a little break."
    voice "audio/voice/E3/HAR/05/HA/HA002.ogg"
    hachiman "I see."
    hachiman "(I'm surprised there's people actually turning up for consultations...)"
    voice "audio/voice/E3/HAR/05/MG/MG002.ogg"
    meguri "There's a whole variety of kids that came for advice. Some still aren't sure what they want to do, others are thinking super far ahead... I wonder what I was like last year."
    voice "audio/voice/E3/HAR/05/HA/HA003.ogg"
    hachiman "You got a recommendation as far as I remember, Shiromeguri-senpai. Although it's a no-brainer if you get one, it'll look like you sat down and actually thought about it."
    show meguri frown with dissolve
    voice "audio/voice/E3/HAR/05/MG/MG003.ogg"
    meguri "That didn't really feel like you were praising me."
    voice "audio/voice/E3/HAR/05/HA/HA004.ogg"
    hachiman "I mean..."
    hide meguri with dissolve
    show meguri school_sunset near angry at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/HAR/05/MG/MG004.ogg"
    meguri "Forget about me! What about you, Hikigaya-kun? Have you really decided which career path you're going down?"
    hachiman "(You're close. Too, too, too, too close all of a sudden...)"
    hachiman "(I can't really say I want to be a \"full-time househusband\"... err...)"
    voice "audio/voice/E3/HAR/05/HA/HA005.ogg"
    hachiman "Yeah..."
    show meguri happy with dissolve
    voice "audio/voice/E3/HAR/05/MG/MG005.ogg"
    meguri "If you're okay with me, I'll give you advice any time!"
    voice "audio/voice/E3/HAR/05/HA/HA006.ogg"
    hachiman "Ah... thank you."
    show meguri vhappy with dissolve
    voice "audio/voice/E3/HAR/05/MG/MG006.ogg"
    meguri "Sure! It's about time I go back now. See you later, Hikigaya-kun!"
    voice "audio/voice/E3/HAR/05/HA/HA007.ogg"
    hachiman "Ah, later."
    hide meguri with dissolve
    hachiman "(The Megurishu effect pervades my somewhat tired mind and body.)"
    hachiman "(With Totsuka and Shiromeguri-senpai, today was a surprisingly good day...)"
    window auto hide dissolve
    stop music fadeout 1.0
    jump E3_G10_01

label E3_HAR_06:
    play sound ["audio/sfx/SE03/SE03_00L.ogg", "audio/sfx/SE03/SE03_00L.ogg"]
    $renpy.pause(delay=0.5, hard=True)
    scene sidewalkB with fade
    window auto show dissolve
    hachiman "(Oh, an e-mail...)"
    stop sound
    play sound "audio/sfx/SE03/SE03_02.ogg"
    hachiman "(................)"
    play music "audio/bgm/BGM44.ogg"
    call mail_function("haruno", "haruno", "", "I'm waiting at the usual cafe, alright~?") from _call_mail_function_20
    show black with dissolve:
        alpha 0.3
    hachiman "(\"I'm waiting at the usual cafe, alright~\"...Huh?)"
    hachiman "(It's not like we \"usually\" go there. And it's not like Haruno-san and I always see each other... What, was she the type of person to think that you're already friends once you've met her once?)"
    voice "audio/voice/E3/HAR/06/HA/HA001.ogg"
    hachiman "*sigh*"
    voice "audio/voice/E3/HAR/06/HA/HA002.ogg"
    hachiman "\"My body hurts and I feel like I'm dying inside so I'll be going home, sorry.\" ...There."
    play sound "audio/sfx/SE03/SE03_02.ogg"
    call mail_function("haruno", "hachiman", "Re:", "My body hurts and I feel like I'm dying inside so I'll be going home, sorry.") from _call_mail_function_21
    $renpy.pause(delay=1.5, hard=False)
    call mail_hide from _call_mail_hide
    hide black with dissolve
    play sound ["audio/sfx/SE03/SE03_00L.ogg", "audio/sfx/SE03/SE03_00L.ogg"]
    hachiman "(She replies so fast! Terrifying!)"
    stop sound
    $renpy.pause(delay=0.5, hard=False)
    call mail_function("haruno", "haruno", "Re2:", "What!? That's dreadful! I'm coming to get you!") from _call_mail_function_22
    show black:
        alpha 0.3
    with dissolve
    hachiman "(\"What!? That's dreadful! I'm coming to get you!\"...There's a compulsion behind the kind words...I can feel it...)"
    hachiman "(................)"
    call mail_clear from _call_mail_clear_5
    hide black with dissolve
    voice "audio/voice/E3/HAR/06/HA/HA004.ogg"
    hachiman "...Yeah, I knew I couldn't get away from this."
    window auto hide dissolve
    stop music fadeout 0.5
    stop voice
    scene cakeShopB with Fade(1.0,0.5,0.5)
    play music "audio/bgm/BGM35.ogg"
    show haruno sweater far_center vhappy at left with dissolve:
        xoffset 355 yoffset 75
    $renpy.pause(delay=0.5, hard=False)
    window auto show dissolve
    voice "audio/voice/E3/HAR/06/HR/HR000.ogg"
    haruno "Wow, you really came~!"
    window auto hide dissolve
    stop voice
    hide haruno with dissolve
    play sound "audio/sfx/SE01/SE01_13.ogg"
    $renpy.pause(delay=0.5, hard=False)
    scene cakeShopB:
        zoom 2.0 xalign 0 ypos -505
    show haruno sweater near_center happy at center:
        xoffset -20 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E3/HAR/06/HA/HA005.ogg"
    hachiman "I heard it's less of a crime to turn yourself in than to be arrested."
    voice "audio/voice/E3/HAR/06/HR/HR001.ogg"
    haruno "Yep, yep. A very auspicious mindset."
    show haruno vhappy with dissolve
    voice "audio/voice/E3/HAR/06/HR/HR002.ogg"
    haruno "But you really do look like you're dying. What did you do?"
    voice "audio/voice/E3/HAR/06/HA/HA006.ogg"
    hachiman "...I ran a marathon."
    show haruno happy with dissolve
    voice "audio/voice/E3/HAR/06/HR/HR003.ogg"
    haruno "The marathon event, huh... Though that's not what I wanted to ask about. You did something, didn't you? About Yukino-chan and Hayato's problem."
    "I have no idea if this person has some connections to a mysterious information network, or if she just has a keen intuition, but Haruno-san talks as if she knows everything there is to know. So much so "
    "in fact that, strangely enough, I think it's useless to try and hide anything from her when she stares at me with those see-through eyes of hers."
    voice "audio/voice/E3/HAR/06/HA/HA007.ogg"
    hachiman "It's not like I did anything significant..."
    window auto hide dissolve
    scene black with fade
    window auto show dissolve
    "And so I told her everything that had transpired."
    "The fact that I recklessly ran alongside Hayama to find out which career course he chose. And how I somehow managed to hear his answer."
    "About me tripping and falling after our conversation and being left behind. And how Hayama won and used that to put an end to the gossip with the speech he gave."
    "I told her the whole story bit by bit."
    window auto hide dissolve
    scene cakeShopB:
        zoom 2.0 xalign 0 ypos -505
    show haruno sweater near_center vhappy at center:
        xoffset -20 yoffset 75
    with Dissolve(1.0)
    window auto show dissolve
    voice "audio/voice/E3/HAR/06/HR/HR004.ogg"
    haruno "Ahaha, so something like that happened. But to think something like that made such a mess of you..."
    show haruno happy with dissolve
    "As she said that, Haruno-san gently touched my still dirty cheek with a wry look on her face that I don't often see."
    voice "audio/voice/E3/HAR/06/HA/HA008.ogg"
    hachiman "............"
    hachiman "(Uh, could you please not suddenly touch people's faces like that, it's making me nervous.)"
    show haruno annoyed with dissolve
    voice "audio/voice/E3/HAR/06/HR/HR005.ogg"
    haruno "You went that far... for whose sake?"
    voice "audio/voice/E3/HAR/06/HA/HA009.ogg"
    hachiman "Nobody. I was just doing my job."
    show haruno happy with dissolve
    voice "audio/voice/E3/HAR/06/HR/HR006.ogg"
    haruno "That's where you say \"for Yukino-chan's sake.\""
    voice "audio/voice/E3/HAR/06/HA/HA010.ogg"
    hachiman "Actually, I can't say that, because it's not like that. We took on a different request this time, and as a result of it, well... that rumor disappeared."
    voice "audio/voice/E3/HAR/06/HA/HA011.ogg"
    hachiman "I didn't do anything for anyone else. So... well... I did it for me. My own self-satisfaction."
    voice "audio/voice/E3/HAR/06/HR/HR007.ogg"
    haruno "So everything you do is for your own sake? You sure do take individualism to a whole new level..."
    hide haruno with dissolve
    show haruno sweater near_center happy at center with dissolve:
        zoom 1.2 xoffset -25 yoffset 315
    voice "audio/voice/E3/HAR/06/HR/HR008.ogg"
    haruno "I like that answer. As expected of the monster of reason. Well done."
    "Haruno-san said, lightly poking my forehead and then moving away."
    voice "audio/voice/E3/HAR/06/HA/HA012.ogg"
    hachiman "............"
    hide haruno with dissolve
    show haruno sweater near_center worried at center with dissolve:
        xoffset -20 yoffset 75
    voice "audio/voice/E3/HAR/06/HR/HR009.ogg"
    haruno "Hah~. Well, with that, things around Yukino have settled down. That's kinda boring~"
    voice "audio/voice/E3/HAR/06/HA/HA013.ogg"
    hachiman "I'm sorry for doing away with your fun..."
    show haruno vhappy with dissolve
    voice "audio/voice/E3/HAR/06/HR/HR010.ogg"
    haruno "Oh, well."
    show haruno happy with dissolve
    voice "audio/voice/E3/HAR/06/HR/HR011.ogg"
    haruno "You were just \"doing your job\", right?"
    voice "audio/voice/E3/HAR/06/HA/HA014.ogg"
    hachiman "............"
    voice "audio/voice/E3/HAR/06/HR/HR012.ogg"
    haruno "Don't look so glum when you're here with such a beautiful young lady."
    voice "audio/voice/E3/HAR/06/HA/HA015.ogg"
    hachiman "Don't just give people noogies. It'll add more pain to my wounds."
    show haruno vhappy with dissolve
    voice "audio/voice/E3/HAR/06/HR/HR013.ogg"
    haruno "It's just a little bit. You really are your own brand of adorable~."
    hachiman "(She-... She's acting like I'm a toy or something... I wonder if this is what Hayama was talking about when he told me about her... Scary.)"
    window auto hide dissolve
    call loading_screen(3) from _call_loading_screen_25
    jump E3_CMM_08
