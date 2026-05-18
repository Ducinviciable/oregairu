label E3_YUK_01:
    scene hallwayB with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM21.ogg"
    window auto show dissolve
    voice "audio/voice/E3/YUK/01/HA/HA000.ogg"
    hachiman "Hey..."
    show yui school_sunset near_center sad at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E3/YUK/01/YI/YI000.ogg"
    yui "Huh?"
    voice "audio/voice/E3/YUK/01/HA/HA001.ogg"
    hachiman "About before, don't talk about it in the clubroom."
    show yui pout with dissolve
    voice "audio/voice/E3/YUK/01/YI/YI001.ogg"
    yui "Huh? Why not?"
    voice "audio/voice/E3/YUK/01/HA/HA002.ogg"
    hachiman "Because she's definitely going to get mad."
    show yui school_sunset near_left pout at center with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E3/YUK/01/YI/YI002.ogg"
    yui "Yeah, true! Ah, but..."
    stop music fadeout 0.5
    voice "audio/voice/E3/YUK/01/YK/YK000.ogg"
    yukino "What is this, \"about before?\""
    show yui near_right surprised2 at center with dissolve:
        xoffset -195 yoffset 70
    play music "audio/bgm/BGM44.ogg"
    voice "audio/voice/E3/YUK/01/YI/YI003.ogg"
    yui "Yukinon!"
    hide yui with dissolve
    show yukino school_sunset mid_center happy at center with dissolve:
        xoffset -105 yoffset 75
    hachiman "(Ack. She got us from behind!)"
    show yukino vhappy with dissolve
    voice "audio/voice/E3/YUK/01/YK/YK001.ogg"
    yukino "Do you mind telling me about what I would be mad about if I heard it?"
    voice "audio/voice/E3/YUK/01/YI/YI004.ogg"
    yui "............"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    #Consider making an even darker sunset...
    scene clubroomB
    show yukino school_sunset mid_center pout at left:
        xoffset 25 yoffset 75
    show yui school_sunset mid_center pout at right:
        xoffset -305 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM10.ogg"
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E3/YUK/01/YK/YK002.ogg"
    yukino "...Hayama-kun and I?"
    show yui mid_left at right with dissolve:
        xoffset -270 yoffset 75
    voice "audio/voice/E3/YUK/01/YI/YI005.ogg"
    yui "That time at New Years... It seems someone saw it and misunderstood."
    show yukino sad with dissolve
    voice "audio/voice/E3/YUK/01/YK/YK003.ogg"
    yukino "I see... I did wonder why people were looking at me today. I understand the reason now."
    voice "audio/voice/E3/YUK/01/HA/HA003.ogg"
    hachiman "You hadn't heard about it yet?"
    show yukino pout with dissolve
    voice "audio/voice/E3/YUK/01/YK/YK004.ogg"
    yukino "No. I thought the class was acting different because they were glad to see each other again."
    show yui sad with dissolve
    voice "audio/voice/E3/YUK/01/YI/YI006.ogg"
    yui "Maybe it would have been better if we didn't say anything like Hikki suggested."
    show yukino vhappy with dissolve
    voice "audio/voice/E3/YUK/01/YK/YK005.ogg"
    yukino "No, it's something I would have found out sooner or later. Thank you for letting me know."
    show yui pout1 with dissolve
    voice "audio/voice/E3/YUK/01/YI/YI007.ogg"
    yui "Yukinon..."
    show yui sad with dissolve
    voice "audio/voice/E3/YUK/01/YI/YI008.ogg"
    yui "Everyone's acting up because there hasn't been a specific rumour with Hayato-kun until now. But in this case, whatever you do would probably have the opposite effect so..."
    show yukino sad with dissolve
    voice "audio/voice/E3/YUK/01/YK/YK006.ogg"
    yukino "Yes, I think you're right."
    "That was right. Unfortunately, the only thing we could do was to stay quiet. Those who found this fun would turn every action against us."
    show yukino unimpressed with dissolve
    voice "audio/voice/E3/YUK/01/YK/YK007.ogg"
    yukino "Either way, it's nothing more than low-lives thinking alike."
    voice "audio/voice/E3/YUK/01/YI/YI009.ogg"
    yui "B-but...!"
    show yukino happy with dissolve
    voice "audio/voice/E3/YUK/01/YK/YK008.ogg"
    yukino "It's okay, Yuigahama-san. This isn't as bad as how it used to be either."
    show yui surprised with dissolve
    voice "audio/voice/E3/YUK/01/YI/YI010.ogg"
    yui "Th-this happened before too?!"
    show yukino unimpressed with dissolve
    voice "audio/voice/E3/YUK/01/YK/YK009.ogg"
    yukino "Just from when we were kids. That's why something as mild as this is nothing."
    hachiman "(Even if you say that, there's no way you'd be fine with this...)"
    show yui pout with dissolve
    voice "audio/voice/E3/YUK/01/YI/YI011.ogg" #I've compared and I'm pretty sure this is the correct version (not YI011a.ogg) for Yukino route at least
    yui "But, there are times this kind of thing is stressful..."
    show yui sad with dissolve
    voice "audio/voice/E3/YUK/01/YI/YI012.ogg"
    yui "Always having rumours circulating around you, being stared at all the time, and sometimes having nasty things said about you for you to hear. The people making these rumours might be having fun but..."
    voice "audio/voice/E3/YUK/01/HA/HA004.ogg"
    hachiman "Yeah. To those people this is just entertainment."
    show yukino vhappy with dissolve
    voice "audio/voice/E3/YUK/01/YK/YK010.ogg"
    yukino "That's true, but..."
    "Saying that, Yukinoshita, with a slightly tired expression, smiled suddenly."
    show yukino pout with dissolve
    voice "audio/voice/E3/YUK/01/YK/YK011.ogg"
    yukino "It's not something to be concerned about at this point. I don't mind as long as the people I'm close with understand. That's enough for me."
    show yui pout with dissolve
    voice "audio/voice/E3/YUK/01/YI/YI013.ogg"
    yui "Yukinon..."
    window auto hide dissolve
    stop voice
    #in original general loading screen with live2d yukino
    stop music fadeout 0.5
    call loading_screen(19, "11") from _call_loading_screen_11
    jump E3_CMM_06
    #scene hallwayB with Fade(1.0, 0.5, 1.0)
    #play music "audio/bgm/BGM29.ogg"
    #"While rumours about Hayama and Yukinoshita were circulating around the school, the Service Club received another new request."

