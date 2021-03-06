#!/usr/bin/python

import rospy
from std_msgs.msg import Bool
from std_msgs.msg import Float64
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):

        def button1_pressed():
            msg=True
            pub.publish(msg)

        def button1_released():
            msg=False
            pub.publish(msg)

        def valuechange():
            size = self.horizontalSlider.value()
            msg= size/1000.0
            pubslide1.publish(msg)

        def valuechange_2():
            size2 = self.horizontalSlider_2.value()
            msg2= size2/1000.0
            pubslide2.publish(msg2)

        Form.setObjectName("Form")
        Form.resize(400, 238)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-10, 0, 421, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(250, 0))
        self.horizontalSlider.setMinimum(-1571)
        self.horizontalSlider.setMaximum(1571)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickInterval(0)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider_2.setMinimumSize(QtCore.QSize(250, 0))
        self.horizontalSlider_2.setMinimum(-262)
        self.horizontalSlider_2.setMaximum(1571)
        self.horizontalSlider_2.setProperty("value", 0)
        self.horizontalSlider_2.setSliderPosition(0)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setInvertedAppearance(False)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayout_2.addWidget(self.horizontalSlider_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.pressed.connect(button1_pressed)
        self.pushButton.released.connect(button1_released)
        self.horizontalSlider.valueChanged.connect(valuechange)
        self.horizontalSlider_2.valueChanged.connect(valuechange_2)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ROS GUI"))
        self.pushButton.setText(_translate("Form", "Button"))


if __name__ == "__main__":
    
    import sys
    
    pub = rospy.Publisher('/button',Bool,queue_size=1)
    pubslide1 = rospy.Publisher('/manbot/finger_joint_position_controller/command',Float64,queue_size=1)
    pubslide2 = rospy.Publisher('/manbot/gripper_joint_position_controller/command',Float64,queue_size=1)
    rospy.init_node('test2', anonymous=True)
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

