# In this program we will be plotting a 3D sine graph
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
sub = fig.add_subplot(1,1,1,projection="3d")
t = np.linspace(0,4*np.pi,500)
x = np.sin(t)
x = np.cos(t)
y = np.sin(t)
z = t
sub.plot(x,y,z)
plt.show()