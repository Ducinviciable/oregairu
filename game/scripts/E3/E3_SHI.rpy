label E3_SHI_01:
    scene skyA with dissolve
    play music "audio/bgm/BGM46.ogg"
    window auto show dissolve
    "The classroom was filled with chatter about the career courses. In the midst of it, you could hear gossip about Hayama and Yukinoshita here and there."
    "I felt irritated about everything. I'm depressed about the unseemly exchanges in class and most of all - by the fact that I can't just ignore them like I used to."
    "I can't say I really had anything to do with it, and I can't do anyhting about it. It all really just reminded me of how half-baked I am."
    window auto hide dissolve
    scene hallwayA with dissolve
    window auto show dissolve
    hachiman "(Ah~ It's so nice and quiet here.)"
    "I stared blankly at the scenery through the window of the corridor, but I still didn't feel any better."
    window auto hide dissolve
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
    window auto show dissolve
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E3/SHI/01/HA/HA000.ogg"
    hachiman "..."
    hachiman "(Recess has never really felt this long... I should be thankful about that, I guess.)"
    voice "audio/voice/E3/SHI/01/SZ/SZ000.ogg"
    hiratsuka "Ah, well if it isn't Hikigaya... What's gotten you so down?"
    window auto hide dissolve
    stop voice
    scene hallwayA
    show hiratsuka school mid_center pout at center:
        xoffset 40 yoffset 75
    with wipeleft
    window auto show dissolve
    "When I turned around, I saw Hiratsuka-sensei standing there, peering at my expression quizzically, but I quickly looked away because I felt she could see through me."
    voice "audio/voice/E3/SHI/01/HA/HA001.ogg"
    hachiman "Nothing really..."
    show hiratsuka unimpressed with dissolve
    voice "audio/voice/E3/SHI/01/SZ/SZ001.ogg"
    hiratsuka "Well, I guess it's not exactly a cause for concern to see you by yourself."
    voice "audio/voice/E3/SHI/01/HA/HA002.ogg"
    hachiman "...It gets pretty ugly when you gather people together."
    hachiman "(I let my true opinion slip out. It sounded like I'm whining, which was embarasing.)"
    show hiratsuka happy with dissolve
    voice "audio/voice/E3/SHI/01/SZ/SZ002.ogg"
    hiratsuka "\"Ugly\"... Well, it's very different when looking at it as an outsider and actually participating in it."
    voice "audio/voice/E3/SHI/01/SZ/SZ003.ogg"
    hiratsuka "Individuals are one thing, but take a group of individuals and we can't really know what they're thinking. It can be uncanny."
    voice "audio/voice/E3/SHI/01/HA/HA003.ogg"
    hachiman "Well, you might be right. I wouldn't know."
    "She always gets right to the point, doesn't she? In short, I guess I just don't really know what to make of it. The rumors about Yukinoshita and Hayama are affecting me more than I thought."
    show hiratsuka sad with dissolve
    voice "audio/voice/E3/SHI/01/SZ/SZ004.ogg"
    hiratsuka "I've heard about the Yukinoshita/Hayama rumors. Well, it's them we're talking about, so I figure there's no reason to be concerned."
    voice "audio/voice/E3/SHI/01/HA/HA004.ogg"
    hachiman "Well, you're right about that."
    "Surprisingly, Hiratsuka-sensei didn't ask me to step in. Maybe she's concerned about me in her own way."
    show hiratsuka happy with dissolve
    voice "audio/voice/E3/SHI/01/SZ/SZ005.ogg"
    hiratsuka "That doesn't mean however that a certain someone isn't hurting. I won't say who. I hope you'll watch over them."
    voice "audio/voice/E3/SHI/01/HA/HA005.ogg"
    hachiman "Well, it's not like I can do much else besides that."
    voice "audio/voice/E3/SHI/01/SZ/SZ006.ogg"
    hiratsuka "Actually, that one thing is the most important thing you can do."
    voice "audio/voice/E3/SHI/01/HA/HA006.ogg"
    hachiman "Is it really?"
    show hiratsuka mid_left happy with dissolve:
        xoffset 110 yoffset 80
    voice "audio/voice/E3/SHI/01/SZ/SZ007.ogg"
    hiratsuka "It absolutely is. Come on, next class is about to start. Get back inside."
    voice "audio/voice/E3/SHI/01/HA/HA007.ogg"
    hachiman "...Right."
    stop music fadeout 0.5
    hide hiratsuka with dissolve
    "Saying that, Hiratsuka-sensei walked gallantly past me and down the hallway, waving her hand."
    play music "audio/bgm/BGM32.ogg"
    "That exchange was much the same as usual, but strangely, I found myself feeling more at ease than before."
    "Perhaps it was because I felt like I had discovered a new option where I had been stuck going only back and forth."
    hachiman "(Watch over her, huh...)"
    window auto hide dissolve
    $renpy.pause(delay=0.5,hard=True)
    stop music fadeout 0.5
    call loading_screen(26, "26") from _call_loading_screen_28
    jump E3_G09_01

