label E2_IRO_01:
    #audio form "audio/voice/E2/IRO/01"
    show komachi pout with dissolve
    voice "audio/voice/E2/IRO/01/KO/KO000.ogg"
    komachi "Sorry, onii-chan. I pressed the wrong button."
    hachiman "(Although I have a bad feeling about this, since it's already connected, it's not so nice to hang up now...)"
    voice "audio/voice/E2/IRO/01/HA/HA000.ogg"
    hachiman "...Ah, it's fine. It's already connected."
    hide komachi with dissolve
    voice "audio/voice/E2/IRO/01/HA/HA001.ogg"
    hachiman "Hello?"
    voice "audio/voice/E2/IRO/01/IR/IR000.ogg"
    iroha "Hello~ Senpai?"
    hachiman "(That voice... it's Isshiki.)"
    voice "audio/voice/E2/IRO/01/IR/IR001.ogg"
    iroha "Could you come to the front of the station for a bit?"
    voice "audio/voice/E2/IRO/01/HA/HA002.ogg"
    hachiman "Eh... What for?"
    voice "audio/voice/E2/IRO/01/IR/IR001_a.ogg"
    iroha "There's a cake shop there that I've been wanting to go to and besides, if there's the 2 of us we'd be able to try many different cakes~"
    voice "audio/voice/E2/IRO/01/IR/IR002.ogg"
    iroha "So how about meeting up 30 minutes from now?"
    voice "audio/voice/E2/IRO/01/HA/HA003.ogg"
    hachiman "Don't know... Isn't it better for you to invite Hayama for this type of thing?"
    voice "audio/voice/E2/IRO/01/IR/IR003.ogg"
    iroha "Hayama-senpai is really busy plus won't it make for a bad start to the year if I get rejected? Besides, you're totally free anyways."
    hachiman "(Why did you think I'd be free? ...Well, it's true right I guess.)"
    voice "audio/voice/E2/IRO/01/HA/HA004.ogg"
    hachiman "I got a few things to do despite what it might seem..."
    voice "audio/voice/E2/IRO/01/IR/IR004.ogg"
    iroha "Oh, if you bring a cake back home for your sister, wouldn't she be pretty happy about it?"
    voice "audio/voice/E2/IRO/01/HA/HA005.ogg"
    hachiman "That might be true..."
    voice "audio/voice/E2/IRO/01/IR/IR005.ogg"
    iroha "Right~? Your sister... um, what was her name again? \"Komeno\" something..."
    voice "audio/voice/E2/IRO/01/HA/HA006.ogg"
    hachiman "Not \"kome\", Komachi. Hikigaya Komachi."
    voice "audio/voice/E2/IRO/01/IR/IR006.ogg"
    iroha "Right, right, Komachi-chan! Something sweet is just what she needs to get her through exam prep."
    voice "audio/voice/E2/IRO/01/HA/HA007.ogg"
    hachiman "That's true."
    voice "audio/voice/E2/IRO/01/IR/IR007.ogg"
    iroha "Okay, it's decided! Let's meet in front of the station in 30 mins."
    voice "audio/voice/E2/IRO/01/IR/IR008.ogg"
    iroha "...Senpai, please don't be late, okay?"
    stop music
    "She spoke in a sweet voice and suddenly hung up."
    window auto hide dissolve
    scene skyA with Fade(1.0, 0.5, 1.0)
    play music ["<silence 0.3>", "audio/bgm/BGM41.ogg"]
    window auto show dissolve
    voice "audio/voice/E2/IRO/01/IR/IR009.ogg"
    iroha "Senpai~! Hurry up! I'm over here!"
    voice "audio/voice/E2/IRO/01/IR/IR010.ogg"
    iroha "I've been wanting to come here for a long time. I'm so glad you had the time to come with me~"
    voice "audio/voice/E2/IRO/01/HA/HA008.ogg"
    hachiman "...I guess?"
    window auto hide dissolve
    scene cakeShopA with dissolve
    window auto show dissolve
    "The shop that I followed Isshiki into was a classy cake shop."
    hachiman "(I may have realized this too late, but... aren't I ill-suited for a place like this? It's so fluffy looking I'm feeling like a sponge cake myself.)"
    window auto hide dissolve
    $renpy.pause(delay=0.5, hard=True)
    scene cakeShopA:
        zoom 1.8 xalign 1.0 ypos -435
    show iroha coat mid_center vhappy at center:
        xoffset 25 yoffset 75
    with dissolve
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E2/IRO/01/IR/IR011.ogg"
    iroha "Wooow, they all look so good, I can't decide~! Senpai, which one catches your eye?"
    voice "audio/voice/E2/IRO/01/HA/HA009.ogg"
    hachiman "Does it really matter? They're all really cute looking, right? You'll look good next to any one of them."
    show iroha unimpressed with dissolve
    voice "audio/voice/E2/IRO/01/IR/IR012.ogg"
    iroha "That's such a lazy answer, senpai... Jeez, what do you take me for?"
    hachiman "(That's my line... What are you taking me for? If I really said which one I'd prefer, I'd probably get a nasty reply, so I keep quiet.)"
    voice "audio/voice/E2/IRO/01/HA/HA010.ogg"
    hachiman "Just hurry up and choose already."
    show iroha happy with dissolve
    voice "audio/voice/E2/IRO/01/IR/IR013.ogg"
    iroha "Ah, here we are. I'll go with this one, and this one... senpai, can I get the cakes from the first row to the fourth one?"
    voice "audio/voice/E2/IRO/01/HA/HA011.ogg"
    hachiman "Hang on? Can you please not be in such a squandering mood? I'm not a rich tycoon or something."
    show iroha vhappy with dissolve
    voice "audio/voice/E2/IRO/01/IR/IR014.ogg"
    iroha "I'm just joking~"
    "That didn't sound like a joke to me. Though she ended up ordering 2 cakes for herself and 4 for me."
    window auto hide dissolve
    stop music fadeout 0.5
    show irohaCakeShop
    with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/BGM09.ogg"
    play sound "<from 0 to 1.5>audio/sfx/SE01/SE01_16.ogg"
    $renpy.pause(delay=1.5, hard=True)
    play sound "audio/sfx/SE01/SE01_21.ogg"
    $renpy.pause(delay=1.0, hard=True)
    window auto show dissolve
    voice "audio/voice/E2/IRO/01/IR/IR015.ogg"
    iroha "Mmmmmm~ This whipped cream is so gooood~"
    voice "audio/voice/E2/IRO/01/HA/HA012.ogg"
    hachiman "...Is that so? Good for you."
    voice "audio/voice/E2/IRO/01/IR/IR016.ogg"
    iroha "Senpai, can I try that cake too?"
    window auto hide dissolve
    menu iroha_cake_menu:
        "No.":
            window auto show dissolve
            voice "audio/voice/E2/IRO/01/HA/HA013.ogg"
            hachiman "No. You have your own."
            voice "audio/voice/E2/IRO/01/IR/IR017.ogg"
            iroha "...Eh? You won't let me? Why are you here senpai?"
            voice "audio/voice/E2/IRO/01/HA/HA014.ogg"
            hachiman "At least, I don't want to believe it was just for you to take my cake..."
            voice "audio/voice/E2/IRO/01/IR/IR018.ogg"
            iroha "Oh, you know exactly what I'm talking about...! {size=35}Are {size=50}you{/size} hitting on me right now? I'm a little flattered that you're mature enough to see through my cute, girlish excuse for a lie, but I just want to eat cake{/size}, {size=50}I'm sorry{/size}."
            voice "audio/voice/E2/IRO/01/HA/HA015.ogg"
            hachiman "Ah, yeah. You're honestly..."
            voice "audio/voice/E2/IRO/01/IR/IR019.ogg"
            iroha "But I wonder, senpai, can you eat all of that by yourself?"
            voice "audio/voice/E2/IRO/01/HA/HA016.ogg"
            hachiman "...Really I don't even know why I am here. Why did I buy 4 of them..."
            voice "audio/voice/E2/IRO/01/IR/IR020.ogg"
            iroha "Oh well, that's what they call a man's manly duty, isn't it?"
            voice "audio/voice/E2/IRO/01/HA/HA017.ogg"
            hachiman "Alright... You can eat as much as you want."
        "Go ahead":
            window auto show dissolve
            voice "audio/voice/E2/IRO/01/HA/HA018.ogg"
            hachiman "Oh, well go ahead. Isn't that why you ordered 4 kinds for me in the first place?"
            voice "audio/voice/E2/IRO/01/IR/IR021.ogg"
            iroha "I just wanted to eat a bunch of them with you, senpai~"
            voice "audio/voice/E2/IRO/01/HA/HA019.ogg"
            hachiman "Then why didn't we just order 3 of each? Ah, nevermind."
        "............":
            window auto show dissolve
            voice "audio/voice/E2/IRO/01/HA/HA020.ogg"
            hachiman "............"
            voice "audio/voice/E2/IRO/01/IR/IR022.ogg"
            iroha "What's that deadpan look in your eyes..."
            voice "audio/voice/E2/IRO/01/HA/HA021.ogg"
            hachiman "No, nothing. I was called here only for this purpose."
            voice "audio/voice/E2/IRO/01/IR/IR023.ogg"
            iroha "You are truly a senpai! You have a very generous heart!"
            voice "audio/voice/E2/IRO/01/HA/HA022.ogg"
            hachiman "Well, just eat as much as you want."

    "I sighed while passing Isshiki the plate with the cake."
    window auto hide dissolve
    show irohaCakeShop with dissolve:
        zoom 1.5 xalign 1.0 yalign 1.0
    window auto show dissolve
    voice "audio/voice/E2/IRO/01/IR/IR024.ogg"
    iroha "Okay, let's dig in... Mmmm~~ it's delicious~~"
    hachiman "(If it makes her this happy, I guess the real reason for this is she really wanted to try these cakes.)"
    voice "audio/voice/E2/IRO/01/IR/IR025.ogg"
    iroha "Oh, which reminds me, didn't we buy a lucky bags together the other day?"
    hide irohaCakeShop
    show irohaCakeShop
    with dissolve
    voice "audio/voice/E2/IRO/01/HA/HA023.ogg"
    hachiman "Huh? Oh, yeah. On New Year's."
    voice "audio/voice/E2/IRO/01/IR/IR026.ogg"
    iroha "I want to go out with some new clothes~ A skirt like that one is so cute!"
    voice "audio/voice/E2/IRO/01/IR/IR027.ogg"
    iroha "So why don't we go shopping next time?"
    voice "audio/voice/E2/IRO/01/HA/HA024.ogg"
    hachiman "How does that follow? Skirts you can't share unlike cakes. And I can't give it to Komachi either."
    voice "audio/voice/E2/IRO/01/IR/IR028.ogg"
    iroha "Ugh, and here you come with the chop logic. What are you talking about? Being able to share memories is the best gift!"
    hachiman "(My god, what is this dreamy logic...?)"
    window auto hide dissolve
    show irohaCakeShop:
        zoom 1.8 xoffset 295 yoffset 840
    with dissolve
    window auto show dissolve
    voice "audio/voice/E2/IRO/01/IR/IR029.ogg"
    iroha "............"
    voice "audio/voice/E2/IRO/01/HA/HA025.ogg"
    hachiman "...What?"
    voice "audio/voice/E2/IRO/01/IR/IR030.ogg"
    iroha "We're making memories we'll both share right now, so please treasure them, senpai~"
    voice "audio/voice/E2/IRO/01/HA/HA026.ogg"
    hachiman "...!"
    voice "audio/voice/E2/IRO/01/HA/HA027.ogg"
    hachiman "I-Is that so..."
    voice "audio/voice/E2/IRO/01/IR/IR031.ogg"
    iroha "Yes! Ah, senpai, it's not good being a picky eater."
    hide irohaCakeShop
    show irohaCakeShop
    with dissolve
    "While I was wondering what she was talking about, Isshiki's fork reached for my plate. She stabbed at the strawberries I had left on my plate."
    voice "audio/voice/E2/IRO/01/HA/HA028.ogg"
    hachiman "Ah, w-wait, I'm not. I wanted to leave these for last."
    voice "audio/voice/E2/IRO/01/IR/IR032.ogg"
    iroha "Oh~? Is that so~? I'm sooo sorry~~"
    voice "audio/voice/E2/IRO/01/IR/IR033.ogg"
    iroha "Here then. Say \"Ahh\"."
    "Isshiki picked up the strawberry with her fork and hovered it in front of my nose as if to seduce me."
    voice "audio/voice/E2/IRO/01/HA/HA029.ogg"
    hachiman "...Nevermind. You can have it."
    voice "audio/voice/E2/IRO/01/IR/IR034.ogg"
    iroha "Can I really? Thank you~"
    "While I gave it up out of embarrassment, the strawberry was sucked right into Isshiki's lips."
    window auto hide dissolve
    stop music fadeout 0.5
    scene stationB
    show iroha coat_sunset mid_center vhappy at center:
        xoffset 25 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    play music ["<silence 0.3>", "audio/bgm/BGM36.ogg"]
    window auto show dissolve
    voice "audio/voice/E2/IRO/01/IR/IR035.ogg"
    iroha "Senpai, I had fun today. I hope your sister likes the cake from here."
    show iroha happy with dissolve
    voice "audio/voice/E2/IRO/01/IR/IR036.ogg"
    iroha "Well then, I'll get going. Senpai, take me out on a date again sometime."
    voice "audio/voice/E2/IRO/01/HA/HA030.ogg"
    hachiman "If I have the time..."
    show iroha coat_sunset mid_left vhappy at center with dissolve:
        xoffset -5 yoffset 65
    voice "audio/voice/E2/IRO/01/IR/IR037.ogg"
    iroha "Fufu, roger tha~t."
    hide iroha with dissolve
    stop music fadeout 0.5
    play ambient "audio/sfx/SE05/SE05_05L.ogg"
    hachiman "(...Take her out again, huh?)"
    hachiman "(I wonder how many men have been destroyed over that lip service.... Well she gets one more to her count today!)"
    hachiman "(...Well, it's fine as long as it makes Komachi happy in one way or another.)"
    "I held the bag with the strawberry tarts that Isshiki had chosen and headed home."
    window auto hide dissolve
    stop ambient fadeout 0.5
    #live2d loading screen
    call loading_screen(2, "33") from _call_iroha_coat2d_loading_cakeShop
    jump E3_CMM_01
