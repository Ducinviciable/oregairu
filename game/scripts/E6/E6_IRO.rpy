label E6_IRO_01:
    scene clubroomB
    show yukino school_sunset mid_center vhappy at left:
        xoffset 25 yoffset 75
    show yui school_sunset mid_center vhappy at right:
        xoffset -300 yoffset 75
    with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/BGM08.ogg"
    window auto show dissolve
    voice "audio/voice/E6/IRO/01/YI/YI000.ogg"
    yui "Eeeeh? So Komachi-chan passed!"
    voice "audio/voice/E6/IRO/01/HA/HA000.ogg"
    hachiman "Yeah. She nearly fainted and fell over the second she saw the results."
    voice "audio/voice/E6/IRO/01/YK/YK000.ogg"
    yukino "That's a very normal reaction given how hard she worked for it."
    show yui mid_left happy with dissolve:
        xoffset -270 yoffset 75
    voice "audio/voice/E6/IRO/01/YI/YI001.ogg"
    yui "You say that, Yukinon, but you were anxious until Hikki told us the news!"
    show yukino pout with dissolve
    voice "audio/voice/E6/IRO/01/YK/YK001.ogg"
    yukino "T-That's..."
    show yui vhappy with dissolve
    voice "audio/voice/E6/IRO/01/YI/YI002.ogg"
    yui "Heehee, it kinda feels like Komachi-chan is everyone's little sister~"
    voice "audio/voice/E6/IRO/01/HA/HA001.ogg"
    hachiman "Wait a minute, Komachi is MY younger sister. Besides, if she was everyone's little sister, a war would break out over her so I'll keep her to myself. Even if you guys find some other little sister somewhere "
    voice sustain
    hachiman "else, make sure you guys continue being nice to Komachi, okay?"
    show yukino unimpressed with dissolve
    voice "audio/voice/E6/IRO/01/YK/YK002.ogg"
    yukino "Why did Komachi-san choose a high school with an older brother like this in it..."
    window auto hide dissolve
    stop voice
    hide yukino
    hide yui
    with dissolve
    $renpy.pause(delay=0.25, hard=True)
    stop music
    play sound "audio/sfx/SE04/SE04_00.ogg"
    $renpy.pause(delay=1.0, hard=True)
    show yukino school_sunset mid_center vhappy at left:
        xoffset -105 yoffset 75
    show iroha school_sunset mid_center vhappy at center:
        xoffset -5 yoffset 75
    show yui school_sunset mid_left vhappy at right:
        xoffset -150 yoffset 75
    with dissolve
    $renpy.pause(delay=0.5, hard=True)
    play music "audio/bgm/BGM36.ogg"
    window auto show dissolve
    voice "audio/voice/E6/IRO/01/IR/IR000.ogg"
    iroha "Good afternoon, everyone!"
    stop sound
    voice "audio/voice/E6/IRO/01/YI/YI003.ogg"
    yui "Ah, Iroha-chan! Yahallo~!"
    voice "audio/voice/E6/IRO/01/YK/YK003.ogg"
    yukino "Good afternoon, Isshiki-san."
    voice "audio/voice/E6/IRO/01/HA/HA002.ogg"
    hachiman "Did you need something?"
    show iroha happy with dissolve
    voice "audio/voice/E6/IRO/01/IR/IR001.ogg"
    iroha "Yes! So, I'll be borrowing senpai for a bit, okay?"
    show yukino surprised
    show yui surprised
    with dissolve
    voice "audio/voice/E6/IRO/01/HA/HA003.ogg"
    hachiman "Wait, what? Just me?"
    voice "audio/voice/E6/IRO/01/IR/IR002.ogg"
    iroha "Well, yeah. I want to choose with you, senpai."
    voice "audio/voice/E6/IRO/01/HA/HA004.ogg"
    hachiman "I'm not quite following, but... choose what, exactly?"
    hide iroha with dissolve
    show iroha school_sunset near_center vhappy at center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E6/IRO/01/IR/IR003.ogg"
    iroha "Alrighty then, let's go, senpai! Here, hold this!"
    voice "audio/voice/E6/IRO/01/HA/HA005.ogg"
    hachiman "H-hey, wai--"
    show iroha near_left vhappy with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E6/IRO/01/IR/IR004.ogg"
    iroha "Anyway, sorry for the interruption!"
    window auto hide dissolve
    stop voice
    hide iroha with dissolve
    show black with Fade(0.5, 0, 0)
    play sound "audio/sfx/SE04/SE04_00.ogg"
    hide yukino
    hide yui
    show yukino school_sunset mid_center vhappy at left:
        xoffset 25 yoffset 75
    show yui school_sunset mid_left vhappy at right:
        xoffset -270 yoffset 75
    hide black 
    with Fade(0, 2.0, 0.5)
    window auto show dissolve
    voice "audio/voice/E6/IRO/01/YI/YI004.ogg"
    yui "We're getting used to seeing this sort of thing, aren't we?"
    voice "audio/voice/E6/IRO/01/YK/YK004.ogg"
    yukino "Yeah, we really are."
    voice "audio/voice/E6/IRO/01/IR/IR005.ogg"
    window auto hide dissolve
    scene mallB
    show iroha school near_left vhappy at center:
        xoffset 260 yoffset 75
    with Fade(0.5, 0.5, 0.5)
    play ambient "audio/sfx/SE05/SE05_01L.ogg"
    window auto show dissolve
    iroha "Senpaaai, hurry up!"
    hide iroha with dissolve
    play sound "audio/sfx/SE00/SE00_01.ogg"
    "Without receiving any details on what's going on, I was brought to the shopping center in front of the station."
    stop sound
    show iroha school far_left vhappy at center with dissolve:
        xoffset -25 yoffset 80
    voice "audio/voice/E6/IRO/01/IR/IR006.ogg"
    iroha "Ah, what a relief. There's still some left!"
    window auto hide dissolve
    stop voice
    scene mallB at right:
        zoom 1.5 xoffset 0 yoffset 175
    show iroha school mid_left vhappy at center:
        xoffset -35 yoffset 65
    with dissolve
    window auto show dissolve
    "Isshiki had run up to an accessory store filled with sparkles as far as the eye could see. A typical shop that catered to girls."
    voice "audio/voice/E6/IRO/01/HA/HA006.ogg"
    hachiman "By \"choose\" earlier, were you talking about these rings?"
    show iroha mid_center happy with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E6/IRO/01/IR/IR007.ogg"
    iroha "Yeah, there's a limited-time sale today!"
    voice "audio/voice/E6/IRO/01/HA/HA007.ogg"
    hachiman "Ah...I see."
    show iroha mid_left angry with dissolve:
        xoffset -35 yoffset 65
    voice "audio/voice/E6/IRO/01/IR/IR008.ogg"
    iroha "Hm...between these two, which do you think looks better?"
    voice "audio/voice/E6/IRO/01/HA/HA008.ogg"
    hachiman "Is this a game of spot the difference or something? They look identical."
    show iroha frown with dissolve
    voice "audio/voice/E6/IRO/01/IR/IR009.ogg"
    iroha "Eh? Okay, well what about these?"
    voice "audio/voice/E6/IRO/01/HA/HA009.ogg"
    hachiman "There isn't really a big difference between those either... why not just buy all the ones you like and put 'em all on at the same time? You'd look super tough."
    hide iroha
    $url = ["iroha school mid_center angry", "iroha school mid_left vhappy"]
    $multiImagePara = [-5, 75, -35, 65, 3.75]
    call multiImage(0, False) from _call_multiImage_84
    voice "audio/voice/E6/IRO/01/IR/IR010.ogg"
    iroha "I'm not trying to look tough; I'm trying to look cute, y'know. Ooh, this one's cute too!!"
    call finishmultiImage from _call_finishmultiImage_88
    with dissolve
    "With sparkles in her eyes, Isshiki went from display to display looking for cute things. I had to admit, watching her facial expression constantly switch between excitement and worry as she searched was "
    "super amusing."
    show iroha school near_center vhappy at center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E6/IRO/01/IR/IR011.ogg"
    iroha "Okay, senpai. Between this one and this one, which one do you think is better? You can make a choice based on your preferences or intuition or whatever you want."
    "Isshiki held out her hands, wearing rings on two different fingers, patiently waiting for my opinion."
    "As I looked carefully, I could surprisingly see that there were a few differences."
    voice "audio/voice/E6/IRO/01/HA/HA010.ogg"
    hachiman "Ah...well, I don't really know much about sort of thing, but I feel like this one looks better."
    "After careful comparison, I chose the pale pink ring decorated with glass beads on her left index finger."
    show iroha surprised with dissolve
    voice "audio/voice/E6/IRO/01/IR/IR012.ogg"
    iroha "Why do you say that?"
    voice "audio/voice/E6/IRO/01/HA/HA011.ogg"
    hachiman "Hmm, I think this one just suits you more. It sorta screams \"Isshiki Iroha\", I guess."
    show iroha blush with dissolve
    voice "audio/voice/E6/IRO/01/IR/IR013.ogg"
    iroha "...!"
    show iroha vhappy with dissolve
    voice "audio/voice/E6/IRO/01/IR/IR014.ogg"
    iroha "Is that so? I'll get this one then!"
    hide iroha with dissolve
    play sound "audio/sfx/SE00/SE00_01.ogg"
    "With a wide grin plastered on her face, Isshiki hurried to the counter."
    voice "audio/voice/E6/IRO/01/HA/HA012.ogg"
    hachiman "............"
    window auto hide dissolve
    stop voice
    stop sound
    scene mallB with Fade(0.5, 0.5, 0.5)
    $renpy.pause(delay=0.5, hard=True)
    show iroha school mid_center vhappy at center with dissolve:
        xoffset -5 yoffset 75
    window auto show dissolve
    voice "audio/voice/E6/IRO/01/IR/IR015.ogg"
    iroha "Sorry to keep you waiting~!"
    voice "audio/voice/E6/IRO/01/HA/HA013.ogg"
    hachiman "............"
    show iroha happy with dissolve
    voice "audio/voice/E6/IRO/01/IR/IR016.ogg"
    iroha "What's wrong?"
    voice "audio/voice/E6/IRO/01/HA/HA014.ogg"
    hachiman "Isn't this the part where you try to make me pay for the ring as some kinda joke?"
    voice "audio/voice/E6/IRO/01/HA/HA015.ogg"
    hachiman "I mean, this is you we're talking about here. You and Komachi try to talk me into promising to do what you want in times like these, even when I clearly point it out that I'm not going to do it."
    stop music fadeout 0.5
    stop ambient fadeout 0.5
    show iroha frown with dissolve
    voice "audio/voice/E6/IRO/01/IR/IR017.ogg"
    iroha "............"
    voice "audio/voice/E6/IRO/01/HA/HA016.ogg"
    hachiman "Eh? What's wrong?"
    voice "audio/voice/E6/IRO/01/IR/IR018.ogg"
    iroha "............"
    show iroha unimpressed with dissolve
    voice "audio/voice/E6/IRO/01/IR/IR019.ogg"
    iroha "Haah..."
    show iroha mid_left unimpressed with dissolve:
        xoffset -35 yoffset 65
    voice "audio/voice/E6/IRO/01/IR/IR020.ogg"
    iroha "This is my fault, huh... I did act that way after all..."
    show iroha mid_center happy with dissolve:
        xoffset -5 yoffset 75
    play music "audio/bgm/BGM42.ogg"
    voice "audio/voice/E6/IRO/01/IR/IR021.ogg"
    iroha "Well, senpai, I didn't try that this time because I didn't want you to think that was my goal."
    voice "audio/voice/E6/IRO/01/IR/IR022.ogg"
    iroha "I didn't want just any ring. I wanted one that you chose, senpai."
    "Hearing that, my gaze was drawn to Isshiki's hand."
    "The ring she had just bought was sparkling on it."
    voice "audio/voice/E6/IRO/01/HA/HA018.ogg"
    hachiman "............"
    show iroha vhappy with dissolve
    "I couldn't find the words to reply, and Isshiki flashed me her usual smile."
    voice "audio/voice/E6/IRO/01/IR/IR023.ogg"
    iroha "Besides, doesn't the idea that I wanted a ring you chose so badly that I bought it myself have a nice ring to it? You don't seem like the type to like a girl that makes you buy her presents, anyway, senpai."
    voice "audio/voice/E6/IRO/01/HA/HA019.ogg"
    hachiman "Just gonna give it to me straight, huh?"
    show iroha happy with dissolve
    voice "audio/voice/E6/IRO/01/IR/IR024.ogg"
    iroha "You made me say it, senpai, 'cause you're so quick to doubt what others say."
    voice "audio/voice/E6/IRO/01/HA/HA020.ogg"
    hachiman "Yep, that's true."
    show iroha angry with dissolve
    voice "audio/voice/E6/IRO/01/IR/IR025.ogg"
    iroha "I'm not Komachi-chan, so you don't get it unless I spell it out for you like that."
    voice "audio/voice/E6/IRO/01/HA/HA021.ogg"
    hachiman "............"
    voice "audio/voice/E6/IRO/01/HA/HA022.ogg"
    hachiman "...Is that so?"
    show iroha happy with dissolve
    voice "audio/voice/E6/IRO/01/IR/IR026.ogg"
    iroha "Yep."
    voice "audio/voice/E6/IRO/01/HA/HA023.ogg"
    hachiman "............"
    voice "audio/voice/E6/IRO/01/HA/HA024.ogg"
    hachiman "Well, uh, do you..  wanna stop by a cafe on the way back?"
    show iroha vhappy with dissolve
    voice "audio/voice/E6/IRO/01/IR/IR027.ogg"
    iroha "Yeah!"
    "I felt like it would be a waste to just head back home now."
    "I wanted to talk to Isshiki more, even if it meant talking about trivial things."
    "That's because I decided to stop dodging and face my feelings head-on."
    "She isn't just \"a girl like my little sister,\" she's a girl named Isshiki Iroha."
    "And I..."
    window auto hide dissolve
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    jump E6_IRO_02

