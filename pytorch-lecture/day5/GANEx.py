# GAN -> Generator 생성모델(위조지폐범)과 Discriminator 분류모델(경찰)의 경쟁하는 메커니즘으로 학습
import torch
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import torch.nn as nn
import matplotlib.pyplot as plt
import torch.optim as optim

total_epochs = 30 # 30
batch_size = 100

trainset = dset.FashionMNIST(root='FashionMNIST_data/',
                             train=True,
                             download=True,
                             transform=transforms.Compose([
                                 transforms.ToTensor(),
                                 transforms.Normalize((0.5,), (0.5,))
                             ]))
train_loader = DataLoader(dataset=trainset,
                          batch_size=batch_size,
                          shuffle=True)

G = nn.Sequential(
    nn.Linear(64, 256),
    nn.ReLU(),
    nn.Linear(256, 256),
    nn.ReLU(),
    nn.Linear(256, 784),
    nn.Tanh()
)

D = nn.Sequential(
    nn.Linear(784, 256),
    nn.LeakyReLU(0.2),
    nn.Linear(256, 256),
    nn.LeakyReLU(0.2),
    nn.Linear(256, 1),
    nn.Sigmoid()
)

loss_func = nn.BCELoss()
d_optimizer = optim.Adam(D.parameters(), lr=0.0002)
g_optimizer = optim.Adam(G.parameters(), lr=0.0002)

for epoch in range(total_epochs):
    for i, (image, _) in enumerate(train_loader):
        image = image.view(batch_size, -1)
        real_label = torch.ones(batch_size, 1)
        fake_label = torch.zeros(batch_size, 1)

        outputs = D(image) # real image 데이터 discriminator에 입력
        d_loss_real = loss_func(outputs, real_label)

        z = torch.rand(batch_size, 64) # noise 값 생성
        fake_images = G(z) # fake image 생성
        outputs = D(fake_images) # fake image를 discriminator에 입력
        d_loss_fake = loss_func(outputs, fake_label)
        
        # Discriminator 학승
        d_loss = d_loss_real + d_loss_fake
        d_optimizer.zero_grad()
        g_optimizer.zero_grad()
        d_loss.backward()
        d_optimizer.step()

        # Generator 학승
        fake_images = G(z)
        outputs = D(fake_images)
        g_loss = loss_func(outputs, real_label) # 진짜로 느끼게끔 학습
        g_optimizer.zero_grad()
        d_optimizer.zero_grad()
        g_loss.backward()
        g_optimizer.step()

    print('epoch:{} d_loss:{:.4f}  g_loss:{:.4f}'.format(epoch, d_loss.item(), g_loss.item()))

z = torch.randn(batch_size, 64)
fake_images = G(z)

import numpy as np

for i in range(3):
    fake_images_img = np.reshape(fake_images.data.numpy()[i], (28, 28))
    plt.imshow(fake_images_img, cmap='gray')
    plt.show()