label E3_YUK_02:
    hide yui
    hide yukino
    with dissolve
    show yukino school_sunset mid_center pout at left:
        xoffset 25 yoffset 75
    show yui school_sunset mid_center pout at right:
        xoffset -305 yoffset 75
    with dissolve
    voice "audio/voice/E3/YUK/02/HA/HA000.ogg"
    hachiman "Okay, we're done."
    show yukino vhappy with dissolve
    voice "audio/voice/E3/YUK/02/YK/YK000.ogg"
    yukino "Yes, the teachers have arrived too."
    hachiman "(Oh no, I need to go home as soon as I can so I don't get caught by our advisor!)"
    show yui vhappy with dissolve
    voice "audio/voice/E3/YUK/02/YI/YI000.ogg"
    yui "We worked up quite the sweat! Iroha-chan! We'll be going now!"
    voice "audio/voice/E3/YUK/02/IR/IR000.ogg"
    iroha "Ah, thank you to you all! Sorry I can't see you off!"
    "Isshiki, being caught up in detailed instructions, waved a hand from afar."
    hachiman "(What an appropriate greeting...)"
    show yui happy with dissolve
    voice "audio/voice/E3/YUK/02/YI/YI001.ogg"
    yui "Looks like Iroha-chan is still quite busy."
    show yukino happy with dissolve
    voice "audio/voice/E3/YUK/02/YK/YK001.ogg"
    yukino "Isshiki-san has become quite like a Student Council President."
    voice "audio/voice/E3/YUK/02/HA/HA001.ogg"
    hachiman "Yeah true."
    hachiman "(Looking carefully, it looks like most of the workload is divided among the Student Council Members. Well, being able to evenly divide the work is another skill.)"
    voice "audio/voice/E3/YUK/02/HA/HA002.ogg"
    hachiman "Shall we get going?"
    voice "audio/voice/E3/YUK/02/HR/HR000.ogg"
    mystery "Huh? Are you leaving already?"
    stop music fadeout 0.5
    show yukino surprised
    show yui surprised
    with dissolve
    hachiman "(Th-this voice is...)"
    hide yukino
    hide yui
    with dissolve
    show haruno sweater_sunset far_center happy at center with dissolve:
        xoffset -15 yoffset 75
    play music "audio/bgm/BGM35.ogg"
    voice "audio/voice/E3/YUK/02/YK/YK002.ogg"
    yukino "Nee-san..."
    hachiman "(Oh right, this person is a graduate from this school...)"
    show haruno vhappy with dissolve
    voice "audio/voice/E3/YUK/02/HR/HR001.ogg"
    haruno "Hyahello! While you're here, get some advice before you go. Come on, Yukino-chan!"
    hide haruno with dissolve
    show haruno sweater_sunset far_left vhappy at center:
        xoffset 220 yoffset 75
    show yukino school_sunset far_center unimpressed at center:
        xoffset -285 yoffset 75
    with dissolve
    voice "audio/voice/E3/YUK/02/YK/YK003.ogg"
    yukino "No need."
    show haruno happy with dissolve
    voice "audio/voice/E3/YUK/02/HR/HR002.ogg"
    haruno "Then you've already decided on your courses?"
    show yukino annoyed with dissolve
    voice "audio/voice/E3/YUK/02/YK/YK004.ogg"
    yukino "It has nothing to do with you."
    hide yukino
    hide haruno
    with dissolve
    show yui school_sunset near_left pout at center with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E3/YUK/02/YI/YI002.ogg"
    yui "Hikki! Yukinon's been captured!"
    voice "audio/voice/E3/YUK/02/HA/HA003.ogg"
    hachiman "Y-yeah..."
    hide yui with dissolve
    show haruno sweater_sunset far_left sly at center:
        xoffset 220 yoffset 75
    show yukino school_sunset far_center annoyed at center:
        xoffset -285 yoffset 75
    with dissolve
    voice "audio/voice/E3/YUK/02/HR/HR003.ogg"
    haruno "How cold! If you've decided then tell your onee-chan!"
    show yukino angry with dissolve
    voice "audio/voice/E3/YUK/02/YK/YK005.ogg"
    yukino "I said it has nothing to do with you."
    show haruno happy with dissolve
    voice "audio/voice/E3/YUK/02/HR/HR004.ogg"
    haruno "There's no way it doesn't. We're sisters, aren't we?"
    "Her voice was calm. Her gaze was gentle. However, her mouth faintly curved upwards and her dark eyes were so cold it made me shiver."
    show yukino stare with dissolve
    voice "audio/voice/E3/YUK/02/YK/YK006.ogg"
    yukino "...True. We're both our only sister."
    "But, at that time, Yukinoshita was..."
    show yukino vhappy with dissolve
    voice "audio/voice/E3/YUK/02/YK/YK007.ogg"
    yukino "But, Nee-san, that's why I want to properly say myself what I've decided on. Not because I was asked; I'll say it myself independantly."
    show haruno sad with dissolve
    "Saying that, she showed a smile. It was a completely unpretentious smile."
    voice "audio/voice/E3/YUK/02/HR/HR005.ogg"
    haruno "............."
    show haruno happy with dissolve
    voice "audio/voice/E3/YUK/02/HR/HR006.ogg"
    haruno "Okay, then I'll be looking forward to it."
    show yukino happy with dissolve
    voice "audio/voice/E3/YUK/02/YK/YK008.ogg"
    yukino "Yes, please do. I'll see you later."
    hide yukino with dissolve
    hide haruno with dissolve
    show haruno sweater_sunset far_center sly at center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E3/YUK/02/HR/HR007.ogg"
    haruno "............"
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    $totsukaTalkFlag = "yukino"
    jump E3_CMM_07


label E3_YUK_03:
    scene hallwayA with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "After submitting my future courses questionnaire and having a short conversation with Hiratsuka-sensei, I was on my way home."
    window auto hide dissolve
    play sound "audio/sfx/SE04/SE04_01.ogg"
    $renpy.pause(delay=2, hard=False)
    play music "audio/bgm/BGM09.ogg"
    show yukino school mid_left unimpressed at center with dissolve:
        xoffset 50 yoffset 80
    window auto show dissolve
    voice "audio/voice/E3/YUK/03/YK/YK000.ogg"
    yukino "Then, please excuse me."
    show yukino happy with dissolve
    voice "audio/voice/E3/YUK/03/YK/YK001.ogg"
    yukino "Oh?"
    voice "audio/voice/E3/YUK/03/HA/HA000.ogg"
    hachiman "Hey."
    show yukino mid_center with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E3/YUK/03/YK/YK002.ogg"
    yukino "Did you talk to Hiratsuka-sensei about something?"
    voice "audio/voice/E3/YUK/03/HA/HA001.ogg"
    hachiman "A bit about future courses."
    show yukino surprised with dissolve
    voice "audio/voice/E3/YUK/03/YK/YK000.ogg"
    yukino "That's a surprise... In your case, I don't think you have anything to worry about."
    voice "audio/voice/E3/YUK/03/HA/HA002.ogg"
    menu E3_YUK_03_choice:
        hachiman "Pretty much..."
        with dissolve
        "My first choice is in private liberal arts after all":
            "unfinished"
            #voice "audio/voice/E3/YUK/03/HA/HA003.ogg"
            #hachiman "「俺は私立文系一択だしな」" #"My first choice is in private liberal arts after all"
            #yukino "「でしょうね。あなたの成績を考えれば至極現実的な選択ね」" #
            #voice "audio/voice/E3/YUK/03/HA/HA004.ogg"
            #hachiman "「だろ？ 悩む必要ないんだよ」"
            #perhaps jump to yukino_career
            jump E3_YUK_03_choice
        "Either way I'm going to be a full-time househusband":
            "unfinished"
            #hachiman "「どの道最後は専業主夫だ」" #"Either way I'm going to be a full-time househusband"
            #yukino "「そんなことを言っているから平塚先生にお説教されるのよ。もっと現実を見なさい」"
            #hachiman "「違う違う。俺クラスともなると現実と目合わせてても向こうが目を逸らすんだよ」"
            #yukino "「さすがの目力ね。その腐った魚のような目は⋯⋯」"
            #perhaps jump to yukino_career
            jump E3_YUK_03_choice
        "Which did you decide on?":
            jump yukino_career
            #I'm not sure but I think all choices lead here in terms of dialogue so perhaps a label is appropriate here
