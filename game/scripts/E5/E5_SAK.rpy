label E5_SAK_01:
    scene houseCB with Fade(1.0, 0.5, 1.0)
    "Finally, the day of Komachi's exams is here. Unfortunately, it's snowing today."
    show komachi school mid_center angry at center with dissolve:
        xoffset -75 yoffset 75
    play music "audio/bgm/BGM09.ogg"
    voice "audio/voice/E5/SAK/01/KO/KO000.ogg"
    komachi "Then... off I go!"
    voice "audio/voice/E5/SAK/01/HA/HA000.ogg"
    hachiman "Yeah, just keep calm."
    voice "audio/voice/E5/SAK/01/HA/HA001.ogg"
    hachiman "Yuigahama and the others are cheering you on. Here."
    "I show Komachi a picture of Yuigahama and Yukinoshita, who apparently had a sleepover after yesterday's tasting event. \"I'm rooting for you!\" is the message attached to it."
    "Looking at Sable in the background, it must be Yuigahama's house."
    show komachi vhappy with dissolve
    voice "audio/voice/E5/SAK/01/KO/KO001.ogg"
    komachi "Yeah. I got a gift too from Taishi-kun, Saki-san said she supports me. This kind of thing is reassuring, isn't it?"
    hachiman "(You were in contact with Taishi the day before...)"
    "...but I don't have the same mild irritation as before. It's because it has become a part of my daily life. The image of the two of them puzzling
        over the problems side by side comes to mind."
    "Now, I honestly think they should both do their best. My beloved sister, and my sister's friend who is like a brother to me."
    voice "audio/voice/E5/SAK/01/HA/HA002.ogg"
    hachiman "I've told you many times, you'll be fine."
    show komachi happy with dissolve
    voice "audio/voice/E5/SAK/01/KO/KO002.ogg"
    komachi "Yeah... Here I go then!"
    voice "audio/voice/E5/SAK/01/HA/HA003.ogg"
    hachiman "Yep. Take care."
    window auto hide dissolve
    stop voice
    # sfx here
    hide komachi with dissolve
    play sound "audio/sfx/SE04/SE04_06.ogg"
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    "I stare at the living room for a moment after Komachi left me with a light wave of her hand."
    hachiman "(I understand there's only so much I can do for those around me, and it's up to Komachi to shape her future after the exam. However, if I'm in Komachi's shoes right now, there's no way I would be able to stay "
    hachiman "calm.)"
    window auto hide dissolve
    play sound ["<silence 1.0>", "audio/sfx/SE00/SE00_25.ogg"]
    scene gatesE with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    hachiman "(I ended up outside my school, waiting for Komachi after all.)"
    "The exams had already started, so there was no one near the school gate. There were traces of students stepping on the snow all the way to the school building, with a light layer of snow on top of it."
    hachiman "(I hope hope she's doing well...)"
    stop music
    play sound "audio/sfx/SE00/SE00_25.ogg"
    hachiman "(Hm?)"
    stop sound
    voice "audio/voice/E5/SAK/01/SA/SA000.ogg"
    mystery "Ah--"
    show saki school_dark mid_right happy at center with dissolve:
        xoffset -115 yoffset 75
    play music "audio/bgm/BGM14.ogg"
    voice "audio/voice/E5/SAK/01/HA/HA004.ogg"
    hachiman "Yo."
    voice "audio/voice/E5/SAK/01/SA/SA001.ogg"
    saki "So you came too."
    voice "audio/voice/E5/SAK/01/HA/HA005.ogg"
    hachiman "There's nothing to do at home."
    show saki blush with dissolve
    voice "audio/voice/E5/SAK/01/SA/SA002.ogg"
    saki "I... I guess you're right."
    voice "audio/voice/E5/SAK/01/HA/HA006.ogg"
    hachiman "............"
    show saki pout with dissolve
    voice "audio/voice/E5/SAK/01/SA/SA003.ogg"
    saki "............"
    voice "audio/voice/E5/SAK/01/HA/HA007.ogg"
    hachiman "You baby your brother too much, you know."
    show saki angry with dissolve
    voice "audio/voice/E5/SAK/01/SA/SA004.ogg"
    saki "I don't want to hear that from someone who's the same for his sister."
    show saki vhappy with dissolve
    voice "audio/voice/E5/SAK/01/MI/MIX000.ogg"
    hachiandsaki "............"
    "Since neither of us couldn't bear staying behind during our siblings' exam day, we're pretty much the same."
    voice "audio/voice/E5/SAK/01/HA/HA009.ogg"
    hachiman "By the way, Komachi said she's really happy because of the encouragement you've given via Taishi's mail."
    show saki blush with dissolve
    voice "audio/voice/E5/SAK/01/SA/SA006.ogg"
    saki "Ah. We're schoolmates, so we should cheer each other on."
    voice "audio/voice/E5/SAK/01/HA/HA010.ogg"
    hachiman "I see."
    "I don't remember doing anything in particular to encourage them, so that kind of surprised me."
    voice "audio/voice/E5/SAK/01/HA/HA011.ogg"
    hachiman "Well, I thought they'd never grow up, but they're in highschool already..."
    show saki vhappy with dissolve
    voice "audio/voice/E5/SAK/01/SA/SA007.ogg"
    saki "Why are you talking like a dad who's about to take his daughter to her wedding?"
    voice "audio/voice/E5/SAK/01/HA/HA012.ogg"
    hachiman "That's just how it feels like to me."
    "While talking to her, I idly made a snowball and lightly threw it."
    voice "audio/voice/E5/SAK/01/HA/HA013.ogg"
    hachiman "Once Komachi enters high school, she'll definitely be popular with the boys, right? That's what I'm rather concerned about."
    show saki happy with dissolve
    "And then, Kawasaki also made a snowball and threw it in my direction."
    show saki vhappy with dissolve
    voice "audio/voice/E5/SAK/01/SA/SA008.ogg"
    saki "Yeah, Keika's cute as well, that'll probably become a problem too someday..."
    voice "audio/voice/E5/SAK/01/HA/HA014.ogg"
    hachiman "Keika's certainly a concern..."
    show saki surprised with dissolve
    "This time, I threw a snowball back with a little more enthusiasm. With a light thud, the snowball hit Kawasaki's cuff and fell."
    window auto hide dissolve
    scene sakiSnowballa with dissolve:
        yoffset 0
    window auto show dissolve
    voice "audio/voice/E5/SAK/01/SA/SA009.ogg"
    saki "Taishi's going to be worried too--!"
    show transition_1a at offscreenright:
        parallel:
            easeout 0.1 xpos -3500
    play sound "audio/sfx/SE01/SE01_13.ogg"
    $renpy.pause(delay=0.15, hard=True)
    hide transition_1a
    "This time, a fairly legit snowball soared past through me. I was grinning before I knew it."
    voice "audio/voice/E5/SAK/01/HA/HA015.ogg"
    hachiman "I'm not done yet!"
    voice "audio/voice/E5/SAK/01/SA/SA010.ogg"
    saki "Now wait just a...  If you're going to hit me, you shouldn't say it out loud-- Kyah!?"
    window auto hide dissolve
    scene sakiSnowballa at Shake((0, 0, 0, 0), 0.5, dist=50):
        zoom 1.4 xoffset -715 yoffset -75
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/SE01/SE01_60.ogg"
    $renpy.pause(delay=0.5, hard=True)
    scene sakiSnowballa:
        yoffset 0
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E5/SAK/01/HA/HA016.ogg"
    hachiman "Ah, crap, I actually hit her."
    voice "audio/voice/E5/SAK/01/SA/SA011.ogg"
    saki "...Why, you!"
    voice "audio/voice/E5/SAK/01/HA/HA017.ogg"
    hachiman "Ouch!"
    window auto hide dissolve
    show black
    show sakiSnowballa zorder 2 at Shake((0, 0, 0, 0), 0.5, dist=50) with Fade(.05, 0, .05, color="#fff"):
        yoffset 0
    play sound "audio/sfx/SE01/SE01_60.ogg"
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    "This time, the snow splattered on my face in a clean headshot. After cleaning it off, I saw Kawasaki making a triumphant face."
    voice "audio/voice/E5/SAK/01/HA/HA018.ogg"
    hachiman "Looks like I no longer need to hold back."
    window auto hide dissolve
    stop voice
    scene sakiSnowballa with Fade(1.0, 0.5, 1.0):
        yoffset 0
    play sound "audio/sfx/SE01/SE01_59L.ogg" loop
    window auto show dissolve
    "Before we knew it, it became a full-scale snowball war."
    hachiman "(She's really getting into this, isn't she?)"
    voice "audio/voice/E5/SAK/01/SA/SA012.ogg"
    saki "You're still a hundred years too early to win against me in a snowball fight."
    voice "audio/voice/E5/SAK/01/HA/HA019.ogg"
    hachiman "Hah, what are you bragging about?"
    "We throw snowballs at each other while talking freely."
    show sakiSnowballb with dissolve:
        yoffset 0
    hachiman "(I couldn't explain it, but for some reason I'm really enjoying this.)"
    voice "audio/voice/E5/SAK/01/SA/SA013.ogg"
    saki "Hey, what will you do when you get to college?"
    voice "audio/voice/E5/SAK/01/HA/HA020.ogg"
    hachiman "I haven't decided yet, but I want to do something fun and use my brain."
    voice "audio/voice/E5/SAK/01/SA/SA014.ogg"
    saki "I think you're pretty good at that. Research and stuff."
    voice "audio/voice/E5/SAK/01/HA/HA021.ogg"
    hachiman "Dunno about that. And you?"
    "With just those few words, I feel like I can have honest conversations with Kawasaki."
    voice "audio/voice/E5/SAK/01/SA/SA015.ogg"
    saki "As for me... since I want to take care of my siblings, I have to find a way to get a good job."
    voice "audio/voice/E5/SAK/01/HA/HA022.ogg"
    hachiman "Maybe you don't need to support them all by yourself?"
    hide sakiSnowballb with dissolve
    voice "audio/voice/E5/SAK/01/SA/SA016.ogg"
    saki "Huh?"
    voice "audio/voice/E5/SAK/01/HA/HA023.ogg"
    hachiman "We've got to give them a chance to shine themselves."
    show sakiSnowballb with dissolve:
        yoffset 0
    voice "audio/voice/E5/SAK/01/SA/SA017.ogg"
    saki "I see... You're right."
    "Kawasaki suddenly stopped throwing. I took advantage of the opportunity and threw a snowball."
    voice "audio/voice/E5/SAK/01/HA/HA024.ogg"
    hachiman "Goal!"
    window auto hide dissolve
    scene sakiSnowballa at Shake((0, 0, 0, 0), 0.5, dist=50):
        zoom 1.4 xoffset -715 yoffset -75
    play sound "audio/sfx/SE01/SE01_60.ogg"
    $renpy.pause(delay=1.0, hard=True)
    scene sakiSnowballa:
        yoffset 0
    $renpy.pause(delay=0.5, hard=True)
    window auto show dissolve
    voice "audio/voice/E5/SAK/01/SA/SA018.ogg"
    saki "Whoa!"
    show sakiSnowballb with dissolve:
        yoffset 0
    voice "audio/voice/E5/SAK/01/SA/SA019.ogg"
    saki "...Heh, bring it on!"
    hachiman "(Crap, Kawasaki-san, you're giving off an aura or seriousness. Scary!)"
    "Kawasaki gripped her snowball tightly, and started making a huge swing--"
    window auto hide dissolve
    play sound "audio/sfx/SE02/SE02_09.ogg"
    $renpy.pause(delay=1.0, hard=True)
    scene gatesE with dissolve
    window auto show dissolve
    voice "audio/voice/E5/SAK/01/SA/SA020.ogg"
    saki "...The exam, is it over already?"
    voice "audio/voice/E5/SAK/01/HA/HA025.ogg"
    hachiman "...It seems like it."
    "Slowly, I lowered my arm and let the snow fall from my hand. We both looked towards the school building, which was becoming more and more crowded. I wondered if Komachi and Taishi finished their exams "
    "without issue."
    voice "audio/voice/E5/SAK/01/HA/HA026.ogg"
    hachiman "............"
    voice "audio/voice/E5/SAK/01/SA/SA021.ogg"
    saki "............"
    voice "audio/voice/E5/SAK/01/KO/KO003.ogg"
    komachi "Huh, onii-chan?"
    voice "audio/voice/E5/SAK/01/TA/TA000.ogg"
    taishi "Oh, onii-san! Nee-chan too?"
    show saki school_dark mid_right vhappy at left:
        xoffset 70  yoffset 75
    show komachi school_dark mid_left happy at right:
        xoffset -275 yoffset 75
    with dissolve
    voice "audio/voice/E5/SAK/01/HA/HA027.ogg"
    hachiman "Hey, Komachi."
    voice "audio/voice/E5/SAK/01/SA/SA022.ogg"
    saki "Taishi, well done."
    hide komachi
    $url = ["komachi school_dark mid_left happy", "komachi school_dark mid_left unimpressed"]
    $multiImagePara = [-275, 75, 0, 0, 3.1]
    call multiImage(1) from _call_multiImage
    voice "audio/voice/E5/SAK/01/KO/KO004.ogg"
    komachi "You came here for me, Onii-chan? ... What are you guys doing?"
    call finishmultiImage from _call_finishmultiImage
    show komachi school_dark mid_left unimpressed at right:
        xoffset -275 yoffset 75
    show saki surprised with dissolve
    voice "audio/voice/E5/SAK/01/MI/MIX001.ogg"
    hachiandsaki "Eh--"
    voice "audio/voice/E5/SAK/01/TA/TA001.ogg"
    taishi "They're both covered in snow..."
    show saki pout with dissolve
    voice "audio/voice/E5/SAK/01/MI/MIX002.ogg"
    hachiandsaki "Ah..."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    jump E5_SAK_02

