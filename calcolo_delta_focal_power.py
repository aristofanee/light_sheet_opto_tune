# -*- coding: utf-8 -*-
"""
Created on Wed May 19 17:38:00 2021

@author: davno
"""

def range_dpt (f1, f2, fcl, delta):
    f1 /= 1000
    f2 /= 1000
    fcl /= 1000
    delta /= 1000
    
    p = delta*(f2/(f1*fcl))**2
    
    return p


ris = range_dpt(60, 100, 75, 1.5)

print(ris)