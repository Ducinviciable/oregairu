label E5_IRO_01:
    scene lodgeroomA
    show kaori home mid vhappy at center:
        xoffset 5 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM44.ogg"
    window auto show dissolve
    voice "audio/voice/E5/IRO/01/OR/OR000.ogg"
    kaori "Hahaha, getting paired up with you to make the beds--that's hilarious!"
    voice "audio/voice/E5/IRO/01/HA/HA000.ogg"
    hachiman "It's really not that funny."
    hachiman "(Let's just get this over with quickly.)"
    window auto hide dissolve
    scene lodgeroomA at truecenter with dissolve:
        zoom 2.0 xalign 0 ypos 740
    play sound "audio/sfx/SE01/SE01_15.ogg"
    $renpy.pause(delay=1.0, hard=True)
    show kaori home near annoyed at left with dissolve:
        xoffset 175 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/IRO/01/OR/OR001.ogg"
    kaori "Woah, Hikigaya, you're a surprisingly hard worker."
    stop sound fadeout 0.5
    voice "audio/voice/E5/IRO/01/HA/HA001.ogg"
    hachiman "I'm practicing for when I become a corporate slave in the working world."
    show kaori vhappy with dissolve
    voice "audio/voice/E5/IRO/01/OR/OR002.ogg"
    kaori "Haha, if you say so."
    window auto hide dissolve
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE04/SE04_05.ogg"
    scene lodgeroomA with dissolve
    show iroha home mid_left vhappy at center with dissolve:
        xoffset -35 yoffset 65
    window auto show dissolve
    voice "audio/voice/E5/IRO/01/IR/IR000.ogg"
    iroha "How's the bed making coming along, you two?"
    voice "audio/voice/E5/IRO/01/HA/HA002.ogg"
    hachiman "Hey, what are you--"
    show iroha happy with dissolve
    voice "audio/voice/E5/IRO/01/IR/IR001.ogg"
    iroha "I'm going around checking on each team to make sure everything is going smoothly."
    hachiman "(That's a nice way of saying that she's not doing anything. I mean this girl is seriously just walking around while we do all the work.)"
    show iroha angry with dissolve
    voice "audio/voice/E5/IRO/01/IR/IR002.ogg"
    iroha "............"
    voice "audio/voice/E5/IRO/01/HA/HA003.ogg"
    hachiman "Is there a problem?"
    show iroha frown with dissolve
    voice "audio/voice/E5/IRO/01/IR/IR003.ogg"
    iroha "Please be more careful laying out the sheets, senpai."
    voice "audio/voice/E5/IRO/01/HA/HA004.ogg"
    hachiman "I am! See?"
    voice "audio/voice/E5/IRO/01/IR/IR004.ogg"
    iroha "Not at all. If the bedspread doesn't look pretty, the whole atmosphere of the place is ruined...so please do it right. Here, hand me that sheet."
    window auto hide dissolve
    stop voice
    image lodgeroomADup = "images/bg/BG59A.jpg"
    show lodgeroomADup at truecenter:
        zoom 2.0 xalign 0 ypos 740
    hide iroha
    with dissolve
    play sound "audio/sfx/SE01/SE01_15.ogg"
    $renpy.pause(delay=1.0, hard=True)
    show iroha home near_left happy at center with dissolve:
        xoffset 260 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/IRO/01/IR/IR005.ogg"
    iroha "See, it should look like this."
    hachiman "(Oh wow!! Not a single crease! Irohasu is a total pro!)"
    stop sound fadeout 0.5
    show iroha unimpressed with dissolve
    voice "audio/voice/E5/IRO/01/IR/IR006.ogg"
    iroha "Well, you do seem like the type of guy to either sleep all day or prowl around the house half-asleep... I get that you don't have experience with this sort of thing, but please try a little harder, alright?"
    show iroha vhappy with dissolve
    voice "audio/voice/E5/IRO/01/IR/IR007.ogg"
    iroha "After this is done it's time to head to the ski slopes, you know."
    hide iroha with dissolve
    play sound "<from 2.0>audio/sfx/SE00/SE00_30L.ogg"
    voice "audio/voice/E5/IRO/01/HA/HA005.ogg"
    hachiman "Got it. By the way, where did that impression of me come from...?"
    $renpy.pause(delay=0.5, hard=True)
    stop sound
    play sound "audio/sfx/SE04/SE04_06.ogg"
    hide lodgeroomADup with dissolve
    hachiman "(Well, she's not wrong about the beds. These neat ones really add a plesant feel to the room.)"
    hachiman "(Maybe I should try doing a nicer job on this one.)"
    show kaori home mid annoyed at center with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E5/IRO/01/OR/OR003.ogg"
    kaori "What's gotten into you, Hikigaya? Let's hurry up and finish this."
    voice "audio/voice/E5/IRO/01/HA/HA006.ogg"
    hachiman "............"
    hachiman "(I work quickly and diligently and they call me messy. I work carefully, and this is what I get. Man, I feel like a corporate slave already. This sucks.)"
    window auto hide dissolve
    stop music fadeout 0.5
    jump E5_G13_01
    
