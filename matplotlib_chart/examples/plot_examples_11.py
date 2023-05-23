import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors
import matplotlib.cm as cm
from matplotlib.ticker import NullFormatter,FormatStrFormatter,FuncFormatter,FixedFormatter,LinearLocator,MultipleLocator,IndexLocator

def gen_x(n):
    ret = []
    x = np.arange(0, n, 1, dtype=np.int8) #[0,1,2,3,...n 0,1,2,3,...n]
    while n > 0:
       ret.extend(x) 
       n-=1   
    return ret

def gen_y(n):
    ret = []
    indx = 0
    while indx < n:
        ret.extend([indx] * n) #[0,0,0,0...n,1,1,1,1....n]
        indx+=1
    return ret    

def formatValue(v,pos):
    return f"({v})" if v < 0 else f"[{v}]"

# https://matplotlib.org/stable/gallery/mplot3d/hist3d.html#sphx-glr-gallery-mplot3d-hist3d-py
# https://www.youtube.com/watch?v=VMuT3llidTk&list=PLA0M1Bcd0w8xQx-X5a6eSEOYULNSnHN_p&index=4
def plot_examples_11():
    size_x_y = 73
   
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    fig = plt.figure()
    ax_3d = fig.add_subplot(projection='3d')
    
    xpos = gen_x(size_x_y)
    ypos = gen_y(size_x_y)

    zpos = 0
    # Construct arrays with the dimensions for the 16 bars.
    dx_size_fig = dy_size_fig = 0.75 * np.ones_like(zpos)
   
    dz_value = np.random.randint(0, 10,size_x_y*size_x_y)
    indx = 0
    for i in dz_value:
        if indx%78==0:
            dz_value[indx] = 25
        indx+=1    

    
    # color bar (https://stackoverflow.com/questions/11950375/apply-color-map-to-mpl-toolkits-mplot3d-axes3d-bar3d)
    offset = dz_value + np.abs(0)
    fracs = offset.astype(float)/offset.max()
    norm = colors.Normalize(fracs.min(), fracs.max())
    color_values = cm.jet(norm(fracs.tolist()))

    ax_3d.bar3d(xpos, ypos, zpos, dx_size_fig, dy_size_fig, dz_value, color=color_values,zsort='average')
    ax_3d.set_xlabel('x')
    ax_3d.set_ylabel('y')
    ax_3d.set_zlabel('z')
    #ax_3d.xaxis.set_major_formatter(FixedFormatter(['',0,'',1,'',2,'',3]))
    #ax_3d.yaxis.set_major_formatter(FixedFormatter(['',0,'',1,'',2,'',3]))
    #ax_3d.yaxis.set_major_formatter(formatValue)
    #ax_3d.set_xlim(xmin=0)
    #ax_3d.set_ylim(ymin=0)
    #ax_3d.xaxis.set_major_locator(MultipleLocator(base=1))
    #ax_3d.yaxis.set_major_locator(MultipleLocator(base=1))

    #ax_3d.xaxis.set_major_formatter(FormatStrFormatter("%d"))
    #ax_3d.yaxis.set_major_formatter(FormatStrFormatter("%d"))
    #ax_3d.xaxis.set_major_locator(IndexLocator(base=1,offset=0.35))
    #ax_3d.yaxis.set_major_locator(IndexLocator(base=1,offset=0.35))

    plt.show()

from matplotlib.animation import ArtistAnimation
import random
def plot_examples_11_animation():
    size_x_y = 10
    fig = plt.figure()
    ax_3d = fig.add_subplot(projection='3d')
    ax_3d.set_xlabel('x')
    ax_3d.set_ylabel('y')
    ax_3d.set_zlabel('z')

    xpos = gen_x(size_x_y)
    ypos = gen_y(size_x_y)
    zpos = 0
    dx_size_fig = dy_size_fig = 0.75
    dz_value = np.zeros(size_x_y*size_x_y)
    dz_value[0]=25
    frames = []

    for i in range(3):
        for index in range(len(dz_value)):
            dz_value[index] = dz_value[index]+random.randint(1,6)

            offset = dz_value + np.abs(0)
            fracs = offset.astype(float)/offset.max()
            norm = colors.Normalize(fracs.min(), fracs.max())
            color_values = cm.jet(norm(fracs.tolist()))

            line = ax_3d.bar3d(xpos, ypos, zpos, dx_size_fig, dy_size_fig, dz_value,color=color_values, zsort='average')
            frames.append([line])
    
    ani = ArtistAnimation(
        fig, # фигура для анимации
        frames,# кадры
        interval=150,# задержка между кадрами в ms
        blit=True,# двойная буферизация для плавной анимации
        repeat=True # зациклить анимацию
    )
    ani.save('output/plot_examples_11_animation.gif', writer='imagemagick', fps=60)
    plt.show()