label E3_SHI_02:
    scene black with Fade(1.0, 0.5, 0)
    play sound "audio/sfx/SE04/SE04_08.ogg"
    scene staffroomA with Fade(0, 0, 1.0)
    show hiratsuka school mid_center happy at center with dissolve:
        xoffset 40 yoffset 75
    $renpy.pause(delay=0.25,hard=True)
    stop sound
    play music "audio/bgm/BGM26.ogg"
    window auto show dissolve
    voice "audio/voice/E3/SHI/02/SZ/SZ000.ogg"
    hiratsuka "Thanks. Leave it here for me."
    "As I delivered the printouts for the career counseling, as Hiratska-sensei had asked me to, she put down her chopsticks next to the katsdon and tempura in the staff room. I wonder if she's going to eat "
    "both of them..."
    show hiratsuka angry with dissolve
    voice "audio/voice/E3/SHI/02/SZ/SZ001.ogg"
    hiratsuka "Hikigaya, you wrote a serious answer this time, I hope?"
    voice "audio/voice/E3/SHI/02/HA/HA000.ogg"
    hachiman "W-Who knows..."
    voice "audio/voice/E3/SHI/02/SZ/SZ002.ogg"
    hiratsuka "Is that so. Then let me change the question. Do you still want to be a stay-at-home husband?"
    voice "audio/voice/E3/SHI/02/HA/HA001.ogg"
    hachiman "Dunno... Maybe I do? In the distant future, such prospects are only vague concepts..."
    show hiratsuka annoyed with dissolve
    voice "audio/voice/E3/SHI/02/SZ/SZ003.ogg"
    hiratsuka "I'd like to ask you, do you think there are potentially many men in the world who have such desire to be provided for?"
    voice "audio/voice/E3/SHI/02/HA/HA002.ogg"
    hachiman "Huh?"
    show hiratsuka surprised with dissolve
    voice "audio/voice/E3/SHI/02/SZ/SZ004.ogg"
    hiratsuka "No, well... Simply in terms of the common populace, er... Just in general, I wanted to know if you think having a stable income is... desirable? We're speaking in generalities of course."
    voice "audio/voice/E3/SHI/02/HA/HA003.ogg"
    hachiman "Right, of course! We're just talking in broad terms, right? It's a general thing, nothing to do with your personal wishes or circumstances at all, right?"
    hachiman "(I'm afraid I can see the seriousness in your question...)"
    voice "audio/voice/E3/SHI/02/HA/HA004.ogg"
    hachiman "In general, I think it's desirable for women to have a stable income, in this age of gender eqality!"
    show hiratsuka happy with dissolve
    voice "audio/voice/E3/SHI/02/SZ/SZ005.ogg"
    hiratsuka "I see. It really is, isn't it? Yeah, of course it would. Yes! It is~~~!"
    window auto hide dissolve
    stop voice
    hide hiratsuka with dissolve
    play sound "audio/sfx/SE01/SE01_13.ogg"
    show hiratsukastaffrooma with dissolve
    window auto show dissolve
    voice "audio/voice/E3/SHI/02/SZ/SZ006.ogg"
    hiratsuka "Be that as it may, I don't want your dream to be being a \"full-time husband\", so I hope you're putting in legitimate thought this time."
    voice "audio/voice/E3/SHI/02/HA/HA005.ogg"
    hachiman "Y-Yeah, I will. Well, to begin with, it depends on my would be partner. I can't do it if I'm single."
    voice "audio/voice/E3/SHI/02/SZ/SZ007.ogg"
    hiratsuka "Can or can I not take that as a cheeky quip directed at me...?"
    "I've been careless. While I've been trying to argue my case like a sore loser, before I knew it, I stepped on the biggest landmine of them all."
    voice "audio/voice/E3/SHI/02/HA/HA006.ogg"
    hachiman "N-No, that's not what I meant at all!"
    stop music fadeout 1.0
    voice "audio/voice/E3/SHI/02/SZ/SZ008.ogg"
    hiratsuka "If only I had a partner... In order to find a partner... Spouse hunting?"
    hachiman "(Oh no, Hiratsuka-sensei is about to completely fall to the dark side!)"
    show hiratsukastaffroomb with dissolve
    $renpy.pause(delay=0.5,hard=True)
    play music "audio/bgm/BGM16.ogg"
    voice "audio/voice/E3/SHI/02/SZ/SZ009.ogg"
    hiratsuka "Then I, as the life guidance counselor and advisor of your club's activities, must help."
    voice "audio/voice/E3/SHI/02/HA/HA007.ogg"
    hachiman "Come again?"
    voice "audio/voice/E3/SHI/02/SZ/SZ010.ogg"
    hiratsuka "If you want to be a full-time husband, then housework is an essential skill! This is a good oportunity for me to polish it up."
    voice "audio/voice/E3/SHI/02/HA/HA008.ogg"
    hachiman "No, what does that even..."
    voice "audio/voice/E3/SHI/02/SZ/SZ011.ogg"
    hiratsuka "Don't worry. Leave it to me! You're in safe hands."
    voice "audio/voice/E3/SHI/02/SZ/SZ012.ogg"
    hiratsuka "For the sake of the students, I have no choice. I have to do my utmost for you as a student and give you real-world expirince. There's no harm in honing your cooking skills to appeal to men-- I mean, for being "
    voice sustain
    hiratsuka "a full-time househusband, right?"
    hachiman "(I don't know why she's doing this for me... Or, so I should ask, but she's doing this for herself, isn't she?)"
    window auto hide dissolve
    $renpy.pause(delay=0.5,hard=True)
    show hiratsuka school near_center vhappy at center:
        xoffset 30 yoffset 75
    play sound "audio/sfx/SE01/SE01_00.ogg"
    hide hiratsukastaffrooma
    hide hiratsukastaffroomb
    with dissolve
    window auto show dissolve
    voice "audio/voice/E3/SHI/02/SZ/SZ013.ogg"
    hiratsuka "Well, let's strike while the iron's hot! Let's get started right away!"
    voice "audio/voice/E3/SHI/02/HA/HA009.ogg"
    hachiman "Hold on a se--"
    hachiman "(I feel like I've switched on her \"motivation switch\" which one should never do...)"
    window auto hide dissolve
    stop music fadeout 0.5
    jump E3_SHI_03

