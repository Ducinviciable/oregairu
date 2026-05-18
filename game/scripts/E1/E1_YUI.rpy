
label E1_YUI_01:
    scene market
    with Fade(1.0, 0.5, 1.0)
    play ambient "<loop 2>audio/sfx/SE05/SE05_00L.ogg" loop
    $ renpy.pause(delay=1, hard=True)
    show yui coat mid_right surprised at right:
        xoffset -150 yoffset 75
    show yukino coat mid_center happy at left:
        yoffset 75
    with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI003.ogg"
    yui "Ah..."
    voice "audio/voice/E1/YUI/01/HA/HA005.ogg"
    hachiman "What's up?"
    play music "audio/bgm/BGM12.ogg"
    show yui coat mid_center blush with dissolve:
        xoffset -150 yoffset 75
    voice "audio/voice/E1/YUI/01/YI/YI004.ogg"
    yui "Eh? No, n-nothing!"
    "Following Yuigahama's line of sight... There's a candy apple stall."
    voice "audio/voice/E1/YUI/01/HA/HA006.ogg"
    hachiman "Candy apples, huh... If you want one, why don't you go over there and buy it?"
    show yui surprised with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI005.ogg"
    yui "Is that okay?"
    voice "audio/voice/E1/YUI/01/HA/HA007.ogg"
    hachiman "Why wouldn't it be? Right?"
    show yukino vhappy with dissolve
    voice "audio/voice/E1/YUI/01/YK/YK001.ogg"
    yukino "Yeah."
    show yui coat mid_right vhappy with dissolve:
        xoffset -150 yoffset 75
    voice "audio/voice/E1/YUI/01/YI/YI006.ogg"
    yui "Yay! I'll go buy it, kay? Please wait here!"
    voice "audio/voice/E1/YUI/01/HA/HA008.ogg"
    hachiman "Oh, look at her go... She's just like a kid."
    voice "audio/voice/E1/YUI/01/YK/YK002.ogg"
    yukino "Fufu... You're right."
    show yui coat mid_left vhappy with dissolve:
        xoffset -150 yoffset 75
    voice "audio/voice/E1/YUI/01/YI/YI007.ogg"
    yui "Thanks for waiting~!"
    voice "audio/voice/E1/YUI/01/HA/HA009.ogg"
    hachiman "Yeah."
    scene yuicandyapple with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI008.ogg"
    yui "Mmmmm, it's so good!"
    voice "audio/voice/E1/YUI/01/YK/YK003.ogg"
    yukino "............"
    voice "audio/voice/E1/YUI/01/YI/YI009.ogg"
    yui "Yukinon, do you want some?"
    voice "audio/voice/E1/YUI/01/YK/YK004.ogg"
    yukino "Eh... No, I'm..."
    voice "audio/voice/E1/YUI/01/YI/YI010.ogg"
    yui "Have a bite! It's really good!"
    voice "audio/voice/E1/YUI/01/YK/YK005.ogg"
    yukino "But..."
    voice "audio/voice/E1/YUI/01/YI/YI011.ogg"
    yui "It's okay, it's okay. Here!"
    voice "audio/voice/E1/YUI/01/YK/YK006.ogg"
    yukino "T-Thank you..."
    voice "audio/voice/E1/YUI/01/YI/YI012.ogg"
    yui "How is it?"
    voice "audio/voice/E1/YUI/01/YK/YK007.ogg"
    yukino "It's good..."
    voice "audio/voice/E1/YUI/01/YI/YI013.ogg"
    yui "I know, right? It's delicious."
    hachiman "(Come to think of it, I don't think I've had candy apples before.)"
    scene market
    show yui coat near_left vhappy at right:
        xoffset -150 yoffset 75
    show yukino coat mid_center vhappy at left:
        yoffset 75
    with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI014.ogg"
    yui "Here Hikki, you too!"
    voice "audio/voice/E1/YUI/01/HA/HA010.ogg"
    hachiman "Eh? Me? I don't..."
    show yui coat near_center sad at right with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI015.ogg"
    yui "...You don't want any?"
    voice "audio/voice/E1/YUI/01/HA/HA011.ogg"
    hachiman "N-No. That's not it..."
    hachiman "(Does she really not notice these things!?)"
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_51.ogg"
    $renpy.pause(delay=1.2, hard=True)
    window auto show dissolve
    show yui coat near_center vhappy at right with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI016.ogg"
    yui "Mmm~! So good!"
    hachiman "(However, looking at how happily she's eating, it makes me want to buy one, too...)"
    show yukino coat mid_center angry at left with dissolve
    voice "audio/voice/E1/YUI/01/YK/YK008.ogg"
    yukino "Ah! That's..."
    voice "audio/voice/E1/YUI/01/HA/HA012.ogg"
    hachiman "Hey..."
    hide yukino
    hide yui
    with dissolve
    "Before Yukinoshita left, it seems like she saw something at the shooting stall."
    "Looking closely, among the prizes was Yukinoshita's favourite mascot character."
    hachiman "(...Pan-san, huh? Managing to spot it even through this crowd... How much does she like that panda?)"
    show yui coat mid_center pout at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/01/YI/YI017.ogg"
    yui "Eh? Ah, Yukinon!?"
    voice "audio/voice/E1/YUI/01/HA/HA013.ogg"
    hachiman "It's okay. She's in her zone."
    show yui surprised with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI018.ogg"
    yui "Eh? Shooting? ...Ah!  It's Pan-san!"
    voice "audio/voice/E1/YUI/01/HA/HA014.ogg"
    hachiman "Shouldn't we just wait for her?"
    show yui pout with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI019.ogg"
    yui "Heheh... Sure."
    show yui happy with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI020.ogg"
    yui "Mm, Hikki, you should've had some too."
    voice "audio/voice/E1/YUI/01/HA/HA015.ogg"
    hachiman "No, like I said..."
    hide yui with dissolve
    stop music fadeout 0.75
    stop ambient fadeout 1.0
    call card_loading from _call_card_loading_4
    scene market:
        zoom 1.5 xoffset -290 ypos -425
    show yui coat mid_center happy at center:
        xoffset 35 yoffset 75
    with dissolve
    $card_queue = ["About \nYui", "About cotton \ncandy", "About food \nstalls", "About \nhatsumode", "About the \nshooting stall", "Cut the \nconversation \nshort"]
    play music "audio/bgm/BGM31.ogg"
    $yui_shrine_card_count = 0
    $yui_shrine_ellipses = 0
    jump yui_shrine_cards


