def neighbor_is_available( directionOfConnection , curState , dict_stateNow_to_statesPossNext ):
    dict_directionOfConnection_to_incrementOrdNeighbor = 
    incrementOrdNeighbor =  dict_directionOfConnection_to_incrementOrdNeighbor[ directionOfConnection ]
    possNextStates = dict_stateNow_to_statesPossNext[ curState ]    
    ordsPossNextStates = [ ord(possNextState) for possNextState in possNextStates ]
    ordNeighbor = ord(curState) +incrementOrdNeighbor
    neighborIsAvailable = ordNeighbor in ordsPossNextStates
    return neighborIsAvailable
    

#        upAvail    = neighbor_is_available('up'   ,stateNow,dict_stateNow_to_statesPossNext)
#        downAvail  = neighbor_is_available('down' ,stateNow,dict_stateNow_to_statesPossNext)
#        leftAvail  = neighbor_is_available('left' ,stateNow,dict_stateNow_to_statesPossNext)
#        rightAvail = neighbor_is_available('right',stateNow,dict_stateNow_to_statesPossNext)
#    
#        vertAvail = upAvail or downAvail
#        horAvail = leftAvail or rightAvail
#    
#        if vertAvail and horAvail :


for curState in states:
    
    if isCornerState( curState ):
        possNextStates = dict_stateNow_to_statesPossNext[ curState ]
        prob = 1.0 / len( possNextStates )
        for possNextState in possNextStates:
            tMat_weightedProbs[ ord(curState)-ord('A'), ord(possNextState)-ord('A') ] = prob
    else:
        probs = [1/3, 1/2, 1/6]
        possNextStates = dict_stateNow_to_statesPossNext[curState]
        possNextStates_and_theirProbs = zip( possNextStates, probs )
        for possNextState_and_itsProb in possNextStates_and_theirProbs:
            possNextState = possNextState_and_itsProb[0]
            prob = possNextState_and_itsProb[1]
            tMat_weightedProbs[ ord(curState)-ord('A') , ord(possNextState)-ord('A')] = prob
#print(t)
print 'utils weighted = '
result = utils.getstationary(tMat_weightedProbs)
print result
