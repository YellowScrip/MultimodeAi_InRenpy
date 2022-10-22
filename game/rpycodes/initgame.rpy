#初始化函数：设置字体及其他信息
init:
    $ style.default.font = "new.ttf"
    $ style.default.language = "new.ttf"
    #$ style.default.language = "STKAITI"


init python:
    import pygame
    import webbrowser
    style.default.layout = "greedy"

    #创建一个音乐空间实例
    mr = MusicRoom(fadeout=1.0)
    mr.add("audio/main_menu_bgm_cir_version.mp3",always_unlocked=True)
    mr.add("bgm/pv/Renai_PV.mp3",always_unlocked=True)
    mr.add("bgm/Nervous/omde.mp3",always_unlocked=True)
    mr.add("bgm/Curious everyday.mp3",always_unlocked=True)
    mr.add("bgm/九衢长街/九衢长街新版.mp3",always_unlocked=True)
    mr.add("bgm/烟火大会插曲/Pyrotechnic_convention_and_enthusiasm.mp3",always_unlocked=True)
    mr.add("bgm/饰演与舞台表演/afternoon.mp3",always_unlocked=True)
    mr.add("bgm/和初咲的学习时间/到学习时间勒！.mp3",always_unlocked=True)


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


#设置游戏开场的动画及其他
label splashscreen:
    image beforegame1 = Movie(play="videos/start logo.mpg",loops=0,stop_music=True)
    image beforegame2 = Movie(play="videos/logo.mpeg",loops=0,stop_music=True)
    show beforegame1
    #$ renpy.pause(10.25,hard = True)#时长是你视频的长度，播完自动退出
    hide beforegame1
    show beforegame2
    #$ renpy.pause(6.0,hard = True)#时长是你视频的长度，播完自动退出
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