label yui_shrine_cards:
    if yui_shrine_card_count < 5:
        $yui_shrine_card_count += 1
        $renpy.pause(delay=0.5, hard=True)
        $ch2 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch2)
        $ch3 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch3)
        window auto hide dissolve
        call screen three_minigame("...", ch2, ch3) with dissolve
        if _return == 1:
            "not done"
            $card_queue.append(ch2)
            $card_queue.append(ch3)
            $yui_shrine_card_count -= 1
            jump yui_shrine_cards
        elif _return == 2:
            $card_queue.append(ch3)
            if ch2 == "About \nYui":
                jump about_yui_card
            elif ch2 == "About cotton \ncandy":
                jump cotton_candy_card
            elif ch2 == "About food \nstalls":
                jump food_stalls_card
            elif ch2 == "About \nhatsumode":
                jump hatsumode_card
            elif ch2 == "About the \nshooting stall":
                jump yui_shooting_stall_card
            else:
                "not done"
                $card_queue.append(ch2)
                $yui_shrine_card_count -= 1
                jump yui_shrine_cards
        elif _return == 3:
            $card_queue.append(ch2)
            if ch3 == "About \nYui":
                jump about_yui_card
            elif ch3 == "About cotton \ncandy":
                jump cotton_candy_card
            elif ch3 == "About food \nstalls":
                jump food_stalls_card
            elif ch3 == "About \nhatsumode":
                jump hatsumode_card
            elif ch3 == "About the \nshooting stall":
                jump yui_shooting_stall_card
            else:
                "not done"
                $card_queue.append(ch3)
                $yui_shrine_card_count -= 1
                jump yui_shrine_cards
    else:
        jump yui_shrine_end

label cotton_candy_card:
    voice "audio/voice/E1/YUI/01/HA/HA044.ogg"
    hachiman "Come to think of it, I liked cotton candy better than candy apples when I was a kid."
    show yui coat mid_center happy with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/01/YI/YI053.ogg"
    yui "Yeah, cotton candy is really tasty! It's all fluffy and sweet."
    voice "audio/voice/E1/YUI/01/HA/HA045.ogg"
    hachiman "If you think about it, though, it's all just regular sugar."
    show yui sad with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI054.ogg"
    yui "But... doesn't saying that kind of kill the magic?"
    voice "audio/voice/E1/YUI/01/HA/HA046.ogg"
    hachiman "I stopped eating it ever since I found out it was a rip-off."
    voice "audio/voice/E1/YUI/01/YI/YI055.ogg"
    yui "Y-You did? Ever since you were a kid... I guess some things never change."
    jump yui_shrine_cards

label food_stalls_card:
    voice "audio/voice/E1/YUI/01/HA/HA032.ogg"
    hachiman "Besides candy apples, is there anything else you like they sell at food stalls?"
    show yui coat mid_left happy with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/01/YI/YI042.ogg"
    yui "Hm? Yeah, of course I do."
    voice "audio/voice/E1/YUI/01/HA/HA033.ogg"
    hachiman "Like what?"
    show yui angry with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI043.ogg"
    yui "Let's see... I like takoyaki, cotton candy, yakisoba, chocolate bananas..."
    voice "audio/voice/E1/YUI/01/HA/HA034.ogg"
    hachiman "It sounds like you like all of them."
    show yui happy with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI044.ogg"
    yui "And.... Goldfish, I guess?"
    voice "audio/voice/E1/YUI/01/HA/HA035.ogg"
    hachiman "That's not even food..."
    show yui coat mid_center vhappy with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/01/YI/YI045.ogg"
    yui "Oh yeah... eheheh..."
    jump yui_shrine_cards

label cut_short_conversation_card:
    jump yui_shrine_end

label hatsumode_card:
    voice "audio/voice/E1/YUI/01/HA/HA028.ogg"
    hachiman "Speaking of Hatsumode..."
    show yui coat mid_center pout with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/01/YI/YI038.ogg"
    yui "Hmm?"
    voice "audio/voice/E1/YUI/01/HA/HA029.ogg"
    hachiman "What did you wish for, Yuigahama?"
    show yui coat mid_left surprised with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/01/YI/YI039.ogg"
    yui "It's not like you to ask something like that, Hikki."
    voice "audio/voice/E1/YUI/01/HA/HA030.ogg"
    hachiman "It's not?"
    show yui vhappy with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI040.ogg"
    yui "Mmm... I think I'll keep it a secret!"
    voice "audio/voice/E1/YUI/01/HA/HA031.ogg"
    hachiman "I see."
    hachiman "(Well, as she naturally would...)"
    show yui sad with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI041.ogg"
    yui "Ehehe..."
    jump yui_shrine_cards

