import numpy as np

a=np.random.random([10])
print(a)
#获取指定位置的的数据
print(a[3])

#截取一段数据
print(a[3:6])

#截取固定间隔的数据每隔两个截取一段数据
print(a[1:6:2])

#倒序取数
print(a[:-2])

b=np.arange(25).reshape([5,5])
print('b',b)
print('zero',b[1])
print('zero1',b[1,0])
print('第一行，第2行',b[1:3])
print('取第一行第2行的数据后再取第1列到第三列',b[1:3,1:3])

print('xxxx',b[(b>2) & (b<5)])

print('第一行二行的数据',b[0:2,:])
print('第二列数据',b[:,2])
print('从第三行第2列开始取数据',b[3:,2:])
print()

print(b[2::2,::2])


