### computing a partion function ###

import utils
import itertools
import numpy as np
    
w_small = utils.w_small
w_medium = utils.w_medium
w_big = utils.w_big

def getlogZ(w):
    Z = 0
    for x in itertools.product([-1, 1], repeat=10):
        Z += np.exp(np.dot(x,w))
    return np.log(Z)

print('%11.4f'%getlogZ(w_small))
print('%11.4f'%getlogZ(w_medium))
print('%11.4f'%getlogZ(w_big))

print ''
print '_________________'
print ''

def getlogZ_opt( w ):
    
    # use the log-sum-exp trick. for the proof see https://www.xarg.org/2016/06/the-log-sum-exp-trick-in-machine-learning/    
    
    argForExp_i1 = []
    
    for x in itertools.product([-1, 1], repeat=10):
        argForExp = np.dot(x,w)
        argForExp_i1.append( argForExp )
    
    offsetForExpArgs = max( argForExp_i1 )
     
    Zrest = 0.
    for x in itertools.product([-1, 1], repeat=10):
        Zrest += np.exp (np.dot(x,w)-offsetForExpArgs )
    
    lnZ = offsetForExpArgs + np.log(Zrest)
    
    return lnZ

#    lnZ = max(w)
#    lnZ += getlogZ( np.array(w)-max(w) )
        
#    return lnZ

print('%11.4f'%getlogZ_opt(w_small))
print('%11.4f'%getlogZ_opt(w_medium))
print('%11.4f'%getlogZ_opt(w_big))
    
