# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:26:22 2017

@author: Refaia
"""

import time

def findAllSolutions1(p) :
    count = 0
    for var1 in range(2, p // 2):
        for var2 in range(1, p // 3):
            var3 = p - var1 - var2
            if (var1**2 + var2**2 == var3**2) :
                count += 1
    return count


def findAllSolutions2(p) :
    count = 0
    for a in range(1, p // 3):
        if p * (p - 2 * a) % (2 * (p - a)) == 0:
            count += 1
    return count

def main():
    maxSolutions = 0
    index = 0
    delta = time.time()
    for p in range(4, 1000, 2) :
        sol = findAllSolutions2(p)
        if sol > maxSolutions :
            maxSolutions = sol
            index  = p
    delta = time.time() - delta
    return index, maxSolutions, delta

print(main())



