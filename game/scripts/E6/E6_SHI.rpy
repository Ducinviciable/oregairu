label E6_SHI_01:
    scene clubroomB
    show yukino school_sunset mid_center happy at left:
        xoffset 25 yoffset 75
    show yui school_sunset mid_center happy at right:
        xoffset -300 yoffset 75
    with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/BGM06.ogg"
    window auto show dissolve
    "It was the end of winter. A normal day like any other. The Service Club's activities for today had come to a close."
    voice "audio/voice/E6/SHI/01/YK/YK000.ogg"
    yukino "Today was quite uneventful."
    voice "audio/voice/E6/SHI/01/YI/YI000.ogg"
    yui "Yeah, it was really peaceful all day."
    hachiman "(Well, it's rather a good thing that nothing is happening, but it really takes away the whole point of this club...)"
    show yui mid_left happy with dissolve:
        xoffset -270 yoffset 75
    voice "audio/voice/E6/SHI/01/YI/YI001.ogg"
    yui "Who wants to return the key today? Want me to go?"
    show yukino sly with dissolve
    voice "audio/voice/E6/SHI/01/YK/YK001.ogg"
    yukino "No, I believe Hikigaya-kun should be the one to do it."
    voice "audio/voice/E6/SHI/01/HA/HA000.ogg"
    hachiman "Huh?"
    show yui vhappy with dissolve
    voice "audio/voice/E6/SHI/01/YI/YI002.ogg"
    yui "Ah! You're right. Let's have Hikki do it."
    voice "audio/voice/E6/SHI/01/HA/HA001.ogg"
    hachiman "Not you too, Yuigahama... why me?"
    show yui mid_center happy with dissolve:
        xoffset -300 yoffset 75
    voice "audio/voice/E6/SHI/01/YI/YI003.ogg"
    yui "Because me and Yukino are going somewhere together."
    show yukino angry with dissolve
    voice "audio/voice/E6/SHI/01/YK/YK002.ogg"
    yukino "That's right. If you understand then get going."
    voice "audio/voice/E6/SHI/01/HA/HA002.ogg"
    hachiman "Don't just exclude someone like it's only natural."
    show yukino vhappy with dissolve
    voice "audio/voice/E6/SHI/01/YK/YK003.ogg"
    yukino "Well, you would prefer to be excluded anyway, wouldn't you?"
    show yui mid_left vhappy with dissolve:
        xoffset -270 yoffset 75
    voice "audio/voice/E6/SHI/01/YI/YI004.ogg"
    yui "Right, right, exactly!"
    voice "audio/voice/E6/SHI/01/HA/HA003.ogg"
    hachiman "What the..."
    "Yuigahama and Yukinoshita looked at each other as they said this. I don't know what they're up to, but they can at least be a little less obvious about it?"
    show yui vhappy with dissolve
    voice "audio/voice/E6/SHI/01/YI/YI005.ogg"
    yui "Then come on, Yukino, let's go!"
    show yukino happy with dissolve
    voice "audio/voice/E6/SHI/01/YK/YK004.ogg"
    yukino "Yes, let's go. We're leaving the rest to you."
    show yui mid_center vhappy with dissolve:
        xoffset -300 yoffset 75
    voice "audio/voice/E6/SHI/01/YI/YI006.ogg"
    yui "Later, Hikki! See you tommorow!"
    voice "audio/voice/E6/SHI/01/HA/HA004.ogg"
    hachiman "Yeah, see you."
    hide yukino
    hide yui
    with dissolve
    hachiman "(What the hell was that about...)"
    window auto hide dissolve
    stop music fadeout 1.0
    scene skyC with Fade(0.5, 1.0, 0.5)
    window auto show dissolve
    "They left and I trudged to the staff room. It was still winter and the sun had already set."
    hachiman "(Winter is about to end, but it's still cold...)"
    hachiman "(It's so dark... is there really someone still here?)"
    voice "audio/voice/E6/SHI/01/HA/HA005.ogg"
    hachiman "Coming in..."
    window auto hide dissolve
    play sound ["<silence 0.5>", "audio/sfx/SE04/SE04_00.ogg"]
    scene staffroomC
    show hiratsuka school mid_center surprised at center:
        xoffset 40 yoffset 75
    with Fade(0.5, 0.5, 0.5)
    $renpy.pause(delay=0.5,hard=True)
    window auto show dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ000.ogg"
    hiratsuka "Ah."
    play music "audio/bgm/BGM10.ogg"
    voice "audio/voice/E6/SHI/01/HA/HA006.ogg"
    hachiman "Ah, Hiratsuka-sensei..."
    show hiratsuka pout with dissolve
    "When Hiratsuka-sensei noticed my presence and turned around, she had a clearly abashed look on her face, which struck me as odd."
    hachiman "(I wonder what happened...)"
    show hiratsuka happy with dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ001.ogg"
    hiratsuka "It's you, Hikigaya. What's up?"
    voice "audio/voice/E6/SHI/01/HA/HA007.ogg"
    hachiman "I just came to drop off the club key."
    show hiratsuka blush with dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ002.ogg"
    hiratsuka "I-I see. You came earlier than expected."
    voice "audio/voice/E6/SHI/01/HA/HA008.ogg"
    hachiman "That... so?"
    hide hiratsuka with dissolve
    play sound "audio/sfx/SE01/SE01_03.ogg"
    "I don't know how to face sensei since the ski camp. And she seems to have the same issue, too."
    hachiman "(We're just a teacher and her student, nothing more. Really, there's something more... to it...)"
    "Being in the teacher's room, that line of our relationship was more pronounced than ever and it really stuck out to me right then."
    "In other words, the reality that I was born ten years later than sensei became clear."
    "I wondered if the reason why such an obvious thing was bothering me again was because I was somehow conscious of sensei as a member of the opposite sex since what happened at the ski camp."
    "The only thing I can say for sure is... I'm still not sure what I'm feeling."
    window auto hide dissolve
    image hiratsukastaffroomcDup = "images/BG/EV37c.jpg"
    scene hiratsukastaffroomc with dissolve
    window auto show dissolve
    voice "audio/voice/E6/SHI/01/HA/HA009.ogg"
    hachiman "What are you working on, sensei?"
    voice "audio/voice/E6/SHI/01/SZ/SZ003.ogg"
    hiratsuka "Hm? Well, on paperwork. I have a lot of it piled up at the end of the year."
    voice "audio/voice/E6/SHI/01/HA/HA010.ogg"
    hachiman "Don't you always say yourself to do things step by step over time?"
    voice "audio/voice/E6/SHI/01/SZ/SZ004.ogg"
    hiratsuka "Haha... well, do as I say not as I do."
    window auto hide dissolve
    stop voice
    show staffroomC
    show hiratsukastaffroomcDup at truecenter:
        zoom 1.6 xoffset 390 yoffset 35
    with dissolve
    window auto show dissolve
    "When I looked at Hiratsuka-sensei's desk, I saw a pile of papers. One by one she was writing something on them in a very careful manner."
    hachiman "(Well, it seems she's always watching over us, huh...)"
    voice "audio/voice/E6/SHI/01/SZ/SZ005.ogg"
    hiratsuka "A-Anyway, I can't be your guy's homeroom teacher forever."
    voice "audio/voice/E6/SHI/01/SZ/SZ006.ogg"
    hiratsuka "You can't always watch over everybody. That's the sorrow of a public servant."
    voice "audio/voice/E6/SHI/01/HA/HA011.ogg"
    hachiman "Is that so..."
    hide hiratsukastaffroomcDup with dissolve
    "It was a sobering thought to think that she had been watching over us for as many words as she had written on these documents."
    voice "audio/voice/E6/SHI/01/HA/HA012.ogg"
    hachiman "....."
    voice "audio/voice/E6/SHI/01/SZ/SZ007.ogg"
    hiratsuka "Ha...."
    hide staffroomC with dissolve
    "With a big sigh, as if she made up her mind about something, sensei smiled."
    voice "audio/voice/E6/SHI/01/SZ/SZ008.ogg"
    hiratsuka "Want to go out with me for a bit?"
    voice "audio/voice/E6/SHI/01/HA/HA013.ogg"
    hachiman "Huh?"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    image fancyCafeDup = "images/bg/BG66A.jpg"
    scene fancyCafe with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/BGM26.ogg"
    window auto show dissolve
    "Hiratsuka-sensei took me to a fancy cafe, which I couldn't help but feel out of place in. The atmosphere was so mature, so I was constantly looking around."
    hachiman "(I definitely thought we were going to a ramen shop, but I was sorely mistaken.)"
    show hiratsuka home mid_center pout at center with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E6/SHI/01/SZ/SZ009.ogg"
    hiratsuka "Well, since this counts as a cafe, bringing a student here shouldn't be a problem."
    voice "audio/voice/E6/SHI/01/HA/HA014.ogg"
    hachiman "So that's why..."
    show hiratsuka happy with dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ010.ogg"
    hiratsuka "I was kind of in the mood to have a more relaxed conversation."
    voice "audio/voice/E6/SHI/01/HA/HA015.ogg"
    hachiman "Right..."
    window auto hide dissolve
    hide hiratsuka with dissolve
    $renpy.pause(delay=0.5,hard=True)
    play sound "audio/sfx/SE01/SE01_12.ogg"
    $renpy.pause(delay=0.75,hard=True)
    stop sound
    show fancyCafeDup at topleft:
        zoom 1.8 xoffset -335 yoffset -400
    show hiratsuka home near_center happy at center:
        xoffset 30 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ011.ogg"
    hiratsuka "Whiskey, on the rocks... and chocolate... and a coffee for him."
    hachiman "(She's so cool... Just how deep does her manliness go?)"
    "I had never seen this side of sensei before, and I couldn't help but admire it. And I realize anew that she is much more mature than I am."
    window auto hide dissolve
    show black with fade
    $renpy.pause(delay=0.5,hard=True)
    play sound "audio/sfx/SE01/SE01_21.ogg"
    $renpy.pause(delay=0.75,hard=True)
    stop sound
    hide black with fade
    window auto show dissolve
    "As I took a sip of the coffee that was brought to me, the rich flavor of the high grade beans filled my mouth."
    hachiman "(Oh, it's good... but it's so bitter when I just drink it black.)"
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ012.ogg"
    hiratsuka "Bitter?"
    voice "audio/voice/E6/SHI/01/HA/HA016.ogg"
    hachiman "Yeah, but... why did I get dark chocolate, too?"
    show hiratsuka happy with dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ013.ogg"
    hiratsuka "This is the perfect amount of sweetness for sake."
    hachiman "(Is that so? I've never had a drink before so I wouldn't know...)"
    voice "audio/voice/E6/SHI/01/SZ/SZ014.ogg"
    hiratsuka "No need to force yourself. Why not add some milk or sugar?"
    voice "audio/voice/E6/SHI/01/HA/HA017.ogg"
    hachiman "I'll do that. I have a sweet tooth anyway."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ015.ogg"
    hiratsuka "That's perfect, then."
    "Hiratsuka-sensei smiles at me as she adds sugar and milk for me. I feel like a little fustrated because I'm starting to feel an awful lot like a child."
    show hiratsuka happy with dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ016.ogg"
    hiratsuka "What do you think, Hikigaya? Haven't you changed a bit recently?"
    voice "audio/voice/E6/SHI/01/HA/HA018.ogg"
    hachiman "......"
    "Sensei breaks the ice casually, as if making small talk, but she has a very serious expression on her face."
    "Perhaps because I was a troublesome student to deal with, she was straight with me and immediately breached the topic as if I weren't a student, but an adult. That was so like her."
    "If she was willing to do that, I should probably give her as serious a reply as I can instead of taking an oblique stance and running away."
    "In that line of thinking, Totsuka's words suddenly crossed my mind."
    window auto hide dissolve
    stop music fadeout 1.0
    show totsukaClassroom with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    voice "audio/voice/E6/SHI/01/SI/SI000.ogg"
    totsuka "I think it's a wonderful thing to be able to get closer with someone."
    window auto hide dissolve
    stop voice
    hide totsukaClassroom with Fade(0.25,0.35, 0.5, color="#fff")
    play music "audio/bgm/BGM42.ogg"
    window auto show dissolve
    hachiman "(A wonderful thing, huh...)"
    voice "audio/voice/E6/SHI/01/HA/HA019.ogg"
    hachiman "I'm probably going to betray your expectations."
    show hiratsuka angry with dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ017.ogg"
    hiratsuka "Oh?"
    voice "audio/voice/E6/SHI/01/HA/HA020.ogg"
    hachiman "If I want to break a relationship, I need to accept how it's been up to this point. It's the only way I can really stand beside them. That's what I think right now."
    show hiratsuka happy with dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ018.ogg"
    hiratsuka "So then why would you be betraying my expectations?"
    "Hiratsuka-sensei peered at me with great interest, as if asking the answer to a riddle."
    voice "audio/voice/E6/SHI/01/HA/HA021.ogg"
    hachiman "That's because..."
    show hiratsuka angry with dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ019.ogg"
    hiratsuka "...?"
    voice "audio/voice/E6/SHI/01/HA/HA022.ogg"
    hachiman "Because... I'm interested in hearing what things you wish could've happened, but didn't, sensei."
    show hiratsuka blush with dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ020.ogg"
    hiratsuka "Wha....!"
    hachiman "(What the hell am I saying...)"
    "I was surprised at the words that came out of my mouth. But I was sure that's how I really felt. I wanted to know more about sensei."
    "Sensei was not a \"teacher\" to me anymore, she's... probably the only person who is really special to me."
    show hiratsuka near_left blush with dissolve:
        xoffset 200 yoffset 80
    voice "audio/voice/E6/SHI/01/SZ/SZ021.ogg"
    hiratsuka "Y-You still remember that!?"
    "Seeing her cheeks flush with surprise, I made up my mind. There's no point in thinking about what could've or should've happened if we met 10 years ago. I should tell her how I feel now, properly."
    voice "audio/voice/E6/SHI/01/HA/HA023.ogg"
    hachiman "I meant to tell you the other day, but... you fell asleep."
    voice "audio/voice/E6/SHI/01/SZ/SZ022.ogg"
    hiratsuka "Is that so?"
    voice "audio/voice/E6/SHI/01/HA/HA024.ogg"
    hachiman "It is."
    voice "audio/voice/E6/SHI/01/HA/HA025.ogg"
    hachiman "I've been thinking about it since the other day. It's been bothering me and... I haven't been able to figure it out."
    voice "audio/voice/E6/SHI/01/HA/HA026.ogg"
    hachiman "I'd never thought I'd want to know about anyone's past, but... I want to know about yours, sensei."
    "Although I was vomiting things out extremely clumsily, my mind was strangely calm. In fact, I even felt strangely refreshed."
    "I'm sure that's because my words contained no falsehood. Because I've finally come to terms with my feelings. And... I've been able to convey them."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ023.ogg"
    hiratsuka "I see."
    "I don't know whether I should take those words as an affirmation or a rejection. But I'm sure she got the message. Looking at sensei's expression, I felt I'd gotten through to her."
    show hiratsuka near_center with dissolve:
        xoffset 30 yoffset 75
    voice "audio/voice/E6/SHI/01/SZ/SZ024.ogg"
    hiratsuka "Then I hope that one day you and I will be able to talk like this again."
    voice "audio/voice/E6/SHI/01/HA/HA027.ogg"
    hachiman "Ah..."
    "Then, she put her index finger on her glossy lips before she gently touched my forehead. I could feel my heart beating faster than it ever had before."
    hachiman "(Eh? Was that an indirect kiss just now?)"
    voice "audio/voice/E6/SHI/01/HA/HA028.ogg"
    hachiman "Sensei... you're drunk, aren't you?"
    show hiratsuka blush with dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ025.ogg"
    hiratsuka "Yes, of course I'm drunk. Otherwise I wouldn't be able to do something this flashy."
    voice "audio/voice/E6/SHI/01/HA/HA029.ogg"
    hachiman "Sure is convinient being drunk."
    "I was so embarrassed, I ended up saying something crude. Hiratsuka-sensei only smiled gently at me. It seemed her red cheeks weren't only due to the alcohol."
    show hiratsuka happy with dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ026.ogg"
    hiratsuka "That's right. You should hurry and grow the hell up so we can have a drink together."
    voice "audio/voice/E6/SHI/01/HA/HA030.ogg"
    hachiman "That's gonna take a while, though."
    show hiratsuka near_left happy with dissolve:
        xoffset 200 yoffset 80
    voice "audio/voice/E6/SHI/01/SZ/SZ027.ogg"
    hiratsuka "Well, I'll be here, waiting..."
    voice "audio/voice/E6/SHI/01/HA/HA031.ogg"
    hachiman "Okay."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E6/SHI/01/SZ/SZ028.ogg"
    hiratsuka "However, your future will not neccessarily only consist of people who are willing to wound you."
    voice "audio/voice/E6/SHI/01/HA/HA032.ogg"
    hachiman "Yeah, I hope not."
    "Me and sensei softly smiled at each other."
    window auto hide dissolve
    stop music fadeout 1.0
    jump E6_SHI_02

