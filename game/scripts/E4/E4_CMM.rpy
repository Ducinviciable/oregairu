label E4_CMM_01:
    scene hallwayB
    with Fade(1.0, 0.5, 1.0)
    play footsteps "<to 3>audio/sfx/SE00/SE00_15.ogg"
    $renpy.pause(delay=3.5, hard=False)
    play sound "audio/sfx/SE04/SE04_01.ogg"
    scene clubroomB
    with wipeleft
    $renpy.pause(delay=0.5, hard=False)
    play music "audio/bgm/BGM11.ogg"
    show yukino school_sunset far_center happy at right with dissolve:
        xoffset -325 yoffset 75
    window auto show dissolve
    voice "audio/voice/E4/CMM/01/YK/YK000.ogg"
    yukino "Good afternoon."
    show yui school_sunset far_right happy at left with dissolve:
        xoffset 170  yoffset 75
    voice "audio/voice/E4/CMM/01/YI/YI000.ogg"
    yui "Yahallo, Yukinon!"
    voice "audio/voice/E4/CMM/01/HA/HA000.ogg"
    hachiman "Sup."
    stop music
    show iroha school_sunset near_center frown at center with dissolve:
        xoffset -15 yoffset 175
        linear 0.25 yoffset 75
    voice "audio/voice/E4/CMM/01/IR/IR000.ogg"
    iroha "Senpai, you're la~te!"
    show yui school_sunset far_center surprised at left with dissolve:
        xoffset 350 yoffset 75
    voice "audio/voice/E4/CMM/01/HA/HA001.ogg"
    hachiman "And why are you here?"
    hide yui
    hide yukino
    hide iroha
    with dissolve
    $renpy.pause(delay=0.5, hard=True)
    show yui school_sunset mid_center surprised at left:
        xoffset 130 yoffset 75
    show iroha school_sunset mid_center happy at center:
        xoffset -5 yoffset 75
    show yukino school_sunset mid_center concerned at right behind iroha:
        xoffset -105 yoffset 75
    with dissolve
    play music "audio/bgm/BGM08.ogg"
    voice "audio/voice/E4/CMM/01/YK/YK001.ogg"
    yukino "I asked if she needed something, but she said she'd wait for you two and has been here since."
    hide iroha with dissolve
    show iroha school_sunset near_center unimpressed at center with dissolve:
        zoom 0.9 xoffset -15 yoffset 75
        linear 0.25 zoom 1
    voice "audio/voice/E4/CMM/01/IR/IR001.ogg"
    iroha "Yukinoshita-senpai had a super big smile when I came in, but quickly became disappointed afterwards and... she's been like that since then."
    show yukino sly with dissolve
    voice "audio/voice/E4/CMM/01/YK/YK002.ogg"
    yukino "...Isshiki-san?"
    hide yui
    hide iroha
    hide yukino
    with dissolve
    $renpy.pause(delay=0.3, hard=True)
    show iroha school_sunset mid_center surprised at left:
        xoffset 300 yoffset 75
    show yukino school_sunset mid_center sly at right:
        xoffset -230 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/01/IR/IR002.ogg"
    iroha "Ah! Y-yes! Sorry, I do have an actual reason for coming!"
    hachiman "(Ah, I know this smile! It's a 'scary Yukinon' smile!)"
    hide iroha
    hide yukino
    with dissolve
    show iroha school_sunset near_center angry at center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E4/CMM/01/IR/IR003.ogg"
    iroha "Hmmmm, senpai, not that I care, but do you like sweet things?"
    hachiman "(Sweet things... Ah, for Valentine's Day. Now that I think about it, the classroom was buzzing about something like that earlier.)"
    voice "audio/voice/E4/CMM/01/HA/HA002.ogg"
    hachiman "Chocolate, right... I think Hayama will happily eat anything."
    "I'd already gotten used to knowing Isshiki's motivations. When I tried to tactfully get to the point, Isshiki made a pouty face."
    show iroha frown with dissolve
    voice "audio/voice/E4/CMM/01/IR/IR004.ogg"
    iroha "...What's with the boring reaction?"
    show yui school_sunset mid_center pout at left:
        xoffset 130 yoffset 75
    show iroha school_sunset mid_center frown at center:
        xoffset -5 yoffset 75
    show yukino school_sunset mid_center happy behind iroha at right:
        xoffset -105 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/01/YI/YI001.ogg"
    yui "Ah, but Hayato-kun said he wouldn't accept any chocolates."
    show iroha surprised with dissolve
    voice "audio/voice/E4/CMM/01/IR/IR005.ogg"
    iroha "Eh, why's that~?"
    show yukino unimpressed with dissolve
    voice "audio/voice/E4/CMM/01/YK/YK003.ogg"
    yukino "Obviously because it'd cause trouble. In primary school, the atmosphere in the classroom the next day was rather tense."
    show yui unimpressed
    show iroha unimpressed with dissolve
    voice "audio/voice/E4/CMM/01/IR/IR006.ogg"
    iroha "Aha..."
    voice "audio/voice/E4/CMM/01/YI/YI002.ogg"
    yui "Ah. I can imagine."
    show iroha angry with dissolve
    voice "audio/voice/E4/CMM/01/IR/IR007.ogg"
    iroha "Well, I'll think about what to do about Hayama-senpai later. I've been wondering about how to make sweet things. People have their own preferences after all."
    show yukino surprised
    show yui surprised
    with dissolve
    voice "audio/voice/E4/CMM/01/YK/YK004.ogg"
    yukino "By \"how sweet\", were you intending to make it yourself?"
    voice "audio/voice/E4/CMM/01/HA/HA003.ogg"
    hachiman "That's unexpected..."
    show iroha annoyed with dissolve
    voice "audio/voice/E4/CMM/01/IR/IR008.ogg"
    iroha "Why is that? I'm good at making sweets!"
    show yukino happy
    show yui sad
    with dissolve
    voice "audio/voice/E4/CMM/01/YI/YI003.ogg"
    yui "That must be nice... I'd like to be able to do it too, but I just can't make it turn out good."
    show iroha school_sunset mid_left vhappy with dissolve:
        xoffset -35 yoffset 65
    voice "audio/voice/E4/CMM/01/IR/IR009.ogg"
    iroha "Yui-senpai, cooking is all about sincerity. What's important in cooking is kindness and your feelings. Thinking about your recipient is the shortcut to improvement!"
    show yui surprised with dissolve
    voice "audio/voice/E4/CMM/01/YI/YI004.ogg"
    yui "Oh!"
    voice "audio/voice/E4/CMM/01/IR/IR010.ogg"
    iroha "Your recipients are boys and they don't know anything about making sweets! That's why it's easy to impress."
    voice "audio/voice/E4/CMM/01/IR/IR011.ogg"
    iroha "Mass-produced at reduced cost, customized with a little extra work at the finishing touches... Like that, you'll have no problem making them for anyone you want!"
    show yui unimpressed
    show yukino unimpressed
    with dissolve
    voice "audio/voice/E4/CMM/01/HA/HA004.ogg"
    hachiman "Your feeling are completely sideways... And your kindness is completely directed at your own wallet too."
    voice "audio/voice/E4/CMM/01/YK/YK005.ogg"
    yukino "What makes it worse is that her thinking isn't wrong..."
    show iroha school_sunset mid_center blush at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/CMM/01/IR/IR012.ogg"
    iroha "I-it's fine if I'm not wrong!"
    voice "audio/voice/E4/CMM/01/YI/YI005.ogg"
    yui "A-anyway, I got a bit of an idea thanks to you. Only from the first half of it anyway."
    show iroha vhappy with dissolve
    voice "audio/voice/E4/CMM/01/IR/IR013.ogg"
    iroha "Right?!"
    voice "audio/voice/E4/CMM/01/YI/YI006.ogg"
    yui "Ah, yeah... Just from the first half, okay? Just a bit, okay?"
    stop music fadeout 1.0
    play sound "audio/sfx/SE04/SE04_13.ogg"
    $renpy.pause(delay=1, hard=False)
    #door knock sfx here
    show yui school_sunset mid_left happy at left:
        xoffset 160 yoffset 75
    show yukino happy
    show iroha happy
    with dissolve
    voice "audio/voice/E4/CMM/01/YI/YI007.ogg"
    yui "Come in!"
    #door slide sfx here
    hide yui
    hide yukino
    hide iroha
    with dissolve

    image yumiko school_sunset far_center pout flat = Flatten("yumiko school_sunset far_center pout")
    image ebina school_sunset far_center happy flat = Flatten("ebina school_sunset far_center happy")

    play sound "audio/sfx/SE04/SE04_01.ogg"
    $renpy.pause(delay=1.5, hard=False)
    show yumiko school_sunset far_center pout flat at center:
        xoffset -390 yoffset 75 alpha 0
        parallel:
            easein 0.5 xoffset -265
        parallel:
            linear 0.5 alpha 1.0
    show ebina school_sunset far_center happy flat at center:
        xoffset 185 yoffset 75 alpha 0
        parallel:
            easein 0.5 xoffset 310
        parallel:
            linear 0.5 alpha 1.0
    $renpy.pause(delay=0.5, hard=False)
    hide yumiko
    hide ebina
    show yumiko school_sunset far_center pout at center:
        xoffset -265 yoffset 75
    show ebina school_sunset far_center happy at center:
        xoffset 310 yoffset 75
    $renpy.pause(delay=0.5, hard=False)
    play music "audio/bgm/BGM38.ogg"
    voice "audio/voice/E4/CMM/01/EB/EB000.ogg"
    ebina "Hello, hello! Got a moment?"
    voice "audio/voice/E4/CMM/01/YI/YI008.ogg"
    yui "Hina... and Yumiko? What's up?"
    voice "audio/voice/E4/CMM/01/YM/YM000.ogg"
    yumiko "I don't know myself..."
    show ebina vhappy with dissolve
    voice "audio/voice/E4/CMM/01/EB/EB001.ogg"
    ebina "It's fine, Yumiko! And I'm not that good at making things myself either."
    voice "audio/voice/E4/CMM/01/YK/YK006.ogg"
    yukino "We'll hear you out. So, what can we do for you?"
    "When Yukinoshita called out, Miura, as if it was hard for her to say, pursed her lips and glanced at Isshiki."
    show yumiko school_sunset far_left happy at center with dissolve:
        xoffset -240 yoffset 75
    voice "audio/voice/E4/CMM/01/YM/YM001.ogg"
    yumiko "Why is she here?"
    hide yumiko
    hide ebina
    with dissolve
    show iroha school_sunset mid_center happy at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/CMM/01/IR/IR014.ogg"
    iroha "Isn't that, kind of like, my line?"
    hide iroha with dissolve
    show yumiko school_sunset far_center frown at left:
        xoffset 225 yoffset 75
    show ebina school_sunset far_center happy at center behind yumiko:
        xoffset 70 yoffset 75
    show yui school_sunset far_left happy at right:
        xoffset -350 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/01/YI/YI009.ogg"
    yui "Ah, umm... Do you feel like it's hard to talk about when there's too many people?"
    voice "audio/voice/E4/CMM/01/HA/HA005.ogg"
    hachiman "Then should we send Isshiki back?"
    hide yui
    hide ebina
    hide yumiko
    with dissolve
    show iroha school_sunset mid_center frown at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/CMM/01/IR/IR015.ogg"
    iroha "Eh!? Why!?"
    hachiman "(I mean, you're not really a club member... It's more strange for you to be here as if it were a given, okay?)"
    hide iroha with dissolve
    show yumiko school_sunset far_center frown at left:
        xoffset 225 yoffset 75
    show ebina school_sunset far_center happy at center behind yumiko:
        xoffset 70 yoffset 75
    show yui school_sunset far_left happy at right:
        xoffset -350 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/01/YI/YI010.ogg"
    yui "W-well... Iroha-chan's opinion could be a good reference."
    show ebina school_sunset far_left happy at center behind yumiko with dissolve:
        xoffset -35 yoffset 75
    voice "audio/voice/E4/CMM/01/EB/EB002.ogg"
    ebina "Come on, Yumiko. It's okay as long as you don't get specific, right?"
    voice "audio/voice/E4/CMM/01/YM/YM002.ogg"
    yumiko "............."
    show ebina school_sunset far_center vhappy at center behind yumiko with dissolve:
        xoffset 70 yoffset 75
    voice "audio/voice/E4/CMM/01/EB/EB003.ogg"
    ebina "I'll go with you afterwards. Come on, come on~."
    hide yui
    hide ebina
    hide yumiko
    with dissolve
    show yumiko school_sunset mid_center happy at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/CMM/01/YM/YM003.ogg"
    yumiko "...What is there to say? I want to try making handmade chocolates... um, because we'll have college entrance exams next year, and... because it'll be kind of the last time we can do this."
    show yumiko blush with dissolve
    voice "audio/voice/E4/CMM/01/YM/YM004.ogg"
    yumiko "That's why, I thought maybe I'll give it a try this one time..."
    hachiman "(Well, we won't be obligated to attend school around this time next year. So this will essentially be the last Valentine's Day of our high school years, huh?)"
    hide yumiko with dissolve
    show ebina school_sunset mid_center happy at center with dissolve:
        xoffset 65 yoffset 75
    voice "audio/voice/E4/CMM/01/EB/EB004.ogg"
    ebina "Yeah, I think handmade is good. I figured I'd learn to make some sweets alongside Yumiko."
    voice "audio/voice/E4/CMM/01/HA/HA006.ogg"
    hachiman "Huh..."
    hachiman "(Ebina-san wants to make handmade chocolates, huh? Can't say I'm not surprised...)"
    show ebina relieved1 with dissolve
    voice "audio/voice/E4/CMM/01/EB/EB005.ogg"
    ebina "Mhm, handmade is the way to go after all! Hikitani-kun should give his friend Hayato some too!"
    voice "audio/voice/E4/CMM/01/HA/HA007.ogg"
    hachiman "No, I won't... And besides, he won't accept any, right?"
    show ebina vhappy with dissolve
    voice "audio/voice/E4/CMM/01/EB/EB006.ogg"
    ebina "It's safe if it's between guys!"
    voice "audio/voice/E4/CMM/01/HA/HA008.ogg"
    hachiman "No, it isn't."
    hide ebina with dissolve
    show iroha school_sunset mid_center sad at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/CMM/01/IR/IR016.ogg"
    iroha "That's the thing. It'll be hard when he's saying he won't accept any. What should we do..."
    hide iroha with dissolve
    show yumiko school_sunset mid_center sad at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/CMM/01/YM/YM005.ogg"
    yumiko "Haa... yeah, there's that."
    hide yumiko with dissolve
    show yumiko school_sunset mid_center happy at left:
        xoffset 125 yoffset 75
    show iroha school_sunset mid_center happy at right:
        xoffset -315 yoffset 75
    with dissolve
    "When Isshiki and Miura's sighs overlapped, they raised their heads at the same time. Their gazes collided and it felt like sparks were flying. I don't like this, it's scary..."
    stop music fadeout 0.5
    hide iroha
    hide yumiko
    with dissolve
    show yukino school_sunset mid_center pout at center with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E4/CMM/01/HA/HA009.ogg"
    hachiman "I'm going to go buy something to drink."
    voice "audio/voice/E4/CMM/01/YK/YK007.ogg"
    yukino "Eh? Sure..."
    window auto hide dissolve
    stop voice
    play sound "audio/sfx/SE04/SE04_01.ogg"
    scene black with CropMove(0.5, mode="wipeleft")
    $renpy.pause(delay=0.5, hard=True)
    scene hallwayB
    show saki school_light_sunset near_right surprised at center:
        xoffset -180 yoffset 75
    with CropMove(0.5, mode="wipeleft")
    window auto show dissolve
    show saki surprised1 with dissolve
    voice "audio/voice/E4/CMM/01/SA/SA000.ogg"
    saki "Eek!"
    show saki surprised with dissolve
    voice "audio/voice/E4/CMM/01/HA/HA010.ogg"
    hachiman "Whoa!"
    hide saki with dissolve
    show saki school_light_sunset mid_right surprised at center with dissolve:
        xoffset -115 yoffset 75
    play music "audio/bgm/BGM14.ogg"
    voice "audio/voice/E4/CMM/01/HA/HA011.ogg"
    hachiman "D-Do you need anything?"
    show saki sad with dissolve
    voice "audio/voice/E4/CMM/01/SA/SA001.ogg"
    saki "Can I talk to you for a bit?"
    voice "audio/voice/E4/CMM/01/HA/HA012.ogg"
    hachiman "It'd be better if you came in. It's a little cold here."
    show saki surprised with dissolve
    voice "audio/voice/E4/CMM/01/SA/SA002.ogg"
    saki "Eh... No, over here is fine, really! I just wanted to ask Yukinoshita something."
    window auto hide dissolve
    stop voice
    play sound "audio/sfx/SE04/SE04_01.ogg"
    scene black with CropMove(0.5, mode="wiperight")
    $renpy.pause(delay=0.5, hard=True)
    scene clubroomB
    show saki school_light_sunset far_right sad at center:
        xoffset -85 yoffset 75
    with CropMove(0.5, mode="wiperight")
    window auto show dissolve
    voice "audio/voice/E4/CMM/01/YI/YI011.ogg"
    yui "Huh, Saki?"
    voice "audio/voice/E4/CMM/01/YK/YK008.ogg"
    yukino "Kawasaki-san, is there something we can do for you? Please sit down with us."
    stop voice
    hide saki with dissolve
    play sound "audio/sfx/SE01/SE01_03.ogg"
    show saki school_light_sunset mid_right sad at center with dissolve:
        xoffset -115 yoffset 75
    voice "audio/voice/E4/CMM/01/SA/SA003.ogg"
    saki "Umm... It's about chocolates..."
    "Why do I feel we'll get nothing but chocolate counseling for today? Not to mention it's all happening simultaneously."
    hide saki with dissolve
    show saki school_light_sunset mid_right sad at left:
        xoffset 70 yoffset 75
    show yumiko school_sunset mid_center happy at right:
        xoffset -130 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/01/YM/YM006.ogg"
    yumiko "What's this? You're giving someone chocolates too? Don't make me laugh."
    show saki angry with dissolve
    voice "audio/voice/E4/CMM/01/SA/SA004.ogg"
    saki "Ah?"
    show yumiko school_sunset mid_left annoyed at right with dissolve:
        xoffset -255 yoffset 75
    voice "audio/voice/E4/CMM/01/YM/YM007.ogg"
    yumiko "Ha?"
    voice "audio/voice/E4/CMM/01/SA/SA005.ogg"
    saki "Can you not group me together with the likes of you? I don't have any interest in unimportant things like that, unlike you."
    show yumiko:
        easein 0.4 xoffset -355
        easein 0.4 xoffset -255
    voice "audio/voice/E4/CMM/01/YM/YM008.ogg"
    yumiko "Ha?"
    show saki:
        easein 0.4 xoffset 170
        easein 0.4 xoffset 70
    voice "audio/voice/E4/CMM/01/SA/SA006.ogg"
    saki "Ah?"
    hachiman "(Please stop it! Be nice to each other!)"
    voice "audio/voice/E4/CMM/01/HA/HA013.ogg"
    hachiman "So, what will you do with the chocolates?"
    hide saki
    hide yumiko
    with dissolve
    show saki school_light_sunset mid_right happy at center with dissolve:
        xoffset -115 yoffset 75
    voice "audio/voice/E4/CMM/01/SA/SA007.ogg"
    saki "My little sister heard about Valentine's day at her preschool, and she wanted to make some too... Is there something even a child can make?"
    voice "audio/voice/E4/CMM/01/EB/EB007.ogg"
    ebina "But Sakisaki... weren't you pretty good with household stuff?"
    show saki unimpressed with dissolve
    voice "audio/voice/E4/CMM/01/SA/SA008.ogg"
    saki "Um... the stuff I make is kind of plain. Kids might not like it very much."
    voice "audio/voice/E4/CMM/01/YK/YK009.ogg"
    yukino "If you don't mind, could you tell us what you can usually make as a sweet?"
    show saki sad with dissolve
    voice "audio/voice/E4/CMM/01/SA/SA009.ogg"
    saki "S-Si..."
    hachiman "(Si... Simple sugar candies maybe? Kids might actually be very happy with that...)"
    voice "audio/voice/E4/CMM/01/SA/SA010.ogg"
    saki "Si... Si..."
    show saki blush with dissolve
    voice "audio/voice/E4/CMM/01/SA/SA011.ogg"
    saki "S-Simmered taro... in sweetened soy sauce."
    hachiman "(That's bland alright...)"
    hide saki with dissolve
    show yui school_sunset mid_left vhappy at left:
        xoffset 285 yoffset 75
    show yukino school_sunset mid_left happy at right:
        xoffset -165 yoffset 80
    with dissolve
    hide yui
    $url = ["yui school_sunset mid_left vhappy", "yui school_sunset mid_right vhappy"]
    $multiImagePara = [285, 75, 20, 75, 6.8]
    call multiImage(-1, False) from _call_multiImage_52
    voice "audio/voice/E4/CMM/01/YI/YI012.ogg"
    yui "I-Isn't that nice!? I can't even make any sweets at all, so I think it's amazing! Right, Yukinon!?"
    call finishmultiImage from _call_finishmultiImage_53
    hide yui
    show yui school_sunset mid_right vhappy at left:
        xoffset 20 yoffset 75
    show yukino vhappy with dissolve
    voice "audio/voice/E4/CMM/01/YK/YK010.ogg"
    yukino "Yeah. Simmered taro balls and cat toy balls kind of have a cute resemblance, don't they?"
    show yui sad with dissolve
    voice "audio/voice/E4/CMM/01/YI/YI013.ogg"
    yui "The follow-up is kind of weird?!"
    hide yui
    hide yukino
    with dissolve
    show saki school_light_sunset mid_right blush at center with dissolve:
        xoffset -115 yoffset 75
    voice "audio/voice/E4/CMM/01/HA/HA014.ogg"
    hachiman "But maybe that's fine? As long as you make it right."
    voice "audio/voice/E4/CMM/01/IR/IR017.ogg"
    iroha "Hmmmm. Well, sure. It's a little plain, but..."
    voice "audio/voice/E4/CMM/01/EB/EB008.ogg"
    ebina "Yeah, I think it's great! It's so Sakisaki-esque!"
    voice "audio/voice/E4/CMM/01/SA/SA012.ogg"
    saki "Uhhh..."
    hide saki with dissolve
    show saki school_light_sunset mid_right blush at left:
        xoffset 70 yoffset 75
    show yumiko school_sunset mid_center happy at right:
        xoffset -130 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/01/YM/YM009.ogg"
    yumiko "So you can cook."
    show saki happy with dissolve
    voice "audio/voice/E4/CMM/01/SA/SA013.ogg"
    saki "Huh? Yeah, well..."
    voice "audio/voice/E4/CMM/01/YM/YM010.ogg"
    yumiko "Hmm?"
    stop music fadeout 3.0
    "While twirling her hair with her fingertips, there seemed to be a tinge of respect in her voice."
    "Well, it does seem like Miura-san can't cook, so from her point of view, such skill as Saki's might be an object of admiration."
    hide yumiko
    hide saki
    with dissolve
    show iroha school_sunset mid_center happy at left:
        xoffset 175 yoffset 75
    show yui school_sunset mid_center vhappy at center:
        xoffset -25 yoffset 75
    show yukino school_sunset mid_left pout at right:
        xoffset -40 yoffset 80
    with dissolve
    play music "audio/bgm/BGM32.ogg"
    voice "audio/voice/E4/CMM/01/YI/YI014.ogg"
    yui "Oh! I want to know, too! If kids can do it, so can I!"
    voice "audio/voice/E4/CMM/01/IR/IR018.ogg"
    iroha "Ah, I'll try it too, just as referance!"
    hide iroha
    hide yukino
    hide yui
    with dissolve
    show saki school_light_sunset mid_right happy at center with dissolve:
        xoffset -115 yoffset 75
    voice "audio/voice/E4/CMM/01/SA/SA014.ogg"
    saki "Thanks for having me."
    hide saki with dissolve
    show yumiko school_sunset mid_center pout at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/CMM/01/YM/YM011.ogg"
    yumiko "Hang on, what about my request?"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    scene black with Fade(1.0, 1, 0)
    play sound "audio/sfx/SE04/SE04_01.ogg"
    scene clubroomB
    show iroha school_sunset mid_center happy at left:
        xoffset 175 yoffset 75
    show yui school_sunset mid_center happy at center:
        xoffset -25 yoffset 75
    show yukino school_sunset mid_left pout at right:
        xoffset -40 yoffset 80
    with Fade(0, 2.0, 1.0)
    play music "audio/bgm/BGM29.ogg"
    window auto show dissolve
    voice "audio/voice/E4/CMM/01/YK/YK011.ogg"
    yukino "Today was pretty tiring, was it not?"
    voice "audio/voice/E4/CMM/01/YI/YI015.ogg"
    yui "Yumiko, Hina, and Saki... We've had more visitors than ever, I think."
    voice "audio/voice/E4/CMM/01/IR/IR019.ogg"
    iroha "I know, right?"
    hachiman "(Iroha, you're a visitor yourself.)"
    show yukino angry with dissolve
    voice "audio/voice/E4/CMM/01/YK/YK012.ogg"
    yukino "Kawasaki-san's request isn't a problem. The problem is Miura-san's..."
    voice "audio/voice/E4/CMM/01/HA/HA015.ogg"
    hachiman "Miura's aim isn't to make chocolate, but to give chocolates to Hayama."
    show iroha angry with dissolve
    voice "audio/voice/E4/CMM/01/IR/IR020.ogg"
    iroha "Right. It seems like such a high hurdle..."
    show yui angry with dissolve
    voice "audio/voice/E4/CMM/01/YI/YI016.ogg"
    yui "But, I do kind of understand how Hayato-kun feels about it... How do I put this... He won't accept anything openly. He's got to be considerate of his surroundings."
    show iroha happy with dissolve
    voice "audio/voice/E4/CMM/01/IR/IR021.ogg"
    iroha "Ah, that's so like you, Yui-senpai. Being kind and considerate."
    show yui pout with dissolve
    voice "audio/voice/E4/CMM/01/YI/YI017.ogg"
    yui "You think so...? Ahaha... \"like me\", huh..."
    voice "audio/voice/E4/CMM/01/HA/HA016.ogg"
    hachiman "...Well, we could just create a reason to give him something. One that Hayama can accept."
    show yukino happy
    show iroha unimpressed
    with dissolve
    voice "audio/voice/E4/CMM/01/IR/IR022.ogg"
    iroha "Huh?"
    voice "audio/voice/E4/CMM/01/HA/HA017.ogg"
    hachiman "If you're forced to accept something, or if it's only natural to do so in a given situation, then it's a different story."
    show yukino angry with dissolve
    voice "audio/voice/E4/CMM/01/YK/YK013.ogg"
    yukino "In other words, we just need an excuse."
    voice "audio/voice/E4/CMM/01/HA/HA018.ogg"
    hachiman "For example, if it isn't a Valentine's Day thing, but a taste-testing thing, Hayama would eat it. Probably."
    show iroha vhappy
    show yui vhappy
    with dissolve
    voice "audio/voice/E4/CMM/01/YI/YI018.ogg"
    yui "I see! We just need to make it together! Then let's do it all together!"
    voice "audio/voice/E4/CMM/01/IR/IR023.ogg"
    iroha "That's a great idea! We can hold an event with everyone who came with a request and help each other! And have Yukinoshita-senpai teach us!"
    show yukino pout with dissolve
    voice "audio/voice/E4/CMM/01/YK/YK014.ogg"
    yukino "S-sure... I don't mind that, but..."
    show iroha school_sunset mid_left happy at left with dissolve:
        xoffset 115 yoffset 65
    # sfx here resolved
    play sound "audio/sfx/SE03/SE03_01.ogg"
    $renpy.pause(delay=2.0, hard=True)
    stop sound
    voice "audio/voice/E4/CMM/01/IR/IR024.ogg"
    iroha "Ah, vice-president? I order you to submit a proposal! For something like a cooking classroom event. ...Ha? No like I said, just stamp it first and make a notice..."
    show yui surprised
    show yukino unimpressed
    with dissolve
    voice "audio/voice/E4/CMM/01/YI/YI019.ogg"
    yui "Iroha-chan's so fast!"
    voice "audio/voice/E4/CMM/01/YK/YK015.ogg"
    yukino "...She excels at this kind of thing."
    window auto hide dissolve
    stop voice
    scene skyB
    with dissolve
    window auto show dissolve
    "Just like that, a plan I didn't really understand was launched into action. We, the Service Club, had to make preparations for it, but I guess we had no choice."
    hachiman "(To think a day would come where someone like me, who's never recieved any chocolates on Valentine's Day, would help others make them...)"
    window auto hide dissolve
    stop music fadeout 1.0
    #if yukino route it goes to a different scene, yukino live2D loading screen here.
    if totsukaTalkFlag == "yukino":
        call loading_screen(12, "32") from _call_loading_screen_7
        jump E4_G13_05
    elif totsukaTalkFlag == "iroha":
        call loading_screen(11, "32") from _call_loading_screen_8
        jump E4_G13_05
    elif totsukaTalkFlag == "saki":
        call loading_screen(16, "32") from _call_loading_screen_10
        jump E4_SAK_01
    elif totsukaTalkFlag == "haruno":
        call loading_screen(3, "32") from _call_loading_screen_9
        jump E4_CMM_02
    elif totsukaTalkFlag == "hiratsuka":
        call loading_screen(filename="32") from _call_loading_screen_34
        jump E4_CMM_02
    elif totsukaTalkFlag == "yui":
        call loading_screen(30, "32") from yui_skiFlag_loading
        jump E4_G13_05
    elif totsukaTalkFlag == "meguri":
        call loading_screen(32, "32") from _call_loading_screen_38
        jump E4_CMM_02

