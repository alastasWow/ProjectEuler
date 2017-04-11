# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:51:26 2017

@author: Refaia
"""
import time

def distanceSquared(p, q) :
    assert isinstance(p, tuple) and isinstance(q, tuple), 'p or q not a tuple'
    return (p[0] - q[0])**2 + (p[1] - q[1])**2

def isRight(o, p, q) :
    distances = [distanceSquared(o, p), distanceSquared(o, q), distanceSquared(q, p)]
    distances.sort()
    return distances[0] + distances[1] == distances[2] 

def main() :
    upperBoundY = 50
    upperBoundX = 50
    count = 0
    delta = time.time()
    for yp in range(upperBoundY + 1) :
        for xp in range(1, upperBoundX + 1) :
            for yq in range(yp, upperBoundY + 1) :
                for xq in range(xp + 1) :
                    if (((xq, yq) != (0, 0)) and ((xp, yp) != (0, 0))) and (xq, yq) != (xp, yp) :
                        if isRight((0, 0), (xp, yp), (xq, yq)) :
                            count += 1
    delta = time.time() - delta
    return count, delta
print(main())