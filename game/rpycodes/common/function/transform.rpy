#出现
transform fs11(x=0.5, z=0.55):
    subpixel True
    ycenter 1.12
    xcenter x
    yoffset 0 zoom z*1.00 alpha 1.00

transform bs11:
    subpixel True
    ycenter 1.52
    zoom 0.54 alpha 0.00
    xcenter 0.5 yoffset -285
    parallel:
        easein .12 alpha 1.0
    parallel:
        easein .12 zoom 0.58
        easein .12 zoom 0.55
    time 0.24
    ycenter 1.12 yoffset 0

transform show_first(x=0.5, z=0.55):
    subpixel True
    on show:
        ycenter 1.12
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -33
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        easein .25 xcenter x zoom z*1.00 yoffset 0 ycenter 1.12
transform s11:
    show_first(0.5)
transform s21:
    show_first(0.3)
transform s22:
    show_first(0.7)
transform s31:
    show_first(0.185)
transform s32:
    show_first(0.5)
transform s33:
    show_first(0.815)
transform s41:
    show_first(0.2)
transform s42:
    show_first(0.4)
transform s43:
    show_first(0.6)
transform s44:
    show_first(0.8)

transform show_firstrl(x=0.5, z=0.55):
    subpixel True
    on show:
        ycenter 1.12
        zoom z*0.98 alpha 0.00
        xcenter x xoffset 110
        easein .5 xoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        easein .25 xcenter x zoom z*1.00 yoffset 0 ycenter 1.12
transform s11rl:
    show_firstrl(0.5)
transform s21rl:
    show_firstrl(0.3)
transform s22rl:
    show_firstrl(0.7)
transform s31rl:
    show_firstrl(0.185)
transform s32rl:
    show_firstrl(0.5)
transform s33rl:
    show_firstrl(0.815)
transform s41rl:
    show_firstrl(0.2)
transform s42rl:
    show_firstrl(0.4)
transform s43rl:
    show_firstrl(0.6)
transform s44rl:
    show_firstrl(0.8)

#小身体
transform fss11(x=0.5, z=0.36):
    subpixel True
    xcenter x zoom z*1.00 yoffset 0 ycenter 0.84
transform show_fast(x=0.5, z=0.36):
    subpixel True
    on show:
        ycenter 0.84
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -22
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        easein .25 xcenter x zoom z*1.00 yoffset 0 ycenter 0.84
transform sb11:
    show_commmon(0.5)
transform sb21:
    show_commmon(0.3)
transform sb22:
    show_commmon(0.7)
transform sb31:
    show_commmon(0.185)
transform sb32:
    show_commmon(0.5)
transform sb33:
    show_commmon(0.815)
transform sb41:
    show_commmon(0.2)
transform sb42:
    show_commmon(0.4)
transform sb43:
    show_commmon(0.6)
transform sb44:
    show_commmon(0.8)

transform show_fastrl(x=0.5, z=0.36):
    subpixel True
    on show:
        ycenter 0.84
        zoom z*0.98 alpha 0.00
        xcenter x xoffset 72
        easein .25 xoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        easein .25 xcenter x zoom z*1.00 yoffset 0 ycenter 0.84
transform sb11rl:
    show_commmonrl(0.5)
transform sb21rl:
    show_commmonrl(0.3)
transform sb22rl:
    show_commmonrl(0.7)
transform sb31rl:
    show_commmonrl(0.185)
transform sb32rl:
    show_commmonrl(0.5)
transform sb33rl:
    show_commmonrl(0.815)
transform sb41rl:
    show_commmonrl(0.2)
transform sb42rl:
    show_commmonrl(0.4)
transform sb43rl:
    show_commmonrl(0.6)
transform sb44rl:
    show_commmonrl(0.8)


#大头
transform fsb(x=0.5, z=1.0):
    subpixel True
    alpha 1.00
    easein .25 xcenter x zoom z*1.00 yoffset 0 ycenter 1.75