label E5_IRO_02:
    hachiman "(I'm having so much fun being forcibly dragged out here and being abandoned!) "
    "Now that it's come to this, maybe I don't even want someone to teach me how to ski. Ideally, I'd be playing in the snow with Komachi."
    hachiman "(At least she's having fun, since we came all the way out here. On second thought, it would be nice if someone came over here and taught me the basics of skiing.)"
    "Speaking of which, someone does come to mind, but there's someone she wants to ski with. I'd feeling like I'd be forcing her to help me."
    play sound "audio/sfx/SE01/SE01_46.ogg"
    hachiman "(Besides, even if I asked nicely, she'd turn me down with an excuse like \"Oh sorry, I can't; I've got a cold.\")"
    hachiman "(You know what, I'm gonna stop thinking about learning how to ski. Skiing is a sport for cool people, anyway.)"
    hachiman "(I've decided. As long as I'm enjoying this pure snow, I don't really care how I do it.) "
    stop sound
    hachiman "(Alright, I'm gonna make a snowman.)"
    window auto hide dissolve
    scene slopesA with dissolve:
        yoffset -2350 zoom 3.2 xcenter 0.23
    $renpy.pause(delay=1, hard=True)
    stop ambient
    play sound "audio/sfx/SE01/SE01_47.ogg"
    stop music fadeout 0.5
    show iroha heavy_coat near_left pout at center with dissolve:
        zoom 2.0 yoffset 160 xoffset 600
        easein 0.7 xoffset 40
    $renpy.pause(delay=1.0, hard=True)
    show iroha heavy_coat near_center happy at center with dissolve:
        zoom 2.0 yoffset 160 xoffset -30
    $renpy.pause(delay=1.0, hard=True)
    scene slopesA
    show iroha heavy_coat mid_center happy at center:
        xoffset -5 yoffset 75
    with dissolve
    play music "audio/bgm/BGM36.ogg"
    window auto show dissolve
    voice "audio/voice/E5/IRO/02/IR/IR000.ogg"
    iroha "Senpai, whatcha doin' squatting over here all by yourself?"
    hachiman "(Here comes one of those cool people.)"
    voice "audio/voice/E5/IRO/02/HA/HA000.ogg"
    hachiman "Can't you see? I'm playing in the snow."
    show iroha pout with dissolve
    voice "audio/voice/E5/IRO/02/IR/IR001.ogg"
    iroha "Ooh, lemme guess: is it 'cause you don't know how to ski?"
    voice "audio/voice/E5/IRO/02/HA/HA001.ogg"
    hachiman "Well, yeah. It doesn't really snow in Chiba"
    hide iroha
    $url = ["iroha heavy_coat mid_center pout", "iroha heavy_coat mid_center happy"]
    $multiImagePara = [-5, 75, 0, 0, 3.1]
    call multiImage() from _call_multiImage_51
    voice "audio/voice/E5/IRO/02/IR/IR002.ogg"
    iroha "There you go again. I guess it can't be helped; I'll give you a special skiing lesson!"
    call finishmultiImage from _call_finishmultiImage_52
    show iroha heavy_coat mid_center happy at center:
        xoffset -5 yoffset 75
    voice "audio/voice/E5/IRO/02/HA/HA002.ogg"
    hachiman "Nah, I'll pass. I'm having fun doing my own thing. "
    voice "audio/voice/E5/IRO/02/HA/HA003.ogg"
    hachiman "Hey, you listening?"
    show iroha mid_left with dissolve:
        xoffset -5 yoffset 65
    voice "audio/voice/E5/IRO/02/IR/IR003.ogg"
    iroha "Okay, so watch me and copy what I do, alright?"
    hide iroha with dissolve
    play sound "audio/sfx/SE01/SE01_45.ogg"
    hachiman "(Looks like Iroha's ski class has already begun.)"
    hachiman "(I'd run, but there's nowhere to hide in this wide open snow field.)"
    hachiman "(Well, I suppose I've got nothing better to do anyway. Could be a good way to kill some time.)"
    window auto hide dissolve
    scene slopesA with Fade(0.5,1.5,0.5):
        zoom 1.75 xoffset -300 yoffset -375
    play ambient "audio/sfx/SE01/SE01_42L.ogg"
    $renpy.pause(delay=2.0, hard=True)
    window auto show dissolve
    voice "audio/voice/E5/IRO/02/IR/IR004.ogg"
    iroha "Lookin' good, senpai! Now lean your weight toward to upper part of the slope..."
    voice "audio/voice/E5/IRO/02/HA/HA004.ogg"
    hachiman "Woah, woah, woah!"
    voice "audio/voice/E5/IRO/02/IR/IR005.ogg"
    iroha "Okay, now slow down. Turn your feet inward like the shape of pizza slice!"
    hachiman "(C'mon, Hachiman, focus. Pizza slice, pizza slice, pizza slice...)"
    window auto hide dissolve
    stop ambient fadeout 0.5
    scene black
    show slopesA at screenShake1:
        zoom 1.5 xpos -950 ypos -535
    with dissolve
    $renpy.pause(delay=0.6, hard=True)
    show slopesA:
        zoom 1.5 xpos -950 ypos -535
    play sound "audio/sfx/SE01/SE01_48.ogg"
    $renpy.pause(delay=2.0, hard=True)
    window auto show dissolve
    voice "audio/voice/E5/IRO/02/HA/HA005.ogg"
    hachiman "Oh, hey...I kinda managed to stop."
    show iroha heavy_coat near_center vhappy at center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E5/IRO/02/IR/IR006.ogg"
    iroha "Wow, that was amazing, senpai!"
    window auto hide dissolve
    show slopesA at screenShake2
    show iroha at center, Shake(None, 0.25, dist=60)
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE01/SE01_12.ogg"
    $renpy.pause(delay=1.0, hard=True)
    scene slopesA:
        zoom 1.5 xpos -950 ypos -535
    show iroha heavy_coat near_center vhappy at center:
        xoffset -15 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/IRO/02/HA/HA006.ogg"
    hachiman "Hey--if you grab my arm, I'll lose my balance!"
    show iroha happy with dissolve
    voice "audio/voice/E5/IRO/02/IR/IR007.ogg"
    iroha "Don't worry, senpai! I'm holding on tight so you won't fall."
    hachiman "(Holding on tight, huh. That actually kinda feels good. Maybe it's best not to move.)"
    voice "audio/voice/E5/IRO/02/IR/IR008.ogg"
    iroha "You know, senpai, you're surprisingly decent at this! If you work at it, you might be able to go to the higher slopes!"
    voice "audio/voice/E5/IRO/02/HA/HA007.ogg"
    hachiman "You think so? Speaking of which, you're actually a pretty good teacher. "
    show iroha vhappy with dissolve
    voice "audio/voice/E5/IRO/02/IR/IR009.ogg"
    iroha "Heehee. Has your opinion of me improved a little?"
    voice "audio/voice/E5/IRO/02/HA/HA008.ogg"
    hachiman "Well, in terms of being a ski instructor at least."
    voice "audio/voice/E5/IRO/02/HA/HA009.ogg"
    hachiman "Ah, wait a minute, what about Hayama? I mean, I'm super grateful that you're teaching me, but..."
    show iroha near_left unimpressed with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E5/IRO/02/IR/IR010.ogg"
    iroha "Well, Hayama-senpai is..."
    window auto hide dissolve
    $renpy.pause(delay=0.5, hard=True)
    scene slopesA at right:
        zoom 1.5 xoffset 0 yoffset 100
    show hayama heavy_coat mid_center happy at center:
        xoffset -25 yoffset 75
    with dissolve
    $renpy.pause(delay=0.5, hard=True)
    show yumiko heavy_coat mid_left blush at right behind hayama with dissolve:
        xoffset -130 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/IRO/02/YM/YM000.ogg"
    yumiko "Hayatooo, ride the lift with meeee! I'm afraid of heights..."
    show kaori heavy_coat mid vhappy at left behind hayama with dissolve:
        xoffset 65 yoffset 75
    voice "audio/voice/E5/IRO/02/OR/OR000.ogg"
    kaori "Hayama-kun~! Teach me how to ski!"
    hide yumiko
    hide kaori
    with dissolve
    $renpy.pause(delay=0.5, hard=True)
    show tobe heavy_coat mid vhappy at right behind hayama with dissolve:
        xoffset 75 yoffset 75 
    voice "audio/voice/E5/IRO/02/TB/TB000.ogg"
    tobe "Hayato-kun! Let's go snowboarding!"
    show ebina heavy_coat mid_left vhappy at left behind hayama with dissolve:
        xoffset -75 yoffset 70
    voice "audio/voice/E5/IRO/02/EB/EB000.ogg"
    ebina "Ooh, that's good! Keep it coming! The camraderie of boys on the snowscape is divine~"
    hide tobe
    hide ebina
    with dissolve
    show hayama vhappy with dissolve
    voice "audio/voice/E5/IRO/02/HY/HY000.ogg"
    hayama "Alright, everyone. How about we all go over to the intermediate course area?"
    hachiman "(Wow, Hayama's popular. Looks like some winter magic has increased his popularity by 20\%.)"
    window auto hide dissolve
    scene slopesA:
        zoom 1.5 xpos -950 ypos -535
    show iroha heavy_coat near_left unimpressed at center:
        xoffset 20 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/IRO/02/IR/IR011.ogg"
    iroha "It's been like that all morning."
    voice "audio/voice/E5/IRO/02/HA/HA010.ogg"
    hachiman "Then shouldn't you be over there too?"
    show iroha pout with dissolve
    voice "audio/voice/E5/IRO/02/IR/IR012.ogg"
    iroha "I don't wanna become another one of his followers."
    show iroha near_center happy with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E5/IRO/02/IR/IR013.ogg"
    iroha "Besides, don't you think he'll find it attractive when he sees how patient I am teaching a beginner how to ski?"
    hachiman "(Damn, Irohasu is a sly one... well, I did get the feeling I was being used, anyway.)"
    hachiman "(Well, even if she did it to impress him, I did get a bit more competent at skiing, and it felt good to hear Irohasu tell me she'd support me so I wouldn't fall. All hail Hayama!)"
    show iroha vhappy with dissolve
    voice "audio/voice/E5/IRO/02/IR/IR014.ogg"
    iroha "Hey, senpai. We're staying in an open-air bath, right? Dipping into that relaxing hot water after all this skiing is the best feeling in the world!"
    voice "audio/voice/E5/IRO/02/HA/HA011.ogg"
    hachiman "Yeah, it'd be nice to refresh my mind with some peace and quiet too."
    show iroha blush with dissolve
    voice "audio/voice/E5/IRO/02/IR/IR015.ogg"
    iroha "Hey... we came all the way out here...do you wanna go in together?"
    voice "audio/voice/E5/IRO/02/HA/HA012.ogg"
    hachiman "What are you on all of a sudden? You know that there's a separate bath for the boys and girls."
    show iroha frown with dissolve
    voice "audio/voice/E5/IRO/02/IR/IR016.ogg"
    iroha "Seriously? What a lame response. C'mon, even if you're joking I expect a better reaction than that..."
    voice "audio/voice/E5/IRO/02/HA/HA013.ogg"
    hachiman "The hell were you expecting?"
    show iroha angry with dissolve
    voice "audio/voice/E5/IRO/02/IR/IR017.ogg"
    iroha "Hmm...let's see...how about whispering \"Yeah, let's go in together and keep it a secret from everyone~\" in my ear gently or something like that."
    voice "audio/voice/E5/IRO/02/HA/HA014.ogg"
    hachiman "That was an unexpectedly girly answer, coming from you."
    show iroha unimpressed with dissolve
    voice "audio/voice/E5/IRO/02/IR/IR018.ogg"
    iroha "Well, now that I picture it, that doesn't suit you at all. To the point where it's extremely concerning. If it wasn't me, this could have been really bad, you know."
    voice "audio/voice/E5/IRO/02/HA/HA015.ogg"
    hachiman "I suppose. Wait a minute, I didn't do anything wrong. I'm being framed. Please entertain your delusions with Hayama instead."
    show iroha vhappy with dissolve
    voice "audio/voice/E5/IRO/02/IR/IR019.ogg"
    iroha "Heehee! Okay, I'll do that! And in the meanwhile I'll think of a line that'll fit you better, senpai!"
    voice "audio/voice/E5/IRO/02/HA/HA016.ogg"
    hachiman "Yeah, I'll be expecting something clever that sounds like I'd actually say it. "
    show iroha blush with dissolve
    "It was nothing more than idle conversation, but I could see a faint rosy tint on Isshiki's cheeks as she pleasantly spoke. "
    "Her smile was dazzling like the bright snow as the sun's brilliant rays beamed down over the shining snowscape."
    window auto hide dissolve
    stop music fadeout 0.5
    jump E5_CMM_03

