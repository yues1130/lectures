import matplotlib as mpl
#%matplotlib notebook
#%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker

import numpy as np
x = np.linspace(1,10,10)
y = np.linspace(1,10,10)



# 1. Line & Marker

# 1) line style
# linestyle=str or ls=str
# solid line: 'solid' or '-'
# dashed line: 'dashed' or '--'
# dash-dotted line: 'dash-dotted' or '-.'
# dotted line: 'dotted' or ':'
# draw nothing: 'None' or ' ' or ''
# dash tuple: dash length/spacing

# 2) line width
# linewidth=num or lw=num

# 3) line color
# linecolor=str or lc=str
# color HEX code: c = '#RRGGBB'
# v2.0: C0, C1, C2, ..., C9
# greyscale: c = 'num'

# 4) marker
# marker=str
# point: '.'
# circle: 'o'
# square: 's'
# plus: '+'
# x: 'x'
# diamond: 'D'
# triangles: 'v' or '^' or '<' or '>'

# 5) marker size
# markersize=num or ms=num

# 6) marker face color
# markerfacecolor=srt or mfc=str
# for empty, mfc='None'

# 7) marker edge color
# markeredgecolor=srt or mec=str
# for empty, mec='None'

# 8) marker edge width
# markeredgewidth=num or mew=num

# 9) alpha: transparency

# c + marker + ls
# fmt=str:[color][marker][line]

ls = '-'
lw = 1
lc = 'C0'
marker = 'o'
ms = 7.5
mfc = 'C0'
mec = 'k'
mew = 0.5
a = 1

fmt=lc+marker+ls

plt.plot(x,y, ls=ls, lw = lw, alpha=a,
         marker = marker,ms=ms,mfc=mfc,mec=mec,mew = mew)
#plt.plot(x,y,fmt)
#plt.savefig('test')
plt.savefig('test.eps', format='eps')
plt.show()



# 2. Error bar
xe = np.random.rand(len(x))
ye = np.random.rand(len(y))

# 1) error bar line width
# elinewidth
# default: line color

# 2) error bar line color
# ecolor
# default: line width

# 3) length of the bar cap
# capsize
# default: no cap

# 4) thickness of the bar cap
# capthick
# default: mew

# 5) put error bar every [num] data points
# errorevery=num
# default: 1

ec = 'C1'
ew = 1
cs = 5
ct = 3

plt.errorbar(x,y,yerr=ye,xerr=xe,fmt='o')
plt.show()

plt.errorbar(x,y,yerr=ye,fmt='-o',
             ecolor=ec, elinewidth=ew, capsize=cs, capthick=ct)
plt.show()

plt.errorbar(x,y,xerr=xe,fmt='o')
plt.show()


# 3. Legend & Label
plt.plot(x,y, label='1')
plt.plot(x,2*y, label='2')
plt.xlim(0,15)
plt.ylim(0,20)
plt.legend()
plt.show()

# legend(loc,grameon)
# loc = int or string
# 0 ~ 10
# custom location: loc=(x,y)
# x, y in the range of [0,1], relative coordinates of the lower-left corner of legend box

# frameon = True or False
# turn on/off a frame
# default: True


# 4. XY limits
plt.plot(x,y)
plt.xlim(0,12)
plt.ylim(0,12)
plt.show()


# 5. Ticks
plt.plot(x,y)
plt.xlim(0,12)
plt.ylim(0,12)
plt.xticks(np.arange(0,21,5))
plt.yticks(np.arange(0,21,20), [r'$alpha$', r'$beta$'])
plt.show()

# removing ticks
# plt.xticks([])
# plt.yticks([])
plt.plot(x,y)
plt.xlim(0,12)
plt.ylim(0,12)
plt.xticks([])
plt.yticks([])
plt.show()


# 6. Logarithmic-scale axis
# default: basex = 10, basey = 10
plt.plot(x,y)
plt.xscale('log',base=2)
plt.yscale('log')
plt.show()


# Things not mentioned
# Adding grid: plt.grid()




# OOP (object-oriented style)
# plt의 function을 call해서 그림을 구성하는 것이 아닌
# axes의 instance를 발생시켜 object를 만들고,
# object에 해당하는 function을 이용해 그림을 그림
# multi-panel을 그릴 때 유리

# Basic Structure of matplotlib
# import packages
# update rcParams: mpl.rcParams.update(...)
# size: fig = plt.figure(figsize=...)
# get axes: ax = plt.gca()
# adjust margins: plt.tight_layout(...)
# save figure: plt.savefig("fig.pdf")


# parent Axes instance
# ax = plt.gca()
# gca: get the current axes

# Methods
# https://matplotlib.org/stable/api/axes_api.html
# ax.plot()
# ax.errorbar()
# ax.scatter()
# ax.loglog()
# ax.tick_params()
# ax.set_xlim()
# ax.set_ylim()
# ax.set_xlabel()
# ax.set_ylabel()
# ax.set_xticks()
# ax.set_yticks()
# ax.set_xscale()
# ax.set_yscale()

# spine formats (frame box): ax.spines
# axis formats: ax.xaxis, ax.yaxis














