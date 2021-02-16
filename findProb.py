from searches import *
from mazeGenerator import maze_generator
import random

def findProbsDFS():
    #find for 0.1
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.125), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.125 is: " + str(success / 150))
    
    #find for 0.2
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.175), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.175 is: " + str(success / 150))

    #find for 0.3
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.225), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.225 is: " + str(success / 150))
    
    #find for 0.4
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.275), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.275 is: " + str(success / 150))
    
    #find for 0.5
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.325), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.325 is: " + str(success / 150))
    
    #find for 0.6
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.375), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.375 is: " + str(success / 150))
    
    #find for 0.7
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.425), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.425 is: " + str(success / 150))
    
    #find for 0.8
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.475), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.475 is: " + str(success / 150))
    
def findBFSData():
    pass