label E3_SHI_03:
    scene kitchenA
    show hiratsuka school mid_center angry at center:
        xoffset 40 yoffset 75
    show yukino school mid_center happy at left behind hiratsuka:
        xoffset -100 yoffset 75
    show yui school mid_center happy at right behind hiratsuka:
        xoffset -175 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM29.ogg"
    window auto show dissolve
    "Hiratsuka-sensei took me to the Home EC room half by force. For some reason, Yukinoshita and Yuigahama were also there."
    voice "audio/voice/E3/SHI/03/SZ/SZ000.ogg"
    hiratsuka "So, we'll be giving Hikigaya career guidance. He wants to be a stay-at-home husband. I'm going to beat the skills of a housewife into him, so I'd appreciate your help."
    voice "audio/voice/E3/SHI/03/YK/YK000.ogg"
    yukino "Could I take this as a part of the Service Club's activities?"
    show hiratsuka mid_left happy with dissolve:
        xoffset 110 yoffset 80
    voice "audio/voice/E3/SHI/03/SZ/SZ001.ogg"
    hiratsuka "Yes, you can think of it like that."
    show yukino vhappy with dissolve
    voice "audio/voice/E3/SHI/03/YK/YK001.ogg"
    yukino "If that's the case, we'll help."
    hachiman "(Hiratsuka-sensei just wants to learn how to cook for men's approval, though...)"
    window auto hide dissolve
    scene black with dissolve
    window auto show dissolve
    "And so, using me as a front, Sensei's homemaking-training cooking class began."
    window auto hide dissolve
    scene kitchenA with dissolve
    show yukino school mid_center happy at center with dissolve:
        xoffset -105 yoffset 75
    window auto show dissolve
    voice "audio/voice/E3/SHI/03/YK/YK002.ogg"
    yukino "It's not easy to make a person unfit for society like yourself into a full-fledged househusband, but... It might be worthwhile in the end."
    hachiman "(But if I'm a stay-at-home husband, I don't need to be a part of society, do I...)"
    hide yukino with dissolve
    show yui school mid_center happy at left:
        xoffset 255 yoffset 75
    show hiratsuka school mid_left angry at right:
        xoffset -20 yoffset 80
    with dissolve
    voice "audio/voice/E3/SHI/03/YI/YI000.ogg"
    yui "So, what should I do?"
    show hiratsuka happy with dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ002.ogg"
    hiratsuka "I'd like you to support Hikigaya. I'm sure doing it on his lonesome will feel disheartning. Besides, this will be good for you, too. It'll be like a bridal training course."
    show yui vhappy with dissolve
    voice "audio/voice/E3/SHI/03/YI/YI001.ogg"
    yui "Bridal training, huh...? O-Okay, now I'm feeling pumped! Let's do this, Hikki~!"
    voice "audio/voice/E3/SHI/03/HA/HA000.ogg"
    hachiman "R-Right."
    hachiman "(Why are you so excited about this...)"
    hide yui
    hide hiratsuka
    with dissolve
    show yukino school mid_center happy at left behind hiratsuka:
        xoffset -100 yoffset 75
    show yui school mid_center vhappy at center:
        xoffset -25 yoffset 75
    show hiratsuka school mid_left happy at right:
        xoffset 110 yoffset 80
    with dissolve
    voice "audio/voice/E3/SHI/03/HA/HA001.ogg"
    hachiman "So, what are we going to make specifically?"
    show hiratsuka mid_center happy with dissolve:
        xoffset 100 yoffset 80
    voice "audio/voice/E3/SHI/03/SZ/SZ003.ogg"
    hiratsuka "Well, something that will appeal to m-- I mean, something family-oriented right?"
    show yukino stare with dissolve
    voice "audio/voice/E3/SHI/03/YK/YK003.ogg"
    yukino "Well then, firstly we'll cook rice and... There's an obvious gap in time there that is wasted. While it's cooking, we'll make a miso soup and something light... Right, how about grilled seasonal fish?"
    show yui happy with dissolve
    voice "audio/voice/E3/SHI/03/YI/YI002.ogg"
    yui "That sounds delicious!"
    hide hiratsuka
    $url = ["hiratsuka school mid_left happy", "hiratsuka school mid_left sad"]
    $multiImagePara = [110, 80, 0, 0, 3.0]
    call multiImage(1) from _call_multiImage_82
    voice "audio/voice/E3/SHI/03/SZ/SZ004.ogg"
    hiratsuka "As expected of Yukinoshita. \"That's the one!\"... Or so I wanted to say, but I've only brought ingredients that would be fit for a beginner like Hikigaya."
    call finishmultiImage from _call_finishmultiImage_86
    show hiratsuka school mid_left sad at right:
        xoffset 110 yoffset 80
    show yukino happy with dissolve
    voice "audio/voice/E3/SHI/03/YK/YK004.ogg"
    yukino "I see... So, what kind of ingredients have you brought?"
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ005.ogg"
    hiratsuka "Ha-ha-ha."
    show hiratsuka mid_center happy at right with dissolve:
        xoffset 100 yoffset 80
    play sound "audio/sfx/SE01/SE01_64.ogg"
    "With that, Hiratsuka-sensei smiled triumphantly and dropped a supermarket bag full of food stuff on the table."
    play sound "audio/sfx/SE01/SE01_09.ogg"
    $renpy.pause(delay=1.25, hard=False)
    show yui pout with dissolve
    voice "audio/voice/E3/SHI/03/YI/YI003.ogg"
    yui "Let's see... Carrots, potatoes, onions and meat...?"
    show yukino stare with dissolve
    voice "audio/voice/E3/SHI/03/YK/YK005.ogg"
    yukino "This really is basic. With this, we can make curry or stew... Maybe croquettes if we really wanted to."
    show yui vhappy with dissolve
    voice "audio/voice/E3/SHI/03/YI/YI004.ogg"
    yui "Ah! Yes, please! I want to have curry!"
    voice "audio/voice/E3/SHI/03/HA/HA002.ogg"
    hachiman "Curry, huh? True, it's basic, but you can always put your own spin on it."
    show yukino happy with dissolve
    voice "audio/voice/E3/SHI/03/YK/YK006.ogg"
    yukino "Yes, as we'll have you demonstrate now."
    voice "audio/voice/E3/SHI/03/HA/HA003.ogg"
    hachiman "Huh?"
    hide yukino
    hide yui
    hide hiratsuka
    with dissolve
    show hiratsuka school near_center annoyed at center with dissolve:
        xoffset 30 yoffset 75
    voice "audio/voice/E3/SHI/03/SZ/SZ006.ogg"
    hiratsuka "What are you shocked about? What's a stay-at-home husband if he can't do a single chore? Surely you didn't think you could just laze around without doing anything?"
    play sound "audio/sfx/SE02/SE02_12.ogg"
    hachiman "(The aura eminating from sensei right now is terrifying!)"
    voice "audio/voice/E3/SHI/03/HA/HA004.ogg"
    hachiman "W-Well, I'd like to learn a bit, too... To help Komachi and all..."
    show hiratsuka happy with dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ007.ogg"
    hiratsuka "Good answer. Now then, let's get started with the rice..."
    window auto hide dissolve
    stop voice
    hide hiratsuka with dissolve
    stop music fadeout 0.5
    show kitchenA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM30.ogg"
    $renpy.pause(delay=0.5, hard=False)
    play sound "audio/sfx/SE01/SE01_17.ogg"
    $renpy.pause(delay=0.5, hard=False)
    window auto show dissolve
    "Under the watchful eye of Hiratsuka-sensei and the strict guidance of Yukinoshita, Yuigahama and I grappled with our knives."
    stop sound fadeout 0.5
    show yukino school mid_center angry at left:
        xoffset 25 yoffset 75
    show yui school mid_center sad at right:
        xoffset -305 yoffset 75
    with dissolve
    voice "audio/voice/E3/SHI/03/YI/YI005.ogg"
    yui "Yukinon~, can I please use a peeler for the potatoes~?"
    voice "audio/voice/E3/SHI/03/YK/YK007.ogg"
    yukino "No, you can't. It's simple taking the easy way out, but we ought not to."
    hide yukino
    hide yui
    with dissolve
    play sound "audio/sfx/SE01/SE01_69.ogg"
    voice "audio/voice/E3/SHI/03/HA/HA005.ogg"
    hachiman "Slice upwards, slice upwards, slice upwards..."
    hachiman "(Why are onions so slippery and why do they sting my eyes like this!?)"
    stop sound fadeout 1.0
    show yukino school mid_center angry at left behind hiratsuka:
        xoffset -100 yoffset 75
    show yui school mid_center sad at center:
        xoffset -25 yoffset 75
    show hiratsuka school mid_left happy at right:
        xoffset 110 yoffset 80
    with dissolve
    voice "audio/voice/E3/SHI/03/YK/YK008.ogg"
    yukino "As for the pork... Right, it's best I deal with it."
    voice "audio/voice/E3/SHI/03/SZ/SZ008.ogg"
    hiratsuka "Aren't you going awfully easy on them, Yukinoshita?"
    voice "audio/voice/E3/SHI/03/YK/YK009.ogg"
    yukino "Pork becomes unsanitary if you fumble about with it and I'm wary of germs, so..."
    voice "audio/voice/E3/SHI/03/YI/YI006.ogg"
    yui "She wasn't going easy, she just had zero faith in us!?"
    show yukino vhappy with dissolve
    voice "audio/voice/E3/SHI/03/YK/YK010.ogg"
    yukino "Yuigahama-san, if you really want to, I'm more than willing to teach you."
    voice "audio/voice/E3/SHI/03/YI/YI007.ogg"
    yukino "Uw... Yukino, you're too nice, it's scary..."
    show yukino angry with dissolve
    voice "audio/voice/E3/SHI/03/YK/YK011.ogg"
    yukino "Now then, Hikigaya-kun, use your judgement and pour enough oil into-- No, pour it into the bowl until I say \"stop\", and let's fry those onions. As for Yuigahama..."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    show black with dissolve
    window auto show dissolve
    "As we were following instructions, Yuigahama and I had less and less time to ask questions. And, as we finally got all the ingredients in the pot, it started to make a simmering sound."
    window auto hide dissolve
    hide black
    show yukino happy
    show yui angry
    with dissolve
    play sound "audio/sfx/SE01/SE01_73.ogg"
    window auto show dissolve
    voice "audio/voice/E3/SHI/03/YK/YK012.ogg"
    yukino "After letting it simmer for a while, I'd like to make my own curry powder, but... This time, we'll use a store-bought one. Just add it in, and we're done."
    hachiman "(You can make your own curry powder?)"
    stop sound
    voice "audio/voice/E3/SHI/03/SZ/SZ009.ogg"
    hiratsuka "Well, we're still in the midst of cooking the rice, so we'll take a break after."
    play music "audio/bgm/BGM33.ogg"
    $renpy.pause(delay=0.5, hard=False)
    show yui sad with dissolve
    voice "audio/voice/E3/SHI/03/YI/YI008.ogg"
    yui "I'm so tired~!"
    voice "audio/voice/E3/SHI/03/HA/HA006.ogg"
    hachiman "Cooking is such a pain..."
    show yukino vhappy with dissolve
    voice "audio/voice/E3/SHI/03/YK/YK013.ogg"
    yukino "Well, I suggest you get used to it."
    voice "audio/voice/E3/SHI/03/HA/HA007.ogg"
    hachiman "Like hell I can..."
    "I was deeply moved, thinking \"Komachi, you've been working so hard inbetween your exams!\""
    show hiratsuka mid_center with dissolve:
        xoffset 105 yoffset 80
    voice "audio/voice/E3/SHI/03/SZ/SZ010.ogg"
    hiratsuka "Well, it's not like I'm just gonna sit here and wait for it to boil. Let's brush up some basics."
    stop music fadeout 0.5
    voice "audio/voice/E3/SHI/03/HA/HA008.ogg"
    hachiman "Eh, there's more...?"
    window auto hide dissolve
    stop voice
    $renpy.pause(delay=0.25, hard=False)
    scene kitchenA
    hide yui
    hide yukino
    hide hiratsuka
    show hiratsuka school near_center annoyed at center:
        xoffset 30 yoffset 75
    play sound "audio/sfx/SE02/SE02_10.ogg"
    with Fade(0.1, 0.2, 0.2, color="#fff")
    play music "audio/bgm/BGM16.ogg"
    $renpy.pause(delay=0.5, hard=False)
    window auto show dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ011.ogg"
    hiratsuka "The most important thing in cooking is... Love! Also known as, passion! In other words, fervor!"
    show hiratsuka happy with dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ012.ogg"
    hiratsuka "Will you be able to answer my questions?"
    hachiman "(She really does have some kind of switch in her...)"
    show hiratsuka angry with dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ013.ogg"
    hiratsuka "\"Not everyone who puts in ______ succeeds, but everyone who succeeds puts in ______.\" Now, how do you fill the blank."
    image yui_far_center_happy = Flatten("yui school far_center happy")
    image yui_far_center_surprised = Flatten("yui school far_center surprised")
    image yui_far_center_sad = Flatten("yui school far_center sad")
    image yui_far_center_pout = Flatten("yui school far_center pout")
    image yukino_far_center_happy = Flatten("yukino school far_center happy")
    image yukino_far_center_angry = Flatten("yukino school far_center angry")
    call screen two_minigame("Effort", "Humility") with dissolve
    if _return == 1:
        $E3_SHI_03_Q_A[0] = True
        window auto show dissolve
        voice "audio/voice/E3/SHI/03/HA/HA009.ogg"
        hachiman "I'm going to go with the cliche and pick what I'm not good at... Effort, is it?"
        show yui_far_center_happy at right behind hiratsuka:
            alpha 0 xoffset 0 yoffset 75
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 xoffset -75
            on hide:
                parallel:
                    linear 0.25 alpha 0
                parallel:
                    linear 0.25 xoffset 0
        $renpy.pause(delay=0.25, hard=False)
        voice "audio/voice/E3/SHI/03/YI/YI009.ogg"
        yui "Well, that one is easy!"
        hide yui_far_center_happy
    elif _return == 2:
        $E3_SHI_03_Q_A[0] = False
        voice "audio/voice/E3/SHI/03/HA/HA010.ogg"
        hachiman "The nails that stick out really do get hammered in. It's about modesty. People like me have to keep that in mind."
        show yui_far_center_surprised at right behind hiratsuka:
            alpha 0 xoffset 0 yoffset 75
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 xoffset -75
            on hide:
                parallel:
                    linear 0.25 alpha 0
                parallel:
                    linear 0.25 xoffset 0
        $renpy.pause(delay=0.25, hard=False)
        voice "audio/voice/E3/SHI/03/YI/YI010.ogg"
        yui "That doesn't sound modest at all!"
        hide yui_far_center_surprised
    $renpy.pause(delay=0.25, hard=False)
    voice "audio/voice/E3/SHI/03/HA/HA011.ogg"
    hachiman "Oh, this is gonna be a piece of cake. Wait, what does this have to do with stay-at home husband practice?"
    show hiratsuka annoyed with dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ014.ogg"
    hiratsuka "Don't think! Just do it!"
    show hiratsuka angry with dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ015.ogg"
    hiratsuka "Let's move on! What is \"youth\"?"
    call screen two_minigame("Never \nlooking \nback", "Correcting \nrotten adults") with dissolve
    if _return == 1:
        $E3_SHI_03_Q_A[1] = True
        voice "audio/voice/E3/SHI/03/HA/HA012.ogg"
        hachiman "Youth is never looking back. \"Say goodbye to tears\" and all. When all is said and done, when you become an adult, you won't be able to do anything but look back."
        show yui_far_center_sad at right behind hiratsuka:
            alpha 0 xoffset 0 yoffset 75
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 xoffset -75
            on hide:
                parallel:
                    linear 0.25 alpha 0
                parallel:
                    linear 0.25 xoffset 0
        $renpy.pause(delay=0.25, hard=False)
        voice "audio/voice/E3/SHI/03/YI/YI011.ogg"
        yui "That's pretty sad, isn't it?"
        hide yui_far_center_sad
    elif _return == 2:
        $E3_SHI_03_Q_A[1] = False
        voice "audio/voice/E3/SHI/03/HA/HA013.ogg"
        hachiman "Rebelling against adults is a young person's right!"
        show yui_far_center_pout at right behind hiratsuka:
            alpha 0 xoffset 0 yoffset 75
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 xoffset -75
            on hide:
                parallel:
                    linear 0.25 alpha 0
                parallel:
                    linear 0.25 xoffset 0
        $renpy.pause(delay=0.25, hard=False)
        voice "audio/voice/E3/SHI/03/YI/YI012.ogg"
        yui "I didn't know you were that type of character, Hikki..."
        hide yui_far_center_pout
    $renpy.pause(delay=0.25, hard=False)
    hide hiratsuka with dissolve
    show yui school mid_center surprised at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E3/SHI/03/YI/YI013.ogg"
    yui "I somehow feel like I'm getting better at house work!?"
    voice "audio/voice/E3/SHI/03/HA/HA014.ogg"
    hachiman "I think it's just in your head..."
    hide yui
    show hiratsuka school near_center happy at center:
        xoffset 30 yoffset 75
    with dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ016.ogg"
    hiratsuka "If there was a world you had to abide in, what kind of world is that?"
    call screen two_minigame("A world \nwithout \nloved ones", "A world \nwhere people \nrepeat their \nfoolishness") with dissolve
    if _return == 1:
        $E3_SHI_03_Q_A[2] = True
        voice "audio/voice/E3/SHI/03/HA/HA015.ogg"
        hachiman "That's surprisingly deep..."
        voice "audio/voice/E3/SHI/03/SZ/SZ017.ogg"
        hiratsuka "Hmph, hot-blooded passion is omnipresent in everything."
        show yui_far_center_sad at right behind hiratsuka:
            alpha 0 xoffset 0 yoffset 75
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 xoffset -75
            on hide:
                parallel:
                    linear 0.25 alpha 0
                parallel:
                    linear 0.25 xoffset 0
        $renpy.pause(delay=0.25, hard=False)
        voice "audio/voice/E3/SHI/03/YI/YI014.ogg"
        yui "What are you guys even talking about!? Well, I knew you would pick that one, but..."
        show yukino_far_center_happy at left behind hiratsuka:
            alpha 0 xoffset -175 yoffset 75
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 xoffset -75
            on hide:
                parallel:
                    linear 0.25 alpha 0
                parallel:
                    linear 0.25 xoffset -175
        $renpy.pause(delay=0.25, hard=False)
        voice "audio/voice/E3/SHI/03/YK/YK014.ogg"
        yukino "If you understand them in your mind, Yuigahama-san, then that's enough."
        voice "audio/voice/E3/SHI/03/YI/YI015.ogg"
        yui "Is-Is that so?"
        hide yui_far_center_sad
        hide yukino_far_center_happy
        $renpy.pause(delay=0.25, hard=False)
        if E3_SHI_03_Q_A[0] == False or E3_SHI_03_Q_A[1] == False:
            jump third_result
        $E3_SHI_03_result = 0
        show hiratsuka near_left happy with dissolve:
            xoffset 250 yoffset 75
        voice "audio/voice/E3/SHI/03/SZ/SZ018.ogg"
        hiratsuka "You're doing better than I thought! Just because your human nature is disappointing doesn't mean your ability itself is terrible."
        voice "audio/voice/E3/SHI/03/HA/HA017.ogg"
        hachiman "There are better ways to compliment somebody..."
    elif _return == 2:
        $E3_SHI_03_Q_A[2] = False
        show yukino_far_center_angry at left behind hiratsuka:
            alpha 0 xoffset -175 yoffset 75
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 xoffset -75
            on hide:
                parallel:
                    linear 0.25 alpha 0
                parallel:
                    linear 0.25 xoffset -175
        $renpy.pause(delay=0.25, hard=False)
        voice "audio/voice/E3/SHI/03/YK/YK015.ogg"
        yukino "..."
        show yui_far_center_surprised at right behind hiratsuka:
            alpha 0 xoffset 0 yoffset 75
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 xoffset -75
            on hide:
                parallel:
                    linear 0.25 alpha 0
                parallel:
                    linear 0.25 xoffset 0
        $renpy.pause(delay=0.25, hard=False)
        voice "audio/voice/E3/SHI/03/YI/YI016.ogg"
        yui "Yukino's face is super serious! She kinda seems different than usual..."
        voice "audio/voice/E3/SHI/03/HA/HA016.ogg"
        hachiman "Well, her sore loser mentality is intact as far as I can see."
        hide yui_far_center_surprised
        hide yukino_far_center_angry
        $renpy.pause(delay=0.25, hard=False)
        if E3_SHI_03_Q_A[0] == True or E3_SHI_03_Q_A[1] == True:
            jump third_result
        $E3_SHI_03_result = 1
        show hiratsuka near_left unimpressed with dissolve:
            xoffset 250 yoffset 75
        voice "audio/voice/E3/SHI/03/SZ/SZ020.ogg"
        hiratsuka "Not even close. How about thinking about it and trying again?"
        voice "audio/voice/E3/SHI/03/HA/HA019.ogg"
        hachiman "Damn, did I really not get a single question right?"

    jump E3_SHI_03_cont

