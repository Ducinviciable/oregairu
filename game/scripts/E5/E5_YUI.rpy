label E5_YUI_01:
    scene lodgeA with dissolve
    play music "audio/bgm/BGM07.ogg"
    "And so, a huge number of people, consisting of me, Yuigahama, Hayama and Tobe, were assigned to clean the floor. I get you'd want to clean the place as soon as you arrive. Besides, our job is easier than the others."
    show hayama coat mid_right happy at left:
        yoffset 75
    show yui coat mid_center pout at center:
        yoffset 75
    show tobe coat mid surprised at right:
        yoffset 75
    with dissolve
    voice "audio/voice/E5/YUI/01/TB/TB000.ogg"
    tobe "Ugh, we're cleaning right off the bat. This sucks..."
    show yui coat mid_center annoyed at center with dissolve:
        yoffset 75
    voice "audio/voice/E5/YUI/01/YI/YI000.ogg"
    yui "Tobecchi, stop complaining! Let's just get this over with!"
    show yui coat mid_center angry at center with dissolve:
        yoffset 75
    play sound "<loop 2>audio/sfx/SE01/SE01_25L.ogg" loop
    voice "audio/voice/E5/YUI/01/YI/YI001.ogg"
    yui "Look, even Hikki's doing it properly!"
    stop sound fadeout 1.25
    hachiman "(I just want this to end quicker...)"
    voice "audio/voice/E5/YUI/01/HA/HA000.ogg"
    hachiman "It's because we'd finish this kind of work faster if we just stopped thinking and just moved."
    voice "It is true however that we'll only get to do this together while we're students."
    show tobe coat mid vhappy at right with dissolve:
        yoffset 75
    voice "audio/voice/E5/YUI/01/TB/TB001.ogg"
    tobe "Right! That's true, Hayato-kun!"
    show hayama coat mid_right vhappy at left with dissolve:
        yoffset 75
    voice "audio/voice/E5/YUI/01/HY/HY001.ogg"
    hayama "But getting to see Hikitani so absorbed in cleaning isn't something you see everyday."
    voice "audio/voice/E5/YUI/01/TB/TB002.ogg"
    tobe "I know, right?"
    hide hayama
    $url = ["hayama coat mid_right sad", "hayama coat mid_right happy"]
    $multiImagePara = [-567, 75, 0, 0, 2]
    call multiImage() from _call_multiImage_E5_YUI_01_1
    voice "audio/voice/E5/YUI/01/HY/HY002.ogg"
    hayama "Tobe, you should learn from him. Then, Hikitani and Yui, you guys can start sweeping from that part towards us, and after we finish our section, we'll start cleaning the floors with cloth."
    call finishmultiImage from _call_finishmultiImage_E5_YUI_01_1
    show hayama coat mid_right happy behind yui at left:
        yoffset 75
    show tobe coat mid sad at right with dissolve:
        yoffset 75
    voice "audio/voice/E5/YUI/01/TB/TB003.ogg"
    tobe "With cloth? That's a thing!?"
    voice "audio/voice/E5/YUI/01/HY/HY003.ogg"
    hayama "Sure is. Yui, Hikitani, I'm leaving the sweeping to you."
    hide hayama
    hide yui
    hide tobe
    with dissolve
    voice "audio/voice/E5/YUI/01/HA/HA001.ogg"
    hachiman "S-Sure... Why did this guy end up taking command?"
    voice "audio/voice/E5/YUI/01/HA/HA002.ogg"
    hachiman "Well, as long as the works alloted, it's fine with me."
    show hayama coat far_center pout at left:
        xoffset 250 yoffset 75
    show tobe coat far surprised at right:
        xoffset -250 yoffset 75
    with dissolve
    voice "audio/voice/E5/YUI/01/HY/HY004.ogg"
    hayama "Come on, Tobe. Let's start."
    voice "audio/voice/E5/YUI/01/TB/TB004.ogg"
    tobe "Hayato-kun, you work smooth! That was crazy!"
    hide hayama
    hide tobe
    with dissolve
    play sound "<loop 2>audio/sfx/SE01/SE01_25L.ogg" loop
    hachiman "(He can rinse a cloth, too... Looks like Hayama can do his fair share of housework.)"
    stop sound fadeout 1.25
    play sound "audio/sfx/SE04/SE04_05.ogg"
    scene lodgeA at truecenter:
        zoom 1.45 xoffset -200 yoffset 80
    show iroha coat mid_left vhappy zorder 1 at right:
        xalign 1.0 yoffset 75 alpha 0
        on show:
            easein 0.35 xalign 0.92 alpha 1
    voice "audio/voice/E5/YUI/01/IR/IR000.ogg"
    iroha "Hayama-senpai~! How's the cleaning coming along~?"
    show hayama coat mid_right happy zorder 1 at left:
        xoffset -50 yoffset 75
    show tobe coat mid surprised at center:
        xoffset 45 yoffset 75
    with dissolve
    voice "audio/voice/E5/YUI/01/HY/HY005.ogg"
    hayama "...Ah, Iroha."
    voice "audio/voice/E5/YUI/01/TB/TB005.ogg"
    tobe "Not good."
    play sound "audio/sfx/SE01/SE01_28.ogg"
    show iroha coat mid_center surprised zorder 1 with dissolve
    voice "audio/voice/E5/YUI/01/IR/IR001.ogg"
    iroha "By the way, when it comes to wiping down the floor, seeing only senpai wiping with a cloth is surprising. It's exactly the opposite of the kind of image you put out."
    show tobe coat mid sad at center with dissolve:
        xoffset 45 yoffset 75
    voice "audio/voice/E5/YUI/01/TB/TB006.ogg"
    tobe "Irohasu~ I'm doing the same thing~"
    show iroha coat mid_left angry zorder 1 with dissolve
    voice "audio/voice/E5/YUI/01/IR/IR002.ogg"
    iroha "Ah, Tobe-senpai, you should wipe the floor clean like that your whole life. You missed a spot in the corner, too."
    hide tobe with dissolve
    voice "audio/voice/E5/YUI/01/HA/HA003.ogg"
    hachiman "He just ended up like that by chance... What does this wiping the floor with a cloth image even entail?"
    voice "audio/voice/E5/YUI/01/HA/HA004.ogg"
    hachiman "Forget that, Ishiki, what about your part in the clean-up?"
    show iroha coat mid_center vhappy zorder 1 with dissolve
    voice "audio/voice/E5/YUI/01/IR/IR003.ogg"
    iroha "I quickly finished up and came here!"
    play sound "audio/sfx/SE01/SE01_28.ogg"
    hachiman "(No way. There's absolutely no way... She just pushed her job on someone and came I bet...)"
    show iroha coat mid_left vhappy zorder 1 with dissolve
    voice "audio/voice/E5/YUI/01/IR/IR004.ogg"
    iroha "Maybe I could help wipe the floors, too."
    show hayama coat mid_right vhappy zorder 1 at left:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/YUI/01/HY/HY006.ogg"
    hayama "It's okay, I think we've got it covered. You can prepare to go skiing, Iroha."
    hide iroha
    $url = ["iroha coat mid_left sad", "iroha coat mid_left happy"]
    $multiImagePara = [550, 75, 0, 0, 2.4]
    call multiImage() from _call_multiImage_E5_YUI_01_2
    voice "audio/voice/E5/YUI/01/IR/IR005.ogg"
    iroha "Oh... But we'd better get it done quicker. For the other's sake."
    call finishmultiImage from _call_finishmultiImage_E5_YUI_01_2
    show iroha coat mid_left happy zorder 1 at center:
        xoffset 550 yoffset 75
    voice "audio/voice/E5/YUI/01/HA/HA005.ogg"
    hachiman "..."
    show hayama coat mid_right relieved zorder 1 at left with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/YUI/01/HY/HY007.ogg"
    hayama "Ah, I think it'll be fine. We got enough people right now I think."
    show tobe coat mid happy at center with dissolve:
        xoffset 45 yoffset 75
    voice "audio/voice/E5/YUI/01/TB/TB007.ogg"
    tobe "True! You can leave it to us."
    show iroha coat mid_left frown zorder 1 with dissolve
    voice "audio/voice/E5/YUI/01/IR/IR006.ogg"
    iroha "No, Tobe-senpai you can shut up and get back to work. The corner. That spot's still there. Everybody's waiting, so hurry up."
    show tobe coat mid worried at center with dissolve:
        xoffset 45 yoffset 75
    voice "audio/voice/E5/YUI/01/TB/TB008.ogg"
    tobe "Right..."
    voice "audio/voice/E5/YUI/01/YI/YI002.ogg"
    yui "Ahaha.. Chatting like this reminds me of summer camp."
    show tobe coat mid vhappy at center:
        xoffset 45 yoffset 75
    show hayama coat mid_right happy zorder 1 at left:
        xoffset -50 yoffset 75
    with dissolve
    voice "audio/voice/E5/YUI/01/HY/HY008.ogg"
    hayama "Yeah, it does."
    voice "audio/voice/E5/YUI/01/TB/TB009.ogg"
    tobe "Right!"
    show iroha coat mid_left surprised zorder 1 with dissolve
    voice "audio/voice/E5/YUI/01/IR/IR007.ogg"
    iroha "Eh~ That's not fair! Only you guys go to go."
    voice "audio/voice/E5/YUI/01/HA/HA006.ogg"
    hachiman "What can we do? You weren't even attending our school..."
    stop music fadeout 1.15
    scene lodgeA with dissolve
    play music "audio/bgm/BGM12.ogg"
    show yui coat mid_center angry at center with dissolve:
        yoffset 75
    voice "audio/voice/E5/YUI/01/YI/YI003.ogg"
    yui "But still... a lot's changed since then."
    menu floor_cleaning_menu:
        "...":
            voice "audio/voice/E5/YUI/01/HA/HA007.ogg"
            hachiman "..."
            hachiman "(I guess that's true. At that time, I still...)"
            voice "audio/voice/E5/YUI/01/HA/HA008.ogg"
            hachiman "Yeah, at the time I would've rather died than to go camp."
            show yui coat mid_center vhappy at center with dissolve:
                yoffset 75
            voice "audio/voice/E5/YUI/01/YI/YI004.ogg"
            yui "Yeah. Hikki~, you look like you wanted to leave all the time."
            show iroha coat mid_left vhappy zorder 1 at right:
                xalign 1.0 yoffset 75 alpha 0
                on show:
                    easein 0.35 xalign 0.9 alpha 1
            voice "audio/voice/E5/YUI/01/IR/IR008.ogg"
            iroha "Eh~ What's this about? Is it something amusing? This is like a little secret talk."
            show yui coat mid_right surprised at center with dissolve:
                xoffset -100 yoffset 75
            voice "audio/voice/E5/YUI/01/YI/YI005.ogg"
            yui "N-No, it's not like that!"
            scene black with Fade(0.5, 1.0, 0.5)
            play sound "audio/sfx/SE01/SE01_28.ogg"
        "What has?":
            "not done"
            jump floor_cleaning_menu
        "It has?": #Google Transalted
            "not done"
            jump floor_cleaning_menu
    scene lodgeA with dissolve
    voice "audio/voice/E5/YUI/01/HA/HA016.ogg"
    hachiman "We're more or less done with the sweeping."
    show hayama coat mid_center pout at left:
        xoffset 155 yoffset 75
    show yui coat mid_left happy at right:
        xoffset -250 yoffset 75
    with dissolve
    voice "audio/voice/E5/YUI/01/HY/HY009.ogg"
    hayama "I see. Then..."
    show yui coat mid_center happy at right with dissolve:
        xoffset -250 yoffset 75
    voice "audio/voice/E5/YUI/01/YI/YI012.ogg"
    yui "T-Then let's get some cloth to wipe the floor with, too, Hikki."
    voice "audio/voice/E5/YUI/01/HA/HA017.ogg"
    hachiman "...Right."
    show hayama coat mid_right happy at left with dissolve:
        xoffset 155 yoffset 75
    voice "audio/voice/E5/YUI/01/HY/HY010.ogg"
    hayama "No, you don't have to, Yui. I think the boys are enough."
    show yui coat mid_left surprised at right with dissolve:
        xoffset -250 yoffset 75
    voice "audio/voice/E5/YUI/01/HA/HA018.ogg"
    hachiman "Figures."
    hachiman "(That's Hayama for you...)"
    play sound "audio/sfx/SE01/SE01_27.ogg"
    voice "audio/voice/E5/YUI/01/HA/HA019.ogg"
    hachiman "Yuigahama, it's like Hayama says. You can get some rest."
    hachiman "(The corporate drone within me is crying though...)"
    show yui coat mid_left sad at right with dissolve:
        xoffset -250 yoffset 75
    voice "audio/voice/E5/YUI/01/YI/YI013.ogg"
    yui "O-Okay."
    hachiman "(Eh? Why does she look so sad? Did she want to wipe the floor, too?)"
    voice "audio/voice/E5/YUI/01/HA/HA020.ogg"
    hachiman "What's wrong, Yuigahama?"
    show yui coat mid_center happy at right with dissolve:
        xoffset -250 yoffset 75
    voice "audio/voice/E5/YUI/01/YI/YI014.ogg"
    yui "I-It's nothing! Well, Hikki, Hayato-kun, Tobecchi, I'll leave the rest to you."
    show hayama coat mid_right vhappy at left with dissolve:
        xoffset 155 yoffset 75
    voice "audio/voice/E5/YUI/01/HY/HY011.ogg"
    hayama "Yep. Good work, Yui."
    voice "audio/voice/E5/YUI/01/HA/HA021.ogg"
    hachiman "Good work."
    hachiman "(Can't we just have Hayama clean the floor? He looks like he's having fun and Isshiki looks like she wants to help out, too.)"
    voice "audio/voice/E5/YUI/01/TB/TB010.ogg"
    tobe "Good wo--rk!"
    show yui coat mid_center sad at right with dissolve:
        xoffset -250 yoffset 75
    voice "audio/voice/E5/YUI/01/YI/YI015.ogg"
    yui "R-Right... Hah."
    stop music fadeout 1.25
    jump E5_G13_01


