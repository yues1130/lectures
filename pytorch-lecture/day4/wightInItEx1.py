import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def ReLU(x):
    return np.maximum(0, x)


input_data = np.random.randn(1000, 100)

node_num = 100
hidden_layer_size = 5
activations = {}
x = input_data

for i in range(hidden_layer_size):
    if i != 0:
        x = activations[i - 1]

    # w = np.random.randn(node_num, node_num) # 0과 1에 값이 많이 분포되어 있어서 학습이 어려움
    # w = np.random.randn(node_num, node_num) * 0.01 # 양 사이드에 분포된 값은 없앴으나 가운데에 집중되어 있음 (위보다는 낫다)
    # w = np.random.randn(node_num, node_num) * np.sqrt(1.0 / node_num) #xavier # 분포도 넓히기 위해 num_in + num_out으로 더히가 나눈 값. xavier가 default로 잡혀 있음
    w = np.random.randn(node_num, node_num) * np.sqrt(2.0 / node_num)  # kaming he #

    a = np.dot(x, w)
    # output = sigmoid(a)
    output = ReLU(a)
    activations[i] = output

for i, a in activations.items():
    plt.subplot(1, len(activations), i + 1)
    plt.title(str(i + 1) + '-layer')
    if i != 0:
        plt.yticks([], [])
    plt.hist(a.flatten(), 30, range=(0, 1))
    plt.xlim(0.1, 1)  # Relu는 0이 의미가 없으므로 Relu 사용 시 풀어준다
    plt.ylim(0, 7000)  # Relu는 0이 의미가 없으므로 Relu 사용 시 풀어준다
plt.show()




