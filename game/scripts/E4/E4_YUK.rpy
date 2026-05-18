label E4_YUK_01:
    play music "audio/bgm/BGM41.ogg"
    play sound "audio/sfx/SE01/SE01_08.ogg"
    $renpy.pause(delay=1,hard=True)
    play sound "audio/sfx/SE01/SE01_07.ogg"
    $renpy.pause(delay=1,hard=True)
    voice "audio/voice/E4/YUK/01/HA/HA000.ogg"
    hachiman "You brought in quite a lot again..."
    show yukino school mid_center vhappy at left:
        xoffset 25 yoffset 75
    show yui school mid_center happy at right:
        xoffset -300 yoffset 75
    with dissolve
    voice "audio/voice/E4/YUK/01/YI/YI000.ogg"
    yui "Yukinon! That's a lot of books on sweets!"
    voice "audio/voice/E4/YUK/01/YK/YK000.ogg"
    yukino "If we have this many, we can make an appropriate menu."
    play sound "audio/sfx/SE01/SE01_07.ogg"
    $renpy.pause(delay=0.5, hard=True)
    show yui mid_right vhappy with dissolve:
        xoffset -235 yoffset 75
    voice "audio/voice/E4/YUK/01/YI/YI001.ogg"
    yui "Seeing this, there sure are a lot of sweets that are made with chocolate. They all look good I know don't know which one to make!"
    play sound "audio/sfx/SE01/SE01_07.ogg"
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E4/YUK/01/YK/YK001.ogg"
    show yukino angry with dissolve
    yukino "That's right... We first need to pick the ones that look as if Yuigahama-san can make them."
    voice "audio/voice/E4/YUK/01/YI/YI002.ogg"
    show yui surprised with dissolve
    yui "That's your standard of how you're choosing!? Your kindness is sometimes painful!."
    play sound "audio/sfx/SE01/SE01_07.ogg"
    $renpy.pause(delay=0.5, hard=True)
    show yukino happy with dissolve
    voice "audio/voice/E4/YUK/01/YK/YK002.ogg"
    yukino "But little children will also be coming on the day, right? There's a definite need to consider the level of difficulty, and then there's the budget to think about too..."
    show yui mid_center surprised with dissolve:
        xoffset -300 yoffset 75
    voice "audio/voice/E4/YUK/01/YI/YI003.ogg"
    yui "And your follow-up makes sense!?"
    voice "audio/voice/E4/YUK/01/HA/HA001.ogg"
    hachiman "Didn't she just pass over it out of pity?"
    show yui frown with dissolve
    voice "audio/voice/E4/YUK/01/YI/YI004.ogg"
    yui "I-I can also make things better than before!... If I have Yukinon's guidance."
    play sound "audio/sfx/SE01/SE01_07.ogg"
    show yukino angry with dissolve
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E4/YUK/01/YK/YK003.ogg"
    yukino "Yes, if she follows the method, she should be able to make things more difficult than Kawasaki-san's little sister... Right, we should start by listing the things children can make first...."
    show yui mid_left sad with dissolve:
        xoffset -270 yoffset 75
    voice "audio/voice/E4/YUK/01/YI/YI005.ogg"
    yui "... I feel like I've been hit so casually..."
    voice "audio/voice/E4/YUK/01/HA/HA002.ogg"
    hachiman "Either way, half of it will be like a festival, so isn't there no need to aim to make things perfect?"
    play sound "audio/sfx/SE01/SE01_07.ogg"
    $renpy.pause(delay=0.5, hard=True)
    show yukino happy with dissolve
    voice "audio/voice/E4/YUK/01/YK/YK004.ogg"
    menu choco_tutorial_response:
        yukino "We can't have that. If nobody enjoys themself, then you can't call it a festival."
        with dissolve
        "Is that also including you?": #most yukino playthrough took this option
            stop music fadeout 1
            voice "audio/voice/E4/YUK/01/HA/HA003.ogg"
            hachiman "Does that include you?"
            show yukino surprised
            show yui surprised
            with dissolve
            play music "audio/bgm/BGM42.ogg"
            voice "audio/voice/E4/YUK/01/YK/YK005.ogg"
            yukino "...!"
            show yukino pout with dissolve
            voice "audio/voice/E4/YUK/01/YK/YK006.ogg"
            yukino "Since I'm... just a helper..."
            voice "audio/voice/E4/YUK/01/HA/HA004.ogg"
            hachiman "I can't speak for others but, shouldn't you think making it enjoyable for youself too?" #人のことは言えんが、自分も楽しめるように考えた方がいいんじゃないの？
            show yui happy with dissolve
            show yui mid_right vhappy with dissolve:
                xoffset -235 yoffset 75
            voice "audio/voice/E4/YUK/01/YI/YI006.ogg"
            yui "Me too, I agree with Hikki!"
            show yukino stare with dissolve
            voice "audio/voice/E4/YUK/01/YK/YK007.ogg"
            yukino "Yes... I'll take it into consideration."
            voice "audio/voice/E4/YUK/01/YK/YK014.ogg"
            yukino "So anyway, the menu... um..."
            show yui mid_center happy at right with dissolve:
                xoffset -300 yoffset 75
            jump E4_YUK_01_CTD
        "That's also true.":
            voice "audio/voice/E4/YUK/01/HA/HA005.ogg"
            hachiman "Well that's also true. However, that's limited to the attendees."
            voice "audio/voice/E4/YUK/01/YK/YK008.ogg"
            yukino "We'd be, what you call behind the scenes."
            show yui mid_center frown with dissolve:
                xoffset -300 yoffset 75
            voice "audio/voice/E4/YUK/01/YI/YI007.ogg"
            yui "Ehh? Isn't that kind of sad?"
            show yukino pout with dissolve
            voice "audio/voice/E4/YUK/01/YK/YK009.ogg"
            yukino "Is.. it?"
            hide yui with dissolve
            show yui school mid_right vhappy at center behind yukino with dissolve:
                xoffset -110 yoffset 75
            voice "audio/voice/E4/YUK/01/YI/YI008.ogg"
            yui "Yukinon, you should enjoy yourself too!"
            show yukino avoid with dissolve
            voice "audio/voice/E4/YUK/01/YK/YK010.ogg"
            yukino "O-okay..."
            voice "audio/voice/E4/YUK/01/YK/YK014.ogg"
            yukino "So anyway, the menu... um..."
            show yui mid_center happy at center with dissolve:
                xoffset -45 yoffset 75
            jump E4_YUK_01_CTD
        "A festival is sacrificing a part of...":
            "not done"
            jump choco_tutorial_response
            voice "audio/voice/E4/YUK/01/HA/HA006.ogg"
            hachiman "祭りとは元来、一部の犠牲を捧げることによってだな⋯⋯"
            voice "audio/voice/E4/YUK/01/YI/YI009.ogg"
            yui "なんかヒッキーが面倒くさそうなこと言い出した！？"
            voice "audio/voice/E4/YUK/01/YK/YK011.ogg"
            yukino "けれど、あながち間違ったことは言ってはいないわね"
            voice "audio/voice/E4/YUK/01/YI/YI010.ogg"
            yui "えっ、そうなの？"
            voice "audio/voice/E4/YUK/01/YK/YK012.ogg"
            yukino "ええ。古来、お祭りとは神に捧げるものだもの。何を捧げるかといえば⋯⋯"
            voice "audio/voice/E4/YUK/01/YI/YI011.ogg"
            yui "もういい！ もういいから！ 難しいことは知らない！ わかんない！"
            voice "audio/voice/E4/YUK/01/HA/HA007.ogg"
            hachiman "お、おう⋯⋯豪快な開き直り方だな⋯⋯"
            voice "audio/voice/E4/YUK/01/YI/YI012.ogg"
            yui "バレンタインはみんながハッピーな気持ちになるお祭りなの！ 古来とか元来とか関係ないの！ だからふたりとも楽しむこと！"
            voice "audio/voice/E4/YUK/01/YK/YK013.ogg"
            yukino "え、ええ⋯⋯"
            voice "audio/voice/E4/YUK/01/HA/HA008.ogg"
            hachiman "あっ、はい⋯⋯"
            jump E4_YUK_01_CTD

