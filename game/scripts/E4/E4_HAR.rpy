label E4_HAR_02:
    show haruno happy with dissolve
    voice "audio/voice/E4/HAR/02/HR/HR000.ogg"
    haruno "Ah."
    voice "audio/voice/E4/HAR/02/HA/HA000.ogg"
    hachiman "Uh."
    show meguri happy
    show haruno sweater far_center happy at center:
        xoffset 225 yoffset 75
    with dissolve
    hachiman "(Crap, she sees me... And she's beckoning me over.)"
    show haruno vhappy with dissolve
    voice "audio/voice/E4/HAR/02/HR/HR001.ogg"
    haruno "That's the stuff Shizuka-chan gave you, isn't it? Come over here, don't be shy~"
    voice "audio/voice/E4/HAR/02/HA/HA001.ogg"
    hachiman "Ah... Right."
    window auto hide dissolve
    stop voice
    hide meguri
    hide haruno
    with dissolve
    scene kitchenA at truecenter:
        zoom 1.45 xoffset -2.5 yoffset -12.5
    show meguri school mid happy at center:
        xoffset -385 yoffset 75
    show haruno sweater mid_center vhappy at center:
        xoffset 420 yoffset 75
    with dissolve
    $renpy.pause(delay=0.5,hard=True)
    show meguri vhappy with dissolve
    window auto show dissolve
    voice "audio/voice/E4/HAR/02/MG/MG000.ogg"
    meguri "Good work, Hikigaya-kun! I'm sorry I finished without you."
    voice "audio/voice/E4/HAR/02/HA/HA002.ogg"
    hachiman "It's fine..."
    hachiman "(Besides, you're both good at what you do... I'm not sure if I'm bearing an inferiority complex, but isn't Meguri-senpai just amazing?)"
    voice "audio/voice/E4/HAR/02/HA/HA003.ogg"
    hachiman "Erm, what are you making? It looks something really elaborate."
    show haruno happy with dissolve
    voice "audio/voice/E4/HAR/02/HR/HR002.ogg"
    haruno "Hm? Are you curious~?"
    voice "audio/voice/E4/HAR/02/HA/HA004.ogg"
    hachiman "More or less..."
    show haruno vhappy with dissolve
    voice "audio/voice/E4/HAR/02/HR/HR003.ogg"
    haruno "But I guess you'll have to wait until it's done. Right, Meguri?"
    show meguri happy with dissolve
    voice "audio/voice/E4/HAR/02/MG/MG001.ogg"
    meguri "Right. We're not sure if we can even make it yet."
    show haruno mid_left happy at center with dissolve:
        xoffset 385 yoffset 75
    voice "audio/voice/E4/HAR/02/HR/HR004.ogg"
    haruno "Meguri is always so humble... I've made it plenty of times, so it's gonna be fine."
    show meguri vhappy with dissolve
    voice "audio/voice/E4/HAR/02/MG/MG002.ogg"
    meguri "Hearing Haru-san say that is such a confidence boost."
    hachiman "(It's a bit awkward being the third wheel in this conversation...)"
    show haruno sweater mid_center vhappy at center:
        xoffset 420 yoffset 75
    voice "audio/voice/E4/HAR/02/HR/HR005.ogg"
    haruno "Hikigaya-kun, which type of chocolate do you prefer? More mature looking ones or cuter ones?"
    voice "audio/voice/E4/HAR/02/HA/HA005.ogg"
    hachiman "I don't know if there can be anything \"mature\" or \"cute\" about a chocolate."
    voice "audio/voice/E4/HAR/02/MG/MG003.ogg"
    menu choco_type:
        meguri "Ah, I want to know, too! So, which one is it, Hikigaya-kun?"
        with dissolve
        "Mature-looking":
            $chocoEventHelp = "haruno"
            voice "audio/voice/E4/HAR/02/HA/HA006.ogg"
            hachiman "Well, if I had to pick... I guess I'll go with mature..."
            hachiman "(The whole place smelled so sweet and chocolatey that, so \"adult\" probably means something like \"a bit less sweet\"."
            show meguri happy with dissolve
            voice "audio/voice/E4/HAR/02/MG/MG004.ogg"
            meguri "Oh? So you prefer Haru-san's then~!"
            hachiman "(Wait, we're being that specific?)"
            show haruno surprised with dissolve
            voice "audio/voice/E4/HAR/02/HR/HR006.ogg"
            haruno "............"
            voice "audio/voice/E4/HAR/02/HA/HA007.ogg"
            hachiman "Wh-what's the matter?"
            show haruno happy with dissolve
            voice "audio/voice/E4/HAR/02/HR/HR007.ogg"
            haruno "Huh? Oh, it's nothing. That was just a bit unexpected."
            voice "audio/voice/E4/HAR/02/HA/HA008.ogg"
            hachiman "Unexpected. huh?"
            voice "audio/voice/E4/HAR/02/HR/HR008.ogg"
            haruno "Hikigaya-kun, I thought you had a weakness for cute things since you have a little sister."
            voice "audio/voice/E4/HAR/02/HA/HA009.ogg"
            hachiman "No, can't say I do."
            show meguri vhappy with dissolve
            voice "audio/voice/E4/HAR/02/MG/MG005.ogg"
            meguri "Oh! You have a little sister, so if we flip that around, you have a thing for big sister types! Or something?"
            voice "audio/voice/E4/HAR/02/HA/HA010.ogg"
            hachiman "I wouldn't say that's the case either..."
            show meguri unimpressed with dissolve
            voice "audio/voice/E4/HAR/02/MG/MG006.ogg"
            meguri "......?"
            voice "audio/voice/E4/HAR/02/HA/HA011.ogg"
            hachiman "It doesn't matter if it's older, younger or the same age - I'm weak against all of them."
            show haruno vhappy with dissolve
            voice "audio/voice/E4/HAR/02/HR/HR009.ogg"
            haruno "*Pfft*, haha! So that's how it is. I like the way you got out of that."
            voice "audio/voice/E4/HAR/02/HA/HA012.ogg"
            hachiman "I was just telling the truth, though..."
            window auto hide dissolve
            stop voice
            stop music fadeout 1.0
            hide meguri
            hide haruno
            with dissolve
            jump E4_HAR_03
        "Cute-looking":
            $chocoEventHelp = "meguri"
            voice "audio/voice/E4/HAR/02/HA/HA013.ogg"
            hachiman "Ah. If I had to pick, I'd go with the cute ones I guess..."
            hachiman "(As a sweet tooth, I'm biased, and I'm guessing the cute-looking ones will have more of a chocolate-y taste.)"
            show haruno mid_left happy at center with dissolve:
                xoffset 385 yoffset 75
            voice "audio/voice/E4/HAR/02/HR/HR010.ogg"
            haruno "Hmph. I guess it'd be Meguri's then."
            hachiman "(Huh? Was I really pickng sides with that one?)"
            show meguri happy with dissolve
            voice "audio/voice/E4/HAR/02/MG/MG007.ogg"
            meguri "I went all out today and made them super cutesy!"
            "Seeing Meguri-senpai puffing out her chest with satisfaction, I felt a sweetness spread in my mouth even though I hadn't eaten any chocolate."
            hachiman "(The Megrishu☆ effect is amazing! It's perfect for no-sugar diets!)"
            window auto hide dissolve
            stop voice
            hide haruno
            hide meguri
            with dissolve
            stop music fadeout 0.5
            $renpy.pause(delay=0.5,hard=True)
            jump E4_HAR_04
            #continue with voices from audio/voice/E4/HAR/04

