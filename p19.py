# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 09:47:50 2017

@author: Refaia
"""

import datetime

numSun = 0

for y in range(1901, 2001) :
    for m in range(1, 13) :
        if datetime.datetime(y, m, 1).weekday() == 6 :
            numSun += 1

print(numSun)