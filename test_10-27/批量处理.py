import  numpy as np

#生成1000个形状为2x3的数组
data_train=np.random.randn(1000,2,3)
print('生成的数组为：\n',data_train)

#打断这1000条数据
np.random.shuffle(data_train)
print('打乱后的数据为:\n',data_train)



#定义批处理大小、
bath_size=100
for i in range(0,len(data_train),bath_size):
    x_bach_sum=np.sum(data_train[i:i+bath_size])
    print('第{}批次处理的数据之和{}'.format(i,x_bach_sum))