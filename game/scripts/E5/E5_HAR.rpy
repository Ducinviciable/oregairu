label E5_HAR_01:
    play music "audio/bgm/BGM08.ogg"
    show hayama happy with dissolve
    voice "audio/voice/E5/HAR/01/HY/HY000.ogg"
    hayama "Well..., I guess it can't be helped. Let's just start."
    show yukino happy with dissolve
    voice "audio/voice/E5/HAR/01/YK/YK000.ogg"
    yukino "Yes, good idea."
    image yumiko coat blush = Flatten("yumiko coat mid_left blush")
    show hayama:
        parallel:
            easein 0.4 xoffset 5
    show yukino:
        parallel:
            easein 0.4 xoffset -40
    show yumiko coat blush at center behind yukino:
        xoffset 330 yoffset 75 alpha 0
        parallel:
            easein 0.6 xoffset 230
        parallel:
            linear 0.6 alpha 1.0
    $renpy.pause(delay=0.6, hard=True)
    hide yumiko
    show yumiko coat mid_left blush at center behind yukino:
        xoffset 230 yoffset 75
    voice "audio/voice/E5/HAR/01/YM/YM000.ogg"
    yumiko "Hey, Hayato? What do you want me to do?"
    show yukino unimpressed with dissolve
    voice "audio/voice/E5/HAR/01/YK/YK001.ogg"
    yukino "............"
    hide yukino with dissolve
    voice "audio/voice/E5/HAR/01/HY/HY001.ogg"
    hayama "Right then, Yumiko and Hina, could you handle the guest rooms? Is that okay, Iroha?"
    "Almost seamlessly Hayama had put himself in charge, directing people around with out missing a beat. He was even running his instruction past Isshiki beforehand."
    show yumiko happy with dissolve
    voice "audio/voice/E5/HAR/01/YM/YM001.ogg"
    yumiko "That's fine with me..."
    image iroha home vhappy = Flatten("iroha home mid_left vhappy")
    show iroha home vhappy at right:
        xoffset -125 yoffset 65 alpha 0
        parallel:
            easein 0.4 xoffset -190
        parallel:
            linear 0.4 alpha 1.0
    $renpy.pause(delay=0.4, hard=True)
    hide iroha
    show iroha home mid_left vhappy at right:
        xoffset -190 yoffset 65
    voice "audio/voice/E5/HAR/01/IR/IR000.ogg"
    iroha "Yup! Perfect!!"
    hide hayama
    hide yumiko
    hide iroha
    with dissolve
    "And so we decided our roles and began cleaning."
    window auto hide dissolve
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE04/SE04_04.ogg"
    $renpy.pause(delay=0.5, hard=True)
    show meguri coat mid happy at center:
        xoffset -385 yoffset 75
    show haruno coat mid_center happy at center:
        xoffset 390 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/HAR/01/HR/HR000.ogg"
    haruno "Hey, hey, how's it going? Are you all working hard? Oh, are you finished already?"
    hachiman "(Agh, you're back a lot sooner than I'd expect. I mean, please don't give me that look while you say that.)"
    voice "audio/voice/E5/HAR/01/HA/HA000.ogg"
    hachiman "...No, we were just about to start."
    show haruno vhappy with dissolve
    voice "audio/voice/E5/HAR/01/HR/HR001.ogg"
    haruno "Really? It's a good thing we got back so soon Meguri!"
    show meguri vhappy with dissolve
    voice "audio/voice/E5/HAR/01/MG/MG000.ogg"
    meguri "Right~. As expected of Haruno-san."
    show haruno mid_left vhappy with dissolve
    voice "audio/voice/E5/HAR/01/HR/HR002.ogg"
    haruno "Okay! Let's see, we'll help, so let's get this done!"
    window auto hide dissolve
    stop voice
    scene lodgeA at truecenter with Fade(1.0, 0.5, 1.0):
        zoom 1.48 xoffset -245 yoffset 85
    play sound "audio/sfx/SE01/SE01_26.ogg"
    $renpy.pause(delay=1.5, hard=True)
    show komachi home mid_center happy at left:
        xoffset 55 yoffset 75
    show haruno sweater mid_left vhappy at center:
        xoffset 390 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/HAR/01/HR/HR003.ogg"
    haruno "It's a little easier if you clean the window like this"
    voice "audio/voice/E5/HAR/01/KO/KO000.ogg"
    komachi "I see!"
    voice "audio/voice/E5/HAR/01/HR/HR004.ogg"
    haruno "Let's get the boys to the high places."
    show komachi vhappy with dissolve
    voice "audio/voice/E5/HAR/01/KO/KO001.ogg"
    komachi "Ooh, good idea."
    hachiman "(Komachi is really starting to get attached to her...)"
    show haruno mid_center happy at center with dissolve:
        xoffset 420
    voice "audio/voice/E5/HAR/01/HR/HR005.ogg"
    haruno "Oh, there's another dustpan over there. I think Shizuka-chan has the bru-"
    show haruno surprised with dissolve
    voice "audio/voice/E5/HAR/01/HR/HR006.ogg"
    haruno "Hm?"
    voice "audio/voice/E5/HAR/01/HA/HA001.ogg"
    hachiman "Ah."
    hide komachi
    hide haruno
    hide lodgeA
    show lodgeA
    with dissolve
    hachiman "(Crap. Our eyes met.)"
    show haruno sweater mid_center sly at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/HAR/01/HR/HR007.ogg"
    haruno "Hikigaya-kun, your hands stopped moving~."
    play sound "audio/sfx/SE01/SE01_28.ogg"
    voice "audio/voice/E5/HAR/01/HA/HA002.ogg"
    hachiman "Right... Sorry"
    stop sound
    show haruno happy with dissolve
    voice "audio/voice/E5/HAR/01/HR/HR008.ogg"
    haruno "What is it? You look like you're about to say something."
    voice "audio/voice/E5/HAR/01/HA/HA003.ogg"
    hachiman "Uhm... You work surprisingly well."
    show haruno vhappy with dissolve
    voice "audio/voice/E5/HAR/01/HR/HR009.ogg"
    haruno "Of course I do! Really, what do you think of me?"
    voice "audio/voice/E5/HAR/01/HA/HA004.ogg"
    hachiman "I couldn't really imagine you working. Honestly, I'm surprised."
    voice "audio/voice/E5/HAR/01/HR/HR010.ogg"
    haruno "Ahaha. Crazy right? Well, I'm a hard worker... just like you"
    voice "audio/voice/E5/HAR/01/HA/HA005.ogg"
    hachiman "I'm not really."
    show haruno happy with dissolve
    voice "audio/voice/E5/HAR/01/HR/HR011.ogg"
    haruno "Oh don't be silly! You're being worked awfully hard!"
    hachiman "(Passive voice? Ahh, I guess I can't really disagree...)"
    window auto hide dissolve
    stop music fadeout 1.0
    jump E5_HAR_03

label E5_HAR_02:
    scene lodgeA with Fade(1.0, 0.5, 1.0)
    play ambient "audio/sfx/SE05/SE05_02L.ogg"
    window auto show dissolve
    "After the shopping team had left, the lodge had become a lawless zone for the slackers."
    "While some, such as Yukinoshita, had started to clean their designated spots at a smooth, quick pace, Isshiki, Tobe and the others weren't in such a hurry."
    "Of course, I was part of the more slacking than not camp."
    hachiman "(Well, nobody likes to clean...)"
    window auto hide dissolve
    stop ambient fadeout 0.5
    play sound "audio/sfx/SE02/SE02_21.ogg"
    $renpy.pause(delay=1.0, hard=True)
    window auto show dissolve
    "Suddenly, a high-pitched whistle sounded."
    voice "audio/voice/E5/HAR/02/MG/MG000.ogg"
    mystery "Eyes over here, everyone!"
    window auto hide dissolve
    stop voice
    image lodgeADup = "images/bg/BG57A.jpg"
    show lodgeADup:
        zoom 1.5 yoffset -200
    show meguri coat mid frown at center:
        xoffset 25 yoffset 75
    with dissolve
    play music "audio/bgm/BGM09.ogg"
    window auto show dissolve
    "I looked towards the source of the sound, and saw Shiromeguri-senpai, who was supposed to be out shopping, holding a whistle in her hand looking irked."
    voice "audio/voice/E5/HAR/02/IR/IR000.ogg"
    iroha "Shi-Shiromeguri-senpai..."
    voice "audio/voice/E5/HAR/02/MG/MG001.ogg"
    meguri "Well, here I thought I'd come back and help a little, so I hurried back, but you guys haven't done anything. Isshiki is here too, so how did this happen?"
    show iroha home mid_left pout at right with dissolve:
        xoffset -120 yoffset 65
    voice "audio/voice/E5/HAR/02/IR/IR001.ogg"
    iroha "Ah, I mean, um... I thought we'd get more work done if we took breaks in between... right?"
    show meguri vhappy with dissolve
    voice "audio/voice/E5/HAR/02/MG/MG002.ogg"
    meguri "I see! That's true! Alright then, break's over!"
    show iroha happy with dissolve
    voice "audio/voice/E5/HAR/02/IR/IR002.ogg"
    iroha "Ah... yeah, t-that's right!"
    "Isshiki replied somewhat panicked in the face of Meguri-senpai's warm smile. In response, Meguri-senpai puffed out her chest."
    show meguri happy with dissolve
    voice "audio/voice/E5/HAR/02/MG/MG003.ogg"
    meguri "All right, everyone! If you want to ski, we're gonna have to clean up! Yeah!"
    show iroha pout with dissolve
    voice "audio/voice/E5/HAR/02/IR/IR003.ogg"
    iroha "Y-Yeah..."
    hide iroha with dissolve
    hachiman "(Ahh... the heavy atmosphere has been Megurified...)"
    show meguri vhappy with dissolve
    voice "audio/voice/E5/HAR/02/MG/MG004.ogg"
    meguri "Hikigaya-kun, can you please handle the outside?"
    voice "audio/voice/E5/HAR/02/HA/HA000.ogg"
    hachiman "... Huh?"
    "After every single one of my cell had been Megurified, I let out a dumb squeek in response."
    show meguri happy with dissolve
    voice "audio/voice/E5/HAR/02/MG/MG005.ogg"
    meguri "I was wondering if you could shovel the snow outside. Hiratsuka-sensei is bringing out the shovels."
    voice "audio/voice/E5/HAR/02/HA/HA001.ogg"
    hachiman "Ah... sure."
    show meguri vhappy with dissolve
    voice "audio/voice/E5/HAR/02/MG/MG006.ogg"
    meguri "Alright, then next we have..."
    hide lodgeADup
    hide meguri
    with dissolve
    hachiman "(What can I say? Meguri-senpai really is amazing. She made the wheels on this clean-up start turning, and even if she scolded me, I wouldn't feel bad about it...)"
    window auto hide dissolve
    stop music fadeout 0.5

