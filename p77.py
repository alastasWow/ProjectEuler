# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 16:32:19 2017

@author: Refaia
"""
import time
import math

def primeBelow(n):
    if n < 2:
        return 0
    primeList = []
    listNum = [2] + [i for i in range(3, n + 1, 2)]
    for i in range(1, int(math.sqrt(n)) + 1, 1): 
        if listNum[i] :
            for j in range(i + listNum[i], len(listNum), listNum[i]):
                listNum[j] = 0
    for prime in listNum :
        if prime :
            primeList.append(prime)
    return primeList

def main() :
    delta = time.time()
    target = 5000
    primes = primeBelow(1000)
    n = 10
    while True :
        ways = {0:1, 1:0}
        p = 0
        while primes[p] <= n :
            for i in range(primes[p], n + 1) :
                if i in ways :
                    ways[i] = ways[i] + ways[i - primes[p]]
                else :
                    ways[i] = ways[i - primes[p]]
            p += 1
        if ways[n] >= target :
            delta = time.time() - delta
            return ways[n], n, delta
        n += 1

print(main())