label E5_YUI_02:
    show yui heavy_coat mid_left vhappy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI000.ogg"
    yui "Okay, Hikki~! Let's begin your special training!"
    voice "audio/voice/E5/YUI/02/HA/HA000.ogg"
    hachiman "Yeah. Say, where's Yukinoshita?"
    show yui heavy_coat mid_left pout at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI001.ogg"
    yui "She got caught by Haruno a little while ago. She had to ride the lift..."
    voice "audio/voice/E5/YUI/02/HA/HA001.ogg"
    hachiman "She probably challenged her to a race..."
    voice "audio/voice/E5/YUI/02/YI/YI002.ogg"
    yui "Looks like it..."
    hachiman "(Looks like Yukinoshita's gotten serious...)"
    voice "audio/voice/E5/YUI/02/HA/HA002.ogg"
    hachiman "Well, it doesn't seem like they'll be back anytime soon. Well, if it's just race, we don't have anything to worry about."
    show yui heavy_coat mid_center pout at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI003.ogg"
    yui "...Yeah."
    show yui heavy_coat mid_center happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI004.ogg"
    yui "Let's get started then!"
    show yui heavy_coat mid_center vhappy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI005.ogg"
    yui "Ehehe, I say that, but I'm really not that good."
    menu yui_ski_choice1:
        "I'm not expecting anything crazy.":
            "not done"
            jump yui_ski_choice1
            voice "audio/voice/E5/YUI/02/HA/HA003.ogg"
            hachiman ""
            voice "audio/voice/E5/YUI/02/HA/HA004.ogg"
            hachiman ""
            voice "audio/voice/E5/YUI/02/YI/YI006.ogg"
            yui ""
            voice "audio/voice/E5/YUI/02/YI/YI007.ogg"
            yui ""
        "Let's take it slow then.":
            voice "audio/voice/E5/YUI/02/HA/HA005.ogg"
            hachiman "Let's take it slow then."
            show yui heavy_coat mid_center blush at center with dissolve:
                xoffset 10 yoffset 75
            voice "audio/voice/E5/YUI/02/YI/YI008.ogg"
            yui "Heheh... I feel kind of relieved to hear you say that."
            voice "audio/voice/E5/YUI/02/HA/HA006.ogg"
            hachiman "How do I say this...? You're surprisingly service-minded."
            voice "audio/voice/E5/YUI/02/YI/YI009.ogg"
            yui "R-Right."
        "Let's get someone to teach us.":
            "not done"
            jump yui_ski_choice1
            voice "audio/voice/E5/YUI/02/HA/HA007.ogg"
            hachiman ""
            voice "audio/voice/E5/YUI/02/HA/HA008.ogg"
            hachiman ""
            voice "audio/voice/E5/YUI/02/YI/YI010.ogg"
            yui ""
            voice "audio/voice/E5/YUI/02/YI/YI011.ogg"
            yui ""
    show yui heavy_coat mid_center happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI012.ogg"
    yui "Well, let's start with \"snowplough turn\"."
    hachiman "(What's that, a luxury ice cream?)"
    show yui heavy_coat mid_left happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI013.ogg"
    yui "Erm, first, you have to open your legs like this..."
    voice "audio/voice/E5/YUI/02/HA/HA009.ogg"
    hachiman "...Like this?"
    $url = ["yui heavy_coat mid_center happy", "yui heavy_coat mid_center angry"]
    $multiImagePara = [10, 75, 0, 0, 2.1]
    call multiImage() from _call_multiImage_E5_YUI_02_1
    voice "audio/voice/E5/YUI/02/YI/YI014.ogg"
    yui "Yeah, like that! Ah, a little wider though."
    call finishmultiImage from _call_finishmultiImage_E5_YUI_02_1
    show yui heavy_coat mid_left angry at center:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/HA/HA010.ogg"
    hachiman "I see...how about this?"
    show yui heavy_coat mid_center vhappy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI015.ogg"
    yui "Exactly! And then just slowly push your legs forward..."
    voice "audio/voice/E5/YUI/02/HA/HA011.ogg"
    hachiman "I never thought I'd be doing a trendy sport like this..."
    hachiman "(And with a kind coach to boot.)"
    $url = ["yui heavy_coat mid_center vhappy", "yui heavy_coat mid_center happy"]
    $multiImagePara = [10, 75, 0, 0, 2.2]
    call multiImage() from _call_multiImage_E5_YUI_02_2
    voice "audio/voice/E5/YUI/02/YI/YI016.ogg"
    yui "You keep saying that, but you're doing pretty good right now, you know?"
    call finishmultiImage from _call_finishmultiImage_E5_YUI_02_2
    show yui heavy_coat mid_center happy at center:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/HA/HA012.ogg"
    hachiman "I-I am? Say, you're a surprisingly good coach."
    show yui heavy_coat mid_center blush at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI017.ogg"
    yui "Eh!? You think? S-Sure I am!"
    hide yui with dissolve
    scene black with Fade(0.5, 1.0, 0.5)
    scene slopesA
    show yui heavy_coat mid_center happy at center:
        xoffset 10 yoffset 75
    with dissolve
    voice "audio/voice/E5/YUI/02/YI/YI018.ogg"
    yui "Okay, wanna try sliding for a bit?"
    voice "audio/voice/E5/YUI/02/HA/HA013.ogg"
    hachiman "Yeah. I think I got the basics down."
    voice "audio/voice/E5/YUI/02/YI/YI019.ogg"
    yui "This is the beginner's course, so I think you'll be fine!"
    window auto hide dissolve
    hide yui with dissolve
    play sound "audio/sfx/SE01/SE01_41.ogg"
    $renpy.pause(delay=2.0, hard=True)
    voice "audio/voice/E5/YUI/02/HA/HA014.ogg"
    hachiman "L-Like this?"
    show yui heavy_coat mid_left vhappy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI020.ogg"
    yui "Yeah, that's the way! Come on, Hikki, you're actually pretty good!"
    voice "audio/voice/E5/YUI/02/HA/HA015.ogg"
    hachiman "No way, this is actually pretty fun."
    hachiman "(Wait, this is actually really fun. I hate to say it, but it is.)"
    voice "audio/voice/E5/YUI/02/YI/YI021.ogg"
    yui "I know, right!?"
    hachiman "(She looks really happy.)"
    scene slopesA at truecenter with dissolve:
        zoom 1.75 xoffset 405 yoffset 35
    voice "audio/voice/E5/YUI/02/YM/YM000.ogg"
    yumiko "Hayato, wanna take it from the top again?"
    voice "audio/voice/E5/YUI/02/TB/TB000.ogg"
    tobe "Hayato-kun, let's snowboard! Wanna try, too, Ebina?"
    voice "audio/voice/E5/YUI/02/EB/EB000.ogg"
    ebina "If you ask me what I want, I'd say I want to see Tobe and Hayato skiing, covered in snow! Boys getting heartily covered in snow..."
    voice "audio/voice/E5/YUI/02/YM/YM001.ogg"
    yumiko "Ebina, put the mask back on."
    voice "audio/voice/E5/YUI/02/HY/HY000.ogg"
    hayama "Alright. Why don' we all go?"
    scene slopesA
    show yui heavy_coat mid_left vhappy at center:
        xoffset 10 yoffset 75
    with dissolve
    voice "audio/voice/E5/YUI/02/HA/HA016.ogg"
    hachiman "Say..."
    show yui heavy_coat mid_left surprised at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI022.ogg"
    yui "Huh?"
    voice "audio/voice/E5/YUI/02/HA/HA017.ogg"
    hachiman "Is it okay if you don't join them?"
    show yui heavy_coat mid_center happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI023.ogg"
    yui "Mm, I might actually just get in the way right now! You know, with... stuff."
    voice "audio/voice/E5/YUI/02/HA/HA018.ogg"
    hachiman "R-Right... I see."
    "Looks like Miura'll be skiing with Hayama and Tobe with Ebina. She doesn't want to get in the way of that."
    hachiman "(That being said... she might be too preoccupied with me. It's not like she doesn't want to spend time with them and make memories.)"
    voice "audio/voice/E5/YUI/02/HA/HA019.ogg"
    hachiman "Well, I think I'll be fine at this level..."
    show yui heavy_coat mid_center unimpressed at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI024.ogg"
    yui "Eh~? Since we've already started, let's get you better!"
    voice "audio/voice/E5/YUI/02/HA/HA020.ogg"
    hachiman "Should we?"
    show yui heavy_coat mid_center vhappy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI025.ogg"
    yui "We should!"
    play sound "<loop 2>audio/sfx/SE01/SE01_44L.ogg" loop
    "Even though Yuigahama shows me a brilliant smile, I still can't shake the feeling I'm getting in the way of her friendships."
    show yui heavy_coat mid_left happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI026.ogg"
    yui "So, this time we'll..."
    window auto hide dissolve
    hide yui with dissolve
    stop sound fadeout 1.0
    stop music fadeout 1.0
    play sound "audio/sfx/SE01/SE01_47.ogg"
    $renpy.pause(delay=0.5, hard=True)
    show kaori heavy_coat mid annoyed at left:
        xoffset 180 yoffset 75
    show yui heavy_coat mid_left happy at right:
        xoffset -255 yoffset 75
    with dissolve
    voice "audio/voice/E5/YUI/02/OR/OR000.ogg"
    kaori "Ah, Hikigaya and... Yuigahama-san?"
    voice "audio/voice/E5/YUI/02/HA/HA021.ogg"
    hachiman "'Sup."
    show yui heavy_coat mid_left vhappy at right with dissolve:
        xoffset -255 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI027.ogg"
    yui "Y-Yahallo! You're pretty good at skiing. Ahaha..."
    play music "audio/bgm/BGM47.ogg"
    show kaori heavy_coat mid closed at left with dissolve:
        xoffset 180 yoffset 75
    voice "audio/voice/E5/YUI/02/OR/OR001.ogg"
    kaori "Oh? This's surprising."
    voice "audio/voice/E5/YUI/02/HA/HA022.ogg"
    hachiman "What is?"
    show kaori heavy_coat mid happy at left with dissolve:
        xoffset 180 yoffset 75
    voice "audio/voice/E5/YUI/02/OR/OR002.ogg"
    kaori "I mean you both just look like absolute opposites, so it's kinda weird to see you together, you know?"
    show yui heavy_coat mid_left pout at right with dissolve:
        xoffset -255 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI028.ogg"
    yui "Huh? Are we really that different?"
    show kaori heavy_coat mid worried at left with dissolve:
        xoffset 180 yoffset 75
    voice "audio/voice/E5/YUI/02/OR/OR003.ogg"
    kaori "Ah, no, I meant it in a good way! I just used to know Hikigaya from back in the day, so it just came in my mind."
    show yui heavy_coat mid_left angry at right with dissolve:
        xoffset -255 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI029.ogg"
    yui "A good way, huh..."
    hachiman "(How do you mean that in a good way? Well, it's not like she's wrong. You'd expect to see Yuigahama hang out with Hayama and the others. That much is true.)"
    hachiman "(You could say she belongs in the company of Hayama and the others... rather than with me.)"
    show kaori heavy_coat mid vhappy at left with dissolve:
        xoffset 180 yoffset 75
    voice "audio/voice/E5/YUI/02/OR/OR004.ogg"
    kaori "Um, sorry, I didn't mean anything by it! Later!"
    voice "audio/voice/E5/YUI/02/YI/YI030.ogg"
    yui "Ah, okay. Later!"
    hide kaori
    hide yui
    with dissolve
    play sound "audio/sfx/SE01/SE01_45.ogg"
    voice "audio/voice/E5/YUI/02/HA/HA023.ogg"
    hachiman "..."
    show yui heavy_coat mid_center pout at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI031.ogg"
    yui "..."
    voice "audio/voice/E5/YUI/02/YI/YI032.ogg"
    yui "A-Are we really that different...?"
    voice "audio/voice/E5/YUI/02/HA/HA024.ogg"
    hachiman "Well, it's not surprising someone might see it that way."
    voice "audio/voice/E5/YUI/02/YI/YI033.ogg"
    yui "You too, Hikki...?"
    voice "audio/voice/E5/YUI/02/HA/HA025.ogg"
    hachiman "..."
    show yui heavy_coat mid_left pout at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUI/02/YI/YI034.ogg"
    yui "..."
    stop music fadeout 1.25
    jump E5_CMM_03


