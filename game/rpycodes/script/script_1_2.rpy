﻿
###  episode1下半部分 ################
label episode1_2:

    window hide
    play music "bgm/testbgm/BGM10.ogg"
    scene black
    show street day with dissolve
    # 转场
    show cx size2 a3 happy:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    with Dissolve(0.2)
    cq  "哼哼哼~！"
    "走在我身旁的初咲一路上哼着歌，不时还会突然走到我的面前原地转个圈"
    "好像从刚才开始，她看上去就非常高兴的样子"
    "虽然已经完全可以用“过分真实且可爱”这种词来形容初咲"
    "不过对于仿生机器人来说，这看上去也不是最新型号做不到的事情…… ……"
    
    ch  "看来初咲真的很喜欢表演啊"
    "虽然我已经用了很小的声音来说这句话"
    "但还是被走在我前面的初咲听到了"
    cq size2 a3 normal "海川刚刚在说什么呀？"
    "少女从前面突然转过身来，稍微俯身"
    ch  "喂喂！嘘~ "
    ch  "我们说好了的呀！"
    ch  "出门之后就不许再说日语了！"
    cq size2 a4 little_serious"唔……唔……"
    "在听到我的斥责之后，初咲明显安静了很多"
    cq "唔……！唔……！"

    "可是不过一会儿，初咲不断挥舞着自己的双手，仿佛有什么很重要的事现在就急着和我说"
    ch  "……"
    ch  "……"
    ch  "……"
    cq  size2 a2 serious"唔……！唔……！"  
    "看上去初咲是真的有什么话想和我说"
    ch  " 哎……"
    ch  "好吧好吧……"
    ch  "你还是可以说的，不过音量控制到只有我们两个人能听到的范围就好了……"
    cq size2 a3 normal"噗哈……"
    cq  "我知道了……"
    cq size2 a3 wry_smile"嗨呀，明明只有我和主人两个人……"
    "尽管我已经预料到了初咲会突然凑上前来"
    "但我还是被吓得不轻，往后稍微躲了躲"

    cq size2 a4 little_serious"莫非……是觉得我和那个叫‘秋月’的女生非常像……？"
    cq  "然后主人对初咲有别的想法……？"
    ch  "不是的！这两件事一点关系都没有"
    ch  "只是你这样突然凑近真的很不适应……"
    ch  "话说初咲对你真正的主人也是这样子活跃的吗？"
    cq size2 a3 normal"唔……"
    cq  "至少是在最近开始……"
    ch  "这样啊……"
    "初咲的话不免让我陷入沉思中"
    "我根本想象不出来自己在她心中充当所谓的“临时主人”到底是怎么样的一个存在"
    "我还真是一个矫情的人……明明从名义上初咲就完全不属于我……"

    # （场景转换，转换到公园，白天）
    cq size2 a4 smile "呐呐，如果是中文……"
    cq  "会不会非常难学呀？"
    ch  "那倒也不至于"
    ch  "因为中文和日语在某种程度上也非常相近……"
    cq  size2 a3 happy"我明白了！"
    cq  "我会努力的，还请主人信任我吧！"
    hide cx size2 a3 happy with Dissolve(0.2)
    # （场景转换，转换到图书馆门口，这里的素材随便找一个就好了）
    hide street day with tran_lf
    show library day with tran_lf 
    show cx size2 a3 surprised:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    with Dissolve(0.2)
    stop music fadeout 1
    play music "bgm/testbgm/BGM04.ogg" fadein 1
    cq  "这就是……"
    cq  "九衢市的中心图书馆诶！"
    ch  "别喊这么大声啊喂！"
    ch  "很容易被被人注意到的！"
    cq size2 a3 smile"好的好的，我明白的啦~"
    ch  "总之，我们先进去看看有没有我们需要的书"
    cq size2 a3 happy "好耶！"
    hide cx size2 a3 happy with Dissolve(0.2)
    hide library day with tran_lf
    show library inside with tran_lf
    # （场景转换，转换到图书馆里面的一个书架，这里的素材随便找一个就好了）

    "很快我们就登上了三楼，瞄准了写有“中文专区”几个大字的书架，开始一本本搜罗初咲恋柚需要学习的书籍…… ……"
    "早在来之前我就已经做好了相关的调查工作……目前网上关于“如何教会新世代仿生机器人一门新语言”这样的论文的数量也约等于0"
    "所有遗留信息也就藏在初咲恋柚的这个型号的部分官方开源代码上……"
    show thinking with Dissolve(0.2)
    # （屏幕加上黑幕遮盖，增加内心思考的那种氛围感）
    ch  "符合初咲型号的……"
    ch  "JAPAN-20500101-LASER-PTF-04……"
    "初咲的PTF-04型号对应着语言学习功能是一个叫做“NLP_JAPTra_CVNN”的算法来实现的"
    "由于这是在设定之初就已经在线迭代了无数次的结果"
    "所以对于现在的我来说，必须在有限的一个月之内采用合适的方式让初咲用同样的方式来学会中文……"
    hide thinking with Dissolve(0.2)
    # （去掉黑幕遮盖）
    show cx size2 a3 normal:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    with Dissolve(0.2)
    cq  "诶……主人你看这本书可以吗？上面写着的是‘中文的急速育成法’……"
    ch  "嗯嗯……可以的……"
    show thinking with Dissolve(0.2)
    # （屏幕加上黑幕遮盖，增加内心思考的那种氛围感）
    "“NLP_JAPTra_CVNNnet+++”的算法，"
    "它的原理其实并不难……"
    "让CVNN神经网络修正另一个CVNN神经网络中的参数，最后还要迭代各种我叫不出名字的算法……"
    "但这种算法……由于追求对声音的极致真实感"
    "需要很多不同情绪，音调高低，语速快慢与人声中细枝末节的要素，给予相应的标签来不断更新学习目标……"
    # （去掉黑幕遮盖）
    hide thinking with Dissolve(0.2)
    cq size2 a3 smile "还有这一本，上面附带的漫画看起来也很适合我欸！"
    ch  "嗯嗯……可以的……"
    # （屏幕加上黑幕遮盖，增加内心思考的那种氛围感）
    show thinking with Dissolve(0.2)
    "换句话说，初咲标准的日语是基于日本传统的CV声线的录音，采集了大量同一声线的样本而生成的结果"
    "其实仔细思考了这么多，得出来的结论无非就是初咲需要一个中文老师来指导她完整的语音……"
    "书籍只是次要的……更重要的是要有人能对每一个中文发音进行严格而且专业的指导……"
    # （去掉黑幕遮盖）
    hide thinking with Dissolve(0.2)
    cq size2 a2 serious "主人~！"
    cq "你根本就没有听我说话嘛！"
    ch  "…… ……"
    ch  "抱歉抱歉"
    ch  "刚刚在想到底该怎么样教初咲学习中文……"
    cq  "真是的！"
    cq  size2 a4 sad"明明是主人要带我来图书馆找书的……"
    cq  "还这样把别人晾在一边……"
    ch  "…… ……"
    
    "我完全没有料到初咲会说出这样的话……"
    "她微微涨红的脸，以及稍微撅起的小嘴……"
    "完完全全带给我一种和真实少女对话的感觉……"
    "只不过在现实中这样可爱的女孩子可以说是少之又少……"

    ch  "放心"
    ch  "来之前我就已经做好了功课"
    ch  "现在只用初咲找到那本我们需要的书就可以了"
    cq  size2 a3 happy"真的吗？！"
    cq  size2 a3 normal"所以那本书的名字是？"
    ch  "嗯……让我想想……"
    ch  "好像是叫做‘《跟加藤老师学中文》’来着……"
    cq  size2 a4 little_serious"唔……让我用我超级厉害的探测眼来仔细扫描一下！"
    ch  "应该就是在这附近的一本书……"
    $renpy.pause(2,hard=False)
    # （停顿5s左右？）
    cq  size2 a3 normal"嘿咻，嘿咻……找到了！"
    ch  "好快……"
    ch  "不愧是人工智能……"
    cq  size2 a4 little_serious"这个"
    "初咲把我刚才提到的那本书很精准地抓给我，然后用力地点了点头，似乎是对自己刚刚出乎我意料的表现非常满意"
    "我低头看了看初咲拿给我的这本书，果然标题上写着的是《跟加藤老师学中文》"
    ch  "谢谢"
    cq  size2 a3 happy"哼哼，我果然还是非常优秀的！"
    cq  size2 a3 smile"不过……能告诉初咲，主人为什么要选这本书吗？"
    ch  "这本书是吗？"
    ch  "因为它是从日语语法的角度来帮助初咲学习中文"
    ch  "也是我见过的专用来为母语是日语……"
    cq  "嗯嗯"
    cq  "果然，主人是一个考虑非常周到的人呢……"
    ch  "嘿嘿，也没有了……"
    ch  "对我来说，只是觉得初咲正处于进退两难的困境，我想要帮助初咲……"
    cq  "也真是个非常温柔的人呢……"
    ch  "……"
    cq  size2 a3 normal"那个……"
    cq  "我还能挑几本自己喜欢的中文书吗？"
    cq  size2 a3 wry_smile"我还想看看别的书……好像都很有趣的样子"
    ch  "当然没问题啊"
    ch  "初咲在图书馆里随便逛逛吧，遇到有什么喜欢的书都可以借走"
    ch  "喏，这是我的借书卡，"
    ch  "最多的话是同时借阅十本书噢，初咲自己看着挑选吧"
    cq  size2 a3 smile"没问题！"
    cq  "谢谢海川！"
    ch  "那我们等下就在门口汇合吧，我去查询一下别的分区的图书……"
    cq  size2 a3 happy"好！"
    hide cx size2 a3 happy with Dissolve(0.2)
    "很快，我就离开了图书馆三层的中文分区"
    stop music fadeout 1
    
    hide library inside with tran_lf
    show park afternoon with tran_lf
    $renpy.pause(2,hard=False)
    # （场景转换，转换到图书馆外部，中午时分，稍微停滞5s）
    "我匆匆从图书馆逃出来"
    "实际上并不是为了去搜罗别的栏目的书籍"
    "而是去见岩崎天桐"
    show bedroom
    show memory
    with dissolve
    # （这里插入暗黄色色调+
    # 电话
    voice "voice/yqtt_voice/episode1/岩崎(电)023.mp3"
    voice sustain
    yqcall "总之回见了，挚友！明天下午，老地方不见不散"
    hide bedroom
    hide memory
    with dissolve
    show cafe with dissolve
    # （背景转换，一个咖啡店内）
    "虽然岩崎是一名仿生机器人"
    "但对儿时的我来说，"
    "简直就是温柔大哥哥一般的存在"
    "我们一直是最好的“基友”，在高中时，我们约定了所谓的集合地点——"
    "也就是在九衢市图书馆附近的一个咖啡店，我和岩崎平常约在这里见面"
    "每当有很重要的事情发生的时候，我总会在这里向他征询意见……"
    "果不其然，在咖啡店的角落中我一下子就发现了那个熟悉的身影"
    play music "bgm/testbgm/BGM13.ogg"
    # 此处岩崎的音声由020开始
    show yq size1 a1 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    voice "voice/yqtt_voice/episode1/岩崎020.mp3"
    voice sustain
    yq  "哟，来得很早嘛！"
    voice "voice/yqtt_voice/episode1/岩崎021.mp3"
    voice sustain
    yq  "我早就在‘魔法书院’旁边的咖啡店等着你了，还以为你是找不到路了……"
    voice "voice/yqtt_voice/episode1/岩崎022.mp3"
    voice sustain
    yq  "看来还是记得我们的暗号的嘛！和主上大人说的那种‘脑子转不过来’的人还是有区别的……"
    ch  "喂喂，不是什么‘魔法书院’，是正经的图书馆啊拜托"
    ch  "还有，‘脑子转不过来’不是什么礼貌的打招呼方式……"
    ch  "别被蘭带偏了！"
    voice "voice/yqtt_voice/episode1/岩崎023.mp3"
    voice sustain
    yq size1 a1 smile "带偏？"
    voice "voice/yqtt_voice/episode1/岩崎024.mp3"
    voice sustain
    yq size3 a1 smile  "我倒是觉得，她是被我给带偏的……"
    voice "voice/yqtt_voice/episode1/岩崎025.mp3"
    voice sustain
    yq  "哈哈哈，好了好了，这是夸你记忆好的意思，赶快来聊正事吧。"
    ch  "……"
    ch  "好"
    voice "voice/yqtt_voice/episode1/岩崎026.mp3"
    voice sustain
    yq size3 a1 smile "欸等等……"
    voice "voice/yqtt_voice/episode1/岩崎027.mp3"
    voice sustain
    yq  "如果海川不喜欢这种氛围的话，换一个地方也是可以的"
    "我四下环视了一圈周围的环境，除了装潢有点显老之外好像挑不出什么瑕疵……"
    "据说这家店已经有五十多年的历史了，甚至是连老板都换了两轮……"
    "不过我同样很喜欢这种古朴的氛围，有一种说不出来的陌生的温馨感……"
    
    ch  "唔……也算不上是差吧"
    ch  "比起现在流行的无人咖啡店，这种有人打理的店面反而会显得与这个时代格格不入……"
    voice "voice/yqtt_voice/episode1/岩崎028.mp3"
    voice sustain
    yq size1 a1 smile "哦？"
    voice "voice/yqtt_voice/episode1/岩崎029.mp3"
    voice sustain
    yq  "这样吗……？"
    voice "voice/yqtt_voice/episode1/岩崎030.mp3"
    voice sustain
    yq  "我倒还蛮享受这种有人打理的感觉"
    voice "voice/yqtt_voice/episode1/岩崎031.mp3"
    voice sustain
    yq  "要我说……"
    voice "voice/yqtt_voice/episode1/岩崎032.mp3"
    voice sustain
    yq  "只有在这种充满魔力气息的地方……出现黑暗生物的概率才会显著增加……"
    ch  "……"
    ch  "不要在我即将进入何你好好谈话的状态的时候擅自进入中二模式啊！"
    voice "voice/yqtt_voice/episode1/岩崎033.mp3"
    voice sustain
    yq  "哈哈哈，抱歉抱歉……"
    ch  "我不介意环境什么的，直接开始吧"
    ch  "这次是因为‘初咲恋柚’的事情，我才会找到好兄弟你的"
    voice "voice/yqtt_voice/episode1/岩崎034.mp3"
    voice sustain
    yq size1 a1 serious "没错"
    ch  "那么就直接告诉我吧"
    ch  "初咲的来历"
    ch  "关于她的事情我一点都不知道"
    ch  "还有你们是怎么把我的事情一股脑都说给初咲啊……"
    ch  "让我把她带到日本是很有风险的事情，可不是闹着玩的！"
    voice "voice/yqtt_voice/episode1/岩崎035.mp3"
    voice sustain
    yq  size1 a1 smile"诶诶，你先别急，先冷静地听我把话说完"
    voice "voice/yqtt_voice/episode1/岩崎036.mp3"
    voice sustain
    yq  size1 a1 serious"这都不是我一个人的决定"
    voice "voice/yqtt_voice/episode1/岩崎037.mp3"
    voice sustain
    yq  "要说的话还是小蘭她自己安排好的"
    voice "voice/yqtt_voice/episode1/岩崎038.mp3"
    voice sustain
    yq  "我们和初咲恋柚不过也才认识几天"
    ch  "就算是这样也要提前给我打声招呼呀！"
    play sound "audio/cafe_chime.ogg"
    # （播放效果音：进店的那种风铃被拉响声）
    # 蘭的音声此处从094开始
    voice "voice/l_voice/episode1/蘭094.mp3"
    voice sustain
    l   "喂喂，我好像听见有人在议论我诶"
    hide yq size1 a1 serious
    show yq size1 a1 little_serious:
        xalign 0.1
        yalign 1.0
        zoom 1.3
    show lan size1 a3 normal:
        xalign 0.9
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    # （展示蘭的立绘在右侧，傲娇脸）
    ch  "……"
    ch  "怎么你也来了"
    ch  "不是说好了只有我们两个人"
    voice "voice/l_voice/episode1/蘭095.mp3"
    voice sustain
    l size1 a1 normal "我为什么不能在这里？"
    voice "voice/yqtt_voice/episode1/岩崎039.mp3"
    voice sustain
    yq size1 a1 smile "我也没说过只有两个人啊"
    ch  "…… ……"
    ch  "明明是找警察就可以解决的事情"
    voice "voice/l_voice/episode1/蘭096.mp3"
    voice sustain
    l size1 a3 mad "你傻啊！"
    voice "voice/l_voice/episode1/蘭097.mp3"
    voice sustain
    l size1 a1 serious "初咲这种型号的日式机器人，如果放任不管的话……"
    voice "voice/l_voice/episode1/蘭098.mp3"
    voice sustain
    l   "最后肯定会被九衢市上层给清除掉的！"
    ch  "但是她是日式型号，日式系统……"
    ch  "照理来说根本就不会违反三大定则……更不会有什么安全隐患"
    ch  "与其让我们这种学生冒着‘那种风险’，还不如交给大人来……"
    voice "voice/yqtt_voice/episode1/岩崎040.mp3"
    voice sustain
    yq size1 a1 serious "问题不是在违反‘三十二条禁令’上"
    voice "voice/yqtt_voice/episode1/岩崎041.mp3"
    voice sustain
    yq  "而是在于这种语言……"
    voice "voice/l_voice/episode1/蘭099.mp3"
    voice sustain
    l size1 a2 little_serious  "没错"
    voice "voice/l_voice/episode1/蘭100.mp3"
    voice sustain
    l   "无论初咲恋柚有没有对安稳的社会造成威胁"
    voice "voice/l_voice/episode1/蘭101.mp3"
    voice sustain
    l   "不同于本地的语言出现在robot的身上"
    voice "voice/l_voice/episode1/蘭102.mp3"
    voice sustain
    l   "和‘披着狼皮的羊’一样，没有区别的"
    ch  "…… ……"
    ch  "但是……"
    voice "voice/l_voice/episode1/蘭103.mp3"
    voice sustain
    l size1 a1 serious "你忍心看着她被送到大人那里，然后被随意处置吗？"
    ch  "可是……"
    voice "voice/l_voice/episode1/蘭104.mp3"
    voice sustain
    l size1 a3 mad  "机器人可不是物品！"
    voice "voice/l_voice/episode1/蘭105.mp3"
    voice sustain
    l   "他们也是有权利，有情感的智能！"
    "蘭用着略显不满的眼神盯着我，看上去对我极力推脱的表现很生气。"
    "但她很快意识到自己刚才的发言已经引起了周围顾客的各种注意"
    voice "voice/l_voice/episode1/蘭106.mp3"
    voice sustain
    l size1 a1 little_serious  "咳咳……我是太着急了一点"
    voice "voice/l_voice/episode1/蘭107.mp3"
    voice sustain
    l   "海川如果没有和robot呆过的话，应该是理解不了我的"
    ch  "robot……"

    "实际上在和初咲恋柚相处的这半天时间里"
    "已经完全让我忘记了自己是在和一个仿生机器人对话"
    "就好像是真的有感情的少女一样"
    "面前的岩崎也是这样"
    voice "voice/yqtt_voice/episode1/岩崎042.mp3"
    voice sustain
    yq size3 a1 normal "海川不是小蘭说的那种人了~"
    voice "voice/yqtt_voice/episode1/岩崎043.mp3"
    voice sustain
    yq size1 a1 proud "他和我一样，都是在黑夜中潜行的‘assassin’……除恶扬善的那种"
    ch  "不要用‘assassin’这种过度中二的词汇啊！"
    ch  "呃……其实我也没有放任不管……"
    ch  "我已经……"
    voice "voice/l_voice/episode1/蘭108.mp3"
    voice sustain
    l size1 a1 wry_smile"本小姐就知道海川不是那种冷漠的人"
    voice "voice/l_voice/episode1/蘭109.mp3"
    voice sustain
    l   "至少还是有点人情味的……"
    ch  "…… ……"
    ch  "利用交换生项目的漏洞通过海关是件很危险的事情！"
    ch  "至少把我说成是正能量的人物啊！"
    voice "voice/yqtt_voice/episode1/岩崎044.mp3"
    voice sustain
    yq size1 a1 smile "好了好了，海川也知道……主上大人说出这种话也算是对你的夸奖"
    voice "voice/yqtt_voice/episode1/岩崎045.mp3"
    voice sustain
    yq "我们其实知道了你已经考虑好要帮初咲了"
    voice "voice/yqtt_voice/episode1/岩崎046.mp3"
    voice sustain
    yq "喏……这是初咲早上发给我们的信息"
    ch  "原来这都是你们安排好的……"
    voice "voice/l_voice/episode1/蘭110.mp3"
    voice sustain
    l size2 a1 normal "那么现在到哪一步了？"
    voice "voice/l_voice/episode1/蘭111.mp3"
    voice sustain
    l size2 a3 normal "语言和铭牌对吧？"
    voice "voice/l_voice/episode1/蘭112.mp3"
    voice sustain
    l   "如果要把初咲顺利带到日本，这两个都是需要解决的问题"
    ch  "语言的话有点困难"
    ch  "蘭，你能来做初咲的指导吗？"
    voice "voice/l_voice/episode1/蘭113.mp3"
    voice sustain
    l size2 a2 normal "我？"
    ch  "没错，因为要让初咲彻底学会中文……需要一个中文标准的人来给初咲大量的语音样本……"
    ch  "现在的时间对我们来说已经非常紧急了"
    voice "voice/l_voice/episode1/蘭114.mp3"
    voice sustain
    l size2 a3 little_serious  "不对，"
    voice "voice/l_voice/episode1/蘭115.mp3"
    voice sustain
    l   "根本不需要这么麻烦"
    "蘭摇了摇头，然后拿出手机在浏览器上搜索着什么……然后把手机伸到我的面前"
    voice "voice/l_voice/episode1/蘭116.mp3"
    voice sustain
    l size2 a4 normal "喏，你看"
    "上面展示的是各种通过海关会询问仿生机器人的问题"
    voice "voice/l_voice/episode1/蘭117.mp3"
    voice sustain
    l   "只要学会过海关时需要用的中文就足够了"
    voice "voice/l_voice/episode1/蘭118.mp3"
    voice sustain
    l size2 a4 smile "完全没有必要学会全部中文嘛"
    ch  "……"
    ch  "很有道理诶！"
    voice "voice/l_voice/episode1/蘭119.mp3"
    voice sustain
    l size1 a3 proud  "让我来做中文的专业指导也是完全没有问题的哟！"


    "在一瞬间，蘭的话打开了我全部的思路"
    "原来很多问题都被我想复杂了……"
    voice "voice/yqtt_voice/episode1/岩崎047.mp3"
    voice sustain
    yq size1 a1 smile "如果是更改铭片的话我们也有办法"
    voice "voice/yqtt_voice/episode1/岩崎048.mp3"
    voice sustain
    yq  "之前主上大人带着我去过一家‘九衢市传说中的最强隐藏修理铺’"
    voice "voice/yqtt_voice/episode1/岩崎049.mp3"
    voice sustain
    yq  "在那个地方，几乎所有机器人的问题都能解决"
    ch  "那不就算是黑市了吗……"
    voice "voice/l_voice/episode1/蘭120.mp3"
    voice sustain
    l size2 a1 smile "不完全是"
    voice "voice/l_voice/episode1/蘭121.mp3"
    voice sustain
    l   "据说这家店的老板是原来从‘高塔’里退隐的总工程师"
    voice "voice/l_voice/episode1/蘭122.mp3"
    voice sustain
    l   "每次岩崎出现问题在那里都可以得到解决"
    ch  "这样啊……"
    ch  "那具体的地址是在？"
    voice "voice/yqtt_voice/episode1/岩崎050.mp3"
    voice sustain
    yq size3 a1 normal "九衢市九山区1037号，森林公园旁边的一家小铺"
    voice "voice/yqtt_voice/episode1/岩崎051.mp3"
    voice sustain
    yq size3 a1 smile  "哼哼，一般人我可是不告诉他‘秘密基地’的位置"
    ch  "九山区……那种地方？"
    ch  "离市中心这么远的地方？？？"
    voice "voice/yqtt_voice/episode1/岩崎052.mp3"
    voice sustain
    yq size1 a1 proud "不会吧，不会吧？"
    voice "voice/yqtt_voice/episode1/岩崎053.mp3"
    voice sustain
    yq  "海川的思维不会还停在‘九昌’，‘九口’，‘九阳’三区为中心的上世纪思维吧？"
    voice "voice/yqtt_voice/episode1/岩崎054.mp3"
    voice sustain
    yq  "时代已经变了……"
    ch  "…… ……"
    voice "voice/yqtt_voice/episode1/岩崎055.mp3"
    voice sustain
    yq size1 a1 smile"总之,只要你去了就肯定知道了"
    voice "voice/yqtt_voice/episode1/岩崎056.mp3"
    voice sustain
    yq  "‘九衢市传说中的最强隐藏修理铺’的称号可不是白叫的！"
    voice "voice/l_voice/episode1/蘭123.mp3"
    voice sustain
    l size1 a3 mad  "够了……"
    voice "voice/l_voice/episode1/蘭124.mp3"
    voice sustain
    l   "别在一口一个‘最强’，‘最强’的了，简直和那个老板一样‘中二’"
    voice "voice/l_voice/episode1/蘭125.mp3"
    voice sustain
    l size1 a3 little_serious  "隔壁桌一直都在看着我们呢……"
    voice "voice/yqtt_voice/episode1/岩崎057.mp3"
    voice sustain
    yq size1 a1 smile "害呀，我知道了"
    voice "voice/yqtt_voice/episode1/岩崎058.mp3"
    voice sustain
    yq  "反正海川一定要记住"
    voice "voice/yqtt_voice/episode1/岩崎059.mp3"
    voice sustain
    yq  "这个小店确实是叫这个名字"
    ch  "？？？"
    voice "voice/yqtt_voice/episode1/岩崎060.mp3"
    voice sustain
    yq  "喊错名字会让老板很不高兴的"
    ch  "……"
    ch  "我知道了"
    voice "voice/l_voice/episode1/蘭126.mp3"
    voice sustain
    l size2 a2 smile  "呼，那今天就到这里吧"
    voice "voice/l_voice/episode1/蘭127.mp3"
    voice sustain
    l  "本小姐还要去负责琴台剧院的冬季表演的剧本编审"
    voice "voice/l_voice/episode1/蘭128.mp3"
    voice sustain
    l   "没有时间和你们在这里坐下来细说了"
    ch  "所以你是因为自己的事情才把初咲丢给我的吧！"
    ch  "…… ……"
    voice "voice/l_voice/episode1/蘭129.mp3"
    voice sustain
    l size2 a2 normal  "才不是！"
    voice "voice/l_voice/episode1/蘭130.mp3"
    voice sustain
    l   "这件事，估计整个九衢市只有你能帮到她了"
    voice "voice/l_voice/episode1/蘭131.mp3"
    voice sustain
    l   "我走了，后续有事再联系"
    hide lan size2 a2 normal 
    hide yq size1 a1 smile 
    with Dissolve(0.2)
    show yq size1 a1 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with Dissolve(0.2)
    play sound "audio/cafe_chime.ogg"
    # （播放效果音：出店的那种风铃被拉响声，蘭的立绘消失）
    voice "voice/yqtt_voice/episode1/岩崎061.mp3"
    voice sustain
    yq size1 a1 little_serious "凭借交换生项目便利的优势渡过海关也确实只有海川了"
    voice "voice/yqtt_voice/episode1/岩崎062.mp3"
    voice sustain
    yq  "蘭要带着我，没办法再额外携带一个初咲了"
    voice "voice/yqtt_voice/episode1/岩崎063.mp3"
    voice sustain
    yq  "本来她真的很想帮忙……"
    ch  "我大概也知道的"
    ch  "作为她的青梅竹马，我也知道她是那种很热心的女生……不然也不会找到我来一起帮忙了"
    voice "voice/yqtt_voice/episode1/岩崎064.mp3"
    voice sustain
    yq size1 a1 smile "海川理解就好"
    voice "voice/yqtt_voice/episode1/岩崎065.mp3"
    voice sustain
    yq  "那我也先行告辞了"
    voice "voice/yqtt_voice/episode1/岩崎066.mp3"
    voice sustain
    yq  "主上大人的家也只能靠我来收拾打理了"
    "说完，岩崎还不忘对我苦笑一下"
    play sound "audio/cafe_chime.ogg"
    # （播放效果音：出店的那种风铃被拉响声，岩崎的立绘消失）
    hide yq size1 a1 smile with Dissolve(0.2)
    stop music fadeout 1
    "看上去，把初咲恋柚带回日本这个任务也没有想象中那样复杂棘手"
    "我慢慢品尝着杯中已经冷却了的咖啡，一边寻思着之后的事情……"
    "从玻璃窗外看过去，街上的几乎没有几个人，大部分是穿着工作制服在匆匆赶路的"
    "冷清的背景看上去也只有远处“高塔”的闪光能够稍微点缀一下"
    "我的目光很快就被锁定在远处的那座高楼上了"
    "它是那样的显眼……"
    play music "bgm/testbgm/BGM23.ogg"
    voice "voice/aqxs_voice/episode1/先生1.mp3"
    voice sustain
    who "小伙子，在想什么呢？"
    "一位看上去稍显年迈的大叔不知道什么时候坐到了我的对面"

    # （镜头平行移动，在咖啡店内景中的桌子上放大滑过去，最后落脚落在1/2视图，单点放大回原比例视图）

    "慈祥的神情和温柔宽厚的声音……"
    voice "voice/aqxs_voice/episode1/先生2.mp3"
    voice sustain
    who "是不是忘记我了？"
    ch  "怎么可能会忘记！"
    "从小学就与这家店结下深厚情结的我，自然不会忘记咖啡店上一任老板的声音和模样"
    "他是一个愿意倾听我的烦恼和心事的大叔"

    "每当我不愿意把一些烦心事告诉岩崎的时候，我都会向这位自称是“阿泉先生”的老板倾诉"
    voice "voice/aqxs_voice/episode1/先生3.mp3"
    voice sustain
    mrquan    "上次来我记得是因为学业的事情，诶，听说你好像是被日本那个‘目黑川’那所排名不错的大学录取了……"
    ch      "嗯是的，还是有一点运气的成分……"
    voice "voice/aqxs_voice/episode1/先生4.mp3"
    voice sustain
    mrquan    "哈哈哈恭喜啊，不愧是高材生！"
    voice "voice/aqxs_voice/episode1/先生5.mp3"
    voice sustain
    mrquan    "最近是发生了什么不高兴的事情吗，看你愁眉苦脸的"
    ch      "确实，最近被一些事情困扰到了"
    voice "voice/aqxs_voice/episode1/先生6.mp3"
    voice sustain
    mrquan    "啊……那这次肯定不是因为学业的事情了吧……不妨说来听听？"
    ch      "比如说……"
    ch      "我有一个朋友，要冒着承担一定法规的风险去做一些事……"
    ch      "虽然他很想帮忙"
    ch      "但因为他不了解帮助的这个对象……"
    ch      "因为只是刚刚认识，他也担心自己会因此连累到很多东西……"
    voice "voice/aqxs_voice/episode1/先生7.mp3"
    voice sustain
    mrquan    "我知道了"
    voice "voice/aqxs_voice/episode1/先生8.mp3"
    voice sustain
    mrquan    "你的这个朋友大概也是陷入到和我当初一样的处境了……"
    voice "voice/aqxs_voice/episode1/先生9.mp3"
    voice sustain
    mrquan    "在给出答案之前，一定不要因为只是看了一眼就拍脑袋做决定……"
    voice "voice/aqxs_voice/episode1/先生10.mp3"
    voice sustain
    mrquan    "如果说再给我一次机会的话，当初我也不会一开始听从父母的话吧……"
    
    "阿泉先生好像是陷入到了自己的回忆中，但很快又用坚定的目光看向我"
    voice "voice/aqxs_voice/episode1/先生11.mp3"
    voice sustain
    mrquan    "如果时间允许的情况下……我建议还是和那个‘要帮助的对象’多多接触……"
    voice "voice/aqxs_voice/episode1/先生12.mp3"
    voice sustain
    mrquan    "不然草草决定‘帮助’和‘不帮助’都是很不明智的选择啊"
    ch      "我大概明白了，也就是说……‘多多接触’"
    voice "voice/aqxs_voice/episode1/先生13.mp3"
    voice sustain
    mrquan    "没错！"
    voice "voice/aqxs_voice/episode1/先生14.mp3"
    voice sustain
    mrquan    "除此之外，‘帮助’也是相互的"
    ch      "‘相互的’？"
    ch      "这是什么意思啊？"
    voice "voice/aqxs_voice/episode1/先生15.mp3"
    voice sustain
    mrquan    "你也要让对方感受到是对你有用的"
    voice "voice/aqxs_voice/episode1/先生16.mp3"
    voice sustain
    mrquan    "或者换句话说，"
    voice "voice/aqxs_voice/episode1/先生17.mp3"
    voice sustain
    mrquan    "‘相互付出’——无论是热恋中的情人，相谈甚欢的友人，又或者说关系没那么紧密的同事关系"
    voice "voice/aqxs_voice/episode1/先生18.mp3"
    voice sustain
    mrquan    "这就是让人与人的关系融洽而稳定的秘诀啊"
    ch      "原来如此……"
    voice "voice/aqxs_voice/episode1/先生19.mp3"
    voice sustain
    mrquan    "只有这样才会让彼此肯定对方的价值"
    ch      "谢谢你，阿泉先生"
    ch      "我大概明白了"
    voice "voice/aqxs_voice/episode1/先生20.mp3"
    voice sustain
    mrquan    "害，谢什么谢啊，只不过是我的一些人生经验而已了。"

    "阿泉先生向我投来温暖的笑容，然后随即盯着洒在茶桌上的夕阳，拿出方巾优雅地擦着摆在桌子上的杯具。"
    voice "voice/aqxs_voice/episode1/先生21.mp3"
    voice sustain
    mrquan    "看来时间也不早了啊……‘你的朋友’应该也和很重要的人有约吧？"
    ch      "嗯嗯"
    ch      "还有……"
    ch      "这大概是我最后一次来这个咖啡店了……下次来就是在那边毕业之后了……"
    ch      "真的很谢谢你，阿泉先生！"
    voice "voice/aqxs_voice/episode1/先生22.mp3"
    voice sustain
    mrquan    "哈哈，不用谢"
    voice "voice/aqxs_voice/episode1/先生23.mp3"
    voice sustain
    mrquan    "好好去国外念书去吧，高材生。我一直都会在这里的"
    ch      "嗯嗯，再见了，阿泉先生！"
    voice "voice/aqxs_voice/episode1/先生24.mp3"
    voice sustain
    mrquan    "欢迎下次光临。"
    stop music fadeout 3

    "不知不觉间，已经到了下午太阳快要落山的时候了"
    "我低头看了看时间，上面赫然写着的是“17：25”"
    "糟了……原来不知不觉已经花了这么多时间，还是先回到图书馆和初咲汇合吧"
    play sound "audio/cafe_chime.ogg"
    scene black with tran_lf
    show library day with tran_lf
    # （播放效果音：出店的那种风铃被拉响声，场景转换到咖啡店外，然后再转换到图书馆外侧，下午夕阳，在转换到图书馆的书架处）

    "以三步化作一步的速度，在图书馆里兜兜转转了好一会儿，我才勉强赶在17：45看到了那个熟悉的身影"
    # （出现初咲的立绘，撅嘴立绘）
    hide library day with tran_lf
    show library inside with tran_lf
    show cx size2 a2 serious:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    with Dissolve(0.2)
    play music "bgm/testbgm/BGM14.ogg"
    "18：00要闭馆了……"
    "不过好在我及时地赶到了初咲的身边"
    cq  "唔……"
    cq size2 a3 happy "诶？！是主人耶！"
    "在看到我之后，初咲一蹦一跳地来到了我的身边"
    cq size2 a4 sad "我真的等了好久好久……我还以为是主人不需要初咲了……"
    ch  "怎么可能呢"
    ch  "忽然想起来今天还要做晚饭，所以刚刚去买了点菜……"
    "我指了指身后的书包，试图瞒过初咲，让她知道我没有骗她。"
    cq size2 a4 little_serious "唔……果然是这样呢"
    cq  "通过我的智能扫描眼完全可以看得一清二楚噢……书包里的东西"
    ch  "诶？？！"
    ch  "原来还可以穿透看到里层吗……未免也太先进了一点吧……"
    cq size2 a3 smile "哼哼，这对我来说就是轻而易举的事情噢"
    ch  "幸好刚才买了一点蔬菜放在书包里……不然还真会露馅"
    # （此处为类似于广播里播放的录音：）

    libaryanounce   "亲爱的读者朋友，本馆将于18：00准时闭馆，请收拾好随身携带的物品，按时离馆，谢谢！"


    "九衢市图书馆闭馆的广播声音突然响起来，我低头看了看时间，只有十分钟了……"
    ch  "快走吧，再待一会儿就要闭馆了"
    cq  "好。"
    "我一边抓起初咲恋柚的手，一边把她挑选的书在借阅的机器上全部扫上。"
    "随着图书馆里出口的指示，我们很快地离开了"

    #（延时3s，场景转换：来到图书馆外）
    scene black with tran_lf
    show park afternoon with tran_lf
    ch  "呼呼……"
    "在闭馆之前，我和初咲勉强赶在了闭门之前跑了出来"
    "我不经意地回头看了一下被我拉着跑的初咲"
    "此时她也正盯着我的手发呆，好像在若有所思着什么"
    show cx size2 a3 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    with Dissolve(0.2)
    ch  "你怎么了？"
    cq size2 a3 smile "原来如此"
    cq  "主人的手好温暖……"
    ch  "？你在说什么……"
    ch  "！"
    "几乎是毫无意识之间，我刚刚因为太过着急，不经意地牵起了初咲的手"
    
    # （展现初咲的立绘）
    "我很快把手抽出来，余光中我可以初咲的脸有一点点微红"
    "虽然是机器人……但是……"
    ch  "抱歉……"
    cq size2 a3 normal "唔呣？"
    cq  "主人为什么要道歉啊？"
    "初咲目不转睛地盯着我的眼睛，和她对视过程中，我还是下意识把眼神瞟向了别处……"
    cq size2 a3 happy "哼哼，我知道了！"
    cq size2 a3 smile "主人肯定是还没有碰过女孩子的手吧？"
    ch  "喂喂，不要胡乱猜测啊！"
    cq  "果然被我猜对了！"
    cq  "很轻松地拿下了海川的第一次呢~"
    ch  "……"
    ch  "咳咳，我们还是赶快回家吧，天色也不早了"
    cq size2 a3 happy "好的！"

    # （场景转换，来到公园，再来到九衢长街，再返回到家门口，背景显示时间为黄昏或者晚上/或者这里加转场动画）
    scene black with tran_lf
    show street afternoon with tran_lf
    hide street afternoon with tran_lf
    show livingroom afternoon with tran_lf
    show cx size2 a3 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    with Dissolve(0.2)
    ch  "好了，你现在可以放开声音说话了"
    cq size2 a3 happy "那么……我回来了！"
    cq size2 a3 smile "今天就让我来给主人做可口的晚饭吧"
    "初咲把袖子撸了起来，看上去干劲满满的样子"
    ch  "那个……"
    "习惯了做这些事的我本来想拒绝初咲的主动申请"
    "但是……"
    show cafe
    show memory
    with dissolve
    # （昏黄色调+
    mrquan    "‘相互付出’——无论是在热恋中的情人，相谈甚欢的友人，又或者说关系没那么紧密的同事"
    mrquan    "这就是让人与人的关系融洽而稳定的秘诀啊"
    hide cafe 
    hide memory
    with dissolve
    ch  "那今天就先暂时交给你吧"
    cq  "还有家务活，也一起交给我来做吧！"
    # （这里是初咲微笑的立绘）

    ch  "没问题，姑且看看你的表现吧……"
    cq size2 a3 happy "好的！"
    "大概……以仿生机器人的性能，应该会和人所差无几甚至更好吧……"
    hide cx size2 a3 happy with Dissolve(0.2)
    scene black with tran_lf
    show bedroom with tran_lf
    # （初咲立绘消失，转到男主房间的场景，晚上）
    "我坐在电脑桌旁的椅子上，开始继续搜寻相关的资料"
    ch  "首先是岩崎说的那家‘黑店’……"
    "虽然说不怎么爱出门的我几乎完全不了解九山区的状况"
    "不过很快我还是在网上定位到了那家店铺……"
    ch"‘九衢市传说中的最强隐藏修理铺’"
    "出乎我的意料……这家店的名字好像真是这个……"
    "这个世界到底是怎么回事啊……"
    stop music fadeout 1
    show cx size2 a2 serious:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    with Dissolve(0.2)
    # （播放效果音："咚咚咚"，很急促地踩踏木质地板的声音）

    cq  "主人……大事不好了！"
    "初咲一把把我的房间门推开，从她慌张的脸色上我似乎预感到有些不好的事情已经发生了……"
    ch  "发生什么了？没事吧？"
    cq size2 a4 little_serious "厨房里……"
    cq  "不小心起火了……"
    ch  "……!"
    ch  "没事的！"
    "我马上抱起旁边的水桶向房间外冲去"
    "虽然嘴上说着“没事”用来安慰初咲，但是我内心已经做好了最坏的打算……"
    hide cx size2 a4 little_serious with Dissolve(0.2)
    hide bedroom with tran_lf
    show livingroom night with tran_lf
    # （场景转换，来到客厅的场景，晚上）

    "房间里没有我预想中明亮的焰火，也没有刺鼻的烧焦味"
    ch  "哪里着火了？"
    "我转头看向初咲，用着几近最大的音量向初咲问道"
    "可是眼前的初咲有些不慌不忙，慢悠悠地走到我的面前"
    play music "bgm/testbgm/BGM17.ogg"
    show cx size2 a3 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    with Dissolve(0.2)
    cq "开个玩笑哦~"
    ch  "……"
    cq size2 a3 happy "哼哼……被我的演出惊艳到了吧？"
    ch  "我说，这种玩笑就真的很过分了！"
    ch  "……"
    cq size2 a3 surprised "阿勒？"
    "可能是察觉到了我的一些怒气，初咲把头低得死死的，就像一个闯了大祸认错的小孩一样"
    cq size2 a4 sad "抱歉……我真的很喜欢表演……我不是故意的"
    "虽然……"
    "对我来说，这个玩笑真的有些过头……"
    "但是每次在看到初咲可怜巴巴的模样后，让我根本生气不起来……"

    cq size2 a3 smile "不过晚饭我已经做好了哦！"
    ch  "…… ……"
    cq size2 a4 sad "主人……不会还在生初咲的气吧？"
    ch  "算了算了"
    ch  "虽然对机器人来说……真的是非常惊人的表演能力……"
    cq size2 a3 happy "真的吗？！谢谢海川的夸奖！"
    cq size2 a3 smile "总之，先来看看我的手艺吧！"
    ch  "好"
    stop music fadeout 1
    # （此处的镜头从右往左移动，图片纵轴比例缩小为三分之一，缓缓移动）
    "我坐在餐桌前，想起来已经一个月没有和别人一起吃饭过了……"
    "这种简单的日式风味的菜肴，看上去对我非常有吸引力……"
    "我夹起一点青菜，往嘴里送去，开始慢慢咀嚼了起来"
    cq  "味道怎么样？"
    ch  "…… ……"
    ch  "很不错欸！"
    "清爽的蔬菜香味伴着似乎是用醋和酱油勾兑成的酸脆口感在一瞬间从嘴里迸发出来"
    "不得不说，这种口感比我自制的蔬菜沙拉要好好多倍……这种厨艺比我预想中的要好上不少"
    cq size2 a3 happy "太好了……我还担心主人不会喜欢的……"
    cq size2 a3 smile "那……没什么事的话我就去打扫咯"
    ch  "去吧"
    hide cx size2 a3 smile with Dissolve(0.2)
    # （初咲立绘消失）
    "虽然很让我烦心……"
    "但这种依赖和被依赖的感觉好像也很不错……"
    "正如阿泉先生说的那样……"
    scene black with tran_lf
    show bedroom with tran_lf
    play music "bgm/testbgm/BGM09.ogg"
    # （场景转换，转到房间里，晚上）

    # 海川在洗完澡并给初咲冲上电后，我来到房间里
    # （播放效果音（也可以不放）："噗"，倒在柔软的床上的声音）

    # （场景转换：转换到房间天花板的灯上）

    "在和初咲恋柚相处的这短短的两天中，我感觉我的日语水平从最开始勉强达到考试标准正逐渐进步"
    "从最开始的完全跟不上，到现在我已经基本上能听得懂初咲恋柚的大部分日语了"
    # （昏黄滤镜+
    show bedroom day
    show cx size2 a3 normal:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    show memory
    with dissolve
    
    cq  "因为在线翻译器也只能告诉初咲一个翻译的结果和人工读音"
    hide bedroom day
    hide memory
    hide cx size2 a3 normal
    with dissolve
    "那如果让初咲说出中文的话……会不会很奇怪呢……"
    "虽然到目前为止，我还并没有完全了解初咲恋柚的身世"
    "包括她的主人，她的由来，她的一切一切……"
    "对初咲来说，我到底是个怎样的存在呢……？"
    scene black with close_eyes
    # （屏幕一黑，转到第二天早上白天，背景为房间）
    show bedroom day with open_eyes
    ch"竟然这样就昏昏沉沉地睡了过去……"
    show cx size2 a3 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    with Dissolve(0.2) 
    ch  "早上好啊，初咲！"
    cq  "早上好~主人"
    "眼前的少女正一边打着哈欠，一边朝我无力地招了招手，"
    ch  "原来充电睡觉都可以拟合地这么真吗，不愧是laser精工……"
    "我端起刚泡好的茶，微微地抿了一口，然后看向窗外的风景"

    # （此处背景由背景客厅左侧缓缓移到右侧，注意要凸显出背景中的高塔）

    ch  "初咲最近联系上了自己的主人吗？"
    cq size2 a3 normal "原本的主人……呃……"
    cq  "好像一直都没什么进展"
    ch  "试过打电话给原先的主人吗？"
    cq  "是"
    ch  "看起来效果也不是很好……"
    cq  "是"
    ch  "从今天早上开始我们要学习中文了"
    cq  "是"
    # （表情转换，从自然到惊愕）
    cq size2 a3 surprised "诶？？？这么快吗？？！"
    ch  "没错，现在留给我们的时间也不多了"
    cq size2 a4 sad "这样啊……"
    cq size2 a3 smile "那我们开始吧！"
    ch  "好！"

    # （黑幕背景转场，背景不变，黑屏幕上显示经过1个小时的白色字幕"一个小时之后…… ……"）

    ch  "这个短语是念作‘谢谢你’"
    ch  "跟着我一起读"
    cq size2 a3 normal "唔……"
    cq  "谢谢你！"
    cq size2 a3 wry_smile "诶……！这样的说话方式好害羞……"
    ch  "已经很不错了！"
    cq size2 a3 surprised "真的吗！？"
    ch  "嗯！"
    ch  "还有这句话，要不你试着读一下？"
    cq size2 a3 smile "这句吗……‘幸福’，‘未来’，‘爱’"
    ch  "对，这个初咲一定要记好了。"
    ch  "可以说，这三个词是海关肯定会考验每个人的问题"
    cq size2 a3 normal "原来如此. . 不过要说的话我还是很了解这三个词的"
    cq  "日语读作：‘幸福’，‘未来’，‘恋爱’"
    "听着初咲的日语，我总感觉有些不对劲……"
    ch  "等等，初咲好像说的是‘恋爱’吧……"
    ch  "要记住这里是‘爱’，不是‘恋爱’"
    cq  "唔……"
    ch  "而且……‘恋爱’的日语读音也不是re na i这种平假名的组合吧"
    cq size2 a2 serious "不对哦！完全不对！"
    cq size2 a4 little_serious "应该读‘re na i’噢！"
    cq  "‘re’是一个英文中的词根，有着‘重新’，‘再次’的意思"
    cq  "‘na i’也是取自英文，有着‘出生’，‘生来的’的意思"
    cq  "字面意思就是‘复生’"
    ch  "…… ……"
    ch  "喂喂，这个词和‘复生’的意思相去甚远啊！"
    cq  size2 a2 normal"唔……"
    cq  "难道不是‘死了之后又可以活过来’的意思吗？"
    ch  "…… ……"
    ch  "联合国怎么可能用这样奇怪的词汇来作为新时代的口号啊"
    ch  "要记好了，是读‘re n ai’"
    ch  "而且‘爱’的意思是……"
    
    
    # （停顿几秒）
    cq  "唔……"
    "一瞬之间，我不知道该用什么言语来解释这个词"
    "本来“爱”这个词的意义和用法就很宽泛……"
    ch  "总之"
    ch"以后不要再读错就行了"
    # （此处切初咲的笑脸）
    "虽然平心而论……要让这种程度的中文水平通过海关还远远不够……"
    "不过照这种超智能型的仿生机器人的学习速度来看，应该会比我预想中的进度快很多……"
    ch  "那今天的中文学习就先到此为止吧"
    cq size2 a3 happy "好的！"

    # （此时转变为笑脸，如果要单点跳过，延迟2s，并采用Q版动画方式转场，转变为黄昏时分的客厅场景。画面慢慢从左往右平移，注意多次调用停留时间参数）
    scene black with dissolve
    $renpy.pause(2,hard=False)
    "这样算起来，初咲住在我的家里已经将近两个月……明天就是飞往东京的日子了"
    "但在这之前，还有一个很重要的事情需要我来决断"
    "那就是铭牌……"
    show cafe
    show yq size3 a1 normal:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    show memory
    with dissolve

    # （这里插入暗黄色色调+九衢の街背景
    voice "voice/yqtt_voice/episode1/岩崎067.mp3"
    voice sustain
    yq  "九衢市九山区1037号森林公园旁有一家小铺"
    voice "voice/yqtt_voice/episode1/岩崎068.mp3"
    voice sustain
    yq size3 a1 smile "哼哼，一般人我可是不告诉的"
    ch  "九山区……那种地方？"
    ch  "离市中心这么远的地方？？？"
    voice "voice/yqtt_voice/episode1/岩崎069.mp3"
    voice sustain
    yq size1 a1 proud "不会吧，不会吧？"
    voice "voice/yqtt_voice/episode1/岩崎070.mp3"
    voice sustain
    yq  "海川的思维不会还停在‘九昌’，‘九口’，‘九阳’三区为中心的上世纪思维吧？"
    voice "voice/yqtt_voice/episode1/岩崎071.mp3"
    voice sustain
    yq  "时代已经变了……"
    ch  "…… ……"
    voice "voice/yqtt_voice/episode1/岩崎072.mp3"
    voice sustain
    yq size1 a1 smile "总之,只要你去了就肯定知道了"
    voice "voice/yqtt_voice/episode1/岩崎073.mp3"
    voice sustain
    yq  "‘九衢市最强隐藏修理铺’的称号可不是白叫的！"
    
    scene black with tran_lf
    show store 
    show cx size2 a3 normal:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    show memory
    with tran_lf
    # （黑幕转场，这里插入暗黄色色调+修理小铺背景，画面是不全的画面，被缩小到中心了
    "一个半月前的这个时候，我已经和初咲来到了yq提到的所谓“九衢市的最强隐藏修理铺”"
    # （场景放大，强制将放大的画面停留2s）

    ch  "老板？"
    ch  "有人在吗？"
    "站在这家店的门口，我也完全感受不到这是岩崎所说的“九衢市的最强隐藏修理铺”的那种感觉……"
    "被本地的住户带到的这间店铺，完全没有我想象中的气派……"
    ch  "这种事看来还是得去稍微知名点的‘珞珈作坊’，毕竟也算得上是个老字号了"

    cq  "不过看资料上说那里的风评不太好诶……"
    
    # （播放效果音：铁门哐当哐当打开的声音）
    voice "voice/qsf_voice/episode1/秋师父001.mp3"
    voice sustain
    who "谁啊？"
    voice "voice/qsf_voice/episode1/秋师父002.mp3"
    voice sustain
    who "不要总是拿‘珞珈作坊’来对比啊，在我看就是一个黑店"
    voice "voice/qsf_voice/episode1/秋师父003.mp3"
    voice sustain
    who "要货真价实的技术还是得来我这里"
    "随着面前锈迹斑斑的铁门应声打开，一股潮湿发霉的难闻气味铺面而来"
    ch  "咳咳……"
    "夹杂着一点腐臭味的灰尘冲进我的鼻腔中，这种味道真的很让我窒息……"
    "满地堆放的零件……随意放在地上的电脑和各种传感器……以及一些我叫不出名字的设备和器材……"
    ch  "您好……"
    ch  "请问这里是‘九衢市的最强隐藏修理铺’吗？"
    "好中二的名字……"
    voice "voice/qsf_voice/episode1/秋师父004.mp3"
    voice sustain
    who "是的，"
    voice "voice/qsf_voice/episode1/秋师父005.mp3"
    voice sustain
    who "我姓秋，你也可以喊我秋师傅"
    "迎面而来的秋师傅是一个满脸胡须，看上去非常邋遢的，完全不修边幅的中年男士"
    voice "voice/qsf_voice/episode1/秋师父006.mp3"
    voice sustain
    mrqiu   "是要换语言包？换核心？还是敲掉？"
    cq size2 a3 surprised "唔！"
    cq  "敲掉是什么意思？！"
    voice "voice/qsf_voice/episode1/秋师父007.mp3"
    voice sustain
    mrqiu   "这么看起来，你就是装了日式系统的仿生机器人了"
    cq size2 a3 normal "是的！"
    voice "voice/qsf_voice/episode1/秋师父008.mp3"
    voice sustain
    mrqiu   "我听不懂日语……看来现在说话得小心了"
    "这位叫“秋师傅”的维修师傅扫了我一眼，然后开始在地上打理着各种元件，看上去是在整理每个零件和设备的位置"
    ch  "就是……想问下能不能把她的铭牌从‘JAPAN’型的换成‘CHINA’型的……"
    "秋师傅上下打量着初咲恋柚，然后又用斜睨的目光很快地瞟了一眼我"
    voice "voice/qsf_voice/episode1/秋师父009.mp3"
    voice sustain
    mrqiu   "小伙子，你知道这是有可能违法的事吗？"
    ch  "啊？"
    voice "voice/qsf_voice/episode1/秋师父010.mp3"
    voice sustain
    mrqiu   "本来日式系统在这边就是不被允许的存在……更何况现在你要改她的铭牌"
    voice "voice/qsf_voice/episode1/秋师父011.mp3"
    voice sustain
    mrqiu   "这要是被发现了，可就是二重罪了"
    ch  "可是……"

    ch  "‘三十二条禁令’中不是只规定了不允许中文机身搭载日语系统吗？"
    ch  "初咲恋柚本身就是日式机身，日式系统。"
    ch  "完完全全不会出现系统和机身不匹配而产生的‘bug’"
    ch  "所以说改动铭牌的话……"
    cq size2 a4 little_serious "是的！"
    cq  "我是完全遵照着准则来的噢！非常优秀且安全的机器人！"
    hide cx size2 a4 little_serious with Dissolve(0.2)
    voice "voice/qsf_voice/episode1/秋师父012.mp3"
    voice sustain
    mrqiu   "哎，"
    voice "voice/qsf_voice/episode1/秋师父013.mp3"
    voice sustain
    mrqiu   "看样子，你现在是成年人了对吧"
    ch  "嗯，刚好成年"
    voice "voice/qsf_voice/episode1/秋师父014.mp3"
    voice sustain
    mrqiu   "那你应该明白这个道理"
    voice "voice/qsf_voice/episode1/秋师父015.mp3"
    voice sustain
    mrqiu   "就算从根本上是正确的事情，"
    voice "voice/qsf_voice/episode1/秋师父016.mp3"
    voice sustain
    mrqiu   "只要表现出来是错的"
    voice "voice/qsf_voice/episode1/秋师父017.mp3"
    voice sustain
    mrqiu   "那就是错的"
    ch  "道理也不能这么说吧……"
    voice "voice/qsf_voice/episode1/秋师父018.mp3"
    voice sustain
    mrqiu   "本来，做出的每一个选择都不是你自己说的算"
    voice "voice/qsf_voice/episode1/秋师父019.mp3"
    voice sustain
    mrqiu   "而是你自以为的价值和意义，遭到不可抗力因素时"
    voice "voice/qsf_voice/episode1/秋师父020.mp3"
    voice sustain
    mrqiu   "会瞬间崩塌瓦解"
    voice "voice/qsf_voice/episode1/秋师父021.mp3"
    voice sustain
    mrqiu   "那个时候，也没有人会愿意从深渊里拉你一把的"
    ch      "…… ……"
    voice "voice/qsf_voice/episode1/秋师父022.mp3"
    voice sustain
    mrqiu   "所以年轻人，还是考虑好风险和价值再过来找我吧……修改这种程度的铭牌，也只需要一会儿的时间。"

    show cafe
    show memory
    with Dissolve(0.1)
    # （此处切换回忆到和阿泉先生对话那一段，白色顺闪转场）
    mrquan"如果时间允许的情况下……我建议还是和那个‘要帮助的对象’多多接触……"
    mrquan"不然草草决定‘帮助’和‘不帮助’都是很不明智的选择啊"
    "和阿泉先生说得简直就是一模一样啊！"
    ch"我明白了"
    ch"我会在最后给到您我的答复的"
    stop music fadeout 1.0
    hide cafe
    hide memory
    with Dissolve(0.1)
    scene bedroom day with dissolve
    # （白色瞬闪，从回忆中切出，回到客厅背景，时间为白天，展现初咲的立绘）
    show cx size2 a3 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    with Dissolve(0.2)
    play music "bgm/testbgm/BGM07.ogg"
    cq  "主人昨天晚上是没有睡好吗？"
    "初咲的话一下子把我从回忆中拉回现实"
    cq  "看上去精神很不好的样子哟~"
    "初咲捏了捏我的脸，指着我被黑眼圈环绕了一周的眼眶这样说道"
    ch  "没事的，"
    cq  "主人能这样为我付出……我真的很高兴"
    cq size2 a4 sad "虽然是这样……但是要找到初咲真正的‘主人’，应该还是很难的吧……"
    ch  "倒也没有……"
    ch  "而且也非常感谢初咲这么多天对我的照顾"
    ch  "为什么会有这么多奇奇怪怪的规定，真是麻烦……"
    ch  "那么，最后的一步就是要解决初咲恋柚‘铭牌’的问题了"
    cq size2 a3 smile "嗯嗯！"
    cq  "这次会带着初咲一起出去吗……"
    ch  "当然"
    "初咲像是没有反应过来我会答应地这么干脆利落，在原地愣住了几秒之后突然意识到自己好像被我允许了可以出门"
    "而且这个决断……也是我经过了缜密的思考得出来的……"
    cq size2 a3 happy "谢谢主人！我一定会好好管住自己的！"
    ch  "……"
    "本来准备再次提醒她有关声音的问题，没想到在我说出来之前初咲就提前立下了要求……"
    "不愧是先进的人工智能……"
    ch  "那我们现在出发吧！"
    cq size2 a3 smile "好！"

    scene black with tran_lf
    show park with tran_lf
    hide park
    show street day with tran_lf
    # （场景转换，转到公园+九衢の街等等，变换）
    "我和初咲穿过昙华林公园，我来到了九衢长街上"
    "这是通往九衢市实验中学和九衢市50型地铁二号线的必经之路"
    "说起来也非常奇怪"
    "仿佛是每一次与重要的人相遇都是在这个地方"
    "初咲，岩崎，或者说是蘭……"
    "承载着我太多太多的回忆片段了……"
    show cx size2 a3 normal:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    with Dissolve(0.2)
    cq  "那个……是叫做‘地铁’的东西吗？"
    ch  "是的"
    "大“M”的标识，虽然听说这种符号已经延用了将近50年……"
    "但它的速度和质量都相比之前有了很大的提升……"
    ch  "走吧"
    stop music fadeout 1.0
    scene black with tran_lf
    # （黑幕转场，播放效果音"哐当哐当"，地铁运行的声音，屏幕为黑，转场到九山の街，时间为白天）
    show street two with tran_lf
    ch  "呼，终于到了"
    "可能是好久没有搭乘地铁的原因"
    "如今的50型已经让原本一个小时的车程缩短到了只用半个小时……"
    "除去中间停靠站的时间，跨越十几公里简直就是弹指间的事情"
    "也不免让我的胃里泛起一阵阵恶心感"
    show cx size2 a4 little_serious:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    with Dissolve(0.2)
    cq  "主人没事吧？"
    "察觉到我极不对劲的神色，初咲关切地询问着我的身体状况"
    ch  "没事，我们走吧……照着导航上指示的地点来应该就不会有问题了"
    cq size2 a3 smile "好的"

    hide street two with tran_lf
    show store with tran_lf
    play music "bgm/testbgm/BGM20.ogg"
    # （场景转换：九山の街转黑屏转小店门口）
    # （如果技术力可以的话，这里可以额外增加一个小游戏——如何到达这个店铺的，有点像走迷宫的玩法，后期增加就行）
    "周转了一个多小时后，我终于在当地居民的帮助下找到了这个“仿生机器人黑市”"
    "虽然之前已经来过一次了……但是仅仅凭着过时的GPS来寻路还是很不靠谱的……"
    # （播放效果音："哐当哐当"，铁门被打开的声音）
    "深厚而雄浑的声音从门后飘出来"
    "清涂满脏迹的地面上还堆放着各种看上去是报废掉，弥留着刺鼻味道的各种零件"
    "果然是秋师傅没错了……"

    mrqiu   "是你啊，我还以为是新顾客……"

    mrqiu   "所以说，考虑的怎么样了？"
    ch  "…… ……"
    ch  "…… ……"
    ch  "…… ……"
    ch  "嗯，我想好了，还是决定要换掉她的铭牌"
    "我指着身旁的初咲，夹杂着半分颤抖与肯定的语气，终于将这句话说了出来"
    "我斜着看了一眼我身旁的初咲后，秋师傅又直视着我的眼睛盯着看了好一阵子"
    voice "voice/qsf_voice/episode1/秋师父023.mp3"
    voice sustain
    mrqiu   "看来你是真的下定了决心"
    voice "voice/qsf_voice/episode1/秋师父024.mp3"
    voice sustain
    mrqiu   "喂！那边的……叫什么来着……初咲恋柚对吧？你觉得他怎么样？"
    show cx size2 a3 normal:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    with Dissolve(0.2)
    cq  "是说主人吗？"
    cq  "大概是一个不会照顾自己的，很冒失的笨蛋吧……"
    ch  "…… ……"
    ch  "也没初咲说得这么不堪吧！"
    cq  "可是……"
    cq size2 a3 smile "主人又同样是个温柔，正直的笨蛋……"
    ch  "…… ……"
    ch  "欲扬先抑也不能这么用啊！"
    "看着初咲恋柚羞涩的神情，我不禁也有些尴尬起来"
    "喂，拜托啊！"
    # （加入屏幕抖动）
    "初咲恋柚也只不过是一个高性能的仿生机器人啊……" 
    "我到底在想些什么……"
    voice "voice/qsf_voice/episode1/秋师父025.mp3"
    voice sustain
    mrqiu   "哈，明白了，看上去你们都给出各自的答案了"
    voice "voice/qsf_voice/episode1/秋师父026.mp3"
    voice sustain
    mrqiu   "那就放心交给我吧"
    hide cx size2 a3 smile
    scene black with close
    # （初咲的立绘消失，场景开始缩小，从右往左移）

    "虽然我很享受着和初咲一同生活的这一个半月，享受着她带给我“女仆级别”的服务"
    show livingroom night
    show cx size2 a3 happy:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    show memory
    with close
    cq  "真的吗？！谢谢海川的夸奖！"
    cq  "总之，先来看看我的手艺吧！"
    ch  "好"
    hide livingroom night
    hide cx size2 a3 happy
    hide memory
    with close
    
    show street day
    show cx size2 a2 serious:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    show memory
    with close
    # （这里是回忆片段）
    # （昏黄滤镜+
    cq  "我……我还有些钱！"
    cq  "一天500元以内的话，我是可以付得起的！"
    # （如果可以的话，红色标注，补充注释：500元钱的具体价值，很低，相当于现代社会的100r）
    ch  "这不是用钱能解决的问题！"
    cq size2 a4 little_serious "唔……"
    cq  "那再加上额外的照顾服务！我可以陪在海川君的旁边，家务活都由我全包了！还是免费的哟！"
    ch  "等下，问题不在这里啊喂！"
    cq size2 a3 smile "海川君如果还不满足的话……就当我的临时主人吧！"
    cq  "海川君有什么命令的话初咲都会服从的！"
    cq size2 a3 happy "My Master~"
    stop music fadeout 1.0
    scene black with close
    "可是……"
    "这样的我……"
    "真的值得为了初咲恋柚……去冒这个风险吗……"
    "这真的是我权衡利弊后得出来的结论吗……"
    show store with close 
    # （黑幕转场，背景图不变，这个地方可以插入一些比较灵动，感情加速的bgm）
    voice "voice/qsf_voice/episode1/秋师父027.mp3"
    voice sustain
    mrqiu   "完成了"
    voice "voice/qsf_voice/episode1/秋师父028.mp3"
    voice sustain
    mrqiu   "现在她铭牌已经彻底显示为中式系统，应该不会被检测到问题"
    play music "bgm/testbgm/BGM82.ogg"
    show cx size2 a4 sad:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    with Dissolve(0.2)
    "初咲突然冲上前来，紧紧地拉着我的手，像个孩子一样轻轻啜泣着"
    cq  "好可怕……"
    cq  "红色的铁真的好疼……"
    ch  "没事的没事的"
    "下意识之间，我一边搂着初咲恋柚的身体，一边用另一只手抚摸着她的头发"
    # "以现在这个视角来看"
    voice "voice/qsf_voice/episode1/秋师父029.mp3"
    voice sustain
    mrqiu   "因为更换铭牌会强制打开她所有的感知传感器……"
    voice "voice/qsf_voice/episode1/秋师父030.mp3"
    voice sustain
    mrqiu   "这种感知痛还是无法避免的……"
    voice "voice/qsf_voice/episode1/秋师父031.mp3"
    voice sustain
    mrqiu   "不过……你们是不是有点太亲近了……"
    "在秋师傅的提示下，我才发现，因为关注初咲恋柚的铭牌，我的身体已经完全和初咲贴在一起……"
    "我立刻把双手从初咲的身上撤走"
    ch  "抱歉……不……不是那个意思"
    ch  "确认铭牌有点太仔细了……"
    cq size2 a3 smile "没……没关系的！"
    cq  "这种感觉……很舒服……"

    mrqiu   "哈……看来你们的关系还真不是一般好。今天就当我心情好，给你们免了这一单吧"
    ch  "没……没有"
    ch  "总之谢谢您！"
    "我拽着初咲的校服袖口，可能是夹杂着尴尬和羞涩的心情"
    "狼狈地逃了出来"

    scene black with tran_lf
    show street two with tran_lf
    # （黑幕转场，背景：九山の街，白天）
    ch  "诶？"
    "忽然间，我感觉到手上传来有一些雨滴滴落的触感"
    ch  "是下雨了？"
    "抬头望向天空，好像并没有任何下雨的迹象"
    "我低头再看向手部，却发现是一滴滴泪水，啪嗒啪嗒地打在我的手上"
    ch  "诶诶？你没事吧？"
    "我拍了拍正在不断流泪的初咲恋柚"
    ch  "你……没事吧？"
    show cx size2 a4 sad:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    with Dissolve(0.2)
    "眼前的初咲恋柚只是摇了摇头，并没有回答我说的话"
    hide cx size2 a4 sad with Dissolve(0.2)
    hide street with tran_lf
    show street day with tran_lf
    $renpy.pause(1,hard=False)
    hide street day with tran_lf
    show home afternoon with tran_lf
    $renpy.pause(1,hard=False)
    hide home afternoon with tran_lf
    scene black with close
    # （黑幕+场景转换，多个场景的切换，九山の街——黑幕——九衢の街——房间门口）

    "一路上当我安慰起初咲的时候她都保持一言不发，虽然我也不知道自己在安慰些什么……" 
    "我始终不知道初咲哭泣的原因是什么……" 

    # （黑幕转场，来到客厅，下午背景）
    "此刻的我也并没有意识到……" 
    "此这是唯一一次"
    "也是最后一次"
    "初咲对我卸下的伪装……"
    $renpy.pause(2,hard=False)
    stop music fadeout 1.0
    # （黑幕转场，强制暂停5s，背景转换到客厅，早晨）
    show bedroom day with dissolve
    show cx size2 a3 smile:
        xalign 0.5
        yalign 1.0
        zoom 1.4
    with Dissolve(0.2)
    play music "bgm/testbgm/BGM02.ogg"
    cq  "早上好！主人！"
    "此刻的初咲仿佛从昨天的低糜情绪种立刻切回了她本身的高昂状态"
    ch  "昨天……"
    cq  "那个呀……这不过是我卓越的表演能力"
    cq  "哼哼，主人不会真的被我吓到了吧~"
    "总感觉……"
    cq size2 a3 happy"毕竟我还是最喜欢表演的了！"
    "好像也是……"
    "从最开始，我就知道了初咲的设定是“精通表演”……这一个半月的时间里也常常用这种能力来给我开玩笑……  "
    ch  "看起来今天也是元气满满的呢"
    cq size2 a3 normal "是的！"
    cq  "今天就是和主人返回东京，"
    cq  "然后寻找到真正的主人的日子对吧？"
    ch  "是这样子的"
    "我把所有的行李和携带的大件物品转在提前预约的出租车上，尽可能去回想自己有没有缺失什么东西"
    "实际上,我能感受到这种愈发强烈的紧张感正慢慢侵袭我的全身"
    "虽然已经让蘭，岩崎一起帮助初咲进行了几百次的模拟海关流程"
    "但是我仍然十分担心……"
    cq  "加油！我们一定可以做到的！"
    ch  "嗯嗯，一定可以的！"
    "那么，就怀着这股必胜的气势，一鼓作气吧！"

    # （黑幕转场，来到海关关口的背景，早晨）
    scene black with tran_lf
    show airport with tran_lf
    "俗话说，“人们对痛苦的回忆总是趋于忘记”"
    "对我来说，我已经忘记了刚才长达几个小时的紧张情绪是怎么缓解的了"
    "总之，我已经通过了海关，非常顺利地成为了“通过者”"
    "这并没有让我感到松懈"
    "远处的初咲正在接受考官的询问和审查……"
    "我甚至已经做好了被制裁的任何最坏的打算……"
    "我低下头，开始思考着和初咲的未来……尽管一切都是未知数……"
    "初咲确实能够给我带来快乐，赶走我一个人在九衢生活的这两个月的寂寞"
    "只不过这种无法获得的，又或者说，这种“终将失去的幸福感”"
    "会让我感觉到突然之间的落寞和空虚"
    "就算是那样……也无所谓了吧……"  
    "在我内心深处，“帮初咲”和“不帮初咲”应该是早就确定好的吧……"
    stop music fadeout 1.0

    # （镜头平行移动，最后聚焦到中心处停留，放大）
    "不过悲伤的情绪很快就烟消云散了"
    "在向我比了一个“OK”的手势之后，初咲一蹦一跳的走了过来"
    "我知道，那一刻积攒了两个月所有的压力瞬间得到释放"
    "一切难过和委屈的情绪都在这一刻化成了无限的希望和激动的心情"
    play music "bgm/testbgm/BGM_A16_2_1.ogg" 
    ch  "我们这是，成功了？！"
    # （缓慢展现蘭的立绘）
    voice "voice/l_voice/episode1/蘭132.mp3"
    voice sustain
    show lan size2 a2 smile:
        xalign 0.1
        yalign 1.0
        zoom 1.3
    with dissolve
    l   "没错没错，果然和我想得一模一样，根本就是非常随意的检查啦"
    "朝我迎面走来的蘭甚至也露出得意的笑容"
    voice "voice/yqtt_voice/episode1/岩崎074.mp3"
    voice sustain
    show yq size1 a1 smile:
        xalign 0.9
        yalign 1.0
        zoom 1.3
    with dissolve
    yq  "那么，首先祝贺我们旗开得胜"
    # （缓慢展现岩崎的立绘）
    ch  "欢迎回家，初咲！"
    show cx size2 a3 happy:
        xalign 0.5
        yalign 1.0
        zoom 1.3
    with dissolve
    cq  "嗯！我回来了！"
    "看着初咲的笑容，我每次都能想到好多好多……"
    "天真，烂漫……"
    "或者说，和玫瑰花，樱花一样美丽动人……"
    "几乎总是让我忘记了她仿生机器人的身份……"
    "对呀，说到花"
    "初咲恋柚这四个字中不是有“咲”这个字，是指花开的意思吗？"
    "眼前的初咲，正伴随着机场的背景音乐在一旁独自地跳起舞来……"
    "完全可以把她说成一朵"
    "沉浸在自己表演世界中的一朵美丽的花朵"
    "至于这场我和她的演出"
    "从此刻起……"
    "正式开幕。"
    stop music
    jump episode2_1