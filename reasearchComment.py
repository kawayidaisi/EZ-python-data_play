# coding=utf-8
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
comments=[]
with open('result.csv', mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        comment = row.split(',')
        if comment != '':
            comments.append(comment)

comment_after_split = jieba.cut_for_search(str(comments))
words = " ".join(comment_after_split)  # 以空格进行拼接

stopwords = STOPWORDS.copy()
stopwords.add("<p>")
stopwords.add("</p>")
stopwords.add("真的")
stopwords.add("游戏")
stopwords.add("这个")
stopwords.add("不是")
stopwords.add("玩家")
stopwords.add("就是")
stopwords.add("感觉")
stopwords.add("觉得")
stopwords.add("一部")
stopwords.add("一个")
stopwords.add("没有")
stopwords.add("什么")
stopwords.add("有点")
stopwords.add("现在")
stopwords.add("还是")
stopwords.add("但是")
stopwords.add("有点")
stopwords.add("然后")
stopwords.add("还有")
stopwords.add("而且")
stopwords.add("可以")
stopwords.add("不过")
stopwords.add("虽然")
stopwords.add("因为")
stopwords.add("所以")
stopwords.add("如果")
stopwords.add("自己")
bg_image = plt.imread('amiya.jpg')

wc = WordCloud(width=1024, height=768, background_color='white', mask=bg_image, font_path='STKAITI.TTF',stopwords=stopwords, max_font_size=400, random_state=50)
wc.generate_from_text(words)
plt.imshow(wc)
plt.axis('off')  # 不显示坐标轴
plt.show()
# 保存结果到本地
wc.to_file('词云图.jpg')
