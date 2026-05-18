label E3_SAK_01:
    play music "audio/bgm/BGM14.ogg"
    show saki school mid_left pout at center with dissolve:
        xoffset 65 yoffset 75
    voice "audio/voice/E3/SAK/01/SA/SA000.ogg"
    saki "............."
    "I looked up and saw Kawasaki stand beside me, glancing in my direction."
    voice "audio/voice/E3/SAK/01/HA/HA000.ogg"
    hachiman "Yo..."
    show saki surprised at center, Shake(None, 0.2, dist=20)
    show saki pout with dissolve
    voice "audio/voice/E3/SAK/01/SA/SA001.ogg"
    saki "Ah! No, this is..."
    hachiman "(She's changed recently... she seems to get nervous quite often lately. She used to be the tough-looking type, so isn't that weird?)"
    "There was no point in playing detective, so I let it slip my mind."
    voice "audio/voice/E3/SAK/01/HA/HA001.ogg"
    hachiman "Did you need something?"
    show saki school mid_right angry at center with dissolve:
        xoffset -120 yoffset 75
    voice "audio/voice/E3/SAK/01/SA/SA002.ogg"
    saki "Here, I want you to give this to Komachi-chan."
    "Saki offered a small package that read \"To: Komachi\", so I accepted it obediently."
    show saki blush with dissolve
    voice "audio/voice/E3/SAK/01/SA/SA003.ogg"
    saki "I-I wanted to thank you for winter break. I know it's nothing fancy, but you have my gratitude."
    voice "audio/voice/E3/SAK/01/HA/HA002.ogg"
    hachiman "O-Oh, I see. Thanks."
    voice "audio/voice/E3/SAK/01/HA/HA003.ogg"
    hachiman "I should be thanking you too. You treated us to dinner."
    voice "audio/voice/E3/SAK/01/SA/SA004.ogg"
    saki "D-Don't sweat it. Later..."
    hide saki with dissolve
    stop music fadeout 1.0
    "Perhaps she was worried about the eyes watching her, but Saki left as soon as she handed over the package."
    "Wait, am I upset that she was rushing because she didn't want to be seen talking to me? My powers of observation are so great, I uncovered yet another truth."
    voice "audio/voice/E3/SAK/01/XI/XI000.ogg"
    sgB "Anyway, you know what? Maybe Yukinoshita-san doesn't bother deciding between sciences and humanities, she's capable of whatever, right? She can probably afford to date someone from a "
    voice sustain
    sgB "different class even with exams coming up."
    voice "audio/voice/E3/SAK/01/XK/XK000.ogg"
    sgC "You can say that again! She's got the brains so it's not like she has to cram for the exams or anything."
    hachiman "(Well, nobody noticed my short exchange with Kawasaki, right? We didn't really stand out that much... Hm?)"
    show saki school far_right angry at center:
        xoffset -325 yoffset 75
    show yumiko school far_left unimpressed at center:
        xoffset 240 yoffset 75
    with dissolve
    voice "audio/voice/E3/SAK/01/YM/YM000.ogg"
    yumiko "Hey, I want to go over there. Can you move out of the way?"
    voice "audio/voice/E3/SAK/01/SA/SA005.ogg"
    saki "Ha? Aren't you the one blocking my way?"
    show yumiko angry with dissolve
    show yumiko:
        linear 0.2 xoffset 200
        linear 0.2 xoffset 240
    voice "audio/voice/E3/SAK/01/YM/YM001.ogg"
    yumiko "Ha?"
    show saki annoyed with dissolve
    show saki:
        linear 0.2 xoffset -285
        linear 0.2 xoffset -325
    voice "audio/voice/E3/SAK/01/SA/SA006.ogg"
    saki "Ha?"
    hachiman "(Woah... Kawasaki-san is scary after all.)"
    window auto hide dissolve
    call loading_screen(duration="short") from _call_general_loading_1
    scene hallwayA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM12.ogg"
    show yui school mid_center pout at center with dissolve:
        xoffset -25 yoffset 75
    window auto show dissolve
    voice "audio/voice/E3/SAK/01/YI/YI000.ogg"
    yui "Yukinon, I wonder if she's okay..."
    voice "audio/voice/E3/SAK/01/HA/HA004.ogg"
    hachiman "Well, you can worry about it after you meet her."
    show yui happy with dissolve
    voice "audio/voice/E3/SAK/01/YI/YI001.ogg"
    yui "Yeah... That's true."
    show yui blush with dissolve
    voice "audio/voice/E3/SAK/01/YI/YI002.ogg"
    yui "By the way..."
    voice "audio/voice/E3/SAK/01/HA/HA005.ogg"
    hachiman "Hmm?"
    show yui happy with dissolve
    voice "audio/voice/E3/SAK/01/YI/YI003.ogg"
    yui "Weren't you talking with Saki earlier about something?"
    voice "audio/voice/E3/SAK/01/HA/HA006.ogg"
    hachiman "Oh. You saw that?"
    show yui pout with dissolve
    voice "audio/voice/E3/SAK/01/YI/YI004.ogg"
    yui "Huh? It's not like I was interested or looking . I just happened to see it, it was kinda in my line of sight, or in my blind spot? It seemed like you got something from her..."
    hachiman "(You won't be able to see me if I was in your blind spot...)"
    voice "audio/voice/E3/SAK/01/HA/HA007.ogg"
    hachiman "Oh, yeah. She was thanking me for the winter break."
    show yui surprised with dissolve
    voice "audio/voice/E3/SAK/01/YI/YI005.ogg"
    yui "Eh! Hikki, did something happen between you and Saki over winter break?"
    voice "audio/voice/E3/SAK/01/HA/HA008.ogg"
    hachiman "It's nothing. I just helped Komachi and Kawasaki's brother study for their exams."
    show yui happy with dissolve
    voice "audio/voice/E3/SAK/01/YI/YI006.ogg"
    yui "Hmm. I see."
    show yui pout with dissolve
    voice "audio/voice/E3/SAK/01/YI/YI007.ogg"
    yui "I should have gone too. My grades are not that good."
    voice "audio/voice/E3/SAK/01/HA/HA009.ogg"
    hachiman " You're not on the high school entrance exam, you know."
    show yui happy with dissolve
    voice "audio/voice/E3/SAK/01/YI/YI008.ogg"
    yui "Oh, I see. I was a little nervous, since we were handed out our future career prospects. Hahaha..."
    hachiman "(That's right. I was completely distracted by Komachi's high school entrance exams, but we will be taking the exam next year too... Perhaps Yuigahama-san should start over from the high school "
    hachiman "entrance exams. Hmm. Yes.)"
    window auto hide dissolve
    stop music fadeout 1.0
    call loading_screen(5, "33") from _call_loading_screen_4
    jump E3_CMM_06

