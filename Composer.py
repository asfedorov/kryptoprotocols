# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Composer.ui'
#
# Created: Wed Jan  9 03:35:01 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(566, 490)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.listOfFiles = QtGui.QListWidget(self.centralwidget)
        self.listOfFiles.setGeometry(QtCore.QRect(10, 10, 541, 192))
        self.listOfFiles.setObjectName(_fromUtf8("listOfFiles"))
        self.addFileButton = QtGui.QPushButton(self.centralwidget)
        self.addFileButton.setGeometry(QtCore.QRect(130, 210, 96, 27))
        self.addFileButton.setObjectName(_fromUtf8("addFileButton"))
        self.removeFileButton = QtGui.QPushButton(self.centralwidget)
        self.removeFileButton.setGeometry(QtCore.QRect(330, 210, 96, 27))
        self.removeFileButton.setObjectName(_fromUtf8("removeFileButton"))
        self.composeButton = QtGui.QPushButton(self.centralwidget)
        self.composeButton.setGeometry(QtCore.QRect(230, 310, 96, 27))
        self.composeButton.setObjectName(_fromUtf8("composeButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.addFileButton.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.removeFileButton.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.composeButton.setText(QtGui.QApplication.translate("MainWindow", "Compose!", None, QtGui.QApplication.UnicodeUTF8))