label E5_HAR_03:
    scene slopesA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM44.ogg"
    window auto show dissolve
    voice "audio/voice/E5/HAR/03/HA/HA000.ogg"
    hachiman "Ah..."
    play sound "audio/sfx/SE01/SE01_46.ogg"
    "After somwhow finishing cleaning up, we finally went to the ski place. This being my first time skiing however, I wasn't particularly motivated and was inevitably at a loss on what to do."
    stop sound
    show yukino heavy_coat mid_center happy at left:
        xoffset 25 yoffset 75
    show yui heavy_coat mid_left vhappy at right:
        xoffset -270 yoffset 75
    with dissolve
    voice "audio/voice/E5/HAR/03/YI/YI000.ogg"
    yui "Yahallo, Hikki~! I something wrong?"
    voice "audio/voice/E5/HAR/03/HA/HA001.ogg"
    hachiman "No, well... I guess...?"
    hachiman "(Naturally, since I didn't even know how to mount the board, I couldn't really say what was wrong..."
    show yukino surprised with dissolve
    voice "audio/voice/E5/HAR/03/YK/YK000.ogg"
    yukino "It couldn't be that you can't..."
    show yui surprised with dissolve
    voice "audio/voice/E5/HAR/03/YI/YI001.ogg"
    yui "Huh~?"
    show yukino angry with dissolve
    voice "audio/voice/E5/HAR/03/YK/YK001.ogg"
    yukino "Hikigaya-kun, put your skis there. Thenm remove the snow from the back of your boots and step into here toe first"
    voice "audio/voice/E5/HAR/03/HA/HA002.ogg"
    hachiman "R-right..."
    "Yukinoshita was incredibly serious, so at once, I obidently followed her instruction."
    voice "audio/voice/E5/HAR/03/YK/YK002.ogg"
    yukino "Now, step into your heel."
    play sound "audio/sfx/SE01/SE01_40.ogg"
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E5/HAR/03/HA/HA003.ogg"
    hachiman "Oh. The board attached itself to my foot."
    show yui mid_center pout at right with dissolve:
        xoffset -240 yoffset 75
    voice "audio/voice/E5/HAR/03/YI/YI002.ogg"
    yui "Hikki, could it be that..."
    show yukino unimpressed with dissolve
    voice "audio/voice/E5/HAR/03/YK/YK003.ogg"
    yukino "Yes, it is. If you don't know how to get on the board, you should have asked someone."
    voice "audio/voice/E5/HAR/03/HA/HA004.ogg"
    hachiman "Well... Yeah, I know."
    hachiman "(But everyone scattered like roaches the moment we got here...)"
    voice "audio/voice/E5/HAR/03/HA/HA005.ogg"
    hachiman "But you really helped me out. Thanks."
    show yukino blush with dissolve
    voice "audio/voice/E5/HAR/03/YK/YK004.ogg"
    yukino "No, it's not a big deal, really."
    show yui happy with dissolve
    voice "audio/voice/E5/HAR/03/YI/YI003.ogg"
    yui "Hikki, if you want to, we can teach you."
    voice "audio/voice/E5/HAR/03/HA/HA006.ogg"
    hachiman "No, I can't ask that much of you. I'll start with walking and then work up from there. You've done more than enough, so go ahead and ski."
    show yui pout with dissolve
    voice "audio/voice/E5/HAR/03/YI/YI004.ogg"
    yui "But..."
    hachiman "(They've only got 2 days to ski, and they're being stuck with an absolute beginner.)"
    voice "audio/voice/E5/HAR/03/HA/HA007.ogg"
    hachiman "When I'm able to walk around, I'll try asking for help again."
    show yukino happy with dissolve
    voice "audio/voice/E5/HAR/03/YK/YK005.ogg"
    yukino "I see. Shall we go then, Yuigahama-san?"
    show yukino vhappy with dissolve
    voice "audio/voice/E5/HAR/03/YK/YK006.ogg"
    yukino "Hikigaya-kun. If... you need anything, don't hesitate to ask."
    voice "audio/voice/E5/HAR/03/HA/HA008.ogg"
    hachiman "I won't. Thanks a lot."
    window auto hide dissolve
    stop voice
    hide yukino
    hide yui
    with dissolve
    $renpy.pause(delay=1.0, hard=True)
    scene slopesA with Fade(1.0, 0.5, 1.0)
    play footsteps "audio/sfx/SE00/SE00_22L.ogg"
    window auto show dissolve
    "By the time I was finally able to walk around on the board, I was feeling fairly tired but somehow I felt like I'd taken the offensive on skiing."
    voice "audio/voice/E5/HAR/03/HA/HA009.ogg"
    hachiman "However... just walking around is pretty hard... How are you all gliding around?"
    "As I looked around, I saw customers enjoying the act of sliding accordingly to their own abilities, occasionally shouting with joy. There is no one just walking around."
    hachiman "(Well... obvoiusly. It's a ski resort.)"
    "I saw a few people teaching skiing here and there, and both the teachers and the students seemed to be enjoying themselves."
    "When I think about it, I feel like I was being stubborn when I refused to be taught earlier. I should have just bit the bullet and obediently ask to be taught."
    stop footsteps fadeout 1.0
    stop music fadeout 1.0
    menu slopes_question2:
        hachiman "(Right. In any case...)"
        with dissolve
        "I want to become good at this":#hiratsuka
            $ski_flag = "hiratsuka"
            hachiman "(In any case, I have to get good... Like those people gliding all  over the place.)"
            "I really didn't think it was all that before coming to the camp, but now, watching people skiing so comfortable, I'm feeling kind of envious."
            hachiman "(Well, it's probably just because of the occasion that I'm feeling like this. I doubt I'll ever go skiing again.)"
            window auto hide dissolve
            $renpy.pause(delay=0.5, hard=False)
            play ambient "audio/sfx/SE01/SE01_44L.ogg"
            $renpy.pause(delay=2.0, hard=False)
            scene slopesA at topleft with dissolve:
                zoom 2.0 xoffset -300 yoffset -225
            $renpy.pause(delay=0.5, hard=False)
            window auto show dissolve
            hachiman "(Oh, those skiiers are so cool, at least from where I'm standing. It looks fun.)"
            window auto hide dissolve
            image slopesDup = "images/bg/BG55A.jpg"
            scene slopesA
            show slopesDup at topleft:
                zoom 1.75 xoffset -305 yoffset -385
            with dissolve
            play music "audio/bgm/BGM22.ogg"
            window auto show dissolve
            hachiman "(Woah, why are they coming towards me!?)"
            hachiman "(Sl-slow down! You're coming at me too fast!)"
            hide slopesDup with dissolve
            hachiman "(I'm going to get hit! I can't really move like this!)"
            window auto hide dissolve
            jump E5_SHI_02
        "I'll learn, slow and steady...":#haruno
            hachiman "(Yeah. Let's just take in steady, and I'll go ask for help.)"
            hachiman "(Right... Yukinoshita, Yukinoshita...)"
            window auto hide dissolve
            scene slopesA at right:
                zoom 1.5 xoffset 0 yoffset 100
            show yukino heavy_coat far_center vhappy at left:
                xoffset 55 yoffset 75
            show komachi heavy_coat far_center vhappy at center:
                xoffset -35 yoffset 75
            show yui heavy_coat far_left vhappy at right:
                xoffset -220 yoffset 75
            with dissolve
            window auto show dissolve
            hachiman "(Ah, there she is. I'll try going to her...)"
            play ambient "audio/sfx/SE01/SE01_44L.ogg"
            voice "audio/voice/E5/HAR/03/HA/HA010.ogg"
            hachiman "Huh?"
            window auto hide dissolve
            scene slopesA with dissolve:
                zoom 3.2 yoffset -2350 xcenter 0.23
            $renpy.pause(delay=1.0, hard=True)
            stop ambient
            play sound "audio/sfx/SE01/SE01_47.ogg"
            show haruno athletic near_left vhappy at center:
                zoom 2.0 xoffset 400 yoffset 165 alpha 0
                parallel:
                    easein 0.5 xoffset -100
                parallel:
                    linear 0.5 alpha 1.0
            $renpy.pause(delay=1.0, hard=True)
            hide haruno
            show haruno athletic near_center vhappy at center:
                zoom 2.0 xoffset 25 yoffset 165
            with dissolve
            $renpy.pause(delay=0.5, hard=True)
            scene slopesA
            hide haruno
            show haruno athletic mid_center vhappy at center:
                xoffset 10 yoffset 75
            with dissolve
            play music "audio/bgm/BGM35.ogg"
            window auto show dissolve
            voice "audio/voice/E5/HAR/03/HR/HR000.ogg"
            haruno "Yahallo~, Hikigaya-kun!"
            voice "audio/voice/E5/HAR/03/HA/HA011.ogg"
            hachiman "Uwahh..."
            jump E5_HAR_04
        "It's fine as long as I'm having fun":#meguri
            play music "audio/bgm/BGM09.ogg"
            hachiman "(Well, as long as I'm having fun...)"
            "I am getting tired, and the aspirations of growth I had for a moment have already become non-existant."
            hachiman "(I don't think I can learn to ski in just a few days... I hope I can at least enjoy the atmosphere.)"
            "I think going out of my way to find Yukinoshita and have her teach me will do nothing but take up more of her time, and she'd be very strict to begin with, too."
            "I thought I could maybe hang out with Totsuka, but I believe he and Kawasaki are already skiing with Keika and Komachi."
            hachiman "(O-kay, what should I do...?)"
            voice "audio/voice/E5/HAR/03/MG/MG000.ogg"
            mystery "Oh, it's Hikigaya-kun!"
            hachiman "(Ahh, I feel a warmth that can alleviate all of my misfortune on this snow-covered mountain...)"
            hachiman "(Hmm? Warmth?)"
            window auto hide dissolve
            jump E5_HAR_05