label E6_IRO_02:
    scene waterPark with Fade(0.5, 1.0, 0.5)
    play ambient "audio/sfx/SE05/SE05_00L.ogg"
    "The snow fell from the sky like dancing flower petals."
    "The wide sidewalk by the station led to the nearby aquarium, and was incredibly crowded with couples and parents with their children."
    "Of course, I'm going to the aquarium, too. Isshiki had invited me by asking \"Why don't we go during our next day off?\""
    window auto hide dissolve
    scene waterPark at center with dissolve:
        zoom 2.0 xoffset 310 yoffset 40
    window auto show dissolve
    hachiman "(Did I arrive too early...?)"
    "I check my watch as I stand in front of the dome-shaped building. I'm fifteen minutes early."
    "Feeling like I might be waiting a while, I make my way to the entrance. As I do--"
    window auto hide dissolve
    scene waterPark
    show iroha coat mid_left surprised at center:
        xoffset -5 yoffset 65
    with dissolve
    window auto show dissolve
    voice "audio/voice/E6/IRO/02/IR/IR000.ogg"
    iroha "Ah."
    voice "audio/voice/E6/IRO/02/HA/HA000.ogg"
    hachiman "Oh."
    play music "audio/bgm/BGM36.ogg"
    "Isshiki had come over from the other side, and we had both arrived at the same time."
    show iroha mid_center pout with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E6/IRO/02/HA/HA001.ogg"
    hachiman "Aren't you a bit early?"
    show iroha frown with dissolve
    voice "audio/voice/E6/IRO/02/IR/IR001.ogg"
    iroha "That's my line. I wanted to come before you, and here you are wasting my efforts. Why don't you go back home to get something you forgot so I can be first?"
    voice "audio/voice/E6/IRO/02/HA/HA002.ogg"
    hachiman "Whaaat... you're this mad over fifteen minutes? Also, it's not like I did something wrong... right?"
    show iroha angry with dissolve
    voice "audio/voice/E6/IRO/02/IR/IR002.ogg"
    iroha "I'll have you know that to a teenage girl, fifteen minutes are incredibly important! You can't compare that to a teenage boy or even a woman in her twenties or thirties!"
    voice "audio/voice/E6/IRO/02/HA/HA003.ogg"
    hachiman "You better not say that in front of Hiratsuka-sensei. That would not only hurt her, but you might get hurt, too."
    show iroha unimpressed with dissolve
    voice "audio/voice/E6/IRO/02/IR/IR003.ogg"
    iroha "Well, whatever."
    "Isshiki sighed and began fixing her hair."
    "As she did so, I could see a glint coming from a familiar ring on her finger."
    hachiman "(Huh, she looks surprisingly happy with it.)"
    show iroha vhappy with dissolve
    voice "audio/voice/E6/IRO/02/IR/IR004.ogg"
    iroha "Shall we get going? On our aquarium date~!"
    window auto hide dissolve
    stop voice
    stop ambient fadeout 0.5
    scene aquarium
    show iroha coat_blue mid_left vhappy at center:
        xoffset -5 yoffset 65
    with Fade(0.5, 1.0, 0.5)
    play ambient "audio/sfx/SE00/SE00_18L.ogg"
    window auto show dissolve
    voice "audio/voice/E6/IRO/02/IR/IR005.ogg"
    iroha "Waaaah, it's so pretty!"
    voice "audio/voice/E6/IRO/02/HA/HA004.ogg"
    hachiman "Yeah, it's quite a sight."
    "We continued to look around in awe as we went from display to display, admiring the various saltwater fish and illuminated water tanks in the aquarium."
    show iroha mid_center happy with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E6/IRO/02/IR/IR006.ogg"
    iroha "Ah, senpai! The freshwater fish area is over here. That's gotta be full of trout and sweetfish!"
    voice "audio/voice/E6/IRO/02/HA/HA005.ogg"
    hachiman "Ooh, sounds delicious."
    show iroha unimpressed with dissolve
    voice "audio/voice/E6/IRO/02/IR/IR007.ogg"
    iroha "I mean, yeah, but you can't say that in an aquarium."
    hachiman "(So, it's all over for me now, huh.)"
    show iroha mid_left happy with dissolve:
        xoffset -5 yoffset 65
    voice "audio/voice/E6/IRO/02/IR/IR008.ogg"
    iroha "Senpai, senpai, look! It's a sakura salmon!"
    voice "audio/voice/E6/IRO/02/HA/HA006.ogg"
    hachiman "Oh! Sakura salmon!"
    "I leaned closer to the plaque by the display. It explained that the name \"sakura salmon\" comes from; many of these salmon being caught around the blooming of sakura in spring. Their scales also become the "
    "\"cherry blossom color of marriage\" when they mature, apparently."
    show iroha vhappy with dissolve
    voice "audio/voice/E6/IRO/02/IR/IR009.ogg"
    iroha "\"The cherry blossom color of marriage\" sounds rather wonderful, doesn't it?"
    voice "audio/voice/E6/IRO/02/HA/HA007.ogg"
    hachiman "Well, it's a pretty color, but it's actually a lot darker in actuality. People say that the sakura salmon are two-faced, too."
    show iroha mid_center surprised with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E6/IRO/02/IR/IR010.ogg"
    iroha "Huh? Is that really true?"
    voice "audio/voice/E6/IRO/02/HA/HA008.ogg"
    hachiman "Yeah. Some go out to sea, while others spend their whole lives in freshwater streams. Two different lifestyles despite being the same species of fish."
    hide iroha
    $url = ["iroha coat_blue mid_center surprised", "iroha coat_blue mid_center vhappy"]
    $multiImagePara = [20, 75, 0, 0, 1.4]
    call multiImage() from _call_multiImage_85
    voice "audio/voice/E6/IRO/02/IR/IR011.ogg"
    iroha "Ah, so that's why you know a lot about the sakura salmon, senpai."
    call finishmultiImage from _call_finishmultiImage_89
    show iroha coat_blue mid_center happy at center:
        xoffset 20 yoffset 75
    with dissolve
    voice "audio/voice/E6/IRO/02/IR/IR012.ogg"
    iroha "Spending their whole lives in freshwater streams sounds an awful lot like living at home your entire life, doesn't it? I see you're empathizing with the fish, huh?"
    hachiman "(It's not necessarily a bad thing when a girl is quick-witted, but sometimes it sucks when they hit you where it hurts...)"
    show iroha mid_left angry with dissolve:
        xoffset -5 yoffset 65
    voice "audio/voice/E6/IRO/02/IR/IR013.ogg"
    iroha "But having two faces, huh..."
    show iroha happy with dissolve
    voice "audio/voice/E6/IRO/02/IR/IR014.ogg"
    iroha "I can kind of relate."
    voice "audio/voice/E6/IRO/02/HA/HA009.ogg"
    hachiman "............"
    voice "audio/voice/E6/IRO/02/HA/HA010.ogg"
    hachiman "That's because you're two-faced, Isshiki."
    show iroha mid_center vhappy with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E6/IRO/02/IR/IR015.ogg"
    iroha "True! But that's just how girls are, no? That's what makes us cute!"
    voice "audio/voice/E6/IRO/02/HA/HA011.ogg"
    hachiman "You may be right."
    window auto hide dissolve
    stop voice
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    jump E6_IRO_03

