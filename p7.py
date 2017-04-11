# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 20:08:20 2017

@author: Refaia
"""
'''
import math
index = 10001
indexResult = 0
i = 3
primeList = [2] 
while indexResult < index - 1  : 
    for item in primeList  :
        if item >= (int(math.sqrt(i)) + 1) :
            primeList.append(i)
            indexResult += 1
            break
        if i % item == 0 :
            break
        if item == primeList[-1] and i % item != 0 :
            primeList.append(i)
            indexResult += 1
    i += 2 
print(primeList[indexResult])
'''
import math
def prime(n):
    if n == 2 :
        return True
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

indexResult = 3
index = 10001
i = 0
while i < index - 1:
  if prime(indexResult):
    i += 1
  indexResult += 2
print(indexResult - 2)