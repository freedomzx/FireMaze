from searches import *
from mazeGenerator import maze_generator
import random

#advance fire in maze via algorithm given in pdf
def advance_fire(maze, q):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            #check if not obstacle and not on fire
            if maze[i][j] != 5 and maze[i][j] != 1:
                #check nu mof neighbors on fire
                numOfFireChildren = 0
                if checkValidChild(maze, i-1, j):
                    if maze[i-1][j] == 5:
                        numOfFireChildren += 1
                
                if checkValidChild(maze, i, j-1):
                    if maze[i][j-1] == 5:
                        numOfFireChildren += 1

                if checkValidChild(maze, i+1, j):
                    if maze[i+1][j] == 5:
                        numOfFireChildren += 1

                if checkValidChild(maze, i, j+1):
                    if maze[i][j+1] == 5:
                        numOfFireChildren += 1

                probability = 1 - pow((1-q), numOfFireChildren)
                probability *= 100
                if random.randint(1, 100) <= probability:
                    maze[i][j] = 5

def start_fire(maze): #start fire with assumption that topleft + bottomright are start/goal
    row = -1
    column = -1
    while (row == -1 or row == 0 or row == len(maze)-1):
        row = random.randint(0, len(maze)-1)
    while (column == -1 or column == 0 or column == len(maze)-1):
        column = random.randint(0, len(maze)-1)

    maze[row][column] = 5

def strategyOne(maze, q):
    shortestPath = []
    curr = [0, 0]
    shortestPath = findShortestBFS(maze, curr, [len(maze)-1, len(maze)-1])
    if shortestPath[0] == 'No path': 
        return -2
    for i in range(len(shortestPath)):
        curr = shortestPath[i]
        if maze[current[0]][current[1]] == 5:
            return -1
        advance_fire(maze, q)


def strategyTwo(maze, q):
    #start from topleft
    current = [0, 0]
    
    #follow a computed shortest path step by step, recompute after each step
    shortestPath = []
    while True:
        shortestPath = findShortestBFS(maze, current, [len(maze)-1, len(maze)-1])
        if shortestPath[0] == 'No path':
            #no path from current node to goal
            return -2
        advance_fire(maze, q)
        current = shortestPath[1]
        if current == [len(maze)-1, len(maze)-1]:
            #found it, return good
            return 200

def strategyThree(maze):
    pass

testMaze = [[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0 , 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]]

start_fire(testMaze)
print(testMaze)
advance_fire(testMaze, 0.3)
print(testMaze)
advance_fire(testMaze, 0.3)
print(testMaze)
advance_fire(testMaze, 0.3)
print(testMaze)