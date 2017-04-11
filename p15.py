# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:01:57 2017

@author: Refaia
"""
import time 

def choices(matrix, size):
    delta = time.time()
    for i in range(0, size + 1):
        matrix[i][size] = 1
        matrix[size][i] = 1
    for i in range(size - 1, -1, -1) :
        for j in range(size - 1, -1, -1) :
            matrix[i][j] = matrix[i + 1][j] + matrix[i][j + 1] 
    delta = time.time() - delta
    return matrix[0][0], delta

size = 20    
matrix = [[0 for i in range(size + 1)] for i in range(size + 1)]
print(choices(matrix, size))
