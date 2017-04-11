# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:49:42 2017

@author: Refaia
"""
import time
import itertools

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


def findPrime() :
    delta = time.time()
    for j in range(7, 0, -3):
        perm = itertools.permutations([i for i in range(j, 0, -1)])
        for num in perm :
            result = int(''.join(map(str,num)))
            if isPrime(result) :
                delta = time.time() - delta
                return result, delta
        

print(findPrime())