# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
font = r'C:\Windows\Fonts\simfang.ttf'
def WordsClound():
    file_name = "奥运会"
    data = pd.read_csv("input/"+file_name+".csv")
    word_list = data['keywords'].tolist()
    count = list(map(int,data['count_num'].tolist()))
    word_dict = dict(zip(word_list,count))
    wordcloud = WordCloud(background_color='white', collocations=False,
                    random_state=50,width=400, height=300,font_path=font)
    wordcloud.generate_from_frequencies(word_dict)
    plt.axis('off')
    plt.title("KeyWords of "+file_name)
    plt.imshow(wordcloud.recolor())
    plt.savefig('KeyWords of '+file_name+'.jpg')