transform show_commmon(x=0.5, z=1.0):
    subpixel True
    on show:
        ycenter 1.75
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -40
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        easein .25 xcenter x zoom z*1.00 yoffset 0 ycenter 1.75
transform ss11:
    show_fast(0.5)
transform ss21:
    show_fast(0.3)
transform ss22:
    show_fast(0.7)
transform ss31:
    show_fast(0.185)
transform ss32:
    show_fast(0.5)
transform ss33:
    show_fast(0.815)

transform show_commmonrl(x=0.5, z=1.0):
    subpixel True
    on show:
        ycenter 1.75
        zoom z*0.98 alpha 0.00
        xcenter x xoffset 200
        easein .25 xoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        easein .25 xcenter x zoom z*1.00 yoffset 0 ycenter 1.75
transform ss11rl:
    show_fastrl(0.5)
transform ss21rl:
    show_fastrl(0.3)
transform ss22rl:
    show_fastrl(0.7)
transform ss31rl:
    show_fastrl(0.185)
transform ss32rl:
    show_fastrl(0.5)
transform ss33rl:
    show_fastrl(0.815)
#蹲下
transform crouch(y = 44):
    subpixel True
    on show:
        yoffset 0
        easein .5 yoffset y alpha 1.00
    on replace:
        easein .5 yoffset y alpha 1.00
transform nd11:
    crouch(38)
transform nd:
    crouch(38)
transform nds:
    crouch(26)
transform ndb:
    crouch(68)
##升起
transform nu11:
    crouch(-38)
transform nu:
    crouch(-38)
transform nus:
    crouch(-26)
transform nub:
    crouch(-68)

#跳跃
transform leap(y = 44):
    subpixel True
    easein .14 yoffset -y alpha 1.00
    easeout .14 yoffset 0 alpha 1.00

transform j11:
    leap(30)
transform j:
    leap(30)
transform jb:
    leap(56)
transform jb11:
    leap(56)
transform js:
    leap(20)
transform js11:
    leap(20)
#点头
transform nod(y = 44):
    subpixel True
    easein .24 yoffset y alpha 1.00
    easeout .24 yoffset 0 alpha 1.00

transform n11:
    nod(36)
transform n:
    nod(36)
transform nb:
    nod(70)
transform nb11:
    nod(70)
transform ns:
    nod(24)
transform ns11:
    nod(24)

# 放大到头像
transform wb:
    subpixel True
    xcenter 0.5 ycenter 0.63 zoom 1.8

transform wbf:
    subpixel True
    xcenter 0.5 ycenter 0.42 zoom 0.56

transform wb2:
    subpixel True
    xcenter 0.5 ycenter 0.82 zoom 2.77

transform wbf2:
    subpixel True
    xcenter 0.5 ycenter 0.38 zoom 0.37

#hide
transform h(z=0.55, y=33):
    # on hide:
    subpixel True
    alpha 1.0
    easein .25 zoom z*1.05 alpha 0.00 yoffset -y
transform hs:
    h(0.36, 22)
transform hb:
    h(1.0, 40)

transform hrl(z=0.55, y=100):
    subpixel True
    zoom z alpha 1.0
    xoffset 0
    parallel:
        easein .25 alpha 0.0
    parallel:
        linear .5 xoffset -y
transform hsrl:
    hrl(0.36, 67)
transform hbrl:
    hrl(1.0, 130)

#rock(time)
transform r(t=0.15):
    subpixel True
    easein t xoffset 20 alpha 1.0
    easeout t xoffset 0
    easein t xoffset -15
    easeout t xoffset 0
    easein t xoffset 10
    easeout t xoffset 0
    easein t xoffset -5
    ease t xoffset 0
transform rr(t=0.15):
    subpixel True
    block:
        easein t xoffset 20
        easeout t xoffset 0
        easein t xoffset -20
        easeout t xoffset 0
        repeat
