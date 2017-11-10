import utils
import numpy as np

def softplus(z): return np.log(1+np.exp(z))

X = utils.softplus_inputs
print(X)

print ''    
print '__________________________'
print ''    


Y = softplus(X)
for x,y in zip(X,Y):
    print('softplus(%11.4f) = %11.4f'%(x,y))

print ''    
print '__________________________'
print ''    
    
for x in X:
    y = softplus(x)
    print('softplus(%11.4f) = %11.4f'%(x,y))

print ''    
print '__________________________'
print ''    

    
def softplus_opt(Z):
    result = []
    for z in Z:
        if z > 100:
            result += [z]
        else:
            result += [np.log(1+np.exp(z))]
    return result

Y = softplus_opt(X)
for x,y in zip(X,Y):
    print('softplus(%11.4f) = %11.4f'%(x,y))

print ''    
print '__________________________'
print ''    


### using clip to give the boundary of input vector. Ref in lecture4 "The sigmoid function (4)"

def softplus_npopt(Z):
    clipZ = np.clip(Z, -10000, 100)
    Y = np.log(1+np.exp(clipZ))
    results = np.where(clipZ == 100, Z, Y)
    return results
    
Y = softplus_npopt(X)

for x,y in zip(X,Y):
    print('softplus3(%11.4f) = %11.4f'%(x,y))

print ''    
print '__________________________'
print ''    
