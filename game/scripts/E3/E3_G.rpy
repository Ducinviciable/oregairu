label E3_G01_01:
    #general loading screen
    #restart music if not playing...
    #play music "audio/bgm/BGM43.ogg"
    scene classroomA with Fade(1.0, 0.5, 1.0)
    voice "audio/voice/E3/G01/01/XE/XE000.ogg"
    sgA "Are they really dating?"
    voice "audio/voice/E3/G01/01/XH/XH000.ogg"
    sgB "If they are, wouldn't they be in shambles right now?"
    voice "audio/voice/E3/G01/01/XJ/XJ000.ogg"
    sgC "Right! I wasn't sure since they get along, but it's looking pretty rough."
    "The gossips continued in the classroom even during break times. Who exactly they're talking about isn't said, but it's definitely about Hayama and Yukinoshita in general."
    "They were absolutely baseless rumours. But the thing is that drama sells. They were gonna beat the dead horse until it wasn't fun anymore."
    "Rigid sounds began to mix in with the whispering gossips. Voices of girls squeaked and they looked toward the source of the sound."
    show yumiko school far_left annoyed at center with dissolve:
        xoffset 405 yoffset 75
    voice "audio/voice/E3/G01/01/YM/YM000.ogg"
    yumiko "..........."
    "There was Miura, legs crossed and angrily tapping her desk with her nails. She was facing towards her friends, but her eyes were glaring sideways at the girls."
    hide yumiko with dissolve
    voice "audio/voice/E3/G01/01/XE/XE001.ogg"
    sgA "G-going to the bathroom for a bit..."
    voice "audio/voice/E3/G01/01/XH/XH001.ogg"
    sgB "Y-yeah..."
    voice "audio/voice/E3/G01/01/XJ/XJ001.ogg"
    sgC "Ah, me too..."
    "As if it had become a bit harder to stay in the classroom, the girls stood up, quickly passed by me, and headed toward the exit."
    voice "audio/voice/E3/G01/01/XE/XE002.ogg"
    sgA "Wasn't she super mad just now? Do you think she heard us?"
    voice "audio/voice/E3/G01/01/XH/XH002.ogg"
    sgB "I dunno, but... I wonder what she makes of it."
    voice "audio/voice/E3/G01/01/XJ/XJ002.ogg"
    sgC "I wanna know, too~"
    #yui route breaks for here
    stop music fadeout 0.5
    play sound "audio/sfx/SE04/SE04_01.ogg"
    play music "audio/bgm/BGM30.ogg"
    show yumiko school far_left unimpressed at center:
        yoffset 75
    show yui school far_right pout at left behind yumiko:
        xoffset 175 yoffset 75
    show ebina school far_left frown at center behind yumiko:
        xoffset 375 yoffset 75
    with dissolve
    voice "audio/voice/E3/G01/01/YI/YI000.ogg"
    yui "Yumiko, it's fine... I was there."
    show yumiko school far_center sad with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E3/G01/01/YM/YM001.ogg"
    yumiko "Hmm... you were?"
    voice "audio/voice/E3/G01/01/YI/YI001.ogg"
    yui "Yeah. We met Yukinon's sister while shopping and both Yukinon and Hayato-kun's families know each other. So it was just a New Year's thing. Yukinon just happened to be there."
    voice "audio/voice/E3/G01/01/YM/YM001.ogg"
    yumiko "That right?"
    voice "audio/voice/E3/G01/01/EB/EB000.ogg"
    ebina "I get it. Someone happened to see that and it ended up becoming a rumour. Both Hayato-kun and Yukinoshita-san stand out so it's easy for people to make assumptions."
    window auto hide dissolve
    stop voice
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE04/SE04_00.ogg"
    scene black with CropMove(0.5, mode="wipeleft")
    window auto show dissolve
    "After I overheard a bit of that conversation, I got off my seat and left the classroom."
    "Just from knowing half the situation, people get into various conversations and it ends up spreading. I just wanted to go outside and get some air."
    window auto hide dissolve
    scene hallwayA with CropMove(0.5, mode="wipeleft")
    window auto show dissolve
    voice "audio/voice/E3/G01/01/HA/HA000.ogg"
    hachiman "............"
    show yui school mid_center pout at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E3/G01/01/YI/YI002.ogg"
    yui "Hikki."
    voice "audio/voice/E3/G01/01/HA/HA001.ogg"
    hachiman "Hm? Yuigahama. What's up?"
    voice "audio/voice/E3/G01/01/YI/YI003.ogg"
    yui "Yeah... I just wanted to talk to you for a bit..."
    voice "audio/voice/E3/G01/01/HA/HA002.ogg"
    hachiman "Yeah, sure."
    show yui school mid_left at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E3/G01/01/YI/YI004.ogg"
    yui "I was surprised. Everone's been caught up in these rumours since coming to school."
    #jump hallway_yuk
    #perhaps new label. Dialogue seems to change here depending on Route.
    #Currently doing dialogue for yukino route.
    #label hallway_yuk:
    voice "audio/voice/E3/G01/01/HA/HA007.ogg"
    hachiman "It looks like that day became a rumour."
    show yui mid_center at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E3/G01/01/YI/YI009.ogg"
    yui "But come on! Haruno-san was there too, and so were we!"
    voice "audio/voice/E3/G01/01/HA/HA008.ogg"
    hachiman "People only see what they want to see. Saying they were on a date sounds like more interesting, so that spread."
    show yui mid_left at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E3/G01/01/YI/YI010.ogg"
    yui "That's true, but... I don't like that kind of thing."
    voice "audio/voice/E3/G01/01/HA/HA009.ogg"
    hachiman "..."
    voice "audio/voice/E3/G01/01/HA/HA010.ogg"
    hachiman "Well rumours are rumours. Obviously untrue."
    show yui sad with dissolve
    voice "audio/voice/E3/G01/01/YI/YI011.ogg"
    yui "I think so too, but..."
    show yui mid_center sad at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E3/G01/01/YI/YI012.ogg"
    yui "But I hate gossip just for the sake of gossip... I hate people saying bad stuff about my friends."
    voice "audio/voice/E3/G01/01/HA/HA011.ogg"
    hachiman "...Well, anyway."
    menu hallway_yui:
        "Do you want to go to the clubroom after school?": #yukino
            voice "audio/voice/E3/G01/01/HA/HA012.ogg"
            hachiman "Do you want to go to the clubroom after school? Either way we can't do anything until then."
            stop music fadeout 0.5
            show yui mid_left happy at center with dissolve:
                xoffset 10 yoffset 75
            voice "audio/voice/E3/G01/01/YI/YI013.ogg"
            yui "Yeah!"
            window auto hide dissolve
            stop voice
            $renpy.pause(delay=0.5, hard=True)
            call loading_screen(filename="02_09") from _call_loading_screen_3
            jump E3_YUK_01

        "If only there was something we could do...":
            voice "audio/voice/E3/G01/01/HA/HA013.ogg"
            hachiman "Well... I don't feel so good about it either. If only there was something we could do. Unfortunately, I don't think there is."
            #^DeepL MTL + AeonArcore. needs check.
            voice "audio/voice/E3/G01/01/YI/YI014.ogg"
            yui "Yeah, I want to do something, too."
            jump E3_YUI_01