#疑问
transform why_alt(x=640):
    xcenter x-95 ycenter 150 zoom 0.70 alpha 0.00 subpixel True
    easein 0.3 xcenter x-115 ycenter 110 alpha 1.00
    easein 0.4 xcenter x-95 ycenter 150
    easein 0.5
    easein 1.0 xcenter x-75 ycenter 190 alpha 0.00
image why11:
    "liluo_common/common/facial/why.png"
    why_alt(x=640)
image why21:
    "liluo_common/common/facial/why.png"
    why_alt(x=384)
image why22:
    "liluo_common/common/facial/why.png"
    why_alt(x=896)
image why31:
    "liluo_common/common/facial/why.png"
    why_alt(x=237)
image why32:
    "liluo_common/common/facial/why.png"
    why_alt(x=640)
image why33:
    "liluo_common/common/facial/why.png"
    why_alt(x=1043)

#汗
transform sinkwater(x=640):
    xcenter x+120 ycenter 265 zoom 0.3 alpha 0.00 subpixel True
    parallel:
        easein 1.5 ycenter 285
    parallel:
        linear 0.25 alpha 1.0
    time 1.0
    linear 0.5 alpha 0.0
image water11:
    "liluo_common/common/facial/water.png"
    sinkwater(x=640)
image water21:
    "liluo_common/common/facial/water.png"
    sinkwater(x=384)
image water22:
    "liluo_common/common/facial/water.png"
    sinkwater(x=896)
image water31:
    "liluo_common/common/facial/water.png"
    sinkwater(x=237)
image water32:
    "liluo_common/common/facial/water.png"
    sinkwater(x=640)
image water33:
    "liluo_common/common/facial/water.png"
    sinkwater(x=1043)

#混乱
transform emmm(x=640):
    xcenter x-107 ycenter 155 zoom 0.8 alpha 0.00 subpixel True
    parallel:
        linear 0.25 alpha 1.00 zoom 0.5
        time 2.0
        linear 0.25 alpha 0.00 zoom 0.8
    parallel:
        easeout_bounce 0.13 xcenter x-102
        easeout_bounce 0.13 xcenter x-112
        repeat
    parallel:
        easeout_bounce 0.2 ycenter 165
        easeout_bounce 0.2 ycenter 145
        repeat
image emm11:
    "liluo_common/common/facial/emmm.png"
    emmm(x=640)
image emm21:
    "liluo_common/common/facial/emmm.png"
    emmm(x=384)
image emm22:
    "liluo_common/common/facial/emmm.png"
    emmm(x=896)
image emm31:
    "liluo_common/common/facial/emmm.png"
    emmm(x=237)
image emm32:
    "liluo_common/common/facial/emmm.png"
    emmm(x=640)
image emm33:
    "liluo_common/common/facial/emmm.png"
    emmm(x=1043)

#慌张
transform rush:
    subpixel True
    alpha 1.0
    linear 1.0 alpha 0.0
image rush11:
    "liluo_common/common/facial/amazing_1.png"
    xcenter 640 ycenter 320 zoom 0.7 alpha 1.00 subpixel True
    pause 0.1
    "liluo_common/common/facial/amazing_2.png"
    xcenter 640 ycenter 320 zoom 0.7 alpha 1.00 subpixel True
    pause 0.1
    repeat
    time 1.0
    rush
image rush21:
    "liluo_common/common/facial/amazing_1.png"
    xcenter 384 ycenter 320 zoom 0.7 alpha 1.00 subpixel True
    pause 0.1
    "liluo_common/common/facial/amazing_2.png"
    xcenter 384 ycenter 320 zoom 0.7 alpha 1.00 subpixel True
    pause 0.1
    repeat
    time 1.0
    rush
