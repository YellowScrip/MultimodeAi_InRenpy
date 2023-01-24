#######  添加词语注解 ###############
init -1 python:
    display_desc = ""
    def play(tag, argument, contents):
        renpy.play(argument)
        return contents
    config.custom_text_tags["play"] = play
    config.hyperlink_handlers["play"] = renpy.play

    glossary_dict = \
        {
        '黄金时代' :'{play=audio/bs.mp3}黄金时代指的是至暗时代之后，科技空前进步，无比伟大而光明的时代。{/play}',
        '东沃国立高大':'{play=audio/bs.mp3}坐落于东京的一所大学{/play}'
        }