import numpy as np
import random as rand
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

def LlyodRelax(vor): #implementation of lloyds algorith for relaxing points
    points = vor.points #take points

    for i in range(points.shape[0]): #match point to region
        regionID = vor.point_region[i]
        vertIDs = vor.regions[regionID]

        vList = [] #match verts to region
        for j in range(len(vertIDs)):
            if(vertIDs[j] != -1): #given invalid vertex ignore it
                vList.append(vor.vertices[vertIDs[j]])
            else:
                continue
        
        verts = np.array(vList)

        #find center of verts
        xAvg=0.0
        yAvg=0.0
        for j in range(verts.shape[0]):
            xAvg += verts[j][0]
        for j in range(verts.shape[0]):
            yAvg += verts[j][1]

        xAvg /= verts.shape[0]; yAvg /= verts.shape[0]
        centroid = np.array([xAvg,yAvg])

        points[i] = centroid #move point to center

    vor = Voronoi(points) #make a voronoi of relaxed points

    return vor

xMax = 2000
yMax = 1000
pointCount = 20
pList = []
relaxations = 10

for i in range(pointCount):
    pList.append([rand.randrange(0,xMax),rand.randrange(0,yMax)])

points = np.array(pList)

vor=Voronoi(points)

plot = voronoi_plot_2d(vor)
plt.show()

#print (vor.regions)
#print (vor.point_region)
#print (vor.points.shape)


for i in range(relaxations): #relaxing points
    LlyodRelax(vor)
    #plot = voronoi_plot_2d(vor)
    #plt.show()

plot = voronoi_plot_2d(vor)
plt.show()
