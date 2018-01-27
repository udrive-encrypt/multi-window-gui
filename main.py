from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Encryption_window import Encryption_Window
from AddNewKey_window import AddNewKey_Window
from DeleteExistingKey_window import DeleteKey_Window
from PyQt5.Qt import *
import sys
import os


class Main_Window(QWidget):
    def __init__(self):
        super(Main_Window, self).__init__()

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.resize(400, 300)

        self.encrpyt = QRadioButton("Encrypt the USB Drives")
        self.encrpyt.setCheckable(True)
        self.encrpyt.setChecked(False)
        self.layout.addWidget(self.encrpyt)

        self.add_new_key = QRadioButton("Add New Key")
        self.add_new_key.setCheckable(True)
        self.add_new_key.setChecked(False)
        self.layout.addWidget(self.add_new_key)

        self.delete_key = QRadioButton("Delete Existing Key")
        self.delete_key.setCheckable(True)
        self.delete_key.setChecked(False)
        self.layout.addWidget(self.delete_key)

        self.Ewindow = Encryption_Window()
        self.Awindow = AddNewKey_Window()
        self.Dwindow = DeleteKey_Window()

        self.encrpyt.toggled.connect(self.Encrypt)
        self.add_new_key.toggled.connect(self.AddNewKey)
        self.delete_key.toggled.connect(self.DeleteKey)

    def Encrypt(self, enabled):
        if enabled:
            self.Dwindow.close()
            self.Awindow.close()
            self.Ewindow.show()

    # self.show()

    #

    # self.window = QWidget.QMainWindow()
    # self.encryption1 = Encryption_Window()
    # self.encryption1.show()

    def AddNewKey(self, enabled):
        if enabled:
            self.Ewindow.close()
            self.Dwindow.close()
            self.Awindow.show()

    #      self.encryption1 = AddNewKey_Window()

    #     self.window.show()

    def DeleteKey(self, enabled):
        if enabled:
            self.Ewindow.close()
            self.Awindow.close()
            self.Dwindow.show()


#        self.encryption1 = DeleteKey_Window()
#  self.window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = Main_Window()
    # screen.mainwindow()
    screen.show()
    sys.exit(app.exec_())

# run()