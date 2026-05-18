label E3_YUI_01:
    voice "audio/voice/E3/YUI/01/YI/YI000.ogg"
    yui "I'm worried about Yukinon..."
    voice "audio/voice/E3/YUI/01/HA/HA000.ogg"
    hachiman "Mhm..."
    "Suddenly, I was reminded of the incident in middle school... Regarding Orimoto..."
    hachiman "(The rumours of the confession and both of us being together, the ones affected feel really bad...)"
    voice "audio/voice/E3/YUI/01/YI/YI001.ogg"
    yui "Hikki~, what are you thinking about?"
    voice "audio/voice/E3/YUI/01/HA/HA001.ogg"
    hachiman "Eh? No, it's nothing."
    hide yui with dissolve
    stop music fadeout 0.5
    call card_loading from _call_card_loading_2
    scene hallwayA
    show yui school mid_center pout at center:
        xoffset 0 yoffset 75
    $card_queue = ["About\nromance", "About the\nnew semester", "Career\npath", "About the\nYukinoshita\nand\nHayama\nrumours", "About\nHayama's\ngroup", "Cut the\nconversation\nshort"]
    play music "audio/bgm/BGM31.ogg"
    $yui_school_card_count = 0
    $yui_school_ellipses = 0
    jump yui_school_cards

label yui_school_cards:
    if yui_school_card_count < 5:
        $yui_school_card_count += 1
        $renpy.pause(delay=0.5, hard=True)
        $ch2 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch2)
        $ch3 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch3)
        window auto hide dissolve
        call screen three_minigame("...", ch2, ch3) with dissolve
        if _return == 1:
            "not done"
            $card_queue.append(ch2)
            $card_queue.append(ch3)
            $yui_school_card_count -= 1
            jump yui_school_cards
        elif _return == 2:
            $card_queue.append(ch3)
            if ch2 == "About\nromance":
                jump romance_card
            elif ch2 == "About the\nnew semester":
                jump new_semester_card
            elif ch2 == "Career\npath":
                jump career_path_card
            elif ch2 == "About the\nYukinoshita\nand\nHayama\nrumours":
                jump rumours_card
            elif ch2 == "About\nHayama's\ngroup":
                jump hayama_group_card
            else:
                "not done"
                $card_queue.append(ch2)
                $yui_school_card_count -= 1
                jump yui_school_cards
        elif _return == 3:
            $card_queue.append(ch2)
            if ch3 == "About\nromance":
                jump romance_card
            elif ch3 == "About the\nnew semester":
                jump new_semester_card
            elif ch3 == "Career\npath":
                jump career_path_card
            elif ch3 == "About the\nYukinoshita\nand\nHayama\nrumours":
                jump rumours_card
            elif ch3 == "About\nHayama's\ngroup":
                jump hayama_group_card
            else:
                "not done"
                $card_queue.append(ch3)
                $yui_school_card_count -= 1
                jump yui_school_cards
    else:
        jump extendedyuihallway

label new_semester_card:
    voice "audio/voice/E3/YUI/01/HA/HA032.ogg"
    hachiman "... Ever since the new semester started, it feels like a lot of troublesome things have been going on, huh?"
    voice "audio/voice/E3/YUI/01/YI/YI039.ogg"
    yui "Yeah..."
    voice "audio/voice/E3/YUI/01/HA/HA033.ogg"
    hachiman "For example..."
    show yui school mid_center surprised with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI040.ogg"
    yui "No, you don't have to tell me! It feels like I already know what you're gonna say..."
    show yui school mid_center angry with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI041.ogg"
    yui "Hikki, spend some actual time thinking about your career path!"
    hachiman "(S-She knew!?)"
    jump yui_school_cards

label career_path_card:
    voice "audio/voice/E3/YUI/01/HA/HA027.ogg"
    hachiman "Oh yeah... The career path..."
    show yui school mid_left surprised with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI033.ogg"
    yui "Eh?"
    voice "audio/voice/E3/YUI/01/HA/HA028.ogg"
    hachiman "Have you decided what path to take?"
    show yui school mid_center pout with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI034.ogg"
    yui "Um... I haven't really sat down and thought about it, but I'm not that smart, so the sciences are probably not an option... Hahaha..."
    voice "audio/voice/E3/YUI/01/HA/HA029.ogg"
    hachiman "You should apologize to all of liberal arts right now. You don't choose the field you're going into just 'cause you're not smart. Think about what you actually want."
    show yui school mid_center sad with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI035.ogg"
    yui "Uuuu... I know that, but..."
    voice "audio/voice/E3/YUI/01/YI/YI036.ogg"
    yui "Oh yeah, Hikki~, your academics are actually pretty good..."
    voice "audio/voice/E3/YUI/01/HA/HA030.ogg"
    hachiman "No, actually..."
    show yui school mid_center happy with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI037.ogg"
    yui "We probably can't go to the same university..."
    voice "audio/voice/E3/YUI/01/HA/HA031.ogg"
    hachiman "...We don't really have to go to the same university right? Please think about it more."
    show yui school mid_center pout with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI038.ogg"
    yui "Oh..."
    jump yui_school_cards

