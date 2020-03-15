# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'success.ui',
# licensing of 'success.ui' applies.
#
# Created: Sat Mar 14 23:00:38 2020
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_message_box(object):
    def setupUi(self, message_box):
        message_box.setObjectName("message_box")
        message_box.resize(213, 89)
        self.label = QtWidgets.QLabel(message_box)
        self.label.setGeometry(QtCore.QRect(40, 20, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(message_box)
        self.pushButton.setGeometry(QtCore.QRect(70, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(message_box)
        QtCore.QMetaObject.connectSlotsByName(message_box)

    def retranslateUi(self, message_box):
        message_box.setWindowTitle(QtWidgets.QApplication.translate("message_box", "Success", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("message_box", "Successfully extracted!!", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("message_box", "OK", None, -1))

