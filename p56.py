# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 11:41:18 2017

@author: Refaia
"""

listSums = []

maximum = max([sum(map(int, str(x ** y))) for x in range(2,100) for y in range(2, 100)])

print(maximum)