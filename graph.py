import matplotlib.pyplot as plt
import numpy as np

x = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
y = [1, 0.84, 0.68, 0.46, 0.34, 0.2, 0.04, 0.02, 0.02, 0, 0.02, 0.02, 0, 0.02, 0.04, 0.06, 0, 0.02, 0, 0, 0]
y2 = [1, 0.98, 0.9, 0.76, 0.6, 0.18, 0.06, 0, 0, 0.02, 0.02, 0.06, 0, 0, 0, 0.02, 0.02, 0.04, 0.02, 0, 0]
y3 = [1, 0.98, 0.9, 0.8, 0.64, 0.28, 0.08, 0.08, 0, 0, 0.02, 0.02, 0.02, 0.04, 0.02, 0, 0.02, 0.02, 0, 0, 0]
plt.plot(x, y, label = "Strategy 1")
plt.plot(x, y2, label = "Strategy 2")
plt.plot(x, y3, label = "Strategy 3")
plt.xlabel(' Flammability ')
plt.ylabel(' Probability of Success')

plt.title(' Strategy 1 vs. Strategy 2 vs. Strategy 3')
plt.xticks(np.arange(0, 1, 0.1))
plt.yticks(np.arange(0, 1, 0.05))
plt.legend()
plt.show()