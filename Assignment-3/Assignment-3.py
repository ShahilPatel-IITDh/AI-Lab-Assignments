import sys
import random
import copy
from collections import Counter
from itertools import combinations
import operator


class Stage:

    def __init__(self,positions,parent = None, heuristic = None,storage = None):
        self.positions = positions
        self.parent = parent
        self.heuristic = heuristic
        self.storage = storage

    def __eq__(self, other):
        if not isinstance(other, Stage):
            return NotImplemented
        
        return self.positions == other.positions

def Inverter(literal):
    
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
        if Inverter(literal) in clause: #if negation of any literal is present then it is tautology
            return 1
    
    return 0

def repetition(clause):
   
    for f in formulas:
        if Counter(clause) == Counter(f): #check if this clause is already present in the formula
            return 1
    return 0

def invert(bit):
    if bit == 1:
        return 0
    else:
        return 1

def Mapper(positions):  # map the literals to its value
    
    dict = {}      #initialize empty dictionary
   
    dict['a'] = positions[0]
    dict['~a'] = invert(positions[0])
    
    dict['b'] = positions[1]
    dict['~b'] = invert(positions[1])
    
    dict['c'] = positions[2]
    dict['~c'] = invert(positions[2])
    
    dict['d'] = positions[3]
    dict['~d'] = invert(positions[3])
    
    return dict

def heuristic_calc(state): # heuristic for number of clauses satisfied
    
    dict = Mapper(state.positions)
    result = 0
    
    for clause in formulas:
        result += dict[clause[0]] or dict[clause[1]] or dict[clause[2]]
    
    return result

def Goal_Test(state):
    
    if state.heuristic == clauses: # goal state when heuristic is equal to number of clauses
        return 1
    return 0


def Move_Gen(node,r,tt=None):
   
    if tt:
        neighbor_list = []
        indices = [0,1,2,3]
        comb = combinations(indices,r) 
        
        for c in list(comb):
            new_state = copy.deepcopy(node) # create a copy as new_state
        
            for index in c:
                if new_state.storage[index] == 0: # only invert if memory value is zero
                    new_state.positions[index] = invert(new_state.positions[index]) # invert that choosen bit
                    new_state.storage[index] = tt # set the tt value in memory
        
                    for i in [item for item in indices if item not in [index]]:
                        new_state.storage[i] = max(0,new_state.storage[i]-1) # decrease other tt value in memory
                    neighbor_list.append(new_state)
        
        return neighbor_list

    neighbor_list = []
    indices = [0,1,2,3]
    comb = combinations(indices,r) 
    
    for combination in list(comb):
        new_state = copy.deepcopy(node) # create a copy as new_state
       
        for index in combination:
            new_state.positions[index] = invert(new_state.positions[index])   #invert the bit at given index
        neighbor_list.append(new_state)
   
    return neighbor_list

def Not_Visited(state,explored,open):
    
    for i in explored:     #checking in explored list
        
        if i.positions == state.positions:     #if positons of i and state match return 0
            return 0

    for i in open:         #checking in open list
       
        if i.positions == state.positions:      #if positions of i and state match return 0
            return 0
    
    return 1 # return true if not visited

def Not_Visited_Tabu(state,explored):
    for i in explored:# check in explored
        if i.positions == state.positions:
            return 0
    return 1

def Path_Track(path,state):
    
    path.append(state.positions)
    
    if state.parent == None:            #if the state has no parent state
        return
    else:
        Path_Track(path,state.parent)# recursively find path


def Not_Explored(state,explored):
    
    for i in explored:          #check in explored list 
        if i.positions == state.positions:     #if postions of i is equal to positions of state then return 0
            return 0
   
    return 1

#VND function 

def VND(initial_state):
   
    initial_state.heuristic = heuristic_calc(initial_state)# calculate heuristic
    next_state=[initial_state]
   
    local_maxima = 0
    r = 1 
    
    while 1:
       
        current_state = next_state[-1]
        
        if Goal_Test(current_state):  #check if current_state is the goal state
            path=[]
            Path_Track(path,current_state)
            output.write("States in path are: "+str(len(path))+"\n")
            output.write("Explored states are: "+str(len(next_state))+"\n")
            for i in reversed(path):
                output.write(str(i)+"\n")
            return 1
        max = current_state
        
        for neighbor in Move_Gen(current_state,r):  # find neighbors of current state
            neighbor.parent = current_state  #now assign value of current state to parent of neighbor
            neighbor.heuristic = heuristic_calc(neighbor)
            if neighbor.heuristic > max.heuristic:
                max = neighbor
        
        if Not_Explored(max,next_state):
            next_state.append(max) 
        
        if max == current_state:
            r = min(4,r+1)   #take minimum of 4 and r+1
    return 0

