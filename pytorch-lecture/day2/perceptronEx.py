import torch
import torch.nn as nn
import torch.optim as optim

torch.manual_seed(777)

x = torch.FloatTensor([[0,0], [0,1], [1,0], [1,1]])
y = torch.FloatTensor([[0], [1], [1], [0]])

model = nn.Sequential(
    nn.Linear(2,2, bias=True),
    nn.Sigmoid(),
    nn.Linear(2,1),
    nn.Sigmoid()
)

loss_func = nn.BCELoss()
optimizer = optim.SGD(model.parameters(), lr=1)

for epoch in range(10001):
    hypothesis = model(x)
    optimizer.zero_grad()
    loss = loss_func(hypothesis, y)
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print('epoch:{} loss:{:.4f}'.format(epoch+1, loss.item()))

with torch.no_grad():
    hypothesis = model(x)
    prediction = (hypothesis > 0.5).float()
    accuracy = (prediction == y).float().mean()
    print('hypothesis:\n{}\nprediction:\n{}\ntarget:\n{}\naccuracy:{:.4f}'.format(
        hypothesis.numpy(), prediction.numpy(), y.numpy(), accuracy.item()
    )) 

