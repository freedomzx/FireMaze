from collections import deque
import time
from mazeGenerator import maze_generator
import pygame
import math
import heapq

testMaze = [[0, 1, 0, 0],
[0, 1, 1, 0],
[0 , 0, 0, 1],
[0, 1, 0, 0]]


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
                #add current procesed node to visited list
                visited.insert(0, current)
    #couldnt find anything
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
                color = green #color start green
            elif i == secondLocation[0] and j == secondLocation[1]:
                color = red #color goal red
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

#visualize BFS via pygame
def visualizeBFS(maze, firstLocation, secondLocation):
    dimen = len(maze)
    width = 6
    height = 6
    margin = 0

    pygame.init()
    screen = pygame.display.set_mode([600, 600])
    pygame.display.set_caption("DFS Visualization")
    screen.fill(black)
    clock = pygame.time.Clock()

    for i in range(dimen):
        for j in range(dimen):
            color = white
            if i == firstLocation[0] and j == firstLocation[1]:
                color = green #color start green
            elif i == secondLocation[0] and j == secondLocation[1]:
                color = red #color goal red
            elif maze[i][j] == 1:
                color = black
            pygame.draw.rect(screen,
                            color,
                            [(margin + width) * j + margin,
                            (margin + height) * i + margin,
                            width,
                            height])
            pygame.display.flip()

    success = [False, []]
    done = False
    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:  
                done = True 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True

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
                success = [True, toReturn]
                break
                
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

                    maze[current[0]][current[1]] = 3
                    color = blue
                    pygame.draw.rect(screen,
                                color,
                                [(margin + width) * current[1] + margin,
                                (margin + height) * current[0] + margin,
                                width,
                                height])
                    pygame.display.flip()
                    visited.append([currentFirst, currentSecond])
            
    pygame.quit()
    return success


#heuristic that guesses distance based on euclidean dist formula
def determineEuDist(firstLocation, secondLocation):
    return math.sqrt(math.pow(firstLocation[0] - secondLocation[0], 2) + math.pow(firstLocation[1] - secondLocation[1], 2))

#find the index in infoList based on row and column
def findILIndex(row, column, dim):
    return row*dim + column

#just check if a child node could be valid for A*
#coudlve made this for DFS/BFS but too lazy to go back and put it in, so just for A* instead
def checkValidChild(maze, row, column):
    if (row >= 0 and row < len(maze)) and (column >= 0 and column < len(maze)) and maze[row][column] != 1:
        return True
    return False

#add or update something to fringe
def addOrUpdate(fringe, newKey, coordinates):
    found = False
    for i in fringe: #check if it exists, update if so
        if i[1] == coordinates:
            i[0] = newKey
            found = True
            break
    #if it doesnt exist, add it in
    if not found:
        heapq.heappush(fringe, [newKey, coordinates])
    #re-heapify the fringe
    heapq.heapify(fringe)
    # print("added/updated")
    # print(fringe)