label E5_YUI_03:
    scene lodgeC:
        zoom 2.0 yoffset -350
    play music "audio/bgm/BGM21.ogg"
    show hiratsuka home mid_center unimpressed at left:
        xoffset 110 yoffset 75
    show haruno sweater mid_left happy at right:
        xoffset -235 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/YUI/03/HR/HR000.ogg"
    haruno "I gotta say, Yukino-chan was really fired up at our ski match earlier."
    voice "audio/voice/E5/YUI/03/SZ/SZ000.ogg"
    hiratsuka "I bet you were just instigating again."
    show haruno sweater mid_left angry at right:
        xoffset -235 yoffset 75
    voice "audio/voice/E5/YUI/03/HR/HR001.ogg"
    haruno "That's just slander~ Right, Hayato?"
    window auto hide dissolve
    stop voice
    scene lodgeC:
        zoom 1.5 yoffset -200
    show yumiko home mid_center happy at right:
        xoffset -125 yoffset 75
    show hayama coat mid_center relieved at left:
        xoffset 153 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/YUI/03/HY/HY000.ogg"
    hayama "Don't know... We were skiing at a different spot."
    voice "audio/voice/E5/YUI/03/YM/YM000.ogg"
    yumiko "Say, doesn't Yukinoshita-san have like, really little stamina?"
    hachiman "(Miura's going out of her way to stick a -san at the end...)"
    window auto hide dissolve
    stop voice
    scene lodgeC:
        zoom 2.0 yoffset -350
    show hiratsuka home mid_center unimpressed at left:
        xoffset 110 yoffset 75
    show haruno sweater mid_center happy at right:
        xoffset -235 yoffset 75
    with dissolve
    voice "audio/voice/E5/YUI/03/HR/HR002.ogg"
    haruno "Right, right! So I wanted to see how many times she'd want to thrown down the gauntlet."
    voice "audio/voice/E5/YUI/03/SZ/SZ001.ogg"
    hiratsuka "That's exacly what instigating is..."
    show haruno sweater mid_left sad at right with dissolve:
        xoffset -235 yoffset 75
    voice "audio/voice/E5/YUI/03/HR/HR003.ogg"
    haruno "No, if she didn't want to, she could just say no, okay? Right, Gahama-chan?"
    window auto hide dissolve
    stop voice
    scene lodgeC:
        zoom 1.9 xoffset -1680 yoffset -450
    show yui home mid_left pout at center:
        xoffset 0 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/YUI/03/YI/YI000.ogg"
    yui "Huh? Ah, um..."
    voice "audio/voice/E5/YUI/03/HR/HR004.ogg"
    haruno "But she hates losing so much, she just couldn't say no~ She's cute like that..."
    scene lodgeC with dissolve
    stop voice
    hachiman "(I-I feel like leaving... Poor Yukinoshita.)"
    "What happened earlier wasn't weighing on my mind. I just wanted to be alone right now."
    stop music fadeout 1.0
    window auto hide dissolve
    scene black with fade
    scene lodgeoutC with dissolve
    play sound "audio/sfx/SE02/SE02_00.ogg"
    window auto show dissolve
    voice "audio/voice/E5/YUI/03/HA/HA000.ogg"
    hachiman "It's so cold."
    "Even so, I felt at peace. Far more than I was back there."
    "The piercing cold, the peaceful, starry sky calmed my racing mind. I felt like I just wanted to sink into the air."
    voice "audio/voice/E5/YUI/03/HA/HA001.ogg"
    hachiman "Ah, being alone is the best after all."
    hachiman "(Or so I thought, but...)"
    window auto hide dissolve
    scene lodgeoutC with dissolve:
        zoom 1.89 xoffset -1650 yoffset -450
    window auto show dissolve
    voice "audio/voice/E5/YUI/03/HY/HY001.ogg"
    hayama "Well, they were rivals since way back. It's proof of how good they get along. But you shouldn't go too far, Haruno-san. I bet there're times when it troubles Yukinoshita."
    voice "audio/voice/E5/YUI/03/YM/YM001.ogg"
    yumiko "You're so kind, Hayato!"
    voice "audio/voice/E5/YUI/03/HR/HR005.ogg"
    haruno "There you go, sticking up for her again. You haven't changed, Hayato. You never come out and say it, though."
    voice "audio/voice/E5/YUI/03/HY/HY002.ogg"
    hayama "Hahaha, I guess so..."
    voice "audio/voice/E5/YUI/03/HR/HR006.ogg"
    haruno "On the topic of never being honest..."
    voice "audio/voice/E5/YUI/03/HA/HA002.ogg"
    hachiman "T-They're annoying..."
    window auto hide dissolve
    scene black with Fade(1.0, 0.5, 1.0)
    scene lodgeLoading with Fade(1.0, 2, 1.0)
    $renpy.pause(delay=2.0, hard=True)
    show yui home mid_center pout at center:
        xoffset -345 yoffset 75 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.6 xoffset -465
            easeout 1.0 xoffset -345
    $renpy.pause(delay=3.0, hard=True)
    scene lodgeC
    show hiratsuka home mid_center unimpressed at left:
        xoffset 110 yoffset 75
    show haruno sweater mid_center happy at right:
        xoffset -235 yoffset 75
    with dissolve
    play music "audio/bgm/BGM47.ogg"
    voice "audio/voice/E5/YUI/03/HR/HR007.ogg"
    haruno "On the topic of never being honest... You're kind of like that, aren't you, Gahama-chan?"
    voice "audio/voice/E5/YUI/03/YI/YI001.ogg"
    yui "I-I might be, but Yukinon's..."
    show haruno sweater mid_center vhappy at right with dissolve:
        xoffset -235 yoffset 75
    voice "audio/voice/E5/YUI/03/HR/HR008.ogg"
    haruno "Ahaha. Yukinon-chan's like that, right?"
    voice "audio/voice/E5/YUI/03/SZ/SZ002.ogg"
    hiratsuka "...Haruno, you've had too much to drink."
    show haruno sweater mid_left angry at right with dissolve:
        xoffset -235 yoffset 75
    voice "audio/voice/E5/YUI/03/HR/HR009.ogg"
    haruno "Eh? I don't want to you hear that from you."
    window auto hide dissolve
    scene lodgeC:
        zoom 1.5 yoffset -200
    show yumiko home mid_center pout at right:
        xoffset -125 yoffset 75
    show hayama coat mid_center relieved at left:
        xoffset 153 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/YUI/03/HY/HY003.ogg"
    hayama "Well, I think Haruno should stay within reason. Right, Yui?"
    voice "audio/voice/E5/YUI/03/YI/YI002.ogg"
    yui "Ahaha... You don't have it too good either, huh, Hayato? In a lot of ways..."
    show yumiko home mid_center frown at right with dissolve:
        xoffset -125 yoffset 75
    voice "audio/voice/E5/YUI/03/YM/YM002.ogg"
    yumiko "Say, isn't she a bit too blunt? Don't you think she kinda resembles Yukinoshita? She keeps saying Hayato isn't honest which is super rude. Hayato's doing just fine."
    voice "audio/voice/E5/YUI/03/YI/YI003.ogg"
    yui "Y-Yumiko..."
    hide hayama with dissolve
    show haruno sweater mid_center happy at left with dissolve:
        xoffset 310 yoffset 75
    voice "audio/voice/E5/YUI/03/HR/HR010.ogg"
    haruno "Not everyone can be as straightforward as Yumiko-chan."
    show yumiko home mid_center blush at right with dissolve:
        xoffset -125 yoffset 75
    voice "audio/voice/E5/YUI/03/YM/YM003.ogg"
    yumiko "Huh? W-What are you saying?"
    show haruno sweater mid_center vhappy at left with dissolve:
        xoffset 310 yoffset 75
    voice "audio/voice/E5/YUI/03/HR/HR011.ogg"
    haruno "I'm just saying, you're really cute, Yumiko."
    show yumiko home mid_left blush at right with dissolve:
        xoffset -250 yoffset 75
    voice "audio/voice/E5/YUI/03/YM/YM004.ogg"
    yumiko "H-Huh!? I don't get you. Ugh, I've gotten all sweaty. I'm taking a bath."
    voice "audio/voice/E5/YUI/03/YI/YI004.ogg"
    yui "A-Ahaha..."
    scene lodgeC with dissolve:
        zoom 1.9 xoffset -1680 yoffset -450
    yui "(Straightforward... with her feelings...)"
    show haruno sweater mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/03/HR/HR012.ogg"
    haruno "Speaking of being straightforward, is there someone you really like, Gahama-chan?"
    voice "audio/voice/E5/YUI/03/YI/YI005.ogg"
    yui "Eh!? Well, um..."
    show haruno sweater mid_center sly at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/03/HR/HR013.ogg"
    haruno "Come on, come on! Spit it out."
    show yukino home mid_center unimpressed at left with dissolve:
        xoffset 7 yoffset 75
    voice "audio/voice/E5/YUI/03/YK/YK000.ogg"
    yukino "Nee-san, aren't you getting ahead of yourself?."
    show haruno sweater mid_left angry at right with dissolve:
        xoffset -235 yoffset 75
    voice "audio/voice/E5/YUI/03/HR/HR014.ogg"
    haruno "Eh? We're just having fun chatting. It has nothing to do with Yukino-chan, does it?"
    voice "audio/voice/E5/YUI/03/YK/YK001.ogg"
    yukino "Yes, I don't. But I had to say that pushing people for an answer is not right."
    show haruno sweater mid_left sly at right with dissolve:
        xoffset -235 yoffset 75
    voice "audio/voice/E5/YUI/03/HR/HR015.ogg"
    haruno "Then how about you, Yukino-chan?"
    show yukino home mid_center sad at left with dissolve:
        xoffset 7 yoffset 75
    voice "audio/voice/E5/YUI/03/YK/YK002.ogg"
    yukino "..."
    yui "(Ah... What should I do...)"
    show yukino home mid_center frown at left with dissolve:
        xoffset 7 yoffset 75
    voice "audio/voice/E5/YUI/03/YK/YK003.ogg"
    yukino "This is ridiculous..."
    hide yukino with dissolve
    show haruno sweater mid_left surprised at right with dissolve:
        xoffset -235 yoffset 75
    voice "audio/voice/E5/YUI/03/HR/HR016.ogg"
    haruno "Ah, Yukino-chan ran away~"
    yui "(Yukinon...)"
    window auto hide dissolve
    stop music fadeout 1.0
    $renpy.pause(delay=0.5, hard=True)
    scene loading_wlogo
    show yui home mid_center pout at center:
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
    hide yui
    $renpy.pause(delay=3.0, hard=True)
    scene black with Fade(1.0, 0.5, 1.0)
    scene lodgeoutC with dissolve
    play music "audio/bgm/BGM11.ogg"
    show yukino coat_shade mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/03/YK/YK004.ogg"
    yukino "Oh? You're here, too."
    voice "audio/voice/E5/YUI/03/HA/HA003.ogg"
    hachiman "...Yukinoshita? Well, I'm bad at these kind of events."
    show yukino coat_shade mid_center sad at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/03/YK/YK005.ogg"
    yukino "I hate to say it, but I agree. Nee-san's was harsher than usual with her teasing this time around..."
    voice "audio/voice/E5/YUI/03/HA/HA004.ogg"
    hachiman "I honestly don't want to be in there."
    show yukino coat_shade mid_center frown at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/03/YK/YK006.ogg"
    yukino "Seriously, isn't it embarrassing for her to mingle with a bunch of minors?"
    voice "audio/voice/E5/YUI/03/HA/HA005.ogg"
    hachiman "It looks bad for whoever's in there with her. Even if it's Yuigahama."
    show yukino coat_shade mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/03/YK/YK007.ogg"
    yukino "Yeah. Having a big social circle seems rather like a misfortune."
    show yukino coat_shade mid_center sad at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/03/YK/YK008.ogg"
    yukino "I ran out without thinking much, but... maybe I should have brought her with me."
    voice "audio/voice/E5/YUI/03/HA/HA006.ogg"
    hachiman "Well, things might've just gotten more complicated."
    voice "audio/voice/E5/YUI/03/YK/YK009.ogg"
    yukino "Yes, that's possible."
    voice "audio/voice/E5/YUI/03/HA/HA007.ogg"
    hachiman "To be honest, even for a hikikomori like myself, the hurdles are pretty high."
    show yukino coat_shade mid_center vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/03/YK/YK010.ogg"
    yukino "Oh, you seem to understand your own position well."
    voice "audio/voice/E5/YUI/03/HA/HA008.ogg"
    hachiman "...I guess."
    hachiman "(I probably would've done more bad than good for Yuigahama if I had jumped in.)"
    hachiman "(Considering Haruno's who she is and the fact Yukinoshita and Hayama's group was there, I just would've made them take more into consideration if I were to jump in.)"
    voice "audio/voice/E5/YUI/03/YK/YK011.ogg"
    yukino "But you're always solving things with methods only you can use."
    voice "audio/voice/E5/YUI/03/HA/HA009.ogg"
    hachiman "..."
    show yukino coat_shade mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/03/YK/YK012.ogg"
    yukino "And as a result of that, we're where we are now."
    voice "audio/voice/E5/YUI/03/HA/HA010.ogg"
    hachiman "All my efforts resulted in this ski trip...? What a shame."
    show yukino coat_shade mid_center vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/03/YK/YK013.ogg"
    yukino "But I'm sure that you won't be able to do things the way are forever. So..."
    voice "audio/voice/E5/YUI/03/HA/HA011.ogg"
    hachiman "So...?"
    voice "audio/voice/E5/YUI/03/YK/YK014.ogg"
    yukino "You should enjoy what you worked to bring into reality from that position."
    "I don't know if Yukinoshita knows all the little details of what happened today."
    "But perhaps Yuigahama's fuss over me is what brought her to the pickles she's in now."
    "Still, I don't know if I can say that's just because Yuigahama wanted things to happen that way."
    voice "audio/voice/E5/YUI/03/HA/HA012.ogg"
    hachiman "I really want to take everything you said just now and say right back to you..."
    show yukino coat_shade mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/03/YK/YK015.ogg"
    yukino "That figures."
    window auto hide dissolve
    stop music fadeout 1.0
    #Yui POV Again
    scene lodgeLoading with dissolve
    $renpy.pause(delay=2.0, hard=True)
    show yui home mid_center sad at center:
        xoffset -345 yoffset 75 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.6 xoffset -465
            easeout 1.0 xoffset -345
    $renpy.pause(delay=3.0, hard=True)
    scene lodgeC with dissolve
    play music "audio/bgm/BGM46.ogg"
    window auto show dissolve
    voice "audio/voice/E5/YUI/03/HR/HR017.ogg"
    haruno "Gahama-chan, you're surprisingly similiar to Yukino-chan."
    voice "audio/voice/E5/YUI/03/YI/YI006.ogg"
    yui "Eh? I-I am? I haven't really paid attention myself..."
    voice "audio/voice/E5/YUI/03/HR/HR018.ogg"
    haruno "That's what I'm talking about."
    voice "audio/voice/E5/YUI/03/YI/YI007.ogg"
    yui "..."
    window auto hide dissolve
    scene lodge2A with Fade(1.0, 0.5, 1.0)
    yui "(Hah... Haruno-san finally let me go...)"
    yui "(That's Hikki and Yukino outside... What are they talking about? Seeing them together feels... kind of... natural.)"
    yui "(I guess Yukinon matches Hikki better after all.)"
    show yumiko home near_center sad at right:
        xoffset 225 yoffset 75
    show ebina home near_center frown at left:
        xoffset -50 yoffset 75
    with dissolve
    voice "audio/voice/E5/YUI/03/YM/YM005.ogg"
    yumiko "...Yui"
    voice "audio/voice/E5/YUI/03/YI/YI008.ogg"
    yui "Ah... Yumiko."
    show yumiko home near_center vhappy at right with dissolve:
        xoffset 225 yoffset 75
    voice "audio/voice/E5/YUI/03/YM/YM006.ogg"
    yumiko "Want to take a bath? You too, Ebina."
    show ebina home near_center happy at left with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/YUI/03/EB/EB000.ogg"
    ebina "Sure, we have an open-air after all."
    voice "audio/voice/E5/YUI/03/YI/YI009.ogg"
    yui "O-Okay..."
    stop music fadeout 1.0
    scene yuiBath1 with Fade(1.0, 0.5, 1.0)
    play sound "audio/sfx/SE01/SE01_30.ogg"
    play music "audio/bgm/BGM10.ogg"
    voice "audio/voice/E5/YUI/03/YM/YM007.ogg"
    yumiko "I've never been to an outdoor hot springs outside school trips."
    voice "audio/voice/E5/YUI/03/YI/YI010.ogg"
    yui "Yumiko, aren't you the type to take baths alone?"
    voice "audio/voice/E5/YUI/03/YM/YM008.ogg"
    yumiko "Aren't outdoor hot springs the kind of thing you do with everyone?"
    voice "audio/voice/E5/YUI/03/EB/EB001.ogg"
    ebina "Yeah, yeah, preach it!"
    voice "audio/voice/E5/YUI/03/YI/YI011.ogg"
    yui "Yeah!"
    voice "audio/voice/E5/YUI/03/YM/YM009.ogg"
    yumiko "Plus, I don't know how much longer I'll be able to do this."
    voice "audio/voice/E5/YUI/03/EB/EB002.ogg"
    ebina "That's exactly why we should treasure the now! Like HayaHachi or TotsuHachi or TobeHachi...? Hm..."
    voice "audio/voice/E5/YUI/03/YM/YM010.ogg"
    yumiko "Ebina, your drool will get in the water."
    voice "audio/voice/E5/YUI/03/EB/EB003.ogg"
    ebina "It's not dripping yet!"
    voice "audio/voice/E5/YUI/03/YM/YM011.ogg"
    yumiko "Besides Ebina, why to those always include Hikio?"
    voice "audio/voice/E5/YUI/03/EB/EB004.ogg"
    ebina "Because you don't get a universally liked character like that everyday! They have to include him!"
    scene yuiBath2 with dissolve
    voice "audio/voice/E5/YUI/03/YI/YI012.ogg"
    yui "That's true."
    voice "audio/voice/E5/YUI/03/YM/YM012.ogg"
    yumiko "..."
    voice "audio/voice/E5/YUI/03/EB/EB005.ogg"
    ebina "..."
    voice "audio/voice/E5/YUI/03/YI/YI013.ogg"
    yui "Hehe..."
    stop music fadeout 1.0
    call loading_screen(0, "02_06") from yui_hotsprings1
    jump E5_CMM_04


