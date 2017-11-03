import utils
import random
import matplotlib.pyplot as plt
import numpy as np

# List of states
S = 'ABCDEFGH'
# Set of transitions
T = {'A':'BE','B':'AFC','C':'BGD','D':'CH','E':'AF','F':'EBG','G':'FCH','H':'GD'}

#substitute meaningless variable names with meaningful variable names. start.
states = list(S)
dict_stateNow_to_statesPossNext = T
#substitute meaningless variable names with meaningful variable names. stop.

def getNextState(curState,dict_stateNow_to_statesPossNext):
    key = curState    
    value = dict_stateNow_to_statesPossNext[key]
    statesPossNext = list(value)
    nextState = random.choice( statesPossNext )
    return nextState

stateStart = 'A'

random.seed(123)
nRuns = 1999

statesOverTime = [ stateStart ]

for iRun in range(nRuns):
    curState = statesOverTime[ -1 ]
    nextState = getNextState(curState,dict_stateNow_to_statesPossNext)
    statesOverTime.append(nextState)
    
statesOverTime_roleModel = 'ABABAEFBAEFBFEFBAEFEFGFEABCGFGHGHGCGHGCDHDHDHGHGFGFGHDCGCBFBFEFBABAEAEAEAEFBAEFG\
FEFEFEFBABFEFEABCGHGCDCGCDHGHDCBAEFBFEAEABAEAEABABCGHDHDCDCGHDCGCGHGFBABFGFEFGHG\
CBABFGHDHGHDCDHGCBFEAEAEFGFEABCGCDCDHGHGCGHGCGHGFGFGFBAEABFEFBAEAEFGFEAEFEABCDCD\
CDHDCGHGCDCBABFBFEFBCDHGHGFEFBABCBCGHGCDCGCBABAEFGFBFEAEABABAEABABABAEFBFGCBAEAB\
FGCBFEFGFGHDCBCDCBFGFGFEFBCGFEFEABCDHGCDCBABCDCBCBAEAEAEABFGCGHDHGHGCDHGHDCBFGFB'

statesOverTime_concatenated = ''.join(statesOverTime[0:400])
print statesOverTime_concatenated
print 'len(statesOverTime_concatenated) = ' + str(len(statesOverTime_concatenated))
print 'len(statesOverTime_roleModel)    = ' + str(len(statesOverTime_roleModel))
print 'our solution is matching role model = '+str( statesOverTime_roleModel == statesOverTime_concatenated )

fracsOfTimeStateXAccepted = [ statesOverTime.count(state)/float(len(statesOverTime)) for state in states ]
plt.bar( range(len(states)) , fracsOfTimeStateXAccepted )


dict_stateNow_to_statesPossNext_specialStateF = {'A':'BE','B':'AFC','C':'BGD','D':'CH','E':'AF','F':'E','G':'FCH','H':'GD'}
#dict is called by reference. thus no simple copying of the dict to create two copies.

statesOverTime_specialStateF = [stateStart]

for iRun in range(nRuns):
    curState = statesOverTime_specialStateF[ -1 ]
    nextState = getNextState(curState,dict_stateNow_to_statesPossNext_specialStateF)
    statesOverTime_specialStateF.append(nextState)
    
fracsOfTimeStateXAccepted = [ statesOverTime_specialStateF.count(state)/float(len(statesOverTime_specialStateF)) for state in states ]
plt.bar( range(len(states)) , fracsOfTimeStateXAccepted )


# transition matrix contains probability to transit from state indexRow to state indexCol.
def getProbsToAcceptStateC_after_stateR( stateR , dict_stateNow_to_statesPossNext ):
    stateNow = stateR
    statesPossNext = dict_stateNow_to_statesPossNext[stateNow]
    prob = 1./len(statesPossNext)
    indicesStatesPossNext = [ states.index( statePossNext ) for statePossNext in statesPossNext ]
    tMatRow = np.zeros(len(states))
    tMatRow[indicesStatesPossNext] = np.ones(len(indicesStatesPossNext)) * prob
    return tMatRow

listOfTMatRows = [ getProbsToAcceptStateC_after_stateR( state , dict_stateNow_to_statesPossNext ) for state in states ]
tMat = np.matrix( listOfTMatRows )
print tMat
print 'tMat row\'s sum = '
print tMat.sum(axis=1)
print 'utils = '
print utils.getstationary(tMat)

tMat_specialStateF = np.matrix( [ getProbsToAcceptStateC_after_stateR( state , dict_stateNow_to_statesPossNext_specialStateF ) for state in states ] )
print tMat_specialStateF
print 'tMat_specialStateF row\'s sum = ' 
print tMat_specialStateF.sum(axis=1)
print 'utils = '
print utils.getstationary(tMat_specialStateF)