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
# https://python-scripts.com/matplotlib
# (envname) $ pip3 install matplotlib
# sudo apt-get install -y python3-tk

import matplotlib.pyplot as plt
import numpy as np

def plot_examples_2(colormaps):
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


def plot_examples():
    nrows = 3
    ncols = 5
    Z = np.arange(nrows * ncols).reshape(nrows, ncols)
    x = np.arange(ncols + 1)
    y = np.arange(nrows + 1)

    fig, ax = plt.subplots()
    ax.pcolormesh(x, y, Z, shading='flat', vmin=Z.min(), vmax=Z.max())
    title = "shading='flat'"
    # this all gets repeated below:
    X, Y = np.meshgrid(x, y)
    ax.plot(X.flat, Y.flat, 'o', color='m')
    ax.set_xlim(-0.7, 5.2)
    ax.set_ylim(-0.7, 3.2)
    ax.set_title(title)
    plt.show()

plot_examples()


















