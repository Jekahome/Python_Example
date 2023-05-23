#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def plot_examples():
    #nrows = 3
    #ncols = 5
    #Z = np.arange(nrows * ncols).reshape(nrows, ncols)
    # np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int8)
    nrows = 50  
    ncols = 106
    Z = np.zeros((nrows,ncols), dtype=np.uint8)
    
    # от фиолет до желтого в диапазоне 0-255
    v=0
    indx=0
    while indx < 106:
        Z[0][indx]=v
        Z[1][indx]=106+v
        v += 1
        indx+=1
    Z[4][5]=106  
    Z[23][5]=106 

    x = np.arange(ncols + 1)
    y = np.arange(nrows + 1)

    fig, ax = plt.subplots(figsize=(ncols, nrows))
    ax.pcolormesh(x, y, Z, shading='flat', vmin=Z.min(), vmax=Z.max())
    title = "shading='flat'"
    # this all gets repeated below:
    X, Y = np.meshgrid(x, y)
    ax.plot(X.flat, Y.flat, '+', color='m')
    #ax.set_xlim(-0.7, 5.2)
    #ax.set_ylim(-0.7, 3.2)
    ax.set_xlim(-0.7, 106.0)
    ax.set_ylim(-0.7, 50.0)
    ax.set_title(title)
    plt.show()

 