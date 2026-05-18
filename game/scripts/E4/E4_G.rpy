label E4_G02_01:
    scene kitchenA with Fade(1.0, 1.0, 1.0)
    play ambient "audio/sfx/SE05/SE05_02L.ogg"
    play music "audio/bgm/BGM40.ogg"
    if hayamaTalk:
        window auto show dissolve
        hachiman "(Ah, I can feel the bitter aftertaste...)"
    show hayama school far_right happy at center:
        xoffset -230 yoffset 65
    show yumiko school far_center blush at center:
        xoffset 215 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E4/G02/01/YM/YM000.ogg"
    yumiko "H-Hayato... Do you mind... tasting this?"
    show hayama vhappy with dissolve
    voice "audio/voice/E4/G02/01/HY/HY000.ogg"
    hayama "Of course, if you're fine with me."
    hide yumiko
    $url = ["yumiko school far_center blush", "yumiko school far_left blush"]
    $multiImagePara = [215, 75, 240, 75, 1.0]
    call multiImage(0, False) from _call_multiImage_64
    voice "audio/voice/E4/G02/01/YM/YM001.ogg"
    yumiko "Yeah...! Yeah."
    call finishmultiImage from _call_finishmultiImage_68
    show yumiko school far_left blush at center:
        xoffset 240 yoffset 75
    image iroha school far_left vhappy flat = Flatten(" iroha school far_left vhappy")
    show iroha school far_left vhappy flat at center behind hayama:
        xoffset 100 yoffset 80 alpha 0
        parallel:
            easein 0.5 xoffset -25
        parallel:
            linear 0.5 alpha 1.0
    $renpy.pause(delay=0.35, hard=True)
    show hayama surprised:
        easein 0.5 xoffset -400
    show yumiko surprised:
        easein 0.5 xoffset 405
    voice "audio/voice/E4/G02/01/IR/IR000.ogg"
    iroha "Hayama-senpai! Please try some of this!"
    show hayama relieved
    show yumiko unimpressed
    with dissolve
    voice "audio/voice/E4/G02/01/HY/HY001.ogg"
    hayama "I wonder if I can eat all this."
    hide hayama
    hide iroha
    hide yumiko
    with dissolve
    show tobe school far vhappy at center with dissolve:
        xoffset -195 yoffset 75
    voice "audio/voice/E4/G02/01/TB/TB000.ogg"
    tobe "Hayato-kun, if you can't take anymore, I can take them anytime."
    show iroha school far_left vhappy at center with dissolve:
        xoffset 215 yoffset 80
    voice "audio/voice/E4/G02/01/IR/IR001.ogg"
    iroha "No, there's none for you, Tobe-senpai."
    show tobe sly with dissolve
    voice "audio/voice/E4/G02/01/TB/TB001.ogg"
    tobe "Irohasu, aren't you cruel!? Hayato-kun."
    hide iroha with dissolve
    show hayama school far_center happy at center behind tobe with dissolve:
        xoffset 195 yoffset 65
    voice "audio/voice/E4/G02/01/HY/HY002.ogg"
    hayama "Thanks for your offer, but you should focus on eating some from over there."
    show tobe vhappy
    show hayama vhappy
    with dissolve
    "Hayama whispered in Tobe's ear. As he did, Tobe gave him a thumbs up and smiled."
    hachiman "(Ha, I see. I'm going to guess those checkered cookies were made by Ebina-san. That's unexpected... and the person in question was watching.)"
    hide tobe
    hide hayama
    with dissolve
    $url = ["ebina school far_left annoyed", "ebina school far_left relieved1"]
    $multiImagePara = [-30, 75, 0, 0, 3.3]
    call multiImage() from _call_multiImage_65
    voice "audio/voice/E4/G02/01/EB/EB000.ogg"
    ebina "HayaTobe, huh... I'm not getting it."
    call finishmultiImage from _call_finishmultiImage_69
    show ebina school far_left relieved at center:
        xoffset -30 yoffset 75
    with dissolve
    hachiman "(Really? I think HayaTobe is good enough. It's definitely better than HayaHachi anyway.)"
    hachiman "(And if I said that, I'm going to get pulled into this coupling, So instead I'm going to fade out from here.)"
    hide ebina with dissolve
    stop music fadeout 0.5
    $renpy.pause(delay=1.0, hard=False)
    play music "audio/bgm/BGM46.ogg"
    "As I leaned back on the wall at a corner in the room, I deeply sighed. I haven't done anything special, but I felt tired nonetheless."
    "But I should have been feeling more satisfied than this."
    "Listening to Miura, Ebina, and the Kawasaki sisters' requests, holding an event with Isshiki and the lot, and interacting with Orimoto, Kaihin General School, and both Meguri-senpai and Haruno-san."
    "Hayama and Tobe also fulfilled their roles as tasters, Totsuka came, and Hiratsuka-sensei gave us gifts."
    "It was definitely enough. \"This sure is fun\", were the words stuck in my throat."
    "I felt a strong itch crawling around the back of my neck and the ends of my mouth were fixed up in place. It was probably because of the cold."
    show haruno sweater near_center vhappy at center with dissolve:
        xoffset -20 yoffset 75
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    voice "audio/voice/E4/G02/01/HR/HR000.ogg"
    haruno "... This is really fun, isn't it."
    hide haruno with dissolve
    play sound "audio/sfx/SE01/SE01_13.ogg"
    show haruno sweater mid_center vhappy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E4/G02/01/HA/HA000.ogg"
    hachiman "Woah! That scared me!"
    play music "audio/bgm/BGM35.ogg"
    hide haruno
    $url = ["haruno sweater mid_center vhappy", "haruno sweater near_center vhappy"]
    $multiImagePara = [10, 75, -20, 75, 3.4]
    call multiImage(0, False) from _call_multiImage_66
    voice "audio/voice/E4/G02/01/HR/HR001.ogg"
    haruno "To Hikigaya-kun who worked hard to make this fun event... Here, your reward."
    call finishmultiImage from _call_finishmultiImage_70
    show haruno sweater near_center vhappy at center:
        xoffset -20 yoffset 75
    voice "audio/voice/E4/G02/01/HA/HA001.ogg"
    hachiman "Eh-"
    "When Haruno-san's soft fingers touched my lips, she pressed something into my mouth. Those slender white fingers softly stroked my lips before retreating."
    hachiman "(J-just what...!?)"
    voice "audio/voice/E4/G02/01/HR/HR002.ogg"
    haruno"How is it? Good?"
    hide haruno with dissolve
    show yukino school mid_center surprised at left:
        xoffset -105 yoffset 75
    show yui school mid_center surprised at center:
        xoffset -25 yoffset 75
    show iroha school mid_center surprised at right:
        xoffset -190 yoffset 75
    with dissolve
    voice "audio/voice/E4/G02/01/MI/MIX000.ogg"
    yukandyuiandiro "...!!"
    hide yukino
    hide yui
    hide iroha
    with dissolve
    show haruno sweater near_center sly at center with dissolve:
        xoffset -20 yoffset 75
    voice "audio/voice/E4/G02/01/HA/HA002.ogg"
    hachiman "... I-it's good, um yes?"
    show hayama school mid_right pout behind haruno at left with dissolve:
        xoffset -60 yoffset 65
    voice "audio/voice/E4/G02/01/HY/HY003.ogg"
    hayama "............"
    hide hayama with dissolve
    "It certainly was good. The chocolate had this bittersweet taste from exquisite macha. Just the scent of its sweetness was satiating enough as it crumbled atop my tongue."
    voice "audio/voice/E4/G02/01/HA/HA003.ogg"
    hachiman "... Um, what was that all of a sudden?"
    show haruno vhappy with dissolve
    voice "audio/voice/E4/G02/01/HR/HR003.ogg"
    haruno "Hm? Was something weird? Ah, the taste? Maybe it's because I tried using different seeds."
    voice "audio/voice/E4/G02/01/HA/HA004.ogg"
    hachiman "No, not about the taste..."
    show haruno sly with dissolve
    voice "audio/voice/E4/G02/01/HR/HR004.ogg"
    haruno "Then everything's fine. Here, one more. Say \"ah\"."
    voice "audio/voice/E4/G02/01/HA/HA005.ogg"
    hachiman "No, I can eat it by myself so I'll decline."
    show haruno vhappy with dissolve
    voice "audio/voice/E4/G02/01/HR/HR005.ogg"
    haruno "This is also your reward! You've tolerated this until now so you may as well until the end. Here, say \"ahh\"."
    voice "audio/voice/E4/G02/01/HA/HA006.ogg"
    hachiman "If this is tolerating then wouldn't this be a penalty-game?"
    show haruno happy with dissolve
    voice "audio/voice/E4/G02/01/HR/HR006.ogg"
    haruno "It might be. Wasn't today kind of like a penalty-game for you anyway?"
    voice "audio/voice/E4/G02/01/HA/HA007.ogg"
    hachiman "... Life itself is like a penalty-game, not just today."
    show haruno vhappy with dissolve
    voice "audio/voice/E4/G02/01/HR/HR007.ogg"
    haruno "I quite like that about you."
    hide haruno with dissolve
    show yukino school mid_center frown at left with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E4/G02/01/YK/YK001.ogg"
    yukino "Nee-san, that's enough. Is it fun teasing that thing?"
    show haruno sweater mid_center sly at right with dissolve:
        xoffset -300 yoffset 75
    voice "audio/voice/E4/G02/01/HR/HR008.ogg"
    haruno "It's rather fun for those feeling troubled though." #Sounds fishy
    hachiman "(I'm feeling troubled too though...)"
    window auto hide dissolve
    #load screen in the original with haruno
    call loading_screen(3) from _call_loading_screen_5
    jump E4_CMM_05

