from collections import deque

testMaze = ([[0, 1, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 1],
[0, 1, 1, 0]]
)

def checkPathDFS(maze, firstLocation, secondLocation): #maze is a dim x dim matrix, firstLocation is a list of 2 nums, secondLocation is the same
    fringe = deque() #use a stack for DFS
    fringe.append(firstLocation)
    visited = []
    while fringe:
        current = fringe.pop()
        if current[0] == secondLocation[0] and current[1] == secondLocation[1]:
            return True #found a path
        else:
            if current not in visited:
                currentFirst = current[0]
                currentSecond = current[1]
                if currentFirst-1 >= 0 and currentFirst-1 < len(maze) and currentSecond >= 0 and currentSecond < len(maze):
                    temp = []
                    temp.append(currentFirst-1)
                    temp.append(currentSecond)
                    if maze[temp[0]][temp[1]] == 0 and temp not in visited:
                        fringe.append(temp)
                if currentFirst >= 0 and currentFirst < len(maze) and currentSecond-1 >= 0 and currentSecond-1 < len(maze):
                    temp = []
                    temp.append(currentFirst)
                    temp.append(currentSecond-1)
                    if maze[temp[0]][temp[1]] == 0 and temp not in visited:
                        fringe.append(temp)
                if currentFirst+1 >= 0 and currentFirst+1 < len(maze) and currentSecond >= 0 and currentSecond < len(maze):
                    temp = []
                    temp.append(currentFirst+1)
                    temp.append(currentSecond)
                    if maze[temp[0]][temp[1]] == 0 and temp not in visited:
                        fringe.append(temp)
                if currentFirst >= 0 and currentFirst < len(maze) and currentSecond+1 >= 0 and currentSecond+1 < len(maze):
                    temp = []
                    temp.append(currentFirst)
                    temp.append(currentSecond+1)
                    if maze[temp[0]][temp[1]] == 0 and temp not in visited:
                        fringe.append(temp)

                visited.insert(0, current)

    return False


print(checkPathDFS(testMaze, [0, 0], [3, 3]))