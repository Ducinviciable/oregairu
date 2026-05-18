label E4_IRO_01:
    scene scouncilroomA with Fade(2.0, 1.0, 2.0)
    play music "audio/bgm/BGM29.ogg"
    show iroha school mid_center vhappy at center with dissolve:
        xoffset -5 yoffset 75
    window auto show dissolve
    voice "audio/voice/E4/IRO/01/IR/IR000.ogg"
    iroha "Now then, senpai. Let's go shopping!"
    voice "audio/voice/E4/IRO/01/HA/HA000.ogg"
    hachiman "Eh? Right now?"
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR001.ogg"
    iroha "We have to pick a budget and a place. Also, we need to contact Kaihin High School. Then after that, we can go shopping~"
    voice "audio/voice/E4/IRO/01/IR/IR002.ogg"
    iroha "Yukiknoshita and Yuigahama-senpai are busy thinking up recipes, so you should be free."
    voice "audio/voice/E4/IRO/01/HA/HA001.ogg"
    hachiman "Well, I don't have anything to do, but... That doesn't mean you can just make me an errand boy."
    show yukino school mid_center happy at left:
        xoffset -105 yoffset 75
    show yui school mid_center happy at right:
        xoffset -180 yoffset 75
    with dissolve
    voice "audio/voice/E4/IRO/01/YK/YK000.ogg"
    yukino "It can be a novel way to kill time. Why not give it a go?"
    voice "audio/voice/E4/IRO/01/YI/YI000.ogg"
    yui "That's right, Hikki. Go with her."
    show iroha vhappy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR003.ogg"
    iroha "Come on, senpai. You really do need a boy tag along when shopping~"
    voice "audio/voice/E4/IRO/01/HA/HA002.ogg"
    hachiman "Do I look like someone who can carry 6 bags at a time?"
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR004.ogg"
    iroha "Well, compared to Hayama-senpai or Tobe-senpai, no, but..."
    voice "audio/voice/E4/IRO/01/HA/HA003.ogg"
    hachiman "Huh?"
    hide iroha
    hide yui
    hide yukino
    with dissolve
    play sound "audio/sfx/SE01/SE01_12.ogg"
    show iroha school near_left happy at center with dissolve:
        xoffset 260 yoffset 75
    "As she said this, Isshiki stood beside me, grabbed my arms and rubbed them softly."
    voice "audio/voice/E4/IRO/01/IR/IR005.ogg"
    iroha "Still, you have bigger arms than me, you know."
    voice "audio/voice/E4/IRO/01/HA/HA004.ogg"
    hachiman "............"
    voice "audio/voice/E4/IRO/01/HA/HA005.ogg"
    hachiman "Fine, I'll go."
    show iroha vhappy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR006.ogg"
    iroha "Then, let's be on our way!"
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    scene stationA with Fade(1.0, 1.0, 1.0)
    play music "audio/bgm/BGM41.ogg"
    show iroha school mid_center happy at center with dissolve:
        xoffset -5 yoffset 75
    window auto show dissolve
    voice "audio/voice/E4/IRO/01/HA/HA006.ogg"
    hachiman "So, where are we going?"
    voice "audio/voice/E4/IRO/01/IR/IR007.ogg"
    iroha "Where do we go~? We have to be particular about where we shop."
    show iroha vhappy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR008.ogg"
    iroha "I think the key to this kind of thing is how much we can get with a limited budget!"
    voice "audio/voice/E4/IRO/01/HA/HA007.ogg"
    hachiman "Well, that goes without saying... how much can we spend per person?"
    show iroha angry with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR009.ogg"
    iroha "H~m, I'd say about a 150 to 200 yen per person."
    voice "audio/voice/E4/IRO/01/HA/HA008.ogg"
    hachiman "Then the 100 yen store it is."
    show iroha school mid_left unimpressed at center with dissolve:
        xoffset -35 yoffset 65
    voice "audio/voice/E4/IRO/01/IR/IR010.ogg"
    iroha "Eh-, but that's so plain,,,"
    show iroha frown with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR011.ogg"
    iroha "Valentine's Day isn't just about making chocolate and calling it a day. Everything from the utensils to the wrapping has to be cute!"
    voice "audio/voice/E4/IRO/01/HA/HA009.ogg"
    hachiman "You can actually get some pretty amazing things at 100 yen stores these days, you know?"
    show iroha angry with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR012.ogg"
    iroha "Fine, that's true, but it doesn't feel special! Don't undermine girls' feelings."
    hachiman "(Girl's feelings, huh...)"
    window auto hide dissolve
    stop music fadeout 0.5
    call card_loading from _call_card_loading_1
    scene stationA with dissolve
    show iroha school mid_center pout at center with dissolve:
        xoffset -5 yoffset 75
    $card_queue = ["About \nValentine's \nDay", "About \nchocolate", "About \nKaihin \nSougou \nHigh", "About \ngoing \nshopping", "About \nthe \ntasting \nevent", "End \nconversation"]
    play music "audio/bgm/BGM31.ogg"
    $iroha_shopping_card_count = 0
    $iroha_shopping_ellipses_count = 0
    jump iroha_shopping_cards

label iroha_shopping_cards:
    if iroha_shopping_card_count < 5:
        $iroha_shopping_card_count += 1
        $renpy.pause(delay=0.5, hard=True)
        $ch2 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch2)
        $ch3 = card_queue[renpy.random.randint(0, len(card_queue)-1)]
        $card_queue.remove(ch3)
        window auto hide dissolve
        call screen three_minigame("...", ch2, ch3) with dissolve
        if _return == 1:
            if ch2 == "End \nconversation":
                $card_queue.append(ch2)
            elif ch3 == "End \nconversation":
                $card_queue.append(ch3)
            else:
                $card_queue.append(renpy.random.choice([ch2,ch3]))
            $iroha_shopping_ellipses_count += 1
            if iroha_shopping_ellipses_count == 1:
                jump iroha_shopping_ellipses1
            elif iroha_shopping_ellipses_count == 2:
                jump iroha_shopping_ellipses2
            elif iroha_shopping_ellipses_count == 3:
                jump iroha_shopping_ellipses3
            elif iroha_shopping_ellipses_count == 4:
                jump iroha_shopping_ellipses4
            elif iroha_shopping_ellipses_count == 5:
                jump iroha_shopping_ellipses5
        elif _return == 2:
            $card_queue.append(ch3)
            if ch2 == "About \nValentine's \nDay":
                jump about_valentine_s_day_card
            elif ch2 == "About \nchocolate":
                jump about_chocolate_card
            elif ch2 == "About \nKaihin \nSougou \nHigh":
                jump about_kaihin_sougou_high_card
            elif ch2 == "About \ngoing \nshopping":
                jump about_going_shopping_card
            elif ch2 == "About \nthe \ntasting \nevent":
                jump about_the_tasting_event_card
            else:
                jump iroha_shopping_exit1
        elif _return == 3:
            $card_queue.append(ch2)
            if ch3 == "About \nValentine's \nDay":
                jump about_valentine_s_day_card
            elif ch3 == "About \nchocolate":
                jump about_chocolate_card
            elif ch3 == "About \nKaihin \nSougou \nHigh":
                jump about_kaihin_sougou_high_card
            elif ch3 == "About \ngoing \nshopping":
                jump about_going_shopping_card
            elif ch3 == "About \nthe \ntasting \nevent":
                jump about_the_tasting_event_card
            else:
                jump iroha_shopping_exit1
    else:
        if iroha_shopping_ellipses_count == 0:
            jump iroha_shopping_exit4
        elif iroha_shopping_ellipses_count < 3:
            jump iroha_shopping_exit3
        else:
            jump iroha_shopping_exit2


label iroha_shopping_ellipses1:
    #file missing
    voice "audio/voice/E3/IRO/03/HA/HA035.ogg"
    hachiman "........."
    voice "audio/voice/E4/IRO/01/IR/IR013.ogg"
    iroha "What's the matter, senpai? You've gone quiet."
    voice "audio/voice/E4/IRO/01/HA/HA011.ogg"
    hachiman "It's just that I've heard the term \"A girls' seriousness\" quite often, but I haven't heard anything like \"A guys' seriousness\"."
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR014.ogg"
    iroha "Ah, that's true. But it'll be white day soon, so we'll get to see it, won't we, se~npai?"
    voice "audio/voice/E4/IRO/01/HA/HA012.ogg"
    hachiman "Don't get your hopes up."
    jump iroha_shopping_cards