label yukino_career:
    voice "audio/voice/E3/YUK/03/HA/HA007.ogg"
    hachiman "Which did you decide on?"
    show yukino angry with dissolve
    voice "audio/voice/E3/YUK/03/YK/YK007.ogg"
    yukino "..."
    voice "audio/voice/E3/YUK/03/HA/HA008.ogg"
    hachiman "Eh? What? What's wrong?"
    show yukino happy with dissolve
    voice "audio/voice/E3/YUK/03/YK/YK008.ogg"
    yukino "Ah, no. It was just surprising somehow to be asked that... It's the first time you've asked something like that."
    voice "audio/voice/E3/YUK/03/HA/HA009.ogg"
    hachiman "Really?"
    "Saying that, I continued playing dumb."
    "Up until now, there'd been plenty of opportunities for me to ask something personal, but I had drawn a line that I would never cross."
    "Because I'd thought that would surely be unforgivable."
    show yukino pout with dissolve
    "Like it was hard to say, Yukinoshita cleared her throat and peered into my eyes from an angle."
    show yukino happy with dissolve
    voice "audio/voice/E3/YUK/03/YK/YK009.ogg"
    yukino "I've decided on the liberal arts for now."
    voice "audio/voice/E3/YUK/03/HA/HA010.ogg"
    hachiman "Okay."
    show yukino vhappy with dissolve
    voice "audio/voice/E3/YUK/03/YK/YK010.ogg"
    yukino "Yes, so... everyone's together for now."
    "Yukinoshita smiled as she spoke. A smile like a girl about to go out."
    voice "audio/voice/E3/YUK/03/HA/HA011.ogg"
    hachiman "Well, in terms of the category."
    voice "audio/voice/E3/YUK/03/HA/HA012.ogg"
    hachiman "It doesn't really matter which course either way... What's important is what you do from there."
    show yukino happy with dissolve
    voice "audio/voice/E3/YUK/03/YK/YK011.ogg"
    yukino "Oh, are you reciting what you got from Hiratsuka-sensei?"
    voice "audio/voice/E3/YUK/03/HA/HA013.ogg"
    hachiman "Good intuition... I was told to think about things for ten years on."
    show yukino stare with dissolve
    voice "audio/voice/E3/YUK/03/YK/YK012.ogg"
    yukino "Ten years... That'd be just arond Hiratsuka-sensei's age."
    voice "audio/voice/E3/YUK/03/HA/HA014.ogg"
    hachiman "Yeah. When I become around Hiratsuka-sensei's age..."
    "What Hiratsuka-sensei talked to me about was to keep things long in the future in mind. Long after graduating, further in the future..."
    "I thought about it, but my expectation of the future didn't really add up and my imagination also fell apart."
    voice "audio/voice/E3/YUK/03/HA/HA015.ogg"
    hachiman "What kind of adult would I be..."
    show yukino pout with dissolve
    voice "audio/voice/E3/YUK/03/YK/YK013.ogg"
    yukino "I can't really imagine it."
    voice "audio/voice/E3/YUK/03/HA/HA016.ogg"
    hachiman "For real."
    voice "audio/voice/E3/YUK/03/YK/YK014.ogg"
    yukino "Yes. Especially for you."
    show yukino vhappy with dissolve
    "Yukinoshita smiled as if teasing me. I peered up at the pale colour of the winter sky. There was no way I knew what was waiting for me beyond."
    "That's why I might've just been dreaming of a distant future. I couldn't predict what would happen. But even then..."
    "Which is what I thought so suddenly, just like that."
    window auto hide dissolve
    stop music fadeout 1.0
    #Originally general load with live2D yukino and bgm
    call loading_screen(12,"33") from _call_loading_screen_12
    jump E3_CMM_08

#audio/voice/E3/YUK/04/
#using a stand in sfx for door close.
label E3_YUK_04:
    scene houseA with Fade(1.0, 1.5, 1.0)
    play music "audio/bgm/BGM41.ogg"
    window auto show dissolve
    "I was lounging around on the sofa as always when Komachi came crashing in straight up to my face."
    show komachi athletic near_center vhappy at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E3/YUK/04/KO/KO000.ogg"
    komachi "Onii-chan! Listen to this!"
    play sound "audio/sfx/SE01/SE01_06.ogg" #Not entirely sure which door close effect
    $renpy.pause(delay=0.5,hard=True)
    voice "audio/voice/E3/YUK/04/HA/HA000.ogg"
    hachiman "Y-yeah... What's up?"
    show komachi happy with dissolve
    voice "audio/voice/E3/YUK/04/KO/KO001.ogg"
    komachi "This!"
    voice "audio/voice/E3/YUK/04/HA/HA001.ogg"
    hachiman "What's this? Tickets? \"Famous paintings of cats\", \"The history of cats and humans\", \"The world's cat show\"? It's kinda cat-centered."
    show komachi near_left at center with dissolve:
        xoffset 10 yoffset 65
    voice "audio/voice/E3/YUK/04/KO/KO002.ogg"
    komachi "Yeah. My friend's dad got them from his company, but she's a dog fan. So she gave these to Komachi."
    voice "audio/voice/E3/YUK/04/HA/HA002.ogg"
    hachiman "Oh, so that's how you got them."
    voice "audio/voice/E3/YUK/04/KO/KO003.ogg"
    show komachi vhappy with dissolve
    komachi "Great, right? But, Komachi has entrance exams to study for. So I thought these would be perfect to say thanks to Yukino-san for coming over!"
    voice "audio/voice/E3/YUK/04/HA/HA003.ogg"
    hachiman "As thanks, huh... Good idea."
    show komachi near_center at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E3/YUK/04/KO/KO004.ogg"
    komachi "Right? So which do you think we should give her?"
    voice "audio/voice/E3/YUK/04/HA/HA004.ogg"
    hachiman "Let's see... I reckon she'd jump with joy from any of them... How about giving all of them?"
    hide komachi
    $url = ["komachi athletic near_center sad", "komachi athletic near_center happy"]
    $multiImagePara = [35, 75, 0, 0, 3.0]
    call multiImage() from _call_multiImage_70
    voice "audio/voice/E3/YUK/04/KO/KO005.ogg"
    komachi "Onii-chan, don't think about things half-way. But you're right. Give them all to her! Here!"
    call finishmultiImage from _call_finishmultiImage_74
    show komachi athletic near_center happy at center:
        xoffset 35 yoffset 75
    voice "audio/voice/E3/YUK/04/HA/HA005.ogg"
    hachiman "Yeah, then I'll give them to Yukinoshita for you."
    show komachi near_left at center with dissolve:
        xoffset 10 yoffset 65
    voice "audio/voice/E3/YUK/04/KO/KO006.ogg"
    komachi "Also, I don't really care, but are you free this weekend?"
    voice "audio/voice/E3/YUK/04/HA/HA006.ogg"
    hachiman "If you don't care, then can you not ask? Well, I'm always free as usual."
    show komachi vhappy with dissolve
    voice "audio/voice/E3/YUK/04/KO/KO007.ogg"
    komachi "That's good to hear. Because Komachi just made a promise with Yukino-san over text."
    voice "audio/voice/E3/YUK/04/HA/HA007.ogg"
    hachiman "Okay, good for you... Huh? Wait, what do you mean?"
    show komachi happy with dissolve
    voice "audio/voice/E3/YUK/04/KO/KO008.ogg"
    komachi "So, thanks {i}IS ESCORT{/i}."
    voice "audio/voice/E3/YUK/04/HA/HA008.ogg"
    hachiman "I see, I don't get it."
    show komachi near_center with dissolve
    voice "audio/voice/E3/YUK/04/KO/KO009.ogg"
    komachi "Just giving her tickets feels bad. So, thanks {i}IS ESCORT WITH MY BROTHER{/i}."
    voice "audio/voice/E3/YUK/04/HA/HA009.ogg"
    hachiman "What suspicious English... Are you really a student sitting for an entrance exam?"
    show komachi frown with dissolve
    voice "audio/voice/E3/YUK/04/KO/KO010.ogg"
    komachi "Shaddap, it doesn't matter. Anyway, I'm counting on you, Onii-chan!"
    voice "audio/voice/E3/YUK/04/HA/HA010.ogg"
    hachiman "S-sure..."
    hachiman "(Anyway, I'll just give these to her on the day.)"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    jump E3_YUK_05