image rush22:
    "liluo_common/common/facial/amazing_1.png"
    xcenter 896 ycenter 320 zoom 0.7 alpha 1.00 subpixel True
    pause 0.1
    "liluo_common/common/facial/amazing_2.png"
    xcenter 896 ycenter 320 zoom 0.7 alpha 1.00 subpixel True
    pause 0.1
    repeat
    time 1.0
    rush
image rush31:
    "liluo_common/common/facial/amazing_1.png"
    xcenter 237 ycenter 320 zoom 0.7 alpha 1.00 subpixel True
    pause 0.1
    "liluo_common/common/facial/amazing_2.png"
    xcenter 237 ycenter 320 zoom 0.7 alpha 1.00 subpixel True
    pause 0.1
    repeat
    time 1.0
    rush
image rush32:
    "liluo_common/common/facial/amazing_1.png"
    xcenter 640 ycenter 320 zoom 0.7 alpha 1.00 subpixel True
    pause 0.1
    "liluo_common/common/facial/amazing_2.png"
    xcenter 640 ycenter 320 zoom 0.7 alpha 1.00 subpixel True
    pause 0.1
    repeat
    time 1.0
    rush
image rush33:
    "liluo_common/common/facial/amazing_1.png"
    xcenter 1043 ycenter 320 zoom 0.7 alpha 1.00 subpixel True
    pause 0.1
    "liluo_common/common/facial/amazing_2.png"
    xcenter 1043 ycenter 320 zoom 0.7 alpha 1.00 subpixel True
    pause 0.1
    repeat
    time 1.0
    rush

#惊讶
transform amazing(x=640):
    xcenter x-125 ycenter 150 zoom 0.72 alpha 1.00 subpixel True
    block:
        linear 0.2 alpha 1.0
        linear 0.0 alpha 0.0
        linear 0.2 alpha 0.0
        linear 0.0 alpha 1.0
        linear 0.2 alpha 1.0
        linear 0.0 alpha 0.0
        linear 0.2 alpha 0.0
        linear 0.0 alpha 1.0
        linear 0.5 alpha 1.0
        linear 0.3 alpha 0.0
image amaz11:
    "liluo_common/common/facial/happy_2.png"
    amazing(x=640)
image amaz21:
    "liluo_common/common/facial/happy_2.png"
    amazing(x=384)
image amaz22:
    "liluo_common/common/facial/happy_2.png"
    amazing(x=896)
image amaz31:
    "liluo_common/common/facial/happy_2.png"
    amazing(x=237)
image amaz32:
    "liluo_common/common/facial/happy_2.png"
    amazing(x=640)
image amaz33:
    "liluo_common/common/facial/happy_2.png"
    amazing(x=1043)

#高兴
image happy11:
    "liluo_common/common/facial/happy_1.png"
    xcenter 640-125 ycenter 150 zoom 0.67 alpha 1.00 subpixel True
    pause 0.4
    "liluo_common/common/facial/happy_2.png"
    xcenter 640-125 ycenter 150 zoom 0.67 alpha 1.00 subpixel True
    pause 0.4
    repeat
    time 2.0
    rush
image happy21:
    "liluo_common/common/facial/happy_1.png"
    xcenter 384-125 ycenter 150 zoom 0.67 alpha 1.00 subpixel True
    pause 0.4
    "liluo_common/common/facial/happy_2.png"
    xcenter 384-125 ycenter 150 zoom 0.67 alpha 1.00 subpixel True
    pause 0.4
    repeat
    time 2.0
    rush
image happy22:
    "liluo_common/common/facial/happy_1.png"
    xcenter 896-125 ycenter 150 zoom 0.67 alpha 1.00 subpixel True
    pause 0.4
    "liluo_common/common/facial/happy_2.png"
    xcenter 896-125 ycenter 150 zoom 0.67 alpha 1.00 subpixel True
    pause 0.4
    repeat
    time 2.0
    rush
