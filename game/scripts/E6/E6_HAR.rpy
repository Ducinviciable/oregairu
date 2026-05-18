label E6_HAR_01:
    scene houseA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM10.ogg"
    window auto show dissolve
    "I was so bummed out about going on the ski trip at first, but now that it's over, it feels like it was nothing more than a fleeting dream."
    "I don't think I'll ever experience such a crazy trip, with classmates, teachers, and alumni that I never had the chance to cross paths with again."
    if ski_flag == "haruno":
        hachiman "(When I first met her, she seemed nothing but ruthlesss Goddess of Misfortune.)"
        hachiman "(No, rather, you turned out to be cold-blooded devil...)"
        hachiman "(Moreover, it should be illegal for someone so vicious to have such warm hands and soft lips...)"
        window auto hide dissolve
        show harunohachimanroomB with Fade(0.25,0.35, 0.5, color="#fff")
        window auto show dissolve
        voice "audio/voice/E6/HAR/01/HR/HR000.ogg"
        haruno "The contract is sealed."
        window auto hide dissolve
        stop voice
        hide harunohachimanroomB with Fade(0.25,0.35, 0.5, color="#fff")
        window auto show dissolve
        hachiman "(Uwaa, I don't know what to do anymore! Was she messing with me or was she serious!? Either way, what should I do!? I'm going crazy!)"
        window auto hide dissolve
        stop music fadeout 1.0
        jump E6_HAR_02
    elif ski_flag == "meguri":
        hachiman "(Yeah, I feel like I received healing for a lifetime to come. I'm glad I went on the ski trip.)"
        window auto hide dissolve
        show slopesA:
            zoom 2.0 xpos -1280 ypos -780
        show meguri heavy_coat mid happy at center:
            xoffset 25 yoffset 75
        with Fade(0.25,0.35, 0.5, color="#fff")
        window auto show dissolve
        "I  am genuinely happy that I was able to open up a little to Meguri-senpai, who up till now seemed somewhat distant."
        hachiman "(If only we'd been in the same year, I could've been blessed with one more year of Megurishu effect...)"
        "Thinking of the upcoming parting with Meguri-senpai, I find myself feeling surprisingly lonely."
        window auto hide dissolve
        hide slopesA
        hide meguri
        with Fade(0.25,0.35, 0.5, color="#fff")
        window auto show dissolve
        hachiman "(Thinking about it, she's the only person I ever called \"senpai\" with a sense of affection...)"
        window auto hide dissolve
        stop music fadeout 1.0
        jump E6_HAR_04