label E5_YUI_04:
    window auto hide dissolve
    scene lodgeA:
        zoom 1.5 yoffset -200
    show tobe coat mid vhappy at left:
        xoffset 125 yoffset 75
    show hayama coat mid_center happy at right:
        xoffset -150 yoffset 75
    with dissolve
    voice "audio/voice/E5/YUI/04/TB/TB000.ogg"
    tobe "Man, we really did prety good yesterday, right? Isn't it kind of clean today? It'll be fine if we don't do any clean-up, right? Since it's the second day, we can just do something real quick and be done."
    voice "audio/voice/E5/YUI/04/HY/HY000.ogg"
    hayama "Well ,we'll do some light clean-up. We'll just roughly divide into teams and figure out the particulars then. Can everyone please pull a stick? We'll randomize the teams."
    hachiman "(Come on. That feels like such a drag for so little...)"
    scene lodgeA with Fade(0.5, 1.0, 0.5)
    "And so, the results of the divisions were way more complicated than I expected."
    show yukino home mid_center happy at left:
        xoffset -150 yoffset 75
    show yui home mid_center pout at center:
        xoffset 0 yoffset 75
    show kaori home mid happy at right:
        xoffset 0 yoffset 75
    with dissolve
    voice "audio/voice/E5/YUI/04/YK/YK000.ogg"
    yukino "So, Yuigahama-san, Hikigaya, Orimoto and me are in charge of dusting the windows and shovelling the snow."
    voice "audio/voice/E5/YUI/04/YI/YI000.ogg"
    yui "..."
    voice "audio/voice/E5/YUI/04/HA/HA000.ogg"
    hachiman "..."
    hachiman "(I-I guess it would be best to just wait for instructions.)"
    show kaori home mid sad at right with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/04/OR/OR000.ogg"
    kaori "Dusting the windows and shovelling sounds pretty tricky."
    show yukino home mid_center vhappy at left with dissolve:
        xoffset -150 yoffset 75
    voice "audio/voice/E5/YUI/04/YK/YK001.ogg"
    yukino "We did them properly yesterday, so it shouldn't be too hard today."
    voice "audio/voice/E5/YUI/04/OR/OR001.ogg"
    kaori "Yeah. I guess you're right."
    show yui home mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/04/YI/YI001.ogg"
    yui "M-Me and Yukinon will go shovel the snow then! Let's go, Yukinon!"
    show yukino home mid_center sad at left with dissolve:
        xoffset -150 yoffset 75
    voice "audio/voice/E5/YUI/04/YK/YK002.ogg"
    yukino "Huh? Okay..."
    hide yukino
    hide yui
    hide kaori
    with dissolve
    hachiman "(Hey, wait...)"
    show kaori home mid happy at center with dissolve:
        xoffset 0 yoffset 75
    hachiman "(Ah...)"
    show kaori home mid vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/04/OR/OR002.ogg"
    kaori "Are they like, dodging you, Hikigaya? Did something happen? Hilarious."
    voice "audio/voice/E5/YUI/04/HA/HA001.ogg"
    hachiman "It's really not funny. And nothing happened..."
    hachiman "(If you think they're dodging, I'd say they're rather dodging you, Orimoto. She inadvertantly dropped a bomb yesterday. Of course, Orimoto probably meant nothing by it.)"
    "And exactly because she wasn't implying anything, it appears as nothing but the truth."
    voice "audio/voice/E5/YUI/04/HA/HA002.ogg"
    hachiman "Well, let's get this done."
    show kaori home mid happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/04/OR/OR003.ogg"
    kaori "Sure thing. I'll be doing this part then."
    voice "audio/voice/E5/YUI/04/HA/HA003.ogg"
    hachiman "Sure."
    hide kaori with dissolve
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_26.ogg"
    $renpy.pause(delay=1.5, hard=True)
    hachiman "(...Hm?)"
    scene black with Fade(0.5, 1.0, 0.5)
    scene lodgeoutA
    show yukino coat mid_center angry at left:
        xoffset 25 yoffset 75
    show yui coat mid_center pout at right:
        xoffset -240 yoffset 75
    with dissolve
    voice "audio/voice/E5/YUI/04/YI/YI002.ogg"
    yui "..."
    voice "audio/voice/E5/YUI/04/YK/YK003.ogg"
    yukino "..."
    play sound "audio/sfx/SE01/SE01_26.ogg"
    hachiman "(What are those two talking about?)"
    voice "audio/voice/E5/YUI/04/OR/OR004.ogg"
    kaori "What's wrong, Hikigaya? Ah. Are you worried about those two?"
    window auto hide dissolve
    scene black with Fade(0.5, 1.0, 0.5)
    scene lodgeA
    show kaori home mid happy at center:
        xoffset 0 yoffset 75
    with dissolve
    voice "audio/voice/E5/YUI/04/HA/HA004.ogg"
    hachiman "Not really."
    voice "audio/voice/E5/YUI/04/OR/OR005.ogg"
    kaori "Hmm... So which one were you going out with?"
    play sound "audio/sfx/SE01/SE01_26.ogg"
    voice "audio/voice/E5/YUI/04/HA/HA005.ogg"
    hachiman "I told you, I'm not..."
    window auto hide dissolve
    scene black with Fade(0.5, 0.5, 0.5)
    scene lodgeoutA
    show yukino coat mid_center pout at left:
        xoffset 25 yoffset 75
    show yui coat mid_center sad at right:
        xoffset -240 yoffset 75
    with dissolve
    voice "audio/voice/E5/YUI/04/YK/YK004.ogg"
    yukino "..."
    voice "audio/voice/E5/YUI/04/YI/YI003.ogg"
    yui "..."
    hachiman "(I really wonder what they're talking about... It looks pretty heavy.)"
    stop music fadeout 1.0
    #Yui POV
    scene lodgeoutLoadingA with dissolve
    $renpy.pause(delay=2.0, hard=True)
    show yui coat mid_center sad at center:
        xoffset -345 yoffset 75 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.6 xoffset -465
            easeout 1.0 xoffset -345
    $renpy.pause(delay=3.0, hard=True)
    jump E5_YUI_05


