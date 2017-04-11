# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:07:35 2017

@author: Refaia
"""
import time


def valueOfLetter(letter) :
    return ord(letter) - 96


def valueOfWord(word) :
    tmp = word[1:-1].lower()
    return sum(map(valueOfLetter,tmp))
    


def main() :
    delta = time.time()
    file = open('p022_names.txt', 'r')
    words = file.read().split(',')
    words.sort()
    result = 0
    for i in range(1, len(words) + 1):
        result += valueOfWord(words[i - 1]) * i
    delta = time.time() - delta
    return result, delta
     
print(main())
