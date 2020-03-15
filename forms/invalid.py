# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'invalid.ui',
# licensing of 'invalid.ui' applies.
#
# Created: Sun Mar 15 11:22:27 2020
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_invalid_message(object):
    def setupUi(self, invalid_message):
        invalid_message.setObjectName("invalid_message")
        invalid_message.resize(194, 112)
        self.label = QtWidgets.QLabel(invalid_message)
        self.label.setGeometry(QtCore.QRect(50, 30, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(invalid_message)
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(invalid_message)
        QtCore.QMetaObject.connectSlotsByName(invalid_message)

    def retranslateUi(self, invalid_message):
        invalid_message.setWindowTitle(QtWidgets.QApplication.translate("invalid_message", "Invalid!", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("invalid_message", "Please fill all field!", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("invalid_message", "Ok", None, -1))