label about_yui_card:
    voice "audio/voice/E1/YUI/01/HA/HA039.ogg"
    hachiman "You really managed to wolf down that candy apple before."
    show yui sad mid_right at center with dissolve:
        xoffset -65 yoffset 75
    voice "audio/voice/E1/YUI/01/YI/YI049.ogg"
    yui "T-That's because... it was tasty, alright!? There's nothing wrong with that, is there!?"
    voice "audio/voice/E1/YUI/01/HA/HA040.ogg"
    hachiman "I really meant that as a compliment."
    show yui angry mid_right at center with dissolve:
        xoffset -65 yoffset 75
    voice "audio/voice/E1/YUI/01/YI/YI050.ogg"
    yui "R-Really?"
    voice "audio/voice/E1/YUI/01/HA/HA041.ogg"
    hachiman "Well, yeah."
    show yui blush mid_center at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/01/YI/YI051.ogg"
    yui "It's really embarrassing for me if you s-say something like that!"
    voice "audio/voice/E1/YUI/01/HA/HA042.ogg"
    hachiman "S-Sorry about that."
    voice "audio/voice/E1/YUI/01/YI/YI052.ogg"
    yui "You didn't look too close, did you...?"
    voice "audio/voice/E1/YUI/01/HA/HA043.ogg"
    hachiman "O-Of course..."
    hachiman "(I-I didn't, alright? So stop looking at me like that...)"
    jump yui_shrine_cards

label yui_shooting_stall_card:
    voice "audio/voice/E1/YUI/01/HA/HA036.ogg"
    hachiman "The shooting stall, huh... Is Yukinoshita really that intent on conquering it?"
    show yui sad mid_center at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/01/YI/YI046.ogg"
    yui "A-Ah... I think she might be... Hikki, are you any good at shooting?"
    voice "audio/voice/E1/YUI/01/HA/HA037.ogg"
    hachiman "No, I've never even tried it."
    show yui happy with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI047.ogg"
    yui "Really? I thought guys loved those sorts of games~"
    voice "audio/voice/E1/YUI/01/HA/HA038.ogg"
    hachiman "That generally happens when they're with their friends or with their girlfriend. So I've obviously never done it."
    show yui surprised with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI048.ogg"
    yui "You just said something so sad so casually!"
    show yui happy with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI064.ogg"
    yui "It'll be a new term at the end of this month..."
    voice "audio/voice/E1/YUI/01/HA/HA055.ogg"
    hachiman "Hmm... Yeah..."
    show yui vhappy with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI065.ogg"
    yui "This year went by like, so quick~!"
    hachiman "(Yeah, some drag on and some go by quick. That's just how it goes, I guess.)"
    show yui happy with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI066.ogg"
    yui "Say, Hikki... Again, let's get along this year, too!"
    voice "audio/voice/E1/YUI/01/HA/HA056.ogg"
    hachiman "Y-Yeah... um... Likewise."
    hachiman "(Well, a lot of things happened, so it really seems it just went by in the blink of an eye.)"
    jump yui_shrine_cards

label yui_shrine_end:
    hide yui with dissolve
    stop music fadeout 0.5
    stop ambient fadeout 1.0
    stop music fadeout 0.5
    scene market
    with Fade(1.0, 0.5, 1.0)
    play ambient "<loop 2>audio/sfx/SE05/SE05_00L.ogg" loop
    $ renpy.pause(delay=1, hard=True)
    play music  "audio/bgm/BGM30.ogg"
    show yui coat mid_center happy at center with dissolve:
        yoffset 75
    voice "audio/voice/E1/YUI/01/YI/YI067.ogg"
    yui "Say, Hikki... Are you free tomorrow?"
    voice "audio/voice/E1/YUI/01/HA/HA057.ogg"
    hachiman "Hm? Can't say I'm busy... Why are you asking?"
    show yui surprised with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI068.ogg"
    yui "Ah, Yukinon!"
    hide yui with dissolve
    show yui coat surprised mid_center at right:
        xoffset -150 yoffset 75
    show yukino coat surprised mid_center at left:
        xoffset 150 yoffset 75
    with dissolve
    voice "audio/voice/E1/YUI/01/YK/YK009.ogg"
    yukino "I'm... sorry. About suddenly going off on my own."
    voice "audio/voice/E1/YUI/01/HA/HA058.ogg"
    hachiman "There was a Pan-san, right? Did you get him?"
    show yukino sad mid_center at left with dissolve
    voice "audio/voice/E1/YUI/01/YK/YK010.ogg"
    yukino "Yes, but upon closer inspection, it was a fake."
    show yui sad mid_left at right with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI069.ogg"
    yui "Aw... yeah, things like that do happen."
    voice "audio/voice/E1/YUI/01/YK/YK011.ogg"
    yukino "I can't believe I wasn't able to realize it at first glance..."
    voice "audio/voice/E1/YUI/01/HA/HA059.ogg"
    hachiman "So, Yuigahama..."
    hide yui with dissolve
    show yui coat blush near_center at right with dissolve
    voice "audio/voice/E1/YUI/01/YI/YI070.ogg"
    yui "Ah, um... I'll mail you about it later, okay?"
    hide yui with dissolve
    show yui coat vhappy mid_left at right with dissolve:
        xoffset -150
    voice "audio/voice/E1/YUI/01/YI/YI071.ogg"
    yui "Hey, Yukinon! Let's grab some takoyaki!"
    show yukino surprised mid_center at left with dissolve
    voice "audio/voice/E1/YUI/01/YK/YK012.ogg"
    yukino "Eh? You still want to eat?"
    hachiman "(She'll mail me later, huh... What does she want?)"
    hide yui
    hide yukino
    with dissolve
    stop music fadeout 0.5
    stop ambient fadeout 1.0
    stop sound fadeout 0.5
    jump E1_CMM_02