label E5_SAK_02:
    scene skyA with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "And so, about a week or so after the exam..."
    window auto hide dissolve
    play ambient ["<silence 1.0>", "audio/sfx/SE05/SE05_03L.ogg"]
    scene classroomA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM08.ogg"
    show yui school mid_center happy at center with dissolve:
        xoffset -25 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/SAK/02/YI/YI000.ogg"
    yui "Hikki--! Komachi-chan got admitted right?"
    voice "audio/voice/E5/SAK/02/HA/HA000.ogg"
    hachiman "Oh, Komachi mailed you?"
    hide yui
    $url = ["yui school mid_center vhappy", "yui school mid_center annoyed"]
    $multiImagePara = [-25, 75, 0, 0, 5.8]
    call multiImage() from _call_multiImage_1
    voice "audio/voice/E5/SAK/02/YI/YI001.ogg"
    yui "Yeah, I was so happy that I had a long chat with Yukinon on the phone about it! But hey, why didn't you tell me!?"
    call finishmultiImage from _call_finishmultiImage_1
    show yui school mid_center annoyed at center:
        xoffset -25 yoffset 75
    voice "audio/voice/E5/SAK/02/HA/HA001.ogg"
    hachiman "I mean, I was going to tell you guys when I saw you, but... I didn't expect Komachi to mail you."
    show yui frown with dissolve
    voice "audio/voice/E5/SAK/02/YI/YI002.ogg"
    yui "Hikki, mailing or calling us is fine you know!"
    voice "audio/voice/E5/SAK/02/HA/HA002.ogg"
    hachiman "I never thought both of you would be so happy for her... Thank you."
    show yui vhappy with dissolve
    voice "audio/voice/E5/SAK/02/YI/YI003.ogg"
    yui "Yeah, we'll be in the same school come april! By the way, Taishi-kun also got admitted, right? You know, Saki's brother."
    hachiman "(Komachi... did you really have to tell them all about it?)"
    voice "audio/voice/E5/SAK/02/HA/HA003.ogg"
    hachiman "It sure seems like it."
    hide yui
    $url = ["yui school mid_center vhappy", "yui school mid_right vhappy"]
    $multiImagePara = [-25, 75, -110, 75, 2.5]
    call multiImage(0, False) from _call_multiImage_2
    voice "audio/voice/E5/SAK/02/YI/YI004.ogg"
    yui "Good to hear. Hey, Saki~!"
    call finishmultiImage from _call_finishmultiImage_2
    with dissolve
    show yui school mid_left vhappy at center:
        xoffset 250 yoffset 75
    show saki school mid_left pout at right:
        xoffset 35 yoffset 75
    with dissolve
    voice "audio/voice/E5/SAK/02/SA/SA000.ogg"
    saki "W-What is it, all of a sudden?."
    "Yuigahama locked her arms with Saki's, and forced her to come along. Kawasaki didn't like it very much, and her eyes betrayed signs of tears."
    hachiman "(She definitely started eavesdropping when we mentioned Taishi's name.)"
    hide yui
    hide saki
    with dissolve
    show yui school mid_right vhappy at left:
        xoffset 20 yoffset 75
    show saki school mid_left pout at right:
        xoffset -95 yoffset 75
    with dissolve
    voice "audio/voice/E5/SAK/02/YI/YI005.ogg"
    yui "Congrats to Taishi-kun for passing the exams!"
    show saki blush with dissolve
    voice "audio/voice/E5/SAK/02/SA/SA001.ogg"
    saki "T-Thank you."
    voice "audio/voice/E5/SAK/02/HA/HA004.ogg"
    hachiman "Glad it all ended well."
    show saki vhappy with dissolve
    voice "audio/voice/E5/SAK/02/SA/SA002.ogg"
    saki "Yeah."
    "After all that's happened, the case regarding our siblings' entrance exams is closed at long last."
    window auto hide dissolve
    stop ambient fadeout 1.0
    stop music fadeout 1.0
    call loading_screen(21, "33") from _call_loading_screen_6
    scene houseB with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM10.ogg"
    window auto show dissolve
    voice "audio/voice/E5/SAK/02/KO/KO000.ogg"
    komachi "Onii-chaaan!"
    show komachi school_sunset mid_center vhappy at center with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E5/SAK/02/HA/HA005.ogg"
    hachiman "Oh, welcome back. What's up?"
    voice "audio/voice/E5/SAK/02/KO/KO001.ogg"
    komachi "Did you know, Taishi-kun invited Komachi to the hot springs!?"
    voice "audio/voice/E5/SAK/02/HA/HA006.ogg"
    hachiman "H-Hot springs you say? What insolence...! This is completely unacceptable, especially towards my cute little sister!"
    hachiman "(I don't know who the hell you are, but there are things in this world that you can do and some things you can't. Is it finally the time to stain these hands with blood...!?)"
    show komachi unimpressed with dissolve
    voice "audio/voice/E5/SAK/02/KO/KO002.ogg"
    komachi "I-It's not what you think it is. Taishi-kun's mother won a one-night trip to the hot springs from a lottery in the downtown area."
    voice "audio/voice/E5/SAK/02/HA/HA007.ogg"
    hachiman "...Oh??"
    show komachi happy with dissolve
    voice "audio/voice/E5/SAK/02/KO/KO003.ogg"
    komachi "And then she said Saki-san, Keika-chan, Komachi and onii-chan should all come along."
    voice "audio/voice/E5/SAK/02/HA/HA008.ogg"
    hachiman "Is that how it is?"
    voice "audio/voice/E5/SAK/02/KO/KO004.ogg"
    komachi "Yes, that's how it is. Since we got invited and all, I say we go, Onii-chan."
    voice "audio/voice/E5/SAK/02/HA/HA009.ogg"
    hachiman "Sure, let's do it."
    show komachi vhappy with dissolve
    voice "audio/voice/E5/SAK/02/KO/KO005.ogg"
    komachi "Yay! Umm..."
    hide komachi with dissolve
    hachiman "(I was so surprised to suddenly hear about hot springs. I thought that kind of thing was a family only affair, so why are we getting invited?)"
    hachiman "(Is this one of those psychological tactics where you demand an impossible request at first, and then take it down a notch to seem more convincing?)"
    "As I looked at her blankly, my mind unable to grasp the situation, Komachi started to make a phone call."
    voice "audio/voice/E5/SAK/02/KO/KO006.ogg"
    komachi "Hello Taishi-kun? Onii-chan said it's fine--! Let's plan our schedule right away!"
    hachiman "(Eh, wait a second.)"
    "As I watched Komachi talking about something, I gradually came to understand what was going on."
    hachiman "(Since we're going as a package with Kawasaki and her sister, I don't think I'll have to worry about Taishi doing something behind my back. That leaves... Kawasaki?! We're going to a spa together! Is she okay "
    hachiman "with that idea!?)"
    show komachi school_sunset far_center vhappy at center with dissolve:
        xoffset 210 yoffset 75
    voice "audio/voice/E5/SAK/02/KO/KO007.ogg"
    komachi "Onii-chan, Saki-san said she's looking forward to it!"
    "Komachi put her hand over the phone and called out to me, perfectly in sync with my thoughts."
    voice "audio/voice/E5/SAK/02/HA/HA010.ogg"
    hachiman "I-Is that so?"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    jump E5_SAK_03