label E5_HAR_04:
    show haruno sad with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR000.ogg"
    haruno "What do you mean \"uwahh\"?? Hmph, you're so rude!"
    "Haruno-san may sound offended, but the look on her face is surprisingly sweet, perhaps she enjoys skiing?"
    hachiman "(Well, it's just a hunch. It's impossible to know what she's thinking. No matter how good a mood she seems to be in, you can't be too careful...)"
    show haruno vhappy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR001.ogg"
    haruno "So, what are you up to?"
    voice "audio/voice/E5/HAR/04/HA/HA000.ogg"
    hachiman "Practising my board walking... I guess."
    show haruno surprised with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR002.ogg"
    haruno "Board walking? For skiing? Could it be that... you can't ski?"
    voice "audio/voice/E5/HAR/04/HA/HA001.ogg"
    hachiman "I mean, I've never done it before."
    show haruno happy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR003.ogg"
    haruno "Well then! Why not have Onee-san teach you~?"
    voice "audio/voice/E5/HAR/04/HA/HA002.ogg"
    hachiman "...Huh?"
    hachiman "(Ah. I didn't think about having her teach me...)"
    "I don't know if it was the lack of discretion, or the vanity with which she offered it, or maybe it was because she looked kind of scary."
    "I was surprised myself that I didn't have the usual feeling that I could be a nuisance."
    hide haruno with dissolve
    show haruno athletic near_center vhappy at center with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E5/HAR/04/HR/HR004.ogg"
    haruno "If you're up for it, I can teach you more than just skiing. I can teach you a lot of things."
    "As she poked my cheek, Haruno-san smiled a more brilliant smile than I'd seen from her before."
    "I really don't know what to make of that. Did I catch a glimpse of the true Yukinoshita Haruno?"
    voice "audio/voice/E5/HAR/04/HA/HA003.ogg"
    hachiman "...Just skiing is enough."
    show haruno happy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR005.ogg"
    haruno "You're such a buzzkill~. Anyway, it's a little surprising you want to learn skiing from me."
    voice "audio/voice/E5/HAR/04/HA/HA004.ogg"
    hachiman "If anything's surprising, it's that you're willing to teach me."
    show haruno sad with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR006.ogg"
    haruno "Come on, that's not true! I'm a big sister. I'm always willing to give a helping hand to my juniors."
    voice "audio/voice/E5/HAR/04/HA/HA005.ogg"
    hachiman "You're mistaking \"give a helping hand\" for \"give trouble to\"..."
    show haruno happy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR007.ogg"
    haruno "I guess you could say that."
    hide haruno with dissolve
    "Haruno-san chuckles, and pushes me lighter on the shoulder."
    voice "audio/voice/E5/HAR/04/HR/HR008.ogg"
    haruno "Alright!! I'm going to get serious, okay? First, let's look at your posture!"
    voice "audio/voice/E5/HAR/04/HA/HA006.ogg"
    hachiman "R-right..."
    window auto hide dissolve
    scene slopesA
    show haruno athletic mid_center annoyed at center:
        xoffset 10 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E5/HAR/04/HR/HR009.ogg"
    haruno "Alright. Okay, try sliding down that slope again..."
    voice "audio/voice/E5/HAR/04/HA/HA007.ogg"
    hachiman "...Isn't this a little too serious?"
    show haruno happy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR010.ogg"
    haruno "When I'm serious, I'm very serious. Well, it doesn't happen very often."
    voice "audio/voice/E5/HAR/04/HA/HA008.ogg"
    hachiman "So there are things that even you take seriously... I'm surprised..."
    show haruno surprised with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR011.ogg"
    haruno "...I'm surprised, too."
    voice "audio/voice/E5/HAR/04/HA/HA009.ogg"
    hachiman "Huh?"
    show haruno happy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR012.ogg"
    haruno "Alright! Time for the advance course!"
    hachiman "(Sh-she's a demon!)"
    voice "audio/voice/E5/HAR/04/HA/HA010.ogg"
    hachiman "That really is too much..."
    hide haruno with dissolve
    show haruno athletic near_left vhappy at center with dissolve:
        xoffset 195 yoffset 75
    voice "audio/voice/E5/HAR/04/HR/HR013.ogg"
    haruno "It'll be fine! Come on, let's go to the lift!"
    voice "audio/voice/E5/HAR/04/HA/HA011.ogg"
    hachiman "U-uhm... You don't have to pull my hand, I can walk by myself you know."
    show haruno happy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR014.ogg"
    haruno "...You won't run away?"
    voice "audio/voice/E5/HAR/04/HA/HA012.ogg"
    hachiman "I can't run away, not with my current ability..."
    show haruno vhappy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR015.ogg"
    haruno "Fair enough. Alright, let's go then."
    hide haruno with dissolve
    hachiman "(Ah, she finally let go of my hand...)"
    window auto hide dissolve
    scene slopesA at topleft with Fade(1.0, 0.5, 1.0):
        zoom 2.0 xoffset -300 yoffset -225
    window auto show dissolve
    voice "audio/voice/E5/HAR/04/HR/HR016.ogg"
    haruno "~~♪"
    "It's true enough that the petrifying mysteries of the advance course laid out before me were enticing, but there was nothing holding me back. I could escape if I wanted to..."
    hachiman "(And yet, for some reason I don't feel like running away... I felt a little lonely when she let go of my hand... What the hell is wrong with me!)"
    hachiman "(It must be the work of some kind of terrifying snow mountain magic from that smile I mentioned earlier!)"
    window auto hide dissolve
    scene slopesA at left:
        zoom 1.5 xoffset 0 yoffset 105
    show haruno athletic mid_center happy at center:
        xoffset 250 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/HAR/04/HR/HR017.ogg"
    haruno "Here we are, the lift!"
    voice "audio/voice/E5/HAR/04/HA/HA013.ogg"
    hachiman "Huh? Oh, right..."
    window auto hide dissolve
    stop voice
    scene black with Fade(1.0, 1.0, 0)
    play ambient "<from 0.5 to 20.0>audio/sfx/SE06/SE06_16L.ogg"
    scene skyA
    show haruno athletic near_left happy at center:
        xoffset -50 yoffset 75
    with Fade(0, 1.0, 1.0)
    window auto show dissolve
    voice "audio/voice/E5/HAR/04/HR/HR018.ogg"
    haruno "You've suddenly gone quiet... Are you okay?"
    voice "audio/voice/E5/HAR/04/HA/HA014.ogg"
    hachiman "...Not really. I'm actually pretty terrified."
    show haruno vhappy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR019.ogg"
    haruno "You're so weirdly honest. You'd be much cuter if you were this straightforwrd normally."
    show haruno sly with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR020.ogg"
    haruno "Hey, hey! Look down! Isn't it already super high?"
    voice "audio/voice/E5/HAR/04/HA/HA015.ogg"
    hachiman "...I hate this."
    hachiman "(I really am absolutely terrified.)"
    show haruno happy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR021.ogg"
    haruno "...Do you regret coming along?"
    voice "audio/voice/E5/HAR/04/HA/HA016.ogg"
    hachiman "I've regretted it since we bumped into each other. How can I regret something I had no choice in the first place?"
    voice "audio/voice/E5/HAR/04/HR/HR022.ogg"
    haruno "Hmm. If you aren't going to resist, I'll just keep pushing..."
    voice "audio/voice/E5/HAR/04/HA/HA017.ogg"
    hachiman "...What more do you want?"
    show haruno vhappy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR023.ogg"
    haruno "That's a secret☆"
    hachiman "(What do you mean \"That's a secret☆\"!? It was scary how hard my heart fluttered there for a second!)"
    voice "audio/voice/E5/HAR/04/HA/HA018.ogg"
    hachiman "...I guess I'm not really cut out for such a bubbly and rowdy sport."
    show haruno happy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR024.ogg"
    haruno "I like it. When you're out there on the snow, all that matters is you and your skates. Past that, it's all just noise."
    voice "audio/voice/E5/HAR/04/HA/HA019.ogg"
    hachiman "That's what you think?"
    voice "audio/voice/E5/HAR/04/HR/HR025.ogg"
    haruno "I do."
    hachiman "(I've never thought of skiing like that before. If that's the case, then maybe this is the right sport for me.)"
    show haruno vhappy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR026.ogg"
    haruno  "In the end, that also means whether you fail or not is entirely up to your own skill!"
    voice "audio/voice/E5/HAR/04/HA/HA020.ogg"
    hachiman "The little admiration I had is now gone."
    voice "audio/voice/E5/HAR/04/HR/HR027.ogg"
    haruno "Don't worry. There's no fun in throwing around a kid that won't let others help. I'll take care of you."
    hachiman "(I'm really scared of that smile.)"
    show haruno happy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR028.ogg"
    haruno "Time to get off!"
    voice "audio/voice/E5/HAR/04/HA/HA021.ogg"
    hachiman "Oh, alright."
    window auto hide dissolve
    stop ambient
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE01/SE01_40.ogg"
    $renpy.pause(delay=0.5, hard=True)
    scene slopes2A with Fade(1.0, 0.5, 1.0)
    play ambient "audio/sfx/SE02/SE02_00.ogg"
    show haruno athletic mid_center happy at center with dissolve:
        xoffset 10 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/HAR/04/HR/HR029.ogg"
    haruno "It's a lovely view, don't you think?"
    voice "audio/voice/E5/HAR/04/HA/HA022.ogg"
    hachiman "I mean... We are pretty high up, so..."
    stop ambient
    show haruno vhappy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR030.ogg"
    haruno "Of course it's high! We're on the advance course you know."
    voice "audio/voice/E5/HAR/04/HA/HA023.ogg"
    hachiman "I-I don't think I can do this after all..."
    show haruno happy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR031.ogg"
    haruno "Hey, I taught you, so be a little bit more confident. This is where you really have to show some gut!"
    voice "audio/voice/E5/HAR/04/HA/HA024.ogg"
    hachiman "Ugh..."
    show haruno athletic near_center vhappy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/HAR/04/HR/HR032.ogg"
    haruno "Alright! Into stance!"
    voice "audio/voice/E5/HAR/04/HA/HA025.ogg"
    hachiman "R-right...!"
    show haruno happy with dissolve
    voice "audio/voice/E5/HAR/04/HR/HR033.ogg"
    haruno "Whatever you do, just try reaching the bottom, okay?"
    hide haruno with dissolve
    "With a thump, a firm hand pushed me forward all of a sudden."
    "Before I even knew what was happening-"
    window auto hide dissolve
    play sound "<loop 2>audio/sfx/SE01/SE01_43L.ogg" loop
    $renpy.pause(delay=2.5, hard=True)
    show transition_1b at offscreenright:
        parallel:
            easein 0.1 xpos -780
    $renpy.pause(delay=0.15, hard=True)
    scene slopes2A at ski_shake2:
        zoom 1.8 xpos -1375 ypos -605
    show transition_1b at offscreenright:
        xpos -780
        parallel:
            easein 0.15 xpos -3500
    $renpy.pause(delay=0.15, hard=True)
    hide transition_1b
    window auto show dissolve
    voice "audio/voice/E5/HAR/04/HA/HA026.ogg"
    hachiman "{size=45}AHHHHHHHHHHHHHHHHHHHHH{/size}"
    "Thus I slid down the slope until my vision was blank, white void."
    window auto hide dissolve
    stop voice
    stop sound fadeout 0.5
    stop music fadeout 0.5
    jump E5_CMM_03

