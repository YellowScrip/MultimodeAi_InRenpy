init python:
    config.overlay_screens.append("exp1")
    config.overlay_screens.append("exp2")

#########    解释一的代码      ##############
default exp_1 = False
screen exp1():
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" pos (600,700)
    if exp_1:
        textbutton (_("科技")):
            xalign 0.376
            yalign 0.84
            action NullAction()
            tooltip "{glitch=2.0}{color=fff}{b}注释:{/b}\n这个世界的科技，已经达到了超高水平{/color}{/glitch}"

#########    解释二的代码      ##############
default exp_2 = False
screen exp2():
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]" pos (600,700)
    if exp_2:
        textbutton (_("黄金时代")):
            xalign 0.224
            yalign 0.843
            action NullAction()
            tooltip "{glitch=2.0}{color=fff}{b}注释:{/b}\n指世界在历经经济衰退的几十年后，科技飞速发展的一个时代{/color}{/glitch}"