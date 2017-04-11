# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:18:46 2017

@author: Refaia
"""
import time
import math

def fact(n) :
    if n < 0 :
        raise ValueError('Negatif number')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(fact(-1))

def main() : 
    delta= time.time()
    setLength = 10
    setOfNum = [i for i in range(setLength)]
    numChosen = 1000000
    result = ""
    if(math.factorial(len(setOfNum)) > numChosen) :
        numOfPerm = 0
        while len(setOfNum) > 1 :
            numOfPermPerNumInSet = math.factorial(len(setOfNum)) // len(setOfNum)
            for j in range(1, len(setOfNum) + 1) :
                if (numOfPerm +  (numOfPermPerNumInSet * j)) >= numChosen :
                    break
            numOfPerm += numOfPermPerNumInSet  * (j - 1)
            result += str(setOfNum[j - 1])
            del(setOfNum[j - 1])
        delta = time.time() - delta
        return result + str(setOfNum[0]), delta
    else : 
        print("this set permutations do not reach that threshold")
        return 0
    
if __name__ == '__main__' :
    print(main())