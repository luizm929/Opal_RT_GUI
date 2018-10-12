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
# Files needed for this program to run
#
#------------------------------------------------------------

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib
from PyQt5.QtCore import QTimer, QSize
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
# Style ideal for engineering
import matplotlib.style as style
#style.use(['bmh' , 'dark_background'])
# Good styles
#style.use('seaborn-paper')  # clean clear colors
#style.use('seaborn-pastel')
style.use('bmh')

from PyQt5.QtWidgets import QSizePolicy
import time
import os
import errno
# When running on console change path to where the file lives (drive E:\). -----------------------------------
#TODO Fix the path problem (when we change HD program complains it cannot find files).
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
#print ("matplotlib.__version__   = ", matplotlib.__version__)
#print ("matplotlib.get_backend() = ", matplotlib.get_backend())
import matplotlib.lines as mlines
#def legends(self):


class mplCanvas(FigureCanvas):
    # Any setting you want to modify with the GUI will first have to me modified here
    # this is the class that redraws(updates) the plots.
   
    def __init__(self, parent=None, width =matplotlib.rcParams['figure.figsize'],
                 height = matplotlib.rcParams['figure.figsize'], dpi=100):
        size = min(width, height)
        
        fig = Figure(size, dpi=dpi)
        
        self.axes = fig.add_subplot(111, polar=True)

        #----------------------------------------------------------------------
        # If we wanted to modify the font size through the GUI we would create a call in the gui
        # and it would point here.
        # Size of font that prints degrees (0 - 360 degs) around the phasor
        plt.rc('xtick', labelsize=10)
        # # Determines size of font on the r values
        plt.rc('ytick', labelsize=9)
        #-----------------------------------------------------------------------

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
        return QSize(300, 400)

    def compute_initial_figure(self):
        pass

    def update_figure(self):
        pass

#Package format:
#---| Time(s) | |Ia| | Ia angle | |Ib| | Ib angle | |Ic|  | Ic angle |  ---

