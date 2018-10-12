#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# First line above makes sure this is compatible with Linux as well as Windows,
# so probably will be compatible with MacOS but has not been tested with MacOS.
# --------------------------------
# Packages needed
# Matplotlib
# Python3
# PyQt5
# Pyserial
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
import os
import errno
import numpy as np
#import math
import matplotlib.pyplot as plt
import matplotlib
from PyQt5.QtCore import QTimer, QSize
from PyQt5.QtWidgets import QSizePolicy

"""This call to matplotlib.use() has no effect because the backend has already
been chosen; matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time. For this reason we comment out next line. """
#matplotlib.use("Qt5Agg")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.lines as mlines
# Plotting style ideal for engineering
import matplotlib.style as style
# Dark background good for battery powered devices.
#style.use(['bmh' , 'dark_background'])
# Good styles
# style.use('seaborn-paper')  # clean clear colors
# style.use('seaborn-pastel')

# -----currently used style--------#
style.use('bmh')



# When running on console change path to where the file lives (drive E in my case).
# You only have to worry about this if you run it from a hard drive that is not C drive.
# TODO Fix the path problem (when we change HD program complains it cannot find files).
cur_path = os.getcwd()
std_path = cur_path[0:cur_path.index("\\") + 1]
new_path = std_path + '\\NMSU_Software_Projects\\Opal_RT_GUI\\'
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



class mplCanvas(FigureCanvas):
    # This is the engine that drives the plots.
    # Any setting you want to modify with the GUI will first have to me modified here
    # this is the class that calls update_figure() to redraw the plot.

    def __init__(self, parent=None, width=matplotlib.rcParams['figure.figsize'],
                 height=matplotlib.rcParams['figure.figsize'], dpi=100):
        size = min(width, height)
        global fig
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
        # The plot gets updated every second.
        timer.start(1000)

    def minimumSizeHint(self):
        return QSize(100, 200)

    def compute_initial_figure(self):
        pass

    def update_figure(self):
        pass


# Package format:
# ---| Time(s) | |Ia| | Ia angle | |Ib| | Ib angle | |Ic|  | Ic angle |  ---

""" loc code for wide monitors  2,6,10
    loc codes for non wide monitors 5,8
    if you want to manage this from the GUI we need to declare loc in mplCanvas
    because mplCanvas class is the one in charge of calling update_figure() """
loc = 10


# ----------------------------------------------------------------------------

