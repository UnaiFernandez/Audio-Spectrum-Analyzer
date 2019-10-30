from serial import Serial
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from scipy.io import wavfile
import tqdm
import csv

import warnings
warnings.simplefilter("ignore")


arduino = Serial('/dev/ttyACMM0', 9600, timeout = 5)

time.sleep(1)
print("Collecting data...")

arduino.flush()

#Open the file with name 'data.csv' truncate it and close it
filename = "data.csv"
file = open(filename, "r+")
file.truncate(0)
file.close()

#open the file to add components to it
data = pd.read_csv('data.csv')
print(data)
#VARIABLES
pos = 1
X = np.array()
f1 = np.array()
f2 = np.array()
f3 = np.array()
f4 = np.array()
f5 = np.array()
Z = np.array()

#loop that creates the progressbar
for i in tqdm.tqdm(range(400)):
    data = int(arduino.readline())
    time.sleep(0.001)
    file.write(str(pos))
    file.write(";")
    file.write(str(data))
    file.write("\n")
    pos = pos + 1 


#read csv and add values to the lists
with open(filename, 'r') as file:
    plots = csv.reader(file, delimiter = ' ')
    for row in plots:
        X = np.append(X, data['time'])
        f1 = np.append(f1, data['Hz1'])
        f2 = np.append(f2, data['Hz1'])
        f3 = np.append(f3, data['Hz1'])
        f4 = np.append(f4, data['Hz1'])
        f5 = np.append(f5, data['Hz1'])
        Z = np.append(Z, data['dB'])

# data = np.loadtxt("pruebaplot3d.csv", delimiter=',')
# print(data)

# X, Y = np.meshgrid(data[:, 6], data[:, 0])

# Z = np.tile(data[:, 5], len(data[:, 5]))
# X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Y = [193, 93, 73, 107, 91, 111, 107, 140, 66, 100]
# Z = [9, 6, 3, 8, 10, 7, 1, 2, 10, 4]

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