label E5_IRO_03:
    scene lodge2A with Fade(1.0, 0.5, 1.0)
    play sound "audio/sfx/SE00/SE00_30L.ogg"
    window auto show dissolve
    "Humming to myself, I approached the bathhouse hall."
    "As I got closer, I saw what appeared to be the figure of a girl aimlessly wandering about."
    stop sound 
    show iroha home near_left frown at center with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E5/IRO/03/IR/IR000.ogg"
    iroha "Senpai, you're late!"
    play music "audio/bgm/BGM36.ogg"
    show iroha near_center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E5/IRO/03/IR/IR001.ogg"
    iroha "It's been so long that I thought you might've already gotten out of the bath!"
    voice "audio/voice/E5/IRO/03/HA/HA000.ogg"
    hachiman "Huh? Oh. I waited until the time where no one else would be around. Anyway, what do you want?"
    show iroha near_left vhappy with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E5/IRO/03/IR/IR002.ogg"
    iroha "Let's go in together~!"
    voice "audio/voice/E5/IRO/03/HA/HA001.ogg"
    hachiman "W-what?"
    show iroha unimpressed with dissolve
    voice "audio/voice/E5/IRO/03/IR/IR003.ogg"
    iroha "Did you really forget? We made a promise in the afternoon, didn't we?"
    voice "audio/voice/E5/IRO/03/HA/HA002.ogg"
    hachiman "Making a joke like that at a time like this really isn't very funny, you know."
    show iroha near_center blush with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E5/IRO/03/IR/IR004.ogg"
    iroha "Well, it's not like I'm joking, though."
    voice "audio/voice/E5/IRO/03/HA/HA003.ogg"
    hachiman "Uh..."
    show iroha vhappy with dissolve
    voice "audio/voice/E5/IRO/03/IR/IR005.ogg"
    iroha "Besides, the baths are separated by gender anyway; we're just going into our sections at the same time!"
    voice "audio/voice/E5/IRO/03/HA/HA004.ogg"
    hachiman "Oh. Right, of course."
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    scene skyC with Fade(1.0, 0.5, 1.0)
    play sound "audio/sfx/SE01/SE01_33.ogg"
    $renpy.pause(delay=1.0, hard=True)
    stop sound
    window auto show dissolve
    voice "audio/voice/E5/IRO/03/HA/HA005.ogg"
    hachiman "Ahh...I'm in heaven."
    voice "audio/voice/E5/IRO/03/HA/HA006.ogg"
    hachiman "Open air baths really are the best, huh... I want one back home. It would totally fit, but then all the neighbors could see. Maybe I'll make one inside the house... ah, but then it wouldn't be an open air bath."
    "As I ramble on about how wonderful this bath feels, I hear a voice from the other side of the fence."
    window auto hide dissolve
    scene irohaHotspring with dissolve
    play music "audio/bgm/BGM42.ogg"
    window auto show dissolve
    voice "audio/voice/E5/IRO/03/IR/IR006.ogg"
    menu E5_IRO_03_menu:
        with dissolve
        iroha "Senpaaii!! This bath feels nice, doesn't it?"
        "This really brings you back to life.": 
            voice "audio/voice/E5/IRO/03/HA/HA007.ogg"
            hachiman "Aah, this really brings you back to life."
            voice "audio/voice/E5/IRO/03/IR/IR007.ogg"
            iroha "Hearing that from you makes it all the more convincing, senpai."
            voice "audio/voice/E5/IRO/03/HA/HA008.ogg"
            hachiman "I feel like you're implying something about me..."
            voice "audio/voice/E5/IRO/03/IR/IR008.ogg"
            iroha "But you're right. It feels like I'm defrosting in real time..."
            voice "audio/voice/E5/IRO/03/IR/IR009.ogg"
            iroha "It's rather soothing~"
        "Oh!":
            voice "audio/voice/E5/IRO/03/HA/HA009.ogg"
            hachiman "Uh..yeah, it does."
            voice "audio/voice/E5/IRO/03/IR/IR010.ogg"
            iroha "This hot water also makes our skin all sleek and smooth, too~"
            voice "audio/voice/E5/IRO/03/IR/IR011.ogg"
            iroha "Wow, senpai! My arm is super smooth...doesn't that make you wanna come touch it?"
            voice "audio/voice/E5/IRO/03/HA/HA010.ogg"
            hachiman "I'm good. I can just touch my own arm, thanks. "
            voice "audio/voice/E5/IRO/03/IR/IR012.ogg"
            iroha "I see...what a shame~"
        "...":
            "not done"
            jump E5_IRO_03_menu

    voice "audio/voice/E5/IRO/03/IR/IR016.ogg"
    iroha "It feels really good though, doesn't it?"
    window auto hide dissolve
    stop voice
    scene hachimanBathc with dissolve:
        zoom 1.7 xoffset -17 yoffset -312
    window auto show dissolve
    hachiman "(This is bad. Every time I hear the water splashing, my mind is filled with some unsavory thoughts...)"
    hachiman "(On the other side of this thin fence, Isshiki is naked...)"
    voice "audio/voice/E5/IRO/03/IR/IR017.ogg"
    iroha "Plus, talking like this makes it really seem like we're in the bath together, huh~"
    voice "audio/voice/E5/IRO/03/HA/HA013.ogg"
    hachiman "There you go again, saying things like that..."
    window auto hide dissolve
    stop voice
    scene irohaHotspring with dissolve
    window auto show dissolve
    voice "audio/voice/E5/IRO/03/IR/IR018.ogg"
    iroha "C'mon, it's fine...it's just you, senpai."
    hachiman "(Actually, that's the very reason why it's not fine..)"
    voice "audio/voice/E5/IRO/03/IR/IR019.ogg"
    iroha "Besides..."
    voice "audio/voice/E5/IRO/03/IR/IR020.ogg"
    iroha "Senpai, you're becoming more aware of my existence. That might make me a little happy."
    window auto hide dissolve
    stop voice
    scene hachimanBathc with dissolve:
        zoom 1.7 xoffset -17 yoffset -312
    window auto show dissolve
    voice "audio/voice/E5/IRO/03/HA/HA014.ogg"
    hachiman "............"
    voice "audio/voice/E5/IRO/03/IR/IR021.ogg"
    iroha "Senpai, you listening?"
    voice "audio/voice/E5/IRO/03/HA/HA015.ogg"
    hachiman "Yep, I'm listening."
    window auto hide dissolve
    stop voice
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE01/SE01_33.ogg"
    scene skyC with Dissolve(2.0)
    window auto show dissolve
    "While trying to fall asleep, I suddenly opened my eyes to the breathtaking winter night sky filled 
    with dazzling stars. "
    hachiman "(How beautiful.)" 
    window auto hide dissolve
    stop music fadeout 0.5
    jump E5_CMM_04

