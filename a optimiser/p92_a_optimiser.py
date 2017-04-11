# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 16:17:05 2017

@author: Refaia
"""
import time

def sumSquares(num) :
    return sum(int(i)**2 for i in str(num))


def firstTry() : 
    delta = time.time()
    index = 2
    upperLimit = 10000000
    count = 0
    while index <= upperLimit :
        num = index
        while (num != 1) and  num != 89 :
            num = sumSquares(num)
        if num == 89 :
            count += 1
        index += 1
    delta = time.time() - delta
    return count, delta


def secondTry() :
    delta = time.time()
    index = 2
    upperLimit = 10000000
    count = 0
    L_89 = set([58, 37, 16, 4, 20, 42, 145, 85, 89])
    L_1 = set([44, 32, 13, 10, 1])
    while index < upperLimit :
        num = index
        while (num not in L_89)  and (num not in L_1):
            num = sumSquares(num)
        if num in L_89 :
            L_89.add(index)
            count += 1
        else :
            L_1.add(index)
        index += 1
    delta = time.time() - delta
    return count, delta

def thirdTry() :
    delta = time.time()
    index = 2
    upperLimit = 10000000
    count = 0
    L_89 = set([89])
    L_1 = set([1])
    while index < upperLimit :
        num = index
        L = [num]
        while (num not in L_89)  and (num not in L_1):
            num = sumSquares(num)
            L.append(num)
        if num in L_89 :
            L_89.update(L)
            count += 1
        else :
            L_1.update(L)
        index += 1
    delta = time.time() - delta
    return count, delta

def main() :
    delta = time.time()
    index = 2
    upperLimit = 10000000
    count = 0
    L_89 = set([58, 37, 16, 4, 20, 42, 145, 85, 89])
    L_1 = set([44, 32, 13, 10, 1])
    while index < upperLimit :
        num = index
        while (num not in L_89)  and (num not in L_1):
            num = sumSquares(num)
        if num in L_89 :
            L_89.add(index)
            count += 1
        else :
            L_1.add(index)
        index += 1
    delta = time.time() - delta
    return count, delta

print(main())