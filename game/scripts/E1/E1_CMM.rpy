label E1_CMM_01:
    scene houseA
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E1/CMM/01/HA/HA000.ogg"
    hachiman "...Huh."
    hachiman "(I'm living the lazy life, just watching people working. It's not bad, honestly.
I chose the right dream job after all. Being a full-time house-husband is the best!)"
    hachiman "(Now I just need to find a way to make it happen... I have to find someone talented and capable of
earning money. Oh, and someone who won't force me to work!)"
    voice "audio/voice/E1/CMM/01/KO/KO000.ogg"
    mystery "-chan?"
    voice "audio/voice/E1/CMM/01/HA/HA001.ogg"
    hachiman "Huh?"
    play music "audio/bgm/BGM44.ogg"
    show komachi home mid_center unimpressed at center with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E1/CMM/01/KO/KO001.ogg"
    komachi "Onii-chan, why are you watching anime re-runs with those dead eyes first thing after New Year's?"
    voice "audio/voice/E1/CMM/01/HA/HA002.ogg"
    hachiman "Ah, I was just thinking about life..."
    show komachi surprised with dissolve
    voice "audio/voice/E1/CMM/01/KO/KO002.ogg"
    komachi "Oh, I don't really care what you were thinking about."
    hachiman "(Geez, so mean...)"
    voice "audio/voice/E1/CMM/01/HA/HA003.ogg"
    hachiman "Guh..."
    show komachi happy with dissolve
    voice "audio/voice/E1/CMM/01/KO/KO003.ogg"
    komachi "Anyway, Happy New Year, Onii-chan! Here's to the new year!"
    voice "audio/voice/E1/CMM/01/HA/HA004.ogg"
    hachiman "Yeah, Happy New Year. Here's to a new one."
    show komachi vhappy with dissolve
    voice "audio/voice/E1/CMM/01/KO/KO004.ogg"
    komachi "So with that said, it's time for a shrine visit, Onii-chan."
    voice "audio/voice/E1/CMM/01/HA/HA005.ogg"
    hachiman "What?"
    show komachi happy with dissolve
    voice "audio/voice/E1/CMM/01/KO/KO005.ogg"
    komachi "It's called Hatsumode, Onii-chan. Hatsumode. The thing where you go pray at a shrine."
    voice "audio/voice/E1/CMM/01/HA/HA006.ogg"
    hachiman "Yeah, I know what that is, but are you crazy? You want to go out in the cold, bump shoulders in a crowd and wait your butt of in a line?"
    show komachi annoyed with dissolve
    voice "audio/voice/E1/CMM/01/KO/KO006.ogg"
    komachi "'Course I do. I'm taking entrance exams, remember? I have to pray for good luck!"
    voice "audio/voice/E1/CMM/01/HA/HA007.ogg"
    hachiman "Yeah, I guess you did have exams."
    show komachi unimpressed with dissolve
    voice "audio/voice/E1/CMM/01/KO/KO007.ogg"
    komachi "You're the one who said we'd go for Hatsumode in the first place, Onii-chan! Komachi studied so hard just so we can go, you know?"
    voice "audio/voice/E1/CMM/01/HA/HA008.ogg"
    hachiman "Sorry, I'll go. The laziness got to me."
    hide komachi
    $url = ["komachi home mid_center happy", "komachi home mid_left vhappy"]
    $multiImagePara = [-75, 75, 10, 75, 1.8]
    call multiImage(0, False) from _call_multiImage_7
    voice "audio/voice/E1/CMM/01/KO/KO008.ogg"
    komachi "Well, as long as you get it. Let's get ready to go!"
    call finishmultiImage from _call_finishmultiImage_8
    with dissolve
    "Having said that, Komachi promptly started getting ready. She's pretty quick-tempered despite being my sister. I, on the other hand, am still having trouble peeling myself off the couch."
    voice "audio/voice/E1/CMM/01/HA/HA009.ogg"
    menu start_menu:
        with dissolve
        hachiman "Ah, I wonder what it'll be like?"
        "Maybe it'll bring good luck.":
            # yui and yukino route
            voice "audio/voice/E1/CMM/01/HA/HA010.ogg"
            hachiman "Well, it is one way of getting good luck. We should properly ask for it."
            voice "audio/voice/E1/CMM/01/KO/KO009.ogg"
            show komachi coat mid_center vhappy at center with dissolve:
                xoffset -75 yoffset 75
            komachi "Yeah! I'm glad you finally get it. With that settled, you should hurry up and get ready too!"
            "My brother-skill is still a work in progress to break Komachi's cheery mood."
            hide komachi with dissolve
            "I got up and turned off the anime I'd been watching."
            hachiman "(...Alright, I'm going to go get changed.)"
            $shrine_flag = "1"
            jump E1_G01_01
        "I bet it'll be a total normie festival.":
            # haruno and yumiko route
            voice "audio/voice/E1/CMM/01/HA/HA011.ogg"
            hachiman "But people who go to these types of events are usually groups of mixed boys and girls, couples, or families who are taking their children out, y'know? Oh man..."
            show komachi coat mid_center pout at center with dissolve:
                xoffset -75 yoffset 75
            voice "audio/voice/E1/CMM/01/KO/KO010.ogg"
            komachi "Nah, I think there are groups with only girls and only boys too. Alright, let's go Onii-chan!"
            voice "audio/voice/E1/CMM/01/HA/HA012.ogg"
            hachiman "Arrrrgh..."
            show komachi happy with dissolve
            voice "audio/voice/E1/CMM/01/KO/KO011.ogg"
            komachi "Stop hesitating and let's go, Onii-chan! Hurry up, hurry up!"
            hachiman "(There's no use whining, huh... I'll do it for Komachi's sake...)"
            $shrine_flag = "2"
            jump E1_G01_01
        "Maybe we'll meet someone there?":
            # saki, iroha, hiratsuka route
            voice "audio/voice/E1/CMM/01/HA/HA013.ogg"
            hachiman "I feel like I'll meet a whole bunch of people if I go... especially today."
            show komachi coat mid_center angry at center with dissolve:
                xoffset -75 yoffset 75
            voice "audio/voice/E1/CMM/01/KO/KO012.ogg"
            komachi "Well, no duh. It's New Year's after all."
            voice "audio/voice/E1/CMM/01/HA/HA014.ogg"
            hachiman "We get to have a long break, and using it to rest properly is important. They're a shrine visit-rest type, I'm a stay-at-home type. It's important to separate the two."
            hide komachi
            $url = ["komachi coat mid_center annoyed", "komachi coat near_center annoyed"]
            $multiImagePara = [-75, 75, 10, 75, 4.5]
            call multiImage(0, False) from _call_multiImage_8
            voice "audio/voice/E1/CMM/01/KO/KO013.ogg"
            komachi "Ahh, stop muttering to yourself get going! Go change! Come on!"
            call finishmultiImage from _call_finishmultiImage_9
            show komachi coat near_center annoyed at center:
                xoffset 10 yoffset 75
            hachiman "(Oh, Komachi is so assertive early in the New Year...)"
            $shrine_flag = "3"
            jump E1_G01_01

