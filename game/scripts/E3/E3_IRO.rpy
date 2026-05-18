label E3_IRO_01:
    "Lying on the desk makes it uncomfortable to rest, I was trying to shift my posture when something in the corridor caught my eye."
    "Near the door, there's some one I know who was jumping in her spot, looking for attention."
    stop music fadeout 0.5
    hachiman "(What is she doing here?)"
    hachiman "(She suddenly glances at me)"
    show iroha school far_left angry at left with dissolve:
        xoffset 215 yoffset 80
    voice "audio/voice/E3/IRO/01/IR/IR000.ogg"
    iroha "......!"
    play music ["<silence 0.3>","audio/bgm/BGM44.ogg"]
    show iroha school far_center angry at left with dissolve:
        xoffset 210 yoffset 75
    show iroha:
        parallel:
            linear 0.1 yoffset 45
            pause 0.08
            linear 0.1 yoffset 75
            pause 0.08
            repeat 5
    voice "audio/voice/E3/IRO/01/IR/IR001.ogg"
    iroha "...., ....!"
    hachiman "(Those gestures... she's asking me to come over. But that's embarrasing...)"
    hide iroha with dissolve
    show iroha school mid_center angry at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E3/IRO/01/HA/HA000.ogg"
    hachiman "What is your case?"
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/01/IR/IR002.ogg"
    iroha "I was just wanted to see what was going down. Though I should probably ask Hayama-senpai in person..."
    voice "audio/voice/E3/IRO/01/HA/HA001.ogg"
    hachiman "Want me to call him?"
    show iroha pout with dissolve
    voice "audio/voice/E3/IRO/01/IR/IR003.ogg"
    iroha "Um... No, actually you'll do. Can you come over for a second?"
    window auto hide dissolve
    stop music fadeout 0.5
    $renpy.pause(delay=0.5, hard=True)
    play sound ["<silence 0.5>", "audio/sfx/SE04/SE04_00.ogg"]
    scene black with CropMove(0.5, mode="wipeleft")
    $renpy.pause(delay=0.2, hard=True)
    scene hallwayA with dissolve
    play music ["<silence 0.3>","audio/bgm/BGM36.ogg"]
    show iroha school mid_center pout at center with dissolve:
        xoffset -5 yoffset 75
    window auto show dissolve
    voice "audio/voice/E3/IRO/01/HA/HA002.ogg"
    hachiman "...So, you were on the lookout?"
    voice "audio/voice/E3/IRO/01/IR/IR004.ogg"
    iroha "There's a rumour circulating around, right? I just wanted to know what it was about..."
    voice "audio/voice/E3/IRO/01/HA/HA007.ogg"
    hachiman "They were probably together because of their families then somebody saw that and things resulted in the rumour."
    voice "audio/voice/E3/IRO/01/IR/IR008.ogg"
    iroha "Oh, so that's what it's about... If it's just a family thing, then there's nothing to worry about. It's pretty much an anti-development..."
    hachiman "(I was actually there too, but... I guess I don't have to tell her that.)"
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/01/IR/IR009.ogg"
    iroha "So that's all. Got it. I'll get going then~"
    hide iroha with dissolve
    "After looking at Isshiki quickly walking away, I returned to the classroom."
    window auto hide dissolve
    stop music fadeout 0.5
    call loading_screen(filename="02_09") from general_loading_iroha_school #school bell sfx required
    jump E3_IRO_02

label E3_IRO_02:
    scene hallwayB with fade
    window auto show dissolve
    voice "audio/voice/E3/IRO/02/IR/IR000.ogg"
    mystery "Ah, Senpa~i!"
    play music ["<silence 0.3>","audio/bgm/BGM36.ogg"]
    show iroha school_sunset far_center happy at center with dissolve:
        xoffset -30 yoffset 75
    "I heard a familiar voice, so I turned towards it, and Isshiki was there."
    voice "audio/voice/E3/IRO/02/HA/HA000.ogg"
    hachiman "............"
    hide iroha with dissolve
    voice "audio/voice/E3/IRO/02/IR/IR001.ogg"
    iroha "Huh? Senpai! Hey, senpai~!!"
    window auto hide dissolve
    stop voice
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE00/SE00_28.ogg"
    $renpy.pause(delay=1.0, hard=True)
    show iroha school_sunset mid_left frown at center with dissolve:
        xoffset -35 yoffset 65
    window auto show dissolve
    voice "audio/voice/E3/IRO/02/IR/IR002.ogg"
    iroha "I got your hand! Geez, why didn't you wait for me? You saw me, didn't you?"
    voice "audio/voice/E3/IRO/02/HA/HA001.ogg"
    hachiman "Well, I wasn't sure if you were calling for me. You do have a lot of senpai(s) after all."
    show iroha school_sunset mid_center frown at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E3/IRO/02/IR/IR003.ogg"
    iroha "Please get this through your mind already. There's no other senpai I can boss arou- Sorry, I misspoke. I can summon- no, that doesn't sound right. Only one I can be so friendly with, senpai!"
    voice "audio/voice/E3/IRO/02/HA/HA002.ogg"
    hachiman "Ah, is that right? So, what's up?"
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/02/IR/IR004.ogg"
    iroha "You know, I wanted to go on the offensive with Hayama-senpai again and I wanted to think one up together. You helped me with those before, remember?"
    voice "audio/voice/E3/IRO/02/HA/HA003.ogg"
    hachiman "...Did I now?"
    voice "audio/voice/E3/IRO/02/IR/IR005.ogg"
    iroha "Geez~ Did you forget, senpai?"
    show iroha vhappy with dissolve
    voice "audio/voice/E3/IRO/02/IR/IR006.ogg"
    iroha "So how about we meet tomorrow at 10 am at Chiba station?"
    menu iroha_date_menu:
        with dissolve
        hachiman "(Hmm, what should I do?)"
        "I'll go.":
            voice "audio/voice/E3/IRO/02/HA/HA004.ogg"
            hachiman "Alright. Tomorrow at 10am?"
            show iroha surprised with dissolve
            voice "audio/voice/E3/IRO/02/IR/IR007.ogg"
            iroha "Huh?"
            voice "audio/voice/E3/IRO/02/HA/HA005.ogg"
            hachiman "Ah?"
            show iroha blush with dissolve
            voice "audio/voice/E3/IRO/02/IR/IR008.ogg"
            iroha "N-No... I was just a little surprised."
            show iroha school_sunset mid_left vhappy at center with dissolve:
                xoffset -35 yoffset 65
            voice "audio/voice/E3/IRO/02/IR/IR009.ogg"
            iroha "Okay, I'll be counting on you tomorrow! I'm looking forward to seeing senpai hard at work! See ya!"
            hide iroha with dissolve
            hachiman "(Hm, I don't think I could've said no either way. Rather than wasting my time trying to, might as well get it over with.)"
            hachiman "(The problem lies with my wallet, though...)"
            window auto hide dissolve
            stop music fadeout 0.5
            jump E3_IRO_03
        "I'll refuse.":
            "not done"
            jump iroha_date_menu

