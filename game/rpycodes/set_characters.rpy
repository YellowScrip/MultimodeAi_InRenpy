#定义角色的名称和各类信息
define who = Character("? ? ?",ctc="ctc",ctc_position = "nestled")
define cq = Character("初咲恋柚" ,who_color = "FF0066",ctc="ctc",ctc_position = "nestled",image="cx")
define ch = Character("我",ctc="ctc",ctc_position = "nestled")
define ma = Character("海川花",ctc="ctc",ctc_position = "nestled")
define xy = Character("西野玥奈",ctc="ctc",ctc_position = "nestled")
define yq = Character("岩崎天桐",ctc="ctc",ctc_position = "nestled",image="yq")
define yqcall = Character("岩崎天桐（电话）",ctc="ctc",ctc_position = "nestled")
define l = Character("蘭",ctc="ctc",ctc_position = "nestled",image="lan")
define jqgb = Character("九衢广播",ctc="ctc",ctc_position = "nestled")
define ym = Character("野猫",ctc="ctc",ctc_position = "nestled")
define mrquan = Character("阿泉先生",ctc="ctc",ctc_position = "nestled")
define libaryanounce = Character("图书馆的广播",ctc="ctc",ctc_position = "nestled")
define mrqiu = Character("秋师傅",ctc="ctc",ctc_position = "nestled")
define sa = Character("同学A",ctc="ctc",ctc_position = "nestled")
define sb = Character("同学B",ctc="ctc",ctc_position = "nestled")
define sc = Character("同学C",ctc="ctc",ctc_position = "nestled")
define wa = Character("围观者A",ctc="ctc",ctc_position = "nestled")
define wb = Character("围观者B",ctc="ctc",ctc_position = "nestled")
define wc = Character("围观者C",ctc="ctc",ctc_position = "nestled")
define wd = Character("围观者D",ctc="ctc",ctc_position = "nestled")
define dy = Character("女店员",ctc="ctc",ctc_position = "nestled")

#设置能够回退对话的最大次数
#define config.hard_rollback_limit = 0

#设置头像，人物转变动画为溶解
#define config.say_attribute_transition = dissolve
define config.say_attribute_transition=Dissolve(0.2)