label E5_HAR_05:
    scene slopesA with dissolve:
        zoom 1.75 xoffset -300 yoffset -750
    show meguri heavy_coat far vhappy at center with dissolve:
        xoffset 20 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/HAR/05/MG/MG000.ogg"
    meguri "He-y, Hikigaya-kun!"
    "When I looked in the direction of the voice, i saw Shiromeguri-senpai waving her hand, apparently just having slid down from above."
    hachiman "(Oh! The Megurin effect is becoming ever more present on this snowy landscape. And she does look cute in her ski wear.)"
    "I bow lightly to say hi."
    window auto hide dissolve
    hide meguri with dissolve
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE01/SE01_48.ogg"
    $renpy.pause(delay=1.5, hard=True)
    scene slopesA
    show meguri heavy_coat mid surprised at center:
        xoffset 25 yoffset 75
    with dissolve
    $renpy.pause(delay=0.5, hard=True)
    stop sound
    window auto show dissolve
    voice "audio/voice/E5/HAR/05/MG/MG001.ogg"
    meguri "What's wrong? Don't you want to ski with everyone?"
    voice "audio/voice/E5/HAR/05/HA/HA000.ogg"
    hachiman "No, I'm just new to skiing, so I don't know how to do it."
    show meguri happy with dissolve
    voice "audio/voice/E5/HAR/05/MG/MG002.ogg"
    meguri "So that's what it was. You could just ask someone to teach you~"
    "Saying go, Meguri-senpai cocked her head, thought for a moment, then suddenly smiled."
    show meguri vhappy with dissolve
    voice "audio/voice/E5/HAR/05/MG/MG003.ogg"
    meguri "If you're okay with me, I can teach you!"
    voice "audio/voice/E5/HAR/05/HA/HA001.ogg"
    hachiman "Eh, is that okay?"
    hachiman "(If it's Meguri-senpai teaching me, she'll be super patient and nice!)"
    show meguri happy with dissolve
    voice "audio/voice/E5/HAR/05/MG/MG004.ogg"
    meguri "Yep. We'll start with basic sliding."
    voice "audio/voice/E5/HAR/05/HA/HA002.ogg"
    hachiman "Okay then... um, ready anytime."
    show meguri vhappy with dissolve
    voice "audio/voice/E5/HAR/05/MG/MG005.ogg"
    meguri "Yup, leave it to me!"
    window auto hide dissolve
    stop voice
    scene slopesA with fade:
        zoom 1.45 xoffset -215 yoffset 0
    voice "audio/voice/E5/HAR/05/MG/MG006.ogg"
    meguri "Hikigaya-kun, lower your hips more! Keep your legs in a ハ(Ha) shape! Like the in ハ Hachiman-kun."
    voice "audio/voice/E5/HAR/05/HA/HA003.ogg"
    hachiman "Here goes...!"
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_56.ogg"
    show black
    show slopesA zorder 1 at Shake(None, 0.5, dist=100):
        zoom 3.2 yoffset -2390 xcenter 0.23
    $renpy.pause(delay=2.0, hard=True)
    scene slopesA
    show meguri heavy_coat mid unimpressed at center:
        xoffset 25 yoffset 75
    with dissolve
    window auto show dissolve
    hachiman "(Uu... I can't learn to ski in one day...)"
    voice "audio/voice/E5/HAR/05/MG/MG007.ogg"
    meguri "Hmm. Your posture's gotten better, but you still open your legs when you ski."
    hachiman "(If I keep going like this, I feel like my legs will fall off. I'm starting to think this is just a method to torture people.)"
    voice "audio/voice/E5/HAR/05/HA/HA004.ogg"
    hachiman "Um... Shiromeguri-senpai, shouldn't we take a break soon?"
    show meguri happy with dissolve
    voice "audio/voice/E5/HAR/05/MG/MG008.ogg"
    meguri "Sure... But you've mostly got it down, so let's do that in just a bit!"
    hachiman "(We've been doing this over and over for a while and she hasn't let me rest...)"
    hachiman "(Coach Meguri is kind of strict, hey? In retrospect, I can kind of see it.)"
    "Being the former student council president, meguri-senpai can somehow give orders with a heartwarming and very apparant earnestness. That's why she can gain the trust of those around her "
    "and really rally people together."
    "With that same Meguri-senpai in front of me, there's no way she would cut corners."
    show meguri vhappy with dissolve
    voice "audio/voice/E5/HAR/05/MG/MG009.ogg"
    meguri "It's fine, it's fine! I'm sure you'll be able to ski in no time, Hikigaya-kun!"
    hachiman "(It's also true however that her smile always soothes me...)"
    voice "audio/voice/E5/HAR/05/MG/MG010.ogg"
    meguri "All right! Let's go over what I just taught you one more time."
    voice "audio/voice/E5/HAR/05/HA/HA005.ogg"
    hachiman "Okay..."
    hide meguri with dissolve
    "In response to my weak reply, Meguri-senpai gets fired up and starts teaching me again."
    show meguri heavy_coat near happy at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E5/HAR/05/MG/MG011.ogg"
    meguri "Posture is important in skiing. Always be aware that your body's vertical axis should be centered."
    voice "audio/voice/E5/HAR/05/HA/HA006.ogg"
    hachiman "Right."
    voice "audio/voice/E5/HAR/05/MG/MG012.ogg"
    meguri "And then keeping your eyes up and not looking down is also key."
    show meguri vhappy with dissolve
    voice "audio/voice/E5/HAR/05/MG/MG013.ogg"
    meguri "I'll be skiing with you in a back wedge arc, so try to ski after me while looking at my face."
    show meguri happy with dissolve
    voice "audio/voice/E5/HAR/05/MG/MG014.ogg"
    meguri "Okay? I want you to look only at me."
    voice "audio/voice/E5/HAR/05/HA/HA007.ogg"
    hachiman "... Got it."
    hachiman "(\"I want you to look only at me\"... that made my heart skip a beat.)"
    voice "audio/voice/E5/HAR/05/MG/MG015.ogg"
    meguri "Alright, now please get in the basic stance!"
    voice "audio/voice/E5/HAR/05/HA/HA008.ogg"
    hachiman "Let's see, I had to imagine I'm lightly sitting on a chair..."
    show meguri vhappy with dissolve
    voice "audio/voice/E5/HAR/05/MG/MG016.ogg"
    meguri "Yep, yep, exactly! Feet in pigeon-toe position and... are you ready?"
    voice "audio/voice/E5/HAR/05/HA/HA009.ogg"
    hachiman "Yes, ready to go."
    show meguri happy with dissolve
    voice "audio/voice/E5/HAR/05/MG/MG017.ogg"
    meguri "Then here we go!"
    window auto hide dissolve
    stop voice
    $renpy.pause(delay=1.0, hard=True)
    play ambient "audio/sfx/SE01/SE01_42L.ogg"
    window auto show dissolve
    voice "audio/voice/E5/HAR/05/HA/HA010.ogg"
    hachiman "Wooah..."
    show meguri vhappy with dissolve
    voice "audio/voice/E5/HAR/05/MG/MG018.ogg"
    meguri "There you go! Now look at my face while you're doing that."
    "Meguri-senpai smiled a megumeguri~n smile at me while sliding backwards."
    hachiman "(Ahh... the ski slope and senpai are shining... What a dazzling world...)"
    show meguri happy with dissolve
    voice "audio/voice/E5/HAR/05/MG/MG019.ogg"
    meguri "Hikigaya-kun, you're really skiing! It's a new record!"
    voice "audio/voice/E5/HAR/05/HA/HA011.ogg"
    hachiman "Eh, really? W-Woah!"
    window auto hide dissolve
    stop ambient fadeout 0.5
    play sound "audio/sfx/SE01/SE01_56.ogg"
    show black
    show slopesA zorder 1 at Shake(None, 0.5, dist=100):
        zoom 3.2 yoffset -2390 xcenter 0.23
    $renpy.pause(delay=1.0, hard=True)
    show meguri heavy_coat near surprised zorder 2 at center with dissolve:
        xoffset -5 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/HAR/05/MG/MG020.ogg"
    meguri "Ah, Hikigaya-kun, are you okay!?"
    voice "audio/voice/E5/HAR/05/HA/HA012.ogg"
    hachiman "S-Sorry. I messed up again."
    show meguri vhappy with dissolve
    voice "audio/voice/E5/HAR/05/MG/MG021.ogg"
    meguri "That's not true. This your best run yet. Way to go, Hikigaya-kun!"
    "Meguri-senpai patted my head lightly with a big smile."
    voice "audio/voice/E5/HAR/05/HA/HA013.ogg"
    hachiman "... Shiromeguri-senpai"
    show meguri happy with dissolve
    voice "audio/voice/E5/HAR/05/MG/MG022.ogg"
    meguri "Hm? What is it?"
    voice "audio/voice/E5/HAR/05/HA/HA014.ogg"
    hachiman "Skiing is surprisingly fun."
    show meguri vhappy with dissolve
    voice "audio/voice/E5/HAR/05/MG/MG023.ogg"
    meguri "fufu. Yeah, skiing is fun!"
    voice "audio/voice/E5/HAR/05/HA/HA015.ogg"
    hachiman "Can we do it one more time? I think I'm getting the hang of it."
    voice "audio/voice/E5/HAR/05/MG/MG024.ogg"
    meguri "Yeah, of course!"
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    jump E5_CMM_03