label E3_G07_01:
    hachiman "(My future courses... Well, I'm going to be a stay at home husband, so I'm not particularly worried.)"
    "However, this questionnaire goes only as far as university, and the future that spreads beyond that is not clear."
    hachiman "(If I say that I'm still aiming for a full-time husband, she would be angry...)"
    "...In the meantime, class started. However, whimsical stories were leaking out everywhere, like trailing morning lingers."
    play music "audio/bgm/BGM26.ogg"
    show hiratsuka school mid_left angry at center with dissolve:
        xoffset 110 yoffset 80
    voice "audio/voice/E3/G07/01/SZ/SZ000.ogg"
    hiratsuka "What's up with you all today, you seem restless..."
    show hiratsuka happy with dissolve
    voice "audio/voice/E3/G07/01/SZ/SZ001.ogg"
    hiratsuka "Real quick. Ah, the questionnaire I handed out earlier was just a draft, but the actual course selection questionnaire that was handed out today will be the standart for classification after spring."
    show hiratsuka angry with dissolve
    voice "audio/voice/E3/G07/01/SZ/SZ002.ogg"
    hiratsuka "Because it'll affect future courses, please write it seriously... Ah, there is also a counseling session led by the student council.
        The graduates will be available for consultation before you have to turn it in."
    show hiratsuka school mid_center angry at center with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E3/G07/01/SZ/SZ003.ogg"
    hiratsuka "...By the way, the deadline for submission is at the end of the month. Make sure you submit it by then."
    play sound "audio/sfx/SE05/SE05_13.ogg"
    show hiratsuka happy with dissolve
    voice "audio/voice/E3/G07/01/SZ/SZ004.ogg"
    hiratsuka "Well, it's a privilege of young people to be able to worry about this. It's good to decide with plenty of time."
    window auto hide dissolve
    stop voice
    stop sound
    stop music fadeout 0.5
    scene classroomD with fade
    window auto show dissolve
    hachiman "(Ah, this is big... I mean, there are many things to consider.)"
    voice "audio/voice/E3/G07/01/XE/XE000.ogg"
    sgA "What do you guys want to do?"
    voice "audio/voice/E3/G07/01/XH/XH000.ogg"
    sgB "Well, I think I'm going to do liberal arts for the time being."
    voice "audio/voice/E3/G07/01/XJ/XJ000.ogg"
    sgC "Oh, not the sciences? My parents told me that I could qualify as a pharmacist..."
    voice "audio/voice/E3/G07/01/XH/XH001.ogg"
    sgB "Yeah, but honestly, I'm not that good at sciences."
    voice "audio/voice/E3/G07/01/XE/XE001.ogg"
    sgA "It's going to be lonely to have different classes, right?"
    voice "audio/voice/E3/G07/01/XJ/XJ001.ogg"
    sgC "I'm not crazy about math, but should I choose the sciences... I think Hayama-kun is in sciences!"
    voice "audio/voice/E3/G07/01/XE/XE002.ogg"
    sgA "Ah, then I will too!"
    voice "audio/voice/E3/G07/01/XH/XH002.ogg"
    sgB "Ah, I won't have time to talk to you if we're in different classes."
    hachiman "(Hayama is so popular... Well, for students, the current relationships are also important. There are many ways of life, careers, and choices...)"
    hachiman "(Well, I can't say about others because my method of choosing a path is the elimination method...)"
    menu E3_G07_01_menu:
        hachiman "(It looks like there's still time before the next class starts...)"
        with dissolve
        "Sleep in the classroom":
            $firstSchoolDayFlag = "saki"
            hachiman "(Maybe I should take a nap...)"
            "By the time I was in my perfect napping position, a girl with long bluish hair entered my field of vision...."
            jump E3_SAK_01
        "Go into the hallway":
            $firstSchoolDayFlag = "hiratsuka"
            hachiman "(I'll got the hallway for a change of scenery.)"
            play sound "audio/sfx/SE04/SE04_01.ogg"
            scene black with CropMove(0.5, mode="wipeleft")
            $renpy.pause(delay=0.5, hard=True)
            scene skyA with CropMove(0.5, mode="wipeleft")
            $renpy.pause(delay=0.5, hard=True)
            window auto show dissolve
            "I left the classroom and headed towards the special use building. There aren't many people who usually head this way, so it's pretty quiet."
            window auto hide dissolve
            stop sound
            show transition_2a at truecenter:
                yoffset -890
                parallel:
                    linear 0.5 yoffset -190
            show transition_2b at truecenter:
                yoffset 890
                parallel:
                    linear 0.5 yoffset 190
            $renpy.pause(delay=0.5, hard=True)
            hide transition_2a
            hide transition_2b
            show black
            play sound "audio/sfx/SE00/SE00_07.ogg"
            window auto show dissolve
            "As I closed my eyes and was immersed in the pleasant silence of the hallway, I heard a pair of shoes clicking their way towards me in a confident stride, and so I opened my eyes."
            window auto hide dissolve
            stop sound
            jump E3_SHI_01

label E3_G07_02:
    "There, something suddenly caught my eye."
    hachiman "(Hm? I recognize that silhouette... Is it who I think it is? Does she also have issues with her course?)"
    window auto hide dissolve
    show sakiHallwaya with Dissolve(1.0)
    play music "audio/bgm/BGM09.ogg"
    window auto show dissolve
    "I looked over and saw Kawasaki in the corner of the hallway, phone in her hand. I don't see her often with such a peaceful look on her face, so I felt as if I just saw something rare."
    show sakiHallwayb
    with dissolve
    voice "audio/voice/E3/G07/02/SA/SA000.ogg"
    saki "............"
    hachiman "(Is she mailing her brother, or perhaps her sister? She's such a good big sister.)"
    hachiman "(But if you have a lot of siblings, you might have a hard time making a decision about your future. I wonder if it would be better for Komachi to go the public school route until college...)"
    stop music
    voice "audio/voice/E3/G07/02/SZ/SZ000.ogg"
    mystery "Huh, Hikigaya? Aren't you going to seek career guidance as well?"
    window auto hide dissolve
    stop voice
    $renpy.pause(delay=0.5, hard=True)
    scene hallwayB
    show hiratsuka school_sunset mid_left angry at center:
        xoffset 110 yoffset 80
    with dissolve
    window auto show dissolve
    play music "audio/bgm/BGM26.ogg"
    "Right behind me stood Hiratsuka-sensei holding a document that seems to be a career guidance group on a side glance."
    voice "audio/voice/E3/G07/02/HA/HA000.ogg"
    hachiman "Sensei. No, I'll probably be going to a private liberal arts school..."
    show hiratsuka sad with dissolve
    voice "audio/voice/E3/G07/02/SZ/SZ001.ogg"
    hiratsuka "That sounds good for a dedicated response, but you might want to take a few steps back and think carefully."
    voice "audio/voice/E3/G07/02/HA/HA001.ogg"
    hachiman "Take a few steps back... then house husband it is."
    show hiratsuka school_sunset near_center annoyed with dissolve:
        xoffset 30 yoffset 75
    voice "audio/voice/E3/G07/02/SZ/SZ002.ogg"
    hiratsuka "Stop that nonsense!"
    voice "audio/voice/E3/G07/02/HA/HA002.ogg"
    hachiman "OuchOuchOuchOuchOuchOuchOuch!"
    show hiratsuka school_sunset near_left annoyed at center with dissolve:
        xoffset 245 yoffset 75
    voice "audio/voice/E3/G07/02/SZ/SZ003.ogg"
    hiratsuka "Be a little more realistic."
    voice "audio/voice/E3/G07/02/HA/HA003.ogg"
    hachiman "Reality is painful, that's why I made that choice, you know..."
    hide hiratsuka with dissolve
    show hiratsuka school_sunset mid_left sad at center with dissolve:
        xoffset 110 yoffset 80
    voice "audio/voice/E3/G07/02/SZ/SZ004.ogg"
    hiratsuka "You're really hopeless... Don't you have any interest in anything at all?"
    voice "audio/voice/E3/G07/02/HA/HA004.ogg"
    hachiman "If it's about my interests, that would be just my hobbies. Such things like having a favorite job makes life itself unpleasant..."
    show hiratsuka frown with dissolve
    voice "audio/voice/E3/G07/02/SZ/SZ005.ogg"
    hiratsuka "Hm, what you said may have a point. It's very like you though. Well there's still time, so try to think about it even a little."
    show hiratsuka happy with dissolve
    voice "audio/voice/E3/G07/02/HA/HA005.ogg"
    hachiman "............"
    "When I couldn't say anything to those well-meaning eyes of hers... Hiratsuka-sensei laughed with a big smile on her face and immediately went inside the guidance counseling room."
    stop music fadeout 1.0
    window auto hide dissolve
    hide hiratsuka with dissolve
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    hachiman "(Anyway...)"
    if firstSchoolDayFlag == "saki":
        jump E3_SAK_02
    jump E3_SHI_04
    #hiratsuka and saki route branches here

