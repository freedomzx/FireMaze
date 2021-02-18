from fire import *
from findProb import recordingNumNodesBFS
from mazeGenerator import maze_generator


testMaze = [[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0 , 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]]

#start_fire(testMaze)
#print(testMaze)
#advance_fire(testMaze, 0.3)
#print(testMaze)
#advance_fire(testMaze, 0.3)
#print(testMaze)
#advance_fire(testMaze, 0.3)
#print(testMaze)
#print(findProbsStratOne())
#advance_fire(maze_generator(100, 0.3), 0.1)
# print(visualizeStrategyOne(maze_generator(100, 0.3), 0.2))
# advance_fire(maze_generator(100, 0.3), 0.3)

print(recordingNumNodesBFS())