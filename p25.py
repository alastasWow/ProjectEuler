# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:24:42 2017

@author: Refaia
"""
import time
def fiboRecMem(tab, n) :
    if len(tab) > n :
        return tab[n]
    tab.insert(n,fiboRecMem(tab, n - 1) + fiboRecMem(tab, n - 2))
    return tab[n]


tabFibo = [1, 1]
#print(fiboRecMem(tabFibo, index - 1) )


def fiboIter(n) :
    if n == 0 or n == 1 :
        return 1
    i = n
    u_n_2 = 1
    u_n_1 = 1
    while i > 1 :
        u_n = u_n_2 + u_n_1
        u_n_2 = u_n_1
        u_n_1 = u_n
        i -= 1
    return u_n
    
    
def main() :
    delta = time.time()
    index = 1
    digits = 1000
    while fiboIter(index - 1) <= 10**(digits - 1) :
        index += 1
    delta = time.time() - delta
    print(index,"time:", delta)



if __name__ == '__main__' :
    main()

