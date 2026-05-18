label E4_SHI_01:
    $chocoEventHelp = "hiratsuka"
    scene kitchenA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM40.ogg"
    window auto show dissolve
    "At least from where I stood, the event seemed to be going on smoothly."
    window auto hide dissolve
    scene kitchenA at truecenter:
        zoom 1.45 xoffset -2.5 yoffset -12.5
    show yumiko school mid_center vhappy at left:
        xoffset 125 yoffset 75
    show yukino school mid_left happy at right:
        xoffset -170 yoffset 80
    with dissolve
    window auto show dissolve
    voice "audio/voice/E4/SHI/01/YM/YM000.ogg"
    yumiko "Chocolate actually seems pretty easy to make. I think I'll start making it more often."
    show yukino vhappy with dissolve
    voice "audio/voice/E4/SHI/01/YK/YK000.ogg"
    yukino "It's not too hard. It's simple once you get the hang of it. As long as you get the basics down, you can really get creative."
    show yumiko blush with dissolve
    voice "audio/voice/E4/SHI/01/YM/YM001.ogg"
    yumiko "Well thanks... for doing this... I guess."
    window auto hide dissolve
    image tobe_flat = Flatten("tobe school mid surprised")
    $renpy.pause(delay=0.25,hard=True)
    scene kitchenA at truecenter:
        zoom 1.45 xalign 0 yoffset -15
    show hayama school mid_center happy at center:
        xoffset 5 yoffset 75
    with dissolve
    $renpy.pause(delay=0.25,hard=True)
    show tobe_flat at left behind hayama:
        xoffset -25 yoffset 75 alpha 0
        parallel:
            linear 0.25 xoffset 10
        parallel:
            linear 0.25 alpha 1.0
    $renpy.pause(delay=0.25,hard=True)
    hide tobe_flat
    show tobe school mid surprised at left behind hayama:
        xoffset 10 yoffset 75
    window auto show dissolve
    voice "audio/voice/E4/SHI/01/TB/TB000.ogg"
    tobe "Hayato-kun, you're too popular! It's like you're running a harem, dude."
    show hayama relieved with dissolve
    voice "audio/voice/E4/SHI/01/HY/HY000.ogg"
    hayama "Ahaha, Tobe, you're blowing things up."
    image ebina_flat = Flatten("ebina school mid_left vhappy")
    show ebina_flat at right behind hayama:
        xoffset -125 yoffset 70 alpha 0
        parallel:
            linear 0.25 xoffset -190
        parallel:
            linear 0.25 alpha 1.0
    $renpy.pause(delay=0.25,hard=True)
    hide ebina_flat
    show ebina school mid_left vhappy at right behind hayama:
        xoffset -190 yoffset 70
    voice "audio/voice/E4/SHI/01/EB/EB000.ogg"
    ebina "Don't worry, Tobe. Hikitani-kun is what completes the harem for Hayama-kun! He has eyes only for him!"
    show tobe sad with dissolve
    voice "audio/voice/E4/SHI/01/TB/TB001.ogg"
    tobe "That's even worse, man."
    show tobe vhappy with dissolve
    voice "audio/voice/E4/SHI/01/TB/TB002.ogg"
    tobe "But Ebina-san, there's this sweeeet smell coming from your spot~."
    hachiman "(Oh, what a proactive appeal from Tobe.)"
    show ebina relieved with dissolve
    voice "audio/voice/E4/SHI/01/EB/EB001.ogg"
    ebina "Buhu! It's coming from the overflowing, piping hot HayaHachi love...!"
    show tobe sad with dissolve
    hachiman "(What a full-rot deflectio form Ebona-san. Poor Tobe."
    voice "audio/voice/E4/SHI/01/HY/HY001.ogg"
    hayama "Hahaha..."
    hachiman "(A-Anyway, better not wander too close.)"
    window auto hide dissolve
    scene kitchenA with dissolve
    window auto show dissolve
    "I have no intention of disavowing their status quo, but watching them somehow makes me feel tired and kind of empty inside."
    hachiman "(I wouldn't say it's entirely exhausting and no fun at all, but...)"
    window auto hide dissolve
    $renpy.pause(delay=0.5,hard=True)
    play sound "audio/sfx/SE04/SE04_01_.ogg"
    $renpy.pause(delay=0.75,hard=True)
    scene kitchenA at truecenter:
        zoom 1.45 xalign 1.0 yoffset -15
    with dissolve
    $renpy.pause(delay=1.25,hard=True)
    stop music fadeout 0.5
    play music "audio/bgm/BGM26.ogg"
    show hiratsuka school mid_left happy at center with dissolve:
        xoffset 110 yoffset 80
    voice "audio/voice/E4/SHI/01/SZ/SZ000.ogg"
    hiratsuka "Hey. Sorry I'm late."
    voice "audio/voice/E4/SHI/01/HA/HA000.ogg"
    hachiman "Ah, Sensei..."
    voice "audio/voice/E4/SHI/01/SZ/SZ001.ogg"
    hiratsuka "You did a good job on this. The whole room is filled with a sweet smell, I guess that's what you would call the spirit of youth!"
    voice "audio/voice/E4/SHI/01/HA/HA001.ogg"
    hachiman "Haha... I think you're a little late to that party too, Sensei."
    show hiratsuka mid_center angry with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E4/SHI/01/SZ/SZ002.ogg"
    hiratsuka "And what exactly does that mean? As your teacher, I order you to answer in 50 words or less."
    voice "audio/voice/E4/SHI/01/HA/HA002.ogg"
    hachiman "No, I didn't mean it in the way you're thining at all. I just thought it would be sad to talk like you're already past your youth."
    show hiratsuka blush with dissolve
    voice "audio/voice/E4/SHI/01/SZ/SZ003.ogg"
    hiratsuka "I-I see... Yes, that was 50 words exactly."
    voice "audio/voice/E4/SHI/01/HA/HA003.ogg"
    hachiman "Yep."
    show hiratsuka pout with dissolve
    voice "audio/voice/E4/SHI/01/SZ/SZ004.ogg"
    hiratsuka "......"
    voice "audio/voice/E4/SHI/01/HA/HA004.ogg"
    hachiman "......"
    hachiman "(Somebody please take her already...)"
    show hiratsuka mid_left frown with dissolve:
        xoffset 110 yoffset 80
    voice "audio/voice/E4/SHI/01/SZ/SZ005.ogg"
    hiratsuka "Nevermind that, I've brought some reference material that might be helpful."
    voice "audio/voice/E4/SHI/01/HA/HA005.ogg"
    hachiman "What is it?"
    show hiratsuka happy with dissolve
    voice "audio/voice/E4/SHI/01/SZ/SZ006.ogg"
    hiratsuka "...Fufufu. Rejoice! This is my gift to you."
    voice "audio/voice/E4/SHI/01/HA/HA006.ogg"
    hachiman "Huh?"
    "With that, she gave me a box of chocolate by a luxury brand that even I'd heard of before."
    hachiman "(Oh, this is amazing. Even something like this is your hobby.)"
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E4/SHI/01/SZ/SZ007.ogg"
    hiratsuka "Everyone, accept my gift to you!"
    window auto hide dissolve
    stop voice
    scene kitchenA with dissolve
    play sound "audio/sfx/SE05/SE05_13.ogg"
    $renpy.pause(delay=2.5,hard=True)
    window auto show dissolve
    "Not only the boys, but everyone in the room got excited at Hiratsuka-sensei's words. She was as generous and gallant as ever."
    show totsuka athletic mid_right happy at left:
        xoffset 270 yoffset 85
    show hiratsuka school mid_left happy at right:
        xoffset -15 yoffset 80
    with dissolve
    stop sound
    voice "audio/voice/E4/SHI/01/SZ/SZ008.ogg"
    hiratsuka "Hikigaya, Totsuka. Would you bring everyone their share?"
    show totsuka vhappy with dissolve
    voice "audio/voice/E4/SHI/01/SI/SI000.ogg"
    totsuka "Roger!"
    hide totsuka
    hide hiratsuka
    with dissolve
    show meguri school mid happy at center with dissolve:
        xoffset 20 yoffset 75
    voice "audio/voice/E4/SHI/01/MG/MG000.ogg"
    meguri "Oh, I'll help too~."
    "Meguri-senpai quickly divided the chocolates into plates, stopping to think for a moment before flashing a smile and handing them to us."
    hide meguri with dissolve
    show totsuka athletic near_right happy at left:
        xoffset 95 yoffset 90
    show meguri school near vhappy at right:
        xoffset -105 yoffset 75
    with dissolve
    voice "audio/voice/E4/SHI/01/MG/MG001.ogg"
    meguri "Alright! Let's go hand them out!"
    voice "audio/voice/E4/SHI/01/HA/HA007.ogg"
    hachiman "Ah... sure."
    window auto hide dissolve
    stop voice
    scene kitchenA with Fade(0.75, 0.25, 0.75)
    window auto show dissolve
    "After handing out each table their plate, I went over to Hiratsuka-sensei to report."
    show hiratsuka school mid_center happy at center with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E4/SHI/01/HA/HA008.ogg"
    hachiman "We're pretty much finished handing them out. Weren't the pretty expensive?"
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E4/SHI/01/SZ/SZ009.ogg"
    hiratsuka "Come on, this only happens once a year. This is nothing."
    show hiratsuka happy with dissolve
    voice "audio/voice/E4/SHI/01/SZ/SZ010.ogg"
    hiratsuka "The event's been going well."
    voice "audio/voice/E4/SHI/01/HA/HA009.ogg"
    hachiman "Yeah, that's true..."
    "To be honest, I don't know if I can really agree with Hiratsuka-sensei. In my mind, it's just like a condensed version of all the tangled relationship we have."
    window auto hide dissolve
    $renpy.pause(delay=0.25,hard=True)
    scene kitchenA at truecenter:
        zoom 1.45 xoffset -2.5 yoffset -12.5
    show yukino school mid_center happy at left:
        xoffset -105 yoffset 75
    show yui school mid_center pout at center:
        xoffset -25 yoffset 75
    show haruno sweater mid_left sly at right:
        xoffset -110 yoffset 75
    with dissolve
    $renpy.pause(delay=0.25,hard=True)
    play music "audio/bgm/BGM35.ogg"
    window auto show dissolve
    voice "audio/voice/E4/SHI/01/HR/HR000.ogg"
    haruno "Hey, Yukino-chan, aren't you going to give someone chocolate~?"
    show yukino frown with dissolve
    voice "audio/voice/E4/SHI/01/YK/YK001.ogg"
    yukino "That's none of your business. Why don't you go back to your table?"
    show haruno happy with dissolve
    voice "audio/voice/E4/SHI/01/HR/HR001.ogg"
    haruno "You're so cold, Yukino-chan~. How about you, Ghama-chan?"
    voice "audio/voice/E4/SHI/01/YI/YI000.ogg"
    yui "Ahaha... Yukinon seems like she's having a pretty hard time teaching me."
    show haruno vhappy with dissolve
    voice "audio/voice/E4/SHI/01/HR/HR002.ogg"
    haruno "Hm? That's not what I meant. I mean how about you give someone chocolate~?"
    voice "audio/voice/E4/SHI/01/YI/YI001.ogg"
    yui "I-I'm not really... thinking about that..."
    show haruno happy with dissolve
    voice "audio/voice/E4/SHI/01/HR/HR003.ogg"
    haruno "Oh, is that right? Then how about I give Hikigaya-kun some...?"
    hachiman "(Say what!?)"
    show yukino surprised
    show yui surprised
    with dissolve
    voice "audio/voice/E4/SHI/01/MI/MIX000.ogg"
    yukandyui "......"
    window auto hide dissolve
    scene kitchenA at truecenter:
        zoom 1.45 xalign 0 yoffset -15
    show hayama school mid_right surprised at center:
        xoffset -25 yoffset 65
    with dissolve
    window auto show dissolve
    voice "audio/voice/E4/SHI/01/HY/HY002.ogg"
    hayama "......"
    window auto hide dissolve
    $renpy.pause(delay=0.25,hard=True)
    scene kitchenA at truecenter:
        zoom 1.45 xoffset -2.5 yoffset -12.5
    show yukino school mid_center surprised at left:
        xoffset -105 yoffset 75
    show yui school mid_center surprised at center:
        xoffset -25 yoffset 75
    show haruno sweater mid_left sly at right:
        xoffset -110 yoffset 75
    with dissolve
    $renpy.pause(delay=0.25,hard=True)
    window auto show dissolve
    voice "audio/voice/E4/SHI/01/HR/HR004.ogg"
    haruno "Or if I did, what would you do?"
    show yukino pout with dissolve
    voice "audio/voice/E4/SHI/01/YK/YK003.ogg"
    yukino "D-Do what you will, I don't care."
    show yui happy with dissolve
    voice "audio/voice/E4/SHI/01/YI/YI003.ogg"
    yui "A-Ahah. I'd be a little surprised, I guess."
    hachiman "(That's what I should be saying...!)"
    show haruno happy with dissolve
    voice "audio/voice/E4/SHI/01/HR/HR005.ogg"
    haruno "Well, it's most fun when things are still not set in stone, you know?"
    show yukino pout
    show yui pout
    with dissolve
    voice "audio/voice/E4/SHI/01/YI/YI004.ogg"
    yui "......"
    voice "audio/voice/E4/SHI/01/YK/YK004.ogg"
    yukino "......"
    image kitchenDup = "images/bg/BG36A.jpg"
    show kitchenDup with dissolve
    hachiman "(As always, Haruno-san puts a strain on the mood everywhere she goes. Or rather, she puts a strain on my peace of mind.)"
    window auto hide dissolve
    $renpy.pause(delay=0.25,hard=True)
    scene kitchenA at truecenter:
        zoom 1.45 xalign 1.0 yoffset -15
    show totsuka athletic mid_center vhappy at left:
        xoffset 135 yoffset 75
    show keika home mid happy at center:
        xoffset -25 yoffset 75
    show saki school mid_left happy at right:
        xoffset 30 yoffset 75
    with dissolve
    $renpy.pause(delay=0.5,hard=True)
    play music "audio/bgm/BGM17.ogg"
    window auto show dissolve
    voice "audio/voice/E4/SHI/01/SI/SI001.ogg"
    totsuka "Ah, you're so good for being so small."
    show keika frown with dissolve
    voice "audio/voice/E4/SHI/01/KE/KE000.ogg"
    keika "Keika's not small!"
    show totsuka mid_right pout with dissolve:
        xoffset 145 yoffset 85
    voice "audio/voice/E4/SHI/01/SI/SI002.ogg"
    totsuka "Ahaha, that's right. Sorry, Keika-chan."
    hide saki
    $url = ["saki school mid_left sad", "saki school mid_left unimpressed"]
    $multiImagePara = [30, 75, 0, 0, 2.2]
    call multiImage(1) from _call_multiImage_24
    voice "audio/voice/E4/SHI/01/SA/SA000.ogg"
    saki "Hey now, Kei-chan. Sorry about my little sister."
    call finishmultiImage from _call_finishmultiImage_25
    show saki school mid_left unimpressed at right:
        xoffset 30 yoffset 75
    voice "audio/voice/E4/SHI/01/SI/SI003.ogg"
    totsuka "Not at all. Ah, I'm Totsuka Saika, a friend of your big sister. Nice to meet you."
    hide keika
    $url = ["keika home mid pout", "keika home mid vhappy"]
    $multiImagePara = [-25, 75, 0, 0, 3.25]
    call multiImage() from _call_multiImage_25
    voice "audio/voice/E4/SHI/01/KE/KE001.ogg"
    keika "Saa-chan... sa... Sai-chan!"
    call finishmultiImage from _call_finishmultiImage_26
    show keika home mid vhappy at center:
        xoffset -25 yoffset 75
    show totsuka vhappy with dissolve
    voice "audio/voice/E4/SHI/01/SI/SI004.ogg"
    totsuka "Yep, that's right."
    hachiman "(This is the only happy looking place I can see... so comforting...)"
    window auto hide dissolve
    scene kitchenA
    show hiratsuka school mid_left happy at center:
        xoffset 110 yoffset 80
    with dissolve
    window auto show dissolve
    voice "audio/voice/E4/SHI/01/SZ/SZ011.ogg"
    hiratsuka "Well, I'm glad to see they're having fun."
    voice "audio/voice/E4/SHI/01/HA/HA010.ogg"
    hachiman "Having... fun..."
    "Hiratsuka-sensei's words brought me back to reality, and I was surprised at the bitter tone of my own words."
    voice "audio/voice/E4/SHI/01/HA/HA011.ogg"
    hachiman "I hope they don't just look like they're having fun..."
    show hiratsuka pout with dissolve
    voice "audio/voice/E4/SHI/01/SZ/SZ012.ogg"
    hiratsuka "...Don't say that. You planned this event yourself. What it becomes should be entirely reliant on your own expectations."
    voice "audio/voice/E4/SHI/01/HA/HA012.ogg"
    hachiman "Well, I guess you're right."
    show hiratsuka mid_center angry with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E4/SHI/01/SZ/SZ013.ogg"
    hiratsuka "Well, you're somebody who doesn't know other well to begin with. And the people you've been involved don't really know you either. It's only natural."
    "With  a cool face, Hiratsuka-sense brushed aside my vague feelings. It's strange that I feel lighter when she said that."
    voice "audio/voice/E4/SHI/01/HA/HA013.ogg"
    hachiman "\"Don't know me\"... isn't that a bit harsh?"
    show hiratsuka happy with dissolve
    voice "audio/voice/E4/SHI/01/SZ/SZ014.ogg"
    hiratsuka "Well, let's say I've come to understand these things more than I used to, probably."
    voice "audio/voice/E4/SHI/01/HA/HA014.ogg"
    hachiman "Probably?"
    show hiratsuka angry with dissolve
    voice "audio/voice/E4/SHI/01/SZ/SZ015.ogg"
    hiratsuka "Your impression of people changes the more you know them. You'll understand it if you spend time together and keep growing together."
    voice "audio/voice/E4/SHI/01/HA/HA015.ogg"
    hachiman "I don't feel like I'm growing. I've been the same as always."
    show hiratsuka happy with dissolve
    voice "audio/voice/E4/SHI/01/SZ/SZ016.ogg"
    hiratsuka "Still, some things do change."
    voice "audio/voice/E4/SHI/01/HA/HA016.ogg"
    hachiman "I guess... they do change. Hearing you say that, it makes me feel some kind of way."
    hide hiratsuka with dissolve
    show hiratsuka school near_center surprised at center with dissolve:
        xoffset 30 yoffset 75
    voice "audio/voice/E4/SHI/01/SZ/SZ017.ogg"
    hiratsuka "Some kind of way?"
    voice "audio/voice/E4/SHI/01/HA/HA017.ogg"
    hachiman "......"
    "She examined my face up close, and I felt embarrassed, so I turn my head away and kept talking."
    stop music fadeout 0.5
    voice "audio/voice/E4/SHI/01/HA/HA018.ogg"
    hachiman "Ah, I just... feel strange, uncomfortable in a way."
    play music "audio/bgm/BGM10.ogg"
    "When I put it into words, it became clearer to me than I expected."
    "Lately, I find myself feeling that way for a moment, unexpectedly - something very different from what I have been feeling up until now. Every time I come in contact with someone, the question arises - "
    "\"Is this how I really feel?\"."
    hachiman "(That's right. Not knowing how I truly feel, I guess you could say that.)"
    "As if reading my mind, I thought I saw Hiratsuka-sensei let show a smile."
    hide hiratsuka with dissolve
    show hiratsuka school mid_center angry at center with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E4/SHI/01/SZ/SZ018.ogg"
    hiratsuka "You feel uncomfortable... I want you to remember that feeling."
    show hiratsuka happy with dissolve
    voice "audio/voice/E4/SHI/01/SZ/SZ019.ogg"
    hiratsuka "I think it's a clear sign of growth in you. As you grow older, you're going to learn to roll with it."
    show hiratsuka mid_left happy at center with dissolve:
        xoffset 110 yoffset 80
    voice "audio/voice/E4/SHI/01/SZ/SZ020.ogg"
    hiratsuka "So, right now, I want you to get to know that uncomfortable feeling. It's very important that you do."
    voice "audio/voice/E4/SHI/01/HA/HA019.ogg"
    hachiman "...Right."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E4/SHI/01/SZ/SZ021.ogg"
    hiratsuka "Keep thinking about that feeling."
    voice "audio/voice/E4/SHI/01/HA/HA020.ogg"
    hachiman "Keep... thinking about it?"
    show hiratsuka happy with dissolve
    voice "audio/voice/E4/SHI/01/SZ/SZ022.ogg"
    hiratsuka "Yes. Always. Maybe one day you'll come to understand it. You don't see how far you've come until you look back."
    voice "audio/voice/E4/SHI/01/SZ/SZ023.ogg"
    hiratsuka "Those who stop growing often feel like they've betrayed the progress they've made in the past."
    show hiratsuka sad with dissolve
    voice "audio/voice/E4/SHI/01/SZ/SZ024.ogg"
    hiratsuka "It's good I can keep close track of it now, but... I won't be able to do it forever."
    voice "audio/voice/E4/SHI/01/HA/HA021.ogg"
    hachiman "Huh?"
    "Hiratsuka-sensei's last words stuck with me in a strange way. She didn't say anything else after that, just looked at the venue in front of her with gaze that looked emotional."
    window auto hide dissolve
    stop music fadeout 0.5
    jump E4_CMM_05

