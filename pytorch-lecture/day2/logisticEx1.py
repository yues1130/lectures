import torch
import torch.optim as optim
import torch.nn.functional as F

x_data = [ [1,2],[2,3],[3,1],[4,3],[5,3],[6,2] ]
y_data = [ [0],[0],[0],[1],[1],[1] ]
x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)

w = torch.zeros((2,1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

hypothesis1 = 1 / (1+torch.exp(-(x_train.matmul(w) + b)))
print(hypothesis1)
print()

hypothesis2 = torch.sigmoid(x_train.matmul(w) + b)
print(hypothesis2)
print()

losses = -( y_train * torch.log(hypothesis2) + (1-y_train)*torch.log(1 - hypothesis2) )
print(losses)
print()

loss = losses.mean()
print(loss)
print()

loss2 = F.binary_cross_entropy(hypothesis2, y_train)
print(loss2)
print()

# model 학습
optimizer = optim.SGD([w,b], lr=1)
for epoch in range(1000):
    optimizer.zero_grad()
    hypothesis = torch.sigmoid(x_train.matmul(w) + b)
    loss = F.binary_cross_entropy(hypothesis, y_train)
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f'epoch:{epoch} loss:{loss.item():.4f}')