label hayama_group_card:
    voice "audio/voice/E3/YUI/01/HA/HA023.ogg"
    hachiman "Yukinoshita's affected as well, but... this time, so are Hayama and the others, right?"
    show yui school mid_center sad with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI029.ogg"
    yui "You knew just by looking, right? Yumiko's taking it extra hard..."
    voice "audio/voice/E3/YUI/01/HA/HA024.ogg"
    hachiman "I bet..."
    voice "audio/voice/E3/YUI/01/YI/YI030.ogg"
    yui "Hayato-kun was also kind of angry... It was a bit scary."
    voice "audio/voice/E3/YUI/01/HA/HA025.ogg"
    hachiman "It was?"
    "I was about to say it was unusual to see him angry, but then I remembered his and Yukinoshita's family situations."
    hachiman "(In that sense, it's a pretty delicate situation...)"
    show yui school mid_center happy with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI031.ogg"
    yui "It's kind of rare to see you concerned about Hayama and the others."
    voice "audio/voice/E3/YUI/01/HA/HA026.ogg"
    hachiman "I'm not worried about them. I just thought you seemed kind of uncomfortable."
    show yui school mid_center vhappy with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI032.ogg"
    yui "...! I wasn't really, but... Ehehe..."
    hachiman "(I feel like she misunderstood me somehow...)"
    jump yui_school_cards

label romance_card:
    voice "audio/voice/E3/YUI/01/HA/HA018.ogg"
    hachiman "Romance... Seems troublesome, huh..."
    show yui school mid_left surprised with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI023.ogg"
    yui "Troublesome!?"
    voice "audio/voice/E3/YUI/01/HA/HA019.ogg"
    hachiman "Nobody would want to go out with some one that they don't like, right?"
    "Frankly, even if I'm unsure what Yukinoshita and Hayama think, looking as a bystander, they don't seem to have any romantic interest in one another."
    "Even if they do, such rumours may stray from what they may have initially felt."
    show yui school mid_center happy with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI024.ogg"
    yui "Ah, that's what you meant..."
    voice "audio/voice/E3/YUI/01/HA/HA020.ogg"
    hachiman "...?"
    voice "audio/voice/E3/YUI/01/YI/YI025.ogg"
    yui "So... , if it's someone you really like, it's okay?"
    voice "audio/voice/E3/YUI/01/HA/HA021.ogg"
    hachiman "Forget me, the other probably won't like it anyway. Rumours as a whole aren't something very likeable, so no it's not okay."
    show yui school mid_center surprised with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI026.ogg"
    yui "Why'd you automatically think the other person wouldn't like it!?"
    show yui school mid_center pout with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI027.ogg"
    yui "There probably are people who... would."
    voice "audio/voice/E3/YUI/01/HA/HA022.ogg"
    hachiman "'Course not."
    show yui school mid_center surprised with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI028.ogg"
    yui "You're doubling down!?"
    jump yui_school_cards

label rumours_card:
    voice "audio/voice/E3/YUI/01/HA/HA015.ogg"
    hachiman "Spreading rumours sure is irresponsible..."
    show yui school mid_center pout with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI020.ogg"
    yui "Yeah..."
    voice "audio/voice/E3/YUI/01/HA/HA016.ogg"
    hachiman "It only affects the people around them, not themselves. What's more, the people spreading the rumours themselves don't even realize it."
    show yui school mid_center happy with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI021.ogg"
    yui "You really... understand this sort of thing, Hikki."
    voice "audio/voice/E3/YUI/01/HA/HA017.ogg"
    hachiman "I guess."
    show yui school mid_center vhappy with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI022.ogg"
    yui "You're... pretty amazing like that... sometimes."
    show yui school mid_left angry with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI054.ogg"
    yui "Um... Wanna head to club together?"
    voice "audio/voice/E3/YUI/01/HA/HA045.ogg"
    hachiman "Both together or seperately works for me."
    show yui school mid_left surprised with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI055.ogg"
    yui "Oh... Huh!?"
    voice "audio/voice/E3/YUI/01/HA/HA046.ogg"
    hachiman "What's wrong?"
    show yui school mid_left pout with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI056.ogg"
    yui "It's just, I thought you'd say the usual \"Let's just go seperately.\""
    hachiman "(I didn't really put any thought into that reply, but now that you say that, I'm getting super self-conscious! Stop it!)"
    voice "audio/voice/E3/YUI/01/HA/HA047.ogg"
    hachiman "Ah, I see... Sorry."
    show yui school mid_center pout with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI057.ogg"
    yui "L-Let's... go together then."
    voice "audio/voice/E3/YUI/01/HA/HA048.ogg"
    hachiman "I'll wait for you in the hallway."
    show yui school mid_center vhappy with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/01/YI/YI058.ogg"
    yui "Okay!"
    jump extendedyuihallway

label extendedyuihallway:
    stop music fadeout 1.0
    scene hallwayA
    show yui school mid_center pout at center:
        xoffset 0 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM46.ogg"
    voice "audio/voice/E3/YUI/01/YI/YI059.ogg"
    yui "With these kinds of rumours, even if the rumoured about person themselves say it isn't bothering them, in reality, it probably does, right?"
    voice "audio/voice/E3/YUI/01/HA/HA049.ogg"
    hachiman "Well... That's just how it goes."
    show yui school mid_center sad with dissolve
    voice "audio/voice/E3/YUI/01/YI/YI060.ogg"
    yui "But only waiting for the rumour to die down without being able to do anything..."
    hachiman "(I should've known. Gahama-san's probably experienced something like this...)"
    voice "audio/voice/E3/YUI/01/HA/HA050.ogg"
    hachiman "What if it were you?"
    show yui school mid_center surprised with dissolve
    voice "audio/voice/E3/YUI/01/YI/YI061.ogg"
    yui "Huh?"
    voice "audio/voice/E3/YUI/01/HA/HA051.ogg"
    hachiman "What would you do if there was a rumor like that about you?"
    voice "audio/voice/E3/YUI/01/YI/YI062.ogg"
    yui "W-Why do you ask all of a sudden?"
    voice "audio/voice/E3/YUI/01/HA/HA052.ogg"
    hachiman "No reason really."
    show yui school mid_center happy with dissolve
    voice "audio/voice/E3/YUI/01/YI/YI063.ogg"
    yui "Let's see... I'd use the opportunity and confess to the person I like! Or something."
    voice "audio/voice/E3/YUI/01/HA/HA053.ogg"
    hachiman "For real?"
    show yui school mid_center blush with dissolve
    voice "audio/voice/E3/YUI/01/YI/YI064.ogg"
    yui "Well, how do I say this... I'm just the kind of person that's not the most decisive, so sometimes I need a little push. Haha..."
    voice "audio/voice/E3/YUI/01/HA/HA054.ogg"
    hachiman "You're pretty optimistic, hey?"
    hachiman "(Besides, that'll only work if you had someone you wanted to confess to in the first place.)"
    voice "audio/voice/E3/YUI/01/YI/YI065.ogg"
    yui "Ah, I mean, this is just a \"What if\" thing! It doesn't really mean anything! Haha..."
    stop music fadeout 1.0
    window auto hide dissolve
    jump E3_YUI_06

