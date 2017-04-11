# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 13:05:49 2017

@author: Refaia
"""
import time 

def powExpRest(x, n, lastDigits) :
    result = 1
    while n >= 1 :
        if n % 2 != 0 :
            result = (result * x) % lastDigits
        x  = (x * x) % lastDigits
        n //= 2
    return result


def main() : 
    delta = time.time()
    lastDigits = 10000000000
    result = (28433 * powExpRest(2, 7830457, lastDigits) + 1) % lastDigits
    delta = time.time() - delta
    return result, delta
                 
print(main())