#BEAM function

def BEAM(initial_state,width):
    
    initial_state.heuristic = heuristic_calc(initial_state)
    open = [initial_state] # initial open list with initial state
    explored = []
    
    while open:
        temp = []
        
        for node in open: #explored width number of node in open
            explored.append(node)
            
            if Goal_Test(node): # check for goal state
                
                path = []
                Path_Track(path,node)
                output.write("States in path are: "+str(len(path))+"\n")
                output.write("Explored states are: "+str(len(explored))+"\n")
                
                for i in reversed(path):
                    output.write(str(i)+"\n")
                return 1
            
            neighbors = Move_Gen(node,1) # get neighbor, r = 1 (perturb only 1 bit)
            
            for neighbor in neighbors:
                
                if Not_Visited(neighbor,explored,open): # if not explored
                    neighbor.heuristic = heuristic_calc(neighbor)
                    neighbor.parent = node
                    temp.append(neighbor) # store all neighbor in temp
        
        current = open[0]
        open.clear()
        open = open + temp  #append temp to open
        open.sort(key = operator.attrgetter('heuristic'),reverse=True) #  then sort the list using heuristic value
        
        open = open[:width] # keep only width number of nodes
       
        if len(open)==0: # boundary case when width is zero
            output.write("0 width")
            return 0
       
        if current.heuristic >= open[0].heuristic: # when stuck in local maxima
            path = []
            Path_Track(path,current)
            output.write("States in path are: "+str(len(path))+"\n")
            output.write("Explored states are:  "+str(len(explored))+"\n")
            
            for i in reversed(path):
                output.write(str(i)+"\n")
            output.write("State is stuck in local maxima")
            
            return 0
    return 0

#TABU function

def TABU(initial_state,tt):
   
    initial_state.heuristic = heuristic_calc(initial_state)
    
    initial_state.storage = [0,0,0,0] # initialize the memory vector
    
    next = initial_state # start the next state as initial state
    explored = []
   
    while 1:
        explored.append(next)
       
        if Goal_Test(next): # check for goal state
            path = []
            Path_Track(path,next) # get path
            output.write("States in path are: "+str(len(path))+"\n")
            output.write("Explored states are: "+str(len(explored))+"\n")
    
            for i in reversed(path):
                output.write(str(i)+"\n")
            return 1
    
        current = next
        max = 0
        neighbors = Move_Gen(current,1,tt) 
       
        for n in neighbors:
            if Not_Visited_Tabu(n,explored):
                n.parent = current
                n.heuristic = heuristic_calc(n)
                if n.heuristic >= max: 
                    max = n.heuristic
                    next = n
        
        if not neighbors: 
            
            path = []
            Path_Track(path,next)
            output.write("States in path are: "+str(len(path))+"\n")
            output.write("Explored states are: "+str(len(explored))+"\n")
            
            for i in reversed(path):
                output.write(str(i)+"\n")
            
            output.write("Reduce the tt value")
            return 0
    
    return 0


literals = 4
clauses = 5
possibilities = ['a','~a','b','~b','c','~c','d','~d']
formulas = []

for clause in range(clauses):
    rejected = True
    while(rejected):
        random_clause = [random.choice(possibilities) for i in range(3)] 
        
        if (not tautology(random_clause)) and (not repetition(random_clause) and (len(set(random_clause)) == len(random_clause))): 
            rejected = False
    
    formulas.append(random_clause)

formula_file = open("formula.txt","w")

for clause in formulas:
    formula_file.write(str(clause)+'\n')


output = open("output.txt","w+")

start_stage = Stage([0,0,0,0]) #initializing the initial / start state

file_code = int(sys.argv[1])

if file_code == 0:
    VND(start_stage)

elif file_code== 1:
    TABU(start_stage,2)         # second argument is beam width

elif file_code == 2:
    BEAM(start_stage,2)     # second argument is tt value