label E5_YUI_05:
    scene lodgeoutA with dissolve
    window auto show dissolve
    voice "audio/voice/E5/YUI/05/YI/YI000.ogg"
    yui "Alright, let's get this done lickety-split!"
    show yukino coat mid_center angry at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/05/YK/YK000.ogg"
    yukino "...Yuigahama-san."
    voice "audio/voice/E5/YUI/05/YI/YI001.ogg"
    yui "Eh?"
    voice "audio/voice/E5/YUI/05/YK/YK001.ogg"
    yukino "You're acting all funny style... What's wrong?"
    voice "audio/voice/E5/YUI/05/YI/YI002.ogg"
    yui "Y-You think?"
    voice "audio/voice/E5/YUI/05/YK/YK002.ogg"
    yukino "Yeah, I do. I know it when I see it."
    play music "audio/bgm/BGM21.ogg"
    voice "audio/voice/E5/YUI/05/YI/YI003.ogg"
    yui "I see... I guess I really can't hide it from you, Yukinon..."
    voice "audio/voice/E5/YUI/05/YI/YI004.ogg"
    yui "You know, I..."
    show yukino coat mid_center vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/05/YK/YK003.ogg"
    yukino "...Go on."
    voice "audio/voice/E5/YUI/05/YI/YI005.ogg"
    yui "I've been worrying about a lot of things and... I don't know what to like, do about it, you know?"
    show yukino coat mid_center surprised at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/05/YK/YK004.ogg"
    yukino "A lot of things?"
    voice "audio/voice/E5/YUI/05/YI/YI006.ogg"
    yui "About my surroundings, and other people and... stuff."
    show yukino coat mid_center sad at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/05/YK/YK005.ogg"
    yukino "I see... a lot, hey?"
    voice "audio/voice/E5/YUI/05/YI/YI007.ogg"
    yui "L-Like... being worried about my surroundings. I guess I never really grow up, huh?"
    show yukino coat mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/05/YK/YK006.ogg"
    yukino "I wonder about that. I think you've grown."
    voice "audio/voice/E5/YUI/05/YI/YI008.ogg"
    yui "I don't know about that..."
    voice "audio/voice/E5/YUI/05/YI/YI009.ogg"
    yui "But in the end, that's just who I am..."
    show yukino coat mid_center concerned at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/05/YK/YK007.ogg"
    yukino "..."
    voice "audio/voice/E5/YUI/05/YI/YI010.ogg"
    yui "I guess... It's for the best after all."
    voice "audio/voice/E5/YUI/05/YI/YI011.ogg"
    yui "I wish I was even dumber than I am!"
    show yukino coat mid_center vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/05/YK/YK008.ogg"
    yukino "It's alright. You're plenty dumb already."
    voice "audio/voice/E5/YUI/05/YI/YI012.ogg"
    yui "Eh!? That's not a compliment!"
    voice "audio/voice/E5/YUI/05/YK/YK009.ogg"
    yukino "Is it not?"
    voice "audio/voice/E5/YUI/05/YI/YI013.ogg"
    yui "Eh?"
    show yukino coat mid_center concerned at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/05/YK/YK010.ogg"
    yukino "Me and him, we cast things away easily."
    voice "audio/voice/E5/YUI/05/YI/YI014.ogg"
    yui "..."
    show yukino coat mid_center vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/05/YK/YK011.ogg"
    yukino "So your being dumb really does help out."
    voice "audio/voice/E5/YUI/05/YI/YI015.ogg"
    yui "Yukinon..."
    voice "audio/voice/E5/YUI/05/YI/YI016.ogg"
    yui "You didn't have to say \"dumb,\" again thoguh."
    voice "audio/voice/E5/YUI/05/YK/YK012.ogg"
    yukino "Fufu..."
    voice "audio/voice/E5/YUI/05/YI/YI017.ogg"
    yui "Hehe..."
    window auto hide dissolve
    stop music fadeout 0.75
    scene loading_wlogo
    show yui coat mid_left vhappy at center:
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
    hide yui
    $renpy.pause(delay=3.0, hard=True)
    scene black with Fade(1.0, 0.5, 1.0)
    jump E5_CMM_05

