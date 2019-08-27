
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats,integrate
sns.set()
d=pd.read_csv('result_3.csv')
time=d["play time"]
def status(x) :
    return pd.Series([x.count(),x.min(),x.quantile(.25),x.median(),
                      x.quantile(.75),x.mean(),x.max(),x.mad(),x.var(),
                      x.std(),x.skew(),x.kurt()],index=['样本总个数','最小值','25%分位数',
                    '中位数','75%分位数','均值','最大值','平均绝对偏差','方差','标准差','偏度','峰度'])
print(status(time))
#Bin size=2IQR(x)n^-1/3 Freedman-Diaconis准则
sns.distplot(time,color='r',
                 rug=True,
                 kde=False,
                 bins=17,
                 fit=None,
                 hist_kws={'alpha':0.6,'color':'orange'},
                 rug_kws={'color':'g'},
                 norm_hist=False)
plt.show()
sns.kdeplot(time)
plt.show()


