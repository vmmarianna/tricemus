# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tricemus.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_file_label = QtWidgets.QLabel(self.centralwidget)
        self.open_file_label.setGeometry(QtCore.QRect(10, 130, 54, 17))
        self.open_file_label.setObjectName("open_file_label")
        self.open_file_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.open_file_lineEdit.setGeometry(QtCore.QRect(70, 120, 113, 25))
        self.open_file_lineEdit.setObjectName("open_file_lineEdit")
        self.open_file_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.open_file_pushButton.setGeometry(QtCore.QRect(190, 120, 80, 25))
        self.open_file_pushButton.setObjectName("open_file_pushButton")
        self.save_to_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.save_to_pushButton.setGeometry(QtCore.QRect(670, 120, 80, 25))
        self.save_to_pushButton.setObjectName("save_to_pushButton")
        self.save_to_label = QtWidgets.QLabel(self.centralwidget)
        self.save_to_label.setGeometry(QtCore.QRect(490, 130, 54, 17))
        self.save_to_label.setObjectName("save_to_label")
        self.save_to_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.save_to_lineEdit.setGeometry(QtCore.QRect(550, 120, 113, 25))
        self.save_to_lineEdit.setText("")
        self.save_to_lineEdit.setObjectName("save_to_lineEdit")
        self.load_text_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.load_text_pushButton.setGeometry(QtCore.QRect(130, 160, 80, 25))
        self.load_text_pushButton.setObjectName("load_text_pushButton")
        self.save_text_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.save_text_pushButton.setGeometry(QtCore.QRect(620, 160, 80, 25))
        self.save_text_pushButton.setObjectName("save_text_pushButton")
        self.encrypt_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt_pushButton.setGeometry(QtCore.QRect(120, 290, 80, 25))
        self.encrypt_pushButton.setObjectName("encrypt_pushButton")
        self.decrypt_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.decrypt_pushButton.setGeometry(QtCore.QRect(610, 290, 80, 25))
        self.decrypt_pushButton.setObjectName("decrypt_pushButton")
        self.keyword_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.keyword_lineEdit.setGeometry(QtCore.QRect(350, 220, 113, 25))
        self.keyword_lineEdit.setObjectName("keyword_lineEdit")
        self.keyword_label = QtWidgets.QLabel(self.centralwidget)
        self.keyword_label.setGeometry(QtCore.QRect(280, 230, 54, 17))
        self.keyword_label.setObjectName("keyword_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_file_label.setText(_translate("MainWindow", "OpenFile"))
        self.open_file_pushButton.setText(_translate("MainWindow", "Open"))
        self.save_to_pushButton.setText(_translate("MainWindow", "Open"))
        self.save_to_label.setText(_translate("MainWindow", "SaveTo"))
        self.load_text_pushButton.setText(_translate("MainWindow", "LoadText"))
        self.save_text_pushButton.setText(_translate("MainWindow", "SaveText"))
        self.encrypt_pushButton.setText(_translate("MainWindow", "Encrypt"))
        self.decrypt_pushButton.setText(_translate("MainWindow", "Decrypt"))
        self.keyword_label.setText(_translate("MainWindow", "keyword"))
