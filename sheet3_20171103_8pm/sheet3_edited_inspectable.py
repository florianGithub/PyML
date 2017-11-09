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
plt.figure('occurence of states usual case')
plt.bar( range(len(states)) , fracsOfTimeStateXAccepted )


dict_stateNow_to_statesPossNext_specialStateF = {'A':'BE','B':'AFC','C':'BGD','D':'CH','E':'AF','F':'E','G':'FCH','H':'GD'}
#dict is called by reference. thus no simple copying of the dict to create two copies.

statesOverTime_specialStateF = [stateStart]

for iRun in range(nRuns):
    curState = statesOverTime_specialStateF[ -1 ]
    nextState = getNextState(curState,dict_stateNow_to_statesPossNext_specialStateF)
    statesOverTime_specialStateF.append(nextState)
    
fracsOfTimeStateXAccepted = [ statesOverTime_specialStateF.count(state)/float(len(statesOverTime_specialStateF)) for state in states ]
plt.figure('occurence of states special case')
plt.bar( range(len(states)) , fracsOfTimeStateXAccepted )


# transition matrix contains probability to transit from state indexRow to state indexCol.
def getEquiProbsToAcceptStateC_after_stateR( stateR , dict_stateNow_to_statesPossNext ):
    stateNow = stateR
    statesPossNext = dict_stateNow_to_statesPossNext[stateNow]
    prob = 1./len(statesPossNext)
    indicesStatesPossNext = [ states.index( statePossNext ) for statePossNext in statesPossNext ]
    tMatRow = np.zeros(len(states))
    tMatRow[indicesStatesPossNext] = np.ones(len(indicesStatesPossNext)) * prob
    return tMatRow

listOfTMatRows = [ getEquiProbsToAcceptStateC_after_stateR( state , dict_stateNow_to_statesPossNext ) for state in states ]
tMat = np.matrix( listOfTMatRows )
print tMat
print 'tMat row\'s sum = '
print tMat.sum(axis=1)
print 'utils = '
print utils.getstationary(tMat)

tMat_specialStateF = np.matrix( [ getEquiProbsToAcceptStateC_after_stateR( state , dict_stateNow_to_statesPossNext_specialStateF ) for state in states ] )
print tMat_specialStateF
print 'tMat_specialStateF row\'s sum = ' 
print tMat_specialStateF.sum(axis=1)
print 'utils = '
print utils.getstationary(tMat_specialStateF)






### TASK 4 ###

dict_direction_to_ordIncrement = {'left':-1,'right':+1,'up':-4,'down':+4}
dict_ordIncrement_to_direction = { -1:'left' , +1:'right' , -4:'up' , +4:'down' , 0:'itself' }

def getDirection_from_ordIncrement( ordIncrement , dict_ordIncrement_to_direction ):
    if ordIncrement in dict_ordIncrement_to_direction.keys():
        direction = dict_ordIncrement_to_direction[ ordIncrement ]        
        return direction
    else:
        return 'unconnected'

# task one: get kindOfNodeNow
# task two: get prob of nodeNext from directionToNodeNext and kind of nodeNow

def getDirection_stateNow_to_stateNext( stateNow, stateNext , dict_ordIncrement_to_direction ):
    
    ordIncrement = ord(stateNext) - ord(stateNow)
    direction = getDirection_from_ordIncrement( ordIncrement , dict_ordIncrement_to_direction )
    return direction
    
def getProb_stateNow_to_stateNext( stateNow , stateNext , dict_stateNow_to_statesPossNext ):

    statesPossNext = dict_stateNow_to_statesPossNext[ stateNow ]

    hasTwoNeighbors   = len(statesPossNext) == 2
    hasThreeNeighbors = len(statesPossNext) == 3
    
    haveConnection = stateNext in statesPossNext    
    
    directionOfConnection = getDirection_stateNow_to_stateNext( stateNow, stateNext, dict_ordIncrement_to_direction )
    
    haveConnectionVert = directionOfConnection == 'up' or directionOfConnection == 'down'    
    haveConnectionHor  = directionOfConnection == 'left' or directionOfConnection == 'right'    
    
    if not haveConnection: return 0.
        
    if haveConnection and hasTwoNeighbors: return 1./2
            
    if haveConnection and hasThreeNeighbors and directionOfConnection=='left' : return 1./3                
    if haveConnection and hasThreeNeighbors and directionOfConnection=='right': return 1./6    
    if haveConnection and hasThreeNeighbors and haveConnectionVert: return 1./2

# transition matrix contains probability to transit from state indexRow to state indexCol.
def getRowOfTransitionMatrix( stateNow , states , dict_stateNow_to_statesPossNext ):        
    tMatRow = np.array( [ getProb_stateNow_to_stateNext( stateNow , stateNext , dict_stateNow_to_statesPossNext ) for stateNext in states ] )
    return tMatRow
        
    
listOfTMatRows_weighted = [ getRowOfTransitionMatrix( stateNow , states , dict_stateNow_to_statesPossNext ) for stateNow in states ]
prob_i1CurState_i2NextState = np.array( listOfTMatRows_weighted )
print prob_i1CurState_i2NextState
print 'tMat row\'s sum = '
print prob_i1CurState_i2NextState.sum(axis=1)
print 'utils = '
print utils.getstationary(prob_i1CurState_i2NextState)
    
### TASK 5 ###
    
nMarkovSteps = 500
#nScenarios = 7# determined by preprogrammed utils.getinitial().
prob_i1CurState_i2NextState_padded = np.pad( prob_i1CurState_i2NextState ,1,mode='constant')[1:-1,:-1]
cur_oneIfInState_i1Scenario_i2State = utils.getinitialstate()

for iMarkovStep in range(nMarkovSteps):
    #print cur_oneIfInState_i1Scenario_i2State
    #print ''
    next_oneIfInState_i1Scenario_i2State = utils.getNext_oneIfInState_i1Scenario_i2State( cur_oneIfInState_i1Scenario_i2State , prob_i1CurState_i2NextState_padded , iMarkovStep )
    cur_oneIfInState_i1Scenario_i2State = next_oneIfInState_i1Scenario_i2State

cur_state_i1scenarios = np.argmax( cur_oneIfInState_i1Scenario_i2State , axis=1 )
unique, counts = np.unique( cur_state_i1scenarios , return_counts=True)
print 'count of final state of all scenarios'
print counts
print 'fractions of final states of scenarios'   
print counts/float(len(cur_state_i1scenarios))
