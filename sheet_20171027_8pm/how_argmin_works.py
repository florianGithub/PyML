import numpy as np

indexAxisRow = 0
indexAxisCol = 1

row1 = [-1,-6]
row2 = [-7,-3]
row3 = [-5,-2]

matrix = np.matrix([row1,row2,row3])

print 'indexOfMinInFlattenedMatrix = '+str(np.argmin(matrix))
print 'indexOfMaxInFlattenedMatrix = '+str(np.argmax(matrix))

indexToVaryForFindingExtremum = indexAxisRow

print 'indexOfMinOfEachCol = '+str(np.argmin(matrix,axis=indexToVaryForFindingExtremum))
print 'indexOfMaxOfEachCol = '+str(np.argmax(matrix,axis=indexToVaryForFindingExtremum))

indexToVaryForFindingExtremum = indexAxisCol

print 'indexOfMinOfEachRow = '+str(np.argmin(matrix,axis=indexToVaryForFindingExtremum))
print 'indexOfMaxOfEachRow = '+str(np.argmax(matrix,axis=indexToVaryForFindingExtremum))