label E5_IRO_04:
    show hayama coat mid_center happy at left:
        xoffset 165 yoffset 75
    show yumiko home mid_center happy at right:
        xoffset -130 yoffset 75
    with dissolve
    voice "audio/voice/E5/IRO/04/YM/YM000.ogg"
    yumiko "It's the second day after all. Why don't we just hurry and get this over with?"
    voice "audio/voice/E5/IRO/04/HY/HY000.ogg"
    hayama "Good idea. Why don't we break into groups and then make any necessary changes after?"
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    scene lodgeA
    show hayama coat mid_center happy at center:
        xoffset 5 yoffset 75
    show iroha home mid_center vhappy at left behind hayama:
        xoffset 175 yoffset 75
    show yumiko home mid_center frown at right behind hayama:
        xoffset -5 yoffset 75
    with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/BGM44.ogg"
    window auto show dissolve
    voice "audio/voice/E5/IRO/04/HY/HY001.ogg"
    hayama "Alright, so for my group, it'll be me, Yumiko, Iroha, and Hikigaya."
    voice "audio/voice/E5/IRO/04/YM/YM001.ogg"
    yumiko "Why'd you have to include Hikio...?"
    voice "audio/voice/E5/IRO/04/IR/IR000.ogg"
    iroha "Lucky you, huh, senpai? Thanks to Hayama-senpai, you didn't end up getting left out alone!"
    hachiman "(There she goes again...if this is my group, it'd be a lot easier being alone, anyway.)"
    show hayama pout with dissolve
    voice "audio/voice/E5/IRO/04/HY/HY002.ogg"
    hayama "Alright, how should we split up the work? We're assigned cleaning of the open-air bath and the living room." 
    show yumiko vhappy with dissolve
    voice "audio/voice/E5/IRO/04/YM/YM002.ogg"
    yumiko "Hayato, which one are you doing?"
    voice "audio/voice/E5/IRO/04/IR/IR001.ogg"
    iroha "Which one are you going to do, Hayama-senpai?"
    show iroha frown
    show yumiko frown
    with dissolve
    voice "audio/voice/E5/IRO/04/YM/YM003.ogg"
    yumiko "............"
    voice "audio/voice/E5/IRO/04/IR/IR002.ogg"
    iroha "............"
    show hayama relieved with dissolve
    hachiman "(Scary! Scaaaary! Sparks are gonna start flying soon.)"
    hachiman "(Well, I've got no choice. I guess I should do something to prevent some serious conflict between those two.)"
    voice "audio/voice/E5/IRO/04/HA/HA000.ogg"
    hachiman "Alright, the boys will take the open-air bath. Let's go, Hayama."
    show hayama vhappy with dissolve
    voice "audio/voice/E5/IRO/04/HY/HY003.ogg"
    hayama "Ah, sure. "
    show yumiko annoyed
    show iroha annoyed
    with dissolve
    voice "audio/voice/E5/IRO/04/YM/YM004.ogg"
    yumiko "Hah? Hikio, wait a minute!"
    voice "audio/voice/E5/IRO/04/IR/IR003.ogg"
    iroha "Hey! Don't just make the decisions for the group like that, senpai!"
    voice "audio/voice/E5/IRO/04/EB/EB000.ogg"
    hide iroha
    hide hayama
    hide yumiko
    with dissolve
    show ebina home mid_left vhappy at right with dissolve:
        xoffset -5 yoffset 70
    ebina "Way to go, Hikitani-kun! To think you'd just jump between them and snatch Hayato away..."
    hachiman "(Ah, shoot, I've attracted some disastrous attention. Better get out of here quick...)"
    window auto hide dissolve
    stop music fadeout 1.0
    scene black with Fade(0.5, 0, 0)
    play sound "audio/sfx/SE04/SE04_08.ogg"
    show hotspringBGA
    show hayama coat mid_center happy at center:
        xoffset 5 yoffset 75
    with Fade(0, 1.5, 1.0)
    play music "audio/bgm/BGM37.ogg"
    stop sound
    window auto show dissolve
    voice "audio/voice/E5/IRO/04/HA/HA001.ogg"
    hachiman "Anyway, to put it simply, I just gotta brush it like this, right?"
    voice "audio/voice/E5/IRO/04/HY/HY004.ogg"
    hayama "Yeah, I think that'll work."
    window auto hide dissolve
    stop voice
    hide hayama with dissolve
    play ambient "audio/sfx/SE01/SE01_23L.ogg"
    $renpy.pause(delay=0.5, hard =True)
    show hayama coat far_center happy at right with dissolve:
        xoffset -290 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/IRO/04/HY/HY005.ogg"
    hayama "That was...a little unexpected."
    voice "audio/voice/E5/IRO/04/HA/HA002.ogg"
    hachiman "Hm? What are you talking about?"
    voice "audio/voice/E5/IRO/04/HY/HY006.ogg"
    hayama "You picking me as your partner..."
    voice "audio/voice/E5/IRO/04/HA/HA003.ogg"
    hachiman "Hah?"
    hachiman "(WHAAAAT!? What is Hayama saying?! If it's with me, it's okay to cross that line!? That's a bit of a problem...! No, that's a HUGE problem!)"
    voice "audio/voice/E5/IRO/04/HA/HA004.ogg"
    hachiman "You should be able to understand. I didn't pick you because I like you."
    show hayama vhappy with dissolve
    voice "audio/voice/E5/IRO/04/HY/HY007.ogg"
    hayama "Yeah, you really saved me back there."
    window auto hide dissolve
    stop voice
    hide hayama with dissolve
    $renpy.pause(delay=0.5, hard =True)
    show hayama coat far_right happy at left with dissolve:
        xoffset 290 yoffset 65
    window auto show dissolve
    voice "audio/voice/E5/IRO/04/HY/HY008.ogg"
    hayama "Seems like Iroha's changed a bit these days."
    voice "audio/voice/E5/IRO/04/HA/HA005.ogg"
    hachiman "Why is this conversation suddenly about Iroha?"
    voice "audio/voice/E5/IRO/04/HY/HY009.ogg"
    hayama "Just a thought."
    voice "audio/voice/E5/IRO/04/HA/HA006.ogg"
    hachiman "I see."
    show hayama vhappy with dissolve
    voice "audio/voice/E5/IRO/04/HY/HY010.ogg"
    hayama "Yeah."
    voice "audio/voice/E5/IRO/04/HA/HA007.ogg"
    hachiman "............"
    show hayama happy with dissolve
    voice "audio/voice/E5/IRO/04/HY/HY011.ogg"
    hayama "............"
    window auto hide dissolve
    stop voice
    hide hayama with dissolve
    $renpy.pause(delay=0.5, hard =True)
    window auto show dissolve
    voice "audio/voice/E5/IRO/04/HA/HA008.ogg"
    hachiman "She just doesn't show you that side of her, you know. That girl has been like that from the beginning."
    show hayama coat far_center happy at center with dissolve:
        xoffset -10 yoffset 75
    voice "audio/voice/E5/IRO/04/HY/HY012.ogg"
    hayama "That's true. But she's definitely changed. In a more fundamental way."
    voice "audio/voice/E5/IRO/04/HA/HA009.ogg"
    hachiman "............"
    voice "audio/voice/E5/IRO/04/HA/HA010.ogg"
    hachiman "You're free to think as you wish, but don't push those ideas on her. Speaking of push, get those hands moving; we can't finish our work if you don't help out."
    show hayama coat far_right happy at center with dissolve:
        xoffset 10 yoffset 65
    voice "audio/voice/E5/IRO/04/HY/HY013.ogg"
    hayama "You're right. Let's hurry and finish."
    voice "audio/voice/E5/IRO/04/HA/HA011.ogg"
    hachiman "Uh-huh, let's do that."
    voice "audio/voice/E5/IRO/04/HY/HY014.ogg"
    hayama "............"
    voice "audio/voice/E5/IRO/04/HA/HA012.ogg"
    hachiman "............"
    window auto hide dissolve
    stop voice
    stop ambient fadeout 0.5
    stop music fadeout 0.5
    
    image iroha_lodge_pov = Flatten("iroha home mid_center vhappy")

    scene lodge_EC with Dissolve(1.0)
    $renpy.pause(delay=1.0, hard=True)
    show iroha_lodge_pov at center:
        xoffset -250 yoffset 75 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.6 xoffset -370
            easeout 1.0 xoffset -250
    $renpy.pause(delay=3.0, hard=True)
    jump E5_IRO_05
    

