from scipy.spatial.distance import cdist
import numpy as np

point1=np.array([0,1])
#point2=np.array([2,0])

point3=np.array([0,100])
point4=np.array([200,0])

A = np.array([point1])
B = np.array([point3,point4])


distMatrix = cdist( A, B )

print distMatrix

print 'conclusion = in rows run points from A. in cols run points from B.'