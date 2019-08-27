import re
import pandas as pd
time_df=pd.read_csv('result_2.csv')
new_time=[]
for x in time_df['play time']:
    if '小时' in x:
        b = re.search('(\d+)小时', x).group(1)
    else:
        b = 0
    if '分钟' in x:
        c = re.search('(\d+)分钟', x).group(1)
    else:
        c = 0
    seconds = int(b)*60 + int(c)
    x = (float)(seconds/60)
    new_time.append(x)
result_time={"play time": new_time,}
resultpd_3=pd.DataFrame(result_time)
resultpd_3.to_csv('result_3.csv',encoding='utf_8_sig')
