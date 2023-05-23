#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
# https://www.youtube.com/watch?v=CG1uTfeyfbk&list=PLA0M1Bcd0w8xQx-X5a6eSEOYULNSnHN_p&index=12

def plot_examples_4():
    nrows = 55 
    ncols = 100
    Z = np.zeros((nrows,ncols), dtype=np.uint8)
    
    fig, ax = plt.subplots(figsize=(nrows,ncols))
    plt.set_cmap('RdYlBu')
    
    v=0
    indx=0
    while indx < 100:
        Z[0][indx]=v
        Z[1][indx]=106+v
        v += 1
        indx+=1
    Z[4][5]=106  
    Z[23][5]=106 

    c = ax.pcolor(Z, edgecolors='k', linewidths=1)
    ax.set_title('Количество раз использования слова')

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    plt.colorbar(c, cax=cax)
    
    plt.show()


