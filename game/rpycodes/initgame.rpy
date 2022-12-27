#初始化函数：设置字体及其他信息
init:
    $ style.default.font = "new.ttf"
    $ style.default.language = "new.ttf"
    #$ style.default.language = "STKAITI"



init python:
    import pygame
    import webbrowser
    import collections
    style.default.layout = "greedy"

    if persistent.unlock_1 == None:
        persistent.unlock_1 = False

    if persistent.unlock_2 == None:
        persistent.unlock_2 = False

    if persistent.unlock_3 == None:
        persistent.unlock_3 = False

    if persistent.unlock_4 == None:
        persistent.unlock_4 = False

    if persistent.unlock_0 == None:
        persistent.unlock_0 = False

    buttons = [
        ## 只有一张图的cg
        GalleryButtonEntry(name="dawn", images=["b1",""],
        condition="persistent.unlock_0"),

        ## 多张cg，有转场效果
        GalleryButtonEntry(name="dark", images=["gallery/a",
            "beach1 mary", "beach2", "beach3"], transform=slideawayleft),

        ## 需要unlock_1是true才会解锁
        GalleryButtonEntry(name="end1",
        images=["transfer", "moonpic", "girlpic"],
        condition="persistent.unlock_1"),

        ## 需要unlock_2是true才会解锁
        GalleryButtonEntry(name="end2",
        images=["transfer1", "moonpic", "girlpic"],
        condition="persistent.unlock_2"),

        ## 需要unlock_3是true才会解锁
        GalleryButtonEntry(name="end3",
        images=["transfer", "moonpic", "girlpic"],
        condition="persistent.unlock_3"),

        ## 需要unlock_4是true才会解锁
        GalleryButtonEntry(name="end4",
        images=["transfer", "moonpic", "girlpic"],
        condition="persistent.unlock_4"),

        ## 单一图的cg
        GalleryButtonEntry(name="p1",
        images=["p1"]),

        GalleryButtonEntry(name="p2",
        images=["p2"]),

        GalleryButtonEntry(name="p3",
        images=["p3"]),

        GalleryButtonEntry(name="p4",
        images=["p3"]),

        GalleryButtonEntry(name="p5",
        images=["p3"]),

        GalleryButtonEntry(name="p6",
        images=["p3"]),

        GalleryButtonEntry(name="p7",
        images=["p3"]),

        GalleryButtonEntry(name="p8",
        images=["p3"]),
    ]

    g = Gallery()
    g.locked_button = Composite(
        (GalleryButtonEntry.SLOT_WIDTH,
        GalleryButtonEntry.SLOT_HEIGHT),
        (0, 0), Solid("#000"),
        (125,55), Text("未解锁", size=50, color="#fff"))

    g.button("beach3")
    g.unlock_image("beach3")
    # 用于图像切换使用的转场(transition)。
    g.transition = dissolve

    gh = GalleryHandler(buttons)
    gh.init_gallery(g)



####     创建一个音乐空间实例
    mr = MusicRoom(fadeout=1.0)
    mr.add("audio/main_menu_bgm_cir_version.mp3",always_unlocked=True)
    mr.add("bgm/pv/Renai_PV.mp3",always_unlocked=True)
    mr.add("bgm/Nervous/omde.mp3",always_unlocked=True)
    mr.add("bgm/Curious everyday.mp3",always_unlocked=True)
    mr.add("bgm/九衢长街/九衢长街新版.mp3",always_unlocked=True)
    mr.add("bgm/烟火大会插曲/Pyrotechnic_convention_and_enthusiasm.mp3",always_unlocked=True)
    mr.add("bgm/饰演与舞台表演/afternoon.mp3",always_unlocked=True)
    mr.add("bgm/和初咲的学习时间/到学习时间勒！.mp3",always_unlocked=True)
    mr.add("bgm/pv/renai_piano_ver.mp3",always_unlocked=True)


    class PlayerButton:
        def __init__(self, channel='music', icon_path='gui/button/musicbutton/', mr=mr):
            self.channel = channel
            self.icon_path = icon_path
            self.mr = mr

        def get_icon(self):
            if not renpy.music.is_playing() and not renpy.music.get_pause():
                return self.icon_path + "music_button_07.png"
            if renpy.music.get_pause(self.channel):
                return self.icon_path + "music_button_07.png"
            return self.icon_path + "music_button_04.png"

        def click(self):
            if not renpy.music.is_playing() and not renpy.music.get_pause():
                self.mr.play()
                return
            renpy.music.set_pause(not renpy.music.get_pause(self.channel),
                channel=self.channel)

    play_button = PlayerButton(mr=mr)



####         创建一个Gallery实例


## 定义画廊里按钮的高度和宽度。
define gui.gallery_slot_height = 100
define gui.gallery_slot_width = 200
define gui.gallery_slot_cols = 3
define gui.gallery_slot_rows = 2




#设置游戏开场的动画及其他
label splashscreen:
    image beforegame1 = Movie(play="videos/start logo.mpg",loops=0,stop_music=True)
    image beforegame2 = Movie(play="videos/logo.mpeg",loops=0,stop_music=True)
    image beforegame3 = Movie(play="videos/renpy_logo.mpg",loops=0,stop_music=True)
    show beforegame3
    $ renpy.pause(3.50,hard = True)#时长是你视频的长度，播完自动退出
    hide beforegame3
    show beforegame1
    $ renpy.pause(9.35,hard = True)#时长是你视频的长度，播完自动退出
    hide beforegame1
    show beforegame2
    $ renpy.pause(6.6,hard = True)#时长是你视频的长度，播完自动退出
    hide beforegame2
    #$ renpy.pause(1.5,hard = True)
    return


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

