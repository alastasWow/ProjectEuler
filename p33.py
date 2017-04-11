# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 11:13:23 2017

@author: Refaia
"""

import time

def gcd(a, b):
    while b != 0 :
        a, b = b, a % b
    return a

def reduce(x, y) :
    newX = str(x)
    newY = str(y)
    for i in str(x):
        if i in str(y):
            newY = str(y).replace(i,'',1)
            newX = str(x).replace(i,'',1)
    if newX == '' :
        newX = '1'
    if newY == '0' :
        newY = '1'
    return int(newX), int(newY)

def main() :
    delta = time.time()
    upperLimit = 100
    nonTrivialNums = []
    for i in range(2, upperLimit) :
        for j in range(1, i) :
            if j % 10 == 0 :
                continue
            x, y = reduce(j, i)
            if (j, i) == (x, y):
                continue
            if x / y == j / i :
                nonTrivialNums.append((j, i))
    resultX, resultY = 1, 1
    for couple in nonTrivialNums :
        resultX *= couple[0]
        resultY *= couple[1]
    denominator = resultY // gcd(resultX, resultY)
    delta = time.time() - delta
    return denominator, delta

print(main())


"""
BEST SOLUTION

def gcd(a, b):
    while b != 0 :
        a, b = b, a % b
    return a

denproduct = 1
nomproduct = 1
delta = time.time()
for i in range(3,10):
    for den in range(2, i) :
        for nom in range(1, den) :
            if ((nom * 10 + i) * den == nom * (i * 10 + den)) :
                denproduct *= den
                nomproduct *= nom
denproduct /= gcd(nomproduct, denproduct)
delta = time.time() - delta
print(denproduct, delta)
"""
            
