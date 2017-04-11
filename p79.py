# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 15:53:59 2017

@author: Refaia
"""

import time

def main() :
    delta = time.time()
    f= open('p079_keylog.txt', 'r')
    keylogs = set(f.read()[:-1].split('\n'))
    digitPos = {}
    
    # finding numbers below (in position) the fixed one
    for num in keylogs :
        for i in range(len(num) - 1):
            if (num[i] not in digitPos) :
                digitPos[num[i]] = set(num[i + 1:] + ' ')
            else :
                digitPos[num[i]].update(list(num[i + 1:]))
            for digitBelow in num[i + 1:] :
                    if digitBelow in digitPos :
                        digitPos[num[i]].update(digitPos[digitBelow])
        if num[len(num) - 1] not in digitPos :
            digitPos[num[len(num) - 1]] = set(' ')
            
    # making  sure that all numbers are accounted for (useless in this problem)
    # exemple 3 : {1,5} and 5:{1,2} ==> 3 : {1,5,2}
    for digit in digitPos :
        size = len(digitPos[digit])
        for i in range(size)  :
            digitBelow = list(digitPos[digit])[i]
            if digitBelow != ' ' :
                digitPos[digit].update(digitPos[digitBelow])
                
    #arranging the numbers function of the numbers below them
    num = [0 for i in range(len(digitPos))] 
    for digit in digitPos :
        num[len(digitPos) - len(digitPos[digit])] = digit
            
    delta = time.time() - delta
    return int(''.join(num)), delta
    
print(main())
