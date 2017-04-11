# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 17:47:47 2017

@author: Refaia
"""

import time
import math


def solDiophantine (num) :
    R = math.floor(math.sqrt(num))
    L = [R, []]
    if R * R == num :
        return L
    a = R
    P = 0
    Q = 1
    P = a * Q - P
    Q = (num - P * P) // Q
    a = (R + P) // Q
    L[1].append(a)
    while Q != 1 :
        P = a * Q - P
        Q = (num - P * P) // Q
        a = (R + P) // Q
        L[1].append(a)
        
    j = 1
    const = j * len(L[1])
    while True :
        i = const - 2
        n, d = 1, L[1][i % len(L[1])]
        while i > 0 :
            i -= 1
            n, d = d, n + d * L[1][i % len(L[1])]
        n, d = d * L[0] + n, d
        if (n*n) - (num * (d**2)) == 1 :
            return n, d
        j += 1
        const *= j
        

def main() :
    delta = time.time()
    maxX, D = 0, 0
    upperBound = 1001
    for d in range(2, upperBound) :
        if math.floor(math.sqrt(d)) * math.floor(math.sqrt(d)) != d : 
            sol = solDiophantine(d) 
            if sol[0] > maxX :
                maxX, D = sol[0], d
    delta = time.time() - delta
    return maxX, D, delta

print(main())
          
    