label E1_YUI_03:
    scene stationA with Fade(1.0, 0.5, 1.0)
    voice "audio/voice/E1/YUI/03/HA/HA000.ogg"
    hachiman "It's freezing! Oddly enough, I've been out and about quite a bit since the New Year."
    show yui coat mid_center surprised2 at center with dissolve:
        xoffset 35 yoffset 75
    play music "audio/bgm/BGM41.ogg"
    voice "audio/voice/E1/YUI/03/YI/YI000.ogg"
    yui "Sorry I'm late!"
    show yui surprised with dissolve
    voice "audio/voice/E1/YUI/03/HA/HA001.ogg"
    hachiman "No worries."
    show yui pout with dissolve
    voice "audio/voice/E1/YUI/03/YI/YI001.ogg"
    yui "Were you waiting a while?"
    menu yui_station:
        "I just got here":
            voice "audio/voice/E1/YUI/03/HA/HA002.ogg"
            hachiman "Nah, I just got here."
            voice "audio/voice/E1/YUI/03/YI/YI002.ogg"
            yui "..."
            voice "audio/voice/E1/YUI/03/HA/HA003.ogg"
            hachiman "..."
            show yui blush with dissolve
            voice "audio/voice/E1/YUI/03/YI/YI003.ogg"
            yui "Even though we're just having a normal conversation, it's kind of embarrassing..."
            voice "audio/voice/E1/YUI/03/HA/HA004.ogg"
            hachiman "Stop it, idiot. I'm starting to feel awkward, too."
            show yui surprised with dissolve
            voice "audio/voice/E1/YUI/03/YI/YI004.ogg"
            yui "You are, Hikki?"
            voice "audio/voice/E1/YUI/03/HA/HA005.ogg"
            hachiman "Uh, well... kind of..."
            show yui vhappy with dissolve
            voice "audio/voice/E1/YUI/03/YI/YI005.ogg"
            yui "Oh... I see."
            hachiman "(Me and Yuigahama are going shopping, but... it'll be just the two of us?)"
            show yui happy with dissolve
            voice "audio/voice/E1/YUI/03/YI/YI012.ogg"
            yui "So, wanna get going?"
            voice "audio/voice/E1/YUI/03/HA/HA013.ogg"
            hachiman "S-Sure..."
            hachiman "(I'm actually getting nervous...)"
        "No, not really": #yukino route
            voice "audio/voice/E1/YUI/03/HA/HA006.ogg"
            hachiman "No, not really."
            show yui happy with dissolve
            voice "audio/voice/E1/YUI/03/YI/YI006.ogg"
            yui "Okay, that's good! There was a point in running!"
            voice "audio/voice/E1/YUI/03/HA/HA007.ogg"
            hachiman "Calm down a bit."
            show yui vhappy with dissolve
            voice "audio/voice/E1/YUI/03/YI/YI007.ogg"
            yui "Yeah, I'm okay now!"
            hachiman "(Me and Yuigahama shopping, huh... Just the two of us?)"
            show yui happy with dissolve
            voice "audio/voice/E1/YUI/03/YI/YI010.ogg"
            yui "Come on, let's go."
            voice "audio/voice/E1/YUI/03/HA/HA013.ogg"
            hachiman "S-Sure..."
            hachiman "(... I'm quite nervous now.)"
        "I've waited a while":
            voice "audio/voice/E1/YUI/03/HA/HA008.ogg"
            hachiman "I've waited a while"
            show yui sad with dissolve
            voice "audio/voice/E1/YUI/03/YI/YI008.ogg"
            yui "I-I'm sorry..."
            voice "audio/voice/E1/YUI/03/HA/HA009.ogg"
            hachiman "Eh, it's cause I came out earlier too..."
            "I was just stating the truth... And seeing how she ran with her cheeks red. I'm starting to get a bit embarrassed."
            show yui blush with dissolve
            voice "audio/voice/E1/YUI/03/YI/YI009.ogg"
            yui "I see... E-Erm, I was up early choosing my clothes and getting my make-up ready, was having a hard time choosing. That's why..."
            voice "audio/voice/E1/YUI/03/HA/HA010.ogg"
            hachiman "Ahh, it's okay, it's okay. I understand."
            hachiman "(The two of us are going to buy a present together... The two of us??)"
            show yui happy with dissolve
            voice "audio/voice/E1/YUI/03/YI/YI010.ogg"
            yui "Hora~ let's go."
            voice "audio/voice/E1/YUI/03/HA/HA013.ogg"
            hachiman "Uh, yeah..."
            hachiman "(... Somehow I'm really nervous.)"

    window auto hide dissolve
    scene black with Fade(1.0, 0,0)
    play ambient "audio/sfx/SE05/SE05_01L.ogg"
    scene mallA
    with Fade(0, 0, 1.0)
    show yui coat mid_center pout at center with dissolve:
        xoffset 35 yoffset 75
    window auto show dissolve
    voice "audio/voice/E1/YUI/03/YI/YI013.ogg"
    yui "It's super crowded, huh..."
    voice "audio/voice/E1/YUI/03/HA/HA014.ogg"
    hachiman "Looks like it's because of the lucky bag sales.                   T/N: Lucky bags are mystery boxes sold on New Year."
    stop music fadeout 0.5
    hachiman "(It's New Year's... I'd rather lie under a kotatsu right now.)"
    show yui sad with dissolve
    voice "audio/voice/E1/YUI/03/YI/YI014.ogg"
    yui "Yui: There's so many people. We're gonna lose each other in the crowd."
    window auto hide dissolve
    stop voice
    play music "audio/bgm/BGM22.ogg"
    scene black
    show yuimallCG:
        zoom 1.8
        xoffset -875
    with dissolve
    window auto show dissolve
    voice "audio/voice/E1/YUI/03/YI/YI015.ogg"
    yui "Ah! Hikki!"
    voice "audio/voice/E1/YUI/03/HA/HA015.ogg"
    hachiman "...!!"
    "Yuigahama grabs onto my arm as the crowd starts pushing us apart."
    hachiman "W-We're touching... W-We don't have a choice though. Still, I'm losing it... This is pretty embarrassing."
    voice "audio/voice/E1/YUI/03/YI/YI016.ogg"
    yui "S-Sorry..."
    voice "audio/voice/E1/YUI/03/HA/HA016.ogg"
    hachiman "W-Well... it's crowded after all. It can't be helped."
    voice "audio/voice/E1/YUI/03/YI/YI017.ogg"
    yui "Yeah... T-That's true... Thanks."
    hachiman "(T-this is an emergency. Calm down, Hachiman. Don't think about the soft warmth touching my arm. I'm a gentleman, after all.)"
    hide yuimallCG
    show yuimallCG
    with dissolve
    voice "audio/voice/E1/YUI/03/HA/HA017.ogg"
    hachiman "A-Anyway, we should go over there."
    voice "audio/voice/E1/YUI/03/YI/YI018.ogg"
    yui "S-Sure!"
    voice "audio/voice/E1/YUI/03/HA/HA018.ogg"
    hachiman "Wait, woah!"
    "(Damn, this place really is packed!)"
    #ideally define another sound channel
    play sound "audio/sfx/SE01/SE01_53.ogg"
    show yuimallCG at center, Shake(None, 0.5, dist=50):
        zoom 1.8 xoffset -875
    voice "audio/voice/E1/YUI/03/YI/YI019.ogg"
    yui "Ah!?"
    voice "audio/voice/E1/YUI/03/HA/HA019.ogg"
    hachiman "...!!"
    "This time, we both nearly got trampled and I held onto both of Yuigahama's arms without thinking."
    voice "audio/voice/E1/YUI/03/HA/HA020.ogg"
    hachiman "S-Sorry... Are you okay?"
    voice "audio/voice/E1/YUI/03/YI/YI020.ogg"
    yui "Y-yeah... I'm really sorry. Thanks..."
    voice "audio/voice/E1/YUI/03/HA/HA021.ogg"
    hachiman "N-nah, there's nothing we can really do about this."
    "(That's right, there's nothing we can do. We're not just hugging in public!)"
    hide yuimallCG
    show yuimallCG
    with dissolve
    voice "audio/voice/E1/YUI/03/YI/YI021.ogg"
    yui "Hikki..."
    voice "audio/voice/E1/YUI/03/HA/HA022.ogg"
    hachiman "Hm?"
    voice "audio/voice/E1/YUI/03/YI/YI022.ogg"
    yui "Um... My hand..."
    voice "audio/voice/E1/YUI/03/HA/HA023.ogg"
    hachiman "Ah, sorry..."
    voice "audio/voice/E1/YUI/03/YI/YI023.ogg"
    yui "I-It's fine. Wanna go?"
    voice "audio/voice/E1/YUI/03/HA/HA024.ogg"
    hachiman "Yeah..."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    scene mallB with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "The floor we went to wasn't nearly as crowded as the main entrance. Everyone wanted the lucky bags after all."
    show yui coat mid_center pout at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/03/YI/YI024.ogg"
    yui "We can finally take a breather..."
    voice "audio/voice/E1/YUI/03/HA/HA025.ogg"
    hachiman "Yeah..."
    voice "audio/voice/E1/YUI/03/YI/YI025.ogg"
    show yui surprised2
    yui "Ah!"
    voice "audio/voice/E1/YUI/03/HA/HA026.ogg"
    hachiman "Eh?"
    hide yui with dissolve
    "Yuigahama pulled me over to a corner filled with cute stuff."
    window auto hide dissolve
    scene mallB:
        zoom 1.8 xoffset -50 yoffset -430
    show yui coat near_left vhappy at center:
        xoffset 290 yoffset 75
    with dissolve
    window auto show dissolve
    play music "audio/bgm/BGM18.ogg"
    voice "audio/voice/E1/YUI/03/YI/YI026.ogg"
    yui "These gloves are so cute! And these socks, too! They'd definitely look good on Yukinon! Right, Hikki?"
    voice "audio/voice/E1/YUI/03/HA/HA027.ogg"
    hachiman "Well I guess she does love cats."
    hachiman "(I really just can't feel at ease in a trendy place like this...)"
    show yui happy with dissolve
    voice "audio/voice/E1/YUI/03/YI/YI027.ogg"
    yui "I think I'll go with this!"
    voice "audio/voice/E1/YUI/03/HA/HA028.ogg"
    hachiman "Yeah, looks good."
    show yui near_center happy at center with dissolve:
        xoffset 280 yoffset 75
    voice "audio/voice/E1/YUI/03/YI/YI028.ogg"
    yui "So what are you gonna get her?"
    voice "audio/voice/E1/YUI/03/HA/HA029.ogg"
    hachiman "Uh..."
    hachiman "(I can't just say I haven't thought about it at all, can I? Hm?)"
    window auto hide dissolve
    hide yui
    scene  mallB
    with dissolve
    window auto show dissolve
    "Something small a little ways away from the trendy corner caught my eye and I made my way over to it."
    voice "audio/voice/E1/YUI/03/HA/HA030.ogg"
    hachiman "Hmm..."
    show yui coat mid_center happy at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/03/YI/YI029.ogg"
    yui "Hikki! What are you looking at? Glasses? It says: \"blue light filter\"?"
    show yui angry with dissolve
    voice "audio/voice/E1/YUI/03/YI/YI030.ogg"
    yui "Hey, Hikki, what does \"blue light filter\" mean? \"blue light filter\"? Does it have something to do with computers?"
    hachiman "(Huh? You don't know?)"
    voice "audio/voice/E1/YUI/03/HA/HA031.ogg"
    hachiman "It has to do with blocking LED light that computer and smartphone screens emit."
    voice "audio/voice/E1/YUI/03/YI/YI031.ogg"
    show yui pout with dissolve
    yui "L? LE? ELT?"
    voice "audio/voice/E1/YUI/03/HA/HA032.ogg"
    hachiman "Your eyes get tired when you use a computer or a phone for a while, right?"
    voice "audio/voice/E1/YUI/03/YI/YI032.ogg"
    yui "S-Sure..."
    voice "audio/voice/E1/YUI/03/HA/HA033.ogg"
    hachiman "It blocks out some of the light that makes your eyes tired, so it's like a protector for the eyes."
    show yui happy with dissolve
    voice "audio/voice/E1/YUI/03/YI/YI033.ogg"
    yui "I don't really get it, but it sounds like they're good for the eyes!"
    voice "audio/voice/E1/YUI/03/HA/HA034.ogg"
    hachiman "Well... Yeah, let's go with that."
    show yui vhappy with dissolve
    voice "audio/voice/E1/YUI/03/YI/YI034.ogg"
    yui "Yukinon uses computer a lot, too. These are nice, they'd definitely suit her!"
    voice "audio/voice/E1/YUI/03/HA/HA035.ogg"
    hachiman "Hm... If you say so."
    hachiman "(It's relieving to hear Yuigahama likes them too.)"
    window auto hide dissolve
    stop music fadeout 0.5
    jump E1_CMM_04