label E3_G08_01:
    scene black with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "I lied on the table caring less about the rest... However, more thoughts appeared in my mind."
    hachiman "(This kind of baseless rumour, if it gets too big, the people involved will be bothered... Hopefully it doesnt....)"
    stop music fadeout 0.5
    play music ["<silence 0.3>","audio/bgm/BGM46.ogg"]
    voice "audio/voice/E3/G08/01/ZH/ZH000.ogg"
    sbA "What are we gonna do about the career path?"
    voice "audio/voice/E3/G08/01/ZI/ZI000.ogg"
    sbB "Why don't you go into humanities with us? Getting credits on science classes in college is hard, you know."
    voice "audio/voice/E3/G08/01/ZC/ZC000.ogg"
    sbC "Right, right, humanities are super free form and like, doable, right? We won’t get to have as much fun when we’re not students, so we have to think about that too!"
    voice "audio/voice/E3/G08/01/ZH/ZH001.ogg"
    sbA "I know, right? If I get into college, I want a girlfriend..."
    voice "audio/voice/E3/G08/01/ZI/ZI001.ogg"
    sbB "Nah, you couldn't. Passing the test, getting a girlfriend... not happening. Unless you're a guy like Hayama."
    voice "audio/voice/E3/G08/01/ZC/ZC001.ogg"
    sbC "Hayama, huh? Yeah, that’s true. If that rumor going around about him is true, I'm seriously jealous..."
    hachiman "(Now even the guys are talking about it.)"
    hachiman "(As I'm laying on my desk, all of it reaches my ears, and I feel like something is pinching at me, deep inside my chest.)"
    window auto hide dissolve
    scene classroomA with Fade(1.0, 0.5, 1.0)
    menu E3_G08_01_menu:
        with dissolve
        hachiman "(I somehow don't feel very comfortable on my desk anymore...)"
        "It's hard staying in the classroom": #教室に居づらいな
            #Yumiko
            window auto show dissolve
            "not done"
            jump E3_G08_01_menu
        "Better not sleep on my desk.": #寝心地が悪い
            #Iroha
            $firstSchoolDayFlag = "iroha"
            jump E3_IRO_01
        "I'll just go to the bathroom.": #トイレでも行くか
            #haruno route
            hachiman "(Ah, well I guess I'll go to the toilet before the teacher comes in...)"
            window auto hide dissolve
            jump E3_HAR_01

