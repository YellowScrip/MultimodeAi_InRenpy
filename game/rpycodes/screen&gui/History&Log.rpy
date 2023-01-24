## Log screen ##############################################################
## 自定义历史界面

screen log():

    tag menu

    # 不使用预加载
    predict False

    add im.AlphaMask("gui/ingame/history/history.png", "gui/ingame/history/history.png") at logscreentransition

    frame:
        style "log_frame_style"

        frame:
            style "log_history_window_frame_style"

            vpgrid:
                cols 1
                yinitial 1.0

                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                # 确保整个Frame塞满
                side_yfill True
                side_xfill True

                for h in _history_list:

                    window:
                        background None

                        ## 此语句可确保如果“history_height”为“None”的话仍可正常显示条目。
                        has fixed:
                            yfit True

                        if h.who:

                            label h.who:
                                style "history_name"
                                substitute False

                                ## 若角色颜色已设置，则从“Character”对象中读取颜色到叙述人文本中。
                                if "color" in h.who_args:
                                    text_color h.who_args["color"]

                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            # 直接使用history_text，也可以自定义其他样式
                            style "log_text_style"
                            substitute False

                if not _history_list:
                    label _("尚无对话历史记录。")

        textbutton _("返回"):
            style "return_button"
            action Return()

# log界面主体显示区域样式
style log_frame_style:
    left_padding 265
    right_padding 265

# log界面文本标签区域样式
style log_label_frame_style:
    top_padding 20
    xfill True

# log界面窗口区域样式
style log_history_window_frame_style:
    top_padding 135
    bottom_padding 90
    xfill True

# log文本样式
style log_text_style:
    color "#444444"
    # 根据自己需要修改文本字体，这里用的是汉仪细简黑简
    font "new.ttf"
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

# log界面按钮区域样式
style log_button_frame_style:
    top_padding 690
    xfill True

# 历史界面动画 ##############
transform logscreentransition:
    yoffset 720
    on show:
        linear 1.0 yoffset 0
    on hide:
        linear 1.0 yoffset 720

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }
