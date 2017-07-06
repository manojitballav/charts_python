# In this program we will be creating a surface plot
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Adding up the values
X = list(range(10))
Y = list(range(10))

# x = [1,100,2]
# y = [1,100,2]
# Setting up the meshgrid with the X and Y values
X,Y = np.meshgrid(X,Y)

# Setting up the values of Z
Z = [10,2,30,40,30,10,5,6,5,20]

# Creating up the entire figure
fig = plt.figure()

# Creating a sub plot to plot the 3D projection
# adding up the features of subplot
sub = fig.add_subplot(1,1,1,projection = "3d")

# Setting up the subplot with values
sub.plot_surface(X,Y,Z)


# Displaying the plot
plt.show()