label E5_SAK_03:
    scene skyA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM07.ogg"
    window auto show dissolve
    "And thus, the one-night trip to the hot springs was immediately decided upon."
    voice "audio/voice/E5/SAK/03/KE/KE000.ogg"
    keika "Wow, Saa-chan, it's steaming!"
    voice "audio/voice/E5/SAK/03/SA/SA000.ogg"
    saki "Yeah. It's a hot spring after all."
    voice "audio/voice/E5/SAK/03/KE/KE001.ogg"
    keika "Yay, hot spring--! --What's a hot spring?"
    voice "audio/voice/E5/SAK/03/SA/SA001.ogg"
    saki "U-Umm... It's a large bath, maybe?"
    voice "audio/voice/E5/SAK/03/KE/KE002.ogg"
    keika "Bath--! We have one at home!"
    voice "audio/voice/E5/SAK/03/SA/SA002.ogg"
    saki "This one's... a bit different though."
    "Keika, who fell asleep as soon as she boarded the express train after being tired from several train connections, shouted with joy at the steam that rose up from everywhere."
    "I rarely travel, so I get really excited when I come to a place like this."
    voice "audio/voice/E5/SAK/03/KO/KO000.ogg"
    komachi "Hey onii-chan, aren't you glad we came?"
    voice "audio/voice/E5/SAK/03/HA/HA000.ogg"
    hachiman "Sure am."
    window auto hide dissolve
    stop voice
    scene hotspringOutsideA
    show saki coat mid_right happy at left:
        xoffset -50 yoffset 75
    show keika heavy_coat mid vhappy at center:
        xoffset 5 yoffset 75
    show komachi coat mid_left happy at right:
        xoffset -150 yoffset 75
    with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    voice "audio/voice/E5/SAK/03/TA/TA000.ogg"
    taishi "Oooh-- it's a ryokan lodging, right onii-san?"
    voice "audio/voice/E5/SAK/03/KE/KE003.ogg"
    keika "Ryokan--!"
    voice "audio/voice/E5/SAK/03/HA/HA001.ogg"
    hachiman "This looks like a very expensive lodging. It's unexpected she won this from a deserted shopping mall."
    show komachi coat mid_center vhappy at right with dissolve:
        xoffset -75
    voice "audio/voice/E5/SAK/03/KO/KO001.ogg"
    komachi "It's a special prize after all. A very special one!"
    voice "audio/voice/E5/SAK/03/TA/TA001.ogg"
    taishi "Speaking of prizes, the lesser one was a trip to Taiwan, I think!"
    voice "audio/voice/E5/SAK/03/HA/HA002.ogg"
    hachiman "Ooh."
    hachiman "(It seems strange that a trip to a hot spring in the vicinity of a prefecture is better than a trip abroad...)"
    "Kawasaki explains as if she read my mind."
    show saki vhappy with dissolve
    voice "audio/voice/E5/SAK/03/SA/SA003.ogg"
    saki "They said \"Nowadays it's cheaper to take a trip abroad, than vacation in a nearby place.\" I think the selling point of this place is that it's a pretty famous inn."
    voice "audio/voice/E5/SAK/03/HA/HA003.ogg"
    hachiman "Was it a good idea to invite us here? Shouldn't you have come with your family?"
    hide saki with dissolve
    voice "audio/voice/E5/SAK/03/SA/SA004.ogg"
    saki "I thought it would be more fun to be with just the kids... and I thought it would be safer to have two, rather than one, high school students with them."
    voice "audio/voice/E5/SAK/03/TA/TA002.ogg"
    taishi "When I told them that onii-san helped me study for the exams, they said that I was lucky I found myself such a caring senpai!"
    hachiman "(No, I'm sure there are senpai who care a lot more then me out there. I think your parents are a bit out of touch.)"
    voice "audio/voice/E5/SAK/03/SA/SA005.ogg"
    saki "Oh, I also told my parents that you consulted me about my scholarship..."
    show komachi happy with dissolve
    voice "audio/voice/E5/SAK/03/KO/KO002.ogg"
    komachi "It's unusual for onii-chan to be this reliable!"
    voice "audio/voice/E5/SAK/03/HA/HA004.ogg"
    hachiman "And that's unusually unnecessary for you to say."
    show saki coat mid_right vhappy at left with dissolve:
        xoffset -50 yoffset 75
    voice "audio/voice/E5/SAK/03/SA/SA006.ogg"
    saki "............"
    voice "audio/voice/E5/SAK/03/HA/HA005.ogg"
    hachiman "It really is. But seriously, I really wouldn't want to give the Kawasaki family the wrong idea about my 'undisputable reliability'."
    voice "audio/voice/E5/SAK/03/SA/SA007.ogg"
    saki "I guess so."
    "Kawasaki chuckled and Keika pulled me by my hand."
    hide keika
    hide komachi
    with dissolve
    show keika heavy_coat near vhappy at right with dissolve:
        xoffset -55 yoffset 75
    voice "audio/voice/E5/SAK/03/KE/KE004.ogg"
    keika "Haa-chan, Saa-chan, let's go!"
    voice "audio/voice/E5/SAK/03/SA/SA008.ogg"
    saki "You're right. No point in just standing around."
    voice "audio/voice/E5/SAK/03/HA/HA006.ogg"
    hachiman "Yeah."
    hide saki
    hide keika
    with dissolve
    "And as if she was waiting for our conversation to settle down, a person who looked like the hostess of the inn approached us excitedly."
    stop music fadeout 1.0
    voice "audio/voice/E5/SAK/03/XU/XU000.ogg"
    hostess "Welcome, we've been waiting for you. You're Hikigaya-sama, aren't you?"
    voice "audio/voice/E5/SAK/03/HA/HA007.ogg"
    hachiman "Umm, yeah."
    play music "audio/bgm/BGM44.ogg"
    show saki coat near_right blush at left with dissolve:
        xoffset -330 yoffset 75
    voice "audio/voice/E5/SAK/03/SA/SA009.ogg"
    saki "Sorry, my mother must've made a reservation under your name..."
    voice "audio/voice/E5/SAK/03/HA/HA008.ogg"
    hachiman "I-I see."
    show keika heavy_coat mid vhappy at center:
        xoffset 5 yoffset 75
    show komachi coat mid_left happy at right:
        xoffset -150 yoffset 75
    with dissolve
    voice "audio/voice/E5/SAK/03/KE/KE005.ogg"
    keika "Oh, Hi-ki-ga-ya-sa-ma--!"
    voice "audio/voice/E5/SAK/03/XU/XU001.ogg"
    hostess "Aww, what a sweet girl. Then... I assume they're your brother and sister?"
    voice "audio/voice/E5/SAK/03/KE/KE006.ogg"
    keika "No, they're Kei-chan's papa and mama--!"
    show komachi coat mid_center vhappy at right with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E5/SAK/03/KO/KO003.ogg"
    komachi "I'm his little sister."
    voice "audio/voice/E5/SAK/03/TA/TA003.ogg"
    taishi "I'm her brother!"
    voice "audio/voice/E5/SAK/03/MI/MIX000.ogg"
    hachiandsaki "Wh...."
    voice "audio/voice/E5/SAK/03/XU/XU002.ogg"
    hostess "It's a pleasure to meet such a cute family. Come in, come in. We'll guide you to your room at once."
    voice "audio/voice/E5/SAK/03/ZM/ZM000.ogg"
    ms "Please let us carry your luggage."
    "I'm upset by the wave of attacks from the hostess' misunderstandings, plus the younger brother and sister thing. Kawasaki has also turned red and is in a state of rigidity."
    hachiman "(How should I put it... This is so embarassing... W-What's going on here!?)"
    window auto hide dissolve
    stop music fadeout 1.0
    call loading_screen(17, "33") from _call_komachi_coat_center_loading
    play sound ["<silence 1.0>", "audio/sfx/SE02/SE02_06.ogg"]
    scene hotspringBGB
    with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM10.ogg"
    window auto show dissolve
    hachiman "(However, the food was delicious, the rooms are also beautiful, and most importantly, Komachi was very pleased... It's a good thing we came here. Hot springs really are great.)"
    voice "audio/voice/E5/SAK/03/HA/HA010.ogg"
    hachiman "Aaahhhh..."
    voice "audio/voice/E5/SAK/03/TA/TA004.ogg"
    taishi "Onii-san, open baths are so good, aren't they?"
    voice "audio/voice/E5/SAK/03/HA/HA011.ogg"
    hachiman "You got that right..."
    hachiman "(So refreshing--)"
    window auto hide dissolve
    play sound "audio/sfx/SE00/SE00_36.ogg"
    $renpy.pause(delay=2.0, hard=True)
    scene skyC with dissolve
    $renpy.pause(delay=1.0, hard=True)
    stop sound fadeout 0.5
    window auto show dissolve
    voice "audio/voice/E5/SAK/03/SA/SA011.ogg"
    saki "W-Wait Kei-chan, you'll slip if you run!"
    voice "audio/voice/E5/SAK/03/KO/KO004.ogg"
    komachi "Oniiiii-chaan, are you having a good time over there?"
    hachiman "(Refreshing... unless you can hear them on the other side.)"
    window auto hide dissolve
    scene sakiBath with dissolve
    window auto show dissolve
    voice "audio/voice/E5/SAK/03/TA/TA005.ogg"
    taishi "Thanks to you, onii-san, I was able to take my entrance exams just fine."
    voice "audio/voice/E5/SAK/03/HA/HA012.ogg"
    hachiman "Oh? That's great then."
    voice "audio/voice/E5/SAK/03/KE/KE007.ogg"
    keika "Taa-chan, that's so unfair! I also want to take a bath with Haa-chan!"
    voice "audio/voice/E5/SAK/03/HA/HA013.ogg"
    hachiman "Oh, so you're called Taa-chan?"
    voice "audio/voice/E5/SAK/03/TA/TA006.ogg"
    taishi "You do get it wrong sometimes... Maybe my presence is just kind of weak?"
    voice "audio/voice/E5/SAK/03/HA/HA014.ogg"
    hachiman "Ah, that's true. Sometimes I ask myself \"who was this guy again?\"."
    window auto hide dissolve
    scene sakiBath with dissolve:
        zoom 1.7 xoffset -20 yoffset -175
    window auto show dissolve
    voice "audio/voice/E5/SAK/03/KO/KO005.ogg"
    komachi "Onii-chan's talking about other people having a weak presence!"
    voice "audio/voice/E5/SAK/03/SA/SA012.ogg"
    saki "Hikigaya, if you keep mocking Taishi, you'll get it from me. In the first place, for other people you are..."
    voice "audio/voice/E5/SAK/03/SA/SA013.ogg"
    saki "Ah. I'm sorry..."
    voice "audio/voice/E5/SAK/03/KO/KO006.ogg"
    komachi "Ah, no! It's quite alright! Batter my brother as you please! I've been wanting a strong older sister like you to beat his attitude into shape!"
    hachiman "(I don't have the guts for a retort here.)"
    show sakiBath with dissolve
    voice "audio/voice/E5/SAK/03/SA/SA014.ogg"
    saki "Eh? Are you sure?"
    hachiman "(\"Are you sure?\", what do you mean \"are you sure?\" ?)"
    voice "audio/voice/E5/SAK/03/KE/KE008.ogg"
    keika "Kei-chan will also batter him!"
    voice "audio/voice/E5/SAK/03/TA/TA007.ogg"
    taishi "Onii-san, it looks like they're going to gang up on you..."
    window auto hide dissolve
    stop voice
    scene hachimanBathc with dissolve:
        zoom 1.7 xoffset -17 yoffset -312
    window auto show dissolve
    voice "audio/voice/E5/SAK/03/HA/HA015.ogg"
    hachiman "............"
    hachiman "(T-This isn't very relaxing anymore...)"
    voice "audio/voice/E5/SAK/03/KO/KO007.ogg"
    komachi "And besides, Saki-san also looks so beautiful and stylish, I think I've got a crush on her already!"
    voice "audio/voice/E5/SAK/03/SA/SA015.ogg"
    saki "T-That's a bit much. I think Komachi-chan's very cute, too."
    voice "audio/voice/E5/SAK/03/KO/KO008.ogg"
    komachi "No need to be humble! Compared to Saki-san, my skin isn't as fair and smooth as hers, my body's also not as beautiful, and whatever sense of style I have, it's not befitting of a model unlike yours..."
    hachiman "(Komachi-chan, stop that weird live reporting.)"
    show sakiBath with dissolve
    voice "audio/voice/E5/SAK/03/SA/SA016.ogg"
    saki "L-Like I said, that's not true at all."
    voice "audio/voice/E5/SAK/03/TA/TA008.ogg"
    taishi "Onii-san, your face's bright! Are you alright!? Do you feel light-headed!?"
    voice "audio/voice/E5/SAK/03/HA/HA016.ogg"
    hachiman "Wha-- Don't be stupid, shut up for a second."
    voice "audio/voice/E5/SAK/03/SA/SA017.ogg"
    saki "If you keep on insulting Taishi, I'll seriously strangle you!"
    hachiman "(I-I don't feel safe anymore.)"
    window auto hide dissolve
    stop music fadeout 1.0
    scene skyC with Fade(1.0, 0.5, 1.0)
    play sound "audio/sfx/SE00/SE00_30L.ogg"
    menu hotsprings1_menu:
        hachiman "The hot water feels good, that's a given... But should I be hitting the sack already?"
        with dissolve
        "I wonder if Kawasaki had fun.":
            voice "audio/voice/E5/SAK/03/HA/HA018.ogg"
            hachiman "I don't feel chilly from the bath, so I won't go back to my room just yet."
            window auto hide dissolve
            stop sound fadeout 0.5
            jump E5_SAK_04
        "I wonder if Komachi had fun.":
            voice "audio/voice/E5/SAK/03/HA/HA017.ogg"
            hachiman "I guess I'll go take a breather outside..."
            window auto hide dissolve
            stop sound fadeout 0.5
            stop voice
            jump E5_SAK_06

