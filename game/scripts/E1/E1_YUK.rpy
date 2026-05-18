label E1_YUK_01:
    scene market
    with Fade(1.0, 0.5, 1.0)
    play ambient "audio/sfx/SE05/SE05_00L.ogg"
    $renpy.pause(delay=1, hard=True)
    show komachi coat mid_center pout at right:
        xoffset -75 yoffset 75
    show yukino coat mid_center concerned at center:
        xoffset -105 yoffset 75
    show yui coat mid_center pout at left:
        xoffset 185 yoffset 75
    with dissolve
    play music "audio/bgm/BGM30.ogg"
    window auto show dissolve
    voice "audio/voice/E1/YUK/01/YK/YK000.ogg"
    yukino "............"
    show yukino unimpressed with dissolve
    voice "audio/voice/E1/YUK/01/YK/YK001.ogg"
    yukino "Crowds of people are tiring after all..."
    voice "audio/voice/E1/YUK/01/HA/HA000.ogg"
    hachiman "Agreed."
    show yui vhappy with dissolve
    voice "audio/voice/E1/YUK/01/YI/YI000.ogg"
    yui "Ah, Komachi-chan! Yukinon! Candied Apples! Hikki, can I go buy some!?"
    show komachi mid_left vhappy with dissolve:
        xoffset -150 yoffset 75
    show yukino surprised with dissolve
    voice "audio/voice/E1/YUK/01/KO/KO000.ogg"
    komachi "Ah! Komachi too! Komachi can go too right, Onii-chan?"
    hide komachi
    hide yui
    with dissolve
    voice "audio/voice/E1/YUK/01/HA/HA001.ogg"
    hachiman "You don't have to ask me do you? And you left without even waiting for a reply anyway... Was there a point in asking?"
    show yukino vhappy with dissolve
    voice "audio/voice/E1/YUK/01/YK/YK002.ogg"
    yukino "There wasn't."
    hachiman "(Well it's okay since it looks like they're having fun.)"
    show yukino blush with dissolve
    voice "audio/voice/E1/YUK/01/YK/YK003.ogg"
    yukino "............!"
    hide yukino with dissolve
    play footsteps "audio/sfx/SE00/SE00_03.ogg"
    voice "audio/voice/E1/YUK/01/HA/HA002.ogg"
    hachiman "H-Hey..."
    window auto hide dissolve
    scene market:
        zoom 1.5 xoffset -290 ypos -425
    show yukino coat mid_center stare at center:
        xoffset -105 yoffset 75
    with dissolve
    stop ambient fadeout 1
    window auto show dissolve
    voice "audio/voice/E1/YUK/01/YK/YK004.ogg"
    yukino "............"
    voice "audio/voice/E1/YUK/01/HA/HA003.ogg"
    hachiman "Hey, don't disappear like that too. What are you looking at so intently?"
    window auto hide dissolve
    stop music fadeout 0.5
    call card_loading from _card_loadingshrine
    scene market:
        zoom 1.5 xoffset -290 ypos -425
    show yukino coat mid_center happy at center:
        xoffset -105 yoffset 75
    with dissolve
    $card_queue = ["About the \nmarriage-\ntier prayer \nset", "About the \nshooting \ngallery \nprize", "About \nPan-san", "About the \nshooting \nbooth", "End \nconversation"]
    play music "audio/bgm/BGM31.ogg"
    $shrine_card_count = 0
    $shrine_ellipses = 0
    jump yuk_shrine_cards

#temporary setup until i get a working system:
#list of finished: ellipses 1 and 2, (not 3), shooting booth, marriage prayer, "that plushy", shooting prize
# first set of cards: ..., Shooting Booth, Marriage Prayer
# second set : ..., (shooting booth or marriage),  shooting prize
# third set: ... (not done), remainder of above, pan-san (not done)
# last set: cut short the convo (not done), about that plushy
#then auto jump to "about that plushy"

label yuk_shrine_cards:
    if shrine_card_count < 3:
        $shrine_card_count += 1
        $renpy.pause(delay=0.5, hard=True)
        $ch2 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch2)
        $ch3 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch3)
        window auto hide dissolve
        call screen three_minigame("...", ch2, ch3) with dissolve
        if _return == 1:
            if shrine_ellipses == 2:
                "not done"
                $card_queue.append(ch2)
                $card_queue.append(ch3)
                $shrine_card_count -= 1
                jump yuk_shrine_cards
            if ch2 == "End \nconversation":
                $card_queue.append(ch2)
            elif ch3 == "End \nconversation":
                $card_queue.append(ch3)
            else:
                $card_queue.append(renpy.random.choice([ch2,ch3]))
            if shrine_ellipses == 0:
                jump shrine_ellipses_card1
            elif shrine_ellipses == 1:
                jump shrine_ellipses_card2
        elif _return == 2:
            $card_queue.append(ch3)
            if ch2 == "About the \nmarriage-\ntier prayer \nset":
                jump marriage_set_card
            elif ch2 == "About the \nshooting \ngallery \nprize":
                jump shooting_prize_card
            elif ch2 == "About \nPan-san":
                $card_queue.append(ch2)
                jump pan_san_card
            elif ch2 == "About the \nshooting \nbooth":
                jump shooting_booth_card
            else:
                "not done"
                $card_queue.append(ch2)
                $shrine_card_count -= 1
                jump yuk_shrine_cards
        elif _return == 3:
            $card_queue.append(ch2)
            if ch3 == "About the \nmarriage-\ntier prayer \nset":
                jump marriage_set_card
            elif ch3 == "About the \nshooting \ngallery \nprize":
                jump shooting_prize_card
            elif ch3 == "About \nPan-san":
                $card_queue.append(ch3)
                jump pan_san_card
            elif ch3 == "About the \nshooting \nbooth":
                jump shooting_booth_card
            else:
                "not done"
                $card_queue.append(ch3)
                $shrine_card_count -= 1
                jump yuk_shrine_cards
    elif shrine_card_count == 3:
        jump yuk_shrine_cards4
    else:
        jump E1_YUK_01_cont

