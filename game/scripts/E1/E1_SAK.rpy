label E1_SAK_01:
    show komachi coat near_left surprised at center with dissolve:
        xoffset 275 yoffset 65
    voice "audio/voice/E1/SAK/01/KO/KO000.ogg"
    komachi "Huh? I think I just spotted a familiar face. Where'd they go...?"
    hachiman "(You didn't have to notice...)"
    voice "audio/voice/E1/SAK/01/KE/KE000.ogg"
    mystery "Saa-chan, it's Haa-chan and his sister!"
    voice "audio/voice/E1/SAK/01/SA/SA000.ogg"
    mystery "What? Haa-chan?"
    show saki coat far_right surprised at left:
        xoffset 0 yoffset 75
    show keika heavy_coat far behind komachi at left:
        xoffset 510 yoffset 70
    show komachi vhappy
    with dissolve
    play music "audio/bgm/BGM14.ogg"
    voice "audio/voice/E1/SAK/01/KO/KO001.ogg"
    komachi "Ah! Over there! That's Saki-san and her siblings, onii-chan! Let's go!"
    # need to add footsteps here
    hide komachi
    hide keika
    hide saki
    with dissolve
    "As I was being dragged along by Komachi, I saw Kawa-something-san with her younger brother and sister, who all came to visit the shrine."
    "Keika's cute and all, but  I get ticked off every time I hear Komachi calling Taishi by his given name. Ah, that's right - it was the Kawasaki family, not the Kawa-something-family."
    show komachi coat mid_left vhappy at right:
        xoffset -150  yoffset 75
    show keika heavy_coat mid vhappy at center:
        xoffset 5 yoffset 75
    show saki coat mid_right surprised at left:
        xoffset -55 yoffset 75
    with dissolve
    voice "audio/voice/E1/SAK/01/KE/KE001.ogg"
    keika "Ah, Haa-chan!"
    voice "audio/voice/E1/SAK/01/HA/HA000.ogg"
    hachiman "Hey, Kei-chan. It's Haa-chan yo-"
    voice "audio/voice/E1/SAK/01/KE/KE002.ogg"
    keika "It's Kei-chan yo-- Ahahahaha!"
    voice "audio/voice/E1/SAK/01/HA/HA001.ogg"
    hachiman "Nahahahaha... Ah... Uhh... Yo."
    show saki pout with dissolve
    voice "audio/voice/E1/SAK/01/SA/SA001.ogg"
    saki "Ah. H-Hey..."
    voice "audio/voice/E1/SAK/01/TA/TA000.ogg"
    taishi "Hikigaya-san! I mean... onii-san! Happy New Year!"
    # ^ changed and to errr
    voice "audio/voice/E1/SAK/01/HA/HA002.ogg"
    hachiman "You don't have the right to call me onii-san. And first of all, who are you?"
    voice "audio/voice/E1/SAK/01/TA/TA001.ogg"
    taishi "Long time no see, onii-san! It's so cruel of you to forget about me! I'm Kawasaki Taishi!"
    show saki annoyed with dissolve
    voice "audio/voice/E1/SAK/01/SA/SA002.ogg"
    saki "Hey you, do you have a problem with my little brother?"
    voice "audio/voice/E1/SAK/01/HA/HA003.ogg"
    hachiman "No, not at all. It's only human to forget things..."
    hide komachi
    $url = ["komachi coat mid_left frown", "komachi coat mid_left vhappy"]
    $multiImagePara = [-150, 75, 0, 0, 5.0]
    call multiImage(1) from _call_multiImage_73
    voice "audio/voice/E1/SAK/01/KO/KO002.ogg"
    komachi "Jeez, onii-chan! I apologize for my brother going and spoiling a brand new year. Taishi-kun, Saki-san, Keika-chan Happy New Year as well!"
    call finishmultiImage from _call_finishmultiImage_77
    show komachi coat mid_left vhappy at right:
        xoffset -150 yoffset 75
    "Despite being scolded by Komachi, I still ended up greeting them, albeit awkwardly. Keika smiled and laughed. \"Happy New Year~\" she said, bowing adorably. Taishi on the other hand gave a pointlessly vigorous \"I wish you a prosperous New Year!\"."
    "And as for Kawasaki Saki, she still glared at me. She can get really worked up when it comes to her brother..."
    show komachi pout with dissolve
    voice "audio/voice/E1/SAK/01/KO/KO003.ogg"
    komachi "Taishi-kun, are you praying for academic success, too? ...Did you work on the old exams?"
    voice "audio/voice/E1/SAK/01/TA/TA002.ogg"
    taishi "Ah, yeah, they were pretty hard... When you can't solve something, you just get super antsy..."
    show komachi unimpressed with dissolve
    voice "audio/voice/E1/SAK/01/KO/KO004.ogg"
    komachi "I know exactly what you mean... I get really, really anxious as well."
    show keika happy with dissolve
    voice "audio/voice/E1/SAK/01/KE/KE003.ogg"
    keika "Haa-chan, Haa-chan. Does this taste good?"
    voice "audio/voice/E1/SAK/01/HA/HA004.ogg"
    hachiman "Hm? That's a fortune slip. Don't eat that, okay?"
    voice "audio/voice/E1/SAK/01/KE/KE004.ogg"
    keika "Saa-chan said it's not good to be picky!"
    voice "audio/voice/E1/SAK/01/HA/HA005.ogg"
    hachiman "I see. It's nice that you listen obediently to what Saa-chan says. But, you still can't eat this one."
    show saki surprised with dissolve
    voice "audio/voice/E1/SAK/01/SA/SA003.ogg"
    saki "Ha?"
    "To cool her head down, I clumsily poked at Keika's cheeks."
    hachiman "(Wow, so soft. She's just like Komachi was when she was younger.)"
    show keika vhappy with dissolve
    voice "audio/voice/E1/SAK/01/KE/KE005.ogg"
    keika "Haa-chan, you're on! Hup!"
    show saki vhappy with dissolve
    voice "audio/voice/E1/SAK/01/SA/SA004.ogg"
    saki "............"
    window auto hide dissolve
    stop music fadeout 1.0
    jump E1_SAK_02

