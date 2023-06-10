# tensor 객체 transform
import torch

t1 = torch.tensor([1,2,3,4,5,6])
print(t1)
print()

t2 = t1.view(2,3) # 참조만 하고, 실질적인 구조 변화 X
print(t2)
print()

print(t1.reshape(2,3)) # 실질적인 구조 변화 (계산량 많음)
print()

t3 = torch.tensor([[1,2],[3,4],[5,6]])
print(t3)
print(t3.size())
print(t3.view(-1)) # 값을 1차원형태로 풀어줌
print(t3.view(1,-1)) # 내부에 1dim을 만들어 그 안에 풀어줌
print()

t4 = torch.tensor([[[1,2],[3,4]],[[5,6],[7,8]]])
print(t4)
print(t4.size())
print()
print(t4.view(-1))
print(t4.view(1,-1))
print(t4.view(2,-1))

