## Main Menu screen ############################################################

# 入参delay用作不同按钮的动画间隔时间，缓动函数选用了结尾平滑的quint
transform main_menu_button_in(delay):
    # 图片宽度273，所以默认偏移量稍微多两个像素
    xoffset 275
    yoffset -50
    on start:
        time delay
        easein_quint 2.0 xoffset 0
transform main_menu_button_hover:
        on hover:
            ease 0.5 xoffset -35
        on idle:
            ease 0.5 xoffset 0

screen main_menu():

    tag menu
    add gui.main_menu_background
    add "gui/logo4.png" xalign 0.90 yalign 0.15
    add "gui/copyright1.png" xalign 0.0 yalign 0.0

    #拉动弹出框按钮
    vbox:
        xalign 1.0
        yalign 0.3
        #公告跳转按钮
        frame:
            background None
            padding (0, 0, 0, 0)
            #$ choose_box = 1
            imagebutton:
                idle "gui/arrow1.png"
                hover "gui/arrow1.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                #action ShowMenu("notice1")
                action Show("notice1")
            at main_menu_button_in(0.0)

    vbox:
        xalign 0.5
        yalign 1.0

        #github url跳转按钮
        frame:
            # 无背景
            background None
            # 不扩展
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/github1.png"
                hover "gui/github1.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset 1000
                yoffset -300
                action OpenURL("https://github.com/YellowScrip")
            at main_menu_button_in(0.0)

        #b站url跳转按钮
        frame:
            # 无背景
            background None
            # 不扩展
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/bilibili1.png"
                hover "gui/bilibili1.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset 920
                yoffset -355
                action OpenURL("https://space.bilibili.com/318948275")
            at main_menu_button_in(0.0)

        #微博url跳转按钮
        frame:
            # 无背景
            background None
            # 不扩展
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/weibo1.png"
                hover "gui/weibo1.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset 840
                yoffset -425
                action OpenURL("https://weibo.com/u/7796171151")
            at main_menu_button_in(0.0)

        #制作组官网url跳转按钮
        frame:
            # 无背景
            background None
            # 不扩展
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ptfod1.png"
                hover "gui/ptfod1.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset 775
                yoffset -490
                action OpenURL("www.ptfod.com")
            at main_menu_button_in(0.0)

        frame:
            # 无背景
            background None
            # 不扩展
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/button/按钮输出/START.png"
                hover "gui/button/按钮输出/START02.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset 600
                yoffset -200
                action Start()
            at main_menu_button_in(0.3)

        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/button/按钮输出/LOAD.png"
                hover "gui/button/按钮输出/LOAD02.png"
                foreground "load_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset 600
                yoffset -175
                action ShowMenu("load")
            at main_menu_button_in(0.6)

        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/button/按钮输出/CONFIG.png"
                hover "gui/button/按钮输出/CONFIG 02.png"
                foreground "load_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset 600
                yoffset -150
                action ShowMenu("navigation")
            at main_menu_button_in(0.9)

        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/button/按钮输出/EXTRA.png"
                hover "gui/button/按钮输出/EXTRA02.png"
                foreground "about_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset 600
                yoffset -125
                action ShowMenu("extra_musicroom")
            at main_menu_button_in(1.2)

        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/button/按钮输出/CONTINUE.png"
                hover "gui/button/按钮输出/CONTINUE02.png"
                foreground "help_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset 600
                yoffset -100
                action ShowMenu("help")
            at main_menu_button_in(1.5)
        if renpy.variant("pc"):

            ## “退出”按钮在 iOS 上被禁止设置，在安卓和网页上也不是必需的。
            frame:
                background None
                padding (0, 0, 0, 0)
                imagebutton:
                    idle "gui/button/按钮输出/EXIT.png"
                    hover "gui/button/按钮输出/EXIT02.png"
                    foreground "quit_button_text"
                    at main_menu_button_hover
                    hover_sound"audio/bs.mp3"
                    xoffset 600
                    yoffset -75
                    action Quit(confirm=not main_menu)
                at main_menu_button_in(1.8)
