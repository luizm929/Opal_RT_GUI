#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#--------------------------------
# Packages needed
# Matplotlib
# Python3
# PyQt5
#
#------------------------------------------------------------
#
# Written by Luis Martinez : luizmartines@gmail.com
#                          : luizm929@nmsu.edu
#------------------------------------------------------------
# Files needed for this program to run:
# mainWindow.py
# phasor_plots.py
# readings.txt
#------------------------------------------------------------
# If you include pictures you should import:
# resources_rc.py

#------------------------------------------------------------

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle, Arrow
import numpy as np

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# Packages needed
# Matplotlib
# Python3
# PyQt5
#
# ------------------------------------------------------------
#
# Written by Luis Martinez : luizmartines@gmail.com
#                          : luizm929@nmsu.edu
# ------------------------------------------------------------
# Files needed for this program to run:
# mainWindow.py
# phasor_plots.py
# readings.txt
# ------------------------------------------------------------
# If you include pictures you should import:
# resources_rc.py

# ------------------------------------------------------------

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib
from PyQt5.QtCore import QTimer, QSize

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Plotting style ideal for engineering
import matplotlib.style as style

# Dark background good for battery powered devices.
# style.use(['bmh' , 'dark_background'])
# Good styles
# style.use('seaborn-paper')  # clean clear colors
# style.use('seaborn-pastel')

# -----currently used style--------#
style.use('bmh')

from PyQt5.QtWidgets import QSizePolicy
import os
import errno

# When running on console change path to where the file lives (drive E in my case).
# You only have to worry about this if you run it from a hard drive that is not C drive.
# TODO Fix the path problem (when we change HD program complains it cannot find files).
cur_path = os.getcwd()
std_path = cur_path[0:cur_path.index("\\") + 1]
new_path = std_path + '\\NMSU_Software_Projects\\Relays_GUI\\'
flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY

try:
    os.chdir(new_path)
except OSError as exc:
    if exc.errno != errno.EEXIST:
        os.makedirs(new_path)
    else:
        pass
# ------------------------------------------------------

# Prints the versions of matplotlib and backend
# print ("matplotlib.__version__   = ", matplotlib.__version__)
# print ("matplotlib.get_backend() = ", matplotlib.get_backend())

import matplotlib.lines as mlines


# def legends(self):


class mplCanvas(FigureCanvas):
    # Any setting you want to modify with the GUI will first have to me modified here
    # this is the class that redraws(updates) the plots.

    def __init__(self, parent=None, width=matplotlib.rcParams['figure.figsize'],
                 height=matplotlib.rcParams['figure.figsize'], dpi=100):
        size = min(width, height)

        fig = Figure(size, dpi=dpi)

        self.axes = fig.add_subplot(111, polar=True)

        # ----------------------------------------------------------------------
        # If we wanted to modify the font size through the GUI we would create a call in the gui
        # and it would point here.
        # Size of font that prints degrees (0 - 360 degs) around the phasor
        plt.rc('xtick', labelsize=10)
        # # Determines size of font on the r values
        plt.rc('ytick', labelsize=9)

        # -----------------------------------------------------------------------

        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Preferred,
                                   QSizePolicy.Preferred)
        FigureCanvas.updateGeometry(self)
        # How often the plot gets updated, gets defined here.
        timer = QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(2000)

    def minimumSizeHint(self):
        return QSize(100, 200)

    def compute_initial_figure(self):
        pass

    def update_figure(self):
        pass



nmax = 9
xdata = range(nmax)
ydata = np.random.random(nmax)

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

    fig.canvas.draw_idle()
    plt.pause(0.4)

plt.waitforbuttonpress()
plt.show()