label E5_YUI_06:
    voice "audio/voice/E5/YUI/06/YI/YI000.ogg"
    yui "Hikki~!"
    voice "audio/voice/E5/YUI/06/HA/HA000.ogg"
    hachiman "Hey."
    stop music fadeout 1.0
    show yui heavy_coat mid_center vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/06/YI/YI001.ogg"
    yui "Now, let's continue yesterday's training!"
    play music "audio/bgm/BGM12.ogg"
    voice "audio/voice/E5/YUI/06/HA/HA001.ogg"
    hachiman "Eh... Are you serious?"
    voice "audio/voice/E5/YUI/06/YI/YI002.ogg"
    yui "I'm super serious!"
    hachiman "(This Yukinoshita cheer her up when they were cleaning up? I don't know why, but she seems as lively as ever... Well, whatever.)"
    voice "audio/voice/E5/YUI/06/HA/HA002.ogg"
    hachiman "Alright."
    "\"Shouldn't you hang out with Hayama and the others?\", \"Hanging out with me is bound to have someone like Orimoto asking questions, you know?\""
    "...Or so I almost blurted out, but kept myself from doing."
    "It could just be me being overly self-conscious. I might be the only one still concerned about yesterday."
    "Only she herself or people she opened up to about it would know why she was feeling down after all."
    show yui heavy_coat mid_center pout at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/06/YI/YI003.ogg"
    yui "...Hikki?"
    voice "audio/voice/E5/YUI/06/HA/HA003.ogg"
    hachiman "Sorry. I was spacing out."
    show yui heavy_coat mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/06/YI/YI004.ogg"
    yui "You might get hurt if you space out!"
    voice "audio/voice/E5/YUI/06/HA/HA004.ogg"
    hachiman "You're right."
    show yui heavy_coat mid_left vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/06/YI/YI005.ogg"
    yui "Alright! Now, since yesterday we went over the basics, wanna try actually skiing today?"
    menu E5_YUI_06_MENU1:
        "You think it'll be alright?":
            voice "audio/voice/E5/YUI/06/HA/HA005.ogg"
            hachiman "You think I'll be alright?"
            show yui heavy_coat mid_left happy at center with dissolve:
                xoffset 0 yoffset 75
            voice "audio/voice/E5/YUI/06/YI/YI006.ogg"
            yui "That what will?"
            voice "audio/voice/E5/YUI/06/HA/HA006.ogg"
            hachiman "Erm, no, it's just that I'm not that confident."
            show yui heavy_coat mid_center vhappy at center with dissolve:
                xoffset 0 yoffset 75
            voice "audio/voice/E5/YUI/06/YI/YI007.ogg"
            yui "Ahaha. You'll be just fine!"
        "S-Sure.":
            "not done"
            jump E5_YUI_06_MENU1
            voice "audio/voice/E5/YUI/06/HA/HA007.ogg"
            hachiman ""
            voice "audio/voice/E5/YUI/06/YI/YI008.ogg"
            yui ""
            voice "audio/voice/E5/YUI/06/HA/HA008.ogg"
            hachiman ""
            voice "audio/voice/E5/YUI/06/YI/YI009.ogg"
            yui ""
        "I'm still a bit worried...":
            "not done"
            jump E5_YUI_06_MENU1
            voice "audio/voice/E5/YUI/06/HA/HA009.ogg"
            hachiman ""
            voice "audio/voice/E5/YUI/06/YI/YI010.ogg"
            yui ""
            voice "audio/voice/E5/YUI/06/HA/HA010.ogg"
            hachiman ""
            voice "audio/voice/E5/YUI/06/YI/YI011.ogg"
            yui ""
    show yui heavy_coat mid_left happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/06/YI/YI012.ogg"
    yui "Right, we'll start with the snowplough turn from yesterday. Try it, Hikki."
    voice "audio/voice/E5/YUI/06/HA/HA011.ogg"
    hachiman "Was it like this?"
    show yui heavy_coat mid_left vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/06/YI/YI013.ogg"
    yui "Yeah! You really got it down! Now, let's start off slow..."
    stop music fadeout 1.0
    voice "audio/voice/E5/YUI/06/HA/HA012.ogg"
    hachiman "Yuigahama! Behind you!"
    play sound "audio/sfx/SE01/SE01_46.ogg"
    show yui heavy_coat mid_left surprised at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E5/YUI/06/YI/YI014.ogg"
    yui "Huh?"
    play music "audio/bgm/BGM22.ogg"
    "There's another skier coming at her from behind with a pretty high speed. There's no time. I instantly went to shield Yuigahama. My body moved on it's own."
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_60.ogg"
    $renpy.pause(delay=0.1, hard=True)
    scene black
    voice "audio/voice/E5/YUI/06/HA/HA013.ogg"
    hachiman "Guh...!"
    voice "audio/voice/E5/YUI/06/YI/YI015.ogg"
    yui "Kyaa!"
    window auto hide dissolve
    scene slopes2A at Shake(None, 0.5, dist=100):
        zoom 2.5  xoffset -1800 yoffset -1600
    play sound "audio/sfx/SE01/SE01_58.ogg"
    $renpy.pause(delay=3.0, hard=True)
    scene slopesA with dissolve
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E5/YUI/06/XT/XT000.ogg"
    femaleSkier "That was close!"
    voice "audio/voice/E5/YUI/06/ZN/ZN000.ogg"
    maleSkier "Sorry about that!"
    voice "audio/voice/E5/YUI/06/XT/XT001.ogg"
    femaleSkier "Don't go that fast on a beginner's course! You're bothering everyone."
    voice "audio/voice/E5/YUI/06/ZN/ZN001.ogg"
    maleSkier "I'll be careful... Um, I'm, really sorry about that!"
    voice "audio/voice/E5/YUI/06/YI/YI016.ogg"
    yui "Hikki!"
    voice "audio/voice/E5/YUI/06/HA/HA014.ogg"
    hachiman "Ow..."
    stop music fadeout 0.75
    window auto hide dissolve
    scene slopesA:
        yoffset -2300 zoom 3.1 xcenter 0.2
    show yui heavy_coat near_center pout at center:
        zoom 1.5 yoffset 500
    with dissolve
    voice "audio/voice/E5/YUI/06/YI/YI017.ogg"
    yui "Are you alright, Hikki? Are you hurt?"
    voice "audio/voice/E5/YUI/06/HA/HA015.ogg"
    hachiman "Ah, no, I just tumbled."
    show yui heavy_coat near_center angry at center with dissolve:
        zoom 1.5 yoffset 500
    voice "audio/voice/E5/YUI/06/YI/YI018.ogg"
    yui "Heave... Try sitting up!"
    voice "audio/voice/E5/YUI/06/HA/HA016.ogg"
    hachiman "You're making a big deal out of it. I'm fine."
    window auto hide dissolve
    play sound "audio/sfx/SE00/SE00_25.ogg"
    scene slopesA with dissolve
    $renpy.pause(delay=1.0, hard=True)
    play sound "audio/sfx/SE01/SE01_12.ogg"
    scene yuiSkiCG with dissolve
    $renpy.pause(delay=1.0, hard=True)
    play music "audio/bgm/BGM42.ogg"
    window auto show dissolve
    "After helping me up, Yuigahama just stuck to my back. I felt the heat from her body through my back and I could hear her sobbing next to my ear."
    voice "audio/voice/E5/YUI/06/HA/HA017.ogg"
    hachiman "H-Hey..."
    hachiman "(Is she... crying?)"
    voice "audio/voice/E5/YUI/06/YI/YI019.ogg"
    yui "Hikki, you idiot..."
    voice "audio/voice/E5/YUI/06/HA/HA018.ogg"
    hachiman "Idiot!?"
    voice "audio/voice/E5/YUI/06/YI/YI020.ogg"
    yui "...Yeah. You're an idiot..."
    voice "audio/voice/E5/YUI/06/HA/HA019.ogg"
    hachiman "..."
    voice "audio/voice/E5/YUI/06/YI/YI021.ogg"
    yui "..."
    voice "audio/voice/E5/YUI/06/YI/YI022.ogg"
    yui "You really come to the rescue when push comes to shove."
    voice "audio/voice/E5/YUI/06/HA/HA020.ogg"
    hachiman "I mean, that was actually dangerous. I'm glad you didn't get hurt."
    voice "audio/voice/E5/YUI/06/YI/YI023.ogg"
    yui "Why do you always do that, Hikki?"
    voice "audio/voice/E5/YUI/06/HA/HA021.ogg"
    hachiman "...\"That\"?"
    window auto hide dissolve
    scene yuiSkiCG with dissolve:
        zoom 1.5 xoffset -700
    window auto show dissolve
    voice "audio/voice/E5/YUI/06/YI/YI024.ogg"
    yui "You always... help others first... and think about yourself later."
    voice "audio/voice/E5/YUI/06/HA/HA022.ogg"
    hachiman "I'm not that great of a person."
    voice "audio/voice/E5/YUI/06/YI/YI025.ogg"
    yui "You say that even though you know you are..."
    voice "audio/voice/E5/YUI/06/HA/HA023.ogg"
    hachiman "..."
    voice "audio/voice/E5/YUI/06/YI/YI026.ogg"
    yui "..."
    voice "audio/voice/E5/YUI/06/HA/HA024.ogg"
    hachiman "..."
    voice "audio/voice/E5/YUI/06/YI/YI027.ogg"
    yui "Thank you, Hikki."
    voice "audio/voice/E5/YUI/06/HA/HA025.ogg"
    hachiman "You're exaggerating."
    voice "audio/voice/E5/YUI/06/YI/YI028.ogg"
    yui "I wish we could stay like this forever..."
    scene yuiSkiCG with dissolve
    voice "audio/voice/E5/YUI/06/HA/HA026.ogg"
    hachiman "..."
    voice "audio/voice/E5/YUI/06/YI/YI029.ogg"
    yui "..."
    "The comfortable weight and warmth Yuigahama entrusted to my back seemed to convey more than a thousand words. I, however... couldn't give those words an answer."
    "It's doesn't matter what excuse I give. I just simply didn't have the courage."
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_12.ogg"
    scene slopesA with dissolve
    show yui heavy_coat near_center happy at center with dissolve:
        yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/YUI/06/YI/YI030.ogg"
    yui "..."
    voice "audio/voice/E5/YUI/06/HA/HA027.ogg"
    hachiman "We should get back soon."
    show yui heavy_coat near_center vhappy at center with dissolve:
        yoffset 75
    voice "audio/voice/E5/YUI/06/YI/YI031.ogg"
    yui "...Yeah."
    stop music fadeout 1.0
    window auto hide dissolve
    jump E5_CMM_06