label E5_IRO_05:
    scene lodgeA
    show yumiko home mid_center frown at center:
        xoffset -5 yoffset 75
    with dissolve
    play music "audio/bgm/BGM36.ogg"
    window auto show dissolve
    voice "audio/voice/E5/IRO/05/IR/IR000.ogg"
    iroha "They really went to go clean together, huh..."
    voice "audio/voice/E5/IRO/05/YM/YM000.ogg"
    yumiko "That Hikio...who does he think he is?"
    show ebina home mid_center relieved at right behind yumiko with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E5/IRO/05/EB/EB000.ogg"
    ebina "Oh Yumiko...deep down I think you know. Heehee, heehee!"
    show yumiko unimpressed with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM001.ogg"
    yumiko "Ebina, your nose is bleeding again... besides, this isn't even your group. Hold your nose and go away already."
    hide ebina with dissolve
    voice "audio/voice/E5/IRO/05/IR/IR001.ogg"
    iroha "I guess we should start too. Our cleaning work, I mean."
    voice "audio/voice/E5/IRO/05/YM/YM002.ogg"
    yumiko "I was gonna start even without you saying anything."
    window auto hide dissolve
    stop voice
    scene black with Fade(0.5, 0, 0)
    play sound "audio/sfx/SE01/SE01_26.ogg"
    scene lodgeA with Fade(0, 1.0, 1.0)
    stop sound
    show yumiko home mid_center sad at center with dissolve:
        xoffset -5 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/IRO/05/YM/YM003.ogg"
    yumiko "Haa, this is so boring."
    voice "audio/voice/E5/IRO/05/IR/IR002.ogg"
    iroha "Happiness escapes from your body when you sigh, you know~"
    show yumiko unimpressed with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM004.ogg"
    yumiko "I don't remember asking for a response to every little thing I do."
    show yumiko angry with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM005.ogg"
    yumiko "Anyway, you and Hikio were getting along last night, weren't you? Wouldn't it have been better if you two got paired up instead?"
    voice "audio/voice/E5/IRO/05/IR/IR003.ogg"
    iroha "You're right, huh."
    voice "audio/voice/E5/IRO/05/IR/IR004.ogg"
    iroha "But, I think senpai was being considerate and trying to prevent a fight between us, Miura-senpai."
    show yumiko happy with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM006.ogg"
    yumiko "Well, Hikio is the type to weirdly try and read too much into things, after all. I believe it."
    show yumiko unimpressed with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM007.ogg"
    yumiko "I don't need his concern. I just wanted to spend some time with Hayato out here, but it seems that's too much to ask."
    voice "audio/voice/E5/IRO/05/IR/IR005.ogg"
    iroha "Hayama-senpai belongs to everyone, after all~"
    show yumiko angry with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM008.ogg"
    yumiko "............"
    stop music
    voice "audio/voice/E5/IRO/05/IR/IR006.ogg"
    iroha "But, I..."
    play music "audio/bgm/BGM18.ogg"
    voice "audio/voice/E5/IRO/05/IR/IR007.ogg"
    iroha "I'm rooting for you, Miura-senpai."
    show yumiko surprised with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM009.ogg"
    yumiko "What!?"
    show yumiko frown with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM010.ogg"
    yumiko "What's this, all of a sudden..."
    voice "audio/voice/E5/IRO/05/IR/IR008.ogg"
    iroha "Hey, please don't get so defensive!"
    voice "audio/voice/E5/IRO/05/IR/IR009.ogg"
    iroha "That's how I really feel. I just thought I'd let you know, Miura-senpai."
    show yumiko happy with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM011.ogg"
    yumiko "............"
    show yumiko pout with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM012.ogg"
    yumiko "So what's going on?"
    voice "audio/voice/E5/IRO/05/IR/IR010.ogg"
    iroha "............"
    voice "audio/voice/E5/IRO/05/IR/IR011.ogg"
    iroha "Well... let's just say I realized a few things."
    voice "audio/voice/E5/IRO/05/IR/IR012.ogg"
    iroha "Something I can call \"real\"...my feelings, stuff like that..."
    show yumiko angry with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM013.ogg"
    yumiko "..............."
    voice "audio/voice/E5/IRO/05/IR/IR013.ogg"
    iroha "Besides, it's a believable story that I chose to give up on Hayama-senpai with a rival like you around, Miura-senpai. People will feel some sympathy for me, too."
    show yumiko happy with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM014.ogg"
    yumiko "I suppose."
    show yumiko vhappy with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM015.ogg"
    yumiko "Well, if you're satisfied with it, it seems like everything worked out?"
    voice "audio/voice/E5/IRO/05/IR/IR014.ogg"
    iroha "Yep."
    voice "audio/voice/E5/IRO/05/IR/IR015.ogg"
    iroha "So do your best, Miura-senpai!"
    show yumiko blush with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM016.ogg"
    yumiko "O-of course! I was before you said anything, anyway."
    voice "audio/voice/E5/IRO/05/IR/IR016.ogg"
    iroha "It's a special occasion, boarding together in this ski lodge, after all."
    show yumiko unimpressed with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM017.ogg"
    yumiko "It really is. Well, it all ends tomorrow, though..."
    show yumiko happy with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM018.ogg"
    yumiko "Wait a minute, isn't this the first time the two of us have had a serious conversation?"
    voice "audio/voice/E5/IRO/05/IR/IR017.ogg"
    iroha "Now that you mention it, I think it is!"
    show yumiko vhappy with dissolve
    voice "audio/voice/E5/IRO/05/YM/YM019.ogg"
    yumiko "Well, it's not half-bad, having conversations like these with you."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    $renpy.pause(delay=0.5, hard=True)
    image iroha_pov_end = Flatten("iroha home mid_left happy")
    scene loading_wlogo
    show iroha_pov_end at center:
        xoffset -280 yoffset 65 alpha 1.0
        on hide:
            parallel:
                1.3
                linear 0.3 alpha 0
            parallel:
                easein 0.6 xoffset -220
                easeout 1.0 xoffset -400
    with Dissolve(1.0)
    $renpy.pause(delay=2.0, hard=True)
    hide iroha_pov_end
    $renpy.pause(delay=3.0, hard=True)
    jump E5_CMM_05

label E5_IRO_06:
    scene slopesA at right:
        zoom 1.75 xoffset 135 yoffset 175
    show hayama heavy_coat mid_right happy at left:
        xoffset 130 yoffset 65
    show iroha heavy_coat mid_left vhappy behind hayama at right:
        xoffset -255 yoffset 65
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/IRO/06/IR/IR000.ogg"
    iroha "Hayama-senpai! You wanna come to the area with the advanced courses with me?"
    show yumiko heavy_coat mid_center frown behind iroha at center:
        xoffset -5 yoffset 75 alpha 0
        parallel:
            linear 0.25 alpha 1.0
    show hayama heavy_coat mid_right happy at left:
        parallel:
            easeout 0.5 xoffset 5
    show iroha heavy_coat mid_left vhappy at right:
        parallel:
            easeout 0.5 xoffset -130
    $renpy.pause(delay=0.25, hard=True)
    hide yumiko
    show yumiko heavy_coat mid_center frown behind iroha at center:
        xoffset -5 yoffset 75
    voice "audio/voice/E5/IRO/06/YM/YM000.ogg"
    yumiko "Hayato already promised to ski with me though?"
    show hayama vhappy with dissolve
    voice "audio/voice/E5/IRO/06/HY/HY000.ogg"
    hayama "How about we all go over there together?"
    show yumiko surprised with dissolve
    voice "audio/voice/E5/IRO/06/YM/YM001.ogg"
    yumiko "What? But you said you were gonna teach me how to long turn!"
    voice "audio/voice/E5/IRO/06/HY/HY001.ogg"
    hayama "Yeah, but it'll be more fun if we're all doing it together."
    show iroha happy with dissolve
    voice "audio/voice/E5/IRO/06/IR/IR001.ogg"
    iroha "That's fine by me. That's okay with you too, right, Miura-senpai?"
    show yumiko pout with dissolve
    voice "audio/voice/E5/IRO/06/YM/YM002.ogg"
    yumiko "Tch..!"
    show yumiko annoyed with dissolve
    $renpy.pause(delay=0.25, hard=True)
    show yumiko:
        parallel:
            easein 0.75 xoffset 205
    show iroha:
        parallel:
            easein 0.75 xoffset -255
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E5/IRO/06/YM/YM003.ogg"
    yumiko "You little...what happened to what you said earlier!?"
    show yumiko:
        xoffset 205
    show iroha vhappy with dissolve:
        xoffset -255
    voice "audio/voice/E5/IRO/06/IR/IR002.ogg"
    iroha "I'm doing this BECAUSE of what I said earlier. Think of it as a little change of methods, hehe."
    show yumiko pout with dissolve
    voice "audio/voice/E5/IRO/06/YM/YM004.ogg"
    yumiko "Huh?"
    window auto hide dissolve
    stop voice
    $renpy.pause(delay=0.5, hard=True)
    scene slopesA
    show yukino heavy_coat mid_center unimpressed at left:
        xoffset 25 yoffset 75
    show yui heavy_coat mid_center pout at right:
        xoffset -245 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/IRO/06/YI/YI000.ogg"
    yui "H-hey, it looks like those two are fighting again..."
    voice "audio/voice/E5/IRO/06/YK/YK000.ogg"
    yukino "Ignore them. Hayama-kun is with them, and I'm sure he'll handle it."
    voice "audio/voice/E5/IRO/06/HA/HA000.ogg"
    hachiman "Well, he's also the reason they're fighting, but yeah."
    hachiman "(Well, it seems like Isshiki is fitting right in perfectly over there.)"
    show yui happy with dissolve
    voice "audio/voice/E5/IRO/06/YI/YI001.ogg"
    yui "Y-yeah, you're right. It's probably best to not get involved. It's been a while for us Service Club members to be together like this anyway."
    show yukino happy with dissolve
    voice "audio/voice/E5/IRO/06/YK/YK001.ogg"
    yukino "True. Not since yesterday, when you were doing something absurdly--"
    show yui mid_left surprised with dissolve:
        xoffset -270
    voice "audio/voice/E5/IRO/06/YI/YI002.ogg"
    yui "Woah, stop right there!"
    show yukino surprised with dissolve
    voice "audio/voice/E5/IRO/06/HA/HA001.ogg"
    hachiman "Hm? Did something happen the other day?"
    show yui mid_center pout with dissolve:
        xoffset -245
    voice "audio/voice/E5/IRO/06/YI/YI003.ogg"
    yui "N-n-no! N-nothing at all! Just the usual things that happen at the ski slopes!"
    show yukino pout with dissolve
    play sound "audio/sfx/SE01/SE01_46.ogg"
    voice "audio/voice/E5/IRO/06/YK/YK002.ogg"
    yukino "Is that so? For me, at least, that was the first time seeing such a sight..."
    stop sound
    voice "audio/voice/E5/IRO/06/HA/HA002.ogg"
    hachiman "Details, please. About that part in particular."
    show yui annoyed with dissolve
    voice "audio/voice/E5/IRO/06/YI/YI004.ogg"
    yui "Don't listen to her, Hikki! That's mean!"
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    scene slopesA at right with dissolve:
        zoom 1.5 xoffset 0 yoffset 100
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE01/SE01_47.ogg"
    show iroha heavy_coat mid_left vhappy at center with dissolve:
        xoffset -5 yoffset 65
    stop sound fadeout 0.5
    play music "audio/bgm/BGM36.ogg"
    window auto show dissolve
    voice "audio/voice/E5/IRO/06/IR/IR003.ogg"
    iroha "Senpaaai! I foooound you!"
    voice "audio/voice/E5/IRO/06/HA/HA003.ogg"
    hachiman "What?"
    voice "audio/voice/E5/IRO/06/HA/HA004.ogg"
    hachiman "Weren't you skiing with Hayama and the others?"
    "As I ask, I spot Hayama and Miura getting onto a lift together."
    show iroha mid_center happy with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E5/IRO/06/IR/IR004.ogg"
    iroha "Yep. But then, I saw you and came over here. Is it okay if I join you guys?"
    voice "audio/voice/E5/IRO/06/HA/HA005.ogg"
    hachiman "I don't mind. But why?"
    show iroha frown with dissolve
    voice "audio/voice/E5/IRO/06/IR/IR005.ogg"
    iroha "What do you mean \"why?\" You should be more welcoming, you know."
    voice "audio/voice/E5/IRO/06/YK/YK003.ogg"
    yukino "Isshiki-san? Isn't it a bit cruel to ask someone who's never received a warm welcome to be welcoming?" 
    voice "audio/voice/E5/IRO/06/HA/HA006.ogg"
    hachiman "You're the cruel one making comments like that."
    voice "audio/voice/E5/IRO/06/HA/HA007.ogg"
    hachiman "Anyway, why'd you come over here? You lose the battle for Hayama?"
    show iroha unimpressed with dissolve
    voice "audio/voice/E5/IRO/06/IR/IR006.ogg"
    iroha "Of course not. I'll have you know, I chose to come here myself."
    show iroha happy with dissolve
    voice "audio/voice/E5/IRO/06/IR/IR007.ogg"
    iroha "Besides, I'm someone who's more or less affiliated with the Service Club, aren't I?"
    voice "audio/voice/E5/IRO/06/HA/HA008.ogg"
    hachiman "Is that right?"
    show iroha vhappy with dissolve
    voice "audio/voice/E5/IRO/06/IR/IR008.ogg"
    iroha "Yep!"
    hachiman "(Hmmm...she seems like a completely different person after coming over here.)"
    hachiman "(Well, this is Iroha we're talking about. She probably got called over here by Miura or something, and just isn't telling us.)"
    show iroha mid_left happy with dissolve:
        xoffset -5 yoffset 65
    voice "audio/voice/E5/IRO/06/IR/IR009.ogg"
    iroha "Besides..."
    voice "audio/voice/E5/IRO/06/HA/HA009.ogg"
    hachiman "Hmm?"
    show iroha vhappy with dissolve
    voice "audio/voice/E5/IRO/06/IR/IR010.ogg"
    iroha "You need me to explain everything to you, starting from the \"I\" in Iroha!"
    voice "audio/voice/E5/IRO/06/HA/HA010.ogg"
    hachiman "............"
    voice "audio/voice/E5/IRO/06/HA/HA011.ogg"
    hachiman "Classic Iroha. No, I appreciate it. Thanks."
    show iroha mid_center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E5/IRO/06/IR/IR011.ogg"
    iroha "Yep!"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    jump E5_CMM_06

