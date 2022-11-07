
###  episode1上半部分 ################
label episode1_1:
    $ config.allow_skipping = False
    window hide
    image episode1_video1 = Movie(play="videos/episode_video/episode1.mpg",loops=0,stop_music=True)
    show episode1_video1
    $ renpy.pause(4.5,hard = True)#时长是你视频的长度，播完自动退出
    hide episode1_video1
    scene bg2
    play music "bgm/九衢长街/九衢长街新版.mp3"
    $ renpy.pause(1.0,hard = True)#时长是你视频的长度，播完自动退出
    $ config.allow_skipping = True
    #（黑幕淡出，播放episode1 01界面画面"被遗弃的冬日旋律"）

    #背景：多云天气，街道

    #（切换场景：九衢の街，白天）

    show bg5 with fade
    "小寒将至的九衢市，在多云的日子里显得格外冷清"
    "笼罩在城市上空，纱般的云朵似乎怎么样也流不完"
    "勾销在日历上，一笔又一笔的墨迹却又清晰地提示着我平澹无奇的日常"
    "我是一个普通的高三学生"
    "父母在中国从事着普通的工作"
    "常年稳定在中等的成绩"
    "正值青春的年龄却完全没有和任何异性擦出火花"
    "除了随父亲取了一个日语名字之外"
    "我完全就是一个纯粹的中国高中生"
    "唔. . ."
    "或许正是因为这个名字的缘故，让我始终无法正常地融入同龄人中"
    "或者说，“普通”这个结果应该算是最理想的情况了"
    "如果要说起有什么成就的话"
    "大概是组建了一个还算比较成功的社团"
    "但似乎也没有被我打理得很好. . ."
    "不过好在，"
    "索然无味的生活就要被改写了"
    "我刚刚收到了通过“东番国立高大交换项目”的信息，十几天来沉重的心情总算释放啦"
    "一切看上去都是那么美好！"
    "终于可以和这平淡无奇的日常说声再会了！"

    #（黑幕，转场特效）

    #背景：咨询台前，询问背景为台子，一般的背景即可，需要蘭站在咨询台只露嘴巴的cg

    #（先放楼道背景，再资料核对处转为核对处背景）

    "我用每次跨越两步的熟练节奏迈上阶梯"
    "说不定，这就是我最后一次来到学校了吧. . ."
    "这么说来内心还多少有点伤感和惋惜的感觉"
    "因为需要填写“东番国立高大交换项目”的个人信息，我再次回到九衢市市实验中学，重新感受到这里的一切一切"
    "没想到已经过去了两年半. . .时间过得真快"
    "中文课上老师经常提到一个专门用来表示时间过得很快的词汇，"
    "叫做“白驹过隙”"
    "指的是白马在细小的缝隙前一闪而过"
    "大抵也能详尽描述出我现在的这种对时间深深感触的心态吧"

    #（转换成书吧背景）

    "穿过书吧，左手边就是在消息中提到的的“资料核对处”"
    "我需要在这里将我的资料和各种入学信息填写完整"
    "“资料核对处”的工位上，一个看上去和我年龄相仿的女孩子正在清点记录手头上的资料"

    #（停顿3s，镜头拉近）

    "我走上前"
    ch "请问这里是资料核对处吗？"
    voice "voice/l_voice/episode1/蘭001.mp3"
    who "是的，你是？"
    voice sustain
    voice "voice/l_voice/episode1/蘭002.mp3"
    who "海川？！！"
    voice sustain
    "面前的这个女生似乎是意识到了什么，发出了大声的惊叹"

    ch "嗯"
    "已经预料到面前这个女生会用一脸诧异的表情看着我的我抬起头，"
    "这个声音. . .是她没错了"

    #（放出立绘：蘭，惊讶表情）
    #show
    "蘭，一个总是习惯用目中无人的态度和轻蔑的口气无视我的“文学创作社”社长"
    "虽然蘭是我从小的“青梅竹马”，但我们的关系，根本就不是日本动漫上所言的“那种关系”"
    "要说起来的话，"
    "应该是“毒舌”+“青梅竹马”+“极度地讨厌我”这种奇怪设定"
    "总之，"
    "她的出现，就意味着接下来发生的事情将变得很棘手. . ."
    "此刻的我们四目相对，"
    "互相的脸上都写满了‘尴尬’和‘无语’"
    ch "话说蘭，你为什么会在这里？"
    #show
    voice "voice/l_voice/episode1/蘭003.mp3"
    l "当然是志愿工作啦！"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭004.mp3"
    l "才不会像某些人一样，只有闲到无聊的时候才会过来转转"
    voice sustain
    "说完蘭还不忘轻蔑地扫了我一眼，摆出一副高傲的姿态"
    voice sustain
    ch "你身上穿的这件看上去十分高档的‘日本高中生’制服又是从哪里弄来的?"
    voice sustain
    ch "在这样的严肃场合. . ."
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭005.mp3"
    voice sustain
    l "你在乱说什么呀？！"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭006.mp3"
    voice sustain
    l "请注意礼貌用语，不要随便用‘弄’这个词。"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭007.mp3"
    voice sustain
    l "海川该不会是在把本小姐污蔑成像小偷那样子的角色吧？"
    voice sustain
    ch ". . . . . ."
    voice sustain
    ch ". . . . . ."
    voice sustain
    ch ". . . . . ."
    voice sustain
    ch "好奇怪的说. . ."
    voice sustain
    ch "在用词上还要斤斤计较. . ."
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭008.mp3"
    voice sustain
    l "这是我的新校服"
    voice sustain
    ch "校服？"
    voice sustain
    ch "我打量着这套校服，目光落在了她胸口的上面那个金闪闪的校徽，上面还有几个用片假名拼在一起的学校名称"
    voice sustain
    ch "东番. . .国立. . .高大？"
    voice sustain
    ch "这简直就是我熟悉到不能再熟悉的日语. . ."
    voice sustain
    ch "在读出来的那一瞬间，我的心“咯噔”地跳动了一下"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭009.mp3"
    voice sustain
    l "bingo~答对了！"
    voice sustain
    "“东番国立高大”，一所以“仿生机器人制造技术”专业而闻名的“高大7年制联合培养”的“高中大学”"
    voice sustain
    "由于这所学校的独特培养方式和优质的教学质量，它成为了每一位海外求学者的梦中情校"
    voice sustain
    ch ". . . . . ."
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭010.mp3"
    voice sustain
    l "喂！一直盯着女生的胸部也太无礼了吧！"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭011.mp3"
    voice sustain
    l "总之，海川羡慕我是没有用的. . .这都是靠我自己的努力才换来的"
    #show
    voice "voice/l_voice/episode1/蘭012.mp3"
    voice sustain
    l "正所谓‘天道酬勤’"
    #show
    voice "voice/l_voice/episode1/蘭013.mp3"
    voice sustain
    l "像你这种懒人肯定是不懂这种道理的"
    voice sustain
    ch ". . . . . ."
    voice sustain
    "说完，眼前的蘭还不忘撩了撩她的头发，斜睨的眼神似乎是在向我强调着对自己的满意和自信"
    voice sustain
    "总之，糟透了。"
    #show
    voice "voice/l_voice/episode1/蘭014.mp3"
    voice sustain
    l "无事不登三宝殿，说吧，你到这儿来有什么目的"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭015.mp3"
    voice sustain
    l "还是说. . ."
    #show
    voice "voice/l_voice/episode1/蘭016.mp3"
    voice sustain
    l "专程从家里跑过来"
    #show
    voice "voice/l_voice/episode1/蘭017.mp3"
    voice sustain
    l "只为了见本小姐最后一面吗？"
    voice sustain
    ch "喂，不要没有证据地胡乱猜测啊！"
    voice sustain
    #（停顿2-3s）
    ch "当然是因为要办理交换项目的手续才过来的"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭018.mp3"
    voice sustain
    l "嗯？！！"
    #show
    voice "voice/l_voice/episode1/蘭019.mp3"
    voice sustain
    l "没想到海川也有去国外进修的机会"
    #show
    voice "voice/l_voice/episode1/蘭020.mp3"
    voice sustain
    l "海川这样的人. . .怎么可能. . ."
    "蘭用指尖指着那份在手机上的名单，仔仔细细地核对着"
    "不时还用狐疑的眼神盯着我，仿佛认定了“我”不是“我”一般"
    "终于，她抬起头，又仔仔细细打量了我一番，然后点了点头，似乎是对我表示了认可"
    #show
    voice "voice/l_voice/episode1/蘭021.mp3"
    voice sustain
    l "真是不可思议，你的名字竟然真的能出现在这份名单上"
    #show
    voice "voice/l_voice/episode1/蘭022.mp3"
    voice sustain
    l "有没有一种可能，我手上拿的这份交换生名单是假的？"
    voice sustain
    ch ". . . . . ."
    voice sustain
    ch "这种不合情理而且打击人的话也不能这样乱讲啊喂！！"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭023.mp3"
    voice sustain
    l "所以说，海川渡是来填写哪个学校的交换项目信息啊？"
    ch "东番国立高大。"
    #show
    l ". . . . . ."
    l ". . . . . ."
    l ". . . . . ."
    #show
    voice "voice/l_voice/episode1/蘭024.mp3"
    voice sustain
    l "诶？？？！"
    #show
    voice "voice/l_voice/episode1/蘭025.mp3"
    voice sustain
    l "竟然和本小姐是同一个学校吗？！"
    #show
    voice "voice/l_voice/episode1/蘭026.mp3"
    voice sustain
    l "学校真的会收留你吗？"
    voice sustain
    ch ". . . . . ."
    voice sustain
    ch "看来也只有你才会说出‘收留’这种词汇. . ."
    voice sustain
    ch "说得我好像是完全就没有参加考试的感觉"
    #show
    voice "voice/l_voice/episode1/蘭027.mp3"
    voice sustain
    l "唔，明明入学考试那么难的说. . ."
    voice sustain
    "蘭在多次核对了我的录取情况之后，她的脸显示出些许不满的情绪。"
    #show
    voice "voice/l_voice/episode1/蘭028.mp3"
    voice sustain
    l "可真是倒霉"
    #show
    voice "voice/l_voice/episode1/蘭029.mp3"
    voice sustain
    l "一想到还要和海川在同一所学校里相处四年半的时间，我就浑身难受. . ."
    ch ". . . . . ."
    #show
    voice "voice/l_voice/episode1/蘭030.mp3"
    voice sustain
    l "不过我是真没想到，唯二的名额能被海川分走一个"
    #show
    voice "voice/l_voice/episode1/蘭031.mp3"
    voice sustain
    l "你还是蛮有本事的嘛，"
    #show
    voice "voice/l_voice/episode1/蘭032.mp3"
    voice sustain
    l "完全超出了本小姐的预料"
    #show
    voice "voice/l_voice/episode1/蘭033.mp3"
    voice sustain
    l "那么，海川肯定和我一样，是‘新媒体传播与交叉演出’专业，对吧？"
    voice sustain
    ch ". . . . . ."
    voice sustain
    ch "不是的"
    voice sustain
    "在我摇了摇头后，蘭露出了更加惊讶的表情看着我"
    #show
    voice "voice/l_voice/episode1/蘭034.mp3"
    voice sustain
    l "让我看看. . .填报院系. . .‘仿生机器人制造技术’，不愧是你. . ."
    #（立绘上切换成蘭无语的表情）
    voice sustain
    "果不其然，每次在和蘭聊天中必不可少的就是那双“像是看着垃圾的眼神”"
    voice sustain
    "尤其是在和我聊天的时候，似乎是有什么不可名状的原因导致蘭一直都很厌恶眼前的我"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭035.mp3"
    voice sustain
    l "我还以为你会继续学习演出的. . ."
    #show
    voice "voice/l_voice/episode1/蘭036.mp3"
    voice sustain
    l "到头来还都是奔着造机器人去啊"
    #show
    voice "voice/l_voice/episode1/蘭037.mp3"
    voice sustain
    l "真不愧是你啊. . .‘PTFOD’的演出社社长"
    voice sustain
    "蘭加重了”PTFOD“这几个字，略微带着一点嘲讽和调侃的语气，看来是故意在说给我听的"
    voice sustain
    "PTFOD演出社团"
    voice sustain
    "一个由于我个人对演出和古典乐抱有强烈喜爱而在中学创建的社团"
    voice sustain
    "在昨天最后的一次表演后，就解散了"
    voice sustain
    "这么想来还很有点可惜"
    voice sustain
    "话说回来，蘭经常会帮助我们的社团写一些演出的剧本"
    voice sustain
    "只不过对我这个社长很不满意就是了. . ."
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭038.mp3"
    voice sustain
    l "诺，这是你需要填写的信息，就在这个表格里面，填满就可以了"
    voice sustain
    ch "谢谢"
    voice sustain
    "我接过填写表"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭039.mp3"
    voice sustain
    l "能给我一个理由吗"
    voice sustain
    ch "什么？"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭040.mp3"
    voice sustain
    l "明明这么喜欢演出，但最后还是去了机器人制造专业"
    #show
    voice "voice/l_voice/episode1/蘭041.mp3"
    voice sustain
    l "这不像你"
    voice sustain
    "我慢慢停下手中的笔，盯着刚刚落笔在“专业确认”那一栏中填下的“仿生机器人制造技术”"
    voice sustain
    "天花板上摇摇欲坠的吊灯在电子屏幕上投影的明晃晃光圈显得那样诱人，"
    voice sustain
    "我发了好一会儿呆，直到蘭伸出手在我的面前挥了挥"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭042.mp3"
    voice sustain
    l "喂喂，你刚刚听到了我问你的问题了吧？"
    voice sustain
    ch ". . ."
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭043.mp3"
    voice sustain
    l "该不会是在计较昨天晚上和秋月的事情吧？"
    voice sustain
    ch "也不算是，只是昨天晚上因为看到录取的消息有点睡不着觉，好困. . ."
    voice sustain
    ch ". . . . . ."
    voice sustain
    ch ". . . . . ."
    voice sustain
    ch ". . . . . ."
    voice sustain
    "这是谎言"
    voice sustain
    "直到现在为止，我都还在为昨天晚上发生的各种事情耿耿于怀"
    voice sustain
    ch "简单来说，就是因为父亲要回到日本工作，加上他本身就是从事‘机器人制造’相关的行业，就执意希望我继承他的工作吧. . ."
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭044.mp3"
    voice sustain
    l "但是你明明更喜欢表演吧，真是奇怪的执念"
    #show
    voice "voice/l_voice/episode1/蘭045.mp3"
    voice sustain
    l "真搞不懂为什么非要有‘子承父业’这种硬性要求啊"
    #show
    voice "voice/l_voice/episode1/蘭046.mp3"
    voice sustain
    l "明明可以大胆追求自己喜欢做的事情啊！"
    voice sustain
    "不得不说，蘭总能在对我一顿“毒舌”之后说出这样似乎是为我着想的话"
    voice sustain
    "出乎意料地为我着想. . ."
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭047.mp3"
    voice sustain
    l "这就是我不喜欢你的理由"
    voice sustain
    ch ". . . . . ."
    voice sustain
    "好吧，收回刚才我说的话"
    voice sustain
    "就算是不喜欢别人的话说出来真够直接啊. . ."
    voice sustain
    who "各位，在这样乌云密布的早晨，"#（日语出场）
    voice sustain
    who "说明了今天肯定会有大事发生. . ."
    voice sustain
    who "换句话说. . ."
    voice sustain
    who "命运的抉择"
    voice sustain
    "一个人影突然从我们的旁边闪过，拍了拍我和蘭的肩膀"
    voice sustain
    #（此处播放类似于手机掉在地上的效果音）
    "蘭向后退了几步，用来做登记的电子屏也因为蘭的惊慌失措掉在地上"
    voice sustain
    "以这种方式出场，也只会是我的那个非常冒失的中二病伙伴了——"
    voice sustain
    "岩崎天桐"
    voice sustain
    "虽然看上去外表和普通人没有两样，但是实际上岩崎天桐却是集结了这个时代最前沿科技的仿生机器人。"
    voice sustain
    "小时候的我一直以为岩崎只是蘭的一个哥哥，直到上了高中之后，才发现他的外貌根本没有变过。"
    voice sustain
    ch "早上好呀，岩崎！"
    voice sustain
    #show
    voice "voice/yqtt_voice/episode1/岩崎001.mp3"
    voice sustain
    yq  "你好啊，海川！"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭048.mp3"
    voice sustain
    l "在学校里就给我好好说中文呀，这样真的很尴尬！"
    #show
    voice "voice/yqtt_voice/episode1/岩崎002.mp3"
    voice sustain
    yq  "咳咳，我明白了"
    #show
    voice "voice/l_voice/episode1/蘭049.mp3"
    voice sustain
    l ". . .你怎么来了？"
    #show
    voice "voice/yqtt_voice/episode1/岩崎003.mp3"
    voice sustain
    yq  "我为什么不能来？"
    #show
    voice "voice/l_voice/episode1/蘭050.mp3"
    voice sustain
    l "明明说了好多次，今天再不要跟着我过来了！"
    voice sustain
    "蘭指着岩崎天桐的鼻梁，看上去非常气恼的样子. . ."
    voice sustain
    "虽然两个人的身高差看上去极不谐调，不过这样的场景在我看来却异常地诙谐"
    voice sustain
    ch "噗嗤"
    voice sustain
    "一个没忍住，我还是笑出声了"
    voice sustain
    "蘭狠狠地盯了我一眼，在轻轻地“哼”了一声之后，就继续开始自己的工作了"
    #show
    voice "voice/yqtt_voice/episode1/岩崎004.mp3"
    voice sustain
    yq  "好了好了，不耽误小蘭的时间"
    #show
    voice "voice/yqtt_voice/episode1/岩崎005.mp3"
    voice sustain
    yq  "还不是因为其他人的魔法结社传唤申请被你落在家里"
    voice sustain
    ch "是留学申请档案"
    #show
    voice "voice/yqtt_voice/episode1/岩崎006.mp3"
    voice sustain
    yq  "我才会专门调用能够快速跨越长江的异界载具. . ."
    voice sustain
    ch "是九衢市50型地铁二号线转五号线"
    voice sustain
    #show
    voice "voice/yqtt_voice/episode1/岩崎007.mp3"
    voice sustain
    yq  "总之，这一路过来可真是辛苦. . ."
    voice sustain
    ch "明明从汉江路到昙华林公园这一带只用不到十分钟的时间. . ."
    #show
    voice "voice/yqtt_voice/episode1/岩崎008.mp3"
    voice sustain
    yq  "哎呀，海川啊海川"
    #show
    voice "voice/yqtt_voice/episode1/岩崎009.mp3"
    voice sustain
    yq  "你说这么直接就没意思了. . ."
    voice sustain
    ch "就在我们谈话间，蘭悄悄地把这一沓档案袋放到了自己的书包里，不过还是被岩崎天桐看到了"
    voice sustain
    #show
    voice "voice/yqtt_voice/episode1/岩崎010.mp3"
    voice sustain
    yq  "喂喂，你还没有感谢我呢！"
    #show
    voice "voice/yqtt_voice/episode1/岩崎011.mp3"
    voice sustain
    yq  "就这样把我辛辛苦苦护送过来的魔法结社传唤申请给拿走了. . .明明是你自己把东西落下了"
    #show
    voice "voice/l_voice/episode1/蘭051.mp3"
    voice sustain
    l "才. . .才不是"

    #（这里让蘭立绘表情的脸变得通红）

    #show
    voice "voice/yqtt_voice/episode1/岩崎012.mp3"
    voice sustain
    yq  "然后呢？"
    #show
    voice "voice/yqtt_voice/episode1/岩崎013.mp3"
    voice sustain
    yq  "我们的大小姐不会一点表示都没有吧？"
    #show
    l ". . ."
    #show
    voice "voice/l_voice/episode1/蘭052.mp3"
    voice sustain
    l "谢. . .谢. . ."
    #show
    voice "voice/l_voice/episode1/蘭053.mp3"
    voice sustain
    l "让你多跑一趟. . .辛苦你了"
    voice sustain
    "蘭用几乎是我们能听到的最低声音喃喃地向岩崎道谢"
    voice sustain
    "满脸通红的她就像是一个认错的小孩，完全就没有刚刚的那种咄咄逼人的锐气"
    voice sustain
    #show
    voice "voice/yqtt_voice/episode1/岩崎014.mp3"
    voice sustain
    yq  "这就对了嘛"
    voice sustain
    "顺势，岩崎天桐把手放在了蘭的头上，轻轻地来回抚摸着"
    voice sustain
    "岩崎天桐对着他的主人轻轻地笑着，那种宠溺的眼神看上去和“蘭的大哥哥”这个标签完全吻合。"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭054.mp3"
    voice sustain
    l "不要这样！"
    voice sustain
    "蘭猛地向后又退了一步"
    voice sustain
    "慌张地向四周看了看，然后装作若无其事地清理咨询台上的各种资料"
    voice sustain
    #show
    voice "voice/yqtt_voice/episode1/岩崎015.mp3"
    voice sustain
    yq  "小蘭，你躲我干什么啊. . ."
    #show
    voice "voice/l_voice/episode1/蘭055.mp3"
    voice sustain
    l "别. . .别一口一个‘小蘭’的，真让人讨厌！"
    #show
    voice "voice/yqtt_voice/episode1/岩崎016.mp3"
    voice sustain
    yq  "明明之前出游的时候还让我偷偷喊你‘妹妹’的. . ."
    #show
    voice "voice/l_voice/episode1/蘭056.mp3"
    voice sustain
    l "你！你. . .我不许你再说了！"
    #show
    voice "voice/l_voice/episode1/蘭057.mp3"
    voice sustain
    l "快给我. . .走开！"
    ch "蘭用力地将岩崎天桐朝向我这边推过来，摆出一副很不耐烦的样子"
    #show
    voice "voice/l_voice/episode1/蘭058.mp3"
    voice sustain
    l "我这边还有很多资料要整理，不要再打扰我了！"
    #show
    voice "voice/yqtt_voice/episode1/岩崎017.mp3"
    voice sustain
    yq  "嘿嘿，我明白了"
    ch "岩崎天桐朝向我不自然地咧嘴笑了笑"
    #show
    voice "voice/yqtt_voice/episode1/岩崎018.mp3"
    voice sustain
    yq  "那我就先行告辞了"
    #show
    voice "voice/yqtt_voice/episode1/岩崎019.mp3"
    voice sustain
    yq  "还请主上大人期待今天我精心准备的‘晚宴’吧"
    voice sustain
    "说完，岩崎天桐还不忘把手架在脸上，颇有一番中二且极为自信的气势"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭059.mp3"
    voice sustain
    l "中. . .中二病！"
    "在和蘭的推推搡搡中，岩崎天桐很快就消失在我的视线中"
    #show
    voice "voice/l_voice/episode1/蘭060.mp3"
    voice sustain
    l "呼. . ."
    #show
    voice "voice/l_voice/episode1/蘭061.mp3"
    voice sustain
    l "真是的. . .还非要摆出这一副傲慢的态度. . ."
    "到底是谁更傲慢一点啊喂. . ."
    ch "看来岩崎中二的个性还是没有改变啊"
    ch "不过感觉你和岩崎的感情还真的是非常好呢。"
    #show
    voice "voice/l_voice/episode1/蘭062.mp3"
    voice sustain
    l "才不是这样！"
    #show
    voice "voice/l_voice/episode1/蘭063.mp3"
    voice sustain
    l "最近感觉岩崎他好烦人，才不想靠近这种自以为是的大傻瓜"
    voice sustain
    "无论怎样，蘭在面对岩崎时露出的奇怪神情总是让我感觉到异样"
    voice sustain
    "甚至给我一种胡乱的大胆猜测"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭064.mp3"
    voice sustain
    l "喂喂，刚才的表你填完了吗？"
    voice sustain
    ch "嗯，填完了"
    voice sustain
    "蘭打断了我的胡乱臆想. . .可能也只是错觉吧？"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭065.mp3"
    voice sustain
    l "好的，给我来检查一下"
    voice sustain
    #show
    l ". . . . . ."
    voice sustain
    #show
    l ". . . . . ."
    voice sustain
    #show
    l ". . . . . ."
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭066.mp3"
    voice sustain
    l "表格是没什么问题了"
    voice sustain
    ch "好"
    voice sustain
    "我拿起了放在一旁的挎包，拍了拍落上面的灰"
    voice sustain
    "正当我准备转身离开的时候，突然被蘭叫住了"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭067.mp3"
    voice sustain
    l "等等！忘记和你说要拿校服了"
    voice sustain
    "蘭俯身从摆放在咨询台旁边的众多的袋子中挑出了看上去最高贵的那个，上面赫然印着“东番国立高大”的名称"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭068.mp3"
    voice sustain
    l "呐！这个是校服"
    #show
    voice "voice/l_voice/episode1/蘭069.mp3"
    voice sustain
    l "还有这些是入学必备的资料"
    voice sustain
    ch "没想到这么快就发到我们学生手上了啊"
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭070.mp3"
    voice sustain
    l "哼哼，毕竟是高大嘛"
    voice sustain
    "我接过蘭递给我的各种资料，然后把这些东西塞回了我的书包中"
    voice sustain
    #show
    #voice "voice/l_voice/episode1/蘭071.mp3"(配音配掉了)
    voice sustain
    l "还有一个私人的问题"
    #ch "嗯，你说"
    #show
    voice "voice/l_voice/episode1/蘭071.mp3"
    voice sustain
    l "为什么海川不会想着携带一个robot入学呢？"
    voice sustain
    ch "是学校强制要求的吗？"
    #show
    voice "voice/l_voice/episode1/蘭072.mp3"
    voice sustain
    l "不是的，只是这样的话会方便很多"
    #show
    voice "voice/l_voice/episode1/蘭073.mp3"
    voice sustain
    l "比如说. . .可以帮你做好家务活之类的"
    voice sustain
    ch ". . . . . ."
    voice sustain
    #show
    voice "voice/l_voice/episode1/蘭075.mp3"
    voice sustain
    l "倒不如说是，校方鼓励携带机器人"
    #show
    voice "voice/l_voice/episode1/蘭076.mp3"
    voice sustain
    l "海川没听说过吗？无论是校服还是出入学校内各种场所的特权，你的仿生机器人都是拥有同等权益的。"
    #show
    voice "voice/l_voice/episode1/蘭077.mp3"
    voice sustain
    l "看来海川还真是不问世事呀，被消息隔离也是理所当然的吧"
    voice sustain
    ch "不要随便毒舌啊，这种事情我还是知道的。"
    voice sustain
    ch "总的来说，东番国立高大在这方面也想得非常周到，充分考虑到之前仿生机器人和人权问题"
    #show
    voice "voice/l_voice/episode1/蘭078.mp3"
    voice sustain
    l "嗯嗯。"
    ch "我是因为家里的缘故才没有买那种东西"
    #show
    voice "voice/l_voice/episode1/蘭079.mp3"
    voice sustain
    l "原来如此. . ."
    voice "voice/l_voice/episode1/蘭080.mp3"
    voice sustain
    "蘭狐疑地看了我两眼，不过很快就没在意我刚刚说地那些话了"
    voice sustain
    l "总之，学校本来已经给我们准备好了四套校服"
    #show
    voice "voice/l_voice/episode1/蘭081.mp3"
    voice sustain
    l "两份是你自己的，两份是给机器人的"
    #show
    voice "voice/l_voice/episode1/蘭082.mp3"
    voice sustain
    l "不过这多的两件校服，你真的不拿着吗？"
    ch "算了，我想我根本就不需要什么robot之类的东西吧. . ."
    #show
    voice "voice/l_voice/episode1/蘭083.mp3"
    voice sustain
    l "好吧"
    #show
    voice "voice/l_voice/episode1/蘭084.mp3"
    voice sustain
    l "这可是你说不要的"
    #show
    voice "voice/l_voice/episode1/蘭085.mp3"
    voice sustain
    l "要知道东番国立大学的校服可是别人想要都要不到的哟"
    "说完，蘭再次专门挺了挺自己胸前的胸章，似乎是非常满意与自豪的样子"
    #show
    voice "voice/l_voice/episode1/蘭086.mp3"
    voice sustain
    l "我想这件校服肯定会留给有需要的人. . ."
    #show
    voice "voice/l_voice/episode1/蘭087.mp3"
    voice sustain
    l "至少不会留给海川这种不珍惜校服的人"
    voice sustain
    ch ". . . . . ."
    voice sustain
    ch "那样听起来也蛮不错的感觉"
    #show
    voice "voice/l_voice/episode1/蘭088.mp3"
    voice sustain
    l "你. . ."
    #show
    voice "voice/l_voice/episode1/蘭089.mp3"
    voice sustain
    l "你还真是不知好歹啊！"#（恼）
    #show
    voice "voice/l_voice/episode1/蘭090.mp3"
    voice sustain
    l "呼. . .算了，不和你这种榆木脑袋解释了"
    #show
    voice "voice/l_voice/episode1/蘭091.mp3"
    voice sustain
    l "好了好了，快从本小姐面前闪开"
    #show
    voice "voice/l_voice/episode1/蘭092.mp3"
    voice sustain
    l "这里没你的事了"

    "于是在蘭的催促之下，我很快离开了书吧"


    #（黑幕动画转场，背景跳转，来到九衢の街场景，下午，画面缓缓移动，并固定在某一点）
    scene bg1 with fade
    play music "bgm/困惑中/2.mp3"
    "在学校内和各位老师以及认识的人说了声道别后，时间很快来到了下午。"
    "离开了九衢市实验中学的我很快又回到了这个日常的上放学街道"
    "自从经历了九衢市市容整改后，在这条街上店家的旧房子都被拆除，建成了更宽阔的马路以及更具有现代感和高科技感的低层建筑"
    "我抬头望了望不远处跃动着的微光，氤氲晨曦的映照下显得那样美丽"
    "即使是在白空中也能璀璨闪烁着的，交织在一起的“群星”，代表着人类的智慧结晶"
    "我时常会惊讶这个顶层建筑物能在这样的一个大城市的高楼建筑物角逐中脱颖而出。"
    "这个名为“laser精工”的机器人制造企业，在我记事起就很快占据了世界各地大城市的中心，源源不断地输送着城市所需要的“新鲜血液”"
    "依稀中，我记起父亲的工作就是在这栋建筑物中，好像是什么境外专员. . ."
    "总之，在我的印象中父亲一刻都没有停歇过，好像一直在忙于工作"
    "就算是在家里都没怎么见到过他. . ."
    "可能这就是我非常向往这座高塔的原因之一吧。"
    "儿时的我经常听蘭讲起自己的父母都在这座高楼中从事着仿生机器人技术制造的工作"
    "好像是在蘭8岁的时候，就收到了一份来自父母给她的礼物——"
    "蘭告诉我说："

    #（此处切入线稿1，并进行变换，第一张为单纯的黄色背景）

    #show
    voice "voice/l_voice/episode1/蘭093.mp3"
    voice sustain
    l "因为爸爸妈妈一直都在‘高塔’里工作，平时也完全没有时间照顾我. . ."
    voice sustain
    "所以就顺理成章地按照蘭的想法给她找了一个能够照顾她的人——"
    voice sustain

    #（此处切入线稿2，一个没有脸的大哥哥线稿出现在屏幕上）

    "名为“小岩”的大哥哥"
    voice sustain
    "当时的我是完全不知道面前的这个大哥哥竟然是一个仿生机器人"
    voice sustain

    #（此处切入线稿3，两个小孩，一年一女，背对着玩家，面向那个没有脸的大哥哥线稿）

    "这位自称是蘭的哥哥的“小岩”，总是能和我们打成一片. . ."
    voice sustain
    "我很羡慕蘭，因为她有这样一个大哥哥，站在她的身边，默默地保护着她"
    voice sustain
    "虽然当时的“小岩”看上去已经有了接近成年人的长相，但是仍然给我一种非常亲近的感觉. . . "
    voice sustain

    #（此处切入线稿4，一个没有脸的大哥哥和两个已经长大了的孩子，只看得到腿部服装的二人）

    "我们长大了之后"
    "小岩哥哥还是那样子的模样，甚至连他的内心好像都没怎么变化过"
    "尽管我和蘭早就过了那样的年纪，但是自称是“岩崎天桐”的他仍然保持着和我们小时候一样的稚气"
    "除此之外，岩崎天桐带给我的全部都是真真切切的“真实感”"
    "仿佛，他就是一个除了稍微中二一点的个性外，完完全全和常人无异的普通高中生"
    "要是我也能有这样一个极具真实感的姐姐就好了。哪怕是一个仿生机器人也足够满足我的各种幻想了. . ."
    "但有时，这样的真实感却会让让我背后一凉. . . . . ."
    "很多年之后，或许我就不能分辨出人和真正的机器人的区别"
    "这还是很让我后怕的想法. . ."


    who "盯. . . . . ."
    "突然之间，我感觉到背后好像有什么东西在看着我一样"

    #（放出Q版的初咲恋柚正在海川渡身后扒着墙，还有一个电线杆）

    ch "这是. . . . . ."
    play music "bgm/九衢长街/九衢长街新版.mp3"
    "一个看起来怪怪的少女正躲在墙的后面偷偷地盯着我"
    "或许. . .是我的错觉？"
    "我转过身，再往前踏一步，余光留意着我身后那个女生"
    #voice ""
    #（播放细细簌簌的声响声）
    "少女也跟随着我的步伐又往前走了一步"
    ch "你这也太明显了！"
    ch "出来吧，我都注意到你在我背后跟踪了！"
    #（后续初咲一直采用日语对话）
    #show
    who ". . ."
    "少女从墙边走了出来，带着一股我熟悉的冷峻感"
    ch "秋月？！！"
    "不经意间，我立刻想起了这个名字，然后很快就脱口而出了"
    "但是少女并没有注意我说的话，径直向我走来"
    ch "你. . ."
    "从刚才我就看出来了，少女的手上持着一个亮闪闪的，可以反光的长柄物"
    "那是. . ."
    "随着她慢慢地向我走进，我也逐渐看清楚了那个东西. . ."
    "刀！"
    "那是一把刀！"
    "虽然在这个叫做“刀”的东西现在已经不常见了，但我记得小时候在母亲做菜的时候用过. . ."
    "看着阴沉的少女越走越近，我却因为无端的紧张感变得无法动弹. . ."
    "给我动起来啊，该死的. . ."
    "我不断催促着自己的大脑让自己迈开双腿跑起来"
    "但这样似乎并没有什么用处"
    "瘫软的双腿让我一下子跌坐在地上"
    "动啊！"
    "动啊！"
    "动啊！"
    "可是此时，少女已经走到我的面前，把那柄蓝色纹理的刀缓缓地高举起来"
    "在此刻，我的脑海中浮现出了各种和“死”有关的画面. . ."
    #voice ""
    #（播放效果音：撕裂声，又像是血溅出来的音效，黑频）

    #第一个cg：从类似倒在地上的人眼中模糊看清的感觉，在视觉的中心是一个模糊的少女的脸，可以看到初咲恋柚像是在男主的上面，举着刀，要记得使屏幕颤动）
    "有人说在临死的时候，一生的所有记忆会短暂地从大脑中流过"
    "如同播放电影一样. . ."
    "失重感. . .目眩感. . .以及恶心到想吐的恐惧感"
    "可是眼前的少女却怎么样都无法从我的眼前消失掉. . ."
    voice "voice/cxly_voice/episode1/初咲012.mp3"
    who "提问："
    voice sustain
    voice "voice/cxly_voice/episode1/初咲013.mp3"
    who "由中国代表在联合国大会上提倡的新世代三个核心词是？"
    ch "嗯？"
    ch "这是. . ."
    ch "日语？"
    ch "你. . .说什么"
    "我用尽龟裂的嘴唇，在这种介于恐惧和无感的心情中缓缓地抛出了我的疑问。"
    "可能. . .升入天国之后，事情变得奇怪也很正常吧. . ."
    voice "voice/cxly_voice/episode1/初咲012.mp3"
    who "提问："#（用稍微冰冷一点的，机械的语气说）”
    voice "voice/cxly_voice/episode1/初咲013.mp3"
    who "由中国代表在联合国大会上提倡的新世代三个核心词是？"#（用稍微冰冷一点的，机械的语气说）”
    voice sustain
    ch "啊咧？"
    voice "voice/cxly_voice/episode1/初咲012.mp3"
    who "提问："
    voice "voice/cxly_voice/episode1/初咲013.mp3"
    who "由中国代表在联合国大会上提倡的新世代三个核心词是？"
    voice sustain
    ch "眼前的少女机械地重复着这个问题，好像是下定了决心要从我这里问出答案一样"
    voice sustain
    ch "少女把那柄小刀悬停在半空中"
    voice sustain
    ch "微微颤动的刀片在阳光的反射下"
    voice sustain
    ch "我想想. . ."
    ch "‘幸福’，‘未来’和‘爱’？"
    #voice ""
    who "回答正确！"#（非常高兴的声音）
    voice "voice/cxly_voice/episode1/初咲014.mp3"
    "少女脸上僵硬的表情逐渐隐去，取而代之的是她灿烂的笑容"
    voice sustain
    #（露出嘴角图片，初咲的微笑）
    #voice ""
    #（播放效果音：从地上把海川渡扶起来，带有摩擦感的声音）
    voice "voice/cxly_voice/episode1/初咲015.mp3"
    who "嘿咻，嘿咻"
    ch "当我还没有从刚才紧张压抑的氛围中喘过气来，少女就一把把面无血色的我从地上拉了起来"
    voice "voice/cxly_voice/episode1/初咲016.mp3"
    who "没事吧？"
    ch ". . ."
    ch "！！！"
    ch "你. . .你不要过来啊. . .！"

    #（此时的cg转化为背景图）

    "我下意识地往后退了一步. . ."
    "少女也随即向前跟进了一步"
    ch "你. . .你. . . "
    voice "voice/cxly_voice/episode1/初咲017.mp3"
    who "诶. . .？"
    "少女似乎是注意到了我对她害怕的情绪，慢慢地把那柄小刀放在地上，慢慢举起手来"
    voice "voice/cxly_voice/episode1/初咲018.mp3"
    who "抱歉抱歉！"
    voice "voice/cxly_voice/episode1/初咲019.mp3"
    who "因为太喜欢这种形式的表演了. . .所以才会对海川. . ."
    voice "voice/cxly_voice/episode1/初咲020.mp3"
    who "不过你放心，我对你是完全没有恶意的！"
    ch ". . . . . ."
    ch ". . . . . ."
    voice "voice/cxly_voice/episode1/初咲021.mp3"
    who "这个只是演出用的伸缩刀，完全不会有任何危险的！"
    "说完，少女还把刀片往自己的脑门上顶了顶，果然和道具一样地缩回去了"
    ch ". . . . . ."
    voice "voice/cxly_voice/episode1/初咲022.mp3"
    who "抱歉抱歉！无论海川有什么要求，初咲都会补偿的！"
    ch ". . ."
    ch "这种性质恶劣的整蛊就不要随便用来吓人啊！"
    #voice ""
    #（播放效果音："扑通"，土下座的声音）

    "这位与我素未谋面过的少女羞红着脸，先是不断地对我点头鞠躬，然后直接铺在地上，不断对我行着异域熟悉的道歉礼数"
    ch "诶. . .你也别这样. . .快站起来啊喂！"
    voice "voice/cxly_voice/episode1/初咲023.mp3"
    who "这样是被海川允许的吗？！"
    voice "voice/cxly_voice/episode1/初咲024.mp3"
    who "！谢谢！"
    "她扑打着身上刚刚因为“土下座”而沾染的灰尘，冲着我再次绽放了花一般的笑容"
    ch "那个. . ."
    "我抬起头，突然发现少女的样貌有种不自然的违和感. . ."
    "说起来的话，简直和我在九衢实验高中认识的一个女生太像了. . ."
    "一样不寻常的银白色头发，甚至连那双眼睛都有着一样的灵动感. . ."
    "不过仔细一看还是能看出一点区别的"
    "比如这身这么熟悉的制服. . ."
    "这不是刚才蘭也穿的那一件吗！"
    "她怎么也穿着东番的校服？"
    "还有. . .她是怎么知道我的名字的？"
    voice "voice/cxly_voice/episode1/初咲025.mp3"
    who "你好，我叫‘初咲恋柚’"
    "这是在向我打招呼. . .？"
    "要说起日语，我还只是在备战交换生项目的时候学过一点"
    "虽然说我还算是有半个日本血统. . .可真是令人惭愧. . ."
    ch "你好，我是海川渡。"
    #show
    voice "voice/cxly_voice/episode1/初咲026.mp3"
    cq "唔. . ."
    "名叫初咲恋柚的银白发少女仔仔细细地盯着我的脸，"
    "然后绕到了我的背后，认真地打量着我身上的每一个部分"
    #show
    voice "voice/cxly_voice/episode1/初咲027.mp3"
    cq "果然，"
    #show
    ch "喂喂！这会让人很不自在的"
    "然后少女又慢悠悠地转到我的面前"
    #show
    voice "voice/cxly_voice/episode1/初咲028.mp3"
    cq "呐，海川君。我听说过你！"
    #show
    voice "voice/cxly_voice/episode1/初咲029.mp3"
    cq "是一个很温柔的男生对吧"
    ch "蛤？？？"
    "在我看来，名为“初咲恋柚”的少女快速的日语让我一下子没有反应过来她的意思"
    ch "抱歉，你刚刚说的是. . .我没有听清"
    #show
    voice "voice/cxly_voice/episode1/初咲030.mp3"
    cq "我说，"
    #show
    voice "voice/cxly_voice/episode1/初咲031.mp3"
    cq "海川君，"
    #show
    voice "voice/cxly_voice/episode1/初咲032.mp3"
    cq "是~一~个~温~柔~的~人~噢"#（一字一顿）
    "眼前的这个自称是初咲恋柚的女生突然凑近到我的面前，对我微笑着"
    #voice ""
    #（播放效果音："咚"）
    "一不小心，我再次被这个女生逼倒在地"
    ch "嘶"
    ch "好疼"
    "看着我摔倒在地，初咲恋柚的脸上露出了些许歉意的表情，伸手把我扶了起来"
    "不经意间，我发现初咲恋柚的手上和小腿上有一些淤青的伤痕，看上去是最近才出现的"
    #show
    voice "voice/cxly_voice/episode1/初咲033.mp3"
    cq "抱歉抱歉"
    #show
    voice "voice/cxly_voice/episode1/初咲034.mp3"
    cq "一不小心就调皮了一下，快站起来吧~"
    "说完，还不忘吐吐舌头，朝我不自然地笑了笑"
    "真是让我感到生气但又完全对她这副样子发不起火来"
    #show
    voice "voice/cxly_voice/episode1/初咲035.mp3"
    cq "容许我重新自我介绍一下，"
    #show
    voice "voice/cxly_voice/episode1/初咲036.mp3"
    cq "主人给我取的名字是‘初咲恋柚’"
    #show
    voice "voice/cxly_voice/episode1/初咲037.mp3"
    cq "是型号为‘JAPAN-20500101-LASER-PTF-04’的新世代仿生机器人"
    voice sustain
    "在初咲恋柚故意放慢给我听而采用的一字一顿的自我介绍中，我凭借我薄弱的日语水平勉强听懂了初咲恋柚在说什么"
    voice sustain
    "原来只是个机器人. . .刚刚在报自己的型号是吗. . .？"
    voice sustain
    "这样说来. . .刚刚那些怪异的行为归结为程序运行的结果也能得到解释了. . ."
    voice sustain
    "可是这种机器人还真是少见. . .白色头发的. . .而且还说着日语. . ."
    voice sustain
    "好像只有小时候和父亲回到日本老家的时候看到过那边的人才会有“白毛控”这种说法. . ."
    voice sustain
    "这个时候的我才开始仔仔细细地打量着眼前的这个看似就是一个普通少女的初咲"
    voice sustain
    "不，准确地来说，眼前的这个机器人少女并不普通. . ."
    voice sustain
    "至少是在我的审美中，这可以算的上是极具青春气息的女生. . .白净的肌肤. . .微红的脸蛋. . .还有极为小巧精致的身材. . ."
    voice sustain
    "简直就是为一个喜欢“妹妹”类型的男生精心打造的. . ."
    voice sustain
    "只可惜是一个机器人，很多方面还是能看出来与真人有所去别的"
    voice sustain
    "注视着初咲恋柚的笑脸，我突然察觉到了刚刚说的话里好像有什么不对劲的地方"
    voice sustain
    "等等. . .日本话？？！"
    ch "初咲，你能再报一遍你的型号吗？"
    "我用撇脚的日语急促地说着这句话，"
    "但初咲好像没有听懂我说的话"
    #show
    voice "voice/cxly_voice/episode1/初咲038.mp3"
    cq "可以不用日语对我说噢"
    #show
    voice "voice/cxly_voice/episode1/初咲039.mp3"
    cq "中文的话初咲也是能够勉强听懂的"
    "哦对，仿生机器人好像在设计上搭载了翻译的功能，至于输出嘛. . ."
    "好像就只能采用一种语言的形式输出"
    "真是令人烦心的设定. . ."
    "不过对于我这种日语半吊子，看上去也刚好能勉强听懂"
    #show
    #voice "voice/cxly_voice/episode1/初咲034.mp3"
    cq "今天能遇上海川君真是太走运了"
    ch "对了？你是怎么知道我的名字的. . .还有，你怎么知道我会在这里？"
    #show
    #voice "voice/cxly_voice/episode1/初咲035mp3"
    cq "哼哼. . .不过这些都只是在我的计算中，我早就料到了海川君会走这一条回家的小道. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲036.mp3"
    cq "呐，看得出我还是很了解你的！"
    "但是无论初咲说什么，盘旋在我心里的只有另一个更可怕的事实. . . . . ."
    ch "初咲，很抱歉打断你，"
    ch "能再报一遍你的型号吗？"
    #show
    #voice "voice/cxly_voice/episode1/初咲037.mp3"
    cq "欸？"
    #show
    #voice "voice/cxly_voice/episode1/初咲038.mp3"
    cq "是‘JAPAN-20500101-LASER-PTF-04’呀"
    #show
    #voice "voice/cxly_voice/episode1/初咲039.mp3"
    cq "是有什么很奇怪的地方吗？"
    "初咲恋柚用着让我极不自然的天真眼神盯着我，好像能一眼把我看穿的那样"
    ch "‘JAPAN-20500101-LASER-PTF-04’. . ."
    "我喃喃自语地念着初咲恋柚说出的型号，看着眼前的初咲恋柚，只觉得她越来越遥远"
    "我甚至不知道该用什么样的眼神看着她"
    "日语，JAPAN，中国，仿生机器人. . . . . ."
    "似乎是所有线索在一瞬间得到收束，一切都有了合理的解释"
    "大概发生在她身上的故事应该就是按照我想象中的剧情展开的吧"
    ch "‘JAPAN-20500101-LASER-PTF-04’. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲040.mp3"
    cq "对的哦，很快记下来了嘛，很不错！"
    ch "听我说，初咲，"
    #show
    #voice "voice/cxly_voice/episode1/初咲041.mp3"
    cq "嗯？"
    #show
    #voice "voice/cxly_voice/episode1/初咲042.mp3"
    cq "什么事？"
    ch "听我说，初咲，"
    ch "你应该不是在中国产出的机器人对吧？"
    ch "初咲恋柚又摆出那个仔细盯着我看的眼神，愣在原地好一会儿。"
    #show
    #voice "voice/cxly_voice/episode1/初咲043.mp3"
    cq "嗯？"
    #show
    #voice "voice/cxly_voice/episode1/初咲044.mp3"
    cq "当然是日本的啦！"
    #show
    #voice "voice/cxly_voice/episode1/初咲045.mp3"
    cq "难道海川君不认识英语吗？"
    #show
    #voice "voice/cxly_voice/episode1/初咲046.mp3"
    cq "明明在我的铭牌上写的是‘JAPAN’欸。"
    ch "我当然知道，对于即将升入东番国立高大仿生机器人制造技术的我来说，这点常识都是扎根在我记忆中的"
    #show
    #voice "voice/cxly_voice/episode1/初咲047.mp3"
    cq "而且我是在laser精工，东京总部生产的最新，优秀且高端的仿生机器人噢！"
    ch ". . . . . ."
    "初咲恋柚若无其事的回答让我陷入思索"
    "根据国家的“三十二条禁令”，在中国的国土上就根本就不可能出现日本产的机器人. . ."
    "面前的这个机器人少女，很有可能关乎到严重至违法犯罪的事情啊！"
    "难道. . .这个机器人少女. . .背后是有什么隐情吗？"
    ch "那初咲，你的主人呢？"
    "听到了我微微颤抖的声音后，初咲恋柚慢慢抬起头，露出了冰雪般伤感的神情，似乎在犹豫着要不要说出来给我听"
    #show
    #voice "voice/cxly_voice/episode1/初咲048.mp3"
    cq "你说主人吗？"
    #show
    #voice "voice/cxly_voice/episode1/初咲049.mp3"
    cq "出来旅行的主人把我落在了九衢市，然后就不见了"
    #show
    #voice "voice/cxly_voice/episode1/初咲050.mp3"
    cq "我一直一直都在寻找主人的踪迹. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲051.mp3"
    cq "跑遍了整个九衢市，问了好多好多人都没有找到主人在哪个地方"
    "说完初咲恋柚还用手臂框成了一个大大的圆形，竭力向我表现出在寻找主人历程上的重重艰辛。"
    #show
    #voice "voice/cxly_voice/episode1/初咲052.mp3"
    cq "不过好在，后来我很意外地收到了主人从日本发来的信"
    #show
    #voice "voice/cxly_voice/episode1/初咲053.mp3"
    cq "大概意思就是主人已经回到了日本，但不小心把我忘记在了九衢市"
    ch ". . . . . ."
    "哪里会有人这么随便就忘记的啊？！"
    "明明是一直陪伴在身边的，怎么可能把这么一大个机器人随便丢下呢？"
    "更何况像这个我面前的这个少女的型号，看上去完全是新型的类型，在我心中估算的价格也肯定不便宜. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲054.mp3"
    cq "主人也真是的. . .明明没有亲口和我说，还要让我自己找一个新的主人. . .这让初咲该怎么办啊？"
    "眉头微皱的初咲叹了口气，看上去像是非常为难的样子"
    "据我所知，在没有得到主人的亲口允诺下，机器人是绝对不能轻易地更换主人的。"
    "初咲恋柚低下头，沉浸在回忆中，又似乎想鼓起勇气说出什么话"
    #show
    #voice "voice/cxly_voice/episode1/初咲055.mp3"
    cq "所以，这也是我来找海川君的原因！"
    #show
    #voice "voice/cxly_voice/episode1/初咲056.mp3"
    cq "我一定要去. . .不对，回到日本，然后找到原来的主人！"
    "初咲恋柚低下头，沉浸在回忆中，好像并没有听出来我的害怕和担心"
    #show
    #voice "voice/cxly_voice/episode1/初咲057.mp3"
    cq "海川君能帮助我吗？"
    "眼前的少女用猫般的眼神可怜巴巴地看着我，就像路边流浪的那种可爱小猫一般. . ."
    "倒不如说，她现在正处于这种情况中。"
    ch "帮你？我这种人该怎么帮到初咲啊？"
    ch "明明我就是一个普通到再也不能普通的高中生而已。"
    #show
    #voice "voice/cxly_voice/episode1/初咲058.mp3"
    cq "不，"
    ch "初咲恋柚摇了摇头，换成了一个更加坚定的眼神注视着我"
    #show
    #voice "voice/cxly_voice/episode1/初咲059.mp3"
    cq "只需要海川君帮我带到日本去就行了！"
    ch ". . . . . ."
    ch ". . . . . ."
    ch ". . . . . ."
    ch "初咲，"
    #show
    #voice "voice/cxly_voice/episode1/初咲060.mp3"
    cq "在！"
    ch "虽然我们在五分钟前才刚刚认识"
    ch "帮助陌生人这件事上我也不是很反感"
    ch "但是这种冒巨大风险的事情我不能承担的起. . ."
    ch "更何况. . .我还只是一个普通的学生，我想不到该用什么办法. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲061.mp3"
    cq "我. . .我还有些钱！"
    #show
    #voice "voice/cxly_voice/episode1/初咲062.mp3"
    cq "一天500元以内的话，我是可以付得起的！"
    #（如果可以的话，红色标注，补充注释：500元钱的具体价值，很低，相当于现代社会的100r）
    #阿伟的话：可以在初咲这句话后加上一句专门的说明。例如”（500元钱的具体价值，很低，相当于现代社会的100r）“，玩家是能理解作者这里是想要说明世界观里面的细节的(应该？)
    ch "这不是用钱能解决的问题！"
    #show
    #voice "voice/cxly_voice/episode1/初咲063.mp3"
    cq "唔. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲064.mp3"
    cq "那再加上额外的照顾服务！我可以陪在海川君的旁边，家务活都由我全包了！还是免费的哟！"
    ch "等下，问题不在这里啊喂！"
    #show
    #voice "voice/cxly_voice/episode1/初咲065.mp3"
    cq "海川君如果还不满足的话. . .就当我的临时主人吧！"
    #show
    #voice "voice/cxly_voice/episode1/初咲066.mp3"
    cq "海川君有什么命令的话初咲都会服从的！"
    #show
    #voice "voice/cxly_voice/episode1/初咲067.mp3"
    cq "My Master~"
    "初咲恋柚又向我走进了一步，轻轻向我的脖颈处吐了一口气"
    "对我来说，少女脸上的微红在这样的距离下显得格外危险"
    "就算我知道是仿生机器人的事实. . ."
    ch "不行！"
    "在这样的攻势下，我又往后退了一步"
    ch "其他的都好说，但是把你带回日本去基本上是不可能的"
    #show
    #voice "voice/cxly_voice/episode1/初咲068.mp3"
    cq "为什么呢？"
    #show
    #voice "voice/cxly_voice/episode1/初咲069.mp3"
    cq "如果要去东京的话，海川君应该是没有别的机器人一起陪同吧？"
    "初咲指了指我手上揣着的校服，一幅好像什么都了然于心的表情看着我"
    ch "？！"
    ch "你怎么知道东东京. . .不对. . ."
    ch "还有，你是怎么知道我是. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲070.mp3"
    cq "一个叫‘蘭’的姐姐告诉我的"
    #show
    #voice "voice/cxly_voice/episode1/初咲071.mp3"
    cq "还有你看. . .这件校服，也是那个叫‘蘭’的姐姐送给我的！"
    ch ". . . . . ."
    "我早就应该猜到的"
    "从初咲身上穿着的这套标准的东番国立高大的制服来看，很明显就是刚刚我在办理手续时留下来的那件"
    ch "所以说，是那个叫‘蘭’的姐姐把我介绍给你的？"
    #show
    #voice "voice/cxly_voice/episode1/初咲072.mp3"
    cq "没错！"
    #show
    #voice "voice/cxly_voice/episode1/初咲073.mp3"
    cq "姐姐还说了："
    #show
    #voice "voice/cxly_voice/episode1/初咲074.mp3"
    cq "‘如果是海川渡的话一定会帮你的’"
    #show
    #voice "voice/cxly_voice/episode1/初咲075.mp3"
    cq "然后，"
    ch "然后？"
    #show
    #voice "voice/cxly_voice/episode1/初咲076.mp3"
    cq "我就来找你了"
    ch ". . . . . ."
    "那家伙还真是会把烫手山芋传递给别人啊. . ."
    "少女把头往右边一偏，看来是完全不能理解我说的话"
    ch "总之就是不行！"
    #show
    #voice "voice/cxly_voice/episode1/初咲077.mp3"
    cq "为什么？海川君的话肯定可以做到的！"
    ch "因为. . ."
    "看着眼前初咲很是期待的目光，我犹豫了一下"
    "如果初咲恋柚知道“三十二条禁令”的内容，就能很容易猜到她的主人完全不是无意把她扔在九衢市的. . ."
    "肯定会对她造成不小的打击吧. . .？"
    "我绕过初咲恋柚，径直从她身旁走过了"
    #show
    #voice "voice/cxly_voice/episode1/初咲078.mp3"
    cq "等等. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲079.mp3"
    cq "海川君真的没有办法吗？"#（伤心语气）
    "初咲恋柚压低了自己的声音，显得格外委屈，让我不自觉停下脚步"
    "我抑制住回头的冲动，不希望因为看到初咲恋柚那张可爱的脸蛋就做出反悔的抉择"
    ch "对不起. . ."
    "说完了这句话之后，我怀着不可名状的心情跑开了"

    #（以下两句话插入背景图片的转换，让玩家感受到一个正在"移动"的感觉，包括："公园，下午"，"九衢の街2，下午"）

    "明明是那个叫做“初咲”的机器人求我把她带到东京. . ."
    "为什么我会感觉到内心的负罪感好重. . ."

    #（切换场景：家门口的背景）

    ch "直到来到家门口，我仍然无法抹去刚刚和她说的话"
    #（这里插入暗黄色色调+
    #show
    #voice "voice/cxly_voice/episode1/初咲080.mp3"
    cq "海川君如果还不满足的话. . .就当我的临时主人吧！"
    #show
    #voice "voice/cxly_voice/episode1/初咲081.mp3"
    cq "海川君有什么命令的话初咲都会服从的！"
    #show
    #voice "voice/cxly_voice/episode1/初咲082.mp3"
    cq "My Master~"
    #）
    "喂喂，我都在想些什么啊！"
    "算了. . .忘记那个叫“初咲”的机器人吧. . .反正也和我没什么关系"

    #（切换场景：客厅的背景，稍微带一点科技感）

    ch "我回来了！"
    "打开门后，我习惯地向家里说了这句话"
    "没有人答应我"
    "原来都走了啊. . ."
    "空无一人的家中就剩下了我一个人站在原地"
    #（从客厅的背景转到房间里的背景，稍微带一点科技感）
    ch "算了，今天早上起这么早，也应该好好休息一下了"
    #voice ""
    #（播放"咚"，倒在床上的效果音）

    #（切换到天花板上和一个灯的背景）

    "我倒在床上，注视着天花板上的灯"
    #（这里插入暗黄色色调+
    #show
    #voice "voice/cxly_voice/episode1/初咲057.mp3"
    cq "海川君能帮助我吗？"
    "先别说帮助她了，在我的面前摆放着一条不能逾越的法律鸿沟——"
    "三十二条禁令"
    "这是一个由中国，美国，俄罗斯等诸多非日本的发达国家基于laser精工带头制作的仿生机器人而提出的三十二条规则约束"
    "简单来说，就是为了维护社会的稳定秩序和发展，针对仿生机器人制造上提出的明文禁令"
    "在备考东番国立高大的入学资格测试中，我就已经把这三十二条规则熟记于心了"
    "让我印象最深的就是一条由亚洲多个国家共同提起的，"
    "希望以此来保护本就岌岌可危的生育率的禁令——"
    "第十四条，仿生机器人在未经联合国仿生机器人委员会的审批同意，不得搭载‘爱恋’模块。"
    "虽然听起来有些好笑，但这确实是经过多次商讨，其他非日本国家得出的讨论结果。"
    "毕竟仿生机器人的个性和特征完全是按照个人的喜好打造的，而且最重要的就是"
    "仿生机器人会认主人，不会对除主人之外的人有二心。"
    "相比起一个人类异性，仿生机器人简直就是集成了每个人心中所向往的另一半的全部特征"
    "无论是谁，应该都会更偏向于选择搭载了先进的生物学模块的仿生机器人作为自己的伴侣吧"
    "还有两条也让我印象非常深刻的禁令——"
    "第三条，不得随意对仿生机器人进行改造，尤其是用于战争行为和使用武器等行为的模块构建. . . . . ."
    "第二十八条，各国不得放宽国内对仿生机器人的保护法律，要尽可能使仿生机器人获得和人平等的待遇和权力。对其物品性和拟人性要经过充分的，科学的考量. . . . . ."
    "但最重要的，还是一条有关于日语提出的禁令——"
    "第二条，非日本区域的仿生机器人制造国家不得采用日语语言包作为仿生机器人的母语语言包。"
    "虽然这个看上去完全没有理由成为禁令中的一条，但它确实就这样存在在这三十二条之中，显得如此突兀"
    #（这里插入暗黄色色调+
    #show
    #voice "voice/cxly_voice/episode1/初咲044.mp3"
    cq "当然是日本的啦！"
    #show
    #voice "voice/cxly_voice/episode1/初咲045.mp3"
    cq "难道海川君不认识英语吗？"
    #show
    #voice "voice/cxly_voice/episode1/初咲046.mp3"
    cq "明明在我的铭牌上写的是‘JAPAN’欸。"
    #show
    #voice "voice/cxly_voice/episode1/初咲047.mp3"
    cq "而且我是在laser精工，东京总部生产的最新，优秀且高端的仿生机器人噢！"
    #）
    "尽管我在备考东番国立高大的入学资格测试的时候，也表现出了同样的疑惑，但是没有老师能够给我相关的解释"
    "大概是因为贸易原因吧. . .毕竟仿生机器人相对来说也是一个. . .贸易品？"
    "因为laser精工总部在日本的原因，搭载了先进系统的日产总是能利用系统更迭的时间差对各国的贸易经济造成不小的冲击。"
    "总之，能列在“三十二条禁令”上，想必也是和上述几条一样，会对国际社会带来不小的影响吧. . ."
    #（这里插入暗黄色色调+
    #show
    #voice "voice/cxly_voice/episode1/初咲083.mp3"
    cq "为什么？海川君可以利用入学要求把初咲带上的欸！"
    #）
    ch "我不知道该以什么样的心情看待今天突然闯进我生活的初咲恋柚"
    #（这里插入暗黄色黄色色调+
    #show
    #voice "voice/cxly_voice/episode1/初咲084.mp3"
    cq "你好，我叫‘初咲恋柚’"

    #show
    #voice "voice/cxly_voice/episode1/初咲048.mp3"
    cq "你说主人吗？"
    #show
    #voice "voice/cxly_voice/episode1/初咲049mp3"
    cq "出来旅行的主人把我落在了九衢市，然后就不见了"
    #）
    "初咲恋柚的话一遍遍冲击着我的思绪，一时之间我陷入了诸多想象——"
    ch "那样可爱的机器人，大概也是有一个非常可爱的主人吧. . .？"
    ch "或者说，她的主人仅仅只是一个健忘的冒失鬼，是真的把初咲恋柚给丢在了九衢市. . ."
    ch "事情应该不是我所想的那样糟糕吧. . ."
    #（这里插入暗黄色色调+
    #show
    #voice "voice/cxly_voice/episode1/初咲050.mp3"
    cq "我一直一直都在寻找主人的踪迹. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲051.mp3"
    cq "跑遍了整个九衢市，问了好多好多人都没有找到主人在哪个地方"
    #）
    ch "一直. . .一直都在寻找主人. . ."
    ch "等等. . ."
    ch "身为机器人的她应该还没有一个固定的住所，现在还是处在四处流浪的境地吧. . . "
    ch "不行"
    ch "我不能一口咬定初咲的主人就是那种在电影中看到的走私犯. . ."
    ch "而且根据初咲的发言，所谓的‘初咲的主人’根本就没有把初咲卖掉. . ."
    ch "应该. . ."
    #voice ""
    #（插入手机铃声的"叮"，开始播放广播~）
    "一不小心，我的手打在了旁边的这个被老爸称作‘收音机’的老旧玩意儿上，不知怎么地把它开启了"
    #voice ""
    jqgb "欢迎来到九衢之声，快来听听今天有什么新闻"
    #voice ""
    jqgb "据最新报道，九衢市近期出现了多起‘霸凌机器人’事件，据悉，事故多发于沙湖路段，在此，提醒各位主人保护好自己的机器人，目前相关的霸凌案件仍在调查中. . ."
    ch "霸凌机器人. . ."
    ch "沙湖路段. . ."
    ch "这不就是在这附近发生的事情吗？"
    #（这里插入暗黄色色调+
    "不经意间，我发现初咲恋柚的手上和小腿上有一些淤青的伤痕，看上去是最近才出现的"
    #）
    "我忽然想起了之前被初咲恋柚拉起来的时候看到的淤青的伤痕"
    "我慌乱地瞟了一眼旁边的时钟，"
    "上面赫然显示的是“19：52”"
    "按照冬令时的时间来算，现在天色已经完全黑下来了"
    ch "初咲有可能会遇到危险！"
    "来不及进行更多的思考，我随手关上了正在继续播放新闻的收音机，匆匆换上衣服，就直接从家里跑出去了"

    #（切换场景：九衢の街，晚上，切换场景+延时5s）

    ch "我来到这个白天和初咲恋柚相遇的这条街，着急地寻找着她的踪影"
    ch "尽管在路灯的照射下，整条街道显得空阔明亮无比，但是和往常一样的是，整条道路上没看到一个人影"
    ch "呼，到底在哪里？"
    ch "初咲？"
    ch "我试着用不是很地道的日语呼唤着她的名字，"
    ch "但空阔的街道没有给我任何回复"
    ch "四周的寂静犹如厉鬼一样悄声地压在我的身体上，给我一种强烈的不适应感和不安感"
    #（放效果音："沙沙"，像是树叶在地上被吹动的声音）
    ch "细细簌簌的声音忽然从眼前的路灯后发出来"
    ch "可以看得出来在路灯的照射下，好像有什么东西正在不断跃动着"
    ch "是初咲吗？"
    ch "我向面前的那个路灯慢慢摸索地前进过去"
    #voice ""
    ym "喵？"
    #（播放猫的效果音，最好有一种被寒冷的天气冻得有点说不出话的感觉）

    "在路灯的光线下，一只母猫正蜷缩着身体，为自己的幼崽做最后一层防寒的保护"
    ch "原来只是一群猫咪啊. . ."
    "我叹了口气，看着母猫在冷空气中瑟瑟发抖的样子，把身上的衣服脱了下来，披在了母猫的身上"
    #voice ""
    ym "喵！"#（播放猫的效果音，最好有感激的情绪在里面）
    ch "应该这样就会好很暖和很多吧. . ."
    #（放效果音："沙沙"，像是树叶在地上被吹动的声音）
    "不知道在什么时候，我没有注意到自己的背后已经出现了一个黑漆漆的影子，仿佛正在我的身后无声地注视着我地所作所为。"
    #show
    #voice "voice/cxly_voice/episode1/初咲1.mp3"
    cq "看来是海川君呢！"#（稍显冰冷）
    "熟悉的日语从我的耳边如和风一般溜过，我知道那是我想要找的人——"
    "但和预想中有点不一样的是，我的后背好像被一个坚硬而且冰冷的东西抵着"
    "轻微的不适感和刺痛感从背后的那一点开始慢慢散开在全身，就好像贯穿了我的整个神经一样"

    #（插入第一张cg：初咲恋柚在一个路灯下拿着一柄小刀抵着海川渡）（不要这张cg了）

    #show
    #voice "voice/cxly_voice/episode1/初咲084.mp3"
    cq "不要回头噢，海川君！"
    #show
    #voice "voice/cxly_voice/episode1/初咲085.mp3"
    cq "要不然很快就会. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲086.mp3"
    cq "没，命，噢~"
    "初咲用着戏谑的口吻调皮地说着这三个字"
    "在这样的黑夜中，显得异常诡异"
    "我大概已经猜到了，"
    "初咲抵住我的那个东西——"
    "是那柄货真价实的冷蓝色金属刀"
    ch "初. . .初咲. . .你在干什么啊？"
    #show
    #voice "voice/cxly_voice/episode1/初咲087.mp3"
    cq "难道海川君看不出来吗？"
    #show
    #voice "voice/cxly_voice/episode1/初咲088.mp3"
    cq "当然是. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲089.mp3"
    cq "杀，了，你，噢~"
    #（此处加入初咲恋柚吹气的声音）
    "初咲贴近我的耳朵边，缓缓地吹着气，用着看上去非常享受的神情不断提醒我就是案板上的牛羊，随时等待她的宰割"

    #（换回九衢の街，背景仍然为夜晚）
    #show
    #voice "voice/cxly_voice/episode1/初咲090.mp3"
    cq "开玩笑的啦~"
    "初咲收回了一直抵在我后背那个异常冰冷的家伙，用着浅浅地笑容看着我"
    ch "呼. . .呼，刚刚真是. . . 你到底是在干什么啊，这样的环境下真的很吓人的！"
    "尽管有了上次的经验，这次虽然不至于腿软到瘫倒在地. . .但这仍然让我的脖颈处生出了一股钻心的凉意"
    #show
    #voice "voice/cxly_voice/episode1/初咲091.mp3"
    cq "嘿嘿. . .抱歉啦"
    #show
    #voice "voice/cxly_voice/episode1/初咲092.mp3"
    cq "没想到海川君竟然会这么胆小. . .不过这么说过来，我的表演还是很成功的对吧？"
    ch "哪里是表演啊，不要再玩这种恶作剧了！"
    "不过作为表演的话，刚刚那种压迫感和切实的体验感着实可以称得上是一位优秀的表演者了"
    #show
    #voice "voice/cxly_voice/episode1/初咲093.mp3"
    cq "下次不会这样了. . ."
    #（换初咲恋柚哭脸的可爱表情）
    ch "不过还是很不错的. . .如果刚刚那个真的是表演的话，完全可以媲美真实的演出"
    #show
    #voice "voice/cxly_voice/episode1/初咲094.mp3"
    cq "真的吗！！！"
    ch "初咲恋柚在一瞬间就将脸上的神情转变为一个大大的兴奋脸"
    ch "嗯，确实是这样的. . .至少对于我这个半吊子的专业人士来看. . .特别是对一个机器人来说. . .已经非常厉害了 "
    #show
    #voice "voice/cxly_voice/episode1/初咲095.mp3"
    cq "谢谢！！！"
    #show
    #voice "voice/cxly_voice/episode1/初咲096.mp3"
    cq "海川君真是太好了！"
    "说完，初咲恋柚直接扑到了我的身上，给了我一个大大的拥抱"
    ch "够. . .够了. . ."
    "我有些尴尬地从初咲的怀抱里挣脱出来，轻轻地拍了一下她的头"
    ch "现在可不是陪你玩的时候"
    ch "你身上的这些伤口和淤青没事吧. . .？"
    "我俯下身，盯着眼前的这一块块不大不小的淤青和伤痕，不自觉地问道"
    #show
    #voice "voice/cxly_voice/episode1/初咲097.mp3"
    cq "没事的啦~"
    #show
    #voice "voice/cxly_voice/episode1/初咲098.mp3"
    cq "这点小伤口对我来说完全不算什么"
    #show
    #voice "voice/cxly_voice/episode1/初咲099.mp3"
    cq "还不是今天蘭姐姐送给我这件校服这么好看"
    #show
    #voice "voice/cxly_voice/episode1/初咲100.mp3"
    cq "然后走在路上一不小心给摔了一跤. . ."
    ch ". . . . . ."
    ch "原来根本就不是我想象中的那个样子啊. . .害得我还白白担心了一场"
    #show
    #voice "voice/cxly_voice/episode1/初咲101.mp3"
    cq "海川君. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲102.mp3"
    cq "哦不对！"
    #show
    #voice "voice/cxly_voice/episode1/初咲103.mp3"
    cq "是主人！"
    #show
    #voice "voice/cxly_voice/episode1/初咲104.mp3"
    cq "主人是终于决定带上初咲一起去日本了嘛！"
    ch ". . .不. . ."
    ch "只是担心你遇到危险所以才要带你回去的"
    #show
    #voice "voice/cxly_voice/episode1/初咲105.mp3"
    cq "危. . .险？"
    ch "嗯，最近九衢市经常出现霸凌机器人的事情. . .外面来说对你太危险了点"
    #show
    #voice "voice/cxly_voice/episode1/初咲106.mp3"
    cq "啊嘞？"
    #show
    #voice "voice/cxly_voice/episode1/初咲107.mp3"
    cq "还好啦"
    #show
    #voice "voice/cxly_voice/episode1/初咲108.mp3"
    cq "初咲我可是跑遍了整个九衢市都没有出任何问题的说！"
    ch ". . . . . ."
    "不知道为什么，在听了初咲说出了这句话后，我隐隐约约感觉到哪里有些奇怪，但说不出来哪里有些奇怪。"
    ch "先和我一起回家吧. . .之后的事情我会委托别人帮助你的. . ."
    "不管怎么样，先把初咲带回家才是当务之急。"
    #show
    #voice "voice/cxly_voice/episode1/初咲109.mp3"
    cq "这样啊. . ."
    "初咲的声音在那一瞬间低沉了下去很多"
    #show
    #voice "voice/cxly_voice/episode1/初咲110.mp3"
    cq "不过这样也好吧. . .主，人~"
    ch "别这样随便乱喊啊，我可没有同意和你有那样的交易！"
    #show
    #voice "voice/cxly_voice/episode1/初咲111.mp3"
    cq "好的好的，初咲是知道的噢。"
    "说完，初咲拉起我的手，朝着街的尽头跑去"
    #show
    #voice "voice/cxly_voice/episode1/初咲112.mp3"
    cq "快点跑起来吧,晚到的小孩可是要被批评的噢"
    ch ". . . . . ."
    "这一天，是我第一次握住女孩子的手. . ."
    "尽管我知道面前的只不过是一个仿生机器人而已，"
    "但是，"
    "初咲恋柚天真的笑容仿佛永远定格在九衢长街的那一晚"
    "就和真正的少女一样"
    "那样的纯真烂漫. . . . . ."

    #（背景转为：家门口，晚）

    #（放效果音：门铃声）
    #voice ""
    "初咲恋柚摁了摁门口这个老旧的门铃，非常有礼貌地站在门口静静地等待着"
    #show
    #voice "voice/cxly_voice/episode1/初咲113.mp3"
    cq "莫西莫西，请问有人吗？"
    ch "你放心，房子里面是没有人的"
    ch "快进去吧"
    #show
    #voice "voice/cxly_voice/episode1/初咲114.mp3"
    cq "是！"

    #（背景转为：带有一点科技感的客厅，晚）
    #show
    #voice "voice/cxly_voice/episode1/初咲115.mp3"
    cq "那个. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲116.mp3"
    cq "海川渡是一个人住在这里吗？"
    ch "这个嘛"
    ch "也不完全是，"
    ch "一个星期之前妈妈也住在这里面，不过她和爸爸都先我一步去日本了"
    ch "所以家里就只剩我一个人了"
    #show
    #voice "voice/cxly_voice/episode1/初咲117.mp3"
    cq "这样呀"
    #show
    #voice "voice/cxly_voice/episode1/初咲118.mp3"
    cq "那我就放心了"
    ch "放心什么？"
    #show
    #voice "voice/cxly_voice/episode1/初咲119.mp3"
    cq "我可以顺理成章地成为海川君的私人女仆了！"
    "看着空荡荡的客厅，初咲恋柚拿起了打扫用的扫帚，看上去很有干劲的样子"
    ch "不用这样的了，"
    ch "毕竟还有一个半月这个房子就用不到了"
    #show
    #voice "voice/cxly_voice/episode1/初咲120.mp3"
    cq "欸？为什么啊，明明看上去还没有旧到要卖出的地步吧？"
    ch "不是要卖掉"
    ch "因为一个半月之后我就要到东番去了，这间房子就没有人住了"
    #show
    #voice "voice/cxly_voice/episode1/初咲121.mp3"
    cq "唔呣. . ."
    "初咲恋柚直勾勾地盯着我看的眼神，让我忽然想起了那个女生——"
    "简直和她平时的习惯动作一模一样. . ."
    ch "那个，初咲"
    ch "你认识秋月吗？"
    #show
    #voice "voice/cxly_voice/episode1/初咲122.mp3"
    cq "唔呣. . ."
    "时间仿佛是在那一刻凝固了一样，初咲什么也没说，似乎是陷入了一会儿思考，但很快抬起头"
    #show
    #voice "voice/cxly_voice/episode1/初咲123.mp3"
    cq "报告主人，在我的记忆中完全没有检索到一个名叫‘秋月’的女生"
    ch "这样啊. . ."
    ch "应该是我太自作多情了点. . .明明初咲恋柚来自日本，又怎么可能会和那个女生牵扯上关系呢. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲124.mp3"
    cq "请问，主人说的这个‘秋月’，是个什么样的人呢. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲125.mp3"
    cq "如果有更多信息的话，初咲觉得自己应该能从九衢市居民名单上检索到主人想找的人"
    ch "没什么，只不过是长得和你很像而已. . ."
    ch "然后一直有件事想向她亲口说出来. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲126.mp3"
    cq "欸~！"
    #（拉长音）
    #show
    #voice "voice/cxly_voice/episode1/初咲127.mp3"
    cq "这种感觉. . .不会是. . .主人喜欢的人吧！？ "
    ch "不要乱讲啊喂！"
    ch "只是简单的朋友关系而已"
    ch "完全没有到那种地步. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲128.mp3"
    cq "真的只是‘而已’吗？ "#（拉长音）
    ch "好了好了，你也别吵了，今天就在客厅好好呆着，哪里都不要去"
    #show
    #voice "voice/cxly_voice/episode1/初咲129.mp3"
    cq "哈"#（打哈欠的声音）
    #show
    #voice "voice/cxly_voice/episode1/初咲130.mp3"
    cq "海川君，我要没电了. . .好困. . ."#（困倦语气）
    ch "啊嘞？"
    ch "原来机器人也需要充电的吗？"
    #show
    #voice "voice/cxly_voice/episode1/初咲131.mp3"
    cq "肯定啊. . .不然我该怎么工作啊. . ."#（困倦语气）
    ch "好的，我给你找一下适合你的充电器. . ."
    "眼前的初咲恋柚完全没有了刚刚的活力，看上去就是从一只活蹦乱跳的兔子一头撞上树干上那种一蹶不振的感觉"
    "摇摇摆摆的初咲如同刚刚酩酊大醉的少女般，"
    #show
    #voice "voice/cxly_voice/episode1/初咲132.mp3"
    cq "主人要记住噢. . .初咲的电量就算是满的也只能供应一天. . ."#（困倦语气）
    ch "找到了，给！"

    #（这里可以插入Q版的初咲恋柚拿着一个插头，摇摇晃晃的样子）

    "初咲拿起我递给她的插头，摇摇晃晃地走向离她最近的那个充电口"
    #voice ""
    #（播放效果音：嘟嘟滴，充上电的声音）
    #voice ""
    #（播放效果音："咚"，像是重物砸地板的声音）
    "果然在踉跄中，初咲还是没有平衡好自己的身体，重重地摔在地上"
    ch "没事吧？"
    ch "我赶快走上前去，"
    #show
    #voice "voice/cxly_voice/episode1/初咲133.mp3"
    cq "我没事的. . ."

    #（转到CG2：初咲恋柚的睡颜，背景墙壁，旁边有一个插线头）

    "说完，初咲像是沉沉地睡过去了一样，完全看不出来和真人睡觉有什么区别"
    "修长的睫毛，红扑扑的脸蛋，加上仔细看才能看到初咲的眼角泛起的因困倦形成的小泪花，在灯光的照射下宛若水晶般的绝美雕塑一般 . . . . ."
    "文静状态下的初咲如同一个挂在博物馆的一幅无人问津的画这样美丽"
    ch "好漂亮. . ."
    "我不由得为人工制造的这玩意儿而啧啧称叹"
    "尽管我知道仿生机器人根本就不会像人类一样生病感冒"
    "但是我仍然取下自己的最后一层外套，轻轻地披在了初咲的身上，生怕惊扰到她"
    "哦对，还有她的伤口！"
    "我放轻脚步，从房间中拿出一瓶蒸馏水，用棉签细致地涂在初咲受伤的小腿上，然后用毛巾擦去了剩下的水渍。"
    ch "这样应该会好一点吧"
    ch "还好我了解一点仿生机器人的基本构造. . ."
    ch "虽然仿生机器人根本就不用像一般人一样担心什么感染，生病的问题。"
    ch "但这种仿生皮肤仍然是用货真价实的生物制材料做成的，在保养上仍然需要下很大功夫才能一直维持它崭新出厂的样子。"

    #（此处镜头移动，不放文字，从右下角缓缓移动到镜头左上角，最终聚集在初咲的脸上，下次点击造成全图放大，变回全图）

    ch "好，完成了"
    ch "剩下的就是等着慢慢自我愈合"
    "我满意地看着自己的作品，收起药剂盒，回到房间里，轻轻地把门带上了，努力不发出一点声响"

    #（此处cg中的初咲眼角处的泪花变成了眼泪，缓缓地流了下来）

    #show
    #voice "voice/cxly_voice/episode1/初咲134.mp3"
    cq "我到底应该怎么办. . ."
    #show
    #oice "voice/cxly_voice/episode1/初咲135.mp3"
    cq "秋月. . ."

    #（此处背景转到房间，晚上）
    #voice ""
    #（播放倒在床上的效果音，"啪"）
    "我径直倒在床上"
    "今天连澡都没有洗. . ."
    "按照平常的惯例，现在应该是一天中最放松的时间"
    "但我的神经紧绷地有点无法松弛"
    ch "电话. . ."
    ch "对，电话"
    ch "现在最重要的是给蘭那家伙打个电话. . ."
    ch "她到底在想些什么啊. . ."
    "我熟练地摁下了那一串熟悉的数字，拨通了那个电话"
    #voice ""
    #（播放电话拨号的效果音，"嘟嘟嘟"）
    #voice ""
    #（播放电话接通的效果音，电话声 "滴"（此处为接通了的效果音））

    #（背景跳转到天花板上的灯）

    ch "喂喂，是蘭吗？"
    voice "voice/yqtt_voice/episode1/岩崎(电)001.mp3"
    voice sustain
    who "喂喂，这边是来自深渊的接应员"#（本句及以下岩崎天桐的话采用半日半中的方式）
    ch "这样的回答，也只可能是那个被蘭称作“中二机器人”了. . ."
    ch ". . . . . ."
    ch "岩崎，别开玩笑了，蘭在不在，是很重要的事情"
    voice "voice/yqtt_voice/episode1/岩崎(电)002.mp3"
    voice sustain
    yq "放心，就让深渊来给你想要的答案吧~"
    ch ". . . . . ."
    ch "你再这样说话我就要挂电话了"
    voice "voice/yqtt_voice/episode1/岩崎(电)003.mp3"
    voice sustain
    yq "诶诶，别着急别着急，我才哄完小蘭睡着"
    voice "voice/yqtt_voice/episode1/岩崎(电)004.mp3"
    voice sustain
    yq "这边也只有我这一个接应人能回复你"
    voice "voice/yqtt_voice/episode1/岩崎(电)005.mp3"
    voice sustain
    yq "我猜. . .是关于初咲的事情对吧"
    ch "岩崎天桐总是能很敏锐地察觉到我的想法. . .这让我总以为他能完完全全看透我的心思"
    ch "是"
    ch "我说，蘭怎么把这件事情推给了我. . ."
    ch "她应该也知道把初咲送回日本基本上是不可能的事情对吧！"
    ch "还有你们为什么不把初咲交给警察来处理. . ."
    voice "voice/yqtt_voice/episode1/岩崎(电)006.mp3"
    voice sustain
    yq "诶，. . .你先别着急"
    voice "voice/yqtt_voice/episode1/岩崎(电)007.mp3"
    voice sustain
    yq "交给警察处置的话，想必下场就是被肢解开来，最后报废，这样很简单粗暴吧. . ."
    voice "voice/yqtt_voice/episode1/岩崎(电)008.mp3"
    voice sustain
    yq "但如果交给海川的话情况就会好转很多了. . ."
    ch "再怎么说，到日本去也要经历海关那一道关卡吧！这也肯定是违法的啊！"
    ch "不会有人真的愿意冒这样的风险吧！"
    ch "况且，你的主人肯定也不敢答应初咲的要求吧. . ."
    voice "voice/yqtt_voice/episode1/岩崎(电)009.mp3"
    voice sustain
    yq "这件事确实让我的主上大人很为难，"
    voice "voice/yqtt_voice/episode1/岩崎(电)010.mp3"
    voice sustain
    yq "不过主上大人本来是执意要帮助初咲的"
    voice "voice/yqtt_voice/episode1/岩崎(电)011.mp3"
    voice sustain
    yq "但如果帮她的结果就是我会留在九衢市"
    ch "留在. . .九衢市？"
    ch "什么意思？"
    voice "voice/yqtt_voice/episode1/岩崎(电)012.mp3"
    voice sustain
    yq "海川可真是不灵光啊"
    voice "voice/yqtt_voice/episode1/岩崎(电)013.mp3"
    voice sustain
    yq "就是字面意思"
    voice "voice/yqtt_voice/episode1/岩崎(电)014.mp3"
    voice sustain
    yq "我没办法再陪小蘭一起去东番了"
    ch "所以说. . .你们是想到了通过. . .项目？"
    voice "voice/yqtt_voice/episode1/岩崎(电)015.mp3"
    voice sustain
    yq "没错，就是利用东番国立高大的项目便捷之处"
    voice "voice/yqtt_voice/episode1/岩崎(电)016.mp3"
    voice sustain
    yq "正因为这个项目，你可以携带一个和我一样的仿生机器人. . ."
    voice "voice/yqtt_voice/episode1/岩崎(电)017.mp3"
    voice sustain
    yq "就算是海川担心的是能不能过海关"
    voice "voice/yqtt_voice/episode1/岩崎(电)018.mp3"
    voice sustain
    yq "我相信，以东番国立高大的名声，这样的一个新生独立通道也不会很难为人吧. . ."
    voice "voice/yqtt_voice/episode1/岩崎(电)019.mp3"
    voice sustain
    yq "刚好海川的项目上是没有申请填写机器人的对吧？"
    ch "我好像明白了"
    ch "但是. . ."
    voice "voice/yqtt_voice/episode1/岩崎(电)020.mp3"
    voice sustain
    yq "海川肯定不能理解主人不在身边的那种滋味吧. . .？"
    voice "voice/yqtt_voice/episode1/岩崎(电)021.mp3"
    voice sustain
    yq "那种感觉. . .是很不好受的"
    voice "voice/yqtt_voice/episode1/岩崎(电)022.mp3"
    voice sustain
    yq "小蘭如果哪一天不在了的话. . .我想我也会求着海川把我杀死吧. . ."
    ch ". . . . . ."
    "岩崎突然间的严肃气氛让我有些喘不上气来"
    "郑重起来的岩崎简直和平常的自己完全是两种感觉. . ."
    voice "voice/yqtt_voice/episode1/岩崎(电)023.mp3"
    voice sustain
    yq "总之回见了，挚友！明天下午，老地方不见不散"
    voice "voice/yqtt_voice/episode1/岩崎(电)024.mp3"
    voice sustain
    yq "你也早点休息吧"
    #voice ""
    #（播放电话挂断的效果音，"嘟嘟嘟"）

    #（背景跳转回房间的场景，夜晚）

    "我回想着岩崎对我说的所有话，忽然感觉到一阵寒意袭来"
    ch "竟然有这么严重吗. . .对于仿生机器人来说. . .自己的主人是这样的一个存在"
    #（此处插入初咲不停地呼唤海川渡为"主人"的场景）
    ch "我又在想些什么啊"
    ch "虽然，我并不反感她用‘主人’这样的方式叫我. . ."
    ch "但在初咲的心中，我又是一个怎么样的存在. . ."
    ch "只是一个临时主人吗. . ."
    "我轻轻推开了房门，看了一眼坐在地上仍然在充电的初咲"
    "我不忍心打破这静谧的氛围，很快就把房门关上了"
    ch "哎"
    "我轻轻地叹了一口气，打开了办公用的电脑，上面赫然写着的时间“22：13”"
    ch "那就全力以赴地去准备吧！"
    "月光从玻璃窗口中透射进来似螺旋状美丽的花瓣般绽放在我的书桌前方"
    ch "忽然间，我想起了那位古老的中国诗人写下的绝美诗句："
    ch "吊影分为千里雁，辞根三座九秋蓬"
    ch "共看明月应垂泪，一夜乡心五处同"
    ch "窗外的月光搭配着远处明亮跳动的星星——"
    ch "也就是高楼上的亮光"
    ch "一同照亮了整个九衢市昏黑的夜晚"
    ch "这首诗讲述的是一位诗人因思念自己远在异乡的家属而作下的诗"
    ch "我想，可能她的主人亦或是她的亲人. . .也应该和初咲一样怀着同样的心情吧. . ."
    #voice ""
    #（播放效果音，"叮"，电脑上的弹窗音）
    "就在我看着窗外的太阳出神的时候，电脑上的提示音把我再次拉回了工作中"
    ch "就是想要的这个！"
    "我盯着电脑屏幕上刚刚跳出不久的资料，激动地阅读着一个接一个有关于东番国立大学交换项目的出境相关事宜"
    ch ". . . . . ."
    ch ". . . . . ."
    ch ". . . . . ."

    #（此时背景转变为深夜，房间，停顿5s）

    ch "有机会. . .完全是有机会的. . .！"
    "我注视着所有关于机器人偷渡事件的案例，竭力从其中找到任何可以避免的风险"
    ch "东番国立高大的新生通道. . .海关. . ."
    ch "实际上，初咲作为日本生产，搭载日语系统的机器人。根本不会违反所谓的“仿生机器人准则”"
    ch "也就是说，作为机器人，初咲根本就不会伤害人，而且是很安全的存在"
    ch "只不过是对于国内而言，“日语”基本上就约等于“禁忌”的代名词. . ."

    #（切入初咲在背后拿小刀抵着海川的cg，昏黄色滤镜）

    ch "尽管那种恐吓的感受却无比真实. . .完全不像是一个仿生机器人会有的行为. . ."
    "不知道过了多久，我开始有些体力不支，不断充斥着我眼球的各种跃动在电脑屏幕上的文字信息让我感觉到越来越疲惫"
    ch "那就，稍微休息一下吧. . ."
    #（使镜头有些摇晃，持续几秒）
    #voice ""
    #（播放效果音："咚"：主角倒在桌子上的声音）
    #（屏幕一黑）

    #（如果可以的话，播放转场动画：构成元素为初咲，标题以及动画）

    #（黑幕切场，此处背景转到白日，房间）

    #show
    #voice "voice/cxly_voice/episode1/初咲136.mp3"
    cq "主人，主人，快起来了！"
    ch ". . . . . ."
    ch "我这是. . .睡着了吗？"
    #show
    #voice "voice/cxly_voice/episode1/初咲137.mp3"
    cq "都已经快到中午了！趴在桌子上怎么能够睡得好觉呢？！"
    "我低头看了看屏幕上显示的时间，不多不少是“10：00”"
    ch "果然很晚了啊. . ."
    "我揉了揉已经被压酸了的胳膊，忽然想起来昨天竟然就这样趴在桌子上睡着了。"
    #show
    #voice "voice/cxly_voice/episode1/初咲138.mp3"
    cq "盯. . ."
    ch "初咲恋柚也注意到了在我电脑上的各种资料，在扫过一遍上面的内容后，很快就向我投来惊讶的目光"
    #show
    #voice "voice/cxly_voice/episode1/初咲139.mp3"
    cq "原来如此. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲140.mp3"
    cq "谢谢主人！！！"
    "还没等我反应过来，初咲已经飞快地扑到了我的身上，用力地搂住我"
    ch "喂喂，你在干什么啊. . ."
    "少女突如其来的拥抱忽然让我有些不知所措，一下子就把我从意犹未尽的睡意中拉回了现实"
    "尽管我很清楚眼前的初咲只不过是一个高性能的仿生机器人，但是她身上好闻的花香味和无比具有少女感的各种反应却又在暗示我. . ."
    "初咲就是一个具有思想和灵魂的机器人"
    ch "好了好了，快放开我"
    ch "在这样用力的话我是会被勒死的！"
    #show
    #voice "voice/cxly_voice/episode1/初咲141.mp3"
    cq "啊，抱歉抱歉！"
    #show
    #voice "voice/cxly_voice/episode1/初咲142.mp3"
    cq "唔. . .辛苦海川了. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲143.mp3"
    cq "完全没有想到主人竟然会这么认真地对待我的事情. . ."
    ch ". . ."
    ch "既然我已经做过了详细的调查，就来和初咲简单说一下我们需要解决的难题"
    #show
    #voice "voice/cxly_voice/episode1/初咲144.mp3"
    cq "好的！"
    ch "首先，你要回到日本的话，就无可避免地要通过海关"
    #show
    #voice "voice/cxly_voice/episode1/初咲145.mp3"
    cq "是这样子的"
    ch "那么就会遇到两个最重要，而且是最棘手的问题"
    #show
    #voice "voice/cxly_voice/episode1/初咲146.mp3"
    cq "两个问题？"
    ch "是的。"
    ch "一个是初咲的身份"
    ch "另一个是初咲的语言"
    #show
    #voice "voice/cxly_voice/episode1/初咲147.mp3"
    cq "身份？语言？"
    ch "嗯嗯"
    ch "身份就是你的铭牌"
    ch "上面写的是‘JAPAN’的字样"
    ch "这样是很危险的，而且在经过海关的时候是肯定会被查出来的. . ."
    ch "本来日产的仿生机器人出现在中国境内就属于是触碰法律边缘底线的行为了"
    #show
    #voice "voice/cxly_voice/episode1/初咲148.mp3"
    cq "这样啊. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲149.mp3"
    cq "也就是说，主人如果是把初咲故意丢在中国的话. . ."
    "在初咲的脸上，很明显地写上了“失望”这两个大字"
    ch "不是这样的. . ."
    ch "我相信初咲恋柚原本的主人肯定是有什么别的原因吧. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲150.mp3"
    cq "诶？"
    ch "就是. . ."
    ch "既然要求把你设计地这么可爱的. . .我想年纪应该也不会很大. . .大概. . .也不会是我们想到的那样故意遗弃你. . .？"
    #show
    #voice "voice/cxly_voice/episode1/初咲151.mp3"
    cq "是的呢！原先的主人和海川君的年纪差不多呢！"
    #show
    #voice "voice/cxly_voice/episode1/初咲152.mp3"
    cq "说起来. . .原来的主人也确实对初咲非常好"
    ch "是吧. . ."
    ch "咳咳. . .回到正题"
    ch "总之，要解决第一个问题也不算太难"
    ch "九衢市有很多的仿生机器人地下小作坊. . .该铭牌参数的化也只是花费一点小钱的事情. . ."
    ch "但想要顺利通过海关，第二个要解决的问题就是——"
    ch "初咲能够完整地说出中文"
    ch "而且必须是那种流利标准的中文才可以"
    ch "因为我也学过一点相关的知识. . ."
    ch "仿生机器人的话，应该也是可以说全部的语言对吧？要不. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲153.mp3"
    cq "这个嘛. . .其实用我存储的翻译系统说出中文来也是没问题的"
    #show
    #voice "voice/cxly_voice/episode1/初咲154.mp3"
    cq "只不过没有经过算法的训练. . .说出来会很奇怪的. . ."
    ch "要不初咲先试试说出中文？"
    #show
    #voice "voice/cxly_voice/episode1/初咲155.mp3"
    cq "真的吗. . .中文. . ."
    ch "嗯嗯"
    #show
    #voice "voice/cxly_voice/episode1/初咲156.mp3"
    cq "那. . .我开始了"
    #show
    #voice "voice/cxly_voice/episode1/初咲157.mp3"
    cq "比如说. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲158.mp3"
    cq "海川君，中午好？"#（日式中文）
    #show
    #voice "voice/cxly_voice/episode1/初咲159.mp3"
    cq "现在需要我做些什么吗？"#（日式中文）
    ch ". . ."
    ch "不行"
    ch "只有这样‘机翻’的水平的话是完全行不通的"
    #show
    #voice "voice/cxly_voice/episode1/初咲160.mp3"
    cq "我就说吧. . .这样子没训练过的中文说出口. . .会让我很为难的！"
    ch "我早就猜到了会是这个样子. . ."
    ch "所以说，我们会进行中文的特训。"
    #show
    #voice "voice/cxly_voice/episode1/初咲161.mp3"
    cq "诶？？？"
    #show
    #voice "voice/cxly_voice/episode1/初咲162.mp3"
    cq "主人是要教初咲学中文吗？"
    ch "没错"
    ch "而且是要达到和我差不多的中文水准才行"
    #show
    #voice "voice/cxly_voice/episode1/初咲163.mp3"
    cq "唔. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲164.mp3"
    cq "初咲不想学习"
    #show
    #voice "voice/cxly_voice/episode1/初咲165.mp3"
    cq "更不想学习中文. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲166.mp3"
    cq "疼疼疼. . ."
    "我把手做成劈刀状，然后轻轻地敲在初咲的脑门上"
    ch "没想到对于这种高性能的仿生机器人竟然也会有这种可爱的反应. . .完全和现实中那种可爱的女孩子一模一样诶. . ."
    ch "科技发达的成果. . .看上去也蛮不错的. . ."
    ch "不系统学习中文的话，初咲根本没有机会回到日本，找到原来的主人"
    ch "今天你在家里好好呆着，我去图书馆借一些中文方面的参考书籍"
    #show
    #voice "voice/cxly_voice/episode1/初咲167.mp3"
    cq "诶. . .主人不带着我一起吗？"
    ch "不行，"
    ch "初咲是日本型号的，基本上出去就会被认出来是仿生机器人！"
    ch "在这之前，还是先别在外面乱跑. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲168.mp3"
    cq "主人，就带我出去一次好不好！"
    #show
    #voice "voice/cxly_voice/episode1/初咲169.mp3"
    cq "就一次！"
    ch ". . ."
    ch ". . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲170.mp3"
    cq "求求主人啦~"
    ch "好吧. . ."
    ch "出门的话也没问题"
    #show
    #voice "voice/cxly_voice/episode1/初咲171.mp3"
    cq "好耶！"
    ch "不过你需要答应我一件事"
    ch "出去的话，就算是一点点日语也不能说. . ."
    ch "初咲要是答应我的话. . ."
    #show
    #voice "voice/cxly_voice/episode1/初咲172.mp3"
    cq "没问题，交给我吧！"
    #show
    #voice "voice/cxly_voice/episode1/初咲173.mp3"
    cq "初咲保证，一定不会说任何日语！"
    ch "行，那就先去图书馆找找资料吧"
    #show
    #voice "voice/cxly_voice/episode1/初咲174.mp3"
    cq "嗯嗯！"
    #voice ""
    #（播放效果音：关门声）
    jump episode1_2