#find shortest path via A* and heuristic
def findShortestA(maze, firstLocation, secondLocation):
    infoList = [] #list of dictionaries for information of each potential index in matrix
    for i in range(len(maze)):
        for j in range(len(maze)):
            toAdd = {} #dictionary of properties
            toAdd["distance"] = 999999 # from root
            toAdd["processed"] = False #processed in while loop or not
            toAdd["previous"] = [-1, -1] #previous coordinates
            toAdd["estimated_distance"] = determineEuDist([i, j], [secondLocation[0], secondLocation[1]]) #heuristic
            infoList.append(toAdd)

    #set the root's distance to itself to 0 and set the previous node for it to itself
    rootIndex = findILIndex(firstLocation[0], firstLocation[1], len(maze))
    infoList[rootIndex]["distance"] = 0
    infoList[rootIndex]["previous"] = [firstLocation[0], secondLocation[0]]
    
    #create fringe and push root onto it
    #fringe priority is estimated distance to the goal node
    fringe = []
    heapq.heappush(fringe, [infoList[rootIndex]["estimated_distance"], [firstLocation[0], firstLocation[1]]])

    #work and process child nodes thru fringe until either fringe is empty or goal is reached
    while fringe:
        current = heapq.heappop(fringe) #current will look like [distance, [coord1, coord2]]
        currentIndex = findILIndex(current[1][0], current[1][1], len(maze))
        currentDistance = infoList[currentIndex]["distance"]
        if not infoList[currentIndex]["processed"]:
            #check 4 potential children
            #up
            if checkValidChild(maze, current[1][0]-1, current[1][1]):
                #print("valid chek1")
                childIndex = findILIndex(current[1][0]-1, current[1][1], len(maze))
                if currentDistance + 1 < infoList[childIndex]["distance"]: #check if the current path is better than recorded
                    infoList[childIndex]["distance"] = currentDistance + 1
                    infoList[childIndex]["previous"] = [current[1][0], current[1][1]]
                    addOrUpdate(fringe, currentDistance + 1, [current[1][0]-1, current[1][1]])

                #now check if that was the goal
                if current[1][0]-1 == secondLocation[0] and current[1][1] == secondLocation[1]:
                    return ["Yes"]
            #left
            if checkValidChild(maze, current[1][0], current[1][1]-1): 
                #print("valid chek2")
                childIndex = findILIndex(current[1][0], current[1][1]-1, len(maze))
                if currentDistance + 1 < infoList[childIndex]["distance"]: #check if the current path is better than recorded
                    infoList[childIndex]["distance"] = currentDistance + 1
                    infoList[childIndex]["previous"] = [current[1][0], current[1][1]]
                    addOrUpdate(fringe, currentDistance + 1, [current[1][0], current[1][1]-1])

                #now check if that was the goal
                if current[1][0] == secondLocation[0] and current[1][1]-1 == secondLocation[1]:
                    return ["Yes"]
            #down
            if checkValidChild(maze, current[1][0]+1, current[1][1]): 
                #print("valid chek3")
                childIndex = findILIndex(current[1][0]+1, current[1][1], len(maze))
                #print(infoList[childIndex]["distance"])
                if currentDistance + 1 < infoList[childIndex]["distance"]: #check if the current path is better than recorded
                    infoList[childIndex]["distance"] = currentDistance + 1
                    infoList[childIndex]["previous"] = [current[1][0], current[1][1]]
                    addOrUpdate(fringe, currentDistance + 1, [current[1][0]+1, current[1][1]])

                #now check if that was the goal
                if current[1][0]+1 == secondLocation[0] and current[1][1] == secondLocation[1]:
                    return ["Yes"]
            #right
            if checkValidChild(maze, current[1][0], current[1][1]+1):
                #print("valid chek4")
                childIndex = findILIndex(current[1][0], current[1][1]+1, len(maze))
                if currentDistance + 1 < infoList[childIndex]["distance"]: #check if the current path is better than recorded
                    infoList[childIndex]["distance"] = currentDistance + 1
                    infoList[childIndex]["previous"] = [current[1][0], current[1][1]]
                    addOrUpdate(fringe, currentDistance + 1, [current[1][0], current[1][1]+1])

                #now check if that was the goal
                if current[1][0] == secondLocation[0] and current[1][1]+1 == secondLocation[1]:
                    return ["Yes"]
            # mark currently popped from fringe node as processed
            infoList[currentIndex]["processed"] = True
    
    #return empty list if it can't find the goal node from the start state
    return []


#print(visualizeDFS(maze_generator(100, 0.3), [0, 0], [99, 99]))
#print(checkPathDFS(testMaze, [0, 0], [3, 3]))
#print(findShortestBFS(testMaze, [0, 0], [3, 3]))
#print(findShortestA(maze_generator(100, 0.3), [0, 0], [99, 99]))
#print(determineEuDist([99, 98], [99, 99]))
print(visualizeBFS(maze_generator(10, 0.3), [0, 0], [9, 9]))