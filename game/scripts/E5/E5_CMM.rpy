label E5_CMM_01:
    scene houseCB with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/BGM20.ogg"
    window auto show dissolve
    hachiman "(A ski trip... Things sure took a strange turn...)"
    show komachi athletic mid_center vhappy at center with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E5/CMM/01/KO/KO000.ogg"
    komachi "Ahhhh. I'm so tired..."
    show komachi pout with dissolve
    voice "audio/voice/E5/CMM/01/KO/KO001.ogg"
    komachi "Huh? What are you doing, onii-chan?"
    voice "audio/voice/E5/CMM/01/HA/HA000.ogg"
    hachiman "I'm dying..."
    show komachi happy with dissolve
    voice "audio/voice/E5/CMM/01/KO/KO002.ogg"
    komachi "Didn't you say you had a Student Council event today? Something to do with Valentines? Onii-chan, did you get any chocolate?"
    voice "audio/voice/E5/CMM/01/HA/HA001.ogg"
    hachiman "I was just a miscellaneous taster, and I didn't get any. And wait, that event wasn't even like that..."
    show komachi angry with dissolve
    voice "audio/voice/E5/CMM/01/KO/KO003.ogg"
    komachi "Huh? Is there something that tiring about that?"
    voice "audio/voice/E5/CMM/01/HA/HA002.ogg"
    hachiman "There is, there definitely is. While everyone got excited for whatever reason, the conversation became about going on a ski trip. And it feels like the Service Club is being forced to participate..."
    hide komachi
    $url = ["komachi athletic mid_center surprised", "komachi athletic mid_center vhappy"]
    $multiImagePara = [-75, 75, 0, 0, 0.6]
    call multiImage() from _call_multiImage_18
    voice "audio/voice/E5/CMM/01/KO/KO004.ogg"
    komachi "Eh?! A ski trip sounds great! I want to go on any trip right about now!"
    call finishmultiImage from _call_finishmultiImage_19
    show komachi athletic mid_center vhappy at center:
        xoffset -75 yoffset 75
    voice "audio/voice/E5/CMM/01/HA/HA003.ogg"
    hachiman "Of course you would. It's right before your entrance exams after all."
    show komachi frown with dissolve
    voice "audio/voice/E5/CMM/01/KO/KO005.ogg"
    komachi "Stop with the reality checks. Nobody asked for them so please shut up."
    voice "audio/voice/E5/CMM/01/HA/HA004.ogg"
    hachiman "This isn't the time you can afford to look away anymore."
    show komachi athletic mid_left happy with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E5/CMM/01/KO/KO006.ogg"
    komachi "Perish the thought. I'm not looking away from reality, I'm just facing my true feelings head on."
    voice "audio/voice/E5/CMM/01/HA/HA005.ogg"
    hachiman "I don't like this girl. She's looks like her brother right now..."
    show komachi vhappy with dissolve
    voice "audio/voice/E5/CMM/01/KO/KO007.ogg"
    komachi "If she was like her brother, that's high in Komachi points, right?"
    voice "audio/voice/E5/CMM/01/HA/HA006.ogg"
    hachiman "Your human points will drop though."
    show komachi sad with dissolve
    voice "audio/voice/E5/CMM/01/KO/KO008.ogg"
    komachi "You even said it yourself."
    hide komachi
    $url = ["komachi athletic mid_center happy", "komachi athletic mid_center angry"]
    $multiImagePara = [-75, 75, 0, 0, 9.0]
    call multiImage() from _call_multiImage_19
    voice "audio/voice/E5/CMM/01/KO/KO009.ogg"
    komachi "But, come on. The Service Club participating means Yukino-san and Yui-san will be as well, right? How nice, being able to to ski with both Yukino-san and Yui-san. Onii-chan, you're going to regret it for the "
    voice sustain
    komachi "rest of your life if you don't go!"
    call finishmultiImage from _call_finishmultiImage_20
    show komachi athletic mid_center angry at center:
        xoffset -75 yoffset 75
    voice "audio/voice/E5/CMM/01/HA/HA007.ogg"
    hachiman "Ah, that's right. You were invited as well. I don't know if I'll go or not, but I've at least delivered the message..."
    show komachi surprised with dissolve
    voice "audio/voice/E5/CMM/01/KO/KO010.ogg"
    komachi "Eh? Komachi too?!"
    hide komachi with dissolve
    play sound "audio/sfx/SE01/SE01_12.ogg"
    #sound effect possibly SE01_12
    show komachi athletic near_center vhappy at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E5/CMM/01/KO/KO011.ogg"
    komachi "Onii-chan! Let's go, let's go, let's definitely go!"
    voice "audio/voice/E5/CMM/01/HA/HA008.ogg"
    hachiman "Eh? You want to go? Seriously?"
    hide komachi with dissolve
    show komachi athletic mid_center sad at center with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E5/CMM/01/KO/KO012.ogg"
    komachi "...Yeah. I want to ski together with Yukino-san, Yui-san, and onii-chan. And we don't know if there'll be another chance like this, either..."
    voice "audio/voice/E5/CMM/01/HA/HA009.ogg"
    hachiman "I see..."
    voice "audio/voice/E5/CMM/01/HA/HA010.ogg"
    hachiman "Well, for now, just try your best on your exams."
    show komachi surprised with dissolve
    voice "audio/voice/E5/CMM/01/KO/KO013.ogg"
    komachi "The-Then...!"
    voice "audio/voice/E5/CMM/01/HA/HA011.ogg"
    hachiman "But, I promise I'll give the ski trip a little more thought."
    show komachi annoyed with dissolve
    voice "audio/voice/E5/CMM/01/KO/KO014.ogg"
    komachi "EH?!"
    voice "audio/voice/E5/CMM/01/HA/HA012.ogg"
    hachiman "No wait, you've got the wrong idea. My human relationships have been in serious chaos recently..."
    show komachi pout with dissolve
    voice "audio/voice/E5/CMM/01/KO/KO015.ogg"
    komachi "Ah, you did say they were complicated."
    show komachi happy with dissolve
    voice "audio/voice/E5/CMM/01/KO/KO016.ogg"
    komachi "But even so, onii-chan. This may just be a possibility, but this is when you need to try your best! And good things are sure to happen! Hardship when you're young is prior investment! It's a forward rate!"
    voice "audio/voice/E5/CMM/01/HA/HA013.ogg"
    hachiman "That sounds like a market about to instantly collapse... Well, you are putting in a lot of effort. I'll try somewhat considering it for now."
    show komachi vhappy with dissolve
    voice "audio/voice/E5/CMM/01/KO/KO017.ogg"
    komachi "Ehehe. Then Komachi will keep doing her best!"
    voice "audio/voice/E5/CMM/01/HA/HA014.ogg"
    hachiman "Yeah. Well, just don't go overboard."
    voice "audio/voice/E5/CMM/01/KO/KO018.ogg"
    komachi "Sure!"
    window auto hide dissolve
    hide komachi with dissolve
    play footsteps "audio/sfx/SE00/SE00_31.ogg"
    $renpy.pause(delay=1.5,hard=True)
    stop footsteps
    window auto show dissolve
    if chocoEventHelp == "saki" or chocoEventHelp == "iroha":
        menu E5_CMM_01_menu:
            hachiman "(I'll do my best here)"
            with dissolve
            "Maybe I should join...":
                pass
            "I shouldn't join":
                #saki route
                hachiman "(Thanks to Komachi's vigorous feeling on the matter... I was seriously tired.)"
                # google translated ^
                hachiman "(I want to give myself a little more time... I'm sorry, Komachi-chan. Please forgive my unfriendly brotherness.)"
                # google translated ^
                window auto hide dissolve
                stop music fadeout 1.0
                jump E5_SAK_01

    #All routes except saki
    hachiman "(Well, if Komachi says that, as a brother, I need to consider going. For Komachi's sake as well.)"
    window auto hide dissolve
    stop music fadeout 1.0
    jump E5_CMM_02

