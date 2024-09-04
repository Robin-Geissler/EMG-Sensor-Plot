# EMG Evaluation Plot

This is a script for visualization of EMG data after a mesurement. It is to be used together with this multichannel EMG sensor: [Multichannel EMG Sensor](./../../../../emg-sensor_board)  

This script visualizes 8 channels simultaneously, and can easily be extended to more channels.
![Visualization](Figures/plot.PNG "Vizualisation")

## Getting Started
To run a live visualization, perform the following steps:
1. Connect an SD card with readings on it to the PC
2. Start the visualization script

## Trouble Shooting
These are known issues and solutions:
1. The script did not find the data file: The SD drive must be under connected under 'D:\' the file name must be LOG.csv. If the file location changes or you want to visualize an other file change the FILE_LOCATION variable in the script. 
2. The Data Format is incorrect: If there is already a reading saved on the SD card and the user performs another reading, the already existing LOG.csv file is not overwritten, instead the writing process is contiued, seperating both measurments with a new header line. Separate the data by hand into two different files and visualize them separately.


## License
For open source projects, say how it is licensed.

## Project status

