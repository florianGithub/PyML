import numpy,numpy.linalg

# Return the stationary distribution of a markov chain with transition matrix P
def getstationary(P):
    A = numpy.concatenate([(P.T - numpy.identity(8)),numpy.ones([1,8])],axis=0)
    b = numpy.array([0]*8+[1])
    return numpy.linalg.lstsq(A,b)[0]

# Performs a Markov chain transition for multiple particles in parallel
def mcstep(X,Ppad,seedval):
    Xp = numpy.dot(X,Ppad)
    Xc = numpy.cumsum(Xp,axis=1)
    L,H = Xc[:,:-1],Xc[:,1:]
    R = numpy.random.mtrand.RandomState(seedval).uniform(0,1,[len(Xp),1])
    return (R > L)*(R < H)*1.0

def getNext_oneIfInState_i1Scenario_i2State( curOneIfInState_i1Scenario_i2State , transitionMatrix_padded , seed ):
    
    nScenarios = len( curOneIfInState_i1Scenario_i2State )
    
    prob_i1Scenario_i2NextState_padded = numpy.dot( curOneIfInState_i1Scenario_i2State , transitionMatrix_padded ) 
    # UNDERSTOOD dot[i1,i2,i3] = np.sum( value1_i1_i2_i3[i1,i2,:] * value2_i1_i2_i3[i1,:,i3] )
    # draw the matrices -> np.dot delivers the desired result.
    
    bordersOfBuckets_i1Scenario_i2Bucket = numpy.cumsum( prob_i1Scenario_i2NextState_padded , axis=1 )
    lowerBorder_i1Scenario_i2Bucket = bordersOfBuckets_i1Scenario_i2Bucket[ : ,   : -1 ]
    upperBorder_i1Scenario_i2Bucket = bordersOfBuckets_i1Scenario_i2Bucket[ : , 1 :    ]
    
    uniformRandomNumber_i1Scenario = numpy.random.mtrand.RandomState(seed).uniform( 0,1, [nScenarios,1] )
    
    uniformRandomNumber_largerThan_lowerBorderBucket_i1Scenario_i2Bucket  = uniformRandomNumber_i1Scenario > lowerBorder_i1Scenario_i2Bucket
    uniformRandomNumber_smallerThan_upperBorderBucket_i1Scenario_i2Bucket = uniformRandomNumber_i1Scenario < upperBorder_i1Scenario_i2Bucket
    
    uniformInBucket_i1Scenario_i2Bucket = uniformRandomNumber_largerThan_lowerBorderBucket_i1Scenario_i2Bucket * uniformRandomNumber_smallerThan_upperBorderBucket_i1Scenario_i2Bucket
    
    next_oneIfInState_i1Scenario_i2State = uniformInBucket_i1Scenario_i2Bucket * 1.
    return next_oneIfInState_i1Scenario_i2State



# Initial position of particles in the lattice
def getinitialstate():
    #X = numpy.random.mtrand.RandomState(123).uniform(0,1,[1000,8]) #1000 rows with 8 cols filled with random number uniformly drawn from the interval [0,1].
    #X = (X == numpy.max(X,axis=1)[:,numpy.newaxis])*1.0 #1000 rows with 8 cols. one col per row is filled with the number 1.	
    #return X    
    
    #1000 rows with 8 cols filled with random number uniformly drawn from the interval [0,1].
    seed = 123
    mat1000x8_uniformRandom = numpy.random.mtrand.RandomState( seed ).uniform(0,1,[1000,8]) # randomState module to use a seed.
    maxsOfEachRow_1dim = numpy.max( mat1000x8_uniformRandom , axis=1 )
    maxsOfEachRow_2dim = maxsOfEachRow_1dim[:,numpy.newaxis] # with maxOfEachRow_1dim elementwise comparision below will fail.
    boolMat_is_max_of_row = ( mat1000x8_uniformRandom == maxsOfEachRow_2dim )
    mat1000x8_zerosWithUniqueOne_inEachRow = boolMat_is_max_of_row*1.0 # False*1 = 0 , True*1 = 1
    startStates_uniformDistributed = mat1000x8_zerosWithUniqueOne_inEachRow
    return startStates_uniformDistributed

