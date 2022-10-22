
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