label iroha_shopping_ellipses2:
    show iroha pout with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR015.ogg"
    iroha "Where should we go next? How about over there?"
    voice "audio/voice/E4/IRO/01/HA/HA013a.ogg"
    hachiman "Yeah, that's way too fancy... If it can't be a 100 yen store or a wholesale supermarket... I guess we can go for a discount store."
    voice "audio/voice/E4/IRO/01/IR/IR016.ogg"
    iroha "We'd have to go to the next station over. That'd be such a pain. It'd be a waste of time, too..."
    hachiman "(Where did that \"girls' seriousness\" go...)"
    jump iroha_shopping_cards

label iroha_shopping_ellipses3:
    show iroha pout with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR017.ogg"
    iroha "It's so cold too! My fingers are freezing over~"
    show iroha surprised with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR018.ogg"
    iroha "...Ah! {size=35}No, {size=40}I did not imply what you're thinking, and neither did I openly invite you to hold my hand or anything,{/size} so please don't try to do so, because that was not my intention at all, {size=50}sorry.{/size}"
    voice "audio/voice/E4/IRO/01/HA/HA014.ogg"
    hachiman "...What are you getting riled up of your own implication for?"
    jump iroha_shopping_cards

label iroha_shopping_ellipses4:
    voice "audio/voice/E4/IRO/01/HA/HA015.ogg"
    hachiman "........."
    show iroha pout with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR019.ogg"
    iroha "Senpai, you sure stay silent a lot."
    voice "audio/voice/E4/IRO/01/HA/HA016.ogg"
    hachiman "Mhm, I guess you're right."
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR020.ogg"
    iroha "You do. Is it really that boring being with me? That's what you're making me think."
    voice "audio/voice/E4/IRO/01/IR/IR021.ogg"
    iroha "Well, it's also rather annoying to see people trying to make a conversation exciting..."
    hachiman "(At least she got good reference. But if a conversation dies, you really go into a stalemate, huh?)"
    jump iroha_shopping_cards

label iroha_shopping_ellipses5:
    show iroha pout with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR022.ogg"
    iroha "What are you thinking about, senpai?"
    voice "audio/voice/E4/IRO/01/HA/HA017.ogg"
    hachiman "Nothing in particular."
    show iroha frown with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR023.ogg"
    iroha "Even though you're with me?"
    voice "audio/voice/E4/IRO/01/HA/HA018.ogg"
    hachiman "Well, if I really had to say, I'm thinking about going home."
    show iroha unimpressed with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR024.ogg"
    iroha "You really should just keep that to yourself."
    jump iroha_shopping_cards

label about_valentine_s_day_card:
    window auto show dissolve
    voice "audio/voice/E4/IRO/01/HA/HA019.ogg"
    hachiman "Women sure love Valentine's."
    show iroha vhappy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR025.ogg"
    iroha "That's right. It's a woman's day, after all!"
    voice "audio/voice/E4/IRO/01/HA/HA020.ogg"
    hachiman "That's the 3rd of March."
    show iroha frown with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR026.ogg"
    iroha "That's not true. Valentine's is a day for girls to battle it out."
    hide iroha
    $url = ["iroha school mid_center angry", "iroha school mid_center happy"]
    $multiImagePara = [-5, 75, 0, 0, 3.0]
    call multiImage() from _call_multiImage_14
    voice "audio/voice/E4/IRO/01/IR/IR027.ogg"
    iroha "I mean it's the day where we give it our all to win. They even say it on TV, don't they?"
    call finishmultiImage from _call_finishmultiImage_15
    show iroha school mid_center happy at center:
        xoffset -5 yoffset 75
    jump iroha_shopping_cards

label about_chocolate_card:
    window auto show dissolve
    voice "audio/voice/E4/IRO/01/HA/HA021.ogg"
    hachiman "By the way, what kind of chocolate do you want to make?"
    show iroha frown with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR028.ogg"
    iroha "Hmm... I'm still trying to figure it out, but I know I have to go all out… Competition seems pretty though this year, huh?"
    voice "audio/voice/E4/IRO/01/HA/HA022.ogg"
    hachiman "That's true. Everybody will be making it together, too, so it'll be easy to see the difference in skill between people."
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR029.ogg"
    iroha "*Fufufu*, sorry not sorry, but that will only make me shine even more."
    hachiman "(Well, how good the chocolate is doesn't really matter, though… Good luck, Irohasu!)"
    jump iroha_shopping_cards

label about_kaihin_sougou_high_card:
    window auto show dissolve
    voice "audio/voice/E4/IRO/01/HA/HA023.ogg"
    hachiman "So this time we're doing a joint event with Kaihin Sougou High, huh?"
    voice "audio/voice/E4/IRO/01/IR/IR030.ogg"
    iroha "Yes. It's convenient in a lot of ways to have a shared budget."
    voice "audio/voice/E4/IRO/01/HA/HA024.ogg"
    hachiman "Won't that actually be more inconvenient? I still get flashbacks from that Christmas event."
    voice "audio/voice/E4/IRO/01/IR/IR031.ogg"
    iroha "This time we're taking the initiative and fully committing to hedging our risks, so we'll be fine."
    hachiman "(I've already been pulled into the Kaihin rip current.)"
    jump iroha_shopping_cards

label about_going_shopping_card:
    window auto show dissolve
    voice "audio/voice/E4/IRO/01/HA/HA025.ogg"
    hachiman "No matter how you look at it, we can't finish everything today."
    show iroha frown with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR032.ogg"
    iroha "Right... Once the recipes are ready, we also need to buy the ingredients."
    voice "audio/voice/E4/IRO/01/HA/HA026.ogg"
    hachiman "So you could've done it after everything was ready to go. We'd have more manpower that way, too..."
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR033.ogg"
    iroha "But then we couldn't have gone with just the two of us. I'd also consider this a date, senpai."
    voice "audio/voice/E4/IRO/01/HA/HA027.ogg"
    hachiman "You're surprisingly basic if you think going out shopping and trying to have a date at the same time is somehow a thing."
    voice "audio/voice/E4/IRO/01/IR/IR034.ogg"
    show iroha annoyed with dissolve
    iroha "Eh~, {size=35}excuse me, are {size=50}you{/size} perhaps thinking “I'm a common folk so I should get along with this here common folk” or something naive like that? Please stop, I was just teasing you, senpai, I don't actually think we're on a date, because if {/size}"
    voice sustain
    iroha "{size=35}I was actually on a date I'd expect it to be more like the real thing{/size},{size=50} so that's a no, sorry.{/size}"
    hachiman "(Not as naive as you can be, Iroha-chan...)"
    show iroha happy with dissolve
    jump iroha_shopping_cards

label about_the_tasting_event_card:
    window auto show dissolve
    voice "audio/voice/E4/IRO/01/HA/HA028.ogg"
    hachiman "Even with the presidents' personal wishes involved, how did the student council even get on-board with something like this? "
    voice "audio/voice/E4/IRO/01/HA/HA029.ogg"
    hachiman "I wonder if this might become an annual tradition."
    show iroha surprised with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR035.ogg"
    iroha "............"
    show iroha vhappy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR036.ogg"
    iroha "Hehe..."
    voice "audio/voice/E4/IRO/01/HA/HA030.ogg"
    hachiman "Hm? What?"
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR037.ogg"
    iroha "No, it's just... I thought it'd be nice if I could leave something I made together with my upperclassmen from the Service Club behind."
    voice "audio/voice/E4/IRO/01/HA/HA031.ogg"
    hachiman "............"
    voice "audio/voice/E4/IRO/01/HA/HA032.ogg"
    hachiman "I guess so."
    jump iroha_shopping_cards

label iroha_shopping_exit1:
    voice "audio/voice/E4/IRO/01/HA/HA033.ogg"
    hachiman "Well, let's get this shopping done with. Show me a \"girl's seriousness\"."
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR038.ogg"
    iroha "You're right. It's no good if we're late."
    jump E4_IRO_01_cont

