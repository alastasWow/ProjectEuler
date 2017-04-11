# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:47:52 2017

@author: Refaia
"""
import time 
import math


def countWays(n, L) :
    result = 0
    tmp = (1 + 24 * n)**0.5
    boundInf = int((1 - tmp) / 6)
    boundSup = int((1 + tmp) / 6)
    pentagonal_k = ((3 * boundInf**2) - boundInf) // 2
    for k in range(boundInf, boundSup + 1) :
        if k != 0 :
            result += (1 if k % 2 else -1) * L[n - pentagonal_k] 
        pentagonal_k += (3 * k) + 1
    return result


def main() :
    delta = time.time()
    L= [1]
    target = 100
    for i in range(1, target + 1) :
        L.append(countWays(i,L))
    delta = time.time() - delta
    return L[target], delta

print(main())
