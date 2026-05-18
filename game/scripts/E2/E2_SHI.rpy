label E2_SHI_02:
    voice "audio/voice/E2/SHI/02/HA/HA000.ogg"
    hachiman "H-Hello?"
    stop music fadeout 0.5
    $renpy.pause(delay=0.5,hard=True)
    play music "audio/bgm/BGM16.ogg"
    $renpy.pause(delay=1.0,hard=True)
    voice "audio/voice/E2/SHI/02/SZ/SZ000.ogg"
    hiratsuka "It's me. Winter break is almost over, so how're you doing? I mailed you several times, but why aren't you answering?"
    voice "audio/voice/E2/SHI/02/HA/HA001.ogg"
    hachiman "...(Crap, she's tiresome to deal with, so I ignored all of her mails.)"
    "When I heard Hiratsuka-sensei's voice over the phone, I sighed in my mind. There's no doubt about it. I'm going to be involved in something troublesome now."
    hachiman "(I really shouldn't have picked up.)"
    voice "audio/voice/E2/SHI/02/SZ/SZ001.ogg"
    hiratsuka "You picked up surprisingly quickly. Well done! You saved me the trouble of calling again and again."
    hachiman "(You were going to keep calling me until I picked up!? She's terrifying!)"
    voice "audio/voice/E2/SHI/02/SZ/SZ002.ogg"
    hiratsuka "Hikigaya, are you free right now?"
    voice "audio/voice/E2/SHI/02/HA/HA002.ogg"
    hachiman "No, I'm not."
    voice "audio/voice/E2/SHI/02/SZ/SZ003.ogg"
    hiratsuka "I see. Then how many minutes from now will you be free?"
    voice "audio/voice/E2/SHI/02/HA/HA003.ogg"
    hachiman "Ah, well, I'm kinda busy the whole day, so..."
    voice "audio/voice/E2/SHI/02/SZ/SZ004.ogg"
    hiratsuka "Alright. So how many hours from now will you be free?"
    hachiman "(Once I've refused, she keeps coming with more and more proposals, so eventually I won't be able to refuse... What is she, some shady salesman? Yikes!)"
    voice "audio/voice/E2/SHI/02/HA/HA004.ogg"
    hachiman "Well, today my sister asked me to go shopping, so that's on the agenda..."
    hachiman "(If I mention my sister, she has to back off! At least for today!)"
    $renpy.pause(delay=0.5,hard=True)
    play sound "audio/sfx/SE06/SE06_03.ogg"
    $renpy.pause(delay=1.25,hard=True)
    voice "audio/voice/E2/SHI/02/SZ/SZ005.ogg"
    hiratsuka "I'll help you with that then. Great timing, I just got here."
    hachiman "(She has me cornered...)"
    voice "audio/voice/E2/SHI/02/HA/HA005.ogg"
    hachiman "Huh? What do you mean you just got here?"
    "As I thought there was no way she was actually at our house, I looked out the window and saw a familiar looking foreign car parked outside. If it hadn't been her, I would've reported it to the cops."
    show komachi pout with dissolve
    voice "audio/voice/E2/SHI/02/KO/KO000.ogg"
    komachi "Onii-chan, is that car parked outside... Could it be the car of that one teacher from Sobu high? It is, isn't it?"
    hachiman "(Her ability to get ahead of me and hunt me down is terrifying!)"
    voice "audio/voice/E2/SHI/02/SZ/SZ006.ogg"
    hiratsuka "I'll be waiting for you. Go ahead and come out when you're ready."
    voice "audio/voice/E2/SHI/02/HA/HA006.ogg"
    hachiman "I'll do that..."
    "After being beaten to submission, I had no choice but to resign myself. I made my way to the door, dragging my feet."
    show komachi happy with dissolve
    voice "audio/voice/E2/SHI/02/KO/KO001.ogg"
    komachi "Oh, if you're going out, buy something for your tired little sister on the way back."
    voice "audio/voice/E2/SHI/02/HA/HA007.ogg"
    hachiman "...Got it."
    window auto hide dissolve
    scene outsideA with Fade(1.0, 0.5, 1.0)
    window auto show dissolve
    "As I gave a feeble reply and left the house, Hiratsuka-sensei lowered her car window and waved at me."
    voice "audio/voice/E2/SHI/02/SZ/SZ007.ogg"
    hiratsuka "Wow, well aren't you quick. Come on, hop in."
    voice "audio/voice/E2/SHI/02/HA/HA008.ogg"
    hachiman "Sure..."
    play sound "audio/sfx/SE06/SE06_11.ogg"
    $renpy.pause(delay=0.5,hard=True)
    "I did as I was told and got in the passenger seat. The car then slowly started to drive off."
    window auto hide dissolve
    stop music fadeout 0.5
    scene skyA with dissolve
    play ambient "audio/sfx/SE06/SE06_02L.ogg"
    window auto show dissolve
    hachiman "(Come to think of it, I haven't been in this car since that one time...)"
    "It was before the Christmas event at the end of last year. The conversation I had with Hiratsuka-sensei flashed through my mind."
    window auto hide dissolve
    stop ambient fadeout 0.5
    show bridgeC
    show hiratsuka coat mid_center_night angry at center:
        xoffset 40 yoffset 75
    with Fade(0.25,0.35, 0.5, color="#fff")
    window auto show dissolve
    voice "audio/voice/E2/SHI/02/SZ/SZ008.ogg"
    hiratsuka "But you know, Hikigaya... Hurting people is inevitable. Just by existing, we hurt people unbeknownst to us. Whether you're alive or dead, you'll always be hurting someone."
    show hiratsuka sad with dissolve
    voice "audio/voice/E2/SHI/02/SZ/SZ009.ogg"
    hiratsuka "If you get involved, you hurt someone, if you try your best not to get involved, someone might get hurt anyway..."
    show hiratsuka angry with dissolve
    voice "audio/voice/E2/SHI/02/SZ/SZ010.ogg"
    hiratsuka "But if you don't care about them, you won't even notice that you hurt them. What you need is self-awareness. It's because you care about someone that you feel like you've hurt them."
    voice "audio/voice/E2/SHI/02/SZ/SZ011.ogg"
    hiratsuka "To care about someone is to have the readiness to consciously hurt that person."
    voice "audio/voice/E2/SHI/02/HA/HA009.ogg"
    hachiman "..."
    show hiratsuka mid_left_night happy at center with dissolve:
        xoffset 140 yoffset 80
    voice "audio/voice/E2/SHI/02/SZ/SZ012.ogg"
    hiratsuka "There are some things that we can't have because we care for each other. But that's not something to be sad about. Perhaps it's something to be proud of."
    voice "audio/voice/E2/SHI/02/HA/HA010.ogg"
    hachiman "Isn't that a little tough?"
    voice "audio/voice/E2/SHI/02/SZ/SZ013.ogg"
    hiratsuka "Yeah, it is."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E2/SHI/02/SZ/SZ014.ogg"
    hiratsuka "But you're capable. I know that because I've been there, too."
    window auto hide dissolve
    stop voice
    hide bridgeC
    hide hiratsuka
    with Fade(0.25,0.35, 0.5, color="#fff")
    play ambient "audio/sfx/SE06/SE06_02L.ogg"
    window auto show dissolve
    voice "audio/voice/E2/SHI/02/SZ/SZ015.ogg"
    hiratsuka "..."
    "I was starting to get a little embarrased, but Hiratsuka-sensei kept driving with her usual calm and collected expression."
    "As I was lost in tought, the car gradually slowed down as it finally arrived at our destination."
    stop ambient fadeout 0.5
    $renpy.pause(delay=0.5,hard=True)
    play sound "audio/sfx/SE06/SE06_03.ogg"
    $renpy.pause(delay=1.5,hard=True)
    play music "audio/bgm/BGM26.ogg"
    voice "audio/voice/E2/SHI/02/SZ/SZ016.ogg"
    hiratsuka "Alright, we're here."
    voice "audio/voice/E2/SHI/02/HA/HA011.ogg"
    hachiman "Is this... a ramen spot!?"
    voice "audio/voice/E2/SHI/02/SZ/SZ017.ogg"
    hiratsuka "This is a spot that is well know even among the connoisseurs. The thing is, you can only get here by car."
    hachiman "(She really loves ramen, doesn't she...)"
    window auto hide dissolve
    scene ramenShop with Fade(0.5, 1.0, 1.0)
    window auto show dissolve
    "Hiratsuka-sensei then gallantly walked into the restaurant and sat down at the counter. It seemed she was a regular. I decided to obediently follow her."
    voice "audio/voice/E2/SHI/02/ZD/ZD000.ogg"
    sk "Welcome!"
    window auto hide dissolve
    scene ramenShop:
        zoom 2.0 xalign .5 ypos -425
    show hiratsuka coat mid_center happy at center:
        xoffset 40 yoffset 75
    with dissolve
    window auto show dissolve
    voice "audio/voice/E2/SHI/02/SZ/SZ018.ogg"
    hiratsuka "Mind if I make a recommendation?"
    voice "audio/voice/E2/SHI/02/HA/HA012.ogg"
    hachiman "Not really... If it's you picking, I'm sure it'll be good."
    show hiratsuka vhappy with dissolve
    voice "audio/voice/E2/SHI/02/SZ/SZ019.ogg"
    hiratsuka "Fu... Now you're just flattering me."
    show hiratsuka happy with dissolve
    voice "audio/voice/E2/SHI/02/SZ/SZ020.ogg"
    hiratsuka "I'll have two of the usual."
    voice "audio/voice/E2/SHI/02/ZD/ZD001.ogg"
    sk "Comin' right up!"
    "After ordering in a macho way, I see sensei smile at me and even though we're at your typical ramen spot, it made my heart flutter a little."
    window auto hide dissolve
    stop music fadeout 1.0
    scene ramenShop with Fade(0.5, 1.0, 0.5):
        zoom 2.0 xalign .5 ypos -425
    window auto show dissolve
    voice "audio/voice/E2/SHI/02/ZD/ZD002.ogg"
    sk "Here you are!"
    window auto hide dissolve
    play sound "audio/sfx/SE01/SE01_85.ogg"
    $renpy.pause(delay=0.5,hard=True)
    play music "audio/bgm/BGM16.ogg"
    window auto show dissolve
    voice "audio/voice/E2/SHI/02/HA/HA013.ogg"
    hachiman "This is...!"
    "The clear, golden coloured soup. The smooth yellowish noodles floating in the broth, the roasted pork fillet, the half-boiled egg and the silvery green onions."
    "I knew before I even tasted it. This ramen will be like none I'd ever had before."
    hachiman "(Way to go, sensei! Let's see...)"
    play sound "audio/sfx/SE01/SE01_86.ogg"
    $renpy.pause(delay=2.0,hard=True)
    hachiman "(It's... delicious!)"
    "It's a simple soy sauce-based soup with a deep flavor. A perfect blend of chicken and seafood broth that makes you want to drink it up right away."
    "As for the noodles, when I slurp them up, they're surprisingly easy to eat, but they still have some bite to them. Not too chewy, not too soft, but just right. It almost feels like they're being eaten for me. Before I "
    "even swallow, I already know... this is perfection."
    "The crunchy texture, the fragrance of the green onion, and the delicious taste of the meat fills my mouth in a perfect harmony."
    hachiman "(Fu... I seriously just gave this ramen a full review in my head.)"
    show hiratsuka home mid_center happy at center with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E2/SHI/02/SZ/SZ021.ogg"
    hiratsuka "How is it? Delicious, right? I was surprised myself the first time I ate here."
    voice "audio/voice/E2/SHI/02/HA/HA014.ogg"
    hachiman "Yeah, it's great, but... why are we here again?"
    show hiratsuka blush with dissolve
    voice "audio/voice/E2/SHI/02/SZ/SZ022.ogg"
    hiratsuka "I thought I'd thank you for the other day."
    voice "audio/voice/E2/SHI/02/HA/HA015.ogg"
    hachiman "Thank me? Are you talking about the shooting stall thing?"
    voice "audio/voice/E2/SHI/02/SZ/SZ023.ogg"
    hiratsuka "Yeah..."
    voice "audio/voice/E2/SHI/02/HA/HA016.ogg"
    hachiman "You really don't have to be so considerate about it."
    show hiratsuka angry with dissolve
    voice "audio/voice/E2/SHI/02/SZ/SZ024.ogg"
    hiratsuka "As a teacher, it's my duty to be this considerate."
    hachiman "(Well, teachers aren't usually supposed to ask students to win them prizes from stalls, either...)"
    "Those words nearly came out of my mouth, but I decided to keep quiet in fear of sensei's iron fist."
    voice "audio/voice/E2/SHI/02/HA/HA017.ogg"
    hachiman "So, are you happy with it?"
    voice "audio/voice/E2/SHI/02/SZ/SZ025.ogg"
    hiratsuka "Why would you think I am?"
    stop music fadeout 0.5
    voice "audio/voice/E2/SHI/02/HA/HA018.ogg"
    hachiman "Because if you weren't, you probably wouldn't be treating me to ramen right now..."
    play music "audio/bgm/BGM20.ogg"
    show hiratsuka sad with dissolve
    voice "audio/voice/E2/SHI/02/SZ/SZ026.ogg"
    hiratsuka "Uuuuu..."
    hide hiratsuka with dissolve
    "As soon as I said that, Hiratsuka-sensei hung her head so low it almost landed in the bowl."
    voice "audio/voice/E2/SHI/02/SZ/SZ027.ogg"
    hiratsuka "It's alright... I didn't trust that thing from the beginning..."
    hachiman "(I've done it now. I've breached the taboo topic.)"
    play sound "audio/sfx/SE01/SE01_86.ogg"
    "Sensei grumbled for a bit, then wholly devoted herself to silently finishing her ramen."
    "The expression on her face remained lifeless long after we left the ramen spot and got in her car."
    window auto hide dissolve
    stop music fadeout 0.5
    scene skyB with Fade(0.5, 1.0, 1.0)
    play ambient "audio/sfx/SE06/SE06_02L.ogg"
    window auto show dissolve
    voice "audio/voice/E2/SHI/02/SZ/SZ028.ogg"
    hiratsuka "..."
    hachiman "(She hasn't said a thing since we left the ramen spot...)"
    voice "audio/voice/E2/SHI/02/HA/HA019.ogg"
    hachiman "Well, you know... It was just a prize at a stall, after all."
    voice "audio/voice/E2/SHI/02/SZ/SZ029.ogg"
    hiratsuka "So have you decided what to pick on the career path?"
    voice "audio/voice/E2/SHI/02/HA/HA020.ogg"
    hachiman "Career path?"
    play music "audio/bgm/BGM43.ogg"
    voice "audio/voice/E2/SHI/02/SZ/SZ030.ogg"
    hiratsuka "I hope you'll gibe it some actual thought this time around."
    voice "audio/voice/E2/SHI/02/HA/HA021.ogg"
    hachiman "Well, I actually did give it thought last time."
    window auto hide dissolve
    stop ambient fadeout 0.5
    $renpy.pause(delay=0.5,hard=True)
    play sound "audio/sfx/SE06/SE06_03.ogg"
    $renpy.pause(delay=1.5,hard=True)
    scene outsideB with dissolve
    play sound "audio/sfx/SE06/SE06_10.ogg"
    $renpy.pause(delay=1.0,hard=True)
    show hiratsuka coat_sunset mid_left pout at center with dissolve:
        xoffset 140 yoffset 80
    window auto show dissolve
    voice "audio/voice/E2/SHI/02/SZ/SZ031.ogg"
    hiratsuka "There's a lot of things I want to say about that, but... I'll give it a rest. We're here."
    voice "audio/voice/E2/SHI/02/HA/HA022.ogg"
    hachiman "Th-Thanks for the ride."
    voice "audio/voice/E2/SHI/02/SZ/SZ032.ogg"
    hiratsuka "See you back at school then."
    voice "audio/voice/E2/SHI/02/HA/HA023.ogg"
    hachiman "See you there..."
    window auto hide dissolve
    hide hiratsuka with dissolve
    $renpy.pause(delay=1.0,hard=True)
    play sound "audio/sfx/SE06/SE06_11.ogg"
    $renpy.pause(delay=1.0,hard=True)
    play sound "audio/sfx/SE06/SE06_01.ogg"
    $renpy.pause(delay=2.0,hard=True)
    window auto show dissolve
    hachiman "(Hah... What was that about? Well anyways, the ramen was good at least.)"
    window auto hide dissolve
    stop sound fadeout 1.0
    stop music fadeout 1.0
    scene black with Fade(0.5, 0.5, 0)
    play sound "audio/sfx/SE04/SE04_03.ogg"
    scene houseB with Fade(0.5, 0.5, 1.0)
    stop sound
    window auto show dissolve
    voice "audio/voice/E2/SHI/02/HA/HA024.ogg"
    hachiman "I'm back~..."
    show komachi athletic_sunset mid_center happy at center with dissolve:
        xoffset -75 yoffset 75
    play music "audio/bgm/BGM41.ogg"
    voice "audio/voice/E2/SHI/02/KO/KO002.ogg"
    komachi "Ah, onii-chan, welcome back~! What did you get for your dear sister?"
    voice "audio/voice/E2/SHI/02/HA/HA025.ogg"
    hachiman "I... forgot. Sorry."
    show komachi annoyed with dissolve
    voice "audio/voice/E2/SHI/02/KO/KO003.ogg"
    komachi "What the hell is wrong with you? I was looking forward to it too!"
    voice "audio/voice/E2/SHI/02/HA/HA026.ogg"
    hachiman "Alright, I get it. I'll go to the convenience store and get you something."
    show komachi mid_left vhappy with dissolve:
        xoffset 40 yoffset 75
    voice "audio/voice/E2/SHI/02/KO/KO004.ogg"
    komachi "I want some ice cream~!"
    voice "audio/voice/E2/SHI/02/HA/HA027.ogg"
    hachiman "...Understood."
    window auto hide dissolve
    stop voice
    $renpy.pause(delay=0.5,hard=True)
    stop music fadeout 0.5
    call loading_screen(25, "33") from _call_loading_screen_33
    jump E3_CMM_01