label iroha_shopping_exit2:
    show iroha pout with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR039.ogg"
    iroha "Senpai, you're not excited even though it's Valentine's~"
    voice "audio/voice/E4/IRO/01/HA/HA034.ogg"
    hachiman "That's not true. I'm incredibly excited."
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR040.ogg"
    iroha "Wow, that's surprising. I thought you were the type who hates Valentine's Day and wishes it would disappear."
    voice "audio/voice/E4/IRO/01/HA/HA035.ogg"
    hachiman "I've long since parted ways with that kind of ressentiment. Komachi gives me one every year and that's enough for me."
    voice "audio/voice/E4/IRO/01/HA/HA036.ogg"
    hachiman "In fact, I don't even want to get chocolate from other people because it would make Komachi's chocolate stand out less."
    show iroha unimpressed with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR041.ogg"
    iroha "Senpai, you're dead serious and it's so creepy. That takes loads off your points..."
    jump E4_IRO_01_cont

label iroha_shopping_exit3:
    show iroha pout with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR042.ogg"
    iroha "S~enpai, even though it's Valentine's Day, you're just as gl~oomy as always. Don't you ever get a little nervous or excited?"
    voice "audio/voice/E4/IRO/01/HA/HA037.ogg"
    hachiman "I'm not nervous, I already know nothing's gonna happen. I am excited, though, Komachi'll give me chocolate."
    show iroha unimpressed with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR043.ogg"
    iroha "Every other word that comes out of your mouth is about Komachi-chan, senpai..."
    hachiman "(And every third word I say is about Totsuka☆)"
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR044.ogg"
    iroha "Although, it's a little different this year."
    voice "audio/voice/E4/IRO/01/HA/HA038.ogg"
    hachiman "Why's that?"
    show iroha vhappy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR045.ogg"
    iroha "Well... I'll keep that to myself☆"
    hachiman "(Why is she being so coy?)"
    jump E4_IRO_01_cont

label iroha_shopping_exit4:
    voice "audio/voice/E4/IRO/01/IR/IR046.ogg"
    iroha "What kind of day is Valentine's to you, senpai?"
    voice "audio/voice/E4/IRO/01/HA/HA039.ogg"
    hachiman "The kind of day I get chocolate from my mom and sister."
    show iroha unimpressed with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR047.ogg"
    iroha "Sorry, I phrased that the wrong way."
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR048.ogg"
    iroha "Um, let's see... Senpai, you'd be happy to get chocolate, right?"
    voice "audio/voice/E4/IRO/01/HA/HA040.ogg"
    hachiman "Well, I guess I would..."
    hachiman "(I was lying. I'd probably be over the moon. Watch me keep it for 3 days without eating it.)"
    voice "audio/voice/E4/IRO/01/IR/IR049.ogg"
    iroha "Right."
    show iroha vhappy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR050.ogg"
    iroha "Then I think you can expect to get some this year, senpai."
    voice "audio/voice/E4/IRO/01/HA/HA041.ogg"
    hachiman "Right, because of the taste-testing event. I'll enjoy tasting and the perks of cleaning up left-overs."
    show iroha pout with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR051.ogg"
    iroha "No, that's not what I meant..."
    hide iroha
    $url = ["iroha school mid_center pout", "iroha school mid_center happy"]
    $multiImagePara = [-5, 75, 0, 0, 4.1]
    call multiImage() from _call_multiImage_15
    voice "audio/voice/E4/IRO/01/IR/IR052.ogg"
    iroha "No, never mind. I guess I'll keep it to myself, after all. Since I want to see the surprise on your face."
    call finishmultiImage from _call_finishmultiImage_16
    show iroha school mid_center happy at center:
        xoffset -5 yoffset 75
    hachiman "(\"the surprise\"... I don't know why, but I have a bad feeling about this.)"
    jump E4_IRO_01_cont

label E4_IRO_01_cont:
    window auto hide dissolve
    stop music fadeout 0.5
    scene stationA with Fade(1.0, 0.5, 1.0)
    play music "audio/bgm/BGM08.ogg"
    window auto show dissolve
    voice "audio/voice/E4/IRO/01/OR/OR000.ogg"
    mystery "Hikigaya?"
    hachiman "(This voice...)"
    show kaori school far happy at center with dissolve:
        xoffset 10 yoffset 75
    voice "audio/voice/E4/IRO/01/OR/OR001.ogg"
    kaori "Didn't expect to see you here! Are you shopping for the tasting event, too?"
    hide kaori with dissolve
    show kaori school mid happy at center:
        xoffset -435 yoffset 75
    show iroha school mid_left vhappy at center:
        xoffset 370 yoffset 65
    with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR053.ogg"
    iroha "Ah, Orimoto-san! Thanks to you all for working with us!"
    "I turned around at the sound of a familiar voice, and sure enough, Kaori Orimoto was there. Behind her were the members of the Kaihin Sougou High School who had “given their all” at last year's Christmas "
    "event."
    voice "audio/voice/E4/IRO/01/OR/OR002.ogg"
    kaori "Hey, why don't we shop around together? That way we won't overlap."
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR054.ogg"
    iroha "Oh, right. That's a good way to save money."
    show kaori vhappy with dissolve
    voice "audio/voice/E4/IRO/01/OR/OR003.ogg"
    kaori "I know right~? Alright, it's decided!"
    hachiman "(I wanna go...)"
    window auto hide dissolve
    stop music fadeout 0.5
    scene mallA
    play music ["<silence 2.0>", "audio/bgm/BGM17.ogg"]
    show kaori school mid happy at center:
        xoffset -435 yoffset 75
    show iroha school mid_left happy at center:
        xoffset 370 yoffset 65
    with Fade(1.0, 0.5, 1.0)
    $renpy.pause(delay=1.0, hard=False)
    window auto show dissolve
    voice "audio/voice/E4/IRO/01/IR/IR055.ogg"
    iroha "How about something like this~?"
    voice "audio/voice/E4/IRO/01/OR/OR004.ogg"
    kaori "Yeah, we can make work with this somehow."
    show kaori vhappy with dissolve
    voice "audio/voice/E4/IRO/01/OR/OR005.ogg"
    kaori "Alright, work's all done. Now we can just enjoy the event~."
    voice "audio/voice/E4/IRO/01/HA/HA042.ogg"
    hachiman "............"
    show kaori happy with dissolve
    voice "audio/voice/E4/IRO/01/OR/OR006.ogg"
    kaori "Come to think of it, have I ever given you chocolate, Hikgaya?"
    show iroha surprised with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR056.ogg"
    iroha "............"
    voice "audio/voice/E4/IRO/01/HA/HA043.ogg"
    hachiman "............"
    voice "audio/voice/E4/IRO/01/HA/HA044.ogg"
    hachiman "No, of course not."
    show kaori worried with dissolve
    voice "audio/voice/E4/IRO/01/OR/OR007.ogg"
    kaori "Right."
    window auto hide dissolve
    stop music fadeout 0.5
    scene stationB with Fade(1.0, 0.5, 1.0)
    show iroha school_sunset mid_center happy at center with dissolve:
        xoffset -5 yoffset 75
    play music "audio/bgm/BGM34.ogg"
    $renpy.pause(delay=0.5, hard=False)
    window auto show dissolve
    voice "audio/voice/E4/IRO/01/IR/IR057.ogg"
    iroha "You really haven't gotten any chocolate, huh, senpai?"
    voice "audio/voice/E4/IRO/01/HA/HA045.ogg"
    hachiman "Leave it alone. The ones who get chocolate are lucky, so not getting chocolate is actually the norm."
    show iroha vhappy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR058.ogg"
    iroha "Ahaha, you sound like a sore loser."
    voice "audio/voice/E4/IRO/01/HA/HA046.ogg"
    hachiman "............"
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/01/IR/IR059.ogg"
    iroha "But if that's the case, senpai, I'm looking forward to the event even more♪."
    voice "audio/voice/E4/IRO/01/HA/HA047.ogg"
    hachiman "Why the hell...?"
    voice "audio/voice/E4/IRO/01/IR/IR060.ogg"
    iroha "............"
    voice "audio/voice/E4/IRO/01/HA/HA048.ogg"
    hachiman "......?"
    show iroha school_sunset mid_left vhappy at center with dissolve:
        xoffset -35 yoffset 65
    voice "audio/voice/E4/IRO/01/IR/IR061.ogg"
    iroha "Want to go back? The shopping is all done."
    hide iroha with dissolve
    voice "audio/voice/E4/IRO/01/HA/HA049.ogg"
    hachiman "............"
    show iroha school_sunset far_center happy at left with dissolve:
        xoffset 340 yoffset 75
    voice "audio/voice/E4/IRO/01/IR/IR062.ogg"
    iroha "What are you doing, senpai? I'll leave you behind~"
    voice "audio/voice/E4/IRO/01/HA/HA050.ogg"
    hachiman "............"
    "Isshiki stopped after walking for a bit, turned around and waited for me."
    "Then her waving lured me to follow her."
    window auto hide dissolve
    stop music fadeout 0.5
    call loading_screen(13, "36") from _call_loading_screen_2
    jump E4_CMM_02

