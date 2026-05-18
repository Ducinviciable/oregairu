label E2_YUI_01:
    scene khstationA
    voice "audio/voice/E2/YUI/01/YI/YI000.ogg"
    mystery "Ah, Hikki~!"
    hachiman "(Hm? That voice...)"
    play music "audio/bgm/BGM12.ogg"
    show yui coat far_center happy at left:
        xoffset 375 yoffset 75
    show yumiko coat far_center happy at center behind yui:
        xoffset 0 yoffset 75
    show ebina coat far_center happy at right:
        xoffset -190 yoffset 75
    with dissolve
    "When I raised my head, I saw that not only Yuigahama was there, but Miura and Ebina as well."
    hide yui
    hide yumiko
    hide ebina
    with dissolve
    show yui coat mid_center vhappy at center with dissolve:
        xoffset 0 yoffset 75
    voice "audio/voice/E2/YUI/01/YI/YI001.ogg"
    yui "Ahaha... Yahallo~"
    hachiman "(Oh, she called out to me without thinking when she saw me. I myself would usually pass other people without even looking at them.)"
    menu E2_YUI_01_menu:
        with dissolve
        "Hey...":
            "not done"
            jump E2_YUI_01_menu
        "'Sup'.":
            "not done"
            jump E2_YUI_01_menu
        "Oh, it's you.":
            voice "audio/voice/E2/YUI/01/HA/HA004.ogg"
            hachiman "It's you."
            hachiman "(Oops, I sounded kinda happy when I said that. Oof, that's embarrassing!)"
            show yui coat mid_center surprised at center with dissolve:
                xoffset 0 yoffset 75
            voice "audio/voice/E2/YUI/01/YI/YI005.ogg"
            yui "...!"
            show yui coat mid_center vhappy at center with dissolve:
                xoffset 0 yoffset 75
            voice "audio/voice/E2/YUI/01/YI/YI006.ogg"
            yui "Yeah! Everyone's with me, too!"
            voice "audio/voice/E2/YUI/01/HA/HA005.ogg"
            hachiman "So it looks."
            hide yui with dissolve
    show yui coat mid_center happy at left:
        xoffset 190 yoffset 75
    show yumiko coat mid_center frown at center behind yui:
        xoffset 0 yoffset 75
    show ebina coat mid_center vhappy at right behind yumiko:
        xoffset 0 yoffset 75
    with dissolve
    voice "audio/voice/E2/YUI/01/EB/EB000.ogg"
    ebina "Hallo Hallo, Hikitani-kun."
    voice "audio/voice/E2/YUI/01/YM/YM000.ogg"
    yumiko "It's just you, Hikio."
    voice "audio/voice/E2/YUI/01/HA/HA006.ogg"
    hachiman "'Sup."
    show yui coat mid_center vhappy at left with dissolve:
        xoffset 190 yoffset 75
    voice "audio/voice/E2/YUI/01/YI/YI007.ogg"
    yui "All of us are out shopping today!"
    voice "audio/voice/E2/YUI/01/HA/HA007.ogg"
    hachiman "That right?"
    hachiman "(Hm? Something feels a bit off... Ah, I got it.)"
    voice "audio/voice/E2/YUI/01/HA/HA008.ogg"
    hachiman "You're not out with Hayama and the others today? That's kinda rare."
    stop music fadeout 0.75
    show yui coat mid_center pout at left with dissolve:
        xoffset 190 yoffset 75
    voice "audio/voice/E2/YUI/01/YI/YI008.ogg"
    yui "Ah..."
    play music "audio/bgm/BGM47.ogg"
    show yumiko coat mid_left frown at center behind yui:
        xoffset 0 yoffset 75
    voice "audio/voice/E2/YUI/01/YM/YM001.ogg"
    yumiko "..."
    voice "audio/voice/E2/YUI/01/YI/YI009.ogg"
    yui "A-Ah, you know, Hikki..."
    show ebina coat mid_center happy at right behind yumiko:
        xoffset 0 yoffset 75
    voice "audio/voice/E2/YUI/01/EB/EB001.ogg"
    ebina "Today's our girls day out. Hayato-kun said he's gonna be busy with family stuff."
    hachiman "(So that's why she's in a bad mood.  I guess that's kind of family he's a part of.)"
    hachiman "(That being the case, the sooner I leave, the better.)"
    voice "audio/voice/E2/YUI/01/HA/HA009.ogg"
    hachiman "Ah, see you then."
    show yui coat mid_center happy at left with dissolve:
        xoffset 190 yoffset 75
    voice "audio/voice/E2/YUI/01/YI/YI010.ogg"
    yui "Ah, see you later!"
    hide yui
    hide yumiko
    hide ebina
    with dissolve
    stop music fadeout 1.0
    play ambient "audio/sfx/SE05/SE05_01L.ogg"
    hachiman "(Damn, the actually really tired me out. I better hurry up and buy something Komachi'll be happy with.)"
    window auto hide dissolve
    stop ambient fadeout 1.0
    jump E2_YUI_02

