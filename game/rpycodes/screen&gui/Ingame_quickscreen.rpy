## Quick Menu screen ###########################################################
screen quick_menu():
    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0

            frame:
                background None
                padding (0, 0, 0, 0)
                imagebutton :
                    idle "gui/ingame/uh_load.png"
                    hover "gui/ingame/h_load.png"
                    hover_sound"audio/bs.mp3"
                    xoffset +750
                    yoffset +92
                    action ShowMenu("load")

            frame:
                background None
                padding (0, 0, 0, 0)
                imagebutton :
                    idle "gui/ingame/uh_save.png"
                    hover "gui/ingame/h_save.png"
                    hover_sound"audio/bs.mp3"
                    xoffset +760
                    yoffset +92
                    action ShowMenu('save')

            frame:
                background None
                padding (0, 0, 0, 0)
                imagebutton :
                    idle "gui/ingame/uh_qload.png"
                    hover "gui/ingame/h_qload.png"
                    hover_sound"audio/bs.mp3"
                    xoffset +770
                    yoffset +92
                    action QuickLoad()

            frame:
                background None
                padding (0, 0, 0, 0)
                imagebutton :
                    idle "gui/ingame/uh_qsave.png"
                    hover "gui/ingame/h_qsave.png"
                    hover_sound"audio/bs.mp3"
                    xoffset +780
                    yoffset +92
                    action QuickSave()

            frame:
                background None
                padding (0, 0, 0, 0)
                imagebutton :
                    idle "gui/ingame/uh_auto.png"
                    hover "gui/ingame/h_auto.png"
                    hover_sound"audio/bs.mp3"
                    xoffset +790
                    yoffset +95
                    action Preference("auto-forward", "toggle")

            frame:
                background None
                padding (0, 0, 0, 0)
                imagebutton :
                    idle "gui/ingame/uh_skip.png"
                    hover "gui/ingame/h_skip.png"
                    hover_sound"audio/bs.mp3"
                    xoffset +800
                    yoffset +92
                    action Skip() alternate Skip(fast=True, confirm=True)

            frame:
                background None
                padding (0, 0, 0, 0)
                imagebutton :
                    idle "gui/ingame/uh_voice.png"
                    hover "gui/ingame/h_voice.png"
                    hover_sound"audio/bs.mp3"
                    xoffset +810
                    yoffset +92
                    action VoiceReplay()

            frame:
                background None
                padding (0, 0, 0, 0)
                imagebutton :
                    idle "gui/ingame/uh_like.png"
                    hover "gui/ingame/h_like.png"
                    hover_sound"audio/bs.mp3"
                    xoffset +820
                    yoffset +92
                    action VoiceReplay()

            frame:
                background None
                padding (0, 0, 0, 0)
                imagebutton :
                    idle "gui/ingame/uh_camera.png"
                    hover "gui/ingame/h_camera.png"
                    hover_sound"audio/bs.mp3"
                    xoffset +830
                    yoffset +92
                    action Screenshot()

            frame:
                background None
                padding (0, 0, 0, 0)
                imagebutton :
                    idle "gui/ingame/uh_history.png"
                    hover "gui/ingame/h_history.png"
                    hover_sound"audio/bs.mp3"
                    xoffset +840
                    yoffset +92
                    action ShowMenu('log')

            frame:
                background None
                padding (0, 0, 0, 0)
                imagebutton :
                    idle "gui/ingame/uh_back.png"
                    hover "gui/ingame/h_back.png"
                    hover_sound"audio/bs.mp3"
                    xoffset +850
                    yoffset +92
                    action MainMenu()

            frame:
                background None
                padding (0, 0, 0, 0)
                imagebutton :
                    idle "gui/ingame/uh_setting.png"
                    hover "gui/ingame/h_setting.png"
                    hover_sound"audio/bs.mp3"
                    xoffset +860
                    yoffset +92
                    action ShowMenu("navigation")

            frame:
                background None
                padding (0, 0, 0, 0)
                imagebutton :
                    idle "ingame_device"
                    xoffset -1050
                    yoffset -0
                    action ShowMenu("INGAMEDEVICE")



init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True