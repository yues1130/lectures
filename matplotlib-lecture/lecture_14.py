# 14. Other types of plot
# https://www.youtube.com/watch?v=LXikrntvAxk&list=PLem3bYZSADLL7JZ_UM9_2v8wO-dEh3j4k&index=14

# 1. Two y-axis in the same plot
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2*np.pi*t)

ax1 = plt.gca()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('sin', color=color)
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)


# 2. Histogram