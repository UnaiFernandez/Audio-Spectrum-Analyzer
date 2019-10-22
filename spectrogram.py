from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# data = np.loadtxt("pruebaplot3d.csv", delimiter=',')
# print(data)

# X, Y = np.meshgrid(data[:, 6], data[:, 0])

# Z = np.tile(data[:, 5], len(data[:, 5]))
# X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Y = [193, 93, 73, 107, 91, 111, 107, 140, 66, 100]
# Z = [9, 6, 3, 8, 10, 7, 1, 2, 10, 4]

data = pd.read_csv('pruebaplot3d.csv')
print(data)
X = np.array(data['time'])
print(X)
f1 = np.array(data['Hz1'])
f2 = np.array(data['Hz2'])
f3 = np.array(data['Hz3'])
f4 = np.array(data['Hz4'])
f5 = np.array(data['Hz5'])
Y = f1+f2+f3+f4+f5
Z = np.array([data['dB']])
# X = [1,1,1,1,2,2,2,2,3,3,3,3]
# Y = [1,4,5,6,1,4,5,6,1,4,5,6]
# Z = [2,6,3,6,2,7,4,6,2,4,2,3]
print(len(X))
print(len(Y))
print(len(Z))

fig = plt.figure()
ax = fig.gca(projection='3d')
#ax.scatter(X, Y, Z)
ax.plot_trisurf(data['time'], data['Hz1'], data['dB'], cmap=plt.cm.viridis, linewidth=0.2)
#ax.contourf(X, Y, Z)
plt.show()