label E5_HAR_06:
    voice "audio/voice/E5/HAR/06/HR/HR000.ogg"
    haruno "And you know, Hikigaya-kun made his debut into the advance course~."
    voice "audio/voice/E5/HAR/06/HA/HA000.ogg"
    hachiman "That's because you forced me, isn't it?"
    show hiratsuka happy with dissolve
    voice "audio/voice/E5/HAR/06/SZ/SZ000.ogg"
    hiratsuka "In Hikigaya's case, without being a little forceful, you won't get anywhere with him, and I'm sure he's usually with the result, but considering the odd time it might result in an accident, I can't exactly "
    voice sustain
    hiratsuka "commend you Haruno."
    show haruno happy with dissolve
    voice "audio/voice/E5/HAR/06/HR/HR001.ogg"
    haruno "It was alright~! I was glued to his side the entire time."
    voice "audio/voice/E5/HAR/06/HA/HA001.ogg"
    hachiman "Eh..., ...Is that how it went down?"
    show haruno mid_center worried at right with dissolve:
        xoffset -300 yoffset 75
    voice "audio/voice/E5/HAR/06/HR/HR002.ogg"
    haruno "What~? You didn't notice? Big sis is so dissapointed~..."
    voice "audio/voice/E5/HAR/06/HA/HA002.ogg"
    hachiman "I didn't have time to notice over my flailing down the trail."
    show haruno sly with dissolve
    voice "audio/voice/E5/HAR/06/HR/HR003.ogg"
    haruno "But it felt good, right?"
    voice "audio/voice/E5/HAR/06/HA/HA003.ogg"
    hachiman "It did indeed. Falling down covered in snow and looking up at the sky was quite exhilarating."
    show haruno annoyed with dissolve
    voice "audio/voice/E5/HAR/06/HR/HR004.ogg"
    haruno "I diligently went and helped you out after that, didn't I? Would it hurt you to show a bit of gratitude?"
    voice "audio/voice/E5/HAR/06/HA/HA004.ogg"
    hachiman "Wouldn't you call that just \"doing what I signed up for\"?"
    show haruno happy with dissolve
    voice "audio/voice/E5/HAR/06/HR/HR005.ogg"
    haruno "Still... being able to rely on someone like that... it's not bad, right?"
    show haruno vhappy with dissolve
    voice "audio/voice/E5/HAR/06/HR/HR006.ogg"
    haruno "You're always helping me out with this and that. You know, once in a while."
    voice "audio/voice/E5/HAR/06/HA/HA005.ogg"
    hachiman "............"
    voice "audio/voice/E5/HAR/06/HA/HA006.ogg"
    hachiman "I'm not aware of doing anything to that extend. It's just that I've developed a sense of corporate slavery, in that I have to do what I'm asked to do."
    voice "audio/voice/E5/HAR/06/HR/HR007.ogg"
    haruno "Ahaha, even corporate slaves aren't that diligent, you know."
    hachiman "(Wait, really?)"
    stop music fadeout 0.5
    show haruno annoyed with dissolve
    voice "audio/voice/E5/HAR/06/HR/HR008.ogg"
    haruno "So then, if I called you, would you come to my aid?"
    play music "audio/bgm/BGM47.ogg"
    "Suddenly, as she said this, Haruno-san's eyes seemed to slightly waver between her usual piercing expression and something else."
    voice "audio/voice/E5/HAR/06/HA/HA007.ogg"
    hachiman "I don't think you ever need saving."
    show haruno vhappy with dissolve
    voice "audio/voice/E5/HAR/06/HR/HR009.ogg"
    haruno "Ahaha, you got me again~."
    "Laughing like that seemed like the usual Yukinoshita Haruno. I wondered if that just now was an illusion."
    voice "audio/voice/E5/HAR/06/HA/HA008.ogg"
    hachiman "............"
    hide hiratsuka with dissolve
    show yukino home near_center frown at left with dissolve:
        xoffset -220 yoffset 75
    voice "audio/voice/E5/HAR/06/YK/YK000.ogg"
    yukino "Hikigaya-kun, you need not so diligently keep this drunk company."
    voice "audio/voice/E5/HAR/06/HA/HA009.ogg"
    hachiman "R-right. I didn't mean to, but..."
    show yukino unimpressed with dissolve
    voice "audio/voice/E5/HAR/06/YK/YK001.ogg"
    yukino "Haah... Good grief. You drink too much, Nee-san."
    show haruno sweater mid_left happy at right with dissolve:
        xoffset -235 yoffset 75
    voice "audio/voice/E5/HAR/06/HR/HR010.ogg"
    haruno "...I guess so... It's been a while since I could let loose and have fun, so I really got into it. ...What about you, Yukino-chan? Are you having fun?"
    show yukino frown with dissolve
    voice "audio/voice/E5/HAR/06/YK/YK002.ogg"
    yukino "As long as there are no drunkards involved. Let's go, Hikigaya-kun."
    voice "audio/voice/E5/HAR/06/HA/HA010.ogg"
    hachiman "R-right..."
    hide yukino with dissolve
    show haruno vhappy with dissolve
    voice "audio/voice/E5/HAR/06/HR/HR011.ogg"
    haruno "Hahah, he got away..."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    scene black with Fade(1.0, 0.5, 0)
    image haruno sweater mid_left happy_flat = Flatten("haruno sweater mid_left happy")
    scene lodge_EC with Fade(1.0, 0.5, 1.0)
    $renpy.pause(delay=2.0, hard=True)
    show haruno sweater mid_left happy_flat at center:
        xoffset -260 yoffset 75 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.6 xoffset -380
            linear 1.0 xoffset -260
    $renpy.pause(delay=2.0, hard=True)
    scene lodgeC with dissolve
    voice "audio/voice/E5/HAR/06/HR/HR012.ogg"
    haruno "............"
    voice "audio/voice/E5/HAR/06/SZ/SZ001.ogg"
    hiratsuka "You look like you're having a blast, Haruno."
    window auto hide dissolve
    stop voice
    scene lodgeC:
        zoom 2 yoffset -350
    show hiratsuka home near_left happy at center:
        xoffset 440 yoffset 80
    with dissolve
    play music "audio/bgm/BGM46.ogg"
    window auto hide dissolve
    voice "audio/voice/E5/HAR/06/HR/HR013.ogg"
    haruno "Because ski camps are so exciting, aren't they? It's been a long time since I've been in this kind of mood~."
    voice "audio/voice/E5/HAR/06/SZ/SZ002.ogg"
    hiratsuka "I can't believe you asked someone to come to your aid."
    voice "audio/voice/E5/HAR/06/HR/HR014.ogg"
    haruno "............"
    voice "audio/voice/E5/HAR/06/HR/HR015.ogg"
    haruno "Well, that's where the conversation went, right?"
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E5/HAR/06/SZ/SZ003.ogg"
    hiratsuka "That's what it was? And here I thought it was a good sign for you."
    voice "audio/voice/E5/HAR/06/HR/HR016.ogg"
    haruno "Shizuka-chan, you shouldn't keep looking over things as a teacher. With that overly lecture-ish nature, you won't be able to get married."
    show hiratsuka surprised with dissolve
    voice "audio/voice/E5/HAR/06/SZ/SZ004.ogg"
    hiratsuka "What?!"
    voice "audio/voice/E5/HAR/06/HR/HR017.ogg"
    haruno "Ahaha, Shizuka-chan, you're so cute~."
    show hiratsuka blush with dissolve
    voice "audio/voice/E5/HAR/06/SZ/SZ005.ogg"
    hiratsuka "You can't just take a grown woman and call her cute like that."
    voice "audio/voice/E5/HAR/06/SZ/SZ006.ogg"
    hiratsuka "Seriously... This is what I get for carelessly drinking with you."
    voice "audio/voice/E5/HAR/06/HR/HR018.ogg"
    haruno "............"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    $renpy.pause(delay=0.5, hard=True)
    image haruno mid_left sad flat = Flatten("haruno sweater mid_left sad")
    scene loading_wlogo
    show haruno mid_left sad flat at center:
        xoffset -260 yoffset 75 alpha 1.0
        on hide:
            parallel:
                1.3
                linear 0.3 alpha 0
            parallel:
                easein 0.6 xoffset -200
                easeout 1.0 xoffset -380
    with Dissolve(1.0)
    $renpy.pause(delay=2.0, hard=True)
    hide haruno
    $renpy.pause(delay=3.0, hard=True)
    jump E5_CMM_04

label E5_HAR_07:
    window auto show dissolve
    voice "audio/voice/E5/HAR/07/HA/HA000.ogg"
    hachiman "Let's see... The guest bedrooms, huh?"
    show yukino home mid_center stare at center with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E5/HAR/07/YK/YK000.ogg"
    yukino "...Guest bedroom clean up."
    hachiman "(Oh, I'm with Yukinoshita.)"
    show yukino happy with dissolve
    voice "audio/voice/E5/HAR/07/YK/YK001.ogg"
    yukino "Oh, you too, Hikigaya-kun? Let's get this done quickly, shall we?"
    voice "audio/voice/E5/HAR/07/HA/HA001.ogg"
    hachiman "Yeah, let's."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    scene lodgeroomA
    show yukino home mid_center happy at center:
        xoffset -105 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E5/HAR/07/YK/YK002.ogg"
    yukino "I'll take care of cleaning the inside and making beds, you can collect all the trash and throw it out in one go."
    voice "audio/voice/E5/HAR/07/HA/HA002.ogg"
    hachiman "Roger."
    hide yukino with dissolve
    play ambient "audio/sfx/SE01/SE01_15.ogg"
    "While exchanging few words, Yukinoshita deftly put all the beds in order."
    "As for me, following Yukinoshita's instructions, I spread out the sheets and helped her fold them nearby."
    window auto hide dissolve
    stop ambient
    scene lodgeroomA at truecenter:
        zoom 2.0 xalign 0 ypos 740
    show yukino home mid_left unimpressed at center:
        xoffset 50 yoffset 80
    with dissolve
    play music "audio/bgm/BGM46.ogg"
    window auto show dissolve
    voice "audio/voice/E5/HAR/07/YK/YK003.ogg"
    yukino "...By the way."
    voice "audio/voice/E5/HAR/07/HA/HA003.ogg"
    hachiman "What's up?"
    show yukino sad with dissolve
    voice "audio/voice/E5/HAR/07/YK/YK004.ogg"
    yukino "Nee-san is always like that, but yesterday, she really was constantly all around you."
    show yukino happy with dissolve
    voice "audio/voice/E5/HAR/07/YK/YK005.ogg"
    yukino "It seems she had you trapped during the day, but for the rest of the time, Hikigaya-kun, you don't have to put up with her. You know that, right?"
    voice "audio/voice/E5/HAR/07/HA/HA004.ogg"
    hachiman "I didn't intend to, but, well, the way things went..."
    "I feel a little embarassed by what I was saying, because it felt like I was making excuses. To my relief, though, Yukinoshita didn't seem to percieve it that way."
    hachiman "(I'm embarassed by acting like a run-of-the-mill teenager... Rather I'm embarassed about having this thought.)"
    voice "audio/voice/E5/HAR/07/HA/HA005.ogg"
    hachiman "I feel like I can't escape from that person. She's like the Great Demon King."
    show yukino angry with dissolve
    voice "audio/voice/E5/HAR/07/YK/YK006.ogg"
    yukino "Like you can't escape..."
    voice "audio/voice/E5/HAR/07/HA/HA006.ogg"
    hachiman "Well, that was just a metaphor. Let's just get this job done."
    show yukino surprised with dissolve
    voice "audio/voice/E5/HAR/07/YK/YK007.ogg"
    yukino "Y-yes. You're right."
    play ambient "audio/sfx/SE01/SE01_15.ogg"
    show yukino sad with dissolve
    voice "audio/voice/E5/HAR/07/YK/YK008.ogg"
    yukino "............"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    jump E5_CMM_05