label E5_YUI_07:
    #Yui POV
    scene black with Fade(1.0, 0.5, 0)
    scene lodgeoutLoading with dissolve
    $renpy.pause(delay=2.0, hard=True)
    show yui home mid_center happy at center:
        xoffset -345 yoffset 75 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.6 xoffset -465
            easeout 1.0 xoffset -345
    $renpy.pause(delay=3.0, hard=True)
    scene lodgeoutC
    show yukino home_shade mid_center pout at center:
        xoffset -110 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/YUI/07/YK/YK000.ogg"
    yukino "Um, Yuigahama-san... Aren't you cold like that?"
    voice "audio/voice/E5/YUI/07/YI/YI000.ogg"
    yui "Ehehe... I'll just cling to you then, Yukinon!"
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_12.ogg"
    scene lodgeoutC at truecenter:
        zoom 1.4 xoffset 75 yoffset -100
    show yukino home_shade near_center pout at center:
        xoffset -215 yoffset 75
    with dissolve
    show yukino home_shade near_center avoid at center with dissolve:
        xoffset -215 yoffset 75
    play music "audio/bgm/BGM18.ogg"
    voice "audio/voice/E5/YUI/07/YK/YK001.ogg"
    yukino "I-I guess sticking together would be fine..."
    voice "audio/voice/E5/YUI/07/YI/YI001.ogg"
    yui "Ehehe... So warm~"
    show yukino home_shade near_center blush at center with dissolve:
        xoffset -215 yoffset 75
    voice "audio/voice/E5/YUI/07/YK/YK002.ogg"
    yukino "S-So... Did something happen?"
    voice "audio/voice/E5/YUI/07/YI/YI002.ogg"
    yui "..."
    show yukino home_shade near_center angry at center with dissolve:
        xoffset -215 yoffset 75
    voice "audio/voice/E5/YUI/07/YK/YK003.ogg"
    yukino "..."
    voice "audio/voice/E5/YUI/07/YI/YI003.ogg"
    yui "Someone crashed into me at the ski slope today..."
    voice "audio/voice/E5/YUI/07/YK/YK004.ogg"
    yukino "..."
    voice "audio/voice/E5/YUI/07/YI/YI004.ogg"
    yui "And... Hikki shielded me."
    show yukino home_shade near_center vhappy at center with dissolve:
        xoffset -215 yoffset 75
    voice "audio/voice/E5/YUI/07/YK/YK005.ogg"
    yukino "I see..."
    voice "audio/voice/E5/YUI/07/YI/YI005.ogg"
    yui "Hikki's always helping other people, huh?"
    voice "audio/voice/E5/YUI/07/YI/YI006.ogg"
    yui "He helped Sable back then, too."
    voice "audio/voice/E5/YUI/07/YI/YI007.ogg"
    yui "Even if he hurts himself, he'll help..."
    show yukino home_shade near_center angry at center with dissolve:
        xoffset -215 yoffset 75
    voice "audio/voice/E5/YUI/07/YK/YK006.ogg"
    yukino "..."
    voice "audio/voice/E5/YUI/07/YI/YI008.ogg"
    yui "I was... really happy."
    voice "audio/voice/E5/YUI/07/YI/YI009.ogg"
    yui "But..."
    show yukino home_shade near_center surprised at center with dissolve:
        xoffset -215 yoffset 75
    voice "audio/voice/E5/YUI/07/YK/YK007.ogg"
    yukino "...But?"
    voice "audio/voice/E5/YUI/07/YI/YI010.ogg"
    yui "When I think how Hikki keeps putting himself after others like that... I get worried."
    voice "audio/voice/E5/YUI/07/YK/YK008.ogg"
    yukino "Yuigahama-san..."
    show yukino home_shade near_center vhappy at center with dissolve:
        xoffset -215 yoffset 75
    voice "audio/voice/E5/YUI/07/YK/YK009.ogg"
    yukino "I see... You've found it."
    voice "audio/voice/E5/YUI/07/YI/YI011.ogg"
    yui "...Huh?"
    voice "audio/voice/E5/YUI/07/YK/YK010.ogg"
    yukino "That guy has a weak defence. So that's why you'll be there with him, right?"
    voice "audio/voice/E5/YUI/07/YI/YI012.ogg"
    yui "That's why... I'll be there...?"
    voice "audio/voice/E5/YUI/07/YI/YI013.ogg"
    yui "I-I don't know..."
    voice "audio/voice/E5/YUI/07/YK/YK011.ogg"
    yukino "You do know."
    voice "audio/voice/E5/YUI/07/YI/YI014.ogg"
    yui "...Yeah."
    stop music fadeout 1.0
    window auto hide dissolve
    scene loading_wlogo
    show yui home mid_center vhappy at center:
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
    hide yui
    $renpy.pause(delay=3.0, hard=True)
    jump E5_YUI_08

