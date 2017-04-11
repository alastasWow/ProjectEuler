# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 11:29:27 2017

@author: Refaia
"""
import time

def expo(x, n):
    r = 1
    while n:
        if n % 2 == 1:
            r *= x
        x *= x
        n //= 2
    return r


def main() :
    print(sum(i**i for i in range(1, 1001)) % 10**10)
    
if __name__ == '__main__' :
    main()