#初始化函数：设置字体及其他信息
init:
    $ style.default.font = "STKAITI.TTF"
    $ style.default.language = "STKAITI"


init python:
    import pygame
    style.default.layout = "greedy"

#设置游戏开场的动画及其他
label splashscreen:
    image beforegame1 = Movie(play="videos/start logo.mpg",loops=0,stop_music=True)
    image beforegame2 = Movie(play="videos/logo.mpeg",loops=0,stop_music=True)
    show beforegame1
    $ renpy.pause(10.25,hard = True)#时长是你视频的长度，播完自动退出
    hide beforegame1
    show beforegame2
    $ renpy.pause(6.0,hard = True)#时长是你视频的长度，播完自动退出
    return


# 定义ctc：采用序列帧动画的方式
image ctc:
    "images/ctc/knife/刀00.png"
    pause 0.04
    "images/ctc/knife/刀01.png"
    pause 0.04
    "images/ctc/knife/刀02.png"
    pause 0.04
    "images/ctc/knife/刀03.png"
    pause 0.04
    "images/ctc/knife/刀04.png"
    pause 0.04
    "images/ctc/knife/刀05.png"
    pause 0.04
    "images/ctc/knife/刀06.png"
    pause 0.04
    "images/ctc/knife/刀07.png"
    pause 0.04
    "images/ctc/knife/刀08.png"
    pause 0.04
    "images/ctc/knife/刀09.png"
    pause 0.04
    "images/ctc/knife/刀10.png"
    pause 0.04
    "images/ctc/knife/刀11.png"
    pause 0.04
    "images/ctc/knife/刀12.png"
    pause 0.04
    "images/ctc/knife/刀13.png"
    pause 0.04
    "images/ctc/knife/刀14.png"
    pause 0.04
    "images/ctc/knife/刀15.png"
    pause 0.04
    "images/ctc/knife/刀16.png"
    pause 0.04
    "images/ctc/knife/刀17.png"
    pause 0.04
    "images/ctc/knife/刀18.png"
    pause 0.04
    "images/ctc/knife/刀19.png"
    pause 0.04
    "images/ctc/knife/刀20.png"
    pause 0.04
    "images/ctc/knife/刀21.png"
    pause 0.04
    "images/ctc/knife/刀22.png"
    pause 0.04
    "images/ctc/knife/刀23.png"
    pause 0.04
    "images/ctc/knife/刀24.png"
    pause 0.04
    repeat


#定义角色的名称和各类信息
define who = Character("? ? ?")
define cq = Character("初崎恋柚" ,who_color = "FF0066",image = "cqly",ctc="ctc",ctc_position = "nestled")
define ch = Character("我")
define ma = Character("海川莉那")
define sz = Character("西野玥奈")
define yq = Character("岩崎天桐")


#设置能够回退对话的最大次数
define config.hard_rollback_limit = 0

#设置头像，人物转变动画为溶解
define config.say_attribute_transition = dissolve


#设置角色头像（可以删除）
image side cqly a = "images/characters/cqly_origin/cqly_a4.png" #定义初崎恋柚的头像1，side a
image side cqly b = "images/characters/cqly_origin/cqly_b4.png" #定义初崎恋柚的头像2，side b

image cqly a = "characters/images/cqly_aa1"
image cqly b = "characters/images/cqly_aa1"


#设置背景音乐，效果音及bgm
define m1 = "bgm/Curious everyday.mp3"


#设置角色声音
define v1 = "voice/cqvoice/v1.wav"


#其他要求如下
#1960*1080 pixel 图片要求


#游戏结束后返回界面的函数，必须存在
label before_main_menu:
    $ main_menu = True
    call screen main_menu()
    return


#实现开幕黑屏及延时时间
screen stop_screen(t):  #开幕黑频转场实现

    zorder 999 ## 确保在其它 界面(screen)上面。

    add "#000"

    button action NullAction()

    key "mouseup_3" action NullAction()

    timer t action Hide('stop_screen', fade)


#游戏内容
label start:
    show screen stop_screen(0.5) with dissolve #开始时黑幕转场
    play music m1
    scene b1
    show cqly_aa1 with fade
    play sound "voice/cqvoice/v1.wav"
    cq a "2025年的3月21日......"
    play sound "voice/cqvoice/v2.wav"
    cq b "我返回了这个从来没见过的，"
    play sound "voice/cqvoice/v3.wav"
    cq "名为故土的地方。"
    play sound "voice/cqvoice/v4.wav"
    cq "无论是从现在开始亦或者是曾经与我有关的一切一切，"
    play sound "voice/cqvoice/v5.wav"
    cq "突然在这一刻闪过。"
    play sound "voice/cqvoice/v6.wav"
    cq "转瞬即逝间，什么都溜走了。"
    hide cqly_aa1 with dissolve
    ch """
    就如同天空上漂浮的这一片片樱花花瓣一样

    终会在路人的眼里，仅仅留下几秒钟飘落的印象

    然后便被碾成了尘土......

    我试图使自己忘掉来到这里之前的所有记忆，

    但我始终忘不掉，

    还是像眼前团簇的樱花一样，

    稍纵即逝，

    但. . .

    无比美丽. . .
    """

    #show b2(这里是转场——海川渡的家里)
    who "欢迎回家，海川君。"
    menu:
        "我到底应该怎么做？"
        "好好反思一下自己在干些什么":
            $x=1
            $mood=5
        "开始展望新的生活":
            $x=2
            $mood=20
        "回忆":
            $x=3
            $mood=0
    "所以最后的结果是..."
    if(x==1):
        "你选择1"
        jump choose1_1
    elif(x==2):
        "你选择2"
        jump choose1_2
    elif(x==3):
        "你选择3"
        show cq11 at left with fade
        ch "我试图使自己忘掉来到这里之前的所有记忆"
        jump choose1_3

label choose1_1:
    ch "是这样的阿"
    return
label choose1_2:
    return
label choose1_3:
    return
label quit:
    play sound "voice/stovvoice/ov.wav"
    pause 2.1
    return