label E6_IRO_03:
    scene aquarium
    show iroha coat_blue mid_left vhappy at center:
        xoffset -5 yoffset 65
    with Fade(0.5, 1.0, 0.5)
    play music "audio/bgm/BGM10.ogg"
    window auto show dissolve
    "We kept walking through the aquarium until we arrived in front of an exceptionally large tank. It was filled with an enormous kelp that swayed through the water."
    show iroha vhappy with dissolve
    voice "audio/voice/E6/IRO/03/IR/IR000.ogg"
    iroha "Waaah! It's so mystical and mysterious-looking!"
    voice "audio/voice/E6/IRO/03/HA/HA000.ogg"
    hachiman "Even seaweed is fascinating, huh?"
    voice "audio/voice/E6/IRO/03/IR/IR001.ogg"
    iroha "Hehe, look between the seaweed! There's tons of tiny little fishes in the spaces between."
    voice "audio/voice/E6/IRO/03/HA/HA001.ogg"
    hachiman "Yeah... it must be nice being a fish. Drifting around all day without a care in the world."
    voice "audio/voice/E6/IRO/03/HA/HA002.ogg"
    hachiman "Alright, I've decided. I'm gonna be a stay-at-home dad one day."
    show iroha unimpressed with dissolve
    voice "audio/voice/E6/IRO/03/IR/IR002.ogg"
    iroha "Please don't make a decision like that from looking at fish."
    show iroha mid_center unimpressed with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E6/IRO/03/IR/IR003.ogg"
    iroha "Besides, being a stay-at-home dad is hard work, you know. Can you even do housework like cooking or laundry, senpai?"
    voice "audio/voice/E6/IRO/03/HA/HA003.ogg"
    hachiman "I've got the knowledge, but no experience."
    voice "audio/voice/E6/IRO/03/IR/IR004.ogg"
    iroha "There's no point in having the knowledge if you're not gonna use it, though."
    voice "audio/voice/E6/IRO/03/HA/HA004.ogg"
    hachiman "Well, what about you? Forget cooking, do you know how to clean, do laundry, save money, or save money?"
    hide iroha
    $url = ["iroha coat_blue mid_center happy", "iroha coat_blue mid_center unimpressed"]
    $multiImagePara = [20, 75, 0, 0, 3.3]
    call multiImage() from _call_multiImage_86
    voice "audio/voice/E6/IRO/03/IR/IR005.ogg"
    iroha "I'm as good at housework as the average person. Hang on, why did you say mention saving money twice? I'm not some huge spender, you know."
    call finishmultiImage from _call_finishmultiImage_90
    show iroha coat_blue mid_center unimpressed at center:
        xoffset 20 yoffset 75
    with dissolve
    hachiman "(I mean, you're pretty close. Well... not recently, I guess.)"
    hachiman "(Now that I think about it, she was really good at making beds during the ski trip...)"
    voice "audio/voice/E6/IRO/03/HA/HA005.ogg"
    hachiman "Well, sounds like you might make a good wife someday."
    show iroha angry with dissolve
    voice "audio/voice/E6/IRO/03/IR/IR006.ogg"
    iroha "Eh? {size=45}What was that,{size=40}{size=35} senpai? Was that perhaps a roundabout way of proposing to me? Please stop it. I can't believe how frugal of a husband you would be, especially when you haven't started working yet. And you don't even "
    voice sustain
    iroha "{size=35}meet the bare minimum in terms of housework ability,{size=40}so I'm {size=45}sorry {size=50}but I refuse"
    voice "audio/voice/E6/IRO/03/HA/HA006.ogg"
    hachiman "O-okay..."
    show iroha annoyed with dissolve
    voice "audio/voice/E6/IRO/03/IR/IR007.ogg"
    iroha "Jeez, you jump to conclusions so fast, senpai!"
    hachiman "(Hang on; I'm the one jumping to conclusions here?)"
    "As I gaze out upon the aquarium tanks, I couldn't help but smile."
    stop music
    show iroha mid_left angry with dissolve:
        xoffset -5 yoffset 65
    voice "audio/voice/E6/IRO/03/IR/IR008.ogg"
    iroha "............"
    "As I did so, Isshiki suddenly asked me a question."
    voice "audio/voice/E6/IRO/03/IR/IR009.ogg"
    iroha "Hey, senpai. Did you ever find the \"real thing\" you were searching for?"
    voice "audio/voice/E6/IRO/03/HA/HA007.ogg"
    hachiman "Uh--"
    play music "audio/bgm/BGM46.ogg"
    "I felt a sharp pang in my chest."
    "The \"real thing\", huh. The thing I had been pursuing from the start."
    voice "audio/voice/E6/IRO/03/IR/IR010.ogg"
    iroha "............"
    "Isshiki observed me without saying a word."
    voice "audio/voice/E6/IRO/03/HA/HA008.ogg"
    hachiman "............"
    show iroha mid_center angry with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E6/IRO/03/IR/IR011.ogg"
    iroha "I've... already found mine."
    "Her expression was crystal clear, and it made me choke on my words."
    jump E6_IRO_04

