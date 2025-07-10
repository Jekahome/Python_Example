#!/usr/bin/python
# -*- coding: utf-8 -*-

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

    #plt.savefig('output/plot_examples_2.png', dpi=150)
    plt.show()

 
