# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:16:20 2017

@author: Refaia
"""
import time 

def pandigital_1_9(n) :
    if len(str(n)) != 9 :
        return False
    for i in range(1, 10) :
        if str(i) not in str(n):
            return False
    return True


def main() :
    delta = time.time() 
    largestNum =  918273645
    num = 9
    while num < 10000 :
        if str(num)[0] == '9':
            concat = ''
            n = 1
            while len(concat) < 9 :
                concat += str(num * n)
                n += 1
            if pandigital_1_9(concat) :
                if int(concat) > largestNum :
                    largestNum = int(concat)
        num += 1
    delta = time.time() - delta
    return largestNum, delta

print(main())