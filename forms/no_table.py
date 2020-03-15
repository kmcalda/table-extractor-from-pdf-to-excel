# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'no_table.ui',
# licensing of 'no_table.ui' applies.
#
# Created: Sun Mar 15 10:48:22 2020
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_message_pdf(object):
    def setupUi(self, message_pdf):
        message_pdf.setObjectName("message_pdf")
        message_pdf.resize(213, 89)
        self.label = QtWidgets.QLabel(message_pdf)
        self.label.setGeometry(QtCore.QRect(30, 20, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(message_pdf)
        self.pushButton.setGeometry(QtCore.QRect(70, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(message_pdf)
        QtCore.QMetaObject.connectSlotsByName(message_pdf)

    def retranslateUi(self, message_pdf):
        message_pdf.setWindowTitle(QtWidgets.QApplication.translate("message_pdf", "Invalid", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("message_pdf", "No table found inside PDF!!", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("message_pdf", "OK", None, -1))