label E2_YUI_02:
    scene bedroomC
    with Fade(1.0, 0.5, 1.0)
    play sound "audio/sfx/SE03/SE03_00L.ogg" loop
    hachiman "(Hm? It's Yuigahama.)"
    "I act surprised, but Yuigahama's probably the only person that'd text me."
    stop sound fadeout 0.75
    window auto hide dissolve
    play sound "audio/sfx/SE03/SE03_01.ogg"
    play music "audio/bgm/BGM06.ogg"
    $renpy.pause(delay=1.0, hard=False)
    call mail_clear from _call_mail_clear_2
    show black with dissolve:
        alpha 0.3
    voice "audio/voice/E2/YUI/02/YI/YI000.ogg"
    call mail_function("yui", "yui", "", "Hikki, are you free right now?") from _call_mail_function_23
    yui "\"Hikki, are you free right now?\""
    voice "audio/voice/E2/YUI/02/HA/HA000.ogg"
    play sound "audio/sfx/SE03/SE03_02.ogg"
    call mail_function("yui", "hachiman", "Re:", "Yes.") from _call_mail_function_24
    hachiman "\"Yes.\""
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    voice "audio/voice/E2/YUI/02/YI/YI001.ogg"
    call mail_function("yui", "yui", "Re2:", "That was fast! And it's just a word!?") from _call_mail_function_25
    yui "\"That was fast! And it's just a word!?\""
    voice "audio/voice/E2/YUI/02/HA/HA001.ogg"
    hachiman "Hm."
    "Now that she says it, I noticed. How recently, when it's Yuigahama mailing me, I respond right away."
    play sound "audio/sfx/SE03/SE03_02.ogg"
    voice "audio/voice/E2/YUI/02/HA/HA002.ogg"
    call mail_function("yui", "hachiman", "Re3:", "I've just gotten used to texting you.") from _call_mail_function_26
    hachiman "\"I've just gotten used to texting you.\""
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    voice "audio/voice/E2/YUI/02/YI/YI002.ogg"
    call mail_function("yui", "yui", "Re4:", "Ehehe~") from _call_mail_function_27
    yui "\"Ehehe~\""
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    voice "audio/voice/E2/YUI/02/YI/YI004.ogg"
    call mail_function("yui", "yui", "", "Say...") from _call_mail_function_28
    yui "\"Say...\"" #Check translation, Yui Part 3 8:28
    "Although it's just short texts, they're creating a pretty tense mood..."

label E2_YUI_03:
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    voice "audio/voice/E2/YUI/03/YI/YI000.ogg"
    call mail_function("yui", "yui", "", "Um... I was really surprised when I ran into you today!") from _call_mail_function_29
    yui "\"Um... I was really surprised when I ran into you today!\""
    hachiman "(Yeah, no kidding.)"
    play sound "audio/sfx/SE03/SE03_02.ogg"
    voice "audio/voice/E2/YUI/03/HA/HA000.ogg"
    call mail_function("yui", "hachiman", "Re:", "I saw who you were with and wanted to run away ASAP.") from _call_mail_function_30
    hachiman "\"I saw who you were with and wanted to run away ASAP.\""
    "Yuigahama took a little longer than usual to reply."
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    voice "audio/voice/E2/YUI/03/YI/YI001.ogg"
    call mail_function("yui", "yui", "", "I'm sorry Yumiko was in a bad mood, okay?") from _call_mail_function_31
    yui "\"I'm sorry Yumiko was in a bad mood, okay?\""
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    voice "audio/voice/E2/YUI/03/YI/YI002.ogg"
    call mail_function("yui", "yui", "", "It's like we can't get Hayato-kun out these days, Yumiko was pretty down about it.") from _call_mail_function_32
    yui "\"We couldn't get a hold of Hayato-kun like, at all. Yumiko was feeling a bit down because of it.\""
    hachiman "(That was her feeling down?)"
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    voice "audio/voice/E2/YUI/03/YI/YI003.ogg"
    call mail_function("yui", "yui", "", "I think it might have something to do with what happened on New Year's.") from _call_mail_function_33
    yui "\"I think it might have something to do with what happened on New Year's.\""
    play sound "audio/sfx/SE03/SE03_02.ogg"
    voice "audio/voice/E2/YUI/03/HA/HA001.ogg"
    call mail_function("yui", "hachiman", "", "Don't you think it doesn't actually have anything to do with it? Not that I care, but Yukinoshita and Hayama seem to have pretty similiar family circumstances.") from _call_mail_function_34
    hachiman "\"Don't you think it doesn't actually have anything to do with it? Not that I care, but Yukinoshita and Hayama seem to have pretty similiar family circumstances.\""
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    voice "audio/voice/E2/YUI/03/YI/YI004.ogg"
    call mail_function("yui", "yui", "", "Right... They're both always so busy, so it gets me kind of curious. Haha.") from _call_mail_function_35
    yui "\"Right... They're both always so busy, so it gets me kind of curious. Haha.\""
    play sound "audio/sfx/SE03/SE03_02.ogg"
    voice "audio/voice/E2/YUI/03/HA/HA002.ogg"
    call mail_function("yui", "hachiman", "", "Well, hopefully nothing's wrong.") from _call_mail_function_36
    hachiman "Well, hopefully nothing's wrong."
    hachiman "(Yumiko's probably thinking that there's something between Hayama and Yukinoshita.)"
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    voice "audio/voice/E2/YUI/03/YI/YI005.ogg"
    call mail_function("yui", "yui", "Re:", "Right~") from _call_mail_function_37
    yui "\"Yeah...\"" #Check transaltion, Yui Part 3 9:25