class CurrentPhasor(mplCanvas):
    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        # A
        self.phase_a = self.axes.arrow(0, 0, 0, 1, alpha=0.5, width=0.015,
                                       edgecolor='blue', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True)
        # B
        self.phase_b = self.axes.arrow(120 / 180. * np.pi, 0, 0, 1, alpha=0.5, width=0.015,
                                       edgecolor='green', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True)
        # C
        self.phase_c = self.axes.arrow(-120 / 180. * np.pi, 0, 0, 1, alpha=0.5, width=0.015,
                                       edgecolor='red', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True)

    def update_figure(self):
        self.axes.clear()
        # Size of font that prints degrees (0 - 360 degs) around the phasor
        self.axes.set_rticks([0.2, 0.4, 0.6, 0.8, 1.0])
        self.axes.set_rmax(1.0)
        self.axes.grid(True)
        #-----------------------------------------------------------------------
        # THis is the txt file we are going to read the values from.
        with open(new_path + '\\readings.txt', 'r') as f:
            # d=list(f)
            d = f.readlines()
        #---------------------------------------------------------------------------
        # check that the file was properly closed
        #print(f.closed)

        r1 = []
        theta1 = []
        r2 = []
        theta2 = []
        r3 = []
        theta3 = []

        # TODO fix the annotation plot
        # degrees font size
        # r1 = np.arange(0, 3.0, 0.01)
        # theta1= 2*np.pi*r1

        for line in d:
            hold = line.split(",")
            r1.append(float(hold[1]))
            theta1.append(float(hold[2]))
            r2.append(float(hold[3]))
            theta2.append(float(hold[4]))
            r3.append(float(hold[5]))
            theta3.append(float(hold[6]))
            # print(r1)

        '''                     !! EXPERIMENTAL !! 
        This will be a dictionary that will hold all arguments for arrows.
        This way we can change how all arrows look by modifying only this dictionary'''
        # args = {'alpha': 1,
        #              'width': 0.025,
        #              'edgecolor': 'blue',
        #              'facecolor': '#17202A',
        #              'lw': 2,
        #              'zorder': 5,
        #              'length_includes_head': True}


        # Axes.arrow(x, y, dx, dy, **kwargs)
        # X and dy are used to control the phasor position
        nmax = 9
        import random
        global xdata, ydata, x1data, y1data, x2data,y2data
        xdata = random.random()
        ydata = random.random()
        x1data = random.random()
        y1data = random.random()
        x2data = random.random()
        y2data = random.random()
        #print(xdata,ydata)

        for i in range(nmax):

            self.phase_a = self.axes.arrow(xdata, 0, 0, ydata, alpha=1, width=0.025,
                                       edgecolor='blue', facecolor='#17202A', lw=2, zorder=5,
                                           length_includes_head=True)
            # B
            self.phase_b = self.axes.arrow(180+x1data, 0, 0, y1data, alpha=1, width=0.015,
                                       edgecolor='green', facecolor='#17202A', lw=2, zorder=5,
                                           length_includes_head=True)
            # C
            self.phase_c = self.axes.arrow(-x2data, 0, 0, y2data, alpha=1, width=0.015,
                                           edgecolor='red', facecolor='#17202A', lw=2, zorder=5,
                                           length_includes_head=True)


            #fig.canvas.draw_idle()
            #plt.pause(0.2)
        # removes phasor a
        # self.phase_a.remove()
        self.phase_a.remove()
        self.phase_b.remove()
        self.phase_c.remove()

        self.axes.set_title("Current 3φ", fontsize=10)
        # Since self.axes.arrow() does not have an artist we can create a label from.
        # we write a custom artist and create its label.
        # the two empty arrays are x, y position wich are given as a 2-tuple or in bbox=()
        # If given as 2-tuple remember that 0,0 is at left bottom corner of plot.
        blue_line = mlines.Line2D([], [], color='blue', markersize=6, label='φA')
        green_line = mlines.Line2D([], [], color='green', markersize=3, label='φB')
        red_line = mlines.Line2D([], [], color='red', markersize=3, label='φC')

        # ---------------------------------------------------------------------------------------
        # TODO fix making the alpha of rticks look transparent when arrows are on top of rticks.
        for label in self.axes.get_xticklabels() + self.axes.get_yticklabels():
            label.set_fontsize(9)
            label.set_bbox(dict(facecolor='black', edgecolor='None', alpha=0.015))
        # ----------------------------------------------------------------------------------------
        # loc code for wide screen  2,6,10
        # loc codes for non wide screens 5,8
        self.axes.legend(handles=[blue_line, green_line, red_line], bbox_to_anchor=(0., 1.1), loc=loc, borderaxespad=0)
        # self.axes.legend(handles=[], bbox_to_anchor=(0., 1.1), loc=loc, borderaxespad=0)
        self.draw()
        plt.show()

        # --------------Experimental --------------------------------------


class VoltagePhasor(mplCanvas):
    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        # A
        self.phase_a = self.axes.arrow(0, 0, 0, 1, alpha=0.5, width=0.015,
                                  edgecolor='blue', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True,
                                  label='Phase A')

        # B
        self.phase_b = self.axes.arrow(120 / 180. * np.pi, 0, 0, 1, alpha=0.5, width=0.015,
                                  edgecolor='green', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True)
        # C
        self.phase_c = self.axes.arrow(-120 / 180. * np.pi, 0, 0, 1, alpha=0.5, width=0.015,
                                  edgecolor='red', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True)

    def update_figure(self):
        self.axes.clear()
        # Size of font that prints degrees (0 - 360 degs) around the phasor
        self.axes.set_rticks([0.2, 0.4, 0.6, 0.8, 1.0])

        self.axes.set_rmax(1.0)
        self.axes.grid(True)

        # Size of font that prints degrees (0 - 360 degs) around the phasor
        # plt.rc('xtick', labelsize=10)
        # # Determines size of font on the r values

        # EXPERIMENTAL ----------------------------------
        # self.axes.set_axis_on()
        # self.axes.autoscale(enable=False,axis='both',tight=None)
        # --------------------------------------------------------

        # THis is the txt file we are going to read the values from.
        with open(new_path + '\\readings.txt', 'r') as f:
            d = f.readlines()
        f.close()
        # Below are the definitions of arrays that will store the values of txt file
        r1 = []
        theta1 = []
        r2 = []
        theta2 = []
        r3 = []
        theta3 = []

        # TODO fix the swirly plot
        # degrees font size
        # r1 = np.arange(0, 3.0, 0.01)
        # theta1= 2*np.pi*r1

        # -------------------------------------
        # This will drive the vectors
        for i in range(len(d)):
            hold = d[i].split(',')
            r1.append(float(hold[0]))
            theta1.append(float(hold[0]))
            r2.append(float(hold[0]))
            theta2.append(float(hold[0]))
            r3.append(float(hold[0]))
            theta3.append(float(hold[0]))

        # Axes.arrow(x, y, dx, dy, **kwargs)
        # X and dy are used to control the phasor position
        self.phase_a = self.axes.arrow(x1data, 0, 0, y1data, alpha=1, width=0.015,
                                       edgecolor='blue', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True,
                                       label='A')

        # B
        self.phase_b = self.axes.arrow(x2data, 0, 0, y2data, alpha=1, width=0.015,
                                       edgecolor='green', facecolor='#17202A', lw=2, zorder=5,
                                       length_includes_head=True, label='B')
        # C
        self.phase_c = self.axes.arrow(xdata, 0, 0, ydata, alpha=1, width=0.015,
                                       edgecolor='red', lw=2, zorder=5, length_includes_head=True, label='C')

        self.axes.set_title("Voltage 3φ", fontsize=10)
        # Since self.axes.arrow() does not have an artist we can create a label from.
        # we write a custom artist and create its label.
        # the two empty arrays are x, y position wich are given as a 2-tuple or in bbox=()
        # If given as 2-tuple remember that 0,0 is at left bottom corner of plot.
        blue_line = mlines.Line2D([], [], color='blue', markersize=3, label='φA')
        green_line = mlines.Line2D([], [], color='green', markersize=3, label='φB')
        red_line = mlines.Line2D([], [], color='red', markersize=3, label='φC')

        # loc code for wide screen  2,6,10
        # loc codes for non wide screens 5,8
        self.axes.legend(handles=[blue_line, green_line, red_line], bbox_to_anchor=(0., 1.1), loc=loc, borderaxespad=0)
        self.draw()