label yuk_shrine_cards4:
    call screen two_minigame("End \nconversation", "About \nthat \nplushie")
    $shrine_card_count = 4
    if _return == 1:
        jump shrine_cut_card
    if _return == 2:
        jump plushie_card

    #unknown for now: lines in the scene. Probably ellipses 3.
    show yukino mid_right surprised at center with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E1/YUK/01/YK/YK012.ogg"
    yukino "!!"
    voice "audio/voice/E1/YUK/01/HA/HA008.ogg"
    hachiman "Yukinoshita?"
    voice "audio/voice/E1/YUK/01/YK/YK013.ogg"
    show yukino mid_left pout with dissolve:
        xoffset 50 yoffset 80
    yukino "That... It's because... it was quite unusual..." #そ⋯⋯その⋯⋯珍しかったから⋯⋯
    voice "audio/voice/E1/YUK/01/HA/HA009.ogg"
    hachiman "Is that so."
    voice "audio/voice/E1/YUK/01/YK/YK014.ogg"
    show yukino sad with dissolve
    yukino "Um, I'm sorry for being so abruptly separated from you." #その、突然離れてしまって、ごめんなさい
    voice "audio/voice/E1/YUK/01/HA/HA010.ogg"
    hachiman "No, it's fine since I found you right away." #いや、すぐに見つかったから別にいい
    voice "audio/voice/E1/YUK/01/YK/YK015.ogg"
    yukino "Yes..." #その、突然離れてしまって、ごめんなさい
    show yukino pout2 with dissolve
    voice "audio/voice/E1/YUK/01/YK/YK016.ogg"
    yukino "Hikigaya-kun!... Um, I'm sorry." #比企谷くん⋯！ その、ごめんなさい
    show yukino pout with dissolve
    voice "audio/voice/E1/YUK/01/HA/HA011.ogg"
    hachiman "? Eh, why are you apologizing?" #？ え、何で謝るの？
    voice "audio/voice/E1/YUK/01/YK/YK017.ogg"
    yukino "..."
    hachiman "(... and why are you silent?)" #(⋯⋯しかもなんで黙るの？)
    voice "audio/voice/E1/YUK/01/YK/YK018.ogg"
    show yukino mid_right pout at center with dissolve:
        xoffset 25 yoffset 75
    yukino "That..."
    voice "audio/voice/E1/YUK/01/HA/HA012.ogg"
    hachiman "... The shooting gallery?" #⋯⋯射的か
    show yukino happy
    voice "audio/voice/E1/YUK/01/YK/YK019.ogg"
    yukino "Yes, that shooting gallery."
    #unknown for now

#done
label shrine_ellipses_card1:
    $shrine_ellipses = 1
    show yukino coat mid_right happy at center with dissolve:
        xoffset 25 yoffset 75
    window auto show dissolve
    voice "audio/voice/E1/YUK/01/YK/YK005.ogg" #head tilt
    yukino "............"
    hachiman "(Uh, Yukinoshita-san?)" #おーい、雪ノ下さーん
    voice "audio/voice/E1/YUK/01/YK/YK006.ogg"
    yukino "............"
    hachiman "I'm not being noticed for a while huh..." #これは、しばらく気付かないな
    jump yuk_shrine_cards
    #end

#done
label shrine_ellipses_card2:
    $shrine_ellipses = 2
    show yukino coat mid_right unimpressed at center with dissolve: #nod head
        xoffset 25 yoffset 75
        0.25
        linear 0.25 yoffset 100
        0.1
        linear 0.25 yoffset 75
    window auto show dissolve
    voice "audio/voice/E1/YUK/01/YK/YK007.ogg"
    yukino "............"
    voice "audio/voice/E1/YUK/01/HA/HA004.ogg"
    hachiman "Yukinoshita?"
    show yukino mid_left surprised at center with dissolve:
        xoffset 50 yoffset 80
    voice "audio/voice/E1/YUK/01/YK/YK008.ogg"
    yukino "A-Ah... Hikigaya-kun. I apologize. I didn't notice you right away." #"あ、ああ⋯⋯比企谷くん。ごめんなさい、すぐに気付かなくて"
    voice "audio/voice/E1/YUK/01/HA/HA005.ogg"
    hachiman "No. I'm used to not being noticed by people." #"いや。人に気付かれないのは慣れてるからな"
    show yukino mid_right vhappy at center with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E1/YUK/01/YK/YK009.ogg" #nod maybe
    yukino "That is true too. Happy New Year to you, I didn't think we would meet at the beginning of the year." #明けましておめでとう新年早々会うとは思わなかったわ
    voice "audio/voice/E1/YUK/01/HA/HA006.ogg"
    hachiman "Eh? You didn't realize it was me from the very beginning?... Just who were you talking to earlier then..." #えぇ⋯⋯最初の時点から気づいてなかったの⋯⋯君、さっき誰と会話してたの⋯⋯
    voice "audio/voice/E1/YUK/01/YK/YK010.ogg"
    show yukino happy with dissolve
    yukino "I'm just kidding. More importantly though..." #冗談よ。それより⋯⋯
    voice "audio/voice/E1/YUK/01/HA/HA007.ogg"
    hachiman "Hmm?"
    show yukino mid_right pout at center with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E1/YUK/01/YK/YK011.ogg"
    yukino "..."
    hachiman "(For the time being, it looks like she won't be moving from here.)" #（これは、しばらくここから動かなそうだな）
    jump yuk_shrine_cards

label shrine_ellipses_card3:
    "not done"
    jump yuk_shrine_cards3