#audio in this scene located in audio/voice/E1/CMM/02
#... Probably depending on which scene it came from some logic might be more efficient to determine voice lines.
label E1_CMM_02:
    scene bedroomC
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E1/CMM/02/HA/HA000.ogg"
    hachiman "I'm tired... I've been moving around too much since the new year..."
    "I returned to my room and mumbled to myself. Strangely the fatigue wasn't feeling all that bad."
    "I hate crowds, but I might like the atmosphere surrounding New Years. The mix of the liveliness giving off the feeling something was starting and the peaceful atmosphere was strangely comforting."
    hachiman "(It's so peaceful... Oh right, it's Yukinoshita's birthday the day after tomorrow. Yuigahama probably remembers too. Those two get along really well...)"
    play sound "<loop 2>audio/sfx/SE03/SE03_00L.ogg"
    $renpy.pause(delay=1.0, hard=False)
    voice "audio/voice/E1/CMM/02/HA/HA001.ogg"
    hachiman "Hm?"
    $renpy.pause(delay=0.5, hard=False)
    stop sound
    play sound "audio/sfx/SE03/SE03_01.ogg"#["audio/sfx/SE03/SE03_02.ogg", "<silence 0.8>", "audio/sfx/SE03/SE03_02.ogg", "<silence 0.4>", "audio/sfx/SE03/SE03_02.ogg"]
    $renpy.pause(delay=1.0, hard=False)
    hachiman "(A message? From Yuigahama? What's it about?)"
    $renpy.pause(delay=1.0, hard=False)
    play music "audio/bgm/BGM06.ogg"
    #"☆★Yui★☆" "test1"
    #"Hikki❤" "test2"
    call mail_clear from _call_mail_clear
    show black with dissolve:
        alpha 0.3
    voice "audio/voice/E1/CMM/02/YI/YI001.ogg"
    call mail_function("yui", "yui", "", "Sorry for messaging you out of the blue! I should've mailed you sooner.") from _call_mail_function
    yui "\"Sorry for messaging you out of the blue! I should've mailed you sooner.\""
    voice "audio/voice/E1/CMM/02/HA/HA002.ogg"
    hachiman "\"It's fine. So, what is it?\" ...There."
    play sound "audio/sfx/SE03/SE03_02.ogg"
    call mail_function("yui", "hachiman", "Re:", "It's fine. So, what is it?") from _call_mail_function_1
    $renpy.pause(delay=1.5, hard=False)
    play sound "audio/sfx/SE03/SE03_00L.ogg"
    $renpy.pause(delay=0.5, hard=False)
    voice "audio/voice/E1/CMM/02/HA/HA004.ogg"
    hachiman "That was fast." #This line is not a mail
    $renpy.pause(delay=0.5, hard=False)
    voice "audio/voice/E1/CMM/02/YI/YI002.ogg"
    call mail_function("yui", "yui", "", "You wanna go buy Yukinon's present tmrw? It's her birthday the day after!") from _call_mail_function_2
    yui "\"You wanna go buy Yukinon's present tmrw? It's her birthday the day after!\""
    hachiman "(Tmrw? Even I can figure this one out without having to think too hard.)"
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    voice "audio/voice/E1/CMM/02/YI/YI003.ogg"
    call mail_function("yui", "yui", "", "\nLet's give her a present and surprise her!") from _call_mail_function_3
    yui "\"Let's give her a present and surprise her!\""
    hachiman "(A surprise, huh? You sure do like that sort of thing...)"
    hachiman "(But tomorrow? Tomorrow, tomorrow... What do I do?)"
    menu birthdaypresentchoice:
        "Go":
            hachiman "(I don't really have any plans tomorrow.)"
            play sound "audio/sfx/SE03/SE03_02.ogg"
            call mail_function("yui", "hachiman", "Re:", "Got it. Let's go then.") from _call_mail_function_13
            $renpy.pause(delay=0.8, hard=True)
            voice "audio/voice/E1/CMM/02/HA/HA005.ogg"
            hachiman "\"Got it. Let's go then.\""
            play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
            $renpy.pause(delay=1, hard=True)
            call mail_function("yui", "yui", "Re2:", "Really!? Yay! Let's go!") from _call_mail_function_14
            $renpy.pause(delay=0.8, hard=True)
            voice "audio/voice/E1/CMM/02/YI/YI004.ogg"
            yui "\"Really!? Yay! Let's go!\""
            play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
            $renpy.pause(delay=1, hard=True)
            call mail_function("yui", "yui", "" ,"Think you can meet in front of Chiba station at 1 o'clock? Ah! If not, no worries! I can adjust to your schedule, Hikki!") from _call_mail_function_15
            $renpy.pause(delay=0.8, hard=True)
            voice "audio/voice/E1/CMM/02/YI/YI005.ogg"
            yui "\"Think you can meet in front of Chiba station at 1 o'clock? Ah! If not, no worries! I can adjust to your schedule, Hikki!\""
            voice "audio/voice/E1/CMM/02/HA/HA006.ogg"
            hachiman "Deciding on plans like child's play. As expected of Gahama-san.  \"Alright, works for me. I'll be there at 1.\" ...There."
            play sound "audio/sfx/SE03/SE03_02.ogg"
            call mail_function("yui", "hachiman", "Re:", "That's alright, I'll be there at 1 o'clock.") from _call_mail_function_16
            $renpy.pause(delay=0.8, hard=True)
            play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
            $renpy.pause(delay=1, hard=True)
            call mail_function("yui", "yui", "Re2:", "Awesome, looking forward to it! Really think about what to buy! Ah, and make sure you're not late! If you are, make sure to tell me, okay?") from _call_mail_function_17
            $renpy.pause(delay=0.8, hard=True)
            voice "audio/voice/E1/CMM/02/YI/YI006.ogg"
            yui "\"Awesome, looking forward to it! Really think about what to buy! Ah, and make sure you're not late! If you are, make sure to tell me, okay?\""
            hachiman "(What are you, my mom? To be honest, you're even kinder than she is.)"
            voice "audio/voice/E1/CMM/02/HA/HA007.ogg"
            hachiman "\"Roger. See you tomorrow then.\"...There."
            $renpy.pause(delay=0.8, hard=True)
            play sound "audio/sfx/SE03/SE03_02.ogg"
            call mail_function("yui", "hachiman", "Re:3", "Roger. See you tomorrow then.") from _call_mail_function_18
            $renpy.pause(delay=2, hard=True)
            call mail_clear from _call_mail_clear_3
            hide black with dissolve
            hachiman "(I wonder what I should get Yukinoshita.)"
            stop music fadeout 1.0
            jump E1_YUI_03
        "Refuse":
            jump E1_CMM_03