class dynPlot1(mplCanvas):
    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        # A
        self.axes.arrow(0, 0, 0, 1, alpha = 0.5, width = 0.015,
                         edgecolor = 'blue', facecolor = '#17202A', lw = 2, zorder = 5,length_includes_head=True)

        # B
        self.axes.arrow(120/180.*np.pi, 0, 0, 1, alpha = 0.5, width = 0.015,
                         edgecolor = 'green', facecolor = '#17202A', lw = 2, zorder = 5,length_includes_head=True)
        # C
        self.axes.arrow(-120/180.*np.pi, 0, 0, 1, alpha = 0.5, width = 0.015,
                         edgecolor = 'red', facecolor = '#17202A', lw = 2, zorder = 5,length_includes_head=True)

    def update_figure(self):
        self.axes.clear()
        self.axes.set_rticks([0.2, 0.4, 0.6, 0.8, 1.0])

        self.axes.set_rmax(1.0)
        self.axes.grid(True)

        # EXPERIMENTAL ----------------------------------
        #self.axes.set_axis_on()
        #self.axes.autoscale(enable=False,axis='both',tight=None)
        #--------------------------------------------------------

        # THis is the txt file we are going to read the values from.
        f = open(std_path + '\\NMSU_Software_Projects\\Relays_GUI\\readings.txt', 'r')
        d = f.readlines()
        f.close()
        # Below are the definitions of arrays that will store the values of txt file
        r1 = []
        theta1 = []
        r2 = []
        theta2 = []
        r3 = []
        theta3 = []

        #TODO fix the swirly plot
        # degrees font size
        #r1 = np.arange(0, 3.0, 0.01)
        #theta1= 2*np.pi*r1

        #-------------------------------------
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


        self.phasor_a = self.axes.arrow(np.pi/6, 0, 0, 1, alpha = 1, width = 0.015,
                 color = 'blue', facecolor = '#17202A', lw = 2, zorder = 5,length_includes_head=True, label=r'$Pha$')

        # B
        self.phasor_b = self.axes.arrow(120/180.*np.pi, 0, 0, 1, alpha = 1, width = 0.015,
                 edgecolor = 'green', facecolor = '#17202A', lw = 2, zorder = 5, length_includes_head=True, label='B')
        # C
        self.phasor_c = self.axes.arrow(-120/180.*np.pi, 0, 0, 1, alpha = 1, width = 0.015,
                 edgecolor = 'red', facecolor = '#17202A',lw = 2, zorder = 5, length_includes_head=True, label='C')



        self.axes.set_title("Phasor ABC", fontsize=10)
        blue_line = mlines.Line2D([], [], color='blue', markersize=3, label='Phase A')
        green_line = mlines.Line2D([], [], color='green', markersize=3, label='Phase B')
        red_line = mlines.Line2D([], [], color='red', markersize=3, label='Phase C')

        # loc code for wide screen  2,6,10
        # loc codes for non wide screens 5,8
        self.axes.legend(handles=[blue_line,green_line,red_line],bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
        self.draw()




class dynPlot2(mplCanvas):
    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        # A
        phase_a = self.axes.arrow(0, 0, 0, 1, alpha=0.5, width=0.015,
                                  edgecolor='blue', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True,
                                  label='Phase A')

        # B
        phase_b = self.axes.arrow(120 / 180. * np.pi, 0, 0, 1, alpha=0.5, width=0.015,
                                  edgecolor='green', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True)
        # C
        phase_c = self.axes.arrow(-120 / 180. * np.pi, 0, 0, 1, alpha=0.5, width=0.015,
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
        f = open(std_path + '\\NMSU_Software_Projects\\Relays_GUI\\readings.txt', 'r')
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
        self.phase_a = self.axes.arrow(np.pi / 6, 0, 0, 1, alpha=1, width=0.015,
                                       edgecolor='blue', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True,
                                       label='A')

        # B
        self.phase_b = self.axes.arrow(120 / 180. * np.pi, 0, 0, 1, alpha=1, width=0.015,
                                       edgecolor='green', facecolor='#17202A', lw=2, zorder=5,
                                       length_includes_head=True, label='B')
        # C
        self.phase_c = self.axes.arrow(-120 / 180. * np.pi, 0, 0, 1, alpha=1, width=0.015,
                                       edgecolor='red', lw=2, zorder=5, length_includes_head=True, label='C')

        self.axes.set_title("Phasor ABC", fontsize=10)
        blue_line = mlines.Line2D([], [], color='blue', markersize=3, label='Phase A')
        green_line = mlines.Line2D([], [], color='green', markersize=3, label='Phase B')
        red_line = mlines.Line2D([], [], color='red', markersize=3, label='Phase C')

        # loc code for wide screen  2,6,10
        # loc codes for non wide screens 5,8
        self.axes.legend(handles=[blue_line, green_line, red_line], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
        self.draw()


class dynPlot3(mplCanvas):
    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        # A
        phase_a = self.axes.arrow(0, 0, 0, 1, alpha=0.5, width=0.015,
                                  edgecolor='blue', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True,
                                  label='Phase A')

        # B
        phase_b = self.axes.arrow(120 / 180. * np.pi, 0, 0, 1, alpha=0.5, width=0.015,
                                  edgecolor='green', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True)
        # C
        phase_c = self.axes.arrow(-120 / 180. * np.pi, 0, 0, 1, alpha=0.5, width=0.015,
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
        f = open(std_path + '\\NMSU_Software_Projects\\Relays_GUI\\readings.txt', 'r')
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
        self.phase_a = self.axes.arrow(np.pi / 6, 0, 0, 1, alpha=1, width=0.015,
                                       edgecolor='blue', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True,
                                       label='A')

        # B
        self.phase_b = self.axes.arrow(120 / 180. * np.pi, 0, 0, 1, alpha=1, width=0.015,
                                       edgecolor='green', facecolor='#17202A', lw=2, zorder=5,
                                       length_includes_head=True, label='B')
        # C
        self.phase_c = self.axes.arrow(-120 / 180. * np.pi, 0, 0, 1, alpha=1, width=0.015,
                                       edgecolor='red', lw=2, zorder=5, length_includes_head=True, label='C')

        self.axes.set_title("Phasor ABC", fontsize=10)
        blue_line = mlines.Line2D([], [], color='blue', markersize=3, label='Phase A')
        green_line = mlines.Line2D([], [], color='green', markersize=3, label='Phase B')
        red_line = mlines.Line2D([], [], color='red', markersize=3, label='Phase C')

        # loc code for wide screen  2,6,10
        # loc codes for non wide screens 5,8
        self.axes.legend(handles=[blue_line, green_line, red_line], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
        self.draw()


class dynPlot4(mplCanvas):
    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        # A
        phase_a = self.axes.arrow(0, 0, 0, 1, alpha=0.5, width=0.015,
                                  edgecolor='blue', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True,
                                  label='Phase A')

        # B
        phase_b = self.axes.arrow(120 / 180. * np.pi, 0, 0, 1, alpha=0.5, width=0.015,
                                  edgecolor='green', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True)
        # C
        phase_c = self.axes.arrow(-120 / 180. * np.pi, 0, 0, 1, alpha=0.5, width=0.015,
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
        f = open(std_path + '\\NMSU_Software_Projects\\Relays_GUI\\readings.txt', 'r')
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
        self.phase_a = self.axes.arrow(np.pi / 6, 0, 0, 1, alpha=1, width=0.015,
                                       edgecolor='blue', facecolor='#17202A', lw=2, zorder=5, length_includes_head=True,
                                       label='A')

        # B
        self.phase_b = self.axes.arrow(120 / 180. * np.pi, 0, 0, 1, alpha=1, width=0.015,
                                       edgecolor='green', facecolor='#17202A', lw=2, zorder=5,
                                       length_includes_head=True, label='B')
        # C
        self.phase_c = self.axes.arrow(-120 / 180. * np.pi, 0, 0, 1, alpha=1, width=0.015,
                                       edgecolor='red', lw=2, zorder=5, length_includes_head=True, label='C')

        self.axes.set_title("Phasor ABC", fontsize=10)
        blue_line = mlines.Line2D([], [], color='blue', markersize=3, label='Phase A')
        green_line = mlines.Line2D([], [], color='green', markersize=3, label='Phase B')
        red_line = mlines.Line2D([], [], color='red', markersize=3, label='Phase C')

        # loc code for wide screen  2,6,10
        # loc codes for non wide screens 5,8
        self.axes.legend(handles=[blue_line, green_line, red_line], bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)

        self.draw()

#--------------------------------------------------------------------
# The next plotting classes are not used, this is just room to grow
#--------------------------------------------------------------------
# class dynPlot5(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
#
#     def update_figure(self):
#         self.axes.clear()
#         f = open('E:\SWTDI_GUI\outlet4.txt', 'r')
#         d = f.readlines()
#         f.close()
#         x = []
#         y = []
#         for i in range(len(d)):
#             hold = d[i].split(',')
#
#             x.append(float(hold[0]))
#             y.append(float(hold[1]))
#
#         self.axes.plot(x, y, 'r', label='Temperature (F)')
#         self.axes.set_xlabel('Time (s)')
#         self.axes.set_ylabel('Temperature (F)')
#         self.axes.legend(loc='upper left')
#         self.draw()
#
#
# class dynPlot6(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
#
#     def update_figure(self):
#         self.axes.clear()
#         f = open(new_path + 'outletPlotDataH1R1O1.txt', 'r')
#         d = f.readlines()
#         f.close()
#         x = []
#         y = []
#         for i in range(len(d)):
#             hold = d[i].split(',')
#
#             x.append(float(hold[0]))
#             y.append(float(hold[1]))
#
#         self.axes.plot(x, y, 'r', label='Temperature (F)')
#         self.axes.set_xlabel('Time (s)')
#         self.axes.set_ylabel('Temperature (F)')
#         self.axes.legend(loc='upper left')
#         self.draw()
#
# class dynPlot7(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
#
#     def update_figure(self):
#         self.axes.clear()
#         f = open(new_path + 'outletPlotDataH1R1O1.txt', 'r')
#         d = f.readlines()
#         f.close()
#         x = []
#         y = []
#         for i in range(len(d)):
#             hold = d[i].split(',')
#
#             x.append(float(hold[0]))
#             y.append(float(hold[1]))
#
#         self.axes.plot(x, y, 'r', label='Temperature (F)')
#         self.axes.set_xlabel('Time (s)')
#         self.axes.set_ylabel('Temperature (F)')
#         self.axes.legend(loc='upper left')
#         self.draw()
#
# class dynPlot8(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
#
#     def update_figure(self):
#         self.axes.clear()
#         f = open(new_path + 'outletPlotDataH1R1O1.txt', 'r')
#         d = f.readlines()
#         f.close()
#         x = []
#         y = []
#         for i in range(len(d)):
#             hold = d[i].split(',')
#
#             x.append(float(hold[0]))
#             y.append(float(hold[1]))
#
#         self.axes.plot(x, y, 'r', label='Temperature (F)')
#         self.axes.set_xlabel('Time (s)')
#         self.axes.set_ylabel('Temperature (F)')
#         self.axes.legend(loc='upper left')
#         self.draw()
#
# class dynPlot9(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
#
#     def update_figure(self):
#         self.axes.clear()
#         f = open(new_path + 'outletPlotDataH1R1O1.txt', 'r')
#         d = f.readlines()
#         f.close()
#         x = []
#         y = []
#         for i in range(len(d)):
#             hold = d[i].split(',')
#
#             x.append(float(hold[0]))
#             y.append(float(hold[1]))
#
#         self.axes.plot(x, y, 'r', label='Temperature (F)')
#         self.axes.set_xlabel('Time (s)')
#         self.axes.set_ylabel('Temperature (F)')
#         self.axes.legend(loc='upper left')
#         self.draw()
#
# class dynPlot10(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
#
#     def update_figure(self):
#         self.axes.clear()
#         f = open(new_path + 'outletPlotDataH1R1O1.txt', 'r')
#         d = f.readlines()
#         f.close()
#         x = []
#         y = []
#         for i in range(len(d)):
#             hold = d[i].split(',')
#
#             x.append(float(hold[0]))
#             y.append(float(hold[1]))
#
#         self.axes.plot(x, y, 'r', label='Temperature (F)')
#         self.axes.set_xlabel('Time (s)')
#         self.axes.set_ylabel('Temperature (F)')
#         self.axes.legend(loc='upper left')
#         self.draw()
#
# class dynPlot11(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
#
#     def update_figure(self):
#         self.axes.clear()
#         f = open(new_path + 'outletPlotDataH1R1O1.txt', 'r')
#         d = f.readlines()
#         f.close()
#         x = []
#         y = []
#         for i in range(len(d)):
#             hold = d[i].split(',')
#
#             x.append(float(hold[0]))
#             y.append(float(hold[1]))
#
#         self.axes.plot(x, y, 'r', label='Temperature (F)')
#         self.axes.set_xlabel('Time (s)')
#         self.axes.set_ylabel('Temperature (F)')
#         self.axes.legend(loc='upper left')
#         self.draw()
#
# class dynPlot12(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
#
#     def update_figure(self):
#         self.axes.clear()
#         f = open(new_path + 'outletPlotDataH1R1O1.txt', 'r')
#         d = f.readlines()
#         f.close()
#         x = []
#         y = []
#         for i in range(len(d)):
#             hold = d[i].split(',')
#
#             x.append(float(hold[0]))
#             y.append(float(hold[1]))
#
#         self.axes.plot(x, y, 'r', label='Temperature (F)')
#         self.axes.set_xlabel('Time (s)')
#         self.axes.set_ylabel('Temperature (F)')
#         self.axes.legend(loc='upper left')
#         self.draw()