image happy31:
    "liluo_common/common/facial/happy_1.png"
    xcenter 237-125 ycenter 150 zoom 0.67 alpha 1.00 subpixel True
    pause 0.4
    "liluo_common/common/facial/happy_2.png"
    xcenter 237-125 ycenter 150 zoom 0.67 alpha 1.00 subpixel True
    pause 0.4
    repeat
    time 2.0
    rush
image happy32:
    "liluo_common/common/facial/happy_1.png"
    xcenter 640-125 ycenter 150 zoom 0.67 alpha 1.00 subpixel True
    pause 0.4
    "liluo_common/common/facial/happy_2.png"
    xcenter 640-125 ycenter 150 zoom 0.67 alpha 1.00 subpixel True
    pause 0.4
    repeat
    time 2.0
    rush
image happy33:
    "liluo_common/common/facial/happy_1.png"
    xcenter 1043-125 ycenter 150 zoom 0.67 alpha 1.00 subpixel True
    pause 0.4
    "liluo_common/common/facial/happy_2.png"
    xcenter 1043-125 ycenter 150 zoom 0.67 alpha 1.00 subpixel True
    pause 0.4
    repeat
    time 2.0
    rush

#愤怒
transform angry(x=640):
    xcenter x+100 ycenter 150 zoom 0.5 alpha 0.00 subpixel True
    parallel:
        dizzy(m=1.6, t=0.2, subpixel=True, k = 1)
    parallel:
        linear 0.25 alpha 1.0
    time 2.0
    linear 0.25 alpha 0.0
image angry11:
    "liluo_common/common/facial/angry.png"
    angry(x=640)
image angry21:
    "liluo_common/common/facial/angry.png"
    angry(x=384)
image angry22:
    "liluo_common/common/facial/angry.png"
    angry(x=896)
image angry31:
    "liluo_common/common/facial/angry.png"
    angry(x=237)
image angry32:
    "liluo_common/common/facial/angry.png"
    angry(x=640)
image angry33:
    "liluo_common/common/facial/angry.png"
    angry(x=1043)


#气
transform steam(x=640):
    xcenter x+50 ycenter 250 zoom 0.6 alpha 0.00 subpixel True
    easein 0.3 xcenter x+250 ycenter 100 alpha 1.00
    easein 1.0
    easein 0.3 alpha 0.00
image steam11:
    "liluo_common/common/facial/steam.png"
    steam(x=640)
image steam21:
    "liluo_common/common/facial/steam.png"
    steam(x=384)
image steam22:
    "liluo_common/common/facial/steam.png"
    steam(x=896)
image steam31:
    "liluo_common/common/facial/steam.png"
    steam(x=237)
image steam32:
    "liluo_common/common/facial/steam.png"
    steam(x=640)
image steam33:
    "liluo_common/common/facial/steam.png"
    steam(x=1043)


#微妙
transform sub(x=640):
    xcenter x ycenter 75 zoom 0.8 alpha 0.00 subpixel True
    parallel:
        linear 0.5 ycenter 150
    parallel:
        linear 0.2 alpha 1.0
        linear 1.0
        linear 0.3 alpha 0.0
image sub11:
    "liluo_common/common/facial/sub.png"
    sub(x=640)
image sub21:
    "liluo_common/common/facial/sub.png"
    sub(x=384)
image sub22:
    "liluo_common/common/facial/sub.png"
    sub(x=896)
image sub31:
    "liluo_common/common/facial/sub.png"
    sub(x=237)
image sub32:
    "liluo_common/common/facial/sub.png"
    sub(x=640)
image sub33:
    "liluo_common/common/facial/sub.png"
    sub(x=1043)


#音乐
transform munote1(x=640):
    xcenter x+100 ycenter 200 zoom 0.35 alpha 0.00 rotate 40 subpixel True
    parallel:
        linear 2.0 rotate -20 xcenter x+300 ycenter 100
    parallel:
        linear 0.5 alpha 1.0
        linear 1.0 alpha 1.0
        linear 0.5 alpha 0.0
