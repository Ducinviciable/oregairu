label E1_HAR_01:
    hachiman "(I feel a scary or some kind of ominous presence from the opposite side... I could only think of one person who has that kind of presence but hell, I'm really afraid.)"
    "Perhaps, it's just me overthinking it. Anyways, Komachi and I head towards the shrine."
    window auto hide dissolve
    stop ambient fadeout 0.5
    scene shrine with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    hachiman "(I wish for Komachi to pass her exams. Also, please let this bad sign go away, for the world to be in peace!)"
    voice "audio/voice/E1/HAR/01/HA/HA000.ogg"
    hachiman "Is that enough for now, Komachi?"
    hide komachi
    $url = ["komachi coat mid_center happy", "komachi coat mid_center pout"]
    $multiImagePara = [245, 75, 0, 0, 10.2]
    call multiImage(0) from _call_multiImage_88
    voice "audio/voice/E1/HAR/01/KO/KO000.ogg"
    komachi "Yep, I'm done~ ...You're acting weird, onii-chan. What's wrong?"
    call finishmultiImage from _call_finishmultiImage_92
    show komachi coat near_center pout at center with dissolve:
        xoffset 245 yoffset 75
    voice "audio/voice/E1/HAR/01/HA/HA001.ogg"
    hachiman "No, nothing..."
    hachiman "(This restlessness... How am I going to explain this, it's like my instinct is telling me that I am going to be eaten by my foe in any moment now...)"
    voice "audio/voice/E1/HAR/01/HR/HR000.ogg"
    stop music fadeout 0.5
    mystery "...Oh, well if it isn't Hikigaya-kun!"
    hachiman "(This voice...)"
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_13.ogg"
    show transition_1a at offscreenright:
        parallel:
            easein 0.1 xpos -780
    play sound "audio/sfx/SE01/SE01_13.ogg"
    $renpy.pause(delay=0.5, hard=True)
    scene market
    show haruno coat mid_center vhappy at left:
        xoffset 260 yoffset 75
    show meguri coat mid happy at center:
        xoffset 265 yoffset 75
    show transition_1a at offscreenright:
        xpos -780
        parallel:
            easein 0.1 xpos -3500
    $renpy.pause(delay=0.15,hard=True)
    play music "audio/bgm/BGM35.ogg"
    $renpy.pause(delay=0.5,hard=True)
    window auto show dissolve
    voice "audio/voice/E1/HAR/01/HR/HR001.ogg"
    haruno "Yahallo! Hikigaya-kun!"
    hachiman "(Wah, she's here...)"
    "That is Yukino Yukinoshita's older sister, whose appearance and skills are flawless, who reeks of danger and whatever she thinks is something that I don't even
        comprehend, Haruno Yukinoshita."
    show meguri vhappy with dissolve
    voice "audio/voice/E1/HAR/01/MG/MG000.ogg"
    meguri "Happy New Year, Hikigaya-kun!"
    "And beside her, smiling, was the previous Student Council President, MeguMegurin. Ahh, her aura is powerful... and so soothing... It's Shiromeguri Meguri-senpai."
    voice "audio/voice/E1/HAR/01/HA/HA002.ogg"
    hachiman "Ah, thanks..."
    show haruno happy with dissolve
    voice "audio/voice/E1/HAR/01/HR/HR002.ogg"
    haruno "As usual, your face is telling me that even New Year's doesn't matter to you. But, you came for the first shrine visit this year? Good boy."
    voice "audio/voice/E1/HAR/01/HA/HA003.ogg"
    hachiman "Well, it's because my sister's exams are coming up."
    show meguri happy with dissolve
    show komachi coat near_left happy at right with dissolve:
        xoffset 190 yoffset 65
    voice "audio/voice/E1/HAR/01/MG/MG001.ogg"
    meguri "Ah, your little sister's exams, huh~"
    voice "audio/voice/E1/HAR/01/KO/KO002.ogg"
    komachi "Ah, yep, that's right."
    show haruno vhappy with dissolve:
    voice "audio/voice/E1/HAR/01/HR/HR003.ogg"
    haruno "Oh, Komachi-chan~"
    show komachi vhappy with dissolve:
    voice "audio/voice/E1/HAR/01/KO/KO003.ogg"
    komachi "It's been a while, Haruno-san! Please take care of my stupid brother this year as well-no, please take care of him in the coming years as well!"
    show haruno happy with dissolve:
    voice "audio/voice/E1/HAR/01/HR/HR004.ogg"
    haruno "Sure, same here. Let's get along for years to come. I see, exams, eh~"
    show komachi happy with dissolve:
    voice "audio/voice/E1/HAR/01/KO/KO004.ogg"
    komachi "Yes, Komachi's really anxious about them... so I dragged my brother here with me to pray for success."
    show haruno vhappy with dissolve:
    voice "audio/voice/E1/HAR/01/HR/HR005.ogg"
    haruno "Fufu. I see that you're really no match for Komachi, Hikigaya-kun."
    voice "audio/voice/E1/HAR/01/HA/HA004.ogg"
    hachiman "Yeah, my little sister is invincible."
    hachiman "(I mean, if Komachi's normally talking with Haruno-san like that, I think she's really invincibl...)"
    voice "audio/voice/E1/HAR/01/MG/MG002.ogg"
    meguri "Where are you taking your exams, Komachi-chan? Private school?"
    voice "audio/voice/E1/HAR/01/KO/KO005.ogg"
    komachi "Sobu High!"
    show meguri vhappy with dissolve:
    voice "audio/voice/E1/HAR/01/MG/MG003.ogg"
    meguri "I see~ If you passed, then you'll become our kouhai~"
    show haruno happy with dissolve:
    voice "audio/voice/E1/HAR/01/HR/HR006.ogg"
    haruno "Meguri and I are, at least, alumni of Sobu High, so you can always depend on us. Ah, Meguri hasn't graduated yet so calling her 'alumnus' isn't right, huh?"
    voice "audio/voice/E1/HAR/01/MG/MG004.ogg"
    meguri "Ehehe. I may be a graduate this year, but I'm free so I can give you some advice whenever~"
    voice "audio/voice/E1/HAR/01/KO/KO006.ogg"
    komachi "Waaah, thank you very much! Komachi feels super encouraged!"
    hachiman "(I can't wait to get out of here~~)"
    show haruno vhappy with dissolve:
    voice "audio/voice/E1/HAR/01/HR/HR007.ogg"
    haruno "Hikigaya-kun, you should take good care of your little sister. Being an examinee is tough."
    voice "audio/voice/E1/HAR/01/HA/HA005.ogg"
    hachiman "Haa, I'd rather steadily look over her progress instead."
    voice "audio/voice/E1/HAR/01/MG/MG005.ogg"
    meguri "Ahaha. That's very you, Hikigaya-kun."
    hachiman "(Ahhh, I feel like I could stay here as much as I want due to Meguri-senpai's Meguri-effect…)"
    hide haruno
    $url = ["haruno coat mid_center surprised", "haruno coat mid_center happy"]
    $multiImagePara = [260, 75, 0, 0, 4.0]
    call multiImage(-1) from _call_multiImage_80
    voice "audio/voice/E1/HAR/01/HR/HR008.ogg"
    haruno "Hm? Oh, that's Yukino-chan. I'll go greet her."
    call finishmultiImage from _call_finishmultiImage_84
    show haruno coat mid_center happy at left:
        xoffset 260 yoffset 75
    voice "audio/voice/E1/HAR/01/HA/HA006.ogg"
    hachiman "Ah, please tell Yukinoshita I said \"Hi\"..."
    hide haruno
    $url = ["haruno coat mid_center annoyed", "haruno coat mid_center happy"]
    $multiImagePara = [260, 75, 0, 0, 2.0]
    call multiImage(-1) from _call_multiImage_81
    voice "audio/voice/E1/HAR/01/HR/HR009.ogg"
    haruno "How about you tell her yourself? Well then, see you two later. Komachi-chan, the two of us should hang out together next time~"
    call finishmultiImage from _call_finishmultiImage_85
    show haruno coat mid_center happy at left:
        xoffset 260 yoffset 75
    show komachi vhappy with dissolve:
    voice "audio/voice/E1/HAR/01/KO/KO007.ogg"
    komachi "Yes, I would love to~"
    show meguri happy with dissolve:
    voice "audio/voice/E1/HAR/01/MG/MG006.ogg"
    meguri "See you both later then~"
    hide haruno
    hide meguri
    hide komachi
    with dissolve
    show komachi coat near_left happy at center with dissolve:
        xoffset 35 yoffset 65
    voice "audio/voice/E1/HAR/01/HA/HA007.ogg"
    hachiman "...How about we go home, too?"
    show komachi near_center happy at center with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E1/HAR/01/KO/KO008.ogg"
    komachi "Right~."
    window auto hide dissolve
    stop voice
    stop music fadeout 1
    scene sidewalkA with Fade(1.0, 0.5, 1.0)
    play sound "audio/sfx/SE00/SE00_18L.ogg"
    play music "audio/bgm/BGM21.ogg"
    show komachi coat mid_center angry at center with dissolve:
        xoffset -75 yoffset 75
    window auto show dissolve
    voice "audio/voice/E1/HAR/01/KO/KO009.ogg"
    komachi "Hey, hey, onii-chan."
    voice "audio/voice/E1/HAR/01/HA/HA008.ogg"
    hachiman "Hm?"
    voice "audio/voice/E1/HAR/01/KO/KO010.ogg"
    komachi "Haruno-san has a totally different vibe than Yukino-san, doesn't she?"
    voice "audio/voice/E1/HAR/01/HA/HA009.ogg"
    hachiman "She sure does."
    show komachi pout with dissolve
    voice "audio/voice/E1/HAR/01/KO/KO011.ogg"
    komachi "Hmm, but onii-chan, Haruno-san seems to be really interested in you, don't you think?"
    voice "audio/voice/E1/HAR/01/HA/HA010.ogg"
    hachiman "Hey, stop saying scary things. That's just her teasing me."
    show komachi happy with dissolve
    voice "audio/voice/E1/HAR/01/KO/KO012.ogg"
    komachi "Ahh, I guess so. Haruno-san looks like a strong person. I feel like she can swallow someone like onii-chan whole!"
    hachiman "(I knew it, Komachi certainly has an eye for people.)"
    voice "audio/voice/E1/HAR/01/HA/HA011.ogg"
    hachiman "She's actually scary."
    show komachi angry with dissolve
    voice "audio/voice/E1/HAR/01/KO/KO013.ogg"
    komachi "...Be careful, onii-chan."
    voice "audio/voice/E1/HAR/01/HA/HA012.ogg"
    hachiman "Can you stop saying stuff like that with such a serious tone all of a sudden?"
    voice "audio/voice/E1/HAR/01/HA/HA013.ogg"
    hachiman "I have a feeling this year won't be a good one for me..."
    window auto hide dissolve
    stop voice
    stop music fadeout 1
    jump E1_CMM_02