label E4_YUK_01_CTD:
    play sound "audio/sfx/SE01/SE01_07.ogg"
    $renpy.pause(delay=0.5, hard=True)
    show yukino angry with dissolve
    voice "audio/voice/E4/YUK/01/YK/YK015.ogg"
    yukino "Hikigaya-kun, could you get those tags?"
    voice "audio/voice/E4/YUK/01/HA/HA009.ogg"
    hachiman "You mean these? Here."
    show yukino vhappy with dissolve
    voice "audio/voice/E4/YUK/01/YK/YK016.ogg"
    yukino "Thank you."
    hide yukino
    hide yui
    with dissolve
    show yukino school near_center surprised at center with dissolve:
        xoffset -165 yoffset 75
    "I extend my hand holding the small tags. As I did, Yukinoshita also extended hers at the same time and our eyes met. Our fingers touched. When I could feel the faint heat-"
    play music "audio/bgm/BGM44.ogg"
    hide yukino
    $url = ["yukino school near_center surprised1", "yukino school near_left blush"]
    $multiImagePara = [-165, 75, 85, 80, 0.6]
    call multiImage(0, False) from _call_multiImage_6
    voice "audio/voice/E4/YUK/01/YK/YK017.ogg"
    yukino "S-Sorry..."
    call finishmultiImage from _call_finishmultiImage_7
    show yukino school near_left blush at center:
        xoffset 85 yoffset 80
    voice "audio/voice/E4/YUK/01/HA/HA010.ogg"
    hachiman "N-nah..."
    hide yukino with dissolve
    show yukino school mid_left blush at left:
        xoffset 270 yoffset 75
    show yui school mid_center surprised at right:
        xoffset -300 yoffset 75
    hachiman "(N-no... That was nothing. Our fingers just slightly touched is all... Why are you getting flustered? You're going to make me feel flustered!)"
    show yui blush with dissolve
    voice "audio/voice/E4/YUK/01/YI/YI013.ogg"
    yui "............"
    show yukino mid_center avoid at left with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E4/YUK/01/YK/YK018.ogg"
    yukino "............"
    voice "audio/voice/E4/YUK/01/HA/HA011.ogg"
    hachiman "............"
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    scene cafeCLoading with Fade(1.0, 2, 1.0)
    $renpy.pause(delay=2.0, hard=True)
    show yukino school mid_center happy flat at center:
        xoffset -345 yoffset 75 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.6 xoffset -465
            easeout 1.0 xoffset -345
    $renpy.pause(delay=3.0, hard=True)
    jump E4_YUK_02
    #loading scene using EC_BG21C.jpg in original with a yukino swipe. https://www.youtube.com/watch?v=B3y8dD-9Fw8 21:15 for animation info. POV change indicator

