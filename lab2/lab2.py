# -*- coding:utf-8 -*-
# схема разделения секрета

import random


class Participant():
    def __init__(self, name):
        self.name = name
        self.part = ""
        self.parts = dict()

class Group():
    def __init__(self, participants=[]):
        self.participants = participants
        g_name = ""
        for p_name in participants:
            g_name = g_name + p_name.name
        self.name = g_name

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
        n = self.group.participants.__len__()

        if( i<=n):
            count = bin(self.secret).__len__() - 2
            # print count
            i1 = pow(2,count-1) + 1
            i2 = pow(2,count) - 1
            # print str(i1)+" "+str(i2)
            sx = random.randrange(i1, i2, 2)
            print str(sn)+" xor "+str(sx)
            
            sni = sn.__xor__(sx)

            print sni.__str__() + " | " + sx.__str__()

            if i!=n:
                currentParticipant = self.group.participants[i-1]
                currentParticipant.part = sx.__str__()
                currentParticipant.parts[self.group.name] = sx.__str__()
            else:
                currentParticipant = self.group.participants[i-1]
                currentParticipant.part = sn.__str__()
                currentParticipant.parts[self.group.name] = sn.__str__()
            
            self.getPart(sni, i+1)
        else:
            print "done"

class Composer():
    def __init__(self,group):
        self.group = group
        self.secret = ""

    def compose(self):
        participants = self.group.participants
        result = int(participants[0].parts[self.group.name])
        i = 1
        while i<participants.__len__():
            result = result.__xor__(int(participants[i].parts[self.group.name]))
            i = i+1
        # for participant in participants:
        #     print participant.parts[self.group.name]
        #     result = result.__xor__(int(participant.parts[self.group.name]))
        #     print result
        print result

class Grouping():
    def __init__(self):
        self.group_list = []

    def addGroup(self, group):
        if group not in self.group_list:
            self.group_list.append(group)
        else:
            pass

    def delGroup(self, group):
        if group in self.group_list:
            self.group_list.remove(group)
        else:
            pass

    def checkGroup(self, group):
        c_group = group
        for x_group in self.group_list:
            if x_group != group:
                # print x_group, " |> ", c_group, " << ", self.group_list


                if c_group.participants.__len__() == x_group.participants.__len__():
                    pass
                elif c_group.participants.__len__() > x_group.participants.__len__():
                    xg_length = x_group.participants.__len__()
                    xgi = 0
                    while xgi < xg_length:
                        if x_group.participants[xgi] not in c_group.participants:
                            break
                        else:
                            xgi = xgi + 1

                    if xgi == xg_length:
                        self.delGroup(c_group)
                        return 0
                elif c_group.participants.__len__() < x_group.participants.__len__():
                    cg_length = c_group.participants.__len__()
                    cgi = 0
                    while cgi < cg_length:
                        if c_group.participants[cgi] not in x_group.participants:
                            break
                        else:
                            cgi = cgi + 1

                    if cgi == cg_length:
                        self.delGroup(x_group)
                        

    def optimize(self):
        for group in self.group_list:
            if group in self.group_list:
                self.checkGroup(group)

# A = Participant('A')
# B = Participant('B')
# C = Participant('C')
# D = Participant('D')
# E = Participant('E')
# # my_group = Group([A,B,C])
# # Ruler = Sender(1011, my_group)
# # Ruler.getPart()
# # print A.parts
# # print B.parts
# # print C.parts

# # Nyan = Composer(my_group)
# # Nyan.compose()

# my_group = Group([A,D])
# m1 = Group([A,C])
# m2 = Group([A,B])
# m3 = Group([D,E,A])
# m4 = Group([D,C,A])

# qq = Grouping()
# qq.addGroup(my_group)
# qq.addGroup(m1)
# qq.addGroup(m2)
# qq.addGroup(m3)
# qq.addGroup(m4)

# # qq.checkGroup(my_group)

# qq.optimize()

# print qq.group_list

# for group in qq.group_list:

#     Ruler = Sender(1011, group)
#     Ruler.getPart()
#     print "A: ", A.parts
#     print "B: ", B.parts
#     print "C: ", C.parts
#     print "D: ", D.parts
#     print "E: ", E.parts
    
#     Nyan = Composer(my_group)
#     Nyan.compose()
#     print "--------------"