label E5_HAR_08:
    scene slopesA with dissolve
    window auto show dissolve
    stop sound fadeout 1.0
    hachiman "(Now then... What should I do today? Speaking of, I wonder if she's going to teach me again today...)"
    "With that in mind, I headed for the slopes, and even though I wasn't looking for her in particular, I soon found Haruno-san."
    play music "audio/bgm/BGM21.ogg"
    show haruno athletic far_left sad at center with dissolve:
        xoffset 225 yoffset 75
    voice "audio/voice/E5/HAR/08/HR/HR000.ogg"
    haruno "............"
    "Her stylish ski outfit made her stand out on the slopes. In addition, she was currenlty looking in another direction with a somewhat sorrowful expression her face, which made her ennui even more eye-catching."
    hide haruno with dissolve
    hachiman "(Conspicious as ever... I find her easily thanks to her standing out. But, it's rare to see her standing so absent-mindedly.)"
    window auto hide dissolve
    scene slopesA at right with dissolve:
        zoom 1.5 xoffset 0 yoffset 100
    window auto show dissolve
    "As I was thinking things along those lines, I stepped onto the crispy snow, and that made Haruno-san suddenly turn her head."
    show haruno athletic mid_center happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/HAR/08/HR/HR001.ogg"
    haruno "Ah, Hikigaya-kun. Want to go skiing with big sis again today?"
    voice "audio/voice/E5/HAR/08/HA/HA000.ogg"
    hachiman "Not in particular..."
    "I didn't want to step into the lion's den of a ski course. I looked around if anyone there was kind and willing enough to teach me..."
    window auto hide dissolve
    scene slopesA at left:
        zoom 1.5 xoffset 0 yoffset 105
    show yukino heavy_coat far_left sad at center:
        xoffset 10 yoffset 80
    with dissolve
    voice "audio/voice/E5/HAR/08/YK/YK000.ogg"
    yukino "............"
    "I saw Yukinoshita resting in a spot some ways away from from Komachi and Yuigahama."
    "It seems she is trying to be considerate of Yuigahama and Komachi. However, I can see she is also physically exhausted. It seems she was what Haruno-san was looking at earlier."
    window auto hide dissolve
    scene slopesA at right:
        zoom 1.5 xoffset 0 yoffset 100
    show haruno athletic mid_center happy at center:
        xoffset 10 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/HAR/08/HA/HA001.ogg"
    hachiman "Give me a second..."
    voice "audio/voice/E5/HAR/08/HR/HR002.ogg"
    haruno "............"
    window auto hide dissolve
    stop voice
    scene slopesA at left:
        zoom 2.0 xoffset 0 yoffset 310
    show yukino heavy_coat mid_left sad at center:
        xoffset 20 yoffset 80
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E5/HAR/08/HA/HA002.ogg"
    hachiman "Yukinoshita, how are you holding up?"
    show yukino happy with dissolve
    voice "audio/voice/E5/HAR/08/YK/YK001.ogg"
    yukino "Hikigaya...-kun? What is it?"
    voice "audio/voice/E5/HAR/08/HA/HA003.ogg"
    hachiman "Don't \"What is it\" me... I'm taking a break, so stay with me here for a bit."
    window auto hide dissolve
    stop voice
    scene slopesA at right:
        zoom 1.5 xoffset 0 yoffset 100
    show haruno athletic mid_center sly at center:
        xoffset 10 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/HAR/08/HR/HR003.ogg"
    haruno "Hmm..."
    window auto hide dissolve
    stop voice
    scene slopesA
    show yukino heavy_coat mid_center sad at center:
        xoffset -105 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E5/HAR/08/YK/YK002.ogg"
    yukino "............"
    play sound "audio/sfx/SE01/SE01_77.ogg"
    $renpy.pause(delay=1.0, hard=False)
    voice "audio/voice/E5/HAR/08/HA/HA004.ogg"
    hachiman "Black tea's fine, right?"
    show yukino vhappy with dissolve
    voice "audio/voice/E5/HAR/08/YK/YK003.ogg"
    yukino "Yes. Thank you."
    voice "audio/voice/E5/HAR/08/HA/HA005.ogg"
    hachiman "Ah, give me a second."
    play sound "audio/sfx/SE01/SE01_76.ogg"
    $renpy.pause(delay=0.75,hard=True)
    voice "audio/voice/E5/HAR/08/HA/HA006.ogg"
    hachiman "Here, drink up, alright?"
    show yukino avoid with dissolve
    voice "audio/voice/E5/HAR/08/YK/YK004.ogg"
    yukino "I can open the lid myself."
    voice "audio/voice/E5/HAR/08/HA/HA007.ogg"
    hachiman "If your hands are that numb, you'll have a hard time."
    show yukino vhappy with dissolve
    voice "audio/voice/E5/HAR/08/YK/YK005.ogg"
    yukino "...I feel warmer."
    voice "audio/voice/E5/HAR/08/HA/HA008.ogg"
    hachiman "Are you? You want me to borrow you a blanket or something like that?"
    voice "audio/voice/E5/HAR/08/YK/YK006.ogg"
    yukino "No... This is more than enough. You're being a little dramatic, Hikigaya-kun."
    voice "audio/voice/E5/HAR/08/HA/HA009.ogg"
    hachiman "It's a good excuse to get away from that person. I wanted a break, too."
    show yukino happy with dissolve
    voice "audio/voice/E5/HAR/08/YK/YK007.ogg"
    yukino "I see. I don't think you can escape her that easily, however."
    voice "audio/voice/E5/HAR/08/HA/HA010.ogg"
    hachiman "Huh?"
    show haruno athletic near_left vhappy at right with dissolve:
        xoffset 70 yoffset 75
    voice "audio/voice/E5/HAR/08/HR/HR004.ogg"
    haruno "Hikigaya-kun, you look like Yukino-chan's big brother."
    voice "audio/voice/E5/HAR/08/YK/YK008.ogg"
    yukino "............"
    voice "audio/voice/E5/HAR/08/HA/HA011.ogg"
    hachiman "W-well... Yukinoshita was taking care of Komachi, so I just happened to notice from the beginning."
    show haruno sly with dissolve
    voice "audio/voice/E5/HAR/08/HR/HR005.ogg"
    haruno "I've never seen Yukino-chan taken care of like that before."
    show yukino vhappy with dissolve
    voice "audio/voice/E5/HAR/08/YK/YK009.ogg"
    yukino "Of course, Nee-san. You're not the kind of person to care about things like this."
    show haruno surprised with dissolve
    voice "audio/voice/E5/HAR/08/HR/HR006.ogg"
    haruno "............"
    show haruno happy with dissolve
    voice "audio/voice/E5/HAR/08/HR/HR007.ogg"
    haruno "Hmm. I see how it is."
    hachiman "(What do you \"see now\"? I have no idea. Isn't that scary? It is...)"
    show haruno athletic near_center vhappy at right with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/HAR/08/HR/HR008.ogg"
    haruno "Then, Hikigaya-kun, I'm going to go ski on my own. If it gets too hard for you out here, come get me and accompany me back to the lodge, okay? Thanks."
    voice "audio/voice/E5/HAR/08/HA/HA012.ogg"
    hachiman "Ah, sure..."
    hide haruno with dissolve
    hachiman "(By the way, she doesn't pry into Yukinoshita like she usually does...)"
    window auto hide dissolve
    scene lodgeoutC with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "I always knew it will happen, but the sun goes down incredibly quick in the winter. It's as if a switch gets switched off and we get plunged into darkness."
    voice "audio/voice/E5/HAR/08/HA/HA013.ogg"
    hachiman "Well, let's finally get some rest."
    window auto hide dissolve
    stop voice
    play sound "audio/sfx/SE04/SE04_03.ogg"
    scene lodge2A with dissolve
    window auto show dissolve
    "By the time I had managed to get Yukinoshita back to the lodge to rest, it was completely dark outside."
    hachiman "(Camp is ending today. The sky looks somehow lonely tonight...)"
    hachiman "(I'm gonna take a bath and relax while I still can... Tomorrow we're going back home and it's bound to get noisy.)"
    window auto hide dissolve
    stop music fadeout 1.0
    jump E5_HAR_10

