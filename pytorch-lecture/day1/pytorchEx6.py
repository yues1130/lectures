# initialization
import torch
import torch.nn.init as init

t1 = init.uniform_(torch.FloatTensor(3,4)) # random variable 생성 (underbar가 최신이므로 최신 버전 사용, 없는거는 옛날거)
print(t1)
print()

t2 = init.normal_(torch.FloatTensor(3,4), mean=10, std=3) #
print(t2)
print()

t3 = torch.FloatTensor(torch.randn(3,4)) # 표준정규분포 mean = 0 & std = 1
print(t3)
print()

t4 = init.constant_(torch.FloatTensor(3,4), 100)
print(t4)
print()