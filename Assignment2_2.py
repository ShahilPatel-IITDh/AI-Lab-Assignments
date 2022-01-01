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

def Heuristic_S1(current_state,goal_state):    #Heuristic for stack 1
    h = 0                 
    
    for stack, goal_stack in zip(current_state.stack_set(),goal_state.stack_set()):
        
        for block in stack: 
            goal_index = None
            
            try:
                goal_index = goal_stack.index(block)    #index of goal stack
                index = stack.index(block)              #index of stack
                if index == 0 and goal_index==0: 
                    h+=1
               
                elif index-1>=0 and stack[index-1] == goal_stack[goal_index-1]: 
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
        test = False
        
        for block in stack:
            try:            #if the goal state has a block
                g = goal_stack[index]
           
            except:         #if goal state has no block
                g = None
           
            if test == True:    
                h-=1*(index+1)
           
            elif block == g and test!=True:     #if on correct structure
                h+=1*(index+1)
            
            else: 
                h-=1*(index+1)
                test = True
            index+=1
    return h


def Heuristic_S3(state,goal_state):    #Heuristic for stack 3
    
    h = 0  
    
    for stack, goal_stack in zip(state.stack_set(),goal_state.stack_set()):#parallel loop through state and goal state stacks of block
        index = 0
        test = False
        for block in stack:
           
            try:# if a goal stack have  block
                g = goal_stack[index]
            
            except:# if a goal stack does not have block
                g = None
            
            if test == True:#if structure below is incorrect
                h-=1*(len(stack)-index)
            
            elif block == g and test!=True:#if on correct structure
                h+=1*(len(stack)-index)
            
            else:#if on incorrect structure
                h-=1*(len(stack)-index)
                test = True
            index+=1
    return h


def Not_Explored(current_state,explored,open):
    
    for s in explored:# check in explored
        if s.s1 == current_state.s1 and s.s2 == current_state.s2 and s.s3 == current_state.s3:
            return False
    
    for (h,s) in open:# check in open
        if s.s1 == current_state.s1 and s.s2 == current_state.s2 and s.s3 == current_state.s3:
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
    
    open = PriorityQueue()
    explored=[]                     #array to store the explored states
    h = Heuristic_S3(goal_state,goal_state) - Heuristic_S3(initial_state,goal_state)
    open.put((h,initial_state))
    
    while not open.empty():
        h,state = open.get() # get head element from priority queue
        explored.append(state)
        
        if GoalTest(state,goal_state):# check for goal state
            path=[]
            Track_Path(path,state)
            output.write("States present in path: "+str(len(path))+"\n")
            output.write("Explored states:  "+str(len(explored))+"\n")
            
            for i in reversed(path):
                for s in i.stack_set():
                    output.write(str(s)+"\n")
                output.write("\n")
            return True
        
        for neighbor in MoveGen(state):
            if Not_Explored(neighbor,explored,open.queue):
                h = Heuristic_S3(goal_state,goal_state)-Heuristic_S3(neighbor,goal_state)
                neighbor.parent = state         # set parent
                open.put((h,neighbor))
    return False


def Hill_Climb(initial_state,goal_state):     #Hill Climbing search
    
    next_state=[]
    h = Heuristic_S3(goal_state,goal_state)-Heuristic_S3(initial_state,goal_state)      #calculate heuristics
    initial_state.heuristic = h
    next_state.append(initial_state)
    local_maxima = False
    
    while not local_maxima:
        state = next_state[-1]
       
        if GoalTest(state,goal_state):  # check for goal state
            path=[]
            Track_Path(path,state)
            output.write("States present in path: "+str(len(path))+"\n")
            output.write("Explored states: "+str(len(next_state))+"\n")
           
            for i in reversed(path):
                for s in i.allstack():
                    output.write(str(s)+"\n")
                output.write("\n")
            return True
        min = state
        
        for neighbor in MoveGen(state):
            h = Heuristic_S3(goal_state,goal_state)-Heuristic_S3(neighbor,goal_state)
            neighbor.parent = state
            neighbor.heuristic = h
            if neighbor.heuristic < min.heuristic:
                min = neighbor
        next_state.append(min)    #it is minimum heuristic value of the stack 
        if min == state:
            local_maxima = True
    
    path=[]

    Track_Path(path,state)                 # get path which is expored if the transition is stuck on local maxima
    
    output.write("States present in path: "+str(len(path))+"\n")
    output.write("Explored states: "+str(len(next_state))+"\n")
    
    for i in reversed(path):
        for s in i.allstack():
            output.write(str(s)+"\n")
        output.write("\n")
    output.write("stuck in local maxima")
    return False

    


filename = open(sys.argv[1], "r")

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
