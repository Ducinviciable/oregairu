# $imageInfo = ""
# $previous = ""
# label komachi(face="pout", info="", _pause=0):
#     hide komachi
#     if info:
#         $imageInfo = info
#     else:
#         $info = imageInfo
#     if info == "coat mid_center":
#         if face == "pout":
#             image komachi pout= LiveComposite(
#             (844, 1080),
#             (0, 0), "images/chara/komachi/mid/coat/center/pout.png",
#             (0, 0), "images/chara/komachi/mid/coat/center/pout.png",
#             (0,0), WhileSpeaking("komachi", "komachi speak pout", "images/chara/komachi/mid/coat/center/pout.png"),
#             )
            
#             image komachi speak pout:
#                 .05
#                 "images/chara/komachi/mid/coat/center/pout.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/komachi/mid/coat/center/pout1.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/komachi/mid/coat/center/pout2.png"
#                 .1
#                 repeat
#         elif face == "happy":
#             image komachi happy = LiveComposite(
#             (844, 1080),
#             (0, 0), "images/chara/komachi/mid/coat/center/pout.png",
#             (0, 0), "images/chara/komachi/mid/coat/center/happy.png",
#             (0,0), WhileSpeaking("komachi", "komachi speak happy", "images/chara/komachi/mid/coat/center/happy.png"),
#             )
            
#             image komachi speak happy:
#                 .05
#                 "images/chara/komachi/mid/coat/center/happy.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/komachi/mid/coat/center/happy1.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/komachi/mid/coat/center/happy2.png"
#                 .1
#                 repeat
#         elif face == "vhappy":
#             image komachi vhappy = LiveComposite(
#             (844, 1080),
#             (0, 0), "images/chara/komachi/mid/coat/center/pout.png",
#             (0, 0), "images/chara/komachi/mid/coat/center/vhappy.png",
#             (0,0), WhileSpeaking("komachi", "komachi speak vhappy", "images/chara/komachi/mid/coat/center/vhappy.png"),
#             )
            
#             image komachi speak vhappy:
#                 .05
#                 "images/chara/komachi/mid/coat/center/vhappy.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/komachi/mid/coat/center/vhappy1.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/komachi/mid/coat/center/vhappy2.png"
#                 .1
#                 repeat


# label hiratsuka(face="pout", info="", _pause=0):
#     hide hiratsuka
#     if info:
#         $imageInfo = info
#     else:
#         $info = imageInfo
#     if info == "coat mid_center":
#         if face == "pout":
#             image hiratsuka pout= LiveComposite(
#             (844, 1080),
#             (0, 0), "images/chara/hiratsuka/mid/coat/center/pout.png",
#             (0, 0), "images/chara/hiratsuka/mid/coat/center/pout.png",
#             (0,0), WhileSpeaking("hiratsuka", "hiratsuka speak pout", "images/chara/hiratsuka/mid/coat/center/pout.png"),
#             )
            
#             image hiratsuka speak pout:
#                 .05
#                 "images/chara/hiratsuka/mid/coat/center/pout.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/hiratsuka/mid/coat/center/pout1.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/hiratsuka/mid/coat/center/pout2.png"
#                 .1
#                 repeat
#         elif face == "happy":
#             image hiratsuka happy = LiveComposite(
#             (844, 1080),
#             (0, 0), "images/chara/hiratsuka/mid/coat/center/pout.png",
#             (0, 0), "images/chara/hiratsuka/mid/coat/center/happy.png",
#             (0,0), WhileSpeaking("hiratsuka", "hiratsuka speak happy", "images/chara/hiratsuka/mid/coat/center/happy.png"),
#             )
            
