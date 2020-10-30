import numpy as np

a=np.arange(10)
print('a',a)

b=np.arange(0,10)
print('b',b)
print('a=b?',a is b)

c=np.arange(9,-1,-1)
print(c)

d=np.linspace(0,1,10)
print(d)

e=np.logspace(0,1,10)
print('e',e)