label E6_HAR_02:
    scene classroomA with Fade(1.0, 0.5, 1.0)
    play ambient "audio/sfx/SE05/SE05_09L.ogg"
    play sound "audio/sfx/SE02/SE02_09.ogg"
    window auto show dissolve
    voice "audio/voice/E6/HAR/02/XW/XW000.ogg"
    sg "Rise!"
    stop ambient fadeout 0.5
    voice "audio/voice/E6/HAR/02/XW/XW001.ogg"
    sg "Bow!"
    "I spent the last few days of the semester in anguish."
    window auto hide dissolve
    stop sound fadeout 0.5
    play ambient ["<silence 1.0>", "audio/sfx/SE06/SE06_14L.ogg"]
    scene sidewalkB with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    hachiman "(I haven't really heard from since then, so it's probably best I just forget about it...)"
    hachiman "(I say that, but I've been frantically checking my phone like some maiden in love... I really do care about this...)"
    "No matter how much I want to know her geniune intention, I'm not the type of person to just casually message her, nor is she the type of person to openly discuss her true self."
    window auto hide dissolve
    scene black with dissolve
    hachiman "(Best to just forget about it... huh?)"
    window auto hide dissolve
    stop ambient fadeout 0.5
    play sound ["<silence 0.5>", "audio/sfx/SE06/SE06_15.ogg"]
    scene outsideB with Dissolve(1.0)
    $renpy.pause(delay=0.5, hard=True)
    hachiman "(A familar-looking luxuary black car is sitting infront of my house...)"
    stop sound
    play sound "audio/sfx/SE06/SE06_10.ogg"
    $renpy.pause(delay=1.0, hard=True)
    voice "audio/voice/E6/HAR/02/HR/HR000.ogg"
    mystery "Took you long enough. Hurry up and get in."
    hachiman "(That voice...!)"
    play music "audio/bgm/BGM35.ogg"
    show haruno heavy_coat_sunset near_left angry at center with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E6/HAR/02/HA/HA000.ogg"
    hachiman "Well, I only just got here and I have a lot of things I need to do, so..."
    show haruno annoyed with dissolve
    voice "audio/voice/E6/HAR/02/HR/HR001.ogg"
    haruno "No, you don't. Hurry up and get in."
    voice "audio/voice/E6/HAR/02/HA/HA001.ogg"
    hachiman "............"
    window auto hide dissolve
    hide haruno with Dissolve(0.25)
    play sound "audio/sfx/SE06/SE06_11.ogg"
    $renpy.pause(delay=1.0, hard=True)
    play sound "audio/sfx/SE06/SE06_04.ogg"
    $renpy.pause(delay=1.0, hard=True)
    stop sound fadeout 1.0
    scene skyB at car_shake1 with Fade(1.0, 0.5, 1.0):
        zoom 1.75 xoffset -100 yoffset -150
    play ambient "<from 2.0>audio/sfx/SE06/SE06_05L.ogg"
    window auto show dissolve
    voice "audio/voice/E6/HAR/02/HA/HA002.ogg"
    hachiman "Um... Where are we going?"
    voice "audio/voice/E6/HAR/02/HR/HR002.ogg"
    haruno "Not telling~."
    voice "audio/voice/E6/HAR/02/HR/HR003.ogg"
    haruno "............"
    "It seems the ski trip incident wasn't an illusion. Haruno-san gently holding my hand was a true sing of that."
    hachiman "(M-my heart is starting to beat out of my chest... Where are we going, anyway?)"
    window auto hide dissolve
    scene skyC at car_shake1 with Fade(0.5, 0.5, 0.5):
        zoom 1.75 xoffset -100 yoffset -150
    window auto show dissolve
    voice "audio/voice/E6/HAR/02/HR/HR004.ogg"
    haruno "It's getting dark..."
    voice "audio/voice/E6/HAR/02/HA/HA003.ogg"
    hachiman "Well, it's night time, after all..."
    voice "audio/voice/E6/HAR/02/HR/HR005.ogg"
    haruno "*fufu*... Very astute observation."
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    stop ambient fadeout 0.5
    scene black with Fade(1.0, 1.0, 0)
    play ambient "<to 5.6>audio/sfx/SE06/SE06_09.ogg" noloop #adjustment required
    scene bridgeC with Fade(0, 2.0, 1.0)
    $renpy.pause(delay=1.0, hard=True)
    play sound "audio/sfx/SE06/SE06_10.ogg"
    $renpy.pause(delay=1.0, hard=True)
    stop ambient fadeout 0.5
    play sound "audio/sfx/SE06/SE06_07.ogg"
    show haruno heavy_coat_night mid_center happy at center with dissolve:
        xoffset -15 yoffset 75
    window auto show dissolve
    voice "audio/voice/E6/HAR/02/HR/HR006.ogg"
    haruno "Walk with me for a bit."
    window auto hide dissolve
    stop sound fadeout 1.0
    hide haruno with dissolve
    $renpy.pause(delay=1.5, hard=True)
    play ambient "audio/sfx/SE00/SE00_34.ogg"
    scene bridgeC
    show haruno heavy_coat_night near_left happy at center:
        xoffset 195 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E6/HAR/02/HA/HA004.ogg"
    hachiman "So... What's the point of all this?"
    show haruno vhappy with dissolve
    voice "audio/voice/E6/HAR/02/HR/HR007.ogg"
    haruno "Let's say it's to... confirm our contract."
    window auto hide dissolve
    stop voice
    stop ambient
    show harunohachimanroomB with Fade(0.25,0.35, 0.5, color="#fff")
    $renpy.pause(delay=1.0, hard=True)
    hide harunohachimanroomB with Fade(0.25,0.35, 0.5, color="#fff")
    play music "audio/bgm/BGM42.ogg"
    window auto show dissolve
    "Contract. The word reminds me of that night in the snowy mountains. The words we exchanged and the kiss we shared. Without even realizing, I quickly put a hand to my mouth."
    jump E6_HAR_03

