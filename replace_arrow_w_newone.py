from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle, Arrow
import numpy as np
import random

nmax = 9
xdata = random.gauss(1.0, 2.0)
ydata = random.gauss(1.0, 2.0)

plt.ion()
fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.plot(xdata, ydata, 'o-')
ax.set_xlim(-1,10)
ax.set_ylim(-1,4)


rect = Rectangle((0, 0), nmax, 1, zorder=10)
ax.add_patch(rect)

x0, y0 = 5, 3
arrow = Arrow(1,1,x0-1,y0-1, color="#aa0088")

a = ax.add_patch(arrow)

plt.draw()

for i in range(nmax):
    rect.set_x(i)
    rect.set_width(nmax - i)

    a.remove()
    arrow = Arrow(1+i,1,x0-i+1,y0-1, color="#aa0088")
    a = ax.add_patch(arrow)

    #fig.canvas.draw_idle()
    plt.pause(0.4)

plt.waitforbuttonpress()
plt.show()