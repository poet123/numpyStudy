import numpy as np

#合并一维数组
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.append(a,b)
print('合并一维数组',c)

#合并多维数组
a=np.arange(4).reshape(2,2)
b=np.arange(4).reshape(2,2)
print('原始数据：\n',a,'\n',b)
#按行合并
c=np.append(a,b,axis=0)
print('按行合并的结果：\n',c,'，维度：',c.shape)
#按照列来合并
d=np.append(a,b,axis=1)
print('按列合并的结果:\n',d,',维度',d.shape)

#沿指定轴连接数组成数组或矩阵
a=np.array([[1,2],[3,4]])
b=np.array([[5,6]])
c=np.concatenate((a,b),axis=0)
print('合并后的c为：\n',c)
print('b.T：\n',b.T)
d=np.concatenate((a,b.T),axis=1)
print(d)

#沿指定轴堆叠数组或者矩阵
a=np.array([[1,2],[3,4]])
b=np.array(([[5,6],[7,8]]))
print('stack 堆叠成矩阵\n',np.stack((a,b),axis=0),',维度：',np.stack((a,b),axis=0).shape)
