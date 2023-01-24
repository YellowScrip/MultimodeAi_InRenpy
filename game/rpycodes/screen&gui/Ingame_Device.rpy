######  游戏内INGAMEDEVICE界面   ########
screen INGAMEDEVICE():
    add "gui/ingame/DEVICE/overlay/0device.png"
    frame:
        background None
        padding (0, 0, 0, 0)
        imagebutton :
            idle "gui/ingame/DEVICE/overlay/0close.png"
            hover "gui/ingame/DEVICE/overlay/0h_close.png"
            hover_sound"audio/bs.mp3"
            xoffset +835
            yoffset +415
            action Return()

    frame:
        background None
        padding (0, 0, 0, 0)
        imagebutton :
            idle "gui/ingame/DEVICE/overlay/0contacts.png"
            hover_sound"audio/bs.mp3"
            xoffset +593.1
            yoffset +280.5
            action Return()

    frame:
        background None
        padding (0, 0, 0, 0)
        imagebutton :
            idle "gui/ingame/DEVICE/overlay/0certificate.png"
            hover_sound"audio/bs.mp3"
            xoffset +835
            yoffset +155
            action [Hide("INGAMEDEVICE"),ShowMenu("device_credit")]
    frame:
        background None
        padding (0, 0, 0, 0)
        imagebutton :
            idle "gui/ingame/DEVICE/overlay/0map.png"
            hover_sound"audio/bs.mp3"
            xoffset +1076.9
            yoffset +280.5
            action [Hide("INGAMEDEVICE"),ShowMenu("device_map")]

    frame:
        background None
        padding (0, 0, 0, 0)
        imagebutton :
            idle "gui/ingame/DEVICE/overlay/0dictionary.png"
            hover_sound"audio/bs.mp3"
            xoffset +593.1
            yoffset +549.5
            action [Hide("INGAMEDEVICE"),ShowMenu("device_dictionary")]

    frame:
        background None
        padding (0, 0, 0, 0)
        imagebutton :
            idle "gui/ingame/DEVICE/overlay/0game.png"
            hover_sound"audio/bs.mp3"
            xoffset +835
            yoffset +675
            action Return()

    frame:
        background None
        padding (0, 0, 0, 0)
        imagebutton :
            idle "gui/ingame/DEVICE/overlay/0reading.png"
            hover_sound"audio/bs.mp3"
            xoffset +1076.9
            yoffset +549.5
            action Return()


#######  查看凭证 ###############
screen device_credit():
    add "gui/ingame/DEVICE/overlay/0device.png"

    frame:
        background None
        padding (0, 0, 0, 0)
        imagebutton :
            idle "gui/ingame/DEVICE/overlay/credit.png"
            xoffset +200
            yoffset +165
            action NullAction()
    frame:
        background None
        padding (0, 0, 0, 0)
        imagebutton :
            idle "gui/ingame/DEVICE/overlay/uh_close.png"
            hover "gui/ingame/DEVICE/overlay/h_close.png"
            hover_sound"audio/bs.mp3"
            xoffset +1700
            yoffset +120
            action Return()

    frame:
        background None
        padding (0, 0, 0, 0)
        imagebutton :
            idle "gui/ingame/DEVICE/overlay/uh_return.png"
            hover "gui/ingame/DEVICE/overlay/h_return.png"
            hover_sound"audio/bs.mp3"
            xoffset +1640
            yoffset +120
            action [Hide("device_credit"),ShowMenu("INGAMEDEVICE")]

#######  地图 ###############
screen device_map():
    add "gui/ingame/DEVICE/overlay/devicemap.png"
    frame:
        background None
        padding (0, 0, 0, 0)
        imagebutton :
            idle "gui/ingame/DEVICE/overlay/uh_close.png"
            hover "gui/ingame/DEVICE/overlay/h_close.png"
            hover_sound"audio/bs.mp3"
            xoffset +1700
            yoffset +120
            action Return()

    frame:
        background None
        padding (0, 0, 0, 0)
        imagebutton :
            idle "gui/ingame/DEVICE/overlay/uh_return.png"
            hover "gui/ingame/DEVICE/overlay/h_return.png"
            hover_sound"audio/bs.mp3"
            xoffset +1640
            yoffset +120
            action [Hide("device_map"),ShowMenu("INGAMEDEVICE")]


#######  辞典 ###############
init python:
    config.hyperlink_handlers["play"] = renpy.play

screen device_dictionary():
    add "gui/ingame/DEVICE/overlay/0device.png"
    text "字典" size 100 xalign 0.5 ypos 200
    hbox spacing 500:
        viewport:
            xpos 250 ypos 300 xsize 300 ysize 600
            child_size (None, 4000)
            scrollbars "vertical"
            spacing 5
            draggable True
            mousewheel True
            arrowkeys True
            add "#000c"
            vbox spacing 20:
                for word in sorted(persistent.palabra, key=str.lower) :
                    textbutton word:
                        action SetVariable("display_desc", word)
        vbox ypos 400 xsize 850 ysize 500 box_wrap True:
            text glossary_dict.get(display_desc, "")

    frame:
        background None
        padding (0, 0, 0, 0)
        imagebutton :
            idle "gui/ingame/DEVICE/overlay/uh_close.png"
            hover "gui/ingame/DEVICE/overlay/h_close.png"
            hover_sound"audio/bs.mp3"
            xoffset +1700
            yoffset +120
            action Return()

    frame:
        background None
        padding (0, 0, 0, 0)
        imagebutton :
            idle "gui/ingame/DEVICE/overlay/uh_return.png"
            hover "gui/ingame/DEVICE/overlay/h_return.png"
            hover_sound"audio/bs.mp3"
            xoffset +1640
            yoffset +120
            action [Hide("device_dictionary"),ShowMenu("INGAMEDEVICE")]


define persistent.palabra= set()

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
    font "new.ttf"