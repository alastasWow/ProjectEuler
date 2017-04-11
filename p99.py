# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 19:25:13 2017

@author: Refaia
"""
import time
import math 

def main() :
    delta = time.time()
    f = open('p099_base_exp.txt', 'r')
    maxValue = 0
    numLineMaxValue = 0
    numLine = 0
    for line in f :
        numLine += 1
        b, e = line.split('\n')[0].split(',')
        localValue = int(e) * math.log10(int(b))
        if localValue > maxValue :
            maxValue = localValue
            numLineMaxValue = numLine
    f.close()
    delta = time.time() - delta
    return numLineMaxValue, delta
    
print(main())