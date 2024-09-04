import matplotlib.pyplot as plt
import pandas as pd
import statistics as stat

FILE_LOCATION = 'D:\LOG.CSV'

# Colum names
data_i = ['value1', 'value2', 'value3', 'value4', 'value5', 'value6', 'value7', 'value8']


def read_data():
    # Read the CSV file into a DataFrame with ';' as the separator
    data = pd.read_csv(FILE_LOCATION, sep=';')

    # Convert 'timestamp' column to datetime objects using the specified format
    data['timestamp'] = pd.to_datetime(data['timestamp'], format='%H-%M-%S-%f')

    # Set the 'timestamp' column as the index of the DataFrame
    data.set_index('timestamp', inplace=True)

    return data


def offset_data(data):
    # Iterate over all channels
   for i, value_i in enumerate(data_i, start=1):
       # Calculate the mean of the current column
        offset = stat.mean(data[value_i])
       # Offset the measurement data
        data[value_i] = data[value_i] - offset


def scale_data(data):
    # Iterate over all channels
    for i, value_i in enumerate(data_i, start=1):
        # Scale the values with a factor of: V_ADC / 2^24 bit / A
        data[value_i] = data[value_i] * (9000 / 16777216 / 24)


def plot_data(timestamp, data, plotName):
    # Create a new figure
    fig_data = plt.figure(figsize=(20, 12))
    # Add a single subplot to the figure
    ax = fig_data.add_subplot(1, 1, 1)
    # Plot the data against timestamps
    ax.plot(timestamp, data)
    # Set the title of the plot
    ax.set_title(plotName)
    # Label the x-axis
    ax.set_xlabel('Time')
    # Label the y-axis
    ax.set_ylabel('EMG')
    # Set the limits for the y-axis
    ax.set_ylim(-10.3, 10.3)
    # Display the plot
    fig_data.show()


def plot_all_data(data):
    # Create a new figure
    fig_data = plt.figure()

    # Iterate over all channels
    for i, value_i in enumerate(data_i, start=1):
        # Add a subplot to the figure in an 8-row grid
        ax = fig_data.add_subplot(8, 1, i)
        # Plot channel data
        ax.plot(data.index, data[value_i])
        # Label the x-axis
        ax.set_xlabel('Time')
        # Label the y-axis with the channel number
        ax.set_ylabel('Channel ' + str(i))
        # Set the y-axis limits
        ax.set_ylim(-10.3, 10.3)

    # Align subplot labels
    fig_data.align_labels()
    # Display the figure with all subplots
    fig_data.show()










"""" main function plots measurement data for 8 EMG channels"""
if __name__ == '__main__':
    # Read and preprocess data from CSV
    data = read_data()
    # Offset the data
    offset_data(data)
    # Scale the data
    scale_data(data)

    # Plot EMG channels in individual figures
    plot_data(data.index, data['value1'], 'EMG Channel 1')
    plot_data(data.index, data['value2'], 'EMG Channel 2')
    plot_data(data.index, data['value3'], 'EMG Channel 3')
    plot_data(data.index, data['value4'], 'EMG Channel 4')
    plot_data(data.index, data['value5'], 'EMG Channel 5')
    plot_data(data.index, data['value6'], 'EMG Channel 6')
    plot_data(data.index, data['value7'], 'EMG Channel 7')
    plot_data(data.index, data['value8'], 'EMG Channel 8')

    # Plot all channels in a single figure
    plot_all_data(data)

    # Display all plots
    plt.show()