label E5_CMM_02:
    scene skyA with Fade(1.0, 0.5, 1.0)
    play sound "audio/sfx/SE00/SE00_25.ogg"
    $renpy.pause(delay=0.5,hard=True)
    play music "audio/bgm/BGM07.ogg"
    $renpy.pause(delay=0.5,hard=True)
    voice "audio/voice/E5/CMM/02/YI/YI000.ogg"
    yui "We're here!"
    voice "audio/voice/E5/CMM/02/TB/TB000.ogg"
    tobe "That was a good nap!"
    voice "audio/voice/E5/CMM/02/YI/YI001.ogg"
    yui "Tobecchi, you were sleeping?!"
    voice "audio/voice/E5/CMM/02/TB/TB001.ogg"
    tobe "Cause I've been seriously so excited since yesterday I couldn't sleep at all! I only got two hours of sleep! After that I just made paper dolls for good weather!"
    hachiman "(Tobe is noisy as usual... But he's a good guy...)"
    "While I pondered over it, in the end I'm participating in the ski trip with Komachi who'd just finished her entrance exams."
    window auto hide dissolve
    play sound "audio/sfx/SE00/SE00_22L.ogg"
    scene lodgeoutA with Fade(1.0, 2.0, 1.0)
    stop sound
    $renpy.pause(delay=1.0, hard=True)
    show hiratsuka coat mid_center happy at left:
        xoffset 110 yoffset 75
    show iroha coat mid_left happy at right:
        xoffset -255 yoffset 65
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/CMM/02/IR/IR000.ogg"
    iroha "Oh what, this is quite a nice lodge!"
    voice "audio/voice/E5/CMM/02/SZ/SZ000.ogg"
    hiratsuka "Well, the school is letting us use it. It's normally a plain lodge though.
        Let's go inside for now."
    hide hiratsuka with dissolve
    play sound "<from 0 to 3.5>audio/sfx/SE00/SE00_24.ogg"
    $renpy.pause(delay=1.0, hard=True)
    show iroha vhappy with dissolve
    $renpy.pause(delay=0.5, hard=True)
    voice "audio/voice/E5/CMM/02/IR/IR001.ogg"
    iroha "Sure."
    show iroha mid_center happy with dissolve:
        yoffset 75
    stop sound
    voice "audio/voice/E5/CMM/02/IR/IR002.ogg"
    iroha "Everyone, we're going into the lodge first!"
    hide iroha with dissolve
    show komachi coat mid_center vhappy at center with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E5/CMM/02/KO/KO000.ogg"
    komachi "Onii-chan, it was good to come after all, right?"
    voice "audio/voice/E5/CMM/02/HA/HA000.ogg"
    hachiman "... Yeah."
    hachiman "(I knew it, it's tiring when there's lots of people... But well, if Komachi is having fun then whatever.)"
    window auto hide dissolve
    scene black with Fade(0.5, 0.5, 0.5)
    play sound "audio/sfx/SE04/SE04_05.ogg"
    scene lodgeA with Fade(1.0, 0.5, 1.0)
    play sound "audio/sfx/SE04/SE04_06.ogg"
    $renpy.pause(delay=1.0, hard=True)
    stop sound
    image yui surprised flat = Flatten("yui coat mid_center surprised")
    show yukino coat mid_center happy at left:
        xoffset -105 yoffset 75
    show yui coat mid_center pout at center:
        xoffset 35 yoffset 75
    show iroha coat mid_left pout at right:
        xoffset -130 yoffset 65
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/CMM/02/YI/YI002.ogg"
    yui "It's pretty neat, but... It's quite dusty."
    voice "audio/voice/E5/CMM/02/YK/YK000.ogg"
    yukino "It can't be helped since the place hasn't been used in such a while. Cleaning should come first."
    show iroha mid_center happy with dissolve:
        yoffset 75
    voice "audio/voice/E5/CMM/02/IR/IR003.ogg"
    iroha "That's true. Then we need to decide on how to divide the work."
    show yui surprised flat:
        parallel:
            0.4
            linear 0.25 xoffset -150
        parallel:
            0.4
            linear 0.25 alpha 0
    show iroha:
        parallel:
            0.4
            easein 0.5 xoffset -665
    show haruno coat mid_left vhappy at right:
        xoffset -50 yoffset 75 alpha 0
        parallel:
            0.4
            linear 0.1 alpha 1.0
        parallel:
            0.4
            easein 0.15 xoffset -110
    voice "audio/voice/E5/CMM/02/HR/HR000.ogg"
    haruno "Ah, then let's do this! Let's draw straws! It sounds like fun too."
    hide yuiFlatLeft
    hide iroha
    hide haruno
    show iroha coat mid_center happy at right:
        xoffset -665 yoffset 75
    show haruno coat mid_left vhappy at right:
        xoffset -110 yoffset 75
    voice "audio/voice/E5/CMM/02/YI/YI003.ogg"
    yui "A draw!?"
    show yukino unimpressed with dissolve
    voice "audio/voice/E5/CMM/02/YK/YK001.ogg"
    yukino "Nee-san, you're doing whatever you want again..."
    show iroha vhappy with dissolve
    voice "audio/voice/E5/CMM/02/IR/IR004.ogg"
    iroha "Isn't it a good idea? It sounds easy too. Right, Senpai?"
    voice "audio/voice/E5/CMM/02/HA/HA001.ogg"
    hachiman "... Is it easy?"
    show iroha happy with dissolve
    voice "audio/voice/E5/CMM/02/IR/IR005.ogg"
    iroha "It is! No one will have disputes if it's by a draw."
    voice "audio/voice/E5/CMM/02/HA/HA002.ogg"
    hachiman "I see. If that's the case, I'm totally fine with it."
    show haruno happy with dissolve
    voice "audio/voice/E5/CMM/02/HR/HR001.ogg"
    haruno "Then it's decided! Just wait a moment."
    hide yukino
    hide iroha
    hide haruno
    with dissolve
    "As she spoke, Haruno-san quickly made a draw by hand and handed it to us."
    "What could it be... Maybe she's used to this as a university student. They do stuff like the
        King's Game, right? Who's the tyrant!? It's this person! Like that anyway."
    show haruno coat near_center happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E5/CMM/02/HR/HR002.ogg"
    haruno "Here, Hikigaya-kun."
    voice "audio/voice/E5/CMM/02/HA/HA003.ogg"
    hachiman "Ah, right."
    hide haruno with dissolve
    "As the tyrant told me to, I pulled one out."
    menu lodge_straws: #I think different options appear depending on possible routes clearage. No script available so not sure how many options, but voice files seem to indicate at least 3
        #Guessing from the voice files:
        #HA_010.ogg says something I don't know
        #HA_012.ogg says Open Air Bath Cleaning
        hachiman "(Let's see, it says...)"
        with dissolve
        "Snow-shoveling": #Yukino
            voice "audio/voice/E5/CMM/02/HA/HA004.ogg"
            hachiman "Snow-shoveling outside the lodge...?"
            "Hey, hey, is this for real? That's way too much labour for this depopulated area... My luck at picking straws must be bad..."
            show yukino coat mid_center stare at center with dissolve:
                xoffset -105 yoffset 75
            voice "audio/voice/E5/CMM/02/YK/YK002.ogg"
            yukino "Snow-shoveling..."
            voice "audio/voice/E5/CMM/02/HA/HA005.ogg"
            hachiman "... Eh?"
            show yukino surprised with dissolve
            voice "audio/voice/E5/CMM/02/YK/YK003.ogg"
            yukino "... Eh?"
            window auto hide dissolve
            stop music fadeout 1
            jump E5_YUK_01
        "Cleaning floors": #Yui
            voice "audio/voice/E5/CMM/02/HA/HA006.ogg"
            hachiman "Floor clean-up? Sounds plain, but it suits me perfect."
            show yui coat mid_center vhappy at center with dissolve:
                xoffset 0 yoffset 75 alpha 1
            voice "audio/voice/E5/CMM/02/YI/YI004.ogg"
            yui "Ah! I also have floor clean-up! Let's do it, Hikki."
            voice "audio/voice/E5/CMM/02/HA/HA007.ogg"
            hachiman "...R-Right."
            show hayama coat mid_right happy at left behind yui:
                xoffset -15 xalign -0.1 yoffset 75 alpha 0
                on show:
                    easein 0.35 xalign 0.0000001 alpha 1
            $renpy.pause(delay=0.5, hard=True)
            voice "audio/voice/E5/CMM/02/HY/HY000.ogg"
            hayama "I also got floor clean-up..."
            show yui coat mid_left surprised zorder 1 at center with dissolve:
                xoffset 0 yoffset 75
            voice "audio/voice/E5/CMM/02/YI/YI005.ogg"
            yui "Eh? You too, Hayato-kun?"
            show tobe coat mid surprised at right behind yui:
                xalign 1.1 yoffset 75 alpha 0
                on show:
                    easein 0.35 xalign 1.0 alpha 1
            $renpy.pause(delay=0.5, hard=True)
            voice "audio/voice/E5/CMM/02/TB/TB002.ogg"
            tobe "Man, I'm floor clean-up, too!"
            show yui coat mid_right surprised zorder 1 at center with dissolve:
                xoffset 0 yoffset 75
            voice "audio/voice/E5/CMM/02/YI/YI006.ogg"
            yui "Eh!? Tobecchi, you too!?"
            voice "audio/voice/E5/CMM/02/HA/HA008.ogg"
            hachiman "Doesn't this seem a bit rigged? Isn't there a tad too many people for this?"
            show hayama coat mid_right vhappy at left with dissolve:
                yoffset 75
            voice "audio/voice/E5/CMM/02/HY/HY001.ogg"
            hayama "Since the place is quite big, if we have more people we'll be able to finish faster."
            show tobe coat mid vhappy at right with dissolve:
                yoffset 75
            voice "audio/voice/E5/CMM/02/TB/TB003.ogg"
            tobe "True!"
            show yui coat mid_right pout zorder 1 at center with dissolve:
                xoffset 0 yoffset 75
            voice "audio/voice/E5/CMM/02/YI/YI007.ogg"
            yui "Y-Yeah, ahaha..."
            stop music fadeout 1.5
            scene black with dissolve
            $renpy.pause(delay=1.5, hard=True)
            jump E5_YUI_01
        "Making the bed" if chocoEventHelp == "iroha":
            hachiman "Making the guest room beds? I'm not that great at this sort of thing...I wonder if I can manage."
            show kaori coat mid vhappy at center with dissolve:
                xoffset 5 yoffset 75
            voice "audio/voice/E5/CMM/02/OR/OR000.ogg"
            kaori "I got the guest room--"
            voice "audio/voice/E5/CMM/02/HA/HA009.ogg"
            hachiman "...!"
            show kaori annoyed with dissolve
            voice "audio/voice/E5/CMM/02/OR/OR001.ogg"
            kaori "Hmm?"
            window auto hide dissolve
            stop voice fadeout 0.5
            stop music fadeout 0.5
            jump E5_IRO_01
        "Everyone will clean simultaneously" if chocoEventHelp == "haruno" or chocoEventHelp == "meguri": #haruno
            show haruno coat mid_center happy at center with dissolve:
                xoffset -20 yoffset 75
            voice "audio/voice/E5/CMM/02/HA/HA010.ogg"
            hachiman "\"Everybody will clean simultaneously\". What does that even mean?"
            show haruno vhappy with dissolve
            voice "audio/voice/E5/CMM/02/HR/HR003.ogg"
            haruno "Ahaha. This is pretty fun, isn't it~?"
            voice "audio/voice/E5/CMM/02/HA/HA011.ogg"
            hachiman "No, there wasn't any point in drawing."
            show haruno mid_left happy with dissolve
            voice "audio/voice/E5/CMM/02/HR/HR004.ogg"
            haruno "Instead of thinking long and hard about it, everyone can just clean together and we'll finish a lot quicker."
            hachiman "(Well, I guess there's some truth to that..., I somehow feel like I've been deceived though...)"
            show haruno vhappy with dissolve
            voice "audio/voice/E5/CMM/02/HR/HR005.ogg"
            haruno "Now then, Meguri, Shizuka and me are going on a supply run. We'll leave the rest to you~!"
            window auto hide dissolve
            stop voice
            hide haruno with dissolve
            stop music fadeout 0.5
            play sound "audio/sfx/SE00/SE00_31.ogg"
            $renpy.pause(delay=2.0, hard=True)
            play sound "audio/sfx/SE04/SE04_06.ogg"
            $renpy.pause(delay=0.5, hard=True)
            show hayama coat mid_right worried at left:
                xoffset 135 yoffset 65
            show yukino coat mid_left unimpressed at right:
                xoffset -170 yoffset 80
            with dissolve
            window auto show dissolve
            voice "audio/voice/E5/CMM/02/YK/YK004.ogg"
            yukino "Nee-san really just ran away..."
            voice "audio/voice/E5/CMM/02/HY/HY002.ogg"
            hayama "Well, it is Haruno-san, after all..."
            hachiman "(These guys sound like a Victim Alliance...)"
            $partner = _calculate_points()
            if partner['haruno'] > partner['meguri']:
                $ski_flag = "haruno"
                jump E5_HAR_01
            elif partner['meguri'] > partner['haruno']:
                $ski_flag = "meguri"
                window auto hide dissolve
                stop music fadeout 0.5
                jump E5_HAR_02
        "Taking care of the open air bath" if chocoEventHelp == "hiratsuka":
            voice "audio/voice/E5/CMM/02/HA/HA012.ogg"
            hachiman "Taking care of the open air bath... that sounds pretty hard..."
            show totsuka coat mid_center happy at center with dissolve:
                xoffset 40 yoffset 75
            voice "audio/voice/E5/CMM/02/SI/SI000.ogg"
            totsuka "Ah, cleaning the open air bath. I'm with you, Hachiman!"
            voice "audio/voice/E5/CMM/02/HA/HA013.ogg"
            hachiman "Oh, you're right!"
            hachiman "(Thank you, God!)"
            window auto hide dissolve
            stop music fadeout 0.5
            jump E5_SHI_01

    #Not complete.
    voice "audio/voice/E5/CMM/02/YK/YK004.ogg"
    yukino "."
    voice "audio/voice/E5/CMM/02/TB/TB002.ogg"
    tobe ""
    voice "audio/voice/E5/CMM/02/HR/HR002.ogg"
    haruno ""
    voice "audio/voice/E5/CMM/02/TB/TB003.ogg"
    tobe ""
    voice "audio/voice/E5/CMM/02/YI/YI005.ogg"
    yui ""
    voice "audio/voice/E5/CMM/02/HA/HA008.ogg"
    hachiman ""
    voice "audio/voice/E5/CMM/02/HA/HA009.ogg"
    hachiman ""
    voice "audio/voice/E5/CMM/02/HR/HR005.ogg"
    haruno ""
    voice "audio/voice/E5/CMM/02/YI/YI006.ogg"
    yui ""
    voice "audio/voice/E5/CMM/02/HA/HA011.ogg"
    hachiman ""
    voice "audio/voice/E5/CMM/02/YI/YI007.ogg"
    yui ""
    voice "audio/voice/E5/CMM/02/HA/HA013.ogg"
    hachiman ""