label E3_IRO_03:
    scene stationA with Fade(1.0, 1.0, 1.0)
    play ambient "audio/sfx/SE05/SE05_05L.ogg"
    window auto show dissolve
    "I looked at all the passersby and confirmed again that it's already 5 past 10."
    "I thought that this would be the best spot to meet in front of Chiba station, but as I waited, stomping my feet to ward of freezing to death, I saw Isshiki's figure in the crowd."
    hide iroha
    $url = ["iroha coat far_left happy", "iroha coat far_center vhappy"]
    $multiImagePara = [5, 80, 5, 75, 1.5]
    call multiImage(0,False) from _call_multiImage_87
    voice "audio/voice/E3/IRO/03/IR/IR000.ogg"
    iroha "...... ......!"
    call finishmultiImage from _call_finishmultiImage_91
    with dissolve
    "When Isshiki noticed me, she came running over, fixing her scarf and tweaking her bangs. She then took a breath and looked up."
    stop ambient fadeout 1.0
    play music ["<silence 0.5>","audio/bgm/BGM36.ogg"]
    show iroha coat mid_center happy at center with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E3/IRO/03/IR/IR001.ogg"
    iroha "Sorry for making you wait. It took me a while to get ready."
    voice "audio/voice/E3/IRO/03/HA/HA000.ogg"
    hachiman "Yeah, you really kept me waiting. Irohasu, you're so slo~w."
    show iroha unimpressed with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR002.ogg"
    iroha "Like I said, this is where you should say \"I just got here\". We're going on a date after all."
    "A date... She did say something like the other day. I did say that I'll \"consider it\"..."
    hachiman "(I was careless! She made a promise for me!)"
    "It's my miscalculation, but I can't just leave her hanging. Let's just get it over with quickly and go home."
    voice "audio/voice/E3/IRO/03/HA/HA001.ogg"
    hachiman "So, where're we going?"
    show iroha coat mid_left unimpressed at center with dissolve:
        xoffset -5 yoffset 65
    voice "audio/voice/E3/IRO/03/IR/IR003.ogg"
    iroha "You're leaving it to me right off the bat? I was hoping you would at least something in mind..."
    voice "audio/voice/E3/IRO/03/HA/HA002.ogg"
    hachiman "I'm super excited when I make plans to go somewhere alone, but when I'm with other people, I usually go with what they want to do."
    show iroha angry with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR004.ogg"
    iroha "Fine, just forget about it... It's cold just standing around, so let's think while we walk."
    voice "audio/voice/E3/IRO/03/HA/HA003.ogg"
    hachiman "Yeah, sure."
    hachiman "(You're the one that made me stand around in the cold...)"
    window auto hide dissolve
    stop music fadeout 1.0
    scene mallA
    show iroha coat mid_center happy at center:
        xoffset 25 yoffset 75
    with Fade(1.0, 1.0, 1.0)
    play music ["<silence 0.5>","audio/bgm/BGM17.ogg"]
    window auto show dissolve
    voice "audio/voice/E3/IRO/03/IR/IR005.ogg"
    iroha "Senpai, where do you usually go?"
    voice "audio/voice/E3/IRO/03/HA/HA004.ogg"
    hachiman "Home."
    show iroha unimpressed with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR006.ogg"
    iroha "Try that again."
    voice "audio/voice/E3/IRO/03/HA/HA005.ogg"
    hachiman "Ngh, right... The library or a bookstore I guess. You can spend time there and not get bored too easily."
    show iroha coat mid_left angry at center with dissolve:
        xoffset -5 yoffset 65
    voice "audio/voice/E3/IRO/03/IR/IR007.ogg"
    iroha "A library date..."
    show iroha coat mid_center happy at center with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E3/IRO/03/IR/IR008.ogg"
    iroha "I'm sorry, but something smart like that suits Hayama-senpai, so please suggest somewhere a bit more trashy?"
    voice "audio/voice/E3/IRO/03/HA/HA006.ogg"
    hachiman "............"
    voice "audio/voice/E3/IRO/03/HA/HA007.ogg"
    hachiman "Generally I'd go to... a karaoke, play darts, billiards, ping pong. A batting center is good too, but there's none near Chiba station."
    voice "audio/voice/E3/IRO/03/IR/IR009.ogg"
    iroha "Not that I care what suits you in particular, I don't think billiards really does."
    voice "audio/voice/E3/IRO/03/HA/HA008.ogg"
    hachiman "Leave me alone."
    show iroha vhappy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR010.ogg"
    iroha "Ah, but ping pong I think suits you!"
    voice "audio/voice/E3/IRO/03/HA/HA009.ogg"
    hachiman "I don't need your consolation."
    voice "audio/voice/E3/IRO/03/HA/HA010.ogg"
    hachiman "In any case, can we make do with a movie? We can waste 2 hours with ease."
    show iroha unimpressed with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR011.ogg"
    iroha "Why do you recommend stuff by how much time they can waste... Well, I did say I'd leave it to you."
    voice "audio/voice/E3/IRO/03/HA/HA011.ogg"
    hachiman "Movie it is then."
    window auto hide dissolve
    scene mallA with Fade(1.0, 1.0, 1.0)
    window auto show dissolve
    "Although Isshiki didn't seem happy about it, we headed to the movie theater."
    "While looking at the screenings, Isshiki was checking out a giant Hollywood movie poster which boasted an Academy Award on the cover."
    show iroha coat mid_center happy at center with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E3/IRO/03/IR/IR012.ogg"
    iroha "I wanna watch this!"
    voice "audio/voice/E3/IRO/03/HA/HA012.ogg"
    hachiman "I'll watch this one then."
    "Meanwhile I chose a movie that had no awards."
    voice "audio/voice/E3/IRO/03/HA/HA013.ogg"
    hachiman "We'll meet up later then. How about the cafe downstairs?"
    show iroha unimpressed with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR013.ogg"
    iroha "............"
    voice "audio/voice/E3/IRO/03/HA/HA014.ogg"
    hachiman "Huh? What's wrong?"
    show iroha coat mid_left unimpressed at center with dissolve:
        xoffset -5 yoffset 65
    voice "audio/voice/E3/IRO/03/IR/IR014.ogg"
    iroha "I get it now. You're like this because you do stuff like that."
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR015.ogg"
    iroha "Let's forget about the movies. Can we do table tennis after all?"
    voice "audio/voice/E3/IRO/03/HA/HA015.ogg"
    hachiman "That's fine too, but... will you be alright with those heels?"
    show iroha pout with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR016.ogg"
    iroha "............"
    "When I say this while looking at Isshiki's boots, Isshiki looked at me with a surprised and confused expression."
    voice "audio/voice/E3/IRO/03/HA/HA016.ogg"
    hachiman "W-What?"
    show iroha coat mid_center pout at center with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E3/IRO/03/IR/IR017.ogg"
    iroha "No, I... was just a little surprised you were paying attention..."
    voice "audio/voice/E3/IRO/03/HA/HA017.ogg"
    hachiman "Your eye level is different than usual, so I didn't really have to look."
    show iroha surprised with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR018.ogg"
    iroha "Eye level..."
    hide iroha with dissolve
    $renpy.pause(delay=0.5, hard=True)
    show iroha coat near_center angry at center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E3/IRO/03/HA/HA018.ogg"
    hachiman "--!"
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR019.ogg"
    iroha "Oh, you're right. We're closer than usual."
    voice "audio/voice/E3/IRO/03/HA/HA019.ogg"
    hachiman "......!"
    show iroha blush with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR020.ogg"
    iroha "............"
    hide iroha with dissolve
    "While I was at a loss for words, Isshiki was indeed puzzled by the closeness of the distance, her cheeks turning red as she looked away."
    show iroha coat mid_left blush at center with dissolve:
        xoffset -5 yoffset 65
    voice "audio/voice/E3/IRO/03/IR/IR021.ogg"
    iroha "............"
    "She then looked at me timidly, trying to look as shy as she can."
    voice "audio/voice/E3/IRO/03/HA/HA020.ogg"
    hachiman "W-Well, we can just rent out a pair of shoes. Let's go."
    voice "audio/voice/E3/IRO/03/IR/IR022.ogg"
    iroha "Okay."
    "Isshiki answered briefly and then followed behind me with small, quick steps."
    hachiman "(This kouhai is too sly...)"
    hachiman "(However, even if she's sly, she's not not cute to begin with... it's a vicious combination.)"
    window auto hide dissolve
    stop music fadeout 0.5
    scene stationA with fade
    play ambient "audio/sfx/SE05/SE05_05L.ogg"
    window auto show dissolve
    "After showing off my signature ping-pong skills to Isshiki, she tapped my shoulder."
    show iroha coat near_left happy at center with dissolve:
        xoffset 260 yoffset 75
    voice "audio/voice/E3/IRO/03/IR/IR023.ogg"
    iroha "Aren't you a bit hungry?"
    voice "audio/voice/E3/IRO/03/HA/HA021.ogg"
    hachiman "Um, kinda... want to go eat something?"
    show iroha vhappy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR024.ogg"
    iroha "Yes."
    voice "audio/voice/E3/IRO/03/HA/HA022.ogg"
    hachiman "......."
    voice "audio/voice/E3/IRO/03/IR/IR025.ogg"
    iroha "............"
    voice "audio/voice/E3/IRO/03/HA/HA023.ogg"
    hachiman "Is there something you'd prefer?"
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR026.ogg"
    iroha "I'm fine with anything."
    hachiman "(T-There it is! What they call the anything-is-fine answer!)"
    show iroha unimpressed with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR027.ogg"
    iroha "*sigh*... We can go somewhere you want to go, senpai."
    voice "audio/voice/E3/IRO/03/HA/HA024.ogg"
    hachiman "Huh? Can we really? You're not testing me or anything?"
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR028.ogg"
    iroha "Well, that's what I'd usually do, but... today, I want to eat what you normally eat, senpai."
    hachiman "(That's what you're usually doing? You're terrifying, Irohasu.)"
    "Anyway, since she's said this, I guess I really should take her to my favorite restaurant. There's only one answer here."
    window auto hide dissolve
    stop ambient fadeout 0.5
    stop music fadeout 0.5
    scene ramenShop with Fade(0.5, 1.0, 1.0)
    play music ["<silence 0.5>","audio/bgm/BGM35.ogg"]
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E3/IRO/03/HA/HA025.ogg"
    hachiman "Ahhh, that hit the spot."
    show iroha home near_center happy at center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E3/IRO/03/IR/IR029.ogg"
    iroha "...Although I initially thought, \"Woah, you'd really take me somewhere like that on date~?\", but while I hate to admit it, it's delicious. The ramen."
    "If you liked it, then that's good enough for me. Alright, now that we're done with lunch, it's time to go home!"
    window auto hide dissolve
    stop music fadeout 0.5
    play music ["<silence 1.0>","audio/bgm/BGM33.ogg"]
    call loading_screen(filename="33") from _call_general_loading_iroha_ramenShop
    stop music fadeout 1.0
    $renpy.pause(delay=0.5, hard=True)
    scene black with fade
    $renpy.pause(delay=2.5, hard=True)
    play footsteps "audio/sfx/SE00/SE00_18L.ogg" loop
    $renpy.pause(delay=1.5, hard=True)
    scene skyA with Fade(1.0, 1.0, 1.0)
    play music ["<silence 0.3>", "audio/bgm/BGM07.ogg"]
    window auto show dissolve
    "Or that's what I wanted to do at least, but here we are, walking through Chiba again."
    window auto hide dissolve
    show white with dissolve
    show iroha coat_white mid_center at center:
        xoffset 25 yoffset 75 alpha .6
    with dissolve
    window auto show dissolve
    voice "audio/voice/E3/IRO/03/IR/IR030.ogg"
    iroha "Don't you want to eat something sweet now?"
    stop voice
    window auto hide dissolve
    hide iroha
    hide white
    with dissolve
    window auto show dissolve
    "We were marching to her beat. Coming from Isshiki, it was just an order in a question's disguise."
    stop footsteps fadeout 0.5
    voice "audio/voice/E3/IRO/03/IR/IR031.ogg"
    iroha "There it is! That one!"
    window auto hide dissolve
    scene parkA
    show iroha coat mid_left happy at center:
        xoffset -5 yoffset 65
    with dissolve
    window auto show dissolve
    "What Isshiki was pointing at was a trendy cafe that didn't look like it belonged in Chiba ."
    "\"How about this one? Pretty good, right? We're going, right? What does \"I don't want to\" mean?\" - I almost hear Isshiki say as she pulls me by the scarf."
    hachiman "(You know this isn't me \"taking the lead\", right?)"
    window auto hide dissolve
    stop music fadeout 0.5
    scene skyB
    with Fade(1.0, 0.5, 1.0)
    play music ["<silence 0.3>", "audio/bgm/BGM32.ogg"]
    window auto show dissolve
    "After paying the bill, we walked out of the restaurant and the sky has started turning black."
    "It seems that we stayed there for quite a long time as we talked idly and enjoyed the sweets."
    voice "audio/voice/E3/IRO/03/HA/HA026.ogg"
    hachiman "Then, let's start heading for the station."
    voice "audio/voice/E3/IRO/03/IR/IR032.ogg"
    iroha "Okay."
    scene stationB with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E3/IRO/03/HA/HA027.ogg"
    hachiman "............"
    "Although it wasn't too late, I let out a yawn from the table tennis and other stuff."
    show iroha coat_sunset mid_left vhappy at center with dissolve:
        xoffset -5 yoffset 65
    voice "audio/voice/E3/IRO/03/IR/IR033.ogg"
    iroha "............"
    "As if it was contagious, Isshiki yawned too."
    voice "audio/voice/E3/IRO/03/HA/HA028.ogg"
    hachiman "............"
    show iroha coat_sunset mid_center happy at center with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E3/IRO/03/IR/IR034.ogg"
    iroha "...Well, I'm feeling about 10 points for today's date."
    hachiman "(Ah, right. The date-course review points.)"
    voice "audio/voice/E3/IRO/03/HA/HA029.ogg"
    hachiman "Just out of curiosity, what's the maximum?"
    show iroha vhappy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR035.ogg"
    iroha "A 100 of course."
    voice "audio/voice/E3/IRO/03/HA/HA030.ogg"
    hachiman "Why are mine so low..."
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR036.ogg"
    iroha "To begin with, you're not Hayama-senpai so that's takes off 10 points."
    voice "audio/voice/E3/IRO/03/HA/HA031.ogg"
    hachiman "It was impossible from the beginning, huh..."
    hachiman "(It's a point reduction system to boot.)"
    show iroha unimpressed with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR037.ogg"
    iroha "Furthermore, we have to shave off another 40 points because of your conduct."
    voice "audio/voice/E3/IRO/03/HA/HA032.ogg"
    hachiman "I guess I can't complain."
    show iroha coat_sunset mid_left unimpressed at center with dissolve:
        xoffset -5 yoffset 65
    voice "audio/voice/E3/IRO/03/IR/IR038.ogg"
    iroha "So you were somewhat aware of it yourself..."
    "Isshiki let the resignation in her voice show before carrying on with the grading."
    show iroha coat_sunset mid_center angry at center with dissolve:
        xoffset 25 yoffset 75
    "Isshiki suddenly clenched her right hand, making a fist, and then punched me lightly in the side."
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR039.ogg"
    iroha "You came sooo readily when a girl called you, so that's another 50 points."
    voice "audio/voice/E3/IRO/03/HA/HA033.ogg"
    hachiman "You were the one who called me, weren't you? And wait, aren't I at 0 points already?"
    voice "audio/voice/E3/IRO/03/IR/IR040.ogg"
    iroha "But I'll give you 10 points since it was fun!"
    voice "audio/voice/E3/IRO/03/HA/HA034.ogg"
    hachiman "Thanks for that."
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    call card_loading from _call_card_loading
    scene stationB with dissolve
    show iroha coat_sunset mid_center vhappy at center with dissolve:
        xoffset 25 yoffset 75
    $card_queue = ["About \nthe date", "About \nping \npong", "About \nthe 10 \npoints", "About \nHayama", "End \nconversation"]
    play music "audio/bgm/BGM31.ogg"
    $iroha_station_card_count = 0
    $iroha_station_ellipses_count = 0
    jump iroha_station_cards