label E4_CMM_02:
    #outside crowd sfx
    scene skyA with Fade(1.0, 1.0, 1.0)
    play ambient "audio/sfx/SE05/SE05_01L.ogg"
    window auto show dissolve
    "A few days after since the consultations, and the day of the event had finally arrived."
    "The community center near the station echoed with students' voices and the sounds of busy footsteps running around."
    "It raised our anticipation as well as our tension slightly, and our pace quickened as we came to help."
    window auto hide dissolve
    #stop crowd sfx
    stop ambient fadeout 3
    scene kitchenA
    show iroha school far_left happy at center:
        xoffset -25 yoffset 80
    with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM07.ogg"
    window auto show dissolve
    voice "audio/voice/E4/CMM/02/IR/IR000.ogg"
    iroha "Uhm, could you please fold those empty box and put them in the back? And after that, it would also be great if you could prepare the printouts for the Kaihin Sogo students..."
    hachiman "(Oh. It looks like she's doing a good job. She might just be giving out orders, but it's a sign that the chain of command is working properly. Umu, umu, nicely done, Irohasu.)"
    hide iroha with dissolve
    show iroha school mid_left happy at center with dissolve:
        xoffset -35 yoffset 65
    voice "audio/voice/E4/CMM/02/HA/HA000.ogg"
    hachiman "Good work."
    show iroha school mid_center vhappy at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/CMM/02/IR/IR001.ogg"
    iroha "Ah, senpai-- you too!"
    hide iroha
    with dissolve
    show iroha school mid_center vhappy at left:
        xoffset 175 yoffset 75
    show yui school mid_left happy at center behind iroha:
        xoffset 10 yoffset 75
    show yukino school mid_left happy at right:
        xoffset -40 yoffset 80
    with dissolve
    voice "audio/voice/E4/CMM/02/YK/YK000.ogg"
    yukino "Hello, Isshiki-san."
    show yui vhappy with dissolve
    voice "audio/voice/E4/CMM/02/YI/YI000.ogg"
    yui "Yahallo--! Looks like things are going well!"
    voice "audio/voice/E4/CMM/02/IR/IR002.ogg"
    iroha "Thank you very much for coming today, Yukino-senpai and Yui-senpai!"
    show yukino vhappy with dissolve
    voice "audio/voice/E4/CMM/02/YK/YK001.ogg"
    yukino "Thank you for having us. We'll do our best."
    show yui happy with dissolve
    voice "audio/voice/E4/CMM/02/YI/YI001.ogg"
    yui "Uhm, is there anything we could do to help?"
    show iroha happy with dissolve
    voice "audio/voice/E4/CMM/02/IR/IR003.ogg"
    iroha "Alright, then... could you please check the kitchenwares and prepare them? Please distribute a set to each table."
    voice "audio/voice/E4/CMM/02/YK/YK002.ogg"
    yukino "Yes. We'll handle it."
    voice "audio/voice/E4/CMM/02/YI/YI002.ogg"
    yui "Okay~! Uhm, this is the kitchenware, right?"
    show yukino school mid_left angry_flat with dissolve:
        yoffset 80
        on hide:
            parallel:
                    linear 0.5 alpha 0
            parallel:
                    linear 0.5 xoffset 40
    voice "audio/voice/E4/CMM/02/YK/YK003.ogg"
    yukino "Yuigahama-san, don't just touch them like that. Wash your hands first."
    show yui school mid_right surprised flat behind iroha at center with dissolve:
        xoffset -110
        on hide:
            parallel:
                    linear 0.5 alpha 0
            parallel:
                    linear 0.5 xoffset 10
    voice "audio/voice/E4/CMM/02/YI/YI003.ogg"
    yui "Ah, right!"
    hide yui
    hide yukino
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E4/CMM/02/HA/HA001.ogg"
    hachiman "How about me?"
    hide iroha with dissolve
    show iroha school mid_center happy at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/CMM/02/IR/IR004.ogg"
    iroha "Ah, please put this poster out. It would be great if you could put it up somewhere it stands out."
    voice "audio/voice/E4/CMM/02/HA/HA002.ogg"
    hachiman "Poster, huh... Roger that."
    hide iroha with dissolve
    play sound "audio/sfx/SE01/SE01_07.ogg"
    hachiman "(\"We welcome beginners! No requirements! You'll feel right at home! Experience the cooking process firsthand and learn how to make chocolates independantly!\"...)"
    voice "audio/voice/E4/CMM/02/HA/HA003.ogg"
    hachiman "...Man, this looks shady."
    voice "audio/voice/E4/CMM/02/OR/OR000.ogg"
    mystery "Ah, Hikigaya! I knew you'd come!"
    voice "audio/voice/E4/CMM/02/HA/HA004.ogg"
    show kaori school mid happy at center with dissolve:
        xoffset -25 yoffset 75
    hachiman "O-Oh."
    hachiman "(Right. It's not strange to see Orimoto here because she's from Kaihin Sogo High.)"
    show iroha school mid_left happy at right with dissolve:
        xoffset -190 yoffset 65
    voice "audio/voice/E4/CMM/02/IR/IR005.ogg"
    iroha "Ah, Orimoto-san will you please help Yukinoshita-senpai and the others prepare?"
    show kaori school mid vhappy_flat with dissolve:
        on hide:
            parallel:
                    linear 0.5 alpha 0
            parallel:
                    linear 0.5 xoffset -150
    voice "audio/voice/E4/CMM/02/OR/OR001.ogg"
    kaori "Yeees, roger that. See ya'~!"
    hide kaori
    $renpy.pause(delay=0.5, hard=True)
    hide iroha with dissolve
    show iroha school mid_center happy at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/CMM/02/IR/IR006.ogg"
    iroha "After you're done with that poster, senpai, please take care of these boxes."
    play sound "audio/sfx/SE04/SE04_08.ogg"
    $renpy.pause(delay=1.0, hard=False)
    show iroha surprised with dissolve
    play ambient "audio/sfx/SE05/SE05_02L.ogg"
    voice "audio/voice/E4/CMM/02/IR/IR007.ogg"
    iroha "It looks like those who'll be participating have gathered! We need to hurry..."
    show iroha happy with dissolve
    voice "audio/voice/E4/CMM/02/IR/IR008.ogg"
    iroha "Senpai, I'm counting on you~"
    hide iroha with dissolve
    hachiman "(Well, time to get to work...)"
    window auto hide dissolve
    stop ambient fadeout 1.0 #Check if this stops in saki route
    stop music fadeout 1.0
    scene kitchenA
    with Fade(1.5, 2.0, 1.5)
    if totsukaTalkFlag == "saki":
        jump E4_SAK_02
    play music "audio/bgm/BGM41.ogg"
    window auto show dissolve
    hachiman "(Haa, the empty boxes are mostly cleared out, and I'm starting to feel like one myself.)"
    voice "audio/voice/E4/CMM/02/HA/HA005.ogg"
    hachiman "Well, it looks like the participants have gathered as well..."

    image tobe school far happy flat = Flatten("tobe school far happy")
    image hayama school far_center happy flat = Flatten("hayama school far_center happy")
    image hayamaFlat = Flatten("hayama school far_center vhappy")

    show iroha school far_center happy at right with Dissolve(0.5):
        xoffset -275 yoffset 75
    show tobe school far happy flat at center:
        xoffset -145 yoffset 75 alpha 0
        parallel:
            linear 0.3 alpha 1.0
        parallel:
            easein 0.3 xoffset 45
        on hide:
            parallel:
                linear 0.3 alpha 0
            parallel:
                easein 0.3 xoffset -145
    show hayama school far_center flat happy at left:
        xoffset 5 yoffset 65 alpha 0
        parallel:
            linear 0.3 alpha 1.0
        parallel:
            easein 0.3 xoffset 105
    $renpy.pause(delay=0.3, hard=True)
    voice "audio/voice/E4/CMM/02/TB/TB000.ogg"
    tobe "Irohasu, whad'we do now?"
    hide iroha
    $url = ["iroha school far_center pout", "iroha school far_left blush"]
    $multiImagePara = [-275, 75, -270, 80, 1.8]
    call multiImage(1, False) from _call_multiImage_53
    voice "audio/voice/E4/CMM/02/IR/IR009.ogg"
    iroha "Ah, good work. Ah! Sorry for asking you to help as well, Hayama-senpai! You were a super life-saver! Thank you very much!"
    call finishmultiImage from _call_finishmultiImage_54
    show iroha school far_left blush at right:
        xoffset -270 yoffset 80
    hachiman "(That is not subtle, Irohasu.)"
    hide hayama
    show hayamaFlat at left:
        xoffset 105 yoffset 65
        on hide:
            parallel:
                linear 0.3 alpha 0
            parallel:
                easein 0.3 xoffset 5
    voice "audio/voice/E4/CMM/02/HY/HY000.ogg"
    hayama "I haven't done anything special though. Okay, Tobe, let's help with the rest of the preparations."
    voice "audio/voice/E4/CMM/02/TB/TB001.ogg"
    tobe "'Kay"
    hide tobe
    hide hayamaFlat
    hide iroha
    image irohaFlat = Flatten("iroha school far_left vhappy")
    show irohaFlat at right:
        xoffset -270 yoffset 80
        on hide:
            parallel:
                linear 0.5 alpha 0
            parallel:
                linear 0.5 xoffset -370
    voice "audio/voice/E4/CMM/02/IR/IR010.ogg"
    iroha "Ah, Hayama-senpai! I'll help prepare over there too!"
    hide irohaFlat
    $renpy.pause(delay=1, hard=False)
    show yumiko school mid_center happy behind ebina at left:
        xoffset -5 yoffset 75
    show ebina school mid_center happy at center:
        xoffset 65 yoffset 75
    show yukino school mid_left happy at right:
        xoffset -40 yoffset 80
    with dissolve
    hide ebina
    $url = ["ebina school mid_center happy", "ebina school mid_center relieved2"]
    $multiImagePara = [65, 75, 0, 0, 1.9]
    call multiImage() from _call_multiImage_54
    voice "audio/voice/E4/CMM/02/EB/EB000.ogg"
    ebina "Hello hello! This image of boys sweating together is great."
    call finishmultiImage from _call_finishmultiImage_55
    show ebina school mid_center relieved2 zorder 1 at center:
        xoffset 65 yoffset 75
    hide yumiko
    $url = ["yumiko school mid_center unimpressed", "yumiko school mid_center blush"]
    $multiImagePara = [-5, 75, 0, 0, 2.31]
    call multiImage(-1) from _call_multiImage_55
    voice "audio/voice/E4/CMM/02/YM/YM000.ogg"
    yumiko "... Ebina, get a hold of yourself. And, well, um..."
    call finishmultiImage from _call_finishmultiImage_56
    show yumiko school mid_center vhappy behind ebina at left:
        xoffset -5 yoffset 75
    with dissolve
    show yukino vhappy with dissolve
    voice "audio/voice/E4/CMM/02/YK/YK004.ogg"
    yukino "Yes, let's do our best."
    show ebina mid_left vhappy with dissolve:
        xoffset -70 yoffset 70
    voice "audio/voice/E4/CMM/02/EB/EB001.ogg"
    ebina "Yep! Let's do our best, Yumiko!"
    show yumiko mid_left blush with dissolve:
        xoffset 115 yoffset 75
    voice "audio/voice/E4/CMM/02/YM/YM001.ogg"
    yumiko "............."
    hide yumiko
    hide ebina
    hide yukino
    with dissolve
    play sound "audio/sfx/SE04/SE04_08.ogg"
    $renpy.pause(delay=1.5,hard=False)
    voice "audio/voice/E4/CMM/02/KE/KE000.ogg"
    mystery "Ah, it's Haa-chan!"
    voice "audio/voice/E4/CMM/02/SA/SA000.ogg"
    mystery "Ah, Kei-chan, don't run!"
    show saki school far_right pout at center:
        xoffset -325 yoffset 75
    show keika home far happy at center:
        xoffset 245 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/02/HA/HA006.ogg"
    hachiman "Ah, it's Kei-chan."
    hide saki
    hide keika
    with dissolve
    show keika home near happy at center with dissolve:
        yoffset 75
    show keika happy1 with dissolve
    voice "audio/voice/E4/CMM/02/KE/KE001.ogg"
    keika "Poke."
    show keika home near happy at center
    voice "audio/voice/E4/CMM/02/HA/HA007.ogg"
    hachiman "Oh, don't poke me. That's dangerous. Kids that poke will end up turning into jelly."
    show keika vhappy2 with dissolve
    voice "audio/voice/E4/CMM/02/KE/KE002.ogg"
    keika "Ahahaha!"
    hide keika with dissolve
    show saki school mid_right pout at left:
        xoffset -55 yoffset 75
    show keika home mid at center:
        xoffset -25 yoffset 75
    show yukino school mid_left pout at right:
        xoffset -40 yoffset 80
    with dissolve
    voice "audio/voice/E4/CMM/02/YK/YK005.ogg"
    yukino "I thought this before too, but you're unexpectedly good with children."
    voice "audio/voice/E4/CMM/02/HA/HA008.ogg"
    hachiman "Well, little kids are like animals after all. I'm liked by things that aren't human."
    show yukino unimpressed with dissolve
    voice "audio/voice/E4/CMM/02/YK/YK006.ogg"
    yukino "That's not something you can say proudly..."
    voice "audio/voice/E4/CMM/02/SA/SA001.ogg"
    saki "Ah, um... Thanks for today."#Ah, um... Thanks for today.
    show yukino happy with dissolve
    voice "audio/voice/E4/CMM/02/YK/YK007.ogg"
    yukino "Yes, thanks for working with me as well. I'm sure we'll be able to make something good."
    hide saki
    $url = ["saki school mid_right pout1", "saki school mid_right vhappy"]
    $multiImagePara = [-55, 75, 0, 0, 1.5]
    call multiImage(-1) from _call_multiImage_56
    voice "audio/voice/E4/CMM/02/SA/SA002.ogg"
    saki "Y-yeah... Then, Kei-chan, let's start preparing over there."
    call finishmultiImage from _call_finishmultiImage_57
    show saki school mid_right pout at left:
        xoffset -55 yoffset 75
    show keika vhappy with dissolve
    voice "audio/voice/E4/CMM/02/KE/KE003.ogg"
    keika "Sure! See ya, Haa-chan!"
    hide saki
    hide keika
    hide yukino
    with dissolve
    play sound "audio/sfx/SE04/SE04_08.ogg"
    $renpy.pause(delay=0.5,hard=False)
    show meguri school far happy at center:
        xoffset -220 yoffset 75
    show haruno sweater far_center happy at center:
        xoffset 225 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/02/HR/HR000.ogg"
    haruno "Hyahallo! Wow, you're all at it!"
    voice "audio/voice/E4/CMM/02/MG/MG000.ogg"
    meguri "Good afternoon! I came after being called over."
    hide meguri
    hide haruno
    with dissolve
    show yukino school mid_center angry at left:
        xoffset 25 yoffset 75
    show haruno sweater mid_left happy at center:
        xoffset 390 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/02/YK/YK008.ogg"
    yukino "Nee-san... What did you come here for?"
    hide haruno
    $url = ["haruno sweater mid_left happy", "haruno sweater mid_center happy"]
    $multiImagePara = [390, 75, 420, 75, 4.0]
    call multiImage(0, False) from _call_multiImage_57
    voice "audio/voice/E4/CMM/02/HR/HR001.ogg"
    haruno "Eh? Meguri and I were asked to be helpers. Right, Iroha-chan?"
    call finishmultiImage from _call_finishmultiImage_58
    hide yukino
    with dissolve
    show iroha school far_left vhappy at right with dissolve:
        xoffset -205 yoffset 80
    voice "audio/voice/E4/CMM/02/IR/IR011.ogg"
    iroha "Yes. After I asked Yukinoshita-senpai to coach us, I thought it'd be hard to do by herself."
    hide iroha with dissolve
    show yukino school mid_center concerned at center with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E4/CMM/02/YK/YK009.ogg"
    yukino "I'd be fine by myself though..."
    voice "audio/voice/E4/CMM/02/HA/HA009.ogg"
    hachiman "Well, nevermind your teaching methods, your cooking does taste really good."
    hide yukino
    $url = ["yukino school mid_center surprised", "yukino school mid_center avoid"]
    $multiImagePara = [-105, 75, 0, 0, 1.0]
    call multiImage() from _call_multiImage_58
    voice "audio/voice/E4/CMM/02/YK/YK010.ogg"
    yukino "... It's nothing special though."
    call finishmultiImage from _call_finishmultiImage_59
    show yukino school mid_center avoid at center:
        xoffset -105 yoffset 75
    "Maybe it's because she didn't expect a compliment, she was speechless for a moment, but quickly turned her face away. Nah, it's not like I just complimented you anyway. I'm saying the way you teach "
    "is terrible."
    hide yukino with dissolve
    #sort of tricky animation here 6:49. Fix timescale

    show yukino school mid_center surprised at center:
        xoffset -340 yoffset 75
        parallel:
            0.4
            easein 0.025 yoffset 70 xoffset -342
            easein 0.025 yoffset 80 xoffset -343
            easein 0.025 yoffset 75 xoffset -345
            easein 0.025 yoffset 70 xoffset -342
            easein 0.025 yoffset 80 xoffset -343
            easein 0.025 yoffset 75 xoffset -345
    show yui school mid_left vhappy behind yukino at center:
        xoffset 250 yoffset 75
        parallel:
            easein 0.4 xoffset -100
            easein 0.5 xoffset 250
    with dissolve
    $renpy.pause(delay=0.75, hard=True)
    hide yukino
    hide yui
    show yukino school mid_center surprised at center:
        xoffset -345 yoffset 75
    show yui school mid_left vhappy behind yukino at center:
        xoffset 250 yoffset 75
    voice "audio/voice/E4/CMM/02/YI/YI004.ogg"
    yui "But I'm looking forward to being taught by Yukinon!"
    show yukino blush with dissolve
    "When Yuigahama clung to Yukinoshita, her mood improved a bit and she cleared her throat like she was embarassed."
    "... Well, if there's someone that needs teaching other than by Yukinoshita, it was Yuigahama, and that's not really anything bad."#Check this line
    #^⋯まぁ、雪ノ下の他にも指導できる人間がいるなら、由比ヶ浜に割けるキャパシティも増えるし、別に悪いことではない
    hide yukino
    hide yui
    with dissolve
    show haruno sweater far_center happy at center with dissolve:
        xoffset -15 yoffset 75
    hachiman "(... But Haruno-san being here was kind of unsettling, and there's a lot of people here too, so this event looks like it's going to be pretty troublesome. Now I kind of want to go home.)"
    hide haruno with dissolve
    show totsuka athletic mid_center sad at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E4/CMM/02/SI/SI000.ogg"
    totsuka "Hachiman, was setting this up really difficult?"
    hachiman "(T-Totsuka...!)"
    voice "audio/voice/E4/CMM/02/HA/HA010.ogg"
    hachiman "N-no, not really. So you came."
    show totsuka vhappy with dissolve
    voice "audio/voice/E4/CMM/02/SI/SI001.ogg"
    totsuka "Yeah, I did!"
    hachiman "(I'm glad I didn't go home...!)"
    window auto hide dissolve
    stop music fadeout 1.0
    #yukinoroute goes to this scene.. not sure what routes follow this but its named as common
    jump E4_CMM_03

    #Possibly different route here. Files are in order though.
    hachiman "(さてと、ポスターも貼り終えたし、戻るか⋯⋯)"
    voice "audio/voice/E4/CMM/02/TB/TB002.ogg"
    tobe "あんれー、ヒキタニくんだべ！"
    voice "audio/voice/E4/CMM/02/HA/HA011.ogg"
    hachiman "⋯⋯お、おう"
    voice "audio/voice/E4/CMM/02/HY/HY001.ogg"
    hayama "またいろはに手伝わされてるのか？ 良かったら俺たちも手伝うけど"
    voice "audio/voice/E4/CMM/02/HA/HA012.ogg"
    hachiman "いや、こっちはだいたい終わってるから⋯⋯"
    voice "audio/voice/E4/CMM/02/IR/IR012.ogg"
    iroha "あ！ 葉山先輩！ 今日は来てくださってありがとうございます！"
    hachiman "(葉山が来たって何でわかっちゃったの？ ひょっとしてエスパー？ いろはすおそろしい子)"
    voice "audio/voice/E4/CMM/02/IR/IR013.ogg"
    iroha "ここは先輩と戸部先輩に任せていいんで、とりあえず会場行きましょうか！"
    voice "audio/voice/E4/CMM/02/HA/HA013.ogg"
    hachiman "ちょっとー？"
    voice "audio/voice/E4/CMM/02/TB/TB003.ogg"
    tobe "いろはすー？"
    voice "audio/voice/E4/CMM/02/HA/HA014.ogg"
    hachiman "一色、ポスター貼ってきたぞ"
    voice "audio/voice/E4/CMM/02/IR/IR014.ogg"
    iroha "あ、お疲れ様です。意外と時間かかりましたねー。遅くなるなら遅くなるで、一本連絡入れるくらいしてほしかったんですけど"
    hachiman "(お礼言われるどころかダメ出しされてしまった⋯⋯)"
    voice "audio/voice/E4/CMM/02/HA/HA015.ogg"
    hachiman "なんなの俺の奥さんなの？"
    voice "audio/voice/E4/CMM/02/IR/IR015.ogg"
    iroha "はぁ？ いや、普通に働くうえで当たり前のこ、はっ！"
    voice "audio/voice/E4/CMM/02/IR/IR016.ogg"
    iroha "もしかして今口説いてましたか共同作業をきっかけに共同生活を意識させるその手腕には感心しましたがごめんなさいいいからあそこの段ボール運んでください"
    voice "audio/voice/E4/CMM/02/HA/HA016.ogg"
    hachiman "あ、うん、はい、もういいです。仕事するね⋯⋯"
    hachiman "(ふう⋯⋯だいたい準備もこんなとこか⋯⋯)"