label E4_YUK_02:
    scene cafeC
    show yui school near_center happy at center:
        xoffset 10 yoffset 75
    with dissolve
    $renpy.pause(delay=0.5,hard=True)
    play sound "audio/sfx/SE01/SE01_08.ogg"
    $renpy.pause(delay=0.5,hard=True)
    play music "audio/bgm/BGM09.ogg"
    $renpy.pause(delay=0.5,hard=True)
    window auto show dissolve
    voice "audio/voice/E4/YUK/02/YK/YK000.ogg"
    yukino "... and that should do."
    show yui vhappy with dissolve
    voice "audio/voice/E4/YUK/02/YI/YI000.ogg"
    yui "Everyone will be able to enjoy themselves with this surely."
    voice "audio/voice/E4/YUK/02/YK/YK001.ogg"
    yukino "If so, that would be nice."
    show yui near_right happy with dissolve:
        xoffset -195 yoffset 70
    voice "audio/voice/E4/YUK/02/YI/YI001.ogg"
    yui "They definitely will!... There's something for me as well in the menu."
    show yui vhappy with dissolve
    voice "audio/voice/E4/YUK/02/YI/YI002.ogg"
    yui "It's a menu Yukinon worked hard on as well! It'll definitely be okay!"
    voice "audio/voice/E4/YUK/02/YK/YK002.ogg"
    yukino "It's thanks to your help."
    voice "audio/voice/E4/YUK/02/YI/YI003.ogg"
    yui "... R-really?"
    show yui surprised with dissolve
    voice "audio/voice/E4/YUK/02/YI/YI004.ogg"
    yui "... Huh? This book is..."
    voice "audio/voice/E4/YUK/02/YK/YK003.ogg"
    yukino "Ah... That's..."
    show yui near_left vhappy with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E4/YUK/02/YI/YI005.ogg"
    yui "Uwah, this looks really hard...  Are we making this at the event as well?"
    voice "audio/voice/E4/YUK/02/YK/YK004.ogg"
    yukino "No, that one's not for the event..."
    show yui surprised1 with dissolve
    voice "audio/voice/E4/YUK/02/YI/YI006.ogg"
    yui "...!"
    show yui near_right surprised with dissolve:
        xoffset -195 yoffset 70
    voice "audio/voice/E4/YUK/02/YI/YI007.ogg"
    yui "..."
    voice "audio/voice/E4/YUK/02/YK/YK005.ogg"
    yukino "No, um... I thought about trying out a new recipe, there's no deep meaning..."
    show yui vhappy with dissolve
    voice "audio/voice/E4/YUK/02/YI/YI008.ogg"
    yui "... I see. Yukinon, do your best."
    voice "audio/voice/E4/YUK/02/YK/YK006.ogg"
    yukino "Yuigahama... san?"
    show yui near_center vhappy with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E4/YUK/02/YI/YI009.ogg"
    yui "I wish I could help as well, but I'm not good at making sweets after all. So... I'll be supporting you."
    voice "audio/voice/E4/YUK/02/YK/YK007.ogg"
    yukino "Supporting...?"
    show yui near_right vhappy with dissolve:
        xoffset -195 yoffset 70
    voice "audio/voice/E4/YUK/02/YI/YI010.ogg"
    yui "Yep, supporting! Well, even though I say that, there won't be much I can actually do... Let's do our best okay, Yukinon?"
    voice "audio/voice/E4/YUK/02/YK/YK008.ogg"
    yukino "Um..."
    voice "audio/voice/E4/YUK/02/YK/YK009.ogg"
    yukino "... Yes. I'll try my best."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    image yukino school mid_center concerned flat = Flatten("yukino school mid_center concerned")
    scene loading_wlogo
    show yukino school mid_center concerned flat at center:
        xoffset -345 yoffset 75 alpha 1.0
        on hide:
            parallel:
                1.3
                linear 0.3 alpha 0
            parallel:
                easein 0.6 xoffset -285
                easeout 1.0 xoffset -465
    with Dissolve(1.0)
    $renpy.pause(delay=2.0, hard=True)
    hide yukino
    $renpy.pause(delay=3.0, hard=True)
    jump E4_CMM_02

