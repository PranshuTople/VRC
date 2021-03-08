#!/usr/bin/python

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoui2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from std_msgs.msg import Float64

class Ui_Form(object):

    


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(379, 219)
		

	def grippervaluechange():
		print("gslider = "+ str(self.gslider.value()))
		g = self.gslider.value()
		msg = g/1000.0
		pubslide1.publish(msg)

	def armvaluechange():
		print("aslider = "+ str(self.aslider.value()))
		a = self.aslider.value()
		msg2  = a/1000.0
		pubslide2.publish(msg2)



        self.gslider = QtWidgets.QSlider(Form)
        self.gslider.setGeometry(QtCore.QRect(40, 30, 311, 81))
        self.gslider.setMinimum(-1571)
        self.gslider.setMaximum(1571)
        self.gslider.setSliderPosition(0)
        self.gslider.setSingleStep(1)
	
        self.gslider.setOrientation(QtCore.Qt.Horizontal)
        self.gslider.setObjectName("gslider")


        self.aslider = QtWidgets.QSlider(Form)
        self.aslider.setGeometry(QtCore.QRect(40, 110, 301, 81))
        self.aslider.setMinimum(-262)
	self.aslider.setMaximum(1571)
	self.aslider.setSingleStep(1)
	self.aslider.setSliderPosition(157)
        self.aslider.setOrientation(QtCore.Qt.Horizontal)
        self.aslider.setObjectName("aslider")


        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 30, 131, 17))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 110, 131, 17))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

	self.gslider.valueChanged.connect(grippervaluechange)
	self.aslider.valueChanged.connect(armvaluechange)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Gripper Slider"))
        self.label_2.setText(_translate("Form", "Arm Slider"))


if __name__ == "__main__":
	import sys

        pubslide1 = rospy.Publisher('/manbot/finger_joint_position_controller/command',Float64,queue_size=1)
	pubslide2 = rospy.Publisher('/manbot/gripper_joint_position_controller/command',Float64,queue_size=1)
	rospy.init_node('myGUI', anonymous=True)
	
	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())