label E5_IRO_07:
    scene lodgeoutC with Fade(1.0, 1.0, 1.0)
    window auto show dissolve
    "Isshiki called me outside, and we stood under the clear winter sky. Stars twinkled as we gazed up at them."
    play music "audio/bgm/BGM10.ogg"
    show iroha coat_dark mid_left vhappy at center with dissolve:
        xoffset -5 yoffset 65
    voice "audio/voice/E5/IRO/07/IR/IR000.ogg"
    iroha "Waah, look, senpai! The stars are super pretty!"
    voice "audio/voice/E5/IRO/07/HA/HA000.ogg"
    hachiman "Wow, the stars from a snowy mountain are seriously romantic. I wanna stand shoulder-to-shoulder with Komachi and Totsuka and say something corny like \"these stars are shining bright, but you're shining "
    voice sustain
    hachiman "brighter!\""
    show iroha mid_center frown with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E5/IRO/07/IR/IR001.ogg"
    iroha "You sound more like a girl than I do right now. I'm pulling you back into line."
    voice "audio/voice/E5/IRO/07/HA/HA001.ogg"
    hachiman "Excuse me, young girls in love aren't the only ones allowed to comment on a starry night sky. Some things are romantic enough to be appreciated by all of humankind, regardless of age or gender. "
    voice sustain
    hachiman "Those things are celestial bodies, Totsuka, and younger sisters."
    show iroha unimpressed with dissolve
    voice "audio/voice/E5/IRO/07/IR/IR002.ogg"
    iroha "In your eyes, Totsuka-senpai and Komachi-chan are at the level of celestial bodies, huh..."
    hachiman "(They're greater than that. For these two, there's nothing I wouldn't do, even if the earth is destroyed.)"
    show iroha happy with dissolve
    voice "audio/voice/E5/IRO/07/IR/IR003.ogg"
    iroha "Anyway, it really is pretty out here. Are you pretty knowledgeable about constellations, senpai?"
    voice "audio/voice/E5/IRO/07/HA/HA002.ogg"
    hachiman "About as much as the average person, I guess."
    show iroha mid_left happy with dissolve:
        xoffset -5 yoffset 65
    voice "audio/voice/E5/IRO/07/IR/IR004.ogg"
    iroha "Hmm, then do you know what that constellation over there is called?"
    voice "audio/voice/E5/IRO/07/HA/HA003.ogg"
    hachiman "Ah, that's Orion. It's probably the most well-known of all the winter constellations, isn't it?"
    voice "audio/voice/E5/IRO/07/HA/HA004.ogg"
    hachiman "In the middle there are three stars lined up, so it makes it pretty easy to tell."
    voice "audio/voice/E5/IRO/07/HA/HA005.ogg"
    hachiman "Orion is in Greek myths too. I think it's the name of one of those arrogant guys whose pride is his downfall."
    show iroha unimpressed with dissolve
    voice "audio/voice/E5/IRO/07/IR/IR005.ogg"
    iroha "Woooow, is that so? That's suuuper interesting."
    voice "audio/voice/E5/IRO/07/HA/HA006.ogg"
    hachiman "You don't really have an interest in stars, huh."
    show iroha mid_center angry with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E5/IRO/07/IR/IR006.ogg"
    iroha "That's not true at all! I make sure to check my horoscope in magazines, after all."
    voice "audio/voice/E5/IRO/07/HA/HA007.ogg"
    hachiman "Doesn't that just mean you have an interest in horoscopes?"
    show iroha happy with dissolve
    voice "audio/voice/E5/IRO/07/IR/IR007.ogg"
    iroha "When you put it like that, maybe that's the case."
    show iroha blush with dissolve
    voice "audio/voice/E5/IRO/07/IR/IR008.ogg"
    iroha "But, I like observing the stars like this. After all, it's romantic. But..."
    hide iroha with dissolve
    stop music
    "That was sudden."
    play sound "audio/sfx/SE01/SE01_12.ogg"
    show iroha coat_dark near_center blush at center with dissolve:
        xoffset -15 yoffset 75
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E5/IRO/07/HA/HA008.ogg"
    hachiman "...!"
    play music "audio/bgm/BGM42.ogg"
    "Isshiki suddenly grabbed my arm and clung to it, while exhaling snowy-white breath from her shapely lips."
    "I could feel her warmth and softness through my jacket, and my heart rate reflexively shot up."
    voice "audio/voice/E5/IRO/07/IR/IR009.ogg"
    iroha "It's a bit chilly, isn't it?"
    hachiman "(This girl has a tendency to cling to me whenever she gets cold...you know I'm not your personal blanket, right?)"
    voice "audio/voice/E5/IRO/07/HA/HA009.ogg"
    hachiman "You're right, it is getting pretty cold. Maybe we should head back inside soon."
    "As I tried to lift my feet to start walking, Isshiki stopped me before I could even take a single step. She planted her feet in the snow as if trying to grow roots, and began to speak."
    show iroha happy with dissolve
    voice "audio/voice/E5/IRO/07/IR/IR010.ogg"
    iroha "Say, senpai..."
    voice "audio/voice/E5/IRO/07/HA/HA010.ogg"
    hachiman "Yeah?"
    show iroha blush with dissolve
    voice "audio/voice/E5/IRO/07/IR/IR011.ogg"
    iroha "Kissing the person you like in a place like this...it'd be pretty amazing, don't you think?"
    voice "audio/voice/E5/IRO/07/HA/HA011.ogg"
    hachiman "...!"
    voice "audio/voice/E5/IRO/07/HA/HA012.ogg"
    hachiman "Ah, well, that's true. But this is the last night we'll get to see these stars, so you'll have to wait for next time to see them with Hayama, huh."
    "I gave Isshiki a straightforward answer to her question."
    show iroha unimpressed with dissolve
    voice "audio/voice/E5/IRO/07/IR/IR012.ogg"
    iroha "*sigh*"
    "But after hearing my response, she let out a heavy sigh. "
    "I wonder if that was because of the cold, or perhaps due to something else."
    window auto hide dissolve
    hide iroha with dissolve
    $renpy.pause(delay=0.5, hard=True)
    scene irohaNightSky with dissolve
    window auto show dissolve
    voice "audio/voice/E5/IRO/07/IR/IR013.ogg"
    iroha "This is hard, huh..."
    "Muttering to herself, Isshiki raised her palms over her head toward the night sky. She observed the shining sea of stars through her fingers, with eyes just as bright."
    voice "audio/voice/E5/IRO/07/IR/IR014.ogg"
    iroha "Even as I reach my hands out, I know they'll never reach. Still, I want it, so I'll keep reaching out my hands..."
    voice "audio/voice/E5/IRO/07/IR/IR015.ogg"
    iroha "I think it's the same for a certain someone, too."
    voice "audio/voice/E5/IRO/07/HA/HA013.ogg"
    hachiman "You mean Hayama?"
    voice "audio/voice/E5/IRO/07/IR/IR016.ogg"
    iroha "............"
    window auto hide dissolve
    show irohaNightSky at right with dissolve:
        zoom 1.5 yoffset 425
    window auto show dissolve
    "Taking in the frigid night air, Isshiki lowered her arms."
    voice "audio/voice/E5/IRO/07/IR/IR017.ogg"
    iroha "Yeah, I bet it's like that for Hayama-senpai."
    voice "audio/voice/E5/IRO/07/IR/IR018.ogg"
    iroha "Still..."
    voice "audio/voice/E5/IRO/07/HA/HA014.ogg"
    hachiman "Hm?"
    voice "audio/voice/E5/IRO/07/IR/IR019.ogg"
    iroha "............"
    "A soft feeling on my cheeks. A scent as sweet as candy. And her alluring breathing."
    "Together, everything made my mind race with thoughts firing all over the place."
    voice "audio/voice/E5/IRO/07/IR/IR020.ogg"
    iroha "I think that more than one thing can be beautiful."
    voice "audio/voice/E5/IRO/07/IR/IR021.ogg"
    iroha "It's the same as those stars."
    hide irohaNightSky
    show irohaNightSky
    with dissolve
    voice "audio/voice/E5/IRO/07/IR/IR022.ogg"
    iroha "If you focus all your attention on a giant shining star, you miss out on the brilliance of the smaller star next to it, right?"
    voice "audio/voice/E5/IRO/07/IR/IR023.ogg"
    menu E5_IRO_07_menu:
        with dissolve
        iroha "Even though, to me, that giant star was the real deal..."
        "...":
            "not done"
            jump E5_IRO_07_menu
        "Even though that other star is smaller, huh?":
            voice "audio/voice/E5/IRO/07/HA/HA017.ogg"
            hachiman "Even though that other star is smaller, huh?"
            voice "audio/voice/E5/IRO/07/IR/IR026.ogg"
            iroha "Yeah. It turns out, the thing important to me wasn't the star's size."
            voice "audio/voice/E5/IRO/07/IR/IR027.ogg"
            iroha "What matters is whether the star is the real deal or not."
            hachiman "(Whether it's the real deal or not...?)"
            voice "audio/voice/E5/IRO/07/HA/HA018.ogg"
            hachiman "Is that so?"
            voice "audio/voice/E5/IRO/07/IR/IR028.ogg"
            iroha "Yeah, it is."
        "Sorry, this reminds me of \"The Nighthawk Star\"":
            "not done"
            jump E5_IRO_07_menu

    window auto hide dissolve
    $renpy.pause(delay=0.5, hard=True)
    scene lodgeoutC
    show iroha coat_dark mid_center happy at center:
        xoffset 25 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/IRO/07/IR/IR032.ogg"
    iroha "Well, I'm gonna head back first."
    show iroha vhappy with dissolve
    voice "audio/voice/E5/IRO/07/IR/IR033.ogg"
    iroha "Senpai, thanks for coming out here with me!"
    voice "audio/voice/E5/IRO/07/HA/HA021.ogg"
    hachiman "Uh--ah, yeah. No problem."
    hide iroha with dissolve
    play sound "audio/sfx/SE00/SE00_22L.ogg"
    "Isshiki returned to the villa, leaving me with her usual mischievous smile and a warm feeling on my cheeks."
    "I stood alone under the starry sky, following the back of Isshiki's figure with my eyes as I found myself thinking."
    "Isshiki had completely caught me off guard, and I considered what she meant by that kiss earlier."
    window auto hide dissolve
    stop sound
    stop music fadeout 1.0
    jump E5_IRO_08