#audio/voice/E3/YUK/05/
#currently done: can follow the flow of options shown in AeonArcore's video.
#to do: Minigame other choices that are not shown in AeonArcore's video. TL those choices. Script and voice files pasted in for now.
label E3_YUK_05:
    scene stationA with Fade(0.5, 1.0, 1.0)
    play footsteps "<to 5>audio/sfx/SE00/SE00_07.ogg" fadeout 1
    $renpy.pause(delay=4.5, hard=True)
    play music "audio/bgm/BGM41.ogg"
    show yukino coat mid_center surprised at center with dissolve:
        xoffset -105 yoffset 75
    window auto show dissolve
    voice "audio/voice/E3/YUK/05/YK/YK000.ogg"
    yukino "Oh?"
    voice "audio/voice/E3/YUK/05/HA/HA000.ogg"
    hachiman "Yo."
    show yukino happy with dissolve
    voice "audio/voice/E3/YUK/05/YK/YK001.ogg"
    yukino "Komachi-san... isn't here, is she?"
    voice "audio/voice/E3/YUK/05/HA/HA001.ogg"
    hachiman "\"Go in my stead because I'm studying\" she said. Um... sorry."
    show yukino pout with dissolve
    voice "audio/voice/E3/YUK/05/YK/YK002.ogg"
    yukino "I see... Well she is studying for her entrance exams. It only makes sense."
    voice "audio/voice/E3/YUK/05/HA/HA002.ogg"
    hachiman "Um, yeah. She really feels like she needs to thank you so don't feel bad and go if you want."
    show yukino surprised with dissolve
    voice "audio/voice/E3/YUK/05/YK/YK003.ogg"
    yukino "Right. Then, I'll thankfully take her offer."
    voice "audio/voice/E3/YUK/05/HA/HA003.ogg"
    hachiman "Ok..."
    show yukino pout1 with dissolve
    voice "audio/voice/E3/YUK/05/YK/YK004.ogg"
    yukino "Yes..."
    show yukino pout with dissolve
    voice "audio/voice/E3/YUK/05/HA/HA004.ogg"
    hachiman "..."
    voice "audio/voice/E3/YUK/05/YK/YK005.ogg"
    yukino "..."
    voice "audio/voice/E3/YUK/05/HA/HA005.ogg"
    hachiman "Ah, then..."
    show yukino surprised with dissolve
    voice "audio/voice/E3/YUK/05/YK/YK006.ogg"
    yukino "Y-yes. Then, shall we go?"
    voice "audio/voice/E3/YUK/05/HA/HA006.ogg"
    hachiman "Eh?"
    show yukino blush with dissolve
    voice "audio/voice/E3/YUK/05/YK/YK007.ogg"
    yukino "Eh?"
    voice "audio/voice/E3/YUK/05/HA/HA007.ogg"
    hachiman "Ah no, right... then let's go."
    show yukino avoid with dissolve
    voice "audio/voice/E3/YUK/05/YK/YK008.ogg"
    yukino "S-sure..."
    hachiman "(I'd thought we meant \"then see you later\"...)"
    voice "audio/voice/E3/YUK/05/HA/HA008.ogg"
    hachiman "Ah, about that..."
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    #loading screen into card game with live2D in original
    call card_loading from _card_loadingcat
    scene stationA
    show yukino coat mid_center avoid at center:
        xoffset -105 yoffset 75
    with dissolve
    play music "audio/bgm/BGM31.ogg"
    $card_queue = ["About \ncats in \nthe \nworld", "About \nthe \nhands-on \nexhibition", "About \ncat-\nthemed \nexhibitions", "About \ncat \npaintings", "About \nhistory \nbetween \ncats and \nhumans"]
    $cat_card_count = 0
    $cat_ellipses = 0
    jump yukino_cat_date
    #single footsteps sfx

label not_done_cat:
    "not done"
    $cat_card_count -= 1
    jump yukino_cat_date

label yukino_cat_date:
    if cat_card_count < 3:
        $cat_card_count += 1
        $renpy.pause(delay=0.5, hard=True)
        $ch2 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch2)
        $ch3 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch3)
        window auto hide dissolve
        call screen three_minigame("...", ch2, ch3) with dissolve
        if _return == 1:
            if cat_ellipses == 2:
                $card_queue.append(ch2)
                $card_queue.append(ch3)
                jump not_done_cat
            $card_queue.append(renpy.random.choice([ch2,ch3]))
            if cat_ellipses == 0:
                jump cat_ellipses_card1
            elif cat_ellipses == 1:
                jump cat_ellipses_card2
        elif _return == 2:
            $card_queue.append(ch3)
            if ch2 == "About \ncats in \nthe \nworld":
                jump cats_world
            elif ch2 == "About \nthe \nhands-on \nexhibition":
                jump hands_on_exhibition
            elif ch2 == "About \ncat-\nthemed \nexhibitions":
                $card_queue.append(ch2)
                jump not_done_cat
            elif ch2 == "About \ncat \npaintings":
                $card_queue.append(ch2)
                jump not_done_cat
            elif ch2 == "About \nhistory \nbetween \ncats and \nhumans":
                $card_queue.append(ch2)
                jump not_done_cat
        elif _return == 3:
            $card_queue.append(ch2)
            if ch3 == "About \ncats in \nthe \nworld":
                jump cats_world
            elif ch3 == "About \nthe \nhands-on \nexhibition":
                jump hands_on_exhibition
            elif ch3 == "About \ncat-\nthemed \nexhibitions":
                $card_queue.append(ch3)
                jump not_done_cat
            elif ch3 == "About \ncat \npaintings":
                $card_queue.append(ch3)
                jump not_done_cat
            elif ch3 == "About \nhistory \nbetween \ncats and \nhumans":
                $card_queue.append(ch3)
                jump not_done_cat
    else:
        jump cats_exit2

label hands_on_exhibition:
#Hands on exhibitions here move this to _return == 3　for first set of cards
    window auto show dissolve
    voice "audio/voice/E3/YUK/05/HA/HA024.ogg"
    hachiman "There are things called hands-on exhibitions, right? Do you go to those too?" #「体験型展示ってあるだろ？ ああいうのも見にいったりするのか？」
    show yukino happy with dissolve
    voice "audio/voice/E3/YUK/05/YK/YK026.ogg"
    yukino "By hands-on exhibitions, are you referring to the thing where people try making ceramics at tourist sites?" #「体験型というと⋯⋯観光地などにある陶芸体験のようなものかしら？」
    voice "audio/voice/E3/YUK/05/HA/HA025.ogg"
    hachiman "Sort of I guess. Like 3D projections in science museums, and other stuff you can experience and try touching for instance." #「まあそうだな。他には科学館なんかに多いが、３Ｄ映像や音を体験するとか触ってみるとか」
    hide yukino
    $url = ["yukino coat mid_center surprised", "yukino coat mid_center angry"]
    $multiImagePara = [-105, 75, 0, 0, 1.8]
    call multiImage() from _call_multiImage_71
    voice "audio/voice/E3/YUK/05/YK/YK027.ogg"
    yukino "Try touching... Sure those can also be called exhibitions." #「⋯⋯触ってみる。確かにそれも、体験型と言えなくは無いわね⋯⋯」
    call finishmultiImage from _call_finishmultiImage_75
    show yukino coat mid_center angry at center:
        xoffset -105 yoffset 75
    "Yukinoshita was repeatedly mumbling in a small voice and seemed to understand." #そう言うと、雪ノ下は『触ってみる』としきりに小声で呟いては、何やら納得していた。
    show yukino mid_right blush with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E3/YUK/05/YK/YK028.ogg"
    yukino "Try touching... Cat... Try touching..." #「触ってみる⋯⋯猫⋯⋯触ってみる⋯⋯」
    show yukino unimpressed with dissolve: #nod head
        0.25
        linear 0.25 yoffset 100
        0.1
        linear 0.25 yoffset 75
    $renpy.pause(delay=0.25, hard=True)
    show yukino blush with dissolve
    voice "audio/voice/E3/YUK/05/YK/YK029.ogg"
    yukino "I didn't really have the chance to go before, but it may be fun." #「自分で行くものにはあまり縁がなかったけれど⋯⋯内容によっては楽しいのかもしれないわね」
    voice "audio/voice/E3/YUK/05/HA/HA026.ogg"
    hachiman "I get the feeling it'll depend on what it's about." #「物によりけりな気はするけどな」
    stop voice
    jump yukino_cat_date

