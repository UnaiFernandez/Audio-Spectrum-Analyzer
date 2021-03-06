from serial import Serial # to use the serial port
import time
import tqdm # library for the progressbar
import matplotlib.pyplot as plt # to plot the data
import numpy as np # to work with numbers
import csv # to work with csv files

import warnings
warnings.simplefilter("ignore")

# this program is going to try to read the data from the serial port,
# if the port is busy, a message will appear in the terminal
#try:
arduino = Serial('/dev/ttyACM0', 9600, timeout = 5)
#except:
 #   print("Busy port!!")

# wait a second
time.sleep(1)
print("Collecting data...")

# to clean the serial port
arduino.flush()

# open the file with name 'data.csv' truncate it and close it
filename = "data.csv"
file = open(filename, "r+")
file.truncate(0)
file.close()

# open the file to add components to it
file = open (filename, "a+")
#VARIABLES
pos = 1 # position variable
x = [] #list for x values
y = [] #list for y values
# loop that creates the progressbar while it reads data from the serial port
for i in tqdm.tqdm(range(400)):
	data = int(arduino.readline()) # to read data from the port
	time.sleep(0.01)
	file.write(str(pos))
	file.write(";")
	file.write(str(data))
	file.write("\n")
	pos = pos + 1

# this part of the code read the data from the csv file previously created and add each value to their correspondet list (x or y)
with open(filename, 'r') as file:
	plots = csv.reader(file, delimiter = ';')
	for row in plots:
		x.append(int(row[0]))
		y.append(int(row[1]))

# to plot the data
fig = plt.figure()
plt.title('Arduino Serial')
plt.xlabel('Position')
plt.ylabel('Voltage')
plt.plot(x, y)
plt.show()

yn = input("--> Do you want to save the plot? [Y/N]")
if (yn.lower() == 'y'):
	print("--> Name your plot file")
	imgfile = input()+".png"
	print("--> Your file has been saved and stored successfully as '" + imgfile + "' in '/plots' directory")
	savepath = "plots/"+imgfile
	fig.savefig(savepath, bbox_inches="tight" )
else:
	print("--> Done!, plot not saved")