label third_result:
    $E3_SHI_03_result = 2
    show hiratsuka near_left angry with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E3/SHI/03/SZ/SZ019.ogg"
    hiratsuka "You did pretty good, but you tripped up at the end. You won't make a decent househusband if you keep that up."
    voice "audio/voice/E3/SHI/03/HA/HA018.ogg"
    hachiman "I guess I messed up somewhere... this goes pretty deep."

label E3_SHI_03_cont:
    show hiratsuka near_center annoyed at center with dissolve:
        xoffset 30 yoffset 75
    voice "audio/voice/E3/SHI/03/SZ/SZ021.ogg"
    hiratsuka "You've done well to come this far... But now I'll show you what I'm really capable of! Watch this!"
    voice "audio/voice/E3/SHI/03/HA/HA020.ogg"
    hachiman "This isn't so much \"hot-bloodedness\" as it is a case of chuunibyou, is it?"
    show hiratsuka happy with dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ022.ogg"
    hiratsuka "Now! Let's move on to the next question!"
    show hiratsuka angry with dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ023.ogg"
    hiratsuka "What is \"strength\"?"
    call screen two_minigame("The power \nto protect \nyour friends", "The power \nto stand \nyour ground") with dissolve
    if _return == 1:
        $E3_SHI_03_Q_A[3] = False
        voice "audio/voice/E3/SHI/03/HA/HA022.ogg"
        hachiman "I guess defending your friends is what makes your real strength come out."
        show yui_far_center_pout at right behind hiratsuka:
            alpha 0 xoffset 0 yoffset 75
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 xoffset -75
            on hide:
                parallel:
                    linear 0.25 alpha 0
                parallel:
                    linear 0.25 xoffset 0
        $renpy.pause(delay=0.25, hard=False)
        voice "audio/voice/E3/SHI/03/YI/YI018.ogg"
        yui "Yeah. They do say true power is kindness..."
        hide yui_far_center_pout
    if _return == 2:
        $E3_SHI_03_Q_A[3] = True
        voice "audio/voice/E3/SHI/03/HA/HA021.ogg"
        hachiman "Yeah, the ability to presist in one's opinion, as a great man once said."
        show yui_far_center_surprised at right behind hiratsuka:
            alpha 0 xoffset 0 yoffset 75
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 xoffset -75
            on hide:
                parallel:
                    linear 0.25 alpha 0
                parallel:
                    linear 0.25 xoffset 0
        $renpy.pause(delay=0.25, hard=False)
        voice "audio/voice/E3/SHI/03/YI/YI017.ogg"
        yui "A great man actually said that?"
        hide yui_far_center_surprised

    $renpy.pause(delay=0.25, hard=False)
    voice "audio/voice/E3/SHI/03/HA/HA023.ogg"
    hachiman "As expected of sensei. Your questions are much higher level than before..."
    voice "audio/voice/E3/SHI/03/SZ/SZ024.ogg"
    hiratsuka "What does one need to be a true prince?"
    call screen two_minigame("Immortality", "Nobility") with dissolve
    if _return == 1:
        $E3_SHI_03_Q_A[4] = False
        voice "audio/voice/E3/SHI/03/HA/HA025.ogg"
        hachiman "This is a trick question, but I see right through it."
        show yui_far_center_surprised at right behind hiratsuka:
            alpha 0 xoffset 0 yoffset 75
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 xoffset -75
            on hide:
                parallel:
                    linear 0.25 alpha 0
                parallel:
                    linear 0.25 xoffset 0
        $renpy.pause(delay=0.25, hard=False)
        voice "audio/voice/E3/SHI/03/YI/YI020.ogg"
        yui "You do!?"
    if _return == 2:
        $E3_SHI_03_Q_A[4] = True
        voice "audio/voice/E3/SHI/03/HA/HA024.ogg"
        hachiman "That's a trick question..."
        show yui_far_center_surprised at right behind hiratsuka:
            alpha 0 xoffset 0 yoffset 75
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 xoffset -75
            on hide:
                parallel:
                    linear 0.25 alpha 0
                parallel:
                    linear 0.25 xoffset 0
        $renpy.pause(delay=0.25, hard=False)
        voice "audio/voice/E3/SHI/03/YI/YI019.ogg"
        yui "I-It is!?"

    hide yui_far_center_surprised
    $renpy.pause(delay=0.25, hard=False)
    show hiratsuka near_left happy with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E3/SHI/03/SZ/SZ025.ogg"
    hiratsuka "How about it, you two? Are you beginning to understand the essence of cooking?"
    voice "audio/voice/E3/SHI/03/HA/HA026.ogg"
    hachiman "Well, I don't know about that. But I do know one thing."
    show hiratsuka angry with dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ026.ogg"
    hiratsuka "Oh? What's that?"
    voice "audio/voice/E3/SHI/03/HA/HA027.ogg"
    hachiman "Hot-bloodedness means... Love!"
    voice "audio/voice/E3/SHI/03/SZ/SZ027.ogg"
    hiratsuka "Fu... You're starting to get it."
    show yui_far_center_surprised at right behind hiratsuka:
        alpha 0 xoffset 0 yoffset 75
        parallel:
            linear 0.25 alpha 1.0
        parallel:
            linear 0.25 xoffset -75
        on hide:
            parallel:
                linear 0.25 alpha 0
            parallel:
                linear 0.25 xoffset 0
    $renpy.pause(delay=0.25, hard=False)
    voice "audio/voice/E3/SHI/03/YI/YI021.ogg"
    yui "I mean, Sensei, you said it yourself just now!"
    show yukino_far_center_happy at left behind hiratsuka:
        alpha 0 xoffset -175 yoffset 75
        parallel:
            linear 0.25 alpha 1.0
        parallel:
            linear 0.25 xoffset -75
        on hide:
            parallel:
                linear 0.25 alpha 0
            parallel:
                linear 0.25 xoffset -175
    $renpy.pause(delay=0.25, hard=False)
    voice "audio/voice/E3/SHI/03/YK/YK016.ogg"
    yukino "Hiratsuka-sensei, the pot will be ready soon."
    show hiratsuka near_center happy at center with dissolve:
        xoffset 30 yoffset 75
    voice "audio/voice/E3/SHI/03/SZ/SZ028.ogg"
    hiratsuka "Oh, right. Now, for the last question. Mind your answer on this one."
    hide yui_far_center_surprised
    hide yukino_far_center_happy
    $renpy.pause(delay=0.25, hard=False)
    show hiratsuka angry with dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ029.ogg"
    hiratsuka "Which hero makes his own costume?"
    call screen two_minigame("Spider-man", "Batman") with dissolve
    if _return == 1:
        $E3_SHI_03_Q_A[5] = True
        voice "audio/voice/E3/SHI/03/HA/HA028.ogg"
        hachiman "Hum... American comics, as expected of Sensei! But I won't lose!"
        show yui_far_center_surprised at right behind hiratsuka:
            alpha 0 xoffset 0 yoffset 75
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 xoffset -75
            on hide:
                parallel:
                    linear 0.25 alpha 0
                parallel:
                    linear 0.25 xoffset 0
        $renpy.pause(delay=0.25, hard=False)
        voice "audio/voice/E3/SHI/03/YI/YI022.ogg"
        yui "Hikki's really into this!?"
        hide yui_far_center_surprised
        $renpy.pause(delay=0.25, hard=False)
        if E3_SHI_03_result == 0:
            if (E3_SHI_03_Q_A[3] == True or E3_SHI_03_Q_A[4] == True):
                jump E3_SHI_03_Q_A_best
            else:
                jump E3_SHI_03_Q_A_good
        elif E3_SHI_03_result == 1:
            if (E3_SHI_03_Q_A[3] == True and E3_SHI_03_Q_A[4] == True):
                jump E3_SHI_03_Q_A_best
            else:
                jump E3_SHI_03_Q_A_good
        elif E3_SHI_03_result == 2:
            if (E3_SHI_03_Q_A[3] == True and E3_SHI_03_Q_A[4] == True):
                jump E3_SHI_03_Q_A_good
            else:
                jump E3_SHI_03_Q_A_bad
    if _return == 2:
        $E3_SHI_03_Q_A[5] = False
        voice "audio/voice/E3/SHI/03/HA/HA029.ogg"
        hachiman "You seem pretty good at baiting, sensei."
        show yui_far_center_pout at right behind hiratsuka:
            alpha 0 xoffset 0 yoffset 75
            parallel:
                linear 0.25 alpha 1.0
            parallel:
                linear 0.25 xoffset -75
            on hide:
                parallel:
                    linear 0.25 alpha 0
                parallel:
                    linear 0.25 xoffset 0
        $renpy.pause(delay=0.25, hard=False)
        voice "audio/voice/E3/SHI/03/YI/YI023.ogg"
        yui "I've seen them only on TV movie commercials. Are you making these up!?"
        hide yui_far_center_pout
        $renpy.pause(delay=0.25, hard=False)
        if E3_SHI_03_result == 0:
            if (E3_SHI_03_Q_A[3] == True and E3_SHI_03_Q_A[4] == True):
                jump E3_SHI_03_Q_A_best
            else:
                jump E3_SHI_03_Q_A_good
        elif E3_SHI_03_result == 1:
            if (E3_SHI_03_Q_A[3] == True or E3_SHI_03_Q_A[4] == True):
                jump E3_SHI_03_Q_A_good
            else:
                jump E3_SHI_03_Q_A_bad
        elif E3_SHI_03_result == 2:
            if (E3_SHI_03_Q_A[3] == True and E3_SHI_03_Q_A[4] == True):
                jump E3_SHI_03_Q_A_good
            else:
                jump E3_SHI_03_Q_A_bad

