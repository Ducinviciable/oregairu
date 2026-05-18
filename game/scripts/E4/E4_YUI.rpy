label E4_YUI_01:
    #Yui's POV
    stop music fadeout 1.0
    scene black with Fade(1.0, 0.5, 1.0)
    hide yui
    hide yukino
    scene mallALoading with Fade(1.0, 2, 1.0)
    $renpy.pause(delay=2.0, hard=True)
    show yui school mid_left happy at center:
        xoffset -345 yoffset 75 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.6 xoffset -465
            easeout 1.0 xoffset -345
    $renpy.pause(delay=3.0, hard=True)
    scene mallA with dissolve
    play music "audio/bgm/BGM17.ogg"
    show yukino school mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/01/YI/YI000.ogg"
    yui "This should be aboout it for the Valentine's Event, right?"
    show yukino school mid_center vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/01/YK/YK000.ogg"
    yukino "Yeah, w've decided on a menu and we've finished the preparations without issue... All that's left is to wait for the day itself."
    voice "audio/voice/E4/YUI/01/YI/YI001.ogg"
    yui "Okay..."
    show yukino school mid_center surprised at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/01/YK/YK001.ogg"
    yukino "What's wrong? I doesn't seem like you're looking forward to it..."
    voice "audio/voice/E4/YUI/01/YI/YI002.ogg"
    yui "Huh? O-Oh, no, I am!"
    voice "audio/voice/E4/YUI/01/YK/YK002.ogg"
    yukino "You are...?"
    voice "audio/voice/E4/YUI/01/YI/YI003.ogg"
    yui "But I don't know if I'll be able to make anything, so I'm nervous... Haha..."
    show yukino school mid_center blush at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/01/YK/YK003.ogg"
    yukino "Um, I don't mean it just as a consolation, but I'll also be trying my best to help. So..."
    voice "audio/voice/E4/YUI/01/YI/YI004.ogg"
    yui "...Ah! Yukinon, look!"
    stop music fadeout 1.0
    hide yukino with dissolve
    scene yuiValentineMall with dissolve
    play music "audio/bgm/BGM42.ogg"
    voice "audio/voice/E4/YUI/01/YK/YK004.ogg"
    yukino "It's gift cake made for Valentine's."
    voice "audio/voice/E4/YUI/01/YI/YI005.ogg"
    yui "Yeah... I wonder if I'll be able to make something like this one day?"
    voice "audio/voice/E4/YUI/01/YK/YK005.ogg"
    yukino "Oh? You want to make something like this, Yuigahama-san?"
    voice "audio/voice/E4/YUI/01/YI/YI006.ogg"
    yui "Eh, I mean... Won't you think it's amazing if someone made you something like this?"
    voice "audio/voice/E4/YUI/01/YI/YI007.ogg"
    yui "Ah, but with my skill, I feel like I'd never be able to make it."
    voice "audio/voice/E4/YUI/01/YK/YK006.ogg"
    yukino "You'll be fine. You don't have to think so hard about it."
    voice "audio/voice/E4/YUI/01/YI/YI008.ogg"
    yui "Huh?"
    voice "audio/voice/E4/YUI/01/YK/YK007.ogg"
    yukino "Originally, Valentine's day was..."
    voice "audio/voice/E4/YUI/01/YI/YI009.ogg"
    yui "Huh?"
    voice "audio/voice/E4/YUI/01/YK/YK008.ogg"
    yukino "\"Saint Valentine's Day.\" in english. In other words, it's a day of Saint Valentine."
    voice "audio/voice/E4/YUI/01/YI/YI010.ogg"
    yui "Saint Valentine?"
    voice "audio/voice/E4/YUI/01/YK/YK009.ogg"
    yukino "He was a saint from the time of Ancient Rome. He became a Martyr on February 14."
    voice "audio/voice/E4/YUI/01/YK/YK010.ogg"
    yukino "The are many accounts, but it's agreed upon that he was martyred for the right for soldiers to marry. On that day, among christian disciples, it became known as the day of pledging your love to a lover."
    voice "audio/voice/E4/YUI/01/YI/YI011.ogg"
    yui "A lover's day..."
    voice "audio/voice/E4/YUI/01/YK/YK011.ogg"
    yukino "So it originally wasn't a day for women to give men chocolate or anything. That just took root as a marketing strategy in Japan."
    voice "audio/voice/E4/YUI/01/YK/YK012.ogg"
    yukino "So even if we're talking about giving something, it would be just as valid for men to give something to women, and it doesn't even have to be chocolate."
    voice "audio/voice/E4/YUI/01/YI/YI012.ogg"
    yui "Yukinon, that's sucks all the spirit out of it..."
    voice "audio/voice/E4/YUI/01/YK/YK013.ogg"
    yukino "Fufu. You're right. Sorry."
    voice "audio/voice/E4/YUI/01/YK/YK014.ogg"
    yukino "Basically, it doesn't have to be something incredible. It's a day where the important thing is conveying your affection and thanks to someone."
    voice "audio/voice/E4/YUI/01/YI/YI013.ogg"
    yui "I-Is that so...?"
    voice "audio/voice/E4/YUI/01/YK/YK015.ogg"
    yukino "Yes. That is to say, yes. You can in fact make it."
    scene mallA with dissolve
    show yukino school mid_center vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/01/YI/YI014.ogg"
    yui "I see... It felt like you were really blunt there for a moment, but I feel way better!"
    voice "audio/voice/E4/YUI/01/YK/YK016.ogg"
    yukino "Right. I think if you're able to convey you're feelings, Yuigahama-san, that would be more than enough."
    voice "audio/voice/E4/YUI/01/YI/YI015.ogg"
    yui "Thank you, Yukinon... I'll try my best!"
    voice "audio/voice/E4/YUI/01/YK/YK017.ogg"
    yukino "Of course. I'm sure you'll do just fine."
    voice "audio/voice/E4/YUI/01/YI/YI016.ogg"
    yui "Yukinon... Thank you!"
    stop music fadeout 0.5
    hide yukino with dissolve
    $renpy.pause(delay=0.5, hard=True)
    scene loading_wlogo
    show yui school mid_right happy at center:
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
    jump E4_CMM_02


