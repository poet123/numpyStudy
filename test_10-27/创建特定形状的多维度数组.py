import numpy as np

a=np.zeros([3,4])
print('a',a)

b=np.ones([3,4])
print('b',b)

#创建空数组
c=np.empty([3,4])
print('c',c)

#以nddr相同的维度创建元素全为0的数组
d=np.zeros_like(c)
print('d',d)
#np.ones_like,np.empty_like同理

#创建对角数组
e=np.eye(5)
print('e',e)

#创建填充数组
f=np.full([3,4],666)
print(f)

#保存数组
np.savetxt(X=d,fname='npzero.txt')

#从文件中读取数组
g=np.loadtxt('npzero.txt')
print('g',g)