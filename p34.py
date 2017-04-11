# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 10:16:32 2017

@author: Refaia
"""

import time

def factIter(x) :
    if x == 0 or x == 1 :
        return 1
    result = x
    for i in range(1, x) :
        result *= i
        
    return result

upperLimit = factIter(9) * 7 + 1
L = [factIter(i) for i in range(10)]


sumNum = 0
delta = time.time()
for i in range(10, upperLimit) :
    num = i
    sumFactDigit = 0
    while num > 0 :
        sumFactDigit += L[num % 10]
        num //= 10
        
    if sumFactDigit == i :
        sumNum += sumFactDigit
delta = time.time() - delta
print(sumNum, delta)
