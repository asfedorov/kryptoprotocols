# -*- coding:utf-8-*-
import sys, random

from PyQt4 import QtCore, QtGui, Qt
from MainWindow import Ui_MainWindow

import lab2


class MainForm(QtGui.QMainWindow):
    def __init__(self, parent=None):

        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)   
        # super(Window, self).__init__(parent)
        self.ui.setupUi(self)

        self.connect(self.ui.addParticipantButton, QtCore.SIGNAL('pressed()'),self.newParticipant)
        self.connect(self.ui.removeParticipantButton, QtCore.SIGNAL('pressed()'),self.removeParticipant)
        self.connect(self.ui.addToGroupButton, QtCore.SIGNAL('pressed()'),self.addParticipantToGroup)
        self.connect(self.ui.listOfParticipants, QtCore.SIGNAL("itemChanged(QListWidgetItem*)"),self.changeParticipantName)
        self.connect(self.ui.listOfParticipants, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"),self.addParticipantToGroup)

    def newParticipant(self):
    	# name = random.randrange(0,10)

        i = 0
        while self.ui.listOfParticipants.findItems("participant"+str(i), QtCore.Qt.MatchExactly).__len__() != 0:
            i = i+1
        name = "participant"+str(i)
        participantCount = self.ui.listOfParticipants.count()
    	participant = lab2.Participant(name)
    	participantItem = QtGui.QListWidgetItem(name)
    	participantItem.setData(32, participant)
    	participantItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
    	self.ui.listOfParticipants.addItem(participantItem)

    def removeParticipant(self):
    	participantItem = self.ui.listOfParticipants.selectedItems()[0]
    	participant = participantItem.data(32).toPyObject()
    	self.ui.listOfParticipants.takeItem(self.ui.listOfParticipants.row(participantItem))


    def addParticipantToGroup(self):
    	participantItem = self.ui.listOfParticipants.selectedItems()[0]
    	participant = participantItem.data(32).toPyObject()
    	self.ui.listOfGroups.clear()
    	# print participant.name
    	self.ui.listOfGroups.addItem(str(participant.name))

    def changeParticipantName(self):
    	participantItem = self.ui.listOfParticipants.selectedItems()[0]
    	participant = participantItem.data(32).toPyObject()
    	participant.name = participantItem.text()
    	participantItem.setData(32, participant)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("KryptoSystem2013")
    myapp = MainForm()
    myapp.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        pass