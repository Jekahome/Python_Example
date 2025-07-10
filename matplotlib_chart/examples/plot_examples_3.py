#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def plot_examples_3():
    nrows = 106   
    ncols = 50
    Z = np.zeros((nrows,ncols), dtype=np.uint8)
    
    # от фиолет до желтого в диапазоне 0-255
    v=0
    indx=0
    while indx < 50:
        Z[0][indx]=v
        Z[1][indx]=106+v
        v += 1
        indx+=1
    Z[4][5]=106  
    Z[23][5]=106 
    Z = np.flip(Z,axis=0)
    plt.matshow(Z)
 
    plt.show()