label E6_IRO_04:
    voice "audio/voice/E6/IRO/04/HA/HA000.ogg"
    hachiman "Your \"real thing\"..."
    voice "audio/voice/E6/IRO/04/IR/IR000.ogg"
    iroha "Yes."
    show iroha happy with dissolve
    voice "audio/voice/E6/IRO/04/IR/IR001.ogg"
    iroha "Senpai, there's snow in your hair."
    voice "audio/voice/E6/IRO/04/HA/HA001.ogg"
    hachiman "Huh? Snow?."
    show iroha vhappy with dissolve
    voice "audio/voice/E6/IRO/04/IR/IR002.ogg"
    iroha "I'll get it for you, so don't move."
    hachiman "(Snow should have melted a long time ago, though.)"
    hide iroha with dissolve
    show iroha coat_blue near_center happy at center with dissolve:
        xoffset -15 yoffset 75
    "I felt like it was a little odd, but Isshiki pressed down hard on my shoulder to reach the snow on my head."
    "I decided to crouch down a bit to make things easier for her."
    window auto hide dissolve
    stop music fadeout 0.5
    #figure out close eyes effect. might need to create a new ImageDissolve
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
    "Then, in that instant--"
    window auto hide dissolve
    show irohaAquariumA at center:
        zoom 1.75 xoffset 425 yoffset 150
    show transition_2a at truecenter:
        yoffset -450
    show transition_2b at truecenter:
        yoffset 450
    with Dissolve(1.0)
    play ambient "audio/sfx/SE02/SE02_18L.ogg"
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    "I felt a soft chest touching mine."
    "Then, I felt the warmth of soft lips pressed against my own."
    voice "audio/voice/E6/IRO/04/HA/HA002.ogg"
    hachiman "...!?"
    window auto hide dissolve
    stop ambient
    hide irohaAquariumA
    show irohaAquariumA
    hide transition_2a
    hide transition_2b
    with Dissolve(1.0)
    $renpy.pause(delay=0.5, hard=True)
    play music "audio/bgm/BGM42.ogg"
    window auto show dissolve
    voice "audio/voice/E6/IRO/04/IR/IR003.ogg"
    iroha "............"
    "Her rose-tinted cheeks, bashful expression, and glossy lips were right in front of my eyes."
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_12.ogg"
    show irohaAquariumB at topleft with dissolve:
        zoom 1.5
    window auto show dissolve
    "Isshiki gently embraced me as she whispered softly."
    "We were so close that I could hear her heartbeat."
    "It was ridiculously fast, as if the sound itself was trying to tell me something."
    play ambient "audio/sfx/SE02/SE02_18L.ogg"
    voice "audio/voice/E6/IRO/04/IR/IR004.ogg"
    iroha "When I'm next to you, senpai, I feel like I can be the real me."
    voice "audio/voice/E6/IRO/04/IR/IR005.ogg"
    iroha "You saw the way I act in public and private, my lies and my truths, and stuck by me."
    voice "audio/voice/E6/IRO/04/IR/IR006.ogg"
    iroha "I love that about you, senpai."
    voice "audio/voice/E6/IRO/04/HA/HA003.ogg"
    hachiman "............"
    "So this is what Isshiki Iroha meant by her \"real thing.\""
    "The \"real thing\" she had told me about."
    "In that case, my... my \"real thing\" is..."
    stop ambient
    show irohaAquariumB with dissolve:
        zoom 1.0
    voice "audio/voice/E6/IRO/04/HA/HA004.ogg"
    hachiman "............"
    voice "audio/voice/E6/IRO/04/HA/HA005.ogg"
    hachiman "......I used to think of you as a little sister, like Komachi."
    voice "audio/voice/E6/IRO/04/IR/IR007.ogg"
    iroha "I know."
    voice "audio/voice/E6/IRO/04/HA/HA006.ogg"
    hachiman "I thought you were cute, and I wanted to take care of you. My feelings of wanting to be together were just an overlap of how I felt about Komachi. I kept doubting myself, telling myself that these were just "
    voice sustain
    hachiman "feelings of love an older brother has."
    voice "audio/voice/E6/IRO/04/HA/HA007.ogg"
    hachiman "And if all that was the truth, then these feelings wouldn't be genuine."
    voice "audio/voice/E6/IRO/04/HA/HA008.ogg"
    hachiman "But I was wrong. It wasn't like that; I don't see Komachi in you anymore. You're not Komachi; you're you."
    voice "audio/voice/E6/IRO/04/HA/HA009.ogg"
    hachiman "Isshiki Iroha. I like you."
    voice "audio/voice/E6/IRO/04/IR/IR008.ogg"
    iroha "Yes..."
    window auto hide dissolve
    show irohaAquariumB at topleft with dissolve:
        zoom 1.5
    window auto show dissolve
    "My throat was incredibly dry as I managed to confess my feelings to Isshiki, and she tightly hugged me once again."
    "My arms were shaking, but I wrapped them around Isshiki's little body."
    "She fit perfectly in my arms as if we were meant to be, and she was incredibly precious to me."
    "Isshiki laughed with a cute smile and lifted her face, looking me straight in the eyes."
    voice "audio/voice/E6/IRO/04/HA/HA010.ogg"
    hachiman "............"
    "I noticed her long eyelashes as she lowered her gaze and how red her cheeks were, as if she was expecting something."
    window auto hide dissolve
    scene irohaAquariumA at topleft with Dissolve(1.0):
        zoom 1.5
    window auto show dissolve
    voice "audio/voice/E6/IRO/04/HA/HA012.ogg"
    hachiman "I, uh, I'm sorry for saying it so late."
    voice "audio/voice/E6/IRO/04/IR/IR009.ogg"
    iroha "Seriously! How long do you think I've been waiting?"
    voice "audio/voice/E6/IRO/04/HA/HA013.ogg"
    hachiman "S-sorry."
    voice "audio/voice/E6/IRO/04/IR/IR010.ogg"
    iroha "But, I..."
    voice "audio/voice/E6/IRO/04/IR/IR011.ogg"
    iroha "I love that annoying part of you, senpai."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    show white with Fade(2.0, 0, 1.0, color="#fff")
    $renpy.movie_cutscene("movies/ed03.mkv")
    jump E6_IRO_07

