#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/10/14 14:34
@Desc   ：
# 采用TextRank方法提取文本关键词  jieba.analyse.textrank
       TextRank权重：
            1、将待抽取关键词的文本进行分词、去停用词、筛选词性
            2、以固定窗口大小(默认为5，通过span属性调整)，词之间的共现关系，构建图
            3、计算图中节点的PageRank，注意是无向带权图
=================================================='''
import jieba.analyse
import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(current_dir)[0]
sys.path.append(rootPath)


# from conf.GetConfParams import GetConfParams
#
# logger = GetConfParams().logger


def getKeywords_textrank(text):
    """
    处理标题和摘要，提取关键词
    :param text:
    :return:
    """
    # logger.info('使用jieba.analyse.textrank提取关键词，默认提取10个')
    topK = 10
    result = []
    jieba.analyse.set_stop_words("../data/stopwords.txt")  # 加载自定义停用词表
    keywords = jieba.analyse.textrank(text, topK=topK, allowPOS=(
        'n', 'nz', 'v', 'vd', 'vn', 'l', 'a', 'd'), withWeight=True)  # TextRank关键词提取，词性筛选withWeight=True
    for item in keywords:
        # print(item[0], item[1]) #打印关键词及权重 参数必须设置withWeight=True
        keyword = {'word': item[0], 'weight': "%.4f" % item[1]}
        result.append(keyword)
    return result


if __name__ == '__main__':
    data = """
中新网北京12月1日电(记者 张曦) 30日晚，高圆圆和赵又廷在京举行答谢宴，诸多明星现身捧场，其中包括张杰(微博)、谢娜(微博)夫妇、何炅(微博)、蔡康永(微博)、徐克、张凯丽、黄轩(微博)等。

30日中午，有媒体曝光高圆圆和赵又廷现身台北桃园机场的照片，照片中两人小动作不断，尽显恩爱。事实上，夫妻俩此行是回女方老家北京举办答谢宴。

群星捧场 谢娜张杰亮相

当晚不到7点，两人十指紧扣率先抵达酒店。这间酒店位于北京东三环，里面摆放很多雕塑，文艺气息十足。

高圆圆身穿粉色外套，看到大批记者在场露出娇羞神色，赵又廷则戴着鸭舌帽，十分淡定，两人快步走进电梯，未接受媒体采访。

随后，谢娜、何炅也一前一后到场庆贺，并对一对新人表示恭喜。接着蔡康永满脸笑容现身，他直言：“我没有参加台湾婚礼，所以这次觉得蛮开心。”

曾与赵又廷合作《狄仁杰之神都龙王》的导演徐克则携女助理亮相，面对媒体的长枪短炮，他只大呼“恭喜！恭喜！”

作为高圆圆的好友，黄轩虽然拍杂志收工较晚，但也赶过来参加答谢宴。问到给新人带什么礼物，他大方拉开外套，展示藏在包里厚厚的红包，并笑言：“封红包吧！”但不愿透露具体数额。

值得一提的是，当晚10点，张杰压轴抵达酒店，他戴着黑色口罩，透露因刚下飞机所以未和妻子谢娜同行。虽然他没有接受采访，但在进电梯后大方向媒体挥手致意。

《我们结婚吧》主创捧场

黄海波(微博)获释仍未出席

在电视剧《咱们结婚吧》里，饰演高圆圆母亲的张凯丽，当晚身穿黄色大衣出席，但只待了一个小时就匆忙离去。

同样有份参演该剧，并扮演高圆圆男闺蜜的大左(微信号：dazuozone) 也到场助阵，28日，他已在台湾参加两人的盛大婚礼。大左30日晚接受采访时直言当时场面感人，“每个人都哭得稀里哗啦，晚上是吴宗宪(微博)(微信号：wushowzongxian) 主持，现场欢声笑语，讲了好多不能播的事，新人都非常开心”。

最令人关注的是在这部剧里和高圆圆出演夫妻的黄海波。巧合的是，他刚好于30日收容教育期满，解除收容教育。

答谢宴细节

宾客近百人，获赠礼物

记者了解到，出席高圆圆、赵又廷答谢宴的宾客近百人，其中不少都是女方的高中同学。

答谢宴位于酒店地下一层，现场安保森严，大批媒体只好在酒店大堂等待。期间有工作人员上来送上喜糖，代两位新人向媒体问好。

记者注意到，虽然答谢宴于晚上8点开始，但从9点开始就陆续有宾客离开，每个宾客都手持礼物，有宾客大方展示礼盒，只见礼盒上印有两只正在接吻的烫金兔子，不过工作人员迅速赶来，拒绝宾客继续展示。

           """
    # 关键词提取
    keyWords = getKeywords_textrank(data)
    print(keyWords)