label E4_IRO_02:
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/02/IR/IR000.ogg"
    iroha "Alright! It's done! Just have to put the icing on the cake"
    show iroha school far_left vhappy at center with dissolve:
        xoffset -25 yoffset 80
    voice "audio/voice/E4/IRO/02/IR/IR001.ogg"
    iroha "Fufu. Now, how should I decorate it~♪"
    hachiman "(Wow, no wonder she said it was her specialty. She's seems really good at it.)"
    hide iroha with dissolve
    show iroha school mid_center blush at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/IRO/02/IR/IR002.ogg"
    iroha "What's wrong, senpai? You've been staring at me for a while~"
    voice "audio/voice/E4/IRO/02/HA/HA000.ogg"
    hachiman "I was just admiring a professional at work. I kept watching because I was curious about how you were making them."
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/02/IR/IR003.ogg"
    iroha "I see. Your face and personality gave away the impression you knew nothing about that."
    hachiman "(I understand personality, but what does my face have to do with it... Well, she's right I guess,  I don't know anything.)"
    show iroha vhappy with dissolve
    voice "audio/voice/E4/IRO/02/IR/IR004.ogg"
    iroha "If you try it, you might find it surprisingly fun. I still have some ingredients left, so wanna try?"
    voice "audio/voice/E4/IRO/02/HA/HA001.ogg"
    hachiman "Well, I still have some odd jobs to finish, so I'll pass for now."
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/02/IR/IR005.ogg"
    iroha "Right. Then..."
    voice "audio/voice/E4/IRO/02/HA/HA002.ogg"
    hachiman "Hm?"
    hide iroha with dissolve
    show iroha school near_center vhappy at center with dissolve:
        xoffset -15 yoffset 75
    voice "audio/voice/E4/IRO/02/IR/IR006.ogg"
    iroha "Here, senpai. Open your mouth."
    "Isshiki held out a cookie in front of my mouth."
    voice "audio/voice/E4/IRO/02/HA/HA003.ogg"
    hachiman "Huh? Do I taste test already? With no icing?"
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/02/IR/IR007.ogg"
    iroha "This isn't a taste test. It's nutritional support for all the hard work you've done."
    voice "audio/voice/E4/IRO/02/HA/HA004.ogg"
    hachiman "Ah, right."
    voice "audio/voice/E4/IRO/02/IR/IR008.ogg"
    iroha "Come on, senpai, open your mouth so I can toss it in."
    voice "audio/voice/E4/IRO/02/HA/HA005.ogg"
    hachiman "I can eat it myself, thank you."
    play sound "audio/sfx/SE01/SE01_52.ogg"
    "I took Isshiki's cookie with the tip of my fingers and put it whole in my mouth."
    "After the crunch of the cookie came the smooth aroma of butter that filled my mouth."
    voice "audio/voice/E4/IRO/02/HA/HA006.ogg"
    hachiman "...It's great."
    show iroha vhappy with dissolve
    voice "audio/voice/E4/IRO/02/IR/IR009.ogg"
    iroha "Ehehe, the finished product is even better~"
    voice "audio/voice/E4/IRO/02/HA/HA007.ogg"
    hachiman "Oh? I'm looking forward to it."
    show iroha near_left unimpressed with dissolve:
        xoffset 20
    voice "audio/voice/E4/IRO/02/IR/IR010.ogg"
    iroha "Excuse me? I didn't say I'd give you any."
    voice "audio/voice/E4/IRO/02/HA/HA008.ogg"
    hachiman "R-right... Sorry, I guess? I got carried away."
    hide iroha with dissolve
    stop music fadeout 0.5
    stop voice fadeout 0.5
    $renpy.pause(delay=0.25, hard=True)
    show saki school mid_right happy at center:
        xoffset -355 yoffset 75
    show keika home mid happy at center:
        xoffset 215 yoffset 75
    with dissolve
    play music "audio/bgm/BGM42.ogg"
    voice "audio/voice/E4/IRO/02/KE/KE000.ogg"
    keika "Haa-chan, look! I made this!"
    voice "audio/voice/E4/IRO/02/HA/HA009.ogg"
    hachiman "Mm? Oh, that's great. You did really well, huh?"
    voice "audio/voice/E4/IRO/02/HA/HA010.ogg"
    hachiman "Did you help, too?"
    voice "audio/voice/E4/IRO/02/SA/SA000.ogg"
    saki "Y-yeah, with the truffles. I had Yukinoshita teach me..."
    show keika vhappy with dissolve
    voice "audio/voice/E4/IRO/02/KE/KE001.ogg"
    keika "Haa-chan, try them!"
    show saki pout with dissolve
    voice "audio/voice/E4/IRO/02/SA/SA001.ogg"
    saki "So... will you try them? They shouldn't be too bad."
    voice "audio/voice/E4/IRO/02/HA/HA011.ogg"
    hachiman "Is that okay? Thank you, Kei chan. Here goes."
    voice "audio/voice/E4/IRO/02/HA/HA012.ogg"
    hachiman "............"
    show saki angry with dissolve
    voice "audio/voice/E4/IRO/02/SA/SA002.ogg"
    saki "............"
    show keika annoyed with dissolve
    voice "audio/voice/E4/IRO/02/KE/KE002.ogg"
    keika "Haa-chan, is it yummy? Is it?"
    voice "audio/voice/E4/IRO/02/HA/HA013.ogg"
    hachiman "Ah, it's tasty. It's really tasty! Kei chan, you really outdid yourself."
    show saki surprised
    show keika vhappy
    with dissolve
    voice "audio/voice/E4/IRO/02/KE/KE003.ogg"
    keika "Yay! Haa chan liked them!"
    show saki vhappy with dissolve
    voice "audio/voice/E4/IRO/02/SA/SA003.ogg"
    saki "Isn't that great, Kei chan?"
    voice "audio/voice/E4/IRO/02/KE/KE004.ogg"
    keika "Yeah!"
    show saki blush with dissolve
    voice "audio/voice/E4/IRO/02/SA/SA004.ogg"
    saki "Well then, w we'll go back to cleaning up."
    voice "audio/voice/E4/IRO/02/HA/HA014.ogg"
    hachiman "Yeah, thanks for coming."
    hide saki
    hide keika
    with dissolve
    $renpy.pause(delay=0.25, hard=True)
    show haruno sweater near_center happy at center with dissolve:
        xoffset -20 yoffset 75
    voice "audio/voice/E4/IRO/02/HR/HR000.ogg"
    haruno "Hey, Hikigaya kun~! Try onee san's sweets, too~"
    voice "audio/voice/E4/IRO/02/HA/HA015.ogg"
    hachiman "Is there any point? They're probably flawless as is."
    show haruno vhappy with dissolve
    voice "audio/voice/E4/IRO/02/HR/HR001.ogg"
    haruno "I certainly didn't make any mistakes, but you need to try them in order to fine tune the taste, right? Come on, don't be shy."
    voice "audio/voice/E4/IRO/02/HA/HA016.ogg"
    hachiman "I'll try them, then..."
    "I put the piece of chocolate Haruno san was holding in my mouth and started chewing. Upon doing so, I was surprised by the flavour that took over my mouth."
    show haruno happy with dissolve
    voice "audio/voice/E4/IRO/02/HR/HR002.ogg"
    haruno "How is it?"
    voice "audio/voice/E4/IRO/02/HA/HA017.ogg"
    hachiman "Wel... It's delicious. It really is."
    "I didn't lie. It was indisputably perfect in taste."
    "What surprised me wasn't just how delicious the chocolate was, but also the sweetness and the slight affect of coffee mixed in. It was a flavour perfectly tailored to me."
    show haruno vhappy with dissolve
    voice "audio/voice/E4/IRO/02/HR/HR003.ogg"
    haruno "Glad you like it. I made it with your tastes in mind, you know."
    voice "audio/voice/E4/IRO/02/HA/HA018.ogg"
    hachiman "............"
    show haruno sly with dissolve
    voice "audio/voice/E4/IRO/02/HR/HR004.ogg"
    haruno "You know onee san sees through everything~"
    "I felt that such an innocuous comment contained an unspoken meaning, and I remembered the dread I got when I was around her."
    show haruno vhappy with dissolve
    voice "audio/voice/E4/IRO/02/HR/HR005.ogg"
    haruno "You're gonna be my brother-in-law, after all~"
    show yukino school mid_center unimpressed at left with dissolve:
        xoffset -170 yoffset 75
    voice "audio/voice/E4/IRO/02/YK/YK000.ogg"
    yukino "Hikigaya kun, you don't need to entertain her."
    voice "audio/voice/E4/IRO/02/HA/HA019.ogg"
    hachiman "Ah, right."
    show haruno sweater near_left happy with dissolve:
        xoffset -45
    voice "audio/voice/E4/IRO/02/HR/HR006.ogg"
    haruno "Oh oh, I made Yukino chan mad. Well then, better head back."
    image haruno sweater near_center happy flat = Flatten("haruno sweater near_center happy")
    show haruno sweater near_center happy flat at center with dissolve:
        xoffset -20 yoffset 75
        0.5
        parallel:
            linear 0.75 alpha 0
        parallel:
            easeout 0.75 xoffset 80
    $renpy.pause(delay=1.0, hard=True)
    hide haruno
    hide yukino with dissolve
    $renpy.pause(delay=0.5, hard=True)
    show yukino school near_left sad at center with dissolve:
        xoffset 80 yoffset 80
    voice "audio/voice/E4/IRO/02/YK/YK001.ogg"
    yukino "I'm sorry about my sister."
    voice "audio/voice/E4/IRO/02/HA/HA020.ogg"
    hachiman "It's alright..."
    show kaori school mid happy at left behind yukino with dissolve:
        xoffset 65 yoffset 75
    voice "audio/voice/E4/IRO/02/OR/OR000.ogg"
    kaori "Ah, Yukinoshita san, I baked this how you told me, so can you teach me how to add some finishing touches. We'll get to taste testing afterwords."
    show yukino happy with dissolve
    voice "audio/voice/E4/IRO/02/YK/YK002.ogg"
    yukino "Yes, I'll be right there."
    hide yukino with dissolve
    $renpy.pause(delay=0.5, hard=True)
    show yukino school mid_left vhappy at right with dissolve:
        xoffset -335 yoffset 80
    voice "audio/voice/E4/IRO/02/YK/YK003.ogg"
    yukino "He's here and all, so why not let Hikigaya kun taste it?"
    show kaori annoyed with dissolve
    voice "audio/voice/E4/IRO/02/OR/OR001.ogg"
    kaori "Hikigaya?"
    voice "audio/voice/E4/IRO/02/HA/HA021.ogg"
    hachiman "............"
    voice "audio/voice/E4/IRO/02/OR/OR002.ogg"
    kaori "Hikigaya, you can tell taste??"
    voice "audio/voice/E4/IRO/02/HA/HA022.ogg"
    hachiman "My taste buds are perfectly fine..."
    show kaori worried with dissolve
    voice "audio/voice/E4/IRO/02/OR/OR003.ogg"
    kaori "No, that's not what I meant. I meant you'd be content with whatever chocolate you receive."
    hachiman "(I wouldn't be happy with just any chocolate, you know. If a girl made the chocolate, I mean even if it isn't chocolate, I'd still be happy...)"
    voice "audio/voice/E4/IRO/02/YK/YK004.ogg"
    yukino "He's got a sweet tooth. I think he's taste testing is trustworthy, at least when it comes to sweetness."
    show kaori annoyed with dissolve
    voice "audio/voice/E4/IRO/02/OR/OR004.ogg"
    kaori "Eh~, for real?"
    show kaori happy with dissolve
    voice "audio/voice/E4/IRO/02/OR/OR005.ogg"
    kaori "Hmm, alright, if it comes out well, I'll give Hikigaya some, too."
    hide kaori
    hide yukino
    with dissolve
    "As I'm watching  Orimoto and Yukinoshita head back to their work space, I suddenly notice someone is looking at me."
    show iroha school mid_center surprised at center with dissolve:
        xoffset -5 yoffset 75
    voice "audio/voice/E4/IRO/02/IR/IR011.ogg"
    iroha "............"
    voice "audio/voice/E4/IRO/02/HA/HA023.ogg"
    hachiman "...? What? Something wrong, Isshiki?"
    show iroha pout with dissolve
    voice "audio/voice/E4/IRO/02/IR/IR012.ogg"
    iroha "N-no, it's just... I was surprised by how popular you seem to be."
    voice "audio/voice/E4/IRO/02/HA/HA024.ogg"
    hachiman "Popular? I guess it's just the fact that a lot of the participants know me. People bringing me their chocolates for taste testing here is as proforma as mandatory gifts or new years greetings."
    show iroha angry with dissolve
    voice "audio/voice/E4/IRO/02/IR/IR013.ogg"
    iroha "Is that right...?"
    show iroha vhappy with dissolve
    voice "audio/voice/E4/IRO/02/IR/IR014.ogg"
    iroha "I don't know about the others, but I let senpai taste my chocolate as a token of my appreciation ☆"
    window auto hide dissolve
    stop music fadeout 0.5
    stop voice fadeout 0.5
    $renpy.pause(delay=0.5, hard=True)
    show irohachocoA with dissolve
    play music "audio/bgm/BGM18.ogg"
    window auto show dissolve
    "Saying that, Irohasu brought out two types of chocolate she had hidden  behind her and held them out to me with a \"ta dah!\""
    hachiman "(Even if it's just token of appreciation, I'll still taste it. I wonder what kind of sacrifice the men of the world would have to make to get a bargain chocolate from this girl.)"
    window auto hide dissolve
    show irohachocoB at truecenter with dissolve:
        zoom 2.0 yoffset -520
    window auto show dissolve
    hachiman "(I'll try the them starting from the left ones.)"
    hachiman "(Oh, it's delicious. Perfect amount of sweetness, the aroma is there, too... The handmade look of it is also very appealing to men.)"
    voice "audio/voice/E4/IRO/02/IR/IR015.ogg"
    iroha "............"
    hachiman "(Let's try the right ones next...)"
    hachiman "(It's kind of powdery, but that doesn't make it bad per say. It has a strange and addictive taste.)"
    "Out of both types of chocolate, they each have their characteristics and stand out taste. As I was pondering what to say, Isshiki said something."
    hide irohachocoB with dissolve
    voice "audio/voice/E4/IRO/02/IR/IR016.ogg"
    iroha "Actually, I made one side, and someone else made the other side.. how were they?"
    voice "audio/voice/E4/IRO/02/HA/HA025.ogg"
    hachiman "Eh, really?"
    hachiman "(Basically, if I guess the ones Iroha made, I'd get praised... I don't know if she'll let me try them again, or if I'll be able to make excuses if I mess up...)"
    menu choco_choice:
        hachiman "(The homemade left ones, or the nostalgic tasting right ones...)"
        with dissolve
        "Left one, I think.":
            voice "audio/voice/E4/IRO/02/HA/HA026.ogg"
            hachiman "The left ones."
            voice "audio/voice/E4/IRO/02/HA/HA027.ogg"
            hachiman "I don't know which were made by you, but I liked the left ones better. I guess heartfelt homemade confection is what describes them best."
            jump E4_IRO_03
        "Right once, I guess.":
            #Orimoto
            voice "audio/voice/E4/IRO/02/HA/HA028.ogg"
            hachiman "I honestly don't know which ones are yours, but... I think I like the sweets on the right better. It's somehow a flavour that makes me want to try it again."
            voice "audio/voice/E4/IRO/02/IR/IR017.ogg"
            iroha "The right one..."
            stop music
            jump E4_IRO_04