label E6_IRO_05:
    voice "audio/voice/E6/IRO/05/HA/HA000.ogg"
    hachiman "......お前の『本物』"
    voice "audio/voice/E6/IRO/05/IR/IR000.ogg"
    iroha "はい"
    "............"
    show iroha mid_left angry with dissolve:
        xoffset -5 yoffset 65
    voice "audio/voice/E6/IRO/05/IR/IR001.ogg"
    iroha "んー......"
    "言葉が見つからず、立ち尽くしていると、一色は何か考えるように人差し指を唇に押し当てた。"
    stop music
    "そして、––"
    hide iroha with dissolve
    show iroha coat_blue near_center vhappy at center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E6/IRO/05/IR/IR002.ogg"
    iroha "えいっ"
    hide iroha
    show black
    show aquarium zorder 1 at center, Shake(None, 0.5, dist=50)
    show iroha coat_blue near_center vhappy zorder 2 at center, Shake(None, 0.3, dist=50):
        xoffset -15 yoffset 75
    $renpy.pause(delay=1.0, hard=True)
    voice "audio/voice/E6/IRO/05/HA/HA001.ogg"
    hachiman "！？"
    "かわいらしいかけ声と共に、一色はその指先を俺の唇にぴとっと押し当てた。"
    voice "audio/voice/E6/IRO/05/HA/HA002.ogg"
    hachiman "え、あ......！？"
    show iroha happy with dissolve
    play music "audio/bgm/BGM50.ogg"
    "うろたえる俺に、一色はいたずらな笑みを浮かべる。"
    voice "audio/voice/E6/IRO/05/IR/IR003.ogg"
    iroha "あざといなこいつーって思いました？"
    show iroha blush with dissolve
    voice "audio/voice/E6/IRO/05/IR/IR004.ogg"
    iroha "......でもこんなこと、ほんとに好きな人にしかしませんよ"
    voice "audio/voice/E6/IRO/05/HA/HA003.ogg"
    hachiman "............"
    show iroha angry with dissolve
    voice "audio/voice/E6/IRO/05/IR/IR005.ogg"
    iroha "先輩は、どうですか？"
    voice "audio/voice/E6/IRO/05/IR/IR006.ogg"
    iroha "わたしじゃ、先輩の『本物』にはなれませんか？"
    voice "audio/voice/E6/IRO/05/HA/HA004.ogg"
    hachiman "お......俺は......"
    voice "audio/voice/E6/IRO/05/HA/HA005.ogg"
    hachiman "......まだ、確信を持てない......"
    show iroha sad with dissolve
    voice "audio/voice/E6/IRO/05/IR/IR007.ogg"
    iroha "......そですか"
    voice "audio/voice/E6/IRO/05/HA/HA006.ogg"
    hachiman "............"
    voice "audio/voice/E6/IRO/05/HA/HA007.ogg"
    hachiman "......けど"
    show iroha pout with dissolve
    voice "audio/voice/E6/IRO/05/IR/IR008.ogg"
    iroha "......？"
    voice "audio/voice/E6/IRO/05/HA/HA008.ogg"
    hachiman "『本物』になったらいいなとは、心底思ってる......"
    show iroha surprised with dissolve
    voice "audio/voice/E6/IRO/05/IR/IR009.ogg"
    iroha "............"
    show iroha blush with dissolve
    voice "audio/voice/E6/IRO/05/IR/IR010.ogg"
    iroha "......先輩の口からそれだけ聞ければ十分ですね"
    show iroha near_left blush with dissolve:
        xoffset 460 yoffset 140
    play sound "audio/sfx/SE01/SE01_12.ogg"
    "一色は頬を染めながら、嬉しそうに身を寄せてきた。"
    stop sound
    voice "audio/voice/E6/IRO/05/IR/IR011.ogg"
    iroha "『本物』にしましょう先輩。ふたりで"
    voice "audio/voice/E6/IRO/05/HA/HA009.ogg"
    hachiman "............"
    voice "audio/voice/E6/IRO/05/HA/HA010.ogg"
    hachiman "......ああ"
    window auto hide dissolve
    stop voice
    scene irohaAquariumB with dissolve
    window auto show dissolve
    "頷いて、俺はおそるおそる一色の肩に手を回す。"
    "初めて自分から抱き寄せた彼女の身体に、俺は驚きを覚えた。"
    "彼女はこんなにも華奢であったのかと。そしてこんなにも柔らかく、温かかったのかと。"
    voice "audio/voice/E6/IRO/05/HA/HA011.ogg"
    hachiman "............"
    "自然と、一色を抱く腕に力が込もる。"
    "これは手放してはいけないものだと、強くそう思ったから。"
    window auto hide dissolve
    stop music fadeout 1.0
    show white with Fade(2.0, 0, 1.0, color="#fff")
    $renpy.movie_cutscene("movies/ed04.mkv")
    scene irohaGoodEnd with Fade(0.5, 1.0, 1.0, color="#fff")
    call game_over("Isshiki Iroha", "Good") from _call_game_over_4
    return

