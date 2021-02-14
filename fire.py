from searches import *
from mazeGenerator import maze_generator
import random

#advance fire in maze via algorithm given in pdf
def advance_fire(maze, q):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            #check if not obstacle and not on fire
            if maze[i][j] != 3 and maze[i][j] != 1:
                #check nu mof neighbors on fire
                numOfFireChildren = 0
                if checkValidChild(maze, i-1, j):
                    if maze[i-1][j] == 3:
                        numOfFireChildren += 1
                
                if checkValidChild(maze, i, j-1):
                    if maze[i][j-1] == 3:
                        numOfFireChildren += 1

                if checkValidChild(maze, i+1, j):
                    if maze[i+1][j] == 3:
                        numOfFireChildren += 1

                if checkValidChild(maze, i, j+1):
                    if maze[i][j+1] == 3:
                        numOfFireChildren += 1

                probability = 1 - pow((1-q), numOfFireChildren)
                probability *= 100
                if random.randint(1, 100) <= probability:
                    maze[i][j] = 3  

def strategyOne(maze):
    pass

def strategyTwo(maze):
    pass

def strategyThree(maze):
    pass