label E1_YUI_04:
    play ambient "audio/sfx/SE05/SE05_01L.ogg"
    scene stationA
    show yui coat mid_center sad at center with dissolve:
        xoffset 35 yoffset 75
    window auto show dissolve
    voice "audio/voice/E1/YUI/04/HA/HA000.ogg"
    hachiman "Buying birthday presents and all is nice, but... that sure was tiring."
    voice "audio/voice/E1/YUI/04/YI/YI000.ogg"
    yui "Yeah, I didn't think there were that many people here."
    voice "audio/voice/E1/YUI/04/HA/HA001.ogg"
    hachiman "I wish people would sleep at home at least on New Year's..."
    show yui coat mid_left surprised at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/04/YI/YI001.ogg"
    yui "Huh?"
    voice "audio/voice/E1/YUI/04/HA/HA002.ogg"
    hachiman "What's wrong?"
    voice "audio/voice/E1/YUI/04/YI/YI002.ogg"
    yui "Hikki, look!"
    voice "audio/voice/E1/YUI/04/HA/HA003.ogg"
    hachiman "Hm? That's..."
    window auto hide dissolve
    stop ambient fadeout 1.0
    play music "audio/bgm/BGM47.ogg"
    scene stationA with Dissolve(1.5):
        zoom 2.0 yalign 1.0
    $renpy.pause(delay=1, hard=True)
    show hayama coat far_right happy flat at left:
        xoffset 140 alpha 0 yoffset 70
        parallel:
            linear 0.3 alpha 1
        on hide:
            parallel:
                linear 0.3 alpha 0
    show yukino coat far_center angry flat at left:
        xoffset 340 alpha 0 yoffset 75
        parallel:
            linear 0.3 alpha 1
        on hide:
            parallel:
                linear 0.3 alpha 0
    $renpy.pause(delay=2.5, hard=False)
    show yukino coat far_center frown flat
    show hayama coat far_right happy flat
    with dissolve
    $renpy.pause(delay=1.0, hard=False)
    show haruno coat far_left sly at right:
        xoffset -330 alpha 0 yoffset 75
        parallel:
            linear 0.3 alpha 1
        on hide:
            parallel:
                linear 0.3 alpha 0
    show haruno coat far_left sly with dissolve
    $renpy.pause(delay=2.0, hard=False)
    hide hayama
    hide yukino
    hide haruno
    $renpy.pause(delay=2.0, hard=False)
    scene stationA
    show yui coat mid_left surprised at center:
        xoffset 35 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E1/YUI/04/YI/YI003.ogg"
    yui "That's Yukino and Hayato, right? Am I seeing things? I'm not, right?"
    voice "audio/voice/E1/YUI/04/HA/HA004.ogg"
    hachiman "No, I don't think you are."
    hachiman "(I saw them only for a moment, but they stand out. And Haruno was the one they were with. She really stands out, so I recognized her from the get go.)"
    show yui coat mid_center pout at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/04/YI/YI004.ogg"
    yui "W-What do we do..."
    voice "audio/voice/E1/YUI/04/HA/HA005.ogg"
    hachiman "Should we call out to them or should we leave them be... No, both of those don't feel right. Hm... What would you do?"
    show yui coat mid_center surprised at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/04/YI/YI005.ogg"
    yui "What would I do!? You flipped the question!?"
    voice "audio/voice/E1/YUI/04/HA/HA006.ogg"
    hachiman "Want to try calling out?"
    show yui coat mid_left surprised at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/04/YI/YI006.ogg"
    yui "Huh? Um... I guess..."
    stop music fadeout 1.0
    show yui coat mid_left angry at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/04/YI/YI007.ogg"
    yui "No, let's stop here today! We'll be jumping the gun!"
    voice "audio/voice/E1/YUI/04/HA/HA007.ogg"
    hachiman "True. Wait, what do you mean by jumping the gun?"
    play music "audio/bgm/BGM42.ogg"
    show yui coat mid_center happy at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/04/YI/YI008.ogg"
    yui "Tomorrow is Yukinon's birthday."
    hachiman "(Come to think of it, you did say it was tomorrow...)"
    voice "audio/voice/E1/YUI/04/YI/YI009.ogg"
    yui "So I want us to congratulate her tomorrow!"
    show yui coat mid_center vhappy at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/04/YI/YI010.ogg"
    yui "I'll ask her later if she has some free time tomorrow! Let's celebrate together!"
    voice "audio/voice/E1/YUI/04/HA/HA009.ogg"
    hachiman "Sure. What about my plans?"
    show yui coat mid_center happy at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/04/YI/YI011.ogg"
    yui "I mean, you never have those anyway."
    voice "audio/voice/E1/YUI/04/HA/HA010.ogg"
    hachiman "You're right, but still..."
    jump E1_YUI_05