label E6_HAR_03:
    show haruno happy with dissolve
    voice "audio/voice/E6/HAR/03/HR/HR000.ogg"
    haruno "Because it's you, Hikigaya-kun, I figured you'd just try to make up some reason to forget about it or pretend it never happened."
    voice "audio/voice/E6/HAR/03/HA/HA000.ogg"
    hachiman "...You know me too well."
    hide haruno
    $url = ["haruno heavy_coat_night near_center vhappy", "haruno heavy_coat_night near_center happy"]
    $multiImagePara = [250, 75, 0, 0, 3.8]
    call multiImage() from _call_multiImage_26
    voice "audio/voice/E6/HAR/03/HR/HR001.ogg"
    haruno "Right~! That's why I came to confirm our contract. So, what do you want to do?"
    window auto hide dissolve
    call finishmultiImage from _call_finishmultiImage_27
    scene harunobridgeA
    with dissolve
    window auto show dissolve
    "Haruno-san gives me a teasing look and smiles. It's the same as that time, no, it's always been this way. No matter what I do, I feel like she has me in the palm of her hand."
    "It's probably not just me that's like that. Likely Yukinoshita and a bunch of other people, too."
    "Ultimately, she's the only person that can play this role. She's more versatile than anyone else, more perfect than anyone else. Therefore, she is exempt from being anything else."
    "That's why she can't trust others."
    "She's like the Tyrant King. Because of her distrust of people, she tests them, making them expose their true intentions, in search of something genuine. She's always been this way."
    "She doesn't believe what she sees is a genuine thing, even when it's plainly laid out to her, so she wants to really dig deep and look inside, sometimes destroying it in the process."
    "-If that's how it is, I have to an answer for her."
    voice "audio/voice/E6/HAR/03/HA/HA001.ogg"
    hachiman "It's a little late for that, isn't it?"
    show harunobridgeB with dissolve
    voice "audio/voice/E6/HAR/03/HR/HR002.ogg"
    haruno "Hmm?"
    voice "audio/voice/E6/HAR/03/HA/HA002.ogg"
    hachiman "You wouldn't believe me no matter what I say."
    voice "audio/voice/E6/HAR/03/HR/HR003.ogg"
    haruno "Yes, you're right. There is no \"genuine thing\". Even if I saw it, I'd likely not believe it."
    voice "audio/voice/E6/HAR/03/HA/HA003.ogg"
    hachiman "Exactly. I don't know if it's real myself. Wouldn't know what it looks like."
    voice "audio/voice/E6/HAR/03/HR/HR004.ogg"
    haruno "............"
    voice "audio/voice/E6/HAR/03/HA/HA004.ogg"
    hachiman "So, in order to confirm it's existence, we should keep looking into the truths and the illusions, shouldn't we?"
    voice "audio/voice/E6/HAR/03/HR/HR005.ogg"
    haruno "...Are you sure you want to keep trying?"
    voice "audio/voice/E6/HAR/03/HA/HA005.ogg"
    hachiman "Well... I'm interested in it, myself."
    "Is the real thing what's hidden deep inside this slush? Or is something covered in this slush still genuine? Or maybe the slush itself is the real thing."
    hide harunobridgeB with dissolve
    voice "audio/voice/E6/HAR/03/HR/HR006.ogg"
    haruno "Then... let's re-establish our contract once more~."
    window auto hide dissolve
    scene harunohachimankissA with dissolve
    play sound "audio/sfx/SE01/SE01_12.ogg"
    $renpy.pause(delay=1.0, hard=True)
    window auto show dissolve
    "Haruno-san gently smiled and wrapped her arms around my neck."
    voice "audio/voice/E6/HAR/03/HR/HR007.ogg"
    haruno "Do you think something genuine exists?"
    voice "audio/voice/E6/HAR/03/HA/HA006.ogg"
    hachiman "...Well I can't say for sure."
    voice "audio/voice/E6/HAR/03/HR/HR008.ogg"
    haruno "Then let's find out."
    "-Haruno-san whispred and just as I realized our breaths had interwined..."
    window auto hide dissolve
    scene harunohachimankissB with dissolve
    window auto show dissolve
    "Our lips connected in a kiss deepre than before."
    window auto hide dissolve
    stop music fadeout 1.0
    scene white with Fade(2.0, 0, 1.0, color="#fff")
    $renpy.movie_cutscene("movies/ed04.mkv")
    jump E6_HAR_05

