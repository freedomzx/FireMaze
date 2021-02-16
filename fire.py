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

def start_fire(maze): #start fire with assumption that topleft + bottomright are start/goal
    row = -1
    column = -1
    while (row == -1 or row == 0 or row == len(maze)-1):
        row = random.randint(0, len(maze)-1)
    while (column == -1 or column == 0 or column == len(maze)-1):
        column = random.randint(0, len(maze)-1)

    maze[row][column] = 3

def strategyOne(maze):
    pass

def strategyTwo(maze):
    pass

def strategyThree(maze):
    pass

testMaze = [[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0 , 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]]

start_fire(testMaze)

print(testMaze)