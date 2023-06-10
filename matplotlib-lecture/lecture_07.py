import matplotlib as mpl
#from mplset import rcParams_default
#mpl.rcParams.update(rcParams_default)
#mpl.rcParams.update(mpl.rcParamsDefault)

# Lecture 07: spins, axis label, ticker
# https://www.youtube.com/watch?v=HHZP0F3lf5M&list=PLem3bYZSADLL7JZ_UM9_2v8wO-dEh3j4k&index=7

# 1. Spines: graph의 경계선 특성을 control하는 메서드

# ax.spines[loc]: loc = "top", "bottom", "left", "right"

# Open-box plot: remove top and right spines (tick은 남음)
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)

# Thickness of spines
# ax.spines["left"].set_linewidth(3)
# ax.spines["bottom"].set_linewidth(3)

# Color of spines
# ax.spines["left"].set_color("r")

import matplotlib.pyplot as plt
import numpy as np

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(1.0)
ax.spines['left'].set_linewidth(1.0)
ax.spines['left'].set_color("r")
plt.tick_params(top=False, right=False)

x = np.linspace(-100,100,2000)
y = np.sin(x)
plt.plot(x,y)
plt.xlim(-6,6)


# 2. Ticks

# ax.tick_params(...)
# or plt.tick_parmas(...)

# axis = {'x', 'y', 'both'}, specifies the axis to be controlled
# which = {'major', 'minor', 'both'}
# direction = {'in', 'out', 'inout'}
# bottom, top, left, right = True/False to turn on/off the ticks
# labelbottom, labeltop, labelleft, labelright = True/False to turn on/off the tick labels

# APIs: matplotlib.org/api/axis_api.html

ax = plt.gca() # get the current axes instance

# ax.set_xlabel('x', labelpad=num, fontsize=num) # x-label
# ax.set_ylabel('y', labelpad=num, fontsize=num) # y-label

ax.xaxis.set_tick_params()
ax.yaxis.set_tick_params()

# options are the same as in plt.tick_parms() except the axisx option
# which it is already set by the parent instance (xaxis, yaxis)

# size and margin options:
# length, width, pad, labelsize

# tick parameters except label pad
#ax.xaxis.set_tick_params(which='major', direction='out', ...,
#                         length=length, width=width, pad=pad, labelsize=labelsize)

# same as
# ax.tick_params(axis='x', ...) or
# ax.tick_params(axis='y', ...)

# label pad
# ax.set_xlabel('x-label', labelpad=labelpad)

































