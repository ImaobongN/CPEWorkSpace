!/usr/bin/python3

#Carbon Monoxide Detection Module
#Team Power House
#Fall 2022 Semester
#python script compatible with handshaking 

import sys
import RPi.GPIO as GPIO
import time
import os
import serial



##########################Function Definitions##############################
#Piped Serial Communication functions used by most module scripts written
#following conversion of MRV to Python

#using connected module as STDIN and STDOUT, read() polls the
#module continuously until an input thats not an empty string
#is forwarded to the MRV
def read():
	out = ""
	while out == "":
		out = sys.stdin.readline()
	return out.rstrip()

#printing will serially send message to module and wait for a response
#used mainly for handshaking and recieving outputs for HUD
def trade(message):
	print(message)
	return read()

#communicate expected communication technique to ModuleCommv2, then close
#Piped Serial was selected for the COD as raw data transfer is the only
#neccessity of the COD
for i, arg in enumerate(sys.argv[1:]):
	if arg == "type":
		print("piped serial")
		quit()
	else:
		print("Unexpected argument:", arg, file=sys.stderr)
		quit()

#Handshake for module recognition, standardized by ModuleCommv2
while trade("Module?") != "COD":
    pass

#after handshaking, script will poll module for a dosage
#then write to the output file for the stream script
while True:
	detect = trade("Count?")
	with open("/usr/local/MRV/out.txt","w") as f:
		f.writelines('COD: %s' %(detect))	
	time.sleep(1)