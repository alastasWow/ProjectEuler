# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:06:52 2017

@author: Refaia
"""
import time
import itertools

primeList = [2, 3, 5, 7, 11, 13, 17]
perm = itertools.permutations([i for i in range(10)])

result = 0
delta = time.time()
for i in perm :
    numString = ''.join(map(str,i))
    subString = numString[1:4]
    propertyFound = True
    shift = 1
    for prime in primeList :
        if int(subString) % prime != 0 :
            propertyFound = False
            break
        subString = numString[1 + shift:4 + shift]
        shift += 1
    if propertyFound :
        result += int(numString)
delta = time.time() - delta
print(result, delta)
           