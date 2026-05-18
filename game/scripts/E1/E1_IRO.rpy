label E1_IRO_01:
    play music ["<silence 0.3>", "audio/bgm/BGM36.ogg"]
    show iroha coat far_left happy at left with dissolve:
        xoffset 340 yoffset 80
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E1/IRO/01/HA/HA000.ogg"
    hachiman "......Isshiki?"
    hachiman "(She's here for new year's visit too? It's surprising to see her alone... eh?)"
    show iroha coat far_center happy at left with dissolve:
        xoffset 335 yoffset 75
    show iroha:
        parallel:
            linear 0.1 yoffset 45
            pause 0.08
            linear 0.1 yoffset 75
            pause 0.08
            repeat 4
    voice "audio/voice/E1/IRO/01/IR/IR000.ogg"
    iroha ".....!"
    hide iroha with dissolve
    show komachi coat mid_center happy at center with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E1/IRO/01/HA/HA001.ogg"
    hachiman "...What is she doing?"
    voice "audio/voice/E1/IRO/01/HA/HA002.ogg"
    hachiman "Komachi, something came up. You can go home ahead."
    show komachi surprised with dissolve
    voice "audio/voice/E1/IRO/01/KO/KO000.ogg"
    komachi "Eh? Ah, Okay!"
    hide komachi with dissolve
    hachiman "(Let's see...)"
    window auto hide dissolve
    scene market:
        zoom 1.5 xoffset -290 ypos -425
    show iroha coat mid_left happy at center:
        xoffset -10 yoffset 65
    with dissolve
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E1/IRO/01/HA/HA003.ogg"
    hachiman "Isshiki, did you want to tell me something?"
    show iroha coat mid_center frown at center with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E1/IRO/01/IR/IR001.ogg"
    iroha "Senpai! Why were you ignoring me~?"
    voice "audio/voice/E1/IRO/01/HA/HA004.ogg"
    hachiman "...No, it's just that I didn't notice earlier. Besides if I really wanted to ignore you I wouldn't have come over."
    voice "audio/voice/E1/IRO/01/HA/HA005.ogg"
    hachiman "...Later then."
    show iroha angry with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR002.ogg"
    iroha "Wait, senpai! Why are you rushing off already?"
    voice "audio/voice/E1/IRO/01/HA/HA006.ogg"
    hachiman "I only came to say hi.."
    hide iroha
    $url = ["iroha coat mid_center unimpressed", "iroha coat mid_center angry"]
    $multiImagePara = [25, 75, 0, 0, 4.5]
    call multiImage(0) from _call_multiImage_74
    voice "audio/voice/E1/IRO/01/IR/IR003.ogg"
    iroha "Hah, I see. Thanks, but... Even if you don't have something to say, I do!"
    call finishmultiImage from _call_finishmultiImage_78
    show iroha coat mid_center angry at center:
        xoffset 25 yoffset 75
    voice "audio/voice/E1/IRO/01/HA/HA007.ogg"
    hachiman "...What's that?"
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR004.ogg"
    iroha "Ahem... Happy New Year."
    voice "audio/voice/E1/IRO/01/HA/HA008.ogg"
    hachiman "What's this all of a sudden?"
    show iroha vhappy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR005.ogg"
    iroha "I wanted to wish you a Happy New Year, Senpai."
    "(The way she's smiling... I can't cut this conversation short like I initially intended.)"
    window auto hide dissolve
    stop music fadeout 0.5
    call card_loading from _call_card_loading_E1_IRO_01
    scene market:
        zoom 1.5 xoffset -290 ypos -425
    show iroha coat mid_center vhappy at center:
        xoffset 25 yoffset 75
    with dissolve
    $card_queue = ["New \nYear's \nvisit", "About \nwinter \nvacation", "Regarding \nyour \nwish", "About \nHayama", "End \nconversation"]
    play music "audio/bgm/BGM31.ogg"
    $E1_IRO_01_card_count = 0
    $E1_IRO_01_ellipses_count = 0
    jump E1_IRO_01_cards

#card minigame
#all ellipses are incomplete

