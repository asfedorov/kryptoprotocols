#-*- coding:utf-8 -*-

class hashCypher():
	def __init__(self, message):
		self.message = message

	def getMessageParts(self):
		messagebin = ""
		for ch in message:
			chBin = bin(ord(ch)).replace("0b", "").zfill(8)
			messageBin = messageBin + chBin

		return messageBin