#card minigame
#all ellipses are incomplete

label iroha_station_cards:
    if iroha_station_card_count < 4:
        $iroha_station_card_count += 1
        $renpy.pause(delay=0.5, hard=True)
        $ch2 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch2)
        $ch3 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch3)
        window auto hide dissolve
        call screen three_minigame("...", ch2, ch3) with dissolve
        if _return == 1:
            if ch2 == "End \nconversation":
                $card_queue.append(ch2)
            elif ch3 == "End \nconversation":
                $card_queue.append(ch3)
            else:
                $card_queue.append(renpy.random.choice([ch2,ch3]))
            $iroha_station_ellipses_count += 1
            if iroha_station_ellipses_count == 1:
                jump E3_IRO_03_ellipses1
            elif iroha_station_ellipses_count == 2:
                jump E3_IRO_03_ellipses2
            elif iroha_station_ellipses_count == 3:
                jump E3_IRO_03_ellipses3
            elif iroha_station_ellipses_count == 4:
                jump E3_IRO_03_ellipses4
        elif _return == 2:
            $card_queue.append(ch3)
            if ch2 == "About \nthe date":
                jump about_the_date_card
            elif ch2 == "About \nping \npong":
                jump about_ping_pong_card
            elif ch2 == "About \nthe 10 \npoints":
                jump about_the_10_points_card
            elif ch2 == "About \nHayama":
                jump about_hayama_card2
            else:
                jump E3_IRO_03_exit1
        elif _return == 3:
            $card_queue.append(ch2)
            if ch3 == "About \nthe date":
                jump about_the_date_card
            elif ch3 == "About \nping \npong":
                jump about_ping_pong_card
            elif ch3 == "About \nthe 10 \npoints":
                jump about_the_10_points_card
            elif ch3 == "About \nHayama":
                jump about_hayama_card2
            else:
                jump E3_IRO_03_exit1
    else:
        if iroha_station_ellipses_count < 2:
            jump E3_IRO_03_exit4
        else:
            jump E3_IRO_03_exit3

