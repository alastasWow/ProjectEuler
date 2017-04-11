# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 09:56:41 2017

@author: Refaia
"""

import time
import math


def wordValue(word) :
    
    result = 0
    for char in word[1:-1].lower() :
        result += ord(char) - 96
    return result
    

def main() :
    delta = time.time()
    f =  open('p042_words.txt','r')
    wordList = f.read().split(',')   
    maxWordLength = max(map(len, wordList)) 
    triangleNum = {(i**2 + i) // 2 for i in range(1, int(math.sqrt(26 * 2 * maxWordLength)) + 1) }
    cpt = 0
    for word in wordList :
        if wordValue(word) in triangleNum :
            cpt += 1
    delta = time.time() - delta
    return cpt, delta


print(main())