label E4_CMM_03:
    scene kitchenA
    show yumiko school mid_center angry at left:
        xoffset 125 yoffset 75
    show ebina school mid_center happy at right:
        xoffset -120 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    play ambient "audio/sfx/SE05/SE05_09L.ogg"
    play music "audio/bgm/BGM09.ogg"
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E4/CMM/03/YM/YM000.ogg"
    yumiko "First, you crush the chocolate and heat them... Also, add sugar to the flour... uhm..."
    voice "audio/voice/E4/CMM/03/EB/EB000.ogg"
    ebina "Yumiko, listen. You shouldn't worry about your chocolate too much. Yukinoshita-san even prepared us a easy-to-understand recipe book.
        Yukinoshita-san sure is careful about these kinds of things."
    show yumiko school mid_left sad at left with dissolve:
        xoffset 240 yoffset 75
    voice "audio/voice/E4/CMM/03/YM/YM001.ogg"
    yumiko "I, I'm not that worried!"
    "Yukinoshita preprared a carefully selected menu and turned them into booklets. According to Yuigahama, the booklets were easier to understand than the previous one, but unfortunately, for me, I don't "
    "see the differences at all."
    hide ebina
    hide yumiko
    with dissolve
    show tobe school far happy at left:
        xoffset 290 yoffset 75
    show iroha school far_center happy at center:
        xoffset -30 yoffset 75
    with dissolve
    hide tobe
    $url = ["tobe school far happy", "tobe school far happy"]
    $multiImagePara = [290, 75, -205, 75, 2.3]
    call setImagesFlat from _call_setImagesFlat_1
    show mood1 at left:
        xoffset multiImagePara[0] yoffset multiImagePara[1]
    with dissolve
    show mood1 at left:
        parallel:
            multiImagePara[4]
            linear 0.3 alpha 0
    show mood2 at right:
        xoffset multiImagePara[2] yoffset multiImagePara[3] alpha 0
        parallel:
            multiImagePara[4]
            linear 0.3 alpha 1.0
    voice "audio/voice/E4/CMM/03/TB/TB000.ogg"
    tobe "For real, those chocos look really delicious! I want to eat chocobit of it~"
    call finishmultiImage from _call_finishmultiImage_60
    show tobe school far happy at right:
        xoffset -205 yoffset 75
    show iroha unimpressed with dissolve
    voice "audio/voice/E4/CMM/03/IR/IR000.ogg"
    iroha "Ha?"
    voice "audio/voice/E4/CMM/03/TB/TB001.ogg"
    tobe "By the way..."
    hide tobe
    hide iroha
    with dissolve
    "When Tobe looked around, he beckoned a little bit."
    window auto hide dissolve
    scene kitchenA at truecenter:
        zoom 1.45 xoffset -2.5 yoffset -12.5
    show yukino school mid_center pout at left:
        xoffset -105 yoffset 75
    show yui school mid_center happy at center:
        xoffset -25 yoffset 75
    show tobe school mid happy at right:
        xoffset 125 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E4/CMM/03/YI/YI000.ogg"
    yui "What is it? A secret talk?"
    voice "audio/voice/E4/CMM/03/YK/YK000.ogg"
    yukino "I can't really let go right now though..."
    voice "audio/voice/E4/CMM/03/TB/TB002.ogg"
    tobe "Ah, nah, you know? Today you guys are making chocolates? And maybe I could get some if I did something to you guys, or so, that's what I think... isn't there any choco for me?"
    show yukino unimpressed
    show yui unimpressed
    with dissolve
    voice "audio/voice/E4/CMM/03/MI/MIX000.ogg"
    yukandyuiandiro ".............."
    voice "audio/voice/E4/CMM/03/HA/HA000.ogg"
    hachiman "...Haaaa, I see. So, for you to get chocolates, you are appealing them, yes...?"
    hide yui
    hide tobe
    hide yukino
    with dissolve
    show tobe school near happy at center with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E4/CMM/03/TB/TB003.ogg"
    tobe "Uh-huh! Exactly!"
    hide tobe with dissolve
    show tobe school mid happy at left:
        xoffset 135 yoffset 75
    show iroha school mid_left frown at right:
        xoffset -315 yoffset 65
    with dissolve
    voice "audio/voice/E4/CMM/03/IR/IR002.ogg"
    iroha "No, no, I have no idea who you're appealing to, but that'll only give you the opposite results. Appealing someone just because you want
        chocolates is obviously disgusting. How about you keep quiet?"
    show tobe worried with dissolve
    voice "audio/voice/E4/CMM/03/TB/TB004.ogg"
    tobe "Y-yeah..."
    hachiman "(Irohasu, that really burns...)"
    voice "audio/voice/E4/CMM/03/HA/HA001.ogg"
    hachiman "After a while, you get to taste them though."
    show tobe vhappy
    show iroha school mid_center frown at right:
        yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/03/TB/TB005.ogg"
    tobe "Yeah! That's it!"
    hachiman "(...He's a really simple guy, but at least this solved his problem...)"
    window auto hide dissolve
    scene kitchenA
    with dissolve
    show meguri school far vhappy at center with dissolve:
        xoffset 20 yoffset 75
    window auto show dissolve
    voice "audio/voice/E4/CMM/03/MG/MG000.ogg"
    meguri "Alrrriiight, let's do our best! Ohhh!"
    # cant find this audio files TODO
    prevscm "Ohhh!"
    hachiman "(...Oh, looks like they're starting as well.)"
    show meguri happy with dissolve
    voice "audio/voice/E4/CMM/03/MG/MG001.ogg"
    meguri "Ahhhhh"
    hide meguri with dissolve
    show haruno sweater far_center happy at center:
        xoffset 225 yoffset 75
    show meguri school far happy zorder 1 at center:
        xoffset -220 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/03/HR/HR000.ogg"
    haruno "Meguri, I see you enthusiastic about this~"
    voice "audio/voice/E4/CMM/03/MG/MG002.ogg"
    meguri "Because it's been a while since I participated Student Council-like events!"
    show haruno sweater far_left at center with dissolve:
        xoffset 225 yoffset 75
    voice "audio/voice/E4/CMM/03/HR/HR001.ogg"
    haruno "Your recommendation's actually been decided so you're at ease now, you~~"
    show meguri surprised with dissolve
    voice "audio/voice/E4/CMM/03/MG/MG003.ogg"
    meguri "Hyaaa, Haruno-san! Please don't poke my forehead!"
    show haruno vhappy with dissolve
    voice "audio/voice/E4/CMM/03/HR/HR002.ogg"
    haruno "I see nothing wrong with it~"
    show meguri happy with dissolve
    voice "audio/voice/E4/CMM/03/MG/MG004.ogg"
    meguri "Uuuuh. But Haruno-san, what kind will you make today? I look forward to your sweets~"
    voice "audio/voice/E4/CMM/03/HR/HR003.ogg"
    haruno "It's a secret to Meguri~"
    show meguri sad with dissolve
    voice "audio/voice/E4/CMM/03/MG/MG005.ogg"
    meguri "Uuuuuhhh..."
    hide haruno
    $url = ["haruno sweater far_left happy", "haruno sweater far_left happy"]
    call setImages from _call_setImages_1
    show mood1 at center:
        xoffset 225 yoffset 75
        parallel:
            1.0
            easein 0.5 xoffset -15
    voice "audio/voice/E4/CMM/03/HR/HR004.ogg"
    haruno "Kidding, kidding. Well, you see..."
    call finishmultiImage from _call_finishmultiImage_61
    show haruno sweater far_left happy at center with None:
        xoffset -15 yoffset 75
    show meguri vhappy
    show haruno vhappy
    with dissolve
    voice "audio/voice/E4/CMM/03/MG/MG006.ogg"
    meguri "Ehhh~! That sounds incredibly good!"
    hachiman "(I don't feel any kind of poisonous intention with the way they're talking. Is it because she's speaking with Meguri-senpai...?)"
    window auto hide dissolve
    scene kitchenA at truecenter:
        zoom 1.45 xalign 0 yoffset -15
    show kaori school mid worried at center:
        xoffset -25 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E4/CMM/03/OR/OR000.ogg"
    kaori "What the heck is this. No matter what I do, the walnut won't become as fine as powder. Hilarious."
    hide kaori with dissolve
    show kaori school mid worried at left:
        xoffset 195 yoffset 75
    show haruno sweater mid_left happy at center:
        xoffset 390 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/03/HR/HR005.ogg"
    haruno "Instead of using a knife to cut it, it's much more comfortable if you put the walnuts into a plastic bad and gently beat it with some kind of rolling pin."
    show kaori vhappy with dissolve
    voice "audio/voice/E4/CMM/03/OR/OR001.ogg"
    kaori "Ah, I see~! Thank you very much~"
    voice "audio/voice/E4/CMM/03/HR/HR006.ogg"
    haruno "That, are you gonna give that to someone?"
    show kaori happy with dissolve
    voice "audio/voice/E4/CMM/03/OR/OR002.ogg"
    kaori "Nope, I haven't specifically decided on it yet~ Though I think it's just nice if a girl can make a homemade sweets."
    show haruno vhappy with dissolve
    voice "audio/voice/E4/CMM/03/HR/HR007.ogg"
    haruno "Ahhh, yes. I know what you're trying to say. Those kinds of girls are popular to the boys, right, right. Did something like this happen during your middle school days? Say, if Hikigaya-kun got to accept sweets "
    voice sustain
    haruno "from a girl too or something."
    show kaori worried with dissolve
    voice "audio/voice/E4/CMM/03/OR/OR003.ogg"
    kaori "Eh, ah, nope, ahahahaha."
    hachiman "(I hate those kinds of talks... I can feel the peculiar gaze from here... Orimoto-san, don't give up...)"
    show yukino school mid_center happy behind kaori at center with dissolve:
        xoffset -105 yoffset 75
    show kaori annoyed at left:
        xoffset 195 yoffset 75
        easein 0.5 xoffset 65
    show haruno surprised at center:
        xoffset 390 yoffset 75
        easein 0.5 xoffset 515
    voice "audio/voice/E4/CMM/03/YK/YK002.ogg"
    yukino "Excuse me, nee-san but if you're done here, would you mind going back to your place and stop talking about your nonsense."
    show kaori worried
    show haruno worried
    with dissolve
    voice "audio/voice/E4/CMM/03/HR/HR008.ogg"
    haruno "Yes, yes. But my motivation disappears if someone tells me to work, you see~"
    hachiman "(Oh yes, I know that feeling quite well. I'll back working before someone tells me to do so... and to escape from here too...)"
    window auto hide dissolve
    scene kitchenA with dissolve
    window auto show dissolve
    voice "audio/voice/E4/CMM/03/KE/KE000.ogg"
    keika "Whoa!! Big choco!"
    show saki school far_right sad at center:
        xoffset -325 yoffset 75
    show keika home far vhappy at center:
        xoffset 245 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/03/SA/SA000.ogg"
    saki "K-Kei-chan, it's going to be a mess if you spread the chocolate around!"
    show keika happy with dissolve
    voice "audio/voice/E4/CMM/03/KE/KE001.ogg"
    keika "Saa-chan, can you eat this? It's so big, see?"
    show saki happy with dissolve
    voice "audio/voice/E4/CMM/03/SA/SA001.ogg"
    saki "You know, to make sweets, you melt and divide them into small pieces."
    voice "audio/voice/E4/CMM/03/KE/KE002.ogg"
    keika "Ohhh? Keika can do it too?"
    show saki vhappy with dissolve
    voice "audio/voice/E4/CMM/03/SA/SA002.ogg"
    saki "Of course Kei-chan, you can do it!"
    hachiman "(What's with the excellently soothing atmosphere over there...?)"
    window auto hide dissolve
    scene kitchenA at truecenter:
        zoom 1.45 xalign 1.0 yoffset -15
    with dissolve
    window auto show dissolve
    "And, as for the boys..."
    show hayama school mid_center happy at left:
        xoffset 165 yoffset 75
    show tobe school mid vhappy at right:
        yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/03/TB/TB006.ogg"
    tobe "Hey, hey, Hayato-kun! It's seriously great to see the ladies making chocos!"
    show hayama vhappy with dissolve
    voice "audio/voice/E4/CMM/03/HY/HY000.ogg"
    hayama "True. But let's not bother them and just keep ourselves quiet."
    show tobe angry with dissolve
    voice "audio/voice/E4/CMM/03/TB/TB007.ogg"
    tobe "Sure thing!"
    hachiman "(After the preparations, we, males, don't have anything to do.)"
    window auto hide dissolve
    stop music fadeout 1.0
    scene kitchenA
    with dissolve
    window auto show dissolve
    hachiman "(...May this be the reason why couples who have been married for a long time suddenly divorce? If I became a full-time husband, I should be
        careful. But, with those thoughts in my head...)"
    play music "audio/bgm/BGM37.ogg"
    show hayama school mid_center happy at center with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E4/CMM/03/HY/HY001.ogg"
    hayama "Hikigaya, are you going to do the food tasting too?"
    voice "audio/voice/E4/CMM/03/HA/HA002.ogg"
    hachiman "Yeah."
    voice "audio/voice/E4/CMM/03/HY/HY002.ogg"
    hayama "...I see."
    voice "audio/voice/E4/CMM/03/HA/HA003.ogg"
    hachiman "...What?"
    show hayama vhappy with dissolve
    voice "audio/voice/E4/CMM/03/HY/HY003.ogg"
    hayama "Ahh, I just thought you're the perfect person for it."
    voice "audio/voice/E4/CMM/03/HA/HA004.ogg"
    hachiman "Ha?"
    show hayama happy with dissolve
    voice "audio/voice/E4/CMM/03/HY/HY004.ogg"
    hayama "You like sweet stuff, right?"
    voice "audio/voice/E4/CMM/03/HA/HA005.ogg"
    hachiman "Y-yeah..."
    hachiman "(...That was dangerous. For a moment, I thought that I'd go \"OMG, you know what stuff I like, KYAAA!\" or something. That won't happen though, definitely.)"
    voice "audio/voice/E4/CMM/03/EB/EB001.ogg"
    ebina "I, I am witnessing one of the best sweet-sour moments of HayaHachi!!OH, SWEET GODS OF VALENTINES!!"
    voice "audio/voice/E4/CMM/03/YM/YM002.ogg"
    yumiko "Wha---Ebina! Your nose is bleeding! Wipe it!"
    stop music fadeout 1.0
    hide hayama with dissolve
    play music "audio/bgm/BGM41.ogg"
    "The smell of sweet is drifting around here and there."
    hachiman "(As expected, there surely are a lot of girls doing their best. No, a part of the boys were, too...)"
    hachiman "(Valentines is truly a special day. With this kind of excuse, there are surely those people who will be helped.)"
    menu E4_CMM_03_menu:
        with dissolve
        hachiman "(But still...)"
        "They sure are getting into it...":
            jump E4_CMM_04
        "There's a lot of people, it's tiring.":
            hachiman "(I knew I'd get tired if there were too many people. It's not just about the number of people, but also about the feelings and thoughts that are involved.)"
            window auto hide dissolve
            stop music fadeout 0.5
            stop ambient fadeout 0.5
            jump E4_SHI_01

