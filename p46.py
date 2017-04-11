# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:08:25 2017

@author: Refaia
"""
import math
import time

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

def main() :
    num = 35
    delta = time.time()
    result = 0
    while True :
        if isPrime(num) :
            num += 2
            continue
        canBeWritten = False
        for prime in range(3, num, 2):
            if isPrime(prime) :
                if (num - prime) % 2 == 0 :
                    if int(math.sqrt((num - prime) / 2)) == math.sqrt((num - prime) / 2) :
                        canBeWritten = True
                        break
        if not canBeWritten :
            result = num
            break
        num += 2
    delta = time.time() - delta
    return result , delta
'''
def primeBelow(n):
    if n < 2:
        return 0
    if n == 2 :
        return [2]
    primeList = []
    listNum = [2] + [i for i in range(3, n + 1, 2)]
    for i in range(1, int(math.sqrt(n)) + 1, 1): 
        if listNum[i] :
            for j in range(i + listNum[i], len(listNum), listNum[i]):
                listNum[j] = 0
    for num in listNum :
         if num :
            primeList.append(num)
    
    return primeList
    
def main() :
    num = 35
    delta = time.time()
    result = 0
    while True and num < 10000:
        L = primeBelow(num)
        if num in L :
            num += 2
            continue
        canBeWritten = False
        for prime in L:
            if (num - prime) % 2 == 0 :
                if int(math.sqrt((num - prime) / 2)) == math.sqrt((num - prime) / 2) :
                    canBeWritten = True
                    break
        if not canBeWritten :
            result = num
            break
        num += 2
    delta = time.time() - delta
    return result , delta
'''
print(main())