label E4_HAR_03:
    show haruno sweater mid_center vhappy at center with dissolve:
        xoffset 10 yoffset 75
    play music "audio/bgm/BGM35.ogg"
    window auto show dissolve
    voice "audio/voice/E4/HAR/03/HA/HA000.ogg"
    hachiman "Ah, that's Matcha isn't it? What are you using it for?"
    image haruno sweater mid_left happy flat = Flatten("haruno sweater mid_left happy")
    show haruno sweater mid_left happy flat at center with dissolve:
        xoffset -20 yoffset 75
        on hide:
            parallel:
                linear 0.4 alpha 0
            parallel:
                easeout 0.4 xoffset -100
    voice "audio/voice/E4/HAR/03/HR/HR000.ogg"
    haruno "That's a secret. Now then, I wonder if it's ready~?"
    hide haruno
    $renpy.pause(delay=0.4, hard=True)
    "After a quick wash of her hands, Haruno-san checks the oven, mutters something about it being almost ready, and begins chopping up the chunks of chocolate."
    hachiman "(Woah, she's pretty good at this.)"
    show haruno sweater mid_center happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E4/HAR/03/HR/HR001.ogg"
    haruno "So, what kind of chocolate do you really like?"
    voice "audio/voice/E4/HAR/03/HA/HA000.ogg"
    hachiman "I'm sure I should be happy to receive any kind. I often buy and eat chocolate myself..."
    voice "audio/voice/E4/HAR/03/HR/HR002.ogg"
    haruno "I see. I thought you had a sweet tooth."
    window auto hide dissolve
    stop voice
    scene kitchenA with dissolve
    window auto show dissolve
    "While we were having this conversation, I aimlessly look around the venue."
    "Miura and Isshiki were sizing each other up while making their respective chocolates, with Hayama being there to handle it in a peaceful and equitable manner. Right beside him, Tobe is frolicking "
    "around and Ebina's keeping him in check with her rotten jokes."
    "At a nearby table, Yuigahama is frantically kneading dough under Yukinoshita's watchful eye, while Tamanawa and his friends are hard at work exchanging bogus marketing terms, and the Kawasaki sisters "
    "are also sparing no effort."
    "The air was filled with a sweet scent and a sense of fun and excitement. As expected of a chocolate testing event - it was a success. I'd say so at least."
    "\"This is fun...\", I mumbled out."
    "It's probably my own fault I can't quite get into the whole atmosphere."
    window auto hide dissolve
    scene kitchenA at truecenter:
        zoom 1.45 xoffset -2.5 yoffset -12.5
    show haruno sweater mid_center happy at center:
        xoffset 10 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E4/HAR/03/HR/HR003.ogg"
    haruno "You have quite the captivating look on your face."
    voice "audio/voice/E4/HAR/03/HA/HA001.ogg"
    hachiman "I know, right? I've been told my eyes are particuarly charming."
    show haruno vhappy with dissolve
    voice "audio/voice/E4/HAR/03/HR/HR004.ogg"
    haruno "...That's true. But you do look like you're particularly bored."
    voice "audio/voice/E4/HAR/03/HA/HA002.ogg"
    hachiman "...Do I now?"
    show haruno happy with dissolve
    voice "audio/voice/E4/HAR/03/HR/HR005.ogg"
    haruno "Well, there are a lot of liars here. And it doesn't look like anything interesting is going to happen."
    voice "audio/voice/E4/HAR/03/HA/HA003.ogg"
    hachiman "............"
    voice "audio/voice/E4/HAR/03/HR/HR006.ogg"
    haruno "You're the one who set this event up, right? Then, is this your supposed genunine article?"
    show haruno annoyed with dissolve
    voice "audio/voice/E4/HAR/03/HR/HR007.ogg"
    haruno "Is the time you spent here what you called the real thing?"
    "As soon as she said that, a chill ran down my spine and I turned my head away from her."
    hide haruno with dissolve
    show haruno sweater near_center annoyed at center with dissolve:
        xoffset -20 yoffset 75
    "But Haruno-san didn't let me run away, and closed the distance between us with a single step"
    voice "audio/voice/E4/HAR/03/HA/HA004.ogg"
    hachiman "...I don't really know."
    "I could only give one such meaningless reply. There was a coldness in Haruno-san's tone, but at the same time her voice was somehow innocuosly inquisitive."
    "It sounded like a confession of incomprehension, as if she actually could't understand, which threw me off."
    show haruno sad with dissolve
    voice "audio/voice/E4/HAR/03/HR/HR008.ogg"
    haruno "Is that all? ...I wouldn't have thought you were that kind of guy. Are you that boring?"
    "She is so close that I can feel her breath on my face, and I can almost touch her skin if I move even a little bit, but her words seem to be coming from terribly far away."
    voice "audio/voice/E4/HAR/03/HA/HA005.ogg"
    hachiman "If I were that interesting, I'd be the most popular guy in the class."
    show haruno happy with dissolve
    voice "audio/voice/E4/HAR/03/HR/HR009.ogg"
    haruno "I like that about you."
    "As I listened to her playful, seductive voice, I clearly understood what she was trying to say."
    "She said it implicitly. That it's not possible for something like this to be real."
    "I agree. If nothing else, these days, these relationships--I can't help but feel uncomfortable. I'm not used to this. I've never experienced anything like it before. "
    "But I thought it might pass. I thought that as time went on, I'd get used to these feelings and learn to accept them."
    "But still--I can't shake this restlessness."
    "Like shrapnel worming its way closer and closer to my heart, I felt it. A phantom chill of sorts. The dark discomfort that I'd avoided until now."
    "And Yukinoshita Haruno had confronted me with that reality."
    voice "audio/voice/E4/HAR/03/HR/HR010.ogg"
    haruno "You don't look like you're enjoying this event. That's a relief..."
    voice "audio/voice/E4/HAR/03/HA/HA006.ogg"
    hachiman "That's..."
    show haruno vhappy with dissolve
    "When I made eye contact with her, Haruno-san smiled at me as if nothing had happened."
    show haruno sweater mid_center happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E4/HAR/03/HR/HR011.ogg"
    haruno "Well, I'll treat you something special, so wait a little longer, Mr. Taste-Tester."
    voice "audio/voice/E4/HAR/03/HA/HA007.ogg"
    hachiman "Sure..."
    hachiman "(Why would she say that to me...?)"
    window auto hide dissolve
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    scene kitchenA with Fade(1.0, 1.0, 1.0)
    play ambient "audio/sfx/SE05/SE05_01L.ogg"
    play music "audio/bgm/BGM17.ogg"
    window auto show dissolve
    hachiman "(At any rate, the air in the venue had already adapted a chocolate-y scent.)"
    "No matter how much of a sweet tooth I have, the smell of western sweets filling my lungs is giving me heartburn, so I decide to go outside and get some air."
    hachiman "(Right now, I'd rather go for Houjicha or some tea rather than Max Coffee.)"
    window auto hide dissolve
    stop ambient
    jump E4_YMK_07

