from searches import *
from mazeGenerator import maze_generator
import random
import pygame

testMaze = [[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0 , 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]]

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)
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
                    #print("fire spread at [{}][{}]".format(i, j))

def start_fire(maze): #start fire with assumption that topleft + bottomright are start/goal
    #find a free spot (matrix index = 0) to start 
    while True:
        row = -1
        column = -1
        while (row == -1 or row == 0 or row == len(maze)-1):
            row = random.randint(0, len(maze)-1)
        while (column == -1 or column == 0 or column == len(maze)-1):
            column = random.randint(0, len(maze)-1)
        if maze[row][column] == 0:
            break
        else:
            continue

    #set on fire
    maze[row][column] = 5
    #print("fire started at [{}][{}]".format(row, column))

def strategyOne(maze, q):
    start_fire(maze)
    shortestPath = []
    curr = [0, 0]
    #check first if theres no apth from start
    shortestPath = findShortestBFS(maze, curr, [len(maze)-1, len(maze)-1])
    if shortestPath[0] == 'No path': 
        return -2
    #iterate thru
    for i in range(len(shortestPath)):
        curr = shortestPath[i]
        if maze[curr[0]][curr[1]] == 5:
            #print("died in a fire")
            return -1
        if [curr[0], curr[1]] == [len(maze)-1, len(maze)-1]:
            return 200
        advance_fire(maze, q)


def strategyTwo(maze, q):
    start_fire(maze)
    #start from topleft
    current = [0, 0]
    if checkPathDFS(maze, current, [len(maze)-1, len(maze)-1]) == False:
        #print("no initial path")
        return -2
    #follow a computed shortest path step by step, recompute after each step
    while True:
        shortestPath = findShortestBFS(maze, current, [len(maze)-1, len(maze)-1])
        if shortestPath[0] == 'No path':
            #print("no where to go " + str(current))
            return -1
        current = shortestPath[1]
        
        if maze[current[0]][current[1]] == 5:
            #print("died tragically in a fire")
            return -1
        elif current == [len(maze)-1, len(maze)-1]:
            #print("found goal")
            return 200
        advance_fire(maze, q)

    return 200

#checks if there is a fire nearby based on given distance safety factor
def checkSafety(maze, location, distance):
    row = location[0]
    col = location[1]
    for i in range(row-distance, row+distance+1):
        #use this to see how far the columns will be checked
        rowDisplacement = abs(row - i)
        #print(str(rowDisplacement))
        for j in range(col - distance + rowDisplacement, col + distance - rowDisplacement+1):
            if (i >= 0 and i < len(maze)) and (j >=0 and j < len(maze)):
                #print(maze[i][j], end=' ')
                if maze[i][j] == 5: #fire nearby
                    return False
        
    return True #safe
        
