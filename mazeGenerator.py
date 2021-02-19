import random
import decimal
import pygame
import time
def maze_generator(x, obstacle_density):
    # since maze is a 2d array, start with list
    maze = []
    obstacles_threshold = obstacle_density * 100

    #go through every index and randomly see whether or not it will be an obstacle
    for i in range(x):
        maze_line = []
        for j in range(x):
            randomNum = random.randint(1, 100)
            if randomNum <= obstacles_threshold:
                maze_line.append(1)
            elif randomNum > obstacles_threshold:
                maze_line.append(0)
        maze.append(maze_line)
    maze[0][0] = 0
    maze[len(maze) - 1][len(maze) - 1] = 0
    return maze