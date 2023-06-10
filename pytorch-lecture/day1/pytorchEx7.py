# squeeze & unsqueeze
import torch

t1 = torch.zeros(1,4)
print(t1)
print(t1.size())
print(torch.squeeze(t1))
print(torch.squeeze(t1).size())
print()

t2 = torch.zeros(2,1,3,1,4)
print(t2.size())
print(torch.squeeze(t2).size()) # 1은 전부 제거
print(torch.squeeze(t2,dim=1).size()) # dim에 해당하는 위치의 1 제거
print(torch.squeeze(t2,dim=3).size())
print()

t3 = torch.zeros(2,3)
print(t3.size())
print(torch.unsqueeze(t3,dim=0).size()) # dim에 해당하는 위치에 1 생성
print(torch.unsqueeze(t3,dim=1).size())
print(torch.unsqueeze(t3,dim=2).size())

