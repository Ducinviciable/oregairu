label E2_CMM_01:
    scene houseA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM06.ogg"
    window auto show dissolve
    voice "audio/voice/E2/CMM/01/HA/HA000.ogg"
    hachiman "Ah..."
    hachiman "(Winter break is the best. Around this time, when the New Year's holiday is ending and the corporate slaves are starting to get busy working, is when it's most enjoyable.)"
    hachiman "(I'm just going to stay under the kotatsu and watch all the anime I've been saving...)"
    hachiman "(What really makes winter break so great is that others are working while I'm not...)"
    voice "audio/voice/E2/CMM/01/WC/WC000.ogg"
    kamakura "Meoooooow."
    voice "audio/voice/E2/CMM/01/HA/HA001.ogg"
    hachiman "Hey Kamakura, you think so too, right?"
    voice "audio/voice/E2/CMM/01/WC/WC001.ogg"
    kamakura "Meoooooow."
    voice "audio/voice/E2/CMM/01/HA/HA002.ogg"
    hachiman "There, there. When I go to the bathroom, I'll bring you something to munch on."
    voice "audio/voice/E2/CMM/01/WC/WC002.ogg"
    kamakura "Meow."
    stop music
    voice "audio/voice/E2/CMM/01/KO/KO000.ogg"
    mystery "There's no point... It's the end for me..."
    window auto hide dissolve
    stop voice
    play music "audio/bgm/BGM47.ogg"
    show komachi athletic mid_left unimpressed at center with dissolve:
        xoffset 40 yoffset 75
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E2/CMM/01/HA/HA003.ogg"
    hachiman "Oh? What's with you?"
    show komachi athletic mid_center unimpressed at center with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E2/CMM/01/KO/KO001.ogg"
    komachi "Ah, onii-chan..."
    hachiman "(Komachi's eyes, usually so lovable, now looked as dead as a fish out of water.)"
    hachiman "(No way, they look like onii-chan's! As expected of siblings! Cute Komachi looking like me means I'll become cute too!)"
    hachiman "(No, but these rotten eyes seriously aren't cute. If I'm not cute even with Komachi's cuteness, aren't I just absolutely repulsive?)"
    hachiman "(Anyway, this is the first time I've seen Komachi so neck-deep in trouble.)"
    voice "audio/voice/E2/CMM/01/HA/HA004.ogg"
    hachiman "Are you okay, Komachi?"
    window auto hide dissolve
    stop voice
    show komachiScene with dissolve
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E2/CMM/01/KO/KO002.ogg"
    komachi "Yeah... I'm not..."
    voice "audio/voice/E2/CMM/01/HA/HA005.ogg"
    hachiman "You're not?"
    voice "audio/voice/E2/CMM/01/KO/KO003.ogg"
    komachi "I have to... do the cleaning. Trash... I have to clean up the trash. I have to clean up Trashnii-chan."
    voice "audio/voice/E2/CMM/01/HA/HA006.ogg"
    hachiman "Calm down, Komachi. You finished cleaning a while ago. Also, you can't get rid of Onii-chan that easily. You're going to have to wait."
    voice "audio/voice/E2/CMM/01/KO/KO004.ogg"
    komachi "Ah... Komachi wants this taken care of sooner..."
    "Because Komachi was procrastinating her studies by cleaning, the house was spotless. The only trash left in the house were just me and our father."
    "\"There's no way you could get rid of annoying ol' me\" ...Isn't what I should say. I should focus on Komachi right now."
    voice "audio/voice/E2/CMM/01/KO/KO005.ogg"
    komachi "No... no more. Komachi can't do this anymore..."
    "Komachi starts holding her head in her hands as she wails."
    voice "audio/voice/E2/CMM/01/KO/KO006a.ogg"
    komachi "Waah... Komachi'll sink into a depression if she fails the exam..."
    voice "audio/voice/E2/CMM/01/KO/KO006b.ogg"
    komachi "\"Hikigaya-san's kids are both shut-ins fufufu\", is what the neighbours will say! There's no way I'll be able to lead a decent life!"
    voice "audio/voice/E2/CMM/01/HA/HA007.ogg"
    hachiman "I'm not a shut-in though..."
    window auto hide dissolve
    hide komachiScene
    show komachi athletic mid_left sad at center:
        xoffset 40 yoffset 75
    with dissolve
    $renpy.pause(delay=1.5, hard=True)
    hide komachi with dissolve
    window auto show dissolve
    "As if she couldn't hear me, Komachi was grabbing at her hair and collapsed on the table."
    hachiman "(She's at it again... She's in the same state now as she was at the end of the year.)"
    hachiman "(Well, there are things like marriage blues and maternity blues. This is probably under the classification \"entrance exam blues\".)"
    hachiman "(Others include squadrons like Point Red and Corporate Slave Black. Anyway, Komachi might just need a slight change of pace to take her mind off things.)"
    voice "audio/voice/E2/CMM/01/HA/HA008.ogg"
    hachiman "Ah... Anyway, you want some, you know, coffee?"
    show komachi athletic mid_center sad at center with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E2/CMM/01/KO/KO007.ogg"
    komachi "Yeah..."
    stop music fadeout 1.0
    menu E2_CMM_01_menu:
        with dissolve
        hachiman "(Yeah... it seems that it'd be inefficient even if she tried to study the way she is now.)"
        "Should I take her out as a distraction?": #yukino route
            play music "audio/bgm/BGM34.ogg"
            voice "audio/voice/E2/CMM/01/HA/HA009.ogg"
            hachiman "Hey, do you want to go out for a bit after coffee?"
            hachiman "(It'd be great if I could keep her mind off things even just a little.)"
            show komachi pout with dissolve
            voice "audio/voice/E2/CMM/01/KO/KO008.ogg"
            komachi "...Where?"
            voice "audio/voice/E2/CMM/01/HA/HA010.ogg"
            hachiman "I haven't decided that part yet... Even if you kept studying, the way you are right now, you wouldn't make much progress."
            show komachi athletic mid_left sad at center with dissolve:
                xoffset 40 yoffset 75
            voice "audio/voice/E2/CMM/01/KO/KO009.ogg"
            komachi "I dunno..."
            voice "audio/voice/E2/CMM/01/HA/HA011.ogg"
            hachiman "Whether it's work or studying, what's important is efficiency.
            What I mean is that there's no point in working overtime regardless of whether it's flexible work or performance-based work. In other "
            voice sustain
            hachiman "words, there are times when it is right to do nothing."
            show komachi athletic mid_center unimpressed at center with dissolve:
                xoffset -75 yoffset 75
            voice "audio/voice/E2/CMM/01/KO/KO010.ogg"
            komachi "...As expected of you. You're a genius at making excuses."
            voice "audio/voice/E2/CMM/01/HA/HA012.ogg"
            hachiman "Hahaha... Okay, let's stay here then."
            show komachi vhappy with dissolve
            voice "audio/voice/E2/CMM/01/KO/KO011.ogg"
            komachi "I'm kidding! Komachi's super ready to go out together!"
            window auto hide dissolve
            stop voice
            stop music fadeout 1.0
            jump E2_G04_01
        "Should I buy her something?":
            play music "audio/bgm/BGM34.ogg"
            voice "audio/voice/E2/CMM/01/HA/HA013.ogg"
            hachiman "Ah, while the coffee is brewing... is there something you wanna eat with it?"
            show komachi pout with dissolve
            voice "audio/voice/E2/CMM/01/KO/KO012.ogg"
            komachi "Something I want to eat?"
            voice "audio/voice/E2/CMM/01/HA/HA014.ogg"
            hachiman "Yeah, they say sweet stuff is good for when you're tired."
            show komachi frown with dissolve
            voice "audio/voice/E2/CMM/01/KO/KO013.ogg"
            komachi "Okay."
            show komachi annoyed with dissolve
            voice "audio/voice/E2/CMM/01/KO/KO014.ogg"
            komachi "Onii-chan, don't tell me when you say sweet stuff you're talking about Max Coffee. You're not, right?"
            voice "audio/voice/E2/CMM/01/HA/HA015.ogg"
            hachiman "What do you mean, \"don't tell me\"... Do you not like Max Coffee?"
            show komachi athletic mid_left pout at center with dissolve:
                xoffset 40 yoffset 75
            voice "audio/voice/E2/CMM/01/KO/KO015.ogg"
            komachi "It's not like I hate it..."
            voice "audio/voice/E2/CMM/01/HA/HA016.ogg"
            hachiman "The way you say that tells me you do..."
            voice "audio/voice/E2/CMM/01/HA/HA017.ogg"
            hachiman "Well, I'll buy you something, so have some coffee and wait here. You like it on the milkier side, right?"
            show komachi happy with dissolve
            voice "audio/voice/E2/CMM/01/KO/KO016.ogg"
            komachi "Yeah, cafe au lait is fine."
            voice "audio/voice/E2/CMM/01/HA/HA018.ogg"
            hachiman "Gotcha."
            show komachi vhappy with dissolve
            window auto hide dissolve
            stop music fadeout 1.0
            jump E2_G05_01
        "Should I cheer her up a little bit?":#iroha and hiratsuka route
            play music ["<silence 0.3>", "audio/bgm/BGM34.ogg"]
            voice "audio/voice/E2/CMM/01/HA/HA019.ogg"
            hachiman "Well, if someone like me managed to do it, you'll be fine, Komachi."
            show komachi annoyed with dissolve
            voice "audio/voice/E2/CMM/01/KO/KO017.ogg"
            komachi "Komachi knows... Actually onii-chan is really good at studying..."
            voice "audio/voice/E2/CMM/01/HA/HA020.ogg"
            hachiman "Well, as long as it's not math..."
            show komachi athletic mid_left annoyed at center with dissolve:
                xoffset 40 yoffset 75
            voice "audio/voice/E2/CMM/01/KO/KO018.ogg"
            komachi "Hmph, it's annoying to have someone good at studying looking down on me."
            voice "audio/voice/E2/CMM/01/HA/HA021.ogg"
            hachiman "No way. You usually never praise onii-chan."
            show komachi unimpressed with dissolve
            voice "audio/voice/E2/CMM/01/KO/KO019.ogg"
            komachi "That wasn't praise..."
            voice "audio/voice/E2/CMM/01/HA/HA022.ogg"
            hachiman "Komachi, you seem to be getting tired. Your voice and even your eyes are turning dead."
            voice "audio/voice/E2/CMM/01/KO/KO020.ogg"
            komachi "It's my best onii-chan impression."
            voice "audio/voice/E2/CMM/01/HA/HA023.ogg"
            hachiman "You don't look like me at all."
            voice "audio/voice/E2/CMM/01/HA/HA024.ogg"
            hachiman "Well, you don't have to worry that much about your future. If it's just you, I should be able to think of something."
            window auto hide dissolve
            stop voice
            hide komachi with dissolve
            show komachi athletic near_center blush at center with dissolve:
                xoffset 35 yoffset 75
            window auto show dissolve
            voice "audio/voice/E2/CMM/01/KO/KO021.ogg"
            komachi "Onii-chan..."
            voice "audio/voice/E2/CMM/01/HA/HA025.ogg"
            hachiman "It shouldn't make a difference if it's just 1 or 2 people, so I'll beg mom and dad to take care of us."
            show komachi athletic near_left unimpressed at center with dissolve:
                xoffset 10 yoffset 65
            voice "audio/voice/E2/CMM/01/KO/KO022.ogg"
            komachi "You really should've said \"I'll get a job\" instead..."
            show komachi vhappy with dissolve
            "Komachi slowly rubbed her eyes and smiled while she said that."
            voice "audio/voice/E2/CMM/01/HA/HA026.ogg"
            hachiman "That will be my last resort... Onii-chan is pretty good at solving problems, if I do say so myself so... don't worry."
            show komachi athletic near_center vhappy at center with dissolve:
                xoffset 35 yoffset 75
            "I raised my hand and patted Komachi on the head."
            show komachi happy with dissolve
            voice "audio/voice/E2/CMM/01/KO/KO023.ogg"
            komachi "You know, onii-chan, when Komachi looks at you.."
            "Komachi put her hand on mine and stared at me with moist eyes. There was a silence and then she finally let out a sigh."
            show komachi unimpressed with dissolve
            voice "audio/voice/E2/CMM/01/KO/KO024.ogg"
            komachi "She sees that you say some pretty ridiculous stuff when you're worried..."
            hide komachi with dissolve
            "She then brushed my hand away."
            voice "audio/voice/E2/CMM/01/HA/HA027.ogg"
            hachiman "If it's just that, then that's fine."
            hachiman "(This is how she is when she's a little nicer. She's cute like this, too, isn't she? Yeah, she is, but it's a little different from the cuteness I'm used to.)"
            show komachi athletic mid_left unimpressed at center with dissolve:
                xoffset 40 yoffset 75
            voice "audio/voice/E2/CMM/01/KO/KO025.ogg"
            komachi "Hah, alright, enough of that. Back to studying for me~"
            hide komachi with dissolve
            "Komachi, contrary to the calm atmosphere, stood up from her chair with a screech, and immedietly went to exit the living room. But as soon as she touched the dorknob, she stopped."
            show komachi athletic far_left blush at center with dissolve:
                xoffset 25 yoffset 75
            voice "audio/voice/E2/CMM/01/KO/KO026.ogg"
            komachi "...Thanks."
            hide komachi with dissolve
            play sound "audio/sfx/SE04/SE04_06.ogg"
            "With that one word, she quickly exited the living room and swiftly closed the door. On the other side, I could hear the, more hectic than usual, sound of her slippers as she walked away."
            window auto hide dissolve
            stop music fadeout 0.5
            jump E2_G06_01
