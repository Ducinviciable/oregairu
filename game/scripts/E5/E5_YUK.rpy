label E5_YUK_01:
    scene lodgeoutA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM32.ogg"
    voice "audio/voice/E5/YUK/01/HA/HA000.ogg"
    hachiman "Snow-shoveling, huh..."
    show yukino coat mid_center angry at center with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E5/YUK/01/YK/YK000.ogg"
    yukino "Let's just think we had bad luck and get it over with."
    voice "audio/voice/E5/YUK/01/HA/HA001.ogg"
    hachiman "Right. Well, let's moderately get it done."
    window auto hide dissolve
    hide yukino with dissolve
    #snow shoveling sfx here: it lasts a long time.
    play ambient "audio/sfx/SE01/SE01_37L.ogg"
    $renpy.pause(delay=2.0,hard=True)
    window auto show dissolve
    "As I spoke, I began shoveling the snow. Even though we knew in advance we'd be clearing the snow, it didn't change the fact it was hard work."
    show yukino coat mid_left pout at center with dissolve:
        xoffset 50 yoffset 80
    voice "audio/voice/E5/YUK/01/YK/YK001.ogg"
    yukino "This is more difficult than I thought..."
    voice "audio/voice/E5/YUK/01/HA/HA002.ogg"
    hachiman "Quite different to the local snow, huh..."
    hide yukino with dissolve
    hachiman "(Well, let's stop complaining and get working...)"
    stop ambient
    hachiman "(Anyway...)"
    window auto hide dissolve
    stop music fadeout 0.5
    call card_loading from _card_loading_lodge
    scene lodgeoutA
    show yukino coat mid_left pout at center:
        xoffset 50 yoffset 80
    with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM31.ogg"
    $card_queue = ["About \nskiiing", "About \nthe camp", "About the \nService \nClub", "About \nthe snow", "About \nher \nname", "End \nconversation"]
    $shovel_card_count = 0
    $shovel_ellipses = 0
    jump shovel_card_set
    jump shovel_cards_set1
    #Card minigame here. Card load screen in original. Rmember to hide menu during choices I guess.
    #From the script.
    #Again not sure order of choices appearing.
    #"..."
    #"スキーについて"      #About skiiing
    #"合宿について"       #About the lodge (camp)
    #"奉仕部について"      #About the Service CLub
    #"雪について"        #About the snow
    #"名前について"       #About Her name
    #"会話を切り上げる"     #Cut short the current chat

label not_done_shovel:
    "not done"
    $shovel_card_count -= 1
    jump shovel_card_set

label shovel_card_set:
    if shovel_card_count < 5:
        $shovel_card_count += 1
        $renpy.pause(delay=0.5, hard=True)
        $ch2 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch2)
        $ch3 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch3)
        window auto hide dissolve
        call screen three_minigame("...", ch2, ch3) with dissolve
        if _return == 1:
            $card_queue.append(ch2)
            $card_queue.append(ch3)
            jump not_done_shovel
        elif _return == 2:
            $card_queue.append(ch3)
            if ch2 == "About \nskiiing":
                jump skiing_card
            elif ch2 == "About \nthe camp":
                jump camp_card
            elif ch2 == "About the \nService \nClub":
                jump service_club_card
            elif ch2 == "About \nthe snow":
                jump snow_card
            elif ch2 == "About \nher \nname":
                jump name_card
            else:
                $card_queue.append(ch2)
                jump not_done_shovel
        elif _return == 3:
            $card_queue.append(ch2)
            if ch3 == "About \nskiiing":
                jump skiing_card
            elif ch3 == "About \nthe camp":
                jump camp_card
            elif ch3 == "About the \nService \nClub":
                jump service_club_card
            elif ch3 == "About \nthe snow":
                jump snow_card
            elif ch3 == "About \nher \nname":
                jump name_card
            else:
                $card_queue.append(ch3)
                jump not_done_shovel
    else:
        jump shovel_exit

label shovel_ellipses_card1:
    "not complete."
    if shovel_card_count == 1:
        jump shovel_cards_set1
    elif shovel_card_count == 2:
        jump shovel_cards_set2
    elif shovel_card_count == 3:
        jump shovel_cards_set3
    elif shovel_card_count == 4:
        jump shovel_cards_set4
    elif shovel_card_count == 5:
        jump shovel_cards_set5
    voice "audio/voice/E5/YUK/01/YK/YK002.ogg"
    yukino "⋯⋯⋯⋯"
    voice "audio/voice/E5/YUK/01/YK/YK003.ogg"
    yukino "その⋯⋯なかなか大変ね"
    voice "audio/voice/E5/YUK/01/HA/HA003.ogg"
    hachiman "運、悪かったよな⋯⋯"
    voice "audio/voice/E5/YUK/01/YK/YK004.ogg"
    yukino "⋯⋯そうね"
    voice "audio/voice/E5/YUK/01/YK/YK005.ogg"
    yukino "⋯⋯⋯⋯"
    voice "audio/voice/E5/YUK/01/HA/HA004.ogg"
    hachiman "⋯⋯⋯⋯"
    voice "audio/voice/E5/YUK/01/YK/YK006.ogg"
    yukino "⋯⋯結構、頑張るのね"
    voice "audio/voice/E5/YUK/01/HA/HA005.ogg"
    hachiman "まあそれなりには⋯⋯"
    voice "audio/voice/E5/YUK/01/YK/YK007.ogg"
    yukino "ふふ⋯⋯"
    voice "audio/voice/E5/YUK/01/YK/YK008.ogg"
    yukino "⋯⋯⋯⋯"
    voice "audio/voice/E5/YUK/01/HA/HA006.ogg"
    hachiman "⋯⋯⋯⋯"
    voice "audio/voice/E5/YUK/01/HA/HA007.ogg"
    hachiman "そんなに必死にやらなくても大丈夫だと思うぞ"
    voice "audio/voice/E5/YUK/01/YK/YK009.ogg"
    yukino "いえ⋯⋯割り振られた仕事だもの⋯⋯"
    hachiman "(いや、そのペースだと雪ノ下が絶対へばりそうだって思って言ったんだが⋯⋯)"
    voice "audio/voice/E5/YUK/01/YK/YK010.ogg"
    yukino "⋯⋯⋯⋯"
    voice "audio/voice/E5/YUK/01/HA/HA008.ogg"
    hachiman "⋯⋯ふう"
    voice "audio/voice/E5/YUK/01/YK/YK011.ogg"
    yukino "⋯⋯あら。もう体力切れ？"
    voice "audio/voice/E5/YUK/01/HA/HA009.ogg"
    hachiman "お前こそ、無理しないほうがいいぞ。意外と重労働だからな"
    voice "audio/voice/E5/YUK/01/YK/YK012.ogg"
    yukino "え⋯⋯ええ"
    voice "audio/voice/E5/YUK/01/YK/YK013.ogg"
    yukino "⋯⋯その"
    voice "audio/voice/E5/YUK/01/HA/HA010.ogg"
    hachiman "⋯⋯何だ？"
    voice "audio/voice/E5/YUK/01/YK/YK014.ogg"
    yukino "雪って⋯⋯意外に重いのね⋯⋯"
    voice "audio/voice/E5/YUK/01/HA/HA011.ogg"
    hachiman "毎年、雪下ろしで事故が起きるのが実感できるよな⋯⋯"
    voice "audio/voice/E5/YUK/01/YK/YK015.ogg"
    yukino "全く、いつもながら何故そう後ろ向きな連想をするのかしら"
    voice "audio/voice/E5/YUK/01/HA/HA012.ogg"
    hachiman "元々後ろ向きだから仕方ない"
    voice "audio/voice/E5/YUK/01/YK/YK016.ogg"
    yukino "そうね"
    voice "audio/voice/E5/YUK/01/HA/HA013.ogg"
    hachiman "そこはフォロー無しか"
    voice "audio/voice/E5/YUK/01/YK/YK017.ogg"
    yukino "もう慣れたわ"
    voice "audio/voice/E5/YUK/01/HA/HA014.ogg"
    hachiman "そ、そうか"
    hachiman "(そんないい笑顔で言われると返す言葉が無いんだが⋯⋯)"

label skiing_card:
    window auto show dissolve
    voice "audio/voice/E5/YUK/01/HA/HA015.ogg"
    hachiman "Yukinoshita, have you skied before?" #skii
    hachiman "(Well, it'd usually be rare for someone not to have done it at least once...)"
    show yukino coat mid_center happy with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E5/YUK/01/YK/YK018.ogg"
    yukino "We went as a family every year when I was younger."
    voice "audio/voice/E5/YUK/01/HA/HA016.ogg"
    hachiman "Hoh, as a family. That means..."
    voice "audio/voice/E5/YUK/01/YK/YK019.ogg"
    yukino "Yes. They aren't fond memories."
    voice "audio/voice/E5/YUK/01/HA/HA017.ogg"
    hachiman "Yeah. I can imagine."
    voice "audio/voice/E5/YUK/01/YK/YK020.ogg"
    show yukino coat mid_left angry with dissolve:
        xoffset 50 yoffset 80
    yukino "Yes."
    show yukino unimpressed with dissolve:
        0.25
        linear 0.25 yoffset 100
        0.1
        linear 0.25 yoffset 75
    show yukino mid_left angry with dissolve:
        xoffset 50 yoffset 80
    jump shovel_card_set
#end

label camp_card:
    window auto show dissolve
    voice "audio/voice/E5/YUK/01/HA/HA018.ogg"
    hachiman "We haven't been on a camp since summer last year"
    show yukino coat mid_center sly with dissolve: #going to use center since it has sly
        xoffset -105 yoffset 75
    voice "audio/voice/E5/YUK/01/YK/YK021.ogg"
    yukino "That was quite terrible. No, it might be even worse this time"
    "The difference this time from then is we've come with the Student Council, and that person."
    voice "audio/voice/E5/YUK/01/HA/HA019.ogg"
    hachiman "Thinking about it only gives me a bad feeling now..."
    show yukino unimpressed with dissolve:
        parallel:
            0.25
            linear 0.25 yoffset 100
            0.1
            linear 0.25 yoffset 75 #nod here
    image yukinoFlat = Flatten("yukino coat mid_center angry")
    show yukinoFlat at center:
        xoffset -105 yoffset 75 alpha 0
        parallel:
            1.1
            linear 0.5 alpha 1.0
    voice "audio/voice/E5/YUK/01/YK/YK022.ogg"
    yukino "Indeed. I hope something like what happened that summer doesn't happen again at least."
    hide yukino
    hide yukinoFlat
    show yukino coat mid_center angry at center:
        xoffset -105 yoffset 75
    voice "audio/voice/E5/YUK/01/HA/HA020.ogg"
    hachiman "Relax. I've at least learned that way of doing things isn't good."
    show yukino vhappy with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK023.ogg"
    yukino "I hope so."
    show yukino coat mid_right unimpressed with dissolve: #Brief Nod once in original
        xoffset 25 yoffset 75
        0.25
        linear 0.25 yoffset 85
        0.1
        linear 0.25 yoffset 75
    show yukino pout with dissolve
    "Yukinoshita smiled for a moment, but then her expression turned cloudy and she let out a small sigh."
    show yukino unimpressed with dissolve:
        0.25
        linear 0.25 yoffset 100
        0.1
        linear 0.25 yoffset 75 #Lengthy Nod in original.
    show yukino pout with dissolve
    voice "audio/voice/E5/YUK/01/HA/HA021.ogg"
    hachiman "Well, it'd be nice if the camp ends without problem..."
    show yukino unimpressed with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK024.ogg"
    yukino "I sure hope so..."
    show yukino sad with dissolve
    jump shovel_card_set

label service_club_card:
    window auto show dissolve
    voice "audio/voice/E5/YUK/01/HA/HA022.ogg"
    hachiman "\"The Service Club is forced to participate\", huh. It's as unreasonable as ever."
    show yukino coat mid_left happy with dissolve:
        xoffset 50 yoffset 80
    voice "audio/voice/E5/YUK/01/YK/YK025.ogg" #head tilt in middle of voice in original
    yukino "I'd like to say it can't be helped, but this time, I don't quite see what the request is."
    voice "audio/voice/E5/YUK/01/HA/HA023.ogg"
    hachiman "The ones who didn't want to go on camp in the first place was just me and you, right?"
    show yukino unimpressed with dissolve: #nod in original
        0.25
        linear 0.25 yoffset 100
        0.1
        linear 0.25 yoffset 75
    show yukino pout with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK026.ogg"
    yukino ".. Right."
    voice "audio/voice/E5/YUK/01/HA/HA024.ogg"
    hachiman "By making us go by calling it forced participation... For whose enjoyment?"
    show yukino happy with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK027.ogg"
    yukino "I don't think you'll come to a good answer even if you pursued that question."
    voice "audio/voice/E5/YUK/01/HA/HA025.ogg"
    hachiman "Agreed."
    show yukino pout with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK028.ogg"
    yukino "But there is someone. Yuigahama-san wished to participate as the Service Club."
    voice "audio/voice/E5/YUK/01/HA/HA026.ogg"
    hachiman "That sounds like her."
    show yukino unimpressed with dissolve: #nod
    show yukino:
        parallel:
            0.25
            linear 0.25 yoffset 100
            0.1
            linear 0.25 yoffset 75
        parallel:
            1.1
            linear 0.5 alpha 0
    image yukinoFlat = Flatten("yukino coat mid_center happy")
    show yukinoFlat at center:
        xoffset -105 yoffset 75 alpha 0
        parallel:
            1.1
            linear 0.5 alpha 1.0
    voice "audio/voice/E5/YUK/01/YK/YK029.ogg"
    yukino "Yes. That's why, if she can enjoy herself as the Service Club, then I think it's fine."
    hide yukino
    hide yukinoFlat
    show yukino coat mid_center happy at center:
        xoffset -105 yoffset 75
    jump shovel_card_set
