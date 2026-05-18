label E3_CMM_01:
    scene black with Fade(1.0, 0.5, 1.0)
    play sound "<loop 0.16>audio/sfx/SE02/SE02_08L.ogg" loop
    window auto show dissolve
    voice "audio/voice/E3/CMM/01/KO/KO000.ogg"
    komachi "Onii-chan, wake up and turn it off!"
    voice "audio/voice/E3/CMM/01/HA/HA000.ogg"
    hachiman "...Ugh."
    window auto hide dissolve
    stop voice
    stop sound fadeout 0.3
    scene bedroomA
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    hachiman "(Ah, I feel dull... Wonder if I've got a fever. Maybe I caught a cold? Maybe it's what they call \"evil wind\" in English?)"
    show komachi school mid_center happy at center with dissolve:
        xoffset -75 yoffset 75
    play music "audio/bgm/BGM08.ogg"
    voice "audio/voice/E3/CMM/01/KO/KO001.ogg"
    komachi "Good morning, onii-chan. Breakfast is ready so hurry up and eat."
    voice "audio/voice/E3/CMM/01/HA/HA001.ogg"
    hachiman "Thanks for always doing this..."
    hide komachi
    $url = ["komachi school mid_center happy", "komachi school mid_center angry"]
    $multiImagePara = [-75, 75, 0, 0, 2.0]
    call multiImage() from _call_multiImage_27
    voice "audio/voice/E3/CMM/01/KO/KO002.ogg"
    komachi "You promised not to say that. Just get up and get ready!"
    call finishmultiImage from _call_finishmultiImage_28
    with dissolve
    voice "audio/voice/E3/CMM/01/HA/HA002.ogg"
    hachiman "Yeah..."
    "I crawl out of bed and while I dread it, I get into my uniform."
    "After getting changed, I went to the living room where Komachi was waiting. Surprisingly, quite some time had passed since I'd turned off my alarm."
    window auto hide dissolve
    scene houseA with Fade(1.0, 0.5, 1.0)
    show komachi school mid_center annoyed at center with dissolve:
        xoffset -75 yoffset 75
    window auto show dissolve
    voice "audio/voice/E3/CMM/01/KO/KO003.ogg"
    komachi "Onii-chan, you're late. You don't have much time left now."
    voice "audio/voice/E3/CMM/01/HA/HA003.ogg"
    hachiman "Yes, I'm well aware."
    show komachi school near_center happy at center with dissolve:
        xoffset 35 yoffset 75
    hachiman "(School is such a drag... it's hard... Even Komachi's breakfast is somehow lacking it's usual taste.)"
    voice "audio/voice/E3/CMM/01/HA/HA004.ogg"
    hachiman "Komachi... Onii-chan is probably sick."
    show komachi unimpressed with dissolve
    voice "audio/voice/E3/CMM/01/KO/KO004.ogg"
    komachi "Yeah, yeah, you're always sick. What is it this time? Home sickness? Hay fever?"
    voice "audio/voice/E3/CMM/01/HA/HA005.ogg"
    hachiman "D-Depression at work maybe..."
    show komachi school near_left unimpressed with dissolve:
        xoffset 10 yoffset 65
    voice "audio/voice/E3/CMM/01/KO/KO005.ogg"
    komachi "Stop talking like a new employee and hurry up and eat your food. You're going to make me late too."
    hide komachi with dissolve
    voice "audio/voice/E3/CMM/01/HA/HA006.ogg"
    hachiman "Sorry, I'll hurry up."
    hachiman "(Well, at least it looks like she's calmed down a bit from her entrance exam blues.)"
    hachiman "(If I don't leave soon, I'm really gonna be late. Alright, I'm feeling kinda pumped after eating Komachi's food!)"
    voice "audio/voice/E3/CMM/01/HA/HA007.ogg"
    hachiman "Thanks for the meal."
    show komachi school mid_center happy at center with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E3/CMM/01/KO/KO006.ogg"
    komachi "You're welcome."
    hide komachi with dissolve
    menu:
        hachiman "(Alright, let's get going.)"
        with dissolve
        "Call out to Komachi":
            hachiman "(I have to say goodbye to Komachi before leaving. I was with her during the entire winter vacation, even though she was very busy. She must be so worried that she can't see onii-chan for half a day!)"
            jump E3_CMM_02
        "Don't call out to Komachi": #yukino
            hachiman "(Damn, I mucked around a bit too long. It looks like Komachi's too busy to have the time to deal with me. I'd better get to school.)"
            jump E3_CMM_03

label E3_CMM_02:
    voice "audio/voice/E3/CMM/02/HA/HA000.ogg"
    hachiman "Well, I'd better get going."
    scene komachiLeaving
    with dissolve
    voice "audio/voice/E3/CMM/02/KO/KO000.ogg"
    komachi "Do you have your handkerchief, onii-chan? Tissues? You're not forgetting anything?"
    voice "audio/voice/E3/CMM/02/HA/HA001.ogg"
    hachiman "Are you my mom?"
    voice "audio/voice/E3/CMM/02/KO/KO001.ogg"
    komachi "Well, I'm surely ready to get married seeing as I can take such good care of onii-chan!"
    voice "audio/voice/E3/CMM/02/HA/HA002.ogg"
    hachiman "...Then it looks like the day you get married off will never come."
    voice "audio/voice/E3/CMM/02/KO/KO002.ogg"
    komachi "I don't know... I think it's coming sooner rather than later."
    voice "audio/voice/E3/CMM/02/HA/HA003.ogg"
    hachiman "Nah! Onii-chan won't allow it! I c-c-can't imagine K-Komachi ever leaving home!"
    voice "audio/voice/E3/CMM/02/KO/KO003.ogg"
    komachi "Yeah, yeah, it's still a long way off, so forget about it. Just get ready to leave already!"
    voice "audio/voice/E3/CMM/02/HA/HA004.ogg"
    hachiman "O-Okay..."
    hachiman "(Am I forgetting anything... Um... Okay I guess, not.)"
    voice "audio/voice/E3/CMM/02/HA/HA005.ogg"
    hachiman "Thanks, Komachi. Don't forget your stuff, either."
    voice "audio/voice/E3/CMM/02/KO/KO004.ogg"
    komachi "Yep. Ah, I'll be wearing the good luck charm I bought on my New Year's visit, so no sweat."
    "There is already a good luck charm hanging on Komachi's bag. I can't help
        but wish Komachi good luck. I might be overreacting."
    voice "audio/voice/E3/CMM/02/HA/HA006.ogg"
    hachiman "I hope it's on and working."
    voice "audio/voice/E3/CMM/02/KO/KO005.ogg"
    komachi "We just have to put our trust in it~. Well, off you go!"
    voice "audio/voice/E3/CMM/02/HA/HA007.ogg"
    hachiman "Oh, you be careful out there, too."
    voice "audio/voice/E3/CMM/02/KO/KO006.ogg"
    komachi "Yessir!"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    jump E3_CMM_04