label E5_SAK_04:
    scene skyC with Fade(1.0, 0.5, 1.0)
    play sound "audio/sfx/SE02/SE02_00.ogg"
    hachiman "(Well... it's a bit chilly, but it feels good...)"
    "After I got out of the open-air bath and finished my dinner, I went outside the inn to cool off."
    "It's a group of people that I don't have to worry around, but as a person who is basically a loner, it's a relief to have some time alone."
    stop sound fadeout 1.0
    hachiman "(I mean, when did they become join the \"people I don't have to worry around\" category for me? Kawasaki and her siblings.)"
    "I felt both embarrassed and deeply moved when I thought that up until recently I had been at the same distance as always from miss Kawa-something-san."
    hachiman "(Well, Komachi is lucky to enter high school together with a friend...)"
    voice "audio/voice/E5/SAK/04/SA/SA000.ogg"
    mystery "Ah--"
    hachiman "(This voice... Kawasaki!?)"
    "As I realized it, my heart skipped a beat. I hope it wasn't too obvious..."
    window auto hide dissolve
    scene hotspringOutsideB
    play music "audio/bgm/BGM18.ogg"
    show saki coat_night near_right happy at left with dissolve:
        xoffset -35 yoffset 75
    window auto show dissolve
    voice "audio/voice/E5/SAK/04/HA/HA000.ogg"
    hachiman "Yo... is Keika in bed already?"
    show saki vhappy with dissolve
    voice "audio/voice/E5/SAK/04/SA/SA001.ogg"
    saki "Yeah, she's very tired so she's sound asleep."
    voice "audio/voice/E5/SAK/04/HA/HA001.ogg"
    hachiman "I see."
    show saki blush with dissolve
    voice "audio/voice/E5/SAK/04/SA/SA002.ogg"
    saki "Umm... T-Thanks for today."
    voice "audio/voice/E5/SAK/04/HA/HA002.ogg"
    hachiman "Ah, not at all, I should be the one thanking you. Komachi had a lot of fun, too."
    show saki vhappy with dissolve
    voice "audio/voice/E5/SAK/04/SA/SA003.ogg"
    saki "Taishi looked happy, too. He said... He's glad to be here with you."
    voice "audio/voice/E5/SAK/04/HA/HA003.ogg"
    hachiman "I guess that means we're all glad we came here together."
    show saki blush with dissolve
    voice "audio/voice/E5/SAK/04/SA/SA004.ogg"
    saki "I-I don't know about that."
    hachiman "(I don't feel comfortable when people say things I'm not used to hearing. I wonder if there's any way to change the flow of this conversation.)"
    "The unfamiliar atmosphere of the conversation was somewhat embarrassing."
    voice "audio/voice/E5/SAK/04/HA/HA004.ogg"
    hachiman "Ah. Now it's our turn...you know, for the exam."
    show saki happy with dissolve
    voice "audio/voice/E5/SAK/04/SA/SA005.ogg"
    saki "Ah, it really is, isn't it?"
    "I don't know if it's because she's just finished taking a bath or if it's because she's in a different environment than usual, but Kawasaki's face is slightly red and her speech was more relaxed than usual. There was none of the usual toughness."
    voice "audio/voice/E5/SAK/04/HA/HA005.ogg"
    hachiman "Yeah, well, let's try to keep it up. I know you can get a scholarship."
    show saki frown with dissolve
    voice "audio/voice/E5/SAK/04/SA/SA006.ogg"
    saki "What about you? Why don't you go for a national school?"
    voice "audio/voice/E5/SAK/04/HA/HA006.ogg"
    hachiman "No, well..."
    show saki happy with dissolve
    voice "audio/voice/E5/SAK/04/SA/SA007.ogg"
    saki "Oh, are the science subjects the problem?"
    hachiman "(S-She's read my thoughts.)"
    show saki angry with dissolve
    voice "audio/voice/E5/SAK/04/SA/SA008.ogg"
    saki "If you want, we can have another study session..."
    voice "audio/voice/E5/SAK/04/HA/HA007.ogg"
    hachiman "...I am greatly in your debt."
    show saki vhappy with dissolve
    voice "audio/voice/E5/SAK/04/SA/SA009.ogg"
    saki "What are you being so uptight about?"
    "Kawasaki chuckles at my words, and I realize now that I really like to see her smile."
    window auto hide dissolve
    stop music fadeout 1.0
    call loading_screen(duration="short") from _call_general_loading
    jump E5_SAK_05

