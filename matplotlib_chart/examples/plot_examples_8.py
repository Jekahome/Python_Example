#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random

# animation 3D ArtistAnimation
# анимация 3 D
# https://www.youtube.com/watch?v=YWt3SKpZwKM
from matplotlib.animation import ArtistAnimation

def plot_examples_8():
    fig = plt.figure(figsize=(10,6))
    ax_3d = fig.add_subplot(projection='3d')

    x = np.arange(-2*np.pi,2*np.pi,0.2)
    y = np.arange(-2*np.pi,2*np.pi,0.2)
    xgrid, ygrid = np.meshgrid(x, y)

    value_change = np.arange(0, 2*np.pi,0.1) # список от и до с шагом
    frames = []

    # для каждого кадра формируем 3D точку
    for p in value_change:
        zgrid = np.sin(xgrid+p) * np.sin(ygrid)/(xgrid*ygrid)

        line = ax_3d.plot_surface(xgrid, ygrid, zgrid, color='b')
        frames.append([line])# собираем ссылки на обьекты для анимации

    ani = ArtistAnimation(
        fig, # фигура для анимации
        frames,# кадры
        interval=30,# задержка между кадрами в ms
        blit=True,# двойная буферизация для плавной анимации
        repeat=True # зациклить анимацию
    )
    ani.save('output/plot_examples_8.gif', writer='imagemagick', fps=60)
    plt.show()



def plot_examples_8_test():
    fig = plt.figure(figsize=(10,6))
    ax_3d = fig.add_subplot(projection='3d')
    ax_3d.set_xlabel('x')
    ax_3d.set_ylabel('y')
    ax_3d.set_zlabel('z')
    SIZE = 25

    x = []
    number = 0
    while number < SIZE:
        x.append(number) 
        number += 1
    
    y = []
    number = 0
    while number < SIZE:
        y.append(random.randint(1,30)) 
        number += 1

    xgrid, ygrid = np.meshgrid(x, y)

    # созданние данных 
    value_change = []
    number = 0
    while number < SIZE:
        value_change.append(random.randint(7,10)) 
        number += 1
     
    frames = []

    # для каждого кадра формируем 3D точку
    indx = 0
    while indx < len(value_change):
        value_change[indx]+=random.randint(1,30)
        indx+=1
        _,zgrid = np.meshgrid(x, value_change) # созданние данных для каждой точки

        line = ax_3d.plot_surface(xgrid, ygrid, zgrid, color='b')
        frames.append([line])# собираем ссылки на обьекты для анимации

    ani = ArtistAnimation(
        fig, # фигура для анимации
        frames,# кадры
        interval=200,# задержка между кадрами в ms
        blit=True,# двойная буферизация для плавной анимации
        repeat=True # зациклить анимацию
    )
    ani.save('output/plot_examples_8_test.gif', writer='imagemagick', fps=60)
    plt.show()