label E3_YUI_06:
    scene hallwayB
    show yui school_sunset mid_center pout at center:
        yoffset 75
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E3/YUI/06/YI/YI001.ogg"
    yui "Um... Yukinon probably isn't feeling well..."
    voice "audio/voice/E3/YUI/06/HA/HA001.ogg"
    hachiman "Well, we can't do anything about it now."
    "That said, it's not like I don't understand her feelings. If I was alone, I'd hesitate going, too."
    show yui school_sunset mid_center angry at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/06/YI/YI002.ogg"
    yui "Y-You're right... Here we go!"
    scene clubroomB with wipeleft
    play sound "audio/sfx/SE04/SE04_01.ogg"
    show yui school_sunset mid_right vhappy at left with easeinleft:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/06/YI/YI003.ogg"
    yui "Yahallo~! Yukinon!"
    show yukino school_sunset mid_left happy at right with dissolve:
        xoffset -100 yoffset 75
    play music "audio/bgm/BGM11.ogg"
    voice "audio/voice/E3/YUI/06/YK/YK000.ogg"
    yukino "Yuigahama-san... Hello."
    voice "audio/voice/E3/YUI/06/HA/HA002.ogg"
    hachiman "...Oh"
    "She looks the same at first glance, but then, her expression looks more tired than usual."
    show yui school_sunset mid_right happy at left with dissolve:
        yoffset 75
    voice "audio/voice/E3/YUI/06/YI/YI009.ogg"
    yui "Um, once again... Happy Birthday!"
    show yui school_sunset mid_center happy at left with dissolve:
        xoffset 200 yoffset 75
    voice "audio/voice/E3/YUI/06/YI/YI010.ogg"
    yui "Come on, Hikki, you too!"
    show yukino school_sunset mid_left surprised at right with dissolve
    voice "audio/voice/E3/YUI/06/HA/HA005.ogg"
    hachiman "H-Happy Birthday."
    show yui school_sunset mid_center vhappy at left with dissolve
    voice "audio/voice/E3/YUI/06/YI/YI011.ogg"
    yui "We couldn't celebrate it properly the other day. So I talked to Hikki about how I wanted us to do it properly."
    voice "audio/voice/E3/YUI/06/HA/HA006.ogg"
    hachiman "Y-Yeah, that's true."
    voice "audio/voice/E3/YUI/06/YK/YK006.ogg"
    yukino "Hikigaya-kun... Yuigahama-san... What do I say..."
    show yukino school_sunset mid_left vhappy at right with dissolve
    voice "audio/voice/E3/YUI/06/YK/YK007.ogg"
    yukino "Having someone congratulate me like this... It's a first time for me. So... Thank you."
    show yui school_sunset mid_right blush at left with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E3/YUI/06/YI/YI012.ogg"
    yui "C-Come on... it's not that big a deal, Yukinon!"
    show yui school_sunset mid_right vhappy at left with dissolve
    voice "audio/voice/E3/YUI/06/YI/YI013.ogg"
    yui "And, check this out... tah-da! We got a cake, too!"
    show yui school_sunset mid_right happy at left with dissolve
    voice "audio/voice/E3/YUI/06/YI/YI014.ogg"
    yui "We really wanted to celebrate your birthday with you, so we were so excited!"
    voice "audio/voice/E3/YUI/06/YK/YK008.ogg"
    yukino "..."
    show yui school_sunset mid_right sad at left with dissolve
    voice "audio/voice/E3/YUI/06/YI/YI015.ogg"
    yui "So, um..."
    voice "audio/voice/E3/YUI/06/HA/HA007.ogg"
    hachiman "..."
    "Yuigahama should have noticed too, Yukinoshita looks happy but still seems apathetic."
    "Despite knowing about the rumours, she pretends she doesn't... I'm doing it as well, but looking at her acting like that makes my heart ache a little."
    show yukino school_sunset mid_left unimpressed at right with dissolve
    voice "audio/voice/E3/YUI/06/YK/YK009.ogg"
    yukino "You're gonna bring up the rumour, right?"
    show yukino school_sunset mid_left vhappy at right with dissolve
    voice "audio/voice/E3/YUI/06/YK/YK010.ogg"
    yukino "It's okay, I'm not bothered by it."
    voice "audio/voice/E3/YUI/06/YI/YI016.ogg"
    yui "But..."
    voice "audio/voice/E3/YUI/06/YK/YK011.ogg"
    yukino "Hayato-kun's and my family often go out together, so... As we were doing our New Year's greet, someone must have seen us and gotten the wrong idea."
    voice "audio/voice/E3/YUI/06/YI/YI019.ogg"
    yui "S-So that's what happened..."
    hachiman "(I see. So that's what Yuigahama saw.)"
    voice "audio/voice/E3/YUI/06/YK/YK016.ogg"
    yukino "Also... As long as the people close to me understand... That's enough for me."
    "Yukinoshita gently smiled while saying so. I honestly thought that she wasn't lying..."
    show yui school_sunset mid_right happy at left with dissolve
    voice "audio/voice/E3/YUI/06/YI/YI020.ogg"
    yui "Yukinon..."
    voice "audio/voice/E3/YUI/06/HA/HA008.ogg"
    hachiman "...I see."
    voice "audio/voice/E3/YUI/06/YK/YK014.ogg"
    yukino "And... thank you... for the presents. I'm... really happy."
    show yui school_sunset mid_right vhappy at left with dissolve
    voice "audio/voice/E3/YUI/06/YI/YI021.ogg"
    yui "For sure! I'll cut the cake then!"
    show yui school_sunset mid_center vhappy at left with dissolve:
        xoffset 200 yoffset 75
    voice "audio/voice/E3/YUI/06/YI/YI022.ogg"
    yui "Hikki~! Clear up the desk a bit~!"
    hachiman "(Well, it's not like I want to talk about the rumours either, so let's leave it at that)."
    voice "audio/voice/E3/YUI/06/HA/HA009.ogg"
    hachiman "Sure thing."
    stop music fadeout 1.0
    scene black with Fade(1.0, 0.5, 1.0)
    jump E3_YUI_07

