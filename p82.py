# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 09:51:30 2017

@author: Refaia
"""
#    f = """131, 673, 234, 103, 18
#    201, 96, 342, 965, 150
#    630, 803, 746, 422, 111
#    537, 699, 497, 121, 956
#    805, 732, 524, 37, 331"""
#    lines = f.split('\n')

import time

def main() :
    delta = time.time()

    f= open('p082_matrix.txt', 'r')
    lines = f.read().split('\n')
    f.close()

    
    matrix = []
    
    for i in range(len(lines)) :
        matrix.append(list(map(int, lines[i].split(','))))
    costs = [0 for i in range(len(matrix))] 
  
    for i in range(len(matrix)) :
        costs[i] = matrix[i][len(matrix) - 1]

    for j in range(len(matrix) - 2, -1, -1):
        
        costs[len(matrix) - 1] += matrix[len(matrix) - 1][j]
        for i in range(len(matrix) - 2, -1, -1) :
            costs[i] = matrix[i][j] + min(costs[i + 1], costs[i])
        
        for i in range(1, len(matrix)) :
            costs[i] = min(matrix[i][j] + costs[i - 1], costs[i])
    
    delta = time.time() - delta
    return min(costs), delta
    
print(main())