import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

class CustomDataset(Dataset):# dataset 상속
    def __init__(self):
        self.x_data = torch.FloatTensor([ [1,2],[2,3],[3,1],[4,3],[5,3],[6,2] ])
        self.y_data = torch.FloatTensor([ [0],[0],[0],[1],[1],[1] ])

    def __len__(self): # data의 수를 먼저 확인해야 함
        return len(self.x_data)

    def __getitem__(self, idx):
        x = torch.FloatTensor(self.x_data[idx])
        y = torch.FloatTensor(self.y_data[idx])
        return x, y # 앞의 tensor dataset과 동일한 것으로 만들어줌

dataset = CustomDataset()
dataloader = DataLoader(dataset)

for data in dataloader:
    print(data, end='\n\n')

#model = nn.Linear(2,1)
model = nn.Sequential( nn.Linear(2, 1), nn.Sigmoid()) # input_dim = 2, output_dim = 1 & 출력은 시그모이드 함수를 거친다
#model = torch.sigmoid(nn.Linear(2,1))
optimizer = torch.optim.SGD(model.parameters(), lr=1e-5)

import torch.nn.functional as F

for epoch in range(20):
    for batch_idx, data in enumerate(dataloader):
        batch_x,batch_y = data
        hypothesis = model(batch_x)
        cost = F.mse_loss(hypothesis, batch_y)
        optimizer.zero_grad()
        cost.backward()
        optimizer.step()
        print('cost: {:.4f}'.format(cost.item()))