#end

label snow_card:
    window auto show dissolve
    voice "audio/voice/E5/YUK/01/HA/HA027.ogg"
    hachiman "You don't see this much snow in Chiba."
    show yukino mid_right vhappy with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E5/YUK/01/YK/YK030.ogg"#Head tilt in original
    yukino "Oh, Chiba is quite broad though?"
    voice "audio/voice/E5/YUK/01/HA/HA028.ogg"
    hachiman "Well, that's true."
    "Thinking back, I'd announced my love for Chiba, but I hadn't exactly travelled around the place.
        The sadness of a high school student without reliable transport."
    "... But, at the very least there wasn't a ski resort."
    voice "audio/voice/E5/YUK/01/YK/YK031.ogg"
    yukino "But... it's true it doesn't snow as much as this."
    voice "audio/voice/E5/YUK/01/HA/HA029.ogg"
    hachiman "Right?"
    show yukino unimpressed with dissolve:
    show yukino:
        parallel:
            0.25
            linear 0.25 yoffset 100
            0.1
            linear 0.15 yoffset 85
        parallel:
            0.75
            linear 0.25 alpha 0
    image yukinoFlat = Flatten("yukino coat mid_center vhappy")
    show yukinoFlat at center:
        xoffset -105 yoffset 85 alpha 0
        parallel:
            0.75
            linear 0.25 alpha 1
        parallel:
            0.75
            linear 0.25 yoffset 75
    voice "audio/voice/E5/YUK/01/YK/YK032.ogg" #nod
    yukino "Yes. That's why, even though I don't know how scary snow can be, snowy days make me a little happy. The town looks completely different..."
    hide yukino
    hide yukinoFlat
    show yukino coat mid_center vhappy at center:
        xoffset -105 yoffset 75
    voice "audio/voice/E5/YUK/01/HA/HA030.ogg"
    hachiman "I feel like I understand. By the way, I'm much more happy if school is cancelled on such a day."
    show yukino mid_left vhappy with dissolve:
        xoffset 50 yoffset 80
    voice "audio/voice/E5/YUK/01/YK/YK033.ogg"
    yukino "That's very much like you."
    voice "audio/voice/E5/YUK/01/HA/HA031.ogg"
    hachiman "Pretty much."
    "That being said, I felt the same unexplainable uplifting feeling on morning days the snow fell.
        Did I feel that way because the everyday landscape was dyed white?"
    "There was that, and the roads would change into masses of brown dirt as people went to work or school."
    "She would have known for sure the pointlessness of wondering about the following, but she did so regardless."
    show yukino happy with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK034.ogg"#head tilt
    yukino "I wonder if it will snow this year."
    voice "audio/voice/E5/YUK/01/HA/HA032.ogg"
    hachiman "It probably will at least once."
    show yukino vhappy with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK035.ogg"
    yukino "It would be nice... if we could see it from the clubroom."
    voice "audio/voice/E5/YUK/01/HA/HA033.ogg"
    hachiman "True..."
    "We looked up at the sky at the same time. Even though was shining through the cloudy sky, snow came fluttering down."
    jump shovel_card_set

label name_card:
    window auto show dissolve
    voice "audio/voice/E5/YUK/01/HA/HA034.ogg"
    hachiman "Your name... was chosen because it snowed on the day you were born... right?"
    show yukino mid_right pout with dissolve: #should be blush probably but for the sake of dynamics in the following expressions
        xoffset 25 yoffset 75
    voice "audio/voice/E5/YUK/01/YK/YK036.ogg"
    yukino "Y-yes... That's what I heard... Why are you asking that all of the sudden?"
    voice "audio/voice/E5/YUK/01/HA/HA035.ogg"
    hachiman "Nah, I just remembered we talked about that seeing all the snow here."
    #no avoid attribute for right so I let the above be pout and this be blush
    show yukino blush with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK037.ogg"
    yukino "... You remember some boring things..."
    voice "audio/voice/E5/YUK/01/HA/HA036.ogg"
    hachiman "I have confidence in my memory."
    show yukino coat mid_center avoid with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E5/YUK/01/YK/YK038.ogg"
    yukino "Shouldn't you remember more useful things? There's no point in remembering where my name comes from..."
    voice "audio/voice/E5/YUK/01/HA/HA037.ogg"
    hachiman "Nah... I think it's a good name though."
    show yukino blush with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK039.ogg"
    yukino "I-is that so... What about.. what about in your case?"
    voice "audio/voice/E5/YUK/01/HA/HA038.ogg"
    hachiman "Me?  Me huh?... Sorry, I've never been asked that before. This is the first time."
    show yukino mid_right unimpressed with dissolve:
        xoffset 25 yoffset 75
        0.25
        linear 0.25 yoffset 100
        0.1
        linear 0.25 yoffset 75 #Nod with transition
    show yukino vhappy with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK040.ogg"
    yukino "For me as well, that might've been the first time I was asked about where my name came from."
    voice "audio/voice/E5/YUK/01/HA/HA039.ogg"
    hachiman "Really?"
    voice "audio/voice/E5/YUK/01/YK/YK041.ogg"
    yukino "Yes..."
    jump shovel_card_set

    #alternative exit?
    #not finished integrating these lines
    voice "audio/voice/E5/YUK/01/HA/HA040.ogg"
    hachiman "あー⋯⋯"
    "何か話そうと思ったが、特に話題があるわけでもないことに気付き、口をつぐんだ。"
    hachiman "(雪ノ下だって、無理やりひねり出したような会話なんかに付き合いたくないだろうしな)"
    voice "audio/voice/E5/YUK/01/HA/HA043.ogg"#
    hachiman "これ、足を取られない程度に寄せとけばいいよな"
    voice "audio/voice/E5/YUK/01/YK/YK044.ogg"
    yukino "そうね⋯⋯少なくとも、しばらく邪魔にならなければ問題ないんじゃないかしら"
    voice "audio/voice/E5/YUK/01/HA/HA044.ogg"
    hachiman "だな。無理に頑張って雪かきしなくても、いずれすべて時間が解決してくれる⋯⋯"
    voice "audio/voice/E5/YUK/01/YK/YK045.ogg"
    yukino "そんな言い方をすると、労働をさぼる言い訳も詩的に聞こえるから不思議ね⋯⋯"

#seems to be exit here
label shovel_exit:
    #shovel sfx
    window auto show dissolve
    voice "audio/voice/E5/YUK/01/HA/HA045.ogg"
    hachiman "Doing this... does it have an end?"
    #stop shovel sfx approximately here
    show yukino mid_right angry with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E5/YUK/01/YK/YK046.ogg"
    yukino "Well... Who knows."
    show yukino vhappy with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK047.ogg"
    yukino "But... the air here is quite clear."
    voice "audio/voice/E5/YUK/01/HA/HA046.ogg"
    hachiman "Right. Let's clear it up and call it a day."
    voice "audio/voice/E5/YUK/01/YK/YK048.ogg"
    yukino "That's quite a forward statement, for you at least."
    voice "audio/voice/E5/YUK/01/HA/HA047.ogg"#
    hachiman "Oh... you think so?"
    voice "audio/voice/E5/YUK/01/YK/YK049.ogg"#nod
    yukino "It is."
    show yukino unimpressed:
        parallel:
            linear 0.25 alpha 1
        parallel:
            linear 0.25 yoffset 100
    show yukino vhappy:
        parallel:
            linear 0.25 alpha 1
        parallel:
            linear 0.25 yoffset 75
    stop music fadeout 1
    window auto hide dissolve
    jump post_shovel
#fin

#alternate exit?
label shovel_cut_card:
    voice "audio/voice/E5/YUK/01/HA/HA041.ogg"
    hachiman "⋯⋯雪かきって案外終わらないもんだよな"
    voice "audio/voice/E5/YUK/01/YK/YK042.ogg"
    yukino "まだ、ほとんど踏み荒らされていない状態だものね"
    voice "audio/voice/E5/YUK/01/HA/HA042.ogg"
    hachiman "やっぱりクジ運悪かったよな⋯⋯"
    voice "audio/voice/E5/YUK/01/YK/YK043.ogg"#
    yukino "そうね⋯⋯"
    "unfinished"
    jump post_shovel

#post 3card
label post_shovel:
    scene lodgeoutA
    show yukino coat mid_left angry at center:
        xoffset 50 yoffset 80
    with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM11.ogg"
    $renpy.pause(delay=1,hard=True)
    play ambient "audio/sfx/SE01/SE01_37L.ogg"
    show yukino pout with dissolve
    window auto show dissolve
    voice "audio/voice/E5/YUK/01/YK/YK050.ogg"#
    yukino "............"
    voice "audio/voice/E5/YUK/01/HA/HA048.ogg"
    hachiman "It's best if you don't push yourself too much."
    show yukino angry with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK051.ogg"
    yukino "That won't do... or so I'd like to say..."
    show yukino sad with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK052.ogg"
    yukino "I am quite exhausted..."
    voice "audio/voice/E5/YUK/01/HA/HA049.ogg"
    hachiman "You didn't have much stamina in the first place."
    show yukino pout with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK053.ogg"
    yukino "Says you... Even though you complain a lot, you work quite well."
    voice "audio/voice/E5/YUK/01/HA/HA050.ogg"
    hachiman "Whatever, just take a break."
    show yukino vhappy with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK054.ogg"
    yukino "That's unexpected of you. Or not, maybe it isn't."
    voice "audio/voice/E5/YUK/01/HA/HA051.ogg"
    hachiman "What isn't?"
    voice "audio/voice/E5/YUK/01/YK/YK055.ogg"
    yukino "Looking at you now, you might become quite a good househusband."
    "Through a gap in the clouds, a clear light shone at the girl who was smiling as she spoke so carefreely. Feeling like I hadn't seen that carefree smile in such a long time, I'd been staring at her without "
    "realising it."
    voice "audio/voice/E5/YUK/01/HA/HA052.ogg"
    hachiman "R-really?"
    stop ambient
    #stop sound effects finally
    show yukino blush with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK056.ogg"
    yukino "N-no... um..."
    show yukino vhappy with dissolve
    voice "audio/voice/E5/YUK/01/YK/YK057.ogg"
    yukino "This place is more peaceful than I thought."
    voice "audio/voice/E5/YUK/01/HA/HA053.ogg"
    hachiman "It's probably really noisy at the ski slopes though."
    voice "audio/voice/E5/YUK/01/YK/YK058.ogg"
    yukino "That's true."
    window auto hide dissolve
    stop music fadeout 1.0
    jump E5_G13_01

