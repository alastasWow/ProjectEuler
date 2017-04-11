# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:03:32 2017

@author: Refaia
"""
import time
import math

def triangle(n):
    return (n**2 + n) // 2
def pentagonal(n) :
    return (3 * n**2 - n) // 2
def hexagonal(n) :
    return (2 * n**2) - n

def main() :
    delta = time.time()
    n = 2
    tph = 0
    counter = 2
    while counter > 0 :
        num = (2 * n**2) - n
        squareRoot = math.sqrt(1 + 24 * num)
        if squareRoot == int(squareRoot) and (int(squareRoot) % 6 == 5) :
            tph = num
            print('Found !!!', n, tph)
            counter -= 1
        n += 1
    delta = time.time() - delta
    return tph, delta

print(main())