label E4_IRO_03:
    voice "audio/voice/E4/IRO/03/IR/IR000.ogg"
    iroha "Eh..."
    voice "audio/voice/E4/IRO/03/HA/HA000.ogg"
    hachiman "They're so good, they can easily cause a misunderstanding  if you gave them to someone on Valentines."
    hachiman "(If I received them, I'd be the one confessing, not the other way around.)"
    show irohachocoB with dissolve
    voice "audio/voice/E4/IRO/03/IR/IR001.ogg"
    iroha "............"
    hachiman "(And Isshiki's reaction as well...)"
    voice "audio/voice/E4/IRO/03/HA/HA001.ogg"
    hachiman "Well... that's just my impressions at least."
    hide irohachocoB with dissolve
    voice "audio/voice/E4/IRO/03/IR/IR002.ogg"
    iroha "Senpai... as expected of you. Correct, I made the left ones."
    hachiman "(Fu~~, alright. I knew it.)"
    voice "audio/voice/E4/IRO/03/IR/IR003.ogg"
    iroha "Fufu, please don't show your relief so blatantly~"
    voice "audio/voice/E4/IRO/03/HA/HA002.ogg"
    hachiman "What do you expect, that was an absurd quiz."
    voice "audio/voice/E4/IRO/03/IR/IR004.ogg"
    iroha "Ahaha, I honestly wasn't expecting you to get it right."
    voice "audio/voice/E4/IRO/03/HA/HA003.ogg"
    hachiman "Right?"
    voice "audio/voice/E4/IRO/03/HA/HA004.ogg"
    hachiman "Though, what I just said wasn't empty flattery. They really were delicious. Thanks."
    voice "audio/voice/E4/IRO/03/IR/IR005.ogg"
    iroha "............"
    show irohachocoB with dissolve
    "When I said that, Isshiki averted her eyes."
    voice "audio/voice/E4/IRO/03/IR/IR006.ogg"
    iroha "I feel a little embarrassed when I get such a straightforward compliment from a cynical senpai."
    hide irohachocoB with dissolve
    voice "audio/voice/E4/IRO/03/IR/IR007.ogg"
    menu choco_ready:
        iroha "This means I can give them to other people, too, right?"
        with dissolve
        "I guarantee you can.":
            "not done"
            jump choco_ready
        "Now all you need to do is wrap them up.":
            "not done"
            jump choco_ready
        "Right...":
            voice "audio/voice/E4/IRO/03/HA/HA017.ogg"
            hachiman "That's right."
            show irohachocoB with dissolve
            voice "audio/voice/E4/IRO/03/IR/IR018.ogg"
            iroha "............"
            voice "audio/voice/E4/IRO/03/HA/HA018.ogg"
            hachiman "What?"
            voice "audio/voice/E4/IRO/03/IR/IR019.ogg"
            iroha "Not, it's just, I... thought I'd ask you first."
            hide irohachocoB with dissolve
            voice "audio/voice/E4/IRO/03/IR/IR020.ogg"
            iroha "Thank you for all of your support."
            voice "audio/voice/E4/IRO/03/HA/HA019.ogg"
            hachiman "S-Sure thing."
            hachiman "(This more honest Irohasu is making my heart race...)"
            hachiman "(Eh, what is this affectionate mood I'm getting into...)"

    window auto hide dissolve
    $renpy.pause(delay=0.25, hard=True)
    hide irohachocoA
    show iroha happy
    with dissolve
    window auto show dissolve
    voice "audio/voice/E4/IRO/03/HA/HA020.ogg"
    hachiman "W-Well, now that the chocolates done, do your best."
    show iroha vhappy with dissolve
    voice "audio/voice/E4/IRO/03/IR/IR021.ogg"
    iroha "I will!"
    stop music fadeout 0.5
    show iroha school mid_left vhappy with dissolve:
        xoffset -35 yoffset 65
    voice "audio/voice/E4/IRO/03/IR/IR022.ogg"
    iroha "Well then, I'll be going over to where Hayama-senpai is."
    window auto hide dissolve
    stop voice fadeout 0.25
    $renpy.pause(delay=0.25, hard=True)
    hide iroha with dissolve
    image iroha school mid_left vhappy flat = Flatten("iroha school mid_left vhappy")
    scene kitchenA at truecenter:
        zoom 1.45 xoffset -25 yoffset -15
    show hayama school mid_right happy at left:
        xoffset 5 yoffset 65
    show yumiko school mid_left happy at center behind hayama:
        xoffset -10 yoffset 75
    with dissolve
    play music "audio/bgm/BGM44.ogg"
    show iroha school mid_left vhappy flat at right with dissolve:
        xoffset -50 yoffset 65 alpha 0
        parallel:
            linear 0.5 alpha 1.0
        parallel:
            easein 0.5 xoffset -190
    $renpy.pause(delay=0.5, hard=True)
    hide iroha
    show iroha school mid_left vhappy at right:
        xoffset -190 yoffset 65
    window auto show dissolve
    voice "audio/voice/E4/IRO/03/IR/IR023.ogg"
    iroha "Hayama senpai! Do you have a moment?"
    show hayama relieved
    show yumiko mid_center frown:
        xoffset -5
    with dissolve
    voice "audio/voice/E4/IRO/03/YM/YM000.ogg"
    yumiko "Are you blind? Can't you see me and Hayama are talking?"
    voice "audio/voice/E4/IRO/03/IR/IR024.ogg"
    iroha "Yeah, and so what's the problem~? Right, Hayama senpai~?"
    window auto hide dissolve
    stop voice
    scene kitchenA with dissolve
    window auto show dissolve
    hachiman "(Your will is so firm, Irohasu...)"
    hachiman "(Anyway, I really do want you to give it your all.)"
    window auto hide dissolve
    stop music fadeout 0.5
    stop ambient fadeout 0.5
    call loading_screen(11, "36") from _call_loading_screen_27
    jump E4_CMM_05

