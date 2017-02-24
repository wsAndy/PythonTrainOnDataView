#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import os
import time


def getWindow(obj_acc,size,plt):
    widnum = len(obj_acc)/size
    left = len(obj_acc)%size
    for id in range(widnum):
        plt.plot(range(id*size+1,id*size+size+1),[np.mean(obj_acc[id*size:id*size+size])]*size,'r-')
        print('ID  '+str(id+1)+' -> '+str(np.mean(obj_acc[id*size:id*size+size])) +'\n')

#        plt.annotate(str(np.mean(obj_acc[id*size:id*size+size])),xy=(id*size+1,np.mean(obj_acc[id*size:id*size+size])), xytext=(id*size,np.mean(obj_acc[id*size:id*size+size]+0.02)),arrowprops=dict(facecolor='black',shrink=0.005) )
    
    if left != 0:
        left_mean = np.mean(obj_acc[widnum*size:len(obj_acc)])
        plt.plot(range(widnum*size+1,len(obj_acc)+1),[left_mean]*left,'r-',label='mean')
        print('ID  '+str(widnum+1) + ' -> ' +str(left_mean) + '\n' )


def sampleLr(lr,plt):
    rsize = []
    rlr = []
    for i in range(len(lr)):
        if lr[i] > -0.001:
            rsize.append(i+1)
            if lr[i] > 1.0:
                rlr.append(lr[i])
            else:
                rlr.append(lr[i])
    plt.plot(rsize,rlr,'r^',label='learning rate *1e5 0.9 means too big')
    

def draw(plt):
    file = open('./../train.log')
    obj_acc = []
    #train_acc = []
    lr = []
    last_stamp_lr = 0

    for line in file.readlines():
        add = line.find('Train-ObjectAcc')
        if add != -1:
            obj_acc.append(  float(line[add+16:].strip()) )
            lr.append(-0.05)
        lr_id = line.find('Change learning rate to')
        if lr_id != -1:
#            lr[last_stamp_lr:len(obj_acc)] = [1e5*float(line[24+lr_id:].strip())]*( len(obj_acc) - last_stamp_lr  )
            lr[len(obj_acc)-1] = 1e3*float(line[24+lr_id:].strip())
   
#            last_time_lr = len(obj_acc)

    file.close()
    plt.plot(range(1,len(obj_acc)+1),obj_acc,'b*--',label='object-acc')
#    plt.plot(range(1,len(lr)+1),lr,'r^',label='learning rate *1e5')
    sampleLr(lr,plt)
    
    size =30
    window = getWindow(obj_acc,size,plt)
    
#    plt.plot(range(1,len(obj_acc)+1),[np.mean(obj_acc)]*len(obj_acc),'g-',label='mean')
#    plt.annotate(str(np.mean(obj_acc)),xy=(1,np.mean(obj_acc)),xytext=(1,np.mean(obj_acc)+0.02),arrowprops=dict(facecolor='black', shrink=0.01))

#    plt.legend(loc='best')
    plt.grid()
    plt.title('learning rate *1e3, 1.0 means too big')
#    plt.show()


if __name__ == '__main__':
    plt.figure(1)
#    while True:
    draw(plt)
    plt.show()