label E5_YUK_02:
    hachiman "(Well, in for a penny, in for a pound applies here. I want to become good at this...)"
    "So that was the situation as I was left in this snowy world. Maybe it was because I wasn't feeling too bad about it,
        I had been thinking ahead of things"
    voice "audio/voice/E5/YUK/02/HA/HA000.ogg"
    hachiman "Or so I say..."
    window auto hide dissolve
    play ambient "audio/sfx/SE01/SE01_44L.ogg"
    $renpy.pause(delay=2, hard=True)
    scene slopesA with dissolve:
        zoom 2.0 xoffset -300 yoffset -225
    window auto show dissolve
    hachiman "(Woah. that person is unbelievably good. Even though I was just an amateur, I could tell.)"
    hachiman "(Must be fun to ski that well... Huh?)"
    window auto hide dissolve
    scene slopesA with dissolve:
        zoom 1.75 xoffset -300 yoffset -375
    window auto show dissolve
    hachiman "(They look like they're coming this way!)"
    window auto hide dissolve
    #okay this was a ridiculous zoom. Could probably be improved more, and fix the lightning
    scene slopesA with dissolve:
        yoffset -2350 zoom 3.2 xcenter 0.23
    #stop loop sfx
    $renpy.pause(delay=1, hard=True)
    stop ambient
    play sound "audio/sfx/SE01/SE01_47.ogg"
    #single slide sfx
    stop music fadeout 0.5
    show yukino heavy_coat near_right pout at center with dissolve:
        zoom 2.0 yoffset 90 xoffset -600
        easein 0.7 xoffset -135
    $renpy.pause(delay=1.0, hard=True)
    show yukino heavy_coat near_center happy at center with dissolve:
        zoom 2.0 yoffset 165  xoffset -385
    window auto show dissolve
    voice "audio/voice/E5/YUK/02/YK/YK000.ogg"
    yukino "... Hikigaya-kun. You aren't going to ski?"
    window auto hide dissolve
    scene slopesA
    show yukino heavy_coat mid_center happy at center:
        xoffset -105 yoffset 75
    with dissolve
    play music "audio/bgm/BGM11.ogg"
    window auto show dissolve
    hachiman "(I hadn't realised it was Yukinoshita Yukino since her goggles had been hiding her face...)"
    voice "audio/voice/E5/YUK/02/HA/HA001.ogg"
    hachiman "You look like a pro at skiing..."
    show yukino avoid with dissolve
    voice "audio/voice/E5/YUK/02/YK/YK001.ogg"
    yukino "I only learned a little... you're exaggerating too much with \"pro\"."
    voice "audio/voice/E5/YUK/02/HA/HA002.ogg"
    hachiman "No, even I can see you're good at it. It was just a moment, but I was wondering what it must be like to be able to ski like that."
    show yukino blush with dissolve
    voice "audio/voice/E5/YUK/02/YK/YK002.ogg"
    yukino "I see..."
    show yukino vhappy with dissolve
    voice "audio/voice/E5/YUK/02/YK/YK003.ogg"
    yukino "But, how were you intending to ski without even securing your equipment?"
    voice "audio/voice/E5/YUK/02/HA/HA003.ogg"
    hachiman "... I don't know how to."
    show yukino surprised with dissolve
    voice "audio/voice/E5/YUK/02/YK/YK004.ogg"
    yukino "... Eh?"
    voice "audio/voice/E5/YUK/02/HA/HA004.ogg"
    hachiman "No, cause I've never done it before."
    show yukino blush with dissolve
    voice "audio/voice/E5/YUK/02/YK/YK005.ogg"
    yukino "Oh... If you're okay with it, should I teach you the basics?"
    voice "audio/voice/E5/YUK/02/HA/HA005.ogg"
    hachiman "Is that okay?"
    show yukino avoid with dissolve
    voice "audio/voice/E5/YUK/02/YK/YK006.ogg"
    yukino "Y-yes... Just making snowmans after coming all this way seems like a waste. Above all else, you'd be a nuisance to everyone else."
    voice "audio/voice/E5/YUK/02/HA/HA006.ogg"
    hachiman "Oh is that so... Well, if that's the case then please. Be nice."
    show yukino happy with dissolve
    voice "audio/voice/E5/YUK/02/YK/YK007.ogg"
    yukino "Yes, let's get started."
    "With my reply, as if a switch had been flicked, Yukinoshita immediately went into instructor mode. She began giving out instructions with a firm expression."
    voice "audio/voice/E5/YUK/02/YK/YK008.ogg"
    yukino "You need to secure your equipment first. Pull up the bindings at the back and remove the snow from under your boots."
    voice "audio/voice/E5/YUK/02/HA/HA007.ogg"
    hachiman "B-binding...?"
    voice "audio/voice/E5/YUK/02/YK/YK009.ogg"
    yukino "If there's snow under your boots, there's a chance the skis might come loose."
    voice "audio/voice/E5/YUK/02/YK/YK010.ogg"
    yukino "From there, fit the tips of your boots into the binding, then the heels..."
    voice "audio/voice/E5/YUK/02/HA/HA008.ogg"
    hachiman "Hold on. I don't get what you're talking about if you use all that jargon. What's this about binding? Is it similar to pudding?"
    show yukino vhappy with dissolve
    voice "audio/voice/E5/YUK/02/YK/YK011.ogg"
    yukino "... Not similar, no. I'm talking about the metal fittings on your skis."
    voice "audio/voice/E5/YUK/02/YK/YK012.ogg"
    yukino "Hikigaya-kun, you really haven't skied before, have you?"
    voice "audio/voice/E5/YUK/02/HA/HA009.ogg"
    hachiman "That's what I said."
    show yukino stare with dissolve
    voice "audio/voice/E5/YUK/02/YK/YK013.ogg"
    yukino "Alright. If that isn't getting through to you, then let's do this."
    window auto hide dissolve
    stop voice
    hide yukino with dissolve
    image yukino heavy_coat near_center happy flat = Flatten("yukino heavy_coat near_center happy")
    show yukino heavy_coat near_center happy flat at center with dissolve:
        xoffset -195 yoffset 75
        on hide:
            parallel:
                linear 0.5 alpha 0
            parallel:
                easeout 0.5 yoffset 125
    $renpy.pause(delay=0.5,hard=True)
    hide yukino
    $renpy.pause(delay=1.0,hard=True)
    scene slopesA:
        yoffset -2350 zoom 3.2 xcenter 0.23
    show yukino heavy_coat near_left happy at center:
        zoom 1.5 xoffset 80 yoffset 505
    with dissolve
    $renpy.pause(delay=0.5,hard=True)
    window auto show dissolve
    voice "audio/voice/E5/YUK/02/HA/HA010.ogg"
    hachiman "H-Hey, what are you..."
    "Yukinoshita suddenly came close and crouched down as she placed her hand on my leg."
    show yukino angry with dissolve
    voice "audio/voice/E5/YUK/02/YK/YK014.ogg"
    yukino "Lift this leg and pull up this part here."
    voice "audio/voice/E5/YUK/02/HA/HA011.ogg"
    hachiman "L-like this...?"
    hachiman "(T-too close! Close close close close! ... Too close.)"
    play sound "audio/sfx/SE01/SE01_40.ogg"
    $renpy.pause(delay=0.5,hard=True)
    show yukino vhappy with dissolve
    voice "audio/voice/E5/YUK/02/YK/YK015.ogg"
    yukino "That's it. And then you use this to remove the snow."
    voice "audio/voice/E5/YUK/02/YK/YK016.ogg"
    yukino "After that, fit the tips of your toes into there, and then try fitting it in your heels."
    play sound "audio/sfx/SE01/SE01_40.ogg"
    $renpy.pause(delay=0.5,hard=True)
    voice "audio/voice/E5/YUK/02/HA/HA012.ogg"
    hachiman "Ah, it fit. I see, so that's how it works."
    window auto hide dissolve
    hide yukino with dissolve
    $renpy.pause(delay=0.5,hard=True)
    scene slopesA
    show yukino heavy_coat mid_center happy at center:
        xoffset -105 yoffset 75
    with dissolve
    window auto show dissolve
    "After confirming my leg was satisfyingly secured onto the skis, Yukinoshita stepped back. Along with the feeling of relief that my leg was secured was a slight feeling of loneliness."
    hachiman "(I was wondering how this would turn out, but she's better at teaching than I thought.)"
    show yukino angry with dissolve
    voice "audio/voice/E5/YUK/02/YK/YK017.ogg"
    yukino "That's only the right side. Don't rejoice, try doing the left side yourself."
    hachiman "(... Albeit strict.)"
    window auto hide dissolve
    play sound ["<silence 1.0>", "audio/sfx/SE01/SE01_40.ogg"]
    scene slopesA
    show yukino heavy_coat mid_center happy at center:
        xoffset -105 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E5/YUK/02/YK/YK018.ogg"
    yukino "Looks like you've secured it well. Okay then, let's move on to the basics of skiing. I'll teach you how to Bogen."
    voice "audio/voice/E5/YUK/02/HA/HA013.ogg"
    hachiman "Bogen, huh. I've heard of that before."
    show yukino angry with dissolve
    voice "audio/voice/E5/YUK/02/YK/YK019.ogg"
    yukino "Bogen is a turning movement on skis."
    voice "audio/voice/E5/YUK/02/YK/YK020.ogg"
    yukino "Keep the tips apart by about the width of two fists. Lower your waist so that the centre of gravity is focused on your inner thighs."
    voice "audio/voice/E5/YUK/02/HA/HA014.ogg"
    hachiman "Two fists... Inner thighs... centre of gravity... L-like this?"
    hide yukino with dissolve
    show yukino heavy_coat near_left angry at center with dissolve:
        xoffset 50 yoffset 75
    voice "audio/voice/E5/YUK/02/YK/YK021.ogg"
    yukino "No. Keep your back straight..."
    voice "audio/voice/E5/YUK/02/HA/HA015.ogg"
    hachiman "............"
    "(Yukinoshita approached me and placed her hands on my stomach and back.)"
    "(I could smell a sweet scent mixed in with the cool air around us.)"
    show yukino happy with dissolve
    hachiman "(Y-Yukinoshita-san. You're kind of too close... Like as if we're glued together here!!)"
    "Without noticing my restlessness, Yukinoshita was correcting my posture as she moved my arms and thighs in place."
    hachiman "(This is bad. I'm thinking too much about her hands. Nothing she says is getting into my head!)"
    show yukino angry with dissolve
    voice "audio/voice/E5/YUK/02/YK/YK022.ogg"
    yukino "Lower your waist a little more and your elbows are too stiff. That's it, stay that way."
    voice "audio/voice/E5/YUK/02/HA/HA016.ogg"
    hachiman "O-ok..."
    voice "audio/voice/E5/YUK/02/YK/YK023.ogg"
    yukino "You're sliding speed will increase if you lean forward so try to maintain this posture for now."
    show yukino happy with dissolve
    voice "audio/voice/E5/YUK/02/YK/YK024.ogg"
    yukino "Keep your gaze forward. Don't only focus on your legs."
    voice "audio/voice/E5/YUK/02/HA/HA017.ogg"
    hachiman "Gaze forward..."
    "When I raised my gaze as she told me to, Yukinoshita's face was right in front of me..."
    show yukino surprised with dissolve
    "Her eyes widened with her surprise and her cheeks were turning redder."
    show yukino blush with dissolve
    voice "audio/voice/E5/YUK/02/YK/YK025.ogg"
    yukino "...!"
    voice "audio/voice/E5/YUK/02/HA/HA018.ogg"
    hachiman "...!"
    voice "audio/voice/E5/YUK/02/YK/YK026.ogg"
    yukino "U-um... Okay then, give it a go."
    voice "audio/voice/E5/YUK/02/HA/HA019.ogg"
    hachiman "R-Right..."
    voice "audio/voice/E5/YUK/02/YK/YK027.ogg"
    yukino "Okay... Then, I'll let go."
    voice "audio/voice/E5/YUK/02/HA/HA020.ogg"
    hachiman "A-Alright..."
    stop music fadeout 0.5
    hide yukino with dissolve
    "While turning her gaze away, Yukinoshita withdrew her hands from my body."
    window auto hide dissolve
    scene slopes2A:
        zoom 1.75 xpos -1145 ypos -595
    with dissolve
    $renpy.pause(delay=0.5, hard=True)
    with Shake((0, 0, 0, 0), 0.35, dist=50)
    play sound "audio/sfx/SE01/SE01_41.ogg"
    $renpy.pause(delay=3.5, hard=True)
    stop sound
    window auto show dissolve
    voice "audio/voice/E5/YUK/02/HA/HA021.ogg"
    hachiman "Starting to move..."
    voice "audio/voice/E5/YUK/02/YK/YK028.ogg"
    yukino "Ah... Don't get frightened and lean forward. Maintain your posture like before."
    window auto hide dissolve
    stop voice
    with Shake((0, 0, 0, 0), 0.35, dist=50)
    play ambient "audio/sfx/SE01/SE01_42L.ogg"
    $renpy.pause(delay=2.0, hard=True)
    play music "audio/bgm/BGM45.ogg"
    $renpy.pause(delay=0.25, hard=True)
    show transition_1b at offscreenright:
        parallel:
            easein 0.1 xpos -780
    $renpy.pause(delay=0.15, hard=True)
    scene slopes2A at ski_shake1:
        zoom 1.75 xpos -1145 ypos -595
    show transition_1b at offscreenright:
        xpos -780
        parallel:
            easein 0.15 xpos -3500
    $renpy.pause(delay=0.15, hard=True)
    hide transition_1b
    #begin screenshake... Figure this out later.
    #with Shake((0, 0, 0, 0), 1.0, dist=20)
    window auto show dissolve
    voice "audio/voice/E5/YUK/02/HA/HA022.ogg"
    hachiman "E-Even if you say that... I'm beginning to speed up...!"
    voice "audio/voice/E5/YUK/02/YK/YK029.ogg"
    yukino "Hikigaya-kun, stop for a moment!"
    window auto hide dissolve
    #additional rumbling sfx start
    play sound "<loop 2>audio/sfx/SE01/SE01_43L.ogg" loop
    $renpy.pause(delay=1.5, hard=True)
    show transition_1b at offscreenright:
        parallel:
            easein 0.1 xpos -780
    $renpy.pause(delay=0.15, hard=True)
    hide slopes2A
    scene slopes2A at ski_shake2:
        zoom 1.8 xpos -1375 ypos -605
    show transition_1b at offscreenright:
        xpos -780
        parallel:
            easein 0.15 xpos -3500
    $renpy.pause(delay=0.15, hard=True)
    hide transition_1b
    window auto show dissolve
    voice "audio/voice/E5/YUK/02/HA/HA023.ogg"
    hachiman "... How do you stop?!"
    voice "audio/voice/E5/YUK/02/YK/YK030.ogg"
    yukino "... Ah. I didn't teach you how to stop. But, just stop somehow!"
    voice "audio/voice/E5/YUK/02/HA/HA024.ogg"
    hachiman "That's unreasonable...!"
    window auto hide dissolve
    $renpy.pause(delay=0.5, hard=True)
    show transition_1b at offscreenright:
        parallel:
            easein 0.1 xpos -780
    window auto show dissolve
    hachiman "(Yukinoshita-senseiiiii!)"
    window auto hide dissolve
    #stop all sfx
    stop music fadeout 0.5
    stop sound fadeout 0.5
    stop ambient fadeout 0.5
    jump E5_CMM_03