label E6_SHI_02:
    scene mallB with Fade(0.5, 1.0, 0.5)
    play ambient "audio/sfx/SE05/SE05_01L.ogg"
    window auto show dissolve
    hachiman "(Let's see, I think the reference books should be here somewhere...)"
    "After school, I stop by a book store to buy some reference books. I don't wan to believe it, but I have an exam I need to take next year."
    show hiratsuka home far_left pout at center with dissolve:
        xoffset 85 yoffset 80
    voice "audio/voice/E6/SHI/02/SZ/SZ000.ogg"
    hiratsuka "......"
    voice "audio/voice/E6/SHI/02/HA/HA000.ogg"
    hachiman "Huh?"
    hachiman "(That's... Hiratsuka-sensei, isn't it? What is she doing sneaking arond like that?)"
    hachiman "(I'll go give her a big surprise...)"
    window auto hide dissolve
    scene mallB at topleft:
        zoom 1.8 xoffset -335 yoffset -395
    show hiratsuka home mid_left pout at center:
        xoffset 115 yoffset 80
    with dissolve
    window auto show dissolve
    voice "audio/voice/E6/SHI/02/SZ/SZ001.ogg"
    hiratsuka "......"
    voice "audio/voice/E6/SHI/02/HA/HA001.ogg"
    hachiman "What are you doing?"
    show hiratsuka surprised at center, Shake(None, 0.2, dist=20)
    voice "audio/voice/E6/SHI/02/SZ/SZ002.ogg"
    hiratsuka "Kyaaa!?"
    show hiratsuka mid_center at center with dissolve:
        xoffset 40 yoffset 75
    stop ambient
    play music "audio/bgm/BGM26.ogg"
    voice "audio/voice/E6/SHI/02/SZ/SZ003.ogg"
    hiratsuka "H-Hikigaya!?"
    hachiman "(You don't need to be so surprised... Hm?)"
    voice "audio/voice/E6/SHI/02/HA/HA002.ogg"
    hachiman "T-This is..."
    hachiman "(A mountain of wedding magazines!?)"
    show hiratsuka pout with dissolve
    voice "audio/voice/E6/SHI/02/SZ/SZ004.ogg"
    hiratsuka "D-Don't say a word. Pretend you didn't see me."
    voice "audio/voice/E6/SHI/02/HA/HA003.ogg"
    hachiman "I-I'll do that."
    window auto hide dissolve
    stop voice
    scene classroomA with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    voice "audio/voice/E6/SHI/02/SZ/SZ005.ogg"
    hiratsuka "Tomorrow is the spring break you've been waiting for. But don't get carried away. You have an exam to take this year."
    window auto hide dissolve
    stop voice
    scene gatesB with Fade(0.5, 0.5, 0.5)
    play ambient "audio/sfx/SE03/SE03_00L.ogg"
    window auto show dissolve
    voice "audio/voice/E6/SHI/02/HA/HA004.ogg"
    hachiman "Hmm? It's from Komachi..."
    "The new semester came around. Although I'm now a third year student, I don't really feel that much has changed. The only major difference is that Komachi had entered Sobu High."
    stop ambient
    play sound "audio/sfx/SE03/SE03_02.ogg"
    voice "audio/voice/E6/SHI/02/HA/HA005.ogg"
    hachiman "\"Komachi will have tea with her friends and come home later~\". Ah, is that so..."
    hachiman "(I thought we were gonna go home together, but Komachi had started to leave me before I even knew it...!)"
    window auto hide dissolve
    stop voice
    scene sidewalkB with Fade(0.5, 0.5, 0.5)
    play sound "audio/sfx/SE06/SE06_12.ogg"
    $renpy.pause(delay=0.5,hard=True)
    window auto show dissolve
    hachiman "(Hm!?)"
    play sound "audio/sfx/SE06/SE06_10.ogg"
    $renpy.pause(delay=0.5,hard=True)
    show hiratsuka home mid_center at center with dissolve:
        xoffset 40 yoffset 75
    play sound "audio/sfx/SE06/SE06_11.ogg"
    $renpy.pause(delay=0.75,hard=True)
    voice "audio/voice/E6/SHI/02/SZ/SZ006.ogg"
    hiratsuka "I fond a good ramen spot. Wanna hit it up?"
    voice "audio/voice/E6/SHI/02/HA/HA006.ogg"
    hachiman "Can I leave my bike over here first, though?"
    window auto hide dissolve
    stop voice
    scene fieldA with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    hachiman "(Oh, this ramen spot looks good... I'll go there with sensei next time.)"
    show iroha school mid_center pout at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E6/SHI/02/IR/IR000.ogg"
    iroha "Senpai, what are you doing in a place like this?"
    voice "audio/voice/E6/SHI/02/HA/HA007.ogg"
    hachiman "I'm eating lunch. What does it look like?"
    show iroha unimpressed with dissolve
    voice "audio/voice/E6/SHI/02/IR/IR001.ogg"
    iroha "H~m? What are you looking on your phone and smiling about? It's honestly creepy, please stop."
    voice "audio/voice/E6/SHI/02/HA/HA008.ogg"
    hachiman "Ah... this is just..."
    show iroha happy with dissolve
    voice "audio/voice/E6/SHI/02/IR/IR002.ogg"
    iroha "Ah, this is a site about ramen shops! Senpai, you're getting creepier and creepier!"
    voice "audio/voice/E6/SHI/02/HA/HA009.ogg"
    hachiman "What is it with you?"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    scene black with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    "Then, the months went by, our exams were over, and while basking in the relief, we were all deciding what path to go down one night."
    window auto hide dissolve
    scene celebratoryParty with Fade(0.5, 0.5, 0.5)
    play ambient "audio/sfx/SE05/SE05_02L.ogg"
    window auto show dissolve
    voice "audio/voice/E6/SHI/02/IR/IR003.ogg"
    iroha "And now, this one's to celebrate all the 3rd years' success in the exams. Cheers!"
    voice "audio/voice/E6/SHI/02/MI/MIX000.ogg"
    evb "Cheers!"
    voice "audio/voice/E6/SHI/02/YI/YI001.ogg"
    yui "Anyway, I'm so glad no one of us have to wait another year to retake our exams."
    voice "audio/voice/E6/SHI/02/YK/YK001.ogg"
    yukino "It's really nice to see that not a single person overtly screwed up."
    voice "audio/voice/E6/SHI/02/HA/HA011.ogg"
    hachiman "That's true. Chances wise, there probably should've been at least one..."
    voice "audio/voice/E6/SHI/02/KO/KO001.ogg"
    komachi "Surprisingly, Onii-chan was the most likely to fail, wasn't he? He was aiming pretty high."
    voice "audio/voice/E6/SHI/02/HA/HA012.ogg"
    hachiman "Nonesense. It was all accounted for."
    hachiman "(In reality, I couldn't sleep every night until I got the acceptance letter...)"
    voice "audio/voice/E6/SHI/02/SZ/SZ008.ogg"
    hiratsuka "When all is said and done, this is a result of all of you properly thinking things through. I'm very happy for you all."
    voice "audio/voice/E6/SHI/02/YI/YI002.ogg"
    yui "Ehehe, I'm honestly pretty worried, though..."
    voice "audio/voice/E6/SHI/02/IR/IR005.ogg"
    iroha "I'm really worried I'll be all alone starting next year~"
    voice "audio/voice/E6/SHI/02/YI/YI003.ogg"
    yui "Yukinon~! Let's have some tea or dinner on the way home!"
    voice "audio/voice/E6/SHI/02/YK/YK002.ogg"
    yukino "Yuigahama-san, stop clinging to me... Besides, nothing will really change from now on."
    hachiman "(They have their usual heartwarming relationship going...)"
    voice "audio/voice/E6/SHI/02/SZ/SZ009.ogg"
    hiratsuka "Hikigaya..."
    voice "audio/voice/E6/SHI/02/HA/HA013.ogg"
    hachiman "Huh?"
    voice "audio/voice/E6/SHI/02/SZ/SZ010.ogg"
    hiratsuka "Well, enjoy your college life as much as you can. We can always get together here with everyone like this."
    voice "audio/voice/E6/SHI/02/HA/HA014.ogg"
    hachiman "Am I really that desperately in need of reassurance?"
    voice "audio/voice/E6/SHI/02/SZ/SZ011.ogg"
    hiratsuka "That's not what I meant, but... we all feel uneasy about things changing."
    voice "audio/voice/E6/SHI/02/HA/HA015.ogg"
    hachiman "Yeah, I suppose that's true..."
    voice "audio/voice/E6/SHI/02/SZ/SZ012.ogg"
    hiratsuka "Just know that... I'll always be waiting for you."
    "Sensei whispers these last words in my ear so that only I can hear."
    voice "audio/voice/E6/SHI/02/HA/HA016.ogg"
    hachiman "I'm betting on it."
    voice "audio/voice/E6/SHI/02/IR/IR006.ogg"
    iroha "By the way, putting senpai aside, do you think Hiratsuka-sensei still thinks we don't know what's up~?"
    voice "audio/voice/E6/SHI/02/KO/KO002.ogg"
    komachi "Maybe she's going in because she just doesn't care?"
    voice "audio/voice/E6/SHI/02/YK/YK003.ogg"
    yukino "I believe it would make things easier if we just acknowledged their relationship already..."
    voice "audio/voice/E6/SHI/02/YI/YI004.ogg"
    yui "I want to pretend not to notice for my own sake, too, you know~?"
    hachiman "(I can hear you loud and clear, you know...)"
    window auto hide dissolve
    stop ambient
    stop music fadeout 1.0
    scene skyA with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    "After a few more months, it was graduation day. Our three years at Sobu High had come to an end."
    "So many things had happened that I wasn't sure if it had been 3 years or only a few short months."
    "But I can say one thing for certain. Those three years of struggling, wondering and confronting made me who I am now."
    "Three years ago, I never would've been able to imagine feeling the way I am now."
    voice "audio/voice/E6/SHI/02/YK/YK004.ogg"
    yukino "Thank you very much for being here today. I wish you all the best and thank you for giving me, alumnus representative, Yukino Yukinoshita, the privilege of expressing my gratitude."
    "As I listened to Yukinoshita's speech, I kept thinking about it. I thought about what the future had in store for me."
    window auto hide dissolve
    scene clubroomA
    show yukino school mid_center happy at left:
        xoffset 25 yoffset 75
    show yui school mid_left sad at right:
        xoffset -270 yoffset 75
    with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/BGM18.ogg"
    window auto show dissolve
    voice "audio/voice/E6/SHI/02/YI/YI005.ogg"
    yui "Yukinon~, you made me cry! Your speech was so cool!"
    show yukino blush with dissolve
    voice "audio/voice/E6/SHI/02/YK/YK005.ogg"
    yukino "Yuigahama-san... you're exaggarating."
    voice "audio/voice/E6/SHI/02/HA/HA017.ogg"
    hachiman "Didn't know you were capable of talking so freely."
    show yukino sly with dissolve
    voice "audio/voice/E6/SHI/02/YK/YK006.ogg"
    yukino "Oh, I'm sure you could've done it, too. You're such a fluent conversationalist after all."
    voice "audio/voice/E6/SHI/02/HA/HA018.ogg"
    hachiman "What's that supposed to mean? I'm an airy conversationalist. I'm even light on words."
    show yui happy with dissolve
    voice "audio/voice/E6/SHI/02/YI/YI006.ogg"
    yui "Ahaha... But, this is the last time we'll be here together like this."
    "As she smiled, large tears appeared in her eyes."
    "It's understandable. So many things have come to pass here, I might start crying myself if I'm not careful."
    show yukino vhappy with dissolve
    voice "audio/voice/E6/SHI/02/YK/YK007.ogg"
    yukino "It really is..."
    voice "audio/voice/E6/SHI/02/HA/HA019.ogg"
    hachiman "Well, it's not like we're dying when we graduate. We can always meet each other."
    "I was surprised at my own words. It seemed that neither of them were expecting me to say something like that and were shooting me dumbfounded looks."
    show yui mid_center vhappy with dissolve:
        xoffset -300 yoffset 75
    voice "audio/voice/E6/SHI/02/YI/YI007.ogg"
    yui "Hikki... Yeah, that's right! Let's always get together like this!"
    voice "audio/voice/E6/SHI/02/YK/YK008.ogg"
    yukino "You know you won't get anything out of saying nice things at the end, right?"
    voice "audio/voice/E6/SHI/02/HA/HA020.ogg"
    hachiman "I'm not really looking to get something out of it... By the way, what are you doing over there, Hiratsuka-sensei?"
    show yui surprised
    show yukino surprised
    with dissolve
    voice "audio/voice/E6/SHI/02/YI/YI008.ogg"
    yui "Huh?"
    voice "audio/voice/E6/SHI/02/HA/HA021.ogg"
    hachiman "Eavesdropping isn't okay, Hiratsuka-sensei."
    show yui mid_left pout with dissolve:
        xoffset -270 yoffset 75
    voice "audio/voice/E6/SHI/02/YI/YI009.ogg"
    yui "Hiratsuka-sensei!?"
    window auto hide dissolve
    stop voice
    hide yui
    hide yukino
    with dissolve
    play sound "audio/sfx/SE04/SE04_01.ogg"
    $renpy.pause(delay=1.5,hard=True)
    show yukino school mid_center surprised at left:
        xoffset -170 yoffset 75
    show yui school mid_center surprised at right:
        xoffset -110 yoffset 75
    show hiratsuka school mid_center vhappy at center:
        xoffset 40 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E6/SHI/02/SZ/SZ013.ogg"
    hiratsuka "I just didn't want to ruin your touching exchange."
    voice "audio/voice/E6/SHI/02/HA/HA022.ogg"
    hachiman "You could've just come in like you always do..."
    show hiratsuka happy with dissolve
    voice "audio/voice/E6/SHI/02/SZ/SZ014.ogg"
    hiratsuka "That aside... I wanted to see it for myself. Your guys' growth. I'm glad I was your teacher from the bottom from my heart."
    show yukino vhappy
    show yui mid_left happy:
        xoffset -80 yoffset 75
    with dissolve
    voice "audio/voice/E6/SHI/02/YK/YK009.ogg"
    yukino "We're also grateful and... thank you for always watching over us."
    show hiratsuka mid_left happy with dissolve:
        xoffset 115 yoffset 80
    voice "audio/voice/E6/SHI/02/SZ/SZ015.ogg"
    hiratsuka "Fu... no need to thank me. You've grown all thanks to your own strength. Besides, it's my job to look over you."
    voice "audio/voice/E6/SHI/02/HA/HA023.ogg"
    hachiman "Well, you say that, but... don't you have other work that needs doing?"
    show yukino stare with dissolve
    voice "audio/voice/E6/SHI/02/YK/YK010.ogg"
    yukino "Come to think of it... don't you?"
    show hiratsuka unimpressed with dissolve
    voice "audio/voice/E6/SHI/02/SZ/SZ016.ogg"
    hiratsuka "Of course I wouldn't come if I wasn't free. I just really wanted to see you guys graduate."
    show yukino unimpressed
    show yui unimpressed
    with dissolve
    voice "audio/voice/E6/SHI/02/YI/YI010.ogg"
    yui "Ah... sounds dodgy."
    voice "audio/voice/E6/SHI/02/YK/YK011.ogg"
    yukino "I agree with Yuigahama-san."
    show hiratsuka blush with dissolve
    voice "audio/voice/E6/SHI/02/SZ/SZ017.ogg"
    hiratsuka "W-Why's that!? You're a bit too suspicious, you know..."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    scene white with dissolve
    window auto show dissolve
    "And so, my... our high school life was over."
    window auto hide dissolve
    show E6_SHI_03