label E4_CMM_04:
    hachiman "(They sure are getting into it. I didn't know how it would go at first, but it looks like the event is a success... For now.)"
    "The event slowly progresses, without any major obstacles or setbacks."
    "The girls, holding their feelings close to their heart with a serious look, were battling it out against the chocolate and cookware."
    "The event doesn't have any progress-impeding issues that stand out. It's just that everybody is going at their own pace, working slowly but surely."
    "The maidens are seriously putting their hearts into it, and the chocolates and kitchenware are taking the brunt of their ambitions."
    hachiman "(Well, I'm glad everybody's having a good time...)"
    show iroha school far_center happy at center with dissolve:
        xoffset -30 yoffset 75
    "Looking at the kitchen table next to me, I see the one responsible for this event---Isshiki Iroha, making sweets at her own pace."
    "From and outsiders perspective, Isshiki's going was going well."
    "After melting the chocolate, she puts it into a bowl and tosses some kind of gentle gloss on it. Also, in another bowl, a foamy meringue was being prepared."
    "Just by the way she moves I could tell she was experienced in making sweets."
    "Isshiki added another teaspoon of what looked like Western liquor to the bowl and gave it another stir. She scooped up a small amount with a spoon and tasted it."
    show iroha school far_left pout at center with dissolve:
        xoffset -25 yoffset 80
    "She stayed still for a while, sucking on the spoon, and then bent her head at an angle."
    show iroha angry with dissolve
    "Apparently, she was not satisfied. She started adding more sugar, cream, cocoa powder and so on."
    hide iroha with dissolve
    show iroha school mid_left angry at center with dissolve:
        xoffset -35 yoffset 65
    voice "audio/voice/E4/CMM/04/HA/HA000.ogg"
    hachiman "You're really good at this..."
    show iroha school mid_center unimpressed at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/CMM/04/IR/IR000.ogg"
    iroha "Senpai, had you been doubting what I said?"
    voice "audio/voice/E4/CMM/04/HA/HA001.ogg"
    hachiman "No, nothing like that. ...I just thought it was amazing. You're doing a great job."
    voice "audio/voice/E4/CMM/04/IR/IR001.ogg"
    iroha "What, are you hitting on me? Just because this is something sweet doesn't mean you can just whisper sweet nothings into my ear. You're too naive about this, so please try again another time, sorry."
    voice "audio/voice/E4/CMM/04/HA/HA002.ogg"
    hachiman "I'm not hitting on you, and I'm not gonna try again... I was just impressed."
    show iroha happy with dissolve
    voice "audio/voice/E4/CMM/04/IR/IR002.ogg"
    iroha "I see. Well, it's nice to see girls putting their hearts into something, isn't it? ...Right, off I go!"
    voice "audio/voice/E4/CMM/04/HA/HA003.ogg"
    hachiman "Yep, good luck..."
    show iroha school mid_left vhappy at center with dissolve:
        xoffset -35 yoffset 65
    voice "audio/voice/E4/CMM/04/IR/IR003.ogg"
    iroha "Hayama-senpai~!"
    hide iroha with dissolve
    voice "audio/voice/E4/CMM/04/HA/HA004.ogg"
    hachiman "............"
    play sound "audio/sfx/SE04/SE04_08.ogg"
    $renpy.pause(delay=0.5, hard=True)
    show hiratsuka school far_center annoyed flat at center:
        xoffset 150 yoffset 75 alpha 0
        on show:
            parallel:
                linear 1.0 alpha 1
            parallel:
                easein 1.0 xoffset -5
    $renpy.pause(delay=1.0, hard=True)
    stop sound
    hide hiratsuka
    show hiratsuka school far_center annoyed at center:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/CMM/04/SZ/SZ000.ogg"
    hiratsuka "Tch, the sweet aroma clinging in the air..."
    hide hiratsuka with dissolve
    show hiratsuka school mid_center frown at center with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E4/CMM/04/HA/HA005.ogg"
    hachiman "Uhm, why are you here, Hiratsuka-sensei?"
    show hiratsuka happy with dissolve
    voice "audio/voice/E4/CMM/04/SZ/SZ001.ogg"
    hiratsuka "Hm? Aah, I saw Isshiki's report so I just came to check it out."
    show hiratsuka school mid_left happy at center with dissolve:
        xoffset 110 yoffset 80
    voice "audio/voice/E4/CMM/04/SZ/SZ002.ogg"
    hiratsuka "You look like you have nothing to do, Hikigaya. How about you help me with something?"
    voice "audio/voice/E4/CMM/04/HA/HA006.ogg"
    hachiman "...What's that?"
    voice "audio/voice/E4/CMM/04/SZ/SZ003.ogg"
    hiratsuka "I thought I'd bring you something for taste-testing reference..."
    "With that being said, Hiratsuka-sensei took out one cold storage bag after the next, taking out the contents of each one. What she took out were luxury-looking packages that looked to contain high-class "
    "chocolates goods lined up neatly inside."
    show haruno sweater mid_center happy behind hiratsuka at right:
        xoffset -100 yoffset 75
        easein 0.5 xoffset -170
    show meguri school mid happy at left:
        xoffset 100 yoffset 75
        easein 0.5 xoffset 145
    with dissolve
    voice "audio/voice/E4/CMM/04/HR/HR000.ogg"
    haruno "Wow, Shizuka, you really went all out. From the standard ones, to the more sophisticated ones... Oh, these are limited edition. It must have been hard to get them."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E4/CMM/04/SZ/SZ004.ogg"
    hiratsuka "Well, yeah. After the reservations were opened, they were sold out in a matter of hours."
    hachiman "(Sensei, that's another hobby you put a lot into, huh...)"
    "If you open the stylish package, you'll find a line of glittering chocolates that looks like the show window of a jewelry store."
    show meguri vhappy with dissolve
    voice "audio/voice/E4/CMM/04/MG/MG000.ogg"
    meguri "Wow, it looks delicious!"
    show haruno sweater mid_left vhappy behind hiratsuka at right with dissolve:
        xoffset -110 yoffset 75
    voice "audio/voice/E4/CMM/04/HR/HR001.ogg"
    haruno "Ahhh, Meguri, you know them too? They are sooo delicious~. Highly recommend them."
    hide haruno
    hide hiratsuka
    hide meguri
    with dissolve
    show hiratsuka school mid_center frown at left:
        xoffset 110 yoffset 75
    show haruno sweater mid_left vhappy at right:
        xoffset -240 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/04/SZ/SZ005.ogg"
    hiratsuka "Wait a sec. Why are you the one bragging about it? I was the one who picked them."
    show haruno happy with dissolve
    voice "audio/voice/E4/CMM/04/HR/HR002.ogg"
    haruno "I was just praising your tastes, Shizuka-chan~. These go so good with a drink! Ahhh, now I reaaally want some booze with these~."
    voice "audio/voice/E4/CMM/04/SZ/SZ006.ogg"
    hiratsuka "I certainly drink alcohol with chocolate, but... today's a no-go for me."
    show haruno worried with dissolve
    voice "audio/voice/E4/CMM/04/HR/HR003.ogg"
    haruno "Muuh, that's too bad."
    show haruno vhappy with dissolve
    voice "audio/voice/E4/CMM/04/HR/HR004.ogg"
    haruno "How about we hang out sometime? There're surely lots of things we can catch up on, right?"
    show hiratsuka happy with dissolve
    voice "audio/voice/E4/CMM/04/SZ/SZ007.ogg"
    hiratsuka "...Haruno. If you really have piled up a lot of things to talk about, then I'll be there for you anytime."
    show haruno angry with dissolve
    voice "audio/voice/E4/CMM/04/HR/HR005.ogg"
    haruno "........."
    image hiratsukaFlat = Flatten("hiratsuka school mid_center frown")
    $url = ["haruno sweater mid_left vhappy", "haruno sweater mid_center happy"]
    call setImagesFlat from _call_setImagesFlat_2
    show hiratsukaFlat at left:
        xoffset 110 yoffset 75
    show mood1 at right:
        xoffset -240 yoffset 75
    with dissolve
    show hiratsukaFlat at left:
        parallel:
            4.25
            linear 0.3 alpha 0
    show mood1 at right:
        parallel:
            4.25
            linear 0.3 alpha 0
    hide hiratsuka
    hide haruno
    show mood2 at center:
        xoffset 10 yoffset 75 alpha 0
        parallel:
            4.8
            linear 0.3 alpha 1
    voice "audio/voice/E4/CMM/04/HR/HR006.ogg"
    haruno "Really~? Then we'll have to make plans. Ah, will you come too, Hikigaya-kun? Have a drink with us ladies~"
    hide hiratsukaFlat
    call finishmultiImage from _call_finishmultiImage_62
    show haruno sweater mid_center happy at center:
        xoffset 10 yoffset 75
    voice "audio/voice/E4/CMM/04/HA/HA007.ogg"
    hachiman "I'm a minor. Alcohol is prohibited to me so I'll have orange juice instead."
    hide haruno
    $url = ["haruno sweater mid_center happy", "haruno sweater mid_left happy"]
    $multiImagePara = [10, 75, -10, 75, 6.0]
    call multiImage(0, False) from _call_multiImage_59
    voice "audio/voice/E4/CMM/04/HR/HR007.ogg"
    haruno "It's boring if you can't drink. Well, you are underage so I guess it can't be helped. Then, Meguri? Will you come along?"
    call finishmultiImage from _call_finishmultiImage_63
    with dissolve
    show haruno sweater mid_left happy at right:
        xoffset -240 yoffset 75
    show meguri school mid unimpressed at left:
        xoffset 270 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/04/MG/MG001.ogg"
    meguri "Haru-san, I am also a minor~. I can drink tea, but..."
    voice "audio/voice/E4/CMM/04/HR/HR008.ogg"
    haruno "I see. Eh, what shall I do then~? Maybe I should ask my classmates~."
    hide meguri with dissolve
    show hiratsuka school mid_center happy at left with dissolve:
        xoffset 110 yoffset 75
    voice "audio/voice/E4/CMM/04/SZ/SZ008.ogg"
    hiratsuka "Well, call me when you need me."
    voice "audio/voice/E4/CMM/04/HR/HR009.ogg"
    haruno "Whenever that is."
    hide hiratsuka
    hide haruno
    with dissolve
    show hiratsuka school mid_center happy at right:
        xoffset -25 yoffset 75
    show meguri school mid happy at left:
        xoffset 270 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/04/SZ/SZ009.ogg"
    hiratsuka "Now, Hikigaya, Shiromeguri. Take some of these and distribute them to everyone."
    hide hiratsuka
    hide meguri
    with dissolve
    show meguri school near angry at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/CMM/04/MG/MG002.ogg"
    meguri "Let's see, in how many pieces do we divide them?"
    voice "audio/voice/E4/CMM/04/MG/MG003.ogg"
    meguri "Hmmmmmm..."
    "Meguri-senpai pondered for a while as she divided the chocolates into the paper plates near her. She finally looked up with a smile, apparently satisfied with the way she had divided them."
    show meguri vhappy with dissolve
    voice "audio/voice/E4/CMM/04/MG/MG004.ogg"
    meguri "Ahhhhh."
    play sound "audio/sfx/SE02/SE02_19.ogg"
    #star character should be added to fonts
    hachiman "(Yep. Meguri-senpai's Megurisshu☆ is super effective. I feel my fatigue melting away...)"
    stop sound fadeout 0.5
    voice "audio/voice/E4/CMM/04/MG/MG005.ogg"
    meguri "Here, Hikigaya-kun, I'll leave these to you."
    voice "audio/voice/E4/CMM/04/HA/HA008.ogg"
    hachiman "Roger that."
    hide meguri with dissolve
    show totsuka athletic mid_center happy at left:
        xoffset 260 yoffset 75
    show meguri school mid happy_flat at right:
        xoffset -225 yoffset 75
        on hide:
            parallel:
                linear 0.5 alpha 0
            parallel:
                linear 0.5 xoffset -150
    with dissolve
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E4/CMM/04/SI/SI000.ogg"
    totsuka "Ah, let me help too."
    voice "audio/voice/E4/CMM/04/HA/HA009.ogg"
    hachiman "Ooh, Totsuka."
    voice "audio/voice/E4/CMM/04/MG/MG006.ogg"
    meguri "I'll be bringing these to the members of the Student Council, alright? Hikigaya-kun, take care of the rest! I'm counting on you~!"
    hide meguri
    $renpy.pause(delay=0.5, hard=True)
    show meguri school mid
    hide meguri
    hide totsuka with dissolve
    show totsuka athletic mid_center happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E4/CMM/04/HA/HA010.ogg"
    hachiman "Well, we have to evenly distribute these among the tables."
    show totsuka vhappy with dissolve
    voice "audio/voice/E4/CMM/04/SI/SI001.ogg"
    totsuka "Got it!"
    hide totsuka with dissolve
    menu E4_CMM_04_menu:
         #According to the script files, there can be up to 6 options here:
         #Yukinoshita, Yuigahama, Isshiki, Miura&Ebina-san, Haruno-san&Meguri-senpai, and Kei-chan.
         #Not sure what is required for each one to appear as an option, assuming some sort of point system and need to sufficiently clear each characters' levels or something.
         #For now I will display all options... Note that with 6 options The top one goes partially off the top of the screen.
         #This is where routing can be senseless...
        hachiman "(Alright where should I go...)"
        with dissolve
        "Yukinoshita":
            $chocoEventHelp = "yukinoshita"
            hachiman "(In Yukinoshita's case, I get the feeling this'll light the \"I hate losing\" fire in her, rather than using this as a reference... Well I'm going to get tired if I don't move around anyway.)"
            show yui school mid_center vhappy at left:
                xoffset 255 yoffset 75
            show yukino school mid_left happy at right:
                xoffset -170 yoffset 80
            with dissolve
            voice "audio/voice/E4/CMM/04/HA/HA011.ogg"
            stop music fadeout 1.0
            hachiman "Yukinoshita. I brought some gifts from Hiratsuka-sensei... ah..."
            play music "audio/bgm/BGM40.ogg"
            voice "audio/voice/E4/CMM/04/YK/YK000.ogg"
            yukino "Yuigahama-san, about the next step..."
            voice "audio/voice/E4/CMM/04/YI/YI000.ogg"
            yui "Um... Do this, and with that..."
            hachiman "(I don't think now's a good time to interrupt them...)"
            jump E4_YUK_03
        "Yuigahama":
            $chocoEventHelp = "yui"
            hachiman "(I'll wait for Yuigahama. She looks like she's really putting it all on the table...)"
            play music "audio/bgm/BGM12.ogg"
            show yukino school far_left happy at center with dissolve:
                xoffset 250 yoffset 75
            voice "audio/voice/E4/CMM/04/YK/YK001.ogg"
            yukino "Yeah, like that. I think it'll be fine."
            hide yukino with dissolve
            show yui school far_left angry at center with dissolve:
                xoffset -220 yoffset 75
            voice "audio/voice/E4/CMM/04/YI/YI001.ogg"
            yui "Um, do this like that and... for this one..."
            hide yui with dissolve
            hachiman "(She looks pretty busy...)"
            hachiman "(Let's see... I wonder if she's doing alright.)"
            stop music fadeout 1.0
            jump E4_YUI_02
        "Isshiki" if iroha_menu:
            $chocoEventHelp = "iroha"
            stop music fadeout 0.5
            hachiman "(I wonder how the girl behind the whole event is doing..)"
            voice "audio/voice/E4/CMM/04/HA/HA012.ogg"
            hachiman "Hey, Isshiki. I got some handouts from Hiratsuka sensei..."
            play music "audio/bgm/BGM36.ogg"
            show iroha school far_center angry at center with dissolve:
                xoffset -30 yoffset 75
            voice "audio/voice/E4/CMM/04/IR/IR004.ogg"
            iroha "............"
            hachiman "(She looks really concentrated right now. I'll come by later...)"
            jump E4_IRO_02
        #"Miura & Ebina-san" if yumiko_menu or ebina_menu: #TL and animations required
            hachiman "(まあ、三浦たちのとこにでも持ってくか。こういうオサレっぽいチョコに一番反応しそうだし)"
            voice "audio/voice/E4/CMM/04/TB/TB000.ogg"
            tobe "っべー。海老名さんマァジ器用だわー。なに？ このチェック模様？ めっちゃ綺麗じゃね？"
            voice "audio/voice/E4/CMM/04/EB/EB000.ogg"
            ebina "市松模様っていうんだよ。わたし、市松大好きだからねー"
            voice "audio/voice/E4/CMM/04/TB/TB001.ogg"
            tobe "市松それマジ俺も好きだわー。かなり食べてみたいわー。ちょこっと食べてみたいわー"
            voice "audio/voice/E4/CMM/04/EB/EB001.ogg"
            ebina "うーん、これは自分で楽しむようだからなぁ"
            voice "audio/voice/E4/CMM/04/TB/TB002.ogg"
            tobe "っべー⋯⋯"
            voice "audio/voice/E4/CMM/04/YM/YM000.ogg"
            yumiko "は、隼人、焼き加減ってこんなんでいいと思う？"
            voice "audio/voice/E4/CMM/04/HY/HY000.ogg"
            hayama "どうかな？ 俺もあまり自信ないけど、いいと思うよ。良かったら誰かに聞いてみるか？"
            voice "audio/voice/E4/CMM/04/YM/YM001.ogg"
            yumiko "う、うん⋯⋯。や、別に隼人がいいなら、いいんだけど⋯⋯"
            "not finished"
            jump E4_CMM_04_menu
        "Haruno-san & Meguri-senpai" if haruno_menu or meguri_menu: #TL and animations required
            stop music
            hachiman "(We'll probaly have a surplus because of the people that know what they're doing...)"
            play music "audio/bgm/BGM41.ogg"
            show meguri school far vhappy at center:
                xoffset -220 yoffset 75
            show haruno sweater far_left happy at center:
                xoffset 225 yoffset 75
            with dissolve
            voice "audio/voice/E4/CMM/04/MG/MG007.ogg"
            meguri "I haven't made sweets in ages!"
            voice "audio/voice/E4/CMM/04/HR/HR010.ogg"
            haruno "Girly things like this suit you, Meguri~"
            show meguri happy with dissolve
            voice "audio/voice/E4/CMM/04/MG/MG008.ogg"
            meguri "*fufu* I'm a girl after all! Making chocolates for Valentine's Day is really fun for me!"
            show haruno sly with dissolve
            voice "audio/voice/E4/CMM/04/HR/HR011.ogg"
            haruno "Hmm. So, as a girl, Meguri, are you going to give them to someone~?"
            show meguri unimpressed with dissolve
            voice "audio/voice/E4/CMM/04/MG/MG009.ogg"
            meguri "Huh? How would I go about that...? Hmm."
            hachiman "(I wonder if Shiromeguri-senpai is just doging Haruno-san's questions... Megu☆ MeguMegurin Megurishu, you really are amazing.)"
            jump E4_HAR_02
        "Kei-chan" if saki_menu:#
            $chocoEventHelp = "saki"
            hachiman "(Umm... how about Kei-chan and Kawa... Kawa... Kawa-something-san..?)"
            show keika home far happy at center:
                xoffset 245 yoffset 75
            show saki school far_right vhappy at center:
                xoffset -325 yoffset 75
            with dissolve
            voice "audio/voice/E4/CMM/04/KE/KE000.ogg"
            keika "Hey Saa-chan. Is the choco done? Is it done already?"
            voice "audio/voice/E4/CMM/04/SA/SA000.ogg"
            saki "You're right, maybe it's about time. Let's take a look, shall we?"
            show keika vhappy with dissolve
            voice "audio/voice/E4/CMM/04/KE/KE001.ogg"
            keika "Yeah!"
            hachiman "(So heartwarming...)"
            window auto hide dissolve
            stop ambient fadeout 0.5
            stop music fadeout 0.5
            jump E4_SAK_03

