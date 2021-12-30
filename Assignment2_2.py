import sys
from queue import PriorityQueue

# Initializing Stacks for storing input

class Blocks:
    def __init__(self, label):
        self.label = label
        self.goalState = None
        self.goallevel = None
    
    def __init__(self,stack1,stack2,stack3,parent=None,heuristic_function=None):
        self.stack1 = stack1
        self.stack2 = stack2
        self.stack3 = stack3
        self.parent = parent
        self.heuristic_function = heuristic_function




def GoalTest(current_state,goal_state):
    
    # Comapring the current state with the goal state

    if current_state.stack1 != goal_state.stack1:
        return False

    if current_state.stack2 != goal_state.stack2:
        return False

    if current_state.stack3 != goal_state.stack3:
        return False
       
    return True


#Main Function for input of file and output of the result.


if (__name__ == "__main__"):

    if (len(sys.argv)==2):
        filename = sys.argv[1]

        file = open(filename,"r")     #Opening the specified file
        data.file.readlines()         #reading lines from the file and storing it in variable named data

        for line in file:
            for char in line:
                if char is None:
                    break

                if char in Stack_1:
                    Stack2.append(char)
                if char != '\n':
                    Stack1.append(char)

    else:
        print("Error in file input: ")
        exit(1)
