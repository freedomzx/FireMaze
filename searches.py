from collections import deque
import time
from mazeGenerator import maze_generator
import pygame
import math

#colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)

#maze is a dim x dim matrix, firstLocation is a list of 2 nums, secondLocation is the same.  check if there's a path from start to goal via bfs
def checkPathDFS(maze, firstLocation, secondLocation): 
    fringe = deque() #use a stack for DFS
    fringe.append(firstLocation)
    visited = []
    while fringe:
        current = fringe.pop()
        if current[0] == secondLocation[0] and current[1] == secondLocation[1]: #if found goal then get out of here
            print(maze)
            return True #found a path
        else:
            if current not in visited:
                currentFirst = current[0]
                currentSecond = current[1]
                #check 4 neighbors to see which we can add to fringe
                if currentFirst-1 >= 0 and currentFirst-1 < len(maze) and currentSecond >= 0 and currentSecond < len(maze): #up
                    temp = []
                    temp.append(currentFirst-1)
                    temp.append(currentSecond)
                    if maze[temp[0]][temp[1]] == 0 and temp not in visited:
                        fringe.append(temp)
                if currentFirst >= 0 and currentFirst < len(maze) and currentSecond-1 >= 0 and currentSecond-1 < len(maze): #left
                    temp = []
                    temp.append(currentFirst)
                    temp.append(currentSecond-1)
                    if maze[temp[0]][temp[1]] == 0 and temp not in visited:
                        fringe.append(temp)
                if currentFirst+1 >= 0 and currentFirst+1 < len(maze) and currentSecond >= 0 and currentSecond < len(maze): #down
                    temp = []
                    temp.append(currentFirst+1)
                    temp.append(currentSecond)
                    if maze[temp[0]][temp[1]] == 0 and temp not in visited:
                        fringe.append(temp)
                if currentFirst >= 0 and currentFirst < len(maze) and currentSecond+1 >= 0 and currentSecond+1 < len(maze): #right
                    temp = []
                    temp.append(currentFirst)
                    temp.append(currentSecond+1)
                    if maze[temp[0]][temp[1]] == 0 and temp not in visited:
                        fringe.append(temp)

                visited.insert(0, current)

    return False

#visualize DFS via pygame
def visualizeDFS(maze, firstLocation, secondLocation): 
    dimen = len(maze)
    width = 5
    height = 5
    margin = 0

    pygame.init()
    screen = pygame.display.set_mode([550, 550])
    pygame.display.set_caption("DFS Visualization")
    screen.fill(black)
    clock = pygame.time.Clock()

    for i in range(dimen):
        for j in range(dimen):
            color = white
            if i == firstLocation[0] and j == firstLocation[1]:
                color = green
            elif i == secondLocation[0] and j == secondLocation[1]:
                color = red
            elif maze[i][j] == 1:
                color = black
            pygame.draw.rect(screen,
                            color,
                            [(margin + width) * j + margin,
                            (margin + height) * i + margin,
                            width,
                            height])
            pygame.display.flip()

    success = False
    done = False
    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:  
                done = True 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True

        fringe = deque() #use a stack for DFS
        fringe.append(firstLocation)
        visited = []
        while fringe:
            current = fringe.pop()
            if current[0] == secondLocation[0] and current[1] == secondLocation[1]: #if found goal then get out of here
                success = True
                break
            else:
                if current not in visited:
                    currentFirst = current[0]
                    currentSecond = current[1]
                    #check 4 neighbors to see which we can add to fringe
                    if currentFirst-1 >= 0 and currentFirst-1 < len(maze) and currentSecond >= 0 and currentSecond < len(maze): #up
                        temp = []
                        temp.append(currentFirst-1)
                        temp.append(currentSecond)
                        if maze[temp[0]][temp[1]] == 0 and temp not in visited:
                            fringe.append(temp)
                    if currentFirst >= 0 and currentFirst < len(maze) and currentSecond-1 >= 0 and currentSecond-1 < len(maze): #left
                        temp = []
                        temp.append(currentFirst)
                        temp.append(currentSecond-1)
                        if maze[temp[0]][temp[1]] == 0 and temp not in visited:
                            fringe.append(temp)
                    if currentFirst+1 >= 0 and currentFirst+1 < len(maze) and currentSecond >= 0 and currentSecond < len(maze): #down
                        temp = []
                        temp.append(currentFirst+1)
                        temp.append(currentSecond)
                        if maze[temp[0]][temp[1]] == 0 and temp not in visited:
                            fringe.append(temp)
                    if currentFirst >= 0 and currentFirst < len(maze) and currentSecond+1 >= 0 and currentSecond+1 < len(maze): #right
                        temp = []
                        temp.append(currentFirst)
                        temp.append(currentSecond+1)
                        if maze[temp[0]][temp[1]] == 0 and temp not in visited:
                            fringe.append(temp)

                    maze[current[0]][current[1]] = 3
                    color = blue
                    pygame.draw.rect(screen,
                                color,
                                [(margin + width) * current[1] + margin,
                                (margin + height) * current[0] + margin,
                                width,
                                height])
                    pygame.display.flip()
                    visited.insert(0, current)
    pygame.quit()
    return success