#done
label shooting_booth_card:
    window auto show dissolve
    voice "audio/voice/E1/YUK/01/HA/HA016.ogg"
    hachiman "Are you interested in target-shooting?"
    voice "audio/voice/E1/YUK/01/YK/YK024.ogg" #shake head
    yukino "No, it's not like that... I just thought it was a bit unusual"
    voice "audio/voice/E1/YUK/01/HA/HA017.ogg"
    hachiman "You were looking at it pretty intensely."
    voice "audio/voice/E1/YUK/01/YK/YK025.ogg"
    yukino "I suppose. I was wondering who would play something like this."
    voice "audio/voice/E1/YUK/01/HA/HA018.ogg"
    hachiman "Okay..."
    #    show yukino coat mid_center concerned at center with dissolve:
    #        xoffset -85
    show yukino coat mid_right vhappy at center with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E1/YUK/01/YK/YK026.ogg"
    yukino "Yes. But it's somewhat nostalgic, isn't it?"
    voice "audio/voice/E1/YUK/01/HA/HA019.ogg"
    hachiman "I suppose."
    voice "audio/voice/E1/YUK/01/YK/YK027.ogg"
    yukino "Yes."
    jump yuk_shrine_cards
    #end

#done
label marriage_set_card:
    window auto show dissolve
    voice "audio/voice/E1/YUK/01/HA/HA023.ogg"
    hachiman "\"Marriage Prayer set?\" There was such a strange thing..." #『縁結び祈願セット』？ 変なものがあるな⋯⋯
    show yukino coat mid_left happy with dissolve:
        xoffset 50 yoffset 75
    voice "audio/voice/E1/YUK/01/YK/YK031.ogg"
    yukino "It's a bit strange indeed... Is there demand for this type of thing?" #確かに少し変ね⋯⋯。こういうの、需要あるのかしら⋯⋯ #Head Tilt
    voice "audio/voice/E1/YUK/01/HA/HA024.ogg"
    hachiman "Demand for marriage huh... Ah."
    show yukino mid_right surprised with dissolve: #Probably Hiratsuka pops into mind
        xoffset 25 yoffset 75
    voice "audio/voice/E1/YUK/01/YK/YK032.ogg"
    yukino "..."
    voice "audio/voice/E1/YUK/01/HA/HA025.ogg"
    hachiman "... There probably is."
    show yukino mid_left unimpressed with dissolve:
        xoffset 50 yoffset 80
        0.25
        linear 0.25 yoffset 100
        0.1
        linear 0.25 yoffset 80
    voice "audio/voice/E1/YUK/01/YK/YK033.ogg" #Head Nod
    yukino "Yes..."
    show yukino pout with dissolve
    stop voice
    jump yuk_shrine_cards

#not done
label pan_san_card:
    "not done"
    $shrine_card_count -= 1
    jump yuk_shrine_cards

#done and confirmed that this ends the scene probably a +1 yukino somewhere too
label plushie_card:
    window auto show dissolve
    voice "audio/voice/E1/YUK/01/HA/HA026.ogg"
    hachiman "Hm? That plushie..."
    show yukino coat mid_right surprised with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E1/YUK/01/YK/YK034.ogg"
    yukino "Wh- What is it!?"
    voice "audio/voice/E1/YUK/01/HA/HA027.ogg"
    hachiman "No, um, I feel like I've seen it somewhere before..."
    hide yukino
    $url = ["yukino coat mid_left vhappy", "yukino coat mid_left unimpressed"]
    $multiImagePara = [50, 80, 0, 0, 0.6]
    call multiImage() from _call_multiImage_31
    show mood1 at center:
        xoffset 50 yoffset 80
        parallel:
            0.5
            alpha 0
    hide mood2
    show mood2 at center: #nod head
        xoffset 50 yoffset 80 alpha 0
        parallel:
            0.4
            linear 0.1 alpha 1.0
            linear 0.25 yoffset 120
            0.1
            linear 0.25 yoffset 80
    voice "audio/voice/E1/YUK/01/YK/YK035.ogg"
    yukino "Yes... it's something you've seen before. Something very close, very nostalgic..."
    call finishmultiImage from _call_finishmultiImage_32
    show yukino coat mid_left vhappy at center:
        xoffset 50 yoffset 80
    voice "audio/voice/E1/YUK/01/HA/HA028.ogg"
    hachiman "I see."
    hachiman "(That's... a Pan-san plushie, right?)"
    show yukino mid_right frown at center with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E1/YUK/01/YK/YK036.ogg"
    yukino "But wait a moment." #tilt head
    voice "audio/voice/E1/YUK/01/HA/HA029.ogg"
    hachiman "What is it?"
    voice "audio/voice/E1/YUK/01/YK/YK037.ogg"
    yukino "There's something bothering me."
    voice "audio/voice/E1/YUK/01/HA/HA030.ogg"
    hachiman "Yeah..."
    voice "audio/voice/E1/YUK/01/YK/YK038.ogg"
    yukino "You've noticed it too?"
    voice "audio/voice/E1/YUK/01/HA/HA031.ogg"
    hachiman "Just somehow."
    hide yukino
    $url = ["yukino coat mid_right frown", "yukino coat mid_right unimpressed"]
    $multiImagePara = [25, 75, 0, 0, 0.9]
    call multiImage() from _call_multiImage_32
    show mood1 at center:
        xoffset 25 yoffset 75
        parallel:
            0.8
            alpha 0
        parallel:
            1.5
            alpha 1
    hide mood2
    show mood2 at center: #nod head
        xoffset 25 yoffset 75 alpha 0
        parallel:
            0.7
            linear 0.1 alpha 1.0
            linear 0.25 yoffset 115
            0.1
            linear 0.25 yoffset 75
        parallel:
            1.5
            alpha 0
    voice "audio/voice/E1/YUK/01/YK/YK039.ogg"
    yukino "Right. There's something off about it."
    call finishmultiImage from _call_finishmultiImage_33
    show yukino coat mid_right frown at center:
        xoffset 25 yoffset 75
    voice "audio/voice/E1/YUK/01/HA/HA032.ogg"
    hachiman "That it's a counterfeit?"
    voice "audio/voice/E1/YUK/01/YK/YK040.ogg" #Jump depending on choice I think.
    yukino "Yes. That probability is high."
    voice "audio/voice/E1/YUK/01/HA/HA042.ogg"#+10
    hachiman "...So? Do you want it?"
    show yukino mid_left sad with dissolve:
        xoffset 50 yoffset 80
    voice "audio/voice/E1/YUK/01/YK/YK052.ogg"#+10
    yukino "...No. There's no point in getting it. Looking at it carefully, it is a Pan-san fake."
    hachiman "(Just how much does this girl like Pan-san...)"
    #no voice on this line ^
    voice "audio/voice/E1/YUK/01/HA/HA043.ogg"
    hachiman "Is that so."
    voice "audio/voice/E1/YUK/01/YK/YK053.ogg"
    yukino "Yes."
    voice "audio/voice/E1/YUK/01/HA/HA044.ogg"
    hachiman "Well, it is from a booth. It means it's popular enough to make counterfeits of."
    show yukino mid_center vhappy with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E1/YUK/01/YK/YK054.ogg"
    yukino "That's true. As expected of Pan-san..."
    jump E1_YUK_01_cont