label E4_HAR_04:
    show meguri school mid happy at center with dissolve:
        xoffset 25 yoffset 75
    play music "audio/bgm/BGM17.ogg"
    window auto show dissolve
    voice "audio/voice/E4/HAR/04/MG/MG000.ogg"
    meguri "Al~right. Now that the meringue is ready, it's time for the macaronage."
    voice "audio/voice/E4/HAR/04/HA/HA000.ogg"
    hachiman "Oh, macaronage..."
    "Hearing the unfamiliar word, I'd unintentionally repeated what she said."
    show meguri vhappy with dissolve
    voice "audio/voice/E4/HAR/04/MG/MG001.ogg"
    meguri "Well see, it's the process of making the macaron dough!"
    voice "audio/voice/E4/HAR/04/HA/HA001.ogg"
    hachiman "Oh, macaron..."
    "I was at the level of wondering what a \"macaron\" was, but not minding my head being full of question marks, Meguri-senpai continued her explanation."
    hachiman "(Hachiman gets she's apparently making something called \"macaron\".)"
    show meguri happy with dissolve
    voice "audio/voice/E4/HAR/04/MG/MG002.ogg"
    meguri "First, you have to mix the flour with the meringue without breaking it's bubbles, but then you have to go ahead and flatten them afterwards. It's pretty hard~"
    hachiman "(Mix them without crushing, and then flatten? How?)"
    image haruno_sweater_flat = Flatten("haruno sweater mid_left vhappy")
    show haruno_sweater_flat at right:
        xoffset 20 yoffset 75 alpha 0
        on show:
            parallel:
                linear 0.25 alpha 1
            parallel:
                linear 0.25 xoffset -45
    voice "audio/voice/E4/HAR/04/HR/HR000.ogg"
    haruno "Hahaha. Hikigaya-kun, you're looking lost at sea right now. Meguri, why don't you show him how it's done?"
    hide haruno_sweater_flat
    show haruno sweater mid_left vhappy at right:
        xoffset -45 yoffset 75
    stop ambient
    stop music
    show meguri angry with dissolve
    voice "audio/voice/E4/HAR/04/MG/MG003.ogg"
    meguri "Alright. Two, three..."
    play music "audio/bgm/BGM16.ogg"
    play ambient "audio/sfx/SE01/SE01_17.ogg"
    "With a huff, Meguri-senpai got herself fired up, and started throwing in something white and some kind of brown powder. As they landed in the bowl one after the other, she began skillfully mixing them together."
    "She looks at it, lets out a big, content sigh, and rubs a mixture onto the rim of the bowl with a spatula."
    show haruno happy with dissolve
    voice "audio/voice/E4/HAR/04/HR/HR001.ogg"
    haruno "She's working on the macaronage right now. Look, it's getting glossier."
    voice "audio/voice/E4/HAR/04/HA/HA001.ogg"
    hachiman "...It really is."
    show haruno annoyed with dissolve
    voice "audio/voice/E4/HAR/04/HR/HR002.ogg"
    haruno "Meguri, stop."
    stop ambient fadeout 0.5
    voice "audio/voice/E4/HAR/04/MG/MG004.ogg"
    meguri "Roger!"
    "Right at Haruno's command, Meguri-senpai stopped her hand and took a deep breath."
    stop ambient fadeout 1.0
    show meguri vhappy
    show haruno happy
    with dissolve
    stop music
    voice "audio/voice/E4/HAR/04/MG/MG005.ogg"
    meguri "Phew, thank you, Haru-san! It's too hard to find the sweet spot and not overdo this!"
    play music "audio/bgm/BGM34.ogg"
    voice "audio/voice/E4/HAR/04/HR/HR003.ogg"
    haruno "Well, it looks like we only need to bake it now. Good job, Meguri."
    voice "audio/voice/E4/HAR/04/MG/MG006.ogg"
    meguri "No biggie. We shouldn't lose focus until the end."
    hide haruno with dissolve
    show meguri happy with dissolve
    "After lightly slapping her own cheek, Meguri-senpai put the dough into a pastry bag and began to slowly squeeze it out onto the baking paper."
    image irohaflat001 = Flatten("iroha school mid_center vhappy")
    show irohaflat001 at left:
        xoffset 50 yoffset 75 alpha 0
        on show:
            parallel:
                linear 0.25 alpha 1
            parallel:
                linear 0.25 xoffset 110
    voice "audio/voice/E4/HAR/04/IR/IR000.ogg"
    iroha "Wah, are these heart-shaped chocolate macaron~?"
    hide irohaflat001
    show iroha school mid_center vhappy at left:
        xoffset 110 yoffset 75
    show meguri vhappy with dissolve
    voice "audio/voice/E4/HAR/04/MG/MG007.ogg"
    meguri "Yep. We're at an event and all, so I wanted to make them cute!"
    hachiman "(So this mysterious shape will turn into a heart...)"
    image yuiflat001 = Flatten("yui school mid_left vhappy")
    show yuiflat001 at right:
        xoffset 0 yoffset 70 alpha 0
        on show:
            parallel:
                linear 0.25 alpha 1
            parallel:
                linear 0.25 xoffset -80
    voice "audio/voice/E4/HAR/04/YI/YI000.ogg"
    yui "Wah! Shiromeguri-senpai, they're so cute! I want to make them like that one day, too!"
    hide yuiflat001
    show yui school mid_left vhappy at right behind meguri:
        xoffset -80 yoffset 70
    voice "audio/voice/E4/HAR/04/YK/YK000.ogg"
    yukino "Be carerful not to overbake your own cookies first and foremost, Yuigahama-san."
    show yui mid_right sad with dissolve:
        xoffset -45 yoffset 75
    voice "audio/voice/E4/HAR/04/YI/YI001.ogg"
    yui "Right..."
    show yui:
        parallel:
            linear 0.25 xoffset 10
        parallel:
            linear 0.25 alpha 0
    $renpy.pause(delay=0.25,hard=True)
    hide yui
    show meguri happy with dissolve
    voice "audio/voice/E4/HAR/04/MG/MG008.ogg"
    meguri "Alrighty! It's about time we get to baking them."
    show iroha mid_left surprised with dissolve:
        xoffset 50 yoffset 70
    voice "audio/voice/E4/HAR/04/IR/IR001.ogg"
    iroha "Ah! I have to finish mine, too."
    show iroha:
        parallel:
            linear 0.25 xoffset -10
        parallel:
            linear 0.25 alpha 0
    $renpy.pause(delay=0.25,hard=True)
    hide iroha
    hide meguri with dissolve
    show haruno sweater mid_center happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E4/HAR/04/HR/HR004.ogg"
    haruno "Yukino-chan should've at least had some fun making her own, too~"
    voice "audio/voice/E4/HAR/04/HA/HA003.ogg"
    hachiman "Probably doesn't have the time to right now..."
    hachiman "(She's preoccupied with all kind of things...)"
    show haruno vhappy with dissolve
    voice "audio/voice/E4/HAR/04/HR/HR005.ogg"
    haruno "I guess so~"
    hide haruno with dissolve
    show meguri school mid happy at center:
        xoffset -385 yoffset 75
    show haruno sweater mid_center vhappy at center:
        xoffset 420 yoffset 75
    with dissolve
    voice "audio/voice/E4/HAR/04/HA/HA004.ogg"
    hachiman "By the way, you're suprisingly deft, Shiromeguri-senpai."
    show meguri frown with dissolve
    voice "audio/voice/E4/HAR/04/MG/MG009.ogg"
    meguri "Eh? I'm always pretty deft."
    voice "audio/voice/E4/HAR/04/HA/HA005.ogg"
    hachiman "Ah, I mean, surprisingly in like a good way..."
    show haruno happy with dissolve
    voice "audio/voice/E4/HAR/04/HR/HR006.ogg"
    haruno "Well, judging by appearances, you'd think so. I can assure you though, her sweets are great."
    show meguri happy with dissolve
    voice "audio/voice/E4/HAR/04/MG/MG010.ogg"
    meguri "Yep. I've got Haru-san's seal of approval. Look forward to them, Hikigaya-kun."
    voice "audio/voice/E4/HAR/04/HA/HA006.ogg"
    hachiman "Eh? Ah, I will..."
    hachiman "(I don't even really know what a \"macaron\" is!)"
    hide meguri
    hide haruno
    with dissolve
    $renpy.pause(delay=0.25,hard=True)
    play sound "audio/sfx/SE01/SE01_19.ogg"
    "A faint, sweet arima begins to waft from the oven nearby. Looking around, I began to hear little cheers of joy from the other tables."
    stop sound
    hachiman "(Oh, Miura's embarrassed by Yukinoshita praising her. You don't see that everyday.)"
    "I had a feeling this event was going to be nothing but exhausting, yet I think I'm kind of glad I came in the end. As I was lost in thought, Meguri-senpai called out to me."
    show meguri school mid vhappy at center with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E4/HAR/04/MG/MG011.ogg"
    meguri "I'm glad the event turned out great! Everybody's having fun!"
    voice "audio/voice/E4/HAR/04/HA/HA007.ogg"
    hachiman "Yeah."
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    jump E4_CMM_05

