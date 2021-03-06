import numpy as np

#reshape改表向量的维度（不修改向量的本身）
arr=np.arange(10)
print('arr',arr)
b=arr.reshape(2,5)

#将向量arr维度变换为2行5列
print('arr不变',arr)
print('将arr维度转换为2行5列',b)

#可以只指定特定行数或者列数，其他用-1代替
c=arr.reshape(5,-1)
print('只保留行',c)

#resize改变向量的维度，同时修改向量的本身
b=arr.resize(2,5)
print('修改后 a也随着改表',arr,'\n\n\n\n')

#转置
a=np.arange(12).reshape(3,4)
print(a)
print('转置后的a',a.T)
print(a)

#展平
print('按照列优先展平',a.ravel('F'))
print('按照行优先级展开',a.ravel())
print('\n\n\n\n')

#将矩阵转换为向量
#np.floor() 向下取整
a=np.floor(10 * np.random.random((3,4)))
print('a',a)
print('转为向量后：',a.flatten())

#降维
b=np.arange(3).reshape(3,1)
print('没有降维前',b)
print('降维后：',b.squeeze())

c=np.arange(6).reshape(3,1,2,1)
print('没有降维\n',c)
print('降维后：\n',c.squeeze().shape)

#高维矩阵的轴对换
d=np.arange(24).reshape(2,3,4)
print('未对换之前\n',d)
#print('对换后\n',d.transpose(0,2,1))#(,2,4,3)(右旋90)
print(d.transpose(2,1,0))#4,3,2

