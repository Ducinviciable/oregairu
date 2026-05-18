label E6_CMM_01:
    scene houseA with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "It was the day after we got back home from the ski camp."
    hachiman "(I don't want to think about anything for the next two or three days...)"
    "As I was laying on the sofa without a care in the world..."
    play sound "audio/sfx/SE00/SE00_31.ogg"
    window auto hide dissolve
    $renpy.pause(delay=1,hard=True)
    play music "audio/bgm/BGM45.ogg"
    show komachi athletic mid_center pout1 at center with dissolve:
        xoffset -75 yoffset 75
    window auto show dissolve
    voice "audio/voice/E6/CMM/01/KO/KO000.ogg"
    stop sound fadeout 1
    komachi "Uwah! This is bad! This is bad! This is bad! I'm done for--!"
    voice "audio/voice/E6/CMM/01/HA/HA000.ogg"
    hachiman "What happened, Komachi?"
    show komachi sad with dissolve
    voice "audio/voice/E6/CMM/01/KO/KO001.ogg"
    komachi "Komachi doesn't know what to do until the results are out!"
    voice "audio/voice/E6/CMM/01/HA/HA001.ogg"
    hachiman "Komachi... Weren't you calm and composed during the trip?"
    show komachi athletic mid_left sad with dissolve:
        xoffset 40
    voice "audio/voice/E6/CMM/01/KO/KO002.ogg"
    komachi "I could get away from reality when I was on the trip! I could get away with not thinking about it!"
    voice "audio/voice/E6/CMM/01/HA/HA002.ogg"
    hachiman "Well, it's not like I don't understand how you feel... But just be a little patient for 10 days."
    show komachi pout with dissolve
    voice "audio/voice/E6/CMM/01/KO/KO003.ogg"
    komachi "It's a whole 10 days away, I can't calm down! If this was going to happen, the ski trip should have been a week long!"
    hachiman "(10 days? No way, my spirit would have long departed by the end!)"
    voice "audio/voice/E6/CMM/01/HA/HA003.ogg"
    hachiman "Say, Komachi..."
    show komachi sad with dissolve
    voice "audio/voice/E6/CMM/01/KO/KO004.ogg"
    komachi "Uh-huh?"
    voice "audio/voice/E6/CMM/01/HA/HA004.ogg"
    hachiman "You worked really hard for the exams, right?"
    show komachi pout with dissolve
    voice "audio/voice/E6/CMM/01/KO/KO005.ogg"
    komachi "Uh-huh."
    voice "audio/voice/E6/CMM/01/HA/HA005.ogg"
    hachiman "We also visited that shrine on New Years, right?"
    show komachi mid_center sad with dissolve:
        xoffset -75
    voice "audio/voice/E6/CMM/01/KO/KO006.ogg"
    komachi "Yeah..."
    voice "audio/voice/E6/CMM/01/HA/HA006.ogg"
    hachiman "You went all out on the real exam, right?"
    show komachi pout with dissolve
    voice "audio/voice/E6/CMM/01/KO/KO007.ogg"
    komachi "Yeah."
    voice "audio/voice/E6/CMM/01/HA/HA007.ogg"
    hachiman "Then have some confidence. You did what you could. If you don't get in, then that just means Sobu High wasn't right for you."
    show komachi sad with dissolve
    voice "audio/voice/E6/CMM/01/KO/KO008.ogg"
    komachi "That doesn't make me feel better at all..."
    voice "audio/voice/E6/CMM/01/HA/HA008.ogg"
    hachiman "And what the hell. If it comes to it, I'll do something about it."
    show komachi happy with dissolve
    voice "audio/voice/E6/CMM/01/KO/KO009.ogg"
    komachi "Onii-chan..."
    voice "audio/voice/E6/CMM/01/HA/HA009.ogg"
    hachiman "It's not much different taking care of two people instead of one. I'll beg our parents to take care of us."
    show komachi unimpressed with dissolve
    voice "audio/voice/E6/CMM/01/KO/KO010.ogg"
    komachi "I wanted you to say you'd get a job right there..."
    show komachi angry with dissolve
    voice "audio/voice/E6/CMM/01/KO/KO011.ogg"
    komachi "Listen, Onii-chan. When Komachi looks at you..."
    voice "audio/voice/E6/CMM/01/HA/HA010.ogg"
    hachiman "Hm?"
    show komachi unimpressed with dissolve
    voice "audio/voice/E6/CMM/01/KO/KO012.ogg"
    komachi "You say some pretty dumb things when you're worried."
    voice "audio/voice/E6/CMM/01/HA/HA011.ogg"
    hachiman "That's good to know."
    voice "audio/voice/E6/CMM/01/HA/HA012.ogg"
    hachiman "Let's go see the cherry blossoms when spring comes."
    show komachi happy with dissolve
    voice "audio/voice/E6/CMM/01/KO/KO013.ogg"
    komachi "Yeah. When we're wearing the same uniform."
    voice "audio/voice/E6/CMM/01/HA/HA013.ogg"
    hachiman "That's right."
    show komachi mid_left happy with dissolve:
        xoffset 40
    voice "audio/voice/E6/CMM/01/KO/KO014.ogg"
    komachi "Alright then. Komachi will go shopping for dinner. Until I can get someone to take you, Komachi has to take care of you."
    voice "audio/voice/E6/CMM/01/HA/HA014.ogg"
    hachiman "That's a long ways away. You won't find someone to take me that easily."
    voice "audio/voice/E6/CMM/01/KO/KO015.ogg"
    komachi "I wonder about that... Think it through, okay?"
    voice "audio/voice/E6/CMM/01/HA/HA015.ogg"
    hachiman "Think what through?"
    show komachi vhappy with dissolve
    voice "audio/voice/E6/CMM/01/KO/KO016.ogg"
    komachi "That's also something you need to figure out yourelf! Okay, I'm off!"
    voice "audio/voice/E6/CMM/01/HA/HA016.ogg"
    hachiman "Yeah, be careful."
    hide komachi with dissolve
    stop music fadeout 0.5
    voice "audio/voice/E6/CMM/01/HA/HA017.ogg"
    hachiman "............"
    hachiman "(\"Figure out\", huh...)"
    window auto hide dissolve
    #figure out close eyes effect. might need to create a new ImageDissolve
    show transition_2a at truecenter:
        yoffset -890
        parallel:
            linear 0.5 yoffset -190
    show transition_2b at truecenter:
        yoffset 890
        parallel:
            linear 0.5 yoffset 190
    $renpy.pause(delay=0.5, hard=True)
    hide transition_2a
    hide transition_2b
    show black
    $points = _calculate_points()
    $hiratsukaPt = points['hiratsuka']
    $harunoPt = points['haruno']
    $meguriPt = points['meguri']
    window auto show dissolve
    menu E6_thoughts:
        "As I lie down on the sofa once again and close my eyes, something comes to mind. That was..."
        with dissolve
        "About Yukinoshita":
            show yukino school near_center vhappy at center with dissolve:
                xoffset -165 yoffset 75
            hachiman "I wonder what Yukinoshita is doing now?"
            hachiman "It would be nice if I could see the cherry blossoms with her..."
            hide yukino with dissolve
            "Without any deception, if that wish could be directly conveyed to her. Embracing that wish, I had at some point fallen asleep."
            window auto hide dissolve
            jump E6_YUK_01
        "I'm not interested.":
            jump E4_IRO_05
        "About Iroha" if ski_flag == "iroha":
            show iroha school near_center happy at center with dissolve:
                xoffset -15 yoffset 75
            hachiman "(My sister...good grief. Komachi is sulky, cries easily, and is a bit pushy. She also tries too hard to help people, which can get annoying, but at least she's dependable. My little sister is the cutest in the "
            hachiman "world.)"
            hachiman "(Then there's that girl. Also a little pushy, calculating, and honest to a fault. I can't keep my eyes off her 'cause it seems like she's always in trouble. Isshiki Iroha is...the cutest girl in the world.)"
            hide iroha with dissolve
            hachiman "(Being dragged around while watching over her was fun, and surprisingly an important part of my life... and I don't think there's anything wrong with that.)"
            window auto hide dissolve
            jump E6_IRO_01
        "That person's true feelings" if ski_flag == "haruno" or ski_flag == "meguri":
            if ski_flag == "haruno" and (totsukaTalkFlag == "haruno" or totsukaTalkFlag == "meguri"):
                show haruno sweater near_center happy at center with dissolve:
                    xoffset -20 yoffset 75
                hachiman "(I wonder how she's doing right now...)"
                "I was never able to figure her out."
                "And yet, I took forward to what she will do next with a mix of fear and excitement. When did I realize that I was beginning to like the arbitrariness of it, I wonder?"
                hide haruno with dissolve
                hachiman "(Is this what they call Stockholm syndrome?)"
                hachiman "(I'm being steadily swept away, aren't I...?)"
                window auto hide dissolve
                jump E6_HAR_01
            elif ski_flag == "meguri" and (totsukaTalkFlag == "haruno" or totsukaTalkFlag == "meguri"):
                show meguri school near vhappy at center with dissolve:
                    xoffset -5 yoffset 75
                hachiman "(You really are one hard-working former student council president, Meguri-senpai...)"
                hachiman "(After her taking my training seriously, I was able to ski... My muscles hurt all over though...)"
                hachiman "(When it comes to muscle pain, the colossal Megurin effect works better than the hot spring we had over there. If I had to choose, I'd have to go with the Megurin effect...)"
                hide meguri with dissolve
                window auto hide dissolve
                jump E6_HAR_01
            else:
                jump E4_IRO_05
        "About Yuigahama" if ski_flag == "yui":
            show yui school near_center happy at center with dissolve:
                xoffset -15 yoffset 75
            hachiman "(Come to think of it, I had a promise I had made with Yuigahama.)"
            "That we'd go to Destiny Sea together one day."
            hide yui with dissolve
            hachiman "(I have to keep my promise...)"
            window auto hide dissolve
            jump E6_YUI_01
        "Hiratsuka-sensei's words":
            if ski_flag != "hiratsuka" or hiratsukaPt < 5:
                show hiratsuka school near_center happy at center with dissolve:
                    xoffset 30 yoffset 75
                "Come to think of it, Hiratsuka-sensei only talked about my future. I guess from a teacher's standpoint, it's only natural."
                "Hiratsuka-sensei won't be my teacher anymore after graduation however."
                "Maybe she was apologizing for something to the me in the future, where our relationship would become distant and eventually be broken entirely."
                jump E4_IRO_05
            elif ski_flag == "hiratsuka":
                hachiman "(\"Something to look back on and feel nostalgic about\", huh...)"
                show hiratsuka school near_center happy at center with dissolve:
                    xoffset 30 yoffset 75
                "Looking back on it, Hiratsuka-sensei was always talking about my future. Maybe that's just the way she sees it as a teacher. It's only natural if you think about it that way."
                "She talked about the future, but... Hiratsuka-sensei won't be my teacher anymore after graduation."
                "Maybe she was just trying to leave me with something for the future, when our relationship will become distant and eventually non-existant."
                hide hiratsuka with dissolve
                hachiman "(But before I knew it, I was wishing for something more with a person who is so close, yet so far away.)"
                jump E6_SHI_01
