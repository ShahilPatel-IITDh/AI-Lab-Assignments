import sys
from queue import PriorityQueue
import copy
import time

class Blocks:

    def __init__(self,s1,s2,s3,parent = None, heuristic = None):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.parent = parent
        self.heuristic = heuristic

    def stack_set(self):
        return [self.s1,self.s2,self.s3]

    #print  function

    def Print(self):

        print(self.s1)
        print(self.s2)
        print(self.s3)

    def __eq__(self, Temp):
       
        if not isinstance(Temp, Blocks):
            return NotImplemented

        return self.s1 == Temp.s1 and self.s2 == Temp.s2 and self.s3 == Temp.s3

    def __lt__(self, Temp):
        return None

#Move Gen Function for state transition

def MoveGen(current_state):

    neighbors=[]
   
    if current_state.s1:        #if current state is in s1
        new_state = copy.deepcopy(current_state) 
        temp = new_state.s1.pop()    
        new_state.s2.append(temp)    
        neighbors.append(new_state)    
       
        new_state = copy.deepcopy(current_state)
        temp = new_state.s1.pop()
        new_state.s3.append(temp)
        neighbors.append(new_state)
    
    if current_state.s2:        #if current state is in s2 
        new_state = copy.deepcopy(current_state)
        temp = new_state.s2.pop()
        new_state.s1.append(temp)
        neighbors.append(new_state)
      
        new_state = copy.deepcopy(current_state)
        temp = new_state.s2.pop()
        new_state.s3.append(temp)
        neighbors.append(new_state)
    
    if current_state.s3:
        new_state = copy.deepcopy(current_state)
        temp = new_state.s3.pop()
        new_state.s1.append(temp)
        neighbors.append(new_state)
       
        new_state = copy.deepcopy(current_state)
        temp = new_state.s3.pop()
        new_state.s2.append(temp)
        neighbors.append(new_state)
    
    return neighbors


#Goal Test function

def GoalTest(current_state,goal_state):
    
    if current_state.s1 != goal_state.s1:
        return False
    
    if current_state.s2 != goal_state.s2:
        return False
    
    if current_state.s3 != goal_state.s3:
        return False

    return True

#Heuristic functions

def Heuristic_S1(current_state,goal_state):    #Heuristic for stack 1
    h = 0                 
    
    for stack, goal_stack in zip(current_state.stack_set(),goal_state.stack_set()):   #initializing a for loop for current state in the object set of state for goal state and current state        
        
        for block in stack:      #for loop within the stack (from previous for loop)
            
            g_index = None
            
            try:        #try and except for exception handling , minimizing the error

                #try statement run when the conditions are pre-defined

                g_index = goal_stack.index(block)       #index of goal stack
                index = stack.index(block)              #index of stack
                
                if index == 0 and g_index==0: 
                    h+=1
               
                elif index>=1 and stack[index-1] == goal_stack[g_index-1]: 
                    h+=1
                
                else:
                    h-=1
            
            except:
                h-=1
    return h

def Heuristic_S2(current_state,goal_state):     #heuristic for stack 2
    
    h = 0  

    for stack, goal_stack in zip(current_state.stack_set(),goal_state.stack_set()):
        
        index = 0
        test = 0
        
        for block in stack:
           
            try:            #if the goal state has a block
                g = goal_stack[index]
           
            except:         #if goal state has no block
                g = None
           
            
            if test == 1:    
                h-=1*(index+1)
           
            elif block == g and test!=1:     #if on correct structure
                h+=1*(index+1)
            
            else: 
                h-=1*(index+1)
                test = 1
            index+=1
    return h


def Heuristic_S3(state,goal_state):    #Heuristic for stack 3
    
    h = 0  
    
    for stack, goal_stack in zip(state.stack_set(),goal_state.stack_set()):#parallel loop through state and goal state stacks of block
        
        index = 0
        test = 0
        
        for block in stack:
           
            try:# if a goal stack have  block
                g = goal_stack[index]
            
            except:# if a goal stack does not have block
                g = None
            
            if test == 1:#if structure below is incorrect
                h-=1*(len(stack)-index)
            
            elif block == g and test!=True:#if on correct structure
                h+=1*(len(stack)-index)
            
            else:#if on incorrect structure
                h-=1*(len(stack)-index)
                test = 1
            index+=1
    return h


