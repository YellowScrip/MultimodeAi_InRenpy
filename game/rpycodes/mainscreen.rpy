default show_notice = True
default show_dlc = True

screen notice_and_dlc():
    zorder 990


    if show_notice:

        frame at transform_notice:

            background Solid("#f7f7f777")
            padding(50,40)
            xsize 250
            ysize 400
            align(0.0,.6)
            vbox:
                align(0.0,0.0)
                spacing 10
                text "公告 Notice" style "notice_text" color gui.accent_color font "SourceHanSansCN-Bold.OTF"
                text "—————————————" style "notice_text" size 10
                text "2022年"  style "notice_text" size 15
                text "{b}9月15日{/b} 每年9月第三个星期六，花城都会拉响防空警报，2012年的这天，城内似乎酝酿着危机，一系列影响花城内几位学生命运的故事就此展开……"  style "notice_text" size 15
                text "{b}9月30日{/b} 游戏已发布,全文共约5万字，两个ED，暂定一个结局，好感度会继承到终章使用"  style "notice_text" size 15

    else:
        pass

    fixed at transform_notice(offset_start=-220):
        if show_notice:

            # background None
            xpos 220
            ypos 350
            textbutton _("<") style "music_room" text_size 25 xysize(30,100) action  ToggleVariable("show_notice",True,False),SelectedIf(1==0)
        else:
            xpos 0
            ypos 350
            textbutton _(">") style "music_room" text_size 25 xysize(30,100) action  ToggleVariable("show_notice",True,False),SelectedIf(1==0)



    if show_dlc:

        frame at transform_notice(offset_start=220):

            background Solid("#f7f7f777")
            padding(20,40,20,40)#左上右下
            xsize 250
            ysize 400
            align(1.0,.6)
            vbox:
                align(1.0,0.0)
                text "DLC管理" style "notice_text" color gui.accent_color font "SourceHanSansCN-Bold.OTF"
                text "—————————————" style "notice_text" size 10
            null height(10* gui.pref_spacing)
            vbox:
                align(1.0,.5)
                # style "music_room"
                xoffset 20
                spacing 10
                if os.path.isfile(config.basedir+"//game/c1.bin") or os.path.isfile(config.basedir+"//game/c1.rpa") or os.path.isfile(config.basedir+"//game/c1/c1.rpyc"):
                    textbutton _("海棠醉日 ▷") style "music_room" align(1.0,.5) xysize(200, 50) action Start('dlc_1')
                else:
                    textbutton _("海棠醉日 ▽") style "music_room" align(1.0,.5) xysize(200, 50) action Confirm(_("开发中，再等一小会儿……"),yes=Return(),no=Return(),confirm_selected=False)
                if os.path.isfile(config.basedir+"//game/c2.bin") or os.path.isfile(config.basedir+"//game/c2.rpa") or os.path.isfile(config.basedir+"//game/2/c2.rpyc"):
                    textbutton _("花晨月夕 ▷") style "music_room" align(1.0,.5) xysize(200, 50) action Start('dlc_2')
                else:
                    textbutton _("花晨月夕 ▽") style "music_room" align(1.0,.5) xysize(200, 50) action Confirm(_("开发中，再等一小会儿……"),yes=Return(),no=Return(),confirm_selected=False)
                if os.path.isfile(config.basedir+"//game/c3.bin") or os.path.isfile(config.basedir+"//game/c3.rpa") or os.path.isfile(config.basedir+"//game/c/c3.rpyc"):
                    textbutton _("玉想琼思 ▷") style "music_room" align(1.0,.5) xysize(200, 50) action Start('dlc_3')
                else:
                    textbutton _("玉想琼思 ▽") style "music_room" align(1.0,.5) xysize(200, 50) action Confirm(_("开发中，再等一小会儿……"),yes=Return(),no=Return(),confirm_selected=False)
    else:
        pass

    fixed at transform_notice(offset_start=220):
        if show_dlc:

            # background None
            xpos 1280-250
            ypos 350
            textbutton _(">") style "music_room" text_size 25 xysize(30,100) action  ToggleVariable("show_dlc",True,False),SelectedIf(1==0)
        else:
            xpos 1280-30
            ypos 350
            textbutton _("<") style "music_room" text_size 25 xysize(30,100) action  ToggleVariable("show_dlc",True,False),SelectedIf(1==0)