label E3_YUI_07:
    scene gatesC with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM42.ogg"
    "Since winter started, once the sun sets, it gets dark pretty fast."
    "As it gets dark earlier, the time to finish club activities is earlier as well. But Yuigahama still seemed uncomfortable about something and suddenly clasped her hands."
    show yukino school_dark mid_center happy at left:
        xoffset 50 yoffset 75
    show yui school_dark mid_center vhappy at right:
        xoffset -300 yoffset 75
    with dissolve
    voice "audio/voice/E3/YUI/07/YI/YI000.ogg"
    yui "...Right! How about the 3 of us head home together after getting some tea?"
    voice "audio/voice/E3/YUI/07/YK/YK000.ogg"
    yukino "I don't really mind... But why?"
    show yui school_dark mid_left happy at right with dissolve
    voice "audio/voice/E3/YUI/07/YI/YI001.ogg"
    yui "Well, no special reason... I just kinda wanted us to do something on the way home."
    voice "audio/voice/E3/YUI/07/HA/HA000.ogg"
    hachiman "...Sorry, I'll have to go home first. Komachi asked me to do some shopping."
    voice "audio/voice/E3/YUI/07/YI/YI002.ogg"
    yui "Really? Then, how about you, Yukinon?"
    show yukino school_dark mid_center vhappy at left with dissolve
    voice "audio/voice/E3/YUI/07/YK/YK001.ogg"
    yukino "I don't mind. I have don't have any plans in particular for today."
    show yui school_dark mid_left vhappy at right with dissolve
    voice "audio/voice/E3/YUI/07/YI/YI003.ogg"
    yui "Yay~! Let's go!"
    stop music fadeout 1.0
    scene black with Fade(1.0, 0.5, 0)
    hide yui
    hide yukino
    scene cafeCLoading with Fade(1.0, 2, 1.0)
    $renpy.pause(delay=2.0, hard=True)
    show yui school mid_right vhappy at center:
        xoffset -345 yoffset 75 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.6 xoffset -465
            easeout 1.0 xoffset -345
    $renpy.pause(delay=3.0, hard=True)
    scene cafeC with dissolve
    show yukino school near_center happy at center with dissolve:
        xoffset -200 yoffset 75
    play music "audio/bgm/BGM12.ogg"
    voice "audio/voice/E3/YUI/07/YI/YI004.ogg"
    yui "And like, once the teacher mentioned career paths, the air changed up and everyone got all riled up..."
    voice "audio/voice/E3/YUI/07/YK/YK002.ogg"
    yukino "I see... We're finally going to be taking exams this year. There'll be a subject divide in my class, so I'm guessing we'll be split into science and liberal arts sub-classes."
    voice "audio/voice/E3/YUI/07/YI/YI005.ogg"
    yui "Right! So everyone wants to like, know which one you're going with!"
    show yukino school near_center surprised with dissolve
    voice "audio/voice/E3/YUI/07/YK/YK003.ogg"
    yukino "Huh? Why would they?"
    voice "audio/voice/E3/YUI/07/YI/YI006.ogg"
    yui "Eh? You know like, being worried if you're gonna end up in the same class as someone else and stuff like that."
    voice "audio/voice/E3/YUI/07/YK/YK004.ogg"
    yukino "Huh? Why would you be?"
    voice "audio/voice/E3/YUI/07/YI/YI007.ogg"
    yui "Eh? You know like, you'll wonder if you'll get to be in the same class and stuff, right...?"
    show yukino school near_center pout with dissolve
    voice "audio/voice/E3/YUI/07/YK/YK005.ogg"
    yukino "Is that... how it works? I just faced it and choose what I wanted to do. If I started wavering now..."
    voice "audio/voice/E3/YUI/07/YI/YI008.ogg"
    yui "Ahahaha... It does actually go like that."
    voice "audio/voice/E3/YUI/07/YI/YI009.ogg"
    yui "You know, everyone wants at least a little to be together with people they get along with or people they like, right? So..."
    voice "audio/voice/E3/YUI/07/YI/YI010.ogg"
    yui "The whole thing around where Hayama-kun is going was pretty insane, you know? Everyone wanted to know."
    yui "(Crap, I accidentally brought up Hayato-kun...)"
    voice "audio/voice/E3/YUI/07/YI/YI011.ogg"
    yui "..."
    show yukino school near_center concerned with dissolve
    voice "audio/voice/E3/YUI/07/YK/YK006.ogg"
    yui "..."
    voice "audio/voice/E3/YUI/07/YI/YI012.ogg"
    yui "Say, about that rumour... Are you okay, Yukinon?"
    show yukino school near_center vhappy with dissolve
    voice "audio/voice/E3/YUI/07/YK/YK007.ogg"
    yukino "Yeah, I'm okay. Really. You don't have to worry about it. I'd say it's more troubling to Hayama-kun rather, don't you think?"
    voice "audio/voice/E3/YUI/07/YI/YI013.ogg"
    yui "Speaking of Hayama-kun, he's never really had a concrete rumour like this about him and it's because he doesn't really talk about himself. But then you get kind curious where his mind is really at, you know?"
    voice "audio/voice/E3/YUI/07/YI/YI014.ogg"
    yui "Say, Yukinon, do you have someone you like?"
    stop music fadeout 1.0
    show yukino school near_center surprised with dissolve
    voice "audio/voice/E3/YUI/07/YK/YK008.ogg"
    yukino "...!"
    yui "(She went quiet... I thought she'd say a clear \"no\" right away, but I never we'd sink in this silence...)"
    play music "audio/bgm/BGM11.ogg"
    show yukino school near_center pout with dissolve
    voice "audio/voice/E3/YUI/07/YK/YK009.ogg"
    yukino "Ahem... Please don't ask weird question out of the blue. I got something stuck in my throat."
    voice "audio/voice/E3/YUI/07/YI/YI015.ogg"
    yui "Sorry..."
    show yukino school near_center avoid with dissolve
    voice "audio/voice/E3/YUI/07/YK/YK010.ogg"
    yukino "I, um... I'm not very good at that sort of talk."
    voice "audio/voice/E3/YUI/07/YI/YI016.ogg"
    yui "I-I see. Say, Yukinon, I don't think we've ever had a girls' talk."
    voice "audio/voice/E3/YUI/07/YI/YI017.ogg"
    yui "Right, right, so then what's your type, Yukinon?"
    show yukino school near_center blush with dissolve
    voice "audio/voice/E3/YUI/07/YK/YK011.ogg"
    yukino "I don't... know even if you ask me."
    show yukino school near_center vhappy with dissolve
    voice "audio/voice/E3/YUI/07/YK/YK012.ogg"
    yukino "Let's see. If I were to go out with someone, I think I'd like someone like you."
    yui "(Is Yukinon just trolling!?)"
    voice "audio/voice/E3/YUI/07/YI/YI018.ogg"
    yui "Eh, so Yukinon, want to try going out!?"
    show yukino school near_center surprised with dissolve
    voice "audio/voice/E3/YUI/07/YK/YK013.ogg"
    yukino "Eh...?"
    voice "audio/voice/E3/YUI/07/YI/YI019.ogg"
    yui "See? If we do that, then the rumours would disappear, too!"
    yui "(What am I even saying?)"
    show yukino school near_center annoyed with dissolve
    voice "audio/voice/E3/YUI/07/YK/YK014.ogg"
    yukino "Another rumour would just take it's place, though."
    voice "audio/voice/E3/YUI/07/YI/YI020.ogg"
    yui "Ah, you're right..."
    show yukino school near_center vhappy with dissolve
    voice "audio/voice/E3/YUI/07/YK/YK015.ogg"
    yukino "...I'm kidding."
    voice "audio/voice/E3/YUI/07/YI/YI021.ogg"
    yui "Ahaha..."
    yui "(Thank goodness... The conversation's back on track.)"
    yui "(But... thinking about Yukinon's face earlier...)"
    yui "(When I asked her who she likes...)"
    voice "audio/voice/E3/YUI/07/YI/YI022.ogg"
    yui "I don't know how I feel about it..."
    voice "audio/voice/E3/YUI/07/YK/YK016.ogg"
    show yukino school near_center surprised with dissolve
    yukino "What's wrong?"
    voice "audio/voice/E3/YUI/07/YI/YI023.ogg"
    yui "A-Ah, no... It's nothing."

    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    $renpy.pause(delay=0.5, hard=True)
    scene loading_wlogo
    show yui school mid_center pout at center:
        xoffset -260 yoffset 75 alpha 1.0
        on hide:
            parallel:
                1.3
                linear 0.3 alpha 0
            parallel:
                easein 0.6 xoffset -200
                easeout 1.0 xoffset -380
    with Dissolve(1.0)
    $renpy.pause(delay=2.0, hard=True)
    hide yui
    $renpy.pause(delay=3.0, hard=True)
    jump E3_CMM_06