label E5_YUK_03:
    scene lodgeroomC with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM10.ogg"
    window auto show dissolve
    "As they seemed to be continying the festivities in the living room as usual, I could hear really loud roars of laughter now and then around where Tobe was."
    hachiman "(... Well, while it's early I'll take a bath and come back. Doesn't seem like anybody's there yet after all.)"
    voice "audio/voice/E5/YUK/03/HA/HA000.ogg"
    hachiman "Oh yeah, this place was a hot spring..."
    window auto hide dissolve
    stop voice
    scene black with Fade(1.0, 0, 0)
    play sound "audio/sfx/SE00/SE00_30L.ogg"
    $renpy.pause(delay=0.5, hard=False)
    scene skyC with Fade(0, 0, 1.0)
    stop sound fadeout 1
    window auto show dissolve
    voice "audio/voice/E5/YUK/03/YK/YK000.ogg"
    yukino "Oh. Are you going to take a bath now as well?"
    voice "audio/voice/E5/YUK/03/HA/HA001.ogg"
    hachiman "Y-yeah... What a coincidence."
    voice "audio/voice/E5/YUK/03/YK/YK001.ogg"
    yukino "Right..."
    window auto hide dissolve
    stop music fadeout 1
    scene hotspringBGB with Fade(1.0, 0.5, 1.0)
    play sound "audio/sfx/SE01/SE01_31.ogg"
    $renpy.pause(delay=4.0, hard=True)
    scene hachimanBathc with dissolve
    window auto show dissolve
    voice "audio/voice/E5/YUK/03/HA/HA002.ogg"
    hachiman "Ahhh..."
    hachiman "(I was scared for a moment, but it looks like the mens and womens baths are separate after all.)"
    voice "audio/voice/E5/YUK/03/HA/HA003.ogg"
    hachiman "Ahh, this water is great..."
    voice "audio/voice/E5/YUK/03/YK/YK002.ogg"
    yukino "It really is."
    window auto hide dissolve
    show yukinoBatha with dissolve
    play music "audio/bgm/BGM11.ogg"
    window auto show dissolve
    voice "audio/voice/E5/YUK/03/HA/HA004.ogg"
    hachiman "Nuoah, that scared me! Don't reply when I'm talking to myself. And wait, you can unexpectedly hear from the other side."
    voice "audio/voice/E5/YUK/03/YK/YK003.ogg"
    yukino "It was me who was surprised. You made a weird sound so suddenly I thought someone was talking to me."
    voice "audio/voice/E5/YUK/03/HA/HA005.ogg"
    hachiman "Ah, sorry. It's a habit of mine to talk to myself in the bath."
    voice "audio/voice/E5/YUK/03/YK/YK004.ogg"
    yukino "It's not like I don't understand what you mean. Anyone would relax if they had such a wonderful bath to themselves."
    voice "audio/voice/E5/YUK/03/HA/HA006.ogg"
    hachiman "Right? This water is really good. I feel like all the pain in my muscles is getting stripped away."
    voice "audio/voice/E5/YUK/03/YK/YK005.ogg"
    yukino "I didn't think I was being that strict though... Today was just the very basics. Aren't you a bit unfit?"
    hide yukinoBatha with dissolve
    voice "audio/voice/E5/YUK/03/HA/HA007.ogg"
    hachiman "I exercise by riding a bike to school though."
    "I was absolutely restless when we began talking over the fence, but as we exchanged meaningless words I started to ease up."
    "Yukinoshita probably was the same as her voice sounded peaceful through the steam which made me absent-minded."
    show yukinoBatha with dissolve
    voice "audio/voice/E5/YUK/03/YK/YK006.ogg"
    yukino "In any case, just why did Nee-san come along I wonder."
    voice "audio/voice/E5/YUK/03/HA/HA008.ogg"
    hachiman "Probably to meddle with you. That was the case last time as well."
    voice "audio/voice/E5/YUK/03/YK/YK007.ogg"
    menu yukino_bath_q: #Not sure how this paths.
        yukino "... Nee-san has always been like that. Like she jests too much."
        with dissolve
        "That's easy to imagine":
            "not finished"
            # voice "audio/voice/E5/YUK/03/HA/HA009.ogg"
            # hachiman ""
            # voice "audio/voice/E5/YUK/03/YK/YK008.ogg"
            # yukino ""
            # voice "audio/voice/E5/YUK/03/HA/HA010.ogg"
            # hachiman ""
            # voice "audio/voice/E5/YUK/03/YK/YK009.ogg"
            # yukino ""
            jump yukino_bath_q
            jump E5_YUK_03_cont
        "You too?": #
            window auto hide dissolve
            show hachimanBatha with dissolve:
                zoom 1.7 xoffset -17 yoffset -312
            window auto show dissolve
            voice "audio/voice/E5/YUK/03/HA/HA011.ogg"
            hachiman "Does that mean you too?"
            voice "audio/voice/E5/YUK/03/YK/YK010.ogg"
            yukino "... Eh?"
            voice "audio/voice/E5/YUK/03/HA/HA012.ogg"
            hachiman "No, I was wondering if you were similar to how you are now as a kid." #Fix'd TL I think.
            voice "audio/voice/E5/YUK/03/YK/YK011.ogg"
            yukino "Um... I wonder about that. I don't know about myself that much."
            voice "audio/voice/E5/YUK/03/HA/HA013.ogg"
            hachiman "Right..."
            hide hachimanBatha with dissolve
            voice "audio/voice/E5/YUK/03/YK/YK012.ogg"
            yukino "Yes... But, it was a bit surprising to be asked about when I was small."
            voice "audio/voice/E5/YUK/03/HA/HA014.ogg"
            hachiman "If Yuigahama were here, I'm sure she'd dive right into this topic."
            voice "audio/voice/E5/YUK/03/YK/YK013.ogg"
            yukino "Would she...?"
            voice "audio/voice/E5/YUK/03/HA/HA015.ogg"
            hachiman "She really likes you after all..."
            voice "audio/voice/E5/YUK/03/YK/YK014.ogg"
            yukino "Oh..."
            jump E5_YUK_03_cont
        "Because humans don't really change":
            "not finished"
            # voice "audio/voice/E5/YUK/03/HA/HA016.ogg"
            # hachiman ""
            # voice "audio/voice/E5/YUK/03/YK/YK015.ogg"
            # yukino ""
            # voice "audio/voice/E5/YUK/03/HA/HA017.ogg"
            # hachiman ""
            # voice "audio/voice/E5/YUK/03/YK/YK016.ogg"
            # yukino ""
            jump yukino_bath_q
            jump E5_YUK_03_cont


label E5_YUK_03_cont:
    #common I think.
    hide yukinoBatha with dissolve
    voice "audio/voice/E5/YUK/03/HA/HA018.ogg"
    hachiman "Regardless of how it used to be, well that person just does the usual."
    voice "audio/voice/E5/YUK/03/YK/YK017.ogg"
    yukino "That... is true, but I wish she'd place her target of interest somewhere else already."
    voice "audio/voice/E5/YUK/03/HA/HA019.ogg"
    hachiman "Whatever kind of person she is, you are you."
    voice "audio/voice/E5/YUK/03/YK/YK018.ogg"
    yukino "............"
    stop voice
    show yukinoBathb with dissolve
    voice "audio/voice/E5/YUK/03/YK/YK019.ogg"
    yukino "Right... In any case..."
    voice "audio/voice/E5/YUK/03/YK/YK020.ogg"
    yukino "I never thought I'd be able to relax like this despite having a sister here like that."
    voice "audio/voice/E5/YUK/03/HA/HA020.ogg"
    hachiman "I don't get too complacent in front of Komachi."
    voice "audio/voice/E5/YUK/03/YK/YK021.ogg"
    yukino "Oh, though it doesn't look that way?"
    show yukinoBatha with dissolve
    voice "audio/voice/E5/YUK/03/YK/YK022.ogg"
    yukino "............"
    #light water sfx
    play sound "audio/sfx/SE01/SE01_33.ogg"
    voice "audio/voice/E5/YUK/03/YK/YK023.ogg"
    yukino "Um..."
    voice "audio/voice/E5/YUK/03/HA/HA021.ogg"
    hachiman "What is it?"
    voice "audio/voice/E5/YUK/03/YK/YK024.ogg"
    yukino "... The water feels good, doesn't it?"
    voice "audio/voice/E5/YUK/03/HA/HA022.ogg"
    hachiman "Oh? Sure. It's like the warmth extends to the core..."
    voice "audio/voice/E5/YUK/03/YK/YK025.ogg"
    yukino "Yes... Um, for example..."
    stop voice
    hide yukinoBatha with dissolve
    hide yukinoBathb with dissolve
    voice "audio/voice/E5/YUK/03/HA/HA023.ogg"
    hachiman "...?"
    hachiman "(What's up with her? Was there something difficult to say in relation to Haruno-san?)"
    voice "audio/voice/E5/YUK/03/YK/YK026.ogg"
    yukino "... No, it's nothing."
    voice "audio/voice/E5/YUK/03/HA/HA024.ogg"
    hachiman "... Ah? Uh, okay. You don't have to force yourself to say something if it's hard to talk about."
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    scene yukinoBatha with dissolve
    window auto show dissolve
    voice "audio/voice/E5/YUK/03/YK/YK027.ogg"
    yukino "R-right..."
    voice "audio/voice/E5/YUK/03/HA/HA025.ogg"
    hachiman "............"
    voice "audio/voice/E5/YUK/03/YK/YK028.ogg"
    yukino "............"
    #light water sfx
    play sound "audio/sfx/SE01/SE01_34.ogg"
    voice "audio/voice/E5/YUK/03/YK/YK029.ogg"
    yukino "... Um ...!"
    voice "audio/voice/E5/YUK/03/IR/IR000.ogg"
    iroha "Ah, Yukinoshita-senpai!"
    voice "audio/voice/E5/YUK/03/MG/MG000.ogg"
    meguri "Huh, are you by yourself?"
    voice "audio/voice/E5/YUK/03/HA/HA026.ogg"
    hachiman "!"
    stop voice
    show hachimanBathc with dissolve
    play music "audio/bgm/BGM44.ogg"
    hachiman "(Isshiki and Meguri-senpai? Th-this has gotten kind of bad. What's so bad? The fact that I'm here itself is bad!)"
    voice "audio/voice/E5/YUK/03/YK/YK030.ogg"
    yukino "Ah... Good evening..."
    voice "audio/voice/E5/YUK/03/YK/YK031.ogg"
    yukino "Um... It's rare to see you two together."
    voice "audio/voice/E5/YUK/03/MG/MG001.ogg"
    meguri "Really?"
    voice "audio/voice/E5/YUK/03/YK/YK032.ogg"
    yukino "Ah, um..."
    voice "audio/voice/E5/YUK/03/IR/IR001.ogg"
    iroha "Those people are getting so excited they're being super noisy. So, I wanted to talk about tomorrow's plans in a quieter area."
    hachiman "(Oh, so that's how it is. This trip has sort of been under the idea of being sponsored by the Student Council.)"
    show hotspringBGB with dissolve
    voice "audio/voice/E5/YUK/03/YK/YK033.ogg"
    yukino "If that's the case, I'll be leaving..."
    voice "audio/voice/E5/YUK/03/MG/MG002.ogg"
    meguri "Eh, stay for a bit longer. It'd be a relief if you'd share your thoughts as well!"
    voice "audio/voice/E5/YUK/03/YK/YK034.ogg"
    yukino "... Is that so ..."
    hachiman "(Yukinoshita tried to leave, huh... Well, that's exactly what I'm trying to do right now though!)"
    voice "audio/voice/E5/YUK/03/IR/IR002.ogg"
    iroha "Anyway! Yukinoshita-senpai, your skin is so pretty. I'm jealous."
    voice "audio/voice/E5/YUK/03/YK/YK035.ogg"
    yukino "Th-that's not true. Both of you also..."
    voice "audio/voice/E5/YUK/03/MG/MG003.ogg"
    meguri "Eh, I don't feel good comparing myself to two youngers!" #Recheck wording?
    hachiman "(I'm going to hurry up and erase my presence from here...)"
    #small water sfx
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_30.ogg"
    scene yukinoBathc with dissolve
    window auto show dissolve
    voice "audio/voice/E5/YUK/03/IR/IR003.ogg"
    iroha "Eh, is there someone on the other side?"
    hachiman "(No way, I got caught!? Irohasu, you're too sharp!)"
    voice "audio/voice/E5/YUK/03/YK/YK036.ogg"
    yukino "Maybe some piled snow fell? You could hear it sometimes..."
    voice "audio/voice/E5/YUK/03/MG/MG004.ogg"
    meguri "Hm... That's less exciting."
    hachiman "(... Hm)"
    window auto hide dissolve
    stop music fadeout 0.5
    scene skyC with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    hachiman "(Anyway... What was Yukinoshita trying to say back then...?)"
    window auto hide dissolve
    call loading_screen from _call_loading_screen_20
    #general loading screen
    #loading screen with hot springs card and home yukino mid_center sad with some animation and sound effect, EC_BG67B.jpg
    #reference: https://www.youtube.com/watch?v=IzrLnvll_Z4 11m 9s
    image yukino home mid_center sad_flat = Flatten("yukino home mid_center sad")
    scene bathLoading with Fade(1.0, 2.0, 1.0)
    $renpy.pause(delay=2.0, hard=True)
    show yukino home mid_center sad_flat at center:
        xoffset -345 yoffset 75 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.6 xoffset -465
            linear 1.0 xoffset -345
    $renpy.pause(delay=2.0, hard=True)
    play sound "audio/sfx/SE02/SE02_06.ogg"
    $renpy.pause(delay=2.0, hard=True)
    jump E5_YUK_04

