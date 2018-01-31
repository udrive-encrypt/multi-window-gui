from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os


class Encryption_Window(QWidget):
    def __init__(self):
        super(Encryption_Window, self).__init__()
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(layout)
        self.setWindowTitle("Encryption")
        self.resize(600,400)
        self.cmb = QComboBox()
        self.cmb.addItem("Select USB Drive Properly")
        layout.addWidget(self.cmb)
        button = QPushButton("Format")
        layout.addWidget(button)
        self.pwdlabel = QLabel("Enter Password")
        layout.addWidget(self.pwdlabel)
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password)
        self.cnfpwdlabel = QLabel("Confirm Password")
        layout.addWidget(self.cnfpwdlabel)
        self.confirmpassword = QLineEdit()
        self.confirmpassword.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.confirmpassword)
        button = QPushButton("Enter Password")
        layout.addWidget(button)
