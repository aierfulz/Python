import csv
import os
from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.mlab as mlab
import matplotlib.font_manager as font_manager
class interpolationcsv:

    def __init__(self,filename,parent=None):
        self.filename = filename

    def draw(self):

        filename = self.filename
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

        #

        plt.gca().set_aspect(1.0)

        font = font_manager.FontProperties(family='times new roman', style='italic', size=16)

        cs = plt.contour(XI, YI, ZI, colors="black")
        plt.clabel(cs, cs.levels, inline=True, fontsize=10, prop=font)

        plt.subplot(1, 1, 1)
        plt.pcolor(XI, YI, ZI, cmap=cm.jet)
        plt.scatter(xx, yy, 100, zz, cmap=cm.jet)


        plt.title('interpolation example')
        plt.xlim(int(xx.min()), int(xx.max()))
        plt.ylim(int(yy.min()), int(yy.max()))
        plt.colorbar()
        plt.savefig("interpolation.jpg")
        #plt.show()

        return ZI, XI, YI
