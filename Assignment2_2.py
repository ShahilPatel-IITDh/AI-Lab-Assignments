import sys
from queue import PriorityQueue
import copy

data=[]

# Initializing Stacks for storing input

class Blocks:                   #Class Blocks to store the goal state, goal level.
    def __init__(self, label):
        self.label = label
        self.goal_state = None
        self.goal_level = None
    
    def __init__(self,stack1,stack2,stack3,parent=None,heuristic_function=None):    #To store stacks, its parent state and value of heuristic_function 
        self.stack1 = stack1
        self.stack2 = stack2
        self.stack3 = stack3
        self.parent = parent
        self.heuristic_function = heuristic_function


    def allstack(self):
        return [self.stack1,self.stack2,self.stack3]

    def Print(self):
        print(self.stack1)
        print(self.stack2)
        print(self.stack3)


#Function for moving the through different states

def MoveGen(current_state):
    Next=[]        #Array to store the states after the various transitions


    if current_state.stack1:            #if the current state is in the stack 1

        #Adding the top element of stack 1 to stack 2

        replica_state = copy.deepcopy(current_state)      # creating the newstate as replica of current_state
        top = replica_state.stack1.pop()    #remove top element from stack 1
        replica_state.stack2.append(top)    
        Next.append(replica_state)       

        #Adding the top element of stack 1 to stack 3

        replica_state = copy.deepcopy(current_state)
        top = replica_state.stack1.pop()
        replica_state.stack3.append(top)
        Next.append(replica_state)


    if current_state.stack2:         #if the current state is in the stack2

        #Adding the top element of stack 2 to stack 1

        replica_state = copy.deepcopy(current_state)
        top = replica_state.stack2.pop()
        replica_state.stack1.append(top)
        Next.append(replica_state)

        #Adding the top element of stack 2 to stack 3

        replica_state = copy.deepcopy(current_state)
        top = replica_state.stack2.pop()
        replica_state.stack3.append(top)
        Next.append(replica_state)


    if current_state.stack3:        #if the current state is in the state 3

        #Adding the top element of stack 3 to stack 1

        replica_state = copy.deepcopy(current_state)
        top = replica_state.stack3.pop()
        replica_state.stack1.append(top)
        Next.append(replica_state)

        #Adding the top element of stack 3 to stack 2

        new_state = copy.deepcopy(current_state)
        top = replica_state.stack3.pop()
        replica_state.stack2.append(top)
        Next.append(replica_state)
    
    
    return Next        #returning the array we used to store the states after the transitions i.e. replica states  


#Function for Goal testing

def GoalTest(current_state,goal_state):

    # Comparing the current state with the goal state

    if current_state.stack1 != goal_state.stack1:
        return False

    if current_state.stack2 != goal_state.stack2:
        return False

    if current_state.stack3 != goal_state.stack3:
        return False
       
    return True


#def heuristic_function


def NotVisited(state,visited,opened):

    for check_state in visited:    #check whether the state is in visited list.
        if (check_state.stack1 == state.stack1) and (check_state.stack2 == state.stack2) and (check_state.stack3 == state.stack3):
            return False

    for (h,check_state) in opened:          #check whether the state is in opened list
        if (check_state.stack1 == state.stack1) and (check_state.stack2 == state.stack2) and (check_state.stack3 == state.stack3):
            return False
    return True                    #return true if not the state is not already visited


#Function for tracing the path 

def Track_Path(path,state):
    
    path.append(state)

    if state.parent == None:              #return the track if we reach the initial state
        return

    else:
        Track_Path(path,state.parent)     #Recursively track the path 




# def Best_First_Search(initial_state, goal_state):

def Best_First_Search(initial_state,goal_state):#best first search
    
    q = PriorityQueue()             #q is a PriorityQueue
    explored=[]                     # to store visited states

    #Assign heuristic value to h
    h = (Heuristic_S3(goal_state,goal_state) - Heuristic_S3(initial_state,goal_state)) # difference between start and goal state
    
    q.put((h,initial_state))

    while not q.empty():

        h,state = q.get()            # get head / 1st element from priority queue
        explored.append(state)
        if GoalTest(state,goal_state):    # check for goal state
            
            path=[]

            Track_Path(path,state)   #call to Tracing function to trace the

            output.write("States in the path are: "+str(len(path))+"\n")
            output.write("Explored states are: "+str(len(explored))+"\n")

            for i in reversed(path):
                for s in i.allstack():
                    output.write(str(s)+"\n")
                output.write("\n")
            return True

        for Next in MoveGen(state):                   #find next states
            if NotVisited(Next,explored,q.queue):
                h = (Heuristic_S3(goal_state,goal_state) - Heuristic_S3(Next,goal_state))
                Next.parent = state                 # set parent for next to check for parent state 
                q.put((h,Next))
    return False


