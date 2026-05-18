label E6_YUI_01:
    scene classroomA with dissolve
    play music "audio/bgm/BGM08.ogg"
    show yui school mid_center happy at center with dissolve:
        xoffset -25 yoffset 75
    window auto show dissolve
    voice "audio/voice/E6/YUI/01/YI/YI000.ogg"
    yui "Ah! Hey, Hikki!"
    voice "audio/voice/E6/YUI/01/HA/HA000.ogg"
    hachiman "Hey, what's up?"
    show yui school mid_center vhappy at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E6/YUI/01/YI/YI001.ogg"
    yui "Komachi-chan passed her exams, right? That's great! Congrats!"
    voice "audio/voice/E6/YUI/01/HA/HA001.ogg"
    hachiman "Yep, thanks."
    hachiman "(I'm still not used to talking freely like this in class...)"
    show yui school mid_left vhappy at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E6/YUI/01/YI/YI002.ogg"
    yui "Say, Komachi'll be a student at our school next year, right? Ah, right! We have to celebrate somehow."
    show yumiko school mid_center happy at right behind yui with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E6/YUI/01/YM/YM000.ogg"
    yumiko "Hikkio's little sister is enrolling here?"
    show yui school mid_center happy at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E6/YUI/01/YI/YI003.ogg"
    yui "Ah, Yumiko. Yeah, that's right! I really can't wait!"
    show yumiko school mid_center vhappy at right behind yui with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E6/YUI/01/YM/YM001.ogg"
    yumiko "Hmm~ Well good for you. Congrats."
    voice "audio/voice/E6/YUI/01/HA/HA002.ogg"
    hachiman "R-Right... Thanks."
    show tobe school mid happy at left behind yui with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E6/YUI/01/TB/TB000.ogg"
    tobe "Eh, what now? Hikitani's little sis is enrolling here? We totally gotta celebrate!"
    voice "audio/voice/E6/YUI/01/HA/HA003.ogg"
    hachiman "Y-You really don't have to go that far. Besides, we're not exactly friends."
    show tobe school mid vhappy at left behind yui with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E6/YUI/01/TB/TB001.ogg"
    tobe "Nah, I mean look, she's practically already my junior too, right? And plus, she's Hikitani's little sis. So if this isn't cause for celebration, I don't know what is!"
    voice "audio/voice/E6/YUI/01/HA/HA004.ogg"
    hachiman "I-Is that right?"
    voice "audio/voice/E6/YUI/01/TB/TB002.ogg"
    tobe "Yeah! Right! We have to talk to Ebina and Hayato. We should tell Totsuka, too!"
    show yumiko school mid_center unimpressed at right behind yui with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E6/YUI/01/YM/YM003.ogg"
    yumiko "Shut up, Tobe. You're a bit too excited. And annoying."
    show tobe school mid sad at left behind yui with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E6/YUI/01/TB/TB003.ogg"
    tobe "Right..."
    show yui school mid_left vhappy at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E6/YUI/01/YI/YI004.ogg"
    yui "Hahaha..."
    voice "audio/voice/E6/YUI/01/HA/HA005.ogg"
    hachiman "Ha..."
    hide tobe
    hide yumiko
    with dissolve
    "A natural smiled slipped out. Be it a good thing or not, I had passed over a barrier that should have stopped me..."
    show yui school mid_left happy at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E6/YUI/01/YI/YI005.ogg"
    yui "..."
    hachiman "(...Don't look at me like that, you're gonna make me start blushing.)"
    voice "audio/voice/E6/YUI/01/HA/HA006.ogg"
    hachiman "..."
    stop music fadeout 1.0
    "I guess we finally stand on the same starting line. Thinking along those lines, I exchanged a low-key smile with Yuigahama."
    window auto hide dissolve
    jump E6_YUI_02

