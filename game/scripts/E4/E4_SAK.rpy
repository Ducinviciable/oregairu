label E4_SAK_01:
    scene black with fade
    play footsteps "audio/sfx/SE00/SE00_30L.ogg"
    scene houseCA with Fade(1.0, 0.5, 1.0)
    $renpy.pause(delay=0.5,hard=True)
    stop footsteps fadeout 0.5
    show komachi athletic mid_center happy at center with dissolve:
        xoffset -75 yoffset 75
    play music "audio/bgm/BGM08.ogg"
    $renpy.pause(delay=1.0,hard=True)
    window auto show dissolve
    voice "audio/voice/E4/SAK/01/HA/HA000.ogg"
    hachiman "Oh, Komachi."
    show komachi pout with dissolve
    voice "audio/voice/E4/SAK/01/KO/KO000.ogg"
    komachi "Hmmm? Onii-chan, you'll catch a cold if you keep lounging around like that."
    hide komachi with dissolve
    play sound "audio/sfx/SE01/SE01_73.ogg"
    "After dinner, as I was lazily reading on the couch, Komachi came into the living room and started rumaging around the kitchen."
    stop sound fadeout 0.5
    show komachi athletic near_center happy at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E4/SAK/01/KO/KO001.ogg"
    komachi "Onii-chan, take this."
    voice "audio/voice/E4/SAK/01/HA/HA001.ogg"
    hachiman "Oh, thank you. Hot!--"
    "The can that Komachi gave me was so hot that it startled me when I took it barehanded."
    hachiman "(She must have warmed up the cans in hot water.)"
    "If you think of it as a hot can, it's warm and comfortable from the start."
    play sound "audio/sfx/SE01/SE01_76.ogg"
    $renpy.pause(delay=0.75,hard=True)
    show komachi vhappy with dissolve
    stop sound
    voice "audio/voice/E4/SAK/01/KO/KO002.ogg"
    komachi "Cheers."
    voice "audio/voice/E4/SAK/01/HA/HA002.ogg"
    hachiman "Yeah, cheers."
    show komachi athletic near_left vhappy at center with dissolve:
        xoffset 10 yoffset 65
    voice "audio/voice/E4/SAK/01/MI/MIX000.ogg"
    hachiandkom "............"
    show komachi blush with dissolve
    voice "audio/voice/E4/SAK/01/KO/KO004.ogg"
    komachi "Ahhhhhh..."
    voice "audio/voice/E4/SAK/01/HA/HA004.ogg"
    hachiman "It warms you up, doesn't it?"
    show komachi happy with dissolve
    voice "audio/voice/E4/SAK/01/KO/KO005.ogg"
    komachi "Yeah, it's soothing to my tired brain!"
    voice "audio/voice/E4/SAK/01/HA/HA005.ogg"
    hachiman "Don't work too hard. Exams are coming up, and it'd be bad for you to break down just before that."
    show komachi athletic near_center pout at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E4/SAK/01/KO/KO006.ogg"
    komachi "Uh, onii-chan gave me a reality check..."
    "She must have accepted her fate. But her voice wasn't as depressed as before."
    voice "audio/voice/E4/SAK/01/HA/HA006.ogg"
    hachiman "Speaking of reality, do you know what day it is today?"
    show komachi happy with dissolve
    voice "audio/voice/E4/SAK/01/KO/KO007.ogg"
    komachi "Oh. So that's that."
    voice "audio/voice/E4/SAK/01/HA/HA007.ogg"
    hachiman "What? I told you it's almost Valentine's Day..."
    show komachi vhappy with dissolve
    voice "audio/voice/E4/SAK/01/KO/KO008.ogg"
    komachi "Yeah, so this is it. I don't have time this year, so I'll give you something like that."
    "Komachi points to the can of hot chocolate in my hand."
    voice "audio/voice/E4/SAK/01/HA/HA008.ogg"
    hachiman "No, I don't mean this kind of chocolate, but a real one... Anyway, give me some chocolate. Give me chocolate from Komachi, or Komachoco for short."
    show komachi pout with dissolve
    voice "audio/voice/E4/SAK/01/KO/KO009.ogg"
    komachi "What is Komachoco? And you wouldn't appreciate it if I gave it to you after you asked me to give it to you."
    hachiman "(Well, Valentine's Day is the day of the entrance exam this year, so I shouldn't expect much... I wanted a Komachoco, though...)"
    show komachi unimpressed with dissolve
    voice "audio/voice/E4/SAK/01/KO/KO010.ogg"
    komachi "............"
    show komachi athletic near_left unimpressed at center with dissolve:
        xoffset 10 yoffset 65
    voice "audio/voice/E4/SAK/01/KO/KO011.ogg"
    komachi "Onii-chan. More importantly, I'm hungry and anxious, so come with me to the convenience store."
    voice "audio/voice/E4/SAK/01/HA/HA009.ogg"
    hachiman "Okay, but..."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    scene skyC
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "When we arrived at the nearby convenience store, Komachi said she was going to take a look around the store, so I went to the magazine section and waited."
    "Eventually, Komachi comes to pick me up with a convenience store bag full of snacks, saying, \"Thanks for waiting\"."
    play sound "audio/sfx/SE04/SE04_18.ogg"
    "I can't find anything to buy, so we just left the convinience store together. It was a little change of pace."
    stop sound fadeout 0.5
    window auto hide dissolve
    # need to shade this for night
    scene neighborhoodC
    play music "audio/bgm/BGM42.ogg"
    show komachi coat_night mid_center surprised at center with dissolve:
        xoffset -75 yoffset 75
    window auto show dissolve
    voice "audio/voice/E4/SAK/01/KO/KO012.ogg"
    komachi "Woah, it's so cold outside~. And the stars are a~mazing."
    voice "audio/voice/E4/SAK/01/HA/HA010.ogg"
    hachiman "Feel a little better now?"
    show komachi coat_night mid_left vhappy at center with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E4/SAK/01/KO/KO013.ogg"
    komachi "Yeah. I really have to go out at least once a day."
    "Komachi laughs as she lets out a puffy white breath."
    voice "audio/voice/E4/SAK/01/HA/HA011.ogg"
    hachiman "It's nice to have a change of pace, but let's go home before we catch a cold."
    show komachi frown with dissolve
    voice "audio/voice/E4/SAK/01/KO/KO014.ogg"
    komachi "...Mhm."
    show komachi coat_night mid_center frown at center with dissolve:
        xoffset -75 yoffset 75
    "As if to reply to me, Komachi takes something out of the convenience store bag and thrusts it my way with a grimace on her face."
    voice "audio/voice/E4/SAK/01/KO/KO015.ogg"
    komachi "I bought it in the store and you asked me to give you some."
    "It's chocolate. It's the pre-wrapped kind from the convenience store, but it's chocolate nonetheless."
    voice "audio/voice/E4/SAK/01/HA/HA012.ogg"
    hachiman "Komachi~~~"
    show komachi blush with dissolve
    voice "audio/voice/E4/SAK/01/KO/KO016.ogg"
    komachi "I was actually planning on getting it tomorrow, but you said you wanted some before I could."
    voice "audio/voice/E4/SAK/01/HA/HA013.ogg"
    hachiman "I mean, you can give me chocolate as many times as you want."
    show komachi unimpressed with dissolve
    voice "audio/voice/E4/SAK/01/KO/KO017.ogg"
    komachi "You only get Komachi's chocolate once a year. Be thankful for it."
    voice "audio/voice/E4/SAK/01/HA/HA014.ogg"
    hachiman "Thank you...thank you so much. And you even went out of your way to buy it for me, disguised as wanting a change of pace..."
    show komachi coat_night mid_left frown at center with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E4/SAK/01/KO/KO018.ogg"
    komachi "No, I really just wanted to go out, and that was just an afterthought."
    show komachi pout with dissolve
    voice "audio/voice/E4/SAK/01/KO/KO019.ogg"
    komachi "But I wish you had someone else besides me to push such selfish requests on."
    voice "audio/voice/E4/SAK/01/HA/HA015.ogg"
    hachiman "I wouldn't dare say anything so embarassing to anyone other than you."
    show komachi unimpressed with dissolve
    voice "audio/voice/E4/SAK/01/KO/KO020.ogg"
    komachi "You're such a trash can, Trashnii-chan."
    hide komachi with dissolve
    show komachi coat_night near_left happy at center with dissolve:
        xoffset 275 yoffset 65
    "Even as she says this, Komachi gently slips her hand into mine."
    window auto hide dissolve
    scene komachiWalka with Dissolve(1.0)
    window auto show dissolve
    voice "audio/voice/E4/SAK/01/KO/KO021.ogg"
    komachi "But you know what? Thanks to winter break, I'll be able to take the exam just fine."
    voice "audio/voice/E4/SAK/01/HA/HA016.ogg"
    hachiman "I see."
    hachiman "(I wonder if they talk like this at Kawasaki's house, too.)"
    "It suddenly occurs to me."
    voice "audio/voice/E4/SAK/01/KO/KO022.ogg"
    komachi "I'm sure they're having this same conversation at Taishi-kun's place too."
    voice "audio/voice/E4/SAK/01/HA/HA017.ogg"
    hachiman "Probably."
    "When I answered that, Komachi showed a mischievous smile."
    show komachiWalkb with dissolve
    voice "audio/voice/E4/SAK/01/KO/KO023.ogg"
    komachi "This coming spring, you'll be a senior in the Service Club."
    voice "audio/voice/E4/SAK/01/HA/HA018.ogg"
    hachiman "No, I don't even know if there will be one, and I might be retired from club activities in the third year. I'm gonna be the one taking the exam this time. I don't know how that will pan out."
    voice "audio/voice/E4/SAK/01/KO/KO024.ogg"
    komachi "Eh~? Why would you say that?"
    "I tried to gloss it over in my mind, but the spring and my third year were just around the corner, even if they still seemed so far away."
    hide komachiWalkb with dissolve
    voice "audio/voice/E4/SAK/01/HA/HA019.ogg"
    hachiman "Well, anyway... Komachi, I'll be waiting for you in that high school."
    voice "audio/voice/E4/SAK/01/KO/KO025.ogg"
    komachi "Yup."
    window auto hide dissolve
    stop music
    call loading_screen(4, "33") from _call_komachi_coat_loading
    jump E4_CMM_02

