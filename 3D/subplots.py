# In this program we will be creating a 3D plot as a sub plot

# imporitng all the libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import axes3D
from matplotlib import cm

fig  = plt.figure(figsize=plt.figaspect = (1))

# Setting up the axes of the subplot
ax = fig.add_subplot(1,1,1, projection="3d")

X = [1,100,1]
Y = 