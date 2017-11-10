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

def logp(X,m,S):
    
    # Find the number of dimensions from the data vector
    d = X.shape[1]
    
    # Invert the covariance matrix
    Sinv = np.linalg.inv(S)
    
    # Compute the quadratic terms for all data points
    Q = -0.5*(np.dot(X-m,Sinv)*(X-m)).sum(axis=1)
    
    # Raise them quadratic terms to the exponential
    Q = np.exp(Q)
    
    # Divide by the terms in the denominator
    P = Q / np.sqrt((2*np.pi)**d * np.linalg.det(S))
    
    # Take the product of the probability of each data points
    Pprod = np.prod(P)
    
    # Return the log-probability
    return np.log(Pprod)


print(logp(utils.X1,utils.m1,utils.S1))
print(logp(utils.X2,utils.m2,utils.S2))
print(logp(utils.X3,utils.m3,utils.S3))