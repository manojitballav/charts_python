# In this program we will be creating a surface plot
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0,1,200)
X,Y = np.meshgrid(x,x)
Z = np.sin(X*Y)
fig = plt.figure()
sub = fig.add_subplot(1,1,1,projection = "3d")
sub.plot_surface(X,Y,Z)
fig.show()
plt.show()