image black = "#000000"
image movietext:
    contains:
        "#000"
        size(1280,150)
        xpos 0 ypos -150
        easein 0.25 ypos 0
    contains:
        "#000"
        size(1280,150)
        xpos 0 ypos 720
        easein 0.25 ypos 570
image white = "#FFFFFF"
image red = "#FF0000"
# 雪花效果
image snow_white_small = SnowBlossom("white_small", count=30, border=10, xspeed=(-10, 10), yspeed=(20, 30), start=0, fast=True, horizontal=False)
image snow_white_big = SnowBlossom("white_big", count=20, border=20, xspeed=(-10, 10), yspeed=(20, 30), start=0, fast=True, horizontal=False)
image snow_white:
    contains:
        "snow_white_small"
    contains:
        "snow_white_big"
image snow_white_small_fast1=SnowBlossom("white_small", count=50, border=20, xspeed=(-120, 300), yspeed=(50, 200), start=0, fast=True, horizontal=False)
image snow_white_small_fast2=SnowBlossom("white_big", count=25, border=20, xspeed=(-120, 300), yspeed=(-70, -40), start=0, fast=True, horizontal=False)
image snow_white_big_fast=SnowBlossom("white_big", count=15, border=20, xspeed=(100, 150), yspeed=(60, 100), start=0, fast=True, horizontal=False)
image snow_white_fast:
    contains:
        "snow_white_small_fast1"
    contains:
        "snow_white_small_fast2"
    contains:
        "snow_white_big_fast"
image white_small:
    "liluo_common/common/snow_white_single.png"
    size(4, 4)
    white_alt
image white_big:
    "liluo_common/common/snow_white_single.png"
    size(7, 7)
    white_alt
transform white_alt:
    zoom 1.0
    alpha 0.75
    parallel:
        choice:
            linear 1.0 alpha 0.5
            linear 1.0 alpha 0.75
        choice:
            linear 1.0 alpha 1.0
            linear 1.0 alpha 0.75
        repeat
    parallel:
        choice:
            linear 1.0 zoom 1.25
            linear 1.0 zoom 1.0
        choice:
            linear 1.0 zoom 0.8
            linear 1.0 zoom 1.0
        repeat
image snow_yellow_small = SnowBlossom("yellow_small", count=40, border=10, xspeed=(-2, 50), yspeed=(20, 30), start=0, fast=True, horizontal=False)
image snow_yellow_big = SnowBlossom("yellow_big", count=25, border=20, xspeed=(-2, 50), yspeed=(20, 30), start=0, fast=True, horizontal=False)
image snow_yellow:
    contains:
        "snow_yellow_small"
    contains:
        "snow_yellow_big"
image yellow_small:
    "liluo_common/common/snow_yellow_single.png"
    size(4, 4)
    white_alt
image yellow_big:
    "liluo_common/common/snow_yellow_single.png"
    size(7, 7)
    white_alt

image snow_blood1=SnowBlossom("blood_single", count=50, border=20, xspeed=(-120, 300), yspeed=(50, 200), start=0, fast=True, horizontal=False)
image snow_blood2=SnowBlossom("blood_single", count=25, border=20, xspeed=(-100, 240), yspeed=(-70, -40), start=0, fast=True, horizontal=False)
image snow_blood:
    contains:
        "snow_blood1"
    contains:
        "snow_blood2"
image blood_single:
    "liluo_common/common/snow_blood_single.png"
    blood_alt
transform blood_alt:
    zoom 1.0
    alpha 0.9
    parallel:
        choice:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.9
        choice:
            linear 1.0 alpha 1.0
            linear 1.0 alpha 0.9
        repeat
    parallel:
        choice:
            linear 1.0 zoom 1.2
            linear 1.0 zoom 1.0
        choice:
            linear 1.0 zoom 0.8
            linear 1.0 zoom 1.0
        repeat
    parallel:
        choice:
            linear 1.0 xzoom -1
            linear 1.0 xzoom 1
        choice:
            linear 1.0 yzoom -1
            linear 1.0 yzoom 1
        choice:
            linear 1.0 yzoom 1
            linear 1.0 yzoom 1
        repeat
    parallel:
        rotate 0
        linear 10 rotate 360
        repeat