#voices are in audio/voice/E1/CMM/03
label E1_CMM_03:
    #yukino route probably
    voice "audio/voice/E1/CMM/02/HA/HA008.ogg"
    hachiman "Tomorrow huh... No wait, tomorrow is..."
    hachiman "(Right, my parents asked me to go buy our daily necessities tomorrow... Behh.. I can't do it tomorrow.)"
    hachiman "(I'll have to apologize to Yuigahama...)"
    #$renpy.pause(delay=1.0, hard=True)
    play sound "audio/sfx/SE03/SE03_02.ogg"
    call mail_function("yui", "hachiman", "Re:", "Sorry, I've got stuff to do at home tomorrow. I'm very sorry.") from _call_mail_function_4
    $renpy.pause(delay=0.8, hard=True)
    voice "audio/voice/E1/CMM/03/HA/HA000.ogg" #Subject line: Re:
    hachiman "Sorry, I've got stuff to do at home tomorrow. I'm very sorry."
    window auto hide dissolve
    $renpy.pause(delay=1, hard=True)
    window auto show dissolve
    voice "audio/voice/E1/CMM/03/HA/HA001.ogg" #This line is not a mail
    hachiman "... There's no reply. S-should I apologize more? No, it makes it look too much like an excuse..."
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    $renpy.pause(delay=0.5, hard=True)
    call mail_function("yui", "yui", "Re2:", "I see... it can't be helped if you have things to do! Sorry for being so sudden!") from _call_mail_function_5
    voice "audio/voice/E1/CMM/03/YI/YI000.ogg" #Subject line: Re2:
    yui "\"I see... it can't be helped if you have things to do! Sorry for being so sudden!\""
    hachiman "(I ended up apologising anyway... and nonono, you're not at fault Gahama-san...)"
    play sound "audio/sfx/SE03/SE03_02.ogg"
    call mail_function("yui", "hachiman", "Re3:", "I'm very sorry. Don't worry about me and go shopping please.") from _call_mail_function_6
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E1/CMM/03/HA/HA002.ogg" #Subject line: Re3:
    hachiman "\"I'm very sorry. Don't worry about me and go shopping please.\""
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    $renpy.pause(delay=0.5, hard=True)
    call mail_function("yui", "yui", "Re4:", "Yeah... I'll do that! I want to give them at school so it'd be great if you could prepare something too. What to do you think? Think about it, okay?") from _call_mail_function_7
    voice "audio/voice/E1/CMM/03/YI/YI001.ogg" #Subject line: Re4:
    yui "\"Yeah... I'll do that! I want to give them at school so it'd be great if you could prepare something too. What to do you think? Think about it, okay?\""
    "What is this guilty feeling... She was being nice and invited me, but instead I made her be considerate of me..."
    "Also, if we're going to celebrate, we'll likely give her presents in the clubroom."
    "And then Yuigahama will be waiting for me, and when I turn up empty-handed she'll be considerate of me again..."
    voice "audio/voice/E1/CMM/03/HA/HA003.ogg" #Subject line: Re5:
    hachiman "... Let's do something about this. It's going to be too painful if I make her any more considerate of me. \"I'll finish my errands quickly.
        I can go if it's in the afternoon tomorrow.\" How is this?..."#The second sentance is a mail
    play sound "audio/sfx/SE03/SE03_02.ogg"
    call mail_function("yui", "hachiman", "Re5:", "I'll finish my errands quickly. I can go if it's in the afternoon tomorrow.") from _call_mail_function_8
    $renpy.pause(delay=2.0, hard=True)
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    $renpy.pause(delay=0.5, hard=True)
    call mail_function("yui", "yui", "Re6:", "Really!? Yay! Then is 13:00 in front of Chiba Station okay with you?") from _call_mail_function_9
    voice "audio/voice/E1/CMM/03/YI/YI002.ogg" #Subject line: Re6:
    yui "\"Really!? Yay! Then is 13:00 in front of Chiba Station okay with you?\""
    #this line, the beep of hachiman sending his text and his text appears before his voice line
    play sound "audio/sfx/SE03/SE03_02.ogg"
    $renpy.pause(delay=0.5, hard=True)
    call mail_function("yui", "hachiman", "Re7:", "Roger. Sorry about this. I don't know what to buy so help me out.") from _call_mail_function_10
    voice "audio/voice/E1/CMM/03/HA/HA004.ogg" #Subject line: Re7:
    hachiman "\"Roger. Sorry about this. I don't know what to buy so help me out.\""
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    $renpy.pause(delay=0.5, hard=True)
    call mail_function("yui", "yui", "Re8:", "I'm glad! Thanks, Hikki! Leave the choosing to me! I'm super good at that kind of thing!") from _call_mail_function_11
    voice "audio/voice/E1/CMM/03/YI/YI003.ogg" #Subject line: Re8:
    yui "\"I'm glad! Thanks, Hikki! Leave the choosing to me! I'm super good at that kind of thing!\""
    #this line, the beep of hachiman sending his text and his text appears before his voice line
    play sound "audio/sfx/SE03/SE03_02.ogg"
    $renpy.pause(delay=0.5, hard=True)
    call mail_function("yui", "hachiman", "Re9", "Then, it's all yours tomorrow.") from _call_mail_function_12
    voice "audio/voice/E1/CMM/03/HA/HA005.ogg" #Subject line: Re9:
    hachiman "\"Then, it's all yours tomorrow.\""
    #all mails cleared from screen
    call mail_clear from _call_mail_clear_1
    hide black with dissolve
    "Well, I don't know if my present would make her happy, but something is better than nothing."
    "I've got nothing better to do. And if I'm giving her a present either way, I should choose something that won't be a bother to Yukinoshita."
    "When I think about that, having Yuigahama's advice is very reassuring."
    "It does pain me to be reliant on Yuigahama though. I've got to avoid causing her a lot of trouble tomorrow!"
    stop music fadeout 1.0
    jump E1_YUI_03

