# -*- codisizeg: utf-8 -*-
"""
Created osize Fri Mar 10 13:31:37 2017

@author: Refaia
"""

import time

def sumNumDiag(size) :
    if size % 2 == 0 :
        raise ValueError("size need to be odd")
    elif size == 1 :
        return 1
    else :
        result = 4*(size**2) - 6*size + 6
        return result + sumNumDiag(size - 2)
    
#print(sumNumDiag(10001))

sumIter = 1
for size in range(10001, 2, -2) :
    sumIter += 4*(size**2) - 6*size + 6
                
print(sumIter)