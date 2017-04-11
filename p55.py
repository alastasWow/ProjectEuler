# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:34:26 2017

@author: Refaia
"""
import time

def lychrel(n) :
    num = n
    lychrelB = True
    for count in range(50) :
        num += int(str(num)[::-1])
        if num == int(str(num)[::-1]) :
            lychrelB = False
            break
    return lychrelB
      
  
def main() :
    delta = time.time()
    countNum = 0 
    for num in range(10000):
        if lychrel(num) :
            countNum += 1
    delta = time.time() - delta
    return countNum, delta

print(main())
        