label E4_CMM_05:
    scene kitchenB with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/BGM34.ogg"
    window auto show dissolve
    "In the room, everyone finished cooking and was enjoying themselves as they chatted while eating sweets and drinking tea."
    show iroha school_sunset far_left vhappy at center with dissolve:
        xoffset -25 yoffset 80
    "Just in time, Isshiki looked around and gave a brief closing speech."
    voice "audio/voice/E4/YMK/08/IR/IR000.ogg"
    iroha "And with that, everyone, thank you all and good work today! We'll finish up the cleaning, so don't forget anything as you go home!"
    "As Isshiki finished speaking, one by one, people began to leave."
    "...Of course, the Service Club was part of the clean-up crew."
    hide iroha with dissolve
    voice "audio/voice/E4/YMK/08/ZG/ZG000.ogg"
    scvp "Ah, sorry for making you help out."
    voice "audio/voice/E4/YMK/08/HA/HA000.ogg"
    hachiman "Not at all..."
    hachiman "(Well this was part of the plan after all...)"
    show yukino school_sunset mid_center vhappy at left:
        xoffset -105 yoffset 75
    show yui school_sunset mid_center happy at center:
        xoffset -25 yoffset 75
    show iroha school_sunset mid_center happy at right:
        xoffset -190 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/05/YI/YI000.ogg"
    yui "Okay! That went by quickly, didn't it?"
    voice "audio/voice/E4/CMM/05/YK/YK000.ogg"
    yukino "Yes, it did. I'm relieved it ended without any major issue."
    show iroha school_sunset mid_left vhappy at right with dissolve:
        xoffset -190 yoffset 65
    voice "audio/voice/E4/CMM/05/IR/IR002.ogg"
    iroha "I want to do something with everyone again!"
    voice "audio/voice/E4/CMM/05/HA/HA000.ogg"
    hachiman "Nah, this one time is enough, right? Isn't it enough?"
    show yui school_sunset mid_right vhappy at center with dissolve:
        xoffset -110 yoffset 75
    voice "audio/voice/E4/CMM/05/YI/YI001.ogg"
    yui "Ah, that's great! I wonder what event we're gonna do next?"
    voice "audio/voice/E4/CMM/05/HA/HA001.ogg"
    hachiman "Hey? Are you listening to me? Could you listen to what I say from time to time?"
    hide iroha
    hide yui
    hide yukino
    with dissolve
    show yumiko school_sunset far_center vhappy at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E4/CMM/05/YM/YM000.ogg"
    yumiko "Then I want to go skiing."
    hide yumiko with dissolve
    show keika home_sunset far happy flat at center with dissolve:
        xoffset 5 yoffset 70
        on hide:
            parallel:
                easein 0.5 xoffset -150
            parallel:
                linear 0.5 alpha 0
    voice "audio/voice/E4/CMM/05/KE/KE000.ogg"
    keika "Yes! Kei-chan wants to go skiing too!"
    show saki school_light_sunset far_right surprised flat behind keika at center:
        xoffset -400 yoffset 75 alpha 0
        parallel:
            linear 0.3 alpha 1.0
        parallel:
            easein 0.3 xoffset -245
        on hide:
            parallel:
                easein 0.5 xoffset -400
            parallel:
                linear 0.5 alpha 0
    $renpy.pause(delay=0.3, hard=True)
    voice "audio/voice/E4/CMM/05/SA/SA000.ogg"
    saki "Wai-- Kei-chan!?"
    hide keika
    hide saki
    $renpy.pause(delay=0.6, hard=True)
    show ebina school_sunset far_center vhappy at center:
        xoffset 310 yoffset 75
    show tobe school_sunset far happy at center:
        xoffset -195 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/05/EB/EB000.ogg"
    ebina "Oh, that sounds good! Winter means skiing!"
    show tobe vhappy with dissolve
    voice "audio/voice/E4/CMM/05/TB/TB000.ogg"
    tobe "Right!"
    show ebina relieved with dissolve
    voice "audio/voice/E4/CMM/05/EB/EB001.ogg"
    ebina "And then, love that makes even the ski slopes melt! No matter what happens to these two, it's basically always the snow's fault! So they can do what they want, all they want!"
    show tobe worried with dissolve
    voice "audio/voice/E4/CMM/05/TB/TB001.ogg"
    tobe "I-I guess?"
    hachiman "(These two? Hey, who are these two?)"
    hide ebina
    hide tobe
    with dissolve
    show kaori school_sunset far happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E4/CMM/05/OR/OR000.ogg"
    kaori "Come to think of it, I haven't gotten on a snowboard before."
    hachiman "(I'm getting the feeling that more people are getting on this bandwagon... I wonder if this unforeseen dark force is what they call girl power... And speaking of dark force, there it is, in the flesh!)"
    hide kaori with dissolve
    show haruno sweater_sunset far_center happy at center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E4/CMM/05/HR/HR000.ogg"
    haruno "Skiing, huh... That sounds great! Right, Meguri, Hayato too."
    hide haruno with dissolve
    show haruno sweater_sunset far_center happy at center:
        xoffset -425 yoffset 75
    show hayama school_sunset far_center happy at center:
        xoffset 360 yoffset 65
    show meguri school_sunset far vhappy at center:
        xoffset 20 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/05/MG/MG000.ogg"
    meguri "Skiing... It sounds like it'd be fun to go with so many people!"
    voice "audio/voice/E4/CMM/05/HY/HY000.ogg"
    hayama "Sure, I guess. We'll be studying for exams starting spring as well... This may be a good chance to do something like this."
    hide hayama
    hide meguri
    hide haruno
    with dissolve
    show hayama school_sunset far_center happy at center:
        xoffset -285 yoffset 65
    show yumiko school_sunset far_left vhappy at center:
        xoffset 240 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/05/YM/YM001.ogg"
    yumiko "You think so too, Hayato?"
    show hayama school_sunset far_right happy at center with dissolve:
        xoffset -230 yoffset 70
    voice "audio/voice/E4/CMM/05/HY/HY001.ogg"
    hayama "We don't have that many opportunities after all. If we're all going, then we need to choose a place though..."
    hide yumiko
    hide hayama
    with dissolve
    show meguri school_sunset far happy at center with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E4/CMM/05/MG/MG001.ogg"
    meguri "Ah, speaking of which, there used to be a ski trip sponsored by the Student Council a while ago. I think there was a lodge the school rented."
    hachiman "(This is the first I've heard of it. This won't do. We Japanese are quite hesitant about new ideas, but when there's a precedent, we're unbelievably easy. As such...)"
    hide meguri with dissolve
    show iroha school_sunset far_center vhappy at center with dissolve:
        xoffset -30 yoffset 75
    voice "audio/voice/E4/CMM/05/IR/IR003.ogg"
    iroha "Ah, if that's the case, should we all go as an event sponsored by the Student Council?"
    hachiman "(Ah... See, I knew it...)"
    voice "audio/voice/E4/CMM/05/IR/IR004.ogg"
    iroha "We can cover the costs that way and won't have to worry about accommodation, either!"
    voice "audio/voice/E4/CMM/05/YI/YI002.ogg"
    yui "Iroha-chan, nice! Nice idea!"
    hide iroha with dissolve
    show yukino school_sunset mid_center happy at left:
        xoffset 25 yoffset 75
    show yui school_sunset mid_left vhappy at right:
        xoffset -270 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/05/YI/YI003.ogg"
    yui "Hey, Yukinon! Skiing together sounds like a lot of fun!"
    voice "audio/voice/E4/CMM/05/YK/YK001.ogg"
    yukino "No, I... Well actually, when was it decided that I will go skiing, too?"
    show yui sad with dissolve
    voice "audio/voice/E4/CMM/05/YI/YI004.ogg"
    yui "I want to go with you, though..."
    show yui:
        easein 0.5 xoffset -680
    $renpy.pause(delay=0.5, hard=True)
    show yukino blush with dissolve
    voice "audio/voice/E4/CMM/05/YK/YK002.ogg"
    yukino "T-too close. Yuigahama-san, you're too close..."
    hide yui
    hide yukino
    with dissolve
    show iroha school_sunset mid_center happy at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/CMM/05/IR/IR005.ogg"
    iroha "Ah, everyone in the Service Club is obligated to come with us, if they would be so kind!"
    voice "audio/voice/E4/CMM/05/HA/HA002.ogg"
    hachiman "Huh? Can you please not contradict yourself in one sentence?"
    hide iroha with dissolve
    show yukino school_sunset mid_center happy at left:
        xoffset -105 yoffset 75
    show yui school_sunset mid_center happy at center:
        xoffset -25 yoffset 75
    show iroha school_sunset mid_center happy at right:
        xoffset -190 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/05/HA/HA003.ogg"
    hachiman "And you guys just want to go skiing, don't you?"
    hide yui
    $url = ["yui school_sunset mid_center happy", "yui school_sunset mid_left happy"]
    $multiImagePara = [-25, 75, 10, 75, 4.5]
    call multiImage(0, False) from _call_multiImage_60
    voice "audio/voice/E4/CMM/05/YI/YI005.ogg"
    yui "That's not true! This is also an important part of our club activities! Right, Yukinon?"
    call finishmultiImage from _call_finishmultiImage_64
    show yui school_sunset mid_left happy at center:
        xoffset 10 yoffset 75
    show iroha school_sunset mid_left happy with dissolve:
        yoffset 65
    voice "audio/voice/E4/CMM/05/IR/IR006.ogg"
    iroha "Yui-senpai, you make a good point! That's right! This is also a part of the Student Council's work! Don't you think so, Yukinoshita-senpai?"
    show yukino pout with dissolve
    voice "audio/voice/E4/CMM/05/YK/YK003.ogg"
    yukino "I... I wonder about that."
    hachiman "(Oh, Yukinoshita doesn't seem to agree. You can do it, Yukinoshita! Resist!)"
    voice "audio/voice/E4/CMM/05/HA/HA004.ogg"
    hachiman "...Must be great to abuse authority."
    show yui school_sunset mid_center vhappy at center:
        xoffset -35 yoffset 75
    show iroha school_sunset mid_center vhappy at right:
        xoffset -190 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/05/MI/MIX000.ogg"
    yuiandiro "That's not true, right, Hiratsuka-sensei?"
    show yui school_sunset mid_right happy at center:
        xoffset -110 yoffset 75
    show iroha school_sunset mid_left happy:
        yoffset 65
    with dissolve
    voice "audio/voice/E4/CMM/05/YI/YI007.ogg"
    yui "Ah, we harmonized..."
    voice "audio/voice/E4/CMM/05/IR/IR008.ogg"
    iroha "We harmonized, didn't we?"
    hide yui
    hide yukino
    hide iroha
    with dissolve
    show hiratsuka school_light_sunset mid_center happy at center with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E4/CMM/05/SZ/SZ000.ogg"
    hiratsuka "Yeah. Well, we did something similar during the summer break too. This is also an important part of club activities. As the Service Club's
        advisor, I shall accompany you as well."
    voice "audio/voice/E4/CMM/05/HA/HA005.ogg"
    hachiman "Seriously...?"
    voice "audio/voice/E4/CMM/05/SZ/SZ001.ogg"
    hiratsuka "Hikigaya. You can also invite your little sister. Won't she want to spread her wings since her entrance exams have just ended?"
    voice "audio/voice/E4/CMM/05/HA/HA006.ogg"
    hachiman "A-ah, ummmm, hmmmm... Well, sure. T-that's right... Actually, I can see that..."
    hachiman "(I feel like I was nearly pulled in just then... Does Hiratsuka-sensei possibly just want to go skiing as well?)"
    hide hiratsuka with dissolve
    show yukino school_sunset mid_center unimpressed at left:
        xoffset -105 yoffset 75
    show yui school_sunset mid_center vhappy at center:
        xoffset -25 yoffset 75
    show iroha school_sunset mid_center vhappy at right:
        xoffset -190 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/05/IR/IR009.ogg"
    iroha "That settles it!"
    voice "audio/voice/E4/CMM/05/YI/YI008.ogg"
    yui "Hooray!"
    voice "audio/voice/E4/CMM/05/YK/YK004.ogg"
    yukino "............"
    hachiman "(F...For it to be decided by a flippant popular vote, in addition to one word from an authoritative figure... Democracy is stupid!)"
    hide iroha
    hide yui
    hide yukino
    with dissolve
    if chocoEventHelp == "yukino" or chocoEventHelp == "yui":
        #yukino/yui route
        jump E4_CMM_05_YUK_YUI
    elif chocoEventHelp == "saki":
        #saki route
        jump E4_CMM_05_SAKI
    elif chocoEventHelp == "haruno" or chocoEventHelp == "meguri":
        #haruno/meguri route
        jump E4_CMM_05_HAR_MEG
    elif chocoEventHelp == "iroha":
        #iroha route
        jump E4_CMM_05_IRO
    elif chocoEventHelp == "hiratsuka":
        #iroha route
        jump E4_CMM_05_SHI