label E3_YUI_08:
    show yui school_sunset mid_left sad at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/08/YI/YI000.ogg"
    yui "W-Well then, we'll be going home..."
    show haruno sweater_sunset far_left vhappy at left with dissolve:
        xoffset 250 yoffset 75
    show yukino school_sunset far_center happy at left with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/08/YK/YK000.ogg"
    yukino "O-Okay."
    voice "audio/voice/E3/YUI/08/HR/HR000.ogg"
    haruno "See you guys~"
    stop music fadeout 0.5
    hide yukino
    hide haruno
    hide yui
    play sound "audio/sfx/SE04/SE04_01.ogg"
    play music "audio/bgm/BGM12.ogg"
    scene hallwayB with wipeleft
    show yui school_sunset mid_center sad at center with dissolve:
        xoffset -300 yoffset 75 alpha 0
        parallel:
            easein 0.5 xoffset 0
        parallel:
            linear 0.5 alpha 1.0
    $renpy.pause(delay=0.75,hard=True)
    hide yui
    show yui school_sunset mid_center sad at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/08/YI/YI001.ogg"
    yui "S-Should we leave her alone in there...?"
    voice "audio/voice/E3/YUI/08/HA/HA000.ogg"
    hachiman "I'm also not sure if I should've but in to that."
    voice "audio/voice/E3/YUI/08/YI/YI002.ogg"
    yui "It was hairy, but..."
    show yui school_sunset mid_center surprised at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/08/YI/YI003.ogg"
    yui "Ah! Crap!"
    voice "audio/voice/E3/YUI/08/HA/HA001.ogg"
    hachiman "What's wrong?"
    show yui school_sunset mid_left surprised at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/08/YI/YI004.ogg"
    yui "I forgot my stuff in the club room, not the classroom! Can you... wait for me at the gate?"
    voice "audio/voice/E3/YUI/08/HA/HA002.ogg"
    hachiman "If you forgot your stuff, we don't have to go home together..."
    show yui school_sunset mid_left angry at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/08/YI/YI005.ogg"
    yui "No, I'll be real quick, so wait for me!"
    hide yui with dissolve
    play sound "audio/sfx/SE00/SE00_00.ogg"
    $renpy.pause(delay=2, hard=True)
    voice "audio/voice/E3/YUI/08/YI/YI006.ogg"
    yui "You have to wait, okay~?"
    voice "audio/voice/E3/YUI/08/HA/HA003.ogg"
    hachiman "H-Hey, you don't have to rush like that."
    stop music fadeout 1.0
    $renpy.pause(delay=0.5, hard=True)
    $totsukaTalkFlag = "yui"
    jump E3_CMM_07

