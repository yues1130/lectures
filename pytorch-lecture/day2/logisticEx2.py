import torch
import torch.optim as optim
import torch.nn.functional as F
import torch.nn as nn

x_data = [ [1,2],[2,3],[3,1],[4,3],[5,3],[6,2] ]
y_data = [ [0],[0],[0],[1],[1],[1] ]
x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)

class LogisticClass(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2,1)
        self.sigmoid = nn.Sigmoid()
    def forward(self,x):
        return self.sigmoid(self.linear(x))
model = LogisticClass()

# model 학습
optimizer = optim.SGD(model.parameters(),lr=1)
for epoch in range(1000):
    optimizer.zero_grad()
    hypothesis = model(x_train)
    loss = F.binary_cross_entropy(hypothesis, y_train)
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f'epoch:{epoch} loss:{loss.item():.4f}')