label E5_YUK_04:
    #scene hotspringBGB with Fade(1.0, 0.5, 1.0)
    scene hotspringBGB with Dissolve(1.5)
    $renpy.pause(delay=0.5, hard=True)
    play music "audio/bgm/BGM18.ogg"
    play sound "audio/sfx/SE01/SE01_33.ogg"
    window auto show dissolve
    voice "audio/voice/E5/YUK/04/MG/MG000.ogg"
    meguri "By the way, Yukinoshita-san. Do you have any plans tomorrow?"
    play sound "audio/sfx/SE01/SE01_34.ogg"
    voice "audio/voice/E5/YUK/04/YK/YK000.ogg"
    yukino "Nothing in particular you'd call plans..."
    voice "audio/voice/E5/YUK/04/IR/IR000.ogg"
    iroha "For real? Then, do you mind if we borrowed Senpai?"
    voice "audio/voice/E5/YUK/04/YK/YK001.ogg"
    yukino "By \"Senpai\", do you mean Hikigaya-kun?"
    voice "audio/voice/E5/YUK/04/IR/IR001.ogg"
    iroha "Yes yes."
    voice "audio/voice/E5/YUK/04/MG/MG001.ogg"
    meguri "Isshiki-san and I were talking about how to do the shopping for dinner tomorrow. Hiratsuka-sensei could bring the car, and we were thinking of asking a boy to help as well."
    show yukinoBathc with dissolve
    voice "audio/voice/E5/YUK/04/YK/YK002.ogg"
    yukino "... I see. U-um, but why was there a need to get my permission?"
    voice "audio/voice/E5/YUK/04/MG/MG002.ogg"
    meguri "That's of course...! Just because?"
    voice "audio/voice/E5/YUK/04/YK/YK003.ogg"
    yukino "H-ha..."
    voice "audio/voice/E5/YUK/04/IR/IR002.ogg"
    iroha "No, no, that's not not it. Since it looked like you two were skiing together today, we were checking if you had any plans with him tomorrow."
    voice "audio/voice/E5/YUK/04/YK/YK004.ogg"
    yukino "Plans... I wonder. All I did was teach him how to ski... I didn't ask Hikigaya-kun whether he wanted to try again tomorrow, and he might've had enoughafter today. If you ask him to help, wouldn't "
    voice sustain
    yukino "he do so?"
    voice "audio/voice/E5/YUK/04/IR/IR003.ogg"
    iroha "This is hopeless. It's a pain that both of them aren't aware of themselves..."
    voice "audio/voice/E5/YUK/04/YK/YK005.ogg"
    yukino "...?"
    voice "audio/voice/E5/YUK/04/IR/IR004.ogg"
    iroha "There's no way Senpai would've gone out of his way to make plans with someone. That person is the type to risk his life into never making any commitments. Like, a stupid boy who thinks not saying anything is "
    voice sustain
    iroha "cool."
    voice "audio/voice/E5/YUK/04/YK/YK006.ogg"
    yukino "That's a harsh way of putting it..."
    stop voice
    hide yukinoBathc with dissolve
    play sound "audio/sfx/SE01/SE01_30.ogg"
    voice "audio/voice/E5/YUK/04/MG/MG003.ogg"
    meguri "How should I put it, he's too serious yup. Like he won't say he can't do something from the beginning."
    voice "audio/voice/E5/YUK/04/IR/IR005.ogg"
    iroha "Though that person won't say he can do things either."
    voice "audio/voice/E5/YUK/04/YK/YK007.ogg"
    yukino "That's... definitely true."
    voice "audio/voice/E5/YUK/04/IR/IR006.ogg"
    iroha "Yep. That's why he's going to stick with you like it's natural tomorrow."
    voice "audio/voice/E5/YUK/04/MG/MG004.ogg"
    meguri "Ah, I can get that! Okay then, let's ask someone else to help with the shopping."
    voice "audio/voice/E5/YUK/04/IR/IR007.ogg"
    iroha "Seems that would be best. I'll ask Tobe-senpai. Probably has nothing to do, that thing."
    voice "audio/voice/E5/YUK/04/MG/MG005.ogg"
    meguri "Right. Okay, let's go with that!"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.5
    scene yukinoBatha with dissolve:
        zoom 1.3 xoffset -100 yoffset -30
    with dissolve
    window auto show dissolve
    yukino "(... Like natural... Being together. At some point, it's become like that...)"
    window auto hide dissolve
    call loading_screen(filename="01_30") from _yuk_hotspring_povx
    jump E5_CMM_04


# audio/voice/E5/CMM/03
# after skiing stuff

#Below is from E5_CMM_03 (scene returning from skiing on first day on ski trip).
#unknown for now. Probably yui route, and haruno route right here
    hachiman "(⋯⋯それにしても騒がしいな。小町が楽しそうだからいいけど、やっぱ来るんじゃなかったかも)"
    "昼間の折本の言葉が耳に付いて離れなかった。正確には、由比ヶ浜の問いにどう答えてやればよかったのかわからなかった自分自身に嫌悪を感じる。"
    hachiman "(⋯⋯とりあえず、一人でぼーっとしたい)"
    hachiman "(とりあえず早くここから逃げよう。そういやここ、温泉だったっけ⋯⋯)"
    hachiman "(いまのうちなら露天風呂独り占めして、ゆっくりできそうだな⋯⋯)"
    "昼間一色が何やら言っていたことをちらっと思い出したが、それはすぐに頭から追い出しておこう。"
    hachiman "(⋯⋯そういや戸部は相変わらずだとして、三浦は⋯⋯。夕食の時も大人しかったしな⋯⋯)"
    hachiman "(いやまあ俺がどうこうするような問題でもないんだが⋯⋯)"
    "とはいえ、一度三浦と葉山の態度が不自然だと感じてしまうと、つい気になってしまう。"
    "そこで頭をよぎるのは、あの日の三浦の真剣なまなざしだ。しかし所詮は奉仕部への依頼として、その心の裡を垣間見ただけの関係にすぎない。"
    hachiman "(ま、空いてそうな今のうちに風呂にでも入ってくるかな⋯⋯)"
    hachiman "(あー。あの人たち、お酒入ったら確実にいつもの三倍めんどくさいぞ⋯⋯しかも平塚先生全力でスキーやってたし、酒回るの早そう⋯⋯)"
    hachiman "(そういや戸塚も『巻き込まれそう』とか不吉な予言してたしな⋯⋯見つからないうちに逃げよう)"
    hachiman "(戸塚⋯⋯戸塚といえばどこ行った？ せっかくだし風呂に誘いたい！ そして一緒に入りたい！)"

label E5_YUK_05:
    voice "audio/voice/E5/YUK/05/HA/HA000.ogg"
    hachiman "Oh?"
    show yui home mid_center surprised at center with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E5/YUK/05/YI/YI000.ogg"
    yui "Hikki, what's wrong?"
    voice "audio/voice/E5/YUK/05/HA/HA001.ogg"
    hachiman "Nah..."
    "It looked like I'd accidentally pulled out two straws. They had \"Guest rooms\" and \"Outdoor hot springs\" written on them."
    play sound "audio/sfx/SE00/SE00_31.ogg"
    hide yui with dissolve
    image keika home near vhappy_flat = Flatten("keika home near vhappy")
    image saki home mid_left vhappy_flat = Flatten("saki home mid_left vhappy")
    show keika home near vhappy_flat at left:
        xoffset 100 yoffset 75 alpha 0
        parallel:
            easein 0.15 xoffset 250
        parallel:
            linear 0.15 alpha 1
    $renpy.pause(delay=0.15, hard=True)
    hide keika
    show keika home near vhappy at left:
        xoffset 250 yoffset 75
    voice "audio/voice/E5/YUK/05/KE/KE000.ogg"
    keika "Haa-chan, give Keika one too."
    stop sound
    voice "audio/voice/E5/YUK/05/HA/HA002.ogg"
    hachiman "Kei-chan, you sure are lively today as well."
    show keika happy with dissolve
    voice "audio/voice/E5/YUK/05/KE/KE001.ogg"
    keika "Yeah! Haa-chan, you don't look very lively."
    voice "audio/voice/E5/YUK/05/HA/HA003.ogg"
    hachiman "... Really?"
    show saki home mid_left vhappy_flat at right:
        xoffset 0 yoffset 75 alpha 0
        parallel:
            easein 0.15 xoffset -95
        parallel:
            linear 0.15 alpha 1
    $renpy.pause(delay=0.15, hard=True)
    hide saki
    show saki home mid_left vhappy at right:
        xoffset -95 yoffset 75
    voice "audio/voice/E5/YUK/05/SA/SA000.ogg"
    saki "Kei-chan, let's clean the windows over there with Saa-chan."
    hide keika with dissolve
    show keika home mid sad zorder 1 at left with dissolve:
        xoffset 310 yoffset 75
    voice "audio/voice/E5/YUK/05/KE/KE002.ogg"
    keika "Keika wants to clean with Haa-chan!"
    hide saki
    $url = ["saki home mid_left pout", "saki home mid_left blush"]
    $multiImagePara = [-95, 75, 0, 0, 3.1]
    call multiImage() from _call_multiImage_37
    voice "audio/voice/E5/YUK/05/SA/SA001.ogg"
    saki "No. Since this was decided by lottery. O-okay, then we'll be going."
    call finishmultiImage from _call_finishmultiImage_38
    hide keika
    with dissolve
    show iroha home mid_center angry at center with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E5/YUK/05/IR/IR000.ogg"
    iroha "I thought this during Christmas and Valentines, Senpai, you're nice to little kids, aren't you? Do you like younger girls after all?"
    voice "audio/voice/E5/YUK/05/HA/HA004.ogg"
    hachiman "It's not like I'm bad with them. Rather, I might be better with younger than older."
    hide iroha
    $url = ["iroha home mid_center surprised", "iroha home mid_center frown"]
    $multiImagePara = [5, 75, 0, 0, 0.7]
    call multiImage() from _call_multiImage_38
    voice "audio/voice/E5/YUK/05/IR/IR001.ogg"
    iroha "Ah!{size=50} {/size}Were {size=50}you {size=35}possibly hitting one me just now of course as a girl I always want someone older gently leading but if there's one difference there's no attraction so could you come back after you usually act like someone older {/size}{/size} "
    voice sustain
    iroha "{size=50}I'm sorry but no{/size}."
    call finishmultiImage from _call_finishmultiImage_39
    show iroha home mid_center frown at center:
        xoffset 5 yoffset 75
    voice "audio/voice/E5/YUK/05/HA/HA005.ogg"
    hachiman "No, I'm not hitting on you, and I'm not acting like someone older either... Whatever, just go and clean."
    hide iroha
    $url = ["iroha home mid_center frown", "iroha home mid_left frown"]
    $multiImagePara = [5, 75, -35, 65, 2.8]
    call multiImage(0, False) from _call_multiImage_39
    voice "audio/voice/E5/YUK/05/IR/IR002.ogg"
    iroha "Isn't your response kind of cold? Right, Yukinoshita-senpai?"
    call finishmultiImage from _call_finishmultiImage_40
    with dissolve
    show yukino home mid_center blush at left:
        xoffset 25 yoffset 75
    show iroha home mid_left frown at right:
        xoffset -315 yoffset 65
    with dissolve
    voice "audio/voice/E5/YUK/05/YK/YK000.ogg"
    yukino "Look... It's probably because the temperature hasn't gone up enough yet, so maybe he's just slow."
    voice "audio/voice/E5/YUK/05/HA/HA006.ogg"
    hachiman "What, was I a hibernating animal? Though sure my eyes look like an amphibians'."
    show yukino avoid with dissolve
    voice "audio/voice/E5/YUK/05/YK/YK001.ogg"
    yukino "Who knows. Isshiki-san, let's hurry and get the cleaning done."
    show iroha vhappy with dissolve
    voice "audio/voice/E5/YUK/05/IR/IR003.ogg"
    iroha "Sure. I want to ski a lot today as well."
    hide yukino
    hide iroha
    with dissolve
    #no script
    menu lodge_cleaning2:
        hachiman "...And with that, which should I clean?"
        with dissolve
        "Guest Rooms":
            hachiman "(Washing the outdoor baths sure seem like it'd hurt my back...)"
            window auto hide dissolve
            stop music fadeout 1
            jump E5_YUK_06
        "Outdoor baths": #I think you encounter meguri in bathhouse (E5_YUK_07).
            "not finished"
            jump lodge_cleaning2

