import random
import decimal
def maze_generator(x, obstacle_density):
    # since maze is a 2d array
    maze = []
    randomObstacles = round(random.uniform(0,1), 2)
    obstacles_threshold = randomObstacles * 100

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

maze = maze_generator(4, .50)
print(maze)

