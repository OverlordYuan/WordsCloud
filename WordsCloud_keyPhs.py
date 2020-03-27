from PIL import Image
import numpy as np
from nltk.corpus import stopwords
from matplotlib import pyplot as plt
import string
from wordcloud import WordCloud, ImageColorGenerator
import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
font = r'C:\Windows\Fonts\simfang.ttf'
# file_name = "shenzhen-new"
file_name = "阿斯利康"
data = pd.read_csv("input/"+file_name+".csv")
word_list = data['keyPhrases'].tolist()
count = list(map(int,data['count_num'].tolist()))
mask_image = np.array(Image.open("circle.jpg"))
word_dict = dict(zip(word_list,count))
# stopwords
punctuation = list(string.punctuation)
stop = stopwords.words('spanish') + punctuation + ['rt', 'via']
# wordcloud
wordcloud = WordCloud(background_color='white', collocations=False,stopwords=stop,
                random_state=50,width=400, height=300,font_path=font)
# wordcloud.generate(",".join(word_list))
wordcloud.generate_from_frequencies(word_dict)
# image colors
# image_colors = ImageColorGenerator(mask_image)
# plt.rcParams["figure.figsize"] = (10,10)
plt.axis('off')
plt.title("KeyPhrases of "+file_name)
plt.imshow(wordcloud.recolor())
# plt.gcf().set_size_inches(10.5, 10.5)
plt.savefig('KeyPhrases of '+file_name+'.jpg')