label E3_SHI_03_Q_A_best:
    show hiratsuka near_left happy with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E3/SHI/03/SZ/SZ030.ogg"
    hiratsuka "Fu... Not bad, Hikigaya. I have nothing more to teach you. You've done well... to train yourself..."
    hide hiratsuka with dissolve
    image kitchenDecoy = "images/bg/BG36A.jpg"
    show black
    show kitchenDecoy at Shake(None, 0.25, dist=100)
    play sound "audio/sfx/SE01/SE01_55.ogg"
    $renpy.pause(delay=0.3, hard=False)
    hide black
    hide kitchenDecoy
    show yui school mid_center surprised at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E3/SHI/03/YI/YI024.ogg"
    yui "I feel kind of burned out myself."
    voice "audio/voice/E3/SHI/03/HA/HA030.ogg"
    hachiman "It's been... A long battle..."
    voice "audio/voice/E3/SHI/03/YI/YI025.ogg"
    yui "I feel like I'm getting caught up in it, too!"
    hide yui with dissolve
    jump E3_SHI_03_cont2

label E3_SHI_03_Q_A_good:
    show hiratsuka near_left angry with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E3/SHI/03/SZ/SZ031.ogg"
    hiratsuka "You were on a row there for a moment, but... Well, with your current power, you did what you could."
    voice "audio/voice/E3/SHI/03/HA/HA031.ogg"
    hachiman "By the way, which ones did I get wrong?"
    show hiratsuka happy with dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ032.ogg"
    hiratsuka "That is something... you yourself know best."
    voice "audio/voice/E3/SHI/03/HA/HA032.ogg"
    hachiman "I really don't though..."
    hide hiratsuka with dissolve
    jump E3_SHI_03_cont2