def Not_Explored(current_state,explored,open):
    
    for i in explored:# check in explored
        if i.s1 == current_state.s1 and i.s2 == current_state.s2 and i.s3 == current_state.s3:
            return False
    
    for (h,i) in open:# check in open
        if i.s1 == current_state.s1 and i.s2 == current_state.s2 and i.s3 == current_state.s3:
            return False

    return True         # return true if the state is not explored



#Function for Path tracking

def Track_Path(path,state):
    
    path.append(state)
    
    if state.parent == None:        #base case
        return
    else:
        Track_Path(path,state.parent)  # find path recursively


#Best_First_Search

def Best_First_Search(initial_state,goal_state):
    
    Qu = PriorityQueue()
    explored=[]                     #array to store the explored states
    h = (Heuristic_S3(goal_state,goal_state) - Heuristic_S3(initial_state,goal_state))
   
    Qu.put((h,initial_state))
    
    while not Qu.empty():
        h,state = Qu.get()     # get head element from priority queue
        explored.append(state)
        
        if GoalTest(state,goal_state):# check for goal state
            path=[]
            Track_Path(path,state)
            output.write("States present in path: "+str(len(path))+"\n")
            output.write("Explored states:  "+str(len(explored))+"\n")
            
            for i in reversed(path):
                for j in i.stack_set():
                    output.write(str(j)+"\n")
                output.write("\n")
            return True
        
        for neighbor in MoveGen(state):
            if Not_Explored(neighbor,explored,Qu.queue):
                h = (Heuristic_S3(goal_state,goal_state)-Heuristic_S3(neighbor,goal_state))
                neighbor.parent = state         # set parent
                Qu.put((h,neighbor))
    return False


def Hill_Climb(initial_state,goal_state):     #Hill Climbing search
    
    next_state=[]
    h = (Heuristic_S3(goal_state,goal_state)-Heuristic_S3(initial_state,goal_state))      #calculate heuristics
    
    initial_state.heuristic = h
   
    next_state.append(initial_state)
   
    local_maxima = 0          #Variable to check whether the state reached local maxima or not 
    
    while (local_maxima == 0):
        
        state = next_state[-1]
       
        if GoalTest(state,goal_state):  # check for goal state
            path=[]
            Track_Path(path,state)
            output.write("States present in path: "+str(len(path))+"\n")
            output.write("Explored states: "+str(len(next_state))+"\n")
           
            for i in reversed(path):
                for j in i.allstack():
                    output.write(str(j)+"\n")
                output.write("\n")
            return True
        min = state

        for neighbor in MoveGen(state):
            h = (Heuristic_S3(goal_state,goal_state)-Heuristic_S3(neighbor,goal_state))
            neighbor.parent = state
            neighbor.heuristic = h
            if neighbor.heuristic < min.heuristic:
                min = neighbor
        next_state.append(min)          #it is minimum heuristic value of the stack 
       
        if min == state:
            local_maxima = 1
    
    path=[]

    Track_Path(path,state)                 # get path which is expored if the transition is stuck on local maxima
    
    output.write("States present in path: "+str(len(path))+"\n")
    output.write("Explored states: "+str(len(next_state))+"\n")
    
    for i in reversed(path):
        for j in i.stack_set():
            output.write(str(j)+"\n")
        output.write("\n")
    output.write("The state is stuck in local maxima")
    return False

    


filename = open(sys.argv[1], "r")       #opening file in read mode

file_code = filename.readline().strip()    #1 for BFS and 2 for Hill Climb

stack1 = list(filename.readline().strip().split())
stack2 = list(filename.readline().strip().split())
stack3 = list(filename.readline().strip().split())

initial_state = Blocks(stack1,stack2,stack3)

stack1 = list(filename.readline().strip().split())
stack2 = list(filename.readline().strip().split())
stack3 = list(filename.readline().strip().split())

goal_state = Blocks(stack1,stack2,stack3)

output = open("output.txt", "w+")


if file_code=='1':
    time_stamp = time.time()
    Best_First_Search(initial_state,goal_state)
    print("Time taken for Best First Search: ",time.time() - time_stamp)

elif file_code=='2':
    time_stamp = time.time()
    Hill_Climb(initial_state,goal_state)
    print("Time taken for Hill Climb ALgorithm: ",time.time() - time_stamp)