label E1_IRO_01_cards:
    if E1_IRO_01_card_count < 4:
        $E1_IRO_01_card_count += 1
        $renpy.pause(delay=0.5, hard=True)
        $ch2 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch2)
        $ch3 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch3)
        window auto hide dissolve
        call screen three_minigame("...", ch2, ch3) with dissolve
        if _return == 1:
            # "not done"
            # $card_queue.append(ch2)
            # $card_queue.append(ch3)
            # $E1_IRO_01_card_count -= 1
            # jump E1_IRO_01_cards
            if ch2 == "End \nconversation":
                $card_queue.append(ch2)
            elif ch3 == "End \nconversation":
                $card_queue.append(ch3)
            else:
                $card_queue.append(renpy.random.choice([ch2,ch3]))
            $E1_IRO_01_ellipses_count += 1
            if E1_IRO_01_ellipses_count == 1:
                jump E1_IRO_01_ellipses1
            elif E1_IRO_01_ellipses_count == 2:
                jump E1_IRO_01_ellipses2
            elif E1_IRO_01_ellipses_count == 3:
                jump E1_IRO_01_ellipses3
            elif E1_IRO_01_ellipses_count == 4:
                jump E1_IRO_01_ellipses4

        elif _return == 2:
            $card_queue.append(ch3)
            if ch2 == "New \nYear's \nvisit":
                jump new_year_s_visit_card
            elif ch2 == "About \nwinter \nvacation":
                jump about_winter_vacation_card
            elif ch2 == "Regarding \nyour \nwish":
                jump regarding_your_wish_card
            elif ch2 == "About \nHayama":
                jump about_hayama_card
            else:
                jump E1_IRO_01_exit1
        elif _return == 3:
            $card_queue.append(ch2)
            if ch3 == "New \nYear's \nvisit":
                jump new_year_s_visit_card
            elif ch3 == "About \nwinter \nvacation":
                jump about_winter_vacation_card
            elif ch3 == "Regarding \nyour \nwish":
                jump regarding_your_wish_card
            elif ch3 == "About \nHayama":
                jump about_hayama_card
            else:
                jump E1_IRO_01_exit1
    else:
        if E1_IRO_01_ellipses_count == 0:
            jump E1_IRO_01_exit4
        elif E1_IRO_01_ellipses_count < 2:
            jump E1_IRO_01_exit3
        else:
            jump E1_IRO_01_exit2

label E1_IRO_01_ellipses1:
    window auto show dissolve
    show iroha frown with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR006.ogg"
    iroha "Why aren't you saying anything?"
    voice "audio/voice/E1/IRO/01/HA/HA009.ogg"
    hachiman "Why would I?"
    voice "audio/voice/E1/IRO/01/IR/IR007.ogg"
    iroha "..."
    voice "audio/voice/E1/IRO/01/IR/IR008.ogg"
    show iroha surprised
    iroha "......"
    voice "audio/voice/E1/IRO/01/IR/IR009.ogg"
    iroha "Ah..."
    hachiman "(Ah...)"
    image iro_sneeze = Flatten("iroha coat mid_center vhappy")
    hide iroha
    show iro_sneeze at center:
        xoffset 25 yoffset 75
    with dissolve
    show iro_sneeze:
        parallel:
            easein 0.2 yoffset 45
            easein 0.1 yoffset 105
            easein 0.2 yoffset 75
    voice "audio/voice/E1/IRO/01/IR/IR010.ogg"
    iroha "Achoo!"
    hide iro_sneeze
    show iroha coat mid_center blush at center:
        xoffset 25 yoffset 75
    with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR011.ogg"
    iroha "Ehehe, sorry I'm a bit cold."
    show iroha vhappy with dissolve
    hachiman "(Even her sneeze sounds cunning!)"
    jump E1_IRO_01_cards

label E1_IRO_01_ellipses2:
    window auto show dissolve
    show iroha unimpressed with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR012.ogg"
    iroha "Senpai you haven't changed at all since New Year. You still have the same dead fish eyes."
    voice "audio/voice/E1/IRO/01/HA/HA010.ogg"
    hachiman "That's gonna need more than just a few weeks to change..."
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR013.ogg"
    iroha "I guess that's true. I've noticed it before, but... senpai, even you can be wise sometimes."
    hachiman "(Why, you...)"
    jump E1_IRO_01_cards