label E5_CMM_03:
    scene lodgeC with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM17.ogg"
    window auto show dissolve
    "As we sluggishly returned from the ski resort, what welcomed us was the girls' cooking."
    "Dishes pleasing to the eye were lined up and everyone was making a fuss... especially Tobe."
    window auto hide dissolve
    scene lodgeC:
        zoom 2.0 yoffset -350
    show haruno sweater mid_center vhappy at center:
        xoffset 10 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/CMM/03/HR/HR000.ogg"
    haruno "............"
    "In any case, Haruno-san, who could accomplish skiing and cooking with a calm face, was really fitting the idea of a perfect superhuman."
    window auto hide dissolve
    scene lodgeC:
        zoom 1.9 xoffset -1680 yoffset -450
    show yukino home mid_center sad at center:
        xoffset -105 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/CMM/03/YK/YK000.ogg"
    yukino "............"
    "Yukinoshita on the other hand appeared quite tired. She doesn't have much stamina after all."
    window auto hide dissolve
    scene lodgeC with dissolve
    show totsuka home mid_center vhappy at left:
        xoffset 260 yoffset 75
    show komachi home mid_center happy at right:
        xoffset -200 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/CMM/03/SI/SI000.ogg"
    totsuka "Dinner tasted really good, right Hachiman?"
    hachiman "(Totsuka's smile is so calming...)"
    voice "audio/voice/E5/CMM/03/HA/HA000.ogg"
    hachiman "I didn't think we'd eat something so good on this trip."
    show komachi vhappy with dissolve
    voice "audio/voice/E5/CMM/03/KO/KO000.ogg"
    komachi "Yukino-san is a given, but the other seniors around you are amazing."
    voice "audio/voice/E5/CMM/03/HA/HA001.ogg"
    hachiman "Well, sure in various meanings..."
    hachiman "(Alright, now that dinner's over, after this is...)"
    voice "audio/voice/E5/CMM/03/HA/HA002.ogg"
    hachiman "H-hey Totsuka... Do you want to go to the baths after this..."
    voice "audio/voice/E5/CMM/03/TB/TB000.ogg"
    tobe "Beh! Now that we've eaten we've gotta play night games!"
    hachiman "(Shut up, Tobe, shut up...)"
    window auto hide dissolve
    scene lodgeC:
        zoom 1.5 yoffset -200
    show tobe coat mid at left:
        xoffset 10 yoffset 75
    show hayama coat mid_center vhappy at center:
        xoffset 245 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/CMM/03/HY/HY000.ogg"
    hayama "We've got tomorrow as well. Can your stamina last?"
    show tobe vhappy with dissolve
    hide hayama with dissolve
    image yumikoFlat = Flatten("yumiko home mid_center happy")
    image ebinaFlat = Flatten("ebina home mid_center happy")
    show yumikoFlat at center behind tobe: #minor problem with layering
        xoffset -5 yoffset 75 alpha 0
        parallel:
            1.7
            linear 0.5 alpha 1.0
    show ebinaFlat at right behind yumikoFlat:
        xoffset 5 yoffset 75 alpha 0
        parallel:
            1.7
            linear 0.5 alpha 1.0
    voice "audio/voice/E5/CMM/03/TB/TB001.ogg"
    tobe "Yeah yeah that's easy! Ah, wanna come with, Yumiko and Ebina-san?"
    hide yumikoFlat
    hide ebinaFlat
    show yumiko home mid_center happy at center behind tobe: #minor problem with layering
        xoffset -5 yoffset 75
    show ebina home mid_center happy at right behind yumiko:
        xoffset 5 yoffset 75
    voice "audio/voice/E5/CMM/03/EB/EB000.ogg"
    ebina "I'm feeling a bit tired."
    show yumiko frown with dissolve
    voice "audio/voice/E5/CMM/03/YM/YM000.ogg"
    yumiko "I'm done for the day too."
    show tobe sad with dissolve
    voice "audio/voice/E5/CMM/03/TB/TB002.ogg"
    tobe "Eh? Nobody's gonna go? Serious?"
    window auto hide dissolve
    stop voice
    scene lodgeC:
        zoom 2 yoffset -350
    show hiratsuka home mid_center happy at left:
        xoffset 110 yoffset 75
    show haruno sweater mid_left happy at right:
        xoffset -235 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/CMM/03/HR/HR001.ogg"
    haruno "Shizuka-chan, night games. Why don't you go?"
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E5/CMM/03/SZ/SZ000.ogg"
    hiratsuka "Nah, I'm definitely tired today... And also, night is all about having a drink."
    show haruno vhappy with dissolve
    voice "audio/voice/E5/CMM/03/HR/HR002.ogg"
    haruno "Sounds good. I want to have a drink with you. Right, Meguri?"
    show meguri home mid vhappy at left with dissolve:
        xoffset -150 yoffset 75
        parallel:
            easein 0.75 xoffset -40
    voice "audio/voice/E5/CMM/03/MG/MG000.ogg"
    meguri "Then I'll join in with oolong tea."
    window auto hide dissolve
    stop voice
    scene lodgeC:
        zoom 1.9 xoffset -1680 yoffset -450
    show yukino home mid_center sad at left:
        xoffset 25 yoffset 75
    show yui home mid_left pout at right:
        xoffset -270 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/CMM/03/YI/YI000.ogg"
    yui "Um, what do you want to do, Yukinon?"
    voice "audio/voice/E5/CMM/03/YK/YK000.ogg"
    yukino "I'm... quite tired."
    show yui sad with dissolve
    voice "audio/voice/E5/CMM/03/YI/YI001.ogg"
    yui "Me too..."
    window auto hide dissolve
    stop voice
    scene lodgeC:
        zoom 1.3 truecenter yoffset 110 xoffset 200
    show saki home mid_right happy at left:
        xoffset 70 yoffset 75
    show keika home mid sad at right:
        xoffset -365 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/CMM/03/KE/KE000.ogg"
    keika "Saa-chan, Keika's tired..."
    show saki vhappy with dissolve
    voice "audio/voice/E5/CMM/03/SA/SA000.ogg"
    saki "Okay, Kei-chan, let's go brush our teeth."
    voice "audio/voice/E5/CMM/03/KE/KE001.ogg"
    keika "Yup..."
    window auto hide dissolve
    stop voice
    scene lodgeC:
        zoom 1.45 xcenter 0.37 yoffset -180
    show iroha home mid_center happy at left:
        xoffset 300 yoffset 75
    show kaori home mid closed at right:
        xoffset -185 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/CMM/03/IR/IR000.ogg"
    iroha "If Hayama-senpai's not going, then I'll pass too."
    voice "audio/voice/E5/CMM/03/OR/OR000.ogg"
    kaori "What should I do. I don't care to go though."
    voice "audio/voice/E5/CMM/03/TB/TB003.ogg"
    tobe "Eh? Eh? Nobody's going? Serious? Eh?"
    window auto hide dissolve
    scene lodgeC with dissolve
    hachiman "(It's sure gotten noisy... What should I do...?)"
    if ski_flag == "yukino":
        hachiman "(I'll get away from here quickly first... Then take a bath and go back to my room.)"
        hachiman "(Thanks to this afternoon's training, my muscles were aching quite a bit... Yukinoshita-san's training is strict...)"
        window auto hide dissolve
        stop music fadeout 1.0
        jump E5_YUK_03 #in hotsprings
    elif ski_flag == "haruno" or ski_flag == "meguri":
        hachiman "(I've had a rough day, I'm tired, I've eaten, so I'm going to bed today.)"
        show hiratsuka home mid_center vhappy at left:
            xoffset 110 yoffset 75
        show haruno sweater mid_left vhappy at right:
            xoffset -235 yoffset 75
        with dissolve
        voice "audio/voice/E5/CMM/03/HR/HR003.ogg"
        haruno "Oh~? Hikigaya-kun, where are you going? Come hang out with us~~."
        hachiman "(Nooot happening~♪)"
        jump E5_HAR_06
    elif ski_flag == "iroha":
        window auto hide dissolve
        stop music fadeout 0.5
        scene black with fade
        window auto show dissolve
        hachiman "(I'll get out of here for now. Which reminds me... there was an open air bath here, wasn't there?)"
        hachiman "(I have an open air bath just for myself right now, so I might as well enjoy it...)"
        "I suddenly remembered what Isshiki had said earlier (today?), but I quickly pushed it out of my mind."
        window auto hide dissolve
        jump E5_IRO_03
    elif ski_flag == "hiratsuka":
        hachiman "(Ah, those three drinking together means three times trouble. Hiratsuka-sensei spent all her energy on skiing, so she'll start drinking early...)"
        hachiman "(Totsuka also predicted I might get caught in thte crossfire here... better slip away before they notice...)"
        hachiman "(Speaking of Totsuka, where is he? I want to invite him t take a bath together!)"
        window auto hide dissolve
        jump E5_SHI_03
    elif ski_flag == "yui":
        hachiman "(It's so noisy in here. Komachi looks like happy though, so I'm glad I came.)"
        "What Orimoto said earlier still stuck in my mind. Honestly, I hated myself for knowing what to say when Yuigahama popped the question about our differences."
        hachiman "(For now I just wanna daze by myself.)"
        jump E5_YUI_03

