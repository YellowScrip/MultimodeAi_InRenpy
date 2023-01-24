## Navigation screen ###########################################################

screen navigation():
    add "gui/main_menu.png"
    add "gui/ingame/setmenu/background.png" xalign 0.5 yalign 0.69
    add "gui/ingame/setmenu/System.png" xalign 0.05 yalign 0.0
    default navigation_key = "a"
    if navigation_key == "a":
        use display_set
    imagebutton:
        idle "gui/ingame/setmenu/uh_reset.png"
        hover "gui/ingame/setmenu/h_reset.png"
        xoffset +1380
        yoffset +960
        action MainMenu()

    imagebutton:
        idle "gui/ingame/setmenu/uh_backtitle.png"
        hover "gui/ingame/setmenu/h_backtitle.png"
        xoffset +1500
        yoffset +960
        if main_menu:
            action [Hide("display_set"),Hide("program_set"),Hide("text_set"),Hide("sound_set"),Hide("dialog_set"),Hide("shortcut_set"),Hide("shortcut_set_keyboard"),Hide("shortcut_set_mouse"),Hide("navigation",fade)]
        else:
            action MainMenu()
#         if _in_replay:
#             action [MainMenu(),Play("music", "bgm/pv/renai_piano.mp3")]
#         elif not main_menu:
#             action [ShowMenu("main_menu"),Play("music", "bgm/pv/renai_piano.mp3")]

    imagebutton:
        idle "gui/ingame/setmenu/uh_backgame.png"
        hover "gui/ingame/setmenu/h_backgame.png"
        xoffset +1620
        yoffset +960
        action Return()

    imagebutton:
        idle "gui/ingame/setmenu/uh_exit.png"
        hover "gui/ingame/setmenu/h_exit.png"
        xoffset +1740
        yoffset +960
        action Quit(confirm = True)

    hbox:
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton :
                idle "gui/ingame/setmenu/uh_displaysettings.png"
                hover "gui/ingame/setmenu/h_displaysettings.png"
                xoffset +650
                yoffset +0
                action [ShowMenu("display_set"),Hide("program_set"),Hide("text_set"),Hide("sound_set"),Hide("dialog_set"),Hide("shortcut_set"),Hide("shortcut_set_keyboard"),Hide("shortcut_set_mouse"),SetScreenVariable("navigation_key","a")]
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/uh_programsettings.png"
                hover "gui/ingame/setmenu/h_programsettings.png"
                xoffset +660
                yoffset +0
                action [Hide("display_set"),ShowMenu("program_set"),Hide("text_set"),Hide("sound_set"),Hide("dialog_set"),Hide("shortcut_set"),Hide("shortcut_set_keyboard"),Hide("shortcut_set_mouse"),SetScreenVariable("navigation_key","b")]
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/uh_textsettings.png"
                hover "gui/ingame/setmenu/h_textsettings.png"
                xoffset +670
                yoffset +0
                action [Hide("display_set"),Hide("program_set"),ShowMenu("text_set"),Hide("sound_set"),Hide("dialog_set"),Hide("shortcut_set"),Hide("shortcut_set_keyboard"),Hide("shortcut_set_mouse"),SetScreenVariable("navigation_key","b")]
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/uh_soundsettings.png"
                hover "gui/ingame/setmenu/h_soundsettings.png"
                xoffset +680
                yoffset +0
                action [Hide("display_set"),Hide("program_set"),Hide("text_set"),ShowMenu("sound_set"),Hide("dialog_set"),Hide("shortcut_set"),Hide("shortcut_set_keyboard"),Hide("shortcut_set_mouse"),SetScreenVariable("navigation_key","b")]
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/uh_dialogsettings.png"
                hover "gui/ingame/setmenu/h_dialogsettings.png"
                xoffset +690
                yoffset +0
                action [Hide("display_set"),Hide("program_set"),Hide("text_set"),Hide("sound_set"),ShowMenu("dialog_set"),Hide("shortcut_set"),Hide("shortcut_set_keyboard"),Hide("shortcut_set_mouse"),SetScreenVariable("navigation_key","b")]
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/uh_shortcutlist.png"
                hover "gui/ingame/setmenu/h_shortcutlist.png"
                xoffset +700
                yoffset +0
                action [Hide("display_set"),Hide("program_set"),Hide("text_set"),Hide("sound_set"),Hide("dialog_set"),ShowMenu("shortcut_set"),ShowMenu("shortcut_set_keyboard"),SetScreenVariable("navigation_key","b")]

