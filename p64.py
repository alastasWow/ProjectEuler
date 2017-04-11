# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 17:24:06 2017

@author: Refaia
"""
import time
import math

    

'''
def continuedFractionList (num) :
    R = math.floor(math.sqrt(num))
    L = [R, []]
    if R * R == num :
        return L
    a = R
    P = 0
    Q = 1
    P = a * Q - P
    Q = (num - P * P) // Q
    a = (R + P) // Q
    L[1].append(a)
    while Q != 1 :
        P = a * Q - P
        Q = (num - P * P) // Q
        a = (R + P) // Q
        L[1].append(a)
    return L


counter = 0
delta = time.time()
for i in range(2, 10001):
    tmp = continuedFractionList(i)
    if len(tmp) == 2 :
        if len(tmp[1]) % 2 == 1 :
            counter += 1
delta = time.time() - delta
print(counter, delta)

''' 
def continuedFractionListLen(num) :
    R = math.floor(math.sqrt(num))
    if R * R == num :
        return 0
    a = R
    P = 0
    Q = 1
    P = a * Q - P
    Q = (num - P * P) // Q
    a = (R + P) // Q
    counter = 1
    while Q != 1 :
        P = a * Q - P
        Q = (num - P * P) // Q
        a = (R + P) // Q
        counter += 1
    return counter

counter = 0
delta = time.time()
for i in range(2, 10001): 
    if continuedFractionListLen(i) % 2 == 1 :
        counter += 1
delta = time.time() - delta
print(counter, delta)
