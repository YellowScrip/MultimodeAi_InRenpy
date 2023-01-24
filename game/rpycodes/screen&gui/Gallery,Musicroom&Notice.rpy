## Gallery & Music Room screen (extra screen)(画廊和音乐室/鉴赏)   #############################

default StartPause0 = True
default StartPause1 = False
default StartPause2 = False
default StartPause3 = False
default StartPause4 = False
default StartPause5 = False
default StartPause6 = False
default StartPause7= False
default StartPause8 = False
default StartPause9 = False
default t = 1

#
image Renai致此刻的你:
    contains:
        Text("REnai致此刻的你", style = "main_menu_button_text_shadow")
    contains:
        Text("REnai致此刻的你", style = "main_menu_button_text_fill")

image 我们之间的爱恋化作少女来谋杀我:
    contains:
        Text("我们之间的爱恋化作少女来谋杀我", style = "main_menu_button_text_shadow")
    contains:
        Text("我们之间的爱恋化作少女来谋杀我", style = "main_menu_button_text_fill")

image 窒息时分:
    contains:
        Text("窒息时分", style = "main_menu_button_text_shadow")
    contains:
        Text("窒息时分", style = "main_menu_button_text_fill")

image Curious everyday:
    contains:
        Text("Curious EveryDay", style = "main_menu_button_text_shadow")
    contains:
        Text("Curious EveryDay", style = "main_menu_button_text_fill")

image 九衢长街:
    contains:
        Text("九衢长街", style = "main_menu_button_text_shadow")
    contains:
        Text("九衢长街", style = "main_menu_button_text_fill")

image 烟花绚烂时:
    contains:
        Text("烟花绚烂时", style = "main_menu_button_text_shadow")
    contains:
        Text("烟花绚烂时", style = "main_menu_button_text_fill")

image 下午，演出，与你:
    contains:
        Text("下午，演出，与你", style = "main_menu_button_text_shadow")
    contains:
        Text("下午，演出，与你", style = "main_menu_button_text_fill")

image 到学习时间了！:
    contains:
        Text("到学习时间了！", style = "main_menu_button_text_shadow")
    contains:
        Text("到学习时间了！", style = "main_menu_button_text_fill")
image Renai_piano_ver:
    contains:
        Text("Renai_piano_ver", style = "main_menu_button_text_shadow")
    contains:
        Text("Renai_piano_ver", style = "main_menu_button_text_fill")

image load_game_button_text:
    contains:
        Text("", style = "main_menu_button_text_shadow")
    contains:
        Text("", style = "main_menu_button_text_fill")

image preference_button_text:
    contains:
        Text("", style = "main_menu_button_text_shadow")
    contains:
        Text("", style = "main_menu_button_text_fill")

image about_button_text:
    contains:
        Text("", style = "main_menu_button_text_shadow")
    contains:
        Text("", style = "main_menu_button_text_fill")

image help_button_text:
    contains:
        Text("", style = "main_menu_button_text_shadow")
    contains:
        Text("", style = "main_menu_button_text_fill")

image quit_button_text:
    contains:
        Text("", style = "main_menu_button_text_shadow")
    contains:
        Text("", style = "main_menu_button_text_fill")

screen extra_musicroom():
    zorder 999
    modal True
    add gui.main_menu_background
    add "gui/musicroom_menu(1).png" xalign 0.4 yalign 0.95
    add "gui/musicroom_logo.png" xalign 0.0351 yalign 0.02
    add "gui/分割条纹.png" xalign 0.33 yalign 0.18
    add "cd" xalign 1.0 yalign 1.0


