from searches import *
from mazeGenerator import maze_generator
import random

def findProbsDFS():
    #find for 0.1
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.1), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.1 is: " + str(success / 150))
    
    #find for 0.2
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.2), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.2 is: " + str(success / 150))

    #find for 0.3
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.3), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.3 is: " + str(success / 150))
    
    #find for 0.4
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.4), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.4 is: " + str(success / 150))
    
    #find for 0.5
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.5), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.5 is: " + str(success / 150))
    
    #find for 0.6
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.6), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.6 is: " + str(success / 150))
    
    #find for 0.7
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.7), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.7 is: " + str(success / 150))
    
    #find for 0.8
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.8), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.8 is: " + str(success / 150))
    
    #find for 0.9
    success = 0
    failures = 0
    for runs in range(150):
        if checkPathDFS(maze_generator(1750, 0.9), [0, 0], [1749, 1749]) is True:
            success += 1
        else:
            failures += 1
    print("Probability of success for 0.9 is: " + str(success / 150))