label E4_YUI_02:
    scene kitchenA at truecenter:
        zoom 1.45 yoffset -15
    play music "audio/bgm/BGM40.ogg"
    show yui school mid_center happy at left:
        xoffset 200 yoffset 75
    show yukino school mid_left happy at right:
        xoffset -150 yoffset 75
    with dissolve
    voice "audio/voice/E4/YUI/02/YK/YK000.ogg"
    yukino "Are you done with your preparations, Yuigahama-san?"
    show yui school mid_right happy at left with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI000.ogg"
    yui "Yep! The butter is room temperature, and the egg yolk is separated from the whites!"
    voice "audio/voice/E4/YUI/02/YK/YK001.ogg"
    yukino "I see. Have you sieved the flower?"
    show yui school mid_right surprised at left with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI001.ogg"
    yui "Ah! I forgot to seperate the eggs!"
    voice "audio/voice/E4/YUI/02/YK/YK002.ogg"
    yukino "When you finish with that, let's get to mixing the ingredients. Ah... we should turn on the oven, too."
    show yui school mid_right happy at left with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI002.ogg"
    yui "Yep, I already did that!"
    show yukino school mid_left sad at right with dissolve:
        xoffset -150 yoffset 75
    voice "audio/voice/E4/YUI/02/YK/YK003.ogg"
    yukino "Yuigahama-san, the oven's temperature was way too high. I've adjusted it so we're going to have to wait a bit."
    show yui school mid_right sad at left with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI003.ogg"
    yui "Okay... sorry, Yukinon."
    show yukino school mid_left happy at right with dissolve:
        xoffset -150 yoffset 75
    voice "audio/voice/E4/YUI/02/YK/YK004.ogg"
    yukino "It's okay. Good thing we didn't notice when it's too late. Let's start mixing the ingredients."
    show yui school mid_right angry at left with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI004.ogg"
    yui "O-Okay!"
    hide yukino
    hide yui
    with dissolve
    show yui school mid_center angry at center with dissolve:
        xoffset 0 yoffset 75
    "Under Yukinoshita's instructions, Yuigahama started working with a serious expression."
    hachiman "(Feels like she's working harder than before... It's amusing to watch her panicked mannerism.)"
    show yui school mid_center blush at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI005.ogg"
    yui "H-Hikki, please don't stare so much. Erm... You're making me nervous."
    voice "audio/voice/E4/YUI/02/HA/HA000.ogg"
    hachiman "Ah, sorry."
    tobe "That's that! The like, sweet smell you only get with chocolate!"
    hide yui with dissolve
    "As she stole glances at the tables around her, all the while following Yukinoshita brisk orders, the cookies found their way inside the oven in the blink of an eye."
    show yui school mid_right vhappy at left with dissolve:
        xoffset 0 yoffset 75
    show yukino school mid_left happy at right with dissolve:
        xoffset -150 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI006.ogg"
    yui "All we have left is the baking now!"
    voice "audio/voice/E4/YUI/02/YK/YK005.ogg"
    yukino "Yes, so now I'll check up on the others."
    show yui school mid_right happy at left with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI007.ogg"
    yui "Okay! I got it covered!"
    show yukino school mid_center happy at right with dissolve:
        xoffset -150 yoffset 75 alpha 1
        on hide:
            easeout 0.6 xalign 1.1 alpha 0
    $renpy.pause(delay=0.5, hard=True)
    hide yukino
    $renpy.pause(delay=1, hard=True)
    voice "audio/voice/E4/YUI/02/HA/HA001.ogg"
    hachiman "Are you gonna be alright by yourself?"
    hide yui with dissolve
    show yui school mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI008.ogg"
    yui "It'll be okay! Yukino thought me everything!"
    show yui school mid_center pout at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI009.ogg"
    yui "Say, I told you not to look too much..."
    voice "audio/voice/E4/YUI/02/HA/HA002.ogg"
    hachiman "I was just a bit worried about how it was gonna go..."
    show yui school mid_left frown at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI010.ogg"
    yui "I don't know if I should be happy or not..."
    voice "audio/voice/E4/YUI/02/HA/HA003.ogg"
    hachiman "Well, I wasn't paying too much attention, so don't worry."
    show yui school mid_right frown at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI011.ogg"
    yui "I don't know if I should be happy or not about that either..."
    voice "audio/voice/E4/YUI/02/HA/HA004.ogg"
    hachiman "Which one is it? Anyways, it seems like you're better at it than before."
    show yui school mid_center vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI012.ogg"
    yui "Hehe! You think!?"
    show yui school mid_center blush at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI013.ogg"
    yui "So you were looking..."
    voice "audio/voice/E4/YUI/02/HA/HA005.ogg"
    hachiman "Well, kind of... Wait, there's no timer on that thing. Is that supposed to be like that?"
    hide yui
    $url = ["yui school mid_center surprised", "yui school mid_right surprised"]
    $multiImagePara = [0, 75, 0, 75, 1]
    call multiImage(0, False) from _call_multiImage_E4_YUI_02_2
    voice "audio/voice/E4/YUI/02/YI/YI014.ogg"
    yui "Huh? Noooo! The time!!"
    call finishmultiImage from _call_finishmultiImage_E4_YUI_02_2
    show yui school mid_right surprised at center:
        xalign 0.5 yoffset 75
        on hide:
            easeout 0.4 xalign 0.65 alpha 0
    hide yui
    voice "audio/voice/E4/YUI/02/HA/HA006.ogg"
    hachiman "H-Hey. Careful not to burn yourself."
    $renpy.pause(delay=1.5, hard=True)
    show yui school mid_center sad at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI015.ogg"
    yui "...I-It's burnt..."
    voice "audio/voice/E4/YUI/02/YI/YI016.ogg"
    yui "I can't give it to anyone like this no matter how much I let it rest..."
    voice "audio/voice/E4/YUI/02/HA/HA007.ogg"
    hachiman "I mean it's an improvement from before, right? And it's not complete charcoal."
    voice "audio/voice/E4/YUI/02/YI/YI017.ogg"
    yui "That's consolation that doesn't really do what's supposed to..."
    show yui school mid_left sad at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI018.ogg"
    menu burned_cookies_menu:
        yui "I guess nothing changes..."
        with dissolve
        "...":
            "not done"
            jump burned_cookies_menu
        "No, you're making progress":
            "not done"
            jump burned_cookies_menu
        "\"Nothing changes\"?":
            voice "audio/voice/E4/YUI/02/HA/HA012.ogg"
            hachiman "\"Nothing changes\"?"
            voice "audio/voice/E4/YUI/02/YI/YI025.ogg"
            yui "In a lot of ways, I guess."
            voice "audio/voice/E4/YUI/02/HA/HA013.ogg"
            hachiman "That's not true. Some things have changed."
            hachiman "(The Service Club fully established when she made her first cookies, too, now that I think about it...)"
            show yui school mid_center happy at center with dissolve:
                xoffset 0 yoffset 75
            voice "audio/voice/E4/YUI/02/YI/YI026.ogg"
            yui "Y-You think?"
            voice "audio/voice/E4/YUI/02/HA/HA014.ogg"
            hachiman "Well, I mean... If you compose yourself, you'll get it right next time, won't you?"
            voice "audio/voice/E4/YUI/02/YI/YI027.ogg"
            yui "I really wanted to get it right today, though..."
            stop music fadeout 0.5
    hachiman "(Did the cookies cool down already?)"
    play music "audio/bgm/BGM09.ogg"
    voice "audio/voice/E4/YUI/02/HA/HA015.ogg"
    hachiman "Ah. Can I try them?"
    show yui school mid_center surprised at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI028.ogg"
    yui "Y-You can't! They'd suck really bad!"
    hide yui with dissolve
    show yui school mid_center surprised at left:
        xoffset 200 yoffset 75
    show yukino school mid_left happy at right:
        xoffset -150 yoffset 75
    voice "audio/voice/E4/YUI/02/YK/YK006.ogg"
    yukino "Why not let him taste test them? They're not fully charcoal, so it should be fine."
    show yui school mid_right frown at left:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI029.ogg"
    yui "You're gonna call them charcoal, too, Yukinon!?"
    play sound "audio/sfx/SE01/SE01_52.ogg"
    voice "audio/voice/E4/YUI/02/HA/HA016.ogg"
    hachiman "It's edible."
    show yui school mid_center surprised at left:
        xoffset 200 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI030.ogg"
    yui "...Huh?"
    voice "audio/voice/E4/YUI/02/YK/YK007.ogg"
    yukino "Yes. If you had taken them out just a bit earlier, they would've been decent."
    play sound "audio/sfx/SE01/SE01_52.ogg"
    show yui school mid_center unimpressed at left:
        xoffset 200 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI031.ogg"
    yui "Hah, you're probably right. This smell of something burnt is killing me right now..."
    voice "audio/voice/E4/YUI/02/HA/HA017.ogg"
    hachiman "You know what actually? The bitterness is just right when you have it among all the sweetness here."
    show yukino school mid_left vhappy at right:
        xoffset -150 yoffset 75
    voice "audio/voice/E4/YUI/02/YK/YK008.ogg"
    yukino "You could say that..."
    show yui school mid_right blush at left:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/02/YI/YI032.ogg"
    yui "Like. I. Keep. Saying! Consolation like that doesn't make me happy at all!"
    stop music fadeout 1.0
    hide yui
    hide yukino
    with dissolve
    jump E4_G02_01