label E5_HAR_09:
    "Meguri-senpai waved her hands and called out to everyone."
    hachiman "(I wonder if everyone can hear her. It's not like we've booked the whole slope to ourselves.)"
    hide meguri with dissolve
    "At any rate, I decided to head towards her. People who seemed to have heard her voice were gradually gathering around Meguri-senpai."
    show totsuka heavy_coat mid_center happy at center with dissolve:
        yoffset 75 xoffset 10
    voice "audio/voice/E5/HAR/09/SI/SI000.ogg"
    totsuka "Ah, Hachiman, where were you? I was looking for you."
    hachiman "(I want to record what you just said and keep it forever...!)"
    voice "audio/voice/E5/HAR/09/HA/HA000.ogg"
    hachiman "Oh, I was just practicing."
    show totsuka vhappy with dissolve
    voice "audio/voice/E5/HAR/09/SI/SI001.ogg"
    totsuka "Oh, I see! Well, let's ski together then!"
    voice "audio/voice/E5/HAR/09/HA/HA001.ogg"
    hachiman "O-Okay!"
    hide totsuka with dissolve
    hachiman "(Skiing is pretty neat, isn't it? I really like skiing...)"
    show yukino heavy_coat mid_center happy at left:
        xoffset -170 yoffset 75
    show yui heavy_coat mid_center vhappy at center:
        xoffset 10 yoffset 75
    show komachi heavy_coat mid_left happy at right:
        xoffset -75 yoffset 75
    voice "audio/voice/E5/HAR/09/YI/YI000.ogg"
    yui "Ah, Hikki~!"
    voice "audio/voice/E5/HAR/09/KO/KO000.ogg"
    komachi "Onii-chan. Can you ski already?"
    voice "audio/voice/E5/HAR/09/HA/HA002.ogg"
    hachiman "Sure can. Did you guys ski together?"
    window auto hide dissolve
    stop voice
    scene slopesA:
        zoom 2.0 xpos -1280 ypos -780
    show meguri heavy_coat mid happy at center:
        xoffset 25 yoffset 75
    with fade
    voice "audio/voice/E5/HAR/09/MG/MG001.ogg"
    meguri "Phew. We can't get everyone, but most of us are here."
    voice "audio/voice/E5/HAR/09/YK/YK000.ogg"
    yukino "More importantly... Shiromeguri-senpai, did you need us for something?"
    show meguri vhappy with dissolve
    voice "audio/voice/E5/HAR/09/MG/MG002.ogg"
    meguri "Yep! It's our last day here, so I thought we could all ski together!"
    voice "audio/voice/E5/HAR/09/HA/HA003.ogg"
    hachiman "Is skiing something everyone does together?"
    "I hated myself for inadvertently quipping at Meguri-senapi as she was smiling a friendly smile."
    show meguri frown with dissolve
    voice "audio/voice/E5/HAR/09/MG/MG003.ogg"
    meguri "Eh, since we're all here together, we should do it togehter~!"
    hachiman "(The snowy mountain cold extinguishing MeguMeguMeguSnugBust GigaMegurin effect blows away any fatigue I had in an instant...)"
    show meguri vhappy with dissolve
    voice "audio/voice/E5/HAR/09/MG/MG004.ogg"
    meguri "So let's ski together!"
    voice "audio/voice/E5/HAR/09/WB/WB000.ogg"
    prevscm "Yeah!"
    voice "audio/voice/E5/HAR/09/YK/YK001.ogg"
    yukino "........"
    window auto hide dissolve
    stop voice
    scene slopesA at right:
        zoom 1.5 xoffset 250 yoffset 100
    show hayama heavy_coat mid_right happy at left:
        xoffset 135 yoffset 70
    show yumiko heavy_coat mid_left sad at right behind hayama:
        xoffset -255 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/HAR/09/YM/YM000.ogg"
    yumiko "I wanted to ski with Hayato though..."
    show hayama vhappy with dissolve
    voice "audio/voice/E5/HAR/09/HY/HY000.ogg"
    hayama "Well since we're all here together, I think this is the way to go."
    hide hayama
    hide yumiko
    with dissolve
    show ebina heavy_coat mid_center vhappy at left:
        xoffset 130 yoffset 75
    show iroha heavy_coat mid_center sad at right behind ebina:
        xoffset -125 yoffset 75
    show tobe heavy_coat mid vhappy at center behind iroha:
        xoffset 10 yoffset 75
    with dissolve
    voice "audio/voice/E5/HAR/09/TB/TB000.ogg"
    tobe "Man, this is kinda exciting! Right, Irohasu?"
    voice "audio/voice/E5/HAR/09/IR/IR000.ogg"
    iroha "W-Well, I agree, maybe we should do this for once."
    voice "audio/voice/E5/HAR/09/EB/EB000.ogg"
    ebina "Yep, yep. No objections here! You can see all the HayaHachi, TotsuHachi and NPC-Hachi you want."
    hachiman "(What the hell is NPC-Hachi...? Moreover, I'm ending up on the recieving end in one too many of these ships now...)"
    window auto hide dissolve
    show meguriSki with dissolve
    window auto show dissolve
    voice "audio/voice/E5/HAR/09/MG/MG005.ogg"
    meguri "Yep, yep! Let's make this something everyone will remember!"
    hachiman "(Well, I don't know what we'll actually be doing in such a large crowd...)"
    voice "audio/voice/E5/HAR/09/HA/HA004.ogg"
    hachiman "Isn't it actually pretty amazing you can gather such a crowd, Shiromeguri-senpai?"
    voice "audio/voice/E5/HAR/09/MG/MG006.ogg"
    meguri "Hearing you say that makes me happy, Hikigaya-kun."
    voice "audio/voice/E5/HAR/09/MG/MG007.ogg"
    meguri "Ehehe, let's all ski together then, everyone!"
    voice "audio/voice/E5/HAR/09/WB/WB001.ogg"
    prevscm "Yeah!"
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    jump E5_CMM_06

label E5_HAR_10:
    scene skyC with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "Tonight was the last day of the camp and the living room was filled with excitement as if we'd just arrived. 2 nights and 3 days went by so fast."
    hachiman "(Maybe I can take a bath alone now.)"
    window auto hide dissolve
    play sound ["<silence 1.0>", "audio/sfx/SE04/SE04_08.ogg"]
    scene hotspringBGB with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    hachiman "(Ugh...)"
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_31.ogg"
    show hachimanBatha with dissolve
    $renpy.pause(delay=1.0, hard=True)
    play music "audio/bgm/BGM21.ogg"
    window auto show dissolve
    voice "audio/voice/E5/HAR/10/HY/HY000.ogg"
    hayama "I'd never thought I'd be in the bath with you like this..."
    voice "audio/voice/E5/HAR/10/HA/HA000.ogg"
    hachiman "That's my line."
    hachiman "(Bathing together with Hayama of all people...)"
    voice "audio/voice/E5/HAR/10/HY/HY001.ogg"
    hayama "Are you getting any better at skiing? I heard you had it rough yesterday."
    voice "audio/voice/E5/HAR/10/HA/HA001.ogg"
    hachiman "Well, I didn't die at least."
    voice "audio/voice/E5/HAR/10/HY/HY002.ogg"
    hayama "...From now, you'll be have a rough time - all the time."
    voice "audio/voice/E5/HAR/10/HA/HA002.ogg"
    hachiman "Is that advice? Or, is it warning?"
    voice "audio/voice/E5/HAR/10/HY/HY003.ogg"
    hayama "No, no. Just a prediction, really."
    window auto hide dissolve
    stop voice
    show hachimanBatha at topleft with dissolve:
        zoom 1.7 xoffset -17 yoffset -312
    window auto show dissolve
    voice "audio/voice/E5/HAR/10/HA/HA003.ogg"
    hachiman "I'll be having worse than just a rough time, aren't I?"
    voice "audio/voice/E5/HAR/10/HY/HY004.ogg"
    hayama "Even if I give you advice, you wouldn't listen to it, would it?"
    voice "audio/voice/E5/HAR/10/HA/HA004.ogg"
    hachiman "What are you talking about? I always listen. In fact, I even think you're right."
    voice "audio/voice/E5/HAR/10/HY/HY005.ogg"
    hayama "I see. As long as you understand, that's good enough. From now on, I'll be talking to myself."
    voice "audio/voice/E5/HAR/10/HA/HA005.ogg"
    hachiman "Huh?"
    voice "audio/voice/E5/HAR/10/HY/HY006.ogg"
    hayama "If possible, I'd be happy to truly get along."
    voice "audio/voice/E5/HAR/10/HY/HY007.ogg"
    hayama "That's something I can't do... and she can't, either. If only we all could have been better liars... But we have no right to be."
    voice "audio/voice/E5/HAR/10/HA/HA006.ogg"
    hachiman "Huh? What are you talking about?"
    hide hachimanBatha with dissolve
    voice "audio/voice/E5/HAR/10/HY/HY008.ogg"
    hayama "I told you, right? I'm talking to myself."
    voice "audio/voice/E5/HAR/10/HA/HA007.ogg"
    hachiman "Ah, right."
    "As soon as I said that, the bathing room was filled with steam and silence once again. The sound of water echoed, and somewhere, snow fell."
    show hachimanBatha with dissolve
    voice "audio/voice/E5/HAR/10/HA/HA008.ogg"
    hachiman "We should have all been better liars... Me included."
    voice "audio/voice/E5/HAR/10/HY/HY009.ogg"
    hayama "What?"
    voice "audio/voice/E5/HAR/10/HA/HA009.ogg"
    hachiman "We're talking to ourselves, remember?"
    voice "audio/voice/E5/HAR/10/HY/HY010.ogg"
    hayama "I see."
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    if ski_flag == "meguri":
        call loading_screen(duration="short") from _call_loading_screen_39
        scene skyC with fade
        play music "audio/bgm/BGM10.ogg"
        window auto show dissolve
        hachiman "(I wanted to take a breather in the bath, but I ended up in a batting cage with Hayama of all people. I guess this really is the age of HayaHachi...)"
        hachiman "(Well, only thing left to do for me is to go to sleep. With this, the camp is over...)"
        play sound "audio/sfx/SE00/SE00_30L.ogg"
        hachiman "(Ahh, and here I thought I could relax and forget about everything...)"
        stop sound fadeout 1.0
        stop music fadeout 1.0
        call loading_screen(33) from _call_loading_screen_40
        jump E6_CMM_01

    image haruno coat mid_center angry_flat = Flatten("haruno coat mid_center angry")
    scene lodgeoutLoading with Dissolve(1.0)
    $renpy.pause(delay=2.0, hard=True)
    show haruno coat mid_center angry_flat at center:
        xoffset -260 yoffset 75 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.6 xoffset -380
            linear 1.0 xoffset -260
    $renpy.pause(delay=2.5, hard=True)
    show harunoyukinoout with dissolve
    play music "audio/bgm/BGM47.ogg"
    window auto show dissolve
    voice "audio/voice/E5/HAR/10/HR/HR000.ogg"
    haruno "What's the matter, Yukino-chan? You called me out of the blue. Bis sis is gonna catch a cold~."
    voice "audio/voice/E5/HAR/10/YK/YK000.ogg"
    yukino "Thank you for what you did today. I'm sorry if I've made you worry about me."
    voice "audio/voice/E5/HAR/10/HR/HR001.ogg"
    haruno "Oh, come on. You should be thanking Hikigaya-kun instead."
    voice "audio/voice/E5/HAR/10/YK/YK001.ogg"
    yukino "I already have."
    window auto hide dissolve
    show harunoyukinoout at right with dissolve:
        zoom 1.6 xoffset 260 yoffset 430
    window auto show dissolve
    voice "audio/voice/E5/HAR/10/HR/HR002.ogg"
    haruno "That so? Well, you didn't have to worry about me."
    voice "audio/voice/E5/HAR/10/YK/YK002.ogg"
    yukino "I do worry. The same way you worry about me."
    voice "audio/voice/E5/HAR/10/HR/HR003.ogg"
    haruno "Ah... Really, there are other people you should be worried about."
    voice "audio/voice/E5/HAR/10/YK/YK003.ogg"
    yukino "Yes. So let me be crystal clear."
    hide harunoyukinoout
    show harunoyukinoout
    with dissolve
    voice "audio/voice/E5/HAR/10/YK/YK004.ogg"
    yukino "Don't even think about doing anything to hurt my friend. If you do, even if you are my sister, I won't forgive you."
    voice "audio/voice/E5/HAR/10/HR/HR004.ogg"
    haruno "Haha... Yukino-chan, I've never seen you get this serious before."
    voice "audio/voice/E5/HAR/10/YK/YK005.ogg"
    yukino "...Eh."
    voice "audio/voice/E5/HAR/10/HR/HR005.ogg"
    haruno "I like this Yukino-chan."
    voice "audio/voice/E5/HAR/10/YK/YK006.ogg"
    yukino "............"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    $renpy.pause(delay=0.5, hard=True)
    scene loading_wlogo
    show haruno coat mid_center angry_flat at center:
        xoffset -260 yoffset 75 alpha 1.0
        on hide:
            parallel:
                1.3
                linear 0.3 alpha 0
            parallel:
                easein 0.6 xoffset -200
                easeout 1.0 xoffset -380
    with Dissolve(1.0)
    $renpy.pause(delay=2.0, hard=True)
    hide haruno
    $renpy.pause(delay=3.0, hard=True)
    scene lodge2A with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    hachiman "(Ah... My bath seemed a lot longer thanks to Hayama. I don't even know how we both went in at the same time.)"
    hachiman "(Nothing left but to go to sleep...)"
    window auto hide dissolve
    play sound "audio/sfx/SE04/SE04_05.ogg"
    scene black with dissolve
    $renpy.pause(delay=0.5, hard=True)
    stop sound
    window auto show dissolve
    voice "audio/voice/E5/HAR/10/HR/HR006.ogg"
    mystery "............"
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_54.ogg"
    show harunohachimanroomA at left, Shake((0, 0, 0, 0), 0.35, dist=100):
        zoom 2.0 yoffset -1070
    $renpy.pause(delay=1.0, hard=True)
    stop sound
    play music "audio/bgm/BGM22.ogg"
    hide harunohachimanroomA
    show harunohachimanroomA
    with dissolve
    window auto show dissolve
    hachiman "(Huh...?)"
    "As soon as I entered the room, I was pushed against the wall by a serious looking Haruno-san. The suddenness of the situation left me dumbfounded, unable to move."
    "Her moonlight face looked somehow captivating as she stared me down."
    voice "audio/voice/E5/HAR/10/HA/HA010.ogg"
    hachiman "...Is this some new way to toy with me?"
    "As her supple fingers caressed my cheek, I felt my breath catch in my throat."
    voice "audio/voice/E5/HAR/10/HR/HR007.ogg"
    haruno "You really are wasted on Yukino-chan."
    voice "audio/voice/E5/HAR/10/HA/HA011.ogg"
    hachiman "I'm wasted... on Yukinoshita?"
    voice "audio/voice/E5/HAR/10/HR/HR008.ogg"
    haruno "I was hoping you might be able to change Yukino-chan."
    voice "audio/voice/E5/HAR/10/HA/HA012.ogg"
    hachiman "It's not my place to change people."
    voice "audio/voice/E5/HAR/10/HA/HA013.ogg"
    hachiman "And besides... you don't want to change other people in the first place."
    show harunohachimanroomB with dissolve
    voice "audio/voice/E5/HAR/10/HR/HR009.ogg"
    haruno "That's right. You're wasted on Yukino-chan. You really are."
    voice "audio/voice/E5/HAR/10/HA/HA014.ogg"
    hachiman "............"
    hide harunohachimanroomB with dissolve
    voice "audio/voice/E5/HAR/10/HR/HR010.ogg"
    haruno "Hey, wanna make a deal?"
    voice "audio/voice/E5/HAR/10/HA/HA015.ogg"
    hachiman "A... deal?"
    voice "audio/voice/E5/HAR/10/HR/HR011.ogg"
    haruno "That's right, a deal. I will take responsibility for all your lies."
    voice "audio/voice/E5/HAR/10/HA/HA016.ogg"
    hachiman "I don't know what you're talking about..."
    voice "audio/voice/E5/HAR/10/HR/HR012.ogg"
    haruno "You'll never get to what you say is the geniune thing. There is no such thing as a relationship without deception and lies. That's why you've all been stuck in limbo, unmoving, clinging to that fantasy."
    voice "audio/voice/E5/HAR/10/HA/HA017.ogg"
    hachiman "............"
    voice "audio/voice/E5/HAR/10/HR/HR013.ogg"
    haruno "So, if you and Yukino-chan can't tell lies, I will do it for you. I'll tell that lie for you no and no matter what, these relationships will change."
    voice "audio/voice/E5/HAR/10/HA/HA018.ogg"
    hachiman "What exactly are you planning on doing?"
    window auto hide dissolve
    stop voice
    show harunohachimanroomA at top:
        zoom 1.3 xoffset 70
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/HAR/10/HR/HR014.ogg"
    haruno "I wonder~. How about I make you mine? Then, I'm going to destroy all of the built up walls. That way, when everything is broken down, what remain is..."
    voice "audio/voice/E5/HAR/10/HA/HA019.ogg"
    hachiman "That's..."
    "In a sense, that could be called the real thing. That which hides in the innermost part, behind the walls and lies."
    voice "audio/voice/E5/HAR/10/HA/HA020.ogg"
    hachiman "What do you get out of this... deal?"
    voice "audio/voice/E5/HAR/10/HR/HR015.ogg"
    haruno "Mhm~. A lot of things. For me, for you, for Yukino-chan. For example... You can be freed from this \"genuine article\" illusion."
    voice "audio/voice/E5/HAR/10/HA/HA021.ogg"
    hachiman "............"
    "-Oh, she doesn't believe in the true, genuine thing, yet she wants to find it more than anyone else."
    "So she defiles, pollutes, destroys, damages... But in the end, still searches for and struggles to obtain what is left behind."
    "The destructive purity of it was so vivid that I-"
    hide harunohachimanroomA
    show harunohachimanroomA
    with dissolve
    voice "audio/voice/E5/HAR/10/HA/HA022.ogg"
    hachiman "It's a deal with the devil..."
    voice "audio/voice/E5/HAR/10/HR/HR016.ogg"
    haruno "Maybe. But... a contract is stronger bond than love, don't you think?"
    voice "audio/voice/E5/HAR/10/HA/HA023.ogg"
    hachiman "You say that like love itself is not a contract."
    voice "audio/voice/E5/HAR/10/HR/HR017.ogg"
    haruno "That's very like you to say... So, what's your answer?"
    voice "audio/voice/E5/HAR/10/HA/HA024.ogg"
    hachiman "To just decide something like that..."
    voice "audio/voice/E5/HAR/10/HR/HR018.ogg"
    haruno "By the way, I will take both words and silence as yes."
    voice "audio/voice/E5/HAR/10/HA/HA025.ogg"
    hachiman "Huh? That's an impossible scenar-"
    window auto hide dissolve
    stop voice
    stop music
    show harunohachimanroomA at center:
        zoom 2.0 xoffset 330 yoffset 30
    $renpy.pause(delay=0.25, hard=True)
    window auto show dissolve
    voice "audio/voice/E5/HAR/10/HA/HA026.ogg"
    hachiman "............"
    "For a moment, I didn't know what had happened. I saw Haruno-san's brilliant, beautiful face closing in on me, and then her soft lips were firmly pressed against mine. My head went numb, unable to formulate a thought."
    voice "audio/voice/E5/HAR/10/HR/HR019.ogg"
    haruno "............"
    voice "audio/voice/E5/HAR/10/HA/HA027.ogg"
    hachiman "............"
    show harunohachimanroomB with dissolve
    voice "audio/voice/E5/HAR/10/HR/HR020.ogg"
    haruno "The contract is sealed."
    voice "audio/voice/E5/HAR/10/HA/HA028.ogg"
    hachiman "You can't just..."
    window auto hide dissolve
    scene black with fade
    play sound "audio/sfx/SE04/SE04_05.ogg"
    $renpy.pause(delay=1.0, hard=True)
    scene lodge2A
    show transition_1a at offscreenright:
        xpos -780
        parallel:
            easein 0.15 xpos -3500
    $renpy.pause(delay=0.15, hard=True)
    hide transition_1a
    play sound "<to 0.75>audio/sfx/SE00/SE00_31.ogg"
    $renpy.pause(delay=0.75, hard=True)
    window auto show dissolve
    hachiman "(What just happened...?)"
    hachiman "(For her usual teasing, this went a bit far.)"
    voice "audio/voice/E5/HAR/10/HA/HA029.ogg"
    hachiman "............"
    hachiman "(I just wanted to take a bath...)"
    voice "audio/voice/E5/HAR/10/YK/YK007.ogg"
    mystery "...Hikigaya-kun."
    voice "audio/voice/E5/HAR/10/HA/HA030.ogg"
    hachiman "Hmm?"
    window auto hide dissolve
    jump E5_HAR_11

