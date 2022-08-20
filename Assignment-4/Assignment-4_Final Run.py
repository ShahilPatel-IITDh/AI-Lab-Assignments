import sys
import random
import copy
import time
import math


#Class for objects for Ant Colony

class Ant_Colony(object):

    def __init__(self, Distances, Num_Of_Ants, Max_It, alpha, beta, rho, Q):

        self.Distances = Distances
        self.Num_Of_Ants = Num_Of_Ants
        self.Max_It = Max_It
       
# Initializing  the parameters       

        self.Q = Q
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Best = int(0.1*(N_Of_Cities)+1)

#Parameters assignment here ph = pheromones of Ant Colony Algorithm

        self.ph = [[0.1 for city in range(N_Of_Cities)] for selectedcity in range(N_Of_Cities)]

#Now assign Optimal Cost and Tour Variables
        
        self.Optimal_Cost = float('inf')
        self.Optimal_Tour = range(N_Of_Cities)

#Function for optimization

    def Optimization(self):

        while (time.time()-start_time) < 298:          #Loop till current time - start time is less than 298

            Ant_List = []         #List for Ant

#phDelta is (0 for x in range(NumOfCities) and 0 for y in range (NumOfCities))
            
            phDelta = [[0 for x in range(N_Of_Cities)] for y in range(N_Of_Cities)]

#loop for j in range of Num of Ants in self object
            for j in range(self.Num_Of_Ants):

                ant = Ant(self.Distances, self.ph, self.alpha, self.beta)

#append ant in the list of Ant
                Ant_List.append(ant)

#run this condition if the current tour cost is less then the optimal cost
                if ant.Tour_Cost(self.Distances) < self.Optimal_Cost:

#if current tour cost is less then optimal cost than update the optimal cost to the current tour cost
                    
                    self.Optimal_Cost = ant.Tour_Cost(self.Distances)
                    self.Optimal_Tour = ant.Current_Tour           #Now as the current tour cost is less than optimal cost, the current tour can be considered as optimal tour
                    self.lastChange = time.time()       #store the time stamp as last change
                    

                    #print the outputs

                    print("The length of Tour is = ", self.Optimal_Cost, sep=' ')
                    print(*self.Optimal_Tour, sep=' ')
                    print("--------------------------------------------------------------------------------------------------------------------------------------------------------\n")

#Sort the ant_list 
            Ant_List.sort(key=lambda city: city.Tour_Cost(self.Distances))
            
            for KiDi in Ant_List[:self.Best]:
                for i, v in enumerate(KiDi.Current_Tour):       #Vaue returned by enumerate class for current tour in KiDi variable
                
                    nextOne = KiDi.Current_Tour[(i+1)%N_Of_Cities]
                    phDelta[v][nextOne] += self.Q/Distances[v][nextOne]

    #Calculate the value of self.ph at given i and j indices        
            for i in range(N_Of_Cities):
               
                for j in range(N_Of_Cities):
                    
                    self.ph[i][j] = (1-self.rho)*self.ph[i][j] + phDelta[i][j]

            if (time.time()-self.lastChange) > 300:    #if the time limit exceeds the limit of 300s, then break the loop
                break

# Ant class structure defined

class Ant(object):

    def __init__(self, Distances, pheromones, alpha, beta):
        
        self.Current_Tour = []
        self.Track_Path(Distances, pheromones, alpha, beta)


# Track the Path for the tour

    def Track_Path(self, Distances, pheromones, alpha, beta):

#Start the tour, initialize a variable randomly in range of [0,N-1]

        starter = random.randint(0, N_Of_Cities-1)    #Random integer in range of 0 to number of cities - 1
        City_Validity = list(range(0, N_Of_Cities))
        City_Validity.remove(starter)

        self.Current_Tour.append(starter)
        while(len(self.Current_Tour) < N_Of_Cities):

            Last_City = self.Current_Tour[-1]      #it is the last city which was visited in the current tour

            #Now find the probability to go to a particular city, we use pow function from 'math' library

            probability = [math.pow((pheromones[Last_City][nextPossibleCity]),alpha) *(math.pow((1/Distances[Last_City][nextPossibleCity]),beta)) for nextPossibleCity in City_Validity]

            probSet = [x/sum(probability) for x in probability]

            Next_City = random.choices(City_Validity, weights=probSet)[0]    #choose the next city using random functin, but using the probability detector
            self.Current_Tour.append(Next_City)    #Add the Next City to list of current tour
            City_Validity.remove(Next_City)

    # Function to calculate the cost of current tour
    
    def Tour_Cost(self, Distances):
        
        cost = 0     #initialize a variable to sum up the cost of current tour
        for i in range(len(self.Current_Tour)):
           
           cost += Distances[self.Current_Tour[i]][self.Current_Tour[(i+1) % N_Of_Cities]]
        
        return cost



if __name__ == '__main__':

    start_time = time.time()
    file = open(sys.argv[1], "r").readlines()
    isEuclidean = 0       #variable to check whether the file contains euclidean distances, if 0 then non-euclidean , if 1 then euclidean

#Check whether the first line of file is euclidean or non-euclidean

    if(file[0] == "euclidean"):
        isEuclidean = 1

    N_Of_Cities = int(file[1])     #the 2nd line of input file contains the number of cities

    City_Coordinates = []    #list to store the coordinates of cities
    Distances = []             #list t store the distaces between the cities
    rlist = []
    for i in range(N_Of_Cities):
        
        c = [float(x) for x in file[i+2].strip().split(' ')]
        City_Coordinates.append(c)

        d = [float(x) for x in file[N_Of_Cities+2+i].strip().split(' ')]
        Distances.append(d)

    #Check if the isEuclidean is true or false and run the algorithm accordingly
    
    if (isEuclidean == 1):
        Tour = Ant_Colony(Distances, Num_Of_Ants=int(N_Of_Cities), Max_It = 200, alpha = 3, beta = 3, rho = 0.1, Q = 0.1)
    
    else:
        Tour = Ant_Colony(Distances, Num_Of_Ants=100 ,Max_It = 500, alpha = 5 , beta = 12, rho = 0.05, Q = 0.05)
                                                                                    
    Tour.Optimization()
