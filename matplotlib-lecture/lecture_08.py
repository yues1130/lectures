# 8. Tick locator & formatter
# https://www.youtube.com/watch?v=5WfAvvlkRHU&list=PLem3bYZSADLL7JZ_UM9_2v8wO-dEh3j4k&index=8

# matplotlib.ticker provides
# NullLocator() : no ticks
# MultipleLocator() : a multiple of int/float, 등간격 설정
# LogLocator() : space ticks logarithmically
# AutoLocator(), AutoMinorLocator() : auto

# NullFormatter() : no tick labels
# FixedFormatter() : sets the tick labels manually
# LogFormatter() : tick labels for a logarithmic scale axis
# FuncFormatter() : from a given function
# FormatStrFormatter() : like a printf
# ScalarFormatter() : default, auto

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.yaxis.set_major_locator(ticker.NullLocator())
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.tick_params(which='major', width=1, length=5)
ax.tick_params(which='minor', width=0.75, length=2.5)
ax.set_xlim(0,5)
ax.set_ylim(0,1)

# 1) 
#ax.xaxis.set_major_locator(ticker.AutoLocator())
#ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())

# 2) 등간격 locator
#ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))

# 3) 
"""
ax = plt.gca()
ax.set_xlim(10**3, 10**10)
ax.set_xscale('log')
loc_major = ticker.LogLocator(base=100.0, numticks=15) # numticks 표시하는 수
loc_minor = ticker.LogLocator(base=100.0, subs=(0.1,))
# minor tick subs: subs[j]*base**i
ax.xaxis.set_major_locator(loc_major)
ax.xaxis.set_minor_locator(loc_minor)
ax.xaxis.set_minor_formatter(ticker.NullFormatter())
"""

ax = plt.gca()
ax.set_xlim(0,5)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1.00))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.25))
#ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:g}"))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))


ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.2f}"))
#ax.xaxis.set_major_formatter(ticker.FormatStrFormatter("%.2f"))


ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: r"$%d\pi$" % x if x!= 0 else "0"))


























