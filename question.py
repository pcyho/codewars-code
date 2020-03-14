# encoding:utf-8

import time
from random import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText

filename = 'C:/Users/17269/Desktop/樱花.png'

root = Tk()

questionlist = [
    """
    雨にも負けず　風にも負けず　雪にもなつの暑さにも負けぬ　丈夫なからだをまち
    欲しはなく　決して怒らず　いつもしずかに笑っている
    日照りの時　涙を流し　寒さの夏はおろおろ歩き　みんなにでくのぼっと呼んでれ
    褒められもせず　苦にもされず　そういうものにわたしはなりたい
    不畏风 不惧雨 更何患那冰火九重天
    无所欲 无所求 我自拈花微笑看凡尘
    惟自强 拓前路 哪怕世人闲言与细语
    度众生 无疾苦 得成就无边无量功德
    上述和歌出自谁的作品
    """,
    """
    中途岛海战日军和美军各失去几艘航母
    """,
    """
    Ruby编程语言的发明者是谁？
    """,
    """
    可以作为冠位caster的是哪几个从者
    """,
    """
    黑泽明的罗生门改编自哪篇小说？
    """,
    """
    以下哪篇太宰治的小说与其他的色彩不同？ 人间失格 斜阳 奔跑吧梅勒斯 小丑之花
    """,
    """
    日本最知名的千本鸟居位于哪所神社里？
    """,
    """
    著名的日漫作品新世纪福音战士中的绫波丽被称为什么？
    """,
    """
    日本由声优出身CD销量最高的女性歌手是？
    """,
    """
    日本知名动画电影导演新海诚第一部长篇电影作品是？
    """,
    """
    在日本视频网站Niconico以及各种社交媒体及论坛上经常会看到类似「草」「大草原不可避」之
    类的留 言，请问这是什么意思？
    A 你马死了   B 感动哭了   C 啊我死了   D 笑死我了
    """,
    """
    在日本视频网站Niconico经常会在视频结束时看到类似「888888」之类的留言，请问这是什么意思？
    A 类似于“啪啪啪啪”的鼓掌声 B 类似于视频结束的散场语   C 类似于“哈哈哈哈”的笑声   D  鼓励
    大家多发弹幕
    """,
    """
    人们常说「惨遭A1动画化」，那么请问以下哪部作品不是A1制作的？
    A 刀剑神域   B 加速世界   C 路人女主   D 黄漫老师
    """,
    """
    日语中的外来词汇，如咖啡、的士、巧克力等，一般是用什么来表示的？
    A 平假名     B 片假名      C 汉字    D 以上均可
    """,
    """
    在日本女子高中生（JK）当中流行着一种「JK语」，例如「マ（ma）」，请问这是什么意思？
    A 真的么     B 糟糕       C 等等     D 真厉害
    """,
    """
    以下京都动画中，到目前为止没有推出第二季的是
    A free！     B 轻音      C CLANNAD   D 境界的彼方
    """,
    """
    下列角色不属于钉宫四萌的是
    A 逢坂大河     B 亚里亚      C 夏娜   D 三千院凪
    """,
    """
    阿姆斯特朗回旋加速喷气式阿姆斯特朗炮“的名字出自哪部动漫?
    """,
    """
    东方project中在人气投票中曾一度排名超过主角组的角色是?
    """,
    """
    在动漫《叛逆的鲁路修》中，C.C.的头发的颜色是?
    """,
    """
    《名侦探柯南》中服部平次是哪里人?
    """,
    """
    声优御三家指的是
    """,
    """
    以下哪位日本作家未获得过诺贝尔文学奖 
    A.川端康成 B.黑石雄一 C.大江健三郎 D.村上春树
    """,
    """
    "非自然死亡"的片尾曲是?
    """,
    """
    请说出6个日本城市名称:
    """,
    """
    日本同人游戏界的三大奇迹是?
    """,
    """
    "目力"这个词出自?
    """,
    """
    狼与香辛料中男主的名字是?
    """,
    """
    自分の（　）、妹を雑誌を買いに行かせた。
    １　あげく　２　かわりに　３　きり　４　一方で
    """,
    """
    日本战国三杰指的是：
    """,
    """
    请列举2个你知道的传统日本游戏
    """,
    """
    花の色は　うつりにけりな　いたづらに　わが身世にふる　ながめせしまに
    上述和歌出自（）之手
    """,
    """
    请列举出5个百鬼夜行中的鬼怪
    """,
    """
    请列举两个你知道的日本都市传说
    """,
    """
    请列举8个你所知道的vtbuer
    """,
    """
    袋の中に赤玉4個、青玉3個、白玉2個が入っている、ここから同時に4個取り出すとき次の確率を求めよ。
    １．赤玉が３個以上出る確率
    ２．３色全てのいろが出る確率
    ３．取り出した玉の色が２色になる確率
    """,
    """
    ruby是一门简单容易上手的语言,其中有如下两个方法，
    str = "rrruuuuuubbbbby"
    p str.squeeze
    输出为： "ruby"
    
    str = "samurai"
    p str.tr("sa", "cu")
    输出为： "cumurui"
    
    那么下面的代码输出为？
    str = "ssssaaaassssuuggggaaaooommaaeeee"
    p str.tr("ag", "se").squeeze   
    """,
    """
    WHITE ALBUM2 中男主的名字是
    """,
    """
    请列举5个日本大学
    """
]
###########################################################################
answerlist = [
    '宫泽贤治',
    '美军一艘(约克城号)，日军四艘(赤城，加贺，苍龙，飞龙)',
    '松本行弘',
    '所罗门、梅林、闪闪',
    '竹林中',
    '奔跑吧梅勒斯',
    '京都的伏见稻荷大社',
    '三无少女的鼻祖',
    '林原惠(美)',
    '《云之彼端，约定的地方》',
    'D',
    'A',
    'B',
    'B',
    'A',
    'D',
    'B',
    '《银魂》',
    '古明地恋',
    '绿色',
    '大阪',
    '崛江由衣  水树奈奈  田村由香里',
    'D',
    'Lemon',
    ' ',
    '寒蝉鸣泣之时,东方project,月姬',
    '仲夏夜的yin梦',
    '罗伦斯',
    '２　1表结果，2表代替，交换，3表界限，终结，4表一方面，从另一个方面来说',
    '德川家康，织田信长，丰臣秀吉',
    '歌留多，花札',
    '小野小町',
    '觉，天狗，幽谷响，玉藻前，飞头蛮，雪女，酒吞童子，河童',
    "裂口女，无头骑士，猿之手，厕所里的花子，藤娘人偶娃哇，如月车站, 八尺",
    "神楽めあ　神楽ナナ　湊あくあ　大神澪　白上吹雪　古守ちゆ　夢ノ栞　本間ひまわり　高槻律　织田信姬",
    "1/6 4/7 53/126",
    '"suesomse"',
    "北原春希(きたはら　はるき)",
    "东京大学 早稻田大学 北海道科学大学 东北工业大学 神奈川工科大学 东海大学 大阪电气通信大学"
]

a = iter([i for i in range(0, len(questionlist))])


def showquestion():
    test.delete('1.0', END)
    try:
        test.insert(INSERT, questionlist[a.__next__()])
    except:
        test.delete('1.0', END)
        test.insert(INSERT, "question finish")


def showanswer():
    question = questionlist.index(test.get('1.0', END)[:-1])
    if question != "question finish":
        test.insert(INSERT, "\n		")
        test.insert(INSERT, answerlist[question])
    else:
        return


def clearworlds():
    test.delete('1.0', END)


photo = PhotoImage(file=filename)
test = ScrolledText(root, width=800, height=20, font=(20))
back_label = Label(root, justify=LEFT, image=photo, compound=CENTER)  # .pack()
test.pack(side=BOTTOM, expand=True, fill=X)

Button(text='下一个问题', command=showquestion).place(
    x=250, y=200, width=150, height=60)
Button(text='显示答案', command=showanswer).place(
    x=450, y=200, width=150, height=60)
Button(text="clear", command=clearworlds).place(
    x=0, y=0, width=150, height=60)
root.title('有奖问答')
mainloop()
