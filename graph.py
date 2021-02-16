import matplotlib.pyplot as plt 
x = [0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575, 0.6]
y = [0.98666667, 0.96, 0.933333, 0.9133333, 0.84, 0.7933333, 0.68, 0.58, 0.54, 0.4133333, 0.2466667, 0.0933334, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

plt.plot(x, y)
plt.xlabel(' Density ')
plt.ylabel(' Probability of Success')

plt.title(' Density vs Probability of Success (DFS)')

plt.show()