label E4_SAK_02:
    play ambient "audio/sfx/SE05/SE05_02L.ogg"
    window auto show dissolve
    hachiman "(Haa, the empty boxes are mostly cleared out, and I'm starting to feel like one myself.)"
    #Seems to branch here. Should have some logic to jump to kawasaki route since the scripts say the default is still E4/CMM/02.
    "I finished my preparations and took a breather."
    play music "audio/bgm/BGM17.ogg"
    show keika heavy_coat far happy at center with dissolve:
        xoffset 5 yoffset 70
    voice "audio/voice/E4/SAK/02/KE/KE000.ogg"
    keika "Ah, it's Haa-chan!"
    hide keika with dissolve
    show keika heavy_coat mid happy at center with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E4/SAK/02/HA/HA000.ogg"
    hachiman "Ohh, if it isn't Kei-chan."
    show yui school mid_left happy behind keika at center with dissolve:
        xoffset 295 yoffset 75
    voice "audio/voice/E4/SAK/02/YI/YI000.ogg"
    yui "Keika-chan, long time no see! Ehehe~"
    show keika annoyed with dissolve
    "Yuigahama strokes Keika's head, but Keika's reaction was not so good."
    voice "audio/voice/E4/SAK/02/KE/KE001.ogg"
    keika "Long time no see...?"
    show yui pout with dissolve
    hachiman "(Doesn't she remember Yuigahama?)"
    show yukino school mid_center happy at left with dissolve:
        xoffset -105 yoffset 75
    voice "audio/voice/E4/SAK/02/YK/YK000.ogg"
    yukino "Yuigahama-san. I wonder if she's forgotten about you already?"
    show yui surprised with dissolve
    voice "audio/voice/E4/SAK/02/YI/YI001.ogg"
    yui "Eh!? She forgot about me!?"
    voice "audio/voice/E4/SAK/02/HA/HA001.ogg"
    hachiman "Kei-chan, didn't you meet last Christmas?"
    show keika sad with dissolve
    voice "audio/voice/E4/SAK/02/KE/KE002.ogg"
    keika "Ah..."
    image yuiFlatLeft = Flatten("yui school mid_left pout")
    image yuiFlatRight = Flatten("yui school mid_right pout")
    show yuiFlatLeft behind keika at center with dissolve:
        xoffset 295 yoffset 75
        parallel:
            4.52
            linear 0.15 alpha 0
        parallel:
            4.52
            easein 0.15 xoffset 175
    show yuiFlatRight behind keika at left:
        xoffset 260 yoffset 75 alpha 0
        parallel:
            4.45
            linear 0.15 alpha 1.0
        parallel:
            4.45
            easein 0.15 xoffset 140
        parallel:
            5.0
            alpha 0
    show yui school mid_right pout behind keika at left:
        xoffset 140 yoffset 75 alpha 0
        parallel:
            5.0
            alpha 1.0
    voice "audio/voice/E4/SAK/02/YI/YI002.ogg"
    yui "Um, you've met us already! I'm Yui, Keika-chan! And this is Yukinon!"
    hide yuiFlatRight
    hide yuiFlatLeft
    hide yui
    show yui school mid_right pout behind keika at left:
        xoffset 140 yoffset 75
    show keika annoyed with dissolve
    voice "audio/voice/E4/SAK/02/KE/KE003.ogg"
    keika "Yui? Yukinon?"
    hide keika
    hide yui
    hide yukino
    with dissolve
    $renpy.pause(delay=0.5, hard=True)
    show saki school mid_left pout flat at center:
        xoffset 200 yoffset 75 alpha 0
        on show:
            parallel:
                linear 0.6 alpha 1
            parallel:
                easein 0.6 xoffset 65
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E4/SAK/02/SA/SA000.ogg"
    saki "Ah, I'm sorry about Keika."
    "Kawasaki hurried over and took Keika's hand embarassed. Before we know it, our eyes met."
    show saki school mid_left blush with dissolve
    voice "audio/voice/E4/SAK/02/SA/SA001.ogg"
    saki "Um, thanks... for today."
    voice "audio/voice/E4/SAK/02/HA/HA002.ogg"
    hachiman "Sure... good luck today."
    hachiman "(Her greeting just now... felt very delicate for some reason?)"
    hide saki with dissolve
    $renpy.pause(delay=0.25, hard=True)
    show keika heavy_coat mid happy at left:
        xoffset 440 yoffset 75
    show saki school mid_right pout behind keika at left:
        xoffset -55 yoffset 75
    show yukino school mid_left happy at right:
        xoffset -170 yoffset 80
    with dissolve
    "While I was having that thought, she left to greet Yukinoshita and the others. Keika looks at her older sister with great interest."
    voice "audio/voice/E4/SAK/02/SA/SA002.ogg"
    saki "...I'll be in your care."
    show keika vhappy with dissolve
    voice "audio/voice/E4/SAK/02/KE/KE004.ogg"
    keika "Please take care of me, too!"
    show yukino vhappy with dissolve
    voice "audio/voice/E4/SAK/02/YK/YK001.ogg"
    yukino "Yes, you're welcome. So, what kind of sweets shall we make?"
    stop voice
    hide saki
    hide keika
    hide yukino
    with dissolve
    show keika heavy_coat near happy at center with dissolve:
        xoffset -30 yoffset 75
    voice "audio/voice/E4/SAK/02/SA/SA003.ogg"
    saki "Kei-chan, what kind of sweets do you want to eat?"
    voice "audio/voice/E4/SAK/02/YI/YI003.ogg"
    yui "Ah, I also want to know!"
    show keika vhappy with dissolve
    voice "audio/voice/E4/SAK/02/KE/KE005.ogg"
    keika "Eel!"
    voice "audio/voice/E4/SAK/02/YI/YI004.ogg"
    yui "Huh?"
    voice "audio/voice/E4/SAK/02/HA/HA003.ogg"
    hachiman "O-Oh, well..."
    hide keika with dissolve
    $renpy.pause(delay=0.25, hard=True)
    show keika heavy_coat mid vhappy at left:
        xoffset 440 yoffset 75
    show saki school mid_right blush behind keika at left:
        xoffset -55 yoffset 75
    show yukino school mid_left happy at right:
        xoffset -170 yoffset 80
    with dissolve
    voice "audio/voice/E4/SAK/02/SA/SA004.ogg"
    saki "Sorry about that. My family ate Eel the other day, and she liked it a lot."
    show yukino angry with dissolve
    voice "audio/voice/E4/SAK/02/YK/YK002.ogg"
    yukino "Eel... Hmm... In that case--"
    voice "audio/voice/E4/SAK/02/HA/HA004.ogg"
    hachiman "Kei-chan, those aren't sweets, okay?"
    hide keika
    $url = ["keika heavy_coat mid surprised", "keika heavy_coat mid vhappy"]
    $multiImagePara = [440, 75, 0, 0, 0.8]
    call multiImage(-1) from _call_multiImage_5
    voice "audio/voice/E4/SAK/02/KE/KE006.ogg"
    keika "Ehh? Okay, Keika will make sweets! Chocolate!"
    call finishmultiImage from _call_finishmultiImage_5
    show keika heavy_coat mid vhappy at left:
        xoffset 440 yoffset 75
    voice "audio/voice/E4/SAK/02/SA/SA005.ogg"
    saki "I want you to teach her... anything is fine, as long as a child can make it."
    hide yukino
    $url = ["yukino school mid_left happy", "yukino school mid_center happy"]
    call setImagesFlat from _call_setImagesFlat
    show mood1 at right:
        xoffset -170 yoffset 80
    with dissolve
    show mood1 at right:
        xoffset -170 yoffset 80
        parallel:
            5.0
            linear 0.5 alpha 0
    show mood2 at right:
        xoffset -235 yoffset 75 alpha 0
        parallel:
            5.0
            linear 0.5 alpha 1.0
    voice "audio/voice/E4/SAK/02/YK/YK003.ogg"
    yukino "I understand. Maybe chocolate truffles will do...? I'll go and get some additional ingredients."
    show mood2 at right:
        xoffset -235 yoffset 75
        parallel:
            linear .5 alpha 0
        parallel:
            linear .5 xoffset -175
    $renpy.pause(delay=0.5, hard=True)
    call finishmultiImage from _call_finishmultiImage_6
    with None
    hide saki
    hide keika
    with dissolve
    show yui school mid_center angry at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E4/SAK/02/YI/YI005.ogg"
    yui "Oh, chocolate truffles? I wonder if I can make some, too..."
    hide yui with dissolve
    show saki school near_right surprised at left:
        xoffset -205 yoffset 75
    show keika heavy_coat near happy at center:
        xoffset -30 yoffset 75
    with dissolve
    voice "audio/voice/E4/SAK/02/HA/HA005.ogg"
    hachiman "Hm?"
    "I don't know what she was thinking, but Keika took my hand. Grasping both my hand and Kawasaki's, Keika made a proud declaration."
    show keika vhappy with dissolve
    voice "audio/voice/E4/SAK/02/KE/KE007.ogg"
    keika "Haa-chan, Keika will do her best making chocolate! Once I'm done, I'll give it to you!"
    voice "audio/voice/E4/SAK/02/HA/HA006.ogg"
    hachiman "Sure, I'm looking forward to it!"
    show keika happy with dissolve
    voice "audio/voice/E4/SAK/02/KE/KE008.ogg"
    keika "Yay, right, Saa-chan?"
    show saki blush with dissolve
    voice "audio/voice/E4/SAK/02/SA/SA006.ogg"
    saki "Umm... Y...Yeah."
    hide saki
    hide keika
    with dissolve
    show yui school mid_center happy at left:
        xoffset 255 yoffset 75
    show iroha school mid_center happy at right:
        xoffset -315 yoffset 75
    with dissolve
    voice "audio/voice/E4/SAK/02/IR/IR000.ogg"
    iroha "You're quite popular with little kids aren't you, Senpai. That's surprising."
    show yui vhappy with dissolve
    voice "audio/voice/E4/SAK/02/YI/YI006.ogg"
    yui "Hikki, you're like an onii-chan. She's become attached so to you. So cute!"
    hide iroha
    hide yui
    with dissolve
    show keika heavy_coat near happy at center with dissolve:
        xoffset -30 yoffset 75
    voice "audio/voice/E4/SAK/02/KE/KE009.ogg"
    keika "Not an onii-chan! Haa-chan will be Keika's papa!"
    voice "audio/voice/E4/SAK/02/MI/MIX000.ogg"
    yuiandiro "P-PAPA!?\nP-Papahaha?!"
    hachiman "(S-She's still going on about that!?)"
    voice "audio/voice/E4/SAK/02/SA/SA007.ogg"
    saki "K-Kei-chan!"
    voice "audio/voice/E4/SAK/02/KE/KE010.ogg"
    show keika vhappy
    keika "Right, Haa-chan?"
    voice "audio/voice/E4/SAK/02/IR/IR002.ogg"
    iroha "I'm surprised she's so fond of you, senpai. It's bizzare."
    hachiman "(I find it quite strange myself...)"
    window auto hide dissolve
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    #new scene here. Alternatively, jump to E4_CMM_03 for different translation and slightly different positions.
    jump E4_CMM_03

