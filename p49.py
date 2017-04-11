# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 15:37:46 2017

@author: Refaia
"""

import time
import math
import itertools

def primeBelow(upperBound, lowerBound = 0):
    if upperBound < 2:
        return 0
    primeList = []
    listNum = [2] + [i for i in range(3, upperBound + 1, 2)]
    for i in range(1, int(math.sqrt(upperBound)) + 1, 1): 
        if listNum[i] :
            for j in range(i + listNum[i], len(listNum), listNum[i]):
                listNum[j] = 0
    for prime in listNum :
        if prime and prime >= lowerBound:
            primeList.append(prime)
    return primeList


def permutationsIn(L) :
    listOfPermutLists= []
    for prime in L :
        permutList = list(itertools.permutations(str(prime)))
        permutListOfNum = [prime]
        for permutNum in permutList :
            num = int(''.join(permutNum))
            if (num in L) and (num not in permutListOfNum) :
                permutListOfNum.append(num)
                L.remove(num)
        if len(permutListOfNum) > 2 :
            permutListOfNum.sort()
            listOfPermutLists.append(permutListOfNum)
    return listOfPermutLists



def main() :
    delta = time.time()
    primeList = primeBelow(9999, 1000)
    L = permutationsIn(primeList)
    posList = []
    for i in range(len(L)) :
        for j in range(len(L[i]) - 2) :
            for k in range(j + 1, len(L[i])) :
                m = (2 * L[i][k] - L[i][j]) 
                if m in L[i] :
                    posList.append(str(L[i][j]) + str(L[i][k]) + str(m))
                if len(posList) == 2 :
                    delta = time.time() - delta
                    return posList[-1], delta
print(main())                    



'''
def binarySearch(n, L) :
    upperBound = len(L) - 1
    lowerBound = 0
    found = False
    if n > L[upperBound] or n < L[lowerBound] :
        return False
    while not found and upperBound >= lowerBound :
        valueMid = L[(upperBound + lowerBound) // 2]
        if n == valueMid :
            found = True
        elif n > valueMid :
            lowerBound = ((upperBound + lowerBound) // 2) + 1
        else :
            upperBound = ((upperBound + lowerBound) // 2) - 1
    return found

def isPermut(n, m) :
    nString = str(n)
    mString = str(m)
    if len(nString) != len(mString) :
        return False
    for i in nString :
        if i not in mString :
            return False
        else :
            mString = mString.replace(i, '', 1)
    return True
 
    
    
def main():
    delta = time.time()
    primeList = primeBelow(9999, 1000)
    L = []
    for i in range(len(primeList)) :
        for j in range(i + 1, len(primeList))  :
            numk = primeList[j] + primeList[j] - primeList[i]
            if binarySearch(numk, primeList) :
                if isPermut(primeList[j], primeList[i]) and isPermut(primeList[j],numk) :
                    L.append( str(primeList[i]) + str(primeList[j]) + str(numk))
                if len(L) == 2 :
                    delta = time.time() - delta
                    return L[-1], delta
    
print(main())
'''