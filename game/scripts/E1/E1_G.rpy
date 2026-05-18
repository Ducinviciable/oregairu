label E1_G01_01:
    window auto hide dissolve
    stop music fadeout 1.0
    scene market
    with Fade(1.0, 0.5, 1.0)
    play ambient "audio/sfx/SE05/SE05_00L.ogg"
    $renpy.pause(delay=1.5, hard=True)
    play music "audio/bgm/BGM08.ogg"
    window auto show dissolve
    voice "audio/voice/E1/G01/01/HA/HA000.ogg"
    hachiman "There's a lot of people here after all..."
    hide komachi
    $url = ["komachi coat near_center happy", "komachi coat near_center vhappy"]
    $multiImagePara = [245, 75, 0, 0, 6.7]
    call multiImage(0, True) from _call_multiImage_44
    voice "audio/voice/E1/G01/01/KO/KO000.ogg"
    komachi "That's how much people have something to wish for. It means the world is overflowing with hopes and dreams. Ah, that might've been high in Komachi points!"
    call finishmultiImage from _call_finishmultiImage_45
    show komachi coat near_center vhappy at center:
        xoffset 245 yoffset 75
    voice "audio/voice/E1/G01/01/HA/HA001.ogg"
    hachiman "It was low. A world full of desires means it's hell itself."
    show komachi happy with dissolve
    voice "audio/voice/E1/G01/01/KO/KO001.ogg"
    komachi "That's exactly why everyone visits the shrine. They say that you'll get unexpected help, right?"
    voice "audio/voice/E1/G01/01/HA/HA002.ogg"
    hachiman "This is a shrine though... Well, humans just rely on themselves and other people after all. That would make you want to pray to the gods."
    show komachi pout with dissolve
    voice "audio/voice/E1/G01/01/KO/KO002.ogg"
    komachi "You have no hopes or dreams... That's low in Komachi points..."
    show komachi unimpressed with dissolve
    voice "audio/voice/E1/G01/01/KO/KO003.ogg"
    komachi "Ahhhhhh, I've become more worried about this year's Onii-chan more than the entrance exams..."
    voice "audio/voice/E1/G01/01/HA/HA003.ogg"
    hachiman "Really? I'm not that worried though. About me, or about you. I'm especially not worried about you at all. I don't believe in other people or
        gods, but I believe in you."
    hachiman "(Oh yeah... I just said some great stuff that has no meaning again!)"
    show komachi happy with dissolve
    voice "audio/voice/E1/G01/01/KO/KO004.ogg"
    komachi "Onii-chan... I don't believe in you at all, but thank you!"
    voice "audio/voice/E1/G01/01/HA/HA004.ogg"
    hachiman "Don't believe in me? Even believing in Onii-chan's love?"
    #^ discrepency in translations
    hide komachi with dissolve
    "While continuing this kind of exchange, the line to visit the shrine slowly advanced forward."
    if shrine_flag == "1":
        jump shrine1
    elif shrine_flag == "2":
        jump shrine2
    else:
        jump shrine3

