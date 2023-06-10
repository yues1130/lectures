# Linear regression 선형회귀 (원시적 형태)
import torch
import torch.optim as optim

x1_train = torch.FloatTensor([[73],[93],[89],[96],[73]])
x2_train = torch.FloatTensor([[80],[88],[91],[98],[65]])
x3_train = torch.FloatTensor([[75],[92],[98],[100],[70]])
y_train = torch.FloatTensor([[152],[185],[180],[196],[142]])

w1 = torch.zeros((1,1),requires_grad=True)
w2 = torch.zeros((1,1),requires_grad=True)
w3 = torch.zeros((1,1),requires_grad=True)
b = torch.zeros(1, requires_grad=True)

# SGD (Stochastic Gradient Descent): 확률적 경사 하강법
optimizer = optim.SGD([w1, w2, w3, b], lr=1e-5) # lr: learning rate

for epoch in range(1000):
    # y = w1 * x1 + w2 * x2 +  w3 * x3 + b
    hypothesis = torch.mm(x1_train, w1) + torch.mm(x2_train, w2) + torch.mm(x3_train, w3) + b # 예측값
    loss = torch.mean((hypothesis - y_train)**2) # MSE (mean square error)
    optimizer.zero_grad() # 미분값 초기화, 누적되지 않도록
    loss.backward() # 미분값
    optimizer.step() # 변수와 미분값을 참조해 lr를 곱해서 빼줌 w1 = w1 - lr * gradient

    if epoch % 100 == 0: # (a % b) : a를 b로 나누고 나머지를 반환
        print('epoch:{}, w1:{:.3f}, w2:{:.3f}, w3:{:.3f}, b:{:.3f}, const:{:.3f}'
              .format(epoch+1, w1.item(), w2.item(), w3.item(), b.item(), loss.item()))
