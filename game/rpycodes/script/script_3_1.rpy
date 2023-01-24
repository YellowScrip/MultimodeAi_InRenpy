
###  episode3上半部分 ################
label episode3_1:
    $ config.allow_skipping = False
    window hide
    image episode1_video3 = Movie(play="videos/episode_video/episode3.mpg",loops=0,stop_music=True)
    show episode1_video3
    $ renpy.pause(4.5,hard = True)#时长是你视频的长度，播完自动退出
    hide episode1_video3
    scene bg2
    play music "bgm/九衢长街/九衢长街新版.mp3"
    $ renpy.pause(1.0,hard = True)#时长是你视频的长度，播完自动退出
    $ config.allow_skipping = True