label E4_SHI_02:
    "By various things, towards the end of the Valentine's Day Event, I was feeling a bit overwhelmed."
    hachiman "(Ugh... I somehow made it through using corporate slave willpower. I'm exhasted, though... both physically and mentally.)"
    show yui school_sunset mid_center surprised at center:
        xoffset -25 yoffset 75
    voice "audio/voice/E4/SHI/02/YI/YI000.ogg"
    yui "Huh? Hikki, you look kind of pale. Are you okay?"
    voice "audio/voice/E4/SHI/02/HA/HA000.ogg"
    hachiman "I think I'll take a breather outside."
    window auto hide dissolve
    stop voice
    scene skyB with Fade(1.0, 0.5, 1.0)
    play sound "audio/sfx/SE01/SE01_77.ogg"
    $renpy.pause(delay=1.0, hard=False)
    play sound "audio/sfx/SE01/SE01_76.ogg"
    $renpy.pause(delay=0.5, hard=False)
    show parkB with dissolve
    hachiman "(Fu~. Just what I needed.)"
    hachiman "(I'll chill out here for a bit...)"
    "It wasn't just the work that tired me out, it was probably all the interpersonal relationships involved. Thinking about it, I didn't want to go back yet."
    window auto hide dissolve
    play sound "<to 1.5>audio/sfx/SE00/SE00_34.ogg"
    $renpy.pause(delay=1.25, hard=False)
    show hiratsuka coat_sunset mid_center pout at center with dissolve:
        xoffset 40 yoffset 75
    play music "audio/bgm/BGM42.ogg"
    window auto show dissolve
    voice "audio/voice/E4/SHI/02/SZ/SZ000.ogg"
    hiratsuka "What's wrong, Hikigaya? You aren't looking too good... are you feeling sick?"
    voice "audio/voice/E4/SHI/02/HA/HA001.ogg"
    hachiman "Yeah, a little bit... I'm fine now, though."
    show hiratsuka happy with dissolve
    voice "audio/voice/E4/SHI/02/SZ/SZ001.ogg"
    hiratsuka "Well, you did have your plate full. Don't overdo it."
    voice "audio/voice/E4/SHI/02/HA/HA002.ogg"
    hachiman "Are you leaving already?"
    "Hiratsuka-sensei was being unsually kind and so I felt like I didn't want her to leave. I couldn't help but ask."
    show hiratsuka pout with dissolve
    voice "audio/voice/E4/SHI/02/SZ/SZ002.ogg"
    hiratsuka "Yeah, I've got a lot of stuff I need to get done before March, so I'll be pretty busy."
    voice "audio/voice/E4/SHI/02/HA/HA003.ogg"
    hachiman "I see."
    show hiratsuka happy with dissolve
    voice "audio/voice/E4/SHI/02/SZ/SZ003.ogg"
    hiratsuka "I said it before, but everyone pitched in and turned out to be great event, didn't it? It looks like they even decided on a ski trip."
    "As I recalled the interactions that took place back inside, I couldn't honestly think so. However, I was hesitant to say it out loud."
    "That discomfort that I thought had melted away just came back with a vengeance because of the ski trip."
    "As if I was open book to her, Hiratsuka-sensei gave me a small sigh and smiled gently at me."
    show hiratsuka mid_left happy with dissolve:
        xoffset 110 yoffset 80
    voice "audio/voice/E4/SHI/02/SZ/SZ004.ogg"
    hiratsuka "Just getting to the bottom of everything is not the most crucial thing of all. Having a truce once a while is just as important."
    voice "audio/voice/E4/SHI/02/HA/HA004.ogg"
    hachiman "A truce...?"
    hachiman "(I rather feel like I'm in the midst of a battle, though...)"
    voice "audio/voice/E4/SHI/02/SZ/SZ005.ogg"
    hiratsuka "Well, don't fret over it too much. You have a ski trip to look forward to."
    voice "audio/voice/E4/SHI/02/HA/HA005.ogg"
    hachiman "Well that's a bummer, isn't it..."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E4/SHI/02/SZ/SZ006.ogg"
    hiratsuka "Hahaha. This much is nothing. Someday, this will become become part of part of your youth."
    voice "audio/voice/E4/SHI/02/HA/HA006.ogg"
    hachiman "I... see."
    show hiratsuka mid_center happy with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E4/SHI/02/SZ/SZ007.ogg"
    hiratsuka "Well, I think you did a good job this time. You should be proud of yourself. Go home and get some rest. I'll see you later."
    voice "audio/voice/E4/SHI/02/HA/HA007.ogg"
    hachiman "Later."
    hide hiratsuka with dissolve
    play sound "audio/sfx/SE00/SE00_34.ogg"
    $renpy.pause(delay=0.25, hard=False)
    stop sound fadeout 2.0
    "As I watched her walk away with a dashing step, I found myself thinking - What was her youth like?"
    window auto hide dissolve
    stop music fadeout 0.5
    jump E5_CMM_01
