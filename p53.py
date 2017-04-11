# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 09:25:58 2017

@author: Refaia
"""
import time

def factIter(n, L) :
    for i in range(1, n + 1) :
        L[i] = i * L[i - 1]
    return L


def combi(n, r, L) :
    return (L[n] // (L[r] * L[n - r]))


def count(upperLimit) :
    result = 0
    L = {0:1, 1:1}
    delta = time.time()
    L = factIter(upperLimit, L)
    for i in range(2, upperLimit + 1) :
        if combi(i, i//2, L) >= 10**6 :
            if i % 2 == 0 :
                result += 1
            else :
                result += 2
            j = 1
            num = 0
            while combi(i, (i//2 - j), L) >= 10**6 :
                num += 1
                j += 1
            result += 2 * (j - 1)
    delta = time.time() - delta
    return result, delta
  
                     
print(count(100))
