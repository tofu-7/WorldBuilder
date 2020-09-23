import numpy as np
import random as rand
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

circumfrence = 4000
height = circumfrence / 2

pList = []


pointFactor = 250
jitterFactor = 75
for i in range(int(circumfrence / pointFactor)):
    for j in range(int(height / pointFactor)):
        nPoint = [ i * pointFactor + (rand.randrange(-jitterFactor, jitterFactor)), 
        j * pointFactor + (rand.randrange(-jitterFactor, jitterFactor))]

        nPointCirc = [nPoint [0] + circumfrence, nPoint[1]]

        pList.append(nPoint)
        pList.append(nPointCirc)


points = np.array(pList)

vor = Voronoi(points)

plot = voronoi_plot_2d(vor)
plt.show()