label E6_YUI_02:
    scene classroomB with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE01/SE01_00.ogg"
    hachiman "(Now then...)"
    show yui school_sunset mid_center happy at center with dissolve:
        xoffset -25 yoffset 75
    play music "audio/bgm/BGM08.ogg"
    voice "audio/voice/E6/YUI/02/YI/YI000.ogg"
    yui "Hikki! I'm coming, too!"
    voice "audio/voice/E6/YUI/02/HA/HA000.ogg"
    hachiman "Alright..."
    show yui school_sunset mid_center vhappy at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E6/YUI/02/YI/YI001.ogg"
    yui "Ehehe..."
    voice "audio/voice/E6/YUI/02/HA/HA001.ogg"
    hachiman "..."
    show yui school_sunset mid_center happy at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E6/YUI/02/YI/YI002.ogg"
    yui "..."
    voice "audio/voice/E6/YUI/02/HA/HA002.ogg"
    hachiman "..."
    "The distance between me and Yuigahama is smaller than before. That being the case, I'm sure there's something I ought to do. A promise I have to fulfill."
    show yui school_sunset mid_left happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E6/YUI/02/MI/MIX000.ogg"
    hachiandyui "B-By the way... \nSay, Hikki..."
    show yui school_sunset mid_left vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E6/YUI/02/MI/MIX001.ogg"
    hachiandyui "Do you have some free time this weekend? \nAre you free this weekend?"
    show yui school_sunset mid_left blush at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E6/YUI/02/YI/YI005.ogg"
    yui "Ah..."
    voice "audio/voice/E6/YUI/02/HA/HA005.ogg"
    hachiman "Um..."
    show yui school_sunset mid_center blush at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E6/YUI/02/YI/YI006.ogg"
    yui "W-What did you want to say, Hikki?"
    voice "audio/voice/E6/YUI/02/HA/HA006.ogg"
    hachiman "R-Right... I wanted to ask you help me find a celebration gift for Komachi... What about you?"
    voice "audio/voice/E6/YUI/02/YI/YI007.ogg"
    yui "Um... I was wondering if you could... help me with deciding my career path."
    voice "audio/voice/E6/YUI/02/HA/HA007.ogg"
    hachiman "I'm not exactly the most reliable when it comes to that."
    show yui school_sunset mid_center surprised at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E6/YUI/02/YI/YI008.ogg"
    yui "No hesitation!?"
    voice "audio/voice/E6/YUI/02/HA/HA008.ogg"
    hachiman "Guh..."
    hachiman "(I can't... look her in the eyes for some reason...)"
    voice "audio/voice/E6/YUI/02/HA/HA009.ogg"
    hachiman "W-Well... why don't you talk to Miura or Ebina about that? Or Yukinoshita for that matter..."
    show yui school_sunset mid_center unimpressed at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E6/YUI/02/YI/YI009.ogg"
    yui "Hikki, you dummy..."
    voice "audio/voice/E6/YUI/02/HA/HA010.ogg"
    hachiman "..."
    show yui school_sunset mid_center happy at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E6/YUI/02/YI/YI010.ogg"
    yui "I just wanted you to hear me out. No actually, I just want you to be there."
    "In sharp relief to my simpering, Yuigahama looks me straight in the eye and tells me what she wants."
    voice "audio/voice/E6/YUI/02/YI/YI011.ogg"
    yui "I've never thought about the future until now, so..."
    hachiman "(Well, that's really no different from me...)"
    show yui school_sunset mid_center angry at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E6/YUI/02/YI/YI012.ogg"
    yui "I mean, you really have to think about it when deciding on a career path, don't you?"
    voice "audio/voice/E6/YUI/02/HA/HA011.ogg"
    hachiman "I-I guess..."
    show yui school_sunset mid_center happy at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E6/YUI/02/YI/YI013.ogg"
    yui "I want to hear what you have to say about it, too."
    "Yuigahama's gaze was dazzling. Piercing through me almost."
    voice "audio/voice/E6/YUI/02/HA/HA012.ogg"
    hachiman "Well anyhow, let's get going..."
    show yui school_sunset mid_center vhappy at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E6/YUI/02/YI/YI014.ogg"
    yui "...Okay!"
    hachiman "(The future, huh...)"
    stop music fadeout 1.0
    window auto hide dissolve
    scene black with dissolve
    $renpy.pause(delay=0.5, hard=True)
    jump E6_YUI_03