label E5_IRO_08:
    scene black with Fade(0.5, 0.5, 0)
    play sound "audio/sfx/SE04/SE04_06.ogg"
    scene lodgeroomC with Fade(0, 0, 0.5)
    $renpy.pause(delay=0.75, hard=True)
    stop sound
    window auto show dissolve
    voice "audio/voice/E5/IRO/08/HA/HA000.ogg"
    hachiman "Damn, outside was freezing...definitely better to stay indoors."
    hachiman "(Well, I guess the stars were pretty at least)"
    window auto hide dissolve
    scene irohaNightSky with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    voice "audio/voice/E5/IRO/08/IR/IR000.ogg"
    iroha "If you focus all your attention on a giant shining star, you miss out on the brilliance of the smaller star next to it, right?"
    voice "audio/voice/E5/IRO/08/IR/IR001.ogg"
    iroha "Even though, to me, that giant star was the real deal..."
    window auto hide dissolve
    stop voice
    scene lodgeroomC with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    voice "audio/voice/E5/IRO/08/HA/HA001.ogg"
    hachiman "............"
    hachiman "(What is that girl thinking...?)"
    hachiman "(More importantly, I was kissed, wasn't I? She kissed my cheek. What the hell? Is Iroha-chan a Westerner or something?)"
    hachiman "(No, no, my head got cold from being outside too long and now I can't think straight.)"
    hachiman "(Maybe I should take a bath...)"
    window auto hide dissolve
    scene black with Fade(0.5, 1.5, 0)
    play sound "audio/sfx/SE04/SE04_08.ogg"
    show hotspringBGB with Fade(0, 0, 0.25)
    window auto show dissolve
    "I pushed open the sliding door to the outdoor bath."
    stop sound
    "As I did so, I spotted the figures of people already inside."
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_31.ogg"
    show hachimanBathe with dissolve
    play music "audio/bgm/BGM40.ogg"
    $renpy.pause(delay=0.75, hard=True)
    window auto show dissolve
    voice "audio/voice/E5/IRO/08/TB/TB000.ogg"
    tobe "Oh, if it isn't Hikitani-kun!"
    voice "audio/voice/E5/IRO/08/HY/HY000.ogg"
    hayama "Ah! You came too, huh?"
    voice "audio/voice/E5/IRO/08/HA/HA002.ogg"
    hachiman "My body was freezing, so..."
    voice "audio/voice/E5/IRO/08/TB/TB001.ogg"
    tobe "That's no goooood~ Well, don't be shy; get in here!"
    hachiman "(Who the hell said anything about being shy?)"
    hide hachimanBathe with dissolve
    "I soaked in the bath and let out a sigh. These two continued their conversation that I probably interrupted."
    voice "audio/voice/E5/IRO/08/TB/TB002.ogg"
    tobe "Man, that was my first time skiing in forever...now I'm sore all over."
    voice "audio/voice/E5/IRO/08/HY/HY001.ogg"
    hayama "Yeah?"
    voice "audio/voice/E5/IRO/08/TB/TB003.ogg"
    tobe "I couldn't even eat, bro! When I tried, my teeth would start bleeding..."
    hachiman "(That has absolutely nothing to do with skiing. Probably a cavity or sensitive teeth.)"
    show hachimanBathe with dissolve
    voice "audio/voice/E5/IRO/08/TB/TB004.ogg"
    tobe "And this muscle soreness, man? Ah, this bath is really doing wonders for it right now."
    voice "audio/voice/E5/IRO/08/HY/HY002.ogg"
    hayama "Hahaha, probably because you're working different muscles from when we play soccer."
    voice "audio/voice/E5/IRO/08/TB/TB005.ogg"
    tobe "Ahh, well, I'm gonna need more than this bath to get rid of this soreness "
    voice "audio/voice/E5/IRO/08/TB/TB006.ogg"
    tobe "Is there a massage chair or somethin' around here?"
    voice "audio/voice/E5/IRO/08/HY/HY003.ogg"
    hayama "Doesn't look like it. You should carefully stretch after you get out of the bath."
    voice "audio/voice/E5/IRO/08/TB/TB007.ogg"
    tobe "Roger that!"
    voice "audio/voice/E5/IRO/08/TB/TB008.ogg"
    tobe "Ah-"
    voice "audio/voice/E5/IRO/08/HY/HY004.ogg"
    hayama "What's up?"
    window auto hide dissolve
    show hachimanBathd with dissolve:
        zoom 1.5 xoffset -75 yoffset -225
    window auto show dissolve
    voice "audio/voice/E5/IRO/08/TB/TB009.ogg"
    tobe "An idea popped into my head!"
    voice "audio/voice/E5/IRO/08/TB/TB010.ogg"
    tobe "What if we got Irohasu to give us massages? As the manager of the soccer club!"
    voice "audio/voice/E5/IRO/08/HA/HA003.ogg"
    hachiman "............"
    "My ears perk up at the sudden mention of Isshiki's name as I can't help but remember that itching feeling in my chest."
    voice "audio/voice/E5/IRO/08/TB/TB011.ogg"
    tobe "C'mon, if we ask, there's a chance!"
    hide hachimanBathd with dissolve
    voice "audio/voice/E5/IRO/08/HY/HY005.ogg"
    hayama "Iroha is...well, how do I put it. I don't think she'd do it."
    voice "audio/voice/E5/IRO/08/TB/TB012.ogg"
    tobe "Guess there's no way, huh. I mean, I always see her help you stretch and stuff, but I've never gotten that kind of treatment before. If anything, she just makes me do a ton of chores."
    voice "audio/voice/E5/IRO/08/HY/HY006.ogg"
    hayama "Tobe...maybe you give her too much attention? I think Iroha likes someone who'll leave her alone from time to time. "
    voice "audio/voice/E5/IRO/08/TB/TB013.ogg"
    tobe "So that's it, huh. But Irohasu feels like a younger sister, so it's hard to not do that, you know?"
    voice "audio/voice/E5/IRO/08/HA/HA004.ogg"
    hachiman "..............."
    hachiman "(Younger sister...)"
    voice "audio/voice/E5/IRO/08/HY/HY007.ogg"
    hayama "Hahaha, a younger sister, huh? Somehow, I kinda get what you mean."
    voice "audio/voice/E5/IRO/08/TB/TB014.ogg"
    tobe "I know, right? She's totally got that little sis vibe! Yay, Hayato-kun totally understands what I'm saying!"
    voice "audio/voice/E5/IRO/08/HA/HA005.ogg"
    hachiman "............"
    stop voice
    stop music
    show skyC with dissolve
    "I hate to admit it, but I understand where Tobe's coming from."
    "I might be contradicting myself or saying something audacious, but it's probably because she kinda reminds me of my dear sister."
    "And I think the reason Isshiki is oddly giving me attention is because she sees me as an older brother."
    voice "audio/voice/E5/IRO/08/HA/HA006.ogg"
    hachiman "............"
    "Even so, that doesn't explain why my cheeks turned as red as Isshiki's lips."
    window auto hide dissolve
    scene skyC with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM10.ogg"
    window auto show dissolve
    hachiman "(I just thought I'd just take some time to relax, but of course I had to run into Hayama in the bath.)"
    hachiman "(Well, all that's left to do after this is sleep, and then this is the end of the trip, huh.)"
    hachiman "(I went into the bath to relax, and yet I still feel exhausted...)"
    play sound "audio/sfx/SE00/SE00_30L.ogg"
    hachiman "(Isshiki Iroha, huh...)"
    window auto hide dissolve
    stop sound fadeout 1.0
    scene lodgeC with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    "Tired from thinking, I wandered to the entrance of the living room. For whatever reason, my throat was super dry."
    hachiman "(Hm?)"
    jump E5_IRO_09