label E6_HAR_04:
    scene scouncilroomA with Fade(1.0, 0.5, 1.5)
    play music "audio/bgm/BGM44.ogg"
    show iroha school mid_center annoyed at center with dissolve:
        xoffset -5 yoffset 75
    window auto show dissolve
    voice "audio/voice/E6/HAR/04/IR/IR000.ogg"
    iroha "God, senpai. That doen't belong there!"
    voice "audio/voice/E6/HAR/04/HA/HA000.ogg"
    hachiman "No, you told me it did before, didn't you?"
    show iroha unimpressed with dissolve
    voice "audio/voice/E6/HAR/04/IR/IR001.ogg"
    iroha "Excuse me? No, I didn't."
    voice "audio/voice/E6/HAR/04/HA/HA001.ogg"
    hachiman "Right, of course, it was just a figment of my imagination. By the way, why are you having me help with this to begin with?"
    show iroha mid_left unimpressed with dissolve:
        xoffset -35 yoffset 65
    voice "audio/voice/E6/HAR/04/IR/IR002.ogg"
    iroha "Because you're a part of the Service Club, aren't you? I'm busy with managing the back end of the graduation ceremony."
    "After the graduation  ceremony to send off the third-year students was over without incident, for some reason, I, rather than the student council, was stuck doing chores for Isshiki."
    hachiman "(So I can't really get lost in the emotion of seeing Meguri-senpai off...)"
    show iroha mid_center happy with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E6/HAR/04/IR/IR003.ogg"
    iroha "Ah, well I still have work to do, so I'm leaving this to you!"
    voice "audio/voice/E6/HAR/04/HA/HA002.ogg"
    hachiman "Ah, that right? Off you go..."
    show iroha vhappy with dissolve
    voice "audio/voice/E6/HAR/04/IR/IR004.ogg"
    iroha "My, you're so reliable, senpai~! I'm counting on you."
    window auto hide dissolve
    scene scouncilroomA with fade
    play sound "audio/sfx/SE04/SE04_13.ogg"
    window auto show dissolve
    "After Isshiki left, I was left alone in the student council room. As I quietly did as she said and cleaned up when there came a knock at the door."
    play sound "audio/sfx/SE04/SE04_01.ogg"
    play music "audio/bgm/BGM10.ogg"
    show meguri school mid happy at center with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E6/HAR/04/MG/MG000.ogg"
    meguri "I'm coming in. Huh? It's Hikigaya-kun."
    stop sound
    voice "audio/voice/E6/HAR/04/HA/HA003.ogg"
    hachiman "Shiromeguri-senpai... Is something wrong?"
    show meguri frown with dissolve
    voice "audio/voice/E6/HAR/04/MG/MG001.ogg"
    meguri "Well, I just came to say hi... I'm really leaving this student council room behind... I'm going to miss it."
    voice "audio/voice/E6/HAR/04/HA/HA004.ogg"
    hachiman "You can come over and hang out anytime."
    show meguri surprised with dissolve
    voice "audio/voice/E6/HAR/04/MG/MG002.ogg"
    meguri "Huh?"
    voice "audio/voice/E6/HAR/04/HA/HA005.ogg"
    hachiman "You might not have imagined this, but... If you ever want to reminisce about those times, I'd be happy to be there to listen."
    show meguri vhappy with dissolve
    voice "audio/voice/E6/HAR/04/MG/MG003.ogg"
    meguri "Hikigaya-kun... thank you."
    "At that moment."
    window auto hide dissolve
    hide meguri with dissolve
    show meguriStudentCouncil with dissolve
    play sound "audio/sfx/SE01/SE01_12.ogg"
    window auto show dissolve
    "Meguri-senpai suddenly wrapped her arms around me from behind. As I was dumbfounded, not knowing what had happened, I was left at her mercy."
    voice "audio/voice/E6/HAR/04/MG/MG004.ogg"
    meguri "It's a promise then... See you later, Hikigaya-kun."
    voice "audio/voice/E6/HAR/04/HA/HA006.ogg"
    hachiman "S-See you..."
    window auto hide dissolve
    stop music fadeout 1.0
    scene white with Fade(2.0, 0, 1.0, color="#fff")
    $renpy.movie_cutscene("movies/ed04.mkv")
    jump E6_HAR_06