label cat_ellipses_card1:
    #from option "..." in 2nd set of cards
    $cat_ellipses = 1
    show yukino coat mid_center happy with dissolve:
        xoffset -105 yoffset 75
    window auto show dissolve
    voice "audio/voice/E3/YUK/05/YK/YK009.ogg"
    yukino "...What is it?" #「⋯⋯何かしら？」
    voice "audio/voice/E3/YUK/05/HA/HA009.ogg"
    hachiman "Uh..." # 「ええと」
    hachiman "(I want to ask which option she wants to go to without minding me... it's surprisingly hard.)" #(どれに行きたいか、気を使わせずに聞きたいんだが⋯⋯案外難しいな)
    voice "audio/voice/E3/YUK/05/YK/YK010.ogg"
    show yukino pout with dissolve
    yukino "If you're not into it, you don't have to mind me..." #「もし、気乗りしないのであれば私のことは気にせず⋯⋯」
    voice "audio/voice/E3/YUK/05/HA/HA010.ogg"
    hachiman "No, that's not it. I'll go, I'll go, I'll definitely go."#「いや、ちがうちがうちがうそうじゃない。行く行く全然行く」
    voice "audio/voice/E3/YUK/05/YK/YK011.ogg"
    show yukino mid_left pout with dissolve:
        xoffset 50 yoffset 80
    yukino "O-okay."#「⋯⋯そ、そう？」
    stop voice
    jump yukino_cat_date

label cat_ellipses_card2:
    $cat_ellipses = 2
    show yukino mid_left happy with dissolve:
        xoffset 50 yoffset 80
    window auto show dissolve
    voice "audio/voice/E3/YUK/05/YK/YK012.ogg"
    yukino "...?"#「⋯⋯？」
    voice "audio/voice/E3/YUK/05/HA/HA011.ogg"
    hachiman "You really love cats don't you."#「⋯⋯お前、本当に猫好きだよな」
    hide yukino
    $url = ["yukino coat mid_left vhappy", "yukino coat mid_left unimpressed"]
    $multiImagePara = [50, 80, 0, 0, 0.75]
    call multiImage() from _call_multiImage_72
    show mood1 at center:
        xoffset 50 yoffset 80
        parallel:
            0.65
            alpha 0
    hide mood2
    show mood2 at center: #nod head
        xoffset 50 yoffset 80 alpha 0
        parallel:
            0.55
            linear 0.1 alpha 1.0
            linear 0.25 yoffset 130
        parallel:
            0.9
            linear 0.5 alpha 0
    show yukino coat mid_center unimpressed at center:
        xoffset -105 yoffset 130 alpha 0
        parallel:
            0.9
            linear 0.5 alpha 1.0
            linear 0.25 yoffset 75
            0.25
            alpha 0
    image yukinoDup = "yukino coat mid_center vhappy"
    show yukinoDup at center:
        xoffset -105 yoffset 75 alpha 0
        parallel:
            1.9
            alpha 1
    voice "audio/voice/E3/YUK/05/YK/YK013.ogg"
    yukino "Yes, well, at least moderately so, to say the least." #「⋯⋯ええ。まぁ、控えめに言ってそれなりに好きではあるわね」
    call finishmultiImage from _call_finishmultiImage_76
    hide yukino
    hide yukinoDup
    show yukino coat mid_center vhappy at center:
        xoffset -105 yoffset 75
    hachiman "(Moderately so, huh..)" #(控えめに言ってそれなのか⋯⋯)
    show yukino happy with dissolve
    voice "audio/voice/E3/YUK/05/YK/YK014.ogg"#head tilt
    yukino "But what about it?" #「でも、それがなにか？」
    voice "audio/voice/E3/YUK/05/HA/HA012.ogg"
    hachiman "Nah, I was just thinking so." #「いや、ふと思ってな」
    voice "audio/voice/E3/YUK/05/YK/YK015.ogg"
    yukino "Is that so." #「⋯⋯そう」
    stop voice
    jump yukino_cat_date

label cat_themed_exhibitions:
    "not done"
    jump yukino_cat_date

label cats_history:
    "not done"
    if cat_card_count == 1:
        jump cat_three_cards_set2
    elif cat_card_count == 2:
        jump cat_three_cards_set3
    jump cats_world

label cat_card_temp: #Put these in proper place. They are in proper order I believe.
#unknown where this is from. Guessing its from ellipses on first or third card sets? These are in correct order though.
    voice "audio/voice/E3/YUK/05/YK/YK016.ogg"
    yukino "" #「⋯⋯何かしら？」
    voice "audio/voice/E3/YUK/05/HA/HA013.ogg"
    hachiman "" #「いや⋯⋯どれに行こうかと思ってな」
    voice "audio/voice/E3/YUK/05/YK/YK017.ogg"
    yukino "" #「⋯⋯『どれに』とは？」
    voice "audio/voice/E3/YUK/05/HA/HA014.ogg"
    hachiman "" #「実は、３種類のチケットを渡されてるんだが、全部回る時間はなさそうでな。しかも会期もそう残ってないから、日を改めてってわけにもいかん。だからある程度絞らないと」
    voice "audio/voice/E3/YUK/05/YK/YK018.ogg"
    yukino "" #「......」
    voice "audio/voice/E3/YUK/05/HA/HA015.ogg"
    hachiman "" #「え、なに、どしたの」
    voice "audio/voice/E3/YUK/05/YK/YK019.ogg"
    yukino "" #「あ、いえ、少し意外だったから」
    voice "audio/voice/E3/YUK/05/HA/HA016.ogg"
    hachiman "" #「は？ なにが？」
    voice "audio/voice/E3/YUK/05/YK/YK020.ogg"
    yukino "" #「あなたが段取りを決めることが」
    voice "audio/voice/E3/YUK/05/HA/HA017.ogg"
    hachiman "" #「ああ、なるほど⋯⋯。あ、いや、なんか勝手に決めてごめんね？
    voice "audio/voice/E3/YUK/05/YK/YK021.ogg"
    yukino "" #「いえ、別に責めたわけではなくて⋯⋯、その、よければあなたに決めてもらってもいいかしら？」
    voice "audio/voice/E3/YUK/05/HA/HA018.ogg"
    hachiman "" #「お、おう⋯⋯。いいの？」
    voice "audio/voice/E3/YUK/05/YK/YK022.ogg"
    yukino "" #「ええ。⋯⋯そ、その、よろしくお願いします」
    voice "audio/voice/E3/YUK/05/HA/HA019.ogg"
    hachiman "" #「は、はい⋯⋯」
    voice "audio/voice/E3/YUK/05/HA/HA020.ogg"
    hachiman "" #「そういや、美術館や博物館って結構行くのか？」
    voice "audio/voice/E3/YUK/05/YK/YK023.ogg"
    yukino "" #「そうね⋯⋯興味がある展示があれば。今はインターネットを通じて、多くのものを見られるようにはなっているけれど、やはり本物を肉眼で見ることは大切だもの」
    voice "audio/voice/E3/YUK/05/HA/HA021.ogg"
    hachiman "" #「やっぱり、違うのか
    voice "audio/voice/E3/YUK/05/YK/YK024.ogg"
    yukino "" #「ええ。データ情報だけで伝わるものはごく僅かよ。写真も同じ。無いよりはましだけれど、その質感や迫力は、実物からしか得られないと思うわ」
    voice "audio/voice/E3/YUK/05/HA/HA022.ogg"
    hachiman "" #「まあ、言われてみればそうかもな」
    voice "audio/voice/E3/YUK/05/YK/YK025.ogg"
    yukino "" #「そうね⋯⋯一例をあげると、猫の画像からでは、その触感や躍動感、生命力のごく限られた一面だけしか伝わらない、といったところかしら」
    voice "audio/voice/E3/YUK/05/HA/HA023.ogg"
    hachiman "" #「⋯⋯なるほど」
    hachiman "()" #(とりあえず、雪ノ下が猫を物凄く好きなことはよく再認識できた)

