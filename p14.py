# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 22:09:57 2017

@author: Refaia
"""
'''
import time

def collatzSeq(l, n):
    if n == 0 :
        return l
    l.append(n)
    if n == 1:
        return l
    if n % 2 == 0:
        
        return collatzSeq(l, n // 2)
    else :
        return collatzSeq(l, 3 * n + 1)

#print(collatzSeq([], 97))
n = 1000000
nums = [i for i in range(n)] 
maxCouple = (0,0)
delta = time.time()
for i in range(len(nums) - 1, -1, -1):
    if nums[i] != 0 :
        l = collatzSeq([], i)
        if maxCouple[0] < len(l):
            maxCouple = (len(l),i)
        for item in l :
            if item < n:
                nums[item] = 0

delta = time.time() - delta
print(maxCouple, delta)
'''
import time

def collatzSeqLen(dic, n):
    if n in dic :
        return dic[n]
    if n % 2 == 0:        
        dic[n] = 1 + collatzSeqLen(dic, n // 2)
    else :
        dic[n] = 1 + collatzSeqLen(dic, 3 * n + 1)
    return dic[n]

n = 1000000
dic = {0:0, 1:1, 2:2}
maxCouple = (0,0)
delta = time.time()
for i in range(0, n, 1):
    if i not in dic :
        l = collatzSeqLen(dic, i)
        if maxCouple[0] < l:
            maxCouple = (l, i)   
delta = time.time() - delta
print(maxCouple, delta)