label E6_HAR_05:
    scene skyA with Fade(1.0, 0.5, 1.5) #To be edited
    show skyB at delayedDissolve1
    show skyC at delayedDissolve2
    "-And so, some time passed since the contract was renewed."
    "However, it doesn't mean that anything much has changed, it's just that in my everyday life of unnoticeable deception, one big lie has been mixed in."
    "There is always someone beside me who keeps lying, and thanks to that, my daily life is not much different from before."
    "-Let me correct that. It's wrong to say there hasn't been much change. I've been involved in unimaginable fights between sisters and unexpected fights between close friends."
    "However, it can be said that by putting another corner on the stagnant and unstable triangle, it has become a stable square."
    window auto hide dissolve
    scene black
    show harunoBedA
    with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM50.ogg"
    window auto show dissolve
    voice "audio/voice/E6/HAR/05/HR/HR000.ogg"
    haruno "Haaah, I'm so tired again today. Hey, Hikigaya-kun~? Is dinner ready yet~?"
    "The prevoisly mentioned corner to a stable square, Haruno-san, can be heard complaining an rolling on the bed, defenseless and vulnerable."
    voice "audio/voice/E6/HAR/05/HA/HA000.ogg"
    hachiman "What's up with you? Suddenly just rolling on the bed like that..."
    voice "audio/voice/E6/HAR/05/HR/HR001.ogg"
    haruno "What's the big deal~? You live alone. There's no one here, so I'm not bothering anyone."
    voice "audio/voice/E6/HAR/05/HA/HA001.ogg"
    hachiman "I'm here, you know, there's an actual person here. Can you not treat me like I'm not human, please?"
    voice "audio/voice/E6/HAR/05/HA/HA002.ogg"
    hachiman "By the way, how come you're here today when you left the other day super pissed for some reason?"
    window auto hide dissolve
    stop voice
    show harunoBedA at truecenter with dissolve:
        zoom 1.5 xoffset -300
    window auto show dissolve
    voice "audio/voice/E6/HAR/05/HR/HR002.ogg"
    haruno "What~? It wasn't just for \"some reason\", now, was it? You went for a meal with Yukino-chan without permission! That's a breach of contract!"
    voice "audio/voice/E6/HAR/05/HA/HA003.ogg"
    hachiman "No, that was just a small highschool reunion. Yuigahama was there, too. It wasn't a breach of contract..."
    voice "audio/voice/E6/HAR/05/HR/HR003.ogg"
    haruno "Gahama-chan was there, too!? That's a double! A double breach of contract! Double yakuman!"
    voice "audio/voice/E6/HAR/05/HA/HA004.ogg"
    hachiman "I'm telling you, it was just a reunion, it was no breach of contract. Totsuka was there, too... Wait, what the hell is \"yakuman\"?"
    voice "audio/voice/E6/HAR/05/HR/HR004.ogg"
    haruno "What!? Totsuka-kun, too! That's a triple! Triple breach of contract! Triple yakuman!"
    voice "audio/voice/E6/HAR/05/HA/HA005.ogg"
    hachiman "What are you going on about... Well, Totsuka was as cute as ever, though."
    voice "audio/voice/E6/HAR/05/HR/HR005.ogg"
    haruno "Mmm... What about Yukino-chan and the others? Anything different about them?"
    voice "audio/voice/E6/HAR/05/HA/HA006.ogg"
    hachiman "Well, not really. Still the same as always."
    hide harunoBedA
    show harunoBedA
    with dissolve
    "I don't think Haruno-san is asking simply about their appearances or their day-to-day life. She wouldn't ask something as simple as that. I consciously answered the question, taking that into consideration."
    "Some time has passed since back then, and my relationship with them had been stuck in limbo for the most part, back and forth between friendship and non-friendship."
    "From an outsider perspective, these relationships seems like a complete quagmire."
    "And all that is because one meddling demon is right around every corner. Poking her head in and getting involved at every oppurtunity."
    voice "audio/voice/E6/HAR/05/HR/HR006.ogg"
    haruno "Lucky you~. I wish I could'vd seen Yukino-chan..."
    voice "audio/voice/E6/HAR/05/HA/HA007.ogg"
    hachiman "I tried to call you once, but you were suddenly abroad at that time, without even saying anything..."
    voice "audio/voice/E6/HAR/05/HR/HR007.ogg"
    haruno "I told you I had work, didn't I~?"
    voice "audio/voice/E6/HAR/05/HA/HA008.ogg"
    hachiman "Yeah, I heard about it via e-mail when you had alraedy arrived..."
    voice "audio/voice/E6/HAR/05/HR/HR008.ogg"
    haruno "Ah, so that's why you're sulking."
    voice "audio/voice/E6/HAR/05/HA/HA009.ogg"
    hachiman "Hah? I'm not sulking at all..."
    voice "audio/voice/E6/HAR/05/HR/HR009.ogg"
    haruno "You're still as honest as ever in the weirdest ways, so cute~. Oh, by the way, how is job hunting going?"
    voice "audio/voice/E6/HAR/05/HA/HA010.ogg"
    hachiman "It's going fine for the most part. Everyone is tied up with putting themselves out there right now."
    voice "audio/voice/E6/HAR/05/HR/HR010.ogg"
    haruno "Oh, I see. Yukino-chan is at that stage now, too... Everyone is growing up, huh? It's about time, now, too."
    voice "audio/voice/E6/HAR/05/HA/HA011.ogg"
    hachiman "About time for what?"
    window auto hide dissolve
    stop voice
    play sound "audio/sfx/SE01/SE01_55.ogg"
    show harunoBedA at center, Shake(None, 0.75, dist=100):
        zoom 2.0 xoffset -650 yoffset -1060
    $renpy.pause(delay=1.0, hard=True)
    stop sound
    window auto show dissolve
    "As I turned my head, Haruno-san reached for me and pulled me onto the bed."
    voice "audio/voice/E6/HAR/05/HA/HA012.ogg"
    hachiman "Whoa..."
    show harunoBedB with dissolve
    voice "audio/voice/E6/HAR/05/HR/HR011.ogg"
    haruno "Do you want to... renew the contract?"
    voice "audio/voice/E6/HAR/05/HA/HA013.ogg"
    hachiman "You're still going on about that...?"
    voice "audio/voice/E6/HAR/05/HR/HR012.ogg"
    haruno "Of course I am. It's the pretext for our relationship."
    voice "audio/voice/E6/HAR/05/HA/HA014.ogg"
    hachiman "You're right."
    "She takes resposibility for all of mine, all of our lies, to keep our lukewarm, but pleasantly fierce relationship in place."
    "As soon as the contract is gone, this relationship will fall apart."
    "More than anything, I feel like if I lose this lie, I'll lose this person, too."
    voice "audio/voice/E6/HAR/05/HR/HR013.ogg"
    haruno "Hey... have you found your genuine article?"
    voice "audio/voice/E6/HAR/05/HA/HA015.ogg"
    hachiman "Not yet, I suppose. So... I'll be extending my contract."
    voice "audio/voice/E6/HAR/05/HR/HR014.ogg"
    haruno "Okay, let me do that for you."
    window auto hide dissolve
    stop voice
    show harunoBedB at truecenter with dissolve:
        zoom 1.5 xoffset -300
    window auto show dissolve
    "With that short answer, Haruno-san sinks down next to me."
    voice "audio/voice/E6/HAR/05/HR/HR015.ogg"
    haruno "...Well then, the contract is now extended~."
    hide harunoBedB
    show harunoBedB
    with dissolve
    "Haruno-san whispered those words to me as our lips parted."
    "Like that, we will continue to tell lies. We will defile and destroy until we hit the very bottom.We will continue to hold on to something that won't change, however."
    "And that's our relationship, filled with errors as it is. But maybe - No, I'm sure that's a lie, too."
    window auto hide dissolve
    stop music fadeout 2.0
    scene harunoEnding with Fade(2.0, 1.0, 1.0, color="#fff")
    call game_over("Yukinoshita Haruno") from _call_game_over_2
    return

