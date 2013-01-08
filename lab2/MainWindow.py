# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Mon Jan  7 02:50:39 2013
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
        self.removeFromGroupButton = QtGui.QPushButton(self.centralwidget)
        self.removeFromGroupButton.setGeometry(QtCore.QRect(260, 126, 51, 41))
        self.removeFromGroupButton.setObjectName(_fromUtf8("removeFromGroupButton"))
        self.addToGroupButton = QtGui.QPushButton(self.centralwidget)
        self.addToGroupButton.setGeometry(QtCore.QRect(260, 50, 51, 41))
        self.addToGroupButton.setObjectName(_fromUtf8("addToGroupButton"))
        self.addParticipantButton = QtGui.QPushButton(self.centralwidget)
        self.addParticipantButton.setGeometry(QtCore.QRect(30, 210, 96, 27))
        self.addParticipantButton.setObjectName(_fromUtf8("addParticipantButton"))
        self.removeParticipantButton = QtGui.QPushButton(self.centralwidget)
        self.removeParticipantButton.setGeometry(QtCore.QRect(140, 210, 96, 27))
        self.removeParticipantButton.setObjectName(_fromUtf8("removeParticipantButton"))
        self.addGroupButton = QtGui.QPushButton(self.centralwidget)
        self.addGroupButton.setGeometry(QtCore.QRect(330, 210, 96, 27))
        self.addGroupButton.setObjectName(_fromUtf8("addGroupButton"))
        self.removeGroupButton = QtGui.QPushButton(self.centralwidget)
        self.removeGroupButton.setGeometry(QtCore.QRect(450, 210, 96, 27))
        self.removeGroupButton.setObjectName(_fromUtf8("removeGroupButton"))
        self.listOfParticipants = QtGui.QListWidget(self.centralwidget)
        self.listOfParticipants.setGeometry(QtCore.QRect(10, 10, 241, 192))
        self.listOfParticipants.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked)
        self.listOfParticipants.setObjectName(_fromUtf8("listOfParticipants"))
        self.listOfGroups = QtGui.QListWidget(self.centralwidget)
        self.listOfGroups.setGeometry(QtCore.QRect(325, 10, 231, 192))
        self.listOfGroups.setObjectName(_fromUtf8("listOfGroups"))
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
        self.removeFromGroupButton.setText(QtGui.QApplication.translate("MainWindow", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.addToGroupButton.setText(QtGui.QApplication.translate("MainWindow", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.addParticipantButton.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.removeParticipantButton.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.addGroupButton.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.removeGroupButton.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))