label E4_IRO_04:
    show irohachocoB with dissolve
    voice "audio/voice/E4/IRO/04/IR/IR000.ogg"
    iroha "............"
    "When I told her what I thought of the chocolate on the right, Isshiki suddenly averted her gaze."
    "Although she was still smiling mischievously, her expression was clearly different from just a few seconds ago. It wasn't bursting with the devilish sentiment I'm used to, but throwing a veil that gently hid "
    "her inner thoughts."
    voice "audio/voice/E4/IRO/04/IR/IR001.ogg"
    iroha "That chocolate is actually... Orimoto-san's chocolate. Right?"
    "Isshiki isn't calling out to me, but someone behind me."
    window auto hide dissolve
    scene kitchenA
    show kaori school mid worried at center:
        xoffset -25 yoffset 75
    with dissolve
    play music "audio/bgm/BGM41.ogg"
    window auto show dissolve
    voice "audio/voice/E4/IRO/04/OR/OR000.ogg"
    kaori "........."
    "Had she been listening to the whole conversation? When I turned around, there was Orimoto, looking somewhat awkward and embarrassed, scratching her cheek."
    voice "audio/voice/E4/IRO/04/OR/OR001.ogg"
    kaori "Um, yeah... It's mine. It's the ones I gave to Isshiki-chan so I can give to Hikigaya later..."
    show kaori vhappy with dissolve
    voice "audio/voice/E4/IRO/04/OR/OR002.ogg"
    kaori "A...Ahaha. That's so like you, Hikigaya! Like, how did you even pick mine?"
    voice "audio/voice/E4/IRO/04/HA/HA000.ogg"
    hachiman "What was I supposed to do? I simply went to taste those first."
    hide kaori
    $url = ["kaori school mid annoyed", "kaori school mid vhappy"]
    $multiImagePara = [-25, 75, 0, 0, 4.6]
    call multiImage() from _call_multiImage_16
    voice "audio/voice/E4/IRO/04/OR/OR003.ogg"
    kaori "Huh? That one was my first try, so I messed up on them and Hikigaya still gives them some kind of taste report... That...That's hilarious...!"
    call finishmultiImage from _call_finishmultiImage_17
    show kaori school mid vhappy at center:
        xoffset -25 yoffset 75
    voice "audio/voice/E4/IRO/04/HA/HA001.ogg"
    hachiman "............"
    voice "audio/voice/E4/IRO/04/OR/OR004.ogg"
    kaori "Ahaha, ahhh~ so funny."
    show kaori happy with dissolve
    voice "audio/voice/E4/IRO/04/OR/OR005.ogg"
    kaori "I've got some freshly baked good ones, so if you're gonna praise something, praise them. Come on, over here~"
    voice "audio/voice/E4/IRO/04/HA/HA002.ogg"
    hachiman "S-Sure thing..."
    window auto hide dissolve
    stop voice
    stop ambient fadeout 0.5
    stop music fadeout 0.5
    scene skyB with Fade(1.0, 2.0, 0.5)
    window auto show dissolve
    "I walked home after the tasting. A sense of fatigue makes me drag my steps."
    hachiman "(Ahhh, it's finally over.)"
    hachiman "(No more chocolate for the time being. No, I'll make an exception for Komachi's chocolate.)"
    window auto hide dissolve
    scene sidewalkB with dissolve
    window auto show dissolve
    "As I slowly made my way back to my neighborhood, I suddenly heard a voice calling my name."
    voice "audio/voice/E4/IRO/04/OR/OR006.ogg"
    mystery "Hikigaya!"
    voice "audio/voice/E4/IRO/04/HA/HA003.ogg"
    hachiman "Hm?"
    window auto hide dissolve
    play sound "audio/sfx/SE06/SE06_15.ogg"
    $renpy.pause(delay=2.0, hard=True)
    show kaori school_sunset mid vhappy at center with dissolve:
        xoffset -25 yoffset 75
    play music "audio/bgm/BGM42.ogg"
    window auto show dissolve
    voice "audio/voice/E4/IRO/04/OR/OR007.ogg"
    kaori "We met again. Hilarous."
    stop sound
    voice "audio/voice/E4/IRO/04/HA/HA004.ogg"
    hachiman "Yeah. We just parted ways, too."
    show kaori worried with dissolve
    voice "audio/voice/E4/IRO/04/OR/OR008.ogg"
    kaori "Ah, no I mean meeting you out and about."
    voice "audio/voice/E4/IRO/04/HA/HA005.ogg"
    hachiman "Ah, that's what you meant."
    show kaori happy with dissolve
    voice "audio/voice/E4/IRO/04/OR/OR009.ogg"
    kaori "Yep, yep."
    "Orimoto and me went to the same junior high school and lived in the same neighborhood. Our houses are not so far apart, and our living areas must overlap. And yet, perhaps because I don't go out much "
    "around the block, I haven't seen Orimoto since I graduated from junior high school."
    "However, relationships are a mysterious thing, and it seems that once the connection is restored, something like a gravitational pull arises."
    "I've never even seen her around before, but I can't help but let out a bitter smile at how frequently I've been metting Orimoto lately."
    "And I'm sure that's how she feels as well."
    show kaori closed with dissolve
    voice "audio/voice/E4/IRO/04/OR/OR010.ogg"
    kaori "We live closer than I thought after all."
    "A monologue realizing the distance between us spilled out of Orimoto's mouth."
    voice "audio/voice/E4/IRO/04/OR/OR011.ogg"
    kaori "........."
    hide kaori with dissolve
    show kaori school_sunset near happy at left with dissolve:
        xoffset 175 yoffset 75
    "Orimoto gets off her bike as if it were a matter of course, pushes the handlebars, and starts walking alongside me."
    hachiman "(I won't mind if you went on ahead...)"
    "My walking speed slows down even more, despite the reluctance I suddenly feel. It was no use, since Orimoto had already started walking alongside me, pushing her bike."
    voice "audio/voice/E4/IRO/04/OR/OR012.ogg"
    kaori "By the way, why are you all alone? Don't you have anyone to go home with? Hilarious."
    voice "audio/voice/E4/IRO/04/HA/HA006.ogg"
    hachiman "It's really not funny. You're alone, too, aren't you?"
    show kaori vhappy with dissolve
    voice "audio/voice/E4/IRO/04/OR/OR013.ogg"
    kaori "I was with my friends until a little while ago, but you were alone from the beginning, right? That's so funny."
    voice "audio/voice/E4/IRO/04/HA/HA007.ogg"
    hachiman "Being alone is high in social value. Even if you were at sea or on a mountain, swimming and climbing would be way easier alone. You could say then I'm a solo Japanese islands crossing, no oxygen "
    voice sustain
    hachiman "climbing, home returning gigantor, right?"
    hide kaori
    $url = ["kaori school_sunset near annoyed", "kaori school_sunset near vhappy"]
    $multiImagePara = [175, 75, 0, 0, 2.9]
    call multiImage(-1) from _call_multiImage_17
    voice "audio/voice/E4/IRO/04/OR/OR014.ogg"
    kaori "Eh? Hikigaya, are you interested in climbing? Mountains and hiking are pretty cool!"
    voice "audio/voice/E4/IRO/04/HA/HA008.ogg"
    call finishmultiImage from _call_finishmultiImage_18
    show kaori school_sunset near vhappy at left:
        xoffset 175 yoffset 75
    voice "audio/voice/E4/IRO/04/HA/HA008.ogg"
    hachiman "It sounds like we're having a lively conversation, but we're on a different plane of existence. Can you not do the selective hearing thing and just a few select words?"
    show kaori closed with dissolve
    voice "audio/voice/E4/IRO/04/OR/OR015.ogg"
    kaori "You know, I saw you today and I was thinking..."
    hachiman "(She's stopped listening entirely.)"
    show kaori happy with dissolve
    voice "audio/voice/E4/IRO/04/OR/OR016.ogg"
    kaori "Hikigaya, you've sure changed a lot, haven't you?"
    voice "audio/voice/E4/IRO/04/HA/HA009.ogg"
    hachiman "........."
    voice "audio/voice/E4/IRO/04/HA/HA010.ogg"
    hachiman "...What?"
    voice "audio/voice/E4/IRO/04/OR/OR017.ogg"
    kaori "I have, too."
    voice "audio/voice/E4/IRO/04/HA/HA011.ogg"
    hachiman "........."
    show kaori vhappy with dissolve
    voice "audio/voice/E4/IRO/04/OR/OR018.ogg"
    kaori "Hey, can I talk to you sometime when you're free?"
    voice "audio/voice/E4/IRO/04/HA/HA012.ogg"
    hachiman "Eh, why would you?"
    show kaori annoyed with dissolve
    voice "audio/voice/E4/IRO/04/OR/OR019.ogg"
    kaori "Why... because I can kill some time when I'm bored??"
    voice "audio/voice/E4/IRO/04/HA/HA013.ogg"
    hachiman "Right, have you looked elsewhere?"
    show kaori angry with dissolve
    voice "audio/voice/E4/IRO/04/OR/OR020.ogg"
    kaori "Eh-- It's fine, isn't it? Go out with me. We live close, so it's easy to just hang out."
    show kaori happy with dissolve
    voice "audio/voice/E4/IRO/04/OR/OR021.ogg"
    kaori "So give me your contact info."
    voice "audio/voice/E4/IRO/04/HA/HA014.ogg"
    hachiman "........."
    "What came to my mind at this time were the memories of my junior high school days, when I was going through a range of emotions everytime I sent an email to Orimoto."
    "However, refusing to go out with Orimoto for that reason would be an enormous commitment to the past. The mere thought of going out with Orimoto again is depressing, but if she actually wants to talk to me, I'll "
    "think of an appropriate reason to brush her off."
    voice "audio/voice/E4/IRO/04/HA/HA015.ogg"
    hachiman "...Alright."
    show kaori vhappy with dissolve
    "Orimoto and I take out our cell phones, and without a second thought, we stick them close to each other."
    voice "audio/voice/E4/IRO/04/HA/HA016.ogg"
    hachiman "........."
    "This is Orimoto we're talking about. She says we'll go out, but I seriously doubt she's serious."
    "It might just be a light-hearted attempt to get to know each other better and smooth out our interactions since we've been seeing each other more lately. In fact, that's most likely the case."
    show kaori angry with dissolve
    "As I was thinking this, Orimoto suddenly muttered something to me."
    voice "audio/voice/E4/IRO/04/OR/OR022.ogg"
    kaori "I'm really going to ask you out. So make sure to come hang out with me, okay?"
    voice "audio/voice/E4/IRO/04/HA/HA017.ogg"
    hachiman "........."
    "She looked me straight in the eye and reminded me, so I couldn't help but give her a little nod."
    voice "audio/voice/E4/IRO/04/HA/HA018.ogg"
    hachiman "Well, if you're so inclined..."
    show kaori vhappy with dissolve
    "Our glowing cell phone screens lit up both of our faces."
    window auto hide dissolve
    stop music fadeout 1.0
    jump E4_IRO_05

