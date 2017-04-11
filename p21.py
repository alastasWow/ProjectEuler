# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 09:50:52 2017

@author: Refaia
"""
import time
import math

def sumDivisorsUnder(num) :
    result = 1
    for i in range(2, int(math.sqrt(num)) + 1) :
        if num % i == 0 :
            if i == num // i :
                result += i
            else :
                result += i + (num // i)
    return result

def isAmical(num) :
    return num != sumDivisorsUnder(num) and num == sumDivisorsUnder(sumDivisorsUnder(num))

result = 0
upperLimit = 10000
sumAmical = 0
delta = time.time()
for i in range(1, upperLimit):
    divisors = sumDivisorsUnder(i)
    if divisors > i :
        if isAmical(i) :
            sumAmical += i 
            if divisors < upperLimit :
                sumAmical += divisors
delta = time.time() - delta                
print(sumAmical, "found in", delta)
