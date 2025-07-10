#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# 3D chart
# https://www.youtube.com/watch?v=Bi02bzYnciQ&list=PLA0M1Bcd0w8xQx-X5a6eSEOYULNSnHN_p&index=12
# plot() - линейный 2D
# step() - ступенчатый 2D
# scatter() - точечный график 3D
# plot_wireframe() - каркасная поверхность в 3D
# plot_surface() - непрерывная поверхность в 3D
def plot_examples_9_linspace():
    fig = plt.figure(figsize=(7, 4))
    ax_3d = fig.add_subplot(projection='3d')
     
    x = np.linspace(0,10,50) # от 0 до 10 диапазон из 50-ти значений
    z = np.cos(x)
    ax_3d.plot(x, x, z) # z - значения по вертикали
    ax_3d.set_xlabel('x')
    ax_3d.set_ylabel('y')
    ax_3d.set_zlabel('z')
    plt.show()

def plot_examples_9_plot_surface():
    fig = plt.figure(figsize=(7, 4))
    ax_3d = fig.add_subplot(projection='3d')
    x = np.arange(-2*np.pi,2*np.pi,0.2)
    y = np.arange(-2*np.pi,2*np.pi,0.2)
    xgrid, ygrid = np.meshgrid(x, y)
    # какие-то значения по какой-то функции
    zgrid = np.sin(xgrid)*np.sin(ygrid)/(xgrid*ygrid)
    #ax_3d.plot_wireframe(xgrid,ygrid,zgrid) 
    ax_3d.plot_surface(xgrid,ygrid,zgrid,rstride=5,cstride=5,cmap='plasma') 
    ax_3d.set_xlabel('x')
    ax_3d.set_ylabel('y')
    ax_3d.set_zlabel('z')
    plt.show()

def plot_examples_9_plot_wireframe():
    fig = plt.figure(figsize=(7, 4))
    ax_3d = fig.add_subplot(projection='3d')
    x = np.arange(-2*np.pi,2*np.pi,0.2)
    y = np.arange(-2*np.pi,2*np.pi,0.2)
    xgrid, ygrid = np.meshgrid(x, y)
    # какие-то значения по какой-то функции
    zgrid = np.sin(xgrid)*np.sin(ygrid)/(xgrid*ygrid)
    ax_3d.plot_wireframe(xgrid,ygrid,zgrid,rstride=1,cstride=5,cmap='plasma') 
    ax_3d.set_xlabel('x')
    ax_3d.set_ylabel('y')
    ax_3d.set_zlabel('z')
    plt.show()

def plot_examples_9_plot_scatter():
    fig = plt.figure(figsize=(7, 4))
    ax_3d = fig.add_subplot(projection='3d')
    x = np.arange(-2*np.pi,2*np.pi,0.2)
    y = np.arange(-2*np.pi,2*np.pi,0.2)
    xgrid, ygrid = np.meshgrid(x, y)
    # какие-то значения по какой-то функции
    zgrid = np.sin(xgrid)*np.sin(ygrid)/(xgrid*ygrid)
    ax_3d.scatter(xgrid,ygrid,zgrid,s=1,color='g') 
    ax_3d.set_xlabel('x')
    ax_3d.set_ylabel('y')
    ax_3d.set_zlabel('z')
    plt.show()
