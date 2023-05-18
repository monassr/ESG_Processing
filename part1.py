import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import numpy as np
from scipy.signal import find_peaks


def FivePointDiff(signal):
    
    temp = []
    for i in range(2,len(signal)-2):
        
        sample = (1/8)*(-signal[i-2] - (2*signal[i-1])+ (2*signal[i+1]) + signal[i+2])
        temp.append(sample)
        
    return temp

def Squaring(signal):
    
    temp =[]
    for i in range(0,len(signal)):
        temp.append(signal[i] * signal[i])
        
    return temp

def Smoothing(data):
    
    temp=[]
 
    for i in range(0,len(data)):
        
        sample = 0
        for j in range(1,31+1):
            if (i - (31-j)) < 0:
                continue
            sample+=data[i - (31-j)]
            
        temp.append(sample*(1/31))
        
    return temp


#need to ask the prof
def AutoCorr(signal):
    
    n = len(signal)
    temp = []

    for i in range(0,len(signal)):
        
        sample = 0
        for j in range(i, len(signal)):
            
            sample += signal[j] * signal[j-i]
            
    
        temp.append(sample)

    return temp




#MAIN

file = open("./Data1.txt", "r")
data_str = file.read()
file.close()
data_str = data_str.split("\n")

signal = []
for i in data_str:
    signal.append(float(i))
    
signal_diff = FivePointDiff(signal)
signal_sq = Squaring(signal_diff)
signal_smooth = Smoothing(signal_sq)
signal_auto = AutoCorr(signal_smooth)

_,plot = plt.subplots(figsize=(12, 6))
plot.plot(signal)
plot.set_title('Original Data')
plt.show()


_,plot = plt.subplots(figsize=(12, 6))
plot.plot(signal_diff)
plot.set_title('After Differentiation')
plt.show()


_,plot = plt.subplots(figsize=(12, 6))
plot.plot(signal_sq)
plot.set_title('After Squaring')
plt.show()


_,plot = plt.subplots(figsize=(12, 6))
plot.plot(signal_smooth)
plot.set_title('After Smoothing')
plt.show()


_,plot = plt.subplots(figsize=(12, 6))
plot.plot(signal_auto)
plot.set_title('Auto')
plt.show()

sampling_rate = 512  


peaks , _ = find_peaks(signal_auto)


firstPeak = peaks[2]

time = firstPeak / sampling_rate
heart_rate = 60 / time  

print("happens at ", firstPeak)
print("time is ", time)
print(f"The heart rate is {heart_rate} beats per minute.")