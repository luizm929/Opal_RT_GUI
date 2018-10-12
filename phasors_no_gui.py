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

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.style as style
style.use('bmh')

# Prints the versions of matplotlib and backend
# print ("matplotlib.__version__   = ", matplotlib.__version__)
# print ("matplotlib.get_backend() = ", matplotlib.get_backend())

# linewidth controls the width of the lines that make up the polar grid.
plt.rc('grid', color='#17202A', linewidth=0.2, linestyle='-')

# Size of font that prints degrees (0 - 360 degs) around the phasor
plt.rc('xtick', labelsize=8)

# Determines size of font on the r values
plt.rc('ytick', labelsize=6)


# force square figure and square axes look better for polar, IMO
width, height = matplotlib.rcParams['figure.figsize']
size = min(width, height)
# make a square figure
fig = plt.figure(figsize=(size, size))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True, facecolor='#E5E7E9')

r = np.arange(0, 3.0, 0.01)
theta = 2*np.pi*r

# if this is uncommented, a swirl will appear on the phasor diagram
#ax.plot(theta, r, color='red', lw=3)
ax.set_rmax(2.0)
plt.grid(True)

# Title of the plot
ax.set_title("3φ", fontsize=12)

#TODO Create functions of the arrows below such that they become dynamic arrows to portray the values of the Phasors.
# Usage of the arrow method
# Axes.arrow(x, y, dx, dy, **kwargs)

# A

phase_a = plt.arrow(0, 0, 0 , 1.9, alpha = 1, width = 0.015,
                 edgecolor = 'blue', facecolor = '#17202A', lw = 2, zorder = 5)

phase_a.remove()
# B
phase_b = plt.arrow(120/180.*np.pi, 0, 0, 1.9, alpha = 1, width = 0.015,
                 edgecolor = 'green', facecolor = '#17202A', lw = 2, zorder = 5)
# C
phase_c = plt.arrow(-120/180.*np.pi, 0, 0, 1.9, alpha = 1, width = 0.015,
                 edgecolor = 'red', facecolor = '#17202A', lw = 2, zorder = 5)
plt.show()