label E6_HAR_06:
    scene parkA with Fade(0.5, 0.5, 0.5)
    play sound "<to 1.5>audio/sfx/SE00/SE00_05.ogg"
    $renpy.pause(delay=1.5,hard=True)
    show meguri coat mid surprised at center with dissolve:
        xoffset 25 yoffset 75
    play music "audio/bgm/BGM48.ogg"
    window auto show dissolve
    voice "audio/voice/E6/HAR/06/MG/MG000.ogg"
    meguri "Sorry, did you wait? Woah!"
    stop sound
    hachiman "(Ah, watch out!)"
    show meguri angry with dissolve
    voice "audio/voice/E6/HAR/06/MG/MG001.ogg"
    meguri "That was close..."
    show meguri happy with dissolve
    voice "audio/voice/E6/HAR/06/MG/MG002.ogg"
    meguri "There."
    "Meguri-senpai, who was about to fall forward, somehow managed to regain her balance and struck a triumphant pose."
    hachiman "(Wow. She somehow managed to avoid falling...)"
    voice "audio/voice/E6/HAR/06/HA/HA000.ogg"
    hachiman "You don't have to rush like that...."
    show meguri vhappy with dissolve
    voice "audio/voice/E6/HAR/06/MG/MG003.ogg"
    meguri "Ehehe. I just wanted to meet you sooner."
    hachiman "(Gu... Dying from Megurishu factor overdose seems like the best way to die...)"
    show meguri happy with dissolve
    voice "audio/voice/E6/HAR/06/MG/MG004.ogg"
    meguri "So where are we gonna go today?"
    voice "audio/voice/E6/HAR/06/HA/HA001.ogg"
    hachiman "How about an art museum? They were giving out tickets at the department."
    "Thanks to the fact I'm going to a different University than Meguri-senpai, I'm able to offer her small side perks that I get from my university's department. When I took the tickets out, Meguri-senpai's"
    "face lit up."
    show meguri vhappy with dissolve
    voice "audio/voice/E6/HAR/06/MG/MG005.ogg"
    meguri "Oh, that's great~! I wanted to go, too!"
    voice "audio/voice/E6/HAR/06/HA/HA002.ogg"
    hachiman "That's good then."
    window auto hide dissolve
    scene stationA:
        zoom 2.0 xalign 0 yalign 1.0
    show meguri coat near happy at right:
        yoffset 75 xoffset -270
    with fade
    play sound "audio/sfx/SE00/SE00_18L.ogg"
    window auto show dissolve
    "With our destination decided on, we started walking side by side."
    stop sound fadeout 0.5
    show meguri frown with dissolve
    hachiman "(Hm?)"
    voice "audio/voice/E6/HAR/06/HA/HA003.ogg"
    hachiman "Um, did something happen?"
    voice "audio/voice/E6/HAR/06/MG/MG006.ogg"
    meguri "Yeah. You know, Hikigaya-kun. Today a friend asked me..."
    show meguri angry with dissolve
    voice "audio/voice/E6/HAR/06/MG/MG007.ogg"
    meguri "How come me and you started hanging out so often?"
    voice "audio/voice/E6/HAR/06/HA/HA004.ogg"
    hachiman "Ah."
    hachiman "(Come to think of it, it feels like I'm missing some part of a bigger story... Why did we start hanging out more?)"
    "While I'm rummaging through my memories, Meguri-senpai was mulling it over with her arms folded beside me."
    show meguri unimpressed with dissolve
    voice "audio/voice/E6/HAR/06/MG/MG008.ogg"
    meguri "Hmm, I wonder if this mean we're dating..."
    voice "audio/voice/E6/HAR/06/HA/HA005.ogg"
    hachiman "B-Beats me..."
    hide meguri
    $url = ["meguri coat near unimpressed", "meguri coat near vhappy"]
    $multiImagePara = [-270, 75, 0, 0, 1.5]
    call multiImage(1,True) from _call_multiImage_90
    "While I was lost on what to say, Meguri-senpai suddenly looked up and smiled."
    call finishmultiImage from _call_finishmultiImage_94
    show meguri coat near vhappy at right:
        xoffset -270 yoffset 75
    voice "audio/voice/E6/HAR/06/MG/MG009.ogg"
    meguri "Well, whatever!"
    show meguri happy with dissolve
    voice "audio/voice/E6/HAR/06/MG/MG010.ogg"
    meguri "More importantly, let's hurry up and go! We won't be able to take our time!"
    voice "audio/voice/E6/HAR/06/HA/HA006.ogg"
    hachiman "Yeah."
    window auto hide dissolve
    stop voice
    show meguriHachiman with dissolve
    play ambient "audio/sfx/SE00/SE00_20L.ogg"
    window auto show dissolve
    "After firmly taking my hand, Meguri-senpai starts walking at a brisk pace."
    voice "audio/voice/E6/HAR/06/HA/HA007.ogg"
    hachiman "W-We don't need to rush. We still have time..."
    hachiman "(Meguri-senpai, who's pulling me by the hand, is really cute, but I'm worried she might fall again!)"
    voice "audio/voice/E6/HAR/06/MG/MG011.ogg"
    meguri "Ahaha, that's true."
    "As we walk together, side by side, hand in hand, Meguri-senpai starts happily swinging her arm back and forth."
    voice "audio/voice/E6/HAR/06/MG/MG012.ogg"
    meguri "Fufu..."
    voice "audio/voice/E6/HAR/06/HA/HA008.ogg"
    hachiman "Haha..."
    "I guess it's true that it doesn't really matter what the reason was. Thinking along those lines, I put a little more strength into my grip on her hand."
    window auto hide dissolve
    stop ambient fadeout 0.5
    stop music fadeout 2.0
    scene meguriEnding with Fade(2.0, 1.0, 1.0, color="#fff")
    call game_over("Shiromeguri Meguri") from _call_game_over_9
    return