label E3_SHI_03_Q_A_bad:
    show hiratsuka near_left unimpressed with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E3/SHI/03/SZ/SZ033.ogg"
    hiratsuka "Hikigaya... what in the world happened? Good grief... my hopes were misplaced."
    hachiman "(I don't know what kind of hopes you had, but I feel like punching the air!) "
    hide hiratsuka with dissolve
    jump E3_SHI_03_cont2

label E3_SHI_03_cont2:
    stop music fadeout 0.5
    $renpy.pause(delay=0.5, hard=False)
    play music "audio/bgm/BGM34.ogg"
    show hiratsuka school mid_center happy at right:
        xoffset 100 yoffset 75
    show yukino school mid_center happy at left:
        xoffset -100 yoffset 75
    show yui school mid_center happy at center behind hiratsuka:
        xoffset -25 yoffset 75
    with dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ034.ogg"
    hiratsuka "Well, we'll leave it at that for today."
    voice "audio/voice/E3/SHI/03/HA/HA033.ogg"
    hachiman "S-Sure..."
    play sound "audio/sfx/SE01/SE01_73.ogg"
    show yui vhappy with dissolve
    voice "audio/voice/E3/SHI/03/YI/YI026.ogg"
    yui "There's this delicious smell in the air!"
    voice "audio/voice/E3/SHI/03/YK/YK017.ogg"
    yukino "Yes. Let's stop fooling around and get around to finishing it, shall we? Hikigaya-kun, slowly mix this into the pot."
    voice "audio/voice/E3/SHI/03/HA/HA034.ogg"
    hachiman "R-Right."
    "Hiratsuka-sensei said something as I, using chopsticks, clumsily tried to stir the pot with the curry powder Yukinoshita had thrown in."
    show hiratsuka mid_left angry with dissolve:
        xoffset 110 yoffset 80
    voice "audio/voice/E3/SHI/03/SZ/SZ035.ogg"
    hiratsuka "It wasn't fooling around at all! But it doesn't have much to do with cooking."
    show yui surprised with dissolve
    voice "audio/voice/E3/SHI/03/YI/YI027.ogg"
    yui "She said it herself!"
    hachiman "(Well, of course it doesn't...)"
    play sound "audio/sfx/SE03/SE03_07.ogg"
    $renpy.pause(delay=1.5, hard=False)
    show hiratsuka mid_center vhappy with dissolve:
        xoffset 100 yoffset 75
    voice "audio/voice/E3/SHI/03/SZ/SZ036.ogg"
    hiratsuka "Oh, nice timing on the rice! Let's try it when the curry is done, too."
    show yukino stare with dissolve
    voice "audio/voice/E3/SHI/03/YK/YK018.ogg"
    yukino "I'd really like to give the curry powder some time to settle in, but..."
    "As the delicious smell of curry stimulated my appetite, I asked a question that suddenly came to mind."
    voice "audio/voice/E3/SHI/03/HA/HA035.ogg"
    hachiman "...By the way, Sensei."
    show hiratsuka happy with dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ037.ogg"
    hiratsuka "What's up?"
    voice "audio/voice/E3/SHI/03/HA/HA036.ogg"
    hachiman "Well, how should I say this... You're surprisingly skilled at household chores, aren't you? So how come you're not..."
    stop voice
    stop music
    $renpy.pause(delay=0.25, hard=False)
    play sound "audio/sfx/SE01/SE01_83.ogg"
    hide hiratsuka
    hide yui
    hide yukino
    show white
    $renpy.pause(delay=0.25, hard=False)
    window auto hide dissolve
    scene kitchenA
    show hiratsuka school near_center annoyed at center:
        xoffset 30 yoffset 75
    with Fade(0, 0, 2.0, color="#fff")
    window auto show dissolve
    voice "audio/voice/E3/SHI/03/HA/HA037.ogg"
    hachiman "Guh!?"
    show hiratsuka near_left frown with dissolve:
        xoffset 250 yoffset 75
    play music "audio/bgm/BGM16.ogg"
    voice "audio/voice/E3/SHI/03/SZ/SZ038.ogg"
    hiratsuka "\"Surprisingly\" is bit harsh, don't you think? Moreover... How come I'm still not... what!?"
    voice "audio/voice/E3/SHI/03/HA/HA038.ogg"
    hachiman "No... I just... misspoke... I'm sorry..."
    show hiratsuka sad with dissolve
    voice "audio/voice/E3/SHI/03/SZ/SZ039.ogg"
    hiratsuka "We all make mistakes. Don't worry about it."
    voice "audio/voice/E3/SHI/03/HA/HA039.ogg"
    hachiman "Ri...ght..."
    "In the end, Sensei's just as I imagined sensei to be... I thought, in my fading consciousness, as I was pigeonholed by the iron fist of justice."
    window auto hide dissolve
    call loading_screen(27) from _call_loading_screen_29
    jump E3_CMM_06