label E3_CMM_03:
    hachiman "(Gotta hurry! I don't really mind being late, but I can't make Komachi late!)"
    voice "audio/voice/E3/CMM/03/KO/KO000.ogg"
    komachi "Onii-chan! It's dangerous if you rush like that! Watch out for cars!"
    voice "audio/voice/E3/CMM/03/HA/HA000.ogg"
    hachiman "Yeah, I'm off then."
    define lefttransition = CropMove(0.25,mode="slideleft")
    window auto hide dissolve
    scene black
    with lefttransition
    play sound "audio/sfx/SE04/SE04_06.ogg"
    $renpy.pause(delay=0.2, hard=True)
    scene outsideA
    with lefttransition
    window auto show dissolve
    hachiman "(Alright, let's get this over with...)"
    window auto hide dissolve
    stop music fadeout 1.0
    jump E3_CMM_04

label E3_CMM_04:
    scene black with Fade(1.0, 0.5, 0)
    play sound "audio/sfx/SE02/SE02_09.ogg"
    scene gatesA with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E3/CMM/04/HA/HA000.ogg"
    hachiman "Oh, it's the bell..."
    hachiman "(I made it in time. I guess I'll be fine since I'm this close now. I hope Komachi made it okay too.)"
    scene hallwayA
    with Fade(1.0, 0.5, 1.0)
    "Once I locked my bike and entered the school building, I slowly headed towards the classroom."
    hachiman "(I don't need to run if I made it this far. I mean, I'm just going to lie on my desk when I'm in the classroom anyway.)"
    voice "audio/voice/E3/CMM/04/HA/HA001.ogg"
    hachiman "Ahhhhhh..."
    hachiman "(Ah, I wish it was still winter break...)"
    voice "audio/voice/E3/CMM/04/SZ/SZ000.ogg"
    mystery "It's a new year and the first thing that comes out of your mouth at school is a sigh."
    voice "audio/voice/E3/CMM/04/HA/HA002.ogg"
    hachiman "Ah..."
    play music "audio/bgm/BGM26.ogg"
    show hiratsuka school mid_center happy at center with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E3/CMM/04/SZ/SZ001.ogg"
    hiratsuka "Morning."
    voice "audio/voice/E3/CMM/04/HA/HA003.ogg"
    hachiman "Good morning..."
    show hiratsuka unimpressed with dissolve
    voice "audio/voice/E3/CMM/04/SZ/SZ002.ogg"
    hiratsuka "Can't you put a bit more enthusiasm into it? That'll make a big difference in how others percieve you."
    voice "audio/voice/E3/CMM/04/HA/HA004.ogg"
    hachiman "I'm the type of guy that doesn't try to be someone I'm not."
    show hiratsuka angry with dissolve
    voice "audio/voice/E3/CMM/04/SZ/SZ003.ogg"
    hiratsuka "There's a difference in not appealing to anyone and being careless. You don't have to be liked by everyone, but you don't have to leave a bad impression either."
    voice "audio/voice/E3/CMM/04/HA/HA005.ogg"
    hachiman "I see. Just being on friendly terms."
    show hiratsuka school mid_left happy at center with dissolve:
        xoffset 110 yoffset 80
    voice "audio/voice/E3/CMM/04/SZ/SZ004.ogg"
    hiratsuka "Exactly. If you get it then hurry and try not to be late. Tardiness leaves a bad impression."
    voice "audio/voice/E3/CMM/04/HA/HA006.ogg"
    hachiman "Yes... I'll hurry."
    stop music fadeout 1.0
    hide hiratsuka with dissolve
    hachiman "(Ah, looks like this semester won't be a busy one for me.)"
    voice "audio/voice/E3/CMM/04/HA/HA007.ogg"
    hachiman "Well, less work means less worrying about work..."
    window auto hide dissolve
    scene black with Fade(1.0, 0.5, 0)
    jump E3_CMM_05

