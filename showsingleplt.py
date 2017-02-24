import os
import matplotlib.pyplot as plt
import numpy as np


def draw(path,name):
    file = open(path+name)
    ynum = []
    for line in file.readlines():
        line = float(line.strip())
        ynum.append(line)
    plt.figure(1)
    plt.plot(range(1,len(ynum)+1),ynum,'r*-',label=name)
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    file = '/home/sheng/ssd_mxnet/mxnet-ssd/data/VOCdevkit/results/VOC2007/epoch_ap/'
    name='tvmonitor_ap.txt'
    draw(file,name)