label E3_SHI_04:
    $totsukaTalkFlag = "hiratsuka"
    play sound "audio/sfx/SE04/SE04_01.ogg"
    scene black with CropMove(0.5, mode="wipeleft")
    $renpy.pause(delay=0.5, hard=True)
    scene meetingRoomB with CropMove(0.5, mode="wipeleft")
    window auto show dissolve
    voice "audio/voice/E3/SHI/04/HA/HA000.ogg"
    hachiman "... At any rate, there are a lot more people here than I expected."
    stop sound
    show hiratsuka school_sunset mid_center surprised at center with dissolve:
        xoffset 40 yoffset 75
    play music "audio/bgm/BGM46.ogg"
    "I suddenly called out to Hiratsuka-sensei, making her stop."
    voice "audio/voice/E3/SHI/04/SZ/SZ000.ogg"
    hiratsuka "What's wrong, Hikigaya?"
    voice "audio/voice/E3/SHI/04/HA/HA001.ogg"
    hachiman "No, it's just surprising this amount of people showed up for advice."
    "I was going to play it off as a light-earted remark, but it turned out ironic."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E3/SHI/04/SZ/SZ001.ogg"
    hiratsuka "Well isn't it nice to know that everyone is serious about their future?"
    voice "audio/voice/E3/SHI/04/HA/HA002.ogg"
    hachiman "I didn't mean it that way."
    "I felt uncomfortable, so I was being evasive. I couldnn't deny that feeling of disgust I felt at the commotion in the classroom yesterday."
    show hiratsuka happy with dissolve
    voice "audio/voice/E3/SHI/04/SZ/SZ002.ogg"
    hiratsuka "I see. That's fine, then."
    voice "audio/voice/E3/SHI/04/HA/HA003.ogg"
    hachiman "......"
    show hiratsuka mid_left with dissolve:
        xoffset 110 yoffset 75
    voice "audio/voice/E3/SHI/04/SZ/SZ003.ogg"
    hiratsuka "Well, if you ever feel lost, you can always come to me."
    "Sensei said gently, as if she could see through all my inner thoghts. For some reason, I couldn't look her in the eyes."
    voice "audio/voice/E3/SHI/04/HA/HA004.ogg"
    hachiman "I'll think about it."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E3/SHI/04/SZ/SZ004.ogg"
    hiratsuka "Of course. I'll be waiting."
    voice "audio/voice/E3/SHI/04/HA/HA005.ogg"
    hachiman "Well then, excuse me."
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    play sound ["<silence 0.25>", "audio/sfx/SE04/SE04_01.ogg"]
    scene hallwayB with wipeleftFast
    $renpy.pause(delay=0.25, hard=True)
    window auto show dissolve
    hachiman "(Strangely enough, I feel tired...)"
    "Maybe I've been overthinking everything. I feel rebellious, sympathetic, impatient, and lost in my relationships with people around me. It was as if all of these things were coming at me at once."
    hachiman "(Anyway, I'll go back to class...)"
    window auto hide dissolve
    jump E3_CMM_07

