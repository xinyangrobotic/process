# _*_ coding:utf-8 _*_
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import scipy.io
import numpy as np
from itertools import islice
from mpl_toolkits.mplot3d import axes3d

params = {  
            
        'axes.labelsize': '35',
        'xtick.labelsize':'27',
        'ytick.labelsize':'27',
        'lines.linewidth':'2',
        'legend.fontsize':'27',
        'figure.figsize':'12,9'
        
            }

#pylab.rcParams.update(params)

def loadData(fileName):
    inFile = open(fileName,'r')
    x = []
    y = []
    z = []
    for line in islice(inFile,3,None):
        trainingSet = line.split()
        x.append(trainingSet[1])
        y.append(trainingSet[2])
        z.append(trainingSet[3])
    return (x,y,z)
(x,y,z) = loadData('groundtruth.txt')
(x1,y1,z1) = loadData('KeyFrameTrajectory.txt')
fig = plt.figure()

ax = fig.gca(projection = '3d')
x = [float( x ) for x in x if x]
y = [float( y ) for y in y if y]
z = [float( z ) for z in z if z]
x1 = [float( x1 ) for x1 in x1 if x1]
y1 = [float( y1 ) for y1 in y1 if y1]
z1 = [float( z1 ) for z1 in z1 if z1]

ax.plot(x,y,z,c = 'r')
ax.plot(x1,y1,z1,c = 'g')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