label E4_G13_05:
    scene scouncilroomA with Fade(2.0, 1.0, 2.0)
    play music "audio/bgm/BGM08.ogg"
    window auto show dissolve
    "In response to many maidens' feelings, the Student Council and the Service Club came together and the \"Chocolate Tasting Event\" was now in the works."
    "In line with that, we, the Service Club, were to follow along with preparations, but..."
    show iroha school mid_left at right with dissolve:
        xoffset -190 yoffset 65
    voice "audio/voice/E4/G13/01/IR/IR000.ogg"
    iroha "Now then, I'll be leaving the menu selection and list of ingredients to you, Yuigahama-senpai, Yukinoshita-senpai!"
    show yukino school mid_center happy at left:
        xoffset -105 yoffset 75
    show yui school mid_center happy at center:
        xoffset -25 yoffset 75
    with dissolve
    voice "audio/voice/E4/G13/05/YK/YK000.ogg"
    yukino "Sure, we'll handle it."
    voice "audio/voice/E4/G13/01/YI/YI000.ogg"
    yui "Yeah! Leave it to us!"
    show iroha vhappy with dissolve
    voice "audio/voice/E4/G13/01/IR/IR001.ogg"
    iroha "The Student Council will do the approving and the announcements."
    show iroha happy with dissolve
    voice "audio/voice/E4/G13/01/IR/IR002.ogg"
    iroha "Ah, I'm also thinking of making this a joint event with Kaihin High. That way we can take from their budget as well!"
    hachiman "(She is sly in various ways, but she is acting as a proper Student Council President.)"
    hachiman "(Wait, noting for me to do? Maybe I can handle some individual advertising of the event?)"
    hide yukino
    hide iroha
    hide yui
    with dissolve
    stop music fadeout 1.0
    if totsukaTalkFlag == "yukino": #Yukino route
        show yukino school mid_center happy at center with dissolve:
            xoffset -105 yoffset 75
        play music "audio/bgm/BGM11.ogg"
        voice "audio/voice/E4/G13/05/YK/YK001.ogg"
        yukino "... Hikigaya-kun, do you have a moment?"
        voice "audio/voice/E4/G13/01/HA/HA000.ogg"
        hachiman "Hm? Something wrong?"
        show yukino vhappy with dissolve
        voice "audio/voice/E4/G13/05/YK/YK002.ogg"
        yukino "I want to hear your thoughts to use as a reference for the menu. From a regular boy's standpoint, what kind of chocolates would they prefer?"
        show yukino pout with dissolve
        voice "audio/voice/E4/G13/05/YK/YK003.ogg"
        yukino "Ah, I'm sorry. There was no deep meaning when I said \"regular\". I wasn't particularly meaning to make a taunt..."
        voice "audio/voice/E4/G13/01/HA/HA001.ogg"
        hachiman "Concentrating on that is already taunting though..."
        voice "audio/voice/E4/G13/01/HA/HA002.ogg"
        hachiman "Ah, well I think anyone would be happy they got anything at all."
        show yukino happy with dissolve
        voice "audio/voice/E4/G13/05/YK/YK004.ogg"
        yukino "I'd like a more specific opinion. Truffles, brownies... Something like those?"
        voice "audio/voice/E4/G13/01/HA/HA003.ogg"
        hachiman "Just the mushrooms and a xylophone-wielding monster come to mind..."
        show yukino unimpressed1 with dissolve
        voice "audio/voice/E4/G13/05/YK/YK005.ogg"
        yukino "..."
        show yukino concerned with dissolve
        voice "audio/voice/E4/G13/05/YK/YK006.ogg"
        yukino "It seems asking you for your opinion was wrong... Forget I asked."
        voice "audio/voice/E4/G13/01/HA/HA004.ogg"
        hachiman "Wait just a minute. You're mistaken about something. Regular guys don't know much about different kinds of chocolates in the first place."
        hide yukino
        $url = ["yukino school mid_center surprised", "yukino school mid_center angry"]
        $multiImagePara = [-105, 75, 0, 0, 3.0]
        call multiImage() from _call_multiImage_67
        voice "audio/voice/E4/G13/05/YK/YK007.ogg"
        yukino "...! That is a point. Then I'll change my question."
        call finishmultiImage from _call_finishmultiImage_71
        show yukino school mid_center angry at center:
            xoffset -105 yoffset 75
        voice "audio/voice/E4/G13/01/HA/HA005.ogg"
        hachiman "What, now it's kind of become like an interrogation?"
        show yukino happy with dissolve
        voice "audio/voice/E4/G13/05/YK/YK008.ogg"
        yukino "A vague image will do. Like what kind of taste."
        voice "audio/voice/E4/G13/01/HA/HA006.ogg"
        hachiman "Well, that'll also depend on the person as well. There are guys that don't like sweet things and guys that do."
        hide yukino
        $url = ["yukino school mid_center unimpressed", "yukino school mid_center angry"]
        $multiImagePara = [-105, 75, 0, 0, 3.5]
        call multiImage() from _call_multiImage_68
        voice "audio/voice/E4/G13/05/YK/YK009.ogg"
        yukino "I see, that is true... Then, can I ask one more thing?"
        call finishmultiImage from _call_finishmultiImage_72
        show yukino school mid_center angry at center:
            xoffset -105 yoffset 75
        voice "audio/voice/E4/G13/01/HA/HA007.ogg"
        hachiman "What, this was an interrogation after all?"
        show yukino blush with dissolve
        voice "audio/voice/E4/G13/05/YK/YK010.ogg"
        yukino "Um... What kind of chocolate do you like...?"
        hachiman "(N-no... if you ask me like that, it makes me a bit uncomfortable...)"
        voice "audio/voice/E4/G13/01/HA/HA008.ogg"
        hachiman "... Sorry to say the same thing, but I think they'll be happy just to receive something. Especially if it's from my little sister."
        show yukino unimpressed with dissolve
        voice "audio/voice/E4/G13/05/YK/YK011.ogg"
        yukino "... It seems I did ask the wrong person after all."
        show iroha school mid_center unimpressed at right:
            xoffset -190 yoffset 75
        with dissolve
        voice "audio/voice/E4/G13/01/IR/IR003.ogg"
        iroha "Senpai, that totally creeped me out."
        voice "audio/voice/E4/G13/01/HA/HA009.ogg"
        hachiman "Better get used to it quickly."
        #jump here i think. probably based on route
        hide yukino
        hide iroha
        with dissolve
        stop music fadeout 0.5
        jump E4_YUK_01

    elif totsukaTalkFlag == "iroha":
        play music "audio/bgm/BGM36.ogg"
        show iroha school mid_center unimpressed at center with dissolve:
            xoffset -5 yoffset 75
        voice "audio/voice/E4/G13/01/IR/IR004.ogg"
        iroha "Senpai, help us if you've got nothing to do~"
        voice "audio/voice/E4/G13/01/HA/HA017.ogg"
        hachiman "Even if you say that, I can't help you with making chocolates."
        show iroha happy with dissolve
        voice "audio/voice/E4/G13/01/IR/IR005.ogg"
        iroha "Ah, not with that. I want to make a poster we can hand out at school, so I want you to give that some thought. Come on, isn't Japanese like, your strong suit, senpai?"
        voice "audio/voice/E4/G13/01/HA/HA018.ogg"
        hachiman "I don't really see the connection here..."
        voice "audio/voice/E4/G13/01/IR/IR006.ogg"
        iroha "I want you to think of a catch-phrase to stick on it. And make it something the Student Council will approve of."
        show iroha vhappy with dissolve
        voice "audio/voice/E4/G13/01/IR/IR007.ogg"
        iroha "It's okay if you just slap something together. That's your specialty, right, senpai?"
        voice "audio/voice/E4/G13/01/HA/HA019.ogg"
        hachiman "That way of asking a favour is the worst, but I get the idea. A catch-phrase, huh... Something like \"Grand Operation Chocolate\" or \"Maidens in Love, Assemble!\". Like that?"
        show iroha school mid_left unimpressed at center with dissolve:
            xoffset -35 yoffset 65
        voice "audio/voice/E4/G13/01/IR/IR008.ogg"
        iroha "The hell was that? 5 points."
        show yukino school mid_left unimpressed at right with dissolve:
            xoffset -40 yoffset 80
        voice "audio/voice/E4/G13/05/YK/YK013.ogg"
        yukino "2 points."
        show yui school mid_right vhappy at left with dissolve:
            xoffset -105 yoffset 75
        voice "audio/voice/E4/G13/01/YI/YI011.ogg"
        yui "10 points!"
        voice "audio/voice/E4/G13/01/HA/HA020.ogg"
        hachiman "What's the max points anyway? And besides, have you got any better ideas yourselves?"
        show yui happy with dissolve
        voice "audio/voice/E4/G13/01/YI/YI012.ogg"
        yui "Iroha-chan, I think we can manage without some eye-catching catch-phrase, you know?"
        voice "audio/voice/E4/G13/01/IR/IR009.ogg"
        iroha "Eh, we can? But how do we make people come to the event..."
        show yukino happy with dissolve
        voice "audio/voice/E4/G13/05/YK/YK014.ogg"
        yukino "This event seems to have been decided upon with participation in mind. Meaning we don't have to actively recruit participants, do we?"
        show iroha school mid_center sad at center with dissolve:
            xoffset -5 yoffset 75
        voice "audio/voice/E4/G13/01/IR/IR010.ogg"
        iroha "Right... But we'd get more bang for the buck if we got a huge crowd to come..."
        hachiman "(She's really capable when it comes to that...)"
        window auto hide dissolve
        stop music fadeout 0.5
        jump E4_IRO_01

    elif totsukaTalkFlag == "yui":
        play music "audio/bgm/BGM12.ogg"
        show yui school mid_left pout at center with dissolve:
            xoffset 0 yoffset 75
        voice "audio/voice/E4/G13/01/YI/YI001.ogg"
        yui "Hmm. Hmm..."
        voice "audio/voice/E4/G13/01/HA/HA010.ogg"
        hachiman "What're you groaning for?"
        show yui school mid_center pout at center with dissolve:
            xoffset 0 yoffset 75
        voice "audio/voice/E4/G13/01/YI/YI002.ogg"
        yui "All the chocolate looks delicious, so I can't decide! Hikki, which do you think is good?"
        voice "audio/voice/E4/G13/01/HA/HA011.ogg"
        hachiman "Which? They all look the same to me."
        show yui school mid_center frown at center with dissolve:
            xoffset 0 yoffset 75
        voice "audio/voice/E4/G13/01/YI/YI003.ogg"
        yui "It's not! This chocolate cookie, this chocolate cake, and this here is a chocolate mousse~!"
        voice "audio/voice/E4/G13/01/HA/HA012.ogg"
        hachiman "Oh? So, what taste is ths one?"
        $url = ["yui school mid_center unimpressed", "yui school mid_center happy"]
        $multiImagePara = [0, 75, 0, 0, 2.5]
        call multiImage() from _call_multiImage_E4_YUI_G_1
        voice "audio/voice/E4/G13/01/YI/YI004.ogg"
        yui "Huh? They're all chocolate?"
        call finishmultiImage from _call_finishmultiImage_E4_YUI_G_1
        show yui school mid_center happy at center:
            yoffset 75
        voice "audio/voice/E4/G13/01/HA/HA013.ogg"
        hachiman "So they are all the same..."
        show yui school mid_center angry at center with dissolve:
            xoffset 0 yoffset 75
        voice "audio/voice/E4/G13/01/YI/YI005.ogg"
        yui "Y-You're wrong! They have to be different!"
        show yui school mid_center frown at center with dissolve:
            xoffset 0 yoffset 75
        voice "audio/voice/E4/G13/01/YI/YI006.ogg"
        yui "Geez, it's harder to pick now because of you!"
        voice "audio/voice/E4/G13/01/HA/HA014.ogg"
        hachiman "Well, guys would be happy regardless of what kind of chocolate they get..."
        show yui school mid_center sad at center with dissolve:
            xoffset 0 yoffset 75
        voice "audio/voice/E4/G13/01/YI/YI007.ogg"
        yui "Huh...? Hikki, is that how you feel?"
        hachiman "(Even if you ask with those upturned, pup eyes, my answer won't change...)"
        voice "audio/voice/E4/G13/01/HA/HA015.ogg"
        hachiman "Well, that's just in general. I just assume everyone's like that."
        $url = ["yui school mid_center angry", "yui school mid_right unimpressed"]
        $multiImagePara = [0, 75, 0, 0, 3.7]
        call multiImage() from _call_multiImage_E4_YUI_G_2
        voice "audio/voice/E4/G13/01/YI/YI008.ogg"
        yui "In general... Everyone... I'm guessing you'd be different then."
        call finishmultiImage from _call_finishmultiImage_E4_YUI_G_2
        show yui school mid_right unimpressed at center:
            yoffset 75
        voice "audio/voice/E4/G13/01/HA/HA016.ogg"
        hachiman "Hey? In general, I fall inside the generalities, so if you're talking generally, I'm your everyday normal guy."
        $url = ["yui school mid_center happy", "yui school mid_center blush"]
        $multiImagePara = [0, 75, 0, 0, 2.9]
        call multiImage() from _call_multiImage_E4_YUI_G_3
        voice "audio/voice/E4/G13/01/YI/YI009.ogg"
        yui "I see. That's good then. Ah, but that doesn't exactly help me!"
        call finishmultiImage from _call_finishmultiImage_E4_YUI_G_3
        show yui school mid_center blush at center:
            yoffset 75
        show yukino school mid_center happy at left with dissolve:
            xoffset -150 yoffset 75
        voice "audio/voice/E4/G13/05/YK/YK012.ogg"
        yukino "Yuigahama-san, it'd be fine if you just pick something you would be able to make. That'll narrow the list of candidates, too, so there's no need to hesitate."
        show yui school mid_left pout at center with dissolve:
            xoffset 0 yoffset 75
        voice "audio/voice/E4/G13/01/YI/YI010.ogg"
        yui "That's not the kind of follow-up I needed, Yukinon!"
        hachiman "(There're actually quite a lot of types of chocolate when you think about it.)"
        jump E4_YUI_01