# 流血
image blood:
    subpixel True
    "liluo_common/common/snow_blood_single.png"
    zoom 0.75
    alpha 0.75
    choice:
        linear 0.25 zoom 0
    choice:
        linear 0.35 zoom 0
    choice:
        linear 0.35 zoom 0
    choice:
        linear 0.55 zoom 0

image blood_thorn:
    size (1, 1)
    truecenter
    Blood("blood", density=50.0, particleTime=1.0, dripChance=0.00, dripSpeedX=0.0, dripSpeedY=120.0, dripTime=180.0, burstSize=80, burstSpeedX=192.0, burstSpeedY=108.0, numSquirts=5, squirtPower=500, squirtTime=0.20).sm
image blood_boom:
    size (1, 1)
    truecenter
    Blood("blood", density=20.0, particleTime=1.0, dripChance=0.00, dripSpeedX=0.0, dripSpeedY=120.0, dripTime=180.0, burstSize=80, burstSpeedX=96.0, burstSpeedY=54.0, numSquirts=40, squirtPower=350, squirtTime=0.12).sm
image blood_shed:
    size (1, 1)
    truecenter
    Blood("blood", dripChance=0.005, numSquirts=0, burstSize=0).sm


# 灰屏
image noise:
    truecenter
    "liluo_common/common/noise1.png"
    pause 0.1
    "liluo_common/common/noise2.png"
    pause 0.1
    "liluo_common/common/noise3.png"
    pause 0.1
    "liluo_common/common/noise4.png"
    pause 0.1
    xzoom -1
    "liluo_common/common/noise1.png"
    pause 0.1
    "liluo_common/common/noise2.png"
    pause 0.1
    "liluo_common/common/noise3.png"
    pause 0.1
    "liluo_common/common/noise4.png"
    pause 0.1
    yzoom -1
    "liluo_common/common/noise1.png"
    pause 0.1
    "liluo_common/common/noise2.png"
    pause 0.1
    "liluo_common/common/noise3.png"
    pause 0.1
    "liluo_common/common/noise4.png"
    pause 0.1
    xzoom 1
    "liluo_common/common/noise1.png"
    pause 0.1
    "liluo_common/common/noise2.png"
    pause 0.1
    "liluo_common/common/noise3.png"
    pause 0.1
    "liluo_common/common/noise4.png"
    pause 0.1
    yzoom 1
    repeat

image linework:
    truecenter
    "liluo_common/common/linework_01.png"
    pause 0.06
    "liluo_common/common/linework_02.png"
    pause 0.06
    "liluo_common/common/linework_03.png"
    pause 0.06
    repeat

image fastwork:
    truecenter
    "liluo_common/common/fastwork_01.png"
    pause 0.06
    "liluo_common/common/fastwork_02.png"
    pause 0.06
    "liluo_common/common/fastwork_03.png"
    pause 0.06
    "liluo_common/common/fastwork_04.png"
    pause 0.06
    repeat

image credits_text = ParameterizedText(style="credits_text", ycenter = 0.5, xcenter=0.5)
image credits_text_up = ParameterizedText(style="credits_text", ycenter = 0.4, xcenter=0.5)
image credits_text_down = ParameterizedText(style="credits_text", ycenter = 0.6, xcenter=0.5)
image credits_text_big = ParameterizedText(style="credits_text_big", ycenter = 0.5, xcenter=0.5)

style credits_text:
    color "#fff"
    size 30
    text_align 0.5
    outlines [ (absolute(3), "#000000", absolute(0), absolute(0)) ]
    slow_cps 35

style credits_text_big:
    color "#fff"
    size 45
    text_align 0.5
    outlines [ (absolute(3), "#000000", absolute(0), absolute(0)) ]
    slow_cps 35
