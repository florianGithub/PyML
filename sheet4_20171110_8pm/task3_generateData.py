### probability of generating data from Gauss model

import utils
import numpy as np

X1 = utils.X1
X2 = utils.X2
X3 = utils.X3

m1 = utils.m1
m2 = utils.m2
m3 = utils.m3


S1 = utils.S1
S2 = utils.S2
S3 = utils.S3

#This function is numerically instable for multiple reasons. 
# 1 The product of many probabilities, 
# 2 the inversion of a large covariance matrix, 
# 3 and the computation of its determinant, 
# are all potential causes for overflow. 

def logp_opt(X,m,S):
    
    # Find the number of dimensions from the data vector
    d = X.shape[1]
    
    # prob2 = inverting large matrix. 
    # seems to work fine here. 
    # but det(Sinv) approx zero -> not invertible.
    detS = np.linalg.det( S )
    #Sinv = np.linalg.inv(S)
    L = np.linalg.cholesky(S)
    LT = np.transpose( L )
    L_inv = np.linalg.inv(L)
    LT_inv = np.linalg.inv(LT)
    detS = np.linalg.det( L ) * np.linalg.det( LT )
    
    # Compute the quadratic terms for all data points
    vecDev = X-m
    vecDevMapped1 = np.dot( vecDev , LT_inv )
    vecDevMapped2 = np.dot( vecDevMapped1 , L_inv )
    prodComponents_i1 = vecDevMapped2 * vecDev
    scalProd = prodComponents_i1.sum(axis=1)
    Q = -0.5*scalProd
    
    # Raise them quadratic terms to the exponential
    Q = np.exp(Q)

    # prob3 = computation of det.    
    # Divide by the terms in the denominator
    P = Q / np.sqrt((2*np.pi)**d * detS )
    
    # prob1 -> solution = replace prod by sum.
    # Take the product of the probability of each data points
    lnP = np.sum( np.log(P) )
    
    # Return the log-probability
    return lnP


print(logp_opt(X1,m1,S1))
print(logp_opt(X2,m2,S2))
print(logp_opt(X3,m3,S3))