label E2_SAK_01:
    scene skyA with Fade(1.0, 0.5, 1.0)
    # add sfx
    play music ["<silence 1>", "audio/bgm/BGM18.ogg"]
    window auto show dissolve
    "As I walked alongside Komachi, we made small talk on various topics - about school, New Years, exams, her friends, and many other things... Our conversation just flowed naturally."
    "Maybe strolling down the empty streets with her like this would help Komachi relax. She spun her words calmly, as usual, without a trace of affection."
    "It pained me to see Komachi tired because of exam taking, but all I could do was silently cheer her on in my heart."
    window auto hide dissolve
    scene gatesA with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E2/SAK/01/HA/HA000.ogg"
    hachiman "Look, it's the school gates."
    voice "audio/voice/E2/SAK/01/KO/KO000.ogg"
    stop music fadeout 0.5
    komachi "Yeah-- Huh?"
    hachiman "...Hm? Isn't that..."
    show saki coat far_right happy at center with dissolve:
        xoffset -85 yoffset 75
    play music "audio/bgm/BGM14.ogg"
    voice "audio/voice/E2/SAK/01/SA/SA000.ogg"
    saki "Ah."
    voice "audio/voice/E2/SAK/01/TA/TA000.ogg"
    taishi "It's Hikigaya-san! I mean... onii-san!"
    stop voice
    hide saki
    show saki coat mid_right pout at left:
        xoffset 75 yoffset 75
    with Dissolve(0.4)
    play sound "audio/sfx/SE00/SE00_29.ogg"
    show komachi coat mid_left vhappy at right with dissolve:
        xoffset -225 yoffset 75
        linear 0.4 xoffset -275
    hide komachi
    show komachi coat mid_left vhappy at right:
        xoffset -275 yoffset 75
    $renpy.pause(delay=0.5,hard=True)
    voice "audio/voice/E2/SAK/01/KO/KO001.ogg"
    komachi "It's Taishi-kun and Saki-san! Hello!"
    voice "audio/voice/E2/SAK/01/HA/HA001.ogg"
    hachiman "Yo. Pretty rare to see someone at school on winter break. What gives?"
    voice "audio/voice/E2/SAK/01/SA/SA001.ogg"
    saki "S-Same goes for you. I just thought that he should get to know the school before his exams..."
    show komachi happy with dissolve
    voice "audio/voice/E2/SAK/01/KO/KO002.ogg"
    komachi "Komachi's here to do that, too!"
    voice "audio/voice/E2/SAK/01/TA/TA001.ogg"
    taishi "Huh, Hikigaya-san too?"
    show komachi sad with dissolve
    voice "audio/voice/E2/SAK/01/KO/KO003.ogg"
    komachi "Yeah, since Komachi was feeling down, onii-chan invited me to check out the school."
    hachiman "(Wow, she figured out that much... I have to say I'm impressed with Komachi. Wait a sec, was my intention really that obvious?! She can see right through me, damn.)"
    hide saki
    hide komachi
    with dissolve
    "I'm both impressed and frightened by the level of my sister's perception."
    show saki coat mid_right blush at center with dissolve:
        xoffset -85 yoffset 75
    voice "audio/voice/E2/SAK/01/SA/SA002.ogg"
    saki "You seem really good at taking care of your sister..."
    voice "audio/voice/E2/SAK/01/HA/HA002.ogg"
    hachiman "I'm sure you love your brothers and sisters very much, too. Besides, my onii-chan skills have reached the point where they operate automatically."
    show saki vhappy with dissolve
    voice "audio/voice/E2/SAK/01/SA/SA003.ogg"
    saki "You're always saying things like that."
    hachiman "(Kawasaki-san is a cute girl when she doesn't act like an ill-bred delinquant - like she always does.)"
    hide saki with dissolve
    "On the other hand, looking at Komachi and Taishi, the students we're having a rather dull conversation."
    voice "audio/voice/E2/SAK/01/KO/KO004.ogg"
    komachi "Which reminds me, my math score from the mock exams the other day was really low..."
    voice "audio/voice/E2/SAK/01/TA/TA002.ogg"
    taishi "And I ran out of time for the Japanese language exams, and I wasn't able to write anything at reading comprehension..."
    voice "audio/voice/E2/SAK/01/KO/KO005.ogg"
    komachi "Ah, that's it!"
    "Komachi's suddenly whispering on Taishi's ears."
    show saki coat mid_right happy at left with dissolve:
        xoffset 75 yoffset 75
    play sound "audio/sfx/SE00/SE00_29.ogg"
    show komachi coat mid_left angry at right with dissolve:
        xoffset -225 yoffset 75
        linear 0.4 xoffset -275
    hide komachi
    show komachi coat mid_left angry at right:
        xoffset -275 yoffset 75
    $renpy.pause(delay=0.5,hard=True)
    voice "audio/voice/E2/SAK/01/MIX000.ogg"
    komandtai "Saki-san, please teach me Math!\nOnii-san, please teach me Japanese!"
    show saki surprised with dissolve
    voice "audio/voice/E2/SAK/01/MIX001.ogg"
    hachiandsaki "Eh?\nHuh?"
    voice "audio/voice/E2/SAK/01/MIX002.ogg"
    komandtai "............"
    show saki pout with dissolve
    voice "audio/voice/E2/SAK/01/SA/SA005.ogg"
    saki "I-I don't mind, but... All our studying materials are back at home... S-So do you guys want to do it at our house? Um, how about it, Hikigaya?"
    show komachi vhappy with dissolve
    voice "audio/voice/E2/SAK/01/MIX003.ogg"
    komandtai "Is it really alright!?\nYes!!"
    "It's good that you're motivated to study now, but we'll have to visit the Kawasaki household again... It's better than letting Komachi and Taishi study alone however..."
    hachiman "(...Well, it can't be helped I guess.)"
    window auto hide dissolve
    stop music fadeout 1.0
    hide komachi
    hide saki
    jump E2_SAK_02

