# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 13:37:36 2017

@author: Refaia
"""


def add(var1, var2, amplitude):
    result = 0
    for i in range(var1, amplitude, var1):
        result += i
    for i in range(var2, amplitude, var2):
        if i % var1 != 0 :
            result += i
    return result

var1 = 3
var2 = 5
amplitude = 1000
print(add(var1, var2, amplitude))
'''
import time
result = 0 
delta = time.time()
for i in range(3, 100000000):
    if (i % 3 == 0) or (i % 5 == 0):
        result += i
delta = time.time() - delta
print('Delta2',delta)
print(result)
'''