label E4_YUI_03:
    scene kitchenB with dissolve
    show yui school_sunset mid_center happy at right:
        xoffset -293 yoffset 75
    show yukino school_sunset mid_center happy at left:
        xoffset 15 yoffset 75
    with dissolve
    play music "audio/bgm/BGM17.ogg"
    voice "audio/voice/E4/YUI/03/HA/HA000.ogg"
    hachiman "But a ski trip? What's the point of that?"
    show yukino school_sunset mid_center pout at left with dissolve:
        xoffset 15 yoffset 75
    voice "audio/voice/E4/YUI/03/YK/YK000.ogg"
    yukino "Yeah, why does the Service Club have to participate?"
    show yui school_sunset mid_center vhappy at right with dissolve:
        xoffset -293 yoffset 75
    voice "audio/voice/E4/YUI/03/YI/YI000.ogg"
    yui "\"Why\"? It sounds fun! Why not?"
    voice "audio/voice/E4/YUI/03/HA/HA001.ogg"
    hachiman "Fun? I've never even skied before."
    hide yui
    hide yukino
    with dissolve
    show yui school_sunset mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E4/YUI/03/YI/YI001.ogg"
    yui "Ah, I can ski a little bit. So, you know... let's ski together!"
    menu ski_together:
        "Um...":
            "not done"
            jump ski_together
        "W-well, uh...":
            "not done"
            jump ski_together
        "Yeah, but...":
            voice "audio/voice/E4/YUI/03/HA/HA007.ogg"
            hachiman "Yeah, but..."
            show yui school_sunset mid_center vhappy at center with dissolve:
                xoffset 0 yoffset 75
            voice "audio/voice/E4/YUI/03/YI/YI007.ogg"
            yui "I'm sure you'll have fun if you try it! Look, I'll help you when you're having a hard time!"
            voice "audio/voice/E4/YUI/03/HA/HA008.ogg"
            hachiman "Are you just assuming I'm gonna have a hard time?"
            show yui school_sunset mid_center pout at center with dissolve:
                xoffset 0 yoffset 75
            voice "audio/voice/E4/YUI/03/YI/YI008.ogg"
            yui "Well, no, but... You won't know until you do it! That's for sure."
            voice "audio/voice/E4/YUI/03/HA/HA009.ogg"
            hachiman "Isn't that something you say when you try food?"
            show yui school_sunset mid_left pout at center with dissolve:
                xoffset 0 yoffset 75
            voice "audio/voice/E4/YUI/03/YI/YI009.ogg"
            yui "Hm? Won't know until you do... Won't know until you eat... Skiing isn't something you eat, though... Huh? T/N: in english you can quote try unquote both, but in japanese you can't."
            show yui school_sunset mid_left annoyed at center with dissolve:
                xoffset 0 yoffset 75
            voice "audio/voice/E4/YUI/03/YI/YI010.ogg"
            yui "Oh, who cares!"
            hide yui with dissolve
    show yui school_sunset mid_center sad at right:
        xoffset -293 yoffset 75
    show yukino school_sunset mid_center happy at left:
        xoffset 15 yoffset 75
    with dissolve
    voice "audio/voice/E4/YUI/03/YI/YI011.ogg"
    yui "It's just... I don't think we'll get another chance to all go skiing again. Exams are right around the corner and..."
    voice "audio/voice/E4/YUI/03/HA/HA010.ogg"
    hachiman "..."
    voice "audio/voice/E4/YUI/03/YK/YK001.ogg"
    yukino "Yeah, that is true."
    "That actually is probably true. These two spoke with the feeling of knowing that all three of us might not have the chance to do this in the future."
    "It's easy to wish for something. But that's all it is in the end, a wish. Moreover."
    voice "audio/voice/E4/YUI/03/HA/HA011.ogg"
    hachiman "Well, it's true we won't get the chance to ski together every day..."
    show yui school_sunset mid_left happy at right with dissolve:
        xoffset -293 yoffset 75
    voice "audio/voice/E4/YUI/03/YI/YI012.ogg"
    yui "I know, right? So..."
    show yukino school_sunset mid_center vhappy at left with dissolve:
        xoffset 15 yoffset 75
    voice "audio/voice/E4/YUI/03/YK/YK002.ogg"
    yukino "I can't get wholly on board with this, but... It is something that can only be done now. I'll train both of you."
    show yui school_sunset mid_left vhappy at right with dissolve:
        xoffset -293 yoffset 75
    voice "audio/voice/E4/YUI/03/YI/YI013.ogg"
    yui "Eh, really? Yay~!"
    voice "audio/voice/E4/YUI/03/HA/HA012.ogg"
    hachiman "No... you..."
    show yukino school_sunset mid_center angry at left with dissolve:
        xoffset 15 yoffset 75
    voice "audio/voice/E4/YUI/03/YK/YK003.ogg"
    yukino "Do you have a problem with that?"
    voice "audio/voice/E4/YUI/03/HA/HA013.ogg"
    hachiman "N-No... You'll be gentle right? You'll reward me with praise right? I'm a youngster after all."
    voice "audio/voice/E4/YUI/03/YI/YI014.ogg"
    yui "Ehehehehe...!"
    show yukino school_sunset mid_center vhappy at left with dissolve:
        xoffset 15 yoffset 75
    voice "audio/voice/E4/YUI/03/YK/YK004.ogg"
    yukino "Fufu..."
    window auto hide dissolve
    stop music fadeout 1.0
    jump E5_CMM_01