label E1_IRO_01_ellipses3:
    window auto show dissolve
    show iroha pout with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR014.ogg"
    iroha "I'm embarrassed to go say hello a second time."
    voice "audio/voice/E1/IRO/01/HA/HA011.ogg"
    hachiman "Really?"
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR015.ogg"
    iroha "Yes!"
    show iroha vhappy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR016.ogg"
    iroha "\"I'm really not very good at anything, but please be nice to me anyway.\" - I would sound something like that!"
    voice "audio/voice/E1/IRO/01/HA/HA012.ogg"
    hachiman "R-Right. It's not like I don't get that, but... I'd say the problem is in your phrasing."
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR017.ogg"
    iroha "So then all it matters is how you say it?"
    voice "audio/voice/E1/IRO/01/HA/HA013.ogg"
    hachiman "It just dawned on me, but... yeah, pretty much."
    show iroha vhappy with dissolve
    jump E1_IRO_01_cards

label E1_IRO_01_ellipses4:
    window auto show dissolve
    show iroha frown with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR018.ogg"
    iroha "..."
    voice "audio/voice/E1/IRO/01/HA/HA014.ogg"
    hachiman "..."
    show iroha pout with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR019.ogg"
    iroha "Senpai... since it's been a while, say something."
    voice "audio/voice/E1/IRO/01/HA/HA015.ogg"
    hachiman "What do you mean \"say something\"?"
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR020.ogg"
    iroha "Anything's fine. Something you want to talk about."
    voice "audio/voice/E1/IRO/01/HA/HA016.ogg"
    hachiman "If only I had something to talk about, I'd be talking."
    show iroha vhappy with dissolve
    jump E1_IRO_01_exit1

label about_winter_vacation_card:
    window auto show dissolve
    voice "audio/voice/E1/IRO/01/HA/HA017.ogg"
    hachiman "What did you do during your winter break?"
    show iroha frown with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR021.ogg"
    iroha "Let's see... club activities, student council stuff. I also went shopping with my friends. I went to that one cake shop, too..."
    show iroha vhappy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR022.ogg"
    iroha "I did a lot of winter break-y things!"
    voice "audio/voice/E1/IRO/01/HA/HA018.ogg"
    hachiman "You do all of that throughout the year anyway..."
    jump E1_IRO_01_cards

label new_year_s_visit_card:
    window auto show dissolve
    voice "audio/voice/E1/IRO/01/HA/HA019.ogg"
    hachiman "Do you do shrine visits every year?"
    show iroha frown with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR023.ogg"
    iroha "Hmm, I wouldn't say every year. I wanted to try coming alone this year."
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR024.ogg"
    iroha "On the off-chance I might run into Hayama-senpai~!"
    voice "audio/voice/E1/IRO/01/IR/IR025.ogg"
    iroha "But the senpai I got to meet was you."
    hachiman "(Well sorry I'm not Hayama!)"
    show iroha vhappy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR026.ogg"
    iroha "But... I'm glad I came."
    voice "audio/voice/E1/IRO/01/HA/HA020.ogg"
    hachiman "...I see."
    hachiman "(What a mischievous reply...)"
    jump E1_IRO_01_cards

label regarding_your_wish_card:
    window auto show dissolve
    voice "audio/voice/E1/IRO/01/HA/HA021.ogg"
    hachiman "Have you already made a wish for this year?"
    voice "audio/voice/E1/IRO/01/IR/IR027.ogg"
    iroha "Yes, of course. I prayed for good things happening throughout the year."
    voice "audio/voice/E1/IRO/01/HA/HA022.ogg"
    hachiman "Oh?"
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR028.ogg"
    iroha "I also wished to get closer to Hayama-senpai, that I get good grades..."
    voice "audio/voice/E1/IRO/01/IR/IR029.ogg"
    iroha "And for student council work to be easier."
    voice "audio/voice/E1/IRO/01/HA/HA023.ogg"
    hachiman "Hey now, that's too many wishes. You'll work the gods to death."
    show iroha frown with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR030.ogg"
    iroha "Eeh~ I have more thing I want though~"
    voice "audio/voice/E1/IRO/01/HA/HA024.ogg"
    hachiman "Seriously?"
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR031.ogg"
    iroha "Of course. For example, Senpa..."
    voice "audio/voice/E1/IRO/01/HA/HA025.ogg"
    hachiman "Hmm?"
    voice "audio/voice/E1/IRO/01/IR/IR032.ogg"
    iroha "I'll stop there. Wishes only come true if you don't share them~"
    "Saying that, Isshiki winked mischievously."
    show iroha vhappy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR033.ogg"
    iroha "So it's a secret♪"
    jump E1_IRO_01_cards