label E3_YUI_09:
    scene gatesB with dissolve
    play sound "audio/sfx/SE00/SE00_05.ogg"
    $renpy.pause(delay=2, hard=True)
    play music "audio/bgm/BGM12.ogg"
    show yui school_sunset mid_center vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI000.ogg"
    yui "I'm here!"
    voice "audio/voice/E3/YUI/09/HA/HA000.ogg"
    hachiman "Right."
    show yui school_sunset mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI001.ogg"
    yui "W-Wanna get going, then?"
    voice "audio/voice/E3/YUI/09/HA/HA001.ogg"
    hachiman "Sure."
    show yui school_sunset mid_center vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI002.ogg"
    yui "Answering me kind of obediently like that is a bit weird, haha..."
    voice "audio/voice/E3/YUI/09/HA/HA002.ogg"
    hachiman "Y-Yeah, you're right."
    show yui school_sunset mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI003.ogg"
    yui "Hikki... Want to walk ahead?"
    voice "audio/voice/E3/YUI/09/HA/HA003.ogg"
    hachiman "No, whatever works for me..."
    hide yui
    scene skyB with dissolve
    play ambient "audio/sfx/SE00/SE00_18L.ogg"
    $renpy.pause(delay=2.5, hard=True)
    voice "audio/voice/E3/YUI/09/YI/YI004.ogg"
    yui "I-It gets pretty cold when the sun goes down, huh?"
    voice "audio/voice/E3/YUI/09/HA/HA004.ogg"
    hachiman "...Yeah."
    hachiman "(W-What's with this bittersweet atmosphere...!?)"
    stop ambient fadeout 1
    scene sidewalkB with dissolve
    show yui school_sunset mid_center sad at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI005.ogg"
    yui "I wonder what Haruno-san's gonna do with Yukino when she caught her."
    "It's not that I don't understand her feelings, but this is Yukinoshita's problem to solve."
    "As I was lost on what to say, I just ended up being blunt."
    voice "audio/voice/E3/YUI/09/HA/HA005.ogg"
    hachiman "It's just sisters messing around, it's better to just leave it alone."
    voice "audio/voice/E3/YUI/09/YI/YI006.ogg"
    yui "It didn't seem that mild back there, though..."
    voice "audio/voice/E3/YUI/09/HA/HA006.ogg"
    hachiman "Well, it's not like she's being physically held down, so if disliked it that much, she could just leave."
    voice "audio/voice/E3/YUI/09/YI/YI007.ogg"
    yui "Right... I guess that's true. Those two seem like they have a pretty complicated relationship."
    hide yui with dissolve
    stop music fadeout 0.5
    call card_loading from _call_card_loading_3
    scene sidewalkB with dissolve
    show yui school_sunset mid_center pout at center with dissolve:
        xoffset 0 yoffset 75
    $card_queue = ["About\nfamily", "About\nYukino", "About\nsiblings", "About\nHaruno-san", "Sibling\nfights", "Cut the\nconversation\nshort"]
    play music "audio/bgm/BGM31.ogg"
    $E3_YUI_09_CARDS_COUNT = 0
    $E3_YUI_09_CARDS_ELLIPSES = 0
    jump E3_YUI_09_CARDS

