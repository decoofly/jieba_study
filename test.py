#/usr/python/envn

# auth :decoofly

import jieba
from jieba import analyse

'''
 there are some base practices:
    精确模式，试图将句子最精确地切开，适合文本分析；
    全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
    搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
'''
lan_list = jieba.cut('我一直都在流浪从未见过海洋', cut_all=True)#全模式
print('全模式：'+'/'.join(lan_list))

lan_list2 = jieba.cut('我一直都在流浪从未见过海洋', cut_all=False)#精确模式,适合文本分析
print('精确模式：'+'/'.join(lan_list2))

lan_list3 = jieba.cut('我一直都在流浪从未见过海洋')#默认是精确模式
print('默认模式：'+'/'.join(lan_list3))

lan_list4 = jieba.cut_for_search('我毕业于中国科学院计算机所，后在日本京都大学深造')#搜索引擎模式
print('搜索引擎模式：'+'/'.join(lan_list4))





text = open('data.txt',encoding='utf-8').read()#打开文件
# text.encode('utf-8')
'''
关键字提取,运用analyse，有两种办法：
    基于 TF-IDF 算法的关键词抽取
  1.使用jieba.analyse.extract_tags()参数提取关键字,默认参数为20
     sentence 为待提取的文本
     topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
     withWeight 为是否一并返回关键词权重值，默认值为 False
     allowPOS 仅包括指定词性的词，默认值为空，即不筛选
'''
for item in analyse.extract_tags(text,20, withWeight=True):
    print(item)

'''
    基于 TextRank 算法的关键词抽取
  2.jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
    其中allowPOS 是词性
     直接使用，接口相同，默认过滤词性。
'''
for item in analyse.textrank(text, topK=20,withWeight=True,allowPOS='ns'):
    print(item)