label E3_IRO_03_ellipses1:
    voice "audio/voice/E3/IRO/03/HA/HA035.ogg"
    hachiman "......"
    show iroha frown with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR041.ogg"
    iroha "Why do you go silent so easily, senpai? When you're talking about nerdy stuff or just quibbling for the sake of it, you talk quite a lot."
    voice "audio/voice/E3/IRO/03/HA/HA036.ogg"
    hachiman "I don't really have anything to say right now."
    show iroha unimpressed with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR042.ogg"
    iroha "Normally, that'd be fine, but today we're on a date, right? You have to try your best and entertain the girl till the end."
    hachiman "(Are you just ignoring the fact that you forced me to come along?)"
    jump iroha_station_cards

label E3_IRO_03_ellipses2:
    show iroha pout with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR043.ogg"
    iroha "Hmm, I think 10 points might be a bit too much. How would you rate yourself, senpai?"
    voice "audio/voice/E3/IRO/03/HA/HA037.ogg"
    hachiman "I don't know what you're grading it on, so I don't know."
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR044.ogg"
    iroha "Ah, I see. Senpai, you've never been on a date before, have you?"
    show iroha vhappy with dissolve
    hachiman "(What the hell do you know about me? It's true, though, I haven't... How did you know that...)"
    jump iroha_station_cards

label E3_IRO_03_ellipses3:
    show iroha pout with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR045.ogg"
    iroha "Senpai, since it's a date, please dress a little more to impress next time. That alone will raise your score."
    voice "audio/voice/E3/IRO/03/HA/HA038.ogg"
    hachiman "To impress, huh? Like a tuxedo with a purple rose on it?"
    show iroha annoyed with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR046.ogg"
    iroha "Why a purple one? A suit is way too fancy, so no. That'd be a straight rejection, let alone a minus."
    voice "audio/voice/E3/IRO/03/HA/HA039.ogg"
    hachiman "What do I have to wear to pass then?"
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR047.ogg"
    iroha "You can't pull off anything similiar to Hayama-senpai, so I think playing it safe with something black or more subdued would be fine."
    show iroha vhappy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR048.ogg"
    iroha "I'll pick out clothes for you next time. Let's go shopping together!"
    hachiman "(In order to do that, I need to have clothes I can wear to begin with...)"
    hachiman "(Oh, but maybe I can use this as an excuse to go shopping with Komachi! I'll ask her to pick out some clothes for me! Yay!)"
    jump iroha_station_cards

label E3_IRO_03_ellipses4:
    voice "audio/voice/E3/IRO/03/HA/HA040.ogg"
    hachiman "........."
    show iroha pout with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR049.ogg"
    iroha "........."
    voice "audio/voice/E3/IRO/03/IR/IR050.ogg"
    iroha "Senpai. Please start talking."
    voice "audio/voice/E3/IRO/03/HA/HA041.ogg"
    hachiman "Why? I thought this was the end of the date."
    show iroha angry with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR051.ogg"
    iroha "It's no good if you're not paying attention until the end. The date's over until you can't see me anymore, senpai."
    hachiman "(First time I'm hearing about that...)"
    jump iroha_station_cards

label about_the_date_card:
    window auto show dissolve
    voice "audio/voice/E3/IRO/03/HA/HA042.ogg"
    hachiman "So, how was the date?"
    voice "audio/voice/E3/IRO/03/IR/IR052.ogg"
    iroha "Although it's different from what I imagined, sometimes different can be good."
    show iroha pout with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR053.ogg"
    iroha "If it's Hayama-senpai instead, I'd have no complaints."
    voice "audio/voice/E3/IRO/03/HA/HA043.ogg"
    hachiman "I'm sorry that it's JUST ME."
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR054.ogg"
    iroha "Didn't I say that you scored 10 points? I'm glad I went out with senpai today."
    voice "audio/voice/E3/IRO/03/HA/HA044.ogg"
    hachiman "...Is that so."
    show iroha vhappy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR055.ogg"
    iroha "Yes!"
    stop voice
    jump iroha_station_cards

label about_ping_pong_card:
    window auto show dissolve
    voice "audio/voice/E3/IRO/03/HA/HA045.ogg"
    hachiman "You were pretty good at ping pong. Do you play regularly?"
    show iroha frown with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR056.ogg"
    iroha "Heh-, I don't-. Isn't ping pong is kinda plain?"
    hachiman "(Ping pong is pretty cool, right? Don't you know of any manga or anime based on ping pong?)"
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR057.ogg"
    iroha "If you want to play, you should play something like bowling, darts, or even billiards"
    show iroha vhappy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR058.ogg"
    iroha "But Senpai looks good at ping pong, so I think it's fine for you to keep playing same old ping pong."
    hachiman "(What do you mean, same old ping pong? Is this some kind of \"stay the way you are\" thing?)"
    jump iroha_station_cards

label about_the_10_points_card:
    window auto show dissolve
    voice "audio/voice/E3/IRO/03/HA/HA049.ogg"
    hachiman "That 10 points, is it good? is it bad?"
    show iroha unimpressed with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR063.ogg"
    iroha "It's out of 100 points, so of course it's bad."
    hachiman "(It could a difficult test with an average score being single digit, you know?)"
    show iroha pout with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR064.ogg"
    iroha "...But, isn't having fun the most important thing about dates? I don't want to make any memories that are not fun."
    voice "audio/voice/E3/IRO/03/HA/HA050.ogg"
    hachiman "...Well, I guess so."
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR065.ogg"
    iroha "On that point, senpai's 10 points are highly valuable because they are points for \"having fun\"."
    show iroha vhappy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR066.ogg"
    iroha "But that' s just an extra 10 points. Senpai is not ready yet. Please continue to work hard from now on. Keep up the good work, senpai!"
    hachiman "(...I don't think I can get 100 points, even if I try...)"
    jump iroha_station_cards

label about_hayama_card2:
    window auto show dissolve
    voice "audio/voice/E3/IRO/03/HA/HA051.ogg"
    hachiman "So did you get anything out of this for your date with Hayama?"
    show iroha pout with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR067.ogg"
    iroha "Mm... Senpai is so special that it doesn't even seem like it would be a good reference for a date with a normal person, let alone Hayama-senpai!"
    voice "audio/voice/E3/IRO/03/HA/HA052.ogg"
    hachiman "On the other hand, it's good reference for dating someone out of the ordinary. That was worthwhile."
    show iroha unimpressed with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR068.ogg"
    iroha "What are you trying to say with that smug grin?"
    jump E3_IRO_03_exit2

label E3_IRO_03_exit1:
    voice "audio/voice/E3/IRO/03/HA/HA053.ogg"
    hachiman "I'm done for today, right? I'll be going then."
    show iroha angry with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR069.ogg"
    iroha "Jeez, senpai, the end of the date is just as important! Why are you trying to leave straight away?"
    voice "audio/voice/E3/IRO/03/HA/HA054.ogg"
    hachiman "I'm pretty tired honestly..."
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR070.ogg"
    iroha "Okay, that just cost you 50 points."
    hachiman "(That's negative 40...)"
    jump E3_IRO_03_end_cont

label E3_IRO_03_exit2:
    voice "audio/voice/E3/IRO/03/IR/IR071.ogg"
    iroha "You failed at the very last moment, senpai."
    voice "audio/voice/E3/IRO/03/HA/HA055.ogg"
    hachiman "Really? Did I do something wrong?"
    show iroha angry with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR072.ogg"
    iroha "Why don't you figure that out yourself? That's it, I'm deducting another 5 points."
    hachiman "(She at least left me 5 points. Irohasu, you're to ki~nd!)"
    jump E3_IRO_03_end_cont

label E3_IRO_03_exit3:
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR073.ogg"
    iroha "But... I had fun today."
    voice "audio/voice/E3/IRO/03/HA/HA056.ogg"
    hachiman "What's this all of a sudden?"
    show iroha angry with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR075.ogg"
    iroha "What do you mean \"what's this\"!? Isn't this how dates are supposed to end?"
    voice "audio/voice/E3/IRO/03/HA/HA057.ogg"
    hachiman "Yeah, you're right. Proforma is important."
    show iroha frown with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR076.ogg"
    iroha "I was being serious..."
    voice "audio/voice/E3/IRO/03/IR/IR077.ogg"
    iroha "Well, that's enough of that. I'll leave your extra 10 points intact."
    hachiman "(Don't need them either way really.)"
    jump E3_IRO_03_end_cont

label E3_IRO_03_exit4:
    show iroha vhappy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR078.ogg"
    iroha "Hm~. maybe I should give you another 5..."
    voice "audio/voice/E3/IRO/03/HA/HA058.ogg"
    hachiman "Eh? Really, now? Why's that?"
    show iroha blush with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR079.ogg"
    iroha "Because I wanted to stay with you a little longer, senpai."
    voice "audio/voice/E3/IRO/03/HA/HA059.ogg"
    hachiman "............"
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR080.ogg"
    iroha "But! It's only right I say goodbye at this point, so that's it for today!"
    voice "audio/voice/E3/IRO/03/IR/IR081.ogg"
    show iroha vhappy with dissolve
    iroha "So, your final score for today's date is 15 points!"
    voice "audio/voice/E3/IRO/03/HA/HA060.ogg"
    hachiman "All right. 15 points is 15 points."
    jump E3_IRO_03_end_cont

