# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:24:22 2017

@author: Refaia
"""

import time
import math

def pentagonal(n) :
    return (n * ((3 * n) - 1)) // 2


def isPentagonal(n):
    squareRoot = (math.sqrt(1 + 24 * n) + 1.0) / 6.0
    return squareRoot == int(squareRoot) 


def main() :
    delta = time.time()
    n = 2
    found = False
    while not found :
        p_n = (n * ((3 * n) - 1)) // 2
        for k in range(n - 1, 0, - 1) :
            p_k = (k * ((3 * k) - 1)) // 2
            d = p_n - p_k
            s = p_k + p_n
            if  isPentagonal(s) and isPentagonal(d) :
                result = d
                found = True
        n += 1
    delta = time.time() - delta
    return result, delta

print(main())