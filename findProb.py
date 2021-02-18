from searches import *
from mazeGenerator import maze_generator
import random
from fire import *

# def findProbsStratOne():
#     #find for 0,1
#     success = 0
#     failures = 0
#     for runs in range(100):
#         if strategyOne(maze_generator(100, 0.3), 0.1) is True:
#             success += 1
#         else:
#             failures += 1
#     print("Probability of success for 0.125 is: " + str(success / 150))


# def findProbsDFS():
#     #find for 0.1
#     success = 0
#     failures = 0
#     for runs in range(150):
#         if checkPathDFS(maze_generator(1750, 0.125), [0, 0], [1749, 1749]) is True:
#             success += 1
#         else:
#             failures += 1
#     #print("Probability of success for 0.125 is: " + str(success / 150))
    
#     #find for 0.2
#     success = 0
#     failures = 0
#     for runs in range(150):
#         if checkPathDFS(maze_generator(1750, 0.175), [0, 0], [1749, 1749]) is True:
#             success += 1
#         else:
#             failures += 1
#     #print("Probability of success for 0.175 is: " + str(success / 150))

#     #find for 0.3
#     success = 0
#     failures = 0
#     for runs in range(150):
#         if checkPathDFS(maze_generator(1750, 0.225), [0, 0], [1749, 1749]) is True:
#             success += 1
#         else:
#             failures += 1
#     #print("Probability of success for 0.225 is: " + str(success / 150))
    
#     #find for 0.4
#     success = 0
#     failures = 0
#     for runs in range(150):
#         if checkPathDFS(maze_generator(1750, 0.275), [0, 0], [1749, 1749]) is True:
#             success += 1
#         else:
#             failures += 1
#     #print("Probability of success for 0.275 is: " + str(success / 150))
    
#     #find for 0.5
#     success = 0
#     failures = 0
#     for runs in range(150):
#         if checkPathDFS(maze_generator(1750, 0.325), [0, 0], [1749, 1749]) is True:
#             success += 1
#         else:
#             failures += 1
#     #print("Probability of success for 0.325 is: " + str(success / 150))
    
#     #find for 0.6
#     success = 0
#     failures = 0
#     for runs in range(150):
#         if checkPathDFS(maze_generator(1750, 0.375), [0, 0], [1749, 1749]) is True:
#             success += 1
#         else:
#             failures += 1
#     #print("Probability of success for 0.375 is: " + str(success / 150))
    
#     #find for 0.7
#     success = 0
#     failures = 0
#     for runs in range(150):
#         if checkPathDFS(maze_generator(1750, 0.425), [0, 0], [1749, 1749]) is True:
#             success += 1
#         else:
#             failures += 1
#     #print("Probability of success for 0.425 is: " + str(success / 150))
    
#     #find for 0.8
#     success = 0
#     failures = 0
#     for runs in range(150):
#         if checkPathDFS(maze_generator(1750, 0.475), [0, 0], [1749, 1749]) is True:
#             success += 1
#         else:
#             failures += 1
#     #print("Probability of success for 0.475 is: " + str(success / 150))
    
# def findBFSData():
#     pass

def recordingNumNodesBFS():
#     #find avg nodes accessed by density 0.05
#     numNodes = 0
#     count = 0
#     for runs in range(100):
#         path, nodes = findShortestBFS(maze_generator(900, 0.05), [0, 0], [899, 899])
#         numNodes += nodes
#         count += 1
#         print( count, "number of nodes = ", numNodes)
#     print("Average number of nodes explored by BFS of density 0.05 is: " + str(numNodes / 100))

# #find avg nodes accessed by density 0.10
#     numNodes = 0
#     count = 0
#     for runs in range(100):
#         path, nodes = findShortestBFS(maze_generator(900, 0.10), [0, 0], [899, 899])
#         numNodes += nodes
#         count += 1
#         print( count, "number of nodes = ", numNodes)
#     print("Average number of nodes explored by BFS of density 0.10 is: " + str(numNodes / 100))

# #find avg nodes accessed by density 0.15
#     numNodes = 0
#     count = 0
#     for runs in range(100):
#         path, nodes = findShortestBFS(maze_generator(900, 0.15), [0, 0], [899, 899])
#         numNodes += nodes
#         count += 1
#         print( count, "number of nodes = ", numNodes)
#     print("Average number of nodes explored by BFS of density 0.15 is: " + str(numNodes / 100))

# #find avg nodes accessed by density 0.20
#     numNodes = 0
#     count = 0
#     for runs in range(100):
#         path, nodes = findShortestBFS(maze_generator(900, 0.20), [0, 0], [899, 899])
#         numNodes += nodes
#         count += 1
#         print( count, "number of nodes = ", numNodes)
#     print("Average number of nodes explored by BFS by the density 0.20 is: " + str(numNodes / 100))

# #find avg nodes accessed by density 0.25
#     numNodes = 0
#     count = 0
#     for runs in range(100):
#         path, nodes = findShortestBFS(maze_generator(900, 0.25), [0, 0], [899, 899])
#         numNodes += nodes
#         count += 1
#         print( count, "number of nodes = ", numNodes)
#     print("Average number of nodes explored by BFS by the density 0.25 is: " + str(numNodes / 100))

# #find avg nodes accessed by density 0.30
#     numNodes = 0
#     count = 0
#     for runs in range(100):
#         path, nodes = findShortestBFS(maze_generator(900, 0.30), [0, 0], [899, 899])
#         numNodes += nodes
#         count += 1
#         print( count, "number of nodes = ", numNodes)
#     print("Average number of nodes explored by BFS by the density 0.30 is: " + str(numNodes / 100))

