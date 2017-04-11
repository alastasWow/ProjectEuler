# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 18:42:40 2017

@author: Refaia
"""


print(sum(a * ((a - 2) if a % 2 == 0 else (a - 1)) for a in range(3, 1001)))
        