label E3_SAK_02:
    hachiman "(I made her wait for too long... Perhaps I should approach her now and say something.)"
    window auto hide dissolve
    show sakiHallwayb with Dissolve(1.0)
    window auto show dissolve
    voice "audio/voice/E3/SAK/02/HA/HA000.ogg"
    hachiman "Hey, we're about start pretty soon."
    window auto hide dissolve
    stop voice
    hide sakiHallwayb
    show saki school_sunset mid_right surprised at center:
        xoffset -115 yoffset 75
    with dissolve
    play music "audio/bgm/BGM14.ogg"
    window auto show dissolve
    "Kawasaki's got a surprised look on her face as she turned away her phone. I bet she was mailing Taishi."
    "It might not have been the best idea to approach her as I was getting a bit scared..."
    show saki pout with dissolve
    voice "audio/voice/E3/SAK/02/SA/SA000.ogg"
    saki "Huh? Oh, got it."
    "After answering, Kawasaki hastily hid the phone into her pocket. Does this mean she's allowing me to continue the conversation?"
    voice "audio/voice/E3/SAK/02/HA/HA001.ogg"
    hachiman "You came here for the career counseling, right?"
    voice "audio/voice/E3/SAK/02/SA/SA001.ogg"
    saki "P-Pretty much... are you here for that as well?"
    voice "audio/voice/E3/SAK/02/HA/HA002.ogg"
    hachiman "No, I was just asked to help with the preparations. And speaking of which... You're seeking career guidance? I don't think you really need any."
    show saki happy with dissolve
    voice "audio/voice/E3/SAK/02/SA/SA002.ogg"
    saki "It's less about seeking career guidance, but securing my scholarship in advance by double-checking my grades and such."
    hachiman "(Kawasaki-san, you're really remarkable as expected.)"
    voice "audio/voice/E3/SAK/02/HA/HA003.ogg"
    hachiman "Well if it's you we're talking about, I'm sure everything will be fine."
    show saki blush with dissolve
    voice "audio/voice/E3/SAK/02/SA/SA003.ogg"
    saki "Y-You think so? I hope so too."
    "Kawasaki suddenly smiled in a timid manner. I think she's better off having this gentle look all the time."
    hachiman "(Well, having a sharp look is cool too... if only it doesn't intimidate people.)"
    show saki happy with dissolve
    voice "audio/voice/E3/SAK/02/SA/SA004.ogg"
    saki "How about you, what's your course?"
    voice "audio/voice/E3/SAK/02/HA/HA004.ogg"
    hachiman "Ah, I wish to become stay-at-home dad."
    show saki vhappy with dissolve
    voice "audio/voice/E3/SAK/02/SA/SA005.ogg"
    saki "Hah, what's with that?"
    show saki angry with dissolve
    voice "audio/voice/E3/SAK/02/SA/SA006.ogg"
    saki "It's alright if you're serious of being a stay-at-home dad, but then how are you going to support someone's family?"
    voice "audio/voice/E3/SAK/02/HA/HA005.ogg"
    hachiman "Ugh."
    show saki surprised with dissolve
    voice "audio/voice/E3/SAK/02/SA/SA007.ogg"
    saki "N-Nevermind, I just thought since I have a lot of family members, and our parents have been working very hard. It was just a sarcastic remark, so don't think much of it."
    voice "audio/voice/E3/SAK/02/HA/HA006.ogg"
    hachiman "A-Ahh... my parents are both working too."
    hachiman "(Come to think of it, I helped out with washing the dishes and other chores at Kawasaki's house... I didn't expect to enjoy any of that.)"
    voice "audio/voice/E3/SAK/02/HA/HA007.ogg"
    hachiman "I definitely can't cook as much as you do, maybe I'm not fit for being a househusband after all."
    hachiman "(Hm? I should be thinking that a stay-at-home dad is someone who lives happily while receiving support and being dependent... But whatever.)"
    show saki happy with dissolve
    voice "audio/voice/E3/SAK/02/SA/SA008.ogg"
    saki "Maybe it's not as easy as you think it is? There's nothing in particular great about me, considering my years of experience."
    voice "audio/voice/E3/SAK/02/HA/HA008.ogg"
    hachiman "You do seem to have lots of cooking experience."
    show saki sad with dissolve
    voice "audio/voice/E3/SAK/02/SA/SA009.ogg"
    saki "My parents are busy... I want to lend them a hand, even just a bit. I want to make sure my younger siblings are eating properly."
    voice "audio/voice/E3/SAK/02/HA/HA009.ogg"
    hachiman "You're amazing."
    show saki blush with dissolve
    voice "audio/voice/E3/SAK/02/SA/SA010.ogg"
    saki "Eh? Ah... um... you think so?"
    voice "audio/voice/E3/SAK/02/HA/HA010.ogg"
    hachiman "By the way, Komachi's really happy about the stuff you gave me the other day. I also ate some and it's really delicious."
    "The tiny gift she handed over as gratitude for winter break was a handmade ohagi rice ball."
    "It's very really like Kawasaki to make such cozily packaged sweets."
    voice "audio/voice/E3/SAK/02/SA/SA011.ogg"
    saki "A-Ah, so you ate some too... I see. I'm glad then."
    voice "audio/voice/E3/SAK/02/HA/HA011.ogg"
    hachiman "............."
    voice "audio/voice/E3/SAK/02/SA/SA012.ogg"
    saki "............."
    show saki angry with dissolve
    voice "audio/voice/E3/SAK/02/SA/SA013.ogg"
    saki " By the way, are you free this weekend?"
    hachiman "(Is this about teaching Taishi for the entrance exams again? Komachi never mentioned anything.)"
    voice "audio/voice/E3/SAK/02/HA/HA012.ogg"
    hachiman "Sure. Is something up?"
    show saki blush with dissolve
    voice "audio/voice/E3/SAK/02/SA/SA014.ogg"
    saki "Keika said she wanted to play with you... So if you're cool with it, do you want to go hang out outside?"
    voice "audio/voice/E3/SAK/02/HA/HA013.ogg"
    hachiman "I-I see... Uhh my weekend is..."
    "With this sudden development, I pretended to think if I have plans for the weekend..."
    menu E3_SAK_02_menu:
        hachiman "(What should I do... Should I go with Kawasaki this weekend?)"
        with dissolve
        "I'll go outside with her":
            "(Well I have nothing in particular to do, so...)"
            voice "audio/voice/E3/SAK/02/HA/HA014.ogg"
            hachiman "O-Okay, if it's Kei-chan's request, then it can't be helped..."
            voice "audio/voice/E3/SAK/02/SA/SA015.ogg"
            saki "Sorry about that. Thanks."
            voice "audio/voice/E3/SAK/02/HA/HA015.ogg"
            hachiman "S-Sure..."
            "The area around the conference room and hallway began to get louder. Apparently the consultation meetings were about to begin."
            voice "audio/voice/E3/SAK/02/SA/SA018.ogg"
            saki "I-I'll be going now then. See you."
            voice "audio/voice/E3/SAK/02/HA/HA019.ogg"
            hachiman "Right. I hope their counseling helps."
            show saki vhappy with dissolve
            voice "audio/voice/E3/SAK/02/SA/SA019.ogg"
            saki "Yeah."
            hide saki with dissolve
            "As I watch Kawasaki's figure enter the guidance counseling room, I unusually gave more serious thought to my own future."
            hachiman "(Pick a course, huh...)"
            window auto hide dissolve
            stop music fadeout 1.0
            if shrineMeetFlag == "saki":
                $totsukaTalkFlag = "saki"
            jump E3_CMM_07        
        "Don't go outside":
            "not finished"
            jump E3_SAK_02_menu