#function to implement hill climb algorithm

def Hill_Climb(initial_state,goal_state):          #Hill climbing search
    
    next_state=[]
    
    h = (Heuristic_S3(goal_state,goal_state) - Heuristic_S3(initial_state,goal_state))
    
    initial_state.heuristic = h

    next_state.append(initial_state)

    local_maxima = 0     #initialize the local maxima variable with 0

    while not local_maxima:

        state = next_state[-1]
        if GoalTest(state,goal_state):          # check for goal state
            
            path=[]
            Track_Path(path,state)
            
            output.write("States in the path are: "+str(len(path))+"\n")
            output.write("Explored states are: "+str(len(next_state))+"\n")
            
            for i in reversed(path):
                for s in i.allstack():
                    output.write(str(s)+"\n")
                output.write("\n")
            return True

        min = state   #store the state in min variable

        for Next in MoveGen(state):             # find next states     
            h = (Heuristic_S3(goal_state,goal_state)-Heuristic_S3(Next,goal_state))
            Next.parent = state
            Next.heuristic = h
           
            if (Next.heuristic < min.heuristic):
                min = Next
        
        next_state.append(min)         #set minimum heuristic valued state
        if min == state:
            local_maxima = 1           #we are stuck at local maxima now
    
    path=[]
    Track_Path(path,state)          # get path travelled if stuck on local maxima
    output.write("States in the path are: "+str(len(path))+"\n")
    output.write("Explored states are: "+str(len(next_state))+"\n")
    
    for i in reversed(path):
        for s in i.allstack():
            output.write(str(s)+"\n")
        output.write("\n")
    output.write("stuck in local maxima")
    return False


#Heuristic functions 
def Heuristic_S1(state,goal_state):
    h = 0 #initialize heuristic
    for stack, goal_stack in zip(state.allstack(),goal_state.allstack()):#parallel loop through state and goal state stacks of block
        for block in stack: # loop through inside a stack
            index_in_goal = None
            try:
                index_in_goal = goal_stack.index(block) # find index of block in goal stack
                index = stack.index(block) # find index of block in current stack
                if index == 0 and index_in_goal==0: #boundary case if they are on table
                    h+=1
                elif index-1>=0 and stack[index-1] == goal_stack[index_in_goal-1]: #if theu are correctly on top of block
                    h+=1
                else:
                    h-=1
            except: # if a goal stack does not have that block
                h-=1
    return h

def Heuristic_S2(state,goal_state):
    h = 0 #initialize heuristic
    for stack, goal_stack in zip(state.allstack(),goal_state.allstack()):#parallel loop through state and goal state stacks of block
        index = 0
        flag = False
        for block in stack:
            try:# if a goal stack have  block
                g = goal_stack[index]
            except:# if a goal stack does not have block
                g = None
            if flag == True:#if structure below is incorrect
                h-=1*(index+1)
            elif block == g and flag!=True:#if on correct structure
                h+=1*(index+1)
            else: #if on incorrect structure
                h-=1*(index+1)
                flag = True
            index+=1
    return h

def Heuristic_S3(state,goal_state):
    h = 0  #initialize heuristic
    for stack, goal_stack in zip(state.allstack(),goal_state.allstack()):#parallel loop through state and goal state stacks of block
        index = 0
        flag = False
        for block in stack:
            try:# if a goal stack have  block
                g = goal_stack[index]
            except:# if a goal stack does not have block
                g = None
            if flag == True:#if structure below is incorrect
                h-=1*(len(stack)-index)
            elif block == g and flag!=True:#if on correct structure
                h+=1*(len(stack)-index)
            else:#if on incorrect structure
                h-=1*(len(stack)-index)
                flag = True
            index+=1
    return h



if (__name__ == "__main__"):

    if(len(sys.argv) == 2):
        filename = sys.argv[1]
    
    else:
        print("Error in file input: ")
        exit(1)


    i = 1
    for line in filename:                  #input in file for mace
        if(i==1):
            file_code = int(line)          #checking condition for Best First Search or Hill Climb
            i=0
    
    stack1 = list(filename.readline().strip().split())
    stack2 = list(filename.readline().strip().split())
    stack3 = list(filename.readline().strip().split())

    initial_state = Blocks(stack1,stack2,stack3)    #the order given in the file is assigned as the initial state

    # stack1 = list(filename.readline().strip().split())
    # stack2 = list(filename.readline().strip().split())
    # stack3 = list(filename.readline().strip().split())

    goal_state = Blocks(stack1,stack2,stack3)

    output = open("output.txt", "w+")

    if file_code =='1':
        Best_First_Search(initial_state,goal_state)
        print("1")

    elif file_code=='2':
        Hill_Climb(initial_state,goal_state)
        print("2")

