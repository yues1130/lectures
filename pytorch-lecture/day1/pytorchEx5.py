# slicing
import torch
t1 = torch.tensor([[1,2,3],[4,5,6]])
print(t1)
print(t1[:,:2])

print(t1 > 4)
print(t1[t1>4])

t1[:,2]=40
print(t1)
print()

t1[t1>10] = 100
print(t1)
print()

t2 = torch.tensor([[1,2,3],[4,5,6]])
t3 = torch.tensor([[7,8,9],[10,11,12]])
t4 = torch.cat([t2,t3], dim=0) # 열 방향으로 붙인다.
t5 = torch.cat([t2,t3], dim=1) # 행 방향으로 붙인다.
print(t2)
print()
print(t3)
print()
print(t4)
print()
print(t5)

# torch.chunk(x, n, dim)
# n: 몇개로 쪼갤지
# dim: 어떤 차원에 적용할지
for c in torch.chunk(t4,4,dim=0): # 행에 따라 slicing
    print(c,end='\n\n')

for c in torch.chunk(t4,3,dim=1): # 열에 따라 slicing
    print(c,end='\n\n')

"""
import numpy as np
d1 = [[1, 2, 3], [4,5, 6]]
n1 = np.array(d1)
print(n1)
print(n1[:,:2])
"""