#fire safe version of BFS using safety number
#safety number = how far to try and keep away from fire
def safeBFS(maze, firstLocation, secondLocation, safety):
    fringe = deque() #use a queue for BFS
    first = (firstLocation[0], firstLocation[1])
    fringe.append(first)
    visited = set()
    parentTracker = []
    for i in range(len(maze)):
        for j in range(len(maze)):
            toAdd = {}
            toAdd["previous"] = []
            parentTracker.append(toAdd)

    parentTracker[0]["previous"] = firstLocation
    #process thru fringe
    while fringe:
        current = fringe.popleft() #pop leftmost = one thats been in the fringe longest (queue)
        if current[0] == secondLocation[0] and current[1] == secondLocation[1]:
            toReturn = []
            toReturn.append([current[0], current[1]])
            curIndex = findILIndex(current[0], current[1], len(maze))
            backtrackCurrent = parentTracker[curIndex]["previous"]
            while True:
                toReturn.insert(0, backtrackCurrent)
                if backtrackCurrent == firstLocation:
                    break
                backtrackCurrent = parentTracker[findILIndex(backtrackCurrent[0], backtrackCurrent[1], len(maze))]["previous"]

            return toReturn
            
        else:
            if current not in visited: #check node, if not already visited then work thru its children if they're valid
                currentFirst = current[0]
                currentSecond = current[1]
                if currentFirst-1 >= 0 and currentFirst-1 < len(maze) and currentSecond >= 0 and currentSecond < len(maze): #up
                    if (currentFirst-1,currentSecond) not in visited and maze[currentFirst-1][currentSecond] == 0 and checkSafety(maze, (currentFirst-1,currentSecond), safety):
                        temp = (currentFirst-1, currentSecond)
                        fringe.append(temp)
                        parentTracker[findILIndex(currentFirst-1, currentSecond, len(maze))]["previous"] = [currentFirst, currentSecond]
                if currentFirst >= 0 and currentFirst < len(maze) and currentSecond-1 >= 0 and currentSecond-1 < len(maze): #left
                    if (currentFirst, currentSecond-1) not in visited and maze[currentFirst][currentSecond-1] == 0 and checkSafety(maze, (currentFirst,currentSecond-1), safety):
                        temp = (currentFirst, currentSecond-1)
                        fringe.append(temp)
                        parentTracker[findILIndex(currentFirst, currentSecond-1, len(maze))]["previous"] = [currentFirst, currentSecond]
                if currentFirst+1 >= 0 and currentFirst+1 < len(maze) and currentSecond >= 0 and currentSecond < len(maze): #down
                    if (currentFirst+1, currentSecond) not in visited and maze[currentFirst+1][currentSecond] == 0 and checkSafety(maze, (currentFirst+1,currentSecond), safety):
                        temp = (currentFirst+1, currentSecond)
                        fringe.append(temp)
                        parentTracker[findILIndex(currentFirst+1, currentSecond, len(maze))]["previous"] = [currentFirst, currentSecond]
                if currentFirst >= 0 and currentFirst < len(maze) and currentSecond+1 >= 0 and currentSecond+1 < len(maze): #right
                    if (currentFirst, currentSecond+1) not in visited and maze[currentFirst][currentSecond+1] == 0 and checkSafety(maze, (currentFirst,currentSecond+1), safety):
                        temp = (currentFirst, currentSecond+1)
                        fringe.append(temp)
                        parentTracker[findILIndex(currentFirst, currentSecond+1, len(maze))]["previous"] = [currentFirst, currentSecond]
                #after done, add node to visited
                visited.add((currentFirst, currentSecond))
                #maze[currentFirst][currentSecond] = 3
    
    return ["No path"]

def strategyThree(maze, q, safety):
    start_fire(maze)
    #start from topleft
    current = [0, 0]
    if checkPathDFS(maze, current, [len(maze)-1, len(maze)-1]) == False:
        #print("no initial path")
        return -2
    #follow computed shortest path step by step, recompute after each step
    #HOWEVER we try to stay as far away from the fire as possible as well.
    while True:
        attempts = 0
        success = False
        status = []
        while attempts < safety:
            status = safeBFS(maze, current, (len(maze)-1, len(maze)-1), safety-attempts)
            #try to see how far away you can stay from the fire
            if status[0] == 'No path':
                attempts += 1
                continue
            else:
                success = True
                break
        #check
        if not success:
            #print("no where to go " + str(current))
            return -1
        current = status[1]
        if maze[current[0]][current[1]] == 5:
            #print("died tragically in a fire")
            return -1
        elif current == [len(maze)-1, len(maze)-1]:
            #print("found goal")
            return 200
        advance_fire(maze, q)
    return 200

testMaze = [[0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 1, 0, 0],
            [1, 0, 0, 1, 0],
            [0, 1, 0, 0, 0]]
#print(checkPathDFS(testMaze, [1, 0], [4, 4]))
#print(findShortestBFS(maze_generator(100, 0.3), [0, 0], [99, 99]))
print(strategyTwo(maze_generator(25, 0.2), 0.2))
print(strategyOne(maze_generator(25, 0.3), 0.05))
#print(findShortestBFS(testMaze, [0, 0], [4, 4]))
# print(safeBFS(testMaze, [0, 0], [4, 4], 3))
print(strategyThree(maze_generator(25, 0.2), 0.2, 2))