# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 18:48:04 2017

@author: Refaia
"""

import time 

def main() :
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = {0:1}
    delta = time.time()
    for coin in coins :
        for i in range(coin, target + 1) :
            if i in ways :
                ways[i] = ways[i] + ways[i - coin]
            else :
                ways[i] = ways[i - coin]
    delta = time.time() - delta
    return ways[target], delta

print(main())