#yui/yukino route
label shrine1:
    show komachi coat near_left surprised at center with dissolve:
        xoffset 275 yoffset 65
    voice "audio/voice/E1/G01/01/KO/KO005.ogg"
    komachi "Ah..."
    voice "audio/voice/E1/G01/01/HA/HA005.ogg"
    hachiman "Hm?"
    hide komachi
    $url = ["komachi coat near_left happy", "komachi coat near_left vhappy"]
    $multiImagePara = [275, 65, 0, 0, 2.25]
    call multiImage(0) from _call_multiImage_45
    voice "audio/voice/E1/G01/01/KO/KO006.ogg"
    komachi "It's Yukino-san and Yui-san! Hey! Yukino-san! Yui-san!"
    call finishmultiImage from _call_finishmultiImage_46
    stop music fadeout 1.0
    hide komachi with dissolve
    play music "audio/bgm/BGM41.ogg"
    show yukino coat far_center at left:
        xoffset 345 yoffset 75
    show yui coat far_center at left:
        xoffset 225 yoffset 75
    with dissolve
    hide yui
    $url = ["yui coat far_center", "yui coat far_center vhappy"]
    $multiImagePara = [225, 75, 0, 0, 4.5]
    call multiImage(-1) from _call_multiImage_46
    voice "audio/voice/E1/G01/01/YI/YI000.ogg"
    yui "Ah! Komachi-chan! ...and Hikki! Yahallo!"
    call finishmultiImage from _call_finishmultiImage_47
    hide yui
    hide yukino
    with dissolve
    show komachi coat mid_left vhappy at right:
        xoffset -150 yoffset 75
    show yukino coat mid_center vhappy at left:
        xoffset 190 yoffset 75
    show yui coat mid_right vhappy at left:
        xoffset -175 yoffset 75
    with dissolve
    voice "audio/voice/E1/G01/01/KO/KO007.ogg"
    komachi "Happy New Years Day!"
    voice "audio/voice/E1/G01/01/YI/YI001.ogg"
    yui "Yeah! Happy New Years!"
    voice "audio/voice/E1/G01/01/YK/YK000.ogg"
    yukino "Happy New Years."
    hachiman "(They came together, huh? Getting along from the start of the new year.)"
    voice "audio/voice/E1/G01/01/HA/HA006.ogg"
    hachiman "Happy New Years. Have you already visited the shrine?"
    show yukino happy
    show yui coat mid_center happy at left:
        xoffset 120 yoffset 75
    with dissolve
    voice "audio/voice/E1/G01/01/YK/YK001.ogg"
    yukino "Yes. You two are about to go, right?"
    show komachi happy with dissolve
    voice "audio/voice/E1/G01/01/KO/KO008.ogg"
    komachi "That's right! Praying to pass the entrance exams!"
    show yui coat mid_right vhappy at left with dissolve:
        xoffset -175 yoffset 75
    voice "audio/voice/E1/G01/01/YI/YI002.ogg"
    yui "I see. The exam is real soon now after all. I visited the shrine here before my exam too!"
    voice "audio/voice/E1/G01/01/HA/HA007.ogg"
    hachiman "Hearing that, it sounds like it's really effective... Komachi, it looks like you'll be able to pass easily."
    show yui coat mid_center surprised at left with dissolve:
        xoffset 120 yoffset 75
    voice "audio/voice/E1/G01/01/YI/YI003.ogg"
    yui "That was so mean!"
    show yukino vhappy with dissolve
    voice "audio/voice/E1/G01/01/YK/YK002.ogg"
    yukino "But if it's that effective, it seems like it'd be a good idea to ask for a change in Hikigaya-kun's human nature. We should probably get it done as soon as possible."
    show yui coat mid_right pout at left with dissolve:
        xoffset -175 yoffset 75
    voice "audio/voice/E1/G01/01/YI/YI004.ogg"
    yui "It's not that effective!"
    voice "audio/voice/E1/G01/01/HA/HA008.ogg"
    hachiman "Hey? Is my human nature that sparingly lower than your academics?"
    show komachi sad with dissolve
    voice "audio/voice/E1/G01/01/KO/KO009.ogg"
    komachi "I'm sorry. My brother's like this, but please be nice to us this year too."
    voice "audio/voice/E1/G01/01/YK/YK003.ogg"
    yukino "Treat us well, too."
    show yui vhappy with dissolve
    voice "audio/voice/E1/G01/01/YI/YI005.ogg"
    yui "Yup, same here!"
    voice "audio/voice/E1/G01/01/HA/HA009.ogg"
    hachiman "Alright, let's go."
    hide komachi
    $url = ["komachi coat mid_center happy", "komachi coat mid_left vhappy"]
    $multiImagePara = [-75, 75, -150, 75, 0.4]
    call multiImage(1, False) from _call_multiImage_47
    voice "audio/voice/E1/G01/01/KO/KO010.ogg"
    komachi "Yup! Then Yukino-san, Yui-san, see ya next time!"
    call finishmultiImage from _call_finishmultiImage_48
    hide yui
    hide yukino
    with dissolve
    "Yuigahama was waving her hand widely and Yukinoshita mildly. While being seen off by those two, Komachi and I approached the shrine."
    window auto hide dissolve
    stop music fadeout 1.0
    stop ambient fadeout 1
    scene shrine
    with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM09.ogg"
    play sound "audio/sfx/SE02/SE02_15.ogg"
    $renpy.pause(delay=2.2, hard=True)
    play sound "audio/sfx/SE02/SE02_16.ogg"
    $renpy.pause(delay=0.9, hard=True)
    window auto show dissolve
    "After waiting a little bit more, Komachi and I finally made it to the front of the shrine. I, of course, prayed for Komachi to pass her entrance exams."
    voice "audio/voice/E1/G01/01/KO/KO011.ogg"
    komachi "Please make Komachi pass her exams. And please make my brother happy!"
    voice "audio/voice/E1/G01/01/HA/HA010.ogg"
    hachiman "Komachi, you don't have to say your wishes out loud. Also, I'm generally always happy."
    show komachi coat mid_center surprised at center with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E1/G01/01/KO/KO012.ogg"
    komachi "How so?"
    voice "audio/voice/E1/G01/01/HA/HA011.ogg"
    hachiman "\"Happiness is always something decided by your own heart.\"\n-Hachiman"
    show komachi happy with dissolve
    voice "audio/voice/E1/G01/01/KO/KO013.ogg"
    komachi "Yeah, I think it'd be better if you gave up being like that. I want you to be genuinely happy and..."
    voice "audio/voice/E1/G01/01/HA/HA012.ogg"
    hachiman "Komachi..."
    show komachi vhappy with dissolve
    voice "audio/voice/E1/G01/01/KO/KO014.ogg"
    komachi "...that was high in Komachi points! The New Years allowance I'll get from Onii-chan will also be high!"
    voice "audio/voice/E1/G01/01/HA/HA013.ogg"
    hachiman "It's not a lot, it's not. It won't be a lot, but how much do you want? Onii-chan only has small bits of change left in his savings though."
    show komachi mid_left angry at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E1/G01/01/KO/KO015.ogg"
    komachi "Tch! Cheapskate."
    voice "audio/voice/E1/G01/01/HA/HA014.ogg"
    hachiman "Wait, did you seriously just click your tongue at me?"
    show komachi mid_center happy at center with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E1/G01/01/KO/KO016.ogg"
    komachi "Did not. Come on, hurry up."
    voice "audio/voice/E1/G01/01/HA/HA015.ogg"
    hachiman "Yeah, sure."
    hide komachi with dissolve
    "This casual banter between siblings... Jeez, Komachi is too cute! God, please bless this wonderful world's little sister all the way..."
    show komachi coat mid_center happy at center with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E1/G01/01/HA/HA016.ogg"
    hachiman "Okay, it looks like we're done. So should we get going?"
    show komachi vhappy with dissolve
    voice "audio/voice/E1/G01/01/KO/KO017.ogg"
    komachi "Yup!"
    window auto hide dissolve
    scene market
    show komachi coat near_center happy at right:
        xoffset 100 yoffset 75
    show yukino coat mid_center vhappy at left:
        xoffset 190 yoffset 75
    show yui coat mid_center vhappy at left:
        xoffset 120 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E1/G01/01/YI/YI006.ogg"
    yui "Ah, Hikki and Komachi-chan! Have you finished your visit?"
    hide komachi with dissolve
    show komachi coat mid_left vhappy at right with dissolve:
        xoffset -150 yoffset 75
    voice "audio/voice/E1/G01/01/KO/KO018.ogg"
    komachi "We're done!"
    voice "audio/voice/E1/G01/01/HA/HA017.ogg"
    hachiman "You bothered to wait for us?"
    show yukino avoid
    show yui pout
    with dissolve
    voice "audio/voice/E1/G01/01/YK/YK004.ogg"
    yukino "Well, yes."
    voice "audio/voice/E1/G01/01/YI/YI007.ogg"
    yui "We happened to meet each other here, and just leaving after that felt kinda weird so..."
    voice "audio/voice/E1/G01/01/HA/HA018.ogg"
    hachiman "I see..."
    show komachi happy with dissolve
    voice "audio/voice/E1/G01/01/KO/KO019.ogg"
    komachi "Yukino-san and Yui-san are so nice after all. I'm so happy!"
    show yui coat mid_right vhappy at left:
        xoffset -175 yoffset 75
    show yukino happy
    with dissolve
    voice "audio/voice/E1/G01/01/YI/YI008.ogg"
    yui "Nah, Yukinon and I wanted to talk to you a bit more too, Komachi-chan."
    hachiman "(Looks like it's getting crowded. What should we do? We bothered these two in waiting for us, so...)"
    voice "audio/voice/E1/G01/01/HA/HA019.ogg"
    hachiman "What are you going to do now?"
    show yui coat mid_center happy at left:
        xoffset 120 yoffset 75
    show yukino stare
    with dissolve
    voice "audio/voice/E1/G01/01/YK/YK005.ogg"
    yukino "Not sure..."
    voice "audio/voice/E1/G01/01/YI/YI009.ogg"
    yui "What about you guys? Do you have stuff to do now?"
    show komachi coat mid_center happy at right with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E1/G01/01/HA/HA020.ogg"
    menu shrine1_menu:
        hachiman "Well..."
        with dissolve
        "Let's get out of here for now":
            $shrineMeetFlag = "yukino"
            # sfx here
            play ambient "audio/sfx/SE05/SE05_00L.ogg"
            "Honestly, I don't want to stay here too long. Looks like it's getting crowded quickly."
            voice "audio/voice/E1/G01/01/HA/HA021.ogg"
            hachiman "Let's move from here first. Seems like more people are coming too."
            show yukino happy
            show yui pout
            with dissolve
            voice "audio/voice/E1/G01/01/YI/YI010.ogg"
            yui "Yeah! This line to the shrine has become incredibly long."
            voice "audio/voice/E1/G01/01/YK/YK006.ogg"
            yukino "So much so they'll be exhausted by the time they finish their visit."
            show yui happy with dissolve
            voice "audio/voice/E1/G01/01/YI/YI011.ogg"
            yui "Then let's go somewhere else first!"
            hide yui
            hide yukino
            hide komachi
            with dissolve
            "We left the compound as a group, then headed towards the main festivities."
            window auto hide dissolve
            stop music fadeout 1.0
            stop ambient fadeout 1.0
            jump E1_YUK_01
        "What's wrong, Komachi?": #Probably yui route
            $shrineMeetFlag = "yui"
            #working on it
            #no animation
            #no audio
            #no sfx
            #no music
            show komachi surprised with dissolve
            voice "audio/voice/E1/G01/01/KO/KO020.ogg"
            komachi "...Ah."
            show yukino surprised
            show yui surprised
            with dissolve
            "I glanced over and saw Komachi looking around all over the place. There were stalls on both sides, so she might be curious about them."
            voice "audio/voice/E1/G01/01/HA/HA022.ogg"
            hachiman "Hm? What's up, Komachi?"
            show komachi happy with dissolve
            voice "audio/voice/E1/G01/01/KO/KO021.ogg"
            komachi "Um, I think... I see something over that way..."
            hachiman "(Doesn't seem like she's looking at a food stall. What are you looking around for then?)"
            voice "audio/voice/E1/YUI/01/KO/KO000.ogg"
            komachi "Ah, that's Taishi-kun over there!"
            show yui happy
            show yukino pout
            with dissolve
            voice "audio/voice/E1/YUI/01/HA/HA000.ogg"
            hachiman "Taishi-kun... who's that?"
            "Komachi pointed in the direction of someone who was with Kawasaki, a classmate of ours..."
            show komachi pout with dissolve
            voice "audio/voice/E1/YUI/01/KO/KO001.ogg"
            komachi "Taishi-kun, remember? His big sister is the Kawasaki from your class. Get it right."
            voice "audio/voice/E1/YUI/01/HA/HA001.ogg"
            hachiman "You know that much, Komachi?"
            show komachi vhappy with dissolve
            voice "audio/voice/E1/YUI/01/KO/KO002.ogg"
            komachi "I'm going to go exchange some intel with him!"
            show komachi coat mid_left happy with dissolve:
                xoffset -150 yoffset 75
            voice "audio/voice/E1/YUI/01/KO/KO003.ogg"
            komachi "That being said Onii-chan, Komachi will go on home on her own so have fun!"
            hide komachi with dissolve
            voice "audio/voice/E1/YUI/01/HA/HA002.ogg"
            hachiman "Ah, wait...!"
            "(You worry me, you know...)"
            jump E1_YUI_01