label E1_YUI_05:
    show yui coat mid_center pout at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/05/YI/YI000.ogg"
    yui "By the way, what do we do now?"
    voice "audio/voice/E1/YUI/05/HA/HA000.ogg"
    hachiman "We did what we came here for, so... go home?"
    show yui coat mid_center surprised at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/05/YI/YI001.ogg"
    yui "Eh? You want to go home already?"
    show yui coat mid_center sad at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/05/YI/YI002.ogg"
    yui "Since we're here and all... why don't we have tea at least?"
    voice "audio/voice/E1/YUI/05/HA/HA001.ogg"
    hachiman "Well, thinking back, we did walk around a lot, so..."
    show yui coat mid_center vhappy at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/05/YI/YI003.ogg"
    yui "Yeah!"
    window auto hide dissolve
    scene cafeA
    show yui coat mid_center pout at center:
        xoffset 35 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E1/YUI/05/HA/HA002.ogg"
    hachiman "It's pretty packed in here, too."
    hide yui
    $url = ["yui coat mid_left pout", "yui coat mid_left happy"]
    $multiImagePara = [30, 75, 0, 0, 2.0]
    call multiImage() from _call_multiImage_900
    voice "audio/voice/E1/YUI/05/YI/YI004.ogg"
    yui "Yeah... Ah! There's free spots there!"
    call finishmultiImage from _call_finishmultiImage_900
    show yui coat mid_left happy at center:
        xoffset 30 yoffset 75
    voice "audio/voice/E1/YUI/05/HA/HA003.ogg"
    hachiman "Isn't it a little cramped?"
    show yui coat mid_center pout at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E1/YUI/05/YI/YI005.ogg"
    yui "There aren't any other seats though."
    voice "audio/voice/E1/YUI/05/HA/HA004.ogg"
    hachiman "Well, can't be helped."
    window auto hide dissolve
    stop music fadeout 1.0
    scene cafeA:
        zoom 2.0 yalign 0.4
    show yui home near_center blush at center:
        xoffset 250 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    play ambient "audio/sfx/SE05/SE05_02L.ogg"
    window auto show dissolve
    hachiman "(Ah... it's cramped. We're close, too...)"
    voice "audio/voice/E1/YUI/05/YI/YI006.ogg"
    yui "Haha... it's a little more, uh... cramped than I thought."
    voice "audio/voice/E1/YUI/05/HA/HA005.ogg"
    hachiman "R-Right..."
    voice "audio/voice/E1/YUI/05/YI/YI007.ogg"
    yui "..."
    voice "audio/voice/E1/YUI/05/HA/HA006.ogg"
    hachiman "..."
    menu yui_cafe1:
        hachiman "(This is awkward...)"
        "Aren't you tired?":
            play music "audio/bgm/BGM18.ogg"
            voice "audio/voice/E1/YUI/05/HA/HA007.ogg"
            hachiman "Aren't you pretty tired? It was packed in there."
            hide yui
            $url = ["yui home near_center surprised", "yui home near_center pout"]
            $multiImagePara = [250, 75, 0, 0, 1.0]
            call multiImage() from _call_multiImage_901
            voice "audio/voice/E1/YUI/05/YI/YI008.ogg"
            yui "Huh? S-Sure..."
            call finishmultiImage from _call_finishmultiImage_901
            show yui home near_center pout at center:
                xoffset 250 yoffset 75
            jump E1_YUI_06
        "I'm pretty tired.":
            "not done"
            jump yui_cafe1

