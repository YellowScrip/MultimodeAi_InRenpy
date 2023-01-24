################################################################################
## Initialization
################################################################################

init offset = -1

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

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


init python:
    config.character_id_prefixes.append('namebox')


## Input screen ################################################################

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

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


define config.narrator_menu = True





## Preferences screen ##########################################################
screen preferences():

    tag menu
    add "gui/main_menu.png"
    vbox:
        hbox:
            box_wrap True

            if renpy.variant("pc") or renpy.variant("web"):

                vbox:
                    style_prefix "radio"
                    label _("显示")
                    textbutton _("窗口") action Preference("display", "window")
                    textbutton _("全屏") action Preference("display", "fullscreen")

            vbox:
                style_prefix "radio"
                label _("回退操作区")
                textbutton _("禁用") action Preference("rollback side", "disable")
                textbutton _("屏幕左侧") action Preference("rollback side", "left")
                textbutton _("屏幕右侧") action Preference("rollback side", "right")

            vbox:
                style_prefix "check"
                label _("快进")
                textbutton _("未读文本") action Preference("skip", "toggle")
                textbutton _("选项后继续") action Preference("after choices", "toggle")
                textbutton _("忽略转场") action InvertSelected(Preference("transitions", "toggle"))

        null height (4 * gui.pref_spacing)

        hbox:
            style_prefix "slider"
            box_wrap True

            vbox:

                label _("文本速度")

                bar value Preference("text speed")

                label _("自动播放间隔时间")

                bar value Preference("auto-forward time")

            vbox:

                if config.has_music:
                    label _("音乐音量")

                    hbox:
                        bar value Preference("music volume")

                if config.has_sound:

                    label _("音效音量")

                    hbox:
                        bar value Preference("sound volume")

                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)

                if config.has_voice:
                    label _("语音音量")

                    hbox:
                        bar value Preference("voice volume")

                        if config.sample_voice:
                            textbutton _("Test") action Play("voice", config.sample_voice)

                if config.has_music or config.has_sound or config.has_voice:
                    null height gui.pref_spacing

                    textbutton _("全部静音"):
                        action Preference("all mute", "toggle")
                        style "mute_all_button"


## Confirm screen ##############################################################

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
                spacing 50

                imagebutton:
                    idle "gui/button/renew_button/yes_button.png"
                    hover "gui/button/renew_button/yes_button_h.png"
                    action yes_action

                imagebutton:
                    idle "gui/button/renew_button/no_button.png"
                    hover "gui/button/renew_button/no_button_h.png"
                    action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action

#### 确认淡出效果  ##############
transform screenfadeinout(st = 0.5):
    alpha 0.0
    on show:
        linear st alpha 1.0
    on hide:
        linear st alpha 0.0


## Skip indicator screen #######################################################

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


## Notify screen ###############################################################

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


## NVL screen ##################################################################


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

define config.nvl_list_length = gui.nvl_list_length