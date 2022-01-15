import sys
import copy
import random
import time
from typing import Iterator

class City:
    def __init__(self,X,Y,distance = None):
        self.X = X
        self.Y = Y
        self.distance = distance


def MoveGen(current_tour,N,city_list,pheromone,alpha,beta):
    
    allowed_moves = [i for i in range(N) if i not in current_tour]
    valid_pheromone = [math.pow(pheromone[current_tour[-1]][allowed_moves[i]],alpha) for i in range(len(allowed_moves))]
    valid_distances = [math.pow((1 / cities[curr_tour[-1]].distance[i]),beta) for i in allowed_moves]
    valid_product = [valid_pheromone[i] * valid_distances[i] for i in range(len(allowed_moves))]
    valid_prob = [valid_product[i] / sum(valid_product) for i in range(len(allowed_moves))]
    
    a = random.random()
    i = 0
    s = valid_prob[0]
    
    while True:
        if s > a:
            return allowed_moves[i]
        i += 1
        s += valid_prob[i]



def TourTrack(N, city_list, maxIteration,pheromone,Ants,alpha,beta,q,rho):
    
    minimum = -1       #initializing a variable to store the minimum value
    optimal_tour = [j for j in range(N)]        #initialize the tour which is optimal
    iteration = 0

    while time.time() < start + 298 and iteration < maxIteration:
        next_pheromone = copy.deepcopy(pheromone)
        for i in range (Ants):
            current_tour = []
            current_tour.append(0)

            while len(current_tour) != N:         #Loop to check whther every city is visited atleast nce or not
                current_tour.append(MoveGen(current_tour,N,city_list,pheromone,alpha,beta))

            cost = 0     #initialize a variable to store the value of cost for travelling cities

            for i in range (len(current_tour)-1):
                cost += city_list[current_tour[i]].distance[current_tour[i+1]]
            
            if minimum == -1:

                minimum = cost
                optimal_tour = current_tour
            
            elif minimum > cost: #update best tour if current tour has less cost
             
                minimum = cost
                optimal_tour = current_tour
        
        s = current_tour
        cost = 0
       
        for i in range(len(current_tour) - 1):            # calculate cost of current tour
            cost += city_list[current_tour[i]].distance[current_tour[i+1]]
       
        for i in range(len(current_tour) - 1):          # update next pheromone
           
            next_pheromone[current_tour[i]][current_tour[i + 1]] *= rho
            next_pheromone[current_tour[i]][current_tour[i + 1]] += q / cost
            next_pheromone[current_tour[i + 1]][current_tour[i]] *= rho
            next_pheromone[current_tour[i + 1]][current_tour[i]] += q / cost
        
        pheromone = next_pheromone

        cost = 0

        for i in range(len(optimal_tour)-1):
            cost += city_list[optimal_tour[i]].distance[optimal_tour[i+1]]
        
        #print the output

        print("The optimal cost found is =", cost, sep=' ')
        print(*optimal_tour, sep=' '"\n")

        iteration += 1
    return optimal_tour


start = time.time()

#input part
file = open(sys.argv[1],"r")
euclidean_check = file.readline().strip()   #check the first line of file for whether the given distances are euclidean are non-euclidean

isEuclidean = 0

if(euclidean_check == "euclidean"):
    isEuclidean = 1


N = int(file.readline().strip())   #variable to store the number of cities as given in input file
    
city_list = []   #list to store the coordinates 

#input the coordinates of cities given in space separated form 
for j in range(N):
    x_coordinate,y_coordinate = file.readline().strip().split()
    coordinates = City(float(x_coordinate),float(y_coordinate))
    city_list.append(city_list)

for i in city_list:

    i.distance = list(map(float,file.readline().split()))

initial_pheromone_matrix = [[1 / (N**2) for j in range(N)] for i in range(N)]

#Main Function / Driver Code
if (isEuclidean == 1):
    #SomeFunction to allow the passage of the salesman
    tour = TourTrack(N, city_list, maxIterations = 200, pheromone=initial_pheromone_matrix, ants=100,alpha = 3.0, beta = 3.0, q = 0.1, rho = 0.1)


else: 
    #some function for non-euclidean part
    tour = TourTrack(N, city_list, maxIterations=300,pheromone=initial_pheromone_matrix, ants=100, alpha=5, beta=5, q=0.05, rho=0.05)