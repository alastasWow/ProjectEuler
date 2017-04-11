# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:30:46 2017

@author: Refaia
"""

import time
import math
'''
def primeBelow(n):
    
    if n % 2 == 0:
        return False
    else :
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True
    
def sumPrime(n) :
    result = 2
    delta = time.time()
    for i in range(3, n + 1, 2) :
        if isPrime(i) :
            result += i
    delta = time.time() - delta
    print(delta)
    return result

num = 2*(10**6)
print(sumPrime(num))
'''
'''
def primeBelow(n):
    sumPrime = 0
    if n < 2:
        return 0
    listNum = [False, False, True] + [True for i in range(3, n, 1)]
    delta = time.time()
    for i in range(2, int(math.sqrt(n)) + 1, 1): 
        if listNum[i] == True:
            for j in range(i**2 , n, i):
                listNum[j] = False
    for i in range(2, len(listNum)):
        if listNum[i] == True:
            sumPrime += i
    delta = time.time() - delta
    print(delta)
    return sumPrime

print(primeBelow(2000000))
'''

def primeBelow(n):
    if n < 2:
        return 0
    listNum = [2] + [i for i in range(3, n, 2)]
    delta = time.time()
    for i in range(1, int(math.sqrt(n)) + 1, 1): 
        if listNum[i] :
            for j in range(i + listNum[i], len(listNum), listNum[i]):
                listNum[j] = 0
    delta = time.time() - delta
    print(delta)
    return len(listNum)

print(primeBelow(200))
