#定义角色的名称和各类信息
define who = Character("? ? ?",ctc="ctc",ctc_position = "nestled")
define cq = Character("初咲恋柚" ,who_color = "FF0066",image = "cqly",ctc="ctc",ctc_position = "nestled")
define ch = Character("我",ctc="ctc",ctc_position = "nestled")
define ma = Character("海川花",ctc="ctc",ctc_position = "nestled")
define xy = Character("西野玥奈",ctc="ctc",ctc_position = "nestled")
define yq = Character("岩崎天桐",ctc="ctc",ctc_position = "nestled")
define yqcall = Character("岩崎天桐（电话）",ctc="ctc",ctc_position = "nestled")
define l = Character("蘭",ctc="ctc",ctc_position = "nestled")
define jqgb = Character("九衢广播",ctc="ctc",ctc_position = "nestled")
define ym = Character("野猫",ctc="ctc",ctc_position = "nestled")
define mrquan = Character("阿泉先生",ctc="ctc",ctc_position = "nestled")
define libaryanounce = Character("图书馆的广播",ctc="ctc",ctc_position = "nestled")
define mrqiu = Character("秋师傅",ctc="ctc",ctc_position = "nestled")

#设置能够回退对话的最大次数
#define config.hard_rollback_limit = 0

#设置头像，人物转变动画为溶解
define config.say_attribute_transition = dissolve

#设置背景图
image bg1 = "images/background/b1.jpg"
image bg2 = "images/background/bg4.png"
image bg3 = "images/background/none.png"
image bg4 = "images/try_background.png"
image bg5 = "images/background/bg3.png"

#设置角色头像（可以删除）
image side cqly a = "images/characters/cxly/cxly_3" #定义初崎恋柚的头像1，side a
image side cqly b = "images/characters/cxly/cxly_3" #定义初崎恋柚的头像2，side b

image cqly a = "characters/images/cxly/cxly_3"
image cqly b = "characters/images/cxly/cxly_4"


#设置背景音乐，效果音及bgm
define m1 = "bgm/Curious everyday.mp3"
define m2 = "bgm/九衢长街/九衢长街新版.mp3"


#define config.allow_skipping = False

#设置镜头语言
define shot1 = CropMove(5.0, "slideawayright", startcrop=(0.5, 0.5, 0.5, 0.5), startpos=(0.5, 0.5), endcrop=(0.5, 0.5, 0.5, 0.5), endpos=(0.5, 0.5), topnew=True)
#define shot2 = CropMove(time, mode="slideright", startcrop=(0.0, 0.0, 0.0, 1.0), startpos=(0.0, 0.0), endcrop=(0.0, 0.0, 1.0, 1.0), endpos=(0.0, 0.0), topnew=True)
#define shot3 = MoveTransition(10.0, enter="slideawayright", leave="slideawayright", old=False, layers=['master'], time_warp=None, enter_time_warp=None, leave_time_warp=None)
define shot4 = PushMove(50.0,"pushleft")
define shot5 = AlphaDissolve("alpha_control", delay=3.5)
define shot6 = AlphaDissolve("rightmove",delay = 10.0)



image alpha_control:
    "spotlight.png"
    anchor (.5, .5)

    parallel:
        zoom 0
        linear .5 zoom .75
        pause 2
        linear 1.0 zoom 4.0

    parallel:
        xpos 0.0 ypos .6
        linear 1.5 xpos 1.0
        linear 1.0 xpos .5 ypos .2

    pause .5
    repeat

image rightmove:
    "anime1.png"
    anchor (0.5, 0.5)

    parallel:
        zoom 0
        linear 0.5 zoom 0.75
        pause 2
        linear 1.0 zoom 4.0

    parallel:
        xpos 0.0 ypos .6
        linear 0.1 xpos 1.0
        linear 1.0 xpos .5 ypos .2

    pause .5
    repeat