label E3_G09_01:
    scene clubroomB
    with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM41.ogg"
    show yui school_sunset mid_right vhappy at left:
        xoffset 20 yoffset 75
    show yukino school_sunset mid_left vhappy at right:
        xoffset -165 yoffset 80
    with dissolve
    window auto show dissolve
    voice "audio/voice/E3/G09/01/YI/YI000.ogg"
    yui "By the way, it's been a while since we checked our e-mail~"
    "Email... the \"Chiba Prefecture Crossing Troubles Mail?\"?"
    "Hiratsuka-sensei actually gave this email to us so that we can help people. It hasn't seen much use however."
    voice "audio/voice/E3/G09/01/HA/HA000.ogg"
    hachiman "Well, we had the New Year's holidays just recently."
    hide yukino
    $url = ["yukino school_sunset mid_left vhappy", "yukino school_sunset mid_left surprised"]
    $multiImagePara = [-165, 80, 0, 0, 1.2]
    call multiImage(1) from _call_multiImage_77
    voice "audio/voice/E3/G09/01/YK/YK000.ogg"
    yukino "Yeah... Ara?"
    call finishmultiImage from _call_finishmultiImage_81
    show yukino school_sunset mid_left surprised at right:
        xoffset -165 yoffset 80
    show yui happy with dissolve
    voice "audio/voice/E3/G09/01/YI/YI001.ogg"
    yui "What's up? Ah! An email came in!"
    show yukino happy with dissolve
    voice "audio/voice/E3/G09/01/YK/YK001.ogg"
    yukino "Yes... It looks to be from Miura-san."
    call mail_function("yumiko", "yumiko", "", "How do people choose between arts and sciences?") from _call_mail_function_yumiko1
    show black with dissolve:
        alpha 0.3
    yumiko "(How do people choose between arts and sciences?)"
    voice "audio/voice/E3/G09/01/HA/HA001.ogg"
    hachiman "Oh? It's about the career path."
    stop voice
    call mail_clear from _call_mail_clear_yumiko
    hide black with dissolve
    show yukino angry with dissolve
    voice "audio/voice/E3/G09/01/YK/YK002.ogg"
    yukino "............"
    voice "audio/voice/E3/G09/01/HA/HA002.ogg"
    hachiman "What's wrong?"
    show yukino pout with dissolve
    voice "audio/voice/E3/G09/01/YK/YK003.ogg"
    yukino "Ah, it's nothing. I was just a little surprised that someone like Miura-san is troubled by this."
    voice "audio/voice/E3/G09/01/HA/HA003.ogg"
    hachiman "You don't have to be so mean... I'm sure even Miura has things to worry about, no matter if she's a bitchy queen-bee."
    show yukino happy with dissolve
    voice "audio/voice/E3/G09/01/YK/YK004.ogg"
    yukino "You're the one saying mean things... I didn't even mean it in that way. I just thought that someone as decisive as her wouldn't be troubled over this."
    show yui school_sunset mid_center vhappy at left:
        xoffset 255 yoffset 75
    with dissolve
    voice "audio/voice/E3/G09/01/YI/YI002.ogg"
    yui "Hahaha.... Of course, Yumiko has her own worries, too. It's about a career path after all."
    voice "audio/voice/E3/G09/01/HA/HA004.ogg"
    hachiman "Is there any reason to worry about a future career? It seems like something you can decide pretty quickly. It's hard to find something you want to do, but it's easy to come up with something you don't want to do."
    show yukino pout with dissolve
    voice "audio/voice/E3/G09/01/YK/YK005.ogg"
    yukino "That's an awfully backwards way of looking at it, but it is efficient."
    show yui angry with dissolve
    voice "audio/voice/E3/G09/01/YI/YI003.ogg"
    yui "Well, I don't think that's what she's worried about. I mean, we're all going to be split up, so she's wondering what to do about it."
    voice "audio/voice/E3/G09/01/HA/HA005.ogg"
    hachiman "Ah, that's true... But that's just how it goes."
    show yui pout with dissolve
    voice "audio/voice/E3/G09/01/YI/YI004.ogg"
    yui "Yeah. That's true, but... We'll, like, seperate, doing our own thing, chasing our own goals and... we can't be in the same class if we're separated by arts and sciences."
    hachiman "(Oh, you mean the \"I want to be in the same class as someone so what do I chose~?\" thing? I heard people talking about it in the classroom.)"
    show yukino happy with dissolve
    voice "audio/voice/E3/G09/01/YK/YK006.ogg"
    yukino "You say that, but I've always been in a different section and class to begin with..."
    show yui school_sunset mid_right surprised at left with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E3/G09/01/YI/YI005.ogg"
    yui "S-Sorry, Yukinon! I really didn't mean anything by it. I-I don't really know it sounded like that, but it doesn't matter if you're in a different class!"
    show yukino surprised with dissolve
    hachiman "(Yuigahama hugged Yukinoshita tightly. Mm-hmm. A good friendship is beautiful, isn't it? Gahama-san and Yukinon are BFFs!)"
    stop music fadeout 1.0
    "As I patted my chest in relief at the sight of how close they were, Yuigahama suddenly noticed something."
    play music ["<silence 0.5>", "audio/bgm/BGM32.ogg"]
    show yui school_sunset mid_center happy at left:
        xoffset 255 yoffset 75
    with dissolve
    voice "audio/voice/E3/G09/01/YI/YI006.ogg"
    yui "Ah, so that's what it is..."
    voice "audio/voice/E3/G09/01/HA/HA006.ogg"
    hachiman "What's that?"
    show yui vhappy with dissolve
    voice "audio/voice/E3/G09/01/YI/YI007.ogg"
    yui "Yeah... Yumiko wants to know about Hayato's career path. She seemed to be interested in it in class now that I think back on it..."
    show yukino happy with dissolve
    voice "audio/voice/E3/G09/01/YK/YK007.ogg"
    yukino "Can't she just ask him herself if that's the case?"
    show yui school_sunset mid_right pout at left:
        xoffset 20 yoffset 75
    with dissolve
    voice "audio/voice/E3/G09/01/YI/YI008.ogg"
    yui "She did try talking to him about it in the classroom, but Hayato said she should figure it out for herself, and didn't tell her..."
    hachiman "(Well, he's not going to like it when his influence cuts off the options of people he's close to.)"
    show yukino angry with dissolve
    voice "audio/voice/E3/G09/01/YK/YK008.ogg"
    yukino "I see..."
    window auto hide dissolve
    call loading_screen from _call_general_loading_shool17
    scene black
    window auto show dissolve
    "We then spent the rest of the day thinking how to deal with Miura's issue."
    window auto hide dissolve
    scene skyB with dissolve
    play sound "audio/sfx/SE04/SE04_13.ogg"
    $renpy.pause(delay=1.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E3/G09/01/YI/YI009.ogg"
    yui "Ah, someone's here. Come in!"
    window auto hide dissolve
    play sound "audio/sfx/SE04/SE04_01.ogg"
    $renpy.pause(delay=1.5, hard=True)
    scene clubroomB with dissolve
    show yumiko school_sunset mid_center happy flat at left:
        xoffset 0 yoffset 75 alpha 0
        parallel:
            easein 0.5 xoffset 125
        parallel:
            linear 0.5 alpha 1.0
    $renpy.pause(delay=1.0, hard=True)
    hide yumiko
    stop sound fadeout 0.5
    show yumiko school_sunset mid_center happy at left:
        xoffset 125 yoffset 75
    window auto show dissolve
    voice "audio/voice/E3/G09/01/YM/YM000.ogg"
    yumiko "Have a moment?"
    play music "audio/bgm/BGM46.ogg"
    show yui school_sunset mid_left surprised at right:
        xoffset -270 yoffset 75
    with dissolve
    voice "audio/voice/E3/G09/01/YI/YI010.ogg"
    yui "Yumiko? What's the matter?"
    show yumiko pout with dissolve
    voice "audio/voice/E3/G09/01/YM/YM001.ogg"
    yumiko "I just had something I wanted to talk about."
    show yui annoyed with dissolve
    voice "audio/voice/E3/G09/01/YI/YI011.ogg"
    yui "Is it something to do with your e-mail?"
    show yumiko sad with dissolve
    voice "audio/voice/E3/G09/01/YM/YM002.ogg"
    yumiko "Not exactly. It's related, but..."
    hide yui with dissolve
    show yumiko school_sunset mid_left annoyed at left:
        xoffset 240 yoffset 75
    with dissolve
    voice "audio/voice/E3/G09/01/YM/YM003.ogg"
    yumiko "Nevermind that. Is there something between you and Hayato?"
    show yukino school_sunset mid_left happy at right:
        xoffset -170 yoffset 80
    with dissolve
    "She was hesitant and careful replying to Yuigahama, but when she spoke to Yukinoshita, she completely changed her attitude."
    show yukino unimpressed with dissolve
    voice "audio/voice/E3/G09/01/YK/YK009.ogg"
    yukino "Nothing really. We're just old acquaintances."
    show yumiko school_sunset mid_center annoyed at left:
        xoffset 125 yoffset 75
    with dissolve
    voice "audio/voice/E3/G09/01/YM/YM004.ogg"
    yumiko "Is that all?"
    show yukino angry with dissolve
    voice "audio/voice/E3/G09/01/YK/YK010.ogg"
    yukino "What would I gain from lying about this? In fact, it's been bothering me for as long as I can remember."
    show yumiko unimpressed with dissolve
    voice "audio/voice/E3/G09/01/YM/YM005.ogg"
    yumiko "Excuse me? What's with the way you said that? It seriously pisses me off. I really hate that about you."
    voice "audio/voice/E3/G09/01/YI/YI012.ogg"
    yui "Yumiko! Didn't I already tell you how that went? Yukinon and Hayato-kun are just connected through their families."
    show yumiko school_sunset mid_left sad at left:
        xoffset 240 yoffset 75
    with dissolve
    voice "audio/voice/E3/G09/01/YM/YM006.ogg"
    yumiko "But, if it's just that then... Hayato wouldn't have been so bothered. I've never seen him like that before."
    show yukino happy with dissolve
    voice "audio/voice/E3/G09/01/YK/YK011.ogg"
    yukino "He's not bothered about me, it's probably something else he's worrying about."
    show yumiko school_sunset mid_center annoyed at left:
        xoffset 125 yoffset 75
    with dissolve
    voice "audio/voice/E3/G09/01/YM/YM007.ogg"
    yumiko "That's just... maybe that's the way you see it. You wouldn't know what Hayato's thinking."
    show yumiko school_sunset mid_left unimpressed at left:
        xoffset 240 yoffset 75
    with dissolve
    voice "audio/voice/E3/G09/01/YM/YM008.ogg"
    yumiko "I mean, something must have happened. Not now, but... in the past."
    show yumiko unimpressed with dissolve
    voice "audio/voice/E3/G09/01/YK/YK012.ogg"
    yukino "Even if something did happen and I gave you a detailed account, would it change anything? Would you... would anyone even believe it?"
    show yukino angry
    show yumiko angry
    with dissolve
    voice "audio/voice/E3/G09/01/YK/YK013.ogg"
    yukino "In the end, none of it matters."
    show yumiko school_sunset mid_center annoyed at left:
        xoffset 110 yoffset 75
    with dissolve
    voice "audio/voice/E3/G09/01/YM/YM009.ogg"
    yumiko "It's this side of you, that I really....!"
    show yukino unimpressed with dissolve
    voice "audio/voice/E3/G09/01/YK/YK014.ogg"
    yukino "Anything else you wish to say?"
    show yumiko zorder 1:
        parallel:
            easein 0.5 xoffset 0
    show yukino:
        parallel:
            easein 0.5 xoffset -45
    hide yui
    $url = ["yui school_sunset mid_left pout", "yui school_sunset mid_right pout"]
    $multiImagePara = [10, 75, -110, 75, 3.5]
    call multiImage(0, False) from _call_multiImage_78
    voice "audio/voice/E3/G09/01/YI/YI013.ogg"
    yui "Yumiko, please calm down... Yukinon you too, okay?"
    call finishmultiImage from _call_finishmultiImage_82
    show yui school_sunset mid_right pout behind yumiko at center:
        xoffset -110 yoffset 75
    show yukino happy with dissolve
    voice "audio/voice/E3/G09/01/YK/YK015.ogg"
    yukino "I'm calm. I'm already used to this kind of thing."
    show yukino unimpressed with dissolve
    voice "audio/voice/E3/G09/01/YK/YK016.ogg"
    yukino "It's not something I have to get worked up over... Besides, as long as the people close to me understand then that's enough."
    show yumiko school_sunset mid_left sad at left with dissolve:
        xoffset 110 yoffset 75
    voice "audio/voice/E3/G09/01/YM/YM010.ogg"
    yumiko "Isn't that a given? That's why I want to..."
    stop music
    show yui school_sunset mid_left pout behind yumiko at center with dissolve:
        xoffset 10 yoffset 75
    show yukino happy with dissolve
    voice "audio/voice/E3/G09/01/YI/YI014.ogg"
    yui "Huh?"
    play music "audio/bgm/BGM42.ogg"
    voice "audio/voice/E3/G09/01/YM/YM011.ogg"
    yumiko "Be someone he considers close. I want to be someone like that to him and I want to know."
    hachiman "(Ah, so that's what it is. Even she's not saying it outright, I get it. I finally understand. I can sympathize with her at the least.)"
    voice "audio/voice/E3/G09/01/HA/HA007.ogg"
    hachiman "Miura. You don't want to know if something's happened in the past, do you?"
    hachiman "(She probably doesn't care about what happened in the past, or even his career path. She just want's to know what he's thinking, what he's feeling. She just wants to understand.)"
    show yumiko school_sunset mid_center pout at left:
        xoffset 0 yoffset 75
    with dissolve
    voice "audio/voice/E3/G09/01/YM/YM012.ogg"
    yumiko "...! I-I just... um. Like, I wanted for us to stay together a bit longer. Um... like this, with everyone..."
    show yukino pout with dissolve
    voice "audio/voice/E3/G09/01/YK/YK017.ogg"
    yukino "Miura-san..."
    show yumiko sad with dissolve
    voice "audio/voice/E3/G09/01/YM/YM013.ogg"
    yumiko "Hayato's been distant lately and... if things keep going that way..."
    show yumiko pout with dissolve
    voice "audio/voice/E3/G09/01/YM/YM014.ogg"
    yumiko "I know it's weird, but..."
    show yui angry with dissolve
    voice "audio/voice/E3/G09/01/YI/YI015.ogg"
    yui "It's not weird. It's not weird at all. Of course you'd want everyone to be together."
    show yumiko sad with dissolve
    voice "audio/voice/E3/G09/01/YM/YM015.ogg"
    yumiko "...Yui."
    show yui school_sunset mid_center happy behind yumiko at center:
        xoffset -25 yoffset 75
    with dissolve
    voice "audio/voice/E3/G09/01/YI/YI016.ogg"
    yui "Yeah..."
    "Miura really managed to sense the confusion, the difference, the distance Hayato's been putting between him and others."
    "But she didn't want to lose that, so she's putting up at least some fight. If only to keep what they have and continue on. All her feelings were wrapped in that short e-mail of hers."
    "I've probably never seen such straightforward and strong emotion in my life. And so, I only need to ask her this."
    voice "audio/voice/E3/G09/01/HA/HA008.ogg"
    hachiman "............"
    voice "audio/voice/E3/G09/01/HA/HA009.ogg"
    hachiman "But you know Miura. The things Hayama doesn't tell you are probably things he doesn't want you to know. If you found out, he might dislike you for it."
    show yui surprised
    show yukino surprised
    with dissolve
    voice "audio/voice/E3/G09/01/YI/YI017.ogg"
    yui "Hey, Hikki!"
    show yukino pout with dissolve
    voice "audio/voice/E3/G09/01/YK/YK018.ogg"
    yukino "Hikigaya-kun..."
    hachiman "(I don't know whether or not stepping into someplace someone doesn't want you is the correct thing to do.)"
    voice "audio/voice/E3/G09/01/HA/HA010.ogg"
    hachiman "Do you want to know regardless?"
    show yui pout with dissolve
    hachiman "(That's why I wanted to know if she really wanted to cross that line, even if it means she will be disliked, ostracized or hurt.)"
    show yumiko pout with dissolve
    voice "audio/voice/E3/G09/01/YM/YM016.ogg"
    yumiko "I do... Even so I want to know... It's the only way."
    voice "audio/voice/E3/G09/01/HA/HA011.ogg"
    hachiman "I see."
    hachiman "(Even knowing you can't obtain it, you still resist and keep asking for it. Everybody is like that and she's no exception.)"
    voice "audio/voice/E3/G09/01/HA/HA012.ogg"
    hachiman "Got it. I'll make it happen somehow."
    show yumiko surprised
    show yui surprised
    show yukino surprised
    with dissolve
    voice "audio/voice/E3/G09/01/YM/YM017.ogg"
    yumiko "............"
    voice "audio/voice/E3/G09/01/YI/YI018.ogg"
    yui "...Hikki"
    voice "audio/voice/E3/G09/01/YK/YK019.ogg"
    yukino "But... how?"
    voice "audio/voice/E3/G09/01/HA/HA013.ogg"
    hachiman "I'll get something out of him whether he likes it or not, I'll investigate thoroughly... I can only guess after that."
    voice "audio/voice/E3/G09/01/HA/HA014.ogg"
    hachiman "In the end it may not be a correct answer, but if you're okay with that, I'll do something about it."
    show yui school_sunset mid_left happy behind yumiko at center:
        xoffset 10 yoffset 75
    with dissolve
    voice "audio/voice/E3/G09/01/YI/YI019.ogg"
    yui "Yumiko, would that be okay with you?"
    show yumiko sad with dissolve
    voice "audio/voice/E3/G09/01/YM/YM018.ogg"
    yumiko "...Yeah."
    show yukino pout with dissolve
    voice "audio/voice/E3/G09/01/YK/YK020.ogg"
    yukino "............"
    window auto hide dissolve
    $renpy.pause(delay=0.5, hard=True)
    call loading_screen from _call_general_loading_shool17_2
    scene black with fade
    $renpy.pause(delay=1.0, hard=True)
    stop sound fadeout 0.5
    scene fieldB with fade
    show hayama school_sunset far_right sad at right:
        xoffset -270 yoffset 65
    with dissolve
    window auto show dissolve
    voice "audio/voice/E3/G09/02/HY/HY000.ogg"
    hayama "............"
    hachiman "(...Huh? Was that Hayama just now? Perfect timing.)"
    hachiman "(...Ah.)"
    scene skyB with fade
    play music ["<silence 0.5>", "audio/bgm/BGM21.ogg"]
    voice "audio/voice/E3/G09/02/HY/HY001.ogg"
    hayama "...Sorry. I'm not interested in having a relationship right now."
    voice "audio/voice/E3/G09/02/XF/XF000.ogg"
    sgA "...So it's like that. Sorry. I'll see you... later..."
    voice "audio/voice/E3/G09/02/HY/HY002.ogg"
    hayama "Sure, see you."
    window auto hide dissolve
    play sound "audio/sfx/SE00/SE00_01.ogg"
    $renpy.pause(delay=2.0, hard=True)
    stop sound
    scene fieldB with fade
    show hayama school_sunset mid_right frown at center with dissolve:
        xoffset -25 yoffset 65
    window auto show dissolve
    voice "audio/voice/E3/G09/02/HY/HY003.ogg"
    hayama "............"
    show hayama school_sunset mid_center pout at center with dissolve:
        xoffset 5 yoffset 75
    $renpy.pause(delay=0.5, hard=True)
    show hayama surprised with dissolve
    voice "audio/voice/E3/G09/02/HY/HY004.ogg"
    hayama "...Hikigaya?"
    voice "audio/voice/E3/G09/02/HA/HA000.ogg"
    hachiman "...Yo."
    show hayama relieved with dissolve
    voice "audio/voice/E3/G09/02/HY/HY005.ogg"
    hayama "I made you see something weird."
    voice "audio/voice/E3/G09/02/HA/HA001.ogg"
    hachiman "Ah, sorry 'bout that."
    show hayama happy with dissolve
    voice "audio/voice/E3/G09/02/HY/HY006.ogg"
    hayama "Don't worry about it. Did you need something?"
    voice "audio/voice/E3/G09/02/HA/HA002.ogg"
    hachiman "No, nothing much. Just wanted to ask you... about your study path and stuff."
    show hayama school_sunset mid_right relieved at center with dissolve:
        xoffset -25 yoffset 65
    voice "audio/voice/E3/G09/02/HY/HY007.ogg"
    hayama "I see. Did someone ask you to?"
    voice "audio/voice/E3/G09/02/HA/HA003.ogg"
    hachiman "Not really... It's for reference."
    show hayama frown with dissolve
    voice "audio/voice/E3/G09/02/HY/HY008.ogg"
    hayama "For your work again, that is?"
    show hayama pout with dissolve
    voice "audio/voice/E3/G09/02/HY/HY009.ogg"
    hayama "You never change, do you?"
    voice "audio/voice/E3/G09/02/HA/HA004.ogg"
    hachiman "I said this before. Just the kind of club I'm in."
    show hayama school_sunset mid_center pout at center with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E3/G09/02/HY/HY010.ogg"
    hayama "That so? Then I have a request for you, too."
    voice "audio/voice/E3/G09/02/HY/HY011.ogg"
    hayama "What you're doing is annoying, so could you please stop?"
    voice "audio/voice/E3/G09/02/HA/HA005.ogg"
    hachiman "............"
    voice "audio/voice/E3/G09/02/HY/HY012.ogg"
    hayama "...Just kidding. What are you going to do if I said something like that next time?"
    voice "audio/voice/E3/G09/02/HA/HA006.ogg"
    hachiman "What will I do? I'll cross that bridge when I get there."
    show hayama happy with dissolve
    voice "audio/voice/E3/G09/02/HY/HY013.ogg"
    hayama "...Is that so?"
    show hayama school_sunset mid_right happy at center with dissolve:
        xoffset -25 yoffset 65
    voice "audio/voice/E3/G09/02/HY/HY014.ogg"
    hayama "Well, I don't know if someone asked you to do this, but... if you don't consider it properly and choose for yourself, you'll definitely regret it."
    voice "audio/voice/E3/G09/02/HA/HA007.ogg"
    hachiman "............"
    show hayama vhappy with dissolve
    voice "audio/voice/E3/G09/02/HY/HY015.ogg"
    hayama "I'll get going then."
    voice "audio/voice/E3/G09/02/HA/HA008.ogg"
    hachiman "Sure."
    hide hayama with dissolve
    window auto hide dissolve
    play sound "audio/sfx/SE00/SE00_03.ogg"
    $renpy.pause(delay=1.5, hard=True)
    window auto show dissolve
    hachiman "(What Hayama said seemed to be directed at a certain someone who wasn't here. And yet, strangely enough, it seemed he was addressing more than that someone.)"
    window auto hide dissolve
    stop music fadeout 0.5
    stop sound
    call loading_screen from _call_general_loading_shool17_3
    if firstSchoolDayFlag == "iroha":
        jump E3_IRO_05#iroha route
    elif firstSchoolDayFlag == "hiratsuka":
        jump E3_SHI_02

label E3_G10_01:
    $hayamaMarathonTalk = True
    scene skyA with Fade(1.5,1.5,1.5)
    play ambient "audio/sfx/SE05/SE05_00L_.ogg"
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E3/G10/01/ZJ/ZJ000.ogg"
    anc "The men's division of the marathon will be starting soon. All participants must be stationed near the starting point. I repeat..."
    window auto hide dissolve
    stop voice
    scene parkA with dissolve
    window auto show dissolve
    "Finally, the day arrived. Today is the campus marathon."
    "Not many people are motivated, but Hayama Hayato, who is expected to win the championship again, is. I'm going catch up to him in the front of the pack, and whether he likes it or not, I'm going to get his "
    "true intentions out of him."
    "It's a very clumsy way to go about it, but it's the only way I can break Hayama's permanent easy-going shield and get an inside read on him."
    hachiman "(It's about to begin...)"
    show hayama athletic far_right pout at center with dissolve:
        xoffset 10 yoffset 65
    voice "audio/voice/E3/G10/01/HY/HY000.ogg"
    hayama "............"
    voice "audio/voice/E3/G10/01/XE/XE000.ogg"
    sgA "Do your best, Hayama-kun!"
    voice "audio/voice/E3/G10/01/XH/XH000.ogg"
    sgB "I'm rooting for you!"
    show hayama vhappy with dissolve
    hachiman "(That's the only place that looks like a sports festival for idols.)"
    hide hayama with dissolve
    play sound "audio/sfx/SE02/SE02_21.ogg"
    $renpy.pause(delay=1.0, hard=True)
    voice "audio/voice/E3/G10/01/ZK/ZK000.ogg"
    peTM "On your mark!"
    stop ambient fadeout 0.5
    play music "audio/bgm/BGM43.ogg"
    hachiman "(Alright, here we go...)"
    voice "audio/voice/E3/G10/01/HA/HA000.ogg"
    hachiman "Totsuka... Counting on you."
    "I look ahead and call out to Totsuka behind me."
    voice "audio/voice/E3/G10/01/SI/SI000.ogg"
    totsuka "Yep, got it. Do your best, Hachiman."
    voice "audio/voice/E3/G10/01/HA/HA001.ogg"
    hachiman "I will."
    "I stare at Hayama's back in front of me. The stage is set. It's been set-up for me. What happens from here on is entirely up to me."
    window auto hide dissolve
    $renpy.pause(delay=1.0, hard=True)
    window auto show dissolve
    voice "audio/voice/E3/G10/01/SZ/SZ000.ogg"
    hiratsuka "Ready, set and... go!"
    window auto hide dissolve
    stop voice
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE02/SE02_22.ogg"
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE00/SE00_33L.ogg"
    $renpy.pause(delay=3.0, hard=True)
    stop sound fadeout 1.5
    $renpy.pause(delay=1.0, hard=True)
    stop music fadeout 1.0
    $renpy.pause(delay=0.5, hard=True)
    call loading_screen(duration="short") from _call_loading_screen_16
    play sound "audio/sfx/SE01/SE01_54.ogg"
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    hachiman "(Aaaah...)"
    window auto hide dissolve
    scene skyA with dissolve
    window auto show dissolve
    voice "audio/voice/E3/G10/01/HA/HA002.ogg"
    hachiman "Ah, the sky is pretty..."
    hachiman "(I fell down... Well, I used up all my energy chasing after Hayama and then fell down.)"
    "With the help of Totsuka and the others, I was able to create a situation in which Hayama and I were alone at the front of the pack, and by surprising him, I was able to somehow determine his career "
    "path."
    "In the end, Hayama didn't say it explicitly, but apparently he chose the humanities."
    "As for the gossip about Yukinoshita and him, he said he would settle that himself."
    hachiman "(It looks like I've been left in the dust. I don't think I'll be able to get up for a while.)"
    hachiman "(Now that the mission is over, let's start by getting up and out of here.)"
    window auto hide dissolve
    call loading_screen(duration="short") from _call_loading_screen_17
    scene parkB with fade
    play ambient "audio/sfx/SE05/SE05_00L_.ogg"
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    hachiman "(Haaa... I can finally see the finish li-huh?)"
    voice "audio/voice/E3/G10/01/IR/IR000.ogg"
    iroha "The winner, Hayama Hayato, please come up on stage!"
    play sound "audio/sfx/SE05/SE05_10.ogg"
    $renpy.pause(delay=1.5, hard=True)
    menu E3_G10_01_menu:
        hachiman "(Oh, they're getting pretty excited...)"
        with dissolve
        "I wonder if he resolved it?":
            stop sound fadeout 0.5
            "not done"
            jump E3_G10_01_menu
        "Looks like he resolved it.":
            stop sound fadeout 0.5
            voice "audio/voice/E3/G10/01/HY/HY001.ogg"
            hayama "I had a few close calls along the way, but thanks to fantastic competition and everyone's support, I was able to do my best and finish the race. Thank you very much."
            voice "audio/voice/E3/G10/01/HY/HY002.ogg"
            hayama "I want to give special thanks to Yumiko and Iroha... Thank you."
            window auto hide dissolve
            play sound "audio/sfx/SE05/SE05_10.ogg"
            $renpy.pause(delay=0.5, hard=True)
            window auto show dissolve
            voice "audio/voice/E3/G10/01/XE/XE001.ogg"
            sgA "So that rumor was really just a rumor..."
            voice "audio/voice/E3/G10/01/XH/XH001.ogg"
            sgB "Hayama-kun and Miura-san sure are close, aren't they?"
            hachiman "(So that's that, huh... I think I did pretty well this time around.)"
            hachiman "(This is bad, though. My body will be in a whole lot of pain starting tomorrow...)"
            if totsukaTalkFlag == "hiratsuka":
                hachiman "(I'll try not to let Hiratsuka-sensei see me. I'll be having muscle cramp 2 days from now and I feel like she'll be jealous of my youthfulness or something...)"
                window auto hide dissolve
                stop sound fadeout 0.5
                stop ambient
                scene black with fade
                jump E3_SHI_05

            window auto hide dissolve
            stop ambient
            stop sound fadeout 0.5
            scene black with fade
            jump E3_HAR_06

label E3_G11_01:
    "The hustle and bustle of the hall was a sure sign that career guidance counseling was about to begin."
    hachiman "(\"Career guidance meeting\", huh... I heard that graduates will be invited to give advice... I have a bad feeling about this.)"
    show yui school_sunset mid_center vhappy at left:
        xoffset 255 yoffset 75
    show yukino school_sunset mid_center happy at right:
        xoffset -230 yoffset 75
    with dissolve
    voice "audio/voice/E3/G11/01/YK/YK000.ogg"
    yukino "...What's wrong, Hikigaya-kun? You've been looking quite restless."
    show yui happy with dissolve
    voice "audio/voice/E3/G11/01/YI/YI000.ogg"
    yui "Are you looking for someone?"
    hachiman "(No, I'm not. But I can't say meeting a scary someone didn't cross my mind though...)"
    voice "audio/voice/E3/G11/01/HA/HA000.ogg"
    hachiman "Nah, it's nothing like that. Let's just finish up and go home."
    show yui vhappy with dissolve
    voice "audio/voice/E3/G11/01/YI/YI001.ogg"
    yui "Yeah, let's!"
    play sound "audio/sfx/SE01/SE01_09.ogg"
    $renpy.pause(delay=1.0, hard=False)
    show yui happy with dissolve
    voice "audio/voice/E3/G11/01/YI/YI002.ogg"
    yui "...So, have you guys decided which field you're going into?"
    voice "audio/voice/E3/G11/01/HA/HA001.ogg"
    hachiman "I'm going for liberal arts."
    show yui surprised with dissolve
    voice "audio/voice/E3/G11/01/YI/YI003.ogg"
    yui "You've already decided!?"
    show yukino vhappy with dissolve
    voice "audio/voice/E3/G11/01/YK/YK001.ogg"
    yukino "The only thing he has going for him is his grades in Japanese, so it was most likely just a process of elimination."
    "Yukinoshita seemed somewhat relieved as she said this. The rumors around her continued, but she didn't seem bothered one bit by them right now."
    voice "audio/voice/E3/G11/01/HA/HA002.ogg"
    hachiman "Hey. \"Only thing\"?"
    show yui happy with dissolve
    voice "audio/voice/E3/G11/01/YI/YI004.ogg"
    yui "I see now~!"
    voice "audio/voice/E3/G11/01/HA/HA003.ogg"
    hachiman "So? What about you?"
    voice "audio/voice/E3/G11/01/YK/YK002.ogg"
    yukino "Who knows? So, Yuigahama-san, which career path have you decided on?"
    show yui pout with dissolve
    voice "audio/voice/E3/G11/01/YI/YI005.ogg"
    yui "Urgh... I don't really even want to think about my future~."
    voice "audio/voice/E3/G11/01/HR/HR000.ogg"
    mystery "Yahallo~"
    show yui surprised
    show yukino frown
    with dissolve
    hachiman "(Uu. That voice...)"
    hide yui
    hide yukino
    with dissolve
    play music "audio/bgm/BGM35.ogg"
    show haruno sweater_sunset far_center vhappy at center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E3/G11/01/YK/YK003.ogg"
    yukino "Nee-san..."
    show haruno sly with dissolve
    voice "audio/voice/E3/G11/01/HR/HR001.ogg"
    haruno "So Yukino-chan was here too. There, there. Big sis will make sure to give you lots of advice today~."
    voice "audio/voice/E3/G11/01/YI/YI006.ogg"
    yui "Ah..."
    show meguri school_sunset far vhappy flat at center behind haruno:
        xoffset 50 yoffset 75 alpha 0
        parallel:
            easein 0.5 xoffset 260
        parallel:
            linear 0.5 alpha 1.0
    $renpy.pause(delay=0.75,hard=True)
    hide meguri
    show meguri school_sunset far vhappy at center behind haruno:
        xoffset 260 yoffset 75
    voice "audio/voice/E3/G11/01/MG/MG000.ogg"
    meguri "Whoa! Long time no see, everyone! Since you're here and all, why don't we give you some advice?"
    "As expected, Haruno-san looked dashing, and Meguri-senpai had popped up from behind her, holding up a finger."
    hachiman "(This healing aura... I feel like my mind and soul have been cleansed by MeguMeguMegu☆rin's Power.)"
    hide meguri
    hide haruno
    with dissolve
    show haruno sweater_sunset mid_center happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E3/G11/01/HR/HR002.ogg"
    menu E3_G12_01_menu:
        haruno "Well, there you have it. Any takers? Hikigaya-kun?"
        with dissolve
        #yui route
        "You sure have a lot of free time...":
            voice "audio/voice/E3/G11/01/HA/HA004.ogg"
            hachiman "...You sure have a lot of free time for a university student."
            show haruno sweater_sunset mid_left vhappy at center with dissolve:
                xoffset -25 yoffset 75
            voice "audio/voice/E3/G11/01/HR/HR003.ogg"
            haruno "I guess it just happens when you have both wealth and smarts."
            voice "audio/voice/E3/G11/01/HA/HA005.ogg"
            hachiman "Don't you have any friends?"
            hide haruno with dissolve
            show yui school_sunset mid_center surprised at left:
                xoffset 255 yoffset 75
            show haruno sweater_sunset mid_left vhappy at right :
                xoffset -240 yoffset 75
            with dissolve
            voice "audio/voice/E3/G11/01/YI/YI007.ogg"
            yui "You're one to talk, Hikki!"
            show haruno sweater_sunset mid_left worried at right with dissolve
            voice "audio/voice/E3/G11/01/HR/HR004.ogg"
            haruno "Yeah, so I can only be friends with someone like Hikigaya-kun!"
            voice "audio/voice/E3/G11/01/YI/YI008.ogg"
            yui "And she went along with it!?"
            hide haruno
            hide yui
            with dissolve
            show haruno sweater_sunset mid_center vhappy at center with dissolve:
                xoffset 10 yoffset 75
            voice "audio/voice/E3/G11/01/HR/HR005.ogg"
            haruno "Well, I'm joking of course. You can either have nothing to do or be really busy in university depending on how you want to play it. The way you take classes changes, too."
            hide haruno with dissolve
            show haruno sweater_sunset far_left vhappy at center:
                xoffset 225 yoffset 75
            show yukino school_sunset far_center happy at center:
                xoffset -285 yoffset 75
            with dissolve
            voice "audio/voice/E3/G11/01/HR/HR006.ogg"
            haruno "So, what kind of university student will you be, Yukinon-chan?"
            show yukino unimpressed with dissolve
            voice "audio/voice/E3/G11/01/YK/YK004.ogg"
            yukino "I don't there's any need to tell you, nee-san."
            show haruno happy with dissolve
            voice "audio/voice/E3/G11/01/HR/HR007.ogg"
            haruno "Mom is asking me about it, too. There aren't many opportunities like this to talk to you about it. You never tells us important things. What will onee-chan do with you?"
            show yukino vhappy with dissolve
            voice "audio/voice/E3/G11/01/YK/YK005.ogg"
            yukino "Oh? What a coincidence. I'm wondering what to do with my sister that keeps pestering me about the stupidest things."
            hide haruno
            hide yukino
            jump E3_YUI_08
        "Now that you mention it, you're an alumnus, right?":
            $firstSchoolDayFlag = "haruno meguri"
            voice "audio/voice/E3/G11/01/HA/HA007.ogg"
            hachiman "...Speaking of which, you're a graduate of this school, right?"
            hide haruno with dissolve
            show haruno sweater_sunset near_center sly at center with dissolve:
                xoffset -20 yoffset 75
            voice "audio/voice/E3/G11/01/HR/HR009.ogg"
            haruno "That's right. I'm your senpai~."
            show yukino school_sunset mid_center happy at left behind haruno with dissolve:
                xoffset 25 yoffset 75
            voice "audio/voice/E3/G11/01/YK/YK007.ogg"
            yukino "We're almost done. Let us go home when we finish."
            show haruno sweater_sunset near_left surprised at center with dissolve:
                xoffset -50 yoffset 75
            voice "audio/voice/E3/G11/01/HR/HR010.ogg"
            haruno "Where are you hurrying off to~? Aren't you going to ask me for advice?"
            show yukino unimpressed with dissolve
            voice "audio/voice/E3/G11/01/YK/YK008.ogg"
            yukino "No, thank you. I've already made up my mind."
            hide haruno with dissolve
            show haruno sweater_sunset mid_left vhappy at right behind yukino with dissolve:
                xoffset -240 yoffset 75
            voice "audio/voice/E3/G11/01/HR/HR011.ogg"
            haruno "Hmm, that's too bad. Gahama-chan will do then. How about a consultation?"
            show yui school_sunset mid_right surprised at center behind haruno with dissolve:
                xoffset -115 yoffset 75
            voice "audio/voice/E3/G11/01/YI/YI010.ogg"
            yui "I'm just an afterthought!? Ah, but I've already decided too..."
            show haruno sad with dissolve
            voice "audio/voice/E3/G11/01/HR/HR012.ogg"
            haruno "Come on, that's so boring. Well, there's no one in particular I want to hear from, so I guess I'll just get it over with and go home too~."
            hachiman "(There is one more person here who she hasn't asked, though. Well, it's not like I really wanted to talk to her anyway...)"
            show yukino angry
            show yui happy
            with dissolve
            voice "audio/voice/E3/G11/01/YK/YK009.ogg"
            yukino "Well then, we'll be going now, but don't do anything too unseemly, nee-san."
            stop voice fadeout 0.5
            hide yui
            hide yukino
            hide haruno
            with dissolve
            show haruno sweater_sunset near_center vhappy at center with dissolve:
                xoffset 390 yoffset 75
            voice "audio/voice/E3/G11/01/HR/HR013.ogg"
            haruno "Yes ma'am. See you later then... Hikigaya-kun."
            hide haruno with dissolve
            voice "audio/voice/E3/G11/01/HA/HA008.ogg"
            stop music fadeout 0.5
            hachiman "......Heh"
            jump E3_HAR_03

label E3_G12_01:
    play music ["<silence 0.5>","audio/bgm/BGM41.ogg"]
    show iroha school_sunset mid_center happy zorder 1 at left:
        xoffset 175 yoffset 75
    show yui school_sunset mid_right happy at center behind iroha:
        xoffset -110 yoffset 75
    show yukino school_sunset mid_center happy at right behind yui:
        xoffset -105 yoffset 75
    with dissolve
    hide yui
    $url = ["yui school_sunset mid_right happy", "yui school_sunset mid_left happy"]
    $multiImagePara = [-110, 75, 10, 75, 3.8]
    call multiImage(0, False) from _call_multiImage_79
    voice "audio/voice/E3/G12/01/YI/YI000.ogg"
    yui "This should be enough. Iroha-chan, what do you think?"
    call finishmultiImage from _call_finishmultiImage_83
    hide yui
    show yui school_sunset mid_left happy behind iroha at center:
        xoffset 10 yoffset 75
    show iroha vhappy with dissolve
    voice "audio/voice/E3/G12/01/IR/IR000.ogg"
    iroha "Yes, this is perfectly fine!"
    #iroha route branches here
    $points = _calculate_points()
    if firstSchoolDayFlag == "iroha" and points['iroha'] > 2:
        $totsukaTalkFlag = "iroha"
        voice "audio/voice/E3/G12/01/YK/YK003.ogg"
        yukino "Then I guess we'd better get going. There are already some students waiting for us in the hallway."
        show iroha happy with dissolve
        voice "audio/voice/E3/G12/01/HA/HA001.ogg"
        hachiman "Then let's hurry on out of here. I'll be getting out of here at least."
        voice "audio/voice/E3/G12/01/IR/IR002.ogg"
        iroha "Yui-senpai, Yukinoshita-senpai, thank you very much."
        show yui school_sunset mid_right happy at center behind iroha with dissolve:
            xoffset -110 yoffset 75
        voice "audio/voice/E3/G12/01/YI/YI004.ogg"
        yui "Sure! If you ever need any help again, just tell us!"
        show yukino vhappy with dissolve
        voice "audio/voice/E3/G12/01/YK/YK004.ogg"
        yukino "We'll be leaving now."
        hachiman "(You have no \"thank you\" in store for me, huh...)"
        show iroha school_sunset mid_left happy at left with dissolve:
            xoffset 115 yoffset 65
        voice "audio/voice/E3/G12/01/IR/IR003.ogg"
        iroha"Thank you too, senpai. I'll be counting on you."
        window auto hide dissolve
        stop music fadeout 0.5
        stop voice fadeout 0.5
        jump E3_IRO_07

    show yui mid_right vhappy with dissolve:
        xoffset -110 yoffset 75
    voice "audio/voice/E3/G12/01/YI/YI001.ogg"
    yui "We worked hard!"
    voice "audio/voice/E3/G12/01/ZG/ZG000.ogg"
    scvp "Ah, President! About this..."
    show yui mid_left surprised:
        xoffset 10 yoffset 75
    show iroha mid_left pout:
        xoffset 115 yoffset 65
        on hide:
            parallel:
                linear 0.5 alpha 0
            parallel:
                linear 0.5 xoffset 0
    with dissolve
    voice "audio/voice/E3/G12/01/IR/IR001.ogg"
    iroha "Eh? Isn't it written in the documents?"
    #Not entirely sure which footstep
    play footsteps "<to 2>audio/sfx/SE00/SE00_03.ogg" fadeout 1
    hide iroha
    $renpy.pause(delay=1,hard=False)
    show yukino vhappy with dissolve
    voice "audio/voice/E3/G12/01/YK/YK000.ogg"
    yukino "The same as usual."
    voice "audio/voice/E3/G12/01/YI/YI002.ogg"
    yui "Right!"
    jump E3_YUK_02
