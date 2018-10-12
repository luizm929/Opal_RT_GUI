# -*- coding: utf-8 -*-
"""
@author: Luis
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QMessageBox, QWidget, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout)

import time

''' In order to write the txtLabel updater
    First, wirte  init function much like int the dynamic plots
    Second, Write a function to initialize values (starting values). 
    Third, write the labelUpdater function with QTimer as the timer to trigger each update.
'''


class Example(QtWidgets.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        init_current_a = 0.0
        init_current_b = 0.0
        init_current_c = 0.0

        init_voltage_a = 0.0
        init_voltage_b = 0.0
        init_voltage_c = 0.0

    #def setup_vars(self):
    #    for setup_v in setups_v()

        current_phase_a = QtWidgets.QLabel(str(init_current_a), self)
        current_phase_b = QtWidgets.QLabel(str(init_current_b), self)
        current_phase_c = QtWidgets.QLabel(str(init_current_c), self)

        voltage_phase_a = QtWidgets.QLabel(str(init_voltage_a), self)
        voltage_phase_b = QtWidgets.QLabel(str(init_voltage_b), self)
        voltage_phase_c = QtWidgets.QLabel(str(init_voltage_c), self)

        current_phase_a.resize(current_phase_a.sizeHint())
        current_phase_b.resize(current_phase_b.sizeHint())
        current_phase_c.resize(current_phase_c.sizeHint())

        voltage_phase_a.resize(voltage_phase_a.sizeHint())
        voltage_phase_b.resize(voltage_phase_b.sizeHint())
        voltage_phase_c.resize(voltage_phase_c.sizeHint())

        current_phase_a.move(150, 90)
        current_phase_b.move(150, 80)
        current_phase_c.move(150, 70)

        voltage_phase_a.move(160, 90)
        voltage_phase_b.move(160, 80)
        voltage_phase_c.move(160, 70)

        # after  seconds (1000 milliseconds), call self.updateLabel
        QtCore.QTimer.singleShot(1000, lambda: self.updateLabel(current_phase_a, current_phase_b, current_phase_c,
                                                                voltage_phase_a, voltage_phase_b, voltage_phase_c))

        grid = QtWidgets.QGridLayout()
        grid.addWidget(current_phase_a, 0, 2)
        grid.addWidget(current_phase_b, 0, 3)
        grid.addWidget(current_phase_c, 0, 4)

        grid.addWidget(voltage_phase_a, 1, 2)
        grid.addWidget(voltage_phase_b, 1, 3)
        grid.addWidget(voltage_phase_c, 1, 4)

        self.setLayout(grid)

        self.setGeometry(300, 200, 600, 400)
        self.setWindowTitle("battery status")
        self.show()

    def updateLabel(self, current_phase_a, current_phase_b, current_phase_c, voltage_phase_a, voltage_phase_b,
                    voltage_phase_c):
           # change the following line to retrieve the new voltage from
           #the device
        newcurrent_phase_a = float(current_phase_a.text()) + 1
        newcurrent_phase_b = float(current_phase_b.text()) + 1
        newcurrent_phase_c = float(current_phase_c.text()) + 1

        newvoltage_phase_a = float(voltage_phase_a.text()) + 1
        newvoltage_phase_b = float(voltage_phase_b.text()) + 1
        newvoltage_phase_c = float(voltage_phase_c.text()) + 1

        current_phase_a.setText(str(newcurrent_phase_a))
        current_phase_b.setText(str(newcurrent_phase_b))
        current_phase_c.setText(str(newcurrent_phase_c))

        voltage_phase_a.setText(str(newvoltage_phase_a))
        voltage_phase_b.setText(str(newvoltage_phase_b))
        voltage_phase_c.setText(str(newvoltage_phase_c))

        QtCore.QTimer.singleShot(1000, lambda: self.updateLabel(current_phase_a, current_phase_b, current_phase_c,
                                                                voltage_phase_a, voltage_phase_b, voltage_phase_c))







def main():

    app=QtWidgets.QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