label E4_SAK_03:
    scene kitchenA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM14.ogg"
    show saki school mid_right vhappy at center:
        xoffset -355 yoffset 75
    show keika home mid vhappy at center:
        xoffset 215 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E4/SAK/03/HA/HA000.ogg"
    hachiman "Yo, Kei-chan."
    show saki surprised with dissolve
    voice "audio/voice/E4/SAK/03/SA/SA000.ogg"
    saki "Huh?! H-Hikigaya--"
    "When I called out to Keika, Kawasaki jumped and turned around before Keika did."
    hachiman "(Why's she so frightened of me whenever we come into contact!?)"
    voice "audio/voice/E4/SAK/03/KE/KE000.ogg"
    keika "Ah, Haa-chan!"
    "With a little chocolate on her cheek, Keika smiles and greets me."
    voice "audio/voice/E4/SAK/03/HA/HA001.ogg"
    hachiman "Kei-chan, you've got chocolate on your face."
    "When I wiped the chocolate with my fingers, Keika giggled and laughed as if she was tickled."
    voice "audio/voice/E4/SAK/03/KE/KE001.ogg"
    keika "Haa-chan, that tickles!"
    hachiman "(I-I feel like I've done something I shouldn't have.)"
    show saki vhappy with dissolve
    voice "audio/voice/E4/SAK/03/SA/SA001.ogg"
    saki "............"
    voice "audio/voice/E4/SAK/03/SA/SA002.ogg"
    saki "I think it's about ready by now... I'll be back in a moment."
    voice "audio/voice/E4/SAK/03/HA/HA002.ogg"
    hachiman "Okay. Oh, I'll leave you something from Hiratsuka-sensei."
    voice "audio/voice/E4/SAK/03/SA/SA003.ogg"
    saki "Got it."
    hide saki
    hide keika
    with dissolve
    "While the Kawasaki sisters were looking for something in the fridge, I looked around the venue."
    window auto hide dissolve
    image iroha school mid_left vhappy flat = Flatten("iroha school mid_left vhappy")
    scene kitchenA at truecenter:
        zoom 1.45 xalign 0 yoffset -15
    show hayama school mid_center happy at left:
        xoffset 35 yoffset 75
    show yumiko school mid_center happy at center behind hayama:
        xoffset -5 yoffset 75
    with dissolve
    show iroha school mid_left vhappy flat at right with dissolve:
        xoffset -50 yoffset 65 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.5 xoffset -190
    $renpy.pause(delay=0.5, hard=True)
    hide iroha
    show iroha school mid_left vhappy at right:
        xoffset -190 yoffset 65
    window auto show dissolve
    voice "audio/voice/E4/SAK/03/IR/IR000.ogg"
    iroha "Hayama-senpai, try this!"
    show yumiko frown with dissolve
    voice "audio/voice/E4/SAK/03/YM/YM000.ogg"
    yumiko "Hey... I'm still talking to..."
    voice "audio/voice/E4/SAK/03/HY/HY000.ogg"
    hayama "It looks like you two are doing well. I'll eat them in turn."
    show iroha angry
    show yumiko annoyed
    with dissolve
    voice "audio/voice/E4/SAK/03/YM/YM001.ogg"
    yumiko "............"
    voice "audio/voice/E4/SAK/03/IR/IR001.ogg"
    iroha "............"
    hachiman "(...He looks like he's in trouble too. Well, I don't think he doesn't deserve it, but it's still scary.)"
    window auto hide dissolve
    scene kitchenA at truecenter:
        zoom 1.45 xoffset -2.5 yoffset -12.5
    show yukino school mid_center annoyed at left:
        xoffset -105 yoffset 75
    show yui school mid_center sad at center:
        xoffset -25 yoffset 75
    show haruno sweater mid_center happy at right:
        xoffset -170 yoffset 75
    with Dissolve(1.0)
    window auto hide dissolve
    voice "audio/voice/E4/SAK/03/YK/YK000.ogg"
    yukino "Nee-san, you can go back."
    show haruno sweater mid_left happy at right with dissolve:
        xoffset -110 yoffset 75
    voice "audio/voice/E4/SAK/03/HR/HR000.ogg"
    haruno "Yukino-chan, you're so cold. Don't you have to make your own sweets too, Yukino-chan? Time's almost up."
    show yui school mid_left sad at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E4/SAK/03/YI/YI000.ogg"
    yui "Yukinon, really, I made you spend all this effort on me..."
    show yukino vhappy with dissolve
    voice "audio/voice/E4/SAK/03/YK/YK001.ogg"
    yukino "No. It's not your fault, Yuigahama-san."
    show haruno sly with dissolve
    voice "audio/voice/E4/SAK/03/HR/HR001.ogg"
    haruno "Yes, that's right. Yukino-chan should be able to easily make her own while taking care of Gahama-chan."
    show yukino annoyed with dissolve
    voice "audio/voice/E4/SAK/03/YK/YK002.ogg"
    yukino "............"
    show yui school mid_center sad at center with dissolve:
        xoffset -25 yoffset 75
    hachiman "(It's heartbraking to always see those two sisters bickering back and forth...)"
    window auto hide dissolve
    scene kitchenA at truecenter:
        zoom 1.45 xalign 1.0 yoffset -15
    show totsuka athletic mid_right happy at center:
        xoffset -10 yoffset 85
    show tobe school mid vhappy at left:
        xoffset 10 yoffset 75
    show ebina school mid_center happy at right:
        xoffset 5 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E4/SAK/03/TB/TB000.ogg"
    tobe "Oh. Ebina-san, that's awesome! How did you make something like this!"
    show totsuka vhappy with dissolve
    voice "audio/voice/E4/SAK/03/SI/SI000.ogg"
    totsuka "Yeah... that was awesome! Looks delicious..."
    show ebina school mid_left vhappy at right with dissolve:
        xoffset -190 yoffset 70
    voice "audio/voice/E4/SAK/03/EB/EB000.ogg"
    ebina "Thank you! Totsuka-kun, would you like to try it?"
    voice "audio/voice/E4/SAK/03/SI/SI001.ogg"
    totsuka "Are you sure? Thank you!"
    show tobe surprised with dissolve
    voice "audio/voice/E4/SAK/03/TB/TB001.ogg"
    tobe "Ah! Ah! Me too! Me too!"
    show ebina annoyed with dissolve
    voice "audio/voice/E4/SAK/03/EB/EB001.ogg"
    ebina "Umm... If there's any left, I suppose?"
    show totsuka athletic mid_center pout at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E4/SAK/03/SI/SI002.ogg"
    totsuka "Oh, To-Tobe-kun, do you want half?"
    show tobe happy with dissolve
    voice "audio/voice/E4/SAK/03/TB/TB003.ogg"
    tobe "...Yeah!"
    show tobe worried with dissolve
    voice "audio/voice/E4/SAK/03/TB/TB002.ogg"
    tobe"Yeah..."
    hachiman "(Tobe's in trouble too...)"
    hide totsuka
    hide ebina
    hide tobe
    with dissolve
    "...There's a small tug on my sleeve."
    window auto hide dissolve
    scene kitchenA
    show keika home mid happy at center:
        xoffset -25 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E4/SAK/03/KE/KE002.ogg"
    keika "Haa-chan, this is for you!"
    "I looked over and saw Keika proudly holding out a small plate of beautifully arranged truffle chocolates. It's quite beautiful to look at."
    voice "audio/voice/E4/SAK/03/HA/HA003.ogg"
    hachiman "Oh? Kei-chan, you're pretty good at this. Well done!"
    hachiman "(This area's different from the rest, so much more relaxing here...)"
    show keika vhappy with dissolve
    voice "audio/voice/E4/SAK/03/KE/KE003.ogg"
    keika "Try it!"
    voice "audio/voice/E4/SAK/03/HA/HA004.ogg"
    hachiman "Okay, don't mind if I do!"
    "As soon as you put it in your mouth, the chunks of chocolate crumble and melt in your mouth, spreading a moderate sweetness with a milk flavor."
    voice "audio/voice/E4/SAK/03/HA/HA005.ogg"
    hachiman "Oh? It's delicious!"
    hide keika with dissolve
    show saki school mid_right happy at center:
        xoffset -355 yoffset 75
    show keika home mid vhappy at center:
        xoffset 215 yoffset 75
    with dissolve
    voice "audio/voice/E4/SAK/03/SA/SA004.ogg"
    saki "We based it on a milk chocolate intended for kids, so... the taste may be a little sweet though..."
    voice "audio/voice/E4/SAK/03/HA/HA006.ogg"
    hachiman "No, I like the flavor just right. Can I have one more?"
    show saki vhappy with dissolve
    voice "audio/voice/E4/SAK/03/SA/SA005.ogg"
    saki "Yeah. She wants to give it to you, so you have it all if you want."
    voice "audio/voice/E4/SAK/03/HA/HA007.ogg"
    hachiman "I see. Thanks a lot, Kei-chan."
    voice "audio/voice/E4/SAK/03/KE/KE004.ogg"
    keika "You're welcome!"
    hachiman "(Well, I'll take her on her word then and take one more...)"
    show saki blush with dissolve
    voice "audio/voice/E4/SAK/03/SA/SA006.ogg"
    saki "T-The ones I've made might be mixed in there."
    voice "audio/voice/E4/SAK/03/HA/HA008.ogg"
    hachiman "Is that so... I can't even tell who made which. Your sister's amazing... she may possibly be as good as you in cooking."
    voice "audio/voice/E4/SAK/03/SA/SA007.ogg"
    saki "I-I wonder about that..."
    voice "audio/voice/E4/SAK/03/HA/HA009.ogg"
    hachiman "I mean it looks beautiful in terms of appearance, and it's delicious to boot."
    "I took another one and enjoyed the chocolate as it melted in my mouth."
    hachiman "(It's really not the same as the ones sold in supermarkets, which are about a 100 yen a pop.)"
    "I nodded to myself, savoring the texture."
    show saki vhappy with dissolve
    voice "audio/voice/E4/SAK/03/KE/KE005.ogg"
    keika "Since Keika gave chocos to Haa-chan, does that Keika Haa-chan's bride?"
    voice "audio/voice/E4/SAK/03/HA/HA010.ogg"
    hachiman "Eh?"
    show saki surprised with dissolve
    voice "audio/voice/E4/SAK/03/SA/SA008.ogg"
    saki "Ahh--I'm sorry about Keika! H-Hey now, Kei-chan!"
    voice "audio/voice/E4/SAK/03/HA/HA011.ogg"
    hachiman "No, it's okay. Kei-chan, it's not good to choose your groom by way of chocolate, you know?"
    hide saki
    hide keika
    with dissolve
    show keika home near frown at center with dissolve:
        yoffset 75
    "I stifled Kawasaki's restlessness and stroked Keika's hair. Keika face, however, turned grim for some reason. "
    voice "audio/voice/E4/SAK/03/KE/KE006.ogg"
    keika "But the nursery said if I gave someone chocos, I'll be a bride!"
    hachiman "(You don't seem to know what that means. You're still a girl though, albeit a small one...)"
    "Feeling moved, I looked up."
    window auto hide dissolve
    scene kitchenA at truecenter:
        zoom 1.45 xoffset -2.5 yoffset -12.5
    show yui school mid_center unimpressed at left:
        xoffset 130 yoffset 75
    show yukino school mid_center stare at center behind yui:
        xoffset -105 yoffset 75
    show iroha school mid_center unimpressed at right:
        xoffset -190 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E4/SAK/03/MI/MIX000.ogg"
    yukandyuiandiro "............"
    hachiman "(Hey, stop that. What's with this suffocating silence?)"
    window auto hide dissolve
    scene kitchenA
    with dissolve
    window auto show dissolve
    "I stepped back to get away from this unsettling atmosphere. And then, a small but tight hug around my waist."
    voice "audio/voice/E4/SAK/03/HA/HA012.ogg"
    hachiman "Huh?"
    show keika home near frown at center with dissolve:
        yoffset 75
    voice "audio/voice/E4/SAK/03/KE/KE007.ogg"
    keika "............"
    hachiman "(You want me to stay? What a sweetheart.)"
    "I pat her on the head."
    hide keika with dissolve
    show saki school mid_right unimpressed at center with dissolve:
        xoffset -115 yoffset 75
    voice "audio/voice/E4/SAK/03/SA/SA009.ogg"
    saki "............"
    show saki vhappy with dissolve
    "Kawasaki let out a chuckle, trying to contain her laughter."
    window auto hide dissolve
    stop music fadeout 1.0
    jump E4_CMM_05

