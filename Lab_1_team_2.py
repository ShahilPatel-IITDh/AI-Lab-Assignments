import sys

#global Variable for number of states explored

States_Explored = 0


#function to read inputs from the file and create a binary graph for applications of algorithms.

def mazeRead(filename):  #function to read the input and make graph from it
    f=open(filename,'r')   #command line input file

    Graph=[]       #grid of 0 and 1 after converting input graph ot binary graph
    Org=[]         #original input from the file
    i = 1
    for line in f:                  #input in file for mace
        if(i==1):
            number_for_running = int(line)   #checking condition for DFS or BFS or DFID
            i=0

        else:
            graphMaze=[]
            originalMaze=[]
            for char in line:
                if (char == ' '):     #checking if the character is blank 
                    graphMaze.append(1)     #assigning 1 to blank space for graphmaze
                    originalMaze.append(char) #creating the original graph

                elif (char=='*'):
                    graphMaze.append(2)
                    originalMaze.append(char)
                
                elif (char=='\n'):
                    pass

                else:
                    graphMaze.append(0)
                    originalMaze.append(char)

            Graph.append(graphMaze)          #Graph is the binary graph which will be used to apply algorithms for searching the goal state.
            Org.append(originalMaze)         #Org is the original graph as given in the input
    return Graph,Org,number_for_running

def Valid(rows, columns, n, m):    #Checking the validity for rows and columns

    if((rows>=0 and rows<n)) and ((columns>=0 and columns<m)):
        return 1
    else:
        return 0

      
# Class Node

class Node:
    def __init__(self,x,y,parent=None):
        self.x = x
        self.y = y
        self.parent = parent

        
#Applying Breadth First Search

def BFS(Graph,Org):
    exploredvertex = []    #variable to store the explored vertices
    array = []
    for x in range(len(Graph[0])):    #x for rows
        line = [] 
        for y in range(len(Graph)):   #y for column
            line.append(None)
        array.append(line)    
    

    que = []   #que for queue
    node = Node(0,0)
    array[0][0] = node
    que.append(node)

    temp = 0

    while (len(que)) and temp == 0:
        node = que.pop(0)
        if Graph[node.y][node.x] == 2:
            goal = node
            temp=1
        
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if Valid(node.y + dy, node.x + dx, len(Graph), len(Graph[0])):
                if Graph[node.y+dy][node.x + dx] != 0 and (array[node.x+dx][node.y+dy] == None):
                    newNode = Node(node.x+dx,node.y+dy, node)
                    array[node.x+dx][node.y+dy] = newNode
                    que.append(newNode)                  
    
        exploredvertex.append(node)
    
    current_Node = goal           #current node takes goal state as input to retract the path to parent nodes.
    OutputPath = Org
    PathLength = 1
    while current_Node.parent:
        OutputPath[current_Node.y][current_Node.x] = 0
        current_Node = current_Node.parent
        PathLength += 1

    OutputPath[current_Node.y][current_Node.x] = 0

    print(len(exploredvertex))         #will print the no. of vertices wich have been explored while the algoritm is runned.
    print(PathLength)                  #will print the path length from initial state to goal state
    for row in OutputPath:
        for char in row:
            print(char,end="")   

        print("")    


#Applying Depth First search

def DFS(Graph,Org):
    exploredvertex = []
    array = []
    for x in range(len(Graph[0])):    #x for rows
        line = [] 
        for y in range(len(Graph)):   #y for column
            line.append(None)
        array.append(line)
    

    stk = []   #stk for stack
    node = Node(0,0)
    array[0][0] = node
    stk.append(node)

    temp = 0

    while (len(stk)) and temp == 0:
        node = stk.pop()
        if Graph[node.y][node.x] == 2:
            goal = node
            temp=1
        
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if Valid(node.y + dy, node.x + dx, len(Graph), len(Graph[0])):
                if Graph[node.y+dy][node.x + dx] != 0 and (array[node.x+dx][node.y+dy] == None):
                    newNode = Node(node.x+dx,node.y+dy, node)
                    array[node.x+dx][node.y+dy] = newNode
                    stk.append(newNode)                  
    
        exploredvertex.append(node)
    
    current_Node = goal
    OutputPath = Org
    PathLength = 1
    while current_Node.parent:
        OutputPath[current_Node.y][current_Node.x] = 0
        current_Node = current_Node.parent
        PathLength += 1

    OutputPath[current_Node.y][current_Node.x] = 0

    print(len(exploredvertex))           #will print the no. of vertices wich have been explored while the algoritm is runned.
    print(PathLength)                     #will print the path length from initial state to goal state
    for row in OutputPath:
        for char in row:
            print(char,end="")   

        print("")    

        
#Output of Limited_DFS will be used for application of DFID. 
def Limited_DFS (Graph, Org,Limit):

    exploredvertex = []
    array = []
    for x in range(len(Graph[0])):    #x for rows
        line = [] 
        for y in range(len(Graph)):   #y for columns
            line.append(None)
        array.append(line)
    

    stk = []   #stk for stack
    node = Node(0,0)
    array[0][0] = node
    stk.append(node)

    temp = 0

    while (len(stk)) and temp == 0:
        node = stk.pop()
        if Graph[node.y][node.x] == 2:
            goal = node
            temp=1
        
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if Valid(node.y + dy, node.x + dx, len(Graph), len(Graph[0])):
                if Graph[node.y+dy][node.x + dx] != 0 and (array[node.x+dx][node.y+dy] == None):
                    newNode = Node(node.x+dx,node.y+dy, node)
                    array[node.x+dx][node.y+dy] = newNode
                    stk.append(newNode)                  
    
        exploredvertex.append(node)
    
    current_Node = goal
    OutputPath = Org
    PathLength = 1
    while current_Node.parent:
        OutputPath[current_Node.y][current_Node.x] = 0
        current_Node = current_Node.parent
        PathLength += 1

    OutputPath[current_Node.y][current_Node.x] = 0
    

#The Main function of the code.

if (__name__ == "__main__"):

    if(len(sys.argv)==2):
        name_of_file = sys.argv[1]
    
    else:
        print("Error in file input: ")
        exit(1)

    graphMaze,originalMaze,number_for_running = mazeRead(name_of_file)
    if number_for_running == 0:
        BFS(graphMaze,originalMaze)
    elif number_for_running == 1:
        DFS(graphMaze,originalMaze)
    # elif number_for_running == 2:
    #     DFID(graphMaze,originalMaze)
