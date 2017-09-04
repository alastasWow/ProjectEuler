# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 12:06:10 2017

@author: refaia
"""

import numpy

def pointInTrig(coords):
    intrig = False
    coordsInt = list(map(int, coords.split(',')))
    v31 = [coordsInt[4] - coordsInt[0], coordsInt[5] - coordsInt[1]]
    v01 = [-coordsInt[0], -coordsInt[1]]
    v12 = [coordsInt[0] - coordsInt[2], coordsInt[1] - coordsInt[3]]
    v02 = [-coordsInt[2], -coordsInt[3]]
    v23 = [coordsInt[2] - coordsInt[4], coordsInt[3] - coordsInt[5]]
    v03 = [-coordsInt[4], -coordsInt[5]]
    
    det1 = int(numpy.linalg.det([v01, v31]))
    det2 = int(numpy.linalg.det([v02, v12]))
    det3 = int(numpy.linalg.det([v03, v23]))   
    
    return (det1 * det2 > 0) and (det3 * det2 > 0)
    

f= open('p102_triangles.txt', 'r')
trigs = f.read().split('\n')[:-1]
f.close()
cpt = 0
for trig in trigs:
    if pointInTrig(trig):
        cpt += 1
print(cpt)
       