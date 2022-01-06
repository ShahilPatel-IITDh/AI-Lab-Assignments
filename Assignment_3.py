import sys
import copy
import random


class Stage:

    def __init__(self,directions,parent = None, heuristic = None, previous_storage = None):
        self.directions = directions
        self.parent = parent
        self.heuristic = heuristic
        self.previous_storage = previous_storage


def negative(literal):

    if literal == 'a':
        return '~a'

    elif literal == '~a':
        return 'a'

    elif literal == 'b':
        return '~b'

    elif literal == '~b':
        return 'b'

    elif literal == 'c':
        return '~c'

    elif literal == '~c':
        return 'c'

    elif literal == '~d':
        return 'd'

    elif literal == 'd':
        return '~d'


def tautology(clause):

    for literal in clause:

        if negative(literal) in clause:     #if negation of any literal is present in clause then it is tautology
            return True

        return False


#Main Function / driver code

n = 4     #here n is no. of literals given in question
k = 5     #here k is no. of clauses given in question

possibilities = ['a','~a','b','~b','c','~c','d','~d']
combination = []
formula = []
for i in range(k):
    reject = 1
    while(reject):
        random_combo=[random.choice(possibilities) for j in range(3)]  #generate random clause

    #     if (not tautology(random_combo)) and (not duplicate(random_combo) and (len(set(random_combo)) == len(random_combo))):   # check if it is allowed
    #         rejected = False
            
    # formula.append(random_combo)