#about cat themed exhibitions I think. These are in correct order.
    hachiman "" #「猫がテーマの展示って、どんなものなら興味ある？」
    voice "audio/voice/E3/YUK/05/YK/YK030.ogg"
    yukino "" #「猫⋯⋯そうね。正直なところ、どんなものでも興味深いのだけれど⋯⋯」
    voice "audio/voice/E3/YUK/05/YK/YK031.ogg"
    yukino "" #「その⋯⋯もしかして、猫、の展示⋯⋯なのかしら？」
    hachiman "()" #(雪ノ下さん？ 何だか息が上がってません？)
    voice "audio/voice/E3/YUK/05/HA/HA028.ogg"
    hachiman "" #「ああ⋯⋯まあな」
    voice "audio/voice/E3/YUK/05/YK/YK032.ogg"
    yukino "" #「そう。それは楽しみね」
    voice "audio/voice/E3/YUK/05/HA/HA029.ogg"
    hachiman "" #「お前、猫がテーマなら、絵も好きだったりするのか？」
    voice "audio/voice/E3/YUK/05/YK/YK033.ogg"
    yukino "" #「絵画を鑑賞するのは好きだけれど⋯⋯そうね。猫が描かれていると、心和むものがあるわね」
    voice "audio/voice/E3/YUK/05/HA/HA030.ogg"
    hachiman "" #「そうか。なら、今日は和み放題だな」
    voice "audio/voice/E3/YUK/05/YK/YK034.ogg"
    yukino "" #「⋯⋯！ まさか⋯⋯」
    voice "audio/voice/E3/YUK/05/HA/HA031.ogg"
    hachiman "" #「ご明察」
    voice "audio/voice/E3/YUK/05/YK/YK035.ogg"
    yukino "" #「猫が描かれた絵画の展示⋯⋯！ そんな企画展もあるのね⋯⋯気づかなかったわ⋯⋯」
    voice "audio/voice/E3/YUK/05/HA/HA032.ogg"
    hachiman "" #「いや⋯⋯まあ、企画展なんて美術館の数だけやってるからな」
    voice "audio/voice/E3/YUK/05/YK/YK036.ogg"
    yukino "" #「そ、それもそうね⋯⋯」
    voice "audio/voice/E3/YUK/05/HA/HA033.ogg"
    hachiman "" #「猫好きっていうのは、猫と人間との歴史にも興味を持ったりするのか？」
    voice "audio/voice/E3/YUK/05/YK/YK037.ogg"
    yukino "" #「人それぞれじゃないかしら。ただひたすら、目の前の猫だけに関心を注ぐ人も少なくないと思うし⋯⋯」
    "placeholder" #ちなみに、そう言う雪ノ下の表情は、こころなしかうっとりしているようだった。いや、間違いなくうっとりしていた。
    voice "audio/voice/E3/YUK/05/YK/YK038.ogg"
    yukino "" #「けれど、猫と人間との歴史⋯⋯それはとても奥深いテーマね。目の前の猫との個人的な歴史をまず考える人もいるでしょうし⋯⋯」
    voice "audio/voice/E3/YUK/05/YK/YK039.ogg"
    yukino "" #「もしくは、猫と人類が共に歩んできた歴史そのものを考えることもできるわ。しかも文化圏によって、当然事情は異なってくるだろうから⋯⋯」
    voice "audio/voice/E3/YUK/05/YK/YK040.ogg"
    yukino "" #「⋯⋯そう、比企谷くん。そうした本が何冊か出版されているのは知っている？」
    voice "audio/voice/E3/YUK/05/HA/HA034.ogg"
    hachiman "" #「そういえば、あったような。読んだことはないが⋯⋯」
    voice "audio/voice/E3/YUK/05/YK/YK041.ogg"
    yukino "" #「ぜひ、一読をお勧めするわ。有名なところでは古代エジプトにおける、太陽神ラーを象徴する動物としての崇拝から始まり、新王朝時代でのハトホル神、そして第２２王朝での⋯⋯こほん」
    voice "audio/voice/E3/YUK/05/HA/HA035.ogg"
    hachiman "" #「それだけ詳しけりゃ、観にいく必要はないかもな。ちなみに『人類と猫の歴史』っていう大きく構えたやつなんだが」
    voice "audio/voice/E3/YUK/05/YK/YK042.ogg"
    yukino "" #「⋯⋯！ いいえ。機会を見て、行こうと思っていた展示よ」
    voice "audio/voice/E3/YUK/05/HA/HA036.ogg"
    hachiman "" #「そうか。ならちょうど良かったな」
    voice "audio/voice/E3/YUK/05/YK/YK043.ogg"
    yukino "" #「ええ。忙しさにかまけて見逃してしまうことも多いもの。小町さんには感謝しなくてはね」

label cats_world: #this card actually an exit card in the scene normally.
    #from 3rd set of cards
#from option "About cat's in the world" from 3rd set of cards in video
    window auto show dissolve
    voice "audio/voice/E3/YUK/05/HA/HA037.ogg"
    hachiman "By the way, what cats do you like?" #「そういえば雪ノ下は、どんな猫が好きなんだ？」
    show yukino mid_right happy with dissolve: #Ahh more head-tilt in the Live2D. too precious.
        xoffset 25 yoffset 75
    voice "audio/voice/E3/YUK/05/YK/YK044.ogg"
    yukino "Even if you ask me that, there are no standards with cats. Every cat is different and every single one is great." #「どんな猫と言われても⋯⋯。猫に貴賎はないわ。どの猫もみんな違ってみんないいわ」
    voice "audio/voice/E3/YUK/05/HA/HA038.ogg"
    hachiman "O-okay... That's a strong belief... But, that may just be perfect." #「お、おう⋯⋯力強いな⋯⋯。けど、それならちょうどいいかもな」
    show yukino mid_center blush with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E3/YUK/05/YK/YK045.ogg"
    yukino "Wh-what do you mean?" #「ど⋯⋯どういう意味、なのかしら？」
    voice "audio/voice/E3/YUK/05/HA/HA039.ogg"
    hachiman "Komachi's ticket includes a hands-on exhibition called, \"Let's play with the cats in the world\". Anyways, it seems there'll be lots of different cat breeds." #「小町のチケットが、『世界の猫とあそぼう』っていう体験型企画展でな。とにかくいろんな品種の猫がいるっぽい」
    show yukino avoid with dissolve
    voice "audio/voice/E3/YUK/05/YK/YK046.ogg"
    yukino "Cats in the world.... Play..." #「⋯⋯世界の猫⋯⋯遊ぼう⋯⋯」
    hachiman "(Hello are you there, Yukinoshita-san?)" #(もしもーし、雪ノ下さーん)
    # if cat_card_count == 1:
    #     jump cat_three_cards_set2
    # elif cat_card_count == 2:
    #     jump cat_three_cards_set3
    # elif cat_card_count == 3:
    jump cats_exit

label cats_exit: #from 3rd set of cards, option cats in the world at least
    show yukino unimpressed with dissolve: #nod head
        0.25
        linear 0.25 yoffset 100
        0.1
        linear 0.25 yoffset 75
    $renpy.pause(delay=0.25, hard=True)
    show yukino angry with dissolve
    window auto show dissolve
    voice "audio/voice/E3/YUK/05/YK/YK048.ogg"
    yukino "Then shall we get going? We've got the chance to see cats... No, we'll have less time to see the exhibition." #「では⋯⋯そろそろ行きましょうか。せっかくの猫が⋯⋯いえ、せっかくの展示を見る時間が少なくなってしまうわ」
    hachiman "(Yukinoshita-san, your eyes are sparkling, you know?)" #(雪ノ下さん、目の輝きが尋常じゃないんですけど？)
    voice "audio/voice/E3/YUK/05/HA/HA040.ogg"
    hachiman "True."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    jump E3_YUK_08

