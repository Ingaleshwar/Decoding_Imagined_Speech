import subprocess
import os
from rpi_lcd import LCD
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import matplotlib.pyplot as plt
import numpy as np
import mne
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")
import logging
logging.getLogger('mne').setLevel(logging.ERROR)
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from scipy.stats import skew, kurtosis
import joblib
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2) 

def send_command(command):
    ser.write(f"{command}".encode())
    time.sleep(1)  # Wait for the Arduino to process the command

# changing the current directory
os.chdir(r'/home/ISR/Desktop/demo/')

# initialising sound module
pygame.init()
hello = pygame.mixer.Sound("audio/hello.wav")
stop = pygame.mixer.Sound("audio/stop.wav")
tq = pygame.mixer.Sound("audio/thank you.wav")

# initialing LCD
lcd = LCD()
lcd.text("Waiting for file",1)
lcd.text("  to be loaded",2)
 

# Reading the .fif file
# 228 4 7_44 Thank You
# 107 3 5_11 Stop
# 168 1 4_2 Hello
lcd.clear()
lcd.text("Loading",1)
lcd.text("the file",2)
sub = 7
trial = 44

data_dir = f'data/{sub}_{trial}.fif'
raw = mne.io.read_raw_fif(data_dir, preload=True)
data, times = raw[:]
raw.close()

# Feature Extraction
lcd.clear()
lcd.text("Extracting the",1)
lcd.text("Features",2)
data_mean_removed = data - np.mean(data, axis=1, keepdims=True)
fft_data = np.fft.fft(data_mean_removed, axis=1)
sampling_freq = 256 
num_samples = fft_data.shape[1]
freq_axis = np.fft.fftfreq(num_samples, d=1/sampling_freq)

magnitude_threshold = 2000
fft_result = np.where(np.abs(fft_data) > magnitude_threshold, 2000, fft_data)
magnitude = np.abs(fft_result)

statistics = np.zeros((1, 10, 4))
for channel_idx in range(10):
    current_magnitude = magnitude[:, channel_idx]
    
    mean_val = np.mean(current_magnitude)
    median_val = np.median(current_magnitude)
    skewness_val = skew(current_magnitude)
    kurtosis_val = kurtosis(current_magnitude)

    statistics[0, channel_idx, 0] = mean_val
    statistics[0, channel_idx, 1] = median_val
    statistics[0, channel_idx, 2] = skewness_val
    statistics[0, channel_idx, 3] = kurtosis_val


X = statistics
n_samples = X.shape[0]
X_flattened = X.reshape(n_samples, -1)

#Running the model
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_flattened.T)
lcd.clear()
lcd.text("Running the",1)
lcd.text("model",2)
model_path = 'model.joblib'
model = joblib.load(model_path)
predictions = model.predict(X_flattened)
output = predictions[0]

#Output Visualization
lcd.clear()
lcd.text("Imagined Word is",1)
    
if output == 1:
    print('Predicted word is "Hello"')
    send_command(1)
    lcd.text("Hello",2)
    hello.play()
elif output == 3:
    send_command(3)
    print('Predicted word is "Stop"')
    lcd.text("Stop", 2)
    stop.play()

elif output == 4:
    send_command(2)
    print('Predicted word is "Thank You"')
    lcd.text("Thank You", 2)
    tq.play()