label E4_YUK_03:
    voice "audio/voice/E4/YUK/03/YI/YI000.ogg"
    yui "Yukinon, it's okay to mix all of these together, right?"
    show yukino angry with dissolve
    voice "audio/voice/E4/YUK/03/YK/YK000.ogg"
    yukino "Wait, Yuigahama-san. It's still too early."
    show yui mid_left sad with dissolve:
        xoffset 285 yoffset 75
    voice "audio/voice/E4/YUK/03/YI/YI001.ogg"
    yui "Eeh!? Did I do something wrong!? The chocolate just went guwah...!"
    hachiman "(It looks like just the usual to me though...)"
    voice "audio/voice/E4/YUK/03/YK/YK001.ogg"
    yukino "It's fine, Yuigahama-san, Have you first sifted the flour properly? It looks like it's clumped up."
    show yui mid_right surprised with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E4/YUK/03/YI/YI002.ogg"
    yui "Eh!?"
    voice "audio/voice/E4/YUK/03/YK/YK002.ogg"
    yukino "Also, there's still hot water remaining in the boiled chocolate. And then..."
    hachiman "(There's too much jargon in there I don't get it... Yuigahama seemed to understand there was still a lot to get through.)"
    show yui mid_center sad at left with dissolve:
        xoffset 255 yoffset 75
    voice "audio/voice/E4/YUK/03/YI/YI003.ogg"
    yui "Why do I end up failing..."
    show yukino vhappy with dissolve
    voice "audio/voice/E4/YUK/03/YK/YK003.ogg"
    yukino "It's okay, Yuigahama-san. Let's check each step and try again."
    window auto hide dissolve
    stop voice
    hide yui
    hide yukino
    with dissolve
    $renpy.pause(delay=0.5, hard=True)
    scene kitchenA at truecenter:
        zoom 1.45 xoffset -2.5 yoffset -12.5
    show ebina school mid_center happy at left:
        xoffset 130 yoffset 75
    show yumiko school mid_center pout at center:
        xoffset -5 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E4/YUK/03/YM/YM000.ogg"
    yumiko "I'm done boiling the water. What do I have to do from here again?"

    image yukino school mid_left happy flat = Flatten("yukino school mid_left happy")
    image yukino school mid_center surprised flat = Flatten("yukino school mid_center surprised")

    show yukino school mid_left happy flat at right:
        xoffset 50 yoffset 80 alpha 0
        parallel:
            easein 0.5 xoffset -40
        parallel:
            linear 0.5 alpha 1.0
    $renpy.pause(delay=0.5, hard=True)
    hide yukino
    show yukino school mid_left happy at right:
        xoffset -40 yoffset 80
    voice "audio/voice/E4/YUK/03/YK/YK004.ogg"
    yukino "Have you already prepared an egg?"
    show yumiko mid_left happy with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/YUK/03/YM/YM001.ogg"
    yumiko "It's in the fridge."
    voice "audio/voice/E4/YUK/03/YK/YK005.ogg"
    yukino "Then let's go into making the texture. Separate the yolk from the egg white..."
    window auto hide dissolve
    scene kitchenA with dissolve
    window auto show dissolve
    show keika home mid pout at center with dissolve:
        xoffset 215 yoffset 75
    voice "audio/voice/E4/YUK/03/KE/KE000.ogg"
    keika "Hey, I want you to look at Keika's too."
    show yukino school mid_center surprised flat at left:
        xoffset -50 yoffset 75 alpha 0
        parallel:
            easein 0.5 xoffset 20
        parallel:
            linear 0.5 alpha 1.0
    $renpy.pause(delay=0.5, hard=True)
    hide yukino
    show yukino school mid_center surprised at left:
        xoffset 20 yoffset 75
    voice "audio/voice/E4/YUK/03/YK/YK006.ogg"
    yukino "Did something happen? Okay then, let's go..."
    show yumiko school far_left happy behind keika at center with dissolve:
        yoffset 30 yoffset 75
    show keika
    voice "audio/voice/E4/YUK/03/YM/YM002.ogg"
    yumiko "Ah, I'll be separating the egg."
    show yukino sad with dissolve
    voice "audio/voice/E4/YUK/03/YK/YK007.ogg"
    yukino "S-sure... Sorry, I'll be back soon."
    voice "audio/voice/E4/YUK/03/YM/YM003.ogg"
    yumiko "You don't really have to hurry."
    hide yumiko with dissolve
    show keika annoyed with dissolve
    voice "audio/voice/E4/YUK/03/KE/KE001.ogg"
    keika "Onee-chan?"
    show yukino vhappy with dissolve
    voice "audio/voice/E4/YUK/03/YK/YK008.ogg"
    yukino "Yes, let's go see it."
    hide yukino
    hide keika
    with dissolve
    show yui school mid_center pout at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E4/YUK/03/YI/YI004.ogg"
    yui "Yukinon looks like she has her hands full... I can't keep being a bother either!"
    voice "audio/voice/E4/YUK/03/HA/HA000.ogg"
    hachiman "... Well, it looks like Yukinoshita likes helping you bake though."
    show yui vhappy with dissolve
    voice "audio/voice/E4/YUK/03/YI/YI005.ogg"
    yui "Really?"
    show yui mid_left angry with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E4/YUK/03/YI/YI006.ogg"
    yui "Ah, no no, this isn't the time to be happy! I need to work hard too and complete this!"
    hide yui with dissolve
    show yui school mid_left angry at left:
        xoffset 285 yoffset 75
    show yukino school mid_center pout at right:
        xoffset -230 yoffset 75
    with dissolve
    voice "audio/voice/E4/YUK/03/YK/YK009.ogg"
    yukino "..."
    show yui mid_right surprised with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E4/YUK/03/YI/YI007.ogg"
    yui "Ah, Yukinon."
    show yukino happy with dissolve
    voice "audio/voice/E4/YUK/03/YK/YK010.ogg"
    yukino "It seems there's no problem where Kawasaki-san is. I'll have a look at Miura-san's then yours."
    show yui sad with dissolve
    voice "audio/voice/E4/YUK/03/YI/YI008.ogg"
    yui "Sorry, Yukinon..."
    show yukino mid_left happy with dissolve:
        xoffset -170 yoffset 80
    voice "audio/voice/E4/YUK/03/YK/YK011.ogg"
    yukino "It's nothing. First of all, can you measure the soft flour proportions then sift them?"
    show yui angry with dissolve
    voice "audio/voice/E4/YUK/03/YI/YI009.ogg"
    yui "Y-yeah! I'll show you I can do it well this time!"
    show yukino vhappy with dissolve
    voice "audio/voice/E4/YUK/03/YK/YK012.ogg"
    yukino "You don't have to worry so much. You become confused because you panic too much. Just be calm and do things one at a time."
    show yui sad with dissolve
    voice "audio/voice/E4/YUK/03/YI/YI010.ogg"
    yui "I might have been a bit too nervous..."
    show yui pout with dissolve
    stop music fadeout 1.5
    voice "audio/voice/E4/YUK/03/YI/YI011.ogg"
    yui "U-um, is yours going to be okay, Yukinon...?"
    show yukino pout with dissolve
    voice "audio/voice/E4/YUK/03/YK/YK013.ogg"
    yukino "............"
    play music "audio/bgm/BGM11.ogg"
    hide yui
    hide yukino
    with dissolve
    show haruno sweater far_left happy at center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E4/YUK/03/HR/HR000.ogg"
    haruno "Yukino-chan sure looks busy."
    hide haruno
    show yukino school mid_center unimpressed at left:
        xoffset 20 yoffset 75
    show haruno sweater mid_left happy at right:
        xoffset -240 yoffset 75
    with dissolve
    voice "audio/voice/E4/YUK/03/YK/YK014.ogg"
    yukino "Yes. That's why I don't have the time to entertain you."
    show haruno vhappy with dissolve
    voice "audio/voice/E4/YUK/03/HR/HR001.ogg"
    haruno "Yukino-chan, you're so cold!"
    show haruno mid_center sly with dissolve:
        xoffset -300 yoffset 75
    voice "audio/voice/E4/YUK/03/HR/HR002.ogg"
    haruno "Actually, will you be okay without making yours? It looks like Gahama-chan was worried about it as well."
    show yukino pout with dissolve
    voice "audio/voice/E4/YUK/03/YK/YK015.ogg"
    yukino "I..."
    hide yukino
    hide haruno
    with dissolve
    show yukino school mid_center pout at center with dissolve:
        xoffset -105 yoffset 75
    menu yuk_choco:
        hachiman "(Come to think of it, Yukinoshita...)"
        with dissolve
        "Well she's instructing today after all":
            "not finished"
            # voice "audio/voice/E4/YUK/03/HA/HA001.ogg"
            # hachiman ""
            # voice "audio/voice/E4/YUK/03/YK/YK016.ogg"
            # yukino ""
            jump yuk_choco
        "I thought you'd make some yourself": #Nost mnake this
            voice "audio/voice/E4/YUK/03/HA/HA002.ogg"
            hachiman "I thought for sure you'd make some yourself."
            show yukino happy with dissolve
            voice "audio/voice/E4/YUK/03/YK/YK017.ogg"
            yukino "Why... would you think that?"
            voice "audio/voice/E4/YUK/03/HA/HA003.ogg"
            hachiman "Nah, because you seemed like you would before. That you would make an example model to teach with. But anyway, in this situation..."
            show yukino pout with dissolve
            voice "audio/voice/E4/YUK/03/YK/YK018.ogg" #not sure when YK019 plays
            yukino "Yes, that's true. I thought about doing that, but it seems I had less time than I thought I would."
            hide yukino with dissolve
            show yui school mid_right sad at left:
                xoffset 20 yoffset 75
            show yukino school mid_left pout at right:
                xoffset -170 yoffset 80
            with dissolve
            voice "audio/voice/E4/YUK/03/YI/YI012.ogg"
            yui "Sorry! I'll do my best!"
            voice "audio/voice/E4/YUK/03/YI/YI014.ogg" #Not sure when YI013 plays
            yui "Um, Yukinon. I'll try more on my own, so..."
            show yukino vhappy with dissolve
            voice "audio/voice/E4/YUK/03/YK/YK020.ogg"
            yukino "No, don't worry about it. I only thought about making my own if I had the time from the start."
            hide yui
            hide yukino
            with dissolve
            show yui school mid_center pout at left:
                xoffset 130 yoffset 75
            show yukino school mid_left vhappy behind yui at center:
                xoffset 50 yoffset 80
            show haruno sweater mid_left sly behind yukino at right:
                xoffset -110 yoffset 75
            with dissolve
            voice "audio/voice/E4/YUK/03/HR/HR003.ogg"
            haruno "Then if you made some yourself, would you give it to someone?"
            show yukino mid_center pout with dissolve:
                xoffset -105 yoffset 75
            voice "audio/voice/E4/YUK/03/YK/YK021.ogg"
            yukino "............"
            show yukino annoyed with dissolve
            voice "audio/voice/E4/YUK/03/YK/YK022.ogg"
            yukino "That's none of your business. Nee-san, you as well. Why don't you go make your own?"
            show haruno happy with dissolve
            voice "audio/voice/E4/YUK/03/HR/HR004.ogg"
            haruno "True. I may as well try making some homemade chocolate while I'm here."
            stop music fadeout 1.0
            show haruno mid_center vhappy with dissolve:
                xoffset -170 yoffset 75
            voice "audio/voice/E4/YUK/03/HR/HR005.ogg"
            haruno "And then... I'll give it to Hikigaya-kun!"
            show yui mid_right surprised:
                xoffset -110 yoffset 75
            show yukino surprised
            with dissolve
            play music "audio/bgm/BGM35.ogg"
            voice "audio/voice/E4/YUK/03/YK/YK023.ogg"
            yukino "...!"
            voice "audio/voice/E4/YUK/03/HA/HA005.ogg"
            hachiman "...Eh?"
            voice "audio/voice/E4/YUK/03/HA/HA006.ogg"
            hachiman "N-nah, aren't there a lot of other people who'd want your chocolate?"
            show haruno happy with dissolve
            voice "audio/voice/E4/YUK/03/HR/HR006.ogg"
            haruno "Eh, that doesn't matter. This is something you give to someone you want to, not someone who wants it, no?"
            show yukino sad with dissolve
            voice "audio/voice/E4/YUK/03/YK/YK024.ogg"
            yukino "..."
            show haruno sly with dissolve
            voice "audio/voice/E4/YUK/03/HR/HR007.ogg"
            haruno "... Well, that only applies if there is someone you want to give it to though."
            show yui mid_center surprised with dissolve:
                xoffset 130 yoffset 75
            voice "audio/voice/E4/YUK/03/YI/YI015.ogg"
            yui "Yu-Yukinon, you're going to give it to me, right?"
            show yukino mid_left pout with dissolve:
                xoffset 50 yoffset 80
            voice "audio/voice/E4/YUK/03/YK/YK025.ogg"
            yukino "Yuigahama-san..."
            show haruno mid_left happy with dissolve:
                xoffset -110 yoffset 75
            voice "audio/voice/E4/YUK/03/HR/HR008.ogg"
            haruno "Gahama-chan, you can't spoil her."
            show yui mid_right surprised with dissolve:
                xoffset -110 yoffset 75
            voice "audio/voice/E4/YUK/03/YI/YI016.ogg"
            yui "N-no... That's not what I was..."
            show yukino mid_center annoyed with dissolve:
                xoffset -105 yoffset 75
            stop music fadeout 1.0
            voice "audio/voice/E4/YUK/03/YK/YK026.ogg"
            yukino "Nee-san, just stop there."
            show yukino mid_left pout with dissolve:
                xoffset 50 yoffset 80
            play music "audio/bgm/BGM11.ogg"
            voice "audio/voice/E4/YUK/03/YK/YK027.ogg"
            yukino "Yuigahama-san, I apologise for my sister. Then, I'll go have a look over there."
            hide yukino with dissolve
            show yui mid_center pout with dissolve:
                xoffset 130 yoffset 75
            voice "audio/voice/E4/YUK/03/YI/YI017.ogg"
            yui "Yukinon..."
            show haruno vhappy with dissolve
            voice "audio/voice/E4/YUK/03/HR/HR009.ogg"
            haruno "Yukino-chan hasn't changed at all."
            hide yui
            hide haruno
            with dissolve
            show haruno sweater mid_left vhappy at center with dissolve:
                xoffset -20 yoffset 75
            voice "audio/voice/E4/YUK/03/HA/HA007.ogg"
            hachiman "Are you a demon? Besides, you didn't need to bring me into this..."
            show haruno sweater mid_center with dissolve:
                xoffset 10 yoffset 75
            voice "audio/voice/E4/YUK/03/HR/HR010.ogg"
            haruno "... But if it wasn't you, then there wouldn't be a point, right?"
            voice "audio/voice/E4/YUK/03/HA/HA008.ogg"
            hachiman "...!"
            hide haruno with dissolve
            show haruno sweater near_center sly at center with dissolve:
                xoffset -20 yoffset 75
            voice "audio/voice/E4/YUK/03/HR/HR011.ogg"
            haruno "Okay then, see ya later, taster-san."
            hide haruno with dissolve
            hachiman "(Th-that was exhausting...)"
            window auto hide dissolve
            stop music fadeout 2.0
            stop ambient fadeout 2.0
            jump E4_G02_01
        "You've been quite busy":
            "not finished"
            jump yuk_choco