#find avg nodes accessed by density 0.35
    numNodes = 0
    count = 0
    for runs in range(100):
        path, nodes = findShortestBFS(maze_generator(900, 0.35), [0, 0], [899, 899])
        numNodes += nodes
        count += 1
        print( count, "number of nodes = ", numNodes)
    print("Average number of nodes explored by BFS by the density 0.35 is: " + str(numNodes / 100))

#find avg nodes accessed by density 0.40
    numNodes = 0
    count = 0
    for runs in range(100):
        path, nodes = findShortestBFS(maze_generator(900, 0.40), [0, 0], [899, 899])
        numNodes += nodes
        count += 1
        print( count, "number of nodes = ", numNodes)
    print("Average number of nodes explored by BFS by the density 0.40 is: " + str(numNodes / 100))

#find avg nodes accessed by density 0.45
    numNodes = 0
    count = 0
    for runs in range(100):
        path, nodes = findShortestBFS(maze_generator(900, 0.45), [0, 0], [899, 899])
        numNodes += nodes
        count += 1
        print( count, "number of nodes = ", numNodes)
    print("Average number of nodes explored by BFS by the density 0.45 is: " + str(numNodes / 100))

#find avg nodes accessed by density 0.50
    numNodes = 0
    count = 0
    for runs in range(100):
        path, nodes = findShortestBFS(maze_generator(900, 0.50), [0, 0], [899, 899])
        numNodes += nodes
        count += 1
        print( count, "number of nodes = ", numNodes)
    print("Average number of nodes explored by BFS by the density 0.50 is: " + str(numNodes / 100))

    #find avg nodes accessed by density 0.55
    numNodes = 0
    count = 0
    for runs in range(100):
        path, nodes = findShortestBFS(maze_generator(900, 0.55), [0, 0], [899, 899])
        numNodes += nodes
        count += 1
        print( count, "number of nodes = ", numNodes)
    print("Average number of nodes explored by BFS by the density 0.55 is: " + str(numNodes / 100))

#find avg nodes accessed by density 0.60
    numNodes = 0
    count = 0
    for runs in range(100):
        path, nodes = findShortestBFS(maze_generator(900, 0.60), [0, 0], [899, 899])
        numNodes += nodes
        count += 1
        print( count, "number of nodes = ", numNodes)
    print("Average number of nodes explored by BFS by the density 0.60 is: " + str(numNodes / 100))

#find avg nodes accessed by density 0.65
    numNodes = 0
    count = 0
    for runs in range(100):
        path, nodes = findShortestBFS(maze_generator(900, 0.65), [0, 0], [899, 899])
        numNodes += nodes
        count += 1
        print( count, "number of nodes = ", numNodes)
    print("Average number of nodes explored by BFS by the density 0.65 is: " + str(numNodes / 100))

#find avg nodes accessed by density 0.70
    numNodes = 0
    count = 0
    for runs in range(100):
        path, nodes = findShortestBFS(maze_generator(900, 0.70), [0, 0], [899, 899])
        numNodes += nodes
        count += 1
        print( count, "number of nodes = ", numNodes)
    print("Average number of nodes explored by BFS by the density 0.70 is: " + str(numNodes / 100))

#find avg nodes accessed by density 0.75
    numNodes = 0
    count = 0
    for runs in range(100):
        path, nodes = findShortestBFS(maze_generator(900, 0.75), [0, 0], [899, 899])
        numNodes += nodes
        count += 1
        print( count, "number of nodes = ", numNodes)
    print("Average number of nodes explored by BFS by the density 0.75 is: " + str(numNodes / 100))

#find avg nodes accessed by density 0.80
    numNodes = 0
    count = 0
    for runs in range(100):
        path, nodes = findShortestBFS(maze_generator(900, 0.80), [0, 0], [899, 899])
        numNodes += nodes
        count += 1
        print( count, "number of nodes = ", numNodes)
    print("Average number of nodes explored by BFS by the density 0.80 is: " + str(numNodes / 100))

#find avg nodes accessed by density 0.85
    numNodes = 0
    count = 0
    for runs in range(100):
        path, nodes = findShortestBFS(maze_generator(900, 0.85), [0, 0], [899, 899])
        numNodes += nodes
        count += 1
        print( count, "number of nodes = ", numNodes)
    print("Average number of nodes explored by BFS by the density 0.85 is: " + str(numNodes / 100))

#find avg nodes accessed by density 0.90
    numNodes = 0
    count = 0
    for runs in range(100):
        path, nodes = findShortestBFS(maze_generator(900, 0.90), [0, 0], [899, 899])
        numNodes += nodes
        count += 1
        print( count, "number of nodes = ", numNodes)
    print("Average number of nodes explored by BFS by the density 0.90 is: " + str(numNodes / 100))

#find avg nodes accessed by density 0.95
    numNodes = 0
    count = 0
    for runs in range(100):
        path, nodes = findShortestBFS(maze_generator(900, 0.95), [0, 0], [899, 899])
        numNodes += nodes
        count += 1
        print( count, "number of nodes = ", numNodes)
    print("Average number of nodes explored by BFS by the density 0.95 is: " + str(numNodes / 100))

#find avg nodes accessed by density 1.00
    numNodes = 0
    count = 0
    for runs in range(100):
        path, nodes = findShortestBFS(maze_generator(900, 1.0), [0, 0], [899, 899])
        numNodes += nodes
        count += 1
        print( count, "number of nodes = ", numNodes)
    print("Average number of nodes explored by BFS by the density 1.0 is: " + str(numNodes / 100))