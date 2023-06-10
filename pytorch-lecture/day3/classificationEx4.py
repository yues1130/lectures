# image classification with mnist
import torch
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

torch.manual_seed(111)
mnist_train = dset.MNIST(root='MNIST_data/', # MNIST data & 저장 위치
                         train=True,
                         download=True,
                         transform=transforms.ToTensor())
mnist_test = dset.MNIST(root='MNIST_data/', # MNIST data & 저장 위치
                         train=False,
                         download=True,
                         transform=transforms.ToTensor())
data_loader = DataLoader(dataset=mnist_train,
                         batch_size=100,
                         shuffle=True,
                         drop_last=True)
data_loader = DataLoader(dataset=mnist_train,
                         batch_size=100,
                         shuffle=True,
                         drop_last=True)
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Linear(256, 10)
)

loss_func = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

for epoch in range(15):
    avg_loss = 0
    total_batch = len(data_loader)

    for x_train, y_train in data_loader:
        optimizer.zero_grad()
        x_train = x_train.view(-1, 28*28)
        hypothesis = model(x_train)
        loss = loss_func(hypothesis, y_train)
        loss.backward()
        optimizer.step()

        avg_loss += loss / total_batch
    print('epoch:{} avg_loss:{:.4f}'.format(epoch + 1, avg_loss))

import random
import matplotlib.pyplot as plt

with torch.no_grad():
    x_test = mnist_test.test_data.view(-1,28*28).float()
    y_test = mnist_test.test_labels

    predictions = model(x_test)
    correction_prediction = torch.argmax(predictions, dim=1) == y_test
    accuracy = correction_prediction.float().mean()
    print('accuracy:', accuracy.item())
    print()

    r = random.randint(0, len(mnist_test)-1)
    x_single_data = mnist_test.test_data[r:r+1].view(-1,28*28).float()
    y_single_data = mnist_test.test_labels[r:r+1]
    print('label:', y_single_data.item())
    s_prediction = model(x_single_data)
    print('prediction:',torch.argmax(s_prediction, dim=1).item())

    plt.imshow(mnist_test.test_data[r:r+1].view(28,28), cmap='gray')
    plt.show()