label E3_SAK_03:
    scene waterPark
    show sakiDate
    with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/BGM07.ogg"
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E3/SAK/03/KE/KE000.ogg"
    keika "Saa-chan, Haa-chan, it's penguin-san!"
    voice "audio/voice/E3/SAK/03/SA/SA000.ogg"
    saki "Kei-chan, If you run like that you'll fall!"
    voice "audio/voice/E3/SAK/03/KE/KE001.ogg"
    keika "Ehh? Penguin-san is running away?"
    voice "audio/voice/E3/SAK/03/SA/SA001.ogg"
    saki "If you suddenly approach penguin-san, he'll be surprised, too. Kei-chan, why don't you try to approach more gently?"
    voice "audio/voice/E3/SAK/03/KE/KE002.ogg"
    keika "O-Okay!"
    "Keika did what Kawasaki advised and slowly approached the penguin. Kawasaki watched over Keika with a fond smile on her face."
    hachiman "(What a heartwarming sight...)"
    window auto hide dissolve
    hide sakiDate with dissolve
    window auto show dissolve
    "This weekend was my appointment with Kawasaki. She brought me along to an aquarium. No, perhaps it would be more accurate to say my appointment with Keika, who brought along Kawasaki?"
    show saki coat mid_left blush at center with dissolve:
        xoffset 65 yoffset 75
    voice "audio/voice/E3/SAK/03/SA/SA002.ogg"
    saki "I'm sorry to make you keep us company like this."
    show saki:
        parallel:
            2.0
            linear 0.3 alpha 0
    voice "audio/voice/E3/SAK/03/HA/HA000.ogg"
    hachiman "No, I'm free today so... Oh--"
    hide saki
    "Just as another penguin was approaching, I saw Keika slip and lose her balance, so I rushed over to her."
    window auto hide dissolve
    play sound "audio/sfx/SE00/SE00_28.ogg"
    show keika heavy_coat near surprised at center with Fade(0.1, 0.15, 0.5, color="#fff"):
        xoffset -30 yoffset 75
    window auto show dissolve
    voice "audio/voice/E3/SAK/03/KE/KE003.ogg"
    keika "Ahh, Haa-chan?"
    hachiman "(Whoah... I was just in time...)"
    voice "audio/voice/E3/SAK/03/HA/HA001.ogg"
    hachiman "You should be careful or you might get hurt, Kei-chan."
    voice "audio/voice/E3/SAK/03/KE/KE004.ogg"
    show keika vhappy with dissolve
    keika "Haah... Haa-chan came within a hair's breadth!"
    voice "audio/voice/E3/SAK/03/HA/HA002.ogg"
    hachiman "You know some hard words, Kei-chan."
    hachiman "(This girl has a lot of potential, doesn't she?)"
    voice "audio/voice/E3/SAK/03/KE/KE005.ogg"
    show keika happy with dissolve
    keika "Is Keika smart?"
    voice "audio/voice/E3/SAK/03/HA/HA003.ogg"
    hachiman "Yeah, very, very smart."
    voice "audio/voice/E3/SAK/03/SA/SA003.ogg"
    saki "Hey now, Kei-chan."
    window auto hide dissolve
    stop voice
    hide keika
    show sakiDate
    with dissolve
    window auto show dissolve
    "Saki, who had been watching the situation anxiously, finally interjected."
    hachiman "(Ah, I think I went a bit overboard with that save...)"
    voice "audio/voice/E3/SAK/03/SA/SA004.ogg"
    saki "If you cause too much trouble for Haa-chan, he might not like you anymore, okay?"
    voice "audio/voice/E3/SAK/03/KE/KE006.ogg"
    keika "Ehh... Haa-chan, do you not like Keika?"
    voice "audio/voice/E3/SAK/03/HA/HA004.ogg"
    hachiman "That's not true!"
    "Because of my perfect brother attributes, I'm almost too sweet."
    voice "audio/voice/E3/SAK/03/HA/HA005.ogg"
    hachiman "It's alright, Kei-chan is my friend after all."
    voice "audio/voice/E3/SAK/03/KE/KE007.ogg"
    keika "Ehh? Keika doesn't want you to be a friend!"
    hachiman "(Huh, even this little girl doesn't like me...)"
    voice "audio/voice/E3/SAK/03/KE/KE008.ogg"
    keika "Haa-chan and Saa-chan are like papa and mama. That's why I like Haa-chan better as my papa."
    voice "audio/voice/E3/SAK/03/MI/MIX000.ogg"
    hachiandsaki "Huh!?"
    hachiman "(I'm pretty sure she's said that before...)"
    window auto hide dissolve
    hide sakiDate
    show saki coat near_right happy at center:
        xoffset -150 yoffset 75
    with dissolve
    window auto show dissolve
    "I couldn't help but look at Kawasaki next to me and our faces were closer than I thought."
    show saki surprised with dissolve
    voice "audio/voice/E3/SAK/03/MI/MIX001.ogg"
    hachiandsaki "Whoa..."
    show saki coat near_left blush at center with dissolve:
        xoffset 175 yoffset 85
    "We both turned our heads away in a panic."
    hachiman "(This is also something I've noticed before. I mean, Kawasaki's eyelashes are pretty long...)"
    window auto hide dissolve
    hide saki
    show sakiDate
    with dissolve
    window auto show dissolve
    voice "audio/voice/E3/SAK/03/KE/KE009.ogg"
    keika "Haa-chan and Saa-chan are turning red!"
    voice "audio/voice/E3/SAK/03/SA/SA007.ogg"
    saki "K-Kei-chan. D-Don't say weird things."
    hachiman "(I think this girl is a little she-devil by nature...)"
    voice "audio/voice/E3/SAK/03/HA/HA008.ogg"
    hachiman "Hey. I'm gonna poke your cheeks."
    voice "audio/voice/E3/SAK/03/KE/KE010.ogg"
    keika "Ahaha! Haa-chan is bullying me! Payback! there!"
    voice "audio/voice/E3/SAK/03/HA/HA009.ogg"
    hachiman "Ohh, you've done it now!"
    voice "audio/voice/E3/SAK/03/SA/SA008.ogg"
    saki "............"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    scene aquarium
    show saki coat_blue mid_right vhappy at center:
        xoffset -325 yoffset 75
    show keika heavy_coat_blue mid surprised at center:
        xoffset 245 yoffset 75
    with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/BGM41.ogg"
    window auto show dissolve
    voice "audio/voice/E3/SAK/03/KE/KE011.ogg"
    keika "Woah, a big fish!"
    voice "audio/voice/E3/SAK/03/HA/HA010.ogg"
    hachiman "Right? It's so big."
    show keika vhappy with dissolve
    voice "audio/voice/E3/SAK/03/KE/KE012.ogg"
    keika "Yummy!"
    voice "audio/voice/E3/SAK/03/HA/HA011.ogg"
    hachiman "O-oh, 'yummy' you say?"
    show keika happy with dissolve
    voice "audio/voice/E3/SAK/03/KE/KE013.ogg"
    keika "Ah, it's a Jellyfish, wobble~wobble!"
    hide keika with dissolve
    "Upon discovering the jellyfish corner, Keika happily rushed to it and was fascinated by their every move."
    hide saki with dissolve
    show saki coat_blue mid_right vhappy at center with dissolve:
        xoffset -85 yoffset 75
    voice "audio/voice/E3/SAK/03/HA/HA012.ogg"
    hachiman "Kei-chan's a real animal lover."
    voice "audio/voice/E3/SAK/03/SA/SA009.ogg"
    saki "You're really good at handling kids."
    voice "audio/voice/E3/SAK/03/HA/HA013.ogg"
    hachiman "It's because I'm good with anything classified under \"little sister\"."
    "I was so embarrassed by Kawasaki's words that I answered bluntly, and I heard her give a small laugh."
    show saki blush with dissolve
    voice "audio/voice/E3/SAK/03/SA/SA010.ogg"
    saki "Umm... Will you play with her again sometime?"
    voice "audio/voice/E3/SAK/03/HA/HA014.ogg"
    hachiman "...Well, if you're alright with me."
    window auto hide dissolve
    stop voice
    call loading_screen(6) from _call_saki_coat_loading
    jump E3_CMM_08

