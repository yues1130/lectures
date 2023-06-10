# Linear regression 선형회귀 (간략화)
import torch
import torch.nn as nn
import torch.nn.init as init
import torch.optim as optim

x = init.uniform_(torch.Tensor(1000,3))
value = init.normal_(torch.Tensor(1000,3),std=0.2)
y_target = 2 * x + 3 + value

# y = w1 * x1 + w2 * x2 +  w3 * x3 + b
model = nn.Linear(3,1) # 3개의 input (x) & 1개의 output (y)
optimizer = optim.SGD(model.parameters(),lr=0.001) # optimizer = optim.SGD([w1, w2, w3, b], lr=1e-5)
cost_func = nn.MSELoss() # MSE

for epoch in range(1000):
    optimizer.zero_grad()
    hypothesis = model(x)
    cost = cost_func(hypothesis, y_target)
    cost.backward()
    optimizer.step()

    if epoch % 100 == 0: # (a % b) : a를 b로 나누고 나머지를 반환
        print('epoch:{}, cost:{:.3f}'
              .format(epoch+1, cost.item()))

pv = [p for p in model.parameters()]
print(pv)
print(pv[0].detach().numpy())
