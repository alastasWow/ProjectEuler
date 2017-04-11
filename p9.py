# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 07:48:04 2017

@author: Refaia
"""

import time

def findNum() :
    for var1 in range(2, 500):
        for var2 in range(1, var1-1):
            var3 = 1000 - var1 - var2
            if (var1**2 + var2**2 == var3**2) :
                return var1 * var2 * var3
            
def main():
    print(findNum())
    
    
if __name__ == '__main__' :
    main()