label E6_YUI_03:
    scene khstationA
    show yui coat mid_center happy at center:
        yoffset 75
    with dissolve
    play music "audio/bgm/BGM12.ogg"
    window auto show dissolve
    voice "audio/voice/E6/YUI/03/HA/HA000.ogg"
    hachiman "Hey."
    show yui coat mid_center vhappy at center with dissolve:
        yoffset 75
    voice "audio/voice/E6/YUI/03/YI/YI000.ogg"
    yui "Ah, Hikki! Yahallo!"
    voice "audio/voice/E6/YUI/03/HA/HA001.ogg"
    hachiman "Did you wait?"
    show yui coat mid_right vhappy at center with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E6/YUI/03/YI/YI001.ogg"
    yui "Nope, not at all!"
    voice "audio/voice/E6/YUI/03/HA/HA002.ogg"
    hachiman "I see. So, what do you want to do now?"
    $url = ["yui coat mid_right pout", "yui coat mid_right happy"]
    $multiImagePara = [-105, 75, 0, 0, 1.5]
    call multiImage() from _call_multiImage_E6_YUI_03_1
    voice "audio/voice/E6/YUI/03/YI/YI002.ogg"
    yui "Mhm... Let's go somewhere!"
    call finishmultiImage from _call_finishmultiImage_E6_YUI_03_1
    show yui coat mid_right happy at center:
        xoffset -105 yoffset 75
    voice "audio/voice/E6/YUI/03/HA/HA003.ogg"
    hachiman "Hey, hold it right there. I thought you wanted my advice."
    voice "audio/voice/E6/YUI/03/YI/YI003.ogg"
    yui "Well, I do, but just sitting all still somewhere and talking would feel kinda weird."
    voice "audio/voice/E6/YUI/03/HA/HA004.ogg"
    hachiman "So basically you just wanted to play around..."
    show yui coat mid_right vhappy at center with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E6/YUI/03/YI/YI004.ogg"
    yui "E-Ehehe..."
    voice "audio/voice/E6/YUI/03/HA/HA005.ogg"
    hachiman "Well, that's fine, too... Let's go somewhere, then."
    voice "audio/voice/E6/YUI/03/YI/YI005.ogg"
    yui "Yeah!"
    voice "audio/voice/E6/YUI/03/HA/HA006.ogg"
    hachiman "Is DisneySea alright?"
    "I'm not sure when it was, but I vaguely remember us deciding that we'd eventually go together. I can finally fulfill a promise that you can't even call a promise."
    $url = ["yui coat mid_right surprised", "yui coat mid_right vhappy"]
    $multiImagePara = [-105, 75, 0, 0, 5]
    call multiImage() from _call_multiImage_E6_YUI_03_2
    voice "audio/voice/E6/YUI/03/YI/YI006.ogg"
    yui "......Yeah!"
    call finishmultiImage from _call_finishmultiImage_E6_YUI_03_2
    hide yui
    show yui coat mid_right vhappy at center:
        xoffset -105 yoffset 75
    window auto hide dissolve
    scene black with dissolve
    $renpy.pause(delay=0.5, hard=True)
    scene trainA with dissolve
    $renpy.pause(delay=2, hard=True)
    scene black with dissolve
    $renpy.pause(delay=0.5, hard=True)
    scene terminalA with dissolve
    $renpy.pause(delay=2, hard=True)
    scene black with dissolve
    $renpy.pause(delay=0.5, hard=True)
    scene destinyLandA
    show yui coat mid_center vhappy at center:
        yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E6/YUI/03/YI/YI007.ogg"
    yui "We're here~!"
    "In front of the entrance gate was a huge heart-shaped object and statues of characters holding hands, the decorative lights illuminating them flashing in a continues loop."
    "The most impressive thing was the gate that adorned the main street from the entrance plaza all the way to the inside of the park."
    "The brickwood venetian, or maybe more broadly italian, structures created an exotic atmosphere."
    "When something like this is shown off to you, you're almost forced to think Disney is where you want to be to have fun from here on out."
    "I was really impressed, but even more so was Yuigahama. Her eyes were sparkling and her face instantly lit up. She then started pulling my hand energetically."
    show yui coat mid_left vhappy at center:
        yoffset 75
    voice "audio/voice/E6/YUI/03/YI/YI008.ogg"
    yui "Hikki! A picture! Take!"
    voice "audio/voice/E6/YUI/03/HA/HA007.ogg"
    hachiman "A-Alright. I think your language ability is kinda falling apart at the seams."
    hide yui with dissolve
    show yui coat near_center happy at center with dissolve:
        xoffset 280 yoffset 75
    "We both stood in front of the viewfinder. The distance between us was the usual. Like there was an invisible person standing beside either of us."
    "The pictures were taken by the park staff, so it looks like I don't need to work the camera. That was a moment of relief for me."
    voice "audio/voice/E6/YUI/03/XV/XV000.ogg"
    fs "Could you get a little closer, please?"
    voice "audio/voice/E6/YUI/03/HA/HA008.ogg"
    hachiman "O-Okay..."
    hide yui with dissolve
    show yui coat near_center vhappy at center with dissolve:
        zoom 1.1 xoffset 290 yoffset 184
    "In reply, Yuigahama just shuffled a half step closer to me."
    show yui coat near_center blush at center with dissolve:
        zoom 1.1 xoffset 290 yoffset 184
    voice "audio/voice/E6/YUI/03/YI/YI009.ogg"
    yui "I think we should get a little closer..."
    "Then, finally, a staff member help up the camera. The time until the shutter clicked was very short. And yet, strangely, it felt like a long time, and I couldn't help but feel flustered."
    show yui coat near_center happy at center with dissolve:
        zoom 1.1 xoffset 290 yoffset 184
    voice "audio/voice/E6/YUI/03/XV/XV001.ogg"
    fs "Okay, here we go!"
    show yui coat near_center happy at center with dissolve:
        zoom 1.3 xoffset 290 yoffset 365
    "Just as the staff member said this, Yuigahama tugged on my scarf. This caught me by surprise and I stumbled for a half step when I unintentionally touched her shoulder."
    show yui coat near_center vhappy at center with dissolve:
        zoom 1.3 xoffset 290 yoffset 365
    "Her face was so close to mine they almost touched. She was all smiles, as if she was proud of a prank she had just pulled."
    "A moment later, the shutter went off."
    window auto hide dissolve
    play sound "audio/sfx/SE03/SE03_06.ogg"
    $renpy.pause(delay=1.0, hard=True)
    scene destinyLandA
    show yui coat near_left vhappy at center:
        yoffset 75
    with Fade(0.5, 1.0, 0.5)
    play ambient "audio/sfx/SE02/SE02_01.ogg"
    voice "audio/voice/E6/YUI/03/YI/YI010.ogg"
    yui "Ahaha, this is fun!"
    hachiman "(It's fun, but you're a bit close! You're too close!)"
    show yui coat near_center happy at center with dissolve:
        yoffset 75
    voice "audio/voice/E6/YUI/03/YI/YI011.ogg"
    yui "Ah, that was fun... Next we just have to ride that one, don't we?"
    voice "audio/voice/E6/YUI/03/HA/HA009.ogg"
    hachiman "No, those are the screamer types."
    show yui coat near_center vhappy at center with dissolve:
        yoffset 75
    voice "audio/voice/E6/YUI/03/YI/YI012.ogg"
    yui "Come on, we didn't come all this way just to miss it!"
    voice "audio/voice/E6/YUI/03/HA/HA010.ogg"
    hachiman "Well, I guess..."
    window auto hide dissolve
    stop ambient fadeout 0.75
    scene black with dissolve
    play sound "audio/sfx/SE02/SE02_01.ogg"
    window auto show dissolve
    voice "audio/voice/E6/YUI/03/YI/YI013.ogg"
    yui "Kyaa!"
    hachiman "(You're too close! Your hand touched me! I won't say where, but it did!)"
    window auto hide dissolve
    stop sound fadeout 1.0
    stop music fadeout 1.0
    $renpy.pause(delay=1.0, hard=True)
    scene destinyLandC
    show yui coat near_center surprised at center:
        yoffset 75
    with dissolve
    play ambient "audio/sfx/SE03/SE03_05L.ogg"
    voice "audio/voice/E6/YUI/03/YI/YI014.ogg"
    yui "...Ah."
    voice "audio/voice/E6/YUI/03/HA/HA011.ogg"
    hachiman "Looks like people are starting to leave..."
    show yui coat near_center happy at center with dissolve:
        yoffset 75
    voice "audio/voice/E6/YUI/03/YI/YI015.ogg"
    yui "I bet the fireworks show is starting soon! They said it in the announcement earlier!"
    voice "audio/voice/E6/YUI/03/HA/HA012.ogg"
    hachiman "Then... wanna go see it?"
    show yui coat near_center surprised at center with dissolve:
        yoffset 75
    voice "audio/voice/E6/YUI/03/YI/YI016.ogg"
    yui "You're okay with that!?"
    voice "audio/voice/E6/YUI/03/HA/HA013.ogg"
    hachiman "Well... We didn't come all this way just to miss it."
    show yui coat near_center vhappy at center with dissolve:
        yoffset 75
    voice "audio/voice/E6/YUI/03/YI/YI017.ogg"
    yui "Yay~!"
    stop ambient fadeout 1.25
    window auto hide dissolve
    scene yuiFireworksA with Fade(0.5, 1.0, 0.5)
    play ambient "audio/sfx/SE02/SE02_04aL.ogg"
    $renpy.pause(delay=1.0, hard=True)
    scene yuiFireworksB with dissolve
    play music "audio/bgm/BGM18.ogg"
    window auto show dissolve
    voice "audio/voice/E6/YUI/03/YI/YI018.ogg"
    yui "So pretty... I'm glad we came."
    "I nodded and looked at the starlit sky. Then, as classical music began to play, an announcement for the start of the fireworks sounded."
    "The sound of fireworks launching was followed by the sound of them going off in the sky. Fireworks bloom on a black canvas, sprinkling it with colorful lights."
    window auto hide dissolve
    scene yuiFireworksB with dissolve:
        zoom 1.38 xoffset -100 yoffset -95
    stop ambient
    play ambient "audio/sfx/SE02/SE02_04bL.ogg"
    scene yuiFireworksA with dissolve:
        zoom 1.38 xoffset -100 yoffset -95
    $renpy.pause(delay=1.0, hard=True)
    scene yuiFireworksB with dissolve:
        zoom 1.38 xoffset -100 yoffset -95
    window auto show dissolve
    voice "audio/voice/E6/YUI/03/YI/YI019.ogg"
    yui "I didn't think we'd actually come here..."
    voice "audio/voice/E6/YUI/03/HA/HA014.ogg"
    hachiman "Really? You were the one who said we'd go, weren't you?"
    voice "audio/voice/E6/YUI/03/YI/YI020.ogg"
    yui "That's true, but that's not what I meant... You kept a promise I didn't think would come true. Thanks."
    voice "audio/voice/E6/YUI/03/HA/HA015.ogg"
    hachiman "That's not something you should thank me for... I promised after all."
    scene yuiFireworksB with dissolve
    "If I didn't have words that bound me, if I didn't have an excuse to move, I surely wouldn't be able to do anything at all."
    "It was always Yuigahama that gave me an excuse to move. If anyone should be grateful, it's me."
    "Yuigahama looked up at me as if peering at my expression. The light from the fireworks reflected and swayed on her upturned eyes."
    "After a hesitant pause, Yuigahama breathes a small sigh and gives me a serious look."
    voice "audio/voice/E6/YUI/03/YI/YI021.ogg"
    yui "A promise... Then, can you promise me something again?"
    voice "audio/voice/E6/YUI/03/HA/HA016.ogg"
    hachiman "..."
    stop ambient fadeout 1.0
    window auto hide dissolve
    scene destinyLandC
    show yui coat near_center sad at center:
        yoffset 75
    with Fade(0.5, 1.0, 0.5)
    play ambient "audio/sfx/SE05/SE05_05L.ogg"
    window auto show dissolve
    voice "audio/voice/E6/YUI/03/YI/YI022.ogg"
    yui "The fireworks are over."
    voice "audio/voice/E6/YUI/03/HA/HA017.ogg"
    hachiman "Yeah. If we don't leave before people start moving again..."
    show yui coat near_center pout at center with dissolve:
        yoffset 75
    voice "audio/voice/E6/YUI/03/YI/YI023.ogg"
    yui "Ah...!"
    voice "audio/voice/E6/YUI/03/HA/HA018.ogg"
    hachiman "Hey, are you alri- Woah!"
    show yui coat near_center surprised at center with dissolve:
        yoffset 75
    voice "audio/voice/E6/YUI/03/YI/YI024.ogg"
    yui "Kya!"
    window auto hide dissolve
    stop ambient fadeout 1.0
    scene destinyLandC at Shake(None, 0.5, dist=100):
        zoom 2.0  xoffset -650 yoffset -1100
    window auto show dissolve
    play sound "audio/sfx/SE01/SE01_58.ogg"
    hachiman "(Ow... I somehow got a hold of Yuigahama...)"
    window auto hide dissolve
    scene destinyLandC
    show yui coat near_center pout at center:
        yoffset 75
    with dissolve
    voice "audio/voice/E6/YUI/03/YI/YI025.ogg"
    yui "Hikki, a-are you okay...?"
    voice "audio/voice/E6/YUI/03/HA/HA019.ogg"
    hachiman "F-Forget me, what about you?"
    jump E6_YUI_04

