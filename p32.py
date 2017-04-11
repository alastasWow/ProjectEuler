# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:27:40 2017

@author: Refaia
"""

import time


def pandigitalMult(i, j) :
    L1 = list(str(i))
    L2 = list(str(j))
    L3 = list(str(i * j))
    L4 = set(L1 + L2 + L3)
    return len(L4) == 9 and '0' not in L4

     
i = 99
j = 1    
L = set()
delta = time.time()
while len(str(i)) + len(str(j)) + len(str(i * j)) < 10:
    while len(str(i)) + len(str(j)) + len(str(i * j)) < 10:
        if len(str(i)) + len(str(j)) + len(str(i * j)) != 9 :
            j += 1
            continue
        else :
            if pandigitalMult(i, j) :
                L.add(i * j)
            j += 1
    i += 1
    j = 1
delta = time.time() - delta
print(sum(L), delta)