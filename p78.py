# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 19:35:14 2017

@author: Refaia
"""
import time
#euler formula
def countWays(n, L) :
    result = 0
    tmp = (1 + 24 * n)**0.5
    boundInf = int((1 - tmp) / 6)
    boundSup = int((1 + tmp) / 6)
    pentagonal_k = ((3 * boundInf**2) - boundInf) // 2
    for k in range(boundInf, boundSup + 1) :
        if k != 0 :
            result += (1 if k % 2 == 1 else -1) * L[n - pentagonal_k] 
        pentagonal_k += (3 * k) + 1
    return result % 1000000

def main() :
    delta = time.time()
    L= [1]
    i = 1
    while True :
        L.append(countWays(i,L))
        if L[-1] == 0 :
            delta= time.time() - delta
            return i, delta
        i += 1
    
print(main())

