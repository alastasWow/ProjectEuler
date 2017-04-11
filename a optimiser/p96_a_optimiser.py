# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 08:48:04 2017

@author: Refaia
"""
import time



def notInRow(num, row, matrix) :
    for column in range(9) :
        if matrix[row][column] == str(num):
            return False
    return True
    
def notInColumn(num, column, matrix) :
    for row in matrix :
        if row[column] == str(num):
            return False
    return True


def notInBlock(num, row, column, matrix) :
    startBlockX = 3 * (row // 3)
    startBlockY = 3 * (column // 3)
    for x in range(startBlockX, startBlockX + 3, 1) :
        for y in range(startBlockY, startBlockY + 3, 1) :
            if matrix[x][y] == str(num) :
                return False
    return True      
    

def solved(position, matrix) :
    if position == 81 :
        return True
    row = position // 9
    column = position % 9
    if matrix[row][column] != str(0) :
        return solved(position + 1, matrix)
    for num in range(1, 10) :
        if notInBlock(num, row, column, matrix) and notInColumn(num, column, matrix) and notInRow(num, row, matrix):
            matrix[row] = matrix[row][:column] + str(num) + matrix[row][column + 1:] 
            if solved(position + 1, matrix) :
                return True
    matrix[row] = matrix[row][:column] + str(0) + matrix[row][column + 1:]
    

        
def main() :
    try :
        delta= time.time()
        f= open('p096_sudoku.txt', 'r')
        matrix = f.read().split('\n')
        f.close()
        matrix = [matrix[1 + (10 * i): 10 +(10 * i)] for i in range(50)]
        result = 0
        for i in range(len(matrix)) :
            print(i)
            solved(0, matrix[i])
            result += int(matrix[i][0][:3])
        delta = time.time() - delta
    except OSError :
        print('cannot open', 'p096_sudoku.txt')    
    return result, delta
print(main())