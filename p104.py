# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 13:57:07 2017

@author: Refaia
"""
import time
import math

#If n is even then k = n/2:
#F(n) = [2*F(k-1) + F(k)]*F(k)
#
#If n is odd then k = (n + 1)/2
#F(n) = F(k)*F(k) + F(k-1)*F(k-1)
def fib(n, f) :
    if n in f :
        return f[n]
    if n == 0 :
        f[n] = 0
        return f[n]
    if n == 1 or n == 2 :
        f[n] = 1
        return f[n]
    if n % 2 == 0 :
        k = n // 2
        f[n] = fib(k,f) * (2 * fib(k - 1,f) + fib(k,f))
    else :
        k = (n + 1) // 2
        f[n] = (fib(k,f)**2) + (fib(k - 1,f)**2)
    return f[n]

def main() :
    delta = time.time() 
    n = 2750
    f = {}
    f_n_last = fib(n, f) % 10**9
    f_n_1_last = fib(n - 1, f) % 10**9
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while True :
        if sorted(str(f_n_last)) == digits :
            tmp = fib(n, f)
            tmp = tmp // 10**(math.ceil(math.log10(tmp)) - 9)
            if sorted(str(tmp)) == digits :
                delta = time.time() - delta
                return n, delta
        f_n_last, f_n_1_last, n = (f_n_last + f_n_1_last) % 10**9, f_n_last, n + 1
print(main())