#not done animations
label cats_exit2: #not sure how to get here...
#assuming these are the conversation enders for different chard choice orders.
    show yukino coat mid_center frown at center with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E3/YUK/05/YK/YK047.ogg"
    yukino "We have been standing around for a while talking... So let's get going... We're wasting time." #「立ち話もこれくらいにして⋯⋯そろそろ行きましょうか。⋯⋯時間も無駄にしてしまうし」
    voice "audio/voice/E3/YUK/05/HA/HA041.ogg"
    hachiman "Oh, yeah." #「ああ、そうだな」
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    jump E3_YUK_08

#need indoor crowd sfx
#need separate cat sfx
#audio/voice/E3/YUK/08/
label E3_YUK_08:
    scene black with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM44.ogg"
    $renpy.pause(delay=1.3, hard=True)
    play sound "audio/sfx/SE07/SE07_02a.ogg"
    $renpy.pause(delay=1.3, hard=True)
    play sound "audio/sfx/SE07/SE07_02b.ogg"
    $renpy.pause(delay=1.3, hard=True)
    play sound "audio/sfx/SE07/SE07_02c.ogg"
    $renpy.pause(delay=2, hard=True)
    play ambient "audio/sfx/SE05/SE05_01L.ogg"
    window auto show dissolve
    voice "audio/voice/E3/YUK/08/YK/YK000.ogg"
    yukino "..."
    "As soon as we reached the place where the cat show was happening, Yukinoshita Yukino was..."
    voice "audio/voice/E3/YUK/08/YK/YK001.ogg"
    yukino "..."
    "It's just, she lost touch with everything around her."
    voice "audio/voice/E3/YUK/08/HA/HA000.ogg"
    hachiman "Hey..."
    voice "audio/voice/E3/YUK/08/YK/YK002.ogg"
    yukino "..."
    voice "audio/voice/E3/YUK/08/HA/HA001.ogg"
    hachiman "Heeyy..."
    voice "audio/voice/E3/YUK/08/YK/YK003.ogg"
    yukino "Nyaa~"
    hachiman "(Let's pretend I didn't hear anything... This is also kindness...)"
    voice "audio/voice/E3/YUK/08/HA/HA002.ogg"
    hachiman "U-um, Yukinoshita... I think you can touch them. The cats."
    voice "audio/voice/E3/YUK/08/YK/YK004.ogg"
    yukino "Eh?! Sure..."
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    play music "audio/bgm/BGM41.ogg"
    scene parkB
    show yukinocatsceneA
    with Fade(0.0, 0.5, 2.0)
    window auto show dissolve
    voice "audio/voice/E3/YUK/08/YK/YK005.ogg"
    yukino "S-so fluffy... As expected of an Angora..."
    voice "audio/voice/E3/YUK/08/HA/HA003.ogg"
    hachiman "It's hair loss is going to be amazing."
    voice "audio/voice/E3/YUK/08/XR/XR000.ogg"
    fs "This type of cat will be happy if you give it a good brush. It's a bit troubling that you have to brush it everyday, but it'll prevent hair from going everywhere and it'll be communication with the cat too."
    voice "audio/voice/E3/YUK/08/YK/YK006.ogg"
    yukino "Communication with the cat..."
    voice "audio/voice/E3/YUK/08/XR/XR001.ogg"
    fs "Also, if you'll keep it with your boyfriend, then caring for it together can be some peaceful time for the two of you and up your love level.."
    hachiman "(HA!?)"
    voice "audio/voice/E3/YUK/08/YK/YK007.ogg"
    yukino "Th-that's...!"
    voice "audio/voice/E3/YUK/08/XR/XR002.ogg"
    fs "Ah, about that cat..."
    voice "audio/voice/E3/YUK/08/YK/YK008.ogg"
    yukino "U-um..."
    voice "audio/voice/E3/YUK/08/HA/HA004.ogg"
    hachiman "S-sorry..."
    voice "audio/voice/E3/YUK/08/YK/YK009.ogg"
    yukino "N-no... it's not really your fault."
    "Looking around, this place was actually full of couples. Well, I don't think she was talking seriously anyway."
    voice "audio/voice/E3/YUK/08/YK/YK010.ogg"
    yukino "U-um... this one is an Abyssinian. It's face really is small... !"
    "The cat had jumped over Yukinoshita's shoulder and took hold of her back."
    voice "audio/voice/E3/YUK/08/HA/HA005.ogg"
    hachiman "Woah, are you alright?"
    voice "audio/voice/E3/YUK/08/YK/YK011.ogg"
    yukino "Yes. It's a lively one. This cat is a LaPerm breed I think."
    voice "audio/voice/E3/YUK/08/HA/HA006.ogg"
    hachiman "It's got rather curly hair."
    voice "audio/voice/E3/YUK/08/YK/YK012.ogg"
    yukino "The curly hair came from a mutation and it became a dominant trait in long-haired species like this one. They're very friendly with people."
    voice "audio/voice/E3/YUK/08/HA/HA007.ogg"
    hachiman "You're well informed..."
    voice "audio/voice/E3/YUK/08/YK/YK013.ogg"
    yukino "Not really. A cat's world is just very profound."
    voice "audio/voice/E3/YUK/08/WD/WD000.ogg"
    cat "Meow-"
    voice "audio/voice/E3/YUK/08/YK/YK014.ogg"
    hide yukinocatsceneA
    show yukinocatsceneB
    with dissolve
    yukino "Good cat... Good kitty good kitty... Nya. Nya-nya."
    hachiman "(Her face looks completely infatuated... Just how much do you like cats?)"
    voice "audio/voice/E3/YUK/08/WD/WD001.ogg"
    cat "Meow~ {i}gorogoro{/i}"
    voice "audio/voice/E3/YUK/08/YK/YK015.ogg"
    yukino "gorogoro~ Nya-..."
    hachiman "(We haven't been moving along for a while now... But, whatever.)"
    hachiman "(Her face rarely becomes this natural as well...)"
    window auto hide dissolve
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    hide yukinocatsceneB
    show yukino coat_sunset mid_left pout at center:
        xoffset 50 yoffset 80
    with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM42.ogg"
    window auto show dissolve
    voice "audio/voice/E3/YUK/08/YK/YK016.ogg"
    yukino "Sorry it took so long..."
    voice "audio/voice/E3/YUK/08/HA/HA008.ogg"
    hachiman "So you say, but you look like you haven't had enough."
    show yukino blush with dissolve
    voice "audio/voice/E3/YUK/08/YK/YK017.ogg"
    yukino "D-does it?"
    voice "audio/voice/E3/YUK/08/HA/HA009.ogg"
    hachiman "Why don't you just keep one?"
    show yukino pout with dissolve
    voice "audio/voice/E3/YUK/08/YK/YK018.ogg"
    yukino "That would have been nice. But I can't since I live alone."
    voice "audio/voice/E3/YUK/08/HA/HA010.ogg"
    hachiman "I don't think that's much of a concern since cats are pretty self-serving animals, unlike dogs."
    voice "audio/voice/E3/YUK/08/HA/HA011.ogg"
    hachiman "They just lie around the house wherever they want and sleep. They don't concern themselves much with people. Rather than saying they're free, they're more audacious."
    show yukino vhappy with dissolve
    voice "audio/voice/E3/YUK/08/YK/YK019.ogg"
    yukino "Sounds just like a certain someone."
    show yukino mid_center avoid with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E3/YUK/08/YK/YK020.ogg"
    yukino "No, um..."
    voice "audio/voice/E3/YUK/08/HA/HA012.ogg"
    hachiman "Well yeah..."
    show yukino vhappy with dissolve
    voice "audio/voice/E3/YUK/08/YK/YK021.ogg"
    yukino "..."
    "Suddenly smiling, Yukinoshita looked up at the darkening winter sky as if she was chasing after something with her eyes."
    voice "audio/voice/E3/YUK/08/YK/YK022.ogg"
    yukino "True... Rather than \"keeping\", it's just living together I suppose."
    voice "audio/voice/E3/YUK/08/HA/HA013.ogg"
    hachiman "Maybe. They probably don't realise when they're being loved either."
    show yukino concerned with dissolve
    voice "audio/voice/E3/YUK/08/YK/YK023.ogg"
    yukino "Yes... I admire them a little..."
    window auto hide dissolve
    stop voice
    scene skyB with dissolve
    window auto show dissolve
    voice "audio/voice/E3/YUK/08/YK/YK024.ogg"
    yukino "Not depending on others... Being able to live in the same space as if it was a given..."
    "Those words weren't directed towards cats. I realised that. If that was the case, I would also agree with every fibre of my being."
    hachiman "(Only if that kind of relationship existed in this world, that is.)"
    voice "audio/voice/E3/YUK/08/HA/HA014.ogg"
    hachiman "Well, it's not a bad feeling."
    voice "audio/voice/E3/YUK/08/YK/YK025.ogg"
    yukino "Indeed..."
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    call loading_screen(20,"11") from _call_loading_screen_1
    jump E3_YUK_09

