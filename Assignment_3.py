import sys
import copy
import random
from collections import Counter
from itertools import combinations
import operator


class Stage:

    def __init__(self,positions,parent = None, heuristic = None,storage = None):
        self.positions = positions
        self.parent = parent
        self.heuristic = heuristic
        self.storage = storage

    def __eq__(self, other):       #it is used specially to compare the positions of stages and it will be called when the program finds '==' sign
        if not isinstance(other, Stage):
            return NotImplemented

        return self.positions == other.positions      #if the position of object is equal to the other stage's position 
      

# Vector in senior = positions in our assignment

def negative(literal):

    if literal == 'a':
        return '~a'

    elif literal == '~a':
        return 'a'

    elif literal == 'b':
        return '~b'

    elif literal == '~b':
        return 'b'

    elif literal == 'c':
        return '~c'

    elif literal == '~c':
        return 'c'

    elif literal == '~d':
        return 'd'

    elif literal == 'd':
        return '~d'


def tautology(clause):

    for literal in clause:

        if negative(literal) in clause:     #if negation of any literal is present in clause then it is tautology
            return True

        return False

def repetition(clause):
    
    for i in formula:
        if Counter(clause) == Counter(i):   #check whether the formula is repeated or not
            return True

    return False

def inverter(value):    #function to invert the value of given bit
    
    if value == 0:
        return 1
    else:
        return 0


def getDirections(positions):      # map the literals to its value
    
    dict = {}                    #creation of a dictionary named dict
    
    dict['a'] = positions[0]
    dict['~a'] = inverter(positions[0])

    dict['b'] = positions[1]
    dict['~b'] = inverter(positions[1])

    dict['c'] = positions[2]
    dict['~c'] = inverter(positions[2])

    dict['d'] = positions[3]
    dict['~d'] = inverter(positions[3])

    return dict

def heuristic_calc(stage):

    dict = getDirections(stage.positions)
    answer=0

    for a in formula:    #Variable a represent clause
        answer += dict[a[0]] or dict[a[1]] or dict[a[2]]
        
    return answer


def Goal_Test(stage):
    if stage.heuristic == clause:    #goal state is achieved when the heuristic is equal to no. of clause
        return True
    return False

def MoveGen(current_stage,r,tt=None):
    if tt:
        neighbor = []
        indices = [0,1,2,3]
        comb = combinations(indices,r)   #choose r from the list of indices
        for c in list(comb):
            new_stage = copy.deepcopy(current_stage)    #create a new state such that it is coppy of current stage
            for index in c:
                
                if new_stage.storage[index] == 0:  #invert if the storage is empty
                    new_stage.positions[index] = inverter(new_stage.positions[index]) # invert that chosen bit
                    new_stage.storage[index] = tt # set the tt value in memory
                    for i in [item for item in indices if item not in [index]]:
                        new_stage.memory[i] = max(0,new_stage.memory[i]-1)  # decrease other tt value in memory
                    neighbor.append(new_stage)
        return neighbor

    neighbor_list = []
    indices = [0,1,2,3]
    comb = combinations(indices,r)          # choose r number from the indices list

    for combination in list(comb):
        new_stage = copy.deepcopy(current_stage)        # create a copy of current_stage in new stage

        for index in combination:
            new_stage.positions[index] = inverter(new_stage.positions[index])     # invert the bits of new stage and store it in new state list
       
        neighbor_list.append(new_stage)
    
    return neighbor_list


def Not_Visited(stage,explored,open):
    
    for i in explored:          # check in explored list 
        if i.positions == stage.positions:  #if present in explored list then return false
            return False

    for i in open:              # check in open list
        if i.positions == stage.positions:     #if present in open list then return false
            return False

    return True                 # return true if not visited


def Not_Visited_tabu(stage,explored):
    
    for i in explored:
        if i.positions == stage.positions:
            return False
        
    return True


def Path_Tracker(path,stage):

    path.append(stage.positions)
    if path.parent == None:
        return
    else:
        Path_Tracker(path,stage.parent)     #recursive call to Path Tracker function to get the path





# Main Function / driver code

literals = 4     #here literals is no. of literals or n as given in question
clause = 5     #clause is the no. of clause or 'k' as given in question

possibilities = ['a','~a','b','~b','c','~c','d','~d']
combination = []
formula = []
for i in range(clause):
    reject = 1
    while(reject):
        RandomClause=[random.choice(possibilities) for j in range(3)]  #generate random clause

        if (not tautology(RandomClause)) and (not repetition(RandomClause) and (len(set(RandomClause)) == len(RandomClause))):   # check if it is allowed
            reject = 0
            
    formula.append(RandomClause)
#create a file to store the formula which is generated randomly

file1 = open("formula_1.txt","w")

for clause in formula:
    file1.write(str(clause)+"\n")   #writing the randomly generated formula in file

output = open("output.txt","w+")

start_stage = Stage([0,0,0,0])   #initializing the initial / start state

file_code = int(sys.argv[1])
if file_code == 0:
   # VND(start_stage)

elif file_code == 1:
   # BEAM(start_stage) 

elif file_code == 2:
