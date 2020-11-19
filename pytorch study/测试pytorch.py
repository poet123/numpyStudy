import torch
print('cuda ',torch.cuda.is_available())
x=torch.tensor([10.0])
#x=x.cuda()
print(x)

y=torch.randn(2,3)
print(y)

z=x+y
print('z',z)

x=torch.tensor([1,2])
y=torch.tensor([3,4])
print('原x \n',x)
print('原y\n',y)

#没加下划线x不变
z=x.add(y)
print('z\n',z)
print('x不变 \n',x)

#加了下划线x改变
z=x.add_(y)
print('z \n',z)
print('x改变 \n',x)

