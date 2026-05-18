
#loading_screen() created to reduce duplication of lines of code since most of the code os the same. Changes can be made for specific loading screens
#_image = layered image,
#filename = for bgm name[only the numbers] e.g, BGM00.ogg use "00" and
#for sfx text after SE e.g, SE01_00.ogg use "01_00",
#transition = transition, deafult = "dissolve"
#duration = "long" or "short", determines when the screen fades away
label loading_screen(_image=0,filename='',transition="dissolve",duration="long"):
    scene loading
    $bgmFlag = False
    if transition == "fade":
        with Fade(1.0, 0.5, 1.0)
    if transition == "dissolve":
        with Dissolve(1.0)

    if filename and len(filename) > 2:
        $_sound = "audio/sfx/SE" + filename[0:2]  + "/SE" + filename + ".ogg"
        play sound ["<silence 2.0>", _sound]
    elif filename:
        $bgmFlag = True
        $bgm = "audio/bgm/BGM" + filename + ".ogg"
        play music bgm

    show paw behind card:
        xpos 1503
        ypos 770
    $renpy.pause(delay=0.5, hard=True)
    show paw behind card as paw2:
        xpos 1327
        ypos 754
    $renpy.pause(delay=0.5, hard=True)

    if _image:
        if _image == 1:
            image chara1 = Flatten("yui coat mid_center pout")
            show chara1 zorder 1 at left:
                xoffset 323 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 2:
            image chara2 = Flatten("iroha coat mid_center vhappy")
            show chara2 zorder 1 at left:
                xoffset 323 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 3:
            image chara3 = Flatten("haruno sweater mid_center happy")
            show chara3 zorder 1 at left:
                xoffset 328 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 4:
            image chara4 = Flatten("komachi coat mid_left vhappy")
            show chara4 zorder 1 at left:
                xoffset 289 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 5:
            image chara5 = Flatten("saki school mid_right happy")
            show chara5 zorder 1 at left:
                xoffset 80 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 6:
            image chara6 = Flatten("saki coat mid_right happy")
            show chara6 zorder 1 at left:
                xoffset 82 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 7:
            image chara7 = Flatten("saki home mid_right vhappy")
            show chara7 zorder 1 at left:
                xoffset 80 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 8:
            image chara8 = Flatten("iroha school mid_center happy")
            show chara8 zorder 1 at left:
                xoffset 311 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 9:
            image chara9 = Flatten("iroha school mid_center vhappy")
            show chara9 zorder 1 at left:
                xoffset 311 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 10:
            image chara10 = Flatten("iroha coat mid_center happy")
            show chara10 zorder 1 at left:
                xoffset 311 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 11:
            image chara11 = Flatten("iroha school mid_center happy")
            show chara11 zorder 1 at left:
                xoffset 311 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 12:
            image chara12 = Flatten("yukino school mid_center happy")
            show chara12 zorder 1 at left:
                xoffset 31 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 13:
            image chara13 = Flatten("iroha school mid_left happy")
            show chara13 zorder 1 at left:
                xoffset 255 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 14:
            image chara14 = Flatten("haruno coat mid_left sly")
            show chara14 zorder 1 at left:
                xoffset 208 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 15:
            image chara15 = Flatten("haruno sweater mid_center sly")
            show chara15 zorder 1 at left:
                xoffset 327 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 16:
            image chara16 = Flatten("komachi home mid_center happy")
            show chara16 zorder 1 at left:
                xoffset 62 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 17:
            image chara17 = Flatten("komachi coat mid_center happy")
            show chara17 zorder 1 at left:
                xoffset 62 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 18:
            image chara18 = Flatten("yukino home_glasses mid_center vhappy")
            show chara18 zorder 1 at left:
                xoffset 31 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 19:
            image chara19 = Flatten("yukino school mid_center vhappy")
            show chara19 zorder 1 at left:
                xoffset 31 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 20:
            image chara20 = Flatten("yukino coat mid_center happy")
            show chara20 zorder 1 at left:
                xoffset 31 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 21:
            image chara21 = Flatten("saki school mid_left vhappy")
            show chara21 zorder 1 at left:
                xoffset 230 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 22:
            image chara22 = Flatten("haruno sweater mid_center worried")
            show chara22 zorder 1 at left:
                xoffset 327 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 23:
            image chara23 = Flatten("yukino coat mid_left happy")
            show chara23 zorder 1 at left:
                xoffset 231 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 24:
            image chara24 = Flatten("yukino coat mid_center concerned")
            show chara24 zorder 1 at left:
                xoffset 31 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 25:
            image chara25 = Flatten("hiratsuka home mid_left sad")
            show chara25 zorder 1 at left:
                xoffset 220 yoffset 82 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 26:
            image chara26 = Flatten("hiratsuka school mid_center happy")
            show chara26 zorder 1 at left:
                xoffset 117 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 27:
            image chara27 = Flatten("hiratsuka school mid_left angry")
            show chara27 zorder 1 at left:
                xoffset 220 yoffset 82 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 28:
            image chara28 = Flatten("hiratsuka home mid_center happy")
            show chara28 zorder 1 at left:
                xoffset 117 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 29:
            image chara29 = Flatten("yui school mid_center pout")
            show chara29 zorder 1 at left:
                xoffset 231 yoffset 75 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 30:
            image chara30 = Flatten("yui school mid_center happy")
            show chara30 zorder 1 at left:
                xoffset 231 yoffset 75 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 31:
            image chara31 = Flatten("yui coat mid_left vhappy")
            show chara31 zorder 1 at left:
                xoffset 231 yoffset 75 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 32:
            image chara32 = Flatten("yumiko school mid_center happy")
            show chara32 zorder 1 at left:
                xoffset 132 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        elif _image == 33:
            image chara33 = Flatten("meguri coat mid happy")
            show chara33 zorder 1 at left:
                xoffset 278 yoffset 76 alpha 0
                parallel:
                    linear 1.5 alpha 1.0
        # if layered image not available add here
    show paw behind card as paw3:
        xpos 1211
        ypos 634
    $renpy.pause(delay=0.5, hard=True)
    show paw behind card as paw4:
        xpos 1033
        ypos 618
    $renpy.pause(delay=0.5, hard=True)
    show paw behind card as paw5:
        xpos 923
        ypos 492
    $renpy.pause(delay=0.5, hard=True)
    show paw behind card as paw6:
        xpos 741
        ypos 474
    if duration == "short":
        show black:
            alpha 0
            parallel:
                linear 1.0 alpha 1.0
    $renpy.pause(delay=0.5, hard=True)
    show paw behind card as paw7:
        xpos 649
        ypos 356
    $renpy.pause(delay=0.5, hard=True)
    if duration == "short":
        stop music fadeout 1.0
        stop sound fadeout 0.5
        return
    if _image == 25:
        hide chara25
        show hiratsuka home mid_left happy zorder 1 at left:
            xoffset 220 yoffset 82
        with dissolve
    show paw behind card as paw8:
        xpos 467
        ypos 340
    $renpy.pause(delay=0.5, hard=True)
    show paw behind card as paw9:
        xpos 385
        ypos 220
    $renpy.pause(delay=0.25, hard=True)
    if duration == "long" and bgmFlag and not _image:
        show black zorder 2:
            alpha 0
            parallel:
                linear 1.0 alpha 1.0
    $renpy.pause(delay=0.25, hard=True)
    # since no 2d live
    if _image == 13:
        hide chara13
        show iroha school mid_left vhappy zorder 1 at left:
            xoffset 255 yoffset 76
        with dissolve
    elif _image == 23:
        hide chara23
        show yukino coat mid_left pout zorder 1 at left:
            xoffset 231 yoffset 76
        with dissolve
    show paw behind card as paw10:
        xpos 200
        ypos 200
    $renpy.pause(delay=0.5, hard=True)
    show paw behind card as paw11:
        xpos 89
        ypos 82
    $renpy.pause(delay=0.25, hard=True)
    if duration == "long" and _image:
        show black zorder 2:
            alpha 0
            parallel:
                linear 1.0 alpha 1.0
    $renpy.pause(delay=0.25, hard=True)
    show paw behind card as paw12:
        xpos -95
        ypos 62
    $renpy.pause(delay=0.5, hard=True)
    stop music fadeout 1.0
    stop sound fadeout 0.5
    return

