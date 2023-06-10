# tensor 객체 연산
import torch

t1 = torch.tensor([1,2,3])
t2 = torch.tensor([1,2,3])

t3 = t1 + 20
print(t3)
print()

t4 = t1 + t2
print(t4)
print()

t5 = torch.tensor([[10,20,30],[50,60,70]])
print(t5)
print()

print(t1 + t5)
print()

t6 = torch.linspace(0,3,10)
print(t6)
print(torch.exp(t6))
print(torch.log(t6))
print()

t7 = torch.tensor([[2,4,6],[1,9,7]])
print(t7)
print()

print(torch.max(t7)) # 전체 최대값
print()
print(torch.max(t7,dim=1)) # 각 최대값 & 각 최대값 위치
print()
print(torch.max(t7,dim=1)[0]) # 각 최대값
print()
print(torch.max(t7,dim=1)[1]) # 각 최대값 위치
print()

