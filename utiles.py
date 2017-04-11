# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:50:20 2017

@author: Refaia
"""
import time
import math
import itertools

def continuedFractionListLen(num) :
    R = math.floor(math.sqrt(num))
    if R * R == num :
        return 0
    a = R
    P = 0
    Q = 1
    P = a * Q - P
    Q = (num - P * P) // Q
    a = (R + P) // Q
    counter = 1
    while Q != 1 :
        P = a * Q - P
        Q = (num - P * P) // Q
        a = (R + P) // Q
        counter += 1
    return counter

def continuedFractionList (num) :
    R = math.floor(math.sqrt(num))
    L = [R, []]
    if R * R == num :
        return L
    a = R
    P = 0
    Q = 1
    P = a * Q - P
    Q = (num - P * P) // Q
    a = (R + P) // Q
    L[1].append(a)
    while Q != 1 :
        P = a * Q - P
        Q = (num - P * P) // Q
        a = (R + P) // Q
        L[1].append(a)
    return L


def pythagoreanTriplets(limitP) :
    delta = time.time() 
    a, b, c = 0, 0, 0
    m = 2
    L = []
    for m in range(2, math.floor(math.sqrt(limitP))):
        for n in range(1, m) :
            if (math.gcd(n, m) == 1) and (n % 2 == 0 or m % 2 == 0) :
                a = (m * m - n * n)
                b = (2 * m * n)
                c = (m * m + n * n)
                if a + b + c > limitP :
                    break
                L.append((a, b, c))
    delta = time.time() - delta
    return L, delta



def gcdBinary(u, v):
    if u == 0: return v
    if v == 0: return u
    u = abs(u)
    v = abs(v)
    k = 1
    while u & 1 == 0 and v & 1 == 0:
        k <<= 1
        u >>= 1
        v >>= 1
    while u & 1 == 0:
        u >>= 1
    while v & 1 == 0:
        v >>= 1
    while v != 0:
        if u > v:
            u, v = v, u
        v = v - u
    return u*k


def gcd(a, b):
    while b != 0 :
        a, b = b, a % b
    return a


def powExp(x, n) :
    result = 1
    while n >= 1 :
        if n % 2 != 0 :
            result *= x
        x *= x
        n //= 2
    return result

        
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


def primeFactors(n):
    i = 2
    factors = set()
    if isPrime(n) :
        factors.add(n)
    else :
        while i * i <= n:
            if n % i != 0:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
    return factors     

def eulerTotient(n) :
    result = n 
    for prime in primeFactors(n) :
        result *= (1 - (1 / prime))
    return int(result)

def triangle(n):
    return (n**2 + n) // 2
def pentagonal(n) :
    return (3 * n**2 - n) // 2
def hexagonal(n) :
    return (2 * n**2) - n

def binarySearch(n, L) :
    upperBound = len(L) - 1
    lowerBound = 0
    found = False
    if n > L[upperBound] or n < L[lowerBound] :
        return False
    while not found and upperBound >= lowerBound :
        valueMid = L[(upperBound + lowerBound) // 2]
        if n == valueMid :
            found = True
        elif n > valueMid :
            lowerBound = ((upperBound + lowerBound) // 2) + 1
        else :
            upperBound = ((upperBound + lowerBound) // 2) - 1
    return found

