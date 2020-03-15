# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui',
# licensing of 'error.ui' applies.
#
# Created: Sat Mar 14 12:28:57 2020
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_error_message(object):
    def setupUi(self, error_message):
        error_message.setObjectName("error_message")
        error_message.resize(225, 106)
        self.label = QtWidgets.QLabel(error_message)
        self.label.setGeometry(QtCore.QRect(30, 30, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(error_message)
        self.pushButton.setGeometry(QtCore.QRect(80, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(error_message)
        QtCore.QMetaObject.connectSlotsByName(error_message)

    def retranslateUi(self, error_message):
        error_message.setWindowTitle(QtWidgets.QApplication.translate("error_message", "Error!", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("error_message", "Oops! something went wrong!", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("error_message", "Ok", None, -1))

