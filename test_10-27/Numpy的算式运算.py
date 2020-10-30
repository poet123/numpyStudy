import numpy as np

#对应元素的相乘
a=np.array([[1,2],[-1,4]])
b=np.array([[2,0],[3,4]])

print('a*b',a*b)

print('np.multiply',np.multiply(a,b))

print('a*2',a*2)
print('a/2',a/2)

x=np.random.rand(2,3)

def softmoid(x):
    return 1/(1+np.exp(-x))

def relu(x):
    return np.maximum(0,x)

def softmax(x):
    return np.exp(x)/np.sum(np.exp(x))

print('输入参数x的形状',x)
print('激活函数softmoid',softmoid(x))
print('relu函数',relu(x))
print('softmax函数',softmax(x))


#点积运算
x1=np.array([[1,2],[3,4]])
x2=np.array([[5,6,7],[8,9,10]])
print('内积：',np.dot(x1,x2))



