#!/usr/bin/python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------------------------------------
# https://wiki.archlinux.org/title/Python_(%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9)/Virtual_environment_(%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9)#:~:text=%D0%92%D0%B8%D1%80%D1%82%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20(virtual%20environment)%20%E2%80%94,%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8%20%D0%B4%D1%80%D1%83%D0%B3%D0%B8%D1%85%20%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D0%B5%D0%B9%20%D0%B2%20%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8.

# virtualenv — это инструмент, используемый для создания изолированного рабочего пространства для приложения Python. Он даёт некоторые преимущества: например, возможность локальной установки модулей, экспорта рабочей среды и выполнения программы Python внутри этого окружения.
# Виртуальное окружение (virtual environment) — это каталог, в который устанавливаются некоторые исполняемые файлы и скрипты. Среди файлов есть python для выполнения скриптов и pip для установки других модулей в окружении. 
# По сути, виртуальное окружение имитирует полную системную установку Python и всех необходимых модулей, не вмешиваясь в работу системы, на которой будет запускаться приложение.

# Install:
# $ python3 -m pip install --user virtualenv

# Создание:
# Используйте venv или virtualenv для создания виртуального окружения в каталоге вашего проекта. 
# Не забудьте исключить каталог venv из вашей системы контроля версий — для его восстановления достаточно копии pip freeze

# $ cd project_dir
# $ virtualenv envname

# Активация:
# $ source envname/bin/activate
#   (envname) jeka@jeka:~/Projects/Python$

# Теперь команды python и pip будут запускаться и управлять пакетами только внутри виртуального окружения, не затрагивая систему.
# Для выхода из виртуального окружения выполните функцию, которую создал скрипт активации:
# (envname) $ deactivate
# ------------------------------------------------------------------------------------------------------------


 

# Построение графиков в Python при помощи Matplotlib
# https://python-scripts.com/matplotlib и https://matplotlib.org/stable/gallery/index.html
# (envname) $ pip3 install matplotlib
# sudo apt-get install -y python3-tk

import matplotlib.pyplot as plt
import numpy as np

def plot_examples_2():
    width = 0.4
    x_list = list(range(0,5))
    y1_list = [22,17,81,41,25] 
    y2_list = [62,37,39,36,49] 
    x_indexes = np.arange(len(x_list))

    plt.figure()

    plt.subplot(2,2,1)
    plt.title('Salary Graph')
    plt.xticks(x_list,['Monday','Truesday','Wednesday','Thursday','Friday'])
    plt.xlabel('days')
    plt.ylabel('salary, $')
    plt.plot(x_list,y1_list,label="Mark",marker='o')
    plt.plot(x_list,y2_list,label="Steven",marker='^')
    plt.legend()


    plt.subplot(2,2,2)
    plt.title('Salary Bars')
    plt.xticks(x_indexes,['Monday','Truesday','Wednesday','Thursday','Friday'])
    plt.xlabel('days')
    plt.ylabel('salary, $')
    plt.bar(x_indexes - (width/2),y1_list,label="Mark",width=width)
    plt.bar(x_indexes + (width/2),y2_list,label="Steven",width=width)
    plt.legend()


    plt.subplot(2,1,2)
    plt.title('Another One Graph')
    plt.xticks(x_indexes,['Monday','Truesday','Wednesday','Thursday','Friday'])
    plt.xlabel('days')
    plt.ylabel('salary, $')
    plt.bar(x_indexes - (width/2),y1_list,label="Mark",width=width)
    plt.bar(x_indexes + (width/2),y2_list,label="Steven",width=width)
    plt.legend()

    plt.show()

# ------------------------------------------------------------
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

#plot_examples()
# ------------------------------------------------------------

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
#plot_examples_3()
# ------------------------------------------------------------

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
#plot_examples_4()

# ------------------------------------------------------------
# animation
import matplotlib.animation as animation
np.random.seed(19680801)
INDEX_START = 0
INDEX_END = 600
COUNT_MAX = 200
COUNT = 1000
VALUE_MIN_FOR_INDEX = 0
VALUE_MAX_FOR_INDEX = 600

