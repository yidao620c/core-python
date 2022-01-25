# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sha256.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SHA256(object):
    def setupUi(self, SHA256):
        SHA256.setObjectName("SHA256")
        SHA256.resize(664, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SHA256.sizePolicy().hasHeightForWidth())
        SHA256.setSizePolicy(sizePolicy)
        SHA256.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SHA256.setWindowIcon(icon)
        SHA256.setStyleSheet("font: 75 10pt \"微软雅黑\";")
        self.centralwidget = QtWidgets.QWidget(SHA256)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 140, 81, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 140, 431, 31))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 140, 31, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 430, 111, 41))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(120, 0, 361, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 311, 51))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("font: 75 14pt \"微软雅黑\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(30, 50, 321, 21))
        self.line.setMinimumSize(QtCore.QSize(321, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.line.setFont(font)
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(110, 190, 431, 211))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.lineEdit.raise_()
        self.label.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.frame.raise_()
        self.plainTextEdit.raise_()
        SHA256.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SHA256)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 29))
        self.menubar.setObjectName("menubar")
        SHA256.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(SHA256)
        self.statusBar.setObjectName("statusBar")
        SHA256.setStatusBar(self.statusBar)

        self.retranslateUi(SHA256)
        QtCore.QMetaObject.connectSlotsByName(SHA256)

    def retranslateUi(self, SHA256):
        _translate = QtCore.QCoreApplication.translate
        SHA256.setWindowTitle(_translate("SHA256", "SHA256小工具"))
        self.label.setText(_translate("SHA256", "选择目录："))
        self.pushButton.setText(_translate("SHA256", "..."))
        self.pushButton_2.setText(_translate("SHA256", "开始"))
        self.label_2.setText(_translate("SHA256", "<html><head/><body><p><span style=\" font-weight:600; color:#00aaff;\">自动生成json文件的散列值</span></p></body></html>"))
from . import images_rc
