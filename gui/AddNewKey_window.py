from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os


class AddNewKey_Window(QWidget):
    def __init__(self):
        super(AddNewKey_Window, self).__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.setWindowTitle("Add New Key")
        self.resize(600, 400)
        self.cmb = QComboBox()
        self.cmb.addItem("Select USB Drive Properly")
        layout.addWidget(self.cmb)
        self.pwdlabel = QLabel("Enter Password")
        layout.addWidget(self.pwdlabel)
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password)
        button = QPushButton("Verify")
        layout.addWidget(button)
        self.cnfpwdlabel = QLabel("Enter Password you want to Delete")
        layout.addWidget(self.cnfpwdlabel)
        self.confirmpassword = QLineEdit()
        self.confirmpassword.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.confirmpassword)
        button = QPushButton("Delete Password")
        layout.addWidget(button)