label shrine2:
    menu shrine2_menu:
        with dissolve
        hachiman "(...But for real, there are a lot of people today. If there is this much people here, then...)"
        "I feel a scary presence...":
            #haruno and meguri
            $shrineMeetFlag = "haruno meguri"
            jump E1_HAR_01
        "I feel a troublesome presence....":
            #yumiko and ebina
            "Not done."
            jump shrine2_menu
            return

label shrine3:
    window auto hide dissolve
    stop voice
    stop ambient fadeout 0.5
    scene shrine with Fade(1.0, 0.5, 1.0)
    show komachi coat mid_center happy at center with dissolve:
        xoffset -75 yoffset 75
    window auto show dissolve
    voice "audio/voice/E1/G03/01/KO/KO005.ogg"
    komachi "Onii-chan, did you pray properly?"
    voice "audio/voice/E1/G03/01/HA/HA005.ogg"
    hachiman "I already did that. Alright, let's go."
    show komachi vhappy with dissolve
    voice "audio/voice/E1/G03/01/KO/KO006.ogg"
    komachi "Yeah! Let's check out the stalls and go home!"
    window auto hide dissolve
    stop voice
    scene market
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "As I pass through the Torii gate and enter the approach road, the number of people on the path increases dramatically. In fact, the amount of chaos increases. It's a true festival scene, I guess."
    menu shrine3_menu:
        with dissolve
        hachiman "(It's no small thing to visit a shrine. But whatever.)"
        "The sound of shooting.....":
            #hiratsuka
            #$shrineMeetFlag = "hiratsuka" in E2_CMM_01_cont hiratsuka will call
            $shrineMeetFlag = "hiratsuka"
            hachiman "(I've been hearing shots ring out for a while now...)"
            window auto hide dissolve
            stop music
            play sound "audio/sfx/SE01/SE01_62.ogg"
            $renpy.pause(delay=0.5, hard=True)
            stop sound
            window auto show dissolve
            voice "audio/voice/E1/G03/01/ZB/ZB000.ogg"
            sk "Ah, unlucky, lady!"
            voice "audio/voice/E1/G03/01/SZ/SZ000.ogg"
            mystery "Tch. I missed again."
            window auto hide dissolve
            play sound "audio/sfx/SE01/SE01_62.ogg"
            $renpy.pause(delay=0.5, hard=True)
            stop sound
            window auto show dissolve
            voice "audio/voice/E1/G03/01/SZ/SZ001.ogg"
            mystery "One more time, keep."
            voice "audio/voice/E1/G03/01/ZB/ZB001.ogg"
            sk "You've already missed 5 times. Shouldn't you just give it up?"
            voice "audio/voice/E1/G03/01/SZ/SZ002.ogg"
            mystery "Just give me another one! I may have lost the battle, but I won't lose the war. I just have to keep shooting until I hit it... I'll get it next time, I have to... If I do, I'll be able to get married this year for sure!"
            hachiman "(That voice... What is she trying so hard for? Is it a \"If I don't step on the crack on my way home, my wish will come true\" type of thing? That's the sort of thing a grade schooler would do...)"
            hachiman "(Seeing a single woman in her thirties doing that is kind of sad... and frightening... More frightening that anything, really. Let's not get involved in that...)"
            window auto hide dissolve
            play sound "audio/sfx/SE01/SE01_62.ogg"
            $renpy.pause(delay=1.5, hard=True)
            jump E1_SHI_01
            return
        "Someone's gaze.....":
            #iroha
            $shrineMeetFlag = "iroha" #in E2_CMM_01_cont iroha will call
            hachiman "(...Hmm? I feel someone's gaze...)"
            window auto hide dissolve
            stop music fadeout 0.5
            jump E1_IRO_01
        "Is someone calling?":
            $shrineMeetFlag = "saki"
            voice "audio/voice/E1/G03/01/TA/TA000.ogg"
            $renpy.music.stop(channel="music")
            mystery "...saan!"
            hachiman "(Did I hear something just now?)"
            voice "audio/voice/E1/G03/01/TA/TA001.ogg"
            mystery "Onii-saan!"
            hachiman "(I felt like I heard someone, but I must be imagining it.)"
            voice "audio/voice/E1/G03/01/TA/TA002.ogg"
            mystery "Onii-san, Onii-saan!"
            hachiman "(Yup, it's definitely my imagination, because I have don't have a brother, let alone a brother-in-law!)"
            jump E1_SAK_01

