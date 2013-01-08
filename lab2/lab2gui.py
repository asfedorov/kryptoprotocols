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
        self.connect(self.ui.listOfParticipants, QtCore.SIGNAL("itemChanged(QListWidgetItem*)"),self.changeParticipantName)
        # self.connect(self.ui.listOfParticipants, QtCore.SIGNAL("itemClicked(QListWidgetItem*)"),self.addParticipantToGroup)

        self.connect(self.ui.addGroupButton, QtCore.SIGNAL('pressed()'),self.newGroup)
        self.connect(self.ui.removeGroupButton, QtCore.SIGNAL('pressed()'),self.removeGroup)

        self.connect(self.ui.addToGroupButton, QtCore.SIGNAL('pressed()'),self.addParticipantToGroup)
        self.connect(self.ui.removeFromGroupButton, QtCore.SIGNAL('pressed()'),self.removeParticipantFromGroup)

    def newParticipant(self):
    	# name = random.randrange(0,10)

        i = 0
        while self.ui.listOfParticipants.findItems("participant"+str(i), QtCore.Qt.MatchExactly).__len__() != 0:
            i = i+1
        name = "participant"+str(i)
        
    	participant = lab2.Participant(name)
    	participantItem = QtGui.QListWidgetItem(name)
    	participantItem.setData(32, participant)
    	participantItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
    	self.ui.listOfParticipants.addItem(participantItem)

    def removeParticipant(self):
    	participantItem = self.ui.listOfParticipants.selectedItems()[0]
    	participant = participantItem.data(32).toPyObject()

        for groupItem in self.ui.listOfGroups.findItems(":"+participant.name, QtCore.Qt.MatchContains):
            groupName = groupItem.text().replace(":"+participant.name, "")
            groupItem.setText(groupName) 
            group = groupItem.data(32).toPyObject()
            group.removeParticipant(participant)

    	self.ui.listOfParticipants.takeItem(self.ui.listOfParticipants.row(participantItem))

    def changeParticipantName(self):
    	participantItem = self.ui.listOfParticipants.selectedItems()[0]
    	participant = participantItem.data(32).toPyObject()
        participantOldName = participant.name
    	participant.name = participantItem.text()
    	participantItem.setData(32, participant)

        for groupItem in self.ui.listOfGroups.findItems(":"+participantOldName, QtCore.Qt.MatchContains):
            groupName = groupItem.text().replace(":"+participantOldName, ":"+participantItem.text())
            groupItem.setText(groupName) 
            


    def newGroup(self):
        group = lab2.Group([])
        group.participants = []

        i = 0
        while self.ui.listOfGroups.findItems("group"+str(i), QtCore.Qt.MatchStartsWith).__len__() != 0:
            i = i+1
        name = "group"+str(i)

        groupItem = QtGui.QListWidgetItem(name)
        groupItem.setData(32, group)
        groupItem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.ui.listOfGroups.addItem(groupItem)

    def removeGroup(self):
        groupItem = self.ui.listOfGroups.selectedItems()[0]
        self.ui.listOfParticipants.takeItem(self.ui.listOfParticipants.row(participantItem))

    def addParticipantToGroup(self):
        participantItem = self.ui.listOfParticipants.selectedItems()[0]
        groupItem = self.ui.listOfGroups.selectedItems()[0]

        participant = participantItem.data(32).toPyObject()
        group = groupItem.data(32).toPyObject()

        if not group.addParticipant(participant) == 0:
            groupName = groupItem.text() + ":" + participant.name
            groupItem.setText(groupName)

    def removeParticipantFromGroup(self):
        participantItem = self.ui.listOfParticipants.selectedItems()[0]
        groupItem = self.ui.listOfGroups.selectedItems()[0]

        participant = participantItem.data(32).toPyObject()
        group = groupItem.data(32).toPyObject()

        if not group.removeParticipant(participant) == 0:
            groupName = groupItem.text().replace(":"+participant.name, "")
            groupItem.setText(groupName)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("KryptoSystem2013")
    myapp = MainForm()
    myapp.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        pass