#find the shortest path via BFS            
def findShortestBFS(maze, firstLocation, secondLocation):
    fringe = deque() #use a queue for BFS
    first = [firstLocation[0], firstLocation[1], []]
    fringe.append(first)
    visited = []

    while fringe:
        current = fringe.popleft()
        if current[0] == secondLocation[0] and current[1] == secondLocation[1]:
            toReturn = []
            for i in current[2]:
                toReturn.append(i)
            toReturn.append([current[0], current[1]])
            return toReturn
            
        else:
            if current not in visited:
                currentFirst = current[0]
                currentSecond = current[1]
                if currentFirst-1 >= 0 and currentFirst-1 < len(maze) and currentSecond >= 0 and currentSecond < len(maze):
                    temp = []
                    temp.append(currentFirst-1)
                    temp.append(currentSecond)
                    temp.append([])
                    if current[2]:
                        for i in current[2]:
                            temp[2].append(i)
                    temp[2].append([currentFirst, currentSecond])
                    if maze[temp[0]][temp[1]] == 0 and [temp[0], temp[1]] not in visited:
                        fringe.append(temp)
                if currentFirst >= 0 and currentFirst < len(maze) and currentSecond-1 >= 0 and currentSecond-1 < len(maze):
                    temp = []
                    temp.append(currentFirst)
                    temp.append(currentSecond-1)
                    temp.append([])
                    if current[2]:
                        for i in current[2]:
                            temp[2].append(i)
                    temp[2].append([currentFirst, currentSecond])
                    if maze[temp[0]][temp[1]] == 0 and [temp[0], temp[1]] not in visited:
                        fringe.append(temp)
                if currentFirst+1 >= 0 and currentFirst+1 < len(maze) and currentSecond >= 0 and currentSecond < len(maze):
                    temp = []
                    temp.append(currentFirst+1)
                    temp.append(currentSecond)
                    temp.append([])
                    if current[2]:
                        for i in current[2]:
                            temp[2].append(i)
                    temp[2].append([currentFirst, currentSecond])
                    if maze[temp[0]][temp[1]] == 0 and [temp[0], temp[1]] not in visited:
                        fringe.append(temp)
                if currentFirst >= 0 and currentFirst < len(maze) and currentSecond+1 >= 0 and currentSecond+1 < len(maze):
                    temp = []
                    temp.append(currentFirst)
                    temp.append(currentSecond+1)
                    temp.append([])
                    if current[2]:
                        for i in current[2]:
                            temp[2].append(i)
                    temp[2].append([currentFirst, currentSecond])
                    if maze[temp[0]][temp[1]] == 0 and [temp[0], temp[1]] not in visited:
                        fringe.append(temp)

                visited.append([currentFirst, currentSecond])
    
    return -1

#find shortest path via A* and heuristic
def findShortestA(maze, firstLocation, secondLocation):
    pass

#heuristic that guesses distance based on euclidean dist formula
def determineEuDist(firstLocation, secondLocation):
    return math.sqrt(math.pow(firstLocation[0] - secondLocation[0], 2) + math.pow(firstLocation[1] - secondLocation[1], 2))

print(visualizeDFS(maze_generator(100, 0.15), [0, 0], [99, 99]))
# print(checkPathDFS(testMaze, [0, 0], [3, 3]))
# print(findShortestBFS(testMaze, [0, 0], [3, 3]))

#print(determineEuDist([0, 0], [99, 99]))