default button1 = True
default button2_1 = True
default button2_2 = True
default button3 = True
default button4 = True
default button5 = True
default button6 = True
screen display_set():
    hbox:
        frame:
            background None
            padding(0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/display/显示模式.png"
                xoffset +100
                yoffset +200
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/display/显示曲名.png"
                xoffset -670
                yoffset +400
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/display/视觉特效.png"
                xoffset -1440
                yoffset +600
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/display/屏幕大小.png"
                xoffset -2210
                yoffset +800
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/display/播放语音.png"
                xoffset -2060
                yoffset +200
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/display/收藏语音.png"
                xoffset -2830
                yoffset +400
                action NullAction()

########### 显示模式 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button1:
                    idle "gui/ingame/setmenu/display/h_window.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_window.png"
                hover "gui/ingame/setmenu/display/h_window.png"
                xoffset -4100
                yoffset +270
                if button1 == False:
                    action [Preference("display", "window"),ToggleVariable("button1",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button1:
                    idle "gui/ingame/setmenu/display/uh_fullscreen.png"
                else:
                    idle "gui/ingame/setmenu/display/h_fullscreen.png"
                hover "gui/ingame/setmenu/display/h_fullscreen.png"
                xoffset -4570
                yoffset +270
                if button1 == True:
                    action [Preference("display", "fullscreen"),ToggleVariable("button1",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 播放语音 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button5 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -3580
                yoffset +270
                if button5 == True:
                    action [Preference("display", "window"),ToggleVariable("button5",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button5 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -4050
                yoffset +270
                if button5 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button5",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 收藏语音 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button6 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -3980
                yoffset +470
                if button6 == True:
                    action [Preference("display", "window"),ToggleVariable("button6",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button6 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -4450
                yoffset +470
                if button6 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button6",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 显示曲名 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button3 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -5300
                yoffset +470
                if button3 == True:
                    action [Preference("display", "window"),ToggleVariable("button3",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button3 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -5770
                yoffset +470
                if button3 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button6",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 视觉特效 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button4 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -5700
                yoffset +670
                if button4 == True:
                    action [Preference("display", "window"),ToggleVariable("button4",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button4 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -6170
                yoffset +670
                if button4 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button4",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 屏幕大小 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if (button2_1 and button2_2 == False):
                    idle "gui/ingame/setmenu/display/h_1600.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_1600.png"
                hover "gui/ingame/setmenu/display/h_1600.png"
                xoffset -6000
                yoffset +870
                if (button2_1 == True and button2_2 == False):
                    action NullAction()
                elif (button2_1 == True and button2_2 == True):
                    action [Preference("display", 0.833),ToggleVariable("button2_2",True,False),SelectedIf(1==0)]
                elif (button2_1 == False and button2_2 == True):
                    action [Preference("display", 0.833),ToggleVariable("button2_2",True,False),SelectedIf(1==0),ToggleVariable("button2_1",True,False),SelectedIf(1==0)]
                elif (button2_1 == False and button2_2 == False):
                    action [Preference("display", 0.833),ToggleVariable("button2_1",True,False),SelectedIf(1==0)]
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if (button2_1 == False and button2_2):
                    idle "gui/ingame/setmenu/display/h_1280.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_1280.png"
                hover "gui/ingame/setmenu/display/h_1280.png"
                xoffset -6420
                yoffset +870
                if (button2_1 == False and button2_2 == True):
                    action NullAction()
                elif (button2_1 == True and button2_2 == True):
                    action [Preference("display", 0.667),ToggleVariable("button2_1",True,False),SelectedIf(1==0)]
                elif (button2_1 == True and button2_2 == False):
                    action [Preference("display", 0.667),ToggleVariable("button2_2",True,False),SelectedIf(1==0),ToggleVariable("button2_1",True,False),SelectedIf(1==0)]
                elif (button2_1 == False and button2_2 == False):
                    action [Preference("display", 0.667),ToggleVariable("button2_2",True,False),SelectedIf(1==0)]
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if (button2_1 == False  and button2_2 == False):
                    idle "gui/ingame/setmenu/display/h_1024.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_1024.png"
                hover "gui/ingame/setmenu/display/h_1024.png"
                xoffset -6840
                yoffset +870
                if (button2_1 == False and button2_2 == False):
                    action NullAction()
                elif (button2_1 == False and button2_2 == True):
                    action [Preference("display", 0.533),ToggleVariable("button2_2",True,False),SelectedIf(1==0)]
                elif (button2_1 == True and button2_2 == True):
                    action [Preference("display", 0.533),ToggleVariable("button2_2",True,False),SelectedIf(1==0),ToggleVariable("button2_1",True,False),SelectedIf(1==0)]
                elif (button2_1 == True and button2_2 == False):
                    action [Preference("display", 0.533),ToggleVariable("button2_1",True,False),SelectedIf(1==0)]

default button7 = True
default button8 = True
default button9 = True
default button10 = True
default button11 = True
screen program_set():
    hbox:
        frame:
            background None
            padding(0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/program/光标自动移动.png"
                xoffset +100
                yoffset +200
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/program/光标移动位置.png"
                xoffset -670
                yoffset +400
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/program/自动隐藏光标.png"
                xoffset -1440
                yoffset +600
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/program/游戏速度.png"
                xoffset -2210
                yoffset +800
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/program/剧场模式.png"
                xoffset -2060
                yoffset +200
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/program/任务栏预览.png"
                xoffset -2830
                yoffset +400
                action NullAction()

########### 光标自动移动 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button7 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -4100
                yoffset +270
                if button7 == True:
                    action [Preference("display", "window"),ToggleVariable("button7",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button7 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -4570
                yoffset +270
                if button7 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button7",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
########### 剧场模式 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button8 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -3580
                yoffset +270
                if button8 == True:
                    action [Preference("display", "window"),ToggleVariable("button8",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button8 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -4050
                yoffset +270
                if button8 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button8",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 任务栏预览 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button9 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -3980
                yoffset +470
                if button9 == True:
                    action [Preference("display", "window"),ToggleVariable("button9",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button9 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -4450
                yoffset +470
                if button9 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button9",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 光标移动位置 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button10 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -5300
                yoffset +470
                if button10 == True:
                    action [Preference("display", "window"),ToggleVariable("button10",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button10 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -5770
                yoffset +470
                if button10 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button10",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 自动隐藏光标 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button11 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -5700
                yoffset +670
                if button11 == True:
                    action [Preference("display", "window"),ToggleVariable("button11",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button11 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -6170
                yoffset +670
                if button11 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button11",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 游戏速度 ##################
        frame:
            xoffset -6390
            yoffset +870
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
#                     label _("Text Speed")
                    bar value Preference("text speed")



default button12 = True
default button13 = True
default button14 = True
default button15 = True
default button16 = True

screen text_set():
    hbox:
        frame:
            background None
            padding(0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/text/自动模式.png"
                xoffset +100
                yoffset +200
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/text/回滚设置.png"
                xoffset -670
                yoffset +400
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/text/按住ctrl快进.png"
                xoffset -1440
                yoffset +600
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/text/文本速度.png"
                xoffset -2210
                yoffset +800
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/text/选项过后是否继续跳过.png"
                xoffset -2060
                yoffset +200
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/text/选项过后是否继续自动模式.png"
                xoffset -2830
                yoffset +400
                action NullAction()

########### 自动模式 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button12 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -4100
                yoffset +270
                if button12 == True:
                    action [Preference("display", "window"),ToggleVariable("button12",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button12 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -4570
                yoffset +270
                if button12 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button12",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
########### 选项过后是否继续跳过 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button13 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -3580
                yoffset +270
                if button13 == True:
                    action [Preference("display", "window"),ToggleVariable("button13",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button13 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -4050
                yoffset +270
                if button13 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button13",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 选项过后是否继续自动模式 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button14 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -3980
                yoffset +470
                if button14 == True:
                    action [Preference("display", "window"),ToggleVariable("button14",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button14 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -4450
                yoffset +470
                if button14 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button14",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 回滚设置 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button15 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -5300
                yoffset +470
                if button15 == True:
                    action [Preference("display", "window"),ToggleVariable("button15",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button15 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -5770
                yoffset +470
                if button15 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button15",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 按住ctrl快进 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button16 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -5700
                yoffset +670
                if button16 == True:
                    action [Preference("display", "window"),ToggleVariable("button16",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button16 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -6170
                yoffset +670
                if button16 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button16",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 文本速度 ##################
        frame:
            xoffset -6390
            yoffset +870
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
#                     label _("Text Speed")
                    bar value Preference("text speed")

########### 自动推进时间 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/text/自动推进时间.png"
                xoffset -6285
                yoffset +600
                action NullAction()
        frame:
            xoffset -6925
            yoffset +670
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    bar value Preference("auto-forward time")


default button17 = True

screen sound_set():
    hbox:
        frame:
            background None
            padding(0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/sound/语音中断.png"
                xoffset +100
                yoffset +200
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/sound/背景音量.png"
                xoffset -670
                yoffset +400
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/sound/语音音量.png"
                xoffset -1440
                yoffset +600
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/sound/特效音量.png"
                xoffset -2210
                yoffset +800
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/sound/系统声音.png"
                xoffset -2060
                yoffset +200
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/sound/角色声音设置.png"
                xoffset -2830
                yoffset +400
                action NullAction()

########### 语音中断 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button17 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -4100
                yoffset +270
                if button17 == True:
                    action [Preference("display", "window"),ToggleVariable("button17",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button17 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -4570
                yoffset +270
                if button17 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button17",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 背景音量 ##################
        frame:
            xoffset -4790
            yoffset +470
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    bar value Preference("music volume")

########### 语音音量 ##################
        frame:
            xoffset -5478
            yoffset +670
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    bar value Preference("voice volume")

########### 特效音量 ##################
        frame:
            xoffset -6164
            yoffset +870
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    bar value Preference("sound volume")

########### 系统声音 ##################
        frame:
            xoffset -5935
            yoffset +270
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    bar value Preference("text speed")

default button18 = True
default button19 = True
default button20 = True
default button21 = True
default button22 = True
default button23 = True
default button24 = True
default button25 = True

screen dialog_set():
    hbox:
        frame:
            background None
            padding(0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/dialog/退出游戏时进行确认.png"
                xoffset +100
                yoffset +200
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/dialog/返回标题画面时进行确认.png"
                xoffset -670
                yoffset +400
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/dialog/读取存档时进行确认.png"
                xoffset -1440
                yoffset +600
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/dialog/覆盖存档时确认.png"
                xoffset -2210
                yoffset +800
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/dialog/快速保存时进行确认.png"
                xoffset -2060
                yoffset +200
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/dialog/快速读取时进行确认.png"
                xoffset -2830
                yoffset +400
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/dialog/删除存档时进行确认.png"
                xoffset -3600
                yoffset +600
                action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                idle "gui/ingame/setmenu/dialog/恢复系统默认时进行确认.png"
                xoffset -4370
                yoffset +800
                action NullAction()

########### 退出游戏时进行确认 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button18 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -5640
                yoffset +270
                if button18 == True:
                    action [Preference("display", "window"),ToggleVariable("button18",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button18 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -6110
                yoffset +270
                if button18 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button18",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 快速保存时进行确认 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button19 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -5120
                yoffset +270
                if button19 == True:
                    action [Preference("display", "window"),ToggleVariable("button19",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button19 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -5590
                yoffset +270
                if button19 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button19",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 快速保读取时进行确认 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button20 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -5520
                yoffset +470
                if button20 == True:
                    action [Preference("display", "window"),ToggleVariable("button20",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button20 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -5990
                yoffset +470
                if button20 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button20",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 返回标题画面时进行确认 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button21 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -6840
                yoffset +470
                if button21 == True:
                    action [Preference("display", "window"),ToggleVariable("button21",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button21 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -7310
                yoffset +470
                if button21 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button21",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 读取存档时进行确认 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button22 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -7240
                yoffset +670
                if button22 == True:
                    action [Preference("display", "window"),ToggleVariable("button22",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button22 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -7710
                yoffset +670
                if button22 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button22",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 删除存档时进行确认 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button23 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -6720
                yoffset +670
                if button23 == True:
                    action [Preference("display", "window"),ToggleVariable("button23",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button23 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -7190
                yoffset +670
                if button23 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button23",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 恢复系统默认时进行确认 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button24 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -7120
                yoffset +870
                if button24 == True:
                    action [Preference("display", "window"),ToggleVariable("button24",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button24 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -7590
                yoffset +870
                if button24 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button24",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()

########### 覆盖存档时进行确认 ##################
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button25 == False:
                    idle "gui/ingame/setmenu/display/h_close.png"
                else:
                    idle "gui/ingame/setmenu/display/uh_close.png"
                hover "gui/ingame/setmenu/display/h_close.png"
                xoffset -8440
                yoffset +870
                if button25 == True:
                    action [Preference("display", "window"),ToggleVariable("button25",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton:
                if button25 == False:
                    idle "gui/ingame/setmenu/display/uh_open.png"
                else:
                    idle "gui/ingame/setmenu/display/h_open.png"
                hover "gui/ingame/setmenu/display/h_open.png"
                xoffset -8910
                yoffset +870
                if button25 == False:
                    action [Preference("display", "fullscreen"),ToggleVariable("button25",True,False),SelectedIf(1==0)]
                else:
                    action NullAction()


screen shortcut_set():
    vbox:
        spacing 15
        hbox:
            textbutton _("键盘"):
                xoffset + 1700 yoffset +150
                action [Hide("shortcut_set_mouse"),ShowMenu("shortcut_set_keyboard")]
            textbutton _("鼠标"):
                xoffset + 1720 yoffset +150
                action [Hide("shortcut_set_keyboard"),ShowMenu("shortcut_set_mouse")]

screen shortcut_set_keyboard():
    add "gui/ingame/setmenu/keyboard.png" xalign 0.5 yalign 0.5
screen shortcut_set_mouse():
    add "gui/ingame/setmenu/mouse.png" xalign 0.5 yalign 0.5


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

