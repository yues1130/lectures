import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

class CustomDataset(Dataset):# dataset 상속
    def __init__(self):
        self.x_data = torch.FloatTensor([[73, 80, 75],
                                         [93, 88, 92],
                                         [89, 91, 90],
                                         [96, 98, 100],
                                         [73, 64, 70]])
        self.y_data = torch.FloatTensor([[152], [185], [180], [196], [142]])

    def __len__(self): # data의 수를 먼저 확인해야 함
        return len(self.x_data)

    def __getitem__(self, idx):
        x = torch.FloatTensor(self.x_data[idx])
        y = torch.FloatTensor(self.y_data[idx])
        return x, y # 앞의 tensor dataset과 동일한 것으로 만들어줌

dataset = CustomDataset()
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

for data in dataloader:
    print(data, end='\n\n')

model = nn.Linear(3,1)
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