#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random

# animation FuncAnimation
# https://www.youtube.com/watch?v=YWt3SKpZwKM
from matplotlib.animation import FuncAnimation

def update_frame(value_change,line,x):
    # value_change - параметр меняющийся от кадра к кадру
    # line - (доп.парам.) ссылка на обьект Line2D
    # x - (доп.парам.)
    # Return object matplotlib.artist.Artist
    line.set_ydata(np.cos(x+value_change))
    return [line]

 
def plot_examples_7():
    fig,ax = plt.subplots()
    x = np.arange(-2*np.pi,2*np.pi,0.1)
    y = np.cos(x)
    # line:Line2D https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib-lines-line2d
    line, = ax.plot(x,y)    

    value_change = np.arange(0,4*np.pi,0.1) # список от и до с шагом

    ani = FuncAnimation(
        fig, # фигура для анимации
        func=update_frame,# ф-ция обновления текущего кадра
        frames=value_change,# меняющтйся параметр от кадра к кадру (т.е. начальнный массив будет передаваться по очереди)
        fargs=(line,x),# дополнительные параметры для ф-ции update_frame
        interval=30,# задержка между кадрами в ms
        blit=True,# двойная буферизация для плавной анимации
        repeat=False # зациклить анимацию
    )
    ani.save('output/plot_examples_7.gif', writer='imagemagick', fps=60)
    plt.show()



from matplotlib.ticker import MultipleLocator,MaxNLocator
def test_7_1_update_frame(value_change,line,v):
    # value_change - параметр меняющийся от кадра к кадру
    # line - (доп.парам.) ссылка на обьект Line2D
    # x - (доп.парам.)
    #value_change[0] = value_change[0]+v
    #v+=1
    v[value_change-1]=v[value_change-1]+2
    line.set_ydata(v)  # Return object matplotlib.artist.Artist
    return [line]

def plot_examples_7_test():
    N = 5200
    fig,ax = plt.subplots()
    ax.set_xlabel('x-index')
    ax.set_ylabel('y-value')
    #ax.grid()
    ax.xaxis.set_major_locator(MultipleLocator(base=200))
    #ax.yaxis.set_major_locator(MultipleLocator(base=5))
    ax.minorticks_on()
    ax.grid(which='major',lw=0.2)
    ax.grid(which='minor')
    #ax.xaxis.set_major_locator(MaxNLocator(N))

    x = []
    y = np.ones(N)
    for i in range(N):
        x.append(i)
        if i %100 == 0:
            y[i] = random.randint(1,5000)
        else:
            y[i] = i  
   
    line, = ax.plot(x,y,'g-+')  
    plt.show()

def plot_examples_7_test2():
    N = 500
    fig,ax = plt.subplots()
    ax.set_xlabel('x-index')
    ax.set_ylabel('y-value')
    #ax.grid()
    ax.xaxis.set_major_locator(MultipleLocator(base=10))
    #ax.yaxis.set_major_locator(MultipleLocator(base=5))
    ax.minorticks_on()
    ax.grid(which='major',lw=2)
    ax.grid(which='minor')
    #ax.xaxis.set_major_locator(MaxNLocator(N))

    x = []
    y = np.ones(N)
    for i in range(N):
        x.append(i)
        y[i]=i
    #x = np.array([1,2,3,4,5,6,7,8,9,10])
    #y = np.random.randint(5, 50, 10)# value
    value_other = y.copy()

    line, = ax.plot(x,y,'g-+')  
    value_change = x.copy()
    #print('value_change',value_change)
    ani = FuncAnimation(
        fig, # фигура для анимации
        func=test_7_1_update_frame,# ф-ция обновления текущего кадра
        frames=value_change,# меняющтйся параметр от кадра к кадру
        fargs=(line,value_other),# дополнительные параметры для ф-ции update_frame
        interval=300,# задержка между кадрами в ms
        blit=True,# двойная буферизация для плавной анимации
        repeat=True # зациклить анимацию
    )
    ani.save('output/plot_examples_7_test.gif', writer='imagemagick', fps=60)
    plt.show()

 