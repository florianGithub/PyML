import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'png')
plt.rcParams['savefig.dpi'] = 90
import time

#formerly pydistance
def get_distance_py(pattern1,pattern2):
    list_of_pairs_attrPattern1_and_attrPattern2 = zip( pattern1,pattern2 )
    return sum( [ (attrPattern1-attrPattern2)**2 for attrPattern1,attrPattern2 in list_of_pairs_attrPattern1_and_attrPattern2 ] )

def get_distance_np( attr1, attr2 ):
    npAttr1 = np.array(attr1)
    npAttr2 = np.array(attr2)
    return np.linalg.norm(npAttr1-npAttr2)**2

#formerly pynearest
def get_labelNearest_py( attrsUnlabeled , listOfAttrs , listOfLabels , get_distance_between_attrs = get_distance_py ):
    
    attrsNearest = None
    labelNearest = None
    distanceNearest = float('inf')
    
    for attrs,label in zip(listOfAttrs,listOfLabels):
        
        distance_between_attrsUnlabeled_and_attrsLabeled = get_distance_between_attrs( attrsUnlabeled , attrs )
        
        if distance_between_attrsUnlabeled_and_attrsLabeled < distanceNearest:
            attrsNearest = attrs
            labelNearest = label
            distanceNearest = distance_between_attrsUnlabeled_and_attrsLabeled
            
    return labelNearest

#formerly npnearest
def get_labelNearest_map( attrsUnlabeled , listOfAttrs , listOfLabels , get_distance_between_attrs = get_distance_np ):
    listOfDistances = [ get_distance_between_attrs(attrsUnlabeled,attrs) for attrs in listOfAttrs ]
    indexNearest = listOfDistances.index( min(listOfDistances) )    
    labelNearest = listOfLabels[indexNearest]
    return labelNearest
#formerly npnearest
def get_labelNearest_np( attrsUnlabeled , listOfAttrs , listOfLabels , get_distance_between_attrs = get_distance_np ):

    matrix = listOfAttrs
    row = attrsUnlabeled
    matrixDiffs = matrix - row # npMatrix - npRow substracts npRow from each row of npMatrix.    
    matrixSquaredDiffs = matrixDiffs**2 # square to ensure positive value of distances.
    colSumOfSquaredDiffs = matrixSquaredDiffs.sum( axis=1 ) # axis=0 -> sum up all rows. axis=1 -> sum up all cols.
    indexNearest = np.argmin( colSumOfSquaredDiffs )
    labelNearest = listOfLabels[ indexNearest ]
    return labelNearest    

# formerly pybatch
def get_listOfNearestLabels_py( listOfUnlabeledAttrs , listOfAttrs , listOfLabels , get_labelNearest=get_labelNearest_py , get_distance=get_distance_py ):
    listOfLabels = [ get_labelNearest_np( unlabeledAttrs , listOfAttrs , listOfLabels , get_distance_between_attrs=get_distance_np ) for unlabeledAttrs in listOfUnlabeledAttrs ]
    return listOfLabels
# formerly npbatch
def get_listOfNearestLabels_np( listOfUnlabeledAttrs , listOfAttrs , listOfLabels ):

    argsNotToVectorize = (1,2,3)
    get_labelNearest_np_vectorized = np.vectorize( get_labelNearest_np , excluded=argsNotToVectorize )
    listOfLabels = get_labelNearest_np_vectorized( listOfUnlabeledAttrs , listOfAttrs , listOfLabels )    
    
    #vectorized_get_listOfNearestLabels_py = np.vectorize( get_listOfNearestLabels_py )
    #listOfLabels = vectorized_get_listOfNearestLabels_py( listOfUnlabeledAttrs , listOfAttrs , listOfLabels , get_labelNearest=get_labelNearest_np , get_distance=get_distance_np )

    return listOfLabels
    


    
import data
# unlabeledAttrs formerly called U
# labeledAttrs   formerly called X
# labels         formerly called Y
numberOfAttrsPerEntity = 50
numberOfLabeledEntities = 100
numberOfUnlabeledEntities = 20
unlabeledAttrs , listOfLabeledAttrs , listOfLabels = data.toy( numberOfUnlabeledEntities , numberOfLabeledEntities , numberOfAttrsPerEntity )


