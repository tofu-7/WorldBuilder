import numpy as np
import random as rand
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.geometry import shape, Point, MultiPoint

xMax = 1999
yMax = 999
pointCount = 20
pList = []

for i in range(pointCount):
    pList.append([rand.randrange(1,xMax),rand.randrange(1,yMax)])

points = np.array(pList)

vor=Voronoi(points)

plot = voronoi_plot_2d(vor)
plt.show()
