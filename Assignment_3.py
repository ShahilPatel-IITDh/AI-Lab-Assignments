import sys
import copy
import random


class Stage:

    def __init__(self,directions,parent = None, heuristic = None, previous_storage = None):
        self.directions = directions
        self.parent = parent
        self.heuristic = heuristic
        self.previous_storage = previous_storage






#Main Function / driver code

n = 4     #here n is no. of literals given in question
k = 5     #here k is no. of clauses given in question
possibilities =['a','~a','b','~b','c','~c','d','~d']
combination =[]

for i in range(k):
    reject = 1
    while(reject):
        random_combo=[random.choice(possibilities) for j in range(3)]