class DynamicPhasor1(mplCanvas):
    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        # A
        self.phase_a = self.axes.arrow(0, 0, 0, 1, alpha=0.5, width=0.015,
                                       edgecolor='blue', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True,
                                       label='Phase A')

        # B
        self.phase_b = self.axes.arrow(120 / 180. * np.pi, 0, 0, 1, alpha=0.5, width=0.015,
                                       edgecolor='green', facecolor='#17202A', lw=2, zorder=5,
                                       length_includes_head=True)
        # C
        self.phase_c = self.axes.arrow(-120 / 180. * np.pi, 0, 0, 1, alpha=0.5, width=0.015,
                                       edgecolor='red', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True)

    def update_figure(self):
        self.axes.clear()
        # Size of font that prints degrees (0 - 360 degs) around the phasor
        self.axes.set_rticks([0.2, 0.4, 0.6, 0.8, 1.0])

        self.axes.set_rmax(1.0)
        self.axes.grid(True)

        # Size of font that prints degrees (0 - 360 degs) around the phasor
        # plt.rc('xtick', labelsize=10)
        # # Determines size of font on the r values

        # EXPERIMENTAL ----------------------------------
        # self.axes.set_axis_on()
        # self.axes.autoscale(enable=False,axis='both',tight=None)
        # --------------------------------------------------------

        # THis is the txt file we are going to read the values from.
        with open(new_path + '\\readings.txt', 'r') as f:
            d = f.readlines()
        f.close()
        # Below are the definitions of arrays that will store the values of txt file
        r1 = []
        theta1 = []
        r2 = []
        theta2 = []
        r3 = []
        theta3 = []

        # TODO fix the swirly plot
        # degrees font size
        # r1 = np.arange(0, 3.0, 0.01)
        # theta1= 2*np.pi*r1

        # -------------------------------------
        # This will drive the vectors
        for i in range(len(d)):
            hold = d[i].split(',')
            r1.append(float(hold[1]))
            theta1.append(float(hold[2]))
            r2.append(float(hold[3]))
            theta2.append(float(hold[4]))
            r3.append(float(hold[5]))
            theta3.append(float(hold[6]))

        # Axes.arrow(x, y, dx, dy, **kwargs)
        # X and dy are used to control the phasor position
        self.phase_a = self.axes.arrow(x2data, 0, 0, y2data, alpha=1, width=0.015,
                                       edgecolor='blue', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True,
                                       label='A')

        # B
        self.phase_b = self.axes.arrow(xdata, 0, 0, ydata, alpha=1, width=0.015,
                                       edgecolor='green', facecolor='#17202A', lw=2, zorder=5,
                                       length_includes_head=True, label='B')
        # C
        self.phase_c = self.axes.arrow(x1data, 0, 0, y1data, alpha=1, width=0.015,
                                       edgecolor='red', lw=2, zorder=5, length_includes_head=True, label='C')

        self.axes.set_title("Power 3φ", fontsize=10)
        # Since self.axes.arrow() does not have an artist we can create a label from.
        # we write a custom artist and create its label.
        # the two empty arrays are x, y position wich are given as a 2-tuple or in bbox=()
        # If given as 2-tuple remember that 0,0 is at left bottom corner of plot.
        blue_line = mlines.Line2D([], [], color='blue', markersize=3, label='φA')
        green_line = mlines.Line2D([], [], color='green', markersize=3, label='φB')
        red_line = mlines.Line2D([], [], color='red', markersize=3, label='φC')

        # loc code for wide screen  2,6,10
        # loc codes for non wide screens 5,8
        self.axes.legend(handles=[blue_line, green_line, red_line], bbox_to_anchor=(0., 1.1), loc=loc, borderaxespad=0)
        self.draw()


