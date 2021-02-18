from fire import *
from searches import *


density = 0.05
while density <= 0.95:
    oneSuccesses = 0
    oneFailures = 0
    iterations = 0
    #run strat 1 for density
    while iterations < 20:
        status = strategyOne(maze_generator(100, 0.3), density)
        if status == -2:
            continue
        elif status == -1:
            oneFailures+=1
        elif status == 200:
            oneSuccesses+=1
        iterations += 1
    print("Strategy 1 success rate for {}: {}".format(density, oneSuccesses/20))
    iterations = 0
    twoSuccesses = 0
    twoFailures = 0
    while iterations < 20:
        status = strategyTwo(maze_generator(100, 0.3), density)
        if status == -2:
            continue
        elif status == -1:
            twoFailures+=1
        elif status == 200:
            twoSuccesses+=1
        iterations += 1
    print("Strategy 2 success rate for {}: {}".format(density, twoSuccesses/20))
    density += 0.05