label E6_IRO_06:
    voice "audio/voice/E6/IRO/06/HA/HA000.ogg"
    hachiman "Your \"real thing\"..."
    voice "audio/voice/E6/IRO/06/IR/IR000.ogg"
    iroha "Yes."
    window auto hide dissolve
    stop music fadeout 0.5
    #figure out close eyes effect. might need to create a new ImageDissolve
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
    play ambient "audio/sfx/SE02/SE02_17.ogg"
    window auto show dissolve
    "一色いろはの見つけた『本物』......。"
    "それがなんであるかの見当は、さすがに俺もついている。"
    "だからこそ、俺は一色には嘘をつきたくない。"
    "それがどんなに情けないものでも、正直に話そう。"
    "今の自分の、胸の内を––。"
    window auto hide dissolve
    stop ambient
    scene aquarium
    show iroha coat_blue mid_center angry at center:
        xoffset 20 yoffset 75
    show transition_2a at truecenter:
        yoffset -190
        parallel:
            linear 0.5 yoffset -890
    show transition_2b at truecenter:
        yoffset 190
        parallel:
            linear 0.5 yoffset 890
    $renpy.pause(delay=0.5, hard=True)
    hide transition_2a
    hide transition_2b
    window auto show dissolve
    voice "audio/voice/E6/IRO/06/HA/HA001.ogg"
    hachiman "『本物』......なのかもしれないものはある"
    voice "audio/voice/E6/IRO/06/IR/IR001.ogg"
    iroha "............"
    voice "audio/voice/E6/IRO/06/HA/HA002.ogg"
    hachiman "ただ、確信がまだ得られない"
    show iroha pout with dissolve
    voice "audio/voice/E6/IRO/06/IR/IR002.ogg"
    iroha "............"
    show iroha mid_left with dissolve:
        xoffset -5 yoffset 65
    play music "audio/bgm/BGM49.ogg"
    voice "audio/voice/E6/IRO/06/IR/IR003.ogg"
    iroha "......そうですか"
    voice "audio/voice/E6/IRO/06/HA/HA003.ogg"
    hachiman "......すまん"
    show iroha mid_center happy with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E6/IRO/06/IR/IR004.ogg"
    iroha "......先輩、あっちにペンギンコーナーがあるみたいですよ"
    voice "audio/voice/E6/IRO/06/HA/HA004.ogg"
    hachiman "え？"
    hide iroha with dissolve
    show iroha coat_blue near_center vhappy at center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E6/IRO/06/IR/IR005.ogg"
    iroha "ほら、行きましょう"
    hide iroha with dissolve
    "一色は俺の手を取るとジャイアントケルプの水槽から離れ、強引に屋外へと連れ出した。"
    window auto hide dissolve
    $renpy.pause(delay=0.5, hard=True)
    scene waterPark at right:
        zoom 2.43 yoffset 250
    show iroha coat near_left happy at center:
        xoffset 20 yoffset 75
    with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    "外へ出ると、雪が激しくなっていた。"
    "冷気に身震いするが、その分、一色の手の温もりも強く感じる。"
    "けれど、どうにも気恥ずかしくて、俺は一色の手を解こうとした。しかし一色は、手を握る力をむしろ強める。"
    voice "audio/voice/E6/IRO/06/HA/HA005.ogg"
    hachiman "......一色、手"
    show iroha angry with dissolve
    voice "audio/voice/E6/IRO/06/IR/IR006.ogg"
    iroha "ダメですよ。これ離したら、先輩迷子になっちゃうかも"
    voice "audio/voice/E6/IRO/06/HA/HA006.ogg"
    hachiman "............"
    "否定する言葉が、なぜか出てこない。"
    show iroha happy with dissolve
    voice "audio/voice/E6/IRO/06/IR/IR007.ogg"
    iroha "わたし、先輩が『本物』を見つけられるまで待っててあげます。だから頑張って探して下さい"
    voice "audio/voice/E6/IRO/06/HA/HA007.ogg"
    hachiman "......見つけられなかったらどうする気だよ"
    show iroha near_center vhappy with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E6/IRO/06/IR/IR008.ogg"
    iroha "心配しなくてもいいですよー。女の子は気まぐれなので、待つのに飽きたらとっととどっか行っちゃいますから"
    voice "audio/voice/E6/IRO/06/HA/HA008.ogg"
    hachiman "............っ"
    voice "audio/voice/E6/IRO/06/HA/HA009.ogg"
    hachiman "......そうか"
    show iroha happy with dissolve
    voice "audio/voice/E6/IRO/06/IR/IR009.ogg"
    iroha "はい"
    voice "audio/voice/E6/IRO/06/HA/HA010.ogg"
    hachiman "すまん"
    show iroha vhappy with dissolve
    voice "audio/voice/E6/IRO/06/IR/IR010.ogg"
    iroha "もー先輩、さっきから暗いですー。せっかくのデートなんだから楽しみましょうよー"
    "一色の屈託のない笑顔が眩しい。"
    hachiman "（ほんと、悪い、一色......）"
    hachiman "（けど、きっといつか......）"
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_12.ogg"
    show iroha surprised with dissolve
    $renpy.pause(delay=0.5, hard=True)
    show iroha blush with dissolve
    window auto show dissolve
    "そんな不確かな約束を口にする事は出来ず、俺はただ彼女の小さな手をそっと握り返した。"
    window auto hide dissolve
    stop music fadeout 1.0
    show white with Fade(2.0, 0, 1.0, color="#fff")
    $renpy.movie_cutscene("movies/ed05.mkv")
    scene normalEnd with Fade(0.5, 1.0, 1.0, color="#fff")
    call game_over("Isshiki Iroha", "Normal") from _call_game_over_5
    return

