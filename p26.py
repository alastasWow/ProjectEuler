# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 11:29:27 2017

@author: Refaia
"""
import time

def count(d) :
    r= 10 % d
    pos = 0 
    rests = {}
    while r not in rests and r != 0 :
        rests[r] = pos
        r = (10 * r) % d
        pos += 1
    if r == 0 :
        return 0
    else :
        return len(rests) - rests[r]

def main(upperLimit) :
    delta = time.time()
    result = 0    
    for i in range(2, upperLimit) :
        length = count(i)
        if length > result :    
            result = i
    delta = time.time() - delta
    return result, delta

print(main(1000))