label shooting_prize_card:
    window auto show dissolve
    voice "audio/voice/E1/YUK/01/HA/HA020.ogg"
    hachiman "Is there something in those prizes which interests you?"#景品に何か気になる物でもあったか？
    show yukino mid_center blush with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E1/YUK/01/YK/YK028.ogg"
    yukino "Um... there are various miscellaneous things placed in there." #その⋯⋯色々なものが雑多に置かれているのね
    voice "audio/voice/E1/YUK/01/HA/HA021.ogg"
    hachiman "Yep. Incidentally, there seem to be many counterfeits." #そうだな。ちなみにパチモンも多い
    show yukino mid_right angry with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E1/YUK/01/YK/YK029.ogg"
    yukino "Is that the case?"
    voice "audio/voice/E1/YUK/01/HA/HA022.ogg"
    hachiman "Having those dubious prizes in there may be part of the fun, I guess." #その胡散臭さも含めての楽しみってとこだな Check this TL
    hide yukino
    $url = ["yukino coat mid_left vhappy", "yukino coat mid_left unimpressed"]
    $multiImagePara = [50, 80, 0, 0, 0.3]
    call multiImage() from _call_multiImage_33
    show mood1 at center:
        xoffset 50 yoffset 80
        parallel:
            0.2
            alpha 0
        parallel:
            0.8
            alpha 1
    hide mood2
    show mood2 at center: #nod head
        xoffset 50 yoffset 80 alpha 0
        parallel:
            0.1
            linear 0.1 alpha 1.0
            linear 0.25 yoffset 120
            0.1
            linear 0.25 yoffset 80
        parallel:
            0.8
            alpha 0
    voice "audio/voice/E1/YUK/01/YK/YK030.ogg"
    yukino "... That may be the case."
    call finishmultiImage from _call_finishmultiImage_34
    show yukino coat mid_left vhappy at center:
        xoffset 50 yoffset 80
    jump yuk_shrine_cards

label shrine_cut_card:
    "not finished"
    jump yuk_shrine_cards4

