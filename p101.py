# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 13:31:31 2017

@author: refaia
"""

import numpy

def lagrangePoly(i, xs):
    num = numpy.array([1.])
    denom = 1
    for j in range(0, len(xs)):
        if j == i:
            continue
        else:
            num, denom = numpy.convolve(num, [1, -xs[j]]), denom * (xs[i] - xs[j])
    return num / denom
    
def main():
    coefs = numpy.array([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])
    i = 1
    xs = []
    ys = []
    result = 0
    while True:
        if i >= len(coefs):
            break
        xs.append(i)
        ys.append(sum(coefs[j] * i**(len(coefs) - 1 - j) for j in range(len(coefs) - 1, -1, -1)))
        op = numpy.array([0. for m in range(len(xs))])
        for k in range(len(xs)):
            op += ys[k] * lagrangePoly(k, xs)
        print('op', op)
        result += sum(op[j] * (i + 1)**(len(op) - 1 - j) for j in range(len(op) - 1, -1, -1))
        i += 1
    print('result', numpy.ceil(result))    
main()
