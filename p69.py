# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 12:11:13 2017

@author: Refaia
"""
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
    delta = time.time()
    maxResult = 3
    nMax = 6
    for n in range(10, 1000001) :
        tmp = (n / eulerTotient(n))
        if (maxResult) < tmp :
            maxResult = tmp
            nMax = n
    delta = time.time() - delta
    return maxResult, nMax, delta
        
print(main())
        
