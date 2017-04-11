# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 17:13:54 2017

@author: Refaia
"""
import time

def main() :
    delta = time.time()
    a, b = 3, 2
    counter = 0
    for i in range(1, 1001) :
        a, b = a + 2 * b, a + b
        if len(str(a)) > len(str(b)) :
            counter += 1
    delta = time.time() - delta
    return counter, delta
    
print(main())

#s= 1 + 1 / (1 + s)

'''
def gcd(a, b) :
    while b > 0 :
        a, b = b, a % b
    return a

def add(n1, d1, n2, d2):
    assert (type(n1) == int and type(d1) == int and type(n2) == int and type(d2) == int)
    d = gcd((d2 * n1) + (d1 * n2), d1 * d2)
    return ((d2 * n1) + (d1 * n2)) // d, (d1 * d2) // d

def div(n1, d1, n2, d2) :
    assert (type(n1) == int and type(d1) == int and type(n2) == int and type(d2) == int)
    d = gcd(n1 * d2, d1 * n2)
    return n1 * d2 // d , d1 * n2 // d 
    
def main() :
    delta = time.time()
    upperBound = 1001
    i = 1
    L = [(1,1)]
    sn, sd = 0, 0
    counter = 0
    while i < upperBound :
        sn, sd = add(1, 1, L[i - 1][0], L[i - 1][1])
        sn, sd = div(1, 1, sn, sd)
        sn, sd = add(1, 1, sn, sd)
        L.append((sn, sd))
        if len(str(sn)) > len(str(sd)) :
            counter += 1
        i += 1
    delta = time.time() - delta
    return counter, delta
'''