label E2_SAK_02:
    show saki_houseA
    with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/BGM17.ogg"
    window auto show dissolve
    voice "audio/voice/E2/SAK/02/KO/KO000.ogg"
    komachi "Saki-san, what do I do on this problem..."
    voice "audio/voice/E2/SAK/02/SA/SA000.ogg"
    saki "Ah, you'll need to use this formula. First you'll need to..."
    "I visited the Kawasaki family again, and we decided to have an impromptu study session. The content we reviewed was that of the recent mock exam. Surely this will relieve some of our examinees "
    "worries."
    "It just so happened that we decided to split the tutoring in 2 sections - I handled questions about humanities, and sciences and mathematics with Kawasaki-san. I didn't want to admit it, but the sight of Komachi "
    "and Taishi working side by side, groaning at questions, made me smile a little."
    voice "audio/voice/E2/SAK/02/TA/TA000.ogg"
    taishi "Onii-san, about this question on classical literature... My grammar's pretty weak, so..."
    voice "audio/voice/E2/SAK/02/HA/HA000.ogg"
    hachiman "Hm? Right. So, where does this \"ya\" go?"
    voice "audio/voice/E2/SAK/02/TA/TA001.ogg"
    taishi "Uhh... next to \"suru\"?"
    voice "audio/voice/E2/SAK/02/HA/HA001.ogg"
    hachiman "Correct. So now does that translate to \"Are we going to see the cherry blossoms?\" or \"I'm not going to see the cherry blossoms.\"?"
    voice "audio/voice/E2/SAK/02/TA/TA002.ogg"
    taishi "Is it \"Are we going to see the cherry blossoms?\"?"
    voice "audio/voice/E2/SAK/02/HA/HA002.ogg"
    hachiman "Boo--. Insert \"ya\" after \"suru\". Combining them like this converts them to linked form. You're treating them as antonyms, don't. Suru as in \"Will I?\", ya as in \"No, I won't\". That's an example of roundabout "
    voice sustain
    hachiman "negation."
    voice "audio/voice/E2/SAK/02/TA/TA003.ogg"
    taishi "Oh! I think I get it now! They taught this in class!"
    voice "audio/voice/E2/SAK/02/HA/HA003.ogg"
    hachiman "See? If you keep rereading the past questions exactly and reviewing these areas, you'll do fine."
    voice "audio/voice/E2/SAK/02/TA/TA004.ogg"
    taishi "Onii-san's way of teaching is so easy to understand!"
    "I'm not going to lie, it's pretty cut and dry, but this late in the school year, it's much more useful to build up your confidence with aesthetic practices rather than cramming it in blindly. Source - me."
    hachiman "(Well, Taishi seems like the type of guy to compensate with energy when he's demotivated  rather than with nodding off...)"
    voice "audio/voice/E2/SAK/02/SA/SA001.ogg"
    saki "Hmm?"
    show saki home mid_right vhappy at center with dissolve:
        xoffset -115 yoffset 75
    voice "audio/voice/E2/SAK/02/HA/HA004.ogg"
    hachiman "What is it?"
    "I noticed that Kawasaki and Komachi were staring blankly at the exchange between me and Taishi."
    show saki blush with dissolve
    voice "audio/voice/E2/SAK/02/SA/SA002.ogg"
    saki "Ah, n-nothing, I just thought you were surprisingly good at teaching. The way you speak isn't that strict as well."
    stop voice
    hide saki with dissolve
    show saki home mid_right blush at left:
        xoffset 70  yoffset 75
    show komachi home mid_left happy at right:
        xoffset -270 yoffset 75
    with dissolve
    voice "audio/voice/E2/SAK/02/KO/KO001.ogg"
    komachi "I know, right? Whenever brother gets into gear, he teaches like a pro! Yeah, that was high in Komachi points!"
    voice "audio/voice/E2/SAK/02/HA/HA005.ogg"
    hachiman "W-Well, it's to be expected of a big brother..."
    voice "audio/voice/E2/SAK/02/TA/TA005.ogg"
    taishi "I know how that feels, onii-san!"
    stop voice
    hide saki
    hide komachi
    with dissolve
    hachiman "(Putting myself aside, I knew  this guy was the type who got carried away easily.)"
    hachiman "(I almost didn't care about being called \"big brother,\" so I decided to stare at the obnoxious Taishi with murder in my eye instead of shouting at him as a reminder to myself.)"
    show keika home near frown at center with dissolve:
        yoffset 175
        linear 0.5 yoffset 75
    hide keika
    show keika home near frown zorder 1 at center:
        yoffset 75
    voice "audio/voice/E2/SAK/02/KE/KE000.ogg"
    keika "Haa-chan, Taa-chan! No fair! I want to study too!"
    "Keika was given a picture book and left to her own devices, but it seemed that she was indeed getting bored."
    voice "audio/voice/E2/SAK/02/HA/HA006.ogg"
    hachiman "Ohh, Kei-chan. Studying? You don't have to do what we're doing you know--"
    show keika happy with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE001.ogg"
    keika "Keika will ask questions, Haa-chan will answer!"
    hachiman "(Eh? I will be the one studying?)"
    hide saki
    $url = ["saki home near_right pout", "saki home near_right vhappy"]
    $multiImagePara = [-145, 75, 0, 0, 2.3]
    call multiImage(-1) from _call_multiImage_42
    voice "audio/voice/E2/SAK/02/SA/SA003.ogg"
    saki "I-I'm sorry Hikigaya... Kei-chan, do you want to play with Saa-chan over there?"
    call finishmultiImage from _call_finishmultiImage_43
    show saki home near_right vhappy at left behind keika:
        xoffset -145 yoffset 75
    "I was a little tired myself, so I decided to take a break and play with Keika."
    hide keika
    hide saki
    image sakiFlat = Flatten("saki home near_right vhappy")
    image keikaFlat = Flatten("keika home near happy")
    show keikaFlat at center:
        yoffset 75
        parallel:
            1.5
            easein 0.5 alpha 0
    show sakiFlat at left behind keikaFlat:
        xoffset -145 yoffset 75
        parallel:
            1.5
            easein 0.5 alpha 0
    voice "audio/voice/E2/SAK/02/HA/HA007.ogg"
    hachiman "Don't worry, it's fine. Taishi, try to get the answers using the classical literature dictionary."
    hide keikaFlat
    hide sakiFlat
    voice "audio/voice/E2/SAK/02/TA/TA006.ogg"
    taishi "Sure!"
    "That's a pretty good answer."
    show saki home mid_right vhappy at left:
        xoffset 70  yoffset 75
    show komachi home mid_left happy at right:
        xoffset -270 yoffset 75
    with dissolve
    voice "audio/voice/E2/SAK/02/SA/SA004.ogg"
    saki "Okay, I'll go make some more tea then. Komachi-chan, let's take a break."
    show komachi vhappy with dissolve
    voice "audio/voice/E2/SAK/02/KO/KO002.ogg"
    komachi "Okay~!"
    hide saki
    hide komachi
    with dissolve
    show keika home near happy at center with dissolve:
        yoffset 75
    voice "audio/voice/E2/SAK/02/HA/HA008.ogg"
    hachiman "Well, Kei-chan, shall we study?"
    show keika vhappy with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE002.ogg"
    keika "Mhmm! Let's do it!"
    show keika pout with dissolve
    stop music fadeout 1.0
    voice "audio/voice/E2/SAK/02/KE/KE003.ogg"
    keika "Umm..."
    show keika happy with dissolve
    play music "audio/bgm/BGM29.ogg"
    voice "audio/voice/E2/SAK/02/KE/KE004.ogg"
    keika "Between Alpaca-san and Llama-san, who's taller?"
    hachiman "(These are the popular animals to younger kids nowadays, I guess. Giraffe-san no longer exists, huh...)"
    window auto hide dissolve
    call screen two_minigame("Alpaca-san", "Llama-san") with dissolve
    #https://m.youtube.com/playlist?list=PLyfUd322vCFHDlY1cmpq8ZJzO2Bby3NYi
    if _return == 1:
        window auto show dissolve
        hachiman "(I think the alpaca's face is scarier... scarier probably means bigger.)"
        voice "audio/voice/E2/SAK/02/HA/HA010.ogg"
        hachiman "Should be alpaca, right?"
    elif _return == 2:
        window auto show dissolve
        hachiman "(I'm sure the llama carried a lot of luggage... I think it would be bigger if it could do that.)"
        voice "audio/voice/E2/SAK/02/HA/HA009.ogg"
        hachiman "Hmmmmm..... Llama?"
    voice "audio/voice/E2/SAK/02/HA/HA011.ogg"
    hachiman "So, did I get it right?"
    show keika vhappy with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE005.ogg"
    keika "Ehhhh, I don't know yet."
    hide keika with dissolve
    show saki home mid_right vhappy at left with dissolve:
        xoffset 0  yoffset 75
        linear 0.5 xoffset 70
    "Kawasaki brought me a cup of tea when I was poking Keika on the cheek and playing with her. She looked at the interaction between Keika and me with a smile."
    hachiman "(No, don't do that. I get embarassed when people look at me like that.)"
    show komachi home mid_left surprised at right with dissolve:
        xoffset -270 yoffset 75
    voice "audio/voice/E2/SAK/02/KO/KO003.ogg"
    komachi "Keika-chan, you sure know a lot of animals."
    show saki blush with dissolve
    voice "audio/voice/E2/SAK/02/SA/SA005.ogg"
    saki "Because Keika, she loves animal shows and zoos..."
    hide saki
    hide komachi
    with dissolve
    show keika home near vhappy at center with dissolve:
        yoffset 75
    voice "audio/voice/E2/SAK/02/KE/KE006.ogg"
    keika "Keika loves animals!"
    show keika frown with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE007.ogg"
    keika "Ok, Haa-chan, next one!"
    voice "audio/voice/E2/SAK/02/HA/HA012.ogg"
    hachiman "Eh? We're still doing this?"
    show keika happy with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE008.ogg"
    keika "Yes, let's do some more!"
    voice "audio/voice/E2/SAK/02/KE/KE009.ogg"
    keika "Who's the one tying up Keika's hair?"
    window auto hide dissolve
    call screen two_minigame("Mama", "Saa-chan") with dissolve
    if _return == 1:
        window auto show dissolve
        hachiman "(I feel that the Saki choice is a bluff. Keika's pretty good at this...)"
        voice "audio/voice/E2/SAK/02/HA/HA013.ogg"
        hachiman "Hmmm. If it's tying your hair.... Is it Mom?"
    elif _return == 2:
        window auto show dissolve
        hachiman "(I just pictured Kawasaki tying up Keika's hair, it's so cute!)"
        voice "audio/voice/E2/SAK/02/HA/HA014.ogg"
        hachiman "Now Kei-chan... It must be Saa-chan?"
        voice "audio/voice/E2/SAK/02/SA/SA006.ogg"
        saki "Did you say S-Saa-chan...!?"
    show keika vhappy with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE010.ogg"
    keika "I'll go again!"
    voice "audio/voice/E2/SAK/02/HA/HA015.ogg"
    hachiman "Oh, what's next?"
    show keika happy with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE011.ogg"
    keika "What food do Octopus-san and Crab-san like to be?"
    window auto hide dissolve
    call screen two_minigame("Wiener", "Okonomiyaki") with dissolve
    if _return == 1:
        window auto show dissolve
        hachiman "(This is a very cute question about Octopus-san and Crab-san... Both of which I would love to have in my lunch box.)"
        voice "audio/voice/E2/SAK/02/HA/HA016.ogg"
        hachiman "It's Wiener, right? Like octopus wieners and crab wieners."
    elif _return == 2:
        window auto show dissolve
        hachiman "(At first glance, the question seems innocent, but children do get some crazy ideas sometimes...)"
        voice "audio/voice/E2/SAK/02/HA/HA017.ogg"
        hachiman "Is it okonomiyaki by any chance? I happen to have an extra stomach for tasty seafood."
    show keika vhappy with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE012.ogg"
    keika "Oh Haa-chan! You're pretty good!"
    voice "audio/voice/E2/SAK/02/HA/HA018.ogg"
    hachiman "Right? You know it, Kei-chan."
    hide keika with dissolve
    show saki home mid_right vhappy at left:
        xoffset 70  yoffset 75
    show komachi home mid_left happy at right:
        xoffset -270 yoffset 75
    with dissolve
    voice "audio/voice/E2/SAK/02/KO/KO004.ogg"
    komachi "Keika-chan's questions are so cute~! Onii-chan, why is she so fond of you?"
    voice "audio/voice/E2/SAK/02/HA/HA020.ogg"
    hachiman "Komachi, go and study up. Off with you!"
    hide komachi
    $url = ["komachi home mid_left frown", "komachi home mid_left happy"]
    $multiImagePara = [-270, 75, 0, 0, 2.3]
    call multiImage(1) from _call_multiImage_43
    voice "audio/voice/E2/SAK/02/KO/KO005.ogg"
    komachi "Eh~ it's Komachi's break time now. Saki-san, is this candy homemade? It's so delicious!"
    call finishmultiImage from _call_finishmultiImage_44
    show komachi home mid_left happy at right:
        xoffset -270 yoffset 75
    show saki blush with dissolve
    voice "audio/voice/E2/SAK/02/SA/SA007.ogg"
    saki "Ah, yeah. It's not a big deal. Thanks for taking care of my sister, too, Hikigaya."
    voice "audio/voice/E2/SAK/02/HA/HA021.ogg"
    hachiman "Ah, no worries..."
    hide saki
    hide komachi
    with dissolve
    show keika home near frown at center with dissolve:
        yoffset 75
    voice "audio/voice/E2/SAK/02/KE/KE015.ogg"
    keika "Haa-chan, let's play some more!"
    hachiman "(Are we still doing this?)"
    show keika pout with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE016.ogg"
    keika "Ummmm..."
    show keika happy with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE017.ogg"
    keika "Who proposed first, Papa or Mama?"
    # maybe its left
    hachiman "(Eh, this isn't a quiz anymore, though...)"
    window auto hide dissolve
    call screen two_minigame("Papa", "Mama") with dissolve
    if _return == 1:
        window auto show dissolve
        hachiman "(Considering Taishi's character, I think it's the mother... however, it may very well be the father that did it...)"
        voice "audio/voice/E2/SAK/02/HA/HA024.ogg"
        hachiman "Normally it would be Papa, right?"
    elif _return == 2:
        window auto show dissolve
        hachiman "(Hmmm. I think it was the father, considering Kawasaki's character, but... it's always the unexpected that wins in these things...)"
        voice "audio/voice/E2/SAK/02/HA/HA022.ogg"
        hachiman "Was it Mom?"
    voice "audio/voice/E2/SAK/02/KO/KO006.ogg"
    komachi "Ah~. Onii-chan wouldn't be able to propose to anyone, though..."
    voice "audio/voice/E2/SAK/02/HA/HA023.ogg"
    hachiman "Huh? What does this have to do with me?"
    show keika vhappy with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE018.ogg"
    keika "Hmmmm..."
    hachiman "(\"Hmmmm\"? What does \"Hmmmm\" mean?)"
    voice "audio/voice/E2/SAK/02/KE/KE019.ogg"
    keika "Next!"
    show keika happy with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE020.ogg"
    keika "Let's see~. What does Saa-chan make best?"
    window auto hide dissolve
    call screen two_minigame("Boiled Fish", "Grilled Fish") with dissolve
    if _return == 1:
        window auto show dissolve
        hachiman "(This seems like a trap... Well played, Keika.)"
        voice "audio/voice/E2/SAK/02/HA/HA026.ogg"
        hachiman "Is it boiled fish?"
    elif _return == 2:
        window auto show dissolve
        hachiman "(It would usually be something simplistic, like, well, grilled fish. You just grill it.)"
        voice "audio/voice/E2/SAK/02/HA/HA027.ogg"
        hachiman "It's grilled fish, right?"
    voice "audio/voice/E2/SAK/02/SA/SA008.ogg"
    saki "Kei-chan, enough about me."
    show keika vhappy with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE021.ogg"
    keika "Hehee..."
    hachiman "(This reaction... What kind of small devil is this?)"
    voice "audio/voice/E2/SAK/02/KE/KE022.ogg"
    keika "More! Let's do some more!"
    show keika happy with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE023.ogg"
    keika "Who does Taa-chan like the most?"
    window auto hide dissolve
    call screen two_minigame("Saa-chan", "Komachi") with dissolve
    if _return == 1:
        window auto show dissolve
        hachiman "(T-There's no way it's Komachi, right? No, I won't accept it even if it is!)"
        voice "audio/voice/E2/SAK/02/HA/HA028.ogg"
        hachiman "It's Saa-chan, isn't it? Right, Kei-chan?"
    elif _return == 2:
        window auto show dissolve
        hachiman "(It can't be Komachi, can it? My fears weren't unfounded, were they?)"
        voice "audio/voice/E2/SAK/02/HA/HA029.ogg"
        hachiman "Ko... Komachi? Is it really Komachi?!"
    voice "audio/voice/E2/SAK/02/KO/KO008.ogg"
    komachi "Onii-chan, you seem kind of distressed about this!"
    voice "audio/voice/E2/SAK/02/TA/TA007.ogg"
    taishi "Keika, that topic about me is a little..."
    show keika vhappy with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE024.ogg"
    keika "Hahahahaha! Taa-chan's blushing!"
    hachiman "(T-This little girl the devil herself...!)"
    show saki home near_right sad at left behind keika with dissolve:
        xoffset -145 yoffset 75
    voice "audio/voice/E2/SAK/02/SA/SA009.ogg"
    saki "Kei-chan, I think it's time for you to take a break."
    "When Kawasaki called out to her, Keika nodded surprisingly quickly, as if she was getting bored by now."
    show keika happy
    voice "audio/voice/E2/SAK/02/KE/KE025.ogg"
    keika "Okay!"
    stop music fadeout 1.0
    hide saki
    hide keika
    with dissolve
    show saki home mid_right sad at left:
        xoffset 70 yoffset 75
    show keika home mid vhappy at right:
        xoffset -365 yoffset 75
    with dissolve
    play music "audio/bgm/BGM33.ogg"
    voice "audio/voice/E2/SAK/02/KE/KE026.ogg"
    keika "Oh, that was so fun!"
    voice "audio/voice/E2/SAK/02/HA/HA030.ogg"
    hachiman "I'm happy for you then...So, Kei-chan, what are the correct answers?"
    voice "audio/voice/E2/SAK/02/KE/KE027.ogg"
    keika "It's a secret!"
    show saki vhappy with dissolve
    voice "audio/voice/E2/SAK/02/SA/SA010.ogg"
    saki "Hikigaya, thanks for playing with Keika."
    show keika frown with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE032.ogg"
    keika "Keika was the one playing with Haa-chan!"
    hachiman "(Ah, even if the things they say are unreasonable, young sisters like her are very cute... No, they're probably cute because they are unreasonable.)"
    voice "audio/voice/E2/SAK/02/HA/HA033.ogg"
    hachiman "Yup, you're right, Kei-chan."
    stop voice
    hide keika
    hide saki
    with dissolve
    show saki home mid_right pout at center with dissolve:
        xoffset -115 yoffset 75
    voice "audio/voice/E2/SAK/02/SA/SA011.ogg"
    saki "A-Aren't you getting hungry? There's still some Osechi left, and some things I whipped up just now, but..."
    voice "audio/voice/E2/SAK/02/HA/HA034.ogg"
    hachiman "Seriously? Don't mind if I do."
    hachiman "(I mean, it's amazing that she cooked something while making that tea earlier.)"
    voice "audio/voice/E2/SAK/02/KO/KO009.ogg"
    komachi "Komachi too! Saki-san's cooking is so good!"
    show saki blush with dissolve
    voice "audio/voice/E2/SAK/02/SA/SA012.ogg"
    saki "The-Then let's all take a break for now and I'll go get something ready."
    stop voice
    hide saki with dissolve
    voice "audio/voice/E2/SAK/02/TA/TA008.ogg"
    taishi "Onii-san, I'm feeling a little more confident now. Please help me with English later."
    voice "audio/voice/E2/SAK/02/HA/HA035.ogg"
    hachiman "Sure thing. There's a trick to that as well."
    hachiman "(Ah... I finally feel myself resigning to being called that.)"
    window auto hide dissolve
    stop music fadeout 1.0
    scene saki_houseA
    with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM32.ogg"
    show saki home mid_right vhappy at center with dissolve:
        xoffset -115 yoffset 75
    window auto show dissolve
    voice "audio/voice/E2/SAK/02/SA/SA013.ogg"
    saki "Sorry to keep you waiting. It's not much to gawk at, though..."
    hide saki with dissolve
    "In response to Kawasaki's words, Komachi and Taishi rushed to clear the table. Kawasaki is humble, but both the remainder of the Osechi that was moved from the large pot to a small plate and the newly "
    "brought soop looked delicious."
    show saki home mid_right vhappy at left:
        xoffset -90 yoffset 75
    show komachi home mid_center happy at right:
        xoffset -200 yoffset 75
    show keika home mid vhappy at left:
        xoffset 475 yoffset 75
    with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE033.ogg"
    keika "Food!"
    voice "audio/voice/E2/SAK/02/KO/KO010.ogg"
    komachi "Woah... Onii-chan, it's ozoni soup!"
    show saki blush with dissolve
    voice "audio/voice/E2/SAK/02/SA/SA014.ogg"
    saki "Ah, maybe you've had enough of my ozoni soups by now?"
    voice "audio/voice/E2/SAK/02/HA/HA036.ogg"
    hachiman "No, we don't eat ozoni soups often, so thank you for this."
    show komachi home mid_left vhappy with dissolve:
        xoffset -270 yoffset 75
    voice "audio/voice/E2/SAK/02/KO/KO011.ogg"
    komachi "I've heard that different families make different variations, so I'm really looking forward to this!"
    voice "audio/voice/E2/SAK/02/SA/SA015.ogg"
    saki "I-Is that so...? That's a relief then."
    hide komachi
    hide saki
    hide keika
    with dissolve
    "Everyone said \"Let's eat\" and picked up their chopsticks. The food was as delicious as it looked."
    "By just eating this meal, I already want to become one of the kids living here, too! I'll supervise the food here, no need to work outside! That's no different from being a NEET though..."
    show saki home mid_right happy at center with dissolve:
        xoffset -115 yoffset 75
    voice "audio/voice/E2/SAK/02/HA/HA037.ogg"
    hachiman "Hey, do you have any tricks for boiling food?"
    voice "audio/voice/E2/SAK/02/SA/SA016.ogg"
    saki "Ah, there isn't really a go-to trick... I just make sure the broth is good, and then adjust it as I taste..."
    voice "audio/voice/E2/SAK/02/HA/HA038.ogg"
    hachiman "Hmm? I see, so that's how it is."
    voice "audio/voice/E2/SAK/02/TA/TA009.ogg"
    taishi "Nee-chan's boiled food is a lot better than Mom's."
    show saki blush with dissolve
    voice "audio/voice/E2/SAK/02/SA/SA017.ogg"
    saki "That's not true!"
    hide saki with dissolve
    show komachi home mid_center happy at center with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E2/SAK/02/KO/KO012.ogg"
    komachi "You're blending in pretty well, onii-chan!"
    voice "audio/voice/E2/SAK/02/HA/HA039.ogg"
    hachiman "You think so?"
    show komachi vhappy with dissolve
    voice "audio/voice/E2/SAK/02/KO/KO013.ogg"
    komachi "Mm-hmm! You'll get your attitude straight, while Komachi'll get to have an elder sister like her!"
    voice "audio/voice/E2/SAK/02/HA/HA040.ogg"
    hachiman "............."
    hachiman "(T-There it is...!! Komachi's \"I want to have an elder sister\" appeal!)"
    hide komachi with dissolve
    show saki home mid_right happy at center:
        xoffset -355 yoffset 75
    show keika home mid vhappy at center:
        xoffset 215 yoffset 75
    with dissolve
    voice "audio/voice/E2/SAK/02/KE/KE034.ogg"
    keika "Haa-chan and Saa-chan are just like papa and mama!"
    show saki blush with dissolve
    voice "audio/voice/E2/SAK/02/SA/SA018.ogg"
    saki "D-D-Don't say s-stupid things!"
    voice "audio/voice/E2/SAK/02/TA/TA010.ogg"
    taishi "Big sis is totally embarassed!"
    show saki frown with dissolve
    voice "audio/voice/E2/SAK/02/SA/SA019.ogg"
    saki "Taishi, I'll smack you!"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    scene sidewalkB with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM34.ogg"
    # komachi has some shading here
    show komachi coat_sunset mid_center happy at center with dissolve:
        xoffset -75 yoffset 75
    window auto show dissolve
    voice "audio/voice/E2/SAK/02/KO/KO014.ogg"
    komachi "Thank you for today, onii-chan."
    voice "audio/voice/E2/SAK/02/HA/HA041.ogg"
    hachiman "What's this all of a sudden?"
    show komachi coat_sunset mid_left happy with dissolve:
        xoffset 5 yoffset 75
    voice "audio/voice/E2/SAK/02/KO/KO015.ogg"
    komachi "I feel somehow really relieved by today. I think I'm going to do well in the exam."
    voice "audio/voice/E2/SAK/02/HA/HA042.ogg"
    hachiman "I see. Well... It's not a bad thing to get all riled up, but keeping a cool head takes priority here."
    show komachi vhappy with dissolve
    voice "audio/voice/E2/SAK/02/KO/KO016.ogg"
    komachi "I'll do my best."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    call loading_screen(7, "33") from _call_saki_house_loading
    jump E3_CMM_01