label E3_IRO_03_end_cont:
    window auto hide dissolve
    stop music fadeout 0.5
    scene stationB with Fade(1.0, 1.0, 1.0)
    play music ["<silence 0.5>", "audio/bgm/BGM36.ogg"]
    show iroha coat_sunset mid_center vhappy at center with dissolve:
        xoffset 25 yoffset 75
    window auto show dissolve
    voice "audio/voice/E3/IRO/03/IR/IR082.ogg"
    iroha "Anyways, today was really helpful. Thank you."
    voice "audio/voice/E3/IRO/03/HA/HA061.ogg"
    hachiman "Sure..."
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/03/IR/IR083.ogg"
    iroha "Make sure to learn from this too, okay, senpai?"
    voice "audio/voice/E3/IRO/03/HA/HA062.ogg"
    hachiman "For sure. Well, um, thanks for today."
    show iroha coat_sunset mid_left happy at center with dissolve:
        xoffset -5 yoffset 65
    voice "audio/voice/E3/IRO/03/IR/IR084.ogg"
    iroha "Well, see you at school then."
    voice "audio/voice/E3/IRO/03/HA/HA063.ogg"
    hachiman "Be careful on your way home."
    hide iroha with dissolve
    stop music fadeout 1.0
    voice "audio/voice/E3/IRO/03/HA/HA064.ogg"
    hachiman "............"
    show iroha coat_sunset far_left vhappy at center with dissolve:
        xoffset 5 yoffset 80
    "As I watched Isshiki leave, she suddenly turned around and gave me a small wave."
    "I responded by lightly raising my hand."
    hide iroha with dissolve
    "I saw her off with my gaze until she wasn't visible anymore."
    window auto hide dissolve
    jump E3_IRO_04

label E3_IRO_04:
    scene sidewalkB with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/BGM18.ogg"
    window auto show dissolve
    "On the way home, I thought about Isshiki."
    "Even though gives me a lot of trouble, it's surprisingly fun. People like her are often called temptresses."
    "With a mild sense of awe, I suddenly remembered the conversation I had with Isshiki while we were playing ping-pong."
    window auto hide dissolve
    show white with dissolve
    show iroha home_white mid_center at center:
        xoffset 25 yoffset 75 alpha .6
    with dissolve
    window auto show dissolve
    voice "audio/voice/E3/IRO/04/IR/IR000.ogg"
    iroha "Isn't it more girl-like to be a little sly?"
    stop voice
    window auto hide dissolve
    hide iroha
    hide white
    with dissolve
    window auto show dissolve
    voice "audio/voice/E3/IRO/04/HA/HA000.ogg"
    hachiman "............"
    "I could understand that. It reminds me of what was said in Mother Goose: \"Girls are made of sugar, spice and something nice.\""
    "It really is like that. Isshiki leans a bit heavily on the spicy side, though."
    window auto hide dissolve
    call loading_screen(10) from call_iroha_coat_loading_outside2
    stop music
    jump E3_G09_01