label E5_CMM_04:
    scene lodgeA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM41.ogg"
    show iroha home mid_center vhappy at center with dissolve:
        xoffset -5 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/CMM/04/IR/IR000.ogg"
    iroha "Okay, let's do a light clean up today, and then head off to the ski slopes! Because I want to go skiing, please chop-chop and get it done."
    hachiman "(\"Because I want to go skiing\", this is completely for your own convenience, isn't it...)"
    show iroha mid_left happy with dissolve:
        xoffset -35 yoffset 65
    voice "audio/voice/E5/CMM/04/IR/IR001.ogg"
    iroha "Haruno-san, can we use the draw from yesterday?"
    hide iroha with dissolve
    show haruno sweater mid_center vhappy at left:
        xoffset 320 yoffset 75
    show iroha home mid_left happy at right:
        xoffset -315 yoffset 65
    with dissolve
    voice "audio/voice/E5/CMM/04/HR/HR000.ogg"
    haruno "Sure sure, use it as much as you want."
    show haruno sweater mid_left vhappy with dissolve:
        xoffset 200
    voice "audio/voice/E5/CMM/04/HR/HR001.ogg"
    haruno "Then, I'm going with Meguri for a morning ski. Everyone, I'll leave it to you!"
    hide haruno with dissolve
    show iroha pout with dissolve
    voice "audio/voice/E5/CMM/04/IR/IR002.ogg"
    iroha "Ah, Haru-san-senpai..."
    show yukino home mid_center unimpressed at left with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E5/CMM/04/YK/YK000.ogg"
    yukino "It's useless trying to stop her, Isshiki-san. Let's just get the cleaning done."
    window auto hide dissolve
    stop voice
    scene lodgeA with Fade(1.0, 1.0, 1.0)
    window auto show dissolve
    "As we finished breakfast, it was cleaning from the morning today as well. We'd start from whichever we drew out of the lottery."
    hachiman "(Actually...)"
    #branch around here for yukino route. going to use the ski flag for yukino route at this point...
    if ski_flag == "yukino":
        hachiman "(Well, getting the cleaning done first then going out to ski seemed best.)"
        "I didn't want to hear Tobe's voice first thing in the morning, but maybe because I was tired yesterday and had a good rest, my mood was feeling lighter."
        hachiman "(... Well, I did end up hearing that super rare Yukinoshita's girl's talk last night at the bath.)"
        "As I remembered that, I became somewhat embarassed and absent-mindedly drew from the lottery."
        jump E5_YUK_05
    elif ski_flag == "haruno":
        "Even though I was feeling quite tired, I realized that in some way I was enjoying this camp, considering the depressing way I was feeling before I came."
        "Looking back on it, I feel I haven't really had a dull moment here. I wonder why is that when I look back on my life, I can't think of a time I've felt the same way I do now."
        hachiman "(I wonder if she's going to toy with me again today...)"
        show iroha home mid_center unimpressed at center with dissolve:
            xoffset -5 yoffset 75
        voice "audio/voice/E5/CMM/04/IR/IR003.ogg"
        iroha "Senpai-. Stop dazing off and pull a stick already."
        voice "audio/voice/E5/CMM/04/HA/HA006.ogg"
        hachiman "Ah, sorry."
        window auto hide dissolve
        stop voice
        hide iroha with dissolve
        play sound "audio/sfx/SE01/SE01_12.ogg"
        $renpy.pause(delay=1.0, hard=True)
        stop sound
        jump E5_HAR_07
    elif ski_flag == "iroha":
        hachiman "(Drawing lots for our tasks, huh. Something about that seems a bit questionable...)"
        window auto hide dissolve
        show irohaHotspring with Fade(0.25,0.35, 0.5, color="#fff")
        window auto show dissolve
        "That's probably because the words Isshiki said to me last night were strangely still stuck in my head."
        voice "audio/voice/E5/CMM/04/IR/IR005.ogg"
        iroha "Senpai, you're so sloooow. Hurry up and draw your task!"
        window auto hide dissolve
        stop voice
        hide irohaHotspring
        show iroha home mid_center frown at center:
            xoffset -5 yoffset 75
        with Fade(0.25,0.35, 0.5, color="#fff")
        window auto show dissolve
        voice "audio/voice/E5/CMM/04/HA/HA002.ogg"
        hachiman "Huh? Ah. Sorry."
        hide iroha with dissolve
        jump E5_IRO_04
    elif ski_flag == "hiratsuka":
        hachiman "(I feel somehow... heavy-headed...)"
        stop music
        voice "audio/voice/E5/CMM/04/HA/HA003.ogg"
        hachiman "Achoo!"
        play music "audio/bgm/BGM47.ogg"
        show yukino home mid_center happy at left:
            xoffset 25 yoffset 75
        show yui home mid_center pout at right:
            xoffset -300 yoffset 75
        with dissolve
        voice "audio/voice/E5/CMM/04/YI/YI001.ogg"
        yui "Hikki, are you okay? You don't look so good."
        voice "audio/voice/E5/CMM/04/HA/HA004.ogg"
        hachiman "*sniff* That so?"
        show yukino angry with dissolve
        voice "audio/voice/E5/CMM/04/YK/YK001.ogg"
        yukino "Yes, you don't. I think you've caught a cold."
        show yukino:
            parallel:
                easein 0.75 xoffset -105
        show yui:
            parallel:
                easein 0.75 xoffset -175
        show iroha home mid_left vhappy at center behind yui with dissolve:
            xoffset -40 yoffset 65
        voice "audio/voice/E5/CMM/04/IR/IR006.ogg"
        iroha "That's from keeping busy all night~"
        voice "audio/voice/E5/CMM/04/HA/HA005.ogg"
        hachiman "Stop saying that in such a wierd way."
        show yukino stare with dissolve
        voice "audio/voice/E5/CMM/04/YK/YK002.ogg"
        yukino "I think it's best you just stay put in bed today."
        jump E5_SHI_05
    elif ski_flag == "yui":
        stop music fadeout 1.0
        "Although I slept soundly, I still feel tired. I feel lethargic too, how should I say..."
        show iroha home mid_center pout at center with dissolve:
            xoffset -5 yoffset 75
        voice "audio/voice/E5/CMM/04/IR/IR004.ogg"
        iroha "Senpai, your eyes don't look so good today, what's wrong?"
        voice "audio/voice/E5/CMM/04/HA/HA001.ogg"
        hachiman "...Ah, sorry."
        "Ishiki asked worriedly, I was daydreaming until she came to me."
        scene lodgeA:
            zoom 1.5 xoffset -715 yoffset -185
        show yumiko home mid_left sad at right:
            xoffset -240 yoffset 75
        show yui home mid_center sad at left:
            xoffset 335 yoffset 75
        with dissolve
        play music "audio/bgm/BGM46.ogg"
        voice "audio/voice/E5/CMM/04/YI/YI000.ogg"
        yui "..."
        voice "audio/voice/E5/CMM/04/YM/YM000.ogg"
        yumiko "..."
        hachiman "(...Yuigahama isn't looking good either.)"
        jump E5_YUI_04

