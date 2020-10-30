import numpy as np
from numpy import random as nr
a=np.arange(1,26,dtype=float)
print('a',a)
b=nr.choice(a,size=(3,4))
print('指定抽取的数组的形状',b)
c=nr.choice(a,size=(3,4),replace=False)
print('不重复的抽取',c)
d=nr.choice(a,size=(3,4),p=a / np.sum(a))
print('p表示出现的概率，按照指定的概率抽取',d)
