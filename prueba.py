import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('pruebaplot3d.csv')

f1 = np.array(data['Hz1'])
f2 = np.array(data['Hz2'])
f3 = np.array(data['Hz3'])
f4 = np.array(data['Hz4'])
f5 = np.array(data['Hz5'])

frequencies = np.concatenate((f1, f2, f3, f4, f5))

print(frequencies)

samplingFrequency = 1

s1 = np.empty([0])
s2 = np.empty([0])

start = 1

stop = samplingFrequency + 1

for frequency in frequencies:
    sub1 = np.arange(start, stop, 1)

    sub2 = np.sin(2 * np.pi * sub1 * frequency * 1 / samplingFrequency) + np.random.randn(len(sub1))

    s1 = np.append(s1, sub1)
    s2 = np.append(s2, sub2)

    start = stop + 1

    stop = start + samplingFrequency

plt.subplot(111)

#powerSpectrum, freqenciesFound, time, imageAxis =
plt.specgram(s2, Fs=samplingFrequency, sides='onesided')

plt.xlabel('Time')

plt.ylabel('Frequency')

plt.show()'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

time1 = np.arange(0,5,0.0001)
time = np.arange(0,15,0.0001)
data1=np.sin(2*np.pi*300*time1)
data2=np.sin(2*np.pi*600*time1)
data3=np.sin(2*np.pi*900*time1)
data=np.append(data1,data2 )
data=np.append(data,data3)
print(len(time))
print(len(data))

NFFT = 200     # the length of the windowing segments
Fs = 500  # the sampling rate

# plot signal and spectrogram

ax1 = plt.subplot(211)
plt.plot(time,data)   # for this one has to either undersample or zoom in
plt.xlim([0,15])
plt.subplot(212 )  # don't share the axis
Pxx, freqs, bins, im = plt.specgram(data, NFFT=NFFT,   Fs=Fs,noverlap=100, cmap=plt.cm.gist_heat)
plt.show()