label E5_YUK_06:
    scene lodgeroomA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM08.ogg"
    show komachi home mid_center vhappy at center with dissolve:
        xoffset -75 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/YUK/06/KO/KO000.ogg"
    komachi "Ohh, Onii-chan."
    voice "audio/voice/E5/YUK/06/HA/HA000.ogg"
    hachiman "Oh, so you were here too."
    "... etc, what a beautiful moment of reunion between siblings."
    show komachi happy with dissolve
    voice "audio/voice/E5/YUK/06/KO/KO001.ogg"
    komachi "Onii-chan, I'll leave you to do that side."
    voice "audio/voice/E5/YUK/06/HA/HA001.ogg"
    hachiman "O-okay..."
    show komachi home mid_left vhappy with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUK/06/KO/KO002.ogg"
    komachi "Hmm~huhum~hmmm~"
    voice "audio/voice/E5/YUK/06/HA/HA002.ogg"
    hachiman "Komachi, you're pretty good at this... How do you do it so well? Show me some more model work?"
    show komachi unimpressed with dissolve
    voice "audio/voice/E5/YUK/06/KO/KO003.ogg"
    komachi "No, this much is only normal. And even if you compliment me, I'm not going to do your share of the work. That's your work."
    voice "audio/voice/E5/YUK/06/HA/HA003.ogg"
    hachiman "How strict..."
    show komachi angry with dissolve
    voice "audio/voice/E5/YUK/06/KO/KO004.ogg"
    komachi "Komachi just finished her exams, so I was thinking of disciplining Onii-chan."
    hachiman "(Discipline from my younger sister... Such a sweet sound...!)"
    show komachi mid_center happy with dissolve:
        xoffset -75 yoffset 75
    play sound "audio/sfx/SE01/SE01_14.ogg"
    $renpy.pause(delay=1, hard=False)
    show komachi vhappy with dissolve
    voice "audio/voice/E5/YUK/06/KO/KO005.ogg"
    komachi "And with that, let's do this efficiently!"
    voice "audio/voice/E5/YUK/06/HA/HA004.ogg"
    hachiman "Y-yeah..."
    play sound "audio/sfx/SE01/SE01_14.ogg"
    show komachi angry with dissolve
    voice "audio/voice/E5/YUK/06/KO/KO006.ogg"
    komachi "And by the way, Onii-chan."
    voice "audio/voice/E5/YUK/06/HA/HA005.ogg"
    hachiman "What's up?"
    show komachi happy with dissolve
    voice "audio/voice/E5/YUK/06/KO/KO007.ogg"
    komachi "Yukino-san looks like she's feeling better. Komachi is relieved."
    voice "audio/voice/E5/YUK/06/HA/HA006.ogg"
    hachiman "What's with that all of a sudden?"
    show komachi angry with dissolve
    voice "audio/voice/E5/YUK/06/KO/KO008.ogg"
    komachi "Because I heard it was rough at school."
    voice "audio/voice/E5/YUK/06/HA/HA007.ogg"
    hachiman "Komachi, you sure are nice."
    show komachi happy with dissolve
    voice "audio/voice/E5/YUK/06/KO/KO009.ogg"
    komachi "Because Komachi likes Yukino-san. So much I want to call her Onee-chan."
    voice "audio/voice/E5/YUK/06/HA/HA008.ogg"
    hachiman "... No, you can't call her that, probably."
    hide komachi
    $url = ["komachi home mid_left frown", "komachi home mid_left happy"]
    $multiImagePara = [10, 75, 0, 0, 1.9]
    call multiImage() from _call_multiImage_40
    voice "audio/voice/E5/YUK/06/KO/KO010.ogg"
    komachi "Tch, no go huh... But actually Yukino-san looked like she was pretty lively. Seeing that made me feel lively as well."
    call finishmultiImage from _call_finishmultiImage_41
    show komachi home mid_left happy at center:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUK/06/HA/HA009.ogg"
    hachiman "Really? She doesn't look any different than usual to me though."
    hide komachi
    $url = ["komachi home mid_left angry", "komachi home mid_left happy"]
    $multiImagePara = [10, 75, 0, 0, 1.4]
    call multiImage() from _call_multiImage_41
    voice "audio/voice/E5/YUK/06/KO/KO011.ogg"
    komachi "Hm... Then how about looking at her more properly? Then you might understand."
    call finishmultiImage from _call_finishmultiImage_42
    show komachi home mid_left happy at center:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/YUK/06/HA/HA010.ogg"
    hachiman "Maybe..."
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    jump E5_CMM_05


label E5_YUK_07:
    "not finished"
    jump E5_CMM_05

label E5_YUK_08:
    voice "audio/voice/E5/YUK/08/HA/HA000.ogg"
    hachiman "You're okay with teaching me today too?"
    show yukino vhappy with dissolve
    voice "audio/voice/E5/YUK/08/YK/YK000.ogg"
    yukino "Yes, since we're here, let's master it before leaving."
    voice "audio/voice/E5/YUK/08/HA/HA001.ogg"
    hachiman "Sorry for the bother."
    show yukino avoid with dissolve
    voice "audio/voice/E5/YUK/08/YK/YK001.ogg"
    yukino "It's nothing, I suggested it as well. It's only natural to take responsibility until the end. Okay then, let's start from revising yesterday's..."
    window auto hide dissolve
    play sound ["<to 2>audio/sfx/SE01/SE01_44L.ogg", "audio/sfx/SE01/SE01_47.ogg"]
    stop music fadeout 1.0
    $renpy.pause(delay=1, hard=True)
    show yukino surprised with dissolve
    $renpy.pause(delay=0.5, hard=True)
    hide yukino with dissolve
    $renpy.pause(delay=1, hard=True)
    play music "audio/bgm/BGM47.ogg"
    show yukino heavy_coat mid_center frown at left:
        xoffset 25 yoffset 75
    show haruno athletic mid_center happy at right:
        xoffset -240 yoffset 75
    with dissolve
    stop sound
    window auto show dissolve
    voice "audio/voice/E5/YUK/08/HR/HR000.ogg"
    haruno "Huh? It's Hikigaya-kun. Is Yukino-chan guiding you?"
    voice "audio/voice/E5/YUK/08/YK/YK002.ogg"
    yukino "Nee-san..."
    voice "audio/voice/E5/YUK/08/HA/HA002.ogg"
    hachiman "Yes.... Well I'm a super beginner."
    show haruno vhappy with dissolve
    voice "audio/voice/E5/YUK/08/HR/HR001.ogg"
    haruno "Is that so. But if Yukino-chan is teaching you, why are you hanging around a place like this?"
    show yukino annoyed with dissolve
    voice "audio/voice/E5/YUK/08/YK/YK003.ogg"
    yukino "..."
    voice "audio/voice/E5/YUK/08/HA/HA003.ogg"
    hachiman "Well, because I'm seriously a super beginner."
    show haruno athletic mid_left sly with dissolve:
        xoffset -240
    voice "audio/voice/E5/YUK/08/HR/HR002.ogg"
    haruno "But you don't look like you're unathletic... Maybe it's how you're being taught."
    show yukino pout with dissolve
    voice "audio/voice/E5/YUK/08/YK/YK004.ogg"
    yukino "..."
    voice "audio/voice/E5/YUK/08/HA/HA004.ogg"
    hachiman "No no no, it's not that, it's because I really am a beginner..."
    show haruno mid_center sly with dissolve:
        xoffset -240
    voice "audio/voice/E5/YUK/08/HR/HR003.ogg"
    haruno "Hikigaya-kun, should I teach you instead? It'd be boring if you didn't ski after being brought all this way."
    show haruno happy with dissolve
    voice "audio/voice/E5/YUK/08/HR/HR004.ogg"
    haruno "You didn't want to come to this ski trip after all, right?"
    voice "audio/voice/E5/YUK/08/HA/HA005.ogg"
    hachiman "Well, that is true. But, thanks to you I'm able to ski a little now and it's been surprisingly fun. I'm able to ski for longer compared to when I started as well.."
    show yukino sly with dissolve
    voice "audio/voice/E5/YUK/08/YK/YK005.ogg"
    yukino "Right, thinking back, you've made quite an improvement."
    voice "audio/voice/E5/YUK/08/HA/HA006.ogg"
    hachiman "Right? I'm pretty capable, aren't I?"
    show haruno mid_left sly with dissolve:
        xoffset -240
    voice "audio/voice/E5/YUK/08/HR/HR005.ogg"
    haruno "Is that so. But if that's the case, isn't it more fun to ski from higher up?"
    voice "audio/voice/E5/YUK/08/HA/HA007.ogg"
    hachiman "... Eh?"
    show yukino angry with dissolve
    voice "audio/voice/E5/YUK/08/YK/YK006.ogg"
    yukino "Yes, I intend to do that."
    voice "audio/voice/E5/YUK/08/HA/HA008.ogg"
    hachiman "Wait a minute? Calm down?"
    show haruno vhappy with dissolve
    voice "audio/voice/E5/YUK/08/HR/HR006.ogg"
    haruno "Of course, Yukino-chan. This follows that saying. The lion will drop its own child down a bottomless valley."
    voice "audio/voice/E5/YUK/08/HA/HA009.ogg"
    hachiman "But you shouldn't kill them off..."
    voice "audio/voice/E5/YUK/08/HA/HA010.ogg"
    hachiman "No, I'm having enough fun down here so..."
    hide yukino
    hide haruno
    with dissolve
    show yukino heavy_coat near_left angry at right with dissolve:
        xoffset -125 yoffset 80
    voice "audio/voice/E5/YUK/08/YK/YK007.ogg"
    yukino "Alright, Hikigaya-kun. Let's go."
    voice "audio/voice/E5/YUK/08/HR/HR007.ogg"
    haruno "Ah, the lifts are over here."
    show yukino happy with dissolve
    voice "audio/voice/E5/YUK/08/YK/YK008.ogg"
    yukino "Yes, I know."
    hachiman "(Hey, that leads up way too high!)"
    voice "audio/voice/E5/YUK/08/HR/HR008.ogg"
    haruno "~~~"#Uh consider revising
    window auto hide dissolve
    stop voice
    scene slopes2A
    show yukino heavy_coat mid_center pout at left:
        xoffset 25 yoffset 75
    show haruno athletic mid_center happy at right:
        xoffset -240 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    play ambient "audio/sfx/SE02/SE02_00.ogg" noloop
    window auto show dissolve
    voice "audio/voice/E5/YUK/08/HR/HR009.ogg"
    haruno "............"
    voice "audio/voice/E5/YUK/08/HA/HA011.ogg"
    hachiman "S-so high..."
    voice "audio/voice/E5/YUK/08/YK/YK009.ogg"
    yukino "............"
    voice "audio/voice/E5/YUK/08/HR/HR010.ogg"
    haruno "Alright, let's have fun and ski!"
    hide haruno with dissolve
    play sound "audio/sfx/SE01/SE01_45.ogg"
    $renpy.pause(delay=0.5, hard=True)
    hide yukino with dissolve
    show yukino heavy_coat mid_center pout at center with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E5/YUK/08/HA/HA012.ogg"
    hachiman "There she goes..."
    voice "audio/voice/E5/YUK/08/YK/YK010.ogg"
    yukino "Yes..."
    voice "audio/voice/E5/YUK/08/HA/HA013.ogg"
    hachiman "Alright then, let's get down."
    show yukino sad with dissolve
    voice "audio/voice/E5/YUK/08/YK/YK011.ogg"
    yukino "............"
    voice "audio/voice/E5/YUK/08/YK/YK012.ogg"
    yukino "... I got carried away... I'm sorry..."
    voice "audio/voice/E5/YUK/08/HA/HA014.ogg"
    hachiman "It's not a big deal. This is as high as it gets. We just have to go down slowly."
    voice "audio/voice/E5/YUK/08/YK/YK013.ogg"
    yukino "But..."
    voice "audio/voice/E5/YUK/08/HA/HA015.ogg"
    hachiman "Well, worst case scenario we can walk down. Though that might take some time."
    show yukino concerned with dissolve
    voice "audio/voice/E5/YUK/08/YK/YK014.ogg"
    yukino "... I ..."
    hachiman "(I'm too embarassed to say this next one...)"
    voice "audio/voice/E5/YUK/08/HA/HA016.ogg"
    hachiman "Yukinoshita. Sorry, but would you mind coming with me?"
    show yukino vhappy with dissolve
    voice "audio/voice/E5/YUK/08/YK/YK015.ogg"
    yukino "Of course."
    voice "audio/voice/E5/YUK/08/HA/HA017.ogg"
    hachiman "Alright, then let's go..."
    hide yukino with dissolve
    "Slowly and carefully... Without thinking about the height or speed...
        But the thing with slopes is that the speed and the bumps in the snow make me sway off course."
    "Each time I avoided the other skiers, my own speed also kept increasing..."
    window auto hide dissolve
    play ambient "audio/sfx/SE01/SE01_42L.ogg"
    $renpy.pause(delay=0.25, hard=True)
    show transition_1b at offscreenright:
        parallel:
            easein 0.1 xpos -780
    $renpy.pause(delay=0.15, hard=True)
    scene slopes2A at ski_shake2:
        zoom 1.8 xpos -1375 ypos -605
    show transition_1b at offscreenright:
        xpos -780
        parallel:
            easein 0.15 xpos -3500
    $renpy.pause(delay=0.15, hard=True)
    hide transition_1b
    #with Shake((0, 0, 0, 0), 1.0, dist=20)
    window auto show dissolve
    voice "audio/voice/E5/YUK/08/HA/HA018.ogg"
    hachiman "Oh... Woah... Wohoh? WOOAH!"
    voice "audio/voice/E5/YUK/08/YK/YK016.ogg"
    yukino "Hi-Hikigaya-kun! Are you okay! Hold on, that way is...!?"
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    stop ambient fadeout 0.5
    scene black with Fade(1.0, 0.5, 0)
    play sound "audio/sfx/SE02/SE02_02.ogg"
    $renpy.pause(delay=1, hard=False)
    play footsteps "<loop 2>audio/sfx/SE01/SE01_59L.ogg" loop
    play music "audio/bgm/BGM46.ogg"
    scene slopes2D
    show yukino heavy_coat_dark mid_left sad at center:
        xoffset 50 yoffset 80
    with Fade(0, 1, 1.0)
    window auto show dissolve
    voice "audio/voice/E5/YUK/08/HA/HA019.ogg"
    hachiman "... I can see the lifts and the centre house in the distance. That's a relief. It looks like we're not lost."
    voice "audio/voice/E5/YUK/08/YK/YK017.ogg"
    yukino "Indeed..."
    voice "audio/voice/E5/YUK/08/HA/HA020.ogg"
    hachiman "But the snow's gotten stronger."
    show yukino pout with dissolve
    voice "audio/voice/E5/YUK/08/YK/YK018.ogg"
    yukino "... That's true."
    voice "audio/voice/E5/YUK/08/YK/YK019.ogg"
    yukino "............"
    hachiman "(Yukinoshita must be really exhausted. She's probably at her physical limit.)"
    hachiman "(Back then I thought this would be a good idea to make her feel better, but we should have just gone down the mountain after all. To think things ended up like this...)"
    voice "audio/voice/E5/YUK/08/HA/HA021.ogg"
    hachiman "Can we take a short break?"
    show yukino frown with dissolve
    voice "audio/voice/E5/YUK/08/YK/YK020.ogg"
    yukino "We cant. It's dangerous to stop. We might no longer be able to move."
    voice "audio/voice/E5/YUK/08/HA/HA022.ogg"
    hachiman "But... hm? What is that...?"
    window auto hide dissolve
    stop voice
    stop footsteps fadeout 1
    scene yukinocabinEVA with Fade(1.0, 1, 1.0)
    play sound "audio/sfx/SE02/SE02_03.ogg"
    window auto show dissolve
    voice "audio/voice/E5/YUK/08/YK/YK021.ogg"
    yukino "This looks like it's a temporary evacuation shelter. It looks like these were built in case of accidents."
    voice "audio/voice/E5/YUK/08/HA/HA023.ogg"
    hachiman "Let's rest here and see how things go. I'm grateful for that designer's foresight."
    voice "audio/voice/E5/YUK/08/YK/YK022.ogg"
    yukino "That's true. I hate my foolishness for not learning from that."
    stop music fadeout 0.5
    voice "audio/voice/E5/YUK/08/YK/YK023.ogg"
    yukino "Um... I'm really sorry. I hadn't been very calm. It looks like we were overconfident in each other... I caused you trouble because of that..."
    "From our close proximity to conserve our body temperatures, I felt Yukinoshita's shoulder slightly tremble. I understood what she meant."
    menu yukino_shelter_menu:
        "To cheer her up, I subtly shifted towards her and I thought I felt her body shake faintly."
        with dissolve
        "I should be thankful for that instead.":
            play music "audio/bgm/BGM11.ogg"
            voice "audio/voice/E5/YUK/08/HA/HA024.ogg"
            hachiman "... I should be thankful for that person instead." #TLed from audio.
            voice "audio/voice/E5/YUK/08/YK/YK024.ogg" #TLed from audio
            yukino "Grateful?"
            voice "audio/voice/E5/YUK/08/HA/HA025.ogg"#transcribed from video
            hachiman "Accidents on the snowy mountains like this are uncommon activities after all."# 雪山で遭難なんて、案外遭遇できることひゃないからな
            voice "audio/voice/E5/YUK/08/YK/YK025.ogg"
            yukino "For mountain climbers or skiiers, it might not be that uncommon though?"#登山やスキーを趣味にすれば案外あるかもしれないわよ？
            voice "audio/voice/E5/YUK/08/HA/HA026.ogg"
            hachiman "In my case, I wouldn't have such hobbies in the first place."#俺の場合、まず趣味にしないからな
            voice "audio/voice/E5/YUK/08/YK/YK026.ogg" #order not set
            yukino "Though it may just be sophistry, I suppose you're right."#屁理屈
            jump E5_YUK_08_cont
        "It was a problem with my skills":
            "not finished"
            jump yukino_shelter_menu
            voice "audio/voice/E5/YUK/08/HA/HA027.ogg"
            hachiman "No, it was purely a problem with my skills." #TL from audio
            voice "audio/voice/E5/YUK/08/YK/YK027.ogg"
            yukino ""
            voice "audio/voice/E5/YUK/08/HA/HA028.ogg"
            hachiman ""
            voice "audio/voice/E5/YUK/08/YK/YK028.ogg"
            yukino ""
            voice "audio/voice/E5/YUK/08/HA/HA029.ogg" #order not set
            hachiman ""
            voice "audio/voice/E5/YUK/08/YK/YK029.ogg"
            yukino ""
            jump E5_YUK_08_cont
        "Mishaps are typical on snow mountains":
            play music "audio/bgm/BGM11.ogg"
            voice "audio/voice/E5/YUK/08/HA/HA030.ogg"
            hachiman "Mishaps are typical on snow mountains."
            voice "audio/voice/E5/YUK/08/YK/YK030.ogg"
            yukino "...Eh?"
            voice "audio/voice/E5/YUK/08/HA/HA031.ogg"
            hachiman "You can even say it's one of the reasons it's an attraction."
            voice "audio/voice/E5/YUK/08/YK/YK031.ogg"
            yukino "Then you can say Nee-san had prepared an attraction for us."
            voice "audio/voice/E5/YUK/08/HA/HA032.ogg"
            hachiman "If you think about it like that, then this itself is fun."
            voice "audio/voice/E5/YUK/08/YK/YK032.ogg"
            yukino "You don't have to expect that much from Nee-san."
            jump E5_YUK_08_cont

    #jump here maybe
    #fast wind blowing sfx 10 seconds