label E4_CMM_05_SHI:
    show hiratsuka coat_sunset far_center angry at center with dissolve:
        xoffset -10 yoffset 75
    voice "audio/voice/E4/CMM/05/SZ/SZ003.ogg"
    hiratsuka "Well, that was that."
    hachiman "(Huh? Is Sensei leaving? I thought she and Haruno-san were going somewhere after.)"
    stop music fadeout 0.5
    show hiratsuka happy with dissolve
    voice "audio/voice/E4/CMM/05/SZ/SZ004.ogg"
    hiratsuka "......"
    hachiman "(Her exppression is makng me curious.)"
    hide hiratsuka with dissolve
    jump E4_SHI_02

label E4_CMM_05_YUK_YUI:
    show yukino school_sunset mid_center pout at left:
        xoffset 25 yoffset 75
    show yui school_sunset mid_center happy at right:
        xoffset -305 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/05/YI/YI009.ogg"
    yui "Hey. Do you two not feel like going skiing after all?"
    voice "audio/voice/E4/CMM/05/HA/HA007.ogg"
    hachiman "Well, yeah... I mean, it's going to be like {i}that{/i}. It's cold, there's going to be a lot of people, and I've never done it before."
    hide yui
    $url = ["yui school_sunset mid_center surprised2", "yui school_sunset mid_center vhappy"]
    $multiImagePara = [-305, 75, 0, 0, 1.62]
    call multiImage(1) from _call_multiImage_61
    voice "audio/voice/E4/CMM/05/YI/YI010.ogg"
    yui "Those are your reasons!? It's fun if you give it a go!"
    call finishmultiImage from _call_finishmultiImage_65
    show yui school_sunset mid_center vhappy at right:
        xoffset -305 yoffset 75
    voice "audio/voice/E4/CMM/05/HA/HA008.ogg"
    hachiman "Really? I mean there's already a lot of people going..."
    hachiman "(Dealing with people is a pain too...)"
    voice "audio/voice/E4/CMM/05/YI/YI011.ogg"
    yui "Come on, this can be a job well done party for Komachi-chan, too! She didn't get to be here with us today!"
    hachiman "(Ku... I'm weak whenever they bring up Komachi's name...)"
    voice "audio/voice/E4/CMM/05/YK/YK004.ogg"
    yukino "............"
    voice "audio/voice/E4/CMM/05/HA/HA009.ogg"
    hachiman "W-well... That's true, but..."
    hide yui
    $url = ["yui school_sunset mid_center frown", "yui school_sunset mid_left pout"]
    $multiImagePara = [-305, 75, -270, 75, 1.5]
    call multiImage(1, False) from _call_multiImage_62
    voice "audio/voice/E4/CMM/05/YI/YI012.ogg"
    yui "Boo... W-What about you, Yukinon?"
    call finishmultiImage from _call_finishmultiImage_66
    show yui school_sunset mid_left pout at right: #pout by default.
        xoffset -270 yoffset 75
    voice "audio/voice/E4/CMM/05/YK/YK005.ogg"
    yukino "Well... I don't mind skiing itself, but..."
    show yukino school_sunset mid_left pout at left with dissolve:
        xoffset 270 yoffset 80
    "As she spoke, Yukinoshita directed her gaze somewhere else. That was of course at that person, who was happily chatting with Hiratsuka-sensei and Meguri-senpai."
    hide yui
    $url = ["yui school_sunset mid_left pout", "yui school_sunset mid_center happy"]
    $multiImagePara = [-270, 75, -305, 75, 1.8]
    call multiImage(1, False) from _call_multiImage_63
    voice "audio/voice/E4/CMM/05/YI/YI013.ogg"
    yui "Ah... b-but, if you think of it as the Service Club going!"
    call finishmultiImage from _call_finishmultiImage_67
    show yui school_sunset mid_center happy at right:
        xoffset -305 yoffset 75
    show yukino mid_center pout with dissolve:
        xoffset 25
    voice "audio/voice/E4/CMM/05/YK/YK006.ogg"
    yukino "That's... Even so..."
    show yukino happy with dissolve
    voice "audio/voice/E4/CMM/05/YK/YK007.ogg"
    yukino "... In any case, let's finish cleaning up."
    show yui mid_left sad with dissolve:
        xoffset -270
    voice "audio/voice/E4/CMM/05/YI/YI014.ogg"
    yui "Y-yeah..."
    hide yukino
    hide yui
    with dissolve
    jump E4_G01_01

