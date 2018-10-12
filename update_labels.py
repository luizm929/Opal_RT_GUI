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
import random
''' In order to write the txtLabel updater
    First, wirte  init function much like int the dynamic plots
    Second, Write a function to initialize values (starting values). 
    Third, write the labelUpdater function with QTimer as the timer to trigger each update.
'''


class LabelsProgram(QtWidgets.QWidget):

    def __init__(self):
        super(LabelsProgram, self).__init__()

        self.initial_values()

    def initial_values(self):
        init_mag_Ia = 0.0
        init_mag_Ib = 0.0
        init_mag_Ic = 0.0

        init_deg_Ia = 0.0
        init_deg_Ib = 0.0
        init_deg_Ic = 0.0

        init_mag_Va = 0.0
        init_mag_Vb = 0.0
        init_mag_Vc = 0.0

        init_deg_Va = 0.0
        init_deg_Vb = 0.0
        init_deg_Vc = 0.0

        init_mag_Pa = 0.0
        init_mag_Pb = 0.0
        init_mag_Pc = 0.0

        init_deg_Pa = 0.0
        init_deg_Pb = 0.0
        init_deg_Pc = 0.0

    #def setup_vars(self):
    #    for setup_v in setups_v()
        #----------- Current----------------------
        mag_Ia = QtWidgets.QLabel(str(init_mag_Ia), self)
        mag_Ib = QtWidgets.QLabel(str(init_mag_Ib), self)
        mag_Ic = QtWidgets.QLabel(str(init_mag_Ic), self)

        deg_Ia = QtWidgets.QLabel(str(init_deg_Ia), self)
        deg_Ib = QtWidgets.QLabel(str(init_deg_Ib), self)
        deg_Ic = QtWidgets.QLabel(str(init_deg_Ic), self)

        # -----------------Voltage--------------------
        mag_Va = QtWidgets.QLabel(str(init_mag_Va), self)
        mag_Vb = QtWidgets.QLabel(str(init_mag_Vb), self)
        mag_Vc = QtWidgets.QLabel(str(init_mag_Vc), self)

        deg_Va = QtWidgets.QLabel(str(init_deg_Va), self)
        deg_Vb = QtWidgets.QLabel(str(init_deg_Vb), self)
        deg_Vc = QtWidgets.QLabel(str(init_deg_Vc), self)

        #-----------------Power -------------------------
        mag_Pa = QtWidgets.QLabel(str(init_mag_Pa), self)
        mag_Pb = QtWidgets.QLabel(str(init_mag_Pb), self)
        mag_Pc = QtWidgets.QLabel(str(init_mag_Pc), self)

        deg_Pa = QtWidgets.QLabel(str(init_deg_Pa), self)
        deg_Pb = QtWidgets.QLabel(str(init_deg_Pb), self)
        deg_Pc = QtWidgets.QLabel(str(init_deg_Pc), self)


        # -------------current-------------------
        mag_Ia.resize(mag_Ia.sizeHint())
        mag_Ib.resize(mag_Ib.sizeHint())
        mag_Ic.resize(mag_Ic.sizeHint())

        deg_Ia.resize(deg_Ia.sizeHint())
        deg_Ib.resize(deg_Ib.sizeHint())
        deg_Ic.resize(deg_Ic.sizeHint())

        #----------Voltage------------------
        mag_Va.resize(mag_Va.sizeHint())
        mag_Vb.resize(mag_Vb.sizeHint())
        mag_Vc.resize(mag_Vc.sizeHint())

        deg_Va.resize(deg_Va.sizeHint())
        deg_Vb.resize(deg_Vb.sizeHint())
        deg_Vc.resize(deg_Vc.sizeHint())

        #------------------Power-----------------
        mag_Pa.resize(mag_Pa.sizeHint())
        mag_Pb.resize(mag_Pb.sizeHint())
        mag_Pc.resize(mag_Pc.sizeHint())

        deg_Pa.resize(deg_Pa.sizeHint())
        deg_Pb.resize(deg_Pb.sizeHint())
        deg_Pc.resize(deg_Pc.sizeHint())


        #--------------Current-------
        mag_Ia.move(150, 90)
        mag_Ib.move(150, 80)
        mag_Ic.move(150, 70)

        deg_Ia.move(160, 90)
        deg_Ib.move(160, 80)
        deg_Ic.move(160, 70)

        #---------------Voltage---------
        mag_Va.move(170, 90)
        mag_Vb.move(170, 80)
        mag_Vc.move(170, 70)

        deg_Va.move(180, 90)
        deg_Vb.move(180, 80)
        deg_Vc.move(180, 70)

        #---------Power------------
        mag_Pa.move(190, 90)
        mag_Pb.move(190, 80)
        mag_Pc.move(190, 70)

        deg_Pa.move(190, 90)
        deg_Pb.move(190, 80)
        deg_Pc.move(190, 70)

        # after 5 seconds (1000 milliseconds), call self.updateLabel
        QtCore.QTimer.singleShot(1000, lambda: self.updateLabel(mag_Ia, mag_Ib, mag_Ic, deg_Ia, deg_Ib, deg_Ic,
                                                                mag_Va, mag_Vb, mag_Vc, deg_Va, deg_Vb, deg_Vc,
                                                                mag_Pa, mag_Pb, mag_Pc, deg_Pa, deg_Pb, deg_Pc))

        grid = QtWidgets.QGridLayout()
        #--------Current----------
        grid.addWidget(mag_Ia, 0, 2)
        grid.addWidget(mag_Ib, 0, 3)
        grid.addWidget(mag_Ic, 0, 4)

        grid.addWidget(deg_Ia, 1, 2)
        grid.addWidget(deg_Ib, 1, 3)
        grid.addWidget(deg_Ic, 1, 4)

        #----------Voltage ------------------
        grid.addWidget(mag_Va, 3, 2)
        grid.addWidget(mag_Vb, 3, 3)
        grid.addWidget(mag_Vc, 3, 4)

        grid.addWidget(deg_Va, 4, 2)
        grid.addWidget(deg_Vb, 4, 3)
        grid.addWidget(deg_Vc, 4, 4)

        #----------------Power -------------

        grid.addWidget(mag_Pa, 5, 2)
        grid.addWidget(mag_Pb, 5, 3)
        grid.addWidget(mag_Pc, 5, 4)

        grid.addWidget(deg_Pa, 6, 2)
        grid.addWidget(deg_Pb, 6, 3)
        grid.addWidget(deg_Pc, 6, 4)

        self.setLayout(grid)

        self.setGeometry(400, 300, 600, 400)
        self.setWindowTitle("battery status")
        self.show()

    def updateLabel(self, current_mag_Ia, current_mag_Ib, current_mag_Ic, current_deg_Ia, current_deg_Ib, current_deg_Ic,
                    current_mag_Va,current_mag_Vb, current_mag_Vc, current_deg_Va, current_deg_Vb, current_deg_Vc,
                    current_mag_Pa, current_mag_Pb, current_mag_Pc, current_deg_Pa, current_deg_Pb, current_deg_Pc):
           # change the following line to retrieve the new voltage from
           #the device
        mag_Ia = mag_Ib = mag_Ic =  random.gauss(20.0, 2.0)


        deg_Ia = random.gauss(0.0, 2.0)
        deg_Ib = random.gauss(-180.0, 2.0)
        deg_Ic = random.gauss(180, 2.0)


        new_mag_Ia = float('%.2f' % mag_Ia)
        new_mag_Ib = float('%.2f' % mag_Ib)
        new_mag_Ic = float('%.2f' % mag_Ic)

        new_deg_Ia = float('%.2f' % deg_Ia)
        new_deg_Ib = float('%.2f' % deg_Ib)
        new_deg_Ic = float('%.2f' % deg_Ic)

        current_mag_Ia.setText(str(new_mag_Ia))
        current_mag_Ib.setText(str(new_mag_Ib))
        current_mag_Ic.setText(str(new_mag_Ic))

        current_deg_Ia.setText(str(new_deg_Ia))
        current_deg_Ib.setText(str(new_deg_Ib))
        current_deg_Ic.setText(str(new_deg_Ic))

        #----------------Voltage--------------------
        mag_Va = mag_Vb = mag_Vc = random.gauss(120.0, 2.0)

        deg_Va = random.gauss(0.0, 2.0)
        deg_Vb = random.gauss(-180.0, 2.0)
        deg_Vc = random.gauss(180, 2.0)

        new_mag_Va = float('%.2f' % mag_Va)
        new_mag_Vb = float('%.2f' % mag_Vb)
        new_mag_Vc = float('%.2f' % mag_Vc)

        new_deg_Va = float('%.2f' % deg_Va)
        new_deg_Vb = float('%.2f' % deg_Vb)
        new_deg_Vc = float('%.2f' % deg_Vc)

        current_mag_Va.setText(str(new_mag_Va))
        current_mag_Vb.setText(str(new_mag_Vb))
        current_mag_Vc.setText(str(new_mag_Vc))

        current_deg_Va.setText(str(new_deg_Va))
        current_deg_Vb.setText(str(new_deg_Vb))
        current_deg_Vc.setText(str(new_deg_Vc))

        #-----------------Power -----------------------
        mag_Pa = mag_Pb = mag_Pc = random.gauss(1200.0, 2.0)

        deg_Pa = random.gauss(0.0, 2.0)
        deg_Pb = random.gauss(-180.0, 2.0)
        deg_Pc = random.gauss(180, 2.0)

        new_mag_Pa = float('%.2f' % mag_Pa)
        new_mag_Pb = float('%.2f' % mag_Pb)
        new_mag_Pc = float('%.2f' % mag_Pc)

        new_deg_Pa = float('%.2f' % deg_Pa)
        new_deg_Pb = float('%.2f' % deg_Pb)
        new_deg_Pc = float('%.2f' % deg_Pc)

        current_mag_Pa.setText(str(new_mag_Pa))
        current_mag_Pb.setText(str(new_mag_Pb))
        current_mag_Pc.setText(str(new_mag_Pc))

        current_deg_Pa.setText(str(new_deg_Pa))
        current_deg_Pb.setText(str(new_deg_Pb))
        current_deg_Pc.setText(str(new_deg_Pc))

        QtCore.QTimer.singleShot(1000, lambda: self.updateLabel(current_mag_Ia, current_mag_Ib, current_mag_Ic,
                                                                current_deg_Ia, current_deg_Ib, current_deg_Ic,
                                                                current_mag_Va, current_mag_Vb, current_mag_Vc,
                                                                current_deg_Va, current_deg_Vb, current_deg_Vc,
                                                                current_mag_Pa, current_mag_Pb, current_mag_Pc,
                                                                current_deg_Pa, current_deg_Pb, current_deg_Pc))

def main():

    app=QtWidgets.QApplication(sys.argv)
    ex=LabelsProgram()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
