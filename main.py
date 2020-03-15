from PySide2.QtWidgets import QFileDialog, QDialog, QApplication, QWidget, QMessageBox
from PySide2 import QtCore
from PySide2.QtGui import QIcon
from forms.pdf_to_csv import Ui_Form_name
from forms.success import Ui_message_box
from forms.invalid import  Ui_invalid_message
from forms.error import Ui_error_message
import sys, getpass, tabula
from pandas import DataFrame
import webbrowser
import numpy.random.common
import numpy.random.bounded_integers
import numpy.random.entropy


class MainWindow(QDialog, Ui_Form_name, Ui_message_box):
    def __init__(self):
        super().__init__()
        self.windows = Ui_Form_name()
        self.windows.setupUi(self)
        self.windows.toolButton.clicked.connect(self.file_opener)
        self.windows.toolButton_2.clicked.connect(self.file_destination)
        self.windows.pushButton.clicked.connect(self.converter)
        self.setWindowIcon(QIcon("icons/image.ico"))

    def file_opener(self):
        global file_name
        file_name = QFileDialog.getOpenFileName(None,"Open File",
        "c:\\users\\{}\\desktop".format(getpass.getuser()),"PDF files(*.pdf)")
        self.windows.lineEdit_4.setText(file_name[0].split("/")[-1])

    def file_destination(self):
        global file_destination
        file_destination = QFileDialog.getExistingDirectory(None,"Destination",
        "c:\\users\\{}\\desktop".format(getpass.getuser()))
        self.windows.lineEdit_5.setText(file_destination.split('/')[-1])
    
    def converter(self):
        if self.windows.lineEdit.text() and self.windows.lineEdit_5.text() and self.windows.lineEdit_4.text():
            try:
                date_extracted = tabula.read_pdf("{}".format(file_name[0]),  
                pages='{}'.format(self.windows.lineEdit.text()), lattice=True)
            
                data_frame = DataFrame(date_extracted)
                data_frame.to_excel("{}/{}.xlsx".format(file_destination,file_name[0].split("/")[-1]))

                self.window2 = QDialog()
                self.message_box = Ui_message_box()
                self.message_box.setupUi(self.window2)
                self.window2.setWindowModality(QtCore.Qt.ApplicationModal)
                self.window2.show()
                self.window2.setWindowIcon(QIcon("icons/image.ico"))
                self.message_box.pushButton.clicked.connect(self.close_message)
            except Exception as e:
                print(e)
                self.window4 = QDialog()
                self.message_box3 = Ui_error_message()
                self.message_box3.setupUi(self.window4)
                self.window4.setWindowModality(QtCore.Qt.ApplicationModal)
                self.window4.show()
                self.window4.setWindowIcon(QIcon("image.ico"))
                self.message_box3.pushButton.clicked.connect(self.error_warning)
            
        
        else:
            self.window3 = QDialog()
            self.message_box2 = Ui_invalid_message()
            self.message_box2.setupUi(self.window3)
            self.window3.setWindowModality(QtCore.Qt.ApplicationModal)
            self.window3.show()
            self.window3.setWindowIcon(QIcon("icons/image.ico"))
            self.message_box2.pushButton.clicked.connect(self.invalid_warning)

    def close_message(self):
        webbrowser.open("{}".format(file_destination))
        self.window2.close()
    
    def invalid_warning(self):
        self.window3.close()
    
    def error_warning(self):
        self.window4.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