#End of minigame here.
label E1_YUK_01_cont:
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    scene market with Fade(1.0, 1.0, 1.0):
        zoom 1.5 xoffset -290 ypos -425
    play ambient "audio/sfx/SE05/SE05_00L.ogg"
    show yukino coat mid_center surprised at center with dissolve:
        xoffset -105 yoffset 75
        on hide:
            alpha 1
            parallel:
                linear 0.2 alpha 0
            parallel:
                linear 0.2 zoom 1.8
            parallel:
                linear 0.2 yoffset 500

    window auto show dissolve
    voice "audio/voice/E1/YUK/01/YK/YK055.ogg"
    yukino "...!"
    voice "audio/voice/E1/YUK/01/HA/HA045.ogg"
    hachiman "Oops-"
    window auto hide dissolve
    hide yukino
    $renpy.pause(delay=0.2, hard=True)
    stop ambient
    play sound "audio/sfx/SE01/SE01_13.ogg"
    scene black
    show yukinoshrine at center, Shake(None, 0.5, dist=50)
    play music "audio/bgm/BGM11.ogg"
    $renpy.pause(delay=1.0, hard=True)
    window auto show dissolve
    voice "audio/voice/E1/YUK/01/HA/HA046.ogg"
    hachiman "S-Sorry."
    voice "audio/voice/E1/YUK/01/YK/YK056.ogg"
    yukino "N-no... I'm sorry."
    window auto hide dissolve
    stop voice
    scene market
    show yukino coat near_center avoid at center:
        xoffset -165 yoffset 75
    with dissolve
    $renpy.pause(delay =0.5, hard=True)
    show yukino mid_center at center with dissolve:
        xoffset -105 yoffset 75
    window auto show dissolve
    "Yukinoshita quickly separated herself from me and the coldness of mid-winter regrettably took away the little bit of warmth lingering from her body temperature."
    voice "audio/voice/E1/YUK/01/HA/HA047.ogg"
    hachiman "............"
    voice "audio/voice/E1/YUK/01/YK/YK057.ogg"
    yukino "............"
    show yui coat far_left happy at right:
        xoffset -290 yoffset 75
    show komachi coat far_left happy at right:
        xoffset -125 yoffset 75
    with dissolve
    $renpy.pause(delay=1.5, hard=True)
    hide yui
    hide komachi
    with dissolve
    $renpy.pause(delay =0.5, hard=True)
    show yui coat mid_center vhappy at left:
        xoffset 190 yoffset 75
    show komachi coat mid_center vhappy at right:
        xoffset -75 yoffset 75
    with dissolve
    voice "audio/voice/E1/YUK/01/YI/YI001.ogg"
    yui "Sorry! Thanks for waiting!"
    voice "audio/voice/E1/YUK/01/KO/KO001.ogg"
    komachi "Onii-chan! We got the apple candies!"
    voice "audio/voice/E1/YUK/01/HA/HA048.ogg"
    hachiman "............"
    voice "audio/voice/E1/YUK/01/YK/YK058.ogg"
    yukino "............"
    show yui surprised
    show komachi surprised
    with dissolve
    voice "audio/voice/E1/YUK/01/YI/YI002.ogg"
    yui "What happened to you two? Did something happen?"
    show yukino blush with dissolve
    voice "audio/voice/E1/YUK/01/HA/HA049.ogg"
    hachiman "No, not really. Just something."
    voice "audio/voice/E1/YUK/01/YI/YI003.ogg"
    show yui happy with dissolve
    yui "Ah, it's Pan-san!"
    show yukino concerned with dissolve
    voice "audio/voice/E1/YUK/01/YK/YK059.ogg"
    yukino "A fake of..."
    show yui unimpressed with dissolve
    voice "audio/voice/E1/YUK/01/YI/YI004.ogg"
    yui "Ahh, I see..."
    show komachi mid_left unimpressed with dissolve:
        xoffset -150 yoffset 75
    voice "audio/voice/E1/YUK/01/KO/KO002.ogg"
    komachi "You'll find counterfeits at booths..."
    voice "audio/voice/E1/YUK/01/YK/YK060.ogg"
    yukino "That's true... it's not something to be disappointed about."
    hachiman "(Though you're completely disappointed.)"
    show yui vhappy with dissolve
    voice "audio/voice/E1/YUK/01/YI/YI005.ogg"
    yui "That's right! Yukinon, are you free tomorrow?"
    show yukino sad with dissolve
    voice "audio/voice/E1/YUK/01/YK/YK061.ogg"
    yukino "Tomorrow is a bit..."
    show yui sad with dissolve
    voice "audio/voice/E1/YUK/01/YI/YI006.ogg"
    yui "Oh..."
    show yui happy with dissolve
    voice "audio/voice/E1/YUK/01/YI/YI007.ogg"
    yui "Th-then, what about the day after?"
    show yukino vhappy with dissolve
    voice "audio/voice/E1/YUK/01/YK/YK062.ogg"
    yukino "I'm free then."
    show yui vhappy with dissolve
    voice "audio/voice/E1/YUK/01/YI/YI008.ogg"
    yui "Then let's all meet up the day after! Come on, Hikki! Komachi-chan too!"
    hachiman "(... You won't ask whether I have plans or not.)"
    voice "audio/voice/E1/YUK/01/HA/HA050.ogg"
    hachiman "Y-Yeah..."
    hide komachi
    $url = ["komachi coat mid_left happy", "komachi coat mid_left vhappy"]
    $multiImagePara = [-150, 75, 0, 0, 4.9]
    call multiImage(1) from _call_multiImage_34
    voice "audio/voice/E1/YUK/01/KO/KO003.ogg"
    komachi "Ah, Komachi has to study for her exams so I'll refrain... Don't worry about Komachi, and have fun the three of you!"
    call finishmultiImage from _call_finishmultiImage_35
    show komachi coat mid_left vhappy at right:
        xoffset -150 yoffset 75
    show yui mid_right happy with dissolve:
        xoffset -110 yoffset 75
    voice "audio/voice/E1/YUK/01/YI/YI009.ogg"
    yui "Ah, I see... That's a shame... Komachi-chan, let's have a party after your exams!"
    voice "audio/voice/E1/YUK/01/YK/YK063.ogg"
    yukino "That's right. Now is an important time. Komachi-san, do your best."
    voice "audio/voice/E1/YUK/01/KO/KO004.ogg"
    komachi "Roger! Yukino-san, Yui-san, thank you very much!"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    scene black with Fade(1.0, 0.5, 0)
    play footsteps "audio/sfx/SE00/SE00_18L.ogg" loop
    scene skyA
    with Fade(1.0, 2.0, 1.0)
    $renpy.pause(delay=1.5, hard=True)
    scene sidewalkA
    with dissolve
    window auto show dissolve
    hachiman "(Yukinoshita's expression had been rather gloomy...)"
    play music "audio/bgm/BGM34.ogg"
    show komachi coat mid_center happy at center with dissolve:
        xoffset -75 yoffset 75
    stop footsteps fadeout 2
    voice "audio/voice/E1/YUK/01/KO/KO005.ogg"
    komachi "Onii-chan, hanging out the day after might just be perfect."
    voice "audio/voice/E1/YUK/01/HA/HA051.ogg"
    hachiman "Huh? Why?"
    show komachi vhappy
    voice "audio/voice/E1/YUK/01/KO/KO006.ogg"
    komachi "It's Yukino-san's birthday that day!"
    voice "audio/voice/E1/YUK/01/HA/HA052.ogg"
    hachiman "Aren't you well informed?"
    show komachi happy
    voice "audio/voice/E1/YUK/01/KO/KO007.ogg"
    komachi "This part of me is high in Komachi points, right?"
    voice "audio/voice/E1/YUK/01/HA/HA053.ogg"
    hachiman "That's true. No actually it's cunning, but as expected of you..."
    hachiman "(Birthday, huh...)"
    window auto hide dissolve
#Fade out and go to someplace at home
    stop music fadeout 1.0
    jump E1_CMM_02