#print( get_listOfNearestLabels_py( unlabeledAttrs , labeledAttrs , labels ) )
#
#
#labels_by_pydistance = get_listOfNearestLabels_py( unlabeledAttrs , labeledAttrs , labels , get_labelNearest=get_labelNearest_py , get_distance=get_distance_py )
#labels_by_npdistance = get_listOfNearestLabels_py( unlabeledAttrs , labeledAttrs , labels , get_labelNearest=get_labelNearest_py , get_distance=get_distance_np )
#print 'py' + str( labels_by_pydistance )
#print 'np' + str( labels_by_npdistance )
#if labels_by_pydistance == labels_by_npdistance:
#    print 'py distance and np distance give same result.'
    

#labels_by_pynearest = get_listOfNearestLabels_py( unlabeledAttrs , listOfLabeledAttrs , listOfLabels , get_labelNearest=get_labelNearest_py , get_distance=get_distance_np )
#labels_by_npnearest = get_listOfNearestLabels_py( unlabeledAttrs , listOfLabeledAttrs , listOfLabels , get_labelNearest=get_labelNearest_np , get_distance=get_distance_np )
#labels_by_mapnearest = get_listOfNearestLabels_py( unlabeledAttrs , listOfLabeledAttrs , listOfLabels , get_labelNearest=get_labelNearest_map , get_distance=get_distance_np )
#print 'py' + str( labels_by_pynearest )
#print 'np' + str( labels_by_npnearest )
#print 'map' + str( labels_by_npnearest )
#if labels_by_pynearest == labels_by_npnearest and labels_by_pynearest == labels_by_mapnearest:
#    print 'pynearest, mapnearest and npnearest give same result.'


#labels_by_pybatch = get_listOfNearestLabels_py( unlabeledAttrs , listOfLabeledAttrs , listOfLabels , get_labelNearest=get_labelNearest_py , get_distance=get_distance_np )
labels_by_npbatch = get_listOfNearestLabels_np( unlabeledAttrs , listOfLabeledAttrs , listOfLabels )
#print 'py' + str( labels_by_pybatch )
print 'np' + str( labels_by_npbatch )
#if labels_by_pybatch == labels_by_npbatch:
#    print 'pybatch and npbatch give same result.'



interval_1_to_1000 = [1,2,5,10,20,50,100,200,500,1000]
interval_10_to_50 = [10,20,50]
#numberOfAttrsPerEntity = interval_1_to_1000 # formerly called d.
#numberOfLabeledEntities = 100 # formerly called N.
#numberOfUnlabeledEntities = 100 # formerly called M.
#
#timesForGettingNearestLabels = []
#
#for numberOfAttrs in numbersOfAttrs:
#    unlabeledAttrs,labeledAttrs,labels = data.toy(numberOfAttrsWithLabel,numberOfAttrsWithoutLabel,numberOfAttrs)
#    
#    timeStart = time.clock()
#    get_listOfNearestLabels( unlabeledAttrs,labeledAttrs,labels )
#    timeEnd = time.clock()
#
#    timesForGettingNearestLabels += [timeEnd-timeStart]
#
#plt.figure(figsize=(5,3))
#plt.plot(numbersOfAttrs,timesForGettingNearestLabels,'-o')
#plt.xscale('log');plt.yscale('log'); plt.xlabel('number of attrs'); plt.ylabel('time for finding nearest labels'); plt.grid(True)
#
#
#
#
#
#numbersOfAttrs = 


#numberOfAttrsPerEntity = 100 # formerly called d.
#numbersOfLabeledEntities = interval_1_to_1000 # formerly called N.
#numberOfUnlabeledEntities = 100 # formerly called M.


