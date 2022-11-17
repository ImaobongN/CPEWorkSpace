#!/usr/bin/python3

#Carbon Monoxide Detection Module
#Team Power House
#Fall 2022 Semester
###################################################################################
# python script to send data string from arduino serial output to raspberry pi (no handshake)
###################################################################################

import sys
import RPi.GPIO as GPIO
import time
import datetime
import os
import serial


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
	
    day = datetime.datetime.now()

    while True:

#check for data in the input buffer. Read data if present 
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()

#create data.txt to append sensor data
		file = open('/usr/local/MRV/modules/COD/AVR/data.txt','a')
		file.write(line)           
		print(line)
		file.close()