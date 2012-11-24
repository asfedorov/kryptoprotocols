# -*- coding:utf-8 -*-
# схема разделения секрета

import random


class Participant():
    def __init__(self, name):
        self.name = name
        self.part = ""

class Group():
    def __init__(self, participants=[]):
        self.participants = participants

# класс раздающего. при инициализации передаётся секрет и группа
class Sender():
    def __init__(self, secret, group):
        self.group = group
        self.secret = secret
        # self.n = group.__len__()

    # функция получения части секрета.
    # sn - предыдущая часть секрета. для первого участника - секрет
    # i - которому участнику выдаётся часть секрета сейчас
    def getPart(self, sn="", i=1):
        if sn=="": sn = self.secret
        n = self.group.__len__()
        if( i<=n):
            count = bin(self.secret).__len__() - 2

            i1 = pow(2,count-1) + 1
            i2 = pow(2,count) - 1
            sx = random.randrange(i1, i2, 2)

            
            sni = sn.__xor__(sx)

            print sni.__str__() + " | " + sx.__str__()
            
            currentParticipant = self.group[i-1]
            currentParticipant.part = sni.__str__()
            
            self.getPart(sni, i+1)
        else:
            print "done"


# получить часть 
def getPart(sn, n, i):

    if( i<=n):
        count = bin(sn).__len__() - 2

        i1 = pow(2,count-1) + 1
        i2 = pow(2,count) - 1
        sx = random.randrange(i1, i2, 2)

        
        sni = sn.__xor__(sx)

        print sni.__str__() + " | " + sx.__str__()

        getPart(sni, n, i+1)
    else:
        print "done"


# makeParts(32, 5)

# getPart(12323212424554334523543352353,5,1)


A = Participant('A')
B = Participant('B')
C = Participant('C')
Ruler = Sender(12323212424554334523543352353, [A,B,C])
Ruler.getPart()
print A.part