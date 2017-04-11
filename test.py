# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:50:20 2017

@author: Refaia
"""
import time
import itertools
import math

def primeFactors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors 

def eulerTotient(n) :
    result = n 
    for prime in primeFactors(n) :
        result *= (1 - (1 / prime))
    return int(result)

def main() :
    upperBound = 10**7
    ratio = 1
    nFinal = 0
    for n in range(2, upperBound) :
        tmp = eulerTotient(n)
        if set(str(n)) == set(str(tmp)) :
            if (n / tmp) < ratio :
                ratio = n / tmp
                nFinal = n
    return ratio, nFinal

print(main())