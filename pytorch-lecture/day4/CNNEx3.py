import torch
import torch.nn as nn
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

batch_size = 20
learning_rate = 0.0002
total_epochs = 20

img_dir = 'images'
img_data = dset.ImageFolder(img_dir,
                            transforms.Compose([
                                transforms.Resize(256),
                                transforms.RandomSizedCrop(224),
                                transforms.ToTensor()
                            ]))
train_loader = DataLoader(img_data,
                          batch_size=batch_size,
                          shuffle=True)

def conv_2_block(in_dim, out_dim):
    model = nn.Sequential(
        nn.Conv2d(in_dim, out_dim, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.Conv2d(out_dim, out_dim, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2, 2)
    )
    return model

def conv_3_block(in_dim, out_dim):
    model = nn.Sequential(
        nn.Conv2d(in_dim, out_dim, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.Conv2d(out_dim, out_dim, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.Conv2d(out_dim, out_dim, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2, 2)
    )
    return model

class VGG16(nn.Module):
    def __init__(self, base_dim, num_classes=2):
        super().__init__()
        self.feature = nn.Sequential(
            conv_2_block(3, base_dim),
            conv_2_block(base_dim, 2 * base_dim),
            conv_3_block(base_dim * 2, base_dim * 4),
            conv_3_block(base_dim * 4, base_dim * 8),
            conv_3_block(base_dim * 8, base_dim * 8)
        )

        self.fc_layer = nn.Sequential(
            nn.Linear(base_dim * 8 * 7 * 7, 100),
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(100, 20),
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(20, num_classes)
        )

    def forward(self, x):
        x = self.feature(x)
        x = x.view(x.size(0), -1)
        y = self.fc_layer(x)
        return y

model = VGG16(base_dim=16)
loss_func = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for c in model.children():
    print(c)

for i in range(total_epochs):
    for x_train, y_train in train_loader:
        optimizer.zero_grad()
        hypothesis = model(x_train)
        loss = loss_func(hypothesis, y_train)
        loss.backward()
        optimizer.step()
    print('epoch:{} loss:{:.4f}'.format(i + 1, loss.item()))
