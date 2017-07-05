# This program will contain code related to map the probability distribution on a histogram
import matplotlib.pyplot as plt
import numpy as np

# generating 1000 randome values
# x = np.random.random(100)

# Getting normal distribution values
x = np.random.normal(0,1,400)

# plotting the probability of the random values
plt.hist(x)
# Displaying the graph
plt.show()