#audio in audio/voice/E1/YUK/02/
label E1_YUK_02:
    scene black with Fade(1.0, 0, 0)
    play ambient "audio/sfx/SE05/SE05_05L.ogg"
    scene stationA with Fade(0, 0.5, 1.0)
#street crowd sfx (has cars and stuff)
    #play sound sfx
    show yui coat mid_center pout at center with dissolve:
        xoffset 35 yoffset 75
    window auto show dissolve
    voice "audio/voice/E1/YUK/02/YI/YI000.ogg"
    yui "Ah... It was packed in there!"
    voice "audio/voice/E1/YUK/02/HA/HA000.ogg"
    hachiman "For real..."
    hachiman "(Hah, God I hate bumping shoulders in a-- Hm? Isn't that...?)" #sounds weird
    window auto hide dissolve
    scene stationA with Dissolve(1.5):
        zoom 2.0 yalign 1.0
    $renpy.pause(delay=1, hard=False)
    show hayama coat far_right happy flat at left:
        xoffset 0 alpha 0 yoffset 70
        parallel:
            linear 0.3 alpha 1
        parallel:
            linear 0.3 xoffset 95
        on hide:
            parallel:
                linear 0.3 alpha 0
            parallel:
                linear 0.3 xoffset 225
    show yukino coat far_center angry flat at left:
        xoffset 200 alpha 0 yoffset 75
        parallel:
            linear 0.3 alpha 1
        parallel:
            linear 0.3 xoffset 340
        on hide:
            parallel:
                linear 0.3 alpha 0
            parallel:
                linear 0.3 xoffset 470
    $renpy.pause(delay=2.5, hard=False)
    show yukino coat far_center frown flat
    show hayama coat far_right relieved flat
    with dissolve
    $renpy.pause(delay=2.0, hard=False)
    #define dissolveright = ComposeTransition(Dissolve(0.35), before=easeoutright)
    hide hayama
    hide yukino
    $renpy.pause(delay=2.0, hard=False)
    window auto show dissolve
    voice "audio/voice/E1/YUK/02/YI/YI001.ogg"
    yui "Hikki? What's wrong?"
    window auto hide dissolve
    scene stationA
    show yui coat mid_center surprised at center:
        xoffset 35 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E1/YUK/02/HA/HA001.ogg"
    hachiman "I thought I just saw Yukinoshita and Hayama over there..."
    hide yui
    $url = ["yui coat mid_left surprised1", "yui coat mid_right happy1"]
    $multiImagePara = [10, 70, -105, 70, 0.48]
    call multiImage(0, False) from _call_multiImage_35
    voice "audio/voice/E1/YUK/02/YI/YI002.ogg"
    yui "You did?! Where?"
    call finishmultiImage from _call_finishmultiImage_36
    show yui coat mid_center pout at center:
        xoffset 35 yoffset 75
    with dissolve
    voice "audio/voice/E1/YUK/02/YI/YI003.ogg"
    yui "I can't see them."
    voice "audio/voice/E1/YUK/02/HA/HA002.ogg"
    hachiman "Well, not in this crowd. It's not like I saw them clearly either. Could've been my imagination."
    show yui happy with dissolve
    voice "audio/voice/E1/YUK/02/YI/YI004.ogg"
    yui "I see. I guess it could have."
    hachiman "(I'm sure I saw them, though...)"
    #fade to load screen with bgm with yui appaering in original
    window auto hide dissolve
    stop ambient fadeout 0.5
    $renpy.pause(delay=0.5, hard=False)
    if shrineMeetFlag == "yukino":
        call loading_screen(1, "32") from _call_loading_screen_35
        jump E1_YUK_03
    call loading_screen(24, "33") from _call_loading_screen_36
    jump E2_CMM_01