label E4_CMM_05_SAKI:
    # saki route branch here
    stop music fadeout 1.0
    play music "audio/bgm/BGM14.ogg"
    show saki school_light_sunset far_right vhappy at center:
        xoffset -325 yoffset 75
    show keika heavy_coat_sunset far happy at center:
        xoffset 245 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/05/SA/SA001.ogg"
    saki "Alright, got your jacket on. Kei-chan, did you forget anything?"
    voice "audio/voice/E4/CMM/05/KE/KE001.ogg"
    keika "Nope! Is Saa-chan also ready?"
    voice "audio/voice/E4/CMM/05/SA/SA002.ogg"
    saki "Yup. Today was pretty fun, right?"
    show keika vhappy with dissolve
    voice "audio/voice/E4/CMM/05/KE/KE002.ogg"
    keika "Keika made amazing truffles!"
    voice "audio/voice/E4/CMM/05/SA/SA003.ogg"
    saki "Yes, you were very good Kei-chan. What do you say we eat them after dinner?"
    hachiman "(Ah... It's time to go home I guess. Come to think of it, it's almost dinner time.)"
    voice "audio/voice/E4/CMM/05/KE/KE003.ogg"
    show keika happy with dissolve
    keika "Ah? Haa-chan!!"
    hide saki
    hide keika
    with dissolve
    show keika heavy_coat_sunset mid happy at center with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E4/CMM/05/HA/HA012.ogg"
    hachiman "Oh, what's up Kei-chan?"
    show keika vhappy with dissolve
    voice "audio/voice/E4/CMM/05/KE/KE004.ogg"
    keika "Come with us, come with us!"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    jump E4_SAK_04

