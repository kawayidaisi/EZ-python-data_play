import pandas as pd
import numpy as np
import requests
import re
from bs4 import BeautifulSoup
import time as tm

url_1="https://www.taptap.com/app/70253/review?order=default&page="        	#url开头
url_2="#review-list"                                                       	#url结尾
page_total=500                                                              	#需要爬取的总页数

comment_out=[]                                                         		#输出容器
score_out=[]
date_out=[]
phone_out=[]
time_out=[]


def get_comment_text(star_bs):
    comment = star_bs.select(".review-item-text ")  # 选中目标class，将从这个class中匹配内容
    pattern_pinglun = '<div class.*?data-review.*?"contents">(.*?)</div>'  # 建立正则表达式，(.*?)是最后会截取出来的内容
    pinglun = re.findall(pattern_pinglun, str(comment), re.S)  # 调用re库进行正则匹配，保存结果

    return pinglun


def get_comment_score(star_bs):
    comment = star_bs.select(".review-item-text ")
    pattern_score = '<i class.*?"width: (.*?)px"></i>'
    score = re.findall(pattern_score, str(comment), re.S)
    score_num = [int(x) / 14 for x in score]  # 抓出来的是字符串，转化为整型，并计算评分

    return score_num


def get_comment_date(star_bs):
    comment_header = star_bs.select(".review-item-text .item-text-header")
    pattern_date = 'data-dynamic-time=".*?">(.*?)</span>'
    date = re.findall(pattern_date, str(comment_header), re.S)

    return date

def get_comment_phone(star_bs):
    comment = star_bs.select(".review-item-text ")
    pattern_phone ='<span class="text-footer-device">(.*?)</span>'
    phone = re.findall(pattern_phone, str(comment), re.S)
    return phone

def get_comment_time(star_bs):
    comment = star_bs.select(".review-item-text ")
    pattern_time ='<span class="text-score-time">(.*?)</span>'
    time =re.findall(pattern_time, str(comment), re.S)
    return time




for j in range(page_total):  # 总共爬5页数据
    t1 = tm.time()
    pagenum = str(j)
    link = url_1 + pagenum + url_2  # 拼接每一页的url

    star = requests.get(link)  # 加载url
    star_bs = BeautifulSoup(star.text, "html.parser")  # 把url对象转化为美味汤

    comment_tmp = get_comment_text(star_bs)  # 获取评论
    score_tmp = get_comment_score(star_bs)  # 获取分数
    date_tmp = get_comment_date(star_bs)  # 获取评论时间
    phone_tmp = get_comment_phone(star_bs)
    time_tmp = get_comment_time(star_bs)

    comment_out.extend(comment_tmp)  # 装入输出容器
    score_out.extend(score_tmp)
    date_out.extend(date_tmp)
    phone_out.extend(phone_tmp)
    time_out.extend(time_tmp)
    t2 = tm.time()
    timing = t2 - t1  # 计时，用于调试
    print('page %d grapped, %5.2f seconds used' % (j, timing))  # 输出爬取进度

result={"comment" : comment_out,
        "score" : score_out,
        "comment_date" : date_out,
                                    }                     #先把列表转为字典
result_phone={"phone" : phone_out,}
result_time={"play time": time_out,}

resultpd=pd.DataFrame(result)
resultpd_1=pd.DataFrame(result_phone)
resultpd_2=pd.DataFrame(result_time)
resultpd.to_csv('result.csv',encoding='utf_8_sig')
resultpd_1.to_csv('result_1.csv',encoding='utf_8_sig')
resultpd_2.to_csv('result_2.csv',encoding='utf_8_sig')