label E6_SHI_03:
    show fancyCafeDup at topleft:
        zoom 1.8 xoffset -335 yoffset -400
    show hiratsuka home near_center happy at center:
        xoffset 30 yoffset 75
    with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/BGM26.ogg"
    window auto show dissolve
    voice "audio/voice/E6/SHI/03/SZ/SZ000.ogg"
    hiratsuka "It's been a while since the last time we were here."
    voice "audio/voice/E6/SHI/03/HA/HA000.ogg"
    hachiman "I know, right?"
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E6/SHI/03/SZ/SZ001.ogg"
    hiratsuka "Sine that one time, huh... it's nostalgic."
    voice "audio/voice/E6/SHI/03/HA/HA001.ogg"
    hachiman "Yeah... it is."
    "And so the years went by and my college life is almost over. Hiratsuka-sensei and I were at the same cafe-bar we had been in a while back."
    show hiratsuka happy with dissolve
    voice "audio/voice/E6/SHI/03/SZ/SZ002.ogg"
    hiratsuka "You're starting to look a bit more stylish now, aren't you?"
    voice "audio/voice/E6/SHI/03/HA/HA002.ogg"
    hachiman "Well... I guess."
    "I still get embarrassed thinking how I confessed my love to her back in high school, but now that I've grown older, it's a funny memory to look back on."
    voice "audio/voice/E6/SHI/03/SZ/SZ003.ogg"
    hiratsuka "Let's have a toast."
    voice "audio/voice/E6/SHI/03/HA/HA003.ogg"
    hachiman "Cheers."
    window auto hide dissolve
    show hiratsuka near_left vhappy with dissolve:
        xoffset 200 yoffset 80
    window auto show dissolve
    voice "audio/voice/E6/SHI/03/SZ/SZ004.ogg"
    hiratsuka "Phew~... cocktails go down so fast!"
    voice "audio/voice/E6/SHI/03/HA/HA004.ogg"
    hachiman "Don't go drinking too much now."
    show hiratsuka happy with dissolve
    voice "audio/voice/E6/SHI/03/SZ/SZ005.ogg"
    hiratsuka "Don't be so uptight, we're celebrating after all."
    voice "audio/voice/E6/SHI/03/HA/HA005.ogg"
    hachiman "I'm the one who's gonna have to carry you home, you know..."
    show hiratsuka near_center happy with dissolve:
        xoffset 30 yoffset 75
    voice "audio/voice/E6/SHI/03/SZ/SZ006.ogg"
    hiratsuka "You'd like that once in a while, won't you?"
    hachiman "(I've been doing it quite often, though...)"
    "Even though our relationship has changed, even though time has passed, our interactions themselves haven't changed much. It was strangely comforting."
    show hiratsuka happy with dissolve
    voice "audio/voice/E6/SHI/03/SZ/SZ007.ogg"
    hiratsuka "So... when will you take me?"
    voice "audio/voice/E6/SHI/03/HA/HA006.ogg"
    hachiman "Ah...."
    "I can't muster up a reply to sensei's teasing comment."
    hachiman "(Well, it certainly won't do to keep her waiting any longer...)"
    voice "audio/voice/E6/SHI/03/SZ/SZ008.ogg"
    hiratsuka "Well, make sure to enjoy the last of your student life."
    voice "audio/voice/E6/SHI/03/HA/HA007.ogg"
    hachiman "...I will."
    "The kindness of sensei, casually changing the topic and smiling at me, made my heart ache a little bit. I knew then she was still watching over me."
    window auto hide dissolve
    stop music fadeout 1.0
    scene outsideC
    show hiratsuka coat_night mid_left vhappy at center:
        xoffset 110 yoffset 80
    with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    voice "audio/voice/E6/SHI/03/SZ/SZ009.ogg"
    hiratsuka "Ah, that hit the spot! Thanks, that was fun."
    hachiman "(You seem like you're in a great mood... Well, I'm just glad you're happy.)"
    voice "audio/voice/E6/SHI/03/HA/HA008.ogg"
    hachiman "You're not as drunk as I thought, surprisingly."
    show hiratsuka happy with dissolve
    voice "audio/voice/E6/SHI/03/SZ/SZ010.ogg"
    hiratsuka "It'd be a shame to get drunk and forget about today."
    voice "audio/voice/E6/SHI/03/HA/HA009.ogg"
    hachiman "I see..."
    voice "audio/voice/E6/SHI/03/SZ/SZ011.ogg"
    hiratsuka "......"
    voice "audio/voice/E6/SHI/03/HA/HA010.ogg"
    hachiman "......"
    hachiman "(I don't know why I couldn't answer her earlier.)"
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E6/SHI/03/SZ/SZ012.ogg"
    hiratsuka "What's wrong, Hikigaya?"
    voice "audio/voice/E6/SHI/03/HA/HA011.ogg"
    hachiman "Nothing."
    hachiman "(In my mind, I've already decided my answer.)"
    voice "audio/voice/E6/SHI/03/HA/HA012.ogg"
    hachiman "Actually..."
    show hiratsuka mid_center happy with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E6/SHI/03/SZ/SZ013.ogg"
    hiratsuka "Hm? What's up?"
    "Perhaps noticing my serious tone, Hiratsuka-sensei turned to me with a smile. Her gentle expression seemed to be encouraging me."
    play music "audio/bgm/BGM42.ogg"
    voice "audio/voice/E6/SHI/03/HA/HA013.ogg"
    hachiman "Well... it's been a long time coming, but... will you marry me?"
    show hiratsuka surprised with dissolve
    voice "audio/voice/E6/SHI/03/SZ/SZ014.ogg"
    hiratsuka "Eh?"
    voice "audio/voice/E6/SHI/03/HA/HA014.ogg"
    hachiman "I'm sorry I couldn't... answer you right away before."
    show hiratsuka blush with dissolve
    voice "audio/voice/E6/SHI/03/SZ/SZ015.ogg"
    hiratsuka "Oh, you, um... you don't need to take that seriously, you know?"
    voice "audio/voice/E6/SHI/03/HA/HA015.ogg"
    hachiman "But I'm serious about this."
    "When I looked her straight in the eye and told her so, her cheeks turned all red at once. She is usally so stoic, but I think this disparity is very cute."
    voice "audio/voice/E6/SHI/03/SZ/SZ016.ogg"
    hiratsuka "A-Are you sure... you're fine with me?"
    voice "audio/voice/E6/SHI/03/HA/HA016.ogg"
    hachiman "I told you, didn't I? If there's ever someone I want to hurt in order to really know, it's you... Shizuka-san."
    "For the first time, I called her by her first name. It's not like it wasn't embarrassing, but... right now, the sound of her name is really dear to me."
    window auto hide dissolve
    hide hiratsuka with dissolve
    $renpy.pause(delay=0.5,hard=True)
    play sound "audio/sfx/SE01/SE01_12.ogg"
    scene hiratsukaHachimanKissa with dissolve
    window auto show dissolve
    "I hugged her gently and was surprised. For someone so stoic and manly, she's really delicate. As if in response, she softly places her hands on my cheek."
    voice "audio/voice/E6/SHI/03/SZ/SZ017.ogg"
    hiratsuka "We're not student and teacher anymore."
    voice "audio/voice/E6/SHI/03/HA/HA017.ogg"
    hachiman "Come to think of it, we haven't been for a while now."
    show hiratsukaHachimanKissc with dissolve
    voice "audio/voice/E6/SHI/03/SZ/SZ018.ogg"
    hiratsuka "Hikigaya..."
    voice "audio/voice/E6/SHI/03/HA/HA018.ogg"
    hachiman "I'm sorry I made you wait so long."
    show hiratsukaHachimanKissb with dissolve
    voice "audio/voice/E6/SHI/03/SZ/SZ019.ogg"
    hiratsuka "Thank you... Hachiman."
    "And then... we hugged each other, and kissing softy, with genuine affection between us."
    show hiratsukaHachimanKissd with dissolve
    voice "audio/voice/E6/SHI/03/HA/HA019.ogg"
    hachiman "Let's be together from now on, Shizuka-san."
    voice "audio/voice/E6/SHI/03/SZ/SZ020.ogg"
    hiratsuka "Yes... let's. Let's be together, now and always."
    window auto hide dissolve
    stop voice fadeout 1.0
    stop music fadeout 1.0
    show white with Fade(2.0, 0, 1.0, color="#fff")
    $renpy.movie_cutscene("movies/ed04.mkv")
    jump E6_SHI_04

