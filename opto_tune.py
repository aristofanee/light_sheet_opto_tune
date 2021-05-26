# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:53:06 2021

@author: davno
"""


from opto import Opto
import numpy as np
import time

risoluzione = 1000

# with Opto(port='COM3') as o:
#     current_low = 0
#     current_high = 50
#     current_delta = current_high-current_low
#     for i in np.linspace(0, 2*np.pi, 1000):
#         o.current(np.sin(i*70)*current_delta+current_low)
#         time.sleep(0.001)
        
def applica_funzione(input_funz):
    global risoluzione
    
    with Opto(port='COM3') as o:
        for i in input_funz():
            o.current(i)
            time.sleep(1/risoluzione)
        
    

def onda_triangolare():
    
    global risoluzione
    k = 2 #coeff angolare
    T = 2*np.pi #periodo
    
    
    x = np.linspace(0, T, risoluzione)
    for i in x:
        if i < x[int(len(x)/2)]:
            yield i*k
        else:
            yield i*(-k) + k*T
            
            
            
print(list(onda_triangolare()))
applica_funzione(onda_triangolare)