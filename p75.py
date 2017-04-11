# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:01:04 2017

@author: Refaia
"""
import time
import math



def main() : 
    limitP = 15*(10**5)
    delta = time.time() 
    a, b, c = 0, 0, 0
    m = 2
    ways = [0 for i in range(limitP + 1)]
    for m in range(2, math.floor(math.sqrt(limitP)) + 1):
        for n in range(1, m) :
            if (math.gcd(n, m) == 1) and (n % 2 == 0 or m % 2 == 0) :
                a = (m * m - n * n)
                b = (2 * m * n)
                c = (m * m + n * n)
                if a + b + c > limitP :
                    break
                s = sum((a, b, c))
                for i in range(s, len(ways), s) :
                    ways[i] += 1
    result = ways.count(1)
    delta = time.time() - delta
    return result, delta


print(main())


