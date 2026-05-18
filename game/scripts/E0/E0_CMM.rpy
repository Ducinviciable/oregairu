label start:
    stop music
    scene skyA with Fade(1.0, 0.5, 1.0)
    "Youth is full of lies and evil. Sometimes you walk right past it, but you always cross paths and it's always just beyond the pale, and before you know it, it's over and done with."
    "If I had to compare it to something, it's like Kantan's Pillow. An empty dream. T/N: Kantan's pillow is a Noh play about 50 years of glory turning out to be just a dream in a nap."
    "Just like a fleeting dream you'd see when you dose off. Like I'm doing right now in my house around New Years."
    "Wrapped in the bright and warm sunlight while taking a nap, dreaming, you remembering those oh-so-transient days you can't go back to. That's exactly what youth is."
    "It's not something you'd generally go out of your way to talk about on your own, but I've got so much time under my belt, I'm telling whoever is asking."
    "For example, if on a sunny day on the veranda, you were asked \"What was your youth like?\"..."
    "You would surely puff out your chest and say this:"
    "\"As expected, my youth was...\""
    scene black with Fade(1.0, 0.5, 1.0)
    $renpy.movie_cutscene("movies/op.mkv")
    with Fade(0, 0.5, 1)
    #$renpy.music.set_volume(0.5, delay=0, channel=u'ambient')
    #$renpy.music.set_volume(0.5, delay=0, channel=u'footsteps')
    play sound "audio/sfx/SE07/SE07_03.ogg"
    $renpy.pause(delay=2, hard=True)
    "The birds are singing."
    voice "audio/voice/E0/CMM/KO/KO00.ogg"
    mystery "-chan? What are you saying?"
    window auto hide dissolve
    stop voice
    show magomachiScene with dissolve:
        zoom 2.0 xoffset -760 yoffset -740
    window auto show dissolve
    play music "audio/bgm/BGM10.ogg"
    voice "audio/voice/E0/CMM/HA/HA00.ogg"
    hachiman "Ah, Komachi. Welcome back."
    voice "audio/voice/E0/CMM/KO/KO01.ogg"
    mystery "Komachi? I'm not Komachi. I'm Komachi's granddaughter. So I'm Magomachi! T/N: Grand-daughter Komachi."
    voice "audio/voice/E0/CMM/HA/HA01.ogg"
    hachiman "Magomachi...? You're not Komachi? Wait, Komachi's grand-daughter?"
    voice "audio/voice/E0/CMM/KO/KO02.ogg"
    magomachi "Why are you so surprised? You're being kind of weird, Ojii-chan."
    voice "audio/voice/E0/CMM/HA/HA02.ogg"
    hachiman "O-ojii-chan?"
    voice "audio/voice/E0/CMM/KO/KO03.ogg"
    magomachi "Yup, yup! Technically, I'm Grandma Komachi's granddaughter, so you're not actually my grandpa, but... What was it again? Well, it doesn't matter!"
    voice "audio/voice/E0/CMM/HA/HA03.ogg"
    hachiman "It does matter though..."
    hide magomachiScene
    show magomachiScene
    with dissolve
    voice "audio/voice/E0/CMM/KO/KO04.ogg"
    magomachi "Ojii-chan... Have you forgotten about Magomachi?"
    voice "audio/voice/E0/CMM/HA/HA04.ogg"
    hachiman "N-No... Now that you mention it, it feels like it's true... No, it has to be true... Yup, no doubt it's true!"
    voice "audio/voice/E0/CMM/KO/KO05.ogg"
    magomachi "Why are you suddenly talking like an old man?"
    voice "audio/voice/E0/CMM/HA/HA05.ogg"
    hachiman "Because I am an old man."
    voice "audio/voice/E0/CMM/KO/KO06.ogg"
    magomachi "Ah, okay... But I'm glad that you remembered! I would've cried if you'd forgotten."
    voice "audio/voice/E0/CMM/HA/HA06.ogg"
    hachiman "Oh, sorry about that..."
    voice "audio/voice/E0/CMM/KO/KO07.ogg"
    magomachi "I cry over the possibility that you'll need to be cared for forever. That feels so real it's hard, and I wish you'd spare me from that."
    voice "audio/voice/E0/CMM/HA/HA07.ogg"
    hachiman "Hmmmm. That kind of complaining... You're undoubtedly Komachi's granddaughter. More importantly, Magomachi, when are we eating?"
    voice "audio/voice/E0/CMM/KO/KO08.ogg"
    magomachi "Ojii-chan, if you mean rice, you ate that last week."
    voice "audio/voice/E0/CMM/HA/HA08.ogg"
    hachiman "I'd like to eat it everyday if I could."
    voice "audio/voice/E0/CMM/KO/KO09.ogg"
    magomachi "Alright, then let's eat after we finish talking."
    window auto hide dissolve
    stop voice
    show magomachiScene:
        zoom 1.6 xalign 0 yalign 0
    with dissolve
    window auto show dissolve
    voice "audio/voice/E0/CMM/HA/HA09.ogg"
    hachiman "Hmmm, talking about what?"
    voice "audio/voice/E0/CMM/KO/KO10.ogg"
    magomachi "Yeah. My homework from school is to ask an elder in the region for old stories. So tell me about when you were younger!"
    voice "audio/voice/E0/CMM/HA/HA10.ogg"
    hachiman "My younger days... When I was young, I was always throwing my weight around. What's with young people these days? I don't get them at all!"
    voice "audio/voice/E0/CMM/KO/KO11.ogg"
    magomachi "Why are you suddenly criticizing young people?"
    voice "audio/voice/E0/CMM/HA/HA11.ogg"
    hachiman "Because I'm old."
    voice "audio/voice/E0/CMM/KO/KO12.ogg"
    magomachi "It's even worse when you're self-aware about it. Do you hate young people?"
    voice "audio/voice/E0/CMM/HA/HA12.ogg"
    hachiman "I don't hate them at all. They pay off my pension."
    voice "audio/voice/E0/CMM/KO/KO13.ogg"
    magomachi "That's the worst reason ever..."
    voice "audio/voice/E0/CMM/HA/HA13.ogg"
    hachiman "Anyway, I don't get young people at all. When I was young, I always threw my weight around."
    stop music
    hide magomachiScene
    show magomachiScene
    with dissolve
    voice "audio/voice/E0/CMM/KO/KO14.ogg"
    magomachi "Ojii-chan, I've heard that already. You always talk about the same things. Wasn't there anything else from when you were young?"
    voice "audio/voice/E0/CMM/HA/HA14.ogg"
    hachiman "That burns! It's not like that. It's just takes some time to remember because I'm an old man."
    voice "audio/voice/E0/CMM/KO/KO15.ogg"
    magomachi "Okay. Magomachi's glad to hear that! Now tell me about your youth, Ojii-chan!"
    voice "audio/voice/E0/CMM/HA/HA15.ogg"
    hachiman "My youth, hey?"
    window auto hide dissolve
    play music ["<silence 2>", "audio/bgm/BGM21.ogg"]
    scene clubroomA
    with Fade(2.0, 1.0, 1.0, color="#fff")
    show yukino school near_center vhappy at center with dissolve:
        xoffset -165 yoffset 75
    $renpy.pause(delay=1.5, hard=True)
    scene clubroomA
    with Fade(2.0, 1.0, 1.0, color="#fff")
    show yui school near_center vhappy at center with dissolve:
        xoffset 10 yoffset 75
    $renpy.pause(delay=1.5, hard=True)
    scene clubroomA
    with Fade(2.0, 1.0, 1.0, color="#fff")
    show iroha school near_center blush at center with dissolve:
        xoffset -10 yoffset 75
    $renpy.pause(delay=1.5, hard=True)
    scene magomachiScene
    with Dissolve(1.0)
    window auto show dissolve
    voice "audio/voice/E0/CMM/HA/HA16.ogg"
    hachiman "Well, a lot of things happened."
    voice "audio/voice/E0/CMM/HA/HA17.ogg"
    hachiman "As expected, my youth romantic comedy is..."
    window auto hide dissolve
    stop music fadeout 1.0
    jump E1_CMM_01
