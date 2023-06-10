# 미분
import torch

w = torch.tensor(2.) # 아무거나 미분 할 수 없음. 미분 가능하도록 setting을 해둬야 함
w = torch.tensor(2., requires_grad=True) # 미분 가능하도록 setting이 됨
print(w)
y = 2 * w
print(y)
y.backward()

print('w로 미분한 값: ',w.grad)

for epoch in range(20):
    y = 2 * w
    y.backward()
    print('w로 미분한 값: ',w.grad) # 미분한 값을 계속 누적하는 컨셉.
    w.grad.zero_() # 초기화
    # optimizer.zero_grad() # 초기화