label E3_YUI_09_CARDS:
    if E3_YUI_09_CARDS_COUNT < 5:
        $E3_YUI_09_CARDS_COUNT += 1
        $renpy.pause(delay=0.5, hard=True)
        $ch2 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch2)
        $ch3 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch3)
        window auto hide dissolve
        call screen three_minigame("...", ch2, ch3) with dissolve
        if _return == 1:
            "not done"
            $card_queue.append(ch2)
            $card_queue.append(ch3)
            $E3_YUI_09_CARDS_COUNT -= 1
            jump E3_YUI_09_CARDS
        elif _return == 2:
            $card_queue.append(ch3)
            if ch2 == "About\nfamily":
                jump family_card
            elif ch2 == "About\nYukino":
                jump yukino_card
            elif ch2 == "About\nsiblings":
                jump siblings_card
            elif ch2 == "About\nHaruno-san":
                jump haruno_card
            elif ch2 == "Sibling\nfights":
                jump fight_card
            else:
                jump E3_YUI_09_CONT
                $card_queue.append(ch2)
                $E3_YUI_09_CARDS_COUNT -= 1
                jump E3_YUI_09_CARDS
        elif _return == 3:
            $card_queue.append(ch2)
            if ch3 == "About\nfamily":
                jump family_card
            elif ch3 == "About\nYukino":
                jump yukino_card
            elif ch3 == "About\nsiblings":
                jump siblings_card
            elif ch3 == "About\nHaruno-san":
                jump haruno_card
            elif ch3 == "Sibling\nfights":
                jump fight_card
            else:
                jump E3_YUI_09_CONT
                $card_queue.append(ch3)
                $E3_YUI_09_CARDS_COUNT -= 1
                jump E3_YUI_09_CARDS
    else:
        jump E3_YUI_09_CONT


label siblings_card:
    voice "audio/voice/E3/YUI/09/HA/HA021.ogg"
    hachiman "There's quite a bit to relationships between siblins, huh?"
    show yui school_sunset mid_right happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI025.ogg"
    yui "You and Komachi-chan get along really well."
    voice "audio/voice/E3/YUI/09/HA/HA022.ogg"
    hachiman "Well that's cause I'm a good brother..."
    show yui school_sunset mid_right sad at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI026.ogg"
    yui "Ahaha..."
    hachiman "(What's with the dry laugh?)"
    show yui school_sunset mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI027.ogg"
    yui "I wonder how it feels like to have Hikki as an older brother."
    voice "audio/voice/E3/YUI/09/HA/HA023.ogg"
    hachiman "Well... it's the best. I'll basically listen to everything you say."
    show yui school_sunset mid_center surprised at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI028.ogg"
    yui "That sounds more like a slave! But... anything, huh? Hmm..."
    show yui school_sunset mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    hachiman "(Huh? Why's she so weirdly happy with that answer? Does she want to do something to me!?)"
    jump E3_YUI_09_CARDS

label haruno_card:
    voice "audio/voice/E3/YUI/09/HA/HA024.ogg"
    hachiman "It's really hard to understand what that person's thinking..."
    show yui school_sunset mid_left sad at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI029.ogg"
    yui "Yeah... Doesn't she kind of seem to like you though, Hikki?"
    voice "audio/voice/E3/YUI/09/HA/HA025.ogg"
    hachiman "She's just making fun of me."
    show yui school_sunset mid_left happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI030.ogg"
    yui "Hikki, do you like that kind of nee-san type?"
    voice "audio/voice/E3/YUI/09/HA/HA026.ogg"
    hachiman "What's this, suddenly?"
    show yui school_sunset mid_left blush at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI031.ogg"
    yui "N-Nothing, I just... thought I'd ask."
    voice "audio/voice/E3/YUI/09/HA/HA027.ogg"
    hachiman "If there's one thing that type of girl did for me, it'd be fear. I'm an onii-chan character after all."
    show yui school_sunset mid_center vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI032.ogg"
    yui "I-I see! That's true! Hehe..."
    jump E3_YUI_09_CARDS

label yukino_card:
    voice "audio/voice/E3/YUI/09/HA/HA028.ogg"
    hachiman "Are you worried about Yukinoshita?"
    show yui school_sunset mid_center pout at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI033.ogg"
    yui "Mhm... A little bit."
    voice "audio/voice/E3/YUI/09/HA/HA029.ogg"
    hachiman "Maybe you should try shooting her a lighthearted text later."
    voice "audio/voice/E3/YUI/09/YI/YI034.ogg"
    yui "Y-Yeah. You're right."
    voice "audio/voice/E3/YUI/09/HA/HA030.ogg"
    hachiman "She's probably not much of a texter, though, right?"
    show yui school_sunset mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI035.ogg"
    yui "She does reply when I text her, you know? Though it's super short replies."
    hachiman "(I knew she'd be the same type of texter as me.)"
    jump E3_YUI_09_CARDS

label family_card:
    voice "audio/voice/E3/YUI/09/HA/HA031.ogg"
    hachiman "When it comes to family, how does your house look like?"
    show yui school_sunset mid_left surprised at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI036.ogg"
    yui "Eh? My house? I don't have any siblings, but... it's normal, I guess?"
    "I'd venture to guess she was raised in a rather warm household as opposed to just a regular one."
    voice "audio/voice/E3/YUI/09/HA/HA032.ogg"
    hachiman "Aren't normal households the best?"
    show yui school_sunset mid_left sad at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI037.ogg"
    yui "Are they really?"
    voice "audio/voice/E3/YUI/09/HA/HA033.ogg"
    hachiman "I mean, aren't they? When you hear about what goes down with Yukinoshita and Hayama, I don't think I'd be able to stand it myself."
    show yui school_sunset mid_left vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI038.ogg"
    yui "Ahaha... It's rare for you to ask about things like that."
    voice "audio/voice/E3/YUI/09/HA/HA034.ogg"
    hachiman "...Well, don't know why I did."
    show yui school_sunset mid_right happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI039.ogg"
    yui "I know! Want to come over to my house next time?"
    voice "audio/voice/E3/YUI/09/HA/HA035.ogg"
    hachiman "Huh!?"
    show yui school_sunset mid_center blush at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI040.ogg"
    yui "Ah... I don't mean that in a weird way! Since I'd never invited you over before and stuff. So that's why I wanted to do it, with Yukino there, too."
    voice "audio/voice/E3/YUI/09/HA/HA036.ogg"
    hachiman "I-I see... We could do it."
    show yui school_sunset mid_center vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI041.ogg"
    yui "yeah!"
    hachiman "(That really surprised me...)"
    jump E3_YUI_09_CARDS

