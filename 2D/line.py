# This python program will contain the code to create a line chart with linear values
import matplotlib.pyplot as plt
import numpy as np

# creating linear values 0,1 with 100 divisions
x = np.linspace(0,1,100)
# mimicing the same values
y = x

# plotting the graph with line (-)red(r) color
plt.plot(x,y,'-r')
# Displaying the graph
plt.show()