label E1_YUI_06:
    show yui home near_center happy at center with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E1/YUI/06/YI/YI000.ogg"
    yui "I was really surprised there was that many people."
    voice "audio/voice/E1/YUI/06/HA/HA000.ogg"
    hachiman "I know, right?"
    voice "audio/voice/E1/YUI/06/YI/YI001.ogg"
    yui "But..."
    voice "audio/voice/E1/YUI/06/HA/HA001.ogg"
    hachiman "Hm?"
    show yui home near_center vhappy at center with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E1/YUI/06/YI/YI002.ogg"
    yui "I'm happy I got to go shopping with you today, Hikki."
    voice "audio/voice/E1/YUI/06/HA/HA002.ogg"
    hachiman "T-That so?"
    show yui home near_center blush at center with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E1/YUI/06/YI/YI003.ogg"
    yui "L-Like, you know, shopping with other people is pretty fun, right? Wondering what you're gonna buy, getting all excited about it and maybe finding something that you never thought you would!"
    voice "audio/voice/E1/YUI/06/HA/HA003.ogg"
    hachiman "Is that how it goes?"
    show yui home near_center happy at center with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E1/YUI/06/YI/YI004.ogg"
    yui "It is! I got to know for the first time what a blue light filter is today!"
    hachiman "(She's a bit far removed from those types of products.)"
    voice "audio/voice/E1/YUI/06/HA/HA004.ogg"
    hachiman "I'm glad we got to get it done together though. I managed to buy a present thanks to that."
    show yui home near_center surprised at center with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E1/YUI/06/YI/YI005.ogg"
    yui "Eh?"
    voice "audio/voice/E1/YUI/06/HA/HA005.ogg"
    hachiman "I honestly would've thought of dodging with a crowd like that."
    show yui home near_center pout at center with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E1/YUI/06/YI/YI006.ogg"
    yui "Ahaha... sounds like you, Hikki..."
    jump E1_YUI_08

