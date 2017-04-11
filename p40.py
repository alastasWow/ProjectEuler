# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 19:49:52 2017

@author: Refaia
"""

import time

def position(n) :
    if n < 10 :
        return n
    lowerBound = 9
    prevLowBound = 0
    i = 2
    while n > lowerBound :
        prevLowBound = lowerBound + 1 
        lowerBound += (9 * (10**(i - 1))) * i 
        i += 1
    i -= 1
    tmp = n - prevLowBound
    return int(str((10**(i - 1)) + (tmp // i))[tmp % i])


def main() :
    delta = time.time()
    result = position(1) * position(10) * position(100) * position(1000) * position(10000) * position(100000) * position(1000000)
    delta = time.time() - delta
    return result, delta

print(main())
    
    