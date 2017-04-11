# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 12:15:47 2017

@author: Refaia
"""

import time

def isPalindrome(x) :
    num = str(x)
    if len(num) == 1 or len(num) == 0 :
        return True
    if num[0] == num[-1] :
        return isPalindrome(num[1:-1])
    return False
    
sumNum = 0
delta = time.time()
for i in range(10**6) :
    if str(i) == str(i)[::-1] and str('{0:b}'.format(i)) == str('{0:b}'.format(i))[::-1]:
        sumNum += i
delta = time.time() - delta
print(sumNum, delta)

