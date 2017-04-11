# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 08:21:50 2017

@author: Refaia
"""
'''
f = """131, 673, 234, 103, 18
201, 96, 342, 965, 150
630, 803, 746, 422, 111
537, 699, 497, 121, 956
805, 732, 524, 37, 331"""
lines = f.split('\n')
'''

import time

delta = time.time()

f= open('p081_matrix.txt', 'r')
lines = f.read().split('\n')
f.close()

matrix = []
for i in range(len(lines)) :
    matrix.append(list(map(int, lines[i].split(','))))
    
paths = [[0 for i in range(len(matrix))] for i in range(len(matrix))] 

paths[len(matrix) - 1][len(matrix) - 1] = matrix[len(matrix) - 1][len(matrix) - 1] 

for i in range(len(matrix) - 2, -1, -1):
        paths[i][len(matrix) - 1] = matrix[i][len(matrix) - 1] + paths[i + 1][len(matrix) - 1]
        paths[len(matrix) - 1][i] = matrix[len(matrix) - 1][i] + paths[len(matrix) - 1][i + 1] 

for i in range(len(matrix) - 2, -1, -1):
    for j in range(len(matrix) - 2, -1, -1) :
        paths[i][j] = matrix[i][j] + min(paths[i][j + 1], paths[i + 1][j])
        
delta = time.time() - delta

print(paths[0][0], delta)