label E6_SHI_04:
    scene hiratsukaHachimanWeddinga with Fade(1.0, 0.5, 1.5)
    play music "audio/bgm/BGM51.ogg"
    window auto show dissolve
    voice "audio/voice/E6/SHI/04/HA/HA000.ogg"
    hachiman "Job-hunting is so much tougher than I imagined. I don't think I'll ever get a job..."
    voice "audio/voice/E6/SHI/04/SZ/SZ000.ogg"
    hiratsuka "Well, that's true. Life's not easy."
    "Shizuka was so on the money I couldn't even reply and that's exactly why it struck home with me. Apparently, finding a job is quite difficult."
    voice "audio/voice/E6/SHI/04/HA/HA001.ogg"
    hachiman "I guess being a full-time husband might have to be the way to go after all."
    voice "audio/voice/E6/SHI/04/SZ/SZ001.ogg"
    hiratsuka "You're still on about that?"
    "We exchanged light-hearted remarks and smiled at each other."
    voice "audio/voice/E6/SHI/04/HA/HA002.ogg"
    hachiman "So, will you let me hear your story?"
    voice "audio/voice/E6/SHI/04/SZ/SZ002.ogg"
    hiratsuka "It's just a story of \"What-Ifs\" and \"Could-Have-Beens\", so why bother about it?"
    "I'm captivated by Shizuka tilting her glass, mischievous smile on her face. To me, she will always be this brawny, pretty and mature woman."
    voice "audio/voice/E6/SHI/04/HA/HA003.ogg"
    hachiman "Still, if it's your story, I'd like to hear it."
    voice "audio/voice/E6/SHI/04/SZ/SZ003.ogg"
    hiratsuka "Well, some day you will."
    show hiratsukaHachimanWeddingb with dissolve
    "As she said this, Shizuka put her hand on my own, looked at me and smiled gently."
    voice "audio/voice/E6/SHI/04/SZ/SZ004.ogg"
    hiratsuka "Right now, we can talk about the story that did come true."
    voice "audio/voice/E6/SHI/04/HA/HA004.ogg"
    hachiman "Yeah, you're right..."
    "I grasped her hand tightly back, as if to confirm it's actually there."
    voice "audio/voice/E6/SHI/04/SZ/SZ005.ogg"
    hiratsuka "That's right, I'd love to hear about you from back in the day."
    voice "audio/voice/E6/SHI/04/HA/HA005.ogg"
    hachiman "Huh?"
    voice "audio/voice/E6/SHI/04/SZ/SZ006.ogg"
    hiratsuka "I guess being an adult isn't bad after all, huh?"
    hachiman "(She's asking some malicious question...)"
    voice "audio/voice/E6/SHI/04/HA/HA006.ogg"
    hachiman "Well, what is there to hear? I'm the same now as I was back then."
    "That was only half the truth. Thanks to her, I've really changed. But at the end of the day, I'm still me."
    "If being able to honestly accept myself as such is called \"becoming an adult,\" then I think it might not be so bad."
    voice "audio/voice/E6/SHI/04/SZ/SZ007.ogg"
    hiratsuka "Well, people can't just change who they really are after all."
    voice "audio/voice/E6/SHI/04/HA/HA007.ogg"
    hachiman "...That's right."
    voice "audio/voice/E6/SHI/04/IR/IR000.ogg"
    mystery "Hey! Come on, senpai! You too, Hiratsuka-sensei!"
    voice "audio/voice/E6/SHI/04/HA/HA008.ogg"
    hachiman "Huh?"
    voice "audio/voice/E6/SHI/04/SZ/SZ008.ogg"
    hiratsuka "Eh?"
    voice "audio/voice/E6/SHI/04/MI/MIX000.ogg"
    hachiandhira "Huh....?"
    show hiratsukaHachimanWeddingc with dissolve
    voice "audio/voice/E6/SHI/04/IR/IR001.ogg"
    iroha "What are you two doing, going of into your own little world at the after-party."
    voice "audio/voice/E6/SHI/04/HA/HA009.ogg"
    hachiman "Ah, sorry..."
    voice "audio/voice/E6/SHI/04/SZ/SZ009.ogg"
    hiratsuka "I-I'm sorry about that."
    "We both apologized. Yes, it was actually Shizuka and I's wedding today. And right now, we were in the middle of the after-party."
    voice "audio/voice/E6/SHI/04/YI/YI000.ogg"
    yui "Hikki, maybe this is what it means to be a full-time househusband after all~?"
    voice "audio/voice/E6/SHI/04/HA/HA010.ogg"
    hachiman "...I hope so."
    voice "audio/voice/E6/SHI/04/SZ/SZ010.ogg"
    hiratsuka "Huff... well what are we going to do if I can't support him by myself?"
    voice "audio/voice/E6/SHI/04/YK/YK000.ogg"
    yukino "With all due respect, please be careful not to say heedless things and go on to spoil him."
    voice "audio/voice/E6/SHI/04/KO/KO000.ogg"
    komachi "Komachi agrees with you~!"
    voice "audio/voice/E6/SHI/04/HA/HA011.ogg"
    hachiman "Uh....."
    hachiman "(Yukinoshita and my sister are as strict as ever...)"
    voice "audio/voice/E6/SHI/04/SZ/SZ011.ogg"
    hiratsuka "Haha... you might be right."
    voice "audio/voice/E6/SHI/04/HR/HR000.ogg"
    haruno "Hikigaya-kun, if you're gonna run away, now's the time to do it."
    voice "audio/voice/E6/SHI/04/SZ/SZ012.ogg"
    hiratsuka "Wha- Haruno, what are you saying!? Ramen enthuiasts have an unbreakable bond!"
    hachiman "(You're freaking out a bit too much... How could I ever run away now?)"
    voice "audio/voice/E6/SHI/04/YK/YK001.ogg"
    yukino "Nee-san, this man is not going to give up his full-time househusband job once he gets it."
    "Old and familiar faces are reunited at our marriage, giving us their blessings from the bottom of their heart... or at least I hope so. I want to think so."
    voice "audio/voice/E6/SHI/04/HA/HA012.ogg"
    hachiman "I somehow feel like all you have a lot to say..."
    voice "audio/voice/E6/SHI/04/HY/HY000.ogg"
    hayama "That's fine, isn't it? It means you're well-liked by everyone."
    voice "audio/voice/E6/SHI/04/HA/HA013.ogg"
    hachiman "Just because it's you saying it, I feel less like believing it."
    voice "audio/voice/E6/SHI/04/HR/HR001.ogg"
    haruno "Hayato, you got told off again."
    voice "audio/voice/E6/SHI/04/SI/SI000.ogg"
    totsuka "Nevertheless, I think congratulations are in order. I think you make a great couple."
    voice "audio/voice/E6/SHI/04/YI/YI001.ogg"
    yui "Hahaha, they really do."
    voice "audio/voice/E6/SHI/04/IR/IR002.ogg"
    iroha "Now then, one more time..."
    voice "audio/voice/E6/SHI/04/MI/MIX001.ogg"
    evb "Congratulations!"
    window auto hide dissolve
    stop voice
    stop music fadeout 2.0
    scene hiratsukaEnding with Fade(2.0, 1.0, 1.0, color="#fff")
    call game_over("Hiratsuka Shizuka") from _call_game_over_3
    return