label E3_SAK_05:
    scene houseA with fade
    play music "audio/bgm/BGM10.ogg"
    window auto show dissolve
    "After breakfast, I cleaned up quickly, and Komachi and I moved to the sofa with a mug in one hand."
    window auto hide dissolve
    scene houseA:
        zoom 2.0 xalign 1.0 ypos -600
    show komachi athletic near_center happy at center:
        xoffset 35 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E3/SAK/05/HA/HA000.ogg"
    hachiman "I should've told you before, but I've been having a hard time since the start of the new semester."
    "I told Komachi about the alleged relationship between Yukinoshita and Hayama, and the fuss over the whole career prospect thing in detail."
    "When I talk about it out loud, I feel like we've been swept up in very petty problems."
    voice "audio/voice/E3/SAK/05/HA/HA001.ogg"
    hachiman "Well, it doesn't matter now that it's over..."
    show komachi angry with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO000.ogg"
    komachi "...Hmm. So that's what happened. But I somehow knew it was going to be tough, I guess."
    voice "audio/voice/E3/SAK/05/HA/HA002.ogg"
    hachiman "You knew about all that?"
    show komachi happy with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO001.ogg"
    komachi "If I didn't, I wouldn't be my big bro's little sister. Was that high in Komachi points?"
    voice "audio/voice/E3/SAK/05/HA/HA003.ogg"
    hachiman "That goes without saying."
    "Then we joked around for a bit, and when the laughter died down, Komachi said:"
    show komachi unimpressed with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO002.ogg"
    komachi "Well, there are a lot of people around you who seem to have troublesome circumstances, aren't there, onii-chan?"
    voice "audio/voice/E3/SAK/05/HA/HA004.ogg"
    hachiman "Well, it mostly revolves around this Hayama guy... Do you remember him?"
    show komachi happy with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO003.ogg"
    komachi "Isn't he that overly cheery guy? We met at summer camp, right?"
    voice "audio/voice/E3/SAK/05/HA/HA005.ogg"
    hachiman "............"
    hachiman "(She just straight up called him \"overly cheery\"...! Accurate, but what a scary thing to say. Girls are cruel!)"
    show komachi surprised with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO004.ogg"
    komachi "Onii-chan are you okay? Did I say something strange?"
    voice "audio/voice/E3/SAK/05/HA/HA006.ogg"
    hachiman "No... no. Nothing strange. You're right infact."
    show komachi pout with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO005.ogg"
    komachi "...? Yeah? I mean..."
    show komachi angry with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO006.ogg"
    komachi "I think that your career path isn't something that you should decide on because of what other people say about you. It's your life, you know."
    voice "audio/voice/E3/SAK/05/HA/HA007.ogg"
    hachiman "I completely agree with you on that."
    hachiman "(As to be expected from THE little sister of the world. That's not easy for a junior high schooler to say.)"
    voice "audio/voice/E3/SAK/05/KO/KO007.ogg"
    komachi "I have a solid life plan for myself."
    voice "audio/voice/E3/SAK/05/HA/HA008.ogg"
    hachiman "Huh? Is that right? Want to tell onii-chan?"
    show komachi happy with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO008.ogg"
    komachi "That's a secret. How about you, onii-chan?"
    voice "audio/voice/E3/SAK/05/HA/HA009.ogg"
    hachiman "Ah, stay-at-home dad of course."
    show komachi unimpressed with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO009.ogg"
    komachi "I was kind of hoping you'd come up with a different answer..."
    voice "audio/voice/E3/SAK/05/HA/HA010.ogg"
    hachiman "You think I'm giving up on that dream easily? Dreams are not meant to be dreamt, but to be fulfilled. I need not lose focus and stay confident on my path towards my dream."
    show komachi angry with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO010.ogg"
    komachi "Whatever floats your boat. By the way Onii-chan, I do have a feeling you've changed a bit, like you've become a little more serious about your life."
    voice "audio/voice/E3/SAK/05/HA/HA011.ogg"
    hachiman "Hey now, I've always been serious. And yeah, something's really about to change. In order to become a splendid househusband, I must be able
        to cook at the very least."
    window auto hide dissolve
    stop voice
    scene saki_houseB
    show saki home_light_sunset mid_right happy at left:
        xoffset -25 yoffset 75
    show komachi home_sunset mid_center happy at right:
        xoffset -200 yoffset 75
    show keika home_sunset mid happy at left:
        xoffset 410 yoffset 75
    with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    # need to add some shaded sakis house flashback here -_-
    "I won't say the peace and harmony showed by Kawasaki's family somehow influenced me, that'll be embarassing. However I really think it prefaced a massive shift in my consciousness."
    window auto hide dissolve
    scene houseA:
        zoom 2.0 xalign 1.0 ypos -600
    show komachi athletic near_center unimpressed at center:
        xoffset 35 yoffset 75
    with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    "--But, instead of being impressed, Komachi just gave a big sigh."
    voice "audio/voice/E3/SAK/05/KO/KO011.ogg"
    komachi "Well, maybe you've changed a bit, but... you haven't really changed at all. Komachi's tired of worrying about you, you know..."
    show komachi happy with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO012.ogg"
    komachi "Well, there's no point in discussing dreams with someone like onii-chan."
    "It's not like I haven't thought about the future at all, but Komachi sure has a lot to say about it."
    "But for example, \"I want to be something\" is as close to dreamy as you can get, while \"I want to be in some industry\" is something else entirely."
    window auto hide dissolve
    scene hallwayA
    show totsuka athletic mid_center happy at center:
        xoffset 10 yoffset 75
    with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    hachiman "(Unless you're a responsible guy like Totsuka who's steadily moving towards his dream or who has a certain path in mind, there aren't many people who have that kind of concrete vision for the future right "
    hachiman "now.)"
    hachiman "(It's not like the world is made up of only reliable guys like that to begin with.)"
    window auto hide dissolve
    scene houseA:
        zoom 2.0 xalign 1.0 ypos -600
    show komachi athletic near_center happy at center:
        xoffset 35 yoffset 75
    with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    voice "audio/voice/E3/SAK/05/HA/HA013.ogg"
    hachiman "The idea that everyone has to have a dream in the first place is ridiculous."
    "Maybe it was because I was with Komachi that I was able saying things without thinking."
    show komachi unimpressed with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO013.ogg"
    komachi "Right, right, Trashnii-chan, Trashnii-chan. In my brain, I can already see a future where I'd be taking care of you in your old age and listening to your spitful monologues like I do now."
    "It's just getting worse and worse, so I forced the conversation back on track."
    voice "audio/voice/E3/SAK/05/HA/HA014.ogg"
    hachiman "No, I agree that Komachi will take care of me in my old age, but instead of being hateful, I'm going to brag to my grandchildren about my saga in high school."
    voice "audio/voice/E3/SAK/05/HA/HA015.ogg"
    hachiman "Well, I'm not talking about myself here, but after high school, family situations really come into play. Hayama and Yukinoshita will have a hard time."
    show komachi pout with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO014.ogg"
    komachi "I agree I have take care of you in your old age. Komachi wouldn't be able to pay attention to her family when she has onii-chan to worry about. I want a strong sister-in-law..."
    voice "audio/voice/E3/SAK/05/HA/HA016.ogg"
    hachiman "Don't ask for what you can't have, Komachi."
    show komachi happy with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO015.ogg"
    komachi "Speaking of older sister... Saki, she's a solid one! I wonder what she's going to do in the future!"
    voice "audio/voice/E3/SAK/05/HA/HA017.ogg"
    hachiman "Wait, what? Wait. I don't follow, what's the connection between my old age... and Kawa...er...what was it..."
    show komachi unimpressed with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO016.ogg"
    komachi "It's Kawasaki-san, onii-chan. They've been helping us out, so at least remember the name."
    "It's not that I didn't really remember it. I was just a little embarrassed. It's probably because I feel like we've suddenly grown closer over the winter break. I feel self-conscious all of a sudden."
    voice "audio/voice/E3/SAK/05/HA/HA018.ogg"
    hachiman "...Well, Kawasaki has a lot of siblings, so it seems she might have trouble getting into college..."
    voice "audio/voice/E3/SAK/05/HA/HA019.ogg"
    hachiman "As for me, I'm trying to make it work, and I've decided on a career path, so I'm set."
    show komachi vhappy with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO017.ogg"
    komachi "You're aiming for a scholarship, aren't you? You're like Saki-san, a hard worker! And actually, she's kind and good at cooking, too!"
    hachiman "(You're observant, Komachi. I mean, is it relevant that she's a good cook in the current context? No, I mean, she is, but...)"
    show komachi happy with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO018.ogg"
    komachi "I'd be so relieved if I had someone like that to take care of onii-chan."
    voice "audio/voice/E3/SAK/05/HA/HA020.ogg"
    hachiman "H-Hey. Don't mock my dream of being a stay-at-home dad."
    show komachi unimpressed with dissolve
    voice "audio/voice/E3/SAK/05/KO/KO019.ogg"
    komachi "It's just a joke, of course. Saki-san would never take my brother off my hands. So take your life seriously."
    voice "audio/voice/E3/SAK/05/HA/HA021.ogg"
    hachiman "I'll do my best..."
    "Regardless of the future, I feel a little better after a trivial talk with Komachi."
    "Maybe it's partly because we're siblings that we don't have to walk on eggshells around each other, but when I'm with Komachi, I can't help but want to talk to her."
    "I don't want to worry my sister right when she has exams to take, so I should at least solve the mess at school by myself."
    window auto hide dissolve
    call loading_screen(5) from _call_saki_school_loading
    jump E4_CMM_01