label E4_IRO_05:
    scene skyA with Fade(1.0, 1.0, 1.0)
    window auto show dissolve
    "--After a couple more years had passed, I had graduated from high school and had went on to college."
    "Compared to high school, college is an order of magnitude different in terms of both the scale of the facilities and the number of students. For example, the cafeteria where I am now is crowded with students, "
    "but they're all people I don't recognize."
    "Except for the person sitting across from me."
    window auto hide dissolve
    $renpy.pause(delay=0.5, hard=True)
    show orimotoCollegeA with dissolve
    play music "audio/bgm/BGM48.ogg"
    window auto show dissolve
    voice "audio/voice/E4/IRO/05/OR/OR000.ogg"
    kaori "Hikigaya, did you decide on a club~?"
    voice "audio/voice/E4/IRO/05/HA/HA000.ogg"
    hachiman "No, I'm still thinking."
    voice "audio/voice/E4/IRO/05/OR/OR001.ogg"
    kaori "Seriously? Clubs are starting to get filled out and people are getting closer! There won't be any room for you! Hurry up!"
    voice "audio/voice/E4/IRO/05/HA/HA001.ogg"
    hachiman "That just gave me a reason not to rush. Thanks, Orimoto."
    voice "audio/voice/E4/IRO/05/OR/OR002.ogg"
    kaori "Why don't you come to my club then?"
    voice "audio/voice/E4/IRO/05/HA/HA002.ogg"
    hachiman "Your club's an all-rounder, right? I'm gonna be so out of place. T/N: All-rounder clubs in college cover a wide range of activities. Some even call themselves that, but only hold drinking parties."
    "Since we exchanged contact information that day, she actually did invite me, and it turned out our college of choice was the same so we discussed things like exams. We've been spending a lot of time "
    "together."
    "Just as it looks, we both passed our entrance exams and here we are."
    window auto hide dissolve
    $renpy.pause(delay=0.5, hard=True)
    show orimotoCollegeA at topright with dissolve:
        zoom 1.5 xoffset 115 yoffset -30
    window auto show dissolve
    voice "audio/voice/E4/IRO/05/OR/OR003.ogg"
    kaori "Yeah, you're right. That's what my friends in the club tell me. \"Why are you always eating lunch with that gloomy-looking guy?\" and stuff. \"What are you - a care giver?\"; Hilarous."
    voice "audio/voice/E4/IRO/05/HA/HA003.ogg"
    hachiman "It's not funny. Bring your friend here. I'll show him how to eat alone."
    voice "audio/voice/E4/IRO/05/HA/HA004.ogg"
    hachiman "Seriously though, I don't mind being by myself."
    voice "audio/voice/E4/IRO/05/OR/OR004.ogg"
    kaori "...? I know that, but... You've been alone the whole time, Hikigaya. It's hilarious~ I could never do it."
    voice "audio/voice/E4/IRO/05/HA/HA005.ogg"
    hachiman "R-Right. That's why... won't it be bad if you keep eating with me?」"
    voice "audio/voice/E4/IRO/05/OR/OR005.ogg"
    kaori "Huh?"
    voice "audio/voice/E4/IRO/05/HA/HA006.ogg"
    hachiman "........."
    voice "audio/voice/E4/IRO/05/OR/OR006.ogg"
    kaori "Ahhh, yeah, you're right."
    voice "audio/voice/E4/IRO/05/HA/HA007.ogg"
    hachiman "........."
    voice "audio/voice/E4/IRO/05/OR/OR007.ogg"
    kaori "Sorry! That wasn't very nice just now. I didn't mean to make you feel like that. I'm silly like that sometimes..."
    voice "audio/voice/E4/IRO/05/HA/HA008.ogg"
    hachiman "Uh?"
    voice "audio/voice/E4/IRO/05/OR/OR008.ogg"
    kaori "Hikigaya, hang out with me at lunch from now on, too."
    voice "audio/voice/E4/IRO/05/OR/OR009.ogg"
    kaori "I don't care what club friends think."
    voice "audio/voice/E4/IRO/05/OR/OR010.ogg"
    kaori "Being with you kind of cracks me up. So..."
    hide orimotoCollegeA
    show orimotoCollegeA
    with dissolve
    voice "audio/voice/E4/IRO/05/HA/HA009.ogg"
    hachiman "........."
    voice "audio/voice/E4/IRO/05/HA/HA010.ogg"
    hachiman "W-Well, I don't mind if you don't..."
    voice "audio/voice/E4/IRO/05/OR/OR011.ogg"
    kaori "Yeah, right on!"
    "As always, she's very outspoken."
    "However, as she said that one day, she's \"changed\" a little."
    "I began to see self-reflection in her simple-mindedness that sometimes hurts people."
    window auto hide dissolve
    show orimotoCollegeA at topright with dissolve:
        zoom 1.5 xoffset 115 yoffset -30
    window auto show dissolve
    voice "audio/voice/E4/IRO/05/OR/OR012.ogg"
    kaori "Speaking of which, one of my friends from the club asked me: \"What kind of relationship do you guys have?\"."
    voice "audio/voice/E4/IRO/05/OR/OR013.ogg"
    kaori "I said that we've just been friends since middle school, but that kinda didn't feel right."
    voice "audio/voice/E4/IRO/05/OR/OR014.ogg"
    kaori "What are we, actually?"
    voice "audio/voice/E4/IRO/05/HA/HA011.ogg"
    hachiman "........."
    "When she asked me, I suddenly stopped eating."
    "What I can say for sure is that we're not lovers. However, I feel somewhat uncomfortable saying that we are just friends."
    "Perhaps it's because of the ups and downs that we've gone through, but I feel that there's something more to Kaori Orimoto and me than just friends."
    "But I can't find the right words to describe it, so I have to answer Orimoto's question like this..."
    voice "audio/voice/E4/IRO/05/HA/HA012.ogg"
    hachiman "I don't know either."
    window auto hide dissolve
    stop voice
    show orimotoCollegeB with dissolve
    window auto show dissolve
    voice "audio/voice/E4/IRO/05/OR/OR015.ogg"
    kaori "I know, right? Hilarious!"
    voice "audio/voice/E4/IRO/05/HA/HA013.ogg"
    hachiman "It's not that funny."
    window auto hide dissolve
    stop voice
    stop music fadeout 1.0
    show white with Fade(2.0, 0, 1.0, color="#fff")
    $renpy.movie_cutscene("movies/ed04.mkv")
    scene orimotoEnd with Fade(0.5, 1.0, 1.0, color="#fff")
    call game_over("Orimoto Kaori") from _call_game_over_6
    return

