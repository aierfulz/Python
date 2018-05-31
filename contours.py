import csv
import os
from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.mlab as mlab

filename = "stations.csv"
file = open(os.getcwd() + "\\" + filename, 'r')
lines = csv.reader(file)
#
data = []
x = []
y = []
z = []
for line in lines:
    try:
        data.append(line)
    except Exception as e:
        print e
        pass
# print data
for i in range(1, len(data)):
    try:
        x.append(float(data[i][0]))
        y.append(float(data[i][1]))
        z.append(float(data[i][3]))
    finally:
        pass

xx = np.array(x)
yy = np.array(y)
zz = np.array(z)
# print np.min(xx)

tx = np.linspace(np.min(xx), np.max(xx), 100)
ty = np.linspace(np.min(yy), np.max(yy), 100)

XI, YI = np.meshgrid(tx, ty)

rbf = interpolate.Rbf(xx, yy, zz, epsilon=2)
ZI = rbf(XI, YI)

plt.gca().set_aspect(1.0)

cs = plt.contour(XI, YI, ZI, colors="black", linewidths=4)
plt.clabel(cs, cs.levels, inline=True, fontsize=10)

plt.show()