label E5_SAK_05:
    play ambient ["<silence 1.0>", "audio/sfx/SE05/SE05_03L.ogg"]
    scene hallwayA with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "With the graduation ceremony for third years and spring break just around the corner, the school was filled with a sense of excitement."
    hachiman "(It's getting warmer and warmer with spring coming...)"
    "After spring break, we'll finally be third years. I wonder if the new semester will be troublesome again as a result of the class changes that will be made based on the career questionnaire."
    hachiman "(Hm?)"
    window auto hide dissolve
    stop ambient fadeout 0.5
    scene sakiHallwayd with dissolve
    play music "audio/bgm/BGM14.ogg"
    window auto show dissolve
    "I looked over and saw Kawasaki in the corner of the hallway, playing with her phone. She was probably emailing Taishi again."
    voice "audio/voice/E5/SAK/05/HA/HA000.ogg"
    hachiman "...Yo."
    hachiman "(...I'm getting deja vu.)"
    show sakiHallwayc
    with dissolve
    voice "audio/voice/E5/SAK/05/SA/SA000.ogg"
    saki "Ah, Hikigaya."
    window auto hide dissolve
    scene hallwayA with dissolve
    window auto show dissolve
    "She looked busy texting, so I decided to leave her be. But just as I was about to walk past her..."
    show saki school near_right surprised at left with dissolve:
        xoffset -35 yoffset 75
    voice "audio/voice/E5/SAK/05/SA/SA001.ogg"
    saki "H-hey, um..."
    voice "audio/voice/E5/SAK/05/HA/HA001.ogg"
    hachiman "...Hm?"
    show saki pout with dissolve
    voice "audio/voice/E5/SAK/05/SA/SA002.ogg"
    saki "You know... Um... I mean, it's not a big deal or anything, but..."
    voice "audio/voice/E5/SAK/05/HA/HA002.ogg"
    hachiman "What is it?"
    show saki sad with dissolve
    voice "audio/voice/E5/SAK/05/SA/SA003.ogg"
    saki "No, it's just that... Hah..."
    show saki annoyed with dissolve
    voice "audio/voice/E5/SAK/05/SA/SA004.ogg"
    saki "Come with me for a second!"
    voice "audio/voice/E5/SAK/05/HA/HA003.ogg"
    hachiman "Huh?"
    window auto hide dissolve
    stop voice
    scene skyA with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "Kawasaki pulls me onto the roof. Despite it being sunny, it was still chilly."
    window auto hide dissolve
    stop music fadeout 1.0
    scene rooftopA
    show saki school mid_right happy at center:
        xoffset -115 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E5/SAK/05/HA/HA004.ogg"
    hachiman "Oh, this is kinda nostalgic."
    show saki surprised with dissolve
    voice "audio/voice/E5/SAK/05/SA/SA005.ogg"
    saki "Huh?"
    voice "audio/voice/E5/SAK/05/HA/HA005.ogg"
    hachiman "Ah, well... it was here. The first time I met you."
    show saki vhappy with dissolve
    play music "audio/bgm/BGM42.ogg"
    voice "audio/voice/E5/SAK/05/SA/SA006.ogg"
    saki "...You remember."
    voice "audio/voice/E5/SAK/05/HA/HA006.ogg"
    hachiman "Yeah, I guess I do..."
    "It's pretty hard to forget. It was intense and shocking. Well, in more than one way."
    voice "audio/voice/E5/SAK/05/HA/HA007.ogg"
    hachiman "So, what did you want to talk about?"
    show saki surprised with dissolve
    voice "audio/voice/E5/SAK/05/SA/SA007.ogg"
    saki "Oh, yeah... Well, it's not really a big deal, but there's something I wanted to tell you...!"
    hachiman "(Come to think of it, she used to have this kind of nervousness about her when starting a conversation in the past... I feel like I haven't seen this reaction in long time, since she's been so calm when talking "
    "lately.)"
    show saki pout with dissolve
    voice "audio/voice/E5/SAK/05/SA/SA008.ogg"
    saki "Well, you see..."
    show saki blush with dissolve
    voice "audio/voice/E5/SAK/05/SA/SA009.ogg"
    saki "You know, I had a lot of fun when you came over to eat at my place. The trip, too..."
    voice "audio/voice/E5/SAK/05/HA/HA008.ogg"
    hachiman "No... you did a lot for me, on both occasions. I thought I'd have to repay you somehow..."
    voice "audio/voice/E5/SAK/05/SA/SA010.ogg"
    saki "No, I didn't mean it that way."
    window auto hide dissolve
    scene sakiRooftopa with dissolve
    window auto show dissolve
    voice "audio/voice/E5/SAK/05/SA/SA011.ogg"
    saki "It's just that... I feel at really at ease when I talk to you, so... um..."
    "Despite what she just said, Kawasaki had a hard time forcing out what she wanted to say, her face turning red and teary-eyed."
    hachiman "(S-strangely enough, this is making my heart race...)"
    voice "audio/voice/E5/SAK/05/SA/SA012.ogg"
    saki "You don't have to, but... I'd really like it if you came to my place again sometime!"
    voice "audio/voice/E5/SAK/05/HA/HA009.ogg"
    hachiman "A-are you sure?"
    "I asked, and Kawasaki nodded repeatedly with tears in her eyes."
    voice "audio/voice/E5/SAK/05/SA/SA013.ogg"
    saki "K-keika will be very happy to see you and... You know, Taishi too."
    voice "audio/voice/E5/SAK/05/HA/HA010.ogg"
    hachiman "Y-Yeah?"
    show sakiRooftopb with dissolve
    voice "audio/voice/E5/SAK/05/SA/SA014.ogg"
    saki "W-What I mean is..."
    "With her face bright red, Kawasaki quickly held out her hand."
    voice "audio/voice/E5/SAK/05/SA/SA015.ogg"
    saki "I... I'd like it if we kept seeing each other, so..."
    voice "audio/voice/E5/SAK/05/HA/HA011.ogg"
    hachiman "R-Right... I'd like that too..."
    "I grasped her hand fearfully and somehow managed to get into a decent handshake. And then."
    voice "audio/voice/E5/SAK/05/SA/SA016.ogg"
    saki "............."
    "As soon as I held her hand, a smile of relief finally appeared on Kawasaki's face."
    hachiman "(Now that I look at them, she's got delicate hands, her fingers are so long and slender...)"
    voice "audio/voice/E5/SAK/05/HA/HA012.ogg"
    hachiman "...Let's continue to get along, then."
    voice "audio/voice/E5/SAK/05/SA/SA017.ogg"
    saki "............."
    voice "audio/voice/E5/SAK/05/HA/HA013.ogg"
    hachiman "............."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    show white with Fade(2.0, 0, 1.0, color="#fff")
    $renpy.movie_cutscene("movies/ed04.mkv")
    jump E6_SAK_01