label E4_SAK_04:
    scene parkB with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM18.ogg"
    window auto show dissolve
    "Keika was clinging to me tightly as we left the venue."
    show saki school_light_sunset mid_right vhappy at center with dissolve:
        xoffset -115 yoffset 75
    voice "audio/voice/E4/SAK/04/SA/SA000.ogg"
    saki "I'm sorry for bothering you until the end."
    voice "audio/voice/E4/SAK/04/HA/HA000.ogg"
    hachiman "It's alright, want me to walk you to the station?"
    voice "audio/voice/E4/SAK/04/SA/SA001.ogg"
    saki "It's fine, we take this route all the time. Beside, you still have things to do, right?"
    hide saki with dissolve
    show saki school_light_sunset mid_right vhappy at center:
        xoffset -180 yoffset 75
    show keika home_sunset mid happy at center:
        xoffset 35 yoffset 75
    with dissolve
    "Kawasaki put her sack and grocery bag back on her back and, with a sigh, squatted down to pick up Keika."
    show saki blush with dissolve
    voice "audio/voice/E4/SAK/04/SA/SA002.ogg"
    saki "Hey... Thank you so much for today."
    voice "audio/voice/E4/SAK/04/HA/HA001.ogg"
    hachiman "Not at all, the chocolate was great."
    voice "audio/voice/E4/SAK/04/SA/SA003.ogg"
    saki "I'm-I'm glad you liked them then. Right, Kei-chan?"
    show keika vhappy with dissolve
    voice "audio/voice/E4/SAK/04/KE/KE000.ogg"
    keika "Yeah!"
    "Seeing sisters like them really is heartwarming."
    show saki vhappy
    show keika happy
    with dissolve
    voice "audio/voice/E4/SAK/04/KE/KE001.ogg"
    keika "Then, then--"
    show keika vhappy with dissolve
    voice "audio/voice/E4/SAK/04/KE/KE002.ogg"
    keika "Haa-chan, bye bye! See you later!"
    voice "audio/voice/E4/SAK/04/HA/HA002.ogg"
    hachiman "Take care on your way back, okay?"
    hide keika
    hide saki
    with dissolve
    "As I waved back at Keika, who kept waving until I couldn't see her anymore, I suddenly felt as if I was missing her. I wondered if this was how I would feel if I were to give my away daughter in marriage."
    "Since I don't have a daughter, what if Komachi were married off? No, that would be unacceptable under any circumstances. Absolutely not."
    window auto hide dissolve
    scene skyB with Dissolve(1.0)
    window auto show dissolve
    "Tomorrow is finally the day of Komachi's exam. \"Do your best\", I muttered to the empty winter sky."
    hachiman "(When I get back, I'm gonna make something nice and warm to eat.)"
    voice "audio/voice/E4/SAK/04/HA/HA003.ogg"
    hachiman "Achoo!"
    "Realizing that the cold was seeping into my body, I returned home from the venue. The chocolate tasting event was finally over."
    window auto hide dissolve
    stop music fadeout 1.0
    jump E5_CMM_01