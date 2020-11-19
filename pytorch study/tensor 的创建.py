import torch

#根据list 生成tensor
print('根据list 生成tensor:',torch.Tensor([1,2,3,4,5,6]))
#根据指定形状生成tensor
print('根据指定形状生成tensor',torch.Tensor(2,3))
#根据给定的tensor形状
t=torch.Tensor([[1,2,3],[4,5,6]])
#查看tensor的形状
print(t.size())
#shape 与size()等价方式
print('shape \n',t.shape)
#根据已有形状创建tensor
print('根据已有形状创建tensor',torch.Tensor(t.size()))

print('生成一个单位矩阵：\n',torch.eye(2,2))
print('生成一个全为0的矩阵 \n',torch.zeros(2,3))
print('根据规则生成数据 \n',torch.linspace(1,10,4))
print('生成一个均匀分布的随机数： \n',torch.rand(2,3))
print('生成标准分布的随机数\n',torch.randn(2,3))
print('返回所给数据形状相同，值为0的张量 \n',torch.zeros_like(torch.rand(2,3)))