label fight_card:
    voice "audio/voice/E3/YUI/09/HA/HA037.ogg"
    hachiman "No matter the siblings, I suppose you'd have fought at least once."
    "Well, I guess for Yukinoshita sisters it's not exactly fights."
    show yui school_sunset mid_right surprised at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI042.ogg"
    yui "Do you fight with Komachi, too, Hikki?"
    voice "audio/voice/E3/YUI/09/HA/HA038.ogg"
    hachiman "Yeah, sometimes."
    voice "audio/voice/E3/YUI/09/YI/YI043.ogg"
    yui "When that happens, how do you make up?"
    voice "audio/voice/E3/YUI/09/HA/HA039.ogg"
    hachiman "It ends with me apologizing 90 \%\ of the time."
    show yui school_sunset mid_right sad at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI044.ogg"
    yui "I-I see..."
    voice "audio/voice/E3/YUI/09/HA/HA040.ogg"
    hachiman "I don't really get why, but it always seems to be my fault."
    show yui school_sunset mid_center unimpressed at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI045.ogg"
    yui "You say that, but you're actually smiling, Hikki."
    show yui school_sunset mid_left pout at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI060.ogg"
    yui "I wonder what Yukinon'll do about her career course in the end."
    voice "audio/voice/E3/YUI/09/HA/HA052.ogg"
    hachiman "Who knows?"
    show yui school_sunset mid_left surprised at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI061.ogg"
    yui "Eh? Is that a little cold?"
    voice "audio/voice/E3/YUI/09/HA/HA053.ogg"
    hachiman "I mean... She can do anything and she has good grades, so I don't really think she's a good reference for us."
    show yui school_sunset mid_left unimpressed at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI062.ogg"
    yui "That's now what I was getting at..."
    "I mostly understood what Yuigahama wanted to say. She wanted to know exactly what Yukino wanted, just like Miura wanted to know about Hayama."
    "Even though I understand the sentiment, I can neither give her words of consolation nor a definite answer."
    voice "audio/voice/E3/YUI/09/HA/HA054.ogg"
    hachiman "Well, you and Yukinoshita don't exactly have a relationship that would break down just from a course difference, right?"
    "That was as much as I was able to say."
    show yui school_sunset mid_left angry at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI063.ogg"
    yui "You think?"
    voice "audio/voice/E3/YUI/09/HA/HA055.ogg"
    hachiman "Whatever course she might go with, I don't feel like she'd lose contact with you."
    show yui school_sunset mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI064.ogg"
    yui "Yeah... I guess so."
    show yui school_sunset mid_center sad at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI065.ogg"
    yui "You won't either, right, Hikki?"
    voice "audio/voice/E3/YUI/09/HA/HA056.ogg"
    hachiman "..."
    "I'd never had someone ask me something like that before, so the words got stuck in my throat."
    hachiman "(If you look at me with those imploring-like, puppy eyes, I won't be able to say no...)"
    voice "audio/voice/E3/YUI/09/YI/YI066.ogg"
    yui "..."
    voice "audio/voice/E3/YUI/09/HA/HA057.ogg"
    hachiman "I, uh... I wouldn't either."
    show yui school_sunset mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI067.ogg"
    yui "...I see."
    hide yui with dissolve
    jump E3_YUI_09_CONT


label E3_YUI_09_CONT:
    stop music fadeout 1.0
    scene sidewalkB with fade
    play music "audio/bgm/BGM32.ogg"
    show yui school_sunset mid_center pout at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI068.ogg"
    yui "..."
    voice "audio/voice/E3/YUI/09/HA/HA058.ogg"
    hachiman "..."
    show yui school_sunset mid_center happy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI069.ogg"
    yui "S-Say, Hikki..."
    voice "audio/voice/E3/YUI/09/HA/HA059.ogg"
    hachiman "...What?"
    show yui school_sunset mid_center blush at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI070.ogg"
    yui "N-Nothing!"
    voice "audio/voice/E3/YUI/09/HA/HA060.ogg"
    hachiman "Eh?"
    voice "audio/voice/E3/YUI/09/YI/YI071.ogg"
    yui "I said it's nothing! Ah, right! I have to go this way to go home!"
    voice "audio/voice/E3/YUI/09/HA/HA061.ogg"
    hachiman "Wait, didn't you..."
    show yui school_sunset mid_left blush at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E3/YUI/09/YI/YI072.ogg"
    yui "S-S-See ya!!"
    hide yui with dissolve
    play sound "audio/sfx/SE00/SE00_00.ogg"
    $renpy.pause(delay=1, hard=True)
    hachiman "(D-Did I do something?)"
    stop music fadeout 1.0
    window auto hide dissolve
    $renpy.pause(delay=1, hard=True)
    play music "audio/bgm/BGM33.ogg"
    call loading_screen(_image = 29, duration = "short") from _call_loading_screen_37
    stop music fadeout 1.0
    jump E3_CMM_08
