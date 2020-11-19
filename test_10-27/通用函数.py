import numpy as np
import time
import math

#math 与 numpy 函数的性能比较
x =[i * 0.001 for i in range(1000000)]

start =time.perf_counter()
for i,t in enumerate(x):
    x[i]=math.sin(t)
print('math sin use time',time.perf_counter()-start)

x=np.array(x)
start=time.perf_counter()
np.sin(x)
print('np sin use time:',time.perf_counter()-start)

#循环与向量运算比较
x1=np.random.rand(1000000)
x2=np.random.rand(1000000)

##使用呢循环计算点积
tic=time.process_time()
dot=0
for i in range(len(x1)):
    dot += x[i] * x2[i]
toc=time.process_time()
print("dot ={},\n for loop ---- Compution time ={} ms".format(str(dot),str(1000*(toc - tic))))


#使用numpy 求点积
tic=time.process_time()
dot=0
dot=np.dot(x1,x2)
toc=time.process_time()
print("dot ={},\n for loop ---- Compution time ={} ms".format(str(dot),str(1000*(toc - tic))))