label E6_YUI_04:
    show yui coat near_center happy at center with dissolve:
        yoffset 75
    voice "audio/voice/E6/YUI/04/YI/YI000.ogg"
    yui "Back with Sable and when we were skiing, too... You're always saving me."
    voice "audio/voice/E6/YUI/04/HA/HA000.ogg"
    hachiman "That's not true. You've saved me a lot, too."
    hachiman "(It's true... If I think back, she had always been saving me.)"
    show yui coat near_center vhappy at center with dissolve:
        yoffset 75
    voice "audio/voice/E6/YUI/04/YI/YI001.ogg"
    yui "I see. Then, we're in the same boat. We stand together."
    "As she said this, Yuigahama gently looked into my eyes. Disney Sea's lights were reflecting and dancing on her eyes in an almost painful fashion."
    stop music fadeout 1.0
    show yui coat near_center annoyed at center with dissolve:
        yoffset 75
    voice "audio/voice/E6/YUI/04/YI/YI002.ogg"
    yui "..."
    voice "audio/voice/E6/YUI/04/HA/HA001.ogg"
    hachiman "..."
    show yui coat near_center angry at center with dissolve:
        yoffset 75
    voice "audio/voice/E6/YUI/04/YI/YI003.ogg"
    yui "I told you before, didn't I? That I'm not waiting for someone that won't come around."
    voice "audio/voice/E6/YUI/04/HA/HA002.ogg"
    hachiman "..."
    voice "audio/voice/E6/YUI/04/YI/YI004.ogg"
    yui "That I'll make the first move."
    show yui coat near_center happy at center with dissolve:
        yoffset 75
    voice "audio/voice/E6/YUI/04/YI/YI005.ogg"
    yui "So, I'm going to say it, okay?"
    "I didn't avert my gaze from Yuigahama's big, slightly damp eyes."
    voice "audio/voice/E6/YUI/04/HA/HA003.ogg"
    hachiman "..."
    window auto hide dissolve
    scene yuiConfessionA with dissolve
    window auto show dissolve
    play music "audio/bgm/BGM42.ogg"
    voice "audio/voice/E6/YUI/04/YI/YI006.ogg"
    yui "Hikigaya Hachiman, I love you."
    "My fingertips softly touched Yuigahama's. I was finally able to gently hold her hand, and I hoped wouldn't break them."
    voice "audio/voice/E6/YUI/04/HA/HA004.ogg"
    hachiman "Yuigahama... I... I love you."
    voice "audio/voice/E6/YUI/04/YI/YI007.ogg"
    yui "...Hikki."
    voice "audio/voice/E6/YUI/04/YI/YI008.ogg"
    yui "This is the first time you've held my hand..."
    voice "audio/voice/E6/YUI/04/HA/HA005.ogg"
    hachiman "...That's true. I finally did."
    window auto hide dissolve
    scene yuiConfessionA with dissolve:
        zoom 1.49 xoffset -925 yoffset -20
    window auto show dissolve
    voice "audio/voice/E6/YUI/04/YI/YI009.ogg"
    yui "Don't ever let go, okay?"
    voice "audio/voice/E6/YUI/04/HA/HA006.ogg"
    hachiman "...I won't."
    "I still couldn't reply all that well. So, in place of that, I could at least put more strength into holding her hand."
    voice "audio/voice/E6/YUI/04/YI/YI010.ogg"
    yui "Hehe..."
    voice "audio/voice/E6/YUI/04/YI/YI011.ogg"
    yui "Hey, Hikki... Lean over a bit."
    voice "audio/voice/E6/YUI/04/HA/HA007.ogg"
    hachiman "L-Like this?"
    scene yuiConfessionA with dissolve
    voice "audio/voice/E6/YUI/04/YI/YI012.ogg"
    yui "Ehehe... Like this, I'm much closer to you than usual."
    voice "audio/voice/E6/YUI/04/HA/HA008.ogg"
    hachiman "That's true..."
    "I saw Yuigahama's face from up close. This was probably the first we've been this close. I noticed her eyes were slighly damp."
    voice "audio/voice/E6/YUI/04/YI/YI013.ogg"
    yui "From now on... Forever... I want to be close to you like this."
    window auto hide dissolve
    scene yuiConfessionA with dissolve:
        zoom 2.0 xoffset -1900 yoffset -900
    window auto show dissolve
    "Yuigahama was staring into my eyes for a while, but before long, she gently closed them."
    "I thought she looked really beautiful. To convey those feelings, I softly pressed my lips against hers."
    voice "audio/voice/E6/YUI/04/HA/HA010.ogg"
    hachiman "..."
    voice "audio/voice/E6/YUI/04/YI/YI014.ogg"
    yui "..."
    window auto hide dissolve
    scene yuiConfessionB with dissolve:
        zoom 1.49 xoffset -925 yoffset -20
    window auto show dissolve
    "I felt Yuigahama's lips for the first time. They were soft and they were trembling slightly."
    voice "audio/voice/E6/YUI/04/YI/YI015.ogg"
    yui "Hikki... I love you."
    voice "audio/voice/E6/YUI/04/HA/HA011.ogg"
    hachiman "Yeah... I love you, too."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    scene white with Fade(2.0, 0, 1.0, color="#fff")
    $renpy.movie_cutscene("movies/ed01.mkv")
    jump E6_YUI_07