HIST_BINS = np.linspace(INDEX_START, INDEX_END, COUNT_MAX)

def prepare_animation(bar_container):

    def animate(frame_number):
        # simulate new data coming in
        data = np.random.randint(VALUE_MIN_FOR_INDEX, VALUE_MAX_FOR_INDEX, COUNT)
        n, _ = np.histogram(data, HIST_BINS)
        for count, rect in zip(n, bar_container.patches):
            rect.set_height(count)
        return bar_container.patches
    return animate

def plot_examples_5():

    data = np.random.randint(VALUE_MIN_FOR_INDEX, VALUE_MAX_FOR_INDEX, COUNT)
    n, _ = np.histogram(data, HIST_BINS)

    fig, ax = plt.subplots()
    _, _, bar_container = ax.hist(data, HIST_BINS, lw=1, ec="yellow", fc="green", alpha=0.5)
    ax.set_ylim(top=COUNT_MAX)  # set safe limit to ensure that all data is visible.

    ani = animation.FuncAnimation(fig, prepare_animation(bar_container), COUNT_MAX, repeat=False, blit=True)
    #ani.save('../../files/animation.gif', writer='imagemagick', fps=60)
    plt.show()
#plot_examples_5();

#data = np.random.randn(10)
#print(data)
# ------------------------------------------------------------
# animation
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

#plot_examples_6()

# ------------------------------------------------------------
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
    line, = ax.plot(x,y)    

    value_change = np.arange(0,4*np.pi,0.1) # список от и до с шагом

    ani = FuncAnimation(
        fig, # фигура для анимации
        func=update_frame,# ф-ция обновления текущего кадра
        frames=value_change,# меняющтйся параметр от кадра к кадру
        fargs=(line,x),# дополнительные параметры для ф-ции update_frame
        interval=30,# задержка между кадрами в ms
        blit=True,# двойная буферизация для плавной анимации
        repeat=False # зациклить анимацию
    )
    plt.show()

# plot_examples_7()

# ------------------------------------------------------------
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

    anim = ArtistAnimation(
        fig, # фигура для анимации
        frames,# кадры
        interval=30,# задержка между кадрами в ms
        blit=True,# двойная буферизация для плавной анимации
        repeat=True # зациклить анимацию
    )
    plt.show()

#plot_examples_8()

# ------------------------------------------------------------
# 3D chart
# https://www.youtube.com/watch?v=Bi02bzYnciQ&list=PLA0M1Bcd0w8xQx-X5a6eSEOYULNSnHN_p&index=12
# plot() - линейный 2D
# step() - ступенчатый 2D
# scatter() - точечный график 3D
# plot_wireframe() - каркасная поверхность в 3D
# plot_surface() - непрерывная поверхность в 3D
def plot_examples_9_plot():
    fig = plt.figure(figsize=(7, 4))
    ax_3d = fig.add_subplot(projection='3d')
     
    x = np.linspace(0,10,50) # от 0 до 10 диапазон из 50-ти значений
    z = np.cos(x)
    ax_3d.plot(x, x, z) # z - значения по вертикали
    ax_3d.set_xlabel('x')
    ax_3d.set_ylabel('y')
    ax_3d.set_zlabel('z')
    plt.show()

def plot_examples_9_plot_2():
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

#plot_examples_9_plot()
#plot_examples_9_plot_2()


# ------------------------------------------------------------
# количество использованных слов за урок
# https://matplotlib.org/stable/gallery/animation/strip_chart.html#sphx-glr-gallery-animation-strip-chart-py


# Количество раз использования слова
# https://matplotlib.org/stable/gallery/mplot3d/custom_shaded_3d_surface.html#sphx-glr-gallery-mplot3d-custom-shaded-3d-surface-py

# Динамика Количество раз использования слова
# https://matplotlib.org/stable/gallery/animation/random_walk.html#sphx-glr-gallery-animation-random-walk-py







