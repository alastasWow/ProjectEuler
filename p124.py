# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 09:36:18 2017

@author: Refaia
"""
import time

def rad(limit) :
    L = [1 for i in range(limit + 1)] 
    for i in range(2, limit + 1) :
        if L[i] == 1 :
            for j in range(i, limit + 1, i) :
                L[j] *= i
    return L

def main() :
    delta = time.time()
    limit = 100000
    radList = rad(limit)
    L = [(i, radList[i]) for i in range(limit + 1)]
    L = sorted(L, key = lambda couple: couple[1])
    delta = time.time() - delta
    return L[10000][0], delta

print(main())