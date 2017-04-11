# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 16:18:49 2017

@author: Refaia
"""

def squaredSum(i) :
    result = 0
    for j in range(i + 1) :
        result += j
    return result**2
    

def sumOfSquares(i):
    if i == 1:
        return i
    return i**2 + sumOfSquares(i - 1)

n = 100
print(squaredSum(n) - sumOfSquares(n))