label E2_YUI_04:
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    voice "audio/voice/E2/YUI/02/YI/YI003.ogg" #Idk why this is in E2 > YUI > 02
    call mail_function("yui", "yui", "", "Ah, by the way") from _call_mail_function_38
    yui "\"Ah, by the way\""
    "I could almost hear her cheery voice through her text messages, and I couldn't help but smile."
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    voice "audio/voice/E2/YUI/04/YI/YI000.ogg"
    call mail_function("yui", "yui", "", "Sorry, Sable jumped on me so I sent that one while I was still typing!") from _call_mail_function_39
    yui "\"Sorry, Sable jumped on me so I sent that one while I was still typing!\""
    "I didn't even have time to think about that before her next message came."
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    voice "audio/voice/E2/YUI/04/YI/YI001.ogg"
    call mail_function("yui", "yui", "", "Sable's been rolling around a lot recently. Maybe he's growing his winter fur?") from _call_mail_function_40
    yui "\"Sable's been rolling around a lot recently. Maybe he's growing his winter fur?\""
    voice "audio/voice/E2/YUI/04/HA/HA000.ogg"
    hachiman "How am I supposed to know? Let's see... \"My cat's been curling up, too. Isn't that what they usually do around winter?\" ...There."
    play sound "audio/sfx/SE03/SE03_02.ogg"
    call mail_function("yui", "hachiman", "Re:", "My cat's been curling up, too. Isn't that what they usually do around winter?") from _call_mail_function_41
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    voice "audio/voice/E2/YUI/04/YI/YI002.ogg"
    call mail_function("yui", "yui", "Re2:", "Yep, yep!") from _call_mail_function_42
    yui "\"Yep, yep!\""
    hachiman "(She really manages bang out these messages out lightning fast.)"
    hachiman "(And am I supposed to reply to this? I don't really get where I should end the conversation...)"
    show komachi athletic mid_center vhappy at center with dissolve:
        xoffset -35 yoffset 70
    voice "audio/voice/E2/YUI/04/KO/KO000.ogg"
    komachi "Sa~y, Onii-chan, who're you texting? Is it Yukino-san? or maybe Yui-san?"
    call mail_clear from _call_mail_clear_6
    show black with dissolve:
        alpha 0
    voice "audio/voice/E2/YUI/04/HA/HA001.ogg"
    hachiman "..."
    "Komachi nods with a grin on her face."
    voice "audio/voice/E2/YUI/04/HA/HA002.ogg"
    hachiman "Did you need something, Komachi-chan?"
    voice "audio/voice/E2/YUI/04/KO/KO001.ogg"
    komachi "Nothing at all. Komachi'll be moonwalking outta here! That show of consideration was high in Komachi points! Night!"
    hide komachi with dissolve
    hachiman "(I feel like she saw a super embarrassing side of me...)"
    call mail_clear from _call_mail_clear_7
    show black with dissolve:
        alpha 0.3
    play sound "<from 0 to 0.5>audio/sfx/SE03/SE03_00L.ogg"
    voice "audio/voice/E2/YUI/04/YI/YI003.ogg"
    call mail_function("yui", "yui", "", "I'm gonna go take a bath soon, so good night!") from _call_mail_function_43
    yui "\"I'm gonna go take a bath soon, so good night!\""
    play sound "audio/sfx/SE03/SE03_02.ogg"
    voice "audio/voice/E2/YUI/04/HA/HA003.ogg"
    call mail_function("yui", "hachiman", "Re:", "Good night.") from _call_mail_function_44
    hachiman "\"Good night.\""
    hachiman "(Send... Wait, did you really have to tell me that? It's embarrassing!)"
    hachiman "(Do people normally talk about stupid things like that?)"
    hachiman "(It's even weirder when it's done via text. What's more, if someone catches you leaving them on read without replying immedietly, you'll get bullied for it! It's terrifying!)"
    "Although... it was kinda fun having a silly exchange like that with Yuigahama."
    call mail_clear from _call_mail_clear_8
    stop music fadeout 1.0
    window auto hide dissolve
    jump E3_CMM_01

#label E2_YUI_05:
