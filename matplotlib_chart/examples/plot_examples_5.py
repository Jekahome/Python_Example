#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
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
    ani.save('output/plot_examples_5.gif', writer='imagemagick', fps=60)
    plt.show()
 