transform munote2(x=640):
    xcenter x+125 ycenter 250 zoom 0.37 alpha 0.00 rotate -20 subpixel True
    time 0.8
    parallel:
        linear 2.0 rotate 40 xcenter x+300 ycenter 175
    parallel:
        linear 0.5 alpha 1.0
        linear 1.0 alpha 1.0
        linear 0.5 alpha 0.0
image munote11:
    contains:
        "liluo_common/common/facial/munote.png"
        munote1(x=640)
    contains:
        "liluo_common/common/facial/munote.png"
        munote2(x=640)
image munote21:
    contains:
        "liluo_common/common/facial/munote.png"
        munote1(x=384)
    contains:
        "liluo_common/common/facial/munote.png"
        munote2(x=384)
image munote22:
    contains:
        "liluo_common/common/facial/munote.png"
        munote1(x=896)
    contains:
        "liluo_common/common/facial/munote.png"
        munote2(x=896)
image munote31:
    contains:
        "liluo_common/common/facial/munote.png"
        munote1(x=237)
    contains:
        "liluo_common/common/facial/munote.png"
        munote2(x=237)
image munote32:
    contains:
        "liluo_common/common/facial/munote.png"
        munote1(x=640)
    contains:
        "liluo_common/common/facial/munote.png"
        munote2(x=640)
image munote33:
    contains:
        "liluo_common/common/facial/munote.png"
        munote1(x=1043)
    contains:
        "liluo_common/common/facial/munote.png"
        munote2(x=1043)

transform floweralt(x=640):
    xcenter x ycenter 275 zoom 0.27 alpha 0.00 subpixel True
    parallel:
        linear 0.25 zoom 0.54
    parallel:
        linear 0.25 alpha 1.0
        linear 1.75 alpha 1.0
        linear 0.25 alpha 0.0
image flower11:
    contains:
        "liluo_common/common/facial/flower1.png"
        floweralt(640 - 220)
    contains:
        "liluo_common/common/facial/flower2.png"
        floweralt(640 + 220)
image flower21:
    contains:
        "liluo_common/common/facial/flower1.png"
        floweralt(384 - 220)
    contains:
        "liluo_common/common/facial/flower2.png"
        floweralt(384 + 220)
image flower22:
    contains:
        "liluo_common/common/facial/flower1.png"
        floweralt(896 - 220)
    contains:
        "liluo_common/common/facial/flower2.png"
        floweralt(896 + 220)
image flower31:
    contains:
        "liluo_common/common/facial/flower1.png"
        floweralt(237 - 220)
    contains:
        "liluo_common/common/facial/flower2.png"
        floweralt(237 + 220)
image flower32:
    contains:
        "liluo_common/common/facial/flower1.png"
        floweralt(640 - 220)
    contains:
        "liluo_common/common/facial/flower2.png"
        floweralt(640 + 220)
image flower33:
    contains:
        "liluo_common/common/facial/flower1.png"
        floweralt(1043 - 220)
    contains:
        "liluo_common/common/facial/flower2.png"
        floweralt(1043 + 220)



transform flicker:
    alpha 1.00
    linear 0.2 alpha 0.7
    0.1
    alpha 0.4
    linear 0.1 alpha 0.90
    alpha 0.0
    0.1
    repeat

transform layerflicker:
    alpha 0.1
    linear 0.25 alpha 0.1
    linear 0.25 alpha 0.2
    linear 0.25 alpha 0.1
    linear 0.25 alpha 0.3
    linear 0.25 alpha 0.2
    linear 0.25 alpha 0.4
    linear 0.25 alpha 0.3
    linear 0.25 alpha 0.4
    linear 0.25 alpha 0.2
    repeat