label E1_G02_02:
    scene cafeA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM17.ogg"
    window auto show dissolve
    voice "audio/voice/E1/G02/02/HA/HA000.ogg"
    hachiman "...How about here?"
    $url = ["yui coat mid_center surprised", "yui coat mid_center vhappy"]
    $multiImagePara = [35, 75, 0, 0, 4.2]
    call multiImage() from _call_multiImage_48
    voice "audio/voice/E1/G02/02/YI/YI000.ogg"
    yui "Ohh... It has a calming atmosphere... To have such a cafe here... You wouldn't have known!"
    call finishmultiImage from _call_finishmultiImage_49
    show yui coat mid_center vhappy at center:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/G02/02/HA/HA001.ogg"
    hachiman"Well.. You did tell me to bring you somewhere with a lesser crowd."
    show yui pout with dissolve
    voice "audio/voice/E1/G02/02/YI/YI001.ogg"
    yui "Feels like you're proud of something sad."
    "At this cafe, they don't really have that many regular customers. So it's a relief to find it still as peaceful"
    show yui happy with dissolve
    voice "audio/voice/E1/G02/02/YI/YI002.ogg"
    yui "We can finally take a break huh~ Hikki~ where should we sit?"
    show yui coat mid_right happy at center with dissolve:
        xoffset -110 yoffset 70
    "Yuigahama happily looked around the cafe."
    stop music
    voice "audio/voice/E1/G02/02/HR/HR000.ogg"
    mystery "Ara, it's Hikigaya-kun."
    show yui coat mid_center surprised at center with dissolve:
        xoffset 35 yoffset 75
    hachiman "(This voice...)"
    window auto hide dissolve
    hide yui with dissolve
    show haruno sweater far_center vhappy at center:
        xoffset -255 yoffset 75
    with dissolve
    play music ["<silence 0.3>", "audio/bgm/BGM35.ogg"]
    window auto show dissolve
    voice "audio/voice/E1/G02/02/HR/HR001.ogg"
    haruno "Yahallo~"
    show yui coat mid_left angry at right with dissolve:
        xoffset -80 yoffset 70
    voice "audio/voice/E1/G02/02/YI/YI003.ogg"
    yui "Haruno-san? ... and..."
    show hayama coat far_center relieved at left behind haruno with dissolve:
        xoffset 75 yoffset 75
    voice "audio/voice/E1/G02/02/HY/HY000.ogg"
    hayama "...Yo"
    show yui surprised with dissolve
    voice "audio/voice/E1/G02/02/YI/YI004.ogg"
    yui "...Hayato-kun!"
    voice "audio/voice/E1/G02/02/HR/HR002.ogg"
    haruno "........."
    hachiman "(she's waving at us so happily... it can't be she wants to sit with us?)"
    show yui coat mid_center pout at right with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E1/G02/02/YI/YI005.ogg"
    yui "Erm, do you want to sit with them?"
    voice "audio/voice/E1/G02/02/HA/HA002.ogg"
    hachiman "...I don't know."
    "It can't be helped since Yuigahama-san and Haruno-san already saw each other. So we made our way to the seats where Haruno-san was indicating."
    window auto hide dissolve
    hide yui
    hide hayama
    hide haruno
    with dissolve
    scene cafeA:
        zoom 1.5 xalign 0 ypos -310
    show haruno sweater mid_center vhappy at center:
        xoffset 10 yoffset 75
    show hayama coat mid_center relieved behind haruno at left:
        xoffset 35 yoffset 75
    with dissolve
    show yui home mid_left pout at right with dissolve:
        xoffset -145 yoffset 75
    window auto show dissolve
    voice "audio/voice/E1/G02/02/HR/HR003.ogg"
    haruno "Why, it feels like it's been a while, Gahama-chan~"
    voice "audio/voice/E1/G02/02/YI/YI006.ogg"
    yui "Ah, haha, it's been a while..."
    show haruno sly with dissolve
    voice "audio/voice/E1/G02/02/HR/HR004.ogg"
    haruno "Are you two on a date? Hey Hey~ You're close as usual~"
    voice "audio/voice/E1/G02/02/HA/HA003.ogg"
    hachiman "Erm, no..."
    show haruno happy with dissolve
    voice "audio/voice/E1/G02/02/HR/HR005.ogg"
    haruno "So, why aren't you with Yukino-chan?"
    show yui happy with dissolve
    voice "audio/voice/E1/G02/02/YI/YI007.ogg"
    yui "Ah, we're out today to buy a present for her."
    show haruno surprised with dissolve
    voice "audio/voice/E1/G02/02/HR/HR006.ogg"
    haruno "Oh yeah, her birthday's coming up soon, I see..."
    show yui pout with dissolve
    voice "audio/voice/E1/G02/02/YI/YI008.ogg"
    yui "So we wanted to give her a surprise... together..."
    show haruno vhappy with dissolve
    voice "audio/voice/E1/G02/02/HR/HR007.ogg"
    haruno "Ohh, a surprise is it? That's nice... Maybe I should give her a surprise too... Oh... I know, let's give her a call to ask her out!"
    stop music
    hide haruno with dissolve
    show yui surprised with dissolve
    voice "audio/voice/E1/G02/02/YI/YI009.ogg"
    yui "......Eh"
    voice "audio/voice/E1/G02/02/HA/HA004.ogg"
    hachiman "......Eh"
    play music ["<silence 0.3>", "audio/bgm/BGM43.ogg"]
    show hayama coat mid_right happy at left with dissolve:
        xoffset 5 yoffset 65
    voice "audio/voice/E1/G02/02/HY/HY001.ogg"
    hayama "She may not come out..."
    "Hayama commented with a strained smile while I nodded in agreement... It makes me uncomfortable to think about what will happen if both sisters meet this early in the year."
    "Hayama, knowing them from childhood, seems to be guessing what might happen, you could see the anxiety in his gentle smile..."
    voice "audio/voice/E1/G02/02/HR/HR008.ogg"
    haruno "Hmm, I think she might come out today after all."
    voice "audio/voice/E1/G02/02/YK/YK000.ogg"
    yukino "...Hello."
    show hayama surprised with dissolve
    voice "audio/voice/E1/G02/02/HR/HR008A.ogg"
    haruno "Ah, Yukino-chan? This is your sister. Can you come out now?"
    voice "audio/voice/E1/G02/02/YK/YK001.ogg"
    yukino "I refuse."
    show yui pout with dissolve
    voice "audio/voice/E1/G02/02/YI/YI010.ogg"
    yui "That's fast!"
    show hayama coat mid_center relieved at left with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/G02/02/HY/HY002.ogg"
    hayama "............"
    voice "audio/voice/E1/G02/02/HR/HR009.ogg"
    haruno "I wonder? Is it okay for you to refuse~?"
    voice "audio/voice/E1/G02/02/YK/YK001A.ogg"
    yukino "...What?"
    voice "audio/voice/E1/G02/02/HR/HR010.ogg"
    haruno "Actually... You see... I'm with Hikigaya-kun now~"
    voice "audio/voice/E1/G02/02/YK/YK001B.ogg"
    yukino "Geez, stop joking around... Please stop your nonsense."
    show haruno sweater near_center vhappy at center with dissolve:
        xoffset -20 yoffset 75
    voice "audio/voice/E1/G02/02/HR/HR011.ogg"
    haruno "Here you go, Hikigaya-kun."
    show hayama happy
    show yui home mid_center surprised at right:
        xoffset -175 yoffset 75
    show haruno sweater mid_center vhappy at center:
        xoffset 10 yoffset 75
    with dissolve
    "Haruno-san handled the phone directly at me without waiting for my response."
    voice "audio/voice/E1/G02/02/HA/HA005.ogg"
    hachiman "W-Wait, eh?"
    "I looked at Haruno-san with her phone in my hand, she gave an expression that she didn't intend to take the phone back until I answered..."
    "I could hear a voice calling for Haruno-san from the phone... Can't be helped, I guess I just have to answer..."
    show yui pout with dissolve
    voice "audio/voice/E1/G02/02/HA/HA006.ogg"
    hachiman "Ah~, ...Hello."
    voice "audio/voice/E1/G02/02/YK/YK001C.ogg"
    yukino "*sigh* I'm amazed... Why are you there?"
    voice "audio/voice/E1/G02/02/HA/HA007.ogg"
    hachiman "Erm, I was just going out for a bit and I got caught..."
    voice "audio/voice/E1/G02/02/YK/YK001D.ogg"
    yukino "That's enough, get my sister back on the phone..."
    voice "audio/voice/E1/G02/02/HA/HA008.ogg"
    hachiman "...Okay, I'm sorry..."
    hide haruno with dissolve
    "Why did I appologize? I wiped the phone screen before passing it back to Haruno-san."
    voice "audio/voice/E1/G02/02/YK/YK002.ogg"
    yukino "............"
    window auto hide dissolve
    show haruno sweater mid_center happy at center with dissolve:
        xoffset 10 yoffset 75
    window auto show dissolve
    voice "audio/voice/E1/G02/02/HR/HR012.ogg"
    haruno "Yukino-chan's coming..."
    show yui home mid_left pout at right with dissolve:
        xoffset -145 yoffset 75
    voice "audio/voice/E1/G02/02/YI/YI011.ogg"
    yui "Erm, why did you have to call Yukino out? It sounded like she didn't want to..."
    hide haruno
    $url = ["haruno sweater mid_center surprised", "haruno sweater mid_center happy"]
    $multiImagePara = [10, 75, 0, 0, 0.8]
    call multiImage() from _call_multiImage_49
    voice "audio/voice/E1/G02/02/HR/HR013.ogg"
    haruno "Hmm? Ah... We have a dinner assignments with our families later... But Yukino-chan was refusing to come..."
    call finishmultiImage from _call_finishmultiImage_50
    show haruno sweater mid_center vhappy at center:
        xoffset 10 yoffset 75
    with dissolve
    voice "audio/voice/E1/G02/02/HR/HR014.ogg"
    haruno "But if you guys are around, then she wouldn't have a reason to refuse anymore... She'll think she has no choice but to come save her friends..."
    hide yui
    $url = ["yui home mid_left pout", "yui home mid_left angry"]
    $multiImagePara = [-145, 75, 0, 0, 2.0]
    call multiImage(1) from _call_multiImage_50
    voice "audio/voice/E1/G02/02/YI/YI012.ogg"
    yui "Are we hostages then? But, if that's the case, how about Hayato-kun?"
    call finishmultiImage from _call_finishmultiImage_51
    show yui home mid_left angry at right:
        xoffset -145 yoffset 75
    show hayama relieved with dissolve
    voice "audio/voice/E1/G02/02/HY/HY003.ogg"
    hayama "Ahhh, our families have been close since long ago... So our families usually will meet for New Year's Greetings and have dinner together, I'm just following along with my family."
    voice "audio/voice/E1/G02/02/HA/HA009.ogg"
    hachiman "Ohh...?"
    voice "audio/voice/E1/G02/02/HR/HR015.ogg"
    haruno "Well, that's that... We're just waiting for our parents' greeting to be over..."
    show yui surprised with dissolve
    voice "audio/voice/E1/G02/02/YI/YI013.ogg"
    yui "Eh~ New Year's Greetings is a big event for you guys huh?"
    show haruno annoyed with dissolve
    voice "audio/voice/E1/G02/02/HR/HR016.ogg"
    haruno "...Well, we're used to it."
    voice "audio/voice/E1/G02/02/HY/HY004.ogg"
    hayama "............"
    "So, with Yuigahama and I as Haruno-san's hostages, we waited for a period of time..."
    voice "audio/voice/E1/G02/02/HA/HA010.ogg"
    hachiman "*sighs*"
    window auto hide dissolve
    hide haruno
    hide hayama
    hide yui
    with dissolve
    stop music fadeout 0.5
    scene cafeA:
        zoom 1.5 xalign 0 ypos -310
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "I can foresee an awkward developement when Yukinoshita finally arrive later..."
    "However..."
    play music ["<silence 0.3>", "audio/bgm/BGM35.ogg"]
    show haruno sweater mid_center happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E1/G02/02/HR/HR017.ogg"
    haruno "............"
    hide haruno with dissolve
    "With her staring at us with a gentle smile... Escaping is not an option... I feel like a toad totally trapped by a snake..."
    window auto hide dissolve
    stop music fadeout 0.5
    jump E1_HAR_02