label E5_CMM_05:
    scene slopesA with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/BGM41.ogg"
    window auto show dissolve
    voice "audio/voice/E5/CMM/05/HA/HA000.ogg"
    hachiman "But anyways..."
    play ambient "<from 2>audio/sfx/SE01/SE01_44L.ogg"
    "And so, once again, I was forcefully taken to the ski slopes, but it didn't really matter to me who wasn't into skiing."
    "Moreover, if I happened to have any competence, I wouldn't have this kind of personality either."
    window auto hide dissolve
    scene slopesA with dissolve:
        yoffset -2350 zoom 3.2 xcenter 0.23
    $renpy.pause(delay=1.0, hard=True)
    stop ambient
    play sound "audio/sfx/SE01/SE01_47.ogg"
    show komachi heavy_coat near_left happy at center:
        zoom 2.0 xoffset 400 yoffset 140 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.5 xoffset 80
    $renpy.pause(delay=1.0, hard=True)
    show komachi heavy_coat near_center happy at center:
        zoom 2.0 xoffset 65 yoffset 165
    with dissolve
    $renpy.pause(delay=0.5, hard=True)
    scene slopesA
    hide komachi
    show komachi heavy_coat mid_center vhappy at right:
        xoffset -370 yoffset 75
    with dissolve
    window auto hide dissolve
    voice "audio/voice/E5/CMM/05/KO/KO000.ogg"
    komachi "Onii-chan! Don't you think Komachi has gotten good at this?"
    voice "audio/voice/E5/CMM/05/HA/HA001.ogg"
    hachiman "Yeah, you sure have."
    window auto hide dissolve
    stop voice
    show komachi heavy_coat mid_left happy with dissolve:
        xoffset -440 yoffset 75
    $renpy.pause(delay=0.5, hard=True)
    hide komachi with dissolve
    play sound "audio/sfx/SE01/SE01_45.ogg"
    $renpy.pause(delay=1.8, hard=True)
    stop sound
    show keika heavy_coat far vhappy at left with dissolve:
        xoffset 215 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/CMM/05/KE/KE000.ogg"
    keika "Ah, it's Haa-chan! Hup!"
    window auto hide dissolve
    hide slopesA
    scene black
    play sound "audio/sfx/SE01/SE01_60.ogg"
    show slopesA at Shake(None, 0.25, dist=100)
    show keika heavy_coat far vhappy at left, Shake(None, 0.25, dist=60):
        xoffset 215 yoffset 75
    $renpy.pause(delay=0.25, hard=True)
    scene slopesA
    show keika heavy_coat far vhappy at left:
        xoffset 215 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/CMM/05/HA/HA002.ogg"
    hachiman "Oh, now you've done it, Kei-chan!"
    show keika heavy_coat mid vhappy at left with dissolve:
        xoffset 310 yoffset 75
    "I hold a snowball and carefully throw it back at Keika so that it misses."
    voice "audio/voice/E5/CMM/05/KE/KE001.ogg"
    keika "Haha! I dodged it!"
    voice "audio/voice/E5/CMM/05/HA/HA003.ogg"
    hachiman "Here."
    hachiman "(This is nice...)"
    hide keika with dissolve
    "And so, while we were throwing snowballs at each other, Keika became tired and sat down next to me."
    window auto hide dissolve
    scene slopesA:
        yoffset -2350 zoom 3.2 xcenter 0.23
    show keika heavy_coat near happy at center:
        xoffset -30 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/CMM/05/HA/HA004.ogg"
    hachiman "Hey, Kei-chan. If you sit here you'll catch a cold."
    play sound "audio/sfx/SE00/SE00_24.ogg"
    voice "audio/voice/E5/CMM/05/KE/KE002.ogg"
    keika "Keika isn't cold."
    voice "audio/voice/E5/CMM/05/SA/SA000.ogg"
    stop sound
    saki "Kei-chan, here you are! I told you to wait by the toilet."
    show keika vhappy2 with dissolve
    voice "audio/voice/E5/CMM/05/KE/KE003.ogg"
    keika "Ah, it's Saa-chan!"
    show keika vhappy with dissolve
    window auto hide dissolve
    scene slopesA
    show saki heavy_coat mid_right happy at left:
        xoffset 15 yoffset 75
    with dissolve
    play sound "audio/sfx/SE01/SE01_57.ogg"
    image keika heavy_coat mid vhappy flat = Flatten("keika heavy_coat mid vhappy")
    show keika heavy_coat mid vhappy flat at right:
        xoffset -305 yoffset 175 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.5 yoffset 75
    $renpy.pause(delay=0.5, hard=True)
    hide keika
    show keika heavy_coat mid vhappy at right:
        xoffset -305 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/CMM/05/HA/HA005.ogg"
    hachiman "Hey. I was wondering where you were."
    show saki pout with dissolve
    voice "audio/voice/E5/CMM/05/SA/SA001.ogg"
    saki "Ah, sorry, Hikigaya. She disappeared when I wasn't looking... Um... thanks for looking after her."
    voice "audio/voice/E5/CMM/05/HA/HA006.ogg"
    hachiman "It was nothing, I had fun."
    show keika happy with dissolve
    voice "audio/voice/E5/CMM/05/KE/KE004.ogg"
    keika "Yeah, Haa-chan played with me!"
    hide saki
    $url = ["saki heavy_coat mid_right happy", "saki heavy_coat mid_right vhappy"]
    $multiImagePara = [15, 75, 0, 0, 4.0]
    call multiImage(-1) from _call_multiImage_20
    voice "audio/voice/E5/CMM/05/SA/SA002.ogg"
    saki "That's not how it went... Okay, Kei-chan, should we go drink something warm?"
    call finishmultiImage from _call_finishmultiImage_21
    show saki heavy_coat mid_right vhappy at left:
        xoffset 15 yoffset 75
    voice "audio/voice/E5/CMM/05/SA/SA003.ogg"
    saki "Skiing must be hard for children after all. She seems a little tired, so I'm going to let her rest."
    voice "audio/voice/E5/CMM/05/HA/HA007.ogg"
    hachiman "Should I take her? You should go skiing while you have the chance too."
    show saki blush with dissolve
    voice "audio/voice/E5/CMM/05/SA/SA004.ogg"
    saki "N-no, you don't have to be considerate! Th-thanks though..."
    show keika vhappy with dissolve
    voice "audio/voice/E5/CMM/05/KE/KE005.ogg"
    keika "Haa-chan, see ya!"
    hide saki
    hide keika
    with dissolve
    hachiman "(You don't have to hold back. I don't have anything to do anyway.)"
    #Will need revisit to confirm branching logic after. for now proceeding as if only yukino route.
    if ski_flag == "yukino":
        stop music fadeout 0.5
        voice "audio/voice/E5/CMM/05/YK/YK000.ogg"
        mystery "Hikigaya-kun."
        voice "audio/voice/E5/CMM/05/HA/HA008.ogg"
        hachiman "Woah!?"
        show yukino heavy_coat mid_center happy at center with dissolve:
            xoffset -105 yoffset 75
        play music "audio/bgm/BGM11.ogg"
        hachiman "(Th-That scared me...!)"
        show yukino pout with dissolve
        voice "audio/voice/E5/CMM/05/YK/YK001.ogg"
        yukino "Um... Did I surprise you?"
        voice "audio/voice/E5/CMM/05/HA/HA009.ogg"
        hachiman "N-nah, it's just because I was spacing out."
        show yukino happy with dissolve
        voice "audio/voice/E5/CMM/05/YK/YK002.ogg" #I think it branches here if not yukino. Below script says he'd make a good Dad, probably in other routes.
        yukino "Is that so? You looked like you were having fun so I didn't want to disturb you."
        voice "audio/voice/E5/CMM/05/HA/HA010.ogg"
        hachiman "Were you watching...?"
        show yukino vhappy with dissolve
        voice "audio/voice/E5/CMM/05/YK/YK003.ogg"
        yukino "I thought this before too... you're good with children, aren't you?"
        voice "audio/voice/E5/CMM/05/HA/HA011.ogg"
        hachiman "Well, I have a brotherly nature... So, what's up?"
        show yukino blush with dissolve
        voice "audio/voice/E5/CMM/05/YK/YK004.ogg"
        yukino "No, um... If you'd like I was thinking we could continue from  yesterday..."
        #yukino route: proceeds into E5_YUK_08
        jump E5_YUK_08
    elif ski_flag == "haruno":
        window auto hide dissolve
        scene slopesA at left:
            zoom 1.5 xoffset 0 yoffset 105
        show yukino heavy_coat mid_center pout at left:
            xoffset -105 yoffset 75
        show komachi heavy_coat mid_left vhappy at center:
            xoffset 5 yoffset 75
        show yui heavy_coat mid_left vhappy at right:
            xoffset -145 yoffset 75
        with dissolve
        window auto show dissolve
        voice "audio/voice/E5/CMM/05/YI/YI002.ogg"
        yui "Yukino~! Is it like this?"
        show yukino happy with dissolve
        voice "audio/voice/E5/CMM/05/YK/YK006.ogg"
        yukino "Yes. You've really improved quite a bit. Now then, Komachi-san, you try sliding down."
        voice "audio/voice/E5/CMM/05/KO/KO001.ogg"
        komachi "Gotcha!"
        hide komachi with dissolve
        play sound "audio/sfx/SE01/SE01_45.ogg"
        $renpy.pause(delay=0.5, hard=True)
        show yui happy with dissolve
        voice "audio/voice/E5/CMM/05/YI/YI003.ogg"
        yui "Komachi-chan, you got good so quick. Yukinon's teaching is the best."
        stop sound
        show yukino vhappy with dissolve
        voice "audio/voice/E5/CMM/05/YK/YK007.ogg"
        yukino "It's not like that. You're already good enough that you don't need much coaching."
        show yui vhappy with dissolve
        voice "audio/voice/E5/CMM/05/YI/YI004.ogg"
        yui "Ehehe. You think so~?"
        stop music fadeout 0.5
        play sound "audio/sfx/SE01/SE01_46.ogg"
        hachiman "(Hmm? Isn't something a bit funny about this situation?)"
        window auto hide dissolve
        jump E5_HAR_08
    elif ski_flag == "iroha":
        stop music fadeout 1.0
        hachiman "(Anyway...)"
        window auto hide dissolve
        scene slopesA at right:
            zoom 1.5 xoffset 0 yoffset 100
        show iroha heavy_coat mid_center unimpressed at left:
            xoffset 240 yoffset 75
        show tobe heavy_coat mid angry at right:
            xoffset -120 yoffset 75
        with dissolve
        play music "audio/bgm/BGM44.ogg"
        window auto show dissolve
        voice "audio/voice/E5/CMM/05/IR/IR000.ogg"
        iroha "No, that's completely wrong. Don't ski like that. You'll slip and fall to your death."
        show tobe sad with dissolve
        voice "audio/voice/E5/CMM/05/TB/TB000.ogg"
        tobe "Tch! Irohasu, that's harsh! Hayato-kun, save meeee!"
        show iroha mid_left with dissolve:
            xoffset 240 yoffset 65
        voice "audio/voice/E5/CMM/05/IR/IR001.ogg"
        iroha "Hayama-senpai, why do I have to be the one to teach Tobe-senpai?"
        play sound "audio/sfx/SE01/SE01_46.ogg"
        hachiman "(It seems pretty noisy over there.)"
        window auto hide dissolve
        stop sound
        play sound "audio/sfx/SE01/SE01_47.ogg"
        $renpy.pause(delay=1.0, hard=True)
        scene slopesA
        show yukino heavy_coat mid_center happy at left:
            xoffset 25 yoffset 75
        show yui heavy_coat mid_center vhappy at right:
            xoffset -245 yoffset 75
        with dissolve
        window auto show dissolve
        voice "audio/voice/E5/CMM/05/YI/YI000.ogg"
        yui "Yahallo, Hikki!"
        show yukino vhappy with dissolve
        voice "audio/voice/E5/CMM/05/YK/YK005.ogg"
        yukino "You seem like you'll make a good father one day."
        voice "audio/voice/E5/CMM/05/HA/HA012.ogg"
        hachiman "So you were watching me, huh."
        show yui happy with dissolve
        voice "audio/voice/E5/CMM/05/YI/YI001.ogg"
        yui "We just happened to stumble across a heartwarming sight. Whoops!"
        hachiman "(Don't \"Whoops!\" me like that. Geez, so embarrassing!)"
        window auto hide dissolve
        jump E5_IRO_06
    elif ski_flag == "meguri":
        voice "audio/voice/E5/CMM/05/MG/MG000.ogg"
        mystery "He--y!"
        hachiman "(Hm?)"
        show meguri heavy_coat far vhappy at center with dissolve:
            xoffset 20 yoffset 75
        voice "audio/voice/E5/CMM/05/MG/MG001.ogg"
        meguri "Everyone! Gather around for a bit!"
        jump E5_HAR_09
    elif ski_flag == "yui":
        stop music fadeout 0.75
        hachiman "(Now, what do I do? Should I call out to Yuigahama?)"
        hachiman "(She's really on the caring side. I think she'd be better off just making memories with Miura's group. Besides, it'll just be sad if I keep bothering her.)"
        window auto hide dissolve
        show white with Dissolve(1.0)
        $renpy.pause(delay=1.0, hard=True)
        scene clubroomA
        show yui school mid_center happy at center:
            xoffset 0 yoffset 75
        with dissolve
        play music "audio/bgm/BGM21.ogg"
        "When she first joined the Service Club, Yuigahama was torn between Yukinoshita and I and Hayama's group."
        "She seemed to have solved that issue by her sheer will and effort, but in the end, just in line with what Orimoto said yesterday, it was nothing more than looking away from the truth."
        "Leaving aside the proudly independant Yukinoshita, Yuigahama and I..."
        window auto hide dissolve
        show white with Dissolve(1.0)
        scene slopesA with dissolve
        hachiman "(I relied on her kindness too much.)"
        window auto hide dissolve
        play sound "audio/sfx/SE01/SE01_57.ogg"
        $renpy.pause(delay=1.0, hard=True)
        show yui heavy_coat mid_center happy at center with dissolve:
            xoffset 0 yoffset 75
        jump E5_YUI_06