#iroha route
label E3_IRO_05:
    scene clubroomB with Fade(1.0, 0.5, 1.0)
    play music ["<silence 0.5>", "audio/bgm/BGM29.ogg"]
    show yukino school_sunset mid_center happy at left:
        xoffset -105 yoffset 75
    show yui school_sunset mid_center happy at center:
        xoffset -25 yoffset 75
    show iroha school_sunset mid_left happy at right:
        xoffset -190 yoffset 65
    with dissolve
    window auto show dissolve
    voice "audio/voice/E3/IRO/05/IR/IR000.ogg"
    iroha "Come to think of it, have you guys decided on your career path?"
    show yukino stare
    show yui school_sunset mid_right pout at center with dissolve:
        xoffset -110 yoffset 75
    voice "audio/voice/E3/IRO/05/YK/YK000.ogg"
    yukino "Yes. More or less."
    voice "audio/voice/E3/IRO/05/YI/YI000.ogg"
    yui "Yeah, I've mostly decided, but I'm still pretty worried about it."
    show iroha pout with dissolve
    voice "audio/voice/E3/IRO/05/IR/IR001.ogg"
    iroha "High school entrance exams and university entrance exams are totally different, huh? Have you decided what you'll do, senpai?"
    voice "audio/voice/E3/IRO/05/HA/HA000.ogg"
    hachiman "I..."
    show iroha vhappy with dissolve
    voice "audio/voice/E3/IRO/05/IR/IR002.ogg"
    iroha "Ah, did anyone of you all happen to hear which one Hayama-senpai chose~?"
    voice "audio/voice/E3/IRO/05/HA/HA001.ogg"
    hachiman "Hey, I didn't even get to answer. And it's really embarrassing if you leave just leave me mumbling like that."
    show iroha school_sunset mid_center happy at right with dissolve:
        xoffset -190 yoffset 75
    voice "audio/voice/E3/IRO/05/IR/IR003.ogg"
    iroha "I did ask casually, but now that I think about it, I don't really care. I wouldn't be very excited to know."
    show yukino sly with dissolve
    voice "audio/voice/E3/IRO/05/YK/YK001.ogg"
    yukino "Oh, Isshiki-san, you're on point. That's right. Hikigaya choosing his career path via the method of elimination is not exactly interesting. Let's chat with just the 3 of us."
    voice "audio/voice/E3/IRO/05/HA/HA002.ogg"
    hachiman "Hey? Can you not just casually exclude me like that?"
    show iroha school_sunset mid_left sad at right with dissolve:
        xoffset -190 yoffset 65
    voice "audio/voice/E3/IRO/05/IR/IR004.ogg"
    iroha "But still it feels like the three of you will start working super hard for the exams next year."
    show yukino happy with dissolve
    voice "audio/voice/E3/IRO/05/YK/YK002.ogg"
    yukino "Yes. That's why the Service Club will be hard-pressed to give the Student Council any support."
    show yui with dissolve
    voice "audio/voice/E3/IRO/05/YI/YI001.ogg"
    yui "Yeah. It's a shame we won't be able to help, but if I'm sure you'll be fine, Iroha-chan!"
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/05/IR/IR005.ogg"
    iroha "Right. More importantly, without you guys here, it'll start to feel lonely..."
    show yui vhappy with dissolve
    voice "audio/voice/E3/IRO/05/YI/YI002.ogg"
    yui "Iroha-chan..."
    hachiman "(How sly...)"
    hachiman"(But it's still making me happy, god damn it!)"
    voice "audio/voice/E3/IRO/05/IR/IR006.ogg"
    iroha "And after all, I'll have less people I can ask to do work for me."
    show yui happy with dissolve
    voice "audio/voice/E3/IRO/05/HA/HA003.ogg"
    hachiman "Ah, right. Mask off."
    show iroha unimpressed with dissolve
    voice "audio/voice/E3/IRO/05/IR/IR007.ogg"
    iroha "Besides, exams shouldn't be that long right~? I wish they'd go away already..."
    show iroha surprised with dissolve
    voice "audio/voice/E3/IRO/05/IR/IR008.ogg"
    iroha "Ah! Why not get recommendations instead!? Then your exams will end earlier, and the Service Club will be back in business again!"
    show yui vhappy with dissolve
    voice "audio/voice/E3/IRO/05/YI/YI003.ogg"
    yui "That's a good idea, Iroha-chan! You won't have to study for exams then!"
    show iroha vhappy with dissolve
    voice "audio/voice/E3/IRO/05/IR/IR009.ogg"
    iroha "Yep! Let's protect the service club together!"
    voice "audio/voice/E3/IRO/05/YI/YI004.ogg"
    yui "Iroha-chan, to think you thought so much of the Service Club..."
    voice "audio/voice/E3/IRO/05/HA/HA004.ogg"
    hachiman "Don't be fooled, Yuigahama. We're nothing but easily plaible underlings to her."
    show yukino angry
    show yui school_sunset mid_center pout at center:
        xoffset -25 yoffset 75
    with dissolve
    voice "audio/voice/E3/IRO/05/YK/YK003.ogg"
    yukino "That's true. Besides, Isshiki-san's plan is not realistic. Yuigahama-san and you are going to have a hard time getting a recommendation."
    voice "audio/voice/E3/IRO/05/HA/HA005.ogg"
    hachiman "I get Yuigahama, but I get pretty decent grades, don't you think?"
    show yukino vhappy with dissolve
    voice "audio/voice/E3/IRO/05/YK/YK004.ogg"
    yukino "Sure. But who exactly is going to recommend you?"
    hachiman "(Who you say? You're one to ta-- I wonder who would actually recommend me.)"
    window auto hide dissolve
    stop music fadeout 0.5
    $renpy.pause(delay=1.0, hard=True)
    call loading_screen(8, "44") from _call_Loading_screen_E3_IRO_05
    scene black with Fade(1.0,0.5,1.5)
    play sound "audio/sfx/SE04/SE04_07.ogg"
    scene hallwayA with wipeleft
    $renpy.pause(delay=1.0, hard=True)
    stop sound
    play music "audio/bgm/BGM36.ogg"
    window auto show dissolve
    hachiman "(I never thought I'd get such a scolding for wanting to be a fulltime house-husband.)"
    stop sound
    hachiman "(I wonder what Hiratsuka-sensei's problem was yesterday. I can only assume she was taking out her frustration on me.)"
    hachiman "(Honestly, someone marry her! Anyone! Let her vent her stress on you!)"
    "I was walking along the corridor when I felt a gentle slap on my back."
    voice "audio/voice/E3/IRO/06/IR/IR000.ogg"
    mystery "Se~npai!"
    voice "audio/voice/E3/IRO/06/HA/HA000.ogg"
    hachiman "...Hm?"
    show iroha school mid_center happy at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E3/IRO/06/HA/HA001.ogg"
    hachiman "It's you..."
    show iroha vhappy with dissolve
    voice "audio/voice/E3/IRO/06/IR/IR001.ogg"
    iroha "nfufu"
    voice "audio/voice/E3/IRO/06/HA/HA002.ogg"
    hachiman "What do you want?"
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/06/IR/IR002.ogg"
    iroha "Well, well, well~ That's exactly the face someone squeezed by a career counselor would make, isn't it?"
    voice "audio/voice/E3/IRO/06/HA/HA003.ogg"
    hachiman "...You could say that. Did you see me coming out of the Counseling Room?"
    show iroha unimpressed with dissolve
    voice "audio/voice/E3/IRO/06/IR/IR003.ogg"
    iroha "...You could have said \"Woah, how did you know?\" or act a bit surprised. You're so boring."
    show iroha school mid_left happy at center with dissolve:
        xoffset -35 yoffset 65
    voice "audio/voice/E3/IRO/06/IR/IR004.ogg"
    iroha "Well, whatever. I have a suggestion for this senpai of mine~"
    show iroha vhappy with dissolve
    voice "audio/voice/E3/IRO/06/IR/IR005.ogg"
    iroha "Want to go to the roof for a bit?"
    voice "audio/voice/E3/IRO/06/HA/HA004.ogg"
    hachiman "Eh, what? Have you finally lost your temper? Am I gonna get a beatdown? And just after getting bullied by Hiratsuka-sensei at at?"
    show iroha school mid_center vhappy at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E3/IRO/06/IR/IR006.ogg"
    iroha "You have to be so wary. Come on, let's go!"
    hide iroha with dissolve
    show iroha school near_center vhappy at center with dissolve:
        xoffset -15 yoffset 75
    "Saying that, Isshiki pulled my hand and made me follow her. ...I feel like I'm already used to this overbearing coercivness."
    voice "audio/voice/E3/IRO/06/HA/HA005.ogg"
    hachiman "The roof needs a key, doesn't it?"
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/06/IR/IR007.ogg"
    iroha "I borrowed it with the power of the Student Council so no worries~"
    voice "audio/voice/E3/IRO/06/HA/HA006.ogg"
    hachiman "Are you really just going to abuse your authority like that...?"
    window auto hide dissolve
    stop music fadeout 0.5
    scene black with fade
    window auto show dissolve
    hachiman"(Come to think of it, I haven't been to the roof since the Cultural Festival...)"
    window auto hide dissolve
    play sound "audio/sfx/SE04/SE04_10.ogg"
    $renpy.pause(delay=1.5, hard=True)
    stop sound
    play sound ["<silence 1.5>", "audio/sfx/SE04/SE04_09.ogg"]
    scene white with Fade(0.25,1.5,0.25)
    play ambient "audio/sfx/SE02/SE02_02.ogg" noloop
    scene skyA with dissolve
    stop sound
    window auto show dissolve
    voice "audio/voice/E3/IRO/06/HA/HA007.ogg"
    hachiman "Wah, so cold!"
    "A cold gust of wind blew over us the moment we opened the door."
    scene rooftopA
    show iroha school mid_center happy at center:
        xoffset -5 yoffset 75
    with dissolve
    voice "audio/voice/E3/IRO/06/IR/IR008.ogg"
    iroha "Ah, it's really cold after all."
    window auto hide dissolve
    stop voice
    stop ambient
    show irohaRooftopB with dissolve
    play music "audio/bgm/BGM42.ogg"
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E3/IRO/06/HA/HA008.ogg"
    hachiman "--!"
    "Isshiki clung to my arm without a second thought."
    voice "audio/voice/E3/IRO/06/HA/HA009.ogg"
    hachiman "...Isshiki, you're close, it's cold and can you not use me as a windbreaker?"
    voice "audio/voice/E3/IRO/06/IR/IR009.ogg"
    iroha "It's fine, isn't it? We'll warm up a bit."
    "With her cheeks flushed, she wrapped herself around my arm."
    hachiman "(This Irohasu warming up method is really effective! I'm even sweating! It's so overeffective, I'm even turning cold.)"
    voice "audio/voice/E3/IRO/06/IR/IR010.ogg"
    iroha "So senpai, why did the career counseling thing leave you so badly beaten?"
    voice "audio/voice/E3/IRO/06/HA/HA010.ogg"
    hachiman "Well, it has to do with the future, so it's a bit complicated."
    voice "audio/voice/E3/IRO/06/IR/IR011.ogg"
    iroha "Oh~? Senpai, what do you want to be in the future?"
    voice "audio/voice/E3/IRO/06/HA/HA011.ogg"
    hachiman "A fulltime house-husband of course."
    voice "audio/voice/E3/IRO/06/IR/IR012.ogg"
    iroha "I'm sorry, I shouldn't have asked."
    voice "audio/voice/E3/IRO/06/HA/HA012.ogg"
    hachiman "Ngh, well what about you then?"
    voice "audio/voice/E3/IRO/06/IR/IR013.ogg"
    iroha "Hmm... I want to become a fulltime house-wife, too."
    voice "audio/voice/E3/IRO/06/HA/HA013.ogg"
    hachiman "See?"
    voice "audio/voice/E3/IRO/06/IR/IR014.ogg"
    iroha "Fufu~ Thinking about it, I really do want a comfortable life too."
    voice "audio/voice/E3/IRO/06/IR/IR015.ogg"
    iroha "...But, if both of us do that fulltime, we'll struggle a bit financially..."
    voice "audio/voice/E3/IRO/06/HA/HA014.ogg"
    hachiman "...Wait, what?"
    hachiman "(No matter how I slice it, I can't help but draw some seriously odd conclusions from what she just said...)"
    voice "audio/voice/E3/IRO/06/IR/IR016.ogg"
    iroha "............"
    "While I stood there, doubting my ears, a stifled laugh escaped Isshiki's lips."
    voice "audio/voice/E3/IRO/06/IR/IR017.ogg"
    iroha "Haaa, I let my guard down too easily when I'm with senpai..."
    voice "audio/voice/E3/IRO/06/IR/IR018.ogg"
    iroha "But I guess it's nice to be able to do that. Being myself that is."
    voice "audio/voice/E3/IRO/06/HA/HA015.ogg"
    hachiman "Can you not talk about me like I'm a product from a face wash commercial?"
    voice "audio/voice/E3/IRO/06/IR/IR019.ogg"
    iroha "It means I feel very comfortable around you, senpai."
    menu E3_IRO_05_menu:
        with dissolve
        "With an absentminded sigh, Isshiki puts her head on my shoulder. A sweet scent drifted softly into the air and tickled my nostrils."
        "Eh...!":
            voice "audio/voice/E3/IRO/06/HA/HA016.ogg"
            hachiman "Eh~.....!"
            voice "audio/voice/E3/IRO/06/IR/IR020.ogg"
            iroha "Is it really that surprising? I'm always at my most natural around you, senpai."
            voice "audio/voice/E3/IRO/06/HA/HA017.ogg"
            hachiman "Even if you say that... Is that so?"
            voice "audio/voice/E3/IRO/06/IR/IR021.ogg"
            iroha "Yeah, so this is really calming for me."
        "Is that so?":
            "not done"
            jump E3_IRO_05_menu
        "Flattery won't get you anywhere.":
            "not done"
            jump E3_IRO_05_menu

    "Isshiki let show a small smile and rested like a spoiled kitten on my shoulder."
    hachiman "(She's being awfully needy today...)"
    voice "audio/voice/E3/IRO/06/HA/HA025.ogg"
    hachiman "You say you're comfortable around me, but I'm pretty sure this isn't exactly a true self I'm seeing."
    voice "audio/voice/E3/IRO/06/IR/IR030.ogg"
    iroha "That's no good~ But that's not what I'm getting at right now."
    voice "audio/voice/E3/IRO/06/HA/HA026.ogg"
    hachiman "?"
    voice "audio/voice/E3/IRO/06/IR/IR031.ogg"
    iroha "For example, even if the whole world somehow found out who I really was, I'd still try to hide it."
    voice "audio/voice/E3/IRO/06/IR/IR032.ogg"
    iroha "But it's different with you."
    voice "audio/voice/E3/IRO/06/IR/IR033.ogg"
    iroha "You're the only one that I feel like I can show who I really am to. You're the only person that I want to see more of the real me."
    voice "audio/voice/E3/IRO/06/HA/HA027.ogg"
    hachiman "Right..."
    "I'm not like Isshiki. I care about what people think, but don't play a character like she does. So I don't understand this \"comfortableness\" she feels around me."
    "But be that as it may..."
    hachiman "(I do get it. Just a little bit.)"
    "\"I want to see more of the real me\"; it's that part I can understand."
    voice "audio/voice/E3/IRO/06/IR/IR034.ogg"
    iroha "............"
    show irohaRooftopA with dissolve
    voice "audio/voice/E3/IRO/06/IR/IR035.ogg"
    iroha "Say, senpai... Have you found your \"real thing\"?"
    "So it seemed very natural to me to be asked such a seemingly unrelated question."
    voice "audio/voice/E3/IRO/06/HA/HA028.ogg"
    hachiman "............"
    voice "audio/voice/E3/IRO/06/IR/IR036.ogg"
    iroha "............"
    "Looking at me with upturned eyes brimming with fleeting expectation and warmth, Isshiki waited for my answer."
    "But whether I can live up to that expectation is another story."
    voice "audio/voice/E3/IRO/06/HA/HA029.ogg"
    hachiman "It looks like I'll need more time."
    hide irohaRooftopA with dissolve
    "Hearing my answer, Isshiki puffed and smiled broadly."
    voice "audio/voice/E3/IRO/06/IR/IR037.ogg"
    iroha "...Is that so?"
    window auto hide dissolve
    hide irohaRooftopB with dissolve
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E3/IRO/06/IR/IR038.ogg"
    iroha "My whole body's freezing now. We should get back soon."
    voice "audio/voice/E3/IRO/06/HA/HA030.ogg"
    hachiman "Yep."
    hide iroha with dissolve
    voice "audio/voice/E3/IRO/06/HA/HA031.ogg"
    hachiman "............"
    play sound "audio/sfx/SE04/SE04_09.ogg"
    $renpy.pause(delay=2.0, hard=True)
    voice "audio/voice/E3/IRO/06/IR/IR039.ogg"
    iroha "Senpai, if you don't hurry, I'm gonna leave~ I'm locking the door~"
    voice "audio/voice/E3/IRO/06/HA/HA032.ogg"
    hachiman "Right."
    hachiman "(\"Have I found the \"real thing\"?\", huh...)"
    "I still haven't found the answer to that question."
    "But I'm sure that someday I will."
    window auto hide dissolve
    stop music fadeout 0.5
    call loading_screen(9, "33") from _call_Loading_screen_E3_IRO_05_2
    scene black with fade
    jump E3_CMM_06