# need to fix paw prints appearing on top of cards, and maybe improve card transitions and positions, and fix the weird screen effect.
label card_loading:
    scene loading with dissolve
    show loading_circle:
        zoom 0.75
        xpos 1670
        ypos 830
    with dissolve
    show loading_text:
        zoom 0.75
        xpos 1707
        ypos 945
    with dissolve
    show paw behind card:
        xpos 1595
        ypos 790
    $renpy.pause(delay=0.5, hard=True)
    show paw behind card as paw2:
        xpos 1445
        ypos 755
    $renpy.pause(delay=0.5, hard=True)
    play sound "audio/sfx/3cards.ogg"
    show card:
        xcenter 0.4
        ycenter 0.5
        xoffset 1000
        linear 0.088 xoffset 0
        on hide:
            linear 0.16 xoffset -1000
    with None
    $renpy.pause(delay=0.088, hard=True)
    #with CropMove(0.088, "slideleft", False)
    show card as card2:
        xcenter 0.5
        ycenter 0.5
        xoffset 1000
        linear 0.088 xoffset 0
        on hide:
            linear 0.16 xoffset -1000
    with None
    $renpy.pause(delay=0.088, hard=True)
    #with CropMove(0.088, "slideleft", False)
    show card as card3:
        xcenter 0.6
        ycenter 0.5
        xoffset 1000
        linear 0.088 xoffset 0
        on hide:
            linear 0.16 xoffset -1000
    with None
    $renpy.pause(delay=0.088, hard=True)
    #with CropMove(0.088, "slideleft", False)
    $renpy.pause(delay=0.25, hard=True)
    show paw behind card as paw3:
        xpos 1280
        ypos 655
    $renpy.pause(delay=0.4, hard=True)
    show paw behind card as paw4:
        xpos 1130
        ypos 620
    $renpy.pause(delay=0.38, hard=True)
    show paw behind card as paw5:
        xpos 965
        ypos 520
    hide card3 with None
    #with CropMove(0.16, "slideleft", False)
    $renpy.pause(delay=0.16, hard=True)
    hide card2 with None
    #with CropMove(0.16, "slideleft", False)
    $renpy.pause(delay=0.16, hard=True)
    hide card with None
    #with CropMove(0.1, "slideleft", False)
    $renpy.pause(delay=0.1, hard=True)
    show paw behind card as paw6:
        xpos 815
        ypos 485
    $renpy.pause(delay=0.4, hard=True)
    show paw behind card as paw7:
        xpos 695
        ypos 385
    $renpy.pause(delay=0.4, hard=True)
    show paw behind card as paw8:
        xpos 500
        ypos 350
    $renpy.pause(delay=0.35, hard=True)
    show paw behind card as paw9:
        xpos 335
        ypos 250
    $renpy.pause(delay=0.3, hard=True)
    show paw behind card as paw10:
        xpos 185
        ypos 215
    $renpy.pause(delay=0.25, hard=True)
    show paw behind card as paw11:
        xpos 60
        ypos 115
    $renpy.pause(delay=0.2, hard=True)
    show paw behind card as paw12:
        xpos -90
        ypos 80
    stop sound fadeout 1.0
    return

# for game over
# route = route name
# end_type = best, good, normal, and None if route has only one ending
label game_over(route, end_type = ""):
    pause
    scene black with Dissolve(2.0)
    $renpy.pause(delay=1.0, hard=True)
    call screen end_card(route, end_type) with dissolve
    $renpy.pause(delay=0.5, hard=True)
    return

# incomplete
label start_card_game(card_list, bgm = "31"):
    $bgm = "audio/bgm/BGM" + filename + ".ogg"
    play music bgm
    return