#label?
#audio in this scene located in: audo/voice/E1/YUK/03/
#sfx street crowd
label E1_YUK_03:
    scene stationA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM41.ogg"
    play ambient "audio/sfx/SE05/SE05_05L.ogg"
    show yui coat mid_center happy at center with dissolve:
        xoffset 35 yoffset 75
    window auto show dissolve
    voice "audio/voice/E1/YUK/03/YI/YI000.ogg"
    yui "Yukinon will be here now, right?"
    voice "audio/voice/E1/YUK/03/HA/HA000.ogg"
    hachiman "Yep."
    show yui mid_left happy at center with dissolve:
        xoffset 10 yoffset 70
    $renpy.pause(delay=0.3, hard=False)
    show yui vhappy1 with dissolve
    voice "audio/voice/E1/YUK/03/YI/YI001.ogg"
    yui "Ah! Yukinon!"
    $renpy.pause(delay=0.2, hard=False)
    window auto hide dissolve
    hide yui
    with dissolve
    $renpy.pause(delay=0.1, hard=False)
    show yui coat mid_left vhappy at right with dissolve:
        xoffset -270 yoffset 75
    $renpy.pause(delay=0.5, hard=False)
    show yukino coat mid_center pout at left with dissolve:
        xoffset 25 yoffset 75
    window auto show dissolve
    voice "audio/voice/E1/YUK/03/HA/HA001.ogg"
    hachiman "Yo."
    show yukino happy with dissolve
    voice "audio/voice/E1/YUK/03/YK/YK000.ogg"
    yukino "I'm sorry. Did I make you wait?"
    show yui happy with dissolve
    voice "audio/voice/E1/YUK/03/YI/YI002.ogg"
    yui "Nope! Not at all!"
    "Yukinoshita arrived at our meeting place, but she looked worn out. I wanted to ask what was wrong, but I wondered if she wouldn't want to go there. I could only hesitate when I thought that."
    show yui vhappy with dissolve
    voice "audio/voice/E1/YUK/03/YI/YI003.ogg"
    yui "Wow, it's cold today too! The New Years holidays were lively and I heard the common cold was spreading too! Are you okay, Yukinon? You're not exhausted?"
    hachiman "(Being considerate is very much like Yuigahama.)"
    show yukino vhappy with dissolve
    voice "audio/voice/E1/YUK/03/YK/YK001.ogg"
    yukino "Yes, just a little but. But it's nothing big. I haven't caught a cold either."
    show yui happy with dissolve
    voice "audio/voice/E1/YUK/03/YI/YI004.ogg"
    yui "I see. Then that's a relief."
    show yui vhappy with dissolve
    voice "audio/voice/E1/YUK/03/YI/YI005.ogg"
    yui "Th-then let's go inside the shop first!"
    window auto hide dissolve
    stop voice fadeout 1.0
    stop ambient fadeout 1.0
    scene cafeA with Fade(1.0, 0.5, 1.0)
    $renpy.pause(delay=1.0, hard=False)
    show yui home mid_left happy at right:
        xoffset -270 yoffset 75
    show yukino home mid_center vhappy at left:
        xoffset 25 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E1/YUK/03/YK/YK002.ogg"
    yukino "What a wonderful shop. It puts you at ease."
    show yui vhappy with dissolve
    voice "audio/voice/E1/YUK/03/YI/YI006.ogg"
    yui "It was me who found it!"
    voice "audio/voice/E1/YUK/03/YK/YK003.ogg"
    yukino "Of course. I can't imagine Hikigaya-kun finding it."
    voice "audio/voice/E1/YUK/03/HA/HA002.ogg"
    hachiman "Well, yeah."
    voice "audio/voice/E1/YUK/03/YI/YI007.ogg"
    yui "I wanted to come here with you, Yukinon! And then...!"
    show yui mid_center happy at right with dissolve:
        xoffset -300 yoffset 75
    stop music fadeout 0.5
    voice "audio/voice/E1/YUK/03/YI/YI008.ogg"
    yui "Okay, Hikki!"
    voice "audio/voice/E1/YUK/03/HA/HA003.ogg"
    hachiman "Y-Yeah..."
    show yukino stare with dissolve
    voice "audio/voice/E1/YUK/03/YK/YK004.ogg"
    yukino "...?"
    show yui mid_left vhappy at right with dissolve:
        xoffset -270 yoffset 75
    play music "audio/bgm/BGM10.ogg"
    voice "audio/voice/E1/YUK/03/YI/YI009.ogg"
    yui "Yukinon happy birthday! This is your present!"
    voice "audio/voice/E1/YUK/03/HA/HA004.ogg"
    hachiman "C-congrats. If this isn't a nuisance either..."
    show yukino surprised
    voice "audio/voice/E1/YUK/03/YK/YK005.ogg"
    yukino "............"
    show yui sad with dissolve
    voice "audio/voice/E1/YUK/03/YI/YI010.ogg"
    yui "Is this a bother? H-Hikki and I wanted to surprise you so we picked it together..."
    show yukino vhappy with dissolve
    voice "audio/voice/E1/YUK/03/YK/YK006.ogg"
    yukino "No... I was just a bit surprised..."
    voice "audio/voice/E1/YUK/03/YK/YK007.ogg"
    yukino "Thank you. I've never been able to celebrate like this before... so I'm very happy."
    show yui happy with dissolve
    menu yukino_present:
        "Saying that, Yukinoshita preciously held the two present wrappings closely. Seeing that, I remembered her expression from when she had appeared at our meeting place yesterday."
        with dissolve
        "You look tired.":
            #voice files from E1/YUK/04 except first two. Possibly some logic evaluated to determine route.
            voice "audio/voice/E1/YUK/03/HA/HA005.ogg"
            hachiman "You look tired."
            show yukino pout with dissolve
            voice "audio/voice/E1/YUK/03/YK/YK008.ogg"
            yukino "............"
            jump E1_YUK_04
#end of scene?
        "Was it tiring?":
            voice "audio/voice/E1/YUK/03/HA/HA006.ogg"
            hachiman "Was yesterday tiring?"
            "not finished"
            jump yukino_present
            #voice files in YUK/05/ probably

label E1_YUK_04:
    show yui surprised with dissolve
    voice "audio/voice/E1/YUK/04/YI/YI000.ogg"
    yui "Yukinon?"
    show yukino vhappy with dissolve
    voice "audio/voice/E1/YUK/04/YK/YK000.ogg"
    yukino "I suppose..."
    window auto hide dissolve
    scene black with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "Yukinoshita talked about what happened yesterday and how she'd been forced to attend the Yukinoshita household's fancy New Years party she didn't want to show her face in."
    "And thus why she had been with Hayama, whose family her parents were very close to."
    hachiman "(Then what I saw yesterday wasn't my imagination.)"
    window auto hide dissolve
    scene cafeA
    show yui home mid_left happy at right:
        xoffset -270 yoffset 70
    show yukino home mid_center angry at left:
        xoffset 25 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E1/YUK/04/YI/YI001.ogg"
    yui "Hey, your family's New Years party sounds like it's really extravagant!"
    voice "audio/voice/E1/YUK/04/YK/YK001.ogg"
    yukino "I suppose... It may be extravagant. But..."
    show yui surprised with dissolve
    voice "audio/voice/E1/YUK/04/YI/YI002.ogg"
    yui "But...?"
    show yukino pout with dissolve
    voice "audio/voice/E1/YUK/04/YK/YK002.ogg"
    yukino "It's like being a prisoner under constant watch. Also other than relatives, it's mostly people related to my parents' work too... That's why I'm just being judged whether I'm a worthy existence as my "
    voice sustain
    yukino "parents' daughter."
    show yui sad with dissolve
    voice "audio/voice/E1/YUK/04/YI/YI003.ogg"
    yui "............"
    voice "audio/voice/E1/YUK/04/HA/HA000.ogg"
    hachiman "That... seems hard."
    show yui angry with dissolve
    voice "audio/voice/E1/YUK/04/YI/YI004.ogg"
    yui "R-right...!"
    voice "audio/voice/E1/YUK/04/HA/HA001.ogg"
    hachiman "Yeah. That kind of thing doesn't happen for me even if our relatives gather. Rather, my relatives respect me and call me the computer master."
    show yui mid_center pout at right:
        xoffset -300 yoffset 75
    show yukino vhappy
    with dissolve
    voice "audio/voice/E1/YUK/04/YK/YK003.ogg"
    yukino "I wonder if they're actually respecting you."
    stop music fadeout 0.5
    jump E1_YUK_06

