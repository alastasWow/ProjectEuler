# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 23:58:20 2017

@author: Refaia
"""

import time

def main() :
    count = 0 
    n = 1
    delta = time.time()
    while True :
        tmp = count
        for i in range(1, 10):
            if len(str(i**n)) == n :
                count += 1
        if tmp == count :
            break
        n += 1
    delta = time.time() - delta
    return count, delta

print(main())