#label skip_yuk:
    hachiman "(さて、どうするかな⋯⋯。由比ヶ浜に声をかけていいものやら⋯⋯)"
    hachiman "(あいつ、いろいろ気を使う方だしな。三浦たちとの思い出もあったほうがいいだろうし。⋯⋯それに、いらんこと言われるのも気の毒だ)"
    "思えば由比ヶ浜が初めて奉仕部に来た頃、あいつは葉山たちと俺や雪ノ下との間で、板挟みになって悩んでいた。"
    "それは由比ヶ浜自身の意志や努力によって解消されたかのように見えたが、所詮は『お目こぼし』されているに過ぎないのだと、昨日の折本の言葉は明確に語っていた。"
    "孤高である雪ノ下はともかく、俺と由比ヶ浜では⋯⋯"
    hachiman "(あいつの優しさに甘えすぎてたな⋯⋯)"

    yumiko "⋯⋯あー。ヒキオ、ちょっといい？"
    voice "audio/voice/E5/CMM/05/HA/HA000.ogg"
    hachiman "⋯⋯おう。どうした？"
    yumiko "⋯⋯さっきはありがと"
    voice "audio/voice/E5/CMM/05/HA/HA000.ogg"
    hachiman "は？ いや、別に特になんもしてないんだけど⋯⋯"
    yumiko "いや、そーいうことじゃなくて"
    voice "audio/voice/E5/CMM/05/HA/HA000.ogg"
    hachiman "⋯⋯⋯⋯"
    yumiko "あーし、ちゃんと言ってみる"
    hachiman "(ま、とりあえず少しは滑ってみるか⋯⋯)"
    voice "audio/voice/E5/CMM/05/SI/SI000.ogg"
    totsuka "はちまーん。探しちゃった"
    voice "audio/voice/E5/CMM/05/HA/HA000.ogg"
    hachiman "お⋯⋯おう、戸塚か"
    hachiman "(『探しちゃった』とか、なんて甘酸っぱい響き！)"
    voice "audio/voice/E5/CMM/05/SI/SI000.ogg"
    totsuka "昨日は何だかはぐれちゃったからさ、今日は一緒に滑りたいな、って⋯⋯"
    voice "audio/voice/E5/CMM/05/HA/HA000.ogg"
    hachiman "そうか⋯⋯悪い。けど俺下手だぞ。超初心者だし"
    voice "audio/voice/E5/CMM/05/SI/SI000.ogg"
    totsuka "あはは。いいよ、八幡と滑れれば"
    hachiman "(『八幡と滑れれば』って言った！？ この一面の銀世界に、白い天使が舞い降りてきた！？)"
    voice "audio/voice/E5/CMM/05/HA/HA000.ogg"
    hachiman "そ、そうか⋯⋯"
    voice "audio/voice/E5/CMM/05/EB/EB000.ogg"
    ebina "はろはろ〜。とつはち発見！"
    voice "audio/voice/E5/CMM/05/SI/SI000.ogg"
    totsuka "あ、海老名さんも一緒に滑ろうよ"
    hachiman "(⋯⋯⋯⋯！！)"
    voice "audio/voice/E5/CMM/05/YI/YI000.ogg"
    yui "ゆきのーん、こんな感じかな？"
    voice "audio/voice/E5/CMM/05/YK/YK000.ogg"
    yukino "ええ。かなり上達したんじゃないかしら。じゃあ次は小町さんが滑ってみて"
    voice "audio/voice/E5/CMM/05/KO/KO000.ogg"
    komachi "はーい！"
    voice "audio/voice/E5/CMM/05/YI/YI000.ogg"
    yui "小町ちゃん、上達早いねー。やっぱゆきのんの教え方が上手いからかな？"
    voice "audio/voice/E5/CMM/05/YK/YK000.ogg"
    yukino "そんなことないわ。あなただって教わるまでもなく、十分上手だと思う"
    voice "audio/voice/E5/CMM/05/YI/YI000.ogg"
    yui "えへへ。そうかなー"
    hachiman "(⋯⋯ん？ 何か様子がおかしくないか？)"
    "not finished"