label E5_IRO_09:
    show komachi home mid_left happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/IRO/09/KO/KO000.ogg"
    komachi "Oh! Onii-chan!"
    voice "audio/voice/E5/IRO/09/HA/HA000.ogg"
    hachiman "Oh? Just get out of the bath?"
    "I bumped into Komachi, who had one hand on her waist and a fruit milk in the other."
    voice "audio/voice/E5/IRO/09/HA/HA001.ogg"
    hachiman "I didn't know you went in the bath, too."
    show komachi mid_center happy with dissolve:
        xoffset -75
    voice "audio/voice/E5/IRO/09/KO/KO001.ogg"
    komachi "I went with Yukino-san and Yui-san!"
    voice "audio/voice/E5/IRO/09/HA/HA002.ogg"
    hachiman "Really? It was so quiet I had no idea. Figured you three would be pretty loud in there."
    show komachi vhappy with dissolve
    voice "audio/voice/E5/IRO/09/KO/KO002.ogg"
    komachi "Probably 'cause we were relaxing and enjoying the scenery."
    show komachi unimpressed with dissolve
    voice "audio/voice/E5/IRO/09/KO/KO003.ogg"
    komachi "I heard some loud yelling and crying from the other side, though."
    voice "audio/voice/E5/IRO/09/HA/HA003.ogg"
    hachiman "Ah, I feel like I should be apologizing here. Sorry it was so loud. I bet it totally ruined the calm vibe over there, huh."
    show komachi happy with dissolve
    voice "audio/voice/E5/IRO/09/KO/KO004.ogg"
    komachi "Not at all, it was exciting. If Onii-chan was having fun, that's what matters to Komachi!"
    voice "audio/voice/E5/IRO/09/HA/HA004.ogg"
    hachiman "Haha."
    show komachi vhappy with dissolve
    voice "audio/voice/E5/IRO/09/KO/KO005.ogg"
    komachi "You were playing by yourself as the others were having exciting conversations, weren't you? I bet you were putting your towel in the water pretending it was a jellyfish...like I said, if you're having fun, "
    voice sustain
    komachi "that's all that matters!"
    voice "audio/voice/E5/IRO/09/HA/HA005.ogg"
    hachiman "What kind of scene are you imagining...that was oddly specific. And I'll have you know that I would never do something like that; it's bad manners, you know..."
    show komachi unimpressed with dissolve
    voice "audio/voice/E5/IRO/09/KO/KO006.ogg"
    komachi "So you're not denying the part about being alone, huh...Onii-chan, Komachi isn't sure if she should feel bad for you or be proud of your manners..."
    show komachi vhappy with dissolve
    stop music fadeout 1.0
    "Another one of our usual childish conversations. Komachi is a bit brash, but it's one of the things I love about my dear sister."
    image iroha_E5 = Flatten("iroha home mid_center happy")
    show black:
        alpha 0
        parallel:
            1.0
            linear 1.0 alpha 1.0
    show iroha_E5 at center:
        xoffset -5 yoffset 75 alpha 0
        parallel:
            1.0
            linear 1.0 alpha 1.0
    "And as I talk to Komachi, Isshiki's face suddenly pops into my mind."
    play music "audio/bgm/BGM46.ogg"
    hide black
    hide iroha_E5
    show black
    show iroha_E5 at center:
        xoffset -5 yoffset 75
    "I can't lie to myself. I have a lot of affection for Isshiki. "
    "She's certainly left an impression on me, and I can't help but be attracted to her."
    "These feelings I have toward Isshiki are the same kind of deep affection I have for Komachi, aren't they? "
    "Isn't this a common feeling that everyone has? It can't just be me."
    window auto hide dissolve
    scene lodgeroomC with Fade(0.5, 0.5, 0.5)
    window auto show dissolve
    voice "audio/voice/E5/IRO/09/HA/HA006.ogg"
    hachiman "............"
    "My thoughts continue to spiral into more and more self-questioning with no sign of stopping."
    "But still..."
    "One thing's for certain. The more I try to simply think of Isshiki as a younger sister, the more I remember that unexplainable itching in my chest."
    window auto hide dissolve
    stop music fadeout 1.0
    call loading_screen(10) from _call_loading_screen_26
    jump E6_CMM_01