label E1_YUI_08:
    show yui home near_center vhappy at center with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E1/YUI/08/YI/YI000.ogg"
    yui "I hope Yukinon'll like her presents!"
    voice "audio/voice/E1/YUI/08/HA/HA000.ogg"
    hachiman "Mhm. That'd be nice."
    show yui home near_center happy at center with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E1/YUI/08/YI/YI001.ogg"
    yui "I hope she'll be free tomorrow."
    voice "audio/voice/E1/YUI/08/HA/HA001.ogg"
    hachiman "..."
    show yui home near_center vhappy at center with dissolve:
        xoffset 250 yoffset 75
    voice "audio/voice/E1/YUI/08/YI/YI002.ogg"
    yui "I wonder if we can surprise her..."
    hachiman "(She's really looking forward to this, huh?)"
    window auto hide dissolve
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    stop voice
    scene black with dissolve
    $renpy.pause(delay=0.5, hard=True)
    play sound "<loop 2>audio/sfx/SE03/SE03_00L.ogg"
    $renpy.pause(delay=1.0, hard=False)
    scene bedroomC with dissolve
    window auto show dissolve
    voice "audio/voice/E1/YUI/08/HA/HA002.ogg"
    hachiman "Hm? Yuigahama?"
    window auto hide dissolve
    stop sound
    play sound "audio/sfx/SE03/SE03_01.ogg"
    call mail_clear from _call_mail_clear_900
    show black with dissolve:
        alpha 0.3
    play music "audio/bgm/BGM21.ogg"
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E1/YUI/08/YI/YI003.ogg"
    call mail_function("yui", "yui", "", "Yukinon, said she can't tomorrow. She said she'll be busy for a while.") from _call_mail_function_900
    yui "\"Yukinon, said she can't tomorrow. She said she'll be busy for a while.\""
    voice "audio/voice/E1/YUI/08/HA/HA003.ogg"
    hachiman "..."
    hachiman "(I'm guessing she's feeling a bit down because she was so excited... I can tell just by how she wrote that text.)"
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E1/YUI/08/YI/YI004.ogg"
    call mail_function("yui", "yui", "", "Yukinon seems like she's in a bit of trouble.") from _call_mail_function_901
    yui "\"Yukinon seems like she's in a bit of trouble.\""
    "What happened at noon flashed through my mind. I push those thoughts away though and start writing."
    play sound "audio/sfx/SE03/SE03_02.ogg"
    $renpy.pause(delay=0.5, hard=True)
    call mail_function("yui", "hachiman", "Re:", "Isn't she just busy with family stuff?") from _call_mail_function_902
    voice "audio/voice/E1/YUI/08/HA/HA004.ogg"
    hachiman "\"Isn't she just busy with family stuff?\""
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E1/YUI/08/YI/YI005.ogg"
    call mail_function("yui", "yui", "Re2:", "Yeah. Yukinon's family's just like that sometimes I guess.") from _call_mail_function_903
    yui "\"Yeah. Yukinon's family's just like that sometimes I guess.\""
    play sound "audio/sfx/SE03/SE03_02.ogg"
    $renpy.pause(delay=0.5, hard=True)
    call mail_function("yui", "hachiman", "", "Well, when the new term starts, she'll have to see us whether she likes it or not, so why not ask her about it then?") from _call_mail_function_904
    voice "audio/voice/E1/YUI/08/HA/HA005.ogg"
    hachiman "\"Well, when the new term starts, she'll have to see us whether she likes it or not, so why not ask her about it then?\""
    play sound "audio/sfx/SE03/SE03_02.ogg"
    $renpy.pause(delay=0.5, hard=True)
    call mail_function("yui", "hachiman", "", "If something really were to happen, I bet she'd tell you about it.") from _call_mail_function_905
    voice "audio/voice/E1/YUI/08/HA/HA006.ogg"
    hachiman "\"If something really were to happen, I bet she'd tell you about it.\""
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E1/YUI/08/YI/YI006.ogg"
    call mail_function("yui", "yui", "Re:", "That'd be nice. I mean, it'd be nice if nothing were to happen! I'm just a little worried, I guess.") from _call_mail_function_906
    yui "\"That'd be nice. I mean, it'd be nice if nothing were to happen! I'm just a little worried, I guess.\""
    "That relationship Yukinoshita has with her family is complicated. Those are relationships outsiders don't understand and it's not something you should thread on lightly."
    "Knowing that, Yuigahama isn't pushing her worries onto Yukinoshita. It's a very noble kindness she has."
    "My words might mean little to someone like her, but..."
    play sound "audio/sfx/SE03/SE03_02.ogg"
    $renpy.pause(delay=0.5, hard=True)
    call mail_function("yui", "hachiman", "Re2:", "Let's throw her a big party that'll drive all that away. Maybe something like surprising her in the club room would do it. Not that I would know.") from _call_mail_function_907
    voice "audio/voice/E1/YUI/08/HA/HA007.ogg"
    hachiman "\"Let's throw her a big party that'll drive all that away. Maybe something like surprising her in the club room would do it. Not that I would know.\""
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E1/YUI/08/YI/YI007.ogg"
    call mail_function("yui", "yui", "Re3:", "Yeah! You might be right! You're right! Thinking about it like that has me kind of excited for the new term!") from _call_mail_function_908
    yui "\"Yeah! You might be right! You're right! Thinking about it like that has me kind of excited for the new term!\""
    hachiman "(I hope all the concerns end up being groundless... for Yuigahama's sake as well.)"
    call mail_clear from _call_mail_clear_901
    window auto hide dissolve
    stop music fadeout 1.0
    jump E2_CMM_01
