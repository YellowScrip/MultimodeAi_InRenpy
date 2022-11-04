################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)




################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("返回") action Rollback()
            textbutton _("历史对话") action ShowMenu('history')
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动播放") action Preference("auto-forward", "toggle")
            textbutton _("存档") action ShowMenu('save')
            textbutton _("快速存档") action QuickSave()
            textbutton _("快速读档") action QuickLoad()
            textbutton _("菜单") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:

        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("开始演出") action Start()

        else:

            textbutton _("历史演出") action ShowMenu("history")

            textbutton _("保存演出") action ShowMenu("save")

        textbutton _("半场演出") action ShowMenu("load")

        textbutton _("演出偏好") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("演出概况") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("帮助") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("退出演出") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")



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



## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

transform main_menu_button_hover:
        on hover:
            ease 0.5 xoffset -35
        on idle:
            ease 0.5 xoffset 0

screen main_menu():

    ## This ensures that any other menu screen is replaced.
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
                action ShowMenu("preferences")
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



# 文字本体样式
style main_menu_button_text_fill:
    align (0.5, 0.5)
    size 30
    font "new.ttf"
    color "#fedaaa"
    outlines [(1, "#fab5a4", 0, 0)]

# 文字投影样式
style main_menu_button_text_shadow:
    align (0.5, 0.5)
    size 30
    font "new.ttf"
    color "#c0c0c0"
    outlines [(2, "#c0c0c0", 3, 3)]
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
# 入参delay用作不同按钮的动画间隔时间，缓动函数选用了结尾平滑的quint
transform main_menu_button_in(delay):
    # 图片宽度273，所以默认偏移量稍微多两个像素
    xoffset 275
    yoffset -50
    on start:
        time delay
        easein_quint 2.0 xoffset 0

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("演出概况"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0


################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("确定") action yes_action
                textbutton _("取消") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)





        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