label E5_YUK_08_cont:
    play sound "audio/sfx/SE02/SE02_03.ogg"
    "Yukinoshita's voice finally had more life in it. Relieved, I looked at the outside scenery.
        Due to the snowstorm, outside this shelter was a world of nothing but a solid white landscape." #sounds awkward.
    window auto hide dissolve
    scene skyD with dissolve
    window auto show dissolve
    voice "audio/voice/E5/YUK/08/YK/YK033.ogg"
    yukino "This view... somehow calms you."
    "She spoke with an enraptured voice."
    "I heard that as a very sad confession. This scenery was sometihng I, and likely Yukinoshita too, had always found familiar."
    voice "audio/voice/E5/YUK/08/HA/HA033.ogg"
    hachiman "It's an empty world though..."
    "I wonder since when did I begin to feel that was sad. I was surprised at my own words which I'd said without thinking. And then..."
    voice "audio/voice/E5/YUK/08/YK/YK034.ogg"
    yukino "But it's different now..."
    window auto hide dissolve
    stop voice
    scene yukinocabinEVB with dissolve
    window auto show dissolve
    voice "audio/voice/E5/YUK/08/YK/YK035.ogg"
    yukino "... You're here."
    voice "audio/voice/E5/YUK/08/HA/HA034.ogg"
    hachiman "............"
    "Her smile and those words surprised me yet again."
    voice "audio/voice/E5/YUK/08/YK/YK036.ogg"
    yukino "............"
    voice "audio/voice/E5/YUK/08/HA/HA035.ogg"
    hachiman "............"
    window auto hide dissolve
    stop voice
    stop music fadeout 1
    scene white with Fade(1.0, 2, 0, color="#fff")
    scene lodgeoutB with Fade(1.0, 2, 1.0)
    play music "audio/bgm/BGM18.ogg"
    window auto show dissolve
    "Eventually the snowstorm passed and with the road passable once again, we finally returned to the lodge."
    "The others had already returned and I didn't care whether they still enjoyed skiing or not."
    show yukino heavy_coat_sunset mid_center sad at center with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E5/YUK/08/HA/HA036.ogg"
    hachiman "We finally made it back... Are you okay?"
    show yukino unimpressed with dissolve
    voice "audio/voice/E5/YUK/08/YK/YK037.ogg"
    yukino "Yes. I rested plenty."
    voice "audio/voice/E5/YUK/08/HA/HA037.ogg"
    hachiman "Yeah, but we've had to walk quite a bit."
    show yukino vhappy with dissolve
    voice "audio/voice/E5/YUK/08/YK/YK038.ogg"
    yukino "Right... To be honest, I'm barely standing."
    voice "audio/voice/E5/YUK/08/HA/HA038.ogg"
    hachiman "To be honest me too."
    voice "audio/voice/E5/YUK/08/YK/YK039.ogg"
    yukino "............"
    voice "audio/voice/E5/YUK/08/HA/HA039.ogg"
    hachiman "............"
    "There wasn't a doubt I was laughing honestly. The same as her.
        It was a good thing our facial expressions were apparent at dusk despite this time of day."
    "Because this kind of expression is hidden yet unmistakable, I was fine not naming this emotion."
    window auto hide dissolve
    stop music fadeout 1
    jump E5_CMM_06
    #end scene.


label E5_YUK_09:
    stop music fadeout 0.5
    show komachi home mid_center angry at center with dissolve:
        xoffset -75 yoffset 75
    play music "audio/bgm/BGM21.ogg"
    voice "audio/voice/E5/YUK/09/KO/KO000.ogg"
    komachi "Onii-chan."
    voice "audio/voice/E5/YUK/09/HA/HA000.ogg"
    hachiman "What's up, Komachi?"
    voice "audio/voice/E5/YUK/09/KO/KO001.ogg"
    komachi "You were with Yukino-san up till now... Did something happen to her?"
    voice "audio/voice/E5/YUK/09/HA/HA001.ogg"
    hachiman "Well, some stuff. How was she?"
    show komachi pout with dissolve
    voice "audio/voice/E5/YUK/09/KO/KO002.ogg"
    komachi "Her face looks pale, like she's really tired. You should go see her too if you're curious."
    voice "audio/voice/E5/YUK/09/HA/HA002.ogg"
    hachiman "No, I wouldn't say I'm curious..."
    show komachi frown with dissolve
    voice "audio/voice/E5/YUK/09/KO/KO003.ogg"
    komachi "Then are you not?"
    voice "audio/voice/E5/YUK/09/HA/HA003.ogg"
    hachiman "... I am worried..."
    show komachi happy with dissolve
    voice "audio/voice/E5/YUK/09/KO/KO004.ogg"
    komachi "Hmm, Well that'll do. But, if you are curious, then it'd be better if you showed it."
    voice "audio/voice/E5/YUK/09/HA/HA004.ogg"
    hachiman "Yeah, I know. Then, good night."
    window auto hide dissolve
    stop voice
    scene lodgeroomC with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E5/YUK/09/HA/HA005.ogg"
    hachiman "Curious, huh..."
    "I couldn't deny I was curious about her. I had forced her to be strong when she didn't have stamina as well. That's why naturally I was curious."
    "That should have been enough reason. It made sense. Yet, I wasn't satisfied with it."
    "There was just an unexpected accident... But was that the only reason I was curious about her right now?"
    "... I didn't have to bother asking myself that."
    "There was a time I'd believed Yukinoshita Yukino to be a strong girl and forced my ideals on her by clinging onto my egoistic beliefs.
        And for that, I'd became disappointed in myself."
    "But it should be different now."
    "Yukinoshita smiled as she said I was here now."
    window auto hide dissolve
    scene yukinocabinEVB with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    voice "audio/voice/E5/YUK/09/YK/YK000.ogg"
    yukino "But it's different now... You're here."
    window auto hide dissolve
    stop voice
    scene lodgeroomC with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    "Emotions that should reply to that smile and those words."
    "What should I name them, and how should I define them."
    window auto hide dissolve
    stop voice
    stop music fadeout 1
    image yukino home mid_center sad_flat = Flatten("yukino home mid_center sad")
    scene lodgeLoading with Fade(1.0, 2, 1.0)
    $renpy.pause(delay=2.0, hard=True)
    show yukino home mid_center sad_flat at center:
        xoffset -345 yoffset 75 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.6 xoffset -465
            easeout 1.0 xoffset -345
    $renpy.pause(delay=3.0, hard=True)
    #original loading screen with yukino home mid_center concerned/sad and animation and EC_BG59C.jpg
    jump E5_YUK_10

