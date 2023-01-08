
###  episode2下半部分 ################
label episode2_2:

    cq size2 a3 normal"这是我第一次真正在舞台上表演. . .那个. . ."
    cq size2 a3 wry_smile"看起来怎么样？"
    xy size2 a2 smile"这演技至少在我认识的同学中绝对算是很不错的了"
    xy size2 a2 smile2"初咲学妹看上去很有干劲的样子呢"  #（此时微笑）
    "这家伙. . .竟然是第一次正式上台演出，完全看不出来. . ."
    "就算是最新的仿生机器人，在学习“如何表演”这件事上，应该也要花上不少的学习时间吧"
    xy size2 a2 smile"海川同学刚刚也表现得很不错"
    xy "可以看得出来你是有一些基础的"
    ch "之前在中国的时候参加过几次演出. . .不过也有将近一年的时间没有登上舞台正式表演过了"
    xy size2 a2 normal"原来是这样. . ."
    xy "刚才的‘吐槽’的做法很聪明"
    xy "用‘吐槽’来增加演出的诙谐感这个做法很不错"
    xy size2 a2 smile"只不过在时机上呢…"  #（这时的表情是微笑脸）
    ch ". . . . . ."
    "虽然这句话说得十分委婉，在其中我还是听出了西野学姐的部分不满情绪"
    "实际上，我自己也知道刚才的试演中水平真的不够. . ."
    "和之前高中时候能够在舞台上自如表演的我完全不在一个等级上了"
    "是和初咲相处太久了的缘故嘛. . ."
    "总是不自觉地就会开始吐槽了"
    ch "但我也没有说几句台词啊. . ."
    ch "真的会有人注意到我吗…"
    xy size2 a2 normal"你这么说就不对了"
    xy "并不是说台词多的角色就是大家的焦点哦"
    xy "也有不少‘人狠话不多’的经典角色吧"
    xy "那他们成为经典是因为台词吗？"
    ch "好像确实是这样子呢…"
    xy "对吧"
    "虽然刚刚的我完全被初咲恋柚突入其来的扮演所深深震撼"
    "但我也确实有点投入刚刚的演出. . .不如说是初咲的表演让我感受到即兴演出的真切"
    xy "那么，两位准备好试演下一个情景了吗？"
    ch "诶？还要继续即兴试演吗？这个已经够了吧. . ."
    cq size2 a3 smile"太天真了，主人看来是完全没有常识的吧？"
    cq "即兴演出一般是有很多场，分为不同的表演内容。"
    cq "这样更能体现出演出者的能力和心理素质哦！"
    xy size2 a2 smile"没错"  #（此时微笑）
    ch "我明白了"
    xy size2 a2 happy"那么请海川来扮演‘凯旋的骑士’，初咲是‘骑士的追随者’，开始吧！"
    "随着西野玥奈的手一挥动，在我们面前的舞台上的投影光束再次发生了和刚刚一样的变化"
    hide xy size2 a2 happy
    hide cx size2 a3 smile
    with Dissolve(0.2)
    hide hall with pixellate
    show village with pixellate
    #（场景转换：从刚才的模拟教室场景转到现在的小乡村场景？（这个地方不一定是要小村庄，剧本审核可以好好考量一下，争取提出具有更好演出效果的场景需求））
    $renpy.pause(1.0,hard= False)
    show cx size2 a3 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    "在设备投影光的变换下，我和初咲很快就置身于一个看上去非常古朴的小镇，在初咲的周围围着不少像是村民一样的角色"
    "在做了一次深呼吸后，初咲很快就进入了状态. . .这次是用非常崇拜我的眼神看着我. . ."
    "我也要快一点进入状态才行. . ." 
    cq size2 a3 happy"骑士大人！"
    cq "是您打败了魔王，给我们带来了和平吗？"
    "初咲十指相扣，将她小小的手举到了胸口前，摆出一副祈祷的样姿势"
    "这样的姿势. . .怎么给我这么熟悉的感觉. . ."
    ch "是的"
    ch "守护这片大地，就是我的职责！"
    cq size2 a3 smile"我可以永远追随着主人，做您最忠实的仆人吗？"
    ch "当然没问题了. . .嗯？"
    ch "不应该是. . .‘骑士大人’吗？‘主人’是什么鬼"
    cq size2 a4 amazing"诶？"

    #（此处初咲的表情是那种好像宕了一下机的感觉，可以理解为突然犯傻）
    hide cx size2 a4 amazing
    hide village
    with pixellate
    show hall
    with pixellate
    show cx size2 a4 amazing:
        xalign 0.1
        yalign 1.0
        zoom 1.3
    with dissolve
    #（场景转换：转换回演出舞台的场景）
    show xy size3 a1 smile:
        xalign 0.9
        yalign 1.0
        zoom 1.2
    with dissolve
    xy "初咲学妹人物关系错了哦"
    xy "是对骑士的崇拜，而不是对主人的服从哦"
    cq size2 a3 wry_smile "抱歉啦~还是一不小心就把我和主人的关系代入演出了"
    xy size2 a2 normal"那个. . ."
    xy "你们现实中真的是的‘主仆关系’吗？"
    xy "从刚刚开始就一直听初咲学妹用‘主人’来称呼海川同学"
    "看着西野玥奈用着疑惑的眼神看着我，我不知道该如何回答她"
    ch "嗯. . ."
    ch "我和初咲. . ."
    cq size2 a3 happy"是那种关系哦！"
    cq "海川渡就是我的主人，我就是他独一无二的女仆！"  #（此处用闭眼得意表情）
    ch "是这样的没错"
    xy size2 a2 smile"我明白了. . .真是令人吃惊呢，主仆之间关系还能这么亲密. . ."
    xy "而且还是一起进入了高大. . ."
    ch "不是的，不是你想得那样子的！"  #此处暂停一秒钟
    $renpy.pause(1.0,hard=False)
    ch ". . ."
    "我忽然意识到，初咲恋柚和我并非真正意义上签订了主仆协定. . .我们之间只不过是互相成全对方而利用的关系. . ."
    "而且把初咲送到日本来的这件事. . .如果让更多的人知道就不好了"
    "更何况是西野家的大小姐. . .对于机器人的条条框框想必都了如指掌吧"
    "看着我一言不发的样子，西野玥奈似乎也没有继续向下追问的意愿了"
    xy size2 a2 smile"那. . .要不我们开始下一个即兴演出的环节？"
    cq size2 a3 happy"好耶！"
    xy "接下来就演辉夜姬吧！我觉得初咲学妹肯定会非常合适！"
    xy "海川的话就请扮演辉夜姬的一个追求者吧"
    cq size2 a3 smile"嗯，没问题的"
    hide xy size2 a2 smile
    hide cx size2 a3 happy
    hide hall
    with pixellate
    show shrine
    with pixellate
    #（场景转换：从演出舞台转换到《竹取物语》的明月演出场景）

    "随着场景灯光的变换，我们的面前慢慢呈现出了《竹取物语》中所描述的那个月圆的离别之夜. . ."
    "面前的初咲恋柚正在舞台映射的月光下翩翩起舞. . ."
    "虽然看上去很有些笨拙，但是这种姿态的舞蹈. . .让我真切地想到了她. . ."
    show white 
    show memory
    with dissolve
    #（此时加入昏黄回忆cg，同e6初咲线的回忆镜头线稿：一个女孩子正在舞台上舞蹈着（这里的cg效果像是老旧电视机那种“滋滋断片的声音”，像是记忆片段那种感觉，记忆有些回忆不起来的那种感觉））
    "初咲和她. . .好像. . ."  #（放完这句话屏幕减暗，然后呈现出下一行字，使得时间流逝，像是男主在回忆中的这么一句内心活动）
    hide white
    hide memory
    with dissolve
    "后续的饰演过程我记得不太清楚了，但在我的零碎记忆中，好像是西野学姐一直在给我们安排剧情，我们照着演出来就可以了"
    "记忆模糊的原因. . .或许是我也有点沉浸其中的缘故吧. . ."
    hide shrine
    with pixellate
    show hall 
    with pixellate
    #（场景转换：转换回演出舞台的场景（如果前面能弄出《竹取物语》的明月演出场景的话，这里就转，没有就不转））
    show xy size2 a2 normal:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with dissolve
    xy "那么，接下来是下一个片段，也是今天最特殊的一个噢"
    xy "由于某些缘故，一位女士非常想杀死另一位男士的剧情"
    ch "啊嘞？"
    xy "男性要被杀. . .也就是说要杀人的角色是. . .初咲学妹"
    "在西野学姐很平静地说完这句话后，仿佛周围的环境一改之前的轻松愉悦，转而变得压抑起来"
    hide xy size2 a2 normal 
    with dissolve
    hide hall
    with pixellate
    show airport afternoon
    with pixellate
    
    #（场景转换：转到一个类似于车站的场景，时间是傍晚黄昏时分）

    "随着光线的变换，我们很快又置身于一个类似于车站的场景，整个舞台看上去非常昏暗，气氛也异常地压抑"
    "台下的工作人员以为正在上演特殊演出，纷纷将目光投在我们的身上"
    "尽管初咲在我身上已经把这种剧本排练了好多次. . ."
    show white at flicker
    show street afternoon
    show cx size2 a2 serious:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    show memory
    with dissolve
    hide white
    #（昏黄滤镜开启
    cq "提问："  #（在e1上中的片段，此处动画为飞闪）
    hide cx size2 a2 serious
    with dissolve
    show white at flicker
    show park night
    show cx size2 a2 serious:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    show memory
    with dissolve
    #（插入第一张cg：初咲恋柚在一个路灯下拿着一柄小刀抵着海川渡）（不要这张cg了）
    hide white
    cq "不要回头噢，海川君！"
    cq "要不然很快就会. . ."
    cq "没，命，噢~"
    #昏黄滤镜关闭)
    hide memory
    hide cx size2 a2 serious
    hide park night
    hide street afternoon
    with dissolve
    "以及在九衢市的那个寒假. . .带着初咲一起学习中文的那段时间也经常和我扮演这样的“过家家式谋杀”"
    "在这样的场合下演出来式很羞耻的啊喂！"
    ch "那个. . .这么严肃的剧本，可能还是. . .不太适合现在的我们？"
    show xy size2 a2 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with dissolve
    xy "大胆尝试一下嘛，毕竟只有困难的东西才有挑战的必要"
    "远处的初咲，好像和平常的举动完全不一样，低着头，似乎是在仔细思索着什么重要的事情. . ."
    ch "但是. . .只有这个真的做不到啊！"
    hide xy size2 a2 smile with dissolve
    show cx size2 a2 serious:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with dissolve
    cq "不"
    cq size2 a3 happy"今天要在这里死去的，会是海川你哟"
    show airport afternoon with hpunch
    #（这里最好来一个震动的动效）

    "不知道是什么时候，初咲恋柚已经闪到了我的背后"
    "硬金属的冰冷触感从我身体上的一小点神经末梢传导到我的全身细胞，直觉告诉我. . ."
    "初咲恋柚正在用一个刀在抵着我的腰部. . .而且. . .绝对是那把我非常熟悉的刀！"
    cq size2 a3 smile"再动的话，小刀马上就会进入海川同学的身体里哦~"
    cq size2 a3 happy "我会刺得很干净利落的哦"
    ch "急促且略带病娇的台词从初咲的口中迸发出来，在这样的情况下，我完全不敢直视她的脸"
    cq "呼哈呼哈. . ."
    "甚至，投入其中的初咲完全没有注意到自己正在发出这样奇怪的喘气声. . ."
    "在与她相处的三个月中，我也并没有"
    ch "这样真的有可能不小心插进我的身体里的！"
    "我尽力压低了说话的语气，希望让初咲理解我现在正处于比平时更害怕的边缘"
    "换做是谁，面对这样一位刚刚还在微笑的女生急转成这样的口吻都会恐惧的吧！"
    cq "没关系的，很快就会过去的哦~"
    cq "死吧"
    xy "完美！"
    play sound "audio/鼓掌.mp3"
    #（此处播放效果音：“鼓掌声”，最好是在那种密闭大歌剧院里的那种感觉）

    #（场景转换：从刚才类似于火车站的场景转换回歌剧院的场景）
    hide cx size2 a3 happy
    hide airport afternoon
    with pixellate
    show hall with pixellate
    "几乎是同一时间，社长在初咲说完‘死吧’这个词后朝我们鼓起掌来，随之而动的是台下所有人员的热烈掌声"
    wa "他们的实力完全可以去参加东京的演出比赛，而且我打包票绝对是前三的实力！"
    wb "明明这个学妹超可爱的说，完全有不输给西野家的气质. . ."
    wc "真的好想和这个女孩子认识一下啊. . ."
    #（上述三句话最好是一种sound，不是那种点一句说一句，而是在旁边你一眼我一嘴的那种感觉）
    show xy size2 a2 smile2:
        xalign 0.1
        yalign 1.0
        zoom 1.2
    with dissolve
    "围观者各自有着自己的说法，不过我能听到的大概都在点评着初咲恋柚刚刚惊人的演出. . ."
    xy "看来你们真的很合适"
    xy size2 a2 smile"初咲学妹把那份决心表现得很好！"
    xy "海川同学也同样把极度的恐惧感给表现出来了"
    "只是真的被吓到了而已. . ."
    show cx size2 a3 happy:
        xalign 0.9
        yalign 1.0
        zoom 1.3
    with dissolve
    cq "好哦，得到前辈的认可了！"
    xy size2 a2 normal"不过让我很好奇的是，明明我还没有把道具发给你. . .没想到初咲学妹还会随身带着这么危险的东西"
    "西野俯下身，仔细打量着初咲手中的那柄冷蓝色小刀"
    "对啊. . .这根本就不像是常人的举止！"
    ch "是她经常给我修苹果用的小刀"
    xy "唔？"
    ch "因为我. . .呃，很喜欢吃苹果的缘故"
    xy "唔. . ."
    "看着我的慌张辩解，西野玥奈似乎是从中察觉到了些许不对劲，但又很快释然了"
    xy size2 a2 smile2 "原来如此"
    cq size2 a3 smile "学姐，还有多少呀？"
    cq size2 a3 happy "今天和主人的次数. . .实在是太多了. . .要坏掉了"
    ch "不要故意掉一两个词来营造这种奇怪的氛围啊喂！"
    "不过，这么说起来. . .我也确实感觉到自己的身体有些受不了了"
    "虽然这其中也有很久没参与演出的原因. . .但更多的是这种即兴表演的临场发挥感让我身心俱疲"
    xy size2 a2 smile"也是哦…你们的试演已经超过了一个小时哦"
    xy "真的是很棒的演出，我已经不想放你们回去了"
    xy "那就进入我们今天最后一个试演内容吧，让我看看. . ."
    "西野玥奈翻动着一张可能是写好了所有饰演项目的纸，仿佛是还有什么没有得到满足，必须让我和初咲进行一次饰演才肯罢休"  #（这里可以加入一个翻动纸张的效果音）
    cq size2 a3 smile"最后一个？忽然期待起来了！"
    ch "只要不是像刚才那样性质的试演我应该都能接受"
    xy size2 a2 smile2"放心点，最后的内容是很简单的"
    "很快，她手上的表单停留在某一面上，可以看得出来西野玥奈已经决定好了最后的演出剧本"
    xy size2 a2 smile"找到了，就是它！"
    xy "最终的kiss"
    ch "这是. . ."
    "一种极不好的预感席卷了我的全身"
    cq size2 a3 happy"哼哼，听上去很简单嘛！"
    "反观初咲，那家伙倒是一脸自信满满"
    xy size2 a2 happy"那么就请两位来为我们呈现即将别离的恋人吧"
    hide xy size2 a2 happy
    hide cx size2 a3 happy
    with dissolve
    hide hall with pixellate
    show schoolpassage day:
        zoom 1.2
    with pixellate
    #（场景转换：从歌剧院的场景转换到像是那种在樱花树下离别的场景（这里别的意境也可以，看审稿人的建议，笔者有些拿捏不准），这里算是cg第0张无人拆分，仅有背景）

    ch "恋人啊. . ."
    ch "等等，是怎么从恋人直接上升到接吻这个环节的？！！"
    show schoolpassage day:
        zoom 1.2
        linear 0.2 xalign 0.0
    "我斜眼向一旁的西野看过去，只见她正用炽热的眼光注视着我和初咲恋柚"
    show xy size2 a2 happy:
        xalign 0.1
        yalign 1.0
        zoom 1.2
    with dissolve
    "这是一种怎样的心理啊. . ."
    hide xy size2 a2 happy with dissolve
    show schoolpassage day:
        zoom 1.2
        linear 0.2 xalign 0.5
        linear 0.2 zoom 1.0
    "更何况，对于机器人来说，在没有安装对应的模块下，根本不可能会和人有那样的接触吧"
    "即便是初咲真正的主人. . ."
    ch "嗯？"
    show cx size2 a3 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with dissolve
    "突然间，一股柔软的触感与我的手臂相连"
    show cx size2 a3 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.3
        linear 0.2 zoom 1.4
    "她的两只手不知什么时候已经抓上我的肩膀上了，微微踮起的脚尖更加拉近了我与她的距离"
    "此时此刻，我的眼里，只剩下初咲一个人了"
    "娇嫩的嘴唇逐渐向我缓缓贴近，最终我感受到了她湿润的鼻息…"
    show white with dissolve #待插入cg
    #（此时插入cg：海川渡和初咲在舞台上（这里的背景是指舞台上呈现出来的背景，比如刚刚提到的樱花树，不是指原生舞台背景）  拆分二：此时两人正在接吻）
    #（注意这个地方需要暂停几秒，以保留cg的作用）

    "瞬时的电流伴随着我的脉搏而律动，最终完全刺激了我的大脑神经. . ."
    "视觉，味觉，触觉. . .似乎是每一个感官都在提示我，我正在与面前的美少女接吻"
    hide white with dissolve 
    cq "嗯. . ."
    ch "？！你. . .你在干什么！"
    show cx size2 a3 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.4
        linear 0.2 zoom 1.3
    "在初咲轻声呻吟了一下后，我的意识重新到了现实。几乎是喊出来的，我把初咲推开，朝后退了好几步"
    hide cx size2 a3 smile
    hide schoolpassage day 
    with pixellate
    show hall 
    with pixellate
    #（场景转换，从cg慢慢通过效果变到演出舞台上）

    wa "那家伙在干什么啊！那个女孩子明明这么配合. . ."
    wb "真是个自作多情的家伙"
    wc "我去真亲啊？"
    wd "可恶，好羡慕啊！我也想和美少女接吻"
    #（上述4句话最好是一个sound文件，不是那种点一句说一句，而是在旁边你一眼我一嘴的那种感觉）

    "恍惚之中，我已经有些听不清楚台下的同学在说什么话了"
    "大概也是在细数我刚刚有些粗暴的行为吧"
    ch ". . ."
    ch "刚刚我有些失控了…"
    show cx size2 a4 sad:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with dissolve
    cq "我也不该突然就那样的…！"
    "实际上，我并不反感刚刚的接吻，主要是一切的一切都太过突然了. . ."
    hide cx size2 a4 sad with dissolve
    show xy size2 a2 happy:
        xalign 0.1
        yalign 1.0
        zoom 1.2
    show cx size2 a4 sad:
        xalign 0.9
        yalign 1.0
        zoom 1.3
    with dissolve
    xy "很不错很不错！"
    xy "不过海川同学请冷静下来"
    xy "刚才初咲学妹并没有实际上亲上去哦. . ."
    ch "诶？？？"
    "这么说来，刚刚我就觉得那种触感. . .不像是柔软的嘴唇带给我的那种感觉"
    cq size2 a3 smile"嘿嘿. . .不会主人以为我真的会就那样就亲上去吧？"
    ch "咳咳，拜托就不要再调侃我了"
    xy size2 a2 smile2"好啦，初咲同学的演技还是很厉害的，已经可以做到以假乱真了"
    cq size2 a3 happy"真的吗！谢谢，我会继续加油的！"
    xy size2 a2 smile"海川同学的话，还要好好磨练一下表演的能力"
    xy "就算有着强烈的感情，如果不能传达给观众的话，那也是没用的"
    ch "嗯，我知道的"
    "那句话，还是被西野学姐说出来了. . ."
    xy size2 a2 happy"今天就先到这里吧，从现在开始海川同学和初咲同学也算正式入部的部员了"
    cq "好耶，我们要好好庆祝一番了！"
    ch "咳咳，拜托就不要再调侃我了"
    play sound "audio/下课铃.ogg"
    #（此时播放效果音：铃声。铃声敲响的声音，日本用的下课铃的那种感觉？？？）

    "学校日常的铃声把我从悸动中敲醒，我突然意识到了一件很重要的事情好像被我忘记了"
    ch "对了"
    ch "初咲是不是忘记了什么重要的事情？"
    cq size2 a3 normal "嗯. . .有吗？"  #（此处的表情转变为疑问脸）
    ch "我记得，初咲应该是在今天下午有高大组织的课程吧？"
    ch "明明在一开始我就觉得初咲出现在这里很奇怪. . ."
    cq size2 a4 amazing "诶？"
    cq "诶~ ？！"
    cq size2 a3 smile"因为太想来创作演绎部了，所以. . ."
    ch"所以就很理所当然地翘掉了第一节机器人学习课呢"
    cq size2 a3 smile"对不起！"
    cq "现在赶过去的话应该也不算迟！"
    ch "所以就很理所当然地翘掉了第一节机器人学习课呢"
    "像是察觉到了我不高兴的情绪，初咲这次并没有选择和我争锋相对，可能是她也意识到了问题的严重性"
    ch "快去吧，不然就是我这个主人的全部失责了"
    cq size2 a4 little_serious"唔. . ."  #（>_< 这种表情的感觉）
    cq size2 a3 smile"那主人可以稍微等我一下嘛，我想一起回家！"
    xy size2 a2 smile2"下次再见了，初咲学妹"
    cq size2 a3 happy"拜拜！"
    "说完，伴随着一路小跑，初咲很快从我的视线中消失了"
    hide cx size2 a3 happy
    hide xy size2 a2 smile2
    with Dissolve(0.2)
    show square day
    show yq size1 a1 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    show memory
    with dissolve
    #（昏黄滤镜开启
    yq "喂喂，你要不要和我一起入部呀，这个真的超厉害的. . ."  #（这里是e2上岩崎拉着男主在摆摊上到处转的一句台词）
    #昏黄滤镜关闭）
    hide square
    hide yq size1 a1 smile
    hide memory
    with dissolve
    "那家伙也把机器人该修习的课程给翘掉了吧. . ."
    "就在我沉浸在对一天的回顾中，西野学姐突然从旁边闪到我的面前"
    show xy size2 a2 normal:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with dissolve
    xy "那个，海川同学"
    ch "嗯？怎么了"
    xy "我没记错的话，今天下午也只有robot会有课程吧？"
    ch "是的. . ."
    "我完全没有想到，自己不经意的对话已经让事情到了一种不可逆转的态势"
    "真是糟糕的局面"
    ch "呼. . ."
    xy "那么，被我说中了吗？"
    ch "呼. . ."
    "就算是要隐瞒，在这样的高大里，加入了创作演绎部的初咲恋柚也不可能永远将自己的身份藏下去. . ."
    ch "是的，应该和西野想的一样，初咲确实是robot"
    xy ". . ."
    xy "你们看起来也像是robot和主人的关系……"
    xy ". . .我明明早该察觉到的. . ."
    "从西野的语气中，我能明显地听出来有一丝丝遗憾裹挟在其中"
    ch "也是，毕竟在同级的学生之中，应该没有比学姐更懂机器人的了"
    xy "初咲学妹在我见到过的机器人中，已经算是最智能的那一类型了"
    ch "这样啊. . .毕竟她是今年的最新款，所以说各项性能应该都是最优的"
    xy "太不可思议了. . ."
    xy "虽然她的表演真的很让我感到惊诧"
    xy size2 a2 littlesad"不过我还是不太能放心地把舞台交给机器人"
    ch "我明白了"
    ch "毕竟再先进的技术也有自己的缺陷. . .不可能所有的东西都是完美的"
    xy size2 a2 normal"不对哦，海川同学"
    xy "我认为，演出更注重的是表演者的情感"
    xy "情感应该是表演者由衷地表现出的真实"
    xy "而机械能做到的不过是通过模仿来拟合最真实的情况"
    xy "所以我认为这不是艺术，只是精巧的模仿"
    ch ". . ."
    "虽然在某些程度上来说，西野学姐对艺术的理解让我并不是很满意"
    "但也并不是毫无道理和依据的"
    "看起来，就算是laser家的大小姐，也对演出有着自己别样的执念. . ."
    ch "我会把学姐的意思告诉初咲的，让她自己做好退出部门的准备"
    hide xy size2 a2 normal
    show airport afternoon
    show cx size2 a3 happy:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    show memory
    with dissolve
    #（昏黄滤镜开启
    cq "真的吗？！"
    cq "看来我还是很有希望的呢，哼哼. . ."
    cq "抱歉啦~还是一不小心就把我和主人的关系代入演出了"
    cq "今天要在这里死去的，会是海川你哟"
    #（此时插入加了昏黄滤镜的cg：海川渡和初咲在舞台上（这里的背景是指舞台上呈现出来的背景，比如刚刚提到的樱花树，不是指原生舞台背景）十指相扣，拆分一：此时两人并没有接吻上去）
    #（这里的动画最好为快闪）
    #昏黄滤镜关闭）
    hide cx size2 a3 happy
    hide airport afternoon
    hide memory
    with Dissolve(0.2)
    "我挑起放在一旁座椅上的书包，正打算离开的时候，被西野学姐叫住了"
    show xy size2 a2 normal:
        xalign 0.5
        yalign 1.0
        zoom 1.2
    with Dissolve(0.2)
    xy "等一下"
    xy "请不要误解我的意思"
    xy "初咲学妹是不用退出创作演绎部的"
    ch "这是可以的吗？刚刚学姐的意思不是. . ."
    xy size2 a2 smile"以初咲学妹的能力，完全可以在部门里给各位做出表率的"
    ch "也就是说. . .初咲恋柚也只能是担当大家的表率吗？"
    xy ". . ."
    xy size2 a2 littlesad"其实，‘创作演绎部’也是今年刚刚成立的"
    xy "就算算上海川同学和初咲同学，到现在为止部门里能上台表演的成员也只有不到十人. . ."
    ch "诶？原来是这样吗"
    ch "我记得，手册上面不是提到了创作演绎部之前的很多场活动"
    ch "而且还是在那样破旧的舞台上. . ."
    xy size2 a2 normal"那个其实. . ."
    xy "东京歌舞团上的表演图. . ."
    ch ". . . . . ."
    ch "原来是这样"
    ch "这么豪华的演出舞台，用那样子的配图也未免太劝退了"
    ch "话说回来，初咲应该还是有机会上台表演吧？"
    xy "当然. . .就是. . .要求也会更高一点"
    xy "总之，就请海川同学替我传达我的意思吧"
    xy "拜托了！"
    "虽然平常喧闹的初咲恋柚总是会给我带来很多烦恼，但在这个时候，我忽然却很想帮她"
    "明明她是这么喜欢的演出. . ."
    ch "时间也不早了，那我就不打扰其他同学的试演了"
    xy size2 a2 smile"下次的部活是在下周的同一时间段，海川记得把初咲带来哦！"
    ch "好的"
    "在了解了下次部活的时间后，我和西野学姐互相道别后就离开了"
    hide xy size2 a2 smile
    with dissolve
    hide hall with tran_lf
    show square day with tran_lf
    #（场景转换：来到学校内的场景，取景华科，稍微用novelai来改一下学校里的画风。这里停顿2-3s？）

    "因为下午没课的缘故，我在学校里兜兜转转了两个小时，最后来到了和初咲约好的地点"
    ch "robot的集中培训啊. . ."
    "我太了解robot的课程，但是根据岩崎给我透露的信息，课程的大部分内容是在检验robot的性能参数，学习能力以及各项指标"
    "毕竟十年前爆发在“华中laser精工”的“那个事件”，对现如今世界各地robot的管理起到了非常大的影响. . ."

    #（播放效果音：“叮铃铃”，那种下课的铃声，在风格上最好和日本用的保持一致，增强故事的真实性，或者这里考虑不使用传统的铃声）
    play sound "audio/下课铃.ogg"
    show cx size2 a3 smile:
        xalign 0.1
        yalign 1.0
        zoom 1.3
    with dissolve
    cq "主人！"  #（这里闪现出初咲恋柚的立绘来）
    "在听到初咲熟悉的呼唤后，我很快又从初咲的身后发现了一同前行的岩崎天桐"
    show yq size3 a1 smile:
        xalign 0.9
        yalign 1.0
        zoom 1.3
    with dissolve
    yq "哟，你也在这里？"  #（这句闪现出岩崎天桐的立绘）
    ch "诶？"
    ch "你刚刚不是在‘超自然研究协会’那儿吗. . ."
    yq "害，别提了"
    yq size3 a1 little_sad"本来我和部长聊得正欢，最后还是被小蘭抓过来了. . ."
    ch ". . ."
    ch "根据学校的规定，除非是解除和主人的关系"
    ch "不然这些责任都是要robot的主人来承担的啊喂！"
    yq size3 a1 smile"原来如此"
    yq "不过幸好，我过去的时候赶上了刚进行了一半的课程"
    yq "还恰巧碰上了初咲同学"
    cq size2 a3 normal"唔. . ."
    cq "我恰巧忘记把上课的这件事丢在记事本里了"
    ch ". . ."
    ch "怎么会有这种‘恰巧’的事情啊！"
    ch "你们都是把‘上课’的日程放在了最后吧！"
    voice "voice/l_voice/episode2/e2 蘭 018.mp3"
    show lan size2 a1 little_serious:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with dissolve
    l "岩崎你这个大笨蛋！不是说好在高大校门口等着我的吗？"  #（这里出现立绘，蘭的不太高兴表情）
    "从我身后突然出现的蘭，狠狠地拍了一下岩崎，用着很是不满的眼神看着他"
    yq size1 a1 amazing"喂喂，这不是你自己找过来的吗，都还没到约定的五点呢"
    voice "voice/l_voice/episode2/e2 蘭 019.mp3"
    l size2 a1 normal"也对"
    voice "voice/l_voice/episode2/e2 蘭 020.mp3"
    l "不过倒也给我注意一点啊，真的很让人着急的. . .今天你的课程也是差点没去成. . ."
    yq size3 a1 smile"好啦好啦，下次我不会再这样的了"
    yq "明明刚刚就被海川教育了一顿. . ."
    ch "咳咳，不如这样"
    ch "既然现在时间还不算太晚，就一起去学校的那家咖啡店看看？"
    voice "voice/l_voice/episode2/e2 蘭 021.mp3"
    l size2 a1 happy"咖啡店？是那家口碑超棒的吗？"
    cq size2 a3 happy"咖啡咖啡！"  #（稍稍显得激动一点的表情）
    yq "看来海川很喜欢去咖啡店那种地方哦"
    ch "毕竟是下午茶时间嘛. . .那种地方，最适合几个人一起聊天"
    cq size2 a3 smile"嗯嗯，我也很喜欢哦！"
    voice "voice/l_voice/episode2/e2 蘭 022.mp3"
    l size2 a1 normal"本小姐今天还要完成剧本编写的工作，可是很忙的喂"
    ch "今天也有剧本编写的任务吗？"
    voice "voice/l_voice/episode2/e2 蘭 023.mp3"
    l size2 a1 proud"当然，还是来自学姐的邀请"
    voice "voice/l_voice/episode2/e2 蘭 024.mp3"
    l "我会亲自完成创作演绎部的第一本剧本"
    ch "创作演绎部？？？"
    cq size2 a3 smile"也是在西野学姐的那个大剧院里工作吗？"
    voice "voice/l_voice/episode2/e2 蘭 025.mp3"
    l size2 a1 proud"是的. . .诶？你们怎么都知道？"
    yq size3 a1 normal"以海川和初咲这样对演出的热爱，他们肯定也加入了‘创作演绎部’"
    yq size3 a1 smile"这才是值得讴歌的青春啊！"
    ch "喂喂，不要用这种奇怪的非口语词汇套在我的身上啊"
    yq "好啦，我早就料到你们也会和小蘭一样加入创作演绎部的. . ."
    voice "voice/l_voice/episode2/e2 蘭 026.mp3"
    l size2 a1 little_serious"诶. . .不要那样喊我了，中二病！"
    ch "那个. . .容我插一句嘴. . .编导部不是单独的另一个部门吗？"
    voice "voice/l_voice/episode2/e2 蘭 027.mp3"
    l size2 a1 smile"海川啊海川，编排剧本又不一定非要在‘编导部’"
    voice "voice/l_voice/episode2/e2 蘭 028.mp3"
    l "就算是‘创作演绎部’，也有相关的工作呀！"
    ch ". . ."
    "阴差阳错地，又莫名多了和蘭一起工作的时间. . ."
    yq "咳咳，我们还是先到咖啡店坐下来慢慢聊吧"
    ch "那就先去那家咖啡店去看一下吧"
    cq size2 a3 happy"一起出发吧！"
    hide cx size2 a3 happy
    hide lan size2 a1 smile
    hide yq size3 a1 smile
    with dissolve
    hide square with tran_lf
    show cafe out with tran_lf
    #（场景转换：咖啡店外，从学校一隅转到了校内的一个咖啡店外侧，和在九衢市咖啡店的样式一样）

    "很快，我们就来到了这家高大里的一家咖啡店"
    "听说是因为这里离主教学楼非常远的缘故，每天来这里喝下午茶的学生都很少"
    show yq size1 a1 smile:
        xalign 0.1
        yalign 1.0
        zoom 1.3
    show lan size2 a1 normal:
        xalign 0.9
        yalign 1.0
        zoom 1.3
    with dissolve
    yq "看上去好熟悉的感觉"
    voice "voice/l_voice/episode2/e2 蘭 029.mp3"
    l "走吧，我的时间是很宝贵的，要不是最近出了这么多事. . ."
    hide cafe out 
    hide yq size1 a1 smile
    hide lan size2 a1 normal
    with tran_lf
    show cafe with tran_lf
    #（场景转换：从咖啡店外转到咖啡店内）

    "咖啡店的环境带给我无比的温馨感"
    "除了店里的标识是用日语标注之外，这家店给我的感觉和九衢市我常去的那家几乎一模一样"
    dy "欢迎光临，请问要点些什么呢？"
    ch "那个，就来两杯美式吧"
    voice "voice/l_voice/episode2/e2 蘭 030.mp3"
    show lan size2 a1 normal:
        xalign 0.1
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    l "一看海川就是不了解咖啡的人吧。美式是很苦的诶！"
    "在蘭仔细地盯着那本日式的菜单默读了半分钟后，她指着菜单上的那个樱花状的咖啡杯"
    voice "voice/l_voice/episode2/e2 蘭 031.mp3"
    l "请给我来一杯这个. . .樱花拿铁"
    dy "好的，是一杯美式，一杯樱花拿铁对吗"
    voice "voice/l_voice/episode2/e2 蘭 032.mp3"
    l "对"
    ch "虽然之前就听岩崎说到过蘭的日语并不是很标准，没想到竟然会比想象中的要差更多. . ."
    ch "看来你的日语还是不够标准啊"
    voice "voice/l_voice/episode2/e2 蘭 033.mp3"
    l size1 a3 mad"彼此彼此"
    voice "voice/l_voice/episode2/e2 蘭 034.mp3"
    l "本小姐也就只有口语稍微逊色了一点. . ."
    "涨红了脸的蘭把头别在一边，看上去对我说的话非常不满意"
    "很快，店员就把准备好的两杯咖啡送到了我们的面前"
    voice "voice/l_voice/episode2/e2 蘭 035.mp3"
    l size1 a2 normal"所以说，你是以演员的身份加入创作演绎部的吗？"
    ch "算是吧"
    ch "纠正一下，是‘你们’，不是‘你’"
    ch "因为初咲恋柚也成为了创作演绎部的演员之一"
    show cx size2 a3 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    cq "没错哦！而且我被西野学姐狠狠表扬了"  #（表情为微笑）
    show yq size3 a1 smile:
        xalign 0.9
        yalign 1,0
        zoom 1.3
    yq "我好像记得，初咲也是非常喜欢表演的对吧？"
    cq "是的！"
    yq "看来你们俩真的很适合凑成一对呢"
    ch ". . ."
    "一想到刚刚的那种场景"
    show white
    show memory 
    with dissolve
    $renpy.pause(1.0,hard=False)
    hide white
    hide memory 
    with dissolve
    cq size2 a3 happy"我和主人可是绝佳的组合哦！"  #（说完这句之后看看用什么效果隐去初咲恋柚的立绘）
    hide cx size2 a3 happy with dissolve
    yq size3 a1 normal"嗯~嗯"
    ch "所以，从创作演绎部的名字上来看，应该是‘创作’和‘演出’结合的那种感觉吧. . ."
    ch "之前在国内的时候还从来没想过这样可以简化交流的成本. . ."
    voice "voice/l_voice/episode2/e2 蘭 036.mp3"
    l size1 a1 proud"是啊，某个人甚至因为之前看不懂我写的剧本来找我理论. . ."
    ch "不要用‘某些个人’来作为‘海川渡’的代名词啊！"
    ch "算了. . .当时我在剧本上的理论学习确实太少了"
    voice "voice/l_voice/episode2/e2 蘭 037.mp3"
    l size2 a1 normal"所以说，对于一个合格的演员，学习剧本理论和表演是同样重要的！"
    voice "voice/l_voice/episode2/e2 蘭 038.mp3"
    l size2 a1 smile"像海川这样轻浮的人是更需要时间来沉淀的"
    ch "我知道的了，现在看懂剧本这种事情对我来说还是很容易"
    yq size3 a1 normal"咳咳，我稍微插句话"
    yq "现在应该不是沉浸在‘创作’和‘演出’上"
    yq "倒不如说最重要的事情上，我们完全没有进展"
    ch "最重要的事？"
    yq "找到初咲的主人"
    "岩崎将头朝一旁不知所措的初咲点了点，试图将我们的目光全部转向初咲的身上"
    voice "voice/l_voice/episode2/e2 蘭 039.mp3"
    l size1 a2 little_serious"对哦，这几天我和岩崎做了不少调查"
    play sound "audio/PC_lock_off.ogg"
    #（此时播放效果音：“咚”，拿出一本书然后放在桌子上的声音，呈现出screen电子屏在界面中，上面密密麻麻地写着各种字样和东京的大概版图，上面标上了几个点，可以通过鼠标点击查看具体的信息）
    voice "voice/l_voice/episode2/e2 蘭 040.mp3"
    l "我们查找了laser数据库里东京有关‘初咲恋柚’的相关信息，只有三个结果可以对应上"
    "蘭从挎包中掏出了电子记事本，上面密密麻麻地标注着各种信息，其中三个亮点表示的是蘭提到的和初咲恋柚同名同型号的机器人"
    yq size3 a1 amazing "话说，laser里这么机密的信息都是能随便公开的吗？"
    ch "其实laser对外公开的也只有robot的各种详细参数，主人的代号也是用只有laser才能识别出的uid来代替的"
    "实际上，这和现在所推行的“仿生机器人”与一般人平权的做法是相悖的"
    "这也是在发生了那次“华中laser精工事件”之后做出的一系列改革. . ."
    voice "voice/l_voice/episode2/e2 蘭 041.mp3"
    l "你们看，系统里的数据也只有这三个能对应上初咲的名字"
    yq size1 a1 little_serious"虽然从robot的‘署名’上来说，初咲的主人可能在登记的时候换了一个名字. . ."
    yq "这样就会导致我们面前的初咲信息缺失. . ."
    ch "所以，你的意思就是当初在注册初咲恋柚的信息的时候，‘初咲恋柚’的真实姓名并不叫‘初咲恋柚’吗"
    yq "没错"
    voice "voice/l_voice/episode2/e2 蘭 042.mp3"
    l "不排除其他信息的替换，我们可能还需要把整个数据库给核对一遍"
    yq "而且还是全世界所有生产出来的robot信息"
    ch "全世界？也不至于有这么多需要一条条检索吧"
    voice "voice/l_voice/episode2/e2 蘭 043.mp3"
    l "要知道在黑市里，篡改任何一条信息都是很简单的"
    "好像之前在九衢市的黑市里，也是这样"
    show store
    show memory
    with dissolve
    $renpy.pause(0.5,hard=False)
    hide store
    hide memory
    with dissolve
    #（昏黄滤镜+九衢市修理铺的背景，快闪动画）

    ch "虽然原先的主人也并不是没有可能全部填错了信息. . ."
    ch "这怎么样看都是故意的吧！"
    "坐在一旁的初咲恋柚一直在盯着我的眼睛"
    "看上去她似乎有什么话很想说出来"
    ch "要不然，我们让初咲也说几句吧. . .比如回忆一下主人的特征还有各种与原本主人相关的信息"
    "虽然之前我一直都听过初咲恋柚断断续续讲过有关于自己真正主人的事，但我好像从来没有完整地听完"
    show cx size2 a4 little_serious:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with dissolve
    cq "大家都为我做了这么多. . .我不知道该怎么感谢各位. . ."
    ch "这都是我们自愿帮忙的，没必要太放在心上. . ."
    yq size1 a1 smile"毕竟都走到这一步了,不帮也是不行啊"
    voice "voice/l_voice/episode2/e2 蘭 044.mp3"
    l size1 a3 mad"喂喂，不会说话就不要说，好好听初咲讲完"
    cq size2 a3 smile"真的很感谢大家！"
    cq size2 a4 sad"不过我完全不记得之前主人的事情了"
    cq "因为和主人相处的时间很短，之前的很多在日本的记忆就被当作垃圾一样处理掉了. . ."
    ch ". . ."
    "虽然我对仿生机器人的技术了解不够深刻，不过之前好像也听说过仿生机器人的系统也会因为保持存储器的存储空间而定期清理. . ."
    "但也不至于把主人的所有信息都给删除掉吧. . . "
    cq size2 a4 little_serious"不过有一点我印象很深刻"
    cq "那就是，原本的主人好像是照着她的样子来打造我的"
    ch "照着她的样子. . .也就是说初咲和原本主人是很相像的？"
    "我原本以为只会是那种中年男性才会购置像初咲这样可爱的robot"
    yq size1 a1 little_serious"嗯嗯，这是一个很好的突破口. . .或许可以减少很多工作量"
    cq "还有就是，主人现在也应该是在目黑川居住的！"
    cq "我知道的就只有这么多了. . ."
    yq "事情不就越来越明朗了嘛"
    yq "如果换做是检索所有robot的信息. . .那至少也要三个月的时间"
    ch "原来如此，这样的话换做是线下寻找. . .工作量也会减少不少"
    voice "voice/l_voice/episode2/e2 蘭 045.mp3"
    l size1 a2 smile"至少，寻找初咲主人的事情正在逐渐明朗起来"
    cq size2 a3 smile"嗯嗯！"
    cq "不过我不着急的哦！"
    cq "倒不如说是想趁着这段时间好好玩一下. . ."
    ch "那就从今天晚上开始吧，我们会帮助初咲一起寻找主人的"
    ch "然后就请蘭和岩崎天桐来负责为我们制定路线以及统计搜查的结果，我们争取在最短的时间把初咲恋柚送回家"
    voice "voice/l_voice/episode2/e2 蘭 046.mp3"
    l "ok，没问题的"
    yq size1 a1 smile"交给我们吧"
    cq size2 a3 normal"诶？不叫上母亲大人吗？"
    ch "她的话. . ."
    show home2 afternoon 
    show mom size1 a1 happy:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    show memory
    with dissolve
    #（昏黄滤镜开启
    ma "原来是这样啊. . ."
    ma "海川君好厉害呀！"
    ma "竟然背着你的母上大人找到了一个日本的女朋友. . ."
    hide home2 afternoon
    hide mom size1 a1 happy
    hide memory with dissolve
    #（此段文本来源于e2上半部分）
    #昏黄滤镜关闭）

    "真的算得上一个让人放心的母亲吗. . ."
    ch "各位还要忙着各种各样的事，真是辛苦大家了"
    ch "对了"
    ch "蘭那边的编剧工作是要几点钟去呀？"
    voice "voice/l_voice/episode2/e2 蘭 047.mp3"
    l size1 a2 smile"也不算晚吧. . .大概是六点钟的样子"
    ch "可是现在都已经快五点了"
    voice "voice/l_voice/episode2/e2 蘭 048.mp3"
    l size1 a2 amazing"诶？？？！怎么过了一个小时了"
    voice "voice/l_voice/episode2/e2 蘭 049.mp3"
    l "岩崎你倒是提醒我一声啊！"
    yq size3 a1 little_sad"看你和海川聊得这么投入，就没想着打搅你们两个人了. .."
    ch "蘭也快点去吧，剧本编审的工作也确实辛苦. . .更何况是刚入学的新生就加入了东京歌剧院的编审部"
    ch "这件事已经貌似还在在同级的学生里已经传开了，好像大家都多少听过你的名字. . ."
    voice "voice/l_voice/episode2/e2 蘭 050.mp3"
    l size1 a1 smile"倒也没有那么厉害啦~"
    yq size3 a1 smile"好啦，我们快走吧！"
    hide yq size3 a1 smile
    hide lan size1 a1 smile
    with dissolve
    ch "很快，岩崎就把蘭给拉走了"
    ch "那我们也走吧？"
    cq size2 a3 happy "好的！"

    play sound "audio/cafe_chime.ogg"
    hide cx size2 a3 happy with dissolve
    hide cafe with tran_lf
    show cafe out afternoon with tran_lf 
    #（场景转换：从咖啡店内转换倒咖啡店外，此时时间为夕阳西下，注意这里要播放离开店的风铃声，和在九衢市的咖啡店环境相对应）

    ch "那个，"
    "虽然这是我一直积压在心理的问题，也是我一直想要得到的答案. . ."
    "我很清楚自从从九衢市毕业之后，我对演出的心态发生了不小的变化"
    "甚至. . ."
    "我感觉到站在台上表演已经完全放不开了. . .能够完整地完成一场演出对我来说应该都是难事"
    show hall 
    show xy size2 a2 normal:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    show memory
    with dissolve
    #（昏黄滤镜开启
    xy "海川同学的话，还要好好磨练一下表演的能力"
    xy "就算有着强烈的感情，如果不能传达给观众的话，那也是没用的"
    #昏黄滤镜关闭）
    hide hall 
    hide xy size2 a2 normal
    hide memory
    with dissolve
    "从这个寒假开始，我也尝试过对着镜子不断地磨砺自己的演技"
    "不过好像. . .从那之后，我的水平就一直在退步，完全放不开来. . ."

    #（场景转换：从咖啡带店外转换到太鼓桥）
    hide cafe out afternoon with tran_lf
    show street2 afternoon with tran_lf
    "不知道什么时候，我和初咲一同走到了家和学校的必经之路——太鼓桥上"

    #（此时场景平滑移动，展现出背景的优美）

    "素有“樱花大道”美誉的太鼓桥，就算再怎么美丽动人我也欣赏不来"
    "我一定要向初咲问清楚这件事"
    ch "那个"
    ch "初咲觉得今天我的表演怎么样啊？"
    show cx size2 a3 surprised:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    cq "诶？"  #（这里的表情是那种一下子愣住，没有料到海川渡会问这种问题的表情）
    cq "主人的表演？"
    cq size2 a3 smile"我觉得很不错哦！"
    ch "说实话，不用想着取悦我的"
    cq size2 a3 normal"唔. . ."
    cq size2 a3 smile"主人，你知道吗？"
    cq size2 a3 happy"今天的你，简直就像一个不知所措的王子呢！"
    ch "诶？你在说什么啊？"

    #（此时暂停几秒，这里的镜头语言笔者不知道该怎么安排，总之尽可能唯美一点）

    "一蹦一跳的初咲走在我的前面，时不时转头冲着我微笑"
    "这家伙. . .仔细看过去还蛮可爱的嘛"
    ch "不知所措的王子. . ."
    "我自顾自地重复着初咲对我的评价，不断思考着这个词的含义"
    "至少. . .不算是贬义词吧！"
    cq "呐呐，与其说起这个，不如想想今天晚上我们去哪里庆祝呀？"
    ch "呼. . ."
    "我深吸了一口气，很快将复杂的心情平静下来"
    ch "那就去你之前说的，一直很想回东京看看的‘最高的樱花树’，顺便再去调查一下你的主人"
    cq "好哦！"
    "看着她满脸的笑容，可能. . ."
    "作为她真正的主人会是很让人高兴的事情吧"
    "至于演出能力的提升，就交给之后的自己吧"
    hide cx size2 a3 happy
    hide street2 afternoon
    with close_eyes
    #（此时播放动画，屏幕先缩成一个椭圆，然后慢慢缩成全黑，类似于电影中那种从主角视角看闭眼的效果）
    #（播放效果音：“咚”，倒在地上的声音，此处的屏幕为全黑）
    cq "主人，没事吧，没事吧？"
    "疲惫的感觉如同藤蔓缠在自己的脖颈处，我很快就没有了知觉. . ."

    stop music
    jump episode3_1
