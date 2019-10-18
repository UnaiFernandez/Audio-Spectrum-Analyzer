from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np




def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-20, 20, 60)
y = np.linspace(-20, 20, 60)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.xlabel('sec')
plt.ylabel('Hz')
plt.colorbar();

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_xlabel('sec')
ax.set_ylabel('Hz')
ax.set_zlabel('dB')
ax.set_title('surface');




plt.show()