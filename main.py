# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as stat
import time
from scipy.fft import fft, fftfreq

window_size = 50000

data_i = ['value1','value2','value3','value4','value5','value6','value7','value8']

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.



def read_data():
    data = pd.read_csv('E:\LOG.CSV', sep=';')
    data['timestamp'] = pd.to_datetime(data['timestamp'], format='%H-%M-%S-%f')
    data.set_index('timestamp', inplace=True)
    return data

def offset_data(data):
    for i, value_i in enumerate(data_i, start=1):
        offset = stat.mean(data[value_i])
        data[value_i] = data[value_i] - offset

def scale_data(data):
    for i, value_i in enumerate(data_i, start=1):
        data[value_i] = data[value_i] * (4500 / 16777216)
def plot_data(timestamp, data, plotName):
    fig_data = plt.figure(figsize=(20, 12))
    ax = fig_data.add_subplot(1, 1, 1)  # hier größe festlegen
    ax.plot(timestamp, data)
    ax.set_title(plotName)
    ax.set_xlabel('Time')
    ax.set_ylabel('EMG')
    fig_data.show()

def plot_all_data( data):
    fig_data = plt.figure()


    for i, value_i in enumerate(data_i, start=1):
        ax = fig_data.add_subplot(8, 1, i)
        ax.plot(data.index, data[value_i])

        ax.set_xlabel('Time')
        ax.set_ylabel('Channel ' + str(i))

    fig_data.show()

def plot_rms(timestamp, data):
    s = data ** 2
    ms = s.rolling(window=window_size).mean()
    rms = ms ** 0.5

    fig_rms = plt.figure(figsize=(20, 12))
    ax = fig_rms.add_subplot(1, 1, 1)  # hier größe festlegen

    ax.plot(timestamp, rms, 'b' )
    ax.set_title('RMS')
    ax.set_xlabel('Time')
    ax.set_ylabel('RMS')
    fig_rms.show()

def plot_mean_freq(data,fs):
    global mean_freq
    mean_freq_arr = []
    for i in range(len(data['value']) - 50):
        spec = np.abs(np.fft.rfft(data['value'][i:(i+49)]))
        freq = np.fft.rfftfreq(len(data['value'][i:(i+49)]), d=1 / fs)
        amp = spec / spec.sum()
        mean_freq = (freq * amp).sum()
        mean_freq_arr.append(mean_freq)

    for i in range(50):
        mean_freq_arr.append(0)

    data['mean_freq'] = mean_freq_arr
    fig_mean_freq = plt.figure(figsize=(20, 12))
    ax = fig_mean_freq.add_subplot(1, 1, 1)  # hier größe festlegen
    ax.plot(data.index, data['mean_freq'])
    ax.set_title('Mean Frequency')
    ax.set_xlabel('Time')
    ax.set_ylabel('Mean Freq')
    fig_mean_freq.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    data = read_data()
    offset_data(data)
    scale_data(data)
    plot_data(data.index, data['value1'], 'EMG Channel 1')
    plot_data(data.index, data['value2'], 'EMG Channel 2')
    plot_data(data.index, data['value3'], 'EMG Channel 3')
    plot_data(data.index, data['value4'], 'EMG Channel 4')
    plot_data(data.index, data['value5'], 'EMG Channel 5')
    plot_data(data.index, data['value6'], 'EMG Channel 6')
    plot_data(data.index, data['value7'], 'EMG Channel 7')
    plot_data(data.index, data['value8'], 'EMG Channel 8')
    plot_all_data( data)
    plot_rms(data.index, data['value1'])
    #plot_mean_freq(data, 1000)
    plt.show()
