#定义角色的名称和各类信息
define who = Character("? ? ?",ctc="ctc",ctc_position = "nestled")
define cq = Character("初咲恋柚" ,who_color = "FF0066",image = "cqly",ctc="ctc",ctc_position = "nestled")
define ch = Character("我",ctc="ctc",ctc_position = "nestled")
define ma = Character("海川花",ctc="ctc",ctc_position = "nestled")
define xy = Character("西野玥奈",ctc="ctc",ctc_position = "nestled")
define yq = Character("岩崎天桐",ctc="ctc",ctc_position = "nestled")
define l = Character("蘭",ctc="ctc",ctc_position = "nestled")
define jqgb = Character("九衢广播",ctc="ctc",ctc_position = "nestled")
define ym = Character("野猫",ctc="ctc",ctc_position = "nestled")

#设置能够回退对话的最大次数
#define config.hard_rollback_limit = 0

#设置头像，人物转变动画为溶解
define config.say_attribute_transition = dissolve

#设置背景图
image bg1 = "images/background/b1.jpg"

#设置角色头像（可以删除）
image side cqly a = "images/characters/cqly_origin/cqly_a4.png" #定义初崎恋柚的头像1，side a
image side cqly b = "images/characters/cqly_origin/cqly_b4.png" #定义初崎恋柚的头像2，side b

image cqly a = "characters/images/cqly_aa1"
image cqly b = "characters/images/cqly_aa1"


#设置背景音乐，效果音及bgm
define m1 = "bgm/Curious everyday.mp3"
define m2 = "bgm/九衢长街/九衢长街新版.mp3"


define config.allow_skipping = False

