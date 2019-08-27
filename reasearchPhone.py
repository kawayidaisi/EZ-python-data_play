import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
comments=[]
with open('result_1.csv', mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        comment = row.split(',')
        if comment != '':
            comments.append(comment)

comment_after_split = jieba.cut_for_search(str(comments))
words = " ".join(comment_after_split)  # 以空格进行拼接

stopwords = STOPWORDS.copy()
stopwords.add("<p>")

bg_image = plt.imread('amiya.jpg')

wc = WordCloud(width=1024, height=768, background_color='white', mask=bg_image, font_path='STKAITI.TTF',stopwords=stopwords, max_font_size=400, random_state=50)
wc.generate_from_text(words)
plt.imshow(wc)
plt.axis('off')  # 不显示坐标轴
plt.show()
# 保存结果到本地
wc.to_file('手机词云图.jpg')