label E6_YUI_07:
    scene skyA with Fade(1.0, 0.5, 1.5)
    window auto show dissolve
    voice "audio/voice/E6/YUI/07/HA/HA000.ogg"
    hachiman "...Yui."
    window auto hide dissolve
    scene yuiTimeskipA with dissolve
    play music "audio/bgm/BGM51.ogg"
    window auto show dissolve
    voice "audio/voice/E6/YUI/07/YI/YI000.ogg"
    yui "Woah!"
    voice "audio/voice/E6/YUI/07/HA/HA001.ogg"
    hachiman "H-Hey!"
    voice "audio/voice/E6/YUI/07/YI/YI001.ogg"
    yui "T-Thanks! Ah, that scared me!"
    show yuiTimeskipB with dissolve
    voice "audio/voice/E6/YUI/07/HA/HA002.ogg"
    hachiman "You told me to call you that, so I've been doing simulations in my head all the time and tried my best to call you that..."
    voice "audio/voice/E6/YUI/07/YI/YI002.ogg"
    yui "S-Sorry! Now that you call me that, I feel like my heart'll jump out of my chest."
    voice "audio/voice/E6/YUI/07/HA/HA003.ogg"
    hachiman "I felt the same way..."
    show yuiTimeskipC with dissolve
    voice "<from 0 to 1>audio/voice/E6/YUI/07/YI/YI003.ogg"
    yui "Ehehe..."
    voice "<from 1>audio/voice/E6/YUI/07/YI/YI003.ogg"
    hachiman "(She looks super happy...)"
    voice "audio/voice/E6/YUI/07/YI/YI004.ogg"
    yui "Hey, can you call me that one more time? Hikki... No, Hachiman."
    voice "audio/voice/E6/YUI/07/HA/HA004.ogg"
    hachiman "Guh..."
    voice "audio/voice/E6/YUI/07/YI/YI005.ogg"
    yui "Please?"
    show yuiTimeskipD with dissolve
    voice "audio/voice/E6/YUI/07/HA/HA005.ogg"
    hachiman "...Yui."
    voice "audio/voice/E6/YUI/07/YI/YI006.ogg"
    yui "Uwa~! That really makes my heart race!"
    voice "audio/voice/E6/YUI/07/HA/HA006.ogg"
    hachiman "Wait, isn't this exchange super stupid!? Isn't it embarrassing?"
    voice "audio/voice/E6/YUI/07/YI/YI007.ogg"
    yui "A-Ah, I kinda thought so, too..."
    voice "audio/voice/E6/YUI/07/HA/HA007.ogg"
    hachiman "Also... People are starting to look at us."
    voice "audio/voice/E6/YUI/07/YI/YI008.ogg"
    yui "...But you called me by my name so suddenly."
    voice "audio/voice/E6/YUI/07/HA/HA008.ogg"
    hachiman "Ah, right. I'm, uh, sorry? Yuigahama."
    voice "audio/voice/E6/YUI/07/YI/YI009.ogg"
    yui "..."
    voice "audio/voice/E6/YUI/07/HA/HA009.ogg"
    hachiman "..."
    voice "audio/voice/E6/YUI/07/YI/YI010.ogg"
    yui "A-Anyway! Let's finish up!"
    voice "audio/voice/E6/YUI/07/HA/HA010.ogg"
    hachiman "R-Right..."
    window auto hide dissolve
    scene skyA with dissolve
    window auto show dissolve
    voice "audio/voice/E6/YUI/07/YI/YI011.ogg"
    yui "Let's see... Today we're buying... Kitchen appliances and a dinner set."
    voice "audio/voice/E6/YUI/07/HA/HA011.ogg"
    hachiman "Right."
    voice "audio/voice/E6/YUI/07/YI/YI012.ogg"
    yui "Then we have... a fridge, a washing machine, a bookshelf..."
    voice "audio/voice/E6/YUI/07/HA/HA012.ogg"
    hachiman "That's right."
    voice "audio/voice/E6/YUI/07/YI/YI013.ogg"
    yui "After then... a b-bed?"
    voice "audio/voice/E6/YUI/07/HA/HA013.ogg"
    hachiman "Hey? Can we stop with the dubious expressions? And can you stop blushing?"
    window auto hide dissolve
    scene yuiTimeskipA with dissolve
    window auto show dissolve
    voice "audio/voice/E6/YUI/07/YI/YI014.ogg"
    yui "B-But..."
    voice "audio/voice/E6/YUI/07/HA/HA014.ogg"
    hachiman "No \"buts\". I'm starting to blush, too, so stop."
    voice "audio/voice/E6/YUI/07/YI/YI015.ogg"
    yui "Okay..."
    voice "audio/voice/E6/YUI/07/HA/HA015.ogg"
    hachiman "Well, what the hell. It'll be furniture for our room after all, so let's take our time picking, Yui."
    hachiman "(I tried to act cool and say that, but... I'm still not used to calling her by her name.)"
    window auto hide dissolve
    scene skyA with dissolve
    window auto show dissolve
    play music "audio/bgm/BGM51.ogg"
    voice "audio/voice/E6/YUI/07/YI/YI016.ogg"
    yui "Yeah! Then let's go shopping~!"
    voice "audio/voice/E6/YUI/07/HA/HA016.ogg"
    hachiman "H-Hey, don't run. You'll fall."
    voice "audio/voice/E6/YUI/07/YI/YI017.ogg"
    yui "It's okay! Because... you're holding my hand tight!"
    voice "audio/voice/E6/YUI/07/HA/HA017.ogg"
    hachiman "Y-Yeah."
    voice "audio/voice/E6/YUI/07/YI/YI018.ogg"
    yui "Ehehe... Hachiman."
    voice "audio/voice/E6/YUI/07/HA/HA018.ogg"
    hachiman "...?"
    show yuiTimeskipD with dissolve
    voice "audio/voice/E6/YUI/07/YI/YI019.ogg"
    yui "We'll... always be together."
    voice "audio/voice/E6/YUI/07/HA/HA019.ogg"
    hachiman "Yeah... Yui."
    "Calling each other by our first names is still a bit embarrassing though. From now on, as we think of what happens next, we slowly, but surely, make our way towards the future."
    window auto hide dissolve
    stop voice
    stop music fadeout 2.0
    scene yuiEnd with Fade(2.0, 1.0, 1.0, color="#fff")
    call game_over("Yuigahama Yui", "Best") from _call_game_over_8
    return
