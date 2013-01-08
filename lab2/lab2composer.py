# -*- coding:utf-8-*-
import sys, random

from PyQt4 import QtCore, QtGui, Qt
from Composer import Ui_MainWindow

import lab2


class MainForm(QtGui.QMainWindow):
    def __init__(self, parent=None):

        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)   
        # super(Window, self).__init__(parent)
        self.ui.setupUi(self)

        self.connect(self.ui.addFileButton, QtCore.SIGNAL('pressed()'),self.openFile)
        self.connect(self.ui.composeButton, QtCore.SIGNAL('pressed()'),self.compose)

    def compose(self):
        secretParts = []

        files = self.ui.listOfFiles.findItems("",QtCore.Qt.MatchContains)

        secretPartFile = open(files[0].text(),"rb")

        result = int(secretPartFile.read(),2)
        secretPartFile.close()
        i = 1
        while i<files.__len__():
            secretPartFile = open(files[i].text(),"rb")
            result = result.__xor__(int(secretPartFile.read(),2))
            secretPartFile.close()
            i = i+1

        result = bin(result)[2:]
        reverseResult = ""
        while result.__len__() > 0:
            reverseResult = reverseResult + result[-128:]
            result = result[:-128]
            print "+++"+reverseResult[-128:]
        reverseResult = reverseResult + result
        secretRevealed = ""
        
        while reverseResult.__len__() >= 128:
            secretBinPart = reverseResult[:8]
            reverseResult = reverseResult[8:]
            secretRevealed =  secretRevealed + unichr(int(secretBinPart,2))

        secretRevealedEnd = ""
        while reverseResult.__len__() > 0:
            secretBinPart = reverseResult[-8:]
            reverseResult = reverseResult[:-8]
            secretRevealedEnd =  unichr(int(secretBinPart,2)) + secretRevealedEnd

        secretRevealed = secretRevealed + secretRevealedEnd
        print secretRevealed

        secretRevealedFile = open("secretRevealed.txt", "w+")
        secretRevealedFile.write(secretRevealed)
        secretRevealedFile.close()

        # for filename in self.ui.listOfFiles.findItems("",QtCore.Qt.MatchContains):
        #     secretPartFile = open(filename.text(),"rb")

        #     secretPart = secretFile.read()

            

    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileNames(self, 'Open File')[0]

        self.ui.listOfFiles.addItem(filename)

        # secret = open(filename,"rb")

        # secretBin = ""
        # while 1:
        #   char = secret.read(1)
        #   if not char: break
        #   charBin = bin(ord(char)).replace("0b", "").zfill(8)
        #   secretBin = secretBin + charBin
        
        # secret.close()

        # while secretBin.__len__() > 128:
        #     secretBinPart = secretBin[-128:]
        #     secretBin = secretBin[:-128]
            
        #     for groupItem in self.ui.listOfGroups.findItems("group", QtCore.Qt.MatchStartsWith):
        #         group = groupItem.data(32).toPyObject()
        #         sender = lab2.Sender(int(secretBinPart,2), group)
        #         sender.getPart()
        #         for participant in group.participants:
        #             filename = group.name + "." + participant.name + "-part"
        #             f = open(filename, "a+")
        #             # print group.name
        #             participantSecret = (bin(int(participant.parts[group.name]))[2:]).zfill(128)
        #             f.seek(0)
        #             f.write(participantSecret)
        #             f.close

        #     # print secretBinPart
        # secretBinPart = secretBin.zfill(128)

        # for groupItem in self.ui.listOfGroups.findItems("group", QtCore.Qt.MatchStartsWith):
        #     group = groupItem.data(32).toPyObject()
        #     sender = lab2.Sender(int(secretBinPart,2), group)
        #     sender.getPart()
        #     for participant in group.participants:
        #         filename = group.name + "." + participant.name + "-part"
        #         f = open(filename, "a+")
        #         # print participant.part
        #         participantSecret = (bin(int(participant.parts[group.name]))[2:]).zfill(128)
        #         f.seek(0)
        #         f.write(participantSecret)
        #         f.close

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("KryptoSystem2013")
    myapp = MainForm()
    myapp.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        pass