label E1_HAR_02:
    scene cafeA:
        zoom 1.5 xalign 0 ypos -310
    with Fade(1.0, 0.5, 1.0)
    play music ["<silence 0.3>", "audio/bgm/BGM47.ogg"]
    show haruno sweater mid_center vhappy at center:
        xoffset 10 yoffset 75
    show hayama coat mid_center relieved behind haruno at left:
        xoffset 35 yoffset 75
    show yui home mid_center pout at right:
        xoffset -175 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E1/HAR/02/YI/YI000.ogg"
    yui "............"
    voice "audio/voice/E1/HAR/02/HY/HY000.ogg"
    hayama "...A birthday present, huh?"
    show haruno vhappy with dissolve
    voice "audio/voice/E1/HAR/02/HR/HR000.ogg"
    haruno "How about I give her one too? It's been a while~"
    voice "audio/voice/E1/HAR/02/HA/HA000.ogg"
    hachiman "...Uh."
    show haruno happy with dissolve
    voice "audio/voice/E1/HAR/02/HA/HA001.ogg"
    hachiman "...I guess this really means we're hostages, huh?"
    voice "audio/voice/E1/HAR/02/HR/HR001.ogg"
    haruno "Hm, you could say that. But wouldn't it make a wonderful story if she rushed here for the sake of her friends who were captured on her behalf?"
    voice "audio/voice/E1/HAR/02/HA/HA002.ogg"
    hachiman "That makes me wonder who the 'tyrant king' is here..."
    show haruno vhappy with dissolve
    voice "audio/voice/E1/HAR/02/HR/HR002.ogg"
    haruno "Oh, we've got a Literature Boy over here."
    show hayama relieved with dissolve
    voice "audio/voice/E1/HAR/02/HY/HY001.ogg"
    hayama "............"
    show yui home mid_left pout at right with dissolve:
        xoffset -145 yoffset 75
    voice "audio/voice/E1/HAR/02/YI/YI001.ogg"
    yui "\"Tyrant...king...\"?"
    show hayama coat mid_right happy at left with dissolve:
        xoffset 5 yoffset 65
    voice "audio/voice/E1/HAR/02/HY/HY002.ogg"
    hayama "It's from \"Run, Melos!\""
    show yui happy with dissolve
    voice "audio/voice/E1/HAR/02/YI/YI002.ogg"
    yui "Oh, ooh, that one! Where the guy runs super fast!"
    hachiman "(Yuigahama, I don't think you get it...)"
    show yui home mid_center surprised at right with dissolve:
        xoffset -175 yoffset 75
    voice "audio/voice/E1/HAR/02/YI/YI003.ogg"
    yui "...! Ah, Yukinon!"
    window auto hide dissolve
    hide hayama
    hide haruno
    hide yui
    scene cafeA:
        zoom 2.0 xalign 1.0 ypos -225
    show yukino coat near_left unimpressed at center:
        xoffset 85 yoffset 80
    with dissolve
    window auto show dissolve
    voice "audio/voice/E1/HAR/02/YK/YK000.ogg"
    yukino "...So you two really are here."
    voice "audio/voice/E1/HAR/02/YI/YI004.ogg"
    yui "Ahaha. Uhm, well, Hikki and I were just shopping and we ended up getting caught..."
    show yukino pout with dissolve
    voice "audio/voice/E1/HAR/02/YK/YK001.ogg"
    yukino "Shopping...? I, I see..."
    voice "audio/voice/E1/HAR/02/YI/YI005.ogg"
    yui "A-anyway, come and sit down too, Yukinon!"
    window auto hide dissolve
    hide yukino with dissolve
    play sound "audio/sfx/SE01/SE01_12.ogg"
    $renpy.pause(delay=1.0, hard=True)
    scene cafeA:
        zoom 1.5 xpos -250 ypos -300
    show haruno sweater mid_center happy at left:
        xoffset 125 yoffset 75
    show yui home mid_center pout at center:
        xoffset 5 yoffset 75
    show yukino home mid_left frown at right:
        xoffset -40 yoffset 80
    with dissolve
    window auto show dissolve
    voice "audio/voice/E1/HAR/02/HR/HR003.ogg"
    haruno "............"
    voice "audio/voice/E1/HAR/02/YK/YK002.ogg"
    yukino "............"
    voice "audio/voice/E1/HAR/02/YI/YI006.ogg"
    yui "............"
    show yukino happy with dissolve
    voice "audio/voice/E1/HAR/02/HR/HR004.ogg"
    haruno "............"
    show yukino sad with dissolve
    voice "audio/voice/E1/HAR/02/YK/YK003.ogg"
    yukino "I'm sorry my older sister was a bother to you."
    show yui happy with dissolve
    voice "audio/voice/E1/HAR/02/YI/YI007.ogg"
    yui "Oh no, not at all."
    voice "audio/voice/E1/HAR/02/HA/HA003.ogg"
    hachiman "It's okay. We had nothing to do anyway."
    show yukino vhappy with dissolve
    voice "audio/voice/E1/HAR/02/YK/YK004.ogg"
    yukino "...I see."
    show haruno vhappy with dissolve
    voice "audio/voice/E1/HAR/02/HR/HR005.ogg"
    haruno "It's been a while since we've had tea like this."
    voice "audio/voice/E1/HAR/02/HY/HY003.ogg"
    hayama "Yeah, it has."
    show yukino angry with dissolve
    voice "audio/voice/E1/HAR/02/YK/YK005.ogg"
    yukino "Such gall... To think you called me out like this all the way here..."
    show haruno happy with dissolve
    voice "audio/voice/E1/HAR/02/HR/HR006.ogg"
    haruno "But you came here pretty fast."
    show yukino surprised with dissolve
    voice "audio/voice/E1/HAR/02/YK/YK006.ogg"
    yukino "That's...!"
    voice "audio/voice/E1/HAR/02/HR/HR007.ogg"
    haruno "Were you that worried about Hikigaya-kun and Gahama-chan?"
    show yukino blush with dissolve
    voice "audio/voice/E1/HAR/02/YK/YK007.ogg"
    yukino "That's not..."
    show yui pout with dissolve
    hachiman "(Oh man, this is scary, I don't want to interfere, but... Yukinoshita came here for our sake so...)"
    voice "audio/voice/E1/HAR/02/HA/HA004.ogg"
    hachiman "W-well, Yukinoshita also had plans so she couldn't come in the first place."
    show yukino vhappy with dissolve
    voice "audio/voice/E1/HAR/02/YK/YK008.ogg"
    yukino "Y-yes. That's right..."
    show haruno sly with dissolve
    voice "audio/voice/E1/HAR/02/HR/HR008.ogg"
    haruno "Hmmm. But Yukino-chan came anyway, huh?"
    show yukino frown with dissolve
    voice "audio/voice/E1/HAR/02/YK/YK009.ogg"
    yukino "............"
    show haruno vhappy with dissolve
    voice "audio/voice/E1/HAR/02/HR/HR009.ogg"
    haruno "Since you came all the way here, you'll come join us, right?"
    show haruno sly with dissolve
    voice "audio/voice/E1/HAR/02/HR/HR010.ogg"
    haruno "Or... are you going home instead?"
    show yukino pout with dissolve
    voice "audio/voice/E1/HAR/02/YK/YK010.ogg"
    yukino "............"
    show yui sad with dissolve
    voice "audio/voice/E1/HAR/02/YI/YI008.ogg"
    yui "Yukinon..."
    hachiman "(Yukinoshita isn't saying anything... I don't think we can go home at this rate...)"
    voice "audio/voice/E1/HAR/02/HY/HY004.ogg"
    hayama "Well, Haruno-san, don't you think it's time we let the two go?"
    show haruno worried with dissolve
    voice "audio/voice/E1/HAR/02/HR/HR011.ogg"
    haruno "Eeeh, since Hikigaya-kun and Gahama-chan are here, they should join us too~!"
    show yukino angry with dissolve
    voice "audio/voice/E1/HAR/02/YK/YK011.ogg"
    yukino "...Enough already, nee-san."
    show haruno happy with dissolve
    voice "audio/voice/E1/HAR/02/HR/HR012.ogg"
    haruno "Well, if that's what Yukino-chan wants~"
    voice "audio/voice/E1/HAR/02/HA/HA005.ogg"
    hachiman "...Guess we'll head home then."
    show yukino sad with dissolve
    voice "audio/voice/E1/HAR/02/YK/YK012.ogg"
    yukino "...Right."
    show yui surprised with dissolve
    voice "audio/voice/E1/HAR/02/YI/YI009.ogg"
    yui "Hikki! 'That'! Aren't we forgetting 'that'!?"
    voice "audio/voice/E1/HAR/02/HA/HA006.ogg"
    hachiman "Huh? Ahhh."
    show yukino surprised with dissolve
    voice "audio/voice/E1/HAR/02/YK/YK013.ogg"
    yukino "............"
    play sound "audio/sfx/SE01/SE01_09.ogg"
    $renpy.pause(delay=1.0, hard=False)
    show yui vhappy with dissolve
    voice "audio/voice/E1/HAR/02/YI/YI010.ogg"
    yui "Yukino, here, your present!"
    voice "audio/voice/E1/HAR/02/YK/YK014.ogg"
    yukino "...Eh?"
    show yui happy with dissolve
    voice "audio/voice/E1/HAR/02/YI/YI011.ogg"
    yui "I know it's a bit early, but it's your birthday tomorrow. Right, Hikki?"
    voice "audio/voice/E1/HAR/02/HA/HA007.ogg"
    hachiman "Yeah, Happy Birthday."
    show yukino happy with dissolve
    voice "audio/voice/E1/HAR/02/YK/YK015.ogg"
    yukino "T-thank you..."
    show haruno annoyed with dissolve
    show yui vhappy with dissolve
    voice "audio/voice/E1/HAR/02/YI/YI012.ogg"
    yui "Ehe... We just bought it a little while ago, though."
    show yukino vhappy with dissolve
    voice "audio/voice/E1/HAR/02/YK/YK016.ogg"
    yukino "Is that so?"
    window auto hide dissolve
    hide haruno
    hide yui
    hide yukino
    scene cafeA:
        zoom 2.0 xalign 0 ypos -430
    show haruno sweater near_center annoyed at center:
        xoffset -20 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E1/HAR/02/HR/HR013.ogg"
    haruno "Hmmm...?"
    voice "audio/voice/E1/HAR/02/HA/HA008.ogg"
    hachiman "What is it?"
    show haruno angry with dissolve
    voice "audio/voice/E1/HAR/02/HR/HR014.ogg"
    haruno "Nothing..."
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_12.ogg"
    $renpy.pause(delay=0.5, hard=True)
    hide haruno
    scene cafeA:
        zoom 1.5 xalign 1.0 ypos -310
    show haruno sweater mid_center angry at left:
        xoffset 10 yoffset 75
    show yukino home mid_center vhappy at center:
        xoffset -105 yoffset 75
    show yui coat mid_center happy at right:
        xoffset -115 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E1/HAR/02/YI/YI013.ogg"
    yui "W-we'll celebrate your birthday more at school, okay?"
    voice "audio/voice/E1/HAR/02/HA/HA009.ogg"
    hachiman "See you later."
    voice "audio/voice/E1/HAR/02/YK/YK017.ogg"
    yukino "Yes. See you..."
    window auto hide dissolve
    stop voice fadeout 0.5
    hide haruno
    hide yukino
    scene stationA with Fade(1.0, 0.5, 1.0)
    show yui coat mid_center pout at center with dissolve:
        xoffset 35 yoffset 75
    window auto show dissolve
    voice "audio/voice/E1/HAR/02/YI/YI014.ogg"
    yui "Fu~u... Yukino has it rough, huh..."
    voice "audio/voice/E1/HAR/02/HA/HA010.ogg"
    hachiman "Yeah, it made me sick to my stomach."
    show yui happy with dissolve
    voice "audio/voice/E1/HAR/02/YI/YI015.ogg"
    yui "B-but I'm glad we got to give her her present, I guess."
    voice "audio/voice/E1/HAR/02/HA/HA011.ogg"
    hachiman "Yeah."
    hachiman "(But I'm seriously tired...)"
    window auto hide dissolve
    stop music fadeout 0.5
    call loading_screen(3, "33") from _call_haruno_sweater_loading
    jump E2_CMM_01