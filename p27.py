# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:39:57 2017

@author: Refaia
"""
import time
import math

def isPrime(n) :
    if n <= 1 :
        return False
    if n <= 3 :
        return True
    if n % 2 == 0 or n % 3 == 0 :
        return False
    i = 5
    while i * i <= n :
        if n % i == 0 or n % (i + 2) == 0 :
            return False
        i += 6
    return True


def primeBelow(n):
    if n < 2:
        return 0
    primeList = []
    listNum = [2] + [i for i in range(3, n + 1, 2)]
    for i in range(1, int(math.sqrt(n)) + 1, 1): 
        if listNum[i] :
            for j in range(i + listNum[i], len(listNum), listNum[i]):
                listNum[j] = 0
    for i in range(len(listNum)):
        if listNum[i]:
            primeList.append(listNum[i])
    return primeList


def main() :
    delta = time.time()
    primeList = primeBelow(1000)
    aSave = 0
    bSave = 0
    maxCount = 0
    for b in primeList:
        for a in range(-999, 1000, 2):
            n = 0
            while isPrime((n**2) + (a * n) + b):
                n += 1
            if maxCount < n :
                maxCount = n
                aSave = a
                bSave = b
    delta = time.time() - delta
    return aSave, bSave, aSave * bSave, maxCount, delta
            

print(main())