label E3_YUK_09:
    scene clubroomB with Fade(1.0, 0.5, 1.0)
    play sound "audio/sfx/SE04/SE04_01.ogg"
    $renpy.pause(delay=3, hard=False)
    show yukino school_sunset mid_left happy at center with dissolve:
        xoffset 50 yoffset 80
    play music "audio/bgm/BGM09.ogg"
    window auto show dissolve
    voice "audio/voice/E3/YUK/09/YK/YK000.ogg"
    yukino "Oh."
    voice "audio/voice/E3/YUK/09/HA/HA000.ogg"
    hachiman "Yo."
    show yukino unimpressed with dissolve
    voice "audio/voice/E3/YUK/09/YK/YK001.ogg"
    yukino "I thought you were Yuigahama-san."
    voice "audio/voice/E3/YUK/09/HA/HA001.ogg"
    hachiman "Sorry it's me. Yuigahama was caught by Miura in the classroom."
    show yukino vhappy with dissolve
    voice "audio/voice/E3/YUK/09/YK/YK002.ogg"
    yukino "I see. That's a pity."
    hide yukino with dissolve
    play sound "audio/sfx/SE01/SE01_22.ogg"
    "While saying that, Yukinoshita poured me a cup of black tea as per the usual."
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_21.ogg"
    $renpy.pause(delay=1.0, hard=True)
    show yukino school_sunset mid_left vhappy at center with dissolve:
        xoffset 50 yoffset 80
    window auto hide dissolve
    voice "audio/voice/E3/YUK/09/YK/YK003.ogg"
    yukino "Here you go."
    voice "audio/voice/E3/YUK/09/HA/HA002.ogg"
    hachiman "Thank you."
    window auto hide dissolve
    scene skyB with dissolve
    window auto show dissolve
    voice "audio/voice/E3/YUK/09/YK/YK004.ogg"
    yukino "A bunch of things have finally settled down."
    voice "audio/voice/E3/YUK/09/HA/HA003.ogg"
    hachiman "Yeah."
    "The alleged rumours about Hayama Hayato and Yukinoshita Yukino. It got sorted out in one go at the Marathon Tournament and the school became quiet as can be."
    "I reckon humans are like cash. They're a pain to listen to and it's purely delightful when those unwanted sounds subside. More importantly, Yukinoshita looks very relieved it's over."
    voice "audio/voice/E3/YUK/09/YK/YK005.ogg"
    yukino "Hikigaya-kun, thank you... You've ended up helping me again this time too."
    voice "audio/voice/E3/YUK/09/HA/HA004.ogg"
    hachiman "Nah, like I said I didn't do anything. The people around me just did what they did best. This is hindsight."
    voice "audio/voice/E3/YUK/09/YK/YK006.ogg"
    yukino "No... You did help me. You always have..."
    "That concluding tone of voice reminded me of the feeling of loneliness, and I subconciously looked at Yukinoshita. Doing so, Yukinoshita, with an affectionate expression, looked outside the window."
    "In those eyes was something far away. Not in the meaning they were just reflecting the sky and scenery, but they were such a deep blue looking at something vastly different."
    window auto hide dissolve
    scene clubroomB with dissolve
    window auto show dissolve
    voice "audio/voice/E3/YUK/09/HA/HA005.ogg"
    hachiman "I didn't really help you... I just did it mostly because I don't like it being so noisy and stuffy."
    voice "audio/voice/E3/YUK/09/HA/HA006.ogg"
    hachiman "Also, this kind of... I don't quite dislike this, um, peaceful time. So well... you don't have to think about this any further."
    show yukino school_sunset mid_left happy at center with dissolve:
        xoffset 50 yoffset 80
    voice "audio/voice/E3/YUK/09/YK/YK007.ogg"
    yukino "I see... Then that's the same as me. I don't dislike this peaceful time either."
    voice "audio/voice/E3/YUK/09/HA/HA007.ogg"
    hachiman "Right?"
    show yukino vhappy with dissolve
    voice "audio/voice/E3/YUK/09/YK/YK008.ogg"
    yukino "Yes."
    # hide window, then play door sliding sfx and hide yukino concurrently
    window auto hide dissolve
    play sound "audio/sfx/SE04/SE04_01.ogg"
    $renpy.pause(delay=1.0, hard=False)
    hide yukino with dissolve
    $renpy.pause(delay=2.0, hard=False)
    stop sound
    hide yukino with dissolve
    window auto show dissolve
    voice "audio/voice/E3/YUK/09/YI/YI000.ogg"
    yui "Yahallo! Sorry I'm late! Jeez, I was just listening to Yumiko and Hayato-kun talking about a bunch of things and I was really surprised at how fast time flies!"
    show yui school_sunset near_right vhappy at left:
        xoffset -280 yoffset 75
    show yukino school_sunset mid_left happy at right:
        xoffset -165 yoffset 80
    with dissolve
    voice "audio/voice/E3/YUK/09/HA/HA008.ogg"
    hachiman "O-oh, okay..."
    show yukino vhappy with dissolve
    voice "audio/voice/E3/YUK/09/YK/YK009.ogg"
    yukino "I don't dislike this kind of time either."
    voice "audio/voice/E3/YUK/09/HA/HA009.ogg"
    hachiman "Yeah. Right."
    show yui school_sunset near_center surprised at left with dissolve: #not sure if I should define a school_sunset near layered images
        xoffset 135 yoffset 75
    voice "audio/voice/E3/YUK/09/YI/YI001.ogg"
    yui "Eh? What is it?"
    voice "audio/voice/E3/YUK/09/YK/YK010.ogg"
    yukino "It's nothing. Here's your tea."
    hide yui with dissolve
    show yui school_sunset mid_right vhappy at left with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E3/YUK/09/YI/YI002.ogg" #not sure when 002a is played
    yui "Ah, thanks! Drinking the tea you make really calms you down..."
    window auto hide dissolve
    stop voice
    scene skyB with dissolve
    window auto hide dissolve
    "And so, the Service Club regained its usual peaceful boredness... Or at least it should have."
    window auto hide dissolve
    stop voice
    #general loading screen in original.
    call loading_screen from _call_loading_screen_13
    jump E4_CMM_01