label E3_SHI_05:
    scene hallwayB with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM34.ogg"
    hachiman "(She didn't see me, that's a relief...)"
    voice "audio/voice/E3/SHI/05/HA/HA000.ogg"
    hachiman "Ow, ow..."
    "The injury itself was nothing serious, but I physically felt like a wreck. Still, strangely enough, I didn't feel so bad."
    hachiman "(Anyway, let's put a bandage on this...)"
    window auto hide dissolve
    play sound "audio/sfx/SE04/SE04_01_.ogg"
    show black with wipeleft
    scene infirmaryB
    show hiratsuka school_sunset near_center surprised at center:
        xoffset 30 yoffset 75
    show black
    $renpy.pause(delay=0.25, hard=True)
    hide black with wipeleft
    voice "audio/voice/E3/SHI/05/SZ/SZ000.ogg"
    hiratsuka "Oh, it's just you, Hikigaya. You startled me."
    "There sat a surprised-looking Hiratsuka-sensei, in the chair that is usually occupied by the nurse."
    voice "audio/voice/E3/SHI/05/HA/HA001.ogg"
    hachiman "Same goes for you, Sensei. What are you doing here?"
    show hiratsuka happy with dissolve
    voice "audio/voice/E3/SHI/05/SZ/SZ001.ogg"
    hiratsuka "The school nurse was absent today. They couldn't leave the nurse's office unattended, so they asked someone younger to be incharge of it. Someone younger, like myself, see?"
    voice "audio/voice/E3/SHI/05/HA/HA002.ogg"
    hiratsuka "I can handle this much myself, though...."
    show hiratsuka near_left happy with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E3/SHI/05/SZ/SZ002.ogg"
    hiratsuka "At times like this, you should just listen and do as you're told. Come on, sit down."
    voice "audio/voice/E3/SHI/05/HA/HA003.ogg"
    hachiman "S-Sure...."
    hide hiratsuka with dissolve
    "Then, Hiratsuka-sensei sat me down in a chair, quickly prepared some antiseptic and plasters, and knelt down in front of me."
    window auto hide dissolve
    stop music fadeout 0.5
    scene hiratsukaInfirmary with Dissolve(1.0)
    play music "audio/bgm/BGM42.ogg"
    window auto show dissolve
    voice "audio/voice/E3/SHI/05/SZ/SZ003.ogg"
    hiratsuka "This will sting a bit."
    voice "audio/voice/E3/SHI/05/HA/HA004.ogg"
    hachiman "..."
    voice "audio/voice/E3/SHI/05/SZ/SZ004.ogg"
    hiratsuka "You alright?"
    voice "audio/voice/E3/SHI/05/HA/HA005.ogg"
    hachiman "I'm... fine."
    hachiman "(I thought she'd be heavy-handed with it, but... she's surprisingly gentle.)"
    "I wondered if it was because we were closer than usual. The smell of cigarettes and the surprisingly sweet smell of her hair mixed together made me nervous."
    voice "audio/voice/E3/SHI/05/SZ/SZ005.ogg"
    hiratsuka "There we go..."
    window auto hide dissolve
    stop music fadeout 0.5
    scene infirmaryB
    show hiratsuka school_sunset near_center happy at center:
        xoffset 30 yoffset 75
    with dissolve
    window auto show dissolve
    "My eyes met Hiratsuka-sensei's as she raised her head. Because of how unexpectedly close we were, we locked eyes for a few seconds. We were frozen, staring at each other."
    show hiratsuka surprised with dissolve
    voice "audio/voice/E3/SHI/05/SZ/SZ006.ogg"
    hiratsuka "..."
    voice "audio/voice/E3/SHI/05/HA/HA006.ogg"
    hachiman "..."
    show hiratsuka blush with dissolve
    voice "audio/voice/E3/SHI/05/HA/HA007.ogg"
    hachiman "Ah... thanks for that."
    voice "audio/voice/E3/SHI/05/SZ/SZ007.ogg"
    hiratsuka "Don't worry about it. It's my duty as a teacher."
    show hiratsuka near_left blush with dissolve:
        xoffset 250 yoffset 75
    "As she said that, Hiratsuka-sensei looked somewhat awkward and quickly pulled back."
    play music "audio/bgm/BGM41.ogg"
    voice "audio/voice/E3/SHI/05/HA/HA008.ogg"
    hachiman "Anyway, shouldn't you be at the marathon event?"
    show hiratsuka near_center happy with dissolve:
        xoffset 30 yoffset 75
    voice "audio/voice/E3/SHI/05/SZ/SZ008.ogg"
    hiratsuka "We've got a closing ceremony later. I think the Student Council can handle it."
    voice "audio/voice/E3/SHI/05/SZ/SZ009.ogg"
    hiratsuka "By the way, judging by the look on your face, it seems like the problem you were talking about the other day has been resolved."
    "She looked outside at the sporting grounds as she said this with relief. It's is as if she's been wanting to say it from the beginning."
    voice "audio/voice/E3/SHI/05/HA/HA009.ogg"
    hachiman "I guess you could say that."
    show hiratsuka near_left with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E3/SHI/05/SZ/SZ010.ogg"
    hiratsuka "That's good to hear."
    voice "audio/voice/E3/SHI/05/HA/HA010.ogg"
    hachiman "My body's a wreck because of it, though."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E3/SHI/05/SZ/SZ011.ogg"
    hiratsuka "You'll be fine. It'll heal soon enough."
    "From her smile I noticed. I realized Hiratsuka-sensei was glad not because I wasn't hurt physically, but because I wasn't hurting myself through my methods."
    show hiratsuka happy with dissolve
    voice "audio/voice/E3/SHI/05/SZ/SZ012.ogg"
    hiratsuka "..."
    "Hiratsuka-sensei, who may or may not have known how deeply moved I felt, gazed leisurely out the window. I felt very relieved at the sight."
    window auto hide dissolve
    stop music fadeout 0.5
    call loading_screen(26) from _call_loading_screen_30
    jump E3_CMM_08
