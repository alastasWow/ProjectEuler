# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 18:54:29 2017

@author: Refaia
"""

import math
import time

def isPalindrome(n) :
    strInt = str(n)
    if len(strInt) == 1 or len(strInt) == 0 :
        return True
    if strInt[0] == strInt[-1] :
        return isPalindrome(strInt[1:-1])
    else :
        return False

def findLargestPalindrome() :
    largestPalindrome = -math.inf
    delta = time.time()
    for i in range(999, 99, -1) :
        for j in range(i, 99, -1) :
            if isPalindrome(i * j) :
                largestPalindrome = max(i * j, largestPalindrome)
            
    delta = time.time() - delta
    print(delta)
    return largestPalindrome
            
def main() :
    print(findLargestPalindrome())
    
if __name__ == "__main__" :
    main()