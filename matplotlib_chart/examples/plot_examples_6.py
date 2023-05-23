#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# Анимация в цикле
def plot_examples_6():
    nrows = 106   
    ncols = 50
    Z = np.zeros((nrows,ncols), dtype=np.uint8)
    Z = np.flip(Z,axis=0)
    # от фиолет до желтого в диапазоне 0-255

    fig, ax = plt.subplots()
    Y = 1
    X = 1
    while X < 50:
        Z[Y][X]=106  
        Z[Y][X]=106
        
        #plt.matshow(Z)
        X +=1
        Y+=1
        ax.clear()
        ax.imshow(Z)
        ax.set_title(f"frame {X}")
        plt.pause(0.4)