label E5_YUI_08:
    scene skyC with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    hachiman "(Hah... Taking a bath alone is the best after all. Except when it's with Totsuka, but then I won't be able to settle down for other reasons rather than being alone.)"
    window auto hide dissolve
    scene black with Fade(0.5, 1.0, 0)
    scene hotspringBGB with dissolve
    play sound "audio/sfx/SE04/SE04_08.ogg"
    window auto show dissolve
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E5/YUI/08/HA/HA000.ogg"
    hachiman "...Ah."
    play music "audio/bgm/BGM40.ogg"
    voice "audio/voice/E5/YUI/08/HY/HY000.ogg"
    hayama "Yo... You're taking a bath, too, I take it?"
    voice "audio/voice/E5/YUI/08/TB/TB000.ogg"
    tobe "Oh, if it ain't Hikitani-kun!"
    voice "audio/voice/E5/YUI/08/HA/HA001.ogg"
    hachiman "R-Right..."
    hachiman "(I came at a time I thought nobody'll be here, but here they are... I miscalculated.)"
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_31.ogg"
    show hachimanBathb with dissolve
    $renpy.pause(delay=1.5, hard=True)
    voice "audio/voice/E5/YUI/08/TB/TB001.ogg"
    tobe "Ah... Taking a bath after you been tired is the best. It really feels like you're being born again~"
    voice "audio/voice/E5/YUI/08/HY/HY001.ogg"
    hayama "Haha... You sound like an old man."
    voice "audio/voice/E5/YUI/08/TB/TB002.ogg"
    tobe "Foreal? Well, we're gonna be third year high schoolers soon, so that's just how it goes. We're already old."
    hachiman "T-This is pain. And I can't chill at all... I'm thinking of leaving already...)"
    voice "audio/voice/E5/YUI/08/TB/TB003.ogg"
    tobe "Anyways, Hayato listen to this! Ah, since you're here, check it out, Hikitani!"
    hachiman "(Since I'm here? Besides, I don't really wanna hear anything...)"
    voice "audio/voice/E5/YUI/08/HY/HY002.ogg"
    hayama "What's up?"
    voice "audio/voice/E5/YUI/08/TB/TB004.ogg"
    tobe "This really ain't the time to give up on Ebina! She fell over and she had me help her up today!"
    voice "audio/voice/E5/YUI/08/HY/HY003.ogg"
    hayama "Well, it'll be a bother to others if she just stayed fallen over on the slope."
    voice "audio/voice/E5/YUI/08/TB/TB005.ogg"
    tobe "Come on, Hayato-kun, what's with the lame reaction? I looked really cool."
    scene hotspringBGB with dissolve
    hachiman "(That was just being indifferent. Besides, you still haven't given up? You're so obsse... I mean, you really like her, huh? I guess that's worth respecting anyway.)"
    hachiman "(I mean, I wonder if his type has any chance of success with Ebina to begin with...)"
    "I was annoyed for some reason. It wasn't Tobe that annoyed me."
    "It was the memories of how I couldn't answer Yuigahama's warmth and of what Orimoto said that tormented me."
    stop music fadeout 1.0
    window auto hide dissolve
    scene hachimanBathb:
        zoom 1.5 xoffset -100 yoffset -200
    window auto show dissolve
    voice "audio/voice/E5/YUI/08/HA/HA002.ogg"
    hachiman "Say, you..."
    voice "audio/voice/E5/YUI/08/TB/TB006.ogg"
    tobe "Huh?"
    voice "audio/voice/E5/YUI/08/HA/HA003.ogg"
    hachiman "Why are you so gung-ho about this? Don't you ever think you're bothering the other person?"
    play music "audio/bgm/BGM19.ogg"
    voice "audio/voice/E5/YUI/08/TB/TB007.ogg"
    tobe "No, I've thought about that, but... What was it? I get the other person's feelings are important, but then so are mine, you know?"
    voice "audio/voice/E5/YUI/08/HA/HA004.ogg"
    hachiman "Your own feelings... Even if those feelings might hurt the other person?"
    voice "audio/voice/E5/YUI/08/TB/TB008.ogg"
    tobe "Huh?"
    voice "audio/voice/E5/YUI/08/HA/HA005.ogg"
    hachiman "Sorry, It's nothing. I asked something weird."
    voice "audio/voice/E5/YUI/08/TB/TB009.ogg"
    tobe "No, no, no. Not at all! What was it? I just never saw Hikitani being serious, so it caught me off! Right, Hayato?"
    scene hachimanBathb with dissolve
    voice "audio/voice/E5/YUI/08/HY/HY004.ogg"
    hayama "I don't think he's never been serious. Hikigaya's a serious dude... and so are you, Tobe."
    voice "audio/voice/E5/YUI/08/HA/HA006.ogg"
    hachiman "Huh?"
    voice "audio/voice/E5/YUI/08/TB/TB010.ogg"
    tobe "Eh?"
    voice "audio/voice/E5/YUI/08/HY/HY005.ogg"
    hayama "So give a proper answer. Same goes for Tobe... You're different from me."
    voice "audio/voice/E5/YUI/08/HA/HA007.ogg"
    hachiman "Don't group me together with Tobe."
    voice "audio/voice/E5/YUI/08/TB/TB011.ogg"
    tobe "That was kinda rude!?"
    voice "audio/voice/E5/YUI/08/HA/HA008.ogg"
    hachiman "I'm getting out. Later..."
    voice "audio/voice/E5/YUI/08/HY/HY006.ogg"
    hayama "Hikigaya, you're not wrong."
    stop music fadeout 1.0
    stop voice
    window auto hide dissolve
    scene skyC with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "Hayama's words hung on my back. I felt that warmth and weight on my back. Getting out of the bath, a cold breeze hit me, but that warmth never faded."
    "Our standpoints and the place we belong are different. I would definitely hurt her if I just ignore that and go marching in with no regard. How can I be sure it's not wrong?"
    window auto hide dissolve
    jump E5_CMM_07_YUI

label E5_YUI_09:
    voice "audio/voice/E5/YUI/09/YM/YM000.ogg"
    yumiko "How do you feel about Yui?"
    voice "audio/voice/E5/YUI/09/HA/HA000.ogg"
    hachiman "Wha--"
    "The straight ball of a question caught me off. That's because it was already something I had been thinking about."
    voice "audio/voice/E5/YUI/09/HA/HA001.ogg"
    hachiman "It's got nothing to do with you."
    show yumiko home near_center angry at center with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/YUI/09/YM/YM001.ogg"
    yumiko "Yes, it does."
    voice "audio/voice/E5/YUI/09/HA/HA002.ogg"
    hachiman "..."
    show yumiko home near_center sad at center with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/YUI/09/YM/YM002.ogg"
    yumiko "Yui's being considerate of me and you because that's just who she is, but it's obvious what she's thinking."
    voice "audio/voice/E5/YUI/09/HA/HA003.ogg"
    hachiman "I see."
    show yumiko home near_center angry at center with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/YUI/09/YM/YM003.ogg"
    yumiko "You haven't noticed? Yui's feelings, that is."
    voice "audio/voice/E5/YUI/09/HA/HA004.ogg"
    hachiman "..."
    voice "audio/voice/E5/YUI/09/HA/HA005.ogg"
    hachiman "I have."
    show yumiko home near_center vhappy at center with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/YUI/09/YM/YM004.ogg"
    yumiko "Right."
    "I had realized. Today it reached the point I couldn't play it off anymore. Well, to be fair, I had an inkling from even before that."
    stop music fadeout 0.75
    window auto hide dissolve
    scene white with dissolve
    show yuiSkiCG with dissolve
    window auto show dissolve
    voice "audio/voice/E5/YUI/09/YI/YI000.ogg"
    yui "You always... help others first... and think about yourself later."
    voice "audio/voice/E5/YUI/09/HA/HA006.ogg"
    hachiman "I'm not that great of a person."
    window auto hide dissolve
    scene white with dissolve
    scene lodge2A
    show yumiko home near_center vhappy at center:
        xoffset -50 yoffset 75
    with dissolve
    window auto show dissolve
    play music "audio/bgm/BGM46.ogg"
    hachiman "(That's right. I don't want to save others. I want to save her. But... I was scared of admitting it.)"
    hachiman "(I was scared of how she might misunderstand, how it might flair up and I would hit rock bottom again. ...Just like in middle school.)"
    window auto hide dissolve
    scene white with dissolve
    scene yuiSkiCG with dissolve
    window auto show dissolve
    voice "audio/voice/E5/YUI/09/YI/YI001.ogg"
    yui "I wish we could stay like this forever..."
    window auto hide dissolve
    scene white with dissolve
    scene lodge2A
    show yumiko home near_center vhappy at center:
        xoffset -50 yoffset 75
    with dissolve
    window auto show dissolve
    hachiman "(But she's not like me. She became torn between us and them, and even though it might hurt her doing so, she conveyed her feelings.)"
    voice "audio/voice/E5/YUI/09/HA/HA007.ogg"
    hachiman "..."
    show yumiko home near_center sad at center with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/YUI/09/YM/YM005.ogg"
    yumiko "She really doesn't have to show some kind of weird consideration for us."
    show yumiko home near_center vhappy at center with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/YUI/09/YM/YM006.ogg"
    yumiko "Yui is Yui no matter who she goes out with. It's actually more hurtful is she holds back for our sake than not. Does she really think that's all our friendship is?"
    "Those words were really straightforward. They opened my eyes."
    "I guess it's not like they were trying to put up with Yuigahama's relationship with the Service Club. In fact, that was just an illusion I created on my own."
    voice "audio/voice/E5/YUI/09/HA/HA008.ogg"
    hachiman "You, Hayama and the others..."
    show yumiko home near_center angry at center with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/YUI/09/YM/YM007.ogg"
    yumiko "I don't know how you'll respond Hikio, but really think about it, won't you? Properly respond to Yui's feelings."
    show yumiko home near_center sad at center with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/YUI/09/YM/YM008.ogg"
    yumiko "I think sitting on the fence is... really fair."
    "I think she's eferencing and overlapping parts of her and Hayama's relationship as she speaks. That instantly came to mind from the look she was giving me. And then, I suddenly realized."
    voice "audio/voice/E5/YUI/09/HA/HA009.ogg"
    hachiman "...You're really kind."
    show yumiko home near_center surprised at center with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/YUI/09/YM/YM009.ogg"
    yumiko "Huh!?"
    voice "audio/voice/E5/YUI/09/HA/HA010.ogg"
    hachiman "You thought Yui was being taken lightly when you knew it was me on the other side of that equation."
    show yumiko home near_center unimpressed at center with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/YUI/09/YM/YM010.ogg"
    yumiko "Look, could not look down on me?"
    voice "audio/voice/E5/YUI/09/HA/HA011.ogg"
    hachiman "Look down? Maybe I am."
    show yumiko home near_center angry at center with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/YUI/09/YM/YM011.ogg"
    yumiko "Yui's serious about this and if you are, too, me and probably Ebina are support it. You've helped me before, too."
    show yumiko home near_center vhappy at center with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/YUI/09/YM/YM012.ogg"
    yumiko "So take this seriously."
    voice "audio/voice/E5/YUI/09/HA/HA012.ogg"
    hachiman "I will."
    "That was surprising. Miura was relatively quick to approve of me. And she has also been paying a surprising amount of attention. To me and Yuigahama."
    hide yumiko with dissolve
    "The snow outside continued to fall as it always had."
    "With every snowflake that danced and fell, I felt like the wall I had built from my warped self perception slowly began to crack and crumble."
    stop music fadeout 1.0
    call loading_screen(31) from yui_feelings1
    jump E6_CMM_01