###   第一首歌曲   #################################
    fixed:
        if StartPause1:
            imagebutton:
                idle "gui/musicroom_button2.png"
                foreground "Renai致此刻的你"
                xalign 0.3 yalign 0.30
                if StartPause0 :
                    action[PauseAudio("music"),SetScreenVariable("StartPause0",False),ToggleVariable("StartPause1",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[PauseAudio("music"),ToggleVariable("StartPause1",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
        else:
            textbutton "Renai致此刻的你":
                xalign 0.3 yalign 0.30
                if StartPause0 :
                    action[mr.Play("audio/main_menu_bgm_cir_version.mp3"),ToggleVariable("StartPause1",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[mr.Play("audio/main_menu_bgm_cir_version.mp3"),SetScreenVariable("StartPause0",True),ToggleVariable("StartPause1",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]

###   第二首歌曲   #################################
    fixed:
        if StartPause2:
            imagebutton :
                idle "gui/musicroom_button2.png"
                foreground "我们之间的爱恋化作少女来谋杀我"
                xalign 0.3 yalign 0.35
                if StartPause0 :
                    action[PauseAudio("music"),SetScreenVariable("StartPause0",False),ToggleVariable("StartPause2",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[PauseAudio("music"),ToggleVariable("StartPause2",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
        else:
            textbutton "我们之间的爱恋化作少女来谋杀我":
                xalign 0.3 yalign 0.35
                if StartPause0 :
                    action[mr.Play("bgm/pv/Renai_PV.mp3"),ToggleVariable("StartPause2",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[mr.Play("bgm/pv/Renai_PV.mp3"),SetScreenVariable("StartPause0",True),ToggleVariable("StartPause2",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]

###   第三首歌曲   #################################
    fixed:
        if StartPause3:
            imagebutton :
                idle "gui/musicroom_button2.png"
                foreground "窒息时分"
                xalign 0.3 yalign 0.40
                if StartPause0 :
                    action[PauseAudio("music"),SetScreenVariable("StartPause0",False),ToggleVariable("StartPause3",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[PauseAudio("music"),ToggleVariable("StartPause3",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
        else:
            textbutton "窒息时分":
                xalign 0.3 yalign 0.40
                if StartPause0 :
                    action[mr.Play("bgm/Nervous/omde.mp3"),ToggleVariable("StartPause3",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[mr.Play("bgm/Nervous/omde.mp3"),SetScreenVariable("StartPause0",True),ToggleVariable("StartPause3",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]

###   第四首歌曲   #################################
    fixed:
        if StartPause4:
            imagebutton :
                idle "gui/musicroom_button2.png"
                foreground "Curious everyday"
                xalign 0.3 yalign 0.45
                if StartPause0 :
                    action[PauseAudio("music"),SetScreenVariable("StartPause0",False),ToggleVariable("StartPause4",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[PauseAudio("music"),ToggleVariable("StartPause4",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
        else:
            textbutton "Curious everyday":
                xalign 0.3 yalign 0.45
                if StartPause0 :
                    action[mr.Play("bgm/Curious everyday.mp3"),ToggleVariable("StartPause4",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[mr.Play("bgm/Curious everyday.mp3"),SetScreenVariable("StartPause0",True),ToggleVariable("StartPause4",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]

###   第五首歌曲   #################################
    fixed:
        if StartPause5:
            imagebutton :
                idle "gui/musicroom_button2.png"
                foreground "九衢长街"
                xalign 0.3 yalign 0.50
                if StartPause0 :
                    action[PauseAudio("music"),SetScreenVariable("StartPause0",False),ToggleVariable("StartPause5",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[PauseAudio("music"),ToggleVariable("StartPause5",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
        else:
            textbutton "九衢长街":
                xalign 0.3 yalign 0.50
                if StartPause0 :
                    action[mr.Play("bgm/九衢长街/九衢长街新版.mp3"),ToggleVariable("StartPause5",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[mr.Play("bgm/九衢长街/九衢长街新版.mp3"),SetScreenVariable("StartPause0",True),ToggleVariable("StartPause5",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]

##   第六首歌曲   #################################
    fixed:
        if StartPause6:
            imagebutton :
                idle "gui/musicroom_button2.png"
                foreground "烟花绚烂时"
                xalign 0.3 yalign 0.55
                if StartPause0 :
                    action[PauseAudio("music"),SetScreenVariable("StartPause0",False),ToggleVariable("StartPause6",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[PauseAudio("music"),ToggleVariable("StartPause6",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
        else:
            textbutton "烟花绚烂时":
                xalign 0.3 yalign 0.55
                if StartPause0 :
                    action[mr.Play("bgm/烟火大会插曲/Pyrotechnic_convention_and_enthusiasm.mp3"),ToggleVariable("StartPause6",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[mr.Play("bgm/烟火大会插曲/Pyrotechnic_convention_and_enthusiasm.mp3"),SetScreenVariable("StartPause0",True),ToggleVariable("StartPause6",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]

##   第七首歌曲   #################################
    fixed:
        if StartPause7:
            imagebutton :
                idle "gui/musicroom_button2.png"
                foreground "下午，演出，与你"
                xalign 0.3 yalign 0.60
                if StartPause0 :
                    action[PauseAudio("music"),SetScreenVariable("StartPause0",False),ToggleVariable("StartPause7",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[PauseAudio("music"),ToggleVariable("StartPause7",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
        else:
            textbutton "下午，演出，与你":
                xalign 0.3 yalign 0.60
                if StartPause0 :
                    action[mr.Play("bgm/饰演与舞台表演/afternoon.mp3"),ToggleVariable("StartPause7",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[mr.Play("bgm/饰演与舞台表演/afternoon.mp3"),SetScreenVariable("StartPause0",True),ToggleVariable("StartPause7",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]

##   第八首歌曲   #################################
    fixed:
        if StartPause8:
            imagebutton :
                idle "gui/musicroom_button2.png"
                foreground "到学习时间了！"
                xalign 0.3 yalign 0.65
                if StartPause0 :
                    action[PauseAudio("music"),SetScreenVariable("StartPause0",False),ToggleVariable("StartPause8",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[PauseAudio("music"),ToggleVariable("StartPause8",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
        else:
            textbutton "到学习时间了！":
                xalign 0.3 yalign 0.65
                if StartPause0 :
                    action[mr.Play("bgm/和初咲的学习时间/到学习时间勒！.mp3"),ToggleVariable("StartPause8",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[mr.Play("bgm/和初咲的学习时间/到学习时间勒！.mp3"),SetScreenVariable("StartPause0",True),ToggleVariable("StartPause8",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]

##   第九首歌曲   #################################
    fixed:
        if StartPause9:
            imagebutton :
                idle "gui/musicroom_button2.png"
                foreground "Renai_piano_ver"
                xalign 0.3 yalign 0.70
                if StartPause0 :
                    action[PauseAudio("music"),SetScreenVariable("StartPause0",False),ToggleVariable("StartPause9",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[PauseAudio("music"),ToggleVariable("StartPause9",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
        else:
            textbutton "Renai_piano_ver":
                xalign 0.3 yalign 0.70
                if StartPause0 :
                    action[mr.Play("bgm/pv/renai_piano_ver.mp3"),ToggleVariable("StartPause9",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]
                else:
                    action[mr.Play("bgm/pv/renai_piano_ver.mp3"),SetScreenVariable("StartPause0",True),ToggleVariable("StartPause9",True,False),SelectedIf(1==0),ToggleVariable("StartPause0",True,False),SelectedIf(1==0)]

#    暂停按钮,在暂停时的按钮分类   ######################
#         if StartPause0:
#             imagebutton:
#                 idle "gui/button/musicbutton/music_button_04.png"
#                 hover "gui/button/musicbutton/music_button_04.png"
#                 hover_sound"audio/bs.mp3"
#                 xalign 0.25
#                 yalign 1.0
#                 action [PauseAudio("music"),SetScreenVariable("StartPause0",False)]
#         ###   开始按钮，在开始时的按钮分类   ########
#         else:
#             imagebutton:
#                 idle "gui/button/musicbutton/music_button_07.png"
#                 hover "gui/button/musicbutton/music_button_07.png"
#                 #foreground "new_game_button_text"
#                 #at main_menu_button_hover
#                 hover_sound"audio/bs.mp3"
#                 xalign 0.25
#                 yalign 1.0
#                 action [mr.Play(),SetScreenVariable("StartPause0",True)]


    vbox:
        #返回按钮
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton :
                idle "gui/backbutton2.png"
                hover "gui/backbutton2.png"
                #foreground "new_game_button_text"
                #at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset +1700
                yoffset +100
                action [Hide("extra_musicroom"),Play("music", "bgm/pv/renai_piano.mp3")]
            at main_menu_button_in(0.2)

        #切换gallery按钮
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton :
                idle "gui/gallery.png"
                hover "gui/gallery.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset +1150
                yoffset -30
                action [ShowMenu("extra_gallery"),Hide("extra_musicroom")]
            at main_menu_button_in(0.0)

        #停留musicroom按钮
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton :
                idle "gui/musicroom.png"
                hover "gui/musicroom.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset +500
                yoffset -182
                action [Hide("extra_musicroom"),ShowMenu("extra_musicroom")]
            at main_menu_button_in(0.0)







#### gallery 网格    ################
screen gallery_slots(buttons):
    # 按钮网格(grid)。
    grid gui.gallery_slot_cols gui.gallery_slot_rows:
        align (0.5, 0.5)
        xysize (1600, 1200)
        xspacing 30
        yspacing 30

        for b in buttons:
            frame:
                foreground Frame("gui/idle.png")
                xysize (GalleryButtonEntry.SLOT_WIDTH, GalleryButtonEntry.SLOT_HEIGHT)

                # 调用make_button显示具体的按钮。
                add g.make_button(name=b.name, unlocked=b.thumbnail,
                    xalign=0.5, yalign=0.5)

        ## 如果格子不满，需要补上空白
        for i in range(gh.SLOT_PER_PAGE - len(buttons)):
            null



###### gallery  主体screen   ################
screen extra_gallery():
    zorder 999
    modal True
    add gui.main_menu_background
    add "gui/gallery_logo.png" xalign 0.04 yalign 0.02
    add "gui/分割条纹.png" xalign 0.72 yalign 0.18

    use gallery_slots(gh.get())

    ## 翻页逻辑
    hbox:
        xalign 0.5 yalign 0.8
        frame:
            textbutton _("上一页"):
                sensitive gh.index > 0
                action SetField(gh, 'index', gh.index-1)

        for i in range(gh.get_total_pages()):
            frame:
                textbutton str(i):
                    action SetField(gh, 'index', i)

        frame:
            textbutton _("下一页"):
                sensitive gh.index < gh.get_total_pages()-1
                action SetField(gh, 'index', gh.index+1)



    vbox:
         #返回按钮
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton :
                idle "gui/backbutton2.png"
                hover "gui/backbutton2.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset +1700
                yoffset +100
                action [Hide(),Play("music", "bgm/pv/renai_piano.mp3")]
            at main_menu_button_in(0.2)

        #停留gallery按钮
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton :
                idle "gui/gallery.png"
                hover "gui/gallery.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset +1150
                yoffset -30
                action [Hide("extra_gallery"),ShowMenu("extra_gallery")]
            at main_menu_button_in(0.0)

        #切换musicroom按钮
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton :
                idle "gui/musicroom.png"
                hover "gui/musicroom.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset +500
                yoffset -182
                action [ShowMenu("extra_musicroom"),Hide("extra_gallery")]
            at main_menu_button_in(0.0)

## Notice screen(公告屏幕 1.0)     ###########################################################

screen notice1():
    zorder 999
    modal True
    add gui.main_menu_background
    add "gui/Notice.png" xalign 0.02 yalign 0.02
    add "gui/投票1.png" xalign 0.5 yalign 0.5
    vbox:
         #返回按钮
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton :
                idle "gui/backbutton2.png"
                hover "gui/backbutton2.png"
                #foreground "new_game_button_text"
                #at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset +1700
                yoffset +100
                action Hide()
            at main_menu_button_in(0.2)

        #左箭头显示
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton :
                xalign 0.0
                yalign 0.5
                idle "gui/leftarrow1.png"
                hover "gui/leftarrow1.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset +20
                yoffset +480
                action [ShowMenu("notice2"),Hide("notice1")]
            at main_menu_button_in(0.0)

        #右箭头显示
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton :
                xalign 1.0
                yalign 0.5
                idle "gui/rightarrow1.png"
                hover "gui/rightarrow1.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset +1800
                yoffset +380
                action [ShowMenu("notice3"),Hide("notice1")]
            at main_menu_button_in(0.0)


screen notice2():
    zorder 999
    modal True
    #main_menu True
    add gui.main_menu_background
    add "gui/Notice.png" xalign 0.02 yalign 0.02
    add "gui/mouse.png" xalign 0.5 yalign 0.5
    vbox:
         #返回按钮
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton :
                idle "gui/backbutton2.png"
                hover "gui/backbutton2.png"
                #foreground "new_game_button_text"
                #at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset +1700
                yoffset +100
                action Hide()
            at main_menu_button_in(1.0)

        #左箭头显示
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton :
                xalign 0.0
                yalign 0.5
                idle "gui/leftarrow1.png"
                hover "gui/leftarrow1.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset +20
                yoffset +480
                action [ShowMenu("notice3"),Hide("notice2")]
            at main_menu_button_in(0.0)

        #右箭头显示
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton :
                xalign 1.0
                yalign 0.5
                idle "gui/rightarrow1.png"
                hover "gui/rightarrow1.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset +1800
                yoffset +380
                action [ShowMenu("notice1"),Hide("notice2")]
            at main_menu_button_in(0.0)


screen notice3():
    zorder 999
    modal True
    #main_menu True
    add gui.main_menu_background
    add "gui/Notice.png" xalign 0.02 yalign 0.02
    add "gui/window_icon.png" xalign 0.5 yalign 0.5
    vbox:
         #返回按钮
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton :
                idle "gui/backbutton2.png"
                hover "gui/backbutton2.png"
                #foreground "new_game_button_text"
                #at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset +1700
                yoffset +100
                action Hide()
            at main_menu_button_in(1.0)

        #左箭头显示
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton :
                xalign 0.0
                yalign 0.5
                idle "gui/leftarrow1.png"
                hover "gui/leftarrow1.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset +20
                yoffset +480
                action [ShowMenu("notice1"),Hide("notice3")]
            at main_menu_button_in(0.0)

        #右箭头显示
        frame:
            background None
            padding (0, 0, 0, 0)
            imagebutton :
                xalign 1.0
                yalign 0.5
                idle "gui/rightarrow1.png"
                hover "gui/rightarrow1.png"
                #foreground "new_game_button_text"
                at main_menu_button_hover
                hover_sound"audio/bs.mp3"
                xoffset +1800
                yoffset +380
                action [ShowMenu("notice2"),Hide("notice3")]
            at main_menu_button_in(0.0)
