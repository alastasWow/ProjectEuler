# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 14:52:50 2017

@author: Refaia
"""
import math

def isPrime(p) :
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

def largestPrimeFactor(n) :
    largestPrime = 1
    num = n
    while num != 1 :
        if isPrime(num) :
            return num
        if num % 2 == 0 :
            largestPrime = max(largestPrime, 2)
            num = num // 2
        else :
            for i in range(3, int(math.sqrt(num)) + 1, 2):
                if isPrime(i) and num % i == 0 :
                    num = num // i
                    largestPrime = max(largestPrime, i)
                    break
    return largestPrime
print(largestPrimeFactor(600851475143))
