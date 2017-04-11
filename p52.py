# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:42:31 2017

@author: Refaia
"""

import time



def sameDigit(x, y) :
    L1 = list(str(x))
    L2 = list(str(y))
    for digit in L2 :
        if digit not in L1 :
            return False
    return True
    
x =  1 
delta = time.time()
while not sameDigit(x, 2 * x) or not sameDigit(x, 3 * x) or not sameDigit(x, 4 * x) or not sameDigit(x, 5 * x) or not sameDigit(x, 6 * x) :
    x += 1
        
delta = time.time() - delta
print(x, delta)