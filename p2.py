# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 14:03:46 2017

@author: Refaia
"""
import time



result = 0
u_n_2 = 1
u_n_1 = 1
u_n = 0
delta = time.time()
while u_n < 4 * (10**1000) :
    u_n = u_n_1 + u_n_2
    u_n_2 = u_n_1
    u_n_1 = u_n
    if u_n % 2 == 0 :
        result += u_n  
delta = time.time() - delta
print(result,"\n\n", delta)