label E5_SAK_06:
    scene hotspringRoomC with Fade(1.0, 0.5, 1.0)
    "When I went back to my room, the futon was already layed out."
    hachiman "(Gotta love it when your futon is all layed out for you when you come back from dinner. This is what a ryoukan is all about...)"
    image komachiHachimanDup = "images/bg/EV56a.jpg"
    window auto hide dissolve
    scene komachiHachiman with dissolve
    play music "audio/bgm/BGM18.ogg"
    window auto show dissolve
    voice "audio/voice/E5/SAK/06/KO/KO000.ogg"
    komachi "Ah, onii-chan. You took you time."
    "Komachi, who'd come back before me, was already rolling around on the futon like it was the best thing in the world."
    voice "audio/voice/E5/SAK/06/HA/HA000.ogg"
    hachiman "Komachi, put something on. You'll catch a cold after that bath."
    voice "audio/voice/E5/SAK/06/KO/KO001.ogg"
    komachi "The room's nice and warm, so it's okay~"
    "As she was saying that, she tapped on the futon right next to her's and I went to lay down on it."
    voice "audio/voice/E5/SAK/06/KO/KO002.ogg"
    komachi "Ehehe. It's been a couple years since we've went on a trip together, huh?"
    voice "audio/voice/E5/SAK/06/HA/HA001.ogg"
    hachiman "We haven't went on family trips as a whole for years, too."
    "Komachi rolled over on her futon to face me. A nice scent of shampoo drifted in the air."
    window auto hide dissolve
    show komachiHachimanDup at center with dissolve:
        zoom 1.3 yoffset 325 xoffset -50
    window auto show dissolve
    voice "audio/voice/E5/SAK/06/KO/KO003.ogg"
    komachi "I wonder if we'll go on another trip together? Ah, it'll have to be after you finish your exams though."
    voice "audio/voice/E5/SAK/06/HA/HA002.ogg"
    hachiman "I mean we still have a whole year before that."
    voice "audio/voice/E5/SAK/06/KO/KO004.ogg"
    komachi "That one year will be over before you know it, you know?"
    voice "audio/voice/E5/SAK/06/HA/HA003.ogg"
    hachiman "You've only just finished exams yourself and now you're all composed."
    voice "audio/voice/E5/SAK/06/KO/KO005.ogg"
    komachi "That's 'cuz Komachi has another 3 years to go!"
    voice "audio/voice/E5/SAK/06/HA/HA004.ogg"
    hachiman "That's what I thought 2 years ago, too..."
    "It's been 2 years since I began high school, but this year in particular felt like it went in the blink of an eye."
    "This year that went by in a bustle. I wonder if I've changed this past year? I probably have. At least as much as to make Komachi happy. I guess even I can change. If even I can, then my little sister..."
    hide komachiHachimanDup with dissolve
    voice "audio/voice/E5/SAK/06/HA/HA005.ogg"
    hachiman "Say, Komachi..."
    voice "audio/voice/E5/SAK/06/KO/KO006.ogg"
    komachi "Hm? What, onii-chan?"
    voice "audio/voice/E5/SAK/06/HA/HA006.ogg"
    hachiman "...Don't grow up too fast."
    voice "audio/voice/E5/SAK/06/KO/KO007.ogg"
    komachi "What're you on about? You sound like dad, Onii-chan. It's gross."
    voice "audio/voice/E5/SAK/06/HA/HA007.ogg"
    hachiman "Rude..."
    voice "audio/voice/E5/SAK/06/KO/KO008.ogg"
    komachi "...Don't worry, Onii-chan. Komachi'll always be your little sister."
    window auto hide dissolve
    show komachiHachimanDup at center with dissolve:
        zoom 1.3 yoffset 325 xoffset -50
    window auto show dissolve
    "Komachi said as she peeked at me, smilling happily."
    voice "audio/voice/E5/SAK/06/KO/KO009.ogg"
    komachi "Ah, that was suuuper high in Komachi points!"
    hachiman "(Yeah, it was up there.)"
    voice "audio/voice/E5/SAK/06/HA/HA008.ogg"
    hachiman "Komachi, let's go on a trip again sometime."
    voice "audio/voice/E5/SAK/06/KO/KO010.ogg"
    komachi "Sure. I've already planned to see you grow old, so I'll be there with you forever!"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    show white with Fade(2.0, 0, 1.0, color="#fff")
    $renpy.movie_cutscene("movies/ed04.mkv")
    jump E5_SAK_07

