#-*- coding:utf-8 -*-

import random

class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.C = 0
        self.D = 0

    def generateC(self,P):
        pass

    def generateD(self, P):
        if self.C == 0:
            self.generateC(P)

        i = 1
        D = 0.1
        while 1:
            D = ((i*(P-1))+1.00)/self.C
            if ( self.C%D == self.C or D%self.C == D ) and D%P == D and D%1 == 0:
                break
            i = i + 1

        self.D = D 


    def encryptDeck(self, deck, P):
        newDeck = []
        
        for card in deck:
            newCard = pow(card, self.C) % P
            newDeck.append(newCard)

        random.shuffle(newDeck)
        return newDeck

    def decryptCard(self, card, P):
        print card
        if self.D == 0:
            self.generateD(P)

        newCard = pow(card, self.D) % P
        print "decrypted"

        return newCard
        

class CardGiver():
    def __init__(self, deck):
        self.deck = deck
        self.playerList = []
        self.P = 0
        self.encrypted = False

    def shuffleDeck(self):
        newDeck = self.deck
        for player in self.playerList:
            newDeck = player.encryptDeck(newDeck, self.P)
            
        print "shuffled"
        self.deck = newDeck
        self.encrypted = True

    def addPlayer(self, player):
        if not player in self.playerList:
            self.playerList.append(player)

    def giveCardToPlayer(self, player):
        if self.encrypted == False:
            self.shuffleDeck()

        playerIndex = self.playerList.index(player)
        card = self.deck.pop(0)
        if playerIndex != self.playerList.__len__()-1:
            i = playerIndex + 1
        else:
            i = 0
        print playerIndex, " > "
        while i != playerIndex:
            print "< ",i
            card = self.playerList[i].decryptCard(card, self.P)
            i = i+1
            if i == self.playerList.__len__():
                i = 0

        card = player.decryptCard(card, self.P)
        player.cards.append(card)

    def round(self):
        if self.playerList.__len__() < self.deck.__len__():
            for player in self.playerList:
                self.giveCardToPlayer(player)

        else:
            print "not enough cards left"


A = Player("A")
A.C = 17
# A.generateD(31)
B = Player("B")
B.C = 7
# B.generateD(31)
C = Player("C")
C.C = 23
# C.generateD(31)

Crupie = CardGiver([2,3,4,5,6])
Crupie.P = 31
Crupie.playerList = [A,B,C]
Crupie.round()

print A.cards
print B.cards
print C.cards 


# c = 23
# p = 31
# i = 1
# d = 0.1
# while 1:
#     d = ((i*(p-1))+1.00)/c
#     if ( c%d == c or d%c == d ) and d%p == d and d%1 == 0:
#         break
#     print d
#     i = i + 1 
# print d
