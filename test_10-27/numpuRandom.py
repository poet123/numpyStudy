import numpy as np


#生成0到1之间的随机数
a=np.random.random([3,3])
print('a',a)

#生成均匀分布的随机数
b=np.random.uniform([3,3])
print('b',b)

#生成标准正态随机数
c=np.random.randn(3)
print('c',c)

#生成随机整数
d=np.random.randint(10)
print('d',d)

#打乱随机数的顺序
e=np.random.shuffle(c)
print(c)

#生成随机浮点数
f=np.random.random_sample([3,3])
print('f',f)