#设置背景图
image bg1 = "images/background/b1.jpg"
image bg2 = "images/background/bg4.png"
image bg3 = "images/background/none.png"
image bg4 = "images/try_background.png"
image library inside= "images/background/bg3.png"
image consultdesk="images/background/consult_desk.png"
#解包背景
image cloudy="images/background/cloudy.png"
image sky night="images/background/sky night.png"
image street day ="images/background/street day.png"
image street afternoon ="images/background/street afternoon.png"
image street two="images/background/streetTwo.png"
image passage day ="images/background/passage day.png"
image home afternoon="images/background/home afternoon.png"
image memory="images/background/memory.png"
image thinking="images/background/thinking.png"
image livingroom afternoon="images/background/livingroom afternoon.png"
image livingroom night="images/background/livingroom night.png"
image bedroom="images/background/bedroom.png"
image bedroom day="images/background/bedroom day.png"
image door night="images/background/door night.png"
image park afternoon="images/background/park afternoon.png"
image park night="images/background/park night.png"
image light="images/background/light.png"
image cafe="images/background/cafe.png"
image library day="images/background/library out.png"
image store="images/background/store.png"
image airport="images/background/airport.png"
#解包cg
image memory_1="images/cg/memory_1.png"
image cg cx sleep="images/cg/cg cx sleep.png"
#测试用人物立绘
#蘭 
#侧身站立
image lan size1 a1 happy="images/characterstest/lan/size1/sara size1 a1 happy.png"
image lan size1 a1 little_serious="images/characterstest/lan/size1/sara size1 a1 little_serious.png"
image lan size1 a1 normal="images/characterstest/lan/size1/sara size1 a1 normal.png"
image lan size1 a1 proud="images/characterstest/lan/size1/sara size1 a1 proud.png"
image lan size1 a1 serious="images/characterstest/lan/size1/sara size1 a1 serious.png"
image lan size1 a1 smile="images/characterstest/lan/size1/sara size1 a1 smile.png"
image lan size1 a1 wry_smile="images/characterstest/lan/size1/sara size1 a1 wry_smile.png"
#侧身举手
image lan size1 a2 amazing="images/characterstest/lan/size1/sara size1 a2 amazing.png"
image lan size1 a2 little_serious="images/characterstest/lan/size1/sara size1 a2 little_serious.png"
image lan size1 a2 happy="images/characterstest/lan/size1/sara size1 a2 happy.png"
image lan size1 a2 normal="images/characterstest/lan/size1/sara size1 a2 normal.png"
image lan size1 a2 smile="images/characterstest/lan/size1/sara size1 a2 smile.png"
#侧身叉腰
image lan size1 a3 little_serious="images/characterstest/lan/size1/sara size1 a3 little_serious.png"
image lan size1 a3 mad="images/characterstest/lan/size1/sara size1 a3 mad.png"
image lan size1 a3 normal="images/characterstest/lan/size1/sara size1 a3 normal.png"
image lan size1 a3 proud="images/characterstest/lan/size1/sara size1 a3 proud.png"
image lan size1 a3 smile="images/characterstest/lan/size1/sara size1 a3 smile.png"
image lan size1 a3 wry_smile="images/characterstest/lan/size1/sara size1 a3 wry_smile.png"
#站立
image lan size2 a1 little_serious="images/characterstest/lan/size2/sara size2 a1 little_serious.png"
image lan size2 a1 happy="images/characterstest/lan/size2/sara size2 a1 happy.png"
image lan size2 a1 normal="images/characterstest/lan/size2/sara size2 a1 normal.png"
image lan size2 a1 proud="images/characterstest/lan/size2/sara size2 a1 proud.png"
image lan size2 a1 sad="images/characterstest/lan/size2/sara size2 a1 sad.png"
image lan size2 a1 smile="images/characterstest/lan/size2/sara size2 a1 smile.png"
#站立撩发
image lan size2 a2 little_serious="images/characterstest/lan/size2/sara size2 a2 little_serious.png"
image lan size2 a2 happy="images/characterstest/lan/size2/sara size2 a2 happy.png"
image lan size2 a2 normal="images/characterstest/lan/size2/sara size2 a2 normal.png"
image lan size2 a2 proud="images/characterstest/lan/size2/sara size2 a2 proud.png"
image lan size2 a2 sad="images/characterstest/lan/size2/sara size2 a2 sad.png"
image lan size2 a2 smile="images/characterstest/lan/size2/sara size2 a2 smile.png"
image lan size2 a2 wry_smile="images/characterstest/lan/size2/sara size2 a2 wry_smile.png"
#站立思考
image lan size2 a3 little_serious="images/characterstest/lan/size2/sara size2 a3 little_serious.png"
image lan size2 a3 happy="images/characterstest/lan/size2/sara size2 a3 happy.png"
image lan size2 a3 normal="images/characterstest/lan/size2/sara size2 a3 normal.png"
image lan size2 a3 proud="images/characterstest/lan/size2/sara size2 a3 proud.png"
image lan size2 a3 smile="images/characterstest/lan/size2/sara size2 a3 smile.png"
#站立举手
image lan size2 a4 sad="images/characterstest/lan/size2/sara size2 a4 sad.png"
image lan size2 a4 happy="images/characterstest/lan/size2/sara size2 a4 happy.png"
image lan size2 a4 normal="images/characterstest/lan/size2/sara size2 a4 normal.png"
image lan size2 a4 proud="images/characterstest/lan/size2/sara size2 a4 proud.png"
image lan size2 a4 smile="images/characterstest/lan/size2/sara size2 a4 smile.png"