label E6_IRO_07:
    scene hallwayA with Fade(1.0, 0.5, 1.5)
    play sound "audio/sfx/SE00/SE00_07.ogg"
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    "I looked around as I walked through the quiet and empty hallway."
    hachiman "(Oh, this sure brings back some memories...)"
    stop sound
    "I felt hits of nostalgia as I made my way to the student council room."
    window auto hide dissolve
    play sound "audio/sfx/SE04/SE04_00.ogg"
    $renpy.pause(delay=0.5, hard=True)
    scene black with fade
    $renpy.pause(delay=1.5, hard=True)
    stop sound
    window auto show dissolve
    voice "audio/voice/E6/IRO/07/HA/HA000.ogg"
    hachiman "Uh, h-hello..."
    voice "audio/voice/E6/IRO/07/IR/IR000.ogg"
    iroha "Ah, senpai! You're late~!"
    window auto hide dissolve
    stop voice
    scene irohaEndSceneA with Fade(0.5, 0.5, 0.5)
    play sound "audio/sfx/SE01/SE01_12.ogg"
    $renpy.pause(delay=0.5, hard=True)
    play music "audio/bgm/BGM18.ogg"
    window auto show dissolve
    voice "audio/voice/E6/IRO/07/IR/IR001.ogg"
    iroha "Don't you have a lot of free time in university?"
    voice "audio/voice/E6/IRO/07/HA/HA001.ogg"
    hachiman "No, I actually ditched my fifth period class to make it here."
    voice "audio/voice/E6/IRO/07/IR/IR002.ogg"
    iroha "C'mon, senpai, you can do better than that! Next time, ditch fourth period too, okay?"
    hachiman "(This girl just says stuff like this as if it's completely normal... at this rate, I bet she'll be asking me to ditch all my classes.)"
    window auto hide dissolve
    $renpy.pause(delay=0.5, hard=True)
    scene scouncilroomA with dissolve
    window auto show dissolve
    "As we spoke, I looked around the student council room. Isshiki smiled as she followed my gaze."
    voice "audio/voice/E6/IRO/07/IR/IR003.ogg"
    iroha "Nostalgic, huh? It's been two whole years, hasn't it, senpai?"
    voice "audio/voice/E6/IRO/07/HA/HA002.ogg"
    hachiman "Yeah."
    voice "audio/voice/E6/IRO/07/HA/HA003.ogg"
    hachiman "Unlike Yukinoshita's sister, there's not really a point in someone like me showing my face around here."
    voice "audio/voice/E6/IRO/07/HA/HA004.ogg"
    hachiman "Hang on, were you by yourself?"
    voice "audio/voice/E6/IRO/07/IR/IR004.ogg"
    iroha "Tomorrow's the general entrance exams, so everyone on duty got called to the staff room."
    voice "audio/voice/E6/IRO/07/HA/HA005.ogg"
    hachiman "Must be nice not having to worry about that, huh?"
    voice "audio/voice/E6/IRO/07/IR/IR005.ogg"
    iroha "It sure is!"
    voice "audio/voice/E6/IRO/07/IR/IR006.ogg"
    iroha "Oh, and do you think this is alright as a response letter?"
    "Isshiki suddenly handed me two sheets of paper."
    window auto hide dissolve
    scene irohaEndSceneA at top with dissolve:
        zoom 1.5 xoffset -240 yoffset -30
    $renpy.pause(delay=0.5, hard=True)
    window auto hide dissolve
    voice "audio/voice/E6/IRO/07/HA/HA006.ogg"
    hachiman "Huh? What's this all of a sudden? \"Response?\""
    voice "audio/voice/E6/IRO/07/IR/IR007.ogg"
    iroha "Yeah, I was hoping you'd look over it and proofread it."
    voice "audio/voice/E6/IRO/07/HA/HA007.ogg"
    hachiman "Didn't you call me over here for something important?"
    voice "audio/voice/E6/IRO/07/IR/IR008.ogg"
    iroha "It was about this."
    voice "audio/voice/E6/IRO/07/HA/HA008.ogg"
    hachiman "I can't believe I missed fifth period for this..."
    window auto hide dissolve
    stop voice
    scene scouncilroomA at truecenter with Fade(0.5, 1.0, 0.5):
        zoom 1.5
    window auto show dissolve
    "I read every last letter of her script, and put down the red pen I was marking it with."
    voice "audio/voice/E6/IRO/07/IR/IR009.ogg"
    iroha "How was it?"
    voice "audio/voice/E6/IRO/07/HA/HA009.ogg"
    hachiman "I think it's good. It's a little too obvious that you're fishing for sympathy, but it's like you to write like that."
    voice "audio/voice/E6/IRO/07/IR/IR010.ogg"
    iroha "Really? That's good to hear."
    voice "audio/voice/E6/IRO/07/IR/IR011.ogg"
    iroha "It's really over now, huh..."
    voice "audio/voice/E6/IRO/07/IR/IR012.ogg"
    iroha "I feel like congratulating myself with a \"good job!\" right about now. I'm the only one in the history of Soubu High to have been the student council president for two years straight!"
    voice "audio/voice/E6/IRO/07/HA/HA010.ogg"
    hachiman "You did ask us to prevent you from becoming the president in the first place, though."
    voice "audio/voice/E6/IRO/07/IR/IR013.ogg"
    iroha "Right, right! That's how it was, back then, wasn't it? Then you convinced me with all the perks of the job."
    voice "audio/voice/E6/IRO/07/HA/HA011.ogg"
    hachiman "Yeah, I did a pretty good job back then, if I do say so myself."
    voice "audio/voice/E6/IRO/07/IR/IR014.ogg"
    iroha "Heehee~"
    stop music fadeout 0.5
    voice "audio/voice/E6/IRO/07/IR/IR015.ogg"
    iroha "............"
    voice "audio/voice/E6/IRO/07/IR/IR016.ogg"
    iroha "Yeah, that's right. So, hey, senpai."
    voice "audio/voice/E6/IRO/07/HA/HA012.ogg"
    hachiman "Hm?"
    window auto hide dissolve
    stop voice
    show irohaEndSceneA with Fade(0.5, 0.5, 0.5)
    play sound "audio/sfx/SE01/SE01_12.ogg"
    $renpy.pause(delay=0.5, hard=True)
    play music "audio/bgm/BGM51.ogg"
    window auto show dissolve
    voice "audio/voice/E6/IRO/07/IR/IR017.ogg"
    iroha "Please give me a reward for working so hard for the last two years."
    voice "audio/voice/E6/IRO/07/HA/HA013.ogg"
    hachiman "Uh..."
    voice "audio/voice/E6/IRO/07/IR/IR018.ogg"
    iroha "You're the one who made me become the student council president, you know."
    voice "audio/voice/E6/IRO/07/IR/IR019.ogg"
    iroha "Can't you at least give me a reward for my hard work?"
    voice "audio/voice/E6/IRO/07/HA/HA014.ogg"
    hachiman "R-right here?"
    voice "audio/voice/E6/IRO/07/IR/IR020.ogg"
    iroha "It's fine, isn't it? C'mon, nobody's even around."
    voice "audio/voice/E6/IRO/07/HA/HA015.ogg"
    hachiman "............"
    voice "audio/voice/E6/IRO/07/HA/HA016.ogg"
    hachiman "A-alright, I got it."
    "I felt my heartbeat quicken as I approached Isshiki's lips."
    hachiman "(For some reason, I'm incredibly nervous.)"
    "Those rosy cheeks, long eyelashes, and shimmering lips. All waiting for me to take initiative."
    voice "audio/voice/E6/IRO/07/HA/HA017.ogg"
    hachiman "You, uh, did a great job in those two years."
    voice "audio/voice/E6/IRO/07/IR/IR021.ogg"
    iroha "............"
    "As those words of appreciation left my mouth, I gently reached towards Isshiki's lips."
    hide irohaEndSceneA
    play sound "audio/sfx/SE04/SE04_01.ogg"
    voice "audio/voice/E6/IRO/07/KO/KO000.ogg"
    komachi "Iroha-senpai! About those documents--"
    stop sound
    voice "audio/voice/E6/IRO/07/HA/HA018.ogg"
    hachiman "...!?"
    voice "audio/voice/E6/IRO/07/IR/IR022.ogg"
    iroha "Ah...!?"
    voice "audio/voice/E6/IRO/07/KO/KO001.ogg"
    komachi "............"
    voice "audio/voice/E6/IRO/07/HA/HA019.ogg"
    hachiman "............"
    voice "audio/voice/E6/IRO/07/KO/KO002.ogg"
    komachi "Sorry for the interruption~!"
    window auto hide dissolve
    stop voice
    play sound "audio/sfx/SE04/SE04_00.ogg"
    $renpy.pause(delay=3.0, hard=True)
    window auto show dissolve
    voice "audio/voice/E6/IRO/07/HA/HA020.ogg"
    hachiman "............"
    voice "audio/voice/E6/IRO/07/IR/IR023.ogg"
    iroha "............"
    window auto hide dissolve
    stop voice
    show irohaEndSceneA with dissolve
    window auto show dissolve
    voice "audio/voice/E6/IRO/07/HA/HA021.ogg"
    hachiman "Hey, the, uh, atmosphere's a bit awkward now... maybe we should give it a rest?"
    voice "audio/voice/E6/IRO/07/IR/IR024.ogg"
    iroha "Heehee, of course not. Instead, we should be thanking the current student council president!"
    voice "audio/voice/E6/IRO/07/IR/IR025.ogg"
    iroha "After all, she helped you loosen up, senpai."
    voice "audio/voice/E6/IRO/07/IR/IR026.ogg"
    iroha "So..."
    show irohaEndSceneB with dissolve
    voice "audio/voice/E6/IRO/07/IR/IR027.ogg"
    iroha "This time, please reward me with a kiss."
    window auto hide dissolve
    stop voice
    stop music fadeout 2.0
    scene irohaBestEnd with Fade(2.0, 1.0, 1.0, color="#fff")
    call game_over("Isshiki Iroha", "Best") from _call_game_over_7
    return
