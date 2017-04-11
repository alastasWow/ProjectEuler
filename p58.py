# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:36:53 2017

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


def matrix(n) :
    primesOnDiag = 0
    for i in range(1, 4):
        if isPrime(n**2 - i * (n - 1)) :
            primesOnDiag += 1
    return primesOnDiag
    
def main() :
    numOnDiag = 13
    primeOnDiag = 8
    size = 9
    delta = time.time()
    while ((primeOnDiag / numOnDiag) > 0.1) :
        primeOnDiag += matrix(size)
        numOnDiag +=4
        size += 2
    delta = time.time() - delta
    return size - 2, delta

print(main())