#岩崎
#侧身站立(右向)(校服)
image yq size1 a1 happy="images/characterstest/yq/size1/higasino size1 a1 happy.png"
image yq size1 a1 amazing="images/characterstest/yq/size1/higasino size1 a1 amazing.png"
image yq size1 a1 little_sad="images/characterstest/yq/size1/higasino size1 a1 little_sad.png"
image yq size1 a1 little_serious="images/characterstest/yq/size1/higasino size1 a1 little_serious.png"
image yq size1 a1 proud="images/characterstest/yq/size1/higasino size1 a1 proud.png"
image yq size1 a1 sad="images/characterstest/yq/size1/higasino size1 a1 sad.png"
image yq size1 a1 serious="images/characterstest/yq/size1/higasino size1 a1 serious.png"
image yq size1 a1 smile="images/characterstest/yq/size1/higasino size1 a1 smile.png"
#正面站立（校服）
image yq size3 a1 amazing="images/characterstest/yq/size3/higasino size3 a1 amazing.png"
image yq size3 a1 happy="images/characterstest/yq/size3/higasino size3 a1 happy.png"
image yq size3 a1 little_sad="images/characterstest/yq/size3/higasino size3 a1 little_sad.png"
image yq size3 a1 mad="images/characterstest/yq/size3/higasino size3 a1 mad.png"
image yq size3 a1 normal="images/characterstest/yq/size3/higasino size3 a1 normal.png"
image yq size3 a1 smile="images/characterstest/yq/size3/higasino size3 a1 smile.png"
#背影
image yq size4 a1 leave="images/characterstest/yq/size4/higasino size4 a1 leave.png"


#初咲恋柚
#背手站立
image cx size2 a1 amazing="images/characterstest/cx/size2/shirone size2 a1 amazing.png"
image cx size2 a1 normal="images/characterstest/cx/size2/shirone size2 a1 normal.png"
#站立按胸
image cx size2 a2 normal="images/characterstest/cx/size2/shirone size2 a2 normal.png"
image cx size2 a2 serious="images/characterstest/cx/size2/shirone size2 a2 serious.png"
image cx size2 a2 surprised="images/characterstest/cx/size2/shirone size2 a2 surprised.png"
image cx size2 a2 wry_smile="images/characterstest/cx/size2/shirone size2 a2 wry_smile.png"
#站立
image cx size2 a3 happy="images/characterstest/cx/size2/shirone size2 a3 happy.png"
image cx size2 a3 normal="images/characterstest/cx/size2/shirone size2 a3 normal.png"
image cx size2 a3 smile="images/characterstest/cx/size2/shirone size2 a3 smile.png"
image cx size2 a3 surprised="images/characterstest/cx/size2/shirone size2 a3 surprised.png"
image cx size2 a3 wry_smile="images/characterstest/cx/size2/shirone size2 a3 wry_smile.png"
#单手按胸
image cx size2 a4 amazing="images/characterstest/cx/size2/shirone size2 a4 amazing.png"
image cx size2 a4 little_serious="images/characterstest/cx/size2/shirone size2 a4 little_serious.png"
image cx size2 a4 normal="images/characterstest/cx/size2/shirone size2 a4 normal.png"
image cx size2 a4 sad="images/characterstest/cx/size2/shirone size2 a4 sad.png"
image cx size2 a4 smile="images/characterstest/cx/size2/shirone size2 a4 smile.png"
image cx size2 a4 wry_smile="images/characterstest/cx/size2/shirone size2 a4 wry_smile.png"
#侧向站立
image cx size4 a1 happy="images/characterstest/cx/size4/shirone size4 a1 happy.png"
image cx size4 a1 normal="images/characterstest/cx/size4/shirone size4 a1 normal.png"
image cx size4 a1 smile="images/characterstest/cx/size4/shirone size4 a1 smile.png"
#侧向站立双手按胸
image cx size4 a2 amazing="images/characterstest/cx/size4/shirone size4 a2 amazing.png"
image cx size4 a2 happy="images/characterstest/cx/size4/shirone size4 a2 happy.png"
image cx size4 a2 normal="images/characterstest/cx/size4/shirone size4 a2 normal.png"
image cx size4 a2 smile="images/characterstest/cx/size4/shirone size4 a2 smile.png"
image cx size4 a2 surprised="images/characterstest/cx/size4/shirone size4 a2 surprised.png"




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