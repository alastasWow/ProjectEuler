# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 18:11:12 2017

@author: Refaia
"""
import time

def nbRectangles(n, m) :
    return n * m * (n + 1) * (m + 1) // 4

def main() :
    delta = time.time()
    n = 1
    target = 20
    while target >= nbRectangles(n, n) :
        n+= 1
    m = n
    L = {}
    for count in range(m**2) :
        L[(abs(target - nbRectangles(n, m)))] = (n, m)
        if nbRectangles(n, m) > target :
            m -= 1
        elif nbRectangles(n, m) < target :
            n += 1
    delta = time.time() - delta   
    return L[min(L.keys())], L[min(L.keys())][0] * L[min(L.keys())][1], delta
    
print(main())