label E5_CMM_06:
    scene lodgeC with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM10.ogg"
    window auto show dissolve
    "As tonight was the last night of this camp, the living room was so lively. Just three days and two nights passed by really quickly."
    "As for me..."
    #maybe branch depending on route
    if ski_flag == "yukino":
        hachiman "(I wonder if Yukinoshita is okay?)"
        "I was curious about how Yukinoshita was doing."
        "She'd gone to rest in her room right after we got back and hadn't come for dinner either. I knew she'd probably just fallen asleep from exhaustion,
            but I still felt curious."
        hachiman "(Well it wasn't unreasonable. She must be really tired...)"
        jump E5_YUK_09
    elif ski_flag == "iroha":
        jump E5_CMM_06_iro
    if ski_flag == "hiratsuka":
        window auto hide dissolve
        scene lodgeroomC with Fade(0.5, 0.5, 0.5)
        play ambient "audio/sfx/SE05/SE05_02L.ogg"
        window auto show dissolve
        "I spent the day in bed with a fever."
        hachiman "(They're getting pretty excited...)"
        "Normally, I wouldn't want to mix with them, but when I'm alone in bed like this, I feel a certain amount of lonliness, which make me think that human are such selfish creatures."
        hachiman "(Come to think of it, I did Hiratsuka-sensei dirty... She wasn't able to ski today I don't think.)"
        window auto hide dissolve
        stop ambient fadeout 0.5
        stop music fadeout 1.0
        jump E5_SHI_07
    elif ski_flag == "meguri":
        jump E5_HAR_10
    elif ski_flag == "yui":
        jump E5_CMM_06_YUI
    jump E5_CMM_06_skip_yuk


label E5_CMM_06_iro:
    hachiman "(A certain someone doesn't seem to be reveling in the excitement like everyone else.)"
    show iroha home far_left pout at center with dissolve:
        xoffset -25 yoffset 80
    "She was standing alone in a corner, absentmindedly lost in thought."
    hachiman "(Hm? What is that girl doing?)"
    show iroha surprised with dissolve
    show iroha:
        parallel:
            linear 0.1 yoffset 50
            pause 0.08
            linear 0.1 yoffset 80
            pause 0.08
            repeat 3
    voice "audio/voice/E5/CMM/06/IR/IR000.ogg"
    iroha "...!!"
    show iroha far_center vhappy with dissolve:
        xoffset 0 yoffset 75
    "Suddenly, she looked up at me and fervently beckoned me over to the door."
    hachiman "(I wonder what trivial tasks she wants me to do now? Guess I don't have a choice...)"
    window auto hide dissolve
    scene lodgeC:
        zoom 1.45 xcenter 0.37 yoffset -180
    show iroha home mid_center vhappy at center:
        xoffset -5 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/CMM/06/HA/HA000.ogg"
    hachiman "What is it?"
    hide iroha with dissolve
    show iroha home near_center happy at center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E5/CMM/06/IR/IR001.ogg"
    iroha "Senpai, it took you way too long to notice."
    voice "audio/voice/E5/CMM/06/HA/HA001.ogg"
    hachiman "And? Did you need something?"
    show iroha blush with dissolve
    voice "audio/voice/E5/CMM/06/IR/IR002.ogg"
    iroha "Could you come with me for a second?"
    window auto hide dissolve
    stop voice
    stop music fadeout 0.5
    jump E5_IRO_07

