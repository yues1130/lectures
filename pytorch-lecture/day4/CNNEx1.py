# CNN
import torch
import torch.nn as nn

inputs = torch.Tensor(1,1,28,28)

# Convolution
conv1 = nn.Conv2d(in_channels=1,
                  out_channels=32,
                  kernel_size=3,
                  padding=1) # same padding
print(conv1)

conv2 = nn.Conv2d(32,64,3, padding=1) # conv1의 output을 받는다.

pool = nn.MaxPool2d(kernel_size=2) # max pooling
print(pool)
print()

output = conv1(inputs)
print(output.size())

output = conv2(output)
print(output.size())

output = pool(output)
print(output.size())

output = output.view(output.size(0), -1)
print(output.size()) # 64 * 14 * 14

flayer = nn.Linear(12544, 10)
output = flayer(output)
print(output.size())


