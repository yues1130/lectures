# 9. Legend
# https://www.youtube.com/watch?v=KcBCkVCSFqU&list=PLem3bYZSADLL7JZ_UM9_2v8wO-dEh3j4k&index=10



# ax.plot(..., label='label') works, but if you want more...

# Legend handle: line0, = ax.plot(...)
# ax.legend(handles, labels)

# handles = [ine0, line1, ...]
# labels = ['label0', 'label1', ...]

# changing the order of labels
# replacing the key with a better-looking one



# 1) Legend options

# bbox_to_anchor: location of the bbox
# loc: relative location to bbox_to_anchor
# ncol: number of columns
# frameon: T (visible frame), F
# fontsize: label fontsize
# markerscale: scale-up/down marker size
# markerfirst: T (marker-label), F (label-marker)
# mode: if 'expand', it fills out the bbox

# labelspacing, handlelength, handletextpad, borderpad, borderaxespad, columnspacing, framealpha, facecolor, edgecolor

# 2) Legend structure

# bbox_to_anchor = (x,y,width,height): legend box shares (x,y) with its loc 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

x = np.linspace(-4,4,10000)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.sin(2*x)
y3 = np.cos(2*x)
ax = plt.gca()
line0, = ax.plot(x,y0)
line1, = ax.plot(x,y1)
line2, = ax.plot(x,y2)
line3, = ax.plot(x,y3)
ax.set_xlim(-4,4)
ax.set_ylim(-1,1)
handles = [line0, line1, line2, line3]
labels = ['a','b','c','d']
ax.legend(handles, labels, bbox_to_anchor=(0, 1.02, 1, 0.5),
          ncol=2, mode='expand',
          loc='lower right',
          borderaxespad=0)


# ax.legend(handles, labels, bbox_)
plt.show()


# 3) Two legends
ax = plt.gca()
lines = []
styles = ['-','--','-.',':']
x = np.linspace(0, 10, 1000)

for i in range(4):
    lines += ax.plot(x, np.sin(x - i * np.pi / 2),
                     styles[i], color='black')
ax.axis('equal') # equal scaling in x & y axis

# Specify the lines and labels of the first legend
leg1 = ax.legend(lines[:2], ['line A','line B'],
                 loc='upper right', frameon=False)

# Create the second legend and add the artist manually
leg2 = mpl.legend.Legend(ax, lines[2:], ['line C', 'line D'],
                         loc='lower right', frameon=False)
ax.add_artist(leg2)




# Legend: more modifiers

# To change frame line width/color/style
leg = ax.legend(...)
frame = leg.get_frame()
frame.set_linewidth(2)
frame.set_edgecolor('black')
frame.set_linestyle(':')

# to update keys without changing the main plot

# change line width
leg = ax.legend(...)
for line in leg.get_lines():
    line.set_linewidth(4.0)


# change line & marker
blue_line = mpl.lines.mlines.Line2D([],[],color='blue',
                                    marker='*', markersize=15, label='Blue stars')
plt.legend(handles=[blue_line])











