label E5_CMM_06_YUI:
    window auto hide dissolve
    show white with Dissolve(1.0)
    $renpy.pause(delay=0.5, hard=True)
    scene yuiSkiCG with dissolve
    window auto show dissolve
    voice "audio/voice/E5/CMM/06/YI/YI000.ogg"
    yui "Thank you, Hikki."
    window auto hide dissolve
    show white with Dissolve(1.0)
    $renpy.pause(delay=0.5, hard=True)
    scene lodgeC with dissolve
    window auto show dissolve
    "The fact I couldn't answer her feelings was tearing me up."
    hachiman "(Yuigahama is a really good person. If I told her, she'd pull a confused face, but she's kinder than she realizes.)"
    hachiman "(What is the right answer to that kindness?)"
    hachiman "(...Hm?)"
    window auto hide dissolve
    scene lodgeC:
        zoom 1.9 xoffset -1680 yoffset -450
    show yukino home mid_center happy at left:
        xoffset 25 yoffset 75
    show yui home mid_left sad at right:
        xoffset -270 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/CMM/06/YI/YI001.ogg"
    yui "Yukinon, um... can I talk to you for a bit?"
    show yukino home mid_center surprised at left with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E5/CMM/06/YK/YK000.ogg"
    yukino "I don't mind... What's wrong?"
    show yui home mid_left happy at right with dissolve:
        xoffset -270 yoffset 75
    voice "audio/voice/E5/CMM/06/YI/YI002.ogg"
    yui "Here is a little... C-Can we go outside?"
    show yukino home mid_center pout at left with dissolve:
        xoffset 25 yoffset 75
    voice "audio/voice/E5/CMM/06/YK/YK001.ogg"
    yukino "Sure..."
    window auto hide dissolve
    scene lodgeC with dissolve
    window auto show dissolve
    voice "audio/voice/E5/CMM/06/HA/HA002.ogg"
    hachiman "Yuigahama?"
    stop music fadeout 1.0
    window auto hide dissolve
    jump E5_YUI_07

label E5_CMM_06_skip_yuk:
    voice "audio/voice/E5/CMM/06/YI/YI000.ogg"
    yui "ヒッキー、ありがとう⋯⋯"
    "俺は、その言葉に答えられなかったことについて、煩悶していた。"
    hachiman "(由比ヶ浜は優しいやつだ。そう言うと複雑な顔になるが、おそらく本人が思っているより、ちゃんと優しいやつだ)"
    hachiman "(その優しさに応える正しい答えは、いったい何だろう⋯⋯)"
    hachiman "(⋯⋯ん？)"
    voice "audio/voice/E5/CMM/06/YI/YI000.ogg"
    yui "ゆきのん、その⋯⋯ちょっといいかな？"
    voice "audio/voice/E5/CMM/06/YK/YK000.ogg"
    yukino "かまわないけれど⋯⋯どうしたの？"
    voice "audio/voice/E5/CMM/06/YI/YI000.ogg"
    yui "ここじゃちょっと⋯⋯あ、あの、外行かない？"
    voice "audio/voice/E5/CMM/06/YK/YK000.ogg"
    yukino "ええ⋯⋯"
    voice "audio/voice/E5/CMM/06/HA/HA000.ogg"
    hachiman "⋯⋯由比ヶ浜？"
    hachiman "(いやー、ここ最近のあの子、ちょっと迷走しすぎじゃないでしょうかね⋯⋯)"
    "リビングの隅で話に加わるでもなく、ぼんやりと考え事をしていた。"
    hachiman "(⋯⋯ん？ 何やってんだあいつ)"
    voice "audio/voice/E5/CMM/06/IR/IR000.ogg"
    iroha "⋯⋯⋯⋯⋯⋯！！"
    "ふと顔を上げると、今まで考えていた当の本人が、入り口のあたりで必死に手招きしていた。"
    hachiman "(⋯⋯また野暮用か？ 仕方ないな⋯⋯)"
    voice "audio/voice/E5/CMM/06/HA/HA000.ogg"
    hachiman "何だ？"
    voice "audio/voice/E5/CMM/06/IR/IR000.ogg"
    iroha "もう先輩、気づくの遅すぎです"
    voice "audio/voice/E5/CMM/06/HA/HA000.ogg"
    hachiman "⋯⋯で、何か用か？"
    voice "audio/voice/E5/CMM/06/IR/IR000.ogg"
    iroha "⋯⋯ちょっと、一緒に来てくれませんか？"
    hachiman "(何だかんだ怒涛の合宿だった気もするが⋯⋯まあ三浦の件も無事解決してよかった⋯⋯よな？)"
    "一方俺はといえば、熱を出してしまい本格的に寝込む一日となってしまった。"
    hachiman "(何だか盛り上がってんな⋯⋯)"
    "普段なら決して混ざりたくないと思うだろうに、こうして一人寝込んでいると、それなりに寂しいものを感じるから、人間というものはつくづく勝手な生き物だ。"
    hachiman "(そういや平塚先生には悪いことしたな⋯⋯結局今日スキーできなかったんじゃないかしら⋯⋯)"

label E5_CMM_07:
    scene skyC with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM10.ogg"
    window auto show dissolve
    hachiman "(I took the effort to take a bath, but why did I have to spend time with Hayama? Is it the age of HayaHachi after all?)"
    hachiman "(Well, I just have to sleep after this, then this trip is over...)"
    window auto hide dissolve
    scene hachimanBatha with Fade(0.25,0.35, 0.5, color="#fff")
    voice "audio/voice/E5/CMM/07/HY/HY000.ogg"
    hayama "If you avert your eyes, and what you see is still broad... what is it you've decided you want to see?"
    window auto show dissolve
    stop voice
    scene skyC with Fade(0.25,0.35, 0.5, color="#fff")
    hachiman "(Even if you ask me that...)"
    window auto hide dissolve
    stop music fadeout 1
    scene black with Fade(1.0, 0.5, 1.0)
    play footsteps "audio/sfx/SE00/SE00_30L.ogg" loop
    window auto show dissolve
    "While Hayama's words stuck to me, as I was returning to my room..."
    window auto hide dissolve
    stop footsteps fadeout 1
    scene lodgeC
    show haruno sweater mid_center vhappy at center:
        xoffset 10 yoffset 75
    with Fade(0, 0.5, 1.0)
    play music "audio/bgm/BGM19.ogg"
    window auto show dissolve
    voice "audio/voice/E5/CMM/07/HR/HR000.ogg"
    haruno "Hyahello, Hikigaya-kun."
    voice "audio/voice/E5/CMM/07/HA/HA000.ogg"
    hachiman "Hey... Well I'll be going."
    show haruno sly with dissolve
    voice "audio/voice/E5/CMM/07/HR/HR001.ogg"
    haruno "Sounds like you're in a super bad mood."
    voice "audio/voice/E5/CMM/07/HA/HA001.ogg"
    hachiman "Yes, I am in a super bad mood. So, see ya."
    show haruno sad with dissolve
    voice "audio/voice/E5/CMM/07/HR/HR002.ogg"
    haruno "That's so cold to a beautiful onee-san."
    jump E5_YUK_12

label E5_CMM_07_YUI:
    scene skyC with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM10.ogg"
    window auto show dissolve
    hachiman "(I just wanted to relax and take a bath, but yet I ended up in a close cage match with Hayama. This might really be the age of HayaHachi...)"
    hachiman "(Well, there's nothing else left to do but sleep. The ski camp is over...)"
    stop music fadeout 1.0
    window auto hide dissolve
    play sound "audio/sfx/SE00/SE00_30L.ogg"
    scene black with dissolve
    window auto show dissolve
    "I headed to my room full of unsettled feelings."
    stop sound fadeout 0.5
    window auto hide dissolve
    scene lodge2A
    show yumiko home near_left frown at center:
        xoffset -50 yoffset 75
    with dissolve
    window auto show dissolve
    hachiman "(Miura? Did she finish her bath, too? Well, anyway...)"
    play music "audio/bgm/BGM19.ogg"
    show yumiko home near_center happy at center with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/CMM/07/YM/YM000.ogg"
    yumiko "Hikkio, can I talk to you for a bit?"
    voice "audio/voice/E5/CMM/07/HA/HA002.ogg"
    hachiman "Eh?"
    hachiman "(T-This is kind of scary for some reason...)"
    show yumiko home near_center frown at center with dissolve:
        xoffset -50 yoffset 75
    jump E5_YUI_09

#not sure how to get here.
label E5_CMM_07_skip_yuk:
    hachiman "(三浦か。あいつも風呂上りかな。ま、いいか⋯⋯)"
    voice "audio/voice/E5/CMM/07/YM/YM000.ogg"
    yumiko "ヒキオ、ちょっといい？"
    voice "audio/voice/E5/CMM/07/HA/HA002.ogg"
    hachiman "え？"
    hachiman "(な、何だか怖いんですけど)"
    hachiman "(風呂に入ったのに、息抜きどころか疲れた⋯⋯)"
    hachiman "(iroha、か⋯⋯)"
    "考え疲れ、ふらふらとリビングの前を通りかかる。何だか喉がとても乾いているような気がした。"
    hachiman "(⋯⋯ん？)"
    hachiman "(あー、せっかく風呂で何もかもさっぱりしようと思ってたのに⋯⋯)"
    hachiman "(ま、三浦も元気になったようだし、結果オーライってとこか。今日は安心して寝れそうだな)"
    hachiman "(⋯⋯寝る前に水分取っとくかな)"
    hachiman "(しかし風呂にまで潜んでいるとは、海老名さんの腐女子力おそろしい⋯⋯)"
    hachiman "(⋯⋯まあ、潜んでいたってより、単にバッティングしただけなんだろうが⋯⋯)"
    hachiman "(いやでもあの勢いだと、誰か男湯に来るまでじっと潜んでいた可能性もあるぞ)"
