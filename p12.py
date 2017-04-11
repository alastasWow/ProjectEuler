# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 07:52:02 2017

@author: Refaia
"""
import time
def numDivisorsLen(num):
    divisorsLen = 2
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            if i == num // i :
                divisorsLen += 1
            else :
                divisorsLen += 2
    return divisorsLen

numStop = 500
i = 1
c = (0, 0)
delta = time.time()
while c[1] < numStop :
    triangle = (i * (i + 1)) // 2
    length = numDivisorsLen(triangle)
    c = (triangle, length)
    i += 1
delta = time.time() - delta
print(c, delta)
