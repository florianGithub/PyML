import utils
import numpy as np

def softplus(z): return np.log(1+np.exp(z))

X = utils.softplus_inputs
print(X)

Y = softplus(X)
for x,y in zip(X,Y):
    print('softplus(%11.4f) = %11.4f'%(x,y))
    
    
for x in X:
    y = softplus(x)
    print('softplus(%11.4f) = %11.4f'%(x,y))
    
### computing a partion function ###
    
import itertools

def getlogZ(w):
    Z = 0
    for x in itertools.product([-1, 1], repeat=10):
        Z += np.exp(np.dot(x,w))
    return np.log(Z)

print('%11.4f'%getlogZ(utils.w_small))
print('%11.4f'%getlogZ(utils.w_medium))
print('%11.4f'%getlogZ(utils.w_big))

### probability of generating data from Gauss model


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