label E3_IRO_07:
    scene black with Fade(1.0,0.5,1.5)
    play sound "audio/sfx/SE04/SE04_01.ogg"
    scene hallwayB with wipeleft
    $renpy.pause(delay=2.0,hard=False)
    window auto show dissolve
    hachiman "(Phew, I'm beat... I'll hurry on home.)"
    stop sound
    voice "audio/voice/E3/IRO/07/YI/YI000.ogg"
    mystery "Hikki, wait for me!"
    voice "audio/voice/E3/IRO/07/HA/HA000.ogg"
    hachiman "Hmm?"
    play music ["<silence 0.5>","audio/bgm/BGM12.ogg"]
    show yui school_sunset mid_right pout flat at center with dissolve:
        xoffset -225 yoffset 75
        parallel:
            easein 0.5 xoffset -110
    $renpy.pause(delay=1.0, hard=True)
    hide yui
    show yui school_sunset mid_right pout at center:
        xoffset -110 yoffset 75
    voice "audio/voice/E3/IRO/07/HA/HA001.ogg"
    hachiman "Why? What's up?"
    show yui school_sunset mid_center pout at center with dissolve:
        xoffset -25 yoffset 75
    voice "audio/voice/E3/IRO/07/YI/YI001.ogg"
    yui "Ah... well, um..."
    voice "audio/voice/E3/IRO/07/HA/HA002.ogg"
    hachiman "What is it? Where's Yukinoshita?"
    show yui happy with dissolve
    voice "audio/voice/E3/IRO/07/YI/YI002.ogg"
    yui "Yukinon was held up by some students who came for the career counseling."
    voice "audio/voice/E3/IRO/07/HA/HA003.ogg"
    hachiman "I see. I'm sure she'll be able to give them proper, harsh advice that hits home."
    hachiman "(How many students will survive...?)"
    voice "audio/voice/E3/IRO/07/YI/YI003.ogg"
    yui "Hahaha, probably. But Iroha-chan was super happy she decided to help."
    voice "audio/voice/E3/IRO/07/HA/HA004.ogg"
    hachiman "I know, right? I'm sure to her Yukinoshita is a rare beast she can summon to insta-win."
    hachiman "(She'll be like an ice-class summon - Yukinoshiva.)"
    voice "audio/voice/E3/IRO/07/HA/HA005.ogg"
    hachiman "Yukinoshita seems to be kind of doting on her from time to time. Those two seem to be getting on surprisingly well."
    show yui sad with dissolve
    voice "audio/voice/E3/IRO/07/YI/YI004.ogg"
    yui "............"
    show yui happy with dissolve
    voice "audio/voice/E3/IRO/07/YI/YI005.ogg"
    yui "Are you getting a bit jealous that she's relying on Yukinoshita instead of you? As another senpai."
    voice "audio/voice/E3/IRO/07/HA/HA006.ogg"
    hachiman "No way. She spells nothing but trouble."
    show yui sad with dissolve
    voice "audio/voice/E3/IRO/07/YI/YI006.ogg"
    yui "...Really?"
    show yui happy with dissolve
    voice "audio/voice/E3/IRO/07/YI/YI007.ogg"
    yui "But you and Iroha-chan are a good match, too."
    voice "audio/voice/E3/IRO/07/HA/HA007.ogg"
    hachiman "Huh? You think so?"
    show yui sad with dissolve
    voice "audio/voice/E3/IRO/07/YI/YI008.ogg"
    yui "Yeah..."
    voice "audio/voice/E3/IRO/07/HA/HA008.ogg"
    hachiman "So, did you want to tell me something in particular?"
    hide yui
    $url = ["yui school_sunset mid_center surprised", "yui school_sunset mid_center happy"]
    $multiImagePara = [-25, 75, 0, 0, 2.4]
    call multiImage() from _call_multiImage_3
    voice "audio/voice/E3/IRO/07/YI/YI009.ogg"
    yui "Huh? ...Ah, right! The work we did today was pretty fun, just like with the Service Club."
    call finishmultiImage from _call_finishmultiImage_3
    show yui school_sunset mid_center happy at center:
        xoffset -25 yoffset 75
    voice "audio/voice/E3/IRO/07/HA/HA009.ogg"
    hachiman "You caught up to me all that way just to say that?"
    show yui sad with dissolve
    hachiman "So, did you want to tell me something in particular?"
    hide yui
    $url = ["yui school_sunset mid_center sad", "yui school_sunset mid_center happy"]
    $multiImagePara = [-25, 75, 0, 0, 2.4]
    call multiImage() from _call_multiImage_4
    voice "audio/voice/E3/IRO/07/YI/YI010.ogg"
    yui "Because it's important! \"It'd be nice if we could all to this again!\" sort of thing."
    call finishmultiImage from _call_finishmultiImage_4
    show yui school_sunset mid_center happy at center:
        xoffset -25 yoffset 75
    voice "audio/voice/E3/IRO/07/HA/HA010.ogg"
    hachiman"No, it really won't. I'm gonna be sore all over tomorrow."
    show yui unimpressed with dissolve
    voice "audio/voice/E3/IRO/07/YI/YI011.ogg"
    yui "You're missing the point..."
    voice "audio/voice/E3/IRO/07/HA/HA011.ogg"
    hachiman "Hmm?"
    show yui sad with dissolve
    voice "audio/voice/E3/IRO/07/YI/YI012.ogg"
    yui "Ah, i-it's nothing!"
    show yui vhappy with dissolve
    voice "audio/voice/E3/IRO/07/YI/YI013.ogg"
    yui "See you later, Hikki!"
    voice "audio/voice/E3/IRO/07/HA/HA012.ogg"
    hachiman "...? Sure."
    window auto hide dissolve
    stop music fadeout 0.5
    jump E3_CMM_07

