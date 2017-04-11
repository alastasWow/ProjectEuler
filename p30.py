# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 11:45:04 2017

@author: Refaia
"""
import time

def pow1(x, n) :
    result = 1
    while n > 0 :
        if n % 2 != 0 :
            result *= x
        x *= x
        n //= 2
    return result


def main() :
    delta = time.time()
    L = [pow1(i, 5) for i in range(10)]
    upperlimit = (9**5) * 6 + 1
    sumNum = 0
    for i in range(10, upperlimit) :
        num = i
        sumPowDigit = 0
        while(num > 0) :
            sumPowDigit += L[num % 10]
            num //= 10
        if sumPowDigit == i :
            sumNum += i
    delta = time.time() - delta
    return sumNum, delta

if __name__ == '__main__' :
    print(main())
              
            