label E1_YUK_06:
    #voice files in E1/YUK/06/. Perhaps this is where the options join up.
    show yui mid_left happy at right with dissolve:
        xoffset -270 yoffset 75
    voice "audio/voice/E1/YUK/06/YI/YI000.ogg"
    yui "Hey, Yukinon! Open your presents!"
    show yukino surprised with dissolve
    voice "audio/voice/E1/YUK/06/YK/YK000.ogg"
    yukino "Can I?"
    show yui vhappy with dissolve
    voice "audio/voice/E1/YUK/06/YI/YI001.ogg"
    yui "Of course! Right, Hikki?"
    voice "audio/voice/E1/YUK/06/HA/HA000.ogg"
    hachiman "Y-Yeah."
    hachiman "(Someone opening something you gave them right in front of you is super embarassing though to be honest...)"
    show yukino angry with dissolve
    voice "audio/voice/E1/YUK/06/YK/YK001.ogg"
    yukino "Then..."
    window auto hide dissolve
    show yui happy with dissolve
    play sound "audio/sfx/SE01/SE01_09.ogg"
    $renpy.pause(delay=2.0, hard=False)
    window auto show dissolve
    show yukino surprised with dissolve
    voice "audio/voice/E1/YUK/06/YK/YK002.ogg"
    yukino "...!"
    play music "audio/bgm/BGM11.ogg"
    "Cat mittens and room-socks from Yuigahama, and the blue-light filtering glasses I had obviously chosen. It'd be scary if something else came from my wrappings..."
    show yui vhappy with dissolve
    voice "audio/voice/E1/YUK/06/YI/YI002.ogg"
    yui "What do you think? This one is from me, and this one is..."
    hachiman "(I can't stay here anymore! I wanna get away from here! Nah, that'd be embarassing!)"
    hachiman "(I-if you don't like it you can be honest, Yukinoshita! It's the first time in my life I bought a present for a girl after all!)"
    show yukino blush with dissolve
    voice "audio/voice/E1/YUK/06/YK/YK003.ogg"
    yukino "............"
    hide yukino with dissolve
    "After preciously stroking over the cat goods, Yukinoshita gently put the glasses on."
    show yukino home_glasses mid_center blush at left with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E1/YUK/06/YK/YK004.ogg"
    yukino "H-How is it...?"
    hide yui
    $url = ["yui home mid_left vhappy", "yui home mid_center vhappy"]
    $multiImagePara = [-270, 75, -300, 75, 3.5]
    call multiImage(1, False) from _call_multiImage_36
    voice "audio/voice/E1/YUK/06/YI/YI003.ogg"
    yui "It looks great on you, Yukinon! Right, Hikki!?"
    call finishmultiImage from _call_finishmultiImage_37
    show yui home mid_center vhappy at right with None:
        xoffset -300 yoffset 75
    menu yukino_glasses:
        with dissolve
        "It suits you":
            "not finished"
            voice "audio/voice/E1/YUK/06/HA/HA000.ogg"
            hachiman ""
            jump yukino_glasses
        "...":
            "not finished"
            jump yukino_glasses
        "...Yeah": #
            voice "audio/voice/E1/YUK/06/HA/HA006.ogg"
            hachiman "...Yeah."
            "The glasses I gave definitely suited Yukinoshita. I was actually so surprised at how much they suited her I could only say that one word."
            show yukino avoid with dissolve
            voice "audio/voice/E1/YUK/06/YK/YK011.ogg"
            yukino "I-I see..."
            hachiman "(T-the awkward silence has come!?)"
            show yui mid_left happy at right with dissolve:
                xoffset -270 yoffset 70
            voice "audio/voice/E1/YUK/06/YI/YI005.ogg"
            yui "Yeah! It's exactly that! So cute! Super cute!"
            show yukino blush with dissolve
            voice "audio/voice/E1/YUK/06/YK/YK012.ogg"
            yukino "Y-you don't have to say it that much..."
            show yui vhappy with dissolve
            voice "audio/voice/E1/YUK/06/YI/YI006.ogg"
            yui "Ehehe!"
            show yukino vhappy with dissolve
            voice "audio/voice/E1/YUK/06/YK/YK013.ogg"
            yukino "Thank you. I'm very happy. These are better than anything I've received before..."
            show yui blush with dissolve
            voice "audio/voice/E1/YUK/06/YI/YI007.ogg"
            yui "No way! You're exaggerating!"
            voice "audio/voice/E1/YUK/06/YK/YK014.ogg"
            yukino "Not at all. It's because this is the first time I've celebrated with friends like this before."
            show yukino blush with dissolve
            voice "audio/voice/E1/YUK/06/YK/YK015.ogg"
            yukino "That's why... I'm very.. happy."
            show yui happy with dissolve
            voice "audio/voice/E1/YUK/06/YI/YI008.ogg"
            yui "Yukinon..."
            hide yukino
            hide yui
            with dissolve
            "This time, the smile she had while wearing the mittens and poking fun at Yuigahama, who had given them to her, appeared shy and very fragile."
            window auto hide dissolve
            stop music fadeout 0.5
            call loading_screen(18, "33") from _call_loading_screen
            jump E2_CMM_01