label E4_IRO_06:
    voice "audio/voice/E4/IRO/06/HA/HA000.ogg"
    hachiman "............"
    show iroha pout with dissolve
    voice "audio/voice/E4/IRO/06/IR/IR000.ogg"
    iroha "Sen~pai!"
    voice "audio/voice/E4/IRO/06/HA/HA001.ogg"
    hachiman "Hm?"
    show iroha happy with dissolve
    voice "audio/voice/E4/IRO/06/IR/IR001.ogg"
    iroha "About the ski camp I mentioned, I'm really, really looking forward to it, okay? Not as just some fancy dating spot, too."
    voice "audio/voice/E4/IRO/06/HA/HA002.ogg"
    hachiman "What, you like skiing that much?"
    voice "audio/voice/E4/IRO/06/IR/IR002.ogg"
    iroha "No, not really."
    show iroha mid_left happy with dissolve:
        xoffset -35 yoffset 65
    voice "audio/voice/E4/IRO/06/IR/IR003.ogg"
    iroha "But... I'm excited to do something together with my seniors."
    voice "audio/voice/E4/IRO/06/HA/HA003.ogg"
    hachiman "Is that so?"
    show iroha vhappy with dissolve
    voice "audio/voice/E4/IRO/06/IR/IR004.ogg"
    iroha "Yes!"
    "She tilted her head in a foxy manner. But just because she said that, it seemed to be worth making this trip happen."
    window auto hide dissolve
    stop music fadeout 0.5
    jump E5_CMM_01