#timesForGettingNearestLabels_np = []
#timesForGettingNearestLabels_map = []
#timesForGettingNearestLabels_py = []
#
#for numberOfLabeledEntities in numbersOfLabeledEntities:
#    unlabeledAttrs,labeledAttrs,labels = data.toy(numberOfLabeledEntities,numberOfUnlabeledEntities,numberOfAttrsPerEntity)
#    
#    timeStart_np = time.clock()
#    get_listOfNearestLabels_py( unlabeledAttrs,labeledAttrs,labels, get_labelNearest=get_labelNearest_np , get_distance=get_distance_np  )
#    timeEnd_np = time.clock()
#
#    timesForGettingNearestLabels_np += [ timeEnd_np - timeStart_np ]
#
#    timeStart_map = time.clock()
#    get_listOfNearestLabels_py( unlabeledAttrs,labeledAttrs,labels, get_labelNearest=get_labelNearest_map , get_distance=get_distance_np  )
#    timeEnd_map = time.clock()
#
#    timesForGettingNearestLabels_map += [ timeEnd_map - timeStart_map ]
#
#    timeStart_py = time.clock()
#    get_listOfNearestLabels_py( unlabeledAttrs,labeledAttrs,labels, get_labelNearest=get_labelNearest_py , get_distance=get_distance_np  )
#    timeEnd_py = time.clock()
#
#    timesForGettingNearestLabels_py += [ timeEnd_py - timeStart_py ]
#        
#plt.figure(figsize=(5,3))
#plt.plot(numbersOfLabeledEntities,timesForGettingNearestLabels_py,'-o',label='py')
#plt.plot(numbersOfLabeledEntities,timesForGettingNearestLabels_np,'-o',label='np')
#plt.plot(numbersOfLabeledEntities,timesForGettingNearestLabels_map,'-o',label='map')
#plt.xscale('log');plt.yscale('log'); plt.xlabel('number of attrs per entity'); plt.ylabel('time'); plt.grid(True); plt.legend( bbox_to_anchor=(1.00, 1.00), loc=2, borderaxespad=0. )



### TASK 3 ###

"""
numberOfAttrsPerEntity = 100 # formerly called d.
numberOfLabeledEntities = 100 # formerly called N.
numbersOfUnlabeledEntities = interval_1_to_1000 # formerly called M.


timesForGettingNearestLabels_np = []
#timesForGettingNearestLabels_map = []
timesForGettingNearestLabels_py = []

for numberOfUnlabeledEntities in numbersOfUnlabeledEntities:
    unlabeledAttrs,labeledAttrs,labels = data.toy(numberOfLabeledEntities,numberOfUnlabeledEntities,numberOfAttrsPerEntity)
    
    timeStart_np = time.clock()
    get_listOfNearestLabels_np( unlabeledAttrs,labeledAttrs,labels, get_labelNearest=get_labelNearest_np , get_distance=get_distance_np  )
    timeEnd_np = time.clock()

    timesForGettingNearestLabels_np += [ timeEnd_np - timeStart_np ]

#    timeStart_map = time.clock()
#    get_listOfNearestLabels_py( unlabeledAttrs,labeledAttrs,labels, get_labelNearest=get_labelNearest_map , get_distance=get_distance_np  )
#    timeEnd_map = time.clock()
#
#    timesForGettingNearestLabels_map += [ timeEnd_map - timeStart_map ]

    timeStart_py = time.clock()
    get_listOfNearestLabels_py( unlabeledAttrs,labeledAttrs,labels, get_labelNearest=get_labelNearest_np , get_distance=get_distance_np  )
    timeEnd_py = time.clock()

    timesForGettingNearestLabels_py += [ timeEnd_py - timeStart_py ]
        
plt.figure(figsize=(5,3))
plt.plot(numbersOfUnlabeledEntities,timesForGettingNearestLabels_py,'-o',label='py')
plt.plot(numbersOfUnlabeledEntities,timesForGettingNearestLabels_np,'-o',label='np')
#plt.plot(numbersOfLabeledEntities,timesForGettingNearestLabels_map,'-o',label='map')
plt.xscale('log');plt.yscale('log'); plt.xlabel('number of attrs per entity'); plt.ylabel('time'); plt.grid(True); plt.legend( bbox_to_anchor=(1.00, 1.00), loc=2, borderaxespad=0. )
"""