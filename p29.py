# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:54:58 2017

@author: Refaia
"""
import time
'''
upperLimitB = 1001
upperLimitA = 1001
L = {}

  
delta = time.time()
for i in range(2,upperLimitA) :
    for j in range(2, upperLimitB) :
        if i ** j not in L:
            L[i ** j] = True   

delta= time.time() - delta
print(len(L), delta)     
'''
s = set()
delta = time.time()
for a in range(2, 1001):
	for b in range(2, 1001):
		s.add(a**b)
delta= time.time() - delta
print( len(s), delta)
