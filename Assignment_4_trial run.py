import sys
import copy
import math
import random

class City:
    def __init__(self,X,Y,distance = None):
        self.X = X
        self.Y = Y
        self.distance = distance



#input part
file = open(sys.argv[1],"r")
euclidean_check = file.readline().strip()   #check the first line of file for whether the given distances are euclidean are non-euclidean

N = int(file.readline().strip())   #variable to store the number of cities as given in input file
    
city_list = []   #list to store the coordinates 

#input the coordinates of cities given in space separated form 
for j in range(N):
    x_coordinate,y_coordinate = file.readline().strip().split()
    coordinates = City(float(x_coordinate),float(y_coordinate))
    city_list.append(city_list)

for i in city_list:

    i.distance = list(map(float,file.readline().split()))



#Main Function / Driver Code
if euclidean_check == 'euclidean':
    #SomeFunction to allow the passage of the salesman
    print("euclidean")    #created for temporary purpose
else: 
    #some function for non-euclidean part
    print("non - euclidean")   #created for temporary purpose