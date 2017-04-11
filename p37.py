# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:34:18 2017

@author: Refaia
"""
import time

def is_prime(n, L) :
    if n in L :
        return True
    if n <= 1 :
        return False
    elif n <= 3 :
        L[n] = True
        return True
    elif n % 2 == 0 or n % 3 == 0 :
        return False
    i = 5
    while i * i <= n :
        if n % i == 0 or n % (i + 2) == 0 :
            return False
        i += 6
    L[n] = True
    return True


def remainPrimeLeft(n, L) :
    tmp = n
    while len(str(tmp)) > 1 :
       tmp = tmp % 10**(len(str(tmp)) - 1) 
       if not is_prime(tmp, L) :
           return False
    return True


def remainPrimeRight(n, L) :
    tmp = n
    while len(str(tmp)) > 1 :
       tmp = tmp // 10
       if not is_prime(tmp, L) :
           return False
    return True


def main() :
    delta = time.time()
    L = {2:True, 3:True}
    cpt = 11
    num = 11
    result = 0
    while cpt > 0 :
        if is_prime(num, L) :
            if remainPrimeLeft(num, L) and remainPrimeRight(num, L) :
                cpt -= 1
                result += num
        num += 2
    delta = time.time() - delta
    return result, delta
    
print(main())