label about_hayama_card:
    window auto show dissolve
    voice "audio/voice/E1/IRO/01/HA/HA026.ogg"
    hachiman "So, did you manage to meet Hayama?"
    show iroha frown with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR034.ogg"
    iroha "...Can't you tell?"
    voice "audio/voice/E1/IRO/01/HA/HA027.ogg"
    hachiman "I guess you didn't."
    voice "audio/voice/E1/IRO/01/IR/IR035.ogg"
    iroha "Geez.. What did I come here for~?"
    voice "audio/voice/E1/IRO/01/HA/HA028.ogg"
    hachiman "For the New Years visit?"
    jump E1_IRO_01_cards

label E1_IRO_01_exit1:
    voice "audio/voice/E1/IRO/01/HA/HA029.ogg"
    hachiman "Well, I'll be leaving now."
    show iroha frown with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR036.ogg"
    iroha "Please stay here and listen to me. I haven't even told you anything yet~"
    hachiman "(I've heard plenty already...)"
    jump E1_IRO_O1_cont

label E1_IRO_01_exit2:
    show iroha pout with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR037.ogg"
    iroha "Did you not make a wish, senpai?"
    voice "audio/voice/E1/IRO/01/HA/HA030.ogg"
    hachiman "Well, I did, just not for myself. Wishful thinking isn't going to change anything and if it did, that'd be rather scary."
    show iroha vhappy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR038.ogg"
    iroha "That's so like you, senpai-"
    jump E1_IRO_O1_cont

label E1_IRO_01_exit3:
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR039.ogg"
    iroha "When I talk to you, senpai, I feel like school is starting up again."
    voice "audio/voice/E1/IRO/01/HA/HA031.ogg"
    hachiman "Why me?"
    voice "audio/voice/E1/IRO/01/IR/IR040.ogg"
    iroha "Well, I basically only talk to you when I'm at school and our personal lives are completely unrelated, so... I guess that's why."
    hachiman "(Yeah, I can understand that.)"
    show iroha vhappy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR041.ogg"
    iroha "Right. And so, here's to the new school year!"
    jump E1_IRO_O1_cont

label E1_IRO_01_exit4:
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR042.ogg"
    iroha "Talking to you, senpai, it feels like a new year has already started."
    voice "audio/voice/E1/IRO/01/HA/HA032.ogg"
    hachiman "Eh, why?"
    voice "audio/voice/E1/IRO/01/IR/IR043.ogg"
    iroha "Talking to you like this has become quite natural for me. A daily occurance."
    voice "audio/voice/E1/IRO/01/HA/HA033.ogg"
    hachiman "............"
    show iroha vhappy with dissolve
    voice "audio/voice/E1/IRO/01/IR/IR044.ogg"
    iroha "So let's get along this year too~"
    voice "audio/voice/E1/IRO/01/HA/HA034.ogg"
    hachiman "Yeah, sure."
    jump E1_IRO_O1_cont

label E1_IRO_O1_cont:
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    scene irohashrine
    with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM34.ogg"
    window auto show dissolve
    voice "audio/voice/E1/IRO/01/HA/HA035.ogg"
    hachiman "So, do you have anything else for me?"
    voice "audio/voice/E1/IRO/01/IR/IR045.ogg"
    iroha "'Course I do! Since it's New Year's and all, let's go somewhere."
    voice "audio/voice/E1/IRO/01/HA/HA036.ogg"
    hachiman "Why do we have to go somewhere just because it's New Year's... Is it 'cause you couldn't meet with Hayama?"
    voice "audio/voice/E1/IRO/01/IR/IR046.ogg"
    iroha "There's that too, but... I won't have as much free time these days, you know~?"
    voice "audio/voice/E1/IRO/01/HA/HA037.ogg"
    hachiman "That \"you know~?\" isn't as convincing to me as you might think..."
    voice "audio/voice/E1/IRO/01/IR/IR047.ogg"
    iroha "So with that being said, how does meeting at Chiba station later sound, senpai?"
    voice "audio/voice/E1/IRO/01/HA/HA038.ogg"
    hachiman "It sounds like I'd rather go home..."
    voice "audio/voice/E1/IRO/01/IR/IR048.ogg"
    iroha "It's a promise then! I'll see you there, senpai!"
    window auto hide dissolve
    scene market:
        zoom 1.5 xoffset -290 ypos -425
    with dissolve
    play footsteps "audio/sfx/SE00/SE00_01.ogg"
    window auto show dissolve
    hachiman "(...She ran off without listening to me.)"
    window auto hide dissolve
    stop footsteps fadeout 0.5
    stop music fadeout 0.5
    jump E1_IRO_02