''' The phasor plot below is not used but it can easily be adapted to GUI if we need it, by reducing the size of the 
    plots currently in use or creating a tabbed window '''
# class DynamicPhasor2(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         # A
#         phase_a = self.axes.arrow(0, 0, 0, 1, alpha=0.5, width=0.015,
#                                   edgecolor='blue', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True,
#                                   label='Phase A')
#
#         # B
#         phase_b = self.axes.arrow(120 / 180. * np.pi, 0, 0, 1, alpha=0.5, width=0.015,
#                                   edgecolor='green', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True)
#         # C
#         phase_c = self.axes.arrow(-120 / 180. * np.pi, 0, 0, 1, alpha=0.5, width=0.015,
#                                   edgecolor='red', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True)
#
#     def update_figure(self):
#         self.axes.clear()
#         # Size of font that prints degrees (0 - 360 degs) around the phasor
#         self.axes.set_rticks([0.2, 0.4, 0.6, 0.8, 1.0])
#
#         self.axes.set_rmax(1.0)
#         self.axes.grid(True)
#
#         # Size of font that prints degrees (0 - 360 degs) around the phasor
#         # plt.rc('xtick', labelsize=10)
#         # # Determines size of font on the r values
#
#
#         # EXPERIMENTAL ----------------------------------
#         # self.axes.set_axis_on()
#         # self.axes.autoscale(enable=False,axis='both',tight=None)
#         # --------------------------------------------------------
#
#         # THis is the txt file we are going to read the values from.
#         with open(std_path + '\\NMSU_Software_Projects\\Relays_GUI\\readings.txt', 'r') as f:
#            d = f.readlines()
#         f.close()
#         # Below are the definitions of arrays that will store the values of txt file
#         r1 = []
#         theta1 = []
#         r2 = []
#         theta2 = []
#         r3 = []
#         theta3 = []
#
#         # TODO fix the swirly plot
#         # degrees font size
#         # r1 = np.arange(0, 3.0, 0.01)
#         # theta1= 2*np.pi*r1
#
#         # -------------------------------------
#         # This will drive the vectors
#         for i in range(len(d)):
#             hold = d[i].split(',')
#             r1.append(float(hold[1]))
#             theta1.append(float(hold[2]))
#             r2.append(float(hold[3]))
#             theta2.append(float(hold[4]))
#             r3.append(float(hold[5]))
#             theta3.append(float(hold[6]))
#
#         # Axes.arrow(x, y, dx, dy, **kwargs)
#         # X and dy are used to control the phasor position
#         self.phase_a = self.axes.arrow(np.pi / 6, 0, 0, 1, alpha=1, width=0.015,
#                                        edgecolor='blue', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True,
#                                        label='A')
#
#         # B
#         self.phase_b = self.axes.arrow(120 / 180. * np.pi, 0, 0, 1, alpha=1, width=0.015,
#                                        edgecolor='green', facecolor='#17202A', lw=2, zorder=5,
#                                        length_includes_head=True, label='B')
#         # C
#         self.phase_c = self.axes.arrow(-120 / 180. * np.pi, 0, 0, 1, alpha=1, width=0.015,
#                                        edgecolor='red', lw=2, zorder=5, length_includes_head=True, label='C')
#
#
#         self.axes.set_title("Phasor ABC", fontsize=10)
#         # Since self.axes.arrow() does not have an artist we can create a label from.
#         # we write a custom artist and create its label.
#         # the two empty arrays are x, y position wich are given as a 2-tuple or in bbox=()
#         # If given as 2-tuple remember that 0,0 is at left bottom corner of plot.
#         blue_line = mlines.Line2D([], [], color='blue', markersize=3, label=r'$Phase A$')
#         green_line = mlines.Line2D([], [], color='green', markersize=3, label='Phase B')
#         red_line = mlines.Line2D([], [], color='red', markersize=3, label='Phase C')
#         # loc code for wide screen  2,6,10
#         # loc codes for non wide screens 5,8
#         self.axes.legend(handles=[blue_line, green_line, red_line], bbox_to_anchor=(0., 1.1), loc=loc, borderaxespad=0)
#
#         self.draw()

# ----------------------------------------------------------------------------------------------------------------------