label E4_YUK_04:
    scene kitchenB
    show yui school_sunset mid_right vhappy at center:
        xoffset -110 yoffset 75
    with dissolve
    #with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    play music "audio/bgm/BGM09.ogg"
    voice "audio/voice/E4/YUK/04/YI/YI000.ogg"
    yui "Hey, Yukinon! The ski camp is exciting, isn't it?"
    voice "audio/voice/E4/YUK/04/YK/YK000.ogg"
    yukino "To be honest, it's disheartening..."
    show yui pout with dissolve
    voice "audio/voice/E4/YUK/04/YI/YI001.ogg"
    yui "Ah... Haruno-san looks like she's definitely willing to go too... That might be a little awkward?"
    voice "audio/voice/E4/YUK/04/YK/YK001.ogg"
    yukino "I'm sorry if she causes you trouble again."
    show yui vhappy with dissolve
    voice "audio/voice/E4/YUK/04/YI/YI002.ogg"
    yui "It's not like that at all! I'm just a little lost on how to react sometimes!"
    voice "audio/voice/E4/YUK/04/YK/YK002.ogg"
    yukino "So you are quite troubled..."
    show yui happy with dissolve
    voice "audio/voice/E4/YUK/04/YI/YI003.ogg"
    yui "Ah, no, I really don't mind! And I'm just looking forward to the ski camp."
    voice "audio/voice/E4/YUK/04/YK/YK003.ogg"
    yukino "I-is that so..."
    show yui school_sunset mid_center blush with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E4/YUK/04/YI/YI004.ogg"
    yui "I mean...! I can't quite say it well..."
    show yui sad with dissolve
    voice "audio/voice/E4/YUK/04/YI/YI005.ogg"
    yui "Being able to do something with everyone like this probably won't happen when we become third years too..."
    show yui vhappy with dissolve
    voice "audio/voice/E4/YUK/04/YI/YI006.ogg"
    yui "Also, this might be the last time it can be the three of us."
    voice "audio/voice/E4/YUK/04/YK/YK004.ogg"
    yukino "..."
    show yui pout with dissolve
    voice "audio/voice/E4/YUK/04/YI/YI007.ogg"
    yui "I don't want to think that way, but..."
    voice "audio/voice/E4/YUK/04/YK/YK005.ogg"
    yukino "... Right."
    show yui mid_right happy with dissolve:
        xoffset -110
    voice "audio/voice/E4/YUK/04/YI/YI008.ogg"
    yui "And there's that. From the ski resort, we can see the widening white landscape from snow."
    show yui vhappy with dissolve
    voice "audio/voice/E4/YUK/04/YI/YI009.ogg"
    yui "We've been through some stuff recently, so maybe this'll help us relax?"
    voice "audio/voice/E4/YUK/04/YK/YK006.ogg"
    yukino "Is that how it works...?"
    show yui happy with dissolve
    voice "audio/voice/E4/YUK/04/YI/YI010.ogg"
    yui "It is! Also..."
    show yui mid_center pout with dissolve:
        xoffset -25
    voice "audio/voice/E4/YUK/04/YI/YI011.ogg"
    yui "Because it's a place like that, I think there'll be something we'll be able to see and understand."
    show yui sad with dissolve
    voice "audio/voice/E4/YUK/04/YI/YI012.ogg"
    yui "If we become third-years, we'll definitely lose the time to be able to do something like this with everyone, along with other things, see, and it might become like it never happened."
    show yui pout with dissolve
    voice "audio/voice/E4/YUK/04/YI/YI013.ogg"
    yui "I just think something like that would be really sad."
    voice "audio/voice/E4/YUK/04/YK/YK007.ogg"
    yukino "It might..."
    show yui mid_right happy with dissolve:
        xoffset -110
    voice "audio/voice/E4/YUK/04/YI/YI014.ogg"
    yui "It would... Right, Yukinon?"
    hide yui
    show yui school_sunset near_center vhappy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E4/YUK/04/YK/YK008.ogg"
    yukino "... Eh? Ah, wai- Don't hug me so suddenly..."
    show yui blush with dissolve
    voice "audio/voice/E4/YUK/04/YI/YI015.ogg"
    yui "Yukinon, I'll be happy with just being able to stay with you... Just remember that."
    voice "audio/voice/E4/YUK/04/YK/YK009.ogg"
    yukino "... Thank you, Yuigahama-san."
    voice "audio/voice/E4/YUK/04/YI/YI016.ogg"
    yui "... Yeah."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    #dissolve generic loading screen with yukino and some transforms https://www.youtube.com/watch?v=ANz8YpMwO6A 16:17 for reference.
    image yukino school mid_center vhappy flat = Flatten("yukino school mid_center vhappy")
    scene loading_wlogo
    show yukino school mid_center vhappy flat at center:
        xoffset -345 yoffset 75 alpha 1.0
        on hide:
            parallel:
                1.3
                linear 0.3 alpha 0
            parallel:
                easein 0.6 xoffset -285
                easeout 1.0 xoffset -465
    with Dissolve(1.0)
    $renpy.pause(delay=2.0, hard=True)
    hide yukino
    $renpy.pause(delay=3.0, hard=True)
    jump E5_CMM_01
