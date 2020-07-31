import numpy as np
import random as rand
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

def llyod(vor):

    return vor

xMax = 100
yMax = 100
pointCount = 10
pList = []
relaxations = 3

for i in range(pointCount):
    pList.append([rand.randrange(0,xMax),rand.randrange(0,yMax)])

points = np.array(pList)

vor=Voronoi(points)

print (vor.regions)
print (vor.point_region)

plot = voronoi_plot_2d(vor)
plt.show()
