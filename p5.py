# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 16:31:15 2017

@author: Refaia
"""
import time
import math

def pgcdCouple(a, b):
    a_bis = max(a, b)
    b_bis = min(a, b)
    if a_bis % b_bis == 0:
        return b_bis
    return pgcdCouple(b_bis, a_bis % b_bis)

def ppcmCouple(a,b):
    return a * b // pgcdCouple(a, b) 

def ppcm(listNum):
    if len(listNum) == 0 :
        return math.inf
    elif len(listNum) == 1 :
        return listNum[0]
    elif len(listNum) == 2 :
        return ppcmCouple(listNum[0],listNum[1])
    elif len(listNum) > 2 :
        return ppcmCouple(ppcmCouple(listNum[0],listNum[1]),ppcm(listNum[2:]))
        
dividers = [11, 13, 16, 17, 19, 2520]
#12 = 4 * 3 Prime(4, 3) = 1 ==> 2520 % 12 == 0
#14 = 7 * 2 Prime(7, 2) = 1 ==> 2520 % 14 == 0
#15 = 5 * 3 ...
#18 = 9 * 2 ...
#20 = 5 * 4 ...
print(ppcm(dividers))


'''
l = [11, 13, 16, 17, 19, 23]
#12 = 4 * 3 Prime(4, 3) = 1
#14 = 7 * 2 Prime(7, 2) = 1
#15 = 5 * 3
#18 = 9 * 2
#20 = 5 * 4
num = 2520
found = False
delta = time.time()
while not found :
    for div in l:
        if num % div != 0:
            num += 2520
            break
        elif div == l[-1] and num % l[-1] == 0:
            found = True
delta = time.time() - delta
print(num)
print(delta)
'''
