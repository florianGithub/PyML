import matplotlib
from matplotlib import pyplot as plt
import time
import data
import numpy as np
import scipy
import scipy.spatial

def pydistance(x1,x2):
	return sum([(x1d-x2d)**2 for x1d,x2d in zip(x1,x2)])

def pynearest(u,X,Y,distance=pydistance):
	xbest = None
	ybest = None
	dbest = float('inf')
	for x,y in zip(X,Y):
		d = distance(u,x)
		if d < dbest:
			ybest = y
			xbest = x
			dbest = d
	return ybest

def pybatch(U,X,Y,nearest=pynearest,distance=pydistance):
	return [nearest(u,X,Y,distance=distance) for u in U]

def npdistance(x1,x2):
	return np.linalg.norm(x1 - x2)

def npnearest(u,X,Y, distance=npdistance):
	#U = np.full((X.shape), u)
	u_array = np.array(u, ndmin=2)
	D = scipy.spatial.distance.cdist(u_array,X)
	#print(D.shape)
	min_idx = np.argmin(D)
	return Y[min_idx]