label E3_IRO_08:
    scene hallwayB with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    hachiman "(...There she is. My back has started straightening up already.)"
    show iroha school_sunset mid_center vhappy at center with dissolve:
        xoffset -5 yoffset 75
    play music "audio/bgm/BGM36.ogg"
    voice "audio/voice/E3/IRO/08/IR/IR000.ogg"
    iroha "Senpai~! Are you going home already?"
    voice "audio/voice/E3/IRO/08/HA/HA000.ogg"
    hachiman "Was just about to. Done with the Career Consultation event already?"
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/08/IR/IR001.ogg"
    iroha "Well, not exactly~. That's why I stepped out for a bit."
    show iroha school_sunset mid_left happy at center with dissolve:
        xoffset -35 yoffset 65
    voice "audio/voice/E3/IRO/08/IR/IR002.ogg"
    iroha "You know how they say when a great superior is watching over you, it's hard to work?"
    hachiman "(Who does she think she is?)"
    show iroha unimpressed with dissolve
    voice "audio/voice/E3/IRO/08/IR/IR003.ogg"
    iroha "Though If only I were part of the Service Club, I could just pop in for a bit and then peace out."
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/08/IR/IR004.ogg"
    iroha "I think I'll join the Service Club at this point."
    voice "audio/voice/E3/IRO/08/HA/HA001.ogg"
    hachiman "Huh?"
    show iroha school_sunset mid_center happy at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E3/IRO/08/IR/IR005.ogg"
    iroha "I mean I've already done a ton of work with you guys, right?"
    show iroha vhappy with dissolve
    voice "audio/voice/E3/IRO/08/IR/IR006.ogg"
    iroha "Besides, all of you will be taking exams next year, so disbanding the club would be pretty sad."
    show iroha school_sunset mid_left happy at center with dissolve:
        xoffset -35 yoffset 65
    voice "audio/voice/E3/IRO/08/IR/IR007.ogg"
    iroha "It's my duty as a junior to reserve a place for my seniors, who have finished their exams, to come back to."
    voice "audio/voice/E3/IRO/08/HA/HA002.ogg"
    hachiman "You're just whispering sweet nothings, but all you want to do is have another excuse to slack off."
    show iroha angry with dissolve
    voice "audio/voice/E3/IRO/08/IR/IR008.ogg"
    iroha "Excuse me? I was kind of serious~."
    voice "audio/voice/E3/IRO/08/HA/HA003.ogg"
    hachiman "If you're relationship with the people there is solely dependant on that \"place to come back to\", it will eventually break apart."
    show iroha sad with dissolve
    voice "audio/voice/E3/IRO/08/IR/IR009.ogg"
    iroha "Isn't that a bit... too real?"
    show iroha school_sunset mid_center sad at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E3/IRO/08/IR/IR010.ogg"
    iroha "Keeping that distance... If we try to shorten it, we can continue the relationship..."
    voice "audio/voice/E3/IRO/08/HA/HA004.ogg"
    hachiman "Well, that's true. Everyone wants to know the other person, so they try to close the distance."
    voice "audio/voice/E3/IRO/08/HA/HA005.ogg"
    hachiman "But what might follow that understanding is seperation."
    voice "audio/voice/E3/IRO/08/IR/IR011.ogg"
    iroha "..."
    stop music fadeout 1.0
    show iroha angry with dissolve
    voice "audio/voice/E3/IRO/08/IR/IR012.ogg"
    iroha "That's why senpai, you..."
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/08/HA/HA006.ogg"
    hachiman "Huh?"
    voice "audio/voice/E3/IRO/08/IR/IR013.ogg"
    iroha "No, it's nothing."
    play music ["<silence 0.5>", "audio/bgm/BGM32.ogg"]
    show iroha vhappy with dissolve
    voice "audio/voice/E3/IRO/08/IR/IR014.ogg"
    iroha "Ah, hey, so, how about... closing that distance with me?"
    menu iroha_hallyway_menu:
        "Um...":
            voice "audio/voice/E3/IRO/08/HA/HA007.ogg"
            hachiman "Umm..."
            show iroha angry with dissolve
            voice "audio/voice/E3/IRO/08/IR/IR015.ogg"
            iroha "..."
            voice "audio/voice/E3/IRO/08/HA/HA008.ogg"
            hachiman "\"Closing it with me?\" you say... What do you mean?"
            show iroha unimpressed with dissolve
            voice "audio/voice/E3/IRO/08/IR/IR016.ogg"
            iroha "I thought you'd go with the flow, senpai..."
            show iroha happy with dissolve
            voice "audio/voice/E3/IRO/08/IR/IR017.ogg"
            iroha "Am I the type of person you would like to get closer to, senpai?"
            hachiman "(Me... Get close to Isshiki Iroha...)"
        "Huh?":
            "not done"
            jump iroha_hallyway_menu
        "...":
            voice "audio/voice/E3/IRO/08/HA/HA010.ogg"
            hachiman "............"
            show iroha blush with dissolve
            voice "audio/voice/E3/IRO/08/IR/IR020.ogg"
            iroha "Senpai, do you want to close that distance with me? Or..."
            voice "audio/voice/E3/IRO/08/HA/HA011.ogg"
            hachiman "Why are you asking me something like that? "
            show iroha happy with dissolve
            voice "audio/voice/E3/IRO/08/IR/IR021.ogg"
            iroha "I was just wondering what I am to you."
            hachiman "(What Isshiki Iroha is... to me?) "

    "We're not a senpai and kouhai at a club, and if I had to say, she's nothing more than \"Isshiki Iroha\" to me."
    "But I was afraid to say that."
    "But on the other hand, saying \"You're irreplacable\" sounds like an insane declaration."
    stop music fadeout 1.0
    show iroha angry with dissolve
    voice "audio/voice/E3/IRO/08/IR/IR022.ogg"
    iroha "..."
    voice "audio/voice/E3/IRO/08/HA/HA012.ogg"
    hachiman  "..."
    play music ["<silence 0.5>", "audio/bgm/BGM36.ogg"]
    show iroha blush with dissolve
    voice "audio/voice/E3/IRO/08/IR/IR023.ogg"
    iroha "*fufu*. It's fine if you don't answer. And anyway, if you interpret my question in a weird way and try to hit on me, that would suck."
    voice "audio/voice/E3/IRO/08/HA/HA013.ogg"
    hachiman  "Right..."
    hachiman "(Shit, that was close. I almost made it weird for her. I'm a real pain in the ass.)"
    show iroha happy with dissolve
    voice "audio/voice/E3/IRO/08/IR/IR024.ogg"
    iroha "But..."
    hide iroha with dissolve
    show iroha school_sunset near_center blush at center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E3/IRO/08/HA/HA014.ogg"
    hachiman "...!"
    voice "audio/voice/E3/IRO/08/IR/IR025.ogg"
    iroha "I was kinda excited just now."
    hide iroha with dissolve
    show iroha school_sunset mid_left vhappy at center with dissolve:
        xoffset -35 yoffset 65
    voice "audio/voice/E3/IRO/08/IR/IR026.ogg"
    iroha "Well, I better get back to work. Laters~."
    hide iroha with dissolve
    play sound "audio/sfx/SE00/SE00_02.ogg"
    hachiman "(What was up with her just now?)"
    hachiman "(...She used me to kill time, huh? Time to go home.)"
    window auto hide dissolve
    stop sound fadeout 0.5
    stop music fadeout 0.5
    #iroha live2d
    call loading_screen(11) from _call_loading_screen_E3_IRO_08
    jump E3_CMM_08
