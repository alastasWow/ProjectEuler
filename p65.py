# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 08:15:29 2017

@author: Refaia
"""
import time

def main() :
    delta = time.time()
    nthTerme = 100
    uN_2_N, uN_2_D = 2, 1
    uN_1_N, uN_1_D = 3, 1
    alpha  = 0
    for i in range(3, nthTerme + 1) :
        if i % 3 == 0 :
            alpha += 2
            uN_N, uN_D = (alpha * uN_1_N) + uN_2_N, (alpha * uN_1_D) + uN_2_D
            uN_2_N, uN_2_D = uN_1_N, uN_1_D
            uN_1_N, uN_1_D = uN_N, uN_D
        else :
            uN_N, uN_D = uN_1_N + uN_2_N, uN_1_D + uN_2_D
            uN_2_N, uN_2_D = uN_1_N, uN_1_D
            uN_1_N, uN_1_D = uN_N, uN_D
    delta = time.time() - delta
    return sum(list(map(int, str(uN_N)))) ,delta

print(main())
                         
            