import sys

Stack_1       #Stack for the input
Stack_2       #Stack for the output
Stack_3

OPEN_list[]                 #Open list to store values of state and check the order of heuristic function's values
CLOSED_list[]               #Closed List to store the state with lowest value of heuristic function

BlockCluster[]       #array to store the inputstack completely in it.

class Blocks:
    def __init__(self, label):
        self.label = label
        self.goalState = None
        self.goallevel = None


def Best_First_Search(current_state):

    OPEN_list.append(current_state)

    if(len(OPEN_list) == print("OPEN list is empty")

    else:
        Heuristic_Function(current_state)

def Heuristic_Function(test_state):
    hn =  #function to calculate the heuristic
    array_for_h_values.append(hn)


if (__name__ == "__main__")

    if (len(sys.argv)==2):
        filename = sys.argv[1]

        file = open(filename,'r')
        data.file.readlines()   #reading lines from the file an dstoring it in variable named data

        for line in file:
            for char in line:
                if char is None:
                    break

                if char in Stack_1:
                    Stack_2.append(char)
                if char != '\n':
                    Stack_1.append(char)

    else:
        print("Error in file input: ")
        exit(1)
