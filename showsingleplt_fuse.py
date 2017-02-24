import os
import matplotlib.pyplot as plt
import numpy as np


def draw(path,name,label,single_size):
    file = open(path+name)
    ynum = []
    for line in file.readlines():
        line = float(line.strip())
        ynum.append(line)
    ypart = []
    for i in range( len(ynum)/single_size ):
        ypart.append(ynum[single_size*i:(i+1)*single_size])

    plt.figure(1)
    color_style = ['r*-','b^-','gv-','b>-']
    
    for i in range(len(ypart)):
        plt.plot(range(1,single_size+1),ypart[i],color_style[i],label=label[i])
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    file = '/home/sheng/ssd_mxnet/mxnet-ssd/data/VOCdevkit/results/VOC2007/epoch_ap/'
    name='tvmonitor_ap.txt'
    single_size = 40
    label=['first','second','third','forth']
    draw(file,name,label,single_size)

