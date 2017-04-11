# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:13:58 2017

@author: Refaia
"""
'''
import math
import time

def isAbundant(num) :
    def sumDivisorsUnder(num) :
        result = 1
        for i in range(2, int(math.sqrt(num)) + 1) :
            if num % i == 0 :
                if i == num // i :
                    result += i
                else :
                    result += i + (num // i)
        return result
    return sumDivisorsUnder(num) > num

def main() : 
    
    delta = time.time()
    upperLimit = 28124
    abundantNums = [] 
    for i in range(12, upperLimit) :
        if isAbundant(i) : 
            abundantNums.append(i)
                        
    sumOf2AbundantNums = [False for i in range(upperLimit)]
    for i in range(0, len(abundantNums)) :
        for j in range(0, len(abundantNums)) :
            if abundantNums[i] + abundantNums[j] < upperLimit :
                sumOf2AbundantNums[abundantNums[i] + abundantNums[j]] = True
    
    sumNotAbundant = 12 * 23 
    
    delta1 = time.time()
    for i in range(24,  upperLimit) :
        if sumOf2AbundantNums[i] == False :
            sumNotAbundant += i
    delta = time.time() - delta
    delta1 = time.time() - delta1
    print(sumNotAbundant, 'Total time:', delta,'// Sum time:', delta1) 


if __name__ == '__main__' :
    main()   



'''
import math
import time

def isAbundant(num) :
    def sumDivisorsUnder(num) :
        result = 1
        for i in range(2, int(math.sqrt(num)) + 1) :
            if num % i == 0 :
                if i == num // i :
                    result += i
                else :
                    result += i + (num // i)
        return result
    return sumDivisorsUnder(num) > num


def sumOf2Abundant(abundantNums, num) :
    if num % 2 == 0 :
        if abundantNums[num // 2] :
            return True
    for i in range(1, (num // 2) + 1) :
        if abundantNums[i] and abundantNums[num - i] :
            return True
    return False
         
   
def main() : 
    delta = time.time()
    upperLimit = 28124
    abundantNums = [False for i in range(upperLimit)]
    for i in range(12, upperLimit) :
        if isAbundant(i) : 
            abundantNums[i] = True

    sumNotAbundant = 12 * 23 # 1 + ... + 23
    
    delta1 = time.time()
    for i in range(24,  upperLimit) :
        if not sumOf2Abundant(abundantNums, i) :
            sumNotAbundant += i
    delta1 = time.time() - delta1
    delta = time.time() - delta
    print(sumNotAbundant, 'Total time:', delta,'// Sum time:', delta1)

if __name__ == '__main__' :
    main() 
          
