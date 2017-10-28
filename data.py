#coding:utf-8
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

x = []
y = []
z = []
f = open("KeyFrameTrajectory.txt")
line = f.readline()
while line:
	c,d,e,k,g,h,i,j = line.split()
	x.append(d)
	y.append(e)
	z.append(k)
	
	line = f.readline()
	
f.close()

#string型转int型
x = [ float( x ) for x in x if x ]
y = [ float( y ) for y in y if y ]
z = [ float( z ) for z in z if z ]

#print x
fig=plt.figure()
ax = fig.gca(projection = '3d')

ax.plot(x,y,z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