label E1_IRO_02:
    scene stationA
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "And just like that, as arranged by my little devil of a kouhai, I could only walk to Chiba station as she'd asked me to."
    voice "audio/voice/E1/IRO/02/IR/IR000.ogg"
    iroha "Sen~pai!"
    window auto hide dissolve
    play footsteps "audio/sfx/SE00/SE00_05.ogg"
    play music ["<silence 0.3>", "audio/bgm/BGM36.ogg"]
    $renpy.pause(delay=1.0, hard=True)
    show iroha coat mid_center vhappy at center with dissolve:
        xoffset 25 yoffset 75
    stop footsteps fadeout 0.5
    window auto show dissolve
    voice "audio/voice/E1/IRO/02/IR/IR001.ogg"
    iroha "...Hah, sorry for making you wait!"
    voice "audio/voice/E1/IRO/02/HA/HA000.ogg"
    hachiman "You should be. I've been waiting for ages."
    hide iroha 
    $url = ["iroha coat mid_center unimpressed", "iroha coat mid_center vhappy"]
    $multiImagePara = [25, 75, 0, 0, 2.6]
    call multiImage() from _call_multiImage_75
    voice "audio/voice/E1/IRO/02/IR/IR002.ogg"
    iroha "Geez, what's with that reaction~~ You should say \"I just got here\", okay?"
    call finishmultiImage from _call_finishmultiImage_79
    show iroha coat mid_center vhappy at center:
        xoffset 25 yoffset 75
    voice "audio/voice/E1/IRO/02/HA/HA001.ogg"
    hachiman "I. Just. Got. Here--"
    hide iroha
    $url = ["iroha coat mid_center frown", "iroha coat mid_center happy"]
    $multiImagePara = [25, 75, 0, 0, 2.6]
    call multiImage() from _call_multiImage_76
    voice "audio/voice/E1/IRO/02/IR/IR003.ogg"
    iroha "Why'd you say it like that? Well, it's good that you're here at least."
    call finishmultiImage from _call_finishmultiImage_80 
    show iroha coat mid_center vhappy at center:
        xoffset 25 yoffset 75
    with dissolve
    "Isshiki puffed her cheeks slightly before giving off a pretty smile and looking at me."
    "Even if it's a new year, she is still as cheeky as ever."
    show iroha angry with dissolve
    voice "audio/voice/E1/IRO/02/IR/IR004.ogg"
    iroha "Just as I thought, there's a lot of people at the station since it's New Year's."
    voice "audio/voice/E1/IRO/02/HA/HA002.ogg"
    hachiman "So... is there anywhere in particular you want to go?"
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/02/IR/IR005.ogg"
    iroha "Of course, isn't it obvious? We're here for lucky bags! {size=30}T/N: Sold on New Year's in Japan. Mystery box that contains various items that can outweigh the original cost.{/30}"
    voice "audio/voice/E1/IRO/02/HA/HA003.ogg"
    hachiman "Huh? Lucky bags?"
    show iroha surprised with dissolve
    voice "audio/voice/E1/IRO/02/IR/IR006.ogg"
    iroha "No way. You don't know about them, senpai? A lucky bag is..."
    voice "audio/voice/E1/IRO/02/HA/HA004.ogg"
    hachiman "You don't have to explain what a lucky bag is to me. I'm asking why you want to get your hands on them."
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/02/IR/IR007.ogg"
    iroha "New Year's and lucky bags go hand in hand, don't they? It's the one thing you have to get on New Year's."
    show iroha vhappy with dissolve
    voice "audio/voice/E1/IRO/02/IR/IR008.ogg"
    iroha "I've heard the more you buy, the luckier you'll get! I thought you'll need some too, so I brought you along."
    hachiman "(In other words, she wants me to carry her stuff...)"
    hide iroha with dissolve
    play sound "audio/sfx/SE01/SE01_12.ogg"
    show iroha coat near_left vhappy at center with dissolve:
        xoffset 260 yoffset 75
    $renpy.pause(delay=1.0, hard=True)
    voice "audio/voice/E1/IRO/02/IR/IR009.ogg"
    iroha "Come on, let's go, senpai! If we don't hurry, they'll be sold out soon!"
    voice "audio/voice/E1/IRO/02/HA/HA005.ogg"
    hachiman "Hold on, okay? Can you please not pull on my sleeve? It'll stretch..."
    window auto hide dissolve
    stop voice
    scene mallA
    with Fade(1.0, 0.5, 1.0)
    play ambient "audio/sfx/SE05/SE05_01L.ogg"
    show iroha coat mid_center happy at center with dissolve:
        xoffset 25 yoffset 75
    window auto show dissolve
    "Once inside the mall, while looking at the crowd, I thought \"is there really this many people in Chiba?\"."
    "Not only that, we're here for the lucky bags, which means we'll have to queue for at least an hour."
    show iroha frown with dissolve
    voice "audio/voice/E1/IRO/02/IR/IR010.ogg"
    iroha "Ahh, geez, there's so many people it's hard to walk."
    hide iroha with dissolve
    show iroha coat near_left happy at center with dissolve:
        xoffset 260 yoffset 75
    voice "audio/voice/E1/IRO/02/IR/IR011.ogg"
    iroha "Horahora, senpai! To protect a delicate girl is a guy's job!"
    voice "audio/voice/E1/IRO/02/HA/HA006.ogg"
    hachiman "Even if you say it's my job... Hah, Ugh... uh!"
    window auto hide dissolve
    hide iroha with dissolve
    play sound "audio/sfx/SE01/SE01_53.ogg"
    show mallA at center, Shake(None, 0.5, dist=50):
        zoom 1.75 xoffset -870 yoffset -415
    $renpy.pause(delay=1.0, hard=True)
    window auto show dissolve
    "Isshiki used me as a human shield to go through the crowd."
    "Something hard, then sharp, then sticky brushes against my body and ...did someone just touch my butt!?"
    show iroha coat near_center happy at center with dissolve:
        xoffset 225 yoffset 75
    voice "audio/voice/E1/IRO/02/IR/IR012.ogg"
    iroha " Senpai, just a little more! Ah, it's on the right here!"
    hachiman "(As expected I was really invited here just to be her shield/carrier.)"
    hachiman "(To have to do this during new year's... Where is all that luck she was talking about...)"
    show iroha surprised with dissolve
    voice "audio/voice/E1/IRO/02/IR/IR013.ogg"
    menu iroha_clinging_menu:
        iroha "Ah, we're starting to get seperated! Senpai, let me hold on to you!"
        with dissolve
        "Erm. That's...":
            "not done"
            jump iroha_clinging_menu
        "Since it's so crowded...":
            voice "audio/voice/E1/IRO/02/HA/HA008.ogg"
            hachiman "Ah, well... sure, since it's so crowded."
            show iroha happy with dissolve
            voice "audio/voice/E1/IRO/02/IR/IR016.ogg"
            iroha "That's what I thought~ If you refused, you'd fail not only as a man, but as a human."
            voice "audio/voice/E1/IRO/02/HA/HA009.ogg"
            hachiman "What am I if I fail even as a human...?"
            show iroha blush with dissolve
            voice "audio/voice/E1/IRO/02/IR/IR017.ogg"
            iroha "That's why..."
            voice "audio/voice/E1/IRO/02/HA/HA010.ogg"
            hachiman "That's why... what?"
            voice "audio/voice/E1/IRO/02/IR/IR018.ogg"
            iroha "...Let me hold on to you for a bit."
            window auto hide dissolve
            play sound "audio/sfx/SE01/SE01_13.ogg"
            show mallA at center, Shake(None, 0.5, dist=50):
                zoom 1.75 xoffset -870 yoffset -415
            show iroha coat near_center blush at center, Shake(None, 0.3, dist=50):
                xoffset 225 yoffset 75
            $renpy.pause(delay=1.0, hard=True)
            window auto show dissolve
            voice "audio/voice/E1/IRO/02/HA/HA013.ogg"
            hachiman "~~!"
            "Right after that, Isshiki held me tight with her slim hands, a whiff of perfume reaching my nose."
            show iroha vhappy with dissolve
            voice "audio/voice/E1/IRO/02/IR/IR022.ogg"
            iroha "Like this, we won't have to worry about getting separated."
            voice "audio/voice/E1/IRO/02/HA/HA014.ogg"
            hachiman "R-Right..."
            "What's making my heart skip, is it that smile, or the warmth I'm feeling from where she's holding me...?"
            hachiman "(But I guess there's only one reason.)"
            window auto hide dissolve
            stop ambient fadeout 0.5
            stop music fadeout 0.5
        "S-sure...":
            "not done"
            jump iroha_clinging_menu
    scene stationA with Fade(1.0, 0.5, 1.0)
    play music ["<silence 0.3>", "audio/bgm/BGM09.ogg"]
    show iroha coat mid_center vhappy at center with dissolve:
        xoffset 25 yoffset 75
    window auto show dissolve
    voice "audio/voice/E1/IRO/02/IR/IR023.ogg"
    iroha "Haaa~~! What a haul! I'm entirely satisfied!"
    voice "audio/voice/E1/IRO/02/HA/HA015.ogg"
    hachiman "I see. Good for you..."
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/02/IR/IR024.ogg"
    iroha "Senpai, where do we go next?"
    menu iro_station_menu:
        hachiman "(...We're still going somewhere?)"
        "Let's rest for a bit.":
            voice "audio/voice/E1/IRO/02/HA/HA016.ogg"
            hachiman "Let's rest for a bit first. If we go on like this, I won't be able to move at all."
            show iroha vhappy with dissolve
            voice "audio/voice/E1/IRO/02/IR/IR025.ogg"
            iroha "I guess so. I'm a little hungry too, so let's go to a cafe nearby."
            "She unexpectedly agrees with my suggestion and leads the way."
            window auto hide dissolve
            stop music fadeout 0.5
            jump E1_IRO_03
        "I want to go home.":
            "not done"
            jump iro_station_menu

