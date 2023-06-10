# 상속
import torch.nn as nn
import torch

class CustomLinear(nn.Module): # module을 상속 받는다.
    def __init__(self, input_size,out_size):
        super().__init__()
        self.linear = nn.Linear(input_size, out_size)

    def forward(self, x): # predict 값을 받는다.
        y = self.linear(x)
        return y

x = torch.FloatTensor(torch.randn(16,10))
CModel = CustomLinear(10,5)
#y = CModel.forward(x)
y = CModel(x) # 위와 동일. 이런 형태로 많이 씀. decorate 함수의 일종, call 함수가 호출되는데 forward가 호출되도록 됨
print(y)
print()
print(CModel.forward(x))