label E3_CMM_05:
    play ambient "audio/sfx/SE05/SE05_09L.ogg"
    scene classroomA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM30.ogg"
    window auto show dissolve
    "The classroom after winter break was quite lively. They probably have a lot to say about their break. Everyone was making a big fuss and was more energetic than usual."
    "The future course questionnaire was being passed around during the short homeroom in the morning. Everyone in the classroom was now in the middle of talking about it."
    "The noisy atmosphere wasn't going to change anytime soon."
    voice "audio/voice/E3/CMM/05/XE/XE000.ogg"
    sgA "I'm so worried about my courses. There aren't many girls in science too."
    voice "audio/voice/E3/CMM/05/XH/XH000.ogg"
    sgB "Yeah, I'm seriously stuck. What's everyone going to decide on?"
    voice "audio/voice/E3/CMM/05/XJ/XJ000.ogg"
    sgC "For real. Though you don't have to worry if you're in Class J."
    voice "audio/voice/E3/CMM/05/XE/XE001.ogg"
    sgA "Ah, hey. Have you heard? About Class J..."
    voice "audio/voice/E3/CMM/05/XH/XH001.ogg"
    sgB "Ah, people were saying they met up. Is that for real?"
    voice "audio/voice/E3/CMM/05/XE/XE002.ogg"
    sgA "Seriously! There were people who saw them together in Chiba..."
    voice "audio/voice/E3/CMM/05/XJ/XJ001.ogg"
    sgC "No way, what's with that? Sounds fun!"
    voice "audio/voice/E3/CMM/05/XH/XH002.ogg"
    sgB "She would seem like the type to go out with Hayama-kun. Actually, back then too..."
    hachiman "(Hayama? At some point the conversation had turned to him as a subject...)"
    "As I was getting ready to go to the clubroom, I'd heard an unexpected name amongst all the buzz. I directed my gaze towards the person in the center of the commotion."
    # background missing need to use copy from regular classroom
    window auto hide dissolve
    scene classroomC
    show tobe school far vhappy at left:
        xoffset 290 yoffset 75
    show hayama school far_center happy at right:
        xoffset -325 yoffset 65
    with dissolve
    window auto show dissolve
    "Tobe was talking about stupid stuff as usual, Hayama was leaning on the wall next to the window while looking outside. At times, he'd smile and respond appropriately like he'd just remembered something."
    window auto hide dissolve
    scene classroomD
    show yumiko school far_left frown at center:
        xoffset 0 yoffset 75
    with dissolve
    window auto show dissolve
    "Miura was leaning back against her seat while twirling her golden hair with one hand as usual and glaring at the future course questionnaire in her other hand."
    show yumiko angry
    show ebina school far_center happy at left:
        xoffset 220 yoffset 75
    show yui school far_center happy at right:
        xoffset -260 yoffset 75
    with dissolve
    voice "audio/voice/E3/CMM/05/YM/YM000.ogg"
    yumiko "What are you going to do, Yui?"
    voice "audio/voice/E3/CMM/05/YI/YI000.ogg"
    yui "I'm... probably going to go into liberal arts."
    show yumiko school far_center angry at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E3/CMM/05/YM/YM001.ogg"
    yumiko "I see. What about you Ebina?"
    voice "audio/voice/E3/CMM/05/EB/EB000.ogg"
    ebina "Liberal arts for me too. What about you, Yumiko?"
    show yumiko pout with dissolve
    voice "audio/voice/E3/CMM/05/YM/YM002.ogg"
    yumiko "I'm... still thinking about it."
    show yumiko angry with dissolve
    voice "audio/voice/E3/CMM/05/YM/YM003.ogg"
    yumiko "Tobe, how about you?"
    window auto hide dissolve
    scene classroomC
    show tobe school far at center:
        xoffset 40 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E3/CMM/05/TB/TB000.ogg"
    tobe "Courses, huh. Nah, I haven't decided yet, but I'm not good at memorizing. I might go into the sciences."
    voice "audio/voice/E3/CMM/05/YM/YM004.ogg"
    yumiko "Ha?"
    voice "audio/voice/E3/CMM/05/YI/YI001.ogg"
    yui "Huh? That's unexpected."
    show tobe sad with dissolve
    voice "audio/voice/E3/CMM/05/TB/TB001.ogg"
    tobe "I mean I don't have much of a choice. I can't remember English vocabulary."
    hachiman "(Hang on, English is necessary in both the liberal arts and sciences.)"
    window auto hide dissolve
    scene classroomE
    show tobe school far happy at right:
        xoffset -80 yoffset 75
    show ebina school far_center happy at center:
        xoffset 70 yoffset 75
    show yui school far_right happy at left:
        xoffset 45 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E3/CMM/05/TB/TB002.ogg"
    tobe "Which course are you all going for?"
    voice "audio/voice/E3/CMM/05/YI/YI002.ogg"
    yui "Ebina and I are probably going into the liberal arts. Yumiko hasn't decided yet."
    show tobe worried with dissolve
    voice "audio/voice/E3/CMM/05/TB/TB003.ogg"
    tobe "For real? Maybe I'll go into the liberal arts too."
    show ebina school far_left happy at center with dissolve:
        xoffset -30 yoffset 75
    voice "audio/voice/E3/CMM/05/EB/EB001.ogg"
    ebina "But they say the sciences have it easier in getting a full-time job. I think the sciences are good. You could mash together any chemical element!"
    show tobe sad with dissolve
    voice "audio/voice/E3/CMM/05/TB/TB004.ogg"
    tobe "A-Ah, I see... That's a thing, yeah, for sure."
    window auto hide dissolve
    stop voice
    scene classroomD
    show yumiko school far_center angry at left:
        xoffset 220 yoffset 75
    show hayama school far_center happy at right:
        xoffset -325 yoffset 65
    with dissolve
    window auto show dissolve
    voice "audio/voice/E3/CMM/05/YM/YM005.ogg"
    yumiko "What about you, Hayato?"
    voice "audio/voice/E3/CMM/05/HY/HY000.ogg"
    hayama "I've... sort of decided, but I need to really think it through."
    voice "audio/voice/E3/CMM/05/YM/YM006.ogg"
    yumiko "Huh..."
    "There was a moment of silence as Miura sighed aloud. In that silence, the classroom's gossiping became much more audible."
    voice "audio/voice/E3/CMM/05/XE/XE003.ogg"
    sgA "Is it true that Hayama-kun is going out with Yukinoshita-san after all?"
    show yumiko surprised1
    show hayama surprised
    with dissolve
    voice "audio/voice/E3/CMM/05/YM/YM007.ogg"
    yumiko "Huh?"
    stop ambient fadeout 1
    stop music
    show yumiko annoyed
    show hayama frown
    with dissolve
    play sound "audio/sfx/SE01/SE01_00.ogg"
    $renpy.pause(delay=0.7, hard=True)
    voice "audio/voice/E3/CMM/05/YM/YM008.ogg"
    yumiko "Whaaaaat?!"
    "Miura stood up with her chair, making a racket. My classmates who'd been absorbed in chatter all stopped and looked at her."
    "You could hear a pin drop in the classroom. In the middle of everyone's attention, Hayama shot daggers at the person who'd made that statement."
    show hayama annoyed with dissolve
    voice "audio/voice/E3/CMM/05/HY/HY001.ogg"
    hayama "Saying something so irresponsible..."
    "Hayama's voice was sharp, and because he was very different from his usual self, everyone was taken aback and at a loss for words."
    hide yumiko with dissolve
    play music "audio/bgm/BGM40.ogg"
    show tobe school far vhappy at left with dissolve:
        xoffset 290 yoffset 75
    voice "audio/voice/E3/CMM/05/TB/TB005.ogg"
    tobe "Ah, that's right! Hey, Hayato-kun, can you tell me your chosen course? I can't choose which path to take."
    voice "audio/voice/E3/CMM/05/HY/HY002.ogg"
    show hayama worried with dissolve
    hayama "What are you going to do by hearing mine? It's your own future, so you need to think about it seriously or you'll regret it."
    show tobe happy with dissolve
    voice "audio/voice/E3/CMM/05/TB/TB006.ogg"
    tobe "Okay, I'll think about it some more. But can I get some kinda input? Anyway, let's go to the bathroom."
    voice "audio/voice/E3/CMM/05/HY/HY003.ogg"
    hayama "At least go to the bathroom by yourself..."
    voice "audio/voice/E3/CMM/05/TB/TB007.ogg"
    tobe "Nah, advice and strategy meetings happen in the bathroom. Those are basically key at mixers."
    show hayama school far_center happy flat with dissolve:
        yoffset 65
        on hide:
            parallel:
                linear 0.5 alpha 0
            parallel:
                linear 0.5 xoffset -390
    voice "audio/voice/E3/CMM/05/HY/HY004.ogg"
    hayama "...Say that after you actually go to one."
    show tobe school far sad flat with dissolve:
        yoffset 75
        on hide:
            parallel:
                linear 0.5 alpha 0
            parallel:
                linear 0.5 xoffset 225
    voice "audio/voice/E3/CMM/05/TB/TB008.ogg"
    tobe "True, I've never been to a mixer before."
    window auto hide dissolve
    # looks a bit weird
    hide tobe
    hide hayama
    stop music fadeout 1.0
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE04/SE04_01.ogg"
    $renpy.pause(delay=1.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E3/CMM/05/YM/YM009.ogg"
    yumiko "............."
    play music "audio/bgm/BGM43.ogg"
    "When Hayama left the classroom, the chatter kicked up again."
    "Other than the gossip around Hayama and Yukinoshita dating, there were other topics, like future courses."
    menu school1_menu:
        with dissolve
        "I'm curious about all this noise. Especially about..."
        "Future courses, huh...":
            jump E3_G07_01
        "Rumours are horrible": #yukino
            window auto hide dissolve
            scene black with Fade(1.0, 0.5, 1.0)
            window auto show dissolve
            "Even though I was lying on my desk, I could still hear the girls sitting diagonally behind me chatting away."
            voice "audio/voice/E3/CMM/05/XE/XE004.ogg"
            sgA "How much of that is true? Are they dating after all?"
            voice "audio/voice/E3/CMM/05/XH/XH003.ogg"
            sgB "Who knows. It's not surprising, though. Yukinoshita-san only goes for good looking guys."
            voice "audio/voice/E3/CMM/05/XE/XE005.ogg"
            sgA "Ah, I know, right? She doesn't look that way, but to date him, she's completely, like, after his face."
            voice "audio/voice/E3/CMM/05/XJ/XJ002.ogg"
            sgC "Lol! It has to be the face!"
            "They kept their giggling low. It grated my ears. Even someone like me who wasn't involved was getting irritated. The people who were being gossiped about must feel even more so."
            "Those people who don't even know anything like to mix in speculations, desires, say whatever they want, and while they're at it, they lead the story towards one that's more interesting to them."
            "Most of those people don't have ill intentions. Their only reason for doing so is because it's more interesting."
            "If someone were to seriously hold them accountable, they'd just say something like, \"It's just gossip. No need to get so serious.\""
            "Yukino Yukinoshita has always lived in this environment. Someone with looks and ability would be the butt end of many expectations, a lot of attention and at the same time - jealousy."
            "I didn't come to know that because of how these rumours have visualized it. No, I knew that from the moment I met her."
            "Yuigahama probably felt the same way I did since she knows Yukinoshita."
            hachiman "(This is really irritating...)"
            window auto hide dissolve
            jump E3_G01_01
        "I'll watch what happens":#iroha and yumiko
            hachiman "(Even if it's just a rumour or real, my decision won't change... Well, as long as I don't do anything.)"
            window auto hide dissolve
            jump E3_G08_01

label E3_CMM_06:
    scene hallwayB with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM29.ogg"
    window auto show dissolve
    "While the dating rumor was still being whispered about throughout the school, the Service Club recieved a request."
    "Hiratsuka-sensei had asked the Service club to help the Student Council prepare for the Prospective Career Path Program. And so, Yukinoshita, Yuigahama and I found ourselves in front of the meeting room."
    "Originally, I should be the only one helping - that's what we agreed on anyway. But because the others had nothing to do apparently, “we're all in it together!”. And that brings us to right now..."
    "This is the first time I've come to this conference room since the preparations for the cultural festival... or maybe it was the sports festival?"
    hachiman "(“Help set up the Prospective Career Path Program”, huh...)"
    window auto hide dissolve
    play sound "audio/sfx/SE04/SE04_00.ogg"
    $renpy.pause(delay=0.5, hard=False)
    scene conferenceB
    show iroha school_sunset far_center frown at center:
        xoffset -30 yoffset 75
    with CropMove(0.5, mode="wipeleft")
    window auto show dissolve
    voice "audio/voice/E3/CMM/06/IR/IR000.ogg"
    iroha "Ah, senpai! You're la~te!"
    hide iroha with dissolve
    show yukino school_sunset mid_center happy at left:
        xoffset -105 yoffset 75
    show yui school_sunset mid_center happy at center:
        xoffset -25 yoffset 75
    show iroha school_sunset mid_left happy at right:
        xoffset -190 yoffset 65
    with dissolve
    voice "audio/voice/E3/CMM/06/IR/IR001.ogg"
    iroha "So, thank you two so much for coming~"
    show yui vhappy
    show yukino vhappy
    with dissolve
    voice "audio/voice/E3/CMM/06/YI/YI000.ogg"
    yui "Yahallo, Iroha-chan!"
    voice "audio/voice/E3/CMM/06/YK/YK000.ogg"
    yukino "Hello, Isshiki-san."
    show yui happy
    show yukino happy
    with dissolve
    voice "audio/voice/E3/CMM/06/YK/YK001.ogg"
    yukino "Now then, what should we do?"
    show iroha happy with dissolve
    voice "audio/voice/E3/CMM/06/IR/IR002.ogg"
    iroha "Um, first off, we need to rearrange these tables over here. Then, there’s papers we need to prepare..."
    voice "audio/voice/E3/CMM/06/IR/IR003.ogg"
    iroha "In the meantime, we, the Student Council, will be present and observe... or, I should say, will help if needed."
    voice "audio/voice/E3/CMM/06/HA/HA000.ogg"
    hachiman "Looks like this’ll be a long haul."
    show iroha sad with dissolve
    voice "audio/voice/E3/CMM/06/IR/IR004.ogg"
    iroha "True... This is also the Student Council's job apparently. If I’m being real, it’s just chores, though."
    voice "audio/voice/E3/CMM/06/HA/HA001.ogg"
    hachiman "I mean that's what the Student Council does - chores."
    show iroha school_sunset mid_center pout at right with dissolve:
        xoffset -190 yoffset 75
    voice "audio/voice/E3/CMM/06/IR/IR005.ogg"
    iroha "First time I'm hearing about that... Well, a certain someone did want me to be the Student Council president~"
    voice "audio/voice/E3/CMM/06/HA/HA002.ogg"
    hachiman "That was slick... But you seem to be doing a decent job, aren't you?"
    show iroha blush with dissolve
    voice "audio/voice/E3/CMM/06/IR/IR006.ogg"
    iroha "W-Well, it’s my job after all."
    show iroha happy with dissolve
    voice "audio/voice/E3/CMM/06/IR/IR007.ogg"
    iroha "That being said, please move the chairs and tables to create six individual booths. We’re leaving the heavy lifting to you, senpai."
    hachiman "(Heavy lifting? I’m a little lacking in that department...)"
    show yui vhappy with dissolve
    voice "audio/voice/E3/CMM/06/YI/YI001.ogg"
    yui "Okay! Let's move the chairs first!"
    voice "audio/voice/E3/CMM/06/YK/YK002.ogg"
    yukino "I agree."
    hide yui
    hide yukino
    hide iroha
    with dissolve
    hachiman "(I’m stuck doing more back lifting than I originally thought...)"
    "I let out a deep sigh and looked around the conference room, which was about to be transformed into a guidance room."
    window auto hide dissolve
    stop music fadeout 1.0
    scene meetingRoomB
    with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM33.ogg"
    window auto show dissolve
    hachiman "(Haaa, I'm tired. My waist hurts...)"
    voice "audio/voice/E3/CMM/06/ZG/ZG000.ogg"
    scvp "Thanks, you helped us big time. We wanted someone to help with setting this up."
    voice "audio/voice/E3/CMM/06/HA/HA003.ogg"
    hachiman "Don’t worry about it. Good job on your end."
    "We're used to Isshiki treating us like her servants. It's my fault anyway---Isshiki is the victim here."
    "With the setting-up nearly finished, each member of the Student Council are off diligently distributing documents to different spots of the Meeting Room."
    show yukino school_sunset mid_center pout at left:
        xoffset 25 yoffset 75
    show yui school_sunset mid_center pout at right:
        xoffset -305 yoffset 75
    with dissolve
    voice "audio/voice/E3/CMM/06/YI/YI002.ogg"
    yui "Hikki, good job!"
    voice "audio/voice/E3/CMM/06/HA/HA004.ogg"
    hachiman "You too. Looks like we’ve exhausted our usefulness here."
    voice "audio/voice/E3/CMM/06/YK/YK003.ogg"
    yukino "You’re right. The rest is up to the Student Council."
    hide yui
    hide yukino
    with dissolve
    "Finally being relieved from duty, I strech and look around the venue."
    menu:
#audio/voice/E3/G12/01
        hachiman "(Well, I think we’re done here, right...?)"
        with dissolve
        "Someone unexpected appeared":
            stop music fadeout 1.0
            jump E3_G07_02
        "I have a bad feeling":
            # haruno route. Note: majority of Yukino playthroughs (2/3) take this choice.
            # yui route
            stop music fadeout 1.0
            jump E3_G11_01
        "I want to go home already":
            # yukino route and iroha
            show iroha school_sunset far_left happy at center with dissolve:
                xoffset -25 yoffset 80
            "I looked over at Isshiki, who seemed to be busy getting things ready."
            hachiman "(Well, let's get the hell out of here. The longer we stick around, the more chores we'll be asked to do.)"
            stop music fadeout 1.0
            jump E3_G12_01

label E3_CMM_07:
    scene black with Fade(1.0, 0.5, 1.0)
    play sound "audio/sfx/SE04/SE04_01.ogg"
    scene classroomB
    with CropMove(0.5, mode="wiperight")
    play music "audio/bgm/BGM13.ogg"
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E3/CMM/07/SI/SI000.ogg"
    totsuka "Ah, Hachiman."
    window auto hide dissolve
    stop sound
    show totsukaClassroom with dissolve
    window auto show dissolve
    voice "audio/voice/E3/CMM/07/HA/HA000.ogg"
    hachiman "Oh, Totsuka. ...You're still here?"
    voice "audio/voice/E3/CMM/07/SI/SI001.ogg"
    totsuka "Yeah. The tennis club just finished their activies for today. What about you, Hachiman?"
    voice "audio/voice/E3/CMM/07/HA/HA001.ogg"
    hachiman "I was asked to help at the Prospective Career Path Program..."
    voice "audio/voice/E3/CMM/07/SI/SI002.ogg"
    totsuka "Ahaha... thanks for your work. That's gotta be though."
    voice "audio/voice/E3/CMM/07/HA/HA002.ogg"
    hachiman "Nah, it wasn't really a big deal."
    voice "audio/voice/E3/CMM/07/SI/SI003.ogg"
    totsuka "No, people are always relying on you, Hachiman. That's a lot of work in itself, but... you always do your very best."
    voice "audio/voice/E3/CMM/07/HA/HA003.ogg"
    hachiman "I don't feel like I'm doing a lot of work, though..."
    voice "audio/voice/E3/CMM/07/SI/SI004.ogg"
    totsuka "But you are! So many people are counting on you, and you always help them... You've helped me in the past too."
    voice "audio/voice/E3/CMM/07/HA/HA004.ogg"
    hachiman "I'm not doing anything, though. No, let me rephrase that--I haven't done anything."
    voice "audio/voice/E3/CMM/07/SI/SI005.ogg"
    totsuka "You know, Hachiman..."
    voice "audio/voice/E3/CMM/07/HA/HA005.ogg"
    hachiman "Hm?"
    voice "audio/voice/E3/CMM/07/SI/SI006.ogg"
    totsuka "Hachiman, when you're in trouble, you can rely on me... It's okay to rely on someone..."
    voice "audio/voice/E3/CMM/07/HA/HA006.ogg"
    hachiman "Totsuka..."
    voice "audio/voice/E3/CMM/07/SI/SI007.ogg"
    totsuka "I think there will be times when I will rely on you again. ...So that is why you can rely on me, too! ...Then I'll be able to walk beside with my head held high!"
    voice "audio/voice/E3/CMM/07/HA/HA007.ogg"
    hachiman "To rely one someone, to be relied on, so that we can stand together as equals... So that's how it is."
    voice "audio/voice/E3/CMM/07/SI/SI008.ogg"
    totsuka "Well, it's kind of hard to put into words, but not exactly. I don't think it's that hard to understand. This is just what I want to do. I want to be closer to you, Hachiman..."
    voice "audio/voice/E3/CMM/07/SI/SI009.ogg"
    totsuka "I think it's a wonderful thing to be able to get closer to someone."
    voice "audio/voice/E3/CMM/07/HA/HA008.ogg"
    hachiman "Getting closer to someone is bound to cause a lot of problems, though, isn't it?"
    voice "audio/voice/E3/CMM/07/SI/SI010.ogg"
    totsuka "But even so, it's a wonderful thing... I think so atleast."
    voice "audio/voice/E3/CMM/07/HA/HA009.ogg"
    hachiman "Is that so...?"
    voice "audio/voice/E3/CMM/07/SI/SI011.ogg"
    totsuka "It is!"
    "Of course, I haven't thought of deepening my bonds with someone. Although, after being forced to join the Service Club, there has certainly been a change."
    "The one who changed wasn't me, but everyone around me. It was almost as if by some force majeure that I became involved with people I should never have been involved with."
    "And what if I create some kind of bond with them? Going by what Totsuka said, I wonder if getting close to someone would be a wonderful thing for me, too."
    voice "audio/voice/E3/CMM/07/HA/HA010.ogg"
    hachiman "Maybe you're right..."
    voice "audio/voice/E3/CMM/07/SI/SI012.ogg"
    totsuka "Yeah. Trust me!"
    "Perhaps it truly is a wonderful thing..."
    stop music fadeout 1.0
#consider use some logic rather than menu? totsukaTalkFlag
#currently using this as a deciding flag for which route... probably not quite right.
#Taking all the yukino choices seems to result in choice between yui and yukino and maybe saki.
#For now default to Yukino if seemingly goes to yukino route.
    $points = _calculate_points()
    image hiratsuka_white = Flatten("hiratsuka school far_center happy")
    image meguri_white = Flatten("meguri school far happy")
    show white with Dissolve(1.0)
    if totsukaTalkFlag == "saki" and points['saki'] > 3:
        $saki_menu = True
        $yukino_menu = True
        show saki school_white far_right at center:
            xoffset -495 yoffset 75 alpha .6
        show yukino school_white far_center at center:
            xoffset 365 yoffset 75 alpha .6
        with dissolve
    elif totsukaTalkFlag == "iroha" and points['iroha'] > 3:
        $iroha_menu = True
        $saki_menu = True
        $yukino_menu = True
        show saki school_white far_right at left:
            xoffset 65 yoffset 75 alpha .6
        show yukino school_white far_center at center:
            xoffset -45 yoffset 75 alpha .6
        show iroha school_white far_center at right:
            xoffset -275 yoffset 75 alpha .6
        with dissolve
    elif totsukaTalkFlag == "hiratsuka" and points['hiratsuka'] > 3:
        $hiratsuka_menu = True
        $yukino_menu = True
        show hiratsuka_white at center:
            xoffset -395 yoffset 75 alpha .6
        show yukino school_white far_center at center:
            xoffset 365 yoffset 75 alpha .6
        with dissolve
    elif totsukaTalkFlag == "haruno" and points['haruno'] > 3 and harunoCafeFlag:
        $haruno_menu = True
        $yukino_menu = True
        show haruno sweater_white far_center at center:
            xoffset -425 yoffset 75 alpha .6
        show yukino school_white far_center at center:
            xoffset 365 yoffset 75 alpha .6
        with dissolve
    elif totsukaTalkFlag == "meguri" and points['meguri'] > 3 and harunoCafeFlag:
        $meguri_menu = True
        $yukino_menu = True
        show meguri_white at center:
            xoffset -400 yoffset 75 alpha .6
        show yukino school_white far_center at center:
            xoffset 365 yoffset 75 alpha .6
        with dissolve
    elif totsukaTalkFlag == "yui":
        $saki_menu = True
        $yui_menu = True
        $yukino_menu = True
        show saki school_white far_right at left:
            xoffset 75 yoffset 75 alpha .6
        show yui school_white far_center at center:
            xoffset -45 yoffset 75 alpha .6
        show yukino school_white far_center at right:
            xoffset -200 yoffset 75 alpha .6
    else:
        jump E3_CMM_07_YUK
    menu totSak_menu:
        with dissolve
        # this isn't completely like the transition
        hachiman "(There's no doubt it's...)"
        "Forming bonds with family and such" if saki_menu:
            $totsukaTalkFlag = "saki"
            #This will be the Valentine Chocolate Event scene (E
            hide saki
            hide yukino
            hide iroha
            with dissolve
            show saki school mid_right happy at center with Dissolve(1.0):
                xoffset -115 yoffset 75
            window auto show dissolve
            hachiman "(There's also forming bonds with family and such... Within that awkward behavior of hers, there lies a certain warmth.)"
            window auto hide dissolve
            hide saki with Dissolve(1.0)
            $renpy.pause(delay=2.0, hard=True)
            jump E3_SAK_03
        "What I've been taught all along" if hiratsuka_menu:
            $totsukaTalkFlag = "hiratsuka"
            hide hiratsuka_white
            hide yukino
            with dissolve
            show hiratsuka school mid_center happy at center with dissolve:
                xoffset 40 yoffset 75
            hachiman "(Perhaps it's what she's always teaching me.)"
            hachiman "(She made me a part of the Service Club and cared for me in all sorts of ways. Trying to make something of me, she always struggled and worried for my sake.)"
            window auto hide dissolve
            hide hiratsuka with Dissolve(1.0)
            $renpy.pause(delay=2.0, hard=True)
            jump E3_G10_01
        "A sunlike warmth" if meguri_menu:
            $totsukaTalkFlag = "meguri"
            hide yukino
            hide meguri_white
            with dissolve
            show meguri school mid happy at center with dissolve:
                xoffset 25 yoffset 75
            hachiman "(It has to be a warmth like the sun. Somewhere where just being present soothes you and makes you feel warm inside. It would be nice to have something like that.)"
            window auto hide dissolve
            hide meguri with Dissolve(1.0)
            $renpy.pause(delay=2.0, hard=True)
            jump E3_HAR_05
        "With a warmth that resembles sunshine" if haruno_menu:
            $totsukaTalkFlag = "haruno"
            hide yukino
            hide haruno
            with dissolve
            show haruno sweater mid_center at center with Dissolve(1.0):
                xoffset 10 yoffset 75
            window auto show dissolve
            hachiman "(A warmth similar to sunshine.... Which will expose everything under it to it's sunlight, drying up anything caught by it's severe illumination.)"
            hachiman "(Because it's so bright, the wisdom is hidden in a darkness so deep beneath the surface, I could never reach it. Maybe that's why I'm straining so hard to see it.)"
            window auto hide dissolve
            hide haruno with Dissolve(1.0)
            $renpy.pause(delay=2.0, hard=True)
            jump E3_HAR_04
        "Understanding more about each other" if yukino_menu:
            $totsukaTalkFlag = "yukino"
            hide saki
            hide haruno
            hide yukino
            hide yui
            hide iroha
            hide hiratsuka_white
            hide meguri_white
            with dissolve
            jump E3_CMM_07_YUK
        "It's like it's made of sugar and spice" if iroha_menu:
            $totsukaTalkFlag = "iroha"
            hide saki
            hide yukino
            hide iroha
            with dissolve
            show iroha school mid_center happy at center with Dissolve(1.0):
                xoffset -5 yoffset 75
            window auto show dissolve
            hachiman "(That's right, it must be a lovely thing made of sugar and spice. Slightly bitter and numbing, but just the right amount of sweet, with hidden flavors that keep you coming back.)"
            window auto hide dissolve
            hide iroha with Dissolve(1.0)
            $renpy.pause(delay=2.0, hard=True)
            jump E3_IRO_08
        "What we call kindness" if yui_menu:
            $totsukaTalkFlag = "yui"
            hide saki
            hide yui
            hide yukino
            with dissolve
            show yui school mid_center happy at center with Dissolve(1.0):
                xoffset -5 yoffset 75
            window auto show dissolve
            hachiman "(It's definitely something I would call kindness, but a kindness I always find excuses to run away from. If only I can get closer to that kindness, though, I might start calling it something else.)"
            window auto hide dissolve
            hide yui with Dissolve(1.0)
            $renpy.pause(delay=2.0, hard=True)
            scene black with Fade(1.0, 0.5, 1.0)
            jump E3_YUI_09

label E3_CMM_07_YUK:
    show yukino school mid_center happy at center with Dissolve(1.0):
        xoffset -105 yoffset 75
    window auto show dissolve
    hachiman "(I hadn't known, but she'd said the same thing. However, I know now. I want to know and understand more than anything to the point I was being horribly egocentric.)"
    hachiman "(Like that I'd been taking one step forward and two steps back, and while exploring the place I could step into, the distance between us would shorten.)"
    window auto hide dissolve
    hide yukino with Dissolve(1.0)
    $renpy.pause(delay=2.0, hard=True)
    jump E3_YUK_03

label E3_CMM_08:
    scene houseA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM34.ogg"
    window auto show dissolve
    voice "audio/voice/E3/CMM/08/HA/HA000.ogg"
    hachiman "...Ahhhh."
    hachiman "(Holidays are great... I wake up earliest on Sundays... I only bother to work hard all week just for this moment where I get to be soothed by Pretty Rhythm in front of the TV...)"
    hachiman "(The freedom to just enjoy anime like this. This is the proof that I've finally returned to my calm everyday life.)"
    if hayamaMarathonTalk == True:
        "Through that marathon, the gossip issue and Miura's wanting to know about Hayama's career were both resolved in one go."
        "When it's all said and done, it was all too abrupt and anticlimactic."
    else:
        window auto hide dissolve
        scene bridgeA
        show hayama athletic near_right pout at center:
            xoffset -25 yoffset 70
        with Fade(0.25,0.35, 0.5, color="#fff")
        window auto show dissolve
        "I'd made a situation where I could put pressure on Hayama during the Marathon Tournament and I somehow managed to determine his future course intentions."
        window auto hide dissolve
        scene parkB
        show hayama athletic_sunset far_center vhappy at center:
            xoffset -10 yoffset 75
        with Fade(0.25,0.35, 0.5, color="#fff")
        window auto show dissolve
        "As for the gossip, Hayama thanked Miura and Isshiki at the podium, as he had said he would settle it himself, and the rumor was put to rest."
        window auto hide dissolve
        scene houseA with Fade(0.25,0.35, 0.5, color="#fff")
        window auto show dissolve

    voice "audio/voice/E3/CMM/08/HA/HA001.ogg"
    hachiman "Ah, I'm tired for some reason. Sundays are great... Can't it be Sunday tomorrow too..."
    $url = ["komachi athletic mid_center happy", "komachi athletic mid_center pout"]
    $multiImagePara = [-75, 75, 0, 0, 2.4]
    call multiImage() from _call_multiImage_28
    play music ["<silence 2.4>", "<to 0.1>audio/bgm/BGM34.ogg"] noloop
    voice "audio/voice/E3/CMM/08/KO/KO000.ogg"
    komachi "Onii-chan, it's time for lunch-- Ah..."
    call finishmultiImage from _call_finishmultiImage_29
    stop music
    show komachi athletic mid_center pout at center:
        xoffset -75 yoffset 75
    voice "audio/voice/E3/CMM/08/HA/HA002.ogg"
    hachiman "Ah?"
    play music "audio/bgm/BGM44.ogg"
    show komachi unimpressed with dissolve
    voice "audio/voice/E3/CMM/08/KO/KO001.ogg"
    komachi "Hey, what are you doing watching anime intended for girls in the morning with such rotten eyes?"
    voice "audio/voice/E3/CMM/08/HA/HA003.ogg"
    hachiman "You're wrong there, Komachi. This anime isn't only for girls, it's also targeted towards big fans like me. So you can't say this is exclusively intended for girls. I'm well-versed in this."
    show komachi pout with dissolve
    voice "audio/voice/E3/CMM/08/KO/KO002.ogg"
    komachi "S-sure... Onii-chan, you really are gross."
    voice "audio/voice/E3/CMM/08/HA/HA004.ogg"
    hachiman "What's more, someone like me is totally normal. I'm not like those rabid fans would go to the theater to watch this and even to events at the mall."
    show komachi athletic mid_left unimpressed at center with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E3/CMM/08/KO/KO003.ogg"
    komachi "Things is, those \"rabid fans\" sound much more normal to me, though."
    show komachi happy with dissolve
    voice "audio/voice/E3/CMM/08/KO/KO004.ogg"
    komachi "Ah, right. Anyway, it's lunchtime. You were saying such gross stuff, the food's gone cold, just like Komachi's affection."
    voice "audio/voice/E3/CMM/08/HA/HA005.ogg"
    hachiman "Eh, that's a problem. Warm it up, please?"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    scene houseA
    show komachi athletic mid_center vhappy at center:
        xoffset -75 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM10.ogg"
    window auto show dissolve
    voice "audio/voice/E3/CMM/08/KO/KO005.ogg"
    komachi "Alright, thank you for the food!"
    voice "audio/voice/E3/CMM/08/HA/HA006.ogg"
    hachiman "Thank you for the food. Warm food is great."
    show komachi happy with dissolve
    voice "audio/voice/E3/CMM/08/KO/KO006.ogg"
    komachi "Yeah. I'm glad we warmed the food up."
    voice "audio/voice/E3/CMM/08/HA/HA007.ogg"
    hachiman "Y-yeah..."
    hachiman "(Wait, I can feel heartwarming affection from this food, you know? Oh crap, I'm getting sleepy... I need to communicate or I'll dose off.)"
    voice "audio/voice/E3/CMM/08/HA/HA008.ogg"
    hachiman "Ah... Are you going to cram school today?"
    hide komachi
    $url = ["komachi athletic mid_center vhappy", "komachi athletic mid_center pout"]
    $multiImagePara = [-75, 75, 0, 0, 4.4]
    call multiImage() from _call_multiImage_29
    voice "audio/voice/E3/CMM/08/KO/KO007.ogg"
    komachi "Nah, it's on break. It's been forever since I could rest on a Sunday! Though I need to study anyway."
    call finishmultiImage from _call_finishmultiImage_30
    show komachi athletic mid_center pout at center:
        xoffset -75 yoffset 75
    voice "audio/voice/E3/CMM/08/HA/HA009.ogg"
    hachiman "I see. Well, resting is important, too. Study in moderation."
    show komachi happy with dissolve
    voice "audio/voice/E3/CMM/08/KO/KO008.ogg"
    komachi "Yeah, will do."
    stop voice
    play sound "audio/sfx/SE01/SE01_16.ogg"
    show komachi angry with dissolve
    voice "audio/voice/E3/CMM/08/KO/KO009.ogg"
    komachi "It rah u shi a e resh oh tei."
    voice "audio/voice/E3/CMM/08/HA/HA010.ogg"
    hachiman "I have no idea what you're trying to say. Swallow what you're eating first."
    hide komachi
    $url = ["komachi athletic mid_center happy", "komachi athletic mid_center pout"]
    $multiImagePara = [-75, 75, 0, 0, 4.4]
    call multiImage() from _call_multiImage_30
    voice "audio/voice/E3/CMM/08/KO/KO010.ogg"
    komachi "Hm... It's rare for you be so relaxed. Huh? Oh, it's not that it's rare, it's just that recently you seemed so busy."
    call finishmultiImage from _call_finishmultiImage_31
    show komachi athletic mid_center pout at center:
        xoffset -75 yoffset 75
    voice "audio/voice/E3/CMM/08/HA/HA011.ogg"
    hachiman "Hmmm, yeah, I was. The job's over and done with, though."
    show komachi surprised with dissolve
    voice "audio/voice/E3/CMM/08/KO/KO011.ogg"
    komachi "Why were you that busy?"
    voice "audio/voice/E3/CMM/08/HA/HA012.ogg"
    hachiman "I wonder why. Just went with the flow."
    show komachi angry with dissolve
    voice "audio/voice/E3/CMM/08/KO/KO012.ogg"
    komachi "Going with the flow..."
    # might become e3/sak/04 or 05 here
    hachiman "(Now that I think about it, it is true. I wonder why.)"
    # biyte working on yukino route here, seems a branch occur here. Making new label using a flag I set at end of E3_YUK_02 (stuff with student council, and haruno ambush),
    if totsukaTalkFlag == "yukino":
        jump E3_CMM_08_YUK
    elif totsukaTalkFlag == "saki":
        jump E3_CMM_08_SAK
    else:
        voice "audio/voice/E3/CMM/08/HA/HA013.ogg"
        hachiman "...Yep, I really don't know."
        show komachi happy with dissolve
        voice "audio/voice/E3/CMM/08/KO/KO013.ogg"
        komachi "Ah, I see."
        voice "audio/voice/E3/CMM/08/HA/HA014.ogg"
        hachiman "But, hey, we managed somehow, so that's good, right?"
        show komachi unimpressed with dissolve
        voice "audio/voice/E3/CMM/08/KO/KO014.ogg"
        komachi "That's the most \"you\" thing I think I've ever heard, onii-chan...."
        window auto hide dissolve
        stop voice
        call loading_screen(duration="short") from _call_loading_screen_19
        jump E4_CMM_01

label E3_CMM_08_YUK:
    voice "audio/voice/E3/CMM/08/HA/HA015.ogg"
    hachiman "It's just that. I was just doing stuff here and there for the Service Club."
    show komachi happy with dissolve
    voice "audio/voice/E3/CMM/08/KO/KO015.ogg"
    komachi "Well whatever. Komachi reckons it's good if you stay active anyway."
    voice "audio/voice/E3/CMM/08/HA/HA016.ogg"
    hachiman "Really?"
    show komachi vhappy with dissolve
    voice "audio/voice/E3/CMM/08/KO/KO016.ogg"
    komachi "Yep. The sister-in-law plan can also go into action..."
    hachiman "(I don't like this, Komachi's eyes are sparkling mischievously...)"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    jump E3_YUK_04

#saki route
label E3_CMM_08_SAK:
    hachiman "(No, I don't know why... I'm afraid I can't put it into words that well... If I were to try and explain, I'd have to go on and on...)"
    voice "audio/voice/E3/CMM/08/HA/HA019.ogg"
    hachiman "Say, Komachi."
    show komachi surprised with dissolve
    voice "audio/voice/E3/CMM/08/KO/KO019.ogg"
    komachi "Hm?"
    voice "audio/voice/E3/CMM/08/HA/HA020.ogg"
    hachiman "When you finish eating, can you listen to me for a moment?"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    jump E3_SAK_05