label E4_HAR_05:
    show haruno happy with dissolve
    voice "audio/voice/E4/HAR/05/HR/HR000.ogg"
    haruno "Skiing, huh? It's been a minute~"
    voice "audio/voice/E4/HAR/05/MG/MG000.ogg"
    meguri "I'm so looking forward to skiing with you, Haru-san!"
    voice "audio/voice/E4/HAR/05/SZ/SZ000.ogg"
    hiratsuka "Come to think of it, I haven't skied in a while. This might be a good opportunity."
    show haruno vhappy with dissolve
    voice "audio/voice/E4/HAR/05/HR/HR001.ogg"
    haruno "I know, right? Besides, Shizuka-chan, we can use this chance and drink together."
    show meguri happy with dissolve
    voice "audio/voice/E4/HAR/05/MG/MG001.ogg"
    meguri "Oh, did you know the lodge has a hot spring? Ahh... A drink after a nice hot bath... I can almost taste it!"
    show haruno happy with dissolve
    voice "audio/voice/E4/HAR/05/HR/HR002.ogg"
    haruno "I think Meguri can join us for a bit, no?"
    show hiratsuka angry with dissolve
    voice "audio/voice/E4/HAR/05/SZ/SZ001.ogg"
    hiratsuka "Hold it, Haruno. Don't encourage minors to drink."
    show haruno sad with dissolve
    voice "audio/voice/E4/HAR/05/HR/HR003.ogg"
    haruno "Yeah, yeah. You're such a stickler, Shizuka-chan~"
    show hiratsuka pout with dissolve
    voice "audio/voice/E4/HAR/05/SZ/SZ002.ogg"
    hiratsuka "Of course I am. I'm a homeroom teacher, just what did you think I'd say?"
    hachiman "(Aren't these guys strangely getting more excited than anyone else?)"
    show meguri vhappy with dissolve
    voice "audio/voice/E4/HAR/05/MG/MG002.ogg"
    meguri "Ah, Hikigaya-kun! You must be so excited to go skiing!"
    show haruno sweater_sunset mid_center happy at right with dissolve:
        xoffset -170 yoffset 75
    voice "audio/voice/E4/HAR/05/HA/HA000.ogg"
    hachiman "Ah... I guess..."
    show haruno sly with dissolve
    voice "audio/voice/E4/HAR/05/HR/HR004.ogg"
    haruno "You don't seem to be too excited about it. Do you dislike events like this after all?"
    voice "audio/voice/E4/HAR/05/HA/HA001.ogg"
    hachiman "Huh, well... Besides, I find it curious that you seem so keen on this."
    show haruno happy with dissolve
    voice "audio/voice/E4/HAR/05/HR/HR005.ogg"
    haruno "It's because we're all going as a big group. I personally want to go skiing with Shizuka and Meguri, so it's perfect."
    hachiman "(Is that how it is? Is that what you want? Am I overthinking this?)"
    voice "audio/voice/E4/HAR/05/HA/HA002.ogg"
    hachiman "Well, I've never skied, and I'm not particularly interested in it, so I don't know how I feel about it."
    show haruno vhappy with dissolve
    voice "audio/voice/E4/HAR/05/HR/HR006.ogg"
    haruno "You didn't immediately decide you didn't like it. Good boy, well done."
    show hiratsuka happy with dissolve
    voice "audio/voice/E4/HAR/05/SZ/SZ003.ogg"
    hiratsuka "Mm, try it, and you might be surprised at how much fine it is."
    show meguri happy with dissolve
    voice "audio/voice/E4/HAR/05/MG/MG003.ogg"
    meguri "Right! And sliding down as fast as you can feels so good!"
    hachiman "(Just your words alone are enough to make me feel so good, Meguri-senpai. I don't have to go skiing anymore, do I?)"
    voice "audio/voice/E4/HAR/05/HR/HR007.ogg"
    haruno "So, if you're still on the fence about it, let me give you a little push."
    show haruno happy with dissolve
    voice "audio/voice/E4/HAR/05/HR/HR008.ogg"
    haruno "There's something about the sight of the opposite sex in an outfit you don't get to see often that really gets you going, isn't there? Swimsuits, yukata, ski wear, etc."
    voice "audio/voice/E4/HAR/05/HA/HA003.ogg"
    hachiman "Right..."
    hachiman "(Well, that's true...)"
    stop music
    show haruno sly with dissolve
    voice "audio/voice/E4/HAR/05/HR/HR009.ogg"
    haruno "Well then. You've got two beautiful girls here. Who do you want to see more in ski wear, me or Meguri?"
    voice "audio/voice/E4/HAR/05/HA/HA004.ogg"
    hachiman "Come again?"
    show meguri surprised with dissolve
    play music "audio/bgm/BGM44.ogg"
    voice "audio/voice/E4/HAR/05/MG/MG004.ogg"
    meguri "What? T-that's embarrassing..."
    "That's like publicly announcing who you care more about. Meguri is waving her arms in embarrassment, while Hiratsuka-sensei is looking at me with interest in her eyes."
    "And Haruno-san was waiting for my answer with a grin on her face, just like she does when she comes up with a nasty way to dunk on me."
    hachiman "(Why is she always playing with me? Don't go leaving Hiratsuka-sensei out of the choice so casually, either!)"
    hide hiratsuka
    hide meguri
    hide haruno
    with dissolve
    hachiman "(The people who might be able to bail me out of this situation are...)"
    window auto hide dissolve
    scene kitchenB at truecenter:
        zoom 1.45 xalign 0 yoffset -15
    show yukino school_sunset mid_center pout at center:
        xoffset -345 yoffset 75
    show yui school_sunset mid_left vhappy at center:
        xoffset 250 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E4/HAR/05/YK/YK000.ogg"
    yukino "............"
    hachiman "(Yuigahama persuaded me into something... And Hayama is...)"
    window auto hide dissolve
    scene kitchenB at truecenter:
        zoom 1.45 xalign 1.0 yoffset -15
    show tobe school_sunset mid vhappy at left:
        xoffset -55 yoffset 75
    show ebina school_sunset mid_center happy at center:
        xoffset -175 yoffset 75
    show yumiko school_sunset mid_center pout at right:
        xoffset -5 yoffset 75
    with dissolve
    window auto show dissolve
    hachiman "(Always gone when you need him the most. Give me a break!)"
    window auto hide dissolve
    scene kitchenB
    show hiratsuka school_light_sunset mid_center happy at left:
        xoffset -15 yoffset 75
    show meguri school_sunset mid happy at center:
        xoffset 25 yoffset 75
    show haruno sweater_sunset mid_center sly at right:
        xoffset -170 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E4/HAR/05/HR/HR010.ogg"
    haruno "Well? Hurry up and pick."
    voice "audio/voice/E4/HAR/05/HA/HA005.ogg"
    menu ski_wear_menu:
        hachiman "Well, then..."
        with dissolve
        "Haruno-san":
            $chocoEventChoice = "haurno"
            voice "audio/voice/E4/HAR/05/HA/HA006.ogg"
            hachiman "Yukinoshita-san, I guess. You look good no matter what you wear, so I'm interested."
            "Rather, I think I am more interested in how she would react. But Haruno-san is..."
            play music "audio/bgm/BGM35.ogg"
            show haruno worried with dissolve
            voice "audio/voice/E4/HAR/05/HR/HR011.ogg"
            haruno "...You're lying."
            voice "audio/voice/E4/HAR/05/HA/HA007.ogg"
            hachiman "No, I'm not... I think you look good no matter what you wear..."
            voice "audio/voice/E4/HAR/05/HR/HR012.ogg"
            show haruno angry with dissolve
            haruno "It feels like you're telling me it doesn't matter what I'm wearing."
            hachiman "(...So bothersome.)"
            show hiratsuka vhappy with dissolve
            voice "audio/voice/E4/HAR/06/SZ/SZ000.ogg"
            hiratsuka "Haruno, you don't have to be so bashful."
            hachiman "(What? Was she embarrassed?)"
            voice "audio/voice/E4/HAR/06/HR/HR000.ogg"
            haruno "I won't embarrassed by that kind of compliment. I'm used to receiving compliments like that."
            voice "audio/voice/E4/HAR/06/SZ/SZ001.ogg"
            hiratsuka "You seem to have been teasing him, though."
            voice "audio/voice/E4/HAR/06/HR/HR001.ogg"
            haruno "...Depends on who the person is."
            hachiman "(I'm surprised to see such a reaction...)"
            show meguri vhappy with dissolve
            voice "audio/voice/E4/HAR/06/MG/MG000.ogg"
            meguri "But, I'd like to see you in you ski wear too. Haru-san is really cool. And you ski really well!"
            show hiratsuka happy with dissolve
            voice "audio/voice/E4/HAR/06/HA/HA000.ogg"
            hachiman "Since she's a perfectionist, she ought to be a good skier."
            show haruno happy with dissolve
            voice "audio/voice/E4/HAR/06/HR/HR002.ogg"
            haruno "What's with the perfectionist thing?"
            voice "audio/voice/E4/HAR/06/HA/HA001.ogg"
            hachiman "Nothing, I'm just talking to myself."
            show haruno vhappy with dissolve
            voice "audio/voice/E4/HAR/06/HR/HR003.ogg"
            haruno "Well, I think skiing \"will\" be exciting. I think it'd be just right for you."
            voice "audio/voice/E4/HAR/06/HA/HA002.ogg"
            hachiman "Well, I wouldn't be so sure..."
            window auto hide dissolve
            stop music fadeout 1.0
            jump E5_CMM_01
        "Meguri-senpai":
            $chocoEventChoice = "meguri"
            stop music fadeout 1.0
            voice "audio/voice/E4/HAR/05/HA/HA008.ogg"
            hachiman "Shiromeguri-senpai."
            "I didn't know what to make of this, but it occured to me that Meguri-senpai in her ski wear could easily produce the Mega Resurrection effect, so that's what I went with."
            play music "audio/bgm/BGM17.ogg"
            show meguri surprised with dissolve
            voice "audio/voice/E4/HAR/05/MG/MG005.ogg"
            meguri "Huh?! My ski wear is not that exciting! I never thought you were that kind of boy to say stuff like that."
            hachiman "(It's because this broad forced me to say it!)"
            voice "audio/voice/E4/HAR/07/HR/HR000.ogg"
            haruno "Oh~?"
            voice "audio/voice/E4/HAR/07/HA/HA000.ogg"
            hachiman "What?"
            show haruno vhappy with dissolve
            voice "audio/voice/E4/HAR/07/HR/HR001.ogg"
            haruno "You were imagining Meguri in her cute, fluffy ski outfit, weren't you?"
            voice "audio/voice/E4/HAR/07/HA/HA001.ogg"
            hachiman "Ah, maybe..."
            hachiman "(Meguri-senpai's image is so dazzling... It's befitting more of meringue than a ski slope...)"
            voice "audio/voice/E4/HAR/07/HR/HR002.ogg"
            haruno "Well, no surprises there, Meguri is a cutie after all~"
            voice "audio/voice/E4/HAR/07/HA/HA002.ogg"
            hachiman "Well, I'd have to agree..."
            voice "audio/voice/E4/HAR/07/MG/MG000.ogg"
            meguri "Huh!? H-Hikigaya-kun, not you too! It's not really like I'm... Ah, I feel so embarrassed... Geez, you guys! I'm blushing..."
            hachiman "(I'm starting to feel embarrassed myself...)"
            window auto hide dissolve
            stop music fadeout 1.0
            jump E5_CMM_01
