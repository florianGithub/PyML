%matplotlib inline
# List of states
S = 'ABCDEFGH'

# Set of transitions
T = {'A':'BE','B':'AFC','C':'BGD','D':'CH','E':'AF','F':'EBG','G':'FCH','H':'GD'}
import random
def fraction_of_time(S, T, iterations):
    states = S[0]
    # simulate the experiment and run it for 1999 iterations.
    for i in range(iterations):
        next_state = random.choice(T[states[i]]) #state[i] is the current state
        states += next_state
    
    # compute the fraction of the time of each state
    counter = {S[i]:0.0 for i in range(len(S))}
    for i in range(len(states)):
        counter[states[i]] = counter[states[i]] + 1
    fractions = list(map(lambda x: x[1] / len(states), counter.items()))
    '''
    # testing
    for i in counter.items():
        print(i)
    print(fractions)
    '''
    return states, fractions
### solutions.exercise1a()
random.seed(123)
states, fractions = fraction_of_time(S, T, 2000)
# print the first 400 states of the simulation
print(states[0:100])
print(states[100:200])
print(states[200:300])
print(states[300:400])
### solutions.exercise1b()
import matplotlib
from matplotlib import pyplot as plt
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'png')
plt.rcParams['savefig.dpi'] = 90

s_list = [S[i] for i in range(len(S))]
matplotlib.pyplot.bar(s_list, fractions, align='center', color='blue')

### solutions.exercise2()
T_modified = {'A':'BE','B':'AFC','C':'BGD','D':'CH','E':'AF','F':'E','G':'FCH','H':'GD'}
states2, fractions2 = fraction_of_time(S, T_modified, 2000)
matplotlib.pyplot.bar(s_list, fractions2, align='center', color='blue')
import numpy
def compute_trasition_matrix(states, transition):
    t = numpy.zeros([8,8])
    #mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    mapping = {states[i]:i for i in range(len(states))}
    for i in states:
        val = 1.0 / len(transition[i])
        for j in transition[i]:
            t[mapping[i], mapping[j]] = val
    #print(t)
    return t

### solutions.exercise3()
#A0 B1 C2 D3 E4 F5 G6 H7
#T = {'A':'BE','B':'AFC','C':'BGD','D':'CH','E':'AF','F':'EBG','G':'FCH','H':'GD'}
#T_modified = {'A':'BE','B':'AFC','C':'BGD','D':'CH','E':'AF','F':'E','G':'FCH','H':'GD'}
import utils

t_matrix1 = compute_trasition_matrix(S, T)
result = utils.getstationary(t_matrix1)
print("Exercise 1 [", end=' ')
for i in result:
    print("{:4.2f}".format(i), end=' ')  #format specifier usage "{[tuple_index]:[width][.precision][type]}"
print("]")

t_matrix2 = compute_trasition_matrix(S, T_modified)
result = utils.getstationary(t_matrix2)
print("Exercise 2 [",end=' ')
for i in result:
    print("{:4.2f}".format(i), end=' ')
print("]")

### solutions.exercise4()
### T = {'A':'BE','B':'AFC','C':'BGD','D':'CH','E':'AF','F':'EBG','G':'FCH','H':'GD'}
t = numpy.zeros([8,8])
#mapping = {states[i]:i for i in range(len(states))} #use ord() instead
for i in S:
    if i in "AEDH":
        val = 1.0 / len(T[i])
        for j in T[i]:
            t[ord(i)-ord('A'), ord(j)-ord('A')] = val
    else:
        val = [1/3, 1/2, 1/6]
        for j in zip(T[i], val):
            t[ord(i)-ord('A'), ord(j[0])-ord('A')] = j[1]
#print(t)
result = utils.getstationary(t)
print("[",end='')
for i in result:
    print("{:5.2f}".format(i), end=' ')
print("]")
