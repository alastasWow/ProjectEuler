# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 08:22:52 2017

@author: Refaia
"""
import time

def oddDigits(num) :
    while num != 0 :
        if num % 2 == 0 :
            return False
        num //=10
    return True

def main() :
    delta = time.time()
    upperBound = 10**9
    result = 0
    for n in range(1, upperBound) :
        if n % 10 == 0  :
            continue
        reverse = str(n)[::-1]
        if oddDigits(n + int(reverse)) :
            result += 1
    delta = time.time() - delta
    return result, delta

print(main())