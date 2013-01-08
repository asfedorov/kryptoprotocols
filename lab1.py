# -*- coding:utf-8 -*-

import random

def makeParts(m, n):

    count = bin(m).__len__() - 2

    i1 = pow(2,count-1) + 1
    i2 = pow(2,count) - 1

    i = 1
    for sx in range(n):
        sx = random.randrange(i1, i2, 2)
        print sx.__str__() + " | " + i.__str__()
        i = i + 1

def getPart(m, sn, n, i):

    if( i<=n):
        count = bin(m).__len__() - 2

        i1 = pow(2,count-1) + 1
        i2 = pow(2,count) - 1
        sx = random.randrange(i1, i2, 2)

        if( i==1 ):
            sni = m.__xor__(sx)
        else:
            sni = sn.__xor__(sx)

        print sni.__str__() + " | " + sx.__str__()

        getPart(m, sni, n, i+1)
    else:
        print "done"


# makeParts(32, 5)
getPart(12323212424554334523543352353,0,5,1)