#             image hiratsuka speak happy:
#                 .05
#                 "images/chara/hiratsuka/mid/coat/center/happy.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/hiratsuka/mid/coat/center/happy1.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/hiratsuka/mid/coat/center/happy2.png"
#                 .1
#                 repeat
#         elif face == "vhappy":
#             image hiratsuka vhappy = LiveComposite(
#             (844, 1080),
#             (0, 0), "images/chara/hiratsuka/mid/coat/center/pout.png",
#             (0, 0), "images/chara/hiratsuka/mid/coat/center/vhappy.png",
#             (0,0), WhileSpeaking("hiratsuka", "hiratsuka speak vhappy", "images/chara/hiratsuka/mid/coat/center/vhappy.png"),
#             )
            
#             image hiratsuka speak vhappy:
#                 .05
#                 "images/chara/hiratsuka/mid/coat/center/vhappy.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/hiratsuka/mid/coat/center/vhappy1.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/hiratsuka/mid/coat/center/vhappy2.png"
#                 .1
#                 repeat
#     if info == "coat mid_left":
#         if face == "pout":
#             image hiratsuka pout= LiveComposite(
#             (844, 1080),
#             (0, 0), "images/chara/hiratsuka/mid/coat/left/pout.png",
#             (0, 0), "images/chara/hiratsuka/mid/coat/left/pout.png",
#             (0,0), WhileSpeaking("hiratsuka", "hiratsuka speak pout", "images/chara/hiratsuka/mid/coat/left/pout.png"),
#             )
            
#             image hiratsuka speak pout:
#                 .05
#                 "images/chara/hiratsuka/mid/coat/left/pout.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/hiratsuka/mid/coat/left/pout1.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/hiratsuka/mid/coat/left/pout2.png"
#                 .1
#                 repeat
#         elif face == "happy":
#             image hiratsuka happy = LiveComposite(
#             (844, 1080),
#             (0, 0), "images/chara/hiratsuka/mid/coat/left/pout.png",
#             (0, 0), "images/chara/hiratsuka/mid/coat/left/happy.png",
#             (0,0), WhileSpeaking("hiratsuka", "hiratsuka speak happy", "images/chara/hiratsuka/mid/coat/left/happy.png"),
#             )
            
#             image hiratsuka speak happy:
#                 .05
#                 "images/chara/hiratsuka/mid/coat/left/happy.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/hiratsuka/mid/coat/left/happy1.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/hiratsuka/mid/coat/left/happy2.png"
#                 .1
#                 repeat
#         elif face == "vhappy":
#             image hiratsuka vhappy = LiveComposite(
#             (844, 1080),
#             (0, 0), "images/chara/hiratsuka/mid/coat/left/pout.png",
#             (0, 0), "images/chara/hiratsuka/mid/coat/left/vhappy.png",
#             (0,0), WhileSpeaking("hiratsuka", "hiratsuka speak vhappy", "images/chara/hiratsuka/mid/coat/left/vhappy.png"),
#             )
            
#             image hiratsuka speak vhappy:
#                 .05
#                 "images/chara/hiratsuka/mid/coat/left/vhappy.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/hiratsuka/mid/coat/left/vhappy1.png"
#                 choice:
#                     .05
#                 choice:
#                     .1
#                 choice:
#                     .15
#                 choice:
#                     .2
#                 "images/chara/hiratsuka/mid/coat/left/vhappy2.png"
#                 .1
#                 repeat

# # image komachi coat mid_center happy = LiveComposite(
# #     (844, 1080),
# #     (0, 0), "images/chara/komachi/mid/coat/center/pout.png",
# #     (0, 0), "images/chara/komachi/mid/home/center/happy.png",
# #     (0,0), WhileSpeaking("komachi", "komachi speak", "images/chara/komachi/mid/home/center/happy.png"),)

# # image komachi speak:
# #     .05
# #     "images/chara/komachi/mid/home/center/happy.png"
# #     choice:
# #         .05
# #     choice:
# #         .1
# #     choice:
# #         .15
# #     choice:
# #         .2
# #     "images/chara/komachi/mid/home/center/happy1.png"
# #     choice:
# #         .05
# #     choice:
# #         .1
# #     choice:
# #         .15
# #     choice:
# #         .2
# #     "images/chara/komachi/mid/home/center/happy2.png"
# #     .1
# #     repeat