label E1_SAK_02:
    scene market with Fade(1.0, 0.5, 1.0)
    show komachi coat mid_left happy at right:
        xoffset -150  yoffset 75
    show keika heavy_coat mid vhappy at center:
        xoffset 5 yoffset 75
    show saki coat mid_right surprised at left:
        xoffset -55 yoffset 75
    with dissolve
    play music "audio/bgm/BGM08.ogg"
    window auto show dissolve
    "I suddenly realized I've been playing with Kei-chan for quite a some time. Komachi and Taishi's exchange seems to have concluded as well."
    voice "audio/voice/E1/SAK/02/HA/HA000.ogg"
    hachiman "I think it's about time we go home, Komachi."
    show komachi coat mid_center happy with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E1/SAK/02/KO/KO000.ogg"
    komachi "Oh... okay. You're right."
    show saki vhappy with dissolve
    voice "audio/voice/E1/SAK/02/SA/SA000.ogg"
    saki "Ah... We'll be on our way too."
    show keika sad with dissolve
    voice "audio/voice/E1/SAK/02/KE/KE000.ogg"
    keika "Keika wants to play more with Haa-chan!"
    show komachi unimpressed with dissolve
    voice "audio/voice/E1/SAK/02/KO/KO001.ogg"
    komachi "Onii-chan, why is Kei-chan so attached to you?"
    show saki sad with dissolve
    voice "audio/voice/E1/SAK/02/SA/SA001.ogg"
    saki "Umm... I'm sorry about my little sister."
    show komachi coat mid_left pout with dissolve:
        xoffset -150  yoffset 75
    voice "audio/voice/E1/SAK/02/KO/KO002.ogg"
    komachi "Ah, that's not what I meant! It's just rare to see people caring about my bro-- No, I mean to see someone so attached to him."
    hachiman "(Hang on, Komachi-chan? Was that slip-up just now intentional?)"
    show saki surprised with dissolve
    voice "audio/voice/E1/SAK/02/SA/SA002.ogg"
    saki "What? Seriously?"
    show komachi surprised with dissolve
    voice "audio/voice/E1/SAK/02/MIX000.ogg"
    hachiandkom "Eh!?"
    show saki blush with dissolve
    voice "audio/voice/E1/SAK/02/SA/SA003.ogg"
    saki "Uhm... Forget about that. Thanks for being so kind to us last Christmas, too..."
    # ^ need to check translation
    # changed its nothing special to nevermind
    show komachi pout with dissolve
    voice "audio/voice/E1/SAK/02/KO/KO004.ogg"
    komachi "Huh?!"
    voice "audio/voice/E1/SAK/02/HA/HA002.ogg"
    hachiman "Being a good big brother is my specialty after all. Wasn't I always looking after you when you were little?"
    show komachi coat mid_center unimpressed with dissolve:
        xoffset -75  yoffset 75
    voice "audio/voice/E1/SAK/02/KO/KO005.ogg"
    komachi "Yeah, when I was little. Oh gosh, and I didn't think you'd still be doing it now... Ah, I'm worried onii-chan is getting old!"
    voice "audio/voice/E1/SAK/02/HA/HA003.ogg"
    hachiman "Whoa, what, you're taking it that far? Well, hope you can take care of me when I do get old."
    show saki vhappy with dissolve
    voice "audio/voice/E1/SAK/02/SA/SA004.ogg"
    saki "............"
    voice "audio/voice/E1/SAK/02/HA/HA004.ogg"
    hachiman "What's so funny?"
    voice "audio/voice/E1/SAK/02/SA/SA005.ogg"
    saki "Nothing really. I just thought that as siblings you two get along really well."
    show komachi coat mid_left vhappy with dissolve:
        xoffset -150  yoffset 75
    voice "audio/voice/E1/SAK/02/KO/KO006.ogg"
    komachi "The same goes for you guys. I've always wanted a badass sister like you, it makes me so jealous!"
    show saki blush with dissolve
    voice "audio/voice/E1/SAK/02/SA/SA006.ogg"
    saki "Huh? W-Well, I think that's a bit too much..."
    "While they were exchanging compliments, Keika tightly held onto my coat and wouldn't let go."
    show saki vhappy with dissolve
    voice "audio/voice/E1/SAK/02/SA/SA007.ogg"
    saki "H-Hey now Kei-chan. Let's go back home now."
    show keika vhappy with dissolve
    voice "audio/voice/E1/SAK/02/KE/KE001.ogg"
    keika "Okay, let's go home together with Haa-chan!"
    show saki surprised with dissolve
    voice "audio/voice/E1/SAK/02/MIX001.ogg"
    hachiandsaki "Huh?!"
    show keika happy with dissolve
    voice "audio/voice/E1/SAK/02/KE/KE002.ogg"
    keika "Umm... and also... Ko... Ko..."
    show komachi happy with dissolve
    voice "audio/voice/E1/SAK/02/KO/KO007.ogg"
    komachi "You mean Komachi?"
    show keika vhappy with dissolve
    voice "audio/voice/E1/SAK/02/KE/KE003.ogg"
    keika "Yeah! Komachi! Komachi let's go home together too!"
    show komachi vhappy with dissolve
    voice "audio/voice/E1/SAK/02/KO/KO008.ogg"
    komachi "You're really inviting me too Keika-chan?"
    voice "audio/voice/E1/SAK/02/KE/KE004.ogg"
    keika "Yes, I'm inviting you!"
    voice "audio/voice/E1/SAK/02/KO/KO009.ogg"
    komachi "Ahaha... She's so cuuute. I also want a little sister like her too. Umm, Onii-chan, what should we do?"
    voice "audio/voice/E1/SAK/02/HA/HA006.ogg"
    hachiman "Well it's a bit rude to do be intruding like that, it's New Year's Day after all."
    "While saying this, I'm still pondering on how to get Keika off of me."
    show saki blush with dissolve
    voice "audio/voice/E1/SAK/02/SA/SA009.ogg"
    saki "Well, my parents are visiting relatives right now."
    voice "audio/voice/E1/SAK/02/TA/TA000.ogg"
    taishi "Yeah, that's right, onii-san! Please come over and hang out with us!"
    voice "audio/voice/E1/SAK/02/HA/HA007.ogg"
    hachiman "Who the heck are you? Don't just show up out of nowhere and say whatever you want."
    voice "audio/voice/E1/SAK/02/TA/TA001.ogg"
    taishi "Kawasaki Taishi! I already introduced myself a while ago!"
    show komachi happy with dissolve
    voice "audio/voice/E1/SAK/02/KO/KO010.ogg"
    komachi "Hee... But would it not be a bother to you if we came?"
    show saki happy with dissolve
    voice "audio/voice/E1/SAK/02/SA/SA010.ogg"
    saki "No, not all... I won't force you to though."
    show komachi vhappy with dissolve
    voice "audio/voice/E1/SAK/02/KO/KO011.ogg"
    komachi "Are you really sure it's alright!?"
    hachiman "(Komachi, do you really want to go? Letting you visit the house of that middle school boy who's been looking at me expectantly for a while now worries me.)"
    voice "audio/voice/E1/SAK/02/KE/KE005.ogg"
    keika "Yeah, it's ok!"
    voice "audio/voice/E1/SAK/02/TA/TA002.ogg"
    taishi "It really is! We'll be glad to have you, onii-san!"
    hachiman "(His pushiness is really concerning... Wait, who was this guy again?)"
    "And just like that, me and my sister agreed to visit Kawasaki's house."
    window auto hide dissolve
    stop music fadeout 1.0
    hide komachi
    hide saki
    hide keika
    with dissolve
    show saki_houseA
    show saki home mid_right at left:
        xoffset 70 yoffset 75
    show komachi home mid_left at right:
        xoffset -270 yoffset 75
    with Fade(0.5, 0.5, 0.5)
    $renpy.pause(delay=0.5, hard=True)
    play music "audio/bgm/BGM09.ogg"
    window auto show dissolve
    voice "audio/voice/E1/SAK/02/SA/SA011.ogg"
    saki "This is just home cooking... but if you'd like some..."
    show komachi vhappy with dissolve
    voice "audio/voice/E1/SAK/02/KO/KO012.ogg"
    komachi "Whoa! This osechi looks so pretty! And super tasty! It's really different from what we usually have~!"
    "Of course, I was nervous because it was my first time at the Kawasakis. However, I was immediately amazed at the quality of Osechi served by Kawasaki."
    voice "audio/voice/E1/SAK/02/HA/HA008.ogg"
    hachiman "I know, right? We've been only buying ours to begin with."
    show saki blush with dissolve
    voice "audio/voice/E1/SAK/02/SA/SA012.ogg"
    saki "I-Is that so...?"
    voice "audio/voice/E1/SAK/02/TA/TA003.ogg"
    taishi "Nee-chan's osechi is incredibly delicious, you know?"
    voice "audio/voice/E1/SAK/02/SA/SA013.ogg"
    saki "Ta-Taishi...!"
    show komachi surprised with dissolve
    voice "audio/voice/E1/SAK/02/KO/KO013.ogg"
    komachi "Huh!? Saki-san made this!? Komachi-chan applauds you!"
    voice "audio/voice/E1/SAK/02/HA/HA009.ogg"
    hachiman "Wow, you cooked this all by yourself?"
    voice "audio/voice/E1/SAK/02/SA/SA014.ogg"
    saki "............."
    show saki vhappy with dissolve
    voice "audio/voice/E1/SAK/02/SA/SA015.ogg"
    saki "It's just some simple cooking, it's not really that impressive..."
    "Saying this, Kawasaki cheerily served Komachi and I our food. In the meantime, she was feeding Keika something that was easy for her to eat, which made me smile."
    voice "audio/voice/E1/SAK/02/HA/HA010.ogg"
    hachiman "Ah, well, thank you anyway."
    show komachi vhappy with dissolve
    voice "audio/voice/E1/SAK/02/KO/KO014.ogg"
    komachi "Let's dig in!"
    show saki blush with dissolve
    voice "audio/voice/E1/SAK/02/SA/SA016.ogg"
    saki "............."
    hachiman "(This is...!)"
    "I'm not going to blow fire out of my mouth and shout \"This is so GOOD!\", that would be going a bit too far. With that being said, simple and tasty home cooking filled with sisterly love is not something you "
    "can buy from a store."
    show komachi mid_center vhappy with dissolve:
        xoffset -200 yoffset 75
    voice "audio/voice/E1/SAK/02/KO/KO015.ogg"
    komachi "Delicious!"
    voice "audio/voice/E1/SAK/02/HA/HA011.ogg"
    hachiman "You're a really good cook, you know that?"
    voice "audio/voice/E1/SAK/02/TA/TA004.ogg"
    taishi "Right, onii-san? She totally is!"
    "The food was so good I almost let it slide, but don't go calling me onii-san. Who is this guy anyway?"
    voice "audio/voice/E1/SAK/02/SA/SA017.ogg"
    saki "I-If you'd like to, you can have as much as you want."
    voice "audio/voice/E1/SAK/02/KE/KE006.ogg"
    keika "Kei-chan wants more too~"
    show komachi happy with dissolve
    voice "audio/voice/E1/SAK/02/KO/KO016.ogg"
    komachi "This kind of feels like a New Years family get-together, right, Onii-chan?"
    voice "audio/voice/E1/SAK/02/HA/HA012.ogg"
    hachiman "It does."
    "I occasionally poked at my food with relief as I watched all these brothers and sisters happily digging into the Osechi."
    "As I watched the comforting scene out of the corner of my eye, I thought to myself that I'd never be able to forget Kawasaki's name again, probably."
    window auto hide dissolve
    stop music fadeout 1.0
    jump E1_CMM_02