label E4_G01_01:
    $renpy.pause(delay=0.5,hard=False)
    #some rustling sfx here
    play sound "audio/sfx/SE01/SE01_64.ogg"
    $renpy.pause(delay=1.0,hard=False)
    show iroha school_sunset mid_center happy at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/G01/01/IR/IR000.ogg"
    iroha "Could you take the trash outside, senpai? We have a spot for them..."
    voice "audio/voice/E4/G01/01/HA/HA000.ogg"
    hachiman "Can I take this much?"
    hide iroha
    $url = ["iroha school_sunset mid_center happy", "iroha school_sunset mid_left pout"]
    $multiImagePara = [-5, 75, -35, 65, 2.5]
    call multiImage(0, False) from _call_multiImage_69
    voice "audio/voice/E4/G01/01/IR/IR001.ogg"
    iroha "Yes. Ah, with that take that one and this one..."
    call finishmultiImage from _call_finishmultiImage_73
    show iroha school_sunset mid_left pout at center:
        xoffset -35 yoffset 65
    voice "audio/voice/E4/G01/01/HA/HA001.ogg"
    hachiman "Yeah, hold your horses. Let me take this out first."
    window auto hide dissolve
    stop voice
    scene black with lefttransition
    #placeholder pause
    play sound "audio/sfx/SE04/SE04_08.ogg"
    $renpy.pause(delay=1.5, hard=True)
    stop sound
    #soft sliding door sfx (squeak at end)
    play sound "audio/sfx/SE01/SE01_64.ogg"
    $renpy.pause(delay=2.0,hard=False)
    stop sound
    window auto show dissolve
    hachiman "(The trash is pretty heavy... Looks like my waist is going to hurt tomorrow.)"
    window auto hide dissolve
    #soft sliding door2 sfx (longer, with a thud at end)
    play sound "audio/sfx/SE04/SE04_07.ogg"
    scene kitchenB with CropMove(0.4, mode="wipeleft")
    $renpy.pause(delay=3.0,hard=False)
    stop sound
    show kaori school_sunset mid vhappy at center with dissolve:
        xoffset -25 yoffset 75
    window auto show dissolve
    voice "audio/voice/E4/G01/01/OR/OR000.ogg"
    kaori "Ah, Hikigaya. What, are you cleaning up? Hilarious!"
    voice "audio/voice/E4/G01/01/HA/HA002.ogg"
    hachiman "It really isn't... I'm just doing clean up."
    voice "audio/voice/E4/G01/01/OR/OR001.ogg"
    kaori "I mean, come on! Your whole image is so different from middle school. You'd never participate in stuff like this in the first place."
    voice "audio/voice/E4/G01/01/HA/HA003.ogg"
    hachiman "Well, I just went with the flow on this one... Are you cleaning up, too?"
    show kaori happy with dissolve
    voice "audio/voice/E4/G01/01/OR/OR002.ogg"
    kaori "Yeah. I just finished washing dishes and stuff."
    voice "audio/voice/E4/G01/01/HA/HA004.ogg"
    hachiman "Oh, okay..."
    hachiman "(Let's see, the remaining trash is...)"
    show kaori vhappy with dissolve
    voice "audio/voice/E4/G01/01/OR/OR003.ogg"
    kaori "Ah, by the way. Hikigaya, did you get chocolate from those two?"
    hachiman "(Trash, where are you~?)"
    voice "audio/voice/E4/G01/01/HA/HA005.ogg"
    hachiman "Aren't Yukinoshita and Yuigahama just giving each other chocolate?"
    show kaori happy with dissolve
    voice "audio/voice/E4/G01/01/OR/OR004.ogg"
    kaori "Oh~? So you do know them..."
    stop music fadeout 1.0
    voice "audio/voice/E4/G01/01/HA/HA006.ogg"
    hachiman "Huh!?"
    show kaori vhappy with dissolve
    play music "audio/bgm/BGM44.ogg"
    voice "audio/voice/E4/G01/01/OR/OR005.ogg"
    kaori "I mean, you're surrounded by a lot of girls. Like Isshiki-chan and those graduate students."
    hachiman "(Was that a leading question?)"
    voice "audio/voice/E4/G01/01/HA/HA007.ogg"
    hachiman "Well, in a place like this, I have to have obligatory conversations. Now too, see?"
    show kaori closed with dissolve
    voice "audio/voice/E4/G01/01/OR/OR006.ogg"
    kaori "Hm... Obligatory conversations, huh..."
    show kaori vhappy with dissolve
    voice "audio/voice/E4/G01/01/OR/OR007.ogg"
    kaori "Anyway, which of them are you going out with?"
    voice "audio/voice/E4/G01/01/HA/HA008.ogg"
    hachiman "I'm not going out with either of them..."
    show kaori happy with dissolve
    voice "audio/voice/E4/G01/01/OR/OR008.ogg"
    kaori "Hmm... Then, which one of them do you like?"
    voice "audio/voice/E4/G01/01/HA/HA009.ogg"
    hachiman "............"
    "That's a similarily surprising question as before. I couldn't give an immediate reply this time. My breath got caught deep in my throat and I was unable to give a quick retort."
    "Speaking of surprises, this silence might've been much more surprising. Maybe because Orimoto found it strange that I didn't reply. She looked at me with a curious look on her face."
    "But then her expression suddenly changed into the apologeic, wry smile one she'd had just before."
    show kaori vhappy with dissolve
    voice "audio/voice/E4/G01/01/OR/OR009.ogg"
    kaori "Well, whatever."
    show kaori happy with dissolve
    voice "audio/voice/E4/G01/01/OR/OR010.ogg"
    kaori "Then, if you could get chocolate either of them them, whose would you want?"
    voice "audio/voice/E4/G01/01/HA/HA010.ogg"
    hachiman "Huh? What's the point of that hypothetical?"
    show kaori annoyed with dissolve
    voice "audio/voice/E4/G01/01/OR/OR011.ogg"
    kaori "Eh, come on! Who cares? It's fine if we compare them via chocolates, right?"
    hachiman "(This girl's definitely finding this amusing. But I'll look self-conscious if I cut off the conversation now...)"
    voice "audio/voice/E4/G01/01/HA/HA011.ogg"
    hachiman "What does \"compare via chocolate\" mean?"
    show kaori vhappy with dissolve
    voice "audio/voice/E4/G01/01/OR/OR012.ogg"
    kaori "You know, like whose you'd rather try eating?"
    voice "audio/voice/E4/G01/01/HA/HA012.ogg"
    hachiman "............"
    stop music fadeout 3.0
    hachiman "(Just chocolate. We're only talking about chocolate. Let's just try zoning in on that chocolate for a bit...)"
    voice "audio/voice/E4/G01/01/HA/HA013.ogg"
    hachiman "Ah, well. If I had to pick..."
    menu yuki_yui_choco:
        hachiman "Ah, well. If I had to pick,"
        with dissolve
        "Yukinoshita I guess":
            $chocoEventChoice = "yukinoshita"
            play music "audio/bgm/BGM11.ogg"
            voice "audio/voice/E4/G01/01/HA/HA014.ogg"
            hachiman "... If I had to pick, I'd be interested in something that Yukinoshita made."
            "I was surprised myself after I said it. I don't think there's ever been a time I thought I wanted to receive anything from Yukinoshita Yukino."
            "An existence with whom we exchanged words, and at times felt like we were in some happy illusion where we shared something in common. Because that was who Yukinoshita Yukino was to me."
            "I don't push my ideals that she's a strong person on her anymore. It's just, we were closer than we were before - at least we should be."
            show kaori happy with dissolve
            voice "audio/voice/E4/G01/01/OR/OR013.ogg"
            kaori "Why?"
            hachiman "(I wonder why. The reason I want Yukinoshita's chocolate is...)"
            voice "audio/voice/E4/G01/01/HA/HA015.ogg"
            hachiman "Because in her case, she does things like a pro. She redefine what going all-out means."
            "While that was what you'd call a \"sound argument\", it was also an excuse. I understood that well as I said that."
            show kaori annoyed with dissolve
            voice "audio/voice/E4/G01/01/OR/OR014.ogg"
            kaori "What's with that...? Like a cooking showdown?"
            voice "audio/voice/E4/G01/01/HA/HA016.ogg"
            hachiman "No, she's not in a showdown. It's more like a matter of interest..."
            show kaori closed with dissolve
            voice "audio/voice/E4/G01/01/OR/OR015.ogg"
            kaori "That's kind of unexpected. Even you can be interested in other people. This might be the first time I've heard you compliment someone."
            voice "audio/voice/E4/G01/01/HA/HA017.ogg"
            hachiman "No, just interested, okay? And wait, I do compliment. I do, okay?"
            show kaori happy with dissolve
            voice "audio/voice/E4/G01/01/OR/OR016.ogg"
            kaori "I wonder about that. Well whatever. Be nice if you get some. Okay, I'm going back after I finish up."
            voice "audio/voice/E4/G01/01/HA/HA018.ogg"
            hachiman "S-sure..."
            hide kaori with dissolve
            hachiman "(... Well, that's true. She probably gets people expressing interest and the like more than others. I doubt I'm wrong about that.)"
            hachiman "(Oh right, taking care of the trash...)"
            window auto hide dissolve
            stop music fadeout 1.0
            scene black with Fade(1.0, 1.5, 0)
            play sound "audio/sfx/SE01/SE01_64.ogg"
            #some rustling sfx
            #loading screen with yukino, images/bg/EC_BG36B.jpg
            #reference https://www.youtube.com/watch?v=ANz8YpMwO6A&t=13m15s 13minutes 15s
            image yukino school mid_center angry_flat = Flatten("yukino school mid_center angry")
            scene kitchenLoading with Fade(1.0, 2, 1.0)
            stop sound
            $renpy.pause(delay=2.0, hard=True)
            show yukino school mid_center angry_flat at center:
                xoffset -345 yoffset 75 alpha 0
                parallel:
                    linear 0.5 alpha 1.0
                parallel:
                    easein 0.6 xoffset -465
                    linear 1.0 xoffset -345
            $renpy.pause(delay=2.0, hard=True)
            jump E4_YUK_04
        "Yuigahama I guess":
            $chocoEventChoice = "yui"
            play music "audio/bgm/BGM12.ogg"
            voice "audio/voice/E4/G01/01/HA/HA019.ogg"
            hachiman "If I had to say... Yuigahama."
            show kaori school_sunset mid happy at center with dissolve:
                xoffset -25 yoffset 75
            "I even surprised myself when her name came out of my mouth without much hesitation. Unfortunately, her sweets are pretty bad, but... No, exactly because of that."
            voice "audio/voice/E4/G01/01/HA/HA020.ogg"
            hachiman "Rather than saying I want to eat her sweets, it's more like I want to see her get better at it."
            "Yeah. It feels like a parental affection. Yukinoshita's sweets are always safe in that regard."
            show kaori mid annoyed at center with dissolve
            voice "<from 0 to 3.54>audio/voice/E4/G01/01/OR/OR017.ogg"
            kaori "What? Is Yuigahama that bad?"
            show kaori mid vhappy at center with dissolve
            voice "<from 3.54>audio/voice/E4/G01/01/OR/OR017.ogg"
            kaori "Hilarious."
            voice "audio/voice/E4/G01/01/HA/HA021.ogg"
            hachiman "It really isn't. And she's not that bad. She's not at level you can laugh at."
            voice "audio/voice/E4/G01/01/OR/OR018.ogg"
            kaori "That bad? That's hilarious. It's kind of surprising though."
            voice "audio/voice/E4/G01/01/HA/HA022.ogg"
            hachiman "Really? You'd think she's bad at it just based on how she looks."
            show kaori school_sunset mid happy at center with dissolve:
                xoffset -25 yoffset 75
            voice "audio/voice/E4/G01/01/OR/OR019.ogg"
            kaori "Not that, I'm talking about you, Hikigaya. I've never heard you talk about how bad someone was at something or how you wanna see them succeed. It threw me off a bit."
            voice "audio/voice/E4/G01/01/HA/HA023.ogg"
            hachiman "Ah, I mean, look, how should I say? It boiled my nii-san blood."
            show kaori mid vhappy at center with dissolve
            voice "audio/voice/E4/G01/01/OR/OR020.ogg"
            kaori "I see. You did have a little sister, Hikigaya. Okay! Well, anyway. Good on you. Well, I'm going home since I finished."
            voice "audio/voice/E4/G01/01/HA/HA024.ogg"
            hachiman "A-Alright..."
            hide kaori with dissolve
            hachiman "(Well, that' true. On it's face, she's just bad, but yet it weighs on my mind.)"
            hachiman "(When I'm always interested and looking though, she realizes she's always weighing on my mind.)"
            hachiman "(Right, the trash...)"
            stop music fadeout 1.0
            scene black with Fade(1.0, 1.5, 0)
            play sound "audio/sfx/SE01/SE01_64.ogg"
            $renpy.pause(delay=2.0, hard=True)
            jump E4_YUI_03
