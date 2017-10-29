# _*_ coding:utf-8 _*_
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import scipy.io
import numpy as np

params = {  
            
        'axes.labelsize': '35',
        'xtick.labelsize':'27',
        'ytick.labelsize':'27',
        'lines.linewidth':'2',
        'legend.fontsize':'27',
        'figure.figsize':'12,9'
        
            }

pylab.rcParams.update(params)

def loadData(fileName):
    inFile = open(fileName,'r')
    x = []
    y = []
    theta = []

    for line in inFile:
        trainingSet = line.split()
        x.append(trainingSet[1])
        y.append(trainingSet[2])
        theta.append(trainingSet[3])

        return(x,y,theta)

import pylab
def plotData(x,y theta)
    length = len(y)
    pylab.figure(1)
    pylab.plot(x,y,theta,)