#Consider New label maybe useful for common?
label E1_CMM_04:
    #voices are located in audio/voice/E1/CMM/04/
    scene black with Fade(1.0, 0.5, 0)
    play ambient "audio/sfx/SE05/SE05_01L.ogg"
    scene  mallB with Fade(0, 0, 1.0)
    play music "audio/bgm/BGM41.ogg"
    $renpy.pause(delay=1.0, hard=False)
    window auto show dissolve
    voice "audio/voice/E1/CMM/04/XA/XA000.ogg"
    fs "Here's your purchase. Thank you for shopping with us!"
    voice "audio/voice/E1/CMM/04/HA/HA000.ogg"
    hachiman "Ah, yes... Thank you."
    window auto hide dissolve
    scene  mallB
    show yui coat mid_center happy at center:
        xoffset 35 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    hachiman "(It sure is tiring to talking with store employees...)"
    show yui vhappy with dissolve
    voice "audio/voice/E1/CMM/04/YI/YI000.ogg"
    yui "It was super crowded, but it's great that we managed to get something nice! Right, Hikki?"
    voice "audio/voice/E1/CMM/04/HA/HA001.ogg"
    hachiman "Yeah, that's true. Sorry I relied on you that much. "
    hide yui
    $url = ["yui coat mid_center vhappy1", "yui coat mid_center happy"]
    $multiImagePara = [35, 75, 0, 0, 1.75]
    call multiImage() from _call_multiImage_9
    voice "audio/voice/E1/CMM/04/YI/YI001.ogg"
    yui "Not at all! Getting to look around was pretty fun!"
    call finishmultiImage from _call_finishmultiImage_10
    show yui coat mid_center happy at center:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/CMM/04/HA/HA002.ogg"
    hachiman "I see... You had fun."
    show yui pout with dissolve
    voice "audio/voice/E1/CMM/04/YI/YI002.ogg"
    yui "D-did you not, Hikki?"
    voice "audio/voice/E1/CMM/04/HA/HA003.ogg"
    hachiman "It's not that. I don't mind hanging around, but when it's this crowded, it's just hard to calm down."
    voice "audio/voice/E1/CMM/04/YI/YI003.ogg"
    yui "Yeah, I get that. There's a lot of people..."
    voice "audio/voice/E1/CMM/04/HA/HA004.ogg"
    hachiman "I bet it'd be pretty fun if this place was empty. Not like I'd know, though."
    hide yui
    $url = ["yui coat mid_center happy", "yui coat mid_center vhappy2"]
    $multiImagePara = [35, 75, 0, 0, 1.3]
    call multiImage() from _call_multiImage_10
    voice "audio/voice/E1/CMM/04/YI/YI004.ogg"
    yui "I see. That's great! Then let's come when it's emptier next time!"
    call finishmultiImage from _call_finishmultiImage_11
    show yui coat mid_center vhappy2 at center:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/CMM/04/HA/HA005.ogg"
    hachiman "Hang on, next time?"
    show yui blush with dissolve
    voice "audio/voice/E1/CMM/04/YI/YI005.ogg"
    yui "C-Come on! Like to buy Komachi-chan a present or something!"
    voice "audio/voice/E1/CMM/04/HA/HA006.ogg"
    hachiman "Eh, ah, yeah, well, o-okay. If it's empty, sure."
    show yui happy with dissolve
    voice "audio/voice/E1/CMM/04/YI/YI006.ogg"
    yui "Yeah!"
    voice "audio/voice/E1/CMM/04/HA/HA007.ogg"
    hachiman "Is it just me, or is it getting crowded again?"
    show yui happy with dissolve
    voice "audio/voice/E1/CMM/04/YI/YI007.ogg"
    yui "Maybe they've started selling lucky bags on this floor, too. You know, like those limited sales?"
    voice "audio/voice/E1/CMM/04/HA/HA008.ogg"
    hachiman "I see... This place is also becoming hell. What do you wanna do now? Go home?"
    hide yui
    $url = ["yui coat mid_center pout1", "yui coat mid_center happy"]
    $multiImagePara = [35, 75, 0, 0, 2.0]
    call multiImage() from _call_multiImage_11
    voice "audio/voice/E1/CMM/04/YI/YI008.ogg"
    yui "We're not going home! Um, you wanna go outside or go get some tea?"
    call finishmultiImage from _call_finishmultiImage_12
    show yui coat mid_center happy at center with None:
        xoffset 35 yoffset 75
    menu yui_shopping:
        with dissolve
        "Let's rest at a cafe.":
            $harunoCafeFlag = True
            voice "audio/voice/E1/CMM/04/HA/HA009.ogg"
            hachiman "Alright. Let's go to a cafe or something and take a breather."
            show yui coat mid_left pout at center with dissolve:
                xoffset 10 yoffset 70
            voice "audio/voice/E1/CMM/04/YI/YI009.ogg"
            yui "You want to go somewhere less crowded? I don't know if we'd find somewhere like that right now..."
            voice "audio/voice/E1/CMM/04/HA/HA010.ogg"
            hachiman "If we don't, we'll just go home. Then we wouldn't have to spend money either."
            hide yui
            $url = ["yui coat mid_center surprised", "yui coat mid_center pout"]
            $multiImagePara = [35, 75, 0, 0, 2.1]
            call multiImage() from _call_multiImage_12
            voice "audio/voice/E1/CMM/04/YI/YI010.ogg"
            yui "What's with the sudden saving mindset!? Don't say that, let's just try and find one!"
            call finishmultiImage from _call_finishmultiImage_13
            show yui coat mid_center pout at center:
                xoffset 35 yoffset 75
            hachiman "(Alright.)"
            voice "audio/voice/E1/CMM/04/HA/HA011.ogg"
            hachiman "If it's somewhere less crowded, I might have just the place in mind..."
            show yui vhappy with dissolve
            voice "audio/voice/E1/CMM/04/YI/YI011.ogg"
            yui "Huh? Really? Let's go then!"
            window auto hide dissolve
            stop ambient fadeout 0.5
            stop voice fadeout 0.5
            stop music fadeout 0.5
            jump E1_G02_02
        "Let's go outside first.":
            voice "audio/voice/E1/CMM/04/HA/HA012.ogg"
            hachiman "Alright, let's get out of here first. It's scary just thinking it's gonna get even worse."
            hide yui
            $url = ["yui coat mid_center happy", "yui coat mid_center pout"]
            $multiImagePara = [35, 75, 0, 0, 4.0]
            call multiImage() from _call_multiImage_13
            voice "audio/voice/E1/CMM/04/YI/YI012.ogg"
            yui "Haha, That's probably true... But don't you think it'll be crowded outside, too?"
            call finishmultiImage from _call_finishmultiImage_14
            show yui coat mid_center pout at center:
                xoffset 35 yoffset 75
            voice "audio/voice/E1/CMM/04/HA/HA013.ogg"
            hachiman "Hah... There's just no place for me in this world."
            show yui surprised with dissolve
            voice "audio/voice/E1/CMM/04/YI/YI013.ogg"
            yui "O-Of course there is! There's definitely is place for you! Come on, like at your home!"
            voice "audio/voice/E1/CMM/04/HA/HA014.ogg"
            hachiman "You're being too real... Besides, I feel small at home, too."
            show yui pout with dissolve
            voice "audio/voice/E1/CMM/04/YI/YI014.ogg"
            yui "I feel like I just heard something really sad..."
            window auto hide dissolve
            stop music fadeout 0.5
            stop voice fadeout 0.5
            stop ambient fadeout 0.5
            if shrineMeetFlag == "yui":
                jump E1_YUI_04
            jump E1_YUK_02