label E4_CMM_05_HAR_MEG:
    hachiman "(On that note, the main culprits invloved in detail sorting of this discussion...)"
    show hiratsuka school_light_sunset mid_center happy at left:
        xoffset -15 yoffset 75
    show meguri school_sunset mid happy at center:
        xoffset 25 yoffset 75
    show haruno sweater_sunset mid_left happy at right:
        xoffset -110 yoffset 75
    with dissolve
    voice "audio/voice/E4/CMM/05/HR/HR001.ogg"
    haruno "Meguri, you even knew about a lodge they used? I didn't even know about stuff like that."
    show meguri vhappy with dissolve
    voice "audio/voice/E4/CMM/05/MG/MG002.ogg"
    meguri "Ehehe. I just remembered that. I found it when I was organazing the materials for the previous Student Council."
    voice "audio/voice/E4/CMM/05/HR/HR002.ogg"
    haruno "...Speaking of which, they don't use it often, do they? That lodge."
    voice "audio/voice/E4/CMM/05/SZ/SZ002.ogg"
    hiratsuka "No, it must have been regularly tended to in order to maintain it. It's just that the school hasn't really used it before, so with some light cleaning, it can work out as a spot."
    hachiman "(Is cleaning the lodge some hidden agenda here?)"
    jump E4_HAR_05

label E4_CMM_05_IRO:
    hide yukino
    hide yui
    hide iroha
    with dissolve
    play music "audio/bgm/BGM36.ogg"
    show iroha school_sunset mid_center unimpressed at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/CMM/05/IR/IR010.ogg"
    iroha "What's with the long face, senpai?"
    voice "audio/voice/E4/CMM/05/HA/HA010.ogg"
    hachiman "I'm just regretting endorsing you for president... don't you think you're a bit too powerful?"
    show iroha happy with dissolve
    voice "audio/voice/E4/CMM/05/IR/IR011.ogg"
    iroha "Am I now~? I think  a trip like this will be a lot of fun for everyone, though. And besides..."
    hide iroha with dissolve
    show iroha school_sunset near_center vhappy at center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E4/CMM/05/IR/IR012.ogg"
    iroha "You'll take responsibility, won't you?"
    voice "audio/voice/E4/CMM/05/HA/HA011.ogg"
    hachiman "Ah, what the hell. I'll think about it at home and I'll see what I can do."
    show iroha unimpressed with dissolve
    voice "audio/voice/E4/CMM/05/IR/IR013.ogg"
    iroha "That makes it sound like it won't happen..."
    hide iroha with dissolve
    show iroha school_sunset mid_center happy at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/CMM/05/IR/IR014.ogg"
    iroha "But I'm still looking forward to hearing the good news. I'm counting on you!"
    jump E4_IRO_06
