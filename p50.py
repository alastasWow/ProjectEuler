# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 08:24:04 2017

@author: Refaia
"""


import time

def primeBelow(n):
    if n < 2:
        return 0
    primeList = []
    listNum = [2] + [i for i in range(3, n, 2)]
    for i in range(1, int(math.sqrt(n)) + 1, 1): 
        if listNum[i] :
            for j in range(i + listNum[i], len(listNum), listNum[i]):
                listNum[j] = 0
    for num in listNum :
         if num :
            primeList.append(num)
    
    return primeList

def isPrime(n) :
    if n <= 1 :
        return False
    if n <= 3 :
        return True
    if n % 2 == 0 or n % 3 == 0 :
        return False
    i = 5
    while i * i <= n :
        if n % i == 0 or n % (i + 2) == 0 :
            return False
        i += 6
    return True

def main() :
    delta = time.time()
    n = 1000000
    listPrime = primeBelow(n)
    maxCount = 0
    maxResult = 0
    index = 0
    while index < len(listPrime) - 1:
        result = 0
        count = 0
        tmpIndex = index
        add = 0
        while add < n :
            add += listPrime[tmpIndex]
            #print (add - listPrime[tmpIndex],' + ', listPrime[tmpIndex], ' = ', add)
            tmpIndex += 1
            if isPrime(add) and (add < n) :
                result = add
                count = tmpIndex - index
                #print(result, count)
        if count > maxCount :
            maxCount = count
            maxResult = result
        index += 1
    delta = time.time() - delta
    return maxResult, maxCount, delta

print(main())