label E5_HAR_11:
    play music "audio/bgm/BGM46.ogg"
    show yukino home near_center sad at center with dissolve:
        xoffset -165 yoffset 75
    voice "audio/voice/E5/HAR/11/HA/HA000.ogg"
    hachiman "Yukinoshita? What's up?"
    voice "audio/voice/E5/HAR/11/YK/YK000.ogg"
    yukino "Could I talk to you for a bit?"
    voice "audio/voice/E5/HAR/11/HA/HA001.ogg"
    hachiman "Are you feeling better, by the way? You still look a bit cold..."
    voice "audio/voice/E5/HAR/11/YK/YK001.ogg"
    yukino "Yes. I just went out for a bit, that's all."
    voice "audio/voice/E5/HAR/11/HA/HA002.ogg"
    hachiman "You'll catch a cold like that."
    show yukino vhappy with dissolve
    voice "audio/voice/E5/HAR/11/YK/YK002.ogg"
    yukino "I'm alright, really. Thanks... for staying with me at the ski resort."
    voice "audio/voice/E5/HAR/11/HA/HA003.ogg"
    hachiman "You don't need to thank me for something like that. Hell, you shouldn't be working youself into that state at all, you know?"
    voice "audio/voice/E5/HAR/11/YK/YK003.ogg"
    yukino "Yes, you're right. I'll be careful."
    show yukino sad with dissolve
    voice "audio/voice/E5/HAR/11/YK/YK004.ogg"
    yukino "So, um..."
    voice "audio/voice/E5/HAR/11/HA/HA004.ogg"
    hachiman "What is it?"
    show yukino angry with dissolve
    voice "audio/voice/E5/HAR/11/YK/YK005.ogg"
    yukino "If Nee-san's... really bothering you, you could just tell her off."
    voice "audio/voice/E5/HAR/11/HA/HA005.ogg"
    hachiman "W-what's this, all of a sudden?"
    voice "audio/voice/E5/HAR/11/YK/YK006.ogg"
    yukino "It's just, I've never seen her like that before. No one has been able to keep up with her antics before... including me."
    show yukino angry with dissolve
    voice "audio/voice/E5/HAR/11/YK/YK007.ogg"
    yukino "...So, I think she likes you."
    voice "audio/voice/E5/HAR/11/HA/HA006.ogg"
    hachiman "I don't like the sound of that."
    voice "audio/voice/E5/HAR/11/YK/YK008.ogg"
    yukino "I wonder about that. But, I'd be happy if you could still talk to me. That is... i-if you want to, of course."
    voice "audio/voice/E5/HAR/11/HA/HA007.ogg"
    hachiman "S-sure."
    show yukino pout with dissolve
    voice "audio/voice/E5/HAR/11/YK/YK009.ogg"
    yukino "T-that is all I wanted to say... I-I'm sorry."
    voice "audio/voice/E5/HAR/11/HA/HA008.ogg"
    hachiman "I-it's fine."
    hide yukino with dissolve
    hachiman "(I'd never have thought Yukinoshita would say something like that...)"
    window auto hide dissolve
    stop music fadeout 1.0
    call loading_screen(22) from _call_loading_screen_21
    jump E6_CMM_01
