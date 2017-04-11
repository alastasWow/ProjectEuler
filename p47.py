# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:22:11 2017

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
    if isPrime(n) :
        factors.add(n)
    else :
        while i * i <= n:
            if n % i != 0:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
    return len(factors)


def main() :
    delta = time.time()
    firstPrime = 0
    pos = 2
    length = 4
    while True:
        if primeFactors(pos) == length and  primeFactors(pos + 1) == length and primeFactors(pos + 2) == length and primeFactors(pos + 3) == length :
            firstPrime = pos
            break
        pos += 1
    delta = time.time() - delta
    return firstPrime, delta


print(main())