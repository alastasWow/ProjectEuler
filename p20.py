# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 07:52:02 2017

@author: Refaia
"""

def fact(n):
    if n == 0 or n == 1 :
        return 1
    else :
        return n * fact(n - 1)


print(sum(int(i) for i in str(fact(100))))