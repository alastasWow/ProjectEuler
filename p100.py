# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:55:34 2017

@author: Refaia
"""
import time
import math

n = 120
b = 85
delta = time.time()
#2b² - 2b - n² + n = 0
while(n < 10**12) :
    b, n = 3 * b + 2 * n - 2, 4 * b + 3 * n - 3
delta = time.time() - delta
print(b, n, delta) 


def main() :
    delta = time.time()
    r = 1
    rNext = 1
    x = 3
    b = 0
    while r + b < 10**12 :
        r = rNext
        tmp = math.sqrt(1 + (8 * r**2))
        if tmp % 2 != 0 :
            b = r + int((tmp + 1) // 2)
        rNext, x = x + 3 * r, 3 * x + 8 * r
    delta = time.time() - delta
    return b, b + r, delta

print(main())