transform shake:
    subpixel True
    parallel:
        xoffset 0
        ease 0.15 xoffset 20
        ease 0.15 xoffset 10
        ease 0.15 xoffset -10
        ease 0.15 xoffset -5
        ease 0.15 xoffset -15
        ease 0.15 xoffset 0
        ease 0.15 xoffset 10
        ease 0.15 xoffset 0
        repeat
    parallel:
        yoffset 0
        ease 0.55 yoffset 10
        ease 1.05 yoffset -10
        easein 0.25 yoffset 0
        repeat

transform dizzy(m=1, t=1.0, subpixel=True, k = 1):
    subpixel subpixel
    parallel:
        xoffset 0
        ease 0.75 * t xoffset 10 * m
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset -5 * m
        ease 0.75 * t xoffset -3 * m
        ease 0.75 * t xoffset -10 * m
        ease 0.75 * t xoffset 0
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset 0
        repeat
    parallel:
        yoffset 0
        ease 1.0 * t yoffset 5 * m * k
        ease 2.0 * t yoffset -5 * m * k
        ease 2.0 * t yoffset 0 * m * k
        ease 2.0 * t yoffset -10 * m * k
        ease 2.0 * t yoffset 2 * m * k
        ease 2.0 * t yoffset 8 * m * k
        easein 1.0 * t yoffset 0
        repeat



###两人 512
###三人 403
transform walks(x):
    subpixel True
    parallel:
        ease 1.6 xcenter x
    parallel:
        ease 0.2 yoffset -20
        ease 0.2 yoffset -0
        repeat
    time 1.6

transform walk21:
    walks(0.3)
transform walk22:
    walks(0.7)
transform walk31:
    walks(0.185)
transform walk32:
    walks(0.5)
transform walk33:
    walks(0.815)
transform walk41:
    walks(0.2)
transform walk42:
    walks(0.4)
transform walk43:
    walks(0.6)
transform walk44:
    walks(0.8)


###
define close_eyes = MultipleTransition([False, Dissolve(0.5), Solid("#000"), Pause(0.25), True])
define open_eyes = MultipleTransition([False, Dissolve(0.5), True])
define push_left = CropMove(2.0, "custom", startcrop=(0.5, 0.0, 0.0, 1.0), endcrop=(0.0, 0.0, 1.0, 1.0))
define clockwise = ImageDissolve("liluo_common/common/transition/clockwise.png", 1.0, 32)
define anticlockwise = ImageDissolve("liluo_common/common/transition/anticlockwise.png", 1.0, 32)
define tran_clockwise = MultipleTransition([False, clockwise ,Solid("#000"), clockwise, True])
define close = ImageDissolve("liluo_common/common/transition/close.png", 0.5, 128, reverse = True)
define tran_close = MultipleTransition([False, close ,Solid("#000"), close ,True])
define tran_water = ImageDissolve("liluo_common/common/transition/watertran.png", 0.5, 64)
define tran_light = ImageDissolve("liluo_common/common/transition/snaketran.png", 0.5, 64)
define tran_fog = ImageDissolve("liluo_common/common/transition/fogtran.png", 0.5, 64)
define tran_fast = ImageDissolve("liluo_common/common/transition/fasttran.png", 0.5, 64)
define tran_updown = ImageDissolve("liluo_common/common/transition/updowntran.png", 0.5, 64)
define tran_uf = ImageDissolve("liluo_common/common/transition/s2.png", 0.2, 32)
define tran_df = ImageDissolve("liluo_common/common/transition/s1.png", 0.2, 32)
define tran_rf = ImageDissolve("liluo_common/common/transition/right.png", 0.2, 32)
define tran_lf = ImageDissolve("liluo_common/common/transition/left.png", 0.2, 32)
define push_up = CropMove(0.4, "custom",startcrop=(0.0, 1.0, 1.0, 1.0), endcrop=(0.0, 0.0, 1.0, 1.0))

define config.window_hide_transition = close
define config.window_show_transition = close