#straight from E5_YUK_09
label E5_YUK_10:
    scene lodgeroomC with Dissolve(1.0)
    play music "audio/bgm/BGM46.ogg"
    show yui home mid_center sad at center with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E5/YUK/10/YI/YI000.ogg"
    yui "Yukinon, how are you feeling? Will you be okay?"
    voice "audio/voice/E5/YUK/10/YK/YK000.ogg"
    yukino "Thank you... I'm okay now. It looks like I made you worry. I'm really sorry..."
    show yui surprised with dissolve
    voice "audio/voice/E5/YUK/10/YI/YI001.ogg"
    yui "Not at all! Don't worry about it! And I haven't really done anything either..."
    voice "audio/voice/E5/YUK/10/YK/YK001.ogg"
    yukino "That's not true. I've been... saved by you."
    show yui pout with dissolve
    voice "audio/voice/E5/YUK/10/YI/YI002.ogg"
    yui "No, I really haven't done anything..."
    voice "audio/voice/E5/YUK/10/YK/YK002.ogg"
    yukino "You helped me. When I think about it, you always have."
    show yui sad with dissolve
    voice "audio/voice/E5/YUK/10/YI/YI003.ogg"
    yui "Yukinon..."
    "She, who always had a smile on her face, now had a shadowed expression."
    "The things I'm saying now, the things I'm going to say from now on, I'm sure they're unfair. But they'll accept someone even as unfair as I am."
    "She would. My friend would."
    "Maybe I just want things to be easier."
    "We can somewhat guess each other's thoughts, so if we put that into words, it would break and be lost."
    "And she's someone that put things into words. Because she's a wonderful person who's honest, bright, and kind.
        She's different from me. I've never been able to put things into words."
    "That's why this discussion is over now. I'll wrap this up without saying it, bury my feelings in a field, then I'll watch over the happy end."
    "At least, that's how it should have been..."
    show yui happy with dissolve
    voice "audio/voice/E5/YUK/10/YI/YI004.ogg"
    yui "Hey, Yukinon. I've always been saved as well. From the very beginning, all the time. And I was the one who was saved first."
    show yui vhappy with dissolve
    voice "audio/voice/E5/YUK/10/YI/YI005.ogg"
    yui "It looks like we've only been saved this whole time."
    voice "audio/voice/E5/YUK/10/YK/YK003.ogg"
    yukino "Right... I'm... Always being spoiled by you and Hikigaya-kun."
    voice "audio/voice/E5/YUK/10/YI/YI006.ogg"
    yui "Yeah."
    voice "audio/voice/E5/YUK/10/YK/YK004.ogg"
    yukino "It became like that at some point. Even though I'd told myself that I had to be independent and not rely on others."
    show yui happy with dissolve
    voice "audio/voice/E5/YUK/10/YI/YI007.ogg"
    yui "Isn't that fine? Relying, being troublesome, or a burden to others."
    show yui vhappy with dissolve
    voice "audio/voice/E5/YUK/10/YI/YI008.ogg"
    yui "Me, Yukinon... and Hikki too. Because we're all troublesome to each other. But that's why, you don't have to worry about it."
    voice "audio/voice/E5/YUK/10/YK/YK005.ogg"
    yukino "Yuigahama-san..."
    "You really are a kind person. If I were to end everything by burying my feelings in a field, she would surely be heartbroken."
    "I don't want to push all the guilt onto her. Regardless of what the result becomes. Even if I lose it. I don't want to be spoiled and always depend on others."
    voice "audio/voice/E5/YUK/10/YK/YK006.ogg"
    yukino "There's something I want."
    window auto hide dissolve
    stop music fadeout 1
    $renpy.pause(delay=2,hard=True)
    window auto show dissolve
    voice "audio/voice/E5/YUK/10/YK/YK007.ogg"
    yukino "Yuigahama-san."
    show yui happy with dissolve
    voice "audio/voice/E5/YUK/10/YI/YI009.ogg"
    yui "What is it?"
    voice "audio/voice/E5/YUK/10/YK/YK008.ogg"
    yukino "I love Hikigaya-kun. I'm sure I won't meet another person like him again."
    window auto hide dissolve
    stop voice
    hide yui with dissolve
    play sound "audio/sfx/SE01/SE01_12.ogg"
    scene yuiyukinoEV with Dissolve(1.0)
    play music "audio/bgm/BGM42.ogg"
    window auto show dissolve
    voice "audio/voice/E5/YUK/10/YI/YI010.ogg"
    yui "Yeah..."
    voice "audio/voice/E5/YUK/10/YK/YK009.ogg"
    yukino "Yuigahama-san, um... I'm sor-"
    voice "audio/voice/E5/YUK/10/YI/YI011.ogg"
    yui "Yukinon. Do your best. I like you, Yukinon. I love you both so... Do your best."
    voice "audio/voice/E5/YUK/10/YK/YK010.ogg"
    yukino "Thank you, Yuigahama-san."
    voice "audio/voice/E5/YUK/10/YI/YI012.ogg"
    yui "Yep."
    window auto hide dissolve
    stop music fadeout 0.5
    image yukino home mid_center vhappy flat = Flatten("yukino home mid_center vhappy")
    scene loading_wlogo
    show yukino home mid_center vhappy flat at center:
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
    #general loading screen with yukino home mid_center vhappy animation
    jump E5_YUK_11

#straight from E5_YUK_10
label E5_YUK_11:
    scene lodgeroomC with Fade(1.0, 0.5, 1.0)  #if using the loading screens, dissolve from loading screen
    window auto show dissolve
    voice "audio/voice/E5/YUK/11/HA/HA000.ogg"
    hachiman "It's pretty cold..."
    hachiman "(I'll get warm taking a bath. If even I collapsed, it'd cause extra worry.)"
    window auto hide dissolve
    play sound "audio/sfx/SE04/SE04_08.ogg"
    scene hotspringBGB with dissolve
    window auto show dissolve
    voice "audio/voice/E5/YUK/11/HA/HA001.ogg"
    hachiman "Hm?"
    voice "audio/voice/E5/YUK/11/HY/HY000.ogg"
    hayama "Hey."
    "As I entered the bath, I saw Hayama relaxing in the water. I wasn't in the mood to see him, but I wasn't in the mood to just leave either."
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_31.ogg"
    show hachimanBatha with dissolve
    play music "audio/bgm/BGM21.ogg"
    window auto hide dissolve
    voice "audio/voice/E5/YUK/11/HY/HY001.ogg"
    hayama "I heard about it from Haruno-san."
    voice "audio/voice/E5/YUK/11/HA/HA002.ogg"
    hachiman "Yeah. Well, it wasn't a big deal."
    voice "audio/voice/E5/YUK/11/HY/HY002.ogg"
    hayama "Only you... and Haruno-san would say that. In that meaning, you and Haruno-san are similar. That's probably why she likes you."
    voice "audio/voice/E5/YUK/11/HA/HA003.ogg"
    hachiman "Only as a toy easy to play with and break."
    voice "audio/voice/E5/YUK/11/HY/HY003.ogg"
    hayama "That's unexpected. You realised."
    voice "audio/voice/E5/YUK/11/HA/HA004.ogg"
    hachiman "I'm very self-aware."
    voice "audio/voice/E5/YUK/11/HY/HY004.ogg"
    hayama "That's true. It's not like you're not self-aware or oblivious. Rather, you're the type to notice."
    voice "audio/voice/E5/YUK/11/HA/HA005.ogg"
    hachiman "What, are you complimenting me? It's past the point of mentioning my attentiveness."
    voice "audio/voice/E5/YUK/11/HY/HY005.ogg"
    hayama "I'm not complimenting you... It's not really something to compliment about."
    voice "audio/voice/E5/YUK/11/HA/HA006.ogg"
    hachiman "That's true."
    stop voice
    hide hachimanBatha with dissolve
    "The words disappeared in the steam and made us appear blurred to each other."
    "There was no conversation between him and I, only the sounds of water. I only gazed up at the stars lightning the heavens."
    "But even that was hard to see through because of the steam."
    voice "audio/voice/E5/YUK/11/HY/HY006.ogg"
    hayama "In the end, you're averting your eyes away... Even though you can't do that forever."
    "I wondered who was he was talking about. No, I already knew. Me and him."
    show hachimanBatha with dissolve
    voice "audio/voice/E5/YUK/11/HA/HA007.ogg"
    hachiman "There's something you can see by averting your eyes away as well."
    voice "audio/voice/E5/YUK/11/HY/HY007.ogg"
    hayama "..."
    voice "audio/voice/E5/YUK/11/HY/HY008.ogg"
    hayama "You've changed a little. Both her... and you."
    voice "audio/voice/E5/YUK/11/HA/HA008.ogg"
    hachiman "Huh?"
    "Hayama looked at me with a somewhat bitter and lonely smile. Those words were so unexpected I could only make that stupid reply."
    voice "audio/voice/E5/YUK/11/HY/HY009.ogg"
    hayama "... I'm the only one who can't change."
    "Hayama muttered with a heavy voice. When I glanced at his expression, his facial features remaining good-looking, but his eyes looked terribly dark."
    "But, it was probably better to say it wasn't rotten or impure. Such self-scorn escaped his mouth."
    show hachimanBatha at topleft with dissolve:
        zoom 1.7 xoffset -17 yoffset -312
    voice "audio/voice/E5/YUK/11/HA/HA009.ogg"
    hachiman "Who knows. Haven't you also changed if you can think others have changed? Not that I would know."
    voice "audio/voice/E5/YUK/11/HY/HY010.ogg"
    hayama "Do you think so?"
    voice "audio/voice/E5/YUK/11/HA/HA010.ogg"
    hachiman "Like I said, I don't know."
    "I answered lightly without really thinking about it. But Hayama, while lightly biting his lip, stared at me and didn't look away."
    "Up until now, I, as well as Hayama, have quickly averted our eyes, turned our faces away, and spoken vague words."
    "But it was only different during this moment, now, when we had nothing between us but the warm water that melted the snow."
    hide hachimanBatha
    show hachimanBatha
    with dissolve 
    voice "audio/voice/E5/YUK/11/HY/HY011.ogg"
    hayama "If you avert your eyes, and what you see is still broad... what is it you've decided you want to see?"
    "The sound of his voice told me he wasn't testing me, nor trying to see through me. It was purely just him questioning me."
    "Hayama Hayato may have wanted to know an answer to not choosing anything, or maybe an answer to choosing something one day. If that was the case, I already knew what I had to say."
    voice "audio/voice/E5/YUK/11/HA/HA011.ogg"
    hachiman "Don't ask me about that. At the very least, it's something different to you."
    voice "audio/voice/E5/YUK/11/HY/HY012.ogg"
    hayama "Is that so..."
    scene hotspringBGB with dissolve
    play sound "audio/sfx/SE01/SE01_30.ogg" #placeholder sfx
    "Hayama let out a satisfied sigh as he left the bath."
    hachiman "(Well, I don't care since I'm finally alone...)"
    "My beloved loneliness."
    window auto hide dissolve
    stop music fadeout 1
    jump E5_CMM_07

label E5_YUK_12:
    show haruno sweater mid_left vhappy with dissolve:
        xoffset -20
    "As I tried to forcibly reject Haruno-san, she blocked me off and suddenly smiled.
        Maybe it was because of the moonlight that was shining in, but she had a gentle smile she'd never shown before."
    show haruno happy with dissolve
    voice "audio/voice/E5/YUK/12/HR/HR000.ogg"
    haruno "About Yukino-chan... She doesn't really change, right. You as well, don't really change."
    voice "audio/voice/E5/YUK/12/HA/HA000.ogg"
    hachiman "Hm?"
    voice "audio/voice/E5/YUK/12/HR/HR001.ogg"
    haruno "Despite that, I wonder why you're still forgiven."
    voice "audio/voice/E5/YUK/12/HA/HA001.ogg"
    hachiman "No reason, maybe it's because we don't think we want to be forgiven by someone."
    show haruno sweater mid_center vhappy with dissolve:
        xoffset 10
    voice "audio/voice/E5/YUK/12/HR/HR002.ogg"
    haruno "I quite like that about you. You're a waste on Yukino-chan after all. And I might be a bit jealous."
    voice "audio/voice/E5/YUK/12/HA/HA002.ogg"
    hachiman "Why... is that?"
    show haruno annoyed with dissolve
    voice "audio/voice/E5/YUK/12/HR/HR003.ogg"
    haruno "Yukino-chan is a troublesome girl. Are you okay with that?"
    voice "audio/voice/E5/YUK/12/HA/HA003.ogg"
    hachiman "What do you mean by that?"
    show haruno sly with dissolve
    voice "audio/voice/E5/YUK/12/HR/HR004.ogg"
    haruno "Who knows. Think about it yourself."
    voice "audio/voice/E5/YUK/12/HA/HA004.ogg"
    hachiman "You really..."
    show haruno happy with dissolve
    voice "audio/voice/E5/YUK/12/HR/HR005.ogg"
    haruno "Alright, I'm going to go drink again."
    voice "audio/voice/E5/YUK/12/HR/HR006.ogg"
    haruno "See ya. Bye bye."
    hide haruno with dissolve
    stop music fadeout 1
    "As that person waved her hand, she stood up and left."
    hachiman "(Jealous, huh...)"
    play music "audio/bgm/BGM46.ogg"
    "I didn't know how much of that was true. In the first place, I don't undersand that person's real motives, and of course I didn't because she was the type to not show them either."
    "But, it felt like there was some truth to those words just now."
    hachiman "(There's no way that person didn't see through Yukinoshita's feelings or mine.)"
    hachiman "(But it was something that person wouldn't have detested. Or was that the case?
        I'd always thought of this person as someone who mocked and hated every kind of deception.)" #not sure
    hachiman "(If that was the case...)"
    "Up until now, how had I seen Yukinoshita Haruno, and also Yukinoshita Yukino as?"
    "She'd commented that we hadn't really changed. But if so, something had changed ever so slightly, and the way we saw each other was also changing..."
    "Then, just what exactly had changed?"
    "That was probably the shape of what we wished for. The ideal figure we pushed onto each other, then one-sidedly got disappointed."
    window auto hide dissolve
    scene yukinocabinEVB with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    voice "audio/voice/E5/YUK/12/YK/YK000.ogg"
    yukino "This view... somehow calms you."
    window auto hide dissolve
    stop voice
    scene lodgeC with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    "It was fine even if we weren't forgiven by someone. But, could I, myself, forgive that change?"
    window auto hide dissolve
    stop music fadeout 1
    #original: general loading screen. with live2D yukino.
    call loading_screen(23) from _call_loading_screen_18
    jump E6_CMM_01
