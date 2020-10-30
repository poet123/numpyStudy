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
print('a 修改后 ')