label E5_SAK_07:
    scene houseA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM08.ogg"
    window auto show dissolve
    "As Komachi's exams were over and we came back from the trip, we returned to the stupor of waiting for our new life which only the graduation ceremony and a short spring break seperated us from."
    "I say waiting, but there was a kind of anxiousness in the air. The kind facing an anxiety inducing season like spring brings."
    show komachi athletic mid_center vhappy at center with dissolve:
        xoffset -75 yoffset 75
    voice "audio/voice/E5/SAK/07/KO/KO000.ogg"
    komachi "The onsen was so fun..."
    "Komachi said as she leisurely sipped her tea. The nerve-wracking atmosphere she was radiating just recently was nowhere to be seen."
    voice "audio/voice/E5/SAK/07/HA/HA000.ogg"
    hachiman "...I know, right?"
    show komachi happy with dissolve
    voice "audio/voice/E5/SAK/07/KO/KO001.ogg"
    komachi "But..."
    voice "audio/voice/E5/SAK/07/HA/HA001.ogg"
    hachiman "Hm?"
    show komachi vhappy with dissolve
    voice "audio/voice/E5/SAK/07/KO/KO002.ogg"
    komachi "Home is still the best. You feel at ease."
    "How long will Komachi think this way? I ended up somehow thinking something a dad would."
    voice "audio/voice/E5/SAK/07/HA/HA002.ogg"
    hachiman "Is it now?"
    hachiman "(Well, as long as Komachi's happy, that's good enough for me.)"
    show komachi happy with dissolve
    voice "audio/voice/E5/SAK/07/KO/KO003.ogg"
    komachi "Yeah."
    voice "audio/voice/E5/SAK/07/HA/HA003.ogg"
    hachiman "........."
    voice "audio/voice/E5/SAK/07/KO/KO004.ogg"
    komachi "........."
    play sound "audio/sfx/SE01/SE01_02.ogg"
    "It feels like forever ago we could last let time go by slowly like this. And so, Komachi suddenly jumped up."
    stop sound
    stop music
    show komachi athletic near_center angry at center with dissolve:
        xoffset 35 yoffset 75
    voice "audio/voice/E5/SAK/07/KO/KO005.ogg"
    komachi "Right!"
    voice "audio/voice/E5/SAK/07/HA/HA004.ogg"
    hachiman "Huh?"
    play sound "audio/sfx/SE00/SE00_31.ogg"
    hide komachi with dissolve
    voice "audio/voice/E5/SAK/07/KO/KO006.ogg"
    komachi "Hold on a second!"
    hachiman "(What's she on about all of a sudden...?)"
    stop sound fadeout 0.5
    "In no time at all, a pair of restless footsteps could be heard coming back to the living room."
    voice "audio/voice/E5/SAK/07/KO/KO007.ogg"
    komachi "Hey, look, Onii-chan!"
    window auto hide dissolve
    scene komachiSchoolA with Dissolve(1.0)
    window auto show dissolve
    play music "audio/bgm/BGM50.ogg"
    voice "audio/voice/E5/SAK/07/HA/HA005.ogg"
    hachiman "Ah..."
    "There stood Komachi, in a Sobu High uniform they just finished tailoring for her."
    voice "audio/voice/E5/SAK/07/KO/KO008.ogg"
    komachi "Ta-dah! How is it? Does it look good on me?"
    voice "audio/voice/E5/SAK/07/HA/HA006.ogg"
    hachiman ".........."
    "It was a little baggy for her, and it still felt like she was a rookie who hadn't gotten used to her uniform yet. But anyway, she was extremely cute."
    hachiman "(No, we're not talking just cute anymore. This is godlike. She might get assaulted immediately if she wore this outside."
    voice "audio/voice/E5/SAK/07/KO/KO009.ogg"
    komachi "Onii---chan?"
    voice "audio/voice/E5/SAK/07/HA/HA007.ogg"
    hachiman "Insanely cute, seriously cute, cutest in the world."
    voice "audio/voice/E5/SAK/07/KO/KO010.ogg"
    komachi "I was asking if it suited me though. And you're praising too much, it's creepy."
    show komachiSchoolB with dissolve
    voice "audio/voice/E5/SAK/07/KO/KO011.ogg"
    komachi "But I'm really happy I got this Sobu High uniform! Komachi's always wanted to wear this!"
    voice "audio/voice/E5/SAK/07/HA/HA008.ogg"
    hachiman "Yeah."
    "I've never once been excited to wear my school's uniform, and I think that's mostly how people feel, but for some people, it's a sign of something they've always yearned after. Komachi just made me realize this all over again."
    voice "audio/voice/E5/SAK/07/HA/HA009.ogg"
    hachiman "Say, Komachi, what do you want to do when you get into high school?"
    voice "audio/voice/E5/SAK/07/KO/KO012.ogg"
    komachi "I wanna join the Service Club! I wanna be together in a club with Yukino-san and Yui-san!"
    hide komachiSchoolB with dissolve
    voice "audio/voice/E5/SAK/07/KO/KO013.ogg"
    komachi "Ah, but I'll be with Onii-chan even at school if I do that."
    voice "audio/voice/E5/SAK/07/HA/HA010.ogg"
    hachiman "Komachi, I'll say it now, but we're 3rd years, so I don't know what'll happen to the Service Club when we leave."
    voice "audio/voice/E5/SAK/07/KO/KO014.ogg"
    komachi "Ah. I see... But Komachi wants the club to go on. Even if Onii-chan isn't there."
    voice "audio/voice/E5/SAK/07/HA/HA011.ogg"
    hachiman "Even when I'm not there? Is there anything else you want to do besides club activites?"
    "I was curious, so I asked on a whim."
    voice "audio/voice/E5/SAK/07/KO/KO015.ogg"
    komachi "Komachi won't do anything she doesn't want to!"
    show komachiSchoolB with dissolve
    voice "audio/voice/E5/SAK/07/KO/KO016.ogg"
    komachi "Komachi's all excited just getting to go to school with this cute uniform!"
    voice "audio/voice/E5/SAK/07/KO/KO017.ogg"
    komachi "I can't wait for April."
    voice "audio/voice/E5/SAK/07/HA/HA012.ogg"
    hachiman "...Yeah."
    "That's how I truly felt. Come to think of it, this is the first time I've looked forward to a new semester."
    window auto hide dissolve
    stop voice
    stop music fadeout 2.0
    scene komachiEnd with Fade(2.0, 1.0, 1.0, color="#fff")
    call game_over("Hikigaya Komachi") from _call_game_over_10
    return
