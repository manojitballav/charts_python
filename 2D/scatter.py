# This python program will contain the code to create a scatter plot with random values
import matplotlib.pyplot as plt
import numpy as np

# generating 100 randome values
x = np.random.random(100)
# generating y random values
y = np.random.random(100)

# plotting scatter plot with red markers
plt.scatter(x,y,marker="o",color="green")
# Displaying the graph
plt.show()