label E1_IRO_03:
    scene cafeA
    with Fade(1.0, 0.5, 1.0)
    play music ["<silence 0.3>", "audio/bgm/BGM41.ogg"]
    play ambient "audio/sfx/SE05/SE05_02L.ogg"
    window auto show dissolve
    voice "audio/voice/E1/IRO/03/IR/IR000.ogg"
    iroha "~♪"
    "Before our orders even came, Isshiki started to opening her lucky bags."
    "Various items started coming out of the bag. Is that bag a fourth dimension? Are you going to take the anywhere door next? {size=30}T/N: Doraemon reference to a convenient portal.{/size}"
    window auto hide dissolve
    $renpy.pause(delay=0.5, hard=True)
    scene cafeA:
        zoom 1.5 xalign 0 ypos -310
    show iroha home mid_center happy at center:
        xoffset -5 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E1/IRO/03/HA/HA000.ogg"
    hachiman "...I gotta hand it to you. I didn't think you'd still want to buy it after seeing so many people."
    voice "audio/voice/E1/IRO/03/IR/IR001.ogg"
    show iroha vhappy with dissolve
    iroha "Heheh, a girl's driving force is buying things~"
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/03/IR/IR002.ogg"
    iroha "Is there a driving force you have, senpai?"
    hachiman "(I almost said \"my little sister\".)"
    voice "audio/voice/E1/IRO/03/HA/HA001.ogg"
    hachiman "Let's see... I guess getting to relax. Moving around is such a chore to begin with."
    show iroha surprised with dissolve
    voice "audio/voice/E1/IRO/03/IR/IR003.ogg"
    iroha "Is that so? But you came with me today, didn't you?"
    voice "audio/voice/E1/IRO/03/HA/HA002.ogg"
    hachiman "...I guess I did. It's New Year's after all."
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/03/IR/IR004.ogg"
    iroha "True. Since it's New Year's only once a year, it'll be a waste not to enjoy it."
    show iroha vhappy with dissolve
    voice "audio/voice/E1/IRO/03/IR/IR005.ogg"
    iroha "Let's go out together again sometime, senpai~!"
    voice "audio/voice/E1/IRO/03/HA/HA003.ogg"
    hachiman "...I'll think about it if I have time and it's someplace not as crowded."
    voice "audio/voice/E1/IRO/03/IR/IR006.ogg"
    iroha "Ahaha, Senpai, you've got nothing but time. We just have to think about where to go~"
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/03/IR/IR007.ogg"
    iroha "It's a promise then."
    "Isshiki didn't wait for my reply before she excitedly welcomed the cake that was just brought to us."
    hachiman "(If you just take the image of her enjoying the cake like this, she's actually pretty cute.)"
    window auto hide dissolve
    stop ambient fadeout 0.5
    scene cafeB:
        zoom 1.5 xalign 0 ypos -310
    with Fade(1.0, 0.5, 1.0)
    show iroha home mid_center happy at center with dissolve:
        xoffset -5 yoffset 75
    window auto show dissolve
    voice "audio/voice/E1/IRO/03/IR/IR008.ogg"
    iroha "This shops' cake and black tea are really good. What do you think, senpai?"
    voice "audio/voice/E1/IRO/03/HA/HA004.ogg"
    hachiman "I agree. It wasn't too sweet, so it went down easily."
    show iroha vhappy with dissolve
    voice "audio/voice/E1/IRO/03/IR/IR009.ogg"
    iroha "If senpai has an opinion that positive, it should be okay to invite Hayama-senpai here."
    hachiman "(...She's really putting in effort to research her date.)"
    "Looking at her innocent smile, I took the receipt thinking that it's about time to go."
    show iroha surprised with dissolve
    voice "audio/voice/E1/IRO/03/IR/IR010.ogg"
    iroha "Oh, are we leaving soon?"
    voice "audio/voice/E1/IRO/03/HA/HA005.ogg"
    hachiman "It's better if we don't stay too long. It'll start getting crowded, too."
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/03/IR/IR011.ogg"
    iroha "You're right. Let's go then."
    window auto hide dissolve
    stop voice fadeout 0.5
    play sound "audio/sfx/SE01/SE01_02.ogg"
    scene cafeB with dissolve
    window auto show dissolve
    hachiman "(Um, my portion was about 1200 yen...)"
    "While I was taking my wallet out, Isshiki also took her pink wallet out from her bag."
    show iroha coat_sunset mid_center happy at center with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E1/IRO/03/IR/IR012.ogg"
    iroha "Hah... Ah, I have just the right amount. Senpai, can you pay for mine with this?"
    "Isshiki passed me just enough for her share."
    voice "audio/voice/E1/IRO/03/HA/HA006.ogg"
    hachiman "............"
    show iroha surprised with dissolve
    voice "audio/voice/E1/IRO/03/IR/IR013.ogg"
    iroha "What is it?"
    voice "audio/voice/E1/IRO/03/HA/HA007.ogg"
    hachiman "It's nothing."
    hide iroha with dissolve
    hachiman "(This girl is pretty serious when it comes to money...)"
    "I walked toward the cashier after expressing my slight surprise."
    "Isshiki was about to exit the cafe when she turned around and whispered in my ear."
    show iroha coat_sunset near_left vhappy at center with dissolve:
        xoffset 260 yoffset 75
    voice "audio/voice/E1/IRO/03/IR/IR014.ogg"
    iroha "Treat me next time, okay?"
    voice "audio/voice/E1/IRO/03/HA/HA008.ogg"
    hachiman "............"
    voice "audio/voice/E1/IRO/03/HA/HA009.ogg"
    hachiman "There's a next time...?"
    show iroha happy with dissolve
    voice "audio/voice/E1/IRO/03/IR/IR015.ogg"
    iroha "What's with that unwilling reaction?"
    hide iroha with dissolve
    "Looking at Isshiki stepping cheerily away, I couldn't help but smile."
    window auto hide dissolve
    stop music fadeout 0.5
    jump E1_CMM_02
