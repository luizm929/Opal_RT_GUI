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

from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_RelayGUI(object):
    def __init__(self):
        super(Ui_RelayGUI, self).__init__()

    #---------------------------------------------------------------------------
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1678, 805)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 1571, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.current_Frame = QtWidgets.QFrame(self.layoutWidget)
        self.current_Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.current_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.current_Frame.setObjectName("current_Frame")
        self.layoutWidget1 = QtWidgets.QWidget(self.current_Frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(140, 20, 211, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.curr_table_layout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.curr_table_layout.setContentsMargins(0, 0, 0, 0)
        self.curr_table_layout.setObjectName("curr_table_layout")
        self.Currents_per_phase_table_title = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Currents_per_phase_table_title.setFont(font)
        self.Currents_per_phase_table_title.setObjectName("Currents_per_phase_table_title")
        self.curr_table_layout.addWidget(self.Currents_per_phase_table_title)
        self.line = QtWidgets.QFrame(self.layoutWidget1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.curr_table_layout.addWidget(self.line)
        self.Ia_horiz_layout = QtWidgets.QHBoxLayout()
        self.Ia_horiz_layout.setObjectName("Ia_horiz_layout")
        # Ia defined and static
        self.Ia = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Ia.setFont(font)
        self.Ia.setObjectName("Ia")
        self.Ia_horiz_layout.addWidget(self.Ia)




        #-----------------------------Part 1 to update QLabels----------------------------------------
        # Initial values for all QLabels
        init_mag_Ia = 0.0
        init_mag_Ib = 0.0
        init_mag_Ic = 0.0

        init_ang_Ia = 0.0
        init_ang_Ib = 0.0
        init_ang_Ic = 0.0

        init_mag_Va = 0.0
        init_mag_Vb = 0.0
        init_mag_Vc = 0.0

        init_ang_Va = 0.0
        init_ang_Vb = 0.0
        init_ang_Vc = 0.0

        init_mag_Pa = 0.0
        init_mag_Pb = 0.0
        init_mag_Pc = 0.0

        init_ang_Pa = 0.0
        init_ang_Pb = 0.0
        init_ang_Pc = 0.0


        #--------------------------Dynamic QLabel------------------------------
        self.mag_Ia = QtWidgets.QLabel(str(init_mag_Ia), self.layoutWidget1)
        #QtCore.QTimer.singleShot(1000, lambda: LabelsProgram.updateLabel(self, current_mag_Ia='0.0'))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.mag_Ia.setFont(font)
        self.mag_Ia.setObjectName("mag_Ia")
        self.Ia_horiz_layout.addWidget(self.mag_Ia)
        #---------------------------------------------------------------------
        # angle_symbol defined and static
        self.angle_symbol_a = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.angle_symbol_a.setFont(font)
        self.angle_symbol_a.setObjectName("angle_symbol_a")
        self.Ia_horiz_layout.addWidget(self.angle_symbol_a)

        #----------deg_Ia dynamic---------------------
        self.deg_Ia = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.deg_Ia.setFont(font)
        self.deg_Ia.setObjectName("deg_Ia")
        self.Ia_horiz_layout.addWidget(self.deg_Ia)

        #---------- deg_symbol_Ia static---------------------
        self.deg_symbol_Ia = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.deg_symbol_Ia.setFont(font)
        self.deg_symbol_Ia.setObjectName("deg_symbol_Ia")
        self.Ia_horiz_layout.addWidget(self.deg_symbol_Ia)
        self.curr_table_layout.addLayout(self.Ia_horiz_layout)
        self.Ib_horiz_layout = QtWidgets.QHBoxLayout()
        self.Ib_horiz_layout.setObjectName("Ib_horiz_layout")
        # --------------------------Static QLabel------------------------------
        self.Ib = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Ib.setFont(font)
        self.Ib.setObjectName("Ib")
        self.Ib_horiz_layout.addWidget(self.Ib)

        # --------------------------Dynamic QLabel------------------------------
        self.mag_Ib = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.mag_Ib.setFont(font)
        self.mag_Ib.setObjectName("mag_Ib")
        #-------------------------------------------------------------------------

        self.Ib_horiz_layout.addWidget(self.mag_Ib)
        self.angle_symbol_b = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.angle_symbol_b.setFont(font)
        self.angle_symbol_b.setObjectName("angle_symbol_b")
        self.Ib_horiz_layout.addWidget(self.angle_symbol_b)

        # --------------------------Dynamic QLabel------------------------------
        self.deg_Ib = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.deg_Ib.setFont(font)
        self.deg_Ib.setObjectName("deg_Ib")
        #-------------------------------------------------------------------------

        self.Ib_horiz_layout.addWidget(self.deg_Ib)
        self.deg_symbol_Ib = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.deg_symbol_Ib.setFont(font)
        self.deg_symbol_Ib.setObjectName("deg_symbol_Ib")
        self.Ib_horiz_layout.addWidget(self.deg_symbol_Ib)
        self.curr_table_layout.addLayout(self.Ib_horiz_layout)
        self.Ic_horiz_layout = QtWidgets.QHBoxLayout()
        self.Ic_horiz_layout.setObjectName("Ic_horiz_layout")
        self.Ic = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Ic.setFont(font)
        self.Ic.setObjectName("Ic")
        self.Ic_horiz_layout.addWidget(self.Ic)
        # --------------------------Dynamic QLabel------------------------------
        self.mag_Ic = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.mag_Ic.setFont(font)
        self.mag_Ic.setObjectName("mag_Ic")
        #-----------------------------------------------------------------------

        self.Ic_horiz_layout.addWidget(self.mag_Ic)
        self.angle_symbol_c = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.angle_symbol_c.setFont(font)
        self.angle_symbol_c.setObjectName("angle_symbol_c")
        self.Ic_horiz_layout.addWidget(self.angle_symbol_c)
        # --------------------------Dynamic QLabel------------------------------
        self.deg_Ic = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.deg_Ic.setFont(font)
        self.deg_Ic.setObjectName("deg_Ic")
        #------------------------------------------------------------------------

        self.Ic_horiz_layout.addWidget(self.deg_Ic)
        self.deg_symbol_Ic = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.deg_symbol_Ic.setFont(font)
        self.deg_symbol_Ic.setObjectName("deg_symbol_Ic")
        self.Ic_horiz_layout.addWidget(self.deg_symbol_Ic)
        self.curr_table_layout.addLayout(self.Ic_horiz_layout)
        self.horizontalLayout.addWidget(self.current_Frame)
        self.voltage_Frame = QtWidgets.QFrame(self.layoutWidget)
        self.voltage_Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.voltage_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.voltage_Frame.setObjectName("voltage_Frame")
        self.layoutWidget2 = QtWidgets.QWidget(self.voltage_Frame)
        self.layoutWidget2.setGeometry(QtCore.QRect(140, 20, 241, 151))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.volt_table_layout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.volt_table_layout.setContentsMargins(0, 0, 0, 0)
        self.volt_table_layout.setObjectName("volt_table_layout")
        self.voltages_per_phase_table_title = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.voltages_per_phase_table_title.setFont(font)
        self.voltages_per_phase_table_title.setObjectName("voltages_per_phase_table_title")
        self.volt_table_layout.addWidget(self.voltages_per_phase_table_title)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.volt_table_layout.addWidget(self.line_2)
        self.va_horiz_layout = QtWidgets.QHBoxLayout()
        self.va_horiz_layout.setObjectName("va_horiz_layout")
        self.Va = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Va.setFont(font)
        self.Va.setObjectName("Va")
        self.va_horiz_layout.addWidget(self.Va)
        # --------------------------Dynamic QLabel------------------------------
        self.mag_Va = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.mag_Va.setFont(font)
        self.mag_Va.setObjectName("mag_Va")
        #-----------------------------------------------------------------------

        self.va_horiz_layout.addWidget(self.mag_Va)
        self.angle_sym_Va = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.angle_sym_Va.setFont(font)
        self.angle_sym_Va.setObjectName("angle_sym_Va")
        self.va_horiz_layout.addWidget(self.angle_sym_Va)

        # --------------------------Dynamic QLabel------------------------------
        self.deg_Va = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.deg_Va.setFont(font)
        self.deg_Va.setObjectName("deg_Va")
        #-------------------------------------------------------------------------

        self.va_horiz_layout.addWidget(self.deg_Va)
        self.deg_sym_Va = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.deg_sym_Va.setFont(font)
        self.deg_sym_Va.setObjectName("deg_sym_Va")
        self.va_horiz_layout.addWidget(self.deg_sym_Va)
        self.volt_table_layout.addLayout(self.va_horiz_layout)
        self.vb_horiz_layout = QtWidgets.QHBoxLayout()
        self.vb_horiz_layout.setObjectName("vb_horiz_layout")
        self.Vb = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Vb.setFont(font)
        self.Vb.setObjectName("Vb")
        self.vb_horiz_layout.addWidget(self.Vb)

        # --------------------------Dynamic QLabel------------------------------
        self.mag_Vb = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.mag_Vb.setFont(font)
        self.mag_Vb.setObjectName("mag_Vb")
        #-----------------------------------------------------------------------

        self.vb_horiz_layout.addWidget(self.mag_Vb)
        self.angle_sym_Vb = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.angle_sym_Vb.setFont(font)
        self.angle_sym_Vb.setObjectName("angle_sym_Vb")
        self.vb_horiz_layout.addWidget(self.angle_sym_Vb)

        # --------------------------Dynamic QLabel------------------------------
        self.deg_Vb = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.deg_Vb.setFont(font)
        self.deg_Vb.setObjectName("deg_Vb")
        #-----------------------------------------------------------------------

        self.vb_horiz_layout.addWidget(self.deg_Vb)
        self.deg_sym_Vb = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.deg_sym_Vb.setFont(font)
        self.deg_sym_Vb.setObjectName("deg_sym_Vb")
        self.vb_horiz_layout.addWidget(self.deg_sym_Vb)
        self.volt_table_layout.addLayout(self.vb_horiz_layout)
        self.vc_horiz_layout = QtWidgets.QHBoxLayout()
        self.vc_horiz_layout.setObjectName("vc_horiz_layout")
        self.Vc = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Vc.setFont(font)
        self.Vc.setObjectName("Vc")
        self.vc_horiz_layout.addWidget(self.Vc)

        # --------------------------Dynamic QLabel------------------------------
        self.mag_Vc = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.mag_Vc.setFont(font)
        self.mag_Vc.setObjectName("mag_Vc")
        #--------------------------------------------------------------------------

        self.vc_horiz_layout.addWidget(self.mag_Vc)
        self.angle_sym_Vc = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.angle_sym_Vc.setFont(font)
        self.angle_sym_Vc.setObjectName("angle_sym_Vc")
        self.vc_horiz_layout.addWidget(self.angle_sym_Vc)

        # --------------------------Dynamic QLabel------------------------------
        self.deg_Vc = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.deg_Vc.setFont(font)
        self.deg_Vc.setObjectName("deg_Vc")
        #-------------------------------------------------------------------------

        self.vc_horiz_layout.addWidget(self.deg_Vc)
        self.deg_sym_Vc = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.deg_sym_Vc.setFont(font)
        self.deg_sym_Vc.setObjectName("deg_sym_Vc")
        self.vc_horiz_layout.addWidget(self.deg_sym_Vc)
        self.volt_table_layout.addLayout(self.vc_horiz_layout)
        self.horizontalLayout.addWidget(self.voltage_Frame)
        self.power_Frame = QtWidgets.QFrame(self.layoutWidget)
        self.power_Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.power_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.power_Frame.setObjectName("power_Frame")
        self.layoutWidget_2 = QtWidgets.QWidget(self.power_Frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(140, 20, 241, 151))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.volt_table_layout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.volt_table_layout_2.setContentsMargins(0, 0, 0, 0)
        self.volt_table_layout_2.setObjectName("volt_table_layout_2")
        self.power_per_phase_table_title = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.power_per_phase_table_title.setFont(font)
        self.power_per_phase_table_title.setObjectName("power_per_phase_table_title")
        self.volt_table_layout_2.addWidget(self.power_per_phase_table_title)
        self.line_3 = QtWidgets.QFrame(self.layoutWidget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.volt_table_layout_2.addWidget(self.line_3)
        self.va_horiz_layout_2 = QtWidgets.QHBoxLayout()
        self.va_horiz_layout_2.setObjectName("va_horiz_layout_2")
        self.Pa = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Pa.setFont(font)
        self.Pa.setObjectName("Pa")
        self.va_horiz_layout_2.addWidget(self.Pa)

        # --------------------------Dynamic QLabel------------------------------
        self.mag_Pa = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.mag_Pa.setFont(font)
        self.mag_Pa.setObjectName("mag_Pa")
        #------------------------------------------------------------------------

        self.va_horiz_layout_2.addWidget(self.mag_Pa)
        self.angle_sym_Pa = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.angle_sym_Pa.setFont(font)
        self.angle_sym_Pa.setObjectName("angle_sym_Pa")
        self.va_horiz_layout_2.addWidget(self.angle_sym_Pa)

        # --------------------------Dynamic QLabel------------------------------
        self.deg_Pa = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.deg_Pa.setFont(font)
        self.deg_Pa.setObjectName("deg_Pa")
        #----------------------------------------------------------------------

        self.va_horiz_layout_2.addWidget(self.deg_Pa)
        self.deg_sym_Pa = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.deg_sym_Pa.setFont(font)
        self.deg_sym_Pa.setObjectName("deg_sym_Pa")
        self.va_horiz_layout_2.addWidget(self.deg_sym_Pa)
        self.volt_table_layout_2.addLayout(self.va_horiz_layout_2)
        self.vb_horiz_layout_2 = QtWidgets.QHBoxLayout()
        self.vb_horiz_layout_2.setObjectName("vb_horiz_layout_2")
        self.Pb = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Pb.setFont(font)
        self.Pb.setObjectName("Pb")
        self.vb_horiz_layout_2.addWidget(self.Pb)

        # --------------------------Dynamic QLabel------------------------------
        self.mag_Pb = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.mag_Pb.setFont(font)
        self.mag_Pb.setObjectName("mag_Pb")
        #------------------------------------------------------------------------

        self.vb_horiz_layout_2.addWidget(self.mag_Pb)
        self.angle_sym_Pb = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.angle_sym_Pb.setFont(font)
        self.angle_sym_Pb.setObjectName("angle_sym_Pb")
        self.vb_horiz_layout_2.addWidget(self.angle_sym_Pb)

        # --------------------------Dynamic QLabel------------------------------
        self.deg_Pb = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.deg_Pb.setFont(font)
        self.deg_Pb.setObjectName("deg_Pb")
        #------------------------------------------------------------------------

        self.vb_horiz_layout_2.addWidget(self.deg_Pb)
        self.deg_sym_Pb = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.deg_sym_Pb.setFont(font)
        self.deg_sym_Pb.setObjectName("deg_sym_Pb")
        self.vb_horiz_layout_2.addWidget(self.deg_sym_Pb)
        self.volt_table_layout_2.addLayout(self.vb_horiz_layout_2)
        self.vc_horiz_layout_2 = QtWidgets.QHBoxLayout()
        self.vc_horiz_layout_2.setObjectName("vc_horiz_layout_2")
        self.Pc = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Pc.setFont(font)
        self.Pc.setObjectName("Pc")
        self.vc_horiz_layout_2.addWidget(self.Pc)

        # --------------------------Dynamic QLabel------------------------------
        self.mag_Pc = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.mag_Pc.setFont(font)
        self.mag_Pc.setObjectName("mag_Pc")
        #-----------------------------------------------------------------------

        self.vc_horiz_layout_2.addWidget(self.mag_Pc)
        self.angle_sym_Pc = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.angle_sym_Pc.setFont(font)
        self.angle_sym_Pc.setObjectName("angle_sym_Pc")
        self.vc_horiz_layout_2.addWidget(self.angle_sym_Pc)

        # --------------------------Dynamic QLabel------------------------------
        self.deg_Pc = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.deg_Pc.setFont(font)
        self.deg_Pc.setObjectName("deg_Pc")
        #------------------------------------------------------------------------

        self.vc_horiz_layout_2.addWidget(self.deg_Pc)
        self.deg_sym_Pc = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.deg_sym_Pc.setFont(font)
        self.deg_sym_Pc.setObjectName("deg_sym_Pc")
        self.vc_horiz_layout_2.addWidget(self.deg_sym_Pc)
        self.volt_table_layout_2.addLayout(self.vc_horiz_layout_2)
        self.horizontalLayout.addWidget(self.power_Frame)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 200, 1571, 531))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.currentPhasor = CurrentPhasor(self.layoutWidget3)
        self.currentPhasor.setObjectName("currentPhasor")
        self.horizontalLayout_2.addWidget(self.currentPhasor)
        self.voltagePhasor = VoltagePhasor(self.layoutWidget3)
        self.voltagePhasor.setObjectName("voltagePhasor")
        self.horizontalLayout_2.addWidget(self.voltagePhasor)
        self.xtraPlot = DynamicPhasor1(self.layoutWidget3)
        self.xtraPlot.setObjectName("xtraPlot")
        self.horizontalLayout_2.addWidget(self.xtraPlot)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1678, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAnalysis = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport_Values_CSV = QtWidgets.QAction(MainWindow)
        self.actionExport_Values_CSV.setObjectName("actionExport_Values_CSV")
        self.actionPlots = QtWidgets.QAction(MainWindow)
        self.actionPlots.setObjectName("actionPlots")
        self.menuFile.addAction(self.actionExport_Values_CSV)
        self.menuAnalysis.addAction(self.actionPlots)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #-------------------------------------------PART 2 to Update QLabels-------------------------------------------
        # after 1 second (1000 milliseconds), call self.updateLabel. This is a trigger that gets current value of QLabes
        # from the updateLabel function
        QtCore.QTimer.singleShot(1000, lambda: self.updateLabel(self.mag_Ia, self.mag_Ib, self.mag_Ic, self.deg_Ia, self.deg_Ib, self.deg_Ic,
                                                                self.mag_Va, self.mag_Vb, self.mag_Vc, self.deg_Va, self.deg_Vb, self.deg_Vc,
                                                                self.mag_Pa, self.mag_Pb, self.mag_Pc, self.deg_Pa, self.deg_Pb, self.deg_Pc))
        #---------------------------------------------------------------------------------------------------------------

    # -------------------------------------------PART 3 to Update QLabels-------------------------------------------
    # updateLabel will keep updating the QLabels on the GUI
    def updateLabel(self, current_mag_Ia, current_mag_Ib, current_mag_Ic, current_deg_Ia, current_deg_Ib, current_deg_Ic,
                    current_mag_Va, current_mag_Vb, current_mag_Vc, current_deg_Va, current_deg_Vb, current_deg_Vc,
                    current_mag_Pa, current_mag_Pb, current_mag_Pc, current_deg_Pa, current_deg_Pb, current_deg_Pc):
           # change the following line to retrieve the new voltage from
           #the device
        mag_Ia = mag_Ib = mag_Ic = random.gauss(20.0, 2.0)


        deg_Ia = random.gauss(0.0, 2.0)
        deg_Ib = random.gauss(-180.0, 2.0)
        deg_Ic = random.gauss(180, 2.0)


        new_mag_Ia = float('%.1f' % mag_Ia)
        new_mag_Ib = float('%.1f' % mag_Ib)
        new_mag_Ic = float('%.1f' % mag_Ic)

        new_deg_Ia = float('%.1f' % deg_Ia)
        new_deg_Ib = float('%.1f' % deg_Ib)
        new_deg_Ic = float('%.1f' % deg_Ic)

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

        new_mag_Va = float('%.1f' % mag_Va)
        new_mag_Vb = float('%.1f' % mag_Vb)
        new_mag_Vc = float('%.1f' % mag_Vc)

        new_deg_Va = float('%.1f' % deg_Va)
        new_deg_Vb = float('%.1f' % deg_Vb)
        new_deg_Vc = float('%.1f' % deg_Vc)

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

        new_mag_Pa = float('%.1f' % mag_Pa)
        new_mag_Pb = float('%.1f' % mag_Pb)
        new_mag_Pc = float('%.1f' % mag_Pc)

        new_deg_Pa = float('%.1f' % deg_Pa)
        new_deg_Pb = float('%.1f' % deg_Pb)
        new_deg_Pc = float('%.1f' % deg_Pc)

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
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Currents_per_phase_table_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Current</p></body></html>"))
        self.Ia.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"> I<span style=\" vertical-align:sub;\">A =</span></p></body></html>"))
        #self.mag_Ia.setText(_translate("MainWindow", "Magn"))
        self.angle_symbol_a.setText(_translate("MainWindow", "∠"))
        self.deg_Ia.setText(_translate("MainWindow", "degree"))
        self.deg_symbol_Ia.setText(_translate("MainWindow", "°"))
        self.Ib.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">I<span style=\" vertical-align:sub;\">B =</span></p></body></html>"))
        self.mag_Ib.setText(_translate("MainWindow", "Magn"))
        self.angle_symbol_b.setText(_translate("MainWindow", "∠"))
        self.deg_Ib.setText(_translate("MainWindow", "degree"))
        self.deg_symbol_Ib.setText(_translate("MainWindow", "°"))
        self.Ic.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">I<span style=\" vertical-align:sub;\">C = </span></p></body></html>"))
        self.mag_Ic.setText(_translate("MainWindow", "Magn"))
        self.angle_symbol_c.setText(_translate("MainWindow", "∠"))
        self.deg_Ic.setText(_translate("MainWindow", "degree"))
        self.deg_symbol_Ic.setText(_translate("MainWindow", "°"))
        self.voltages_per_phase_table_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Voltage</p></body></html>"))
        self.Va.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">V<span style=\" vertical-align:sub;\">A =</span></p></body></html>"))
        self.mag_Va.setText(_translate("MainWindow", "Magn"))
        self.angle_sym_Va.setText(_translate("MainWindow", "∠"))
        self.deg_Va.setText(_translate("MainWindow", "degree"))
        self.deg_sym_Va.setText(_translate("MainWindow", "°"))
        self.Vb.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">V<span style=\" vertical-align:sub;\">B =</span></p></body></html>"))
        self.mag_Vb.setText(_translate("MainWindow", "Magn"))
        self.angle_sym_Vb.setText(_translate("MainWindow", "∠"))
        self.deg_Vb.setText(_translate("MainWindow", "degree"))
        self.deg_sym_Vb.setText(_translate("MainWindow", "°"))
        self.Vc.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">V<span style=\" vertical-align:sub;\">C =</span></p></body></html>"))
        self.mag_Vc.setText(_translate("MainWindow", "Magn"))
        self.angle_sym_Vc.setText(_translate("MainWindow", "∠"))
        self.deg_Vc.setText(_translate("MainWindow", "degree"))
        self.deg_sym_Vc.setText(_translate("MainWindow", "°"))
        self.power_per_phase_table_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Power</p></body></html>"))
        self.Pa.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">P<span style=\" vertical-align:sub;\">A =</span></p></body></html>"))
        self.mag_Pa.setText(_translate("MainWindow", "Magn"))
        self.angle_sym_Pa.setText(_translate("MainWindow", "∠"))
        self.deg_Pa.setText(_translate("MainWindow", "degree"))
        self.deg_sym_Pa.setText(_translate("MainWindow", "°"))
        self.Pb.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">P<span style=\" vertical-align:sub;\">B =</span></p></body></html>"))
        self.mag_Pb.setText(_translate("MainWindow", "Magn"))
        self.angle_sym_Pb.setText(_translate("MainWindow", "∠"))
        self.deg_Pb.setText(_translate("MainWindow", "degree"))
        self.deg_sym_Pb.setText(_translate("MainWindow", "°"))
        self.Pc.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">P<span style=\" vertical-align:sub;\">C =</span></p></body></html>"))
        self.mag_Pc.setText(_translate("MainWindow", "Magn"))
        self.angle_sym_Pc.setText(_translate("MainWindow", "∠"))
        self.deg_Pc.setText(_translate("MainWindow", "degree"))
        self.deg_sym_Pc.setText(_translate("MainWindow", "°"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.actionExport_Values_CSV.setText(_translate("MainWindow", "Export Values (*.CSV)"))
        self.actionPlots.setText(_translate("MainWindow", "Faults"))



from phasor_plots import *
import resources_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_RelayGUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
