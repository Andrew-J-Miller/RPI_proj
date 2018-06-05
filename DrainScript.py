import RPi.GPIO as GPIO
import time
import sys
import os
import tkinter as tk
from tkinter import ttk
import datetime

#libraries for thermocouple ADC and GPIO SPI
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855



#Definition for child process that will run to display current temperature
def child(msg):
    popup = tk.Tk()


    def leavemini():
        popup.destroy()


    popup.wm_title("Running Boil")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1=ttk.Button(popup, text="Stop", command = leavemini)
    B1.pack()


    popup.mainloop()

	
# Raspberry Pi hardware SPI configuration.
SPI_PORT   = 0
SPI_DEVICE = 0
sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

GPIO.setmode(GPIO.BCM)

#pin for activating pump relay currently set to 17 but may need to be changed later
GPIO.setup(19, GPIO.OUT)
#pin for activating solenoid valve
GPIO.setup(25, GPIO.OUT)

newpid = os.fork()
if newpid == 0:
    child("Draining wort")
    GPIO.cleanup()
    os.system("pkill -f MashScript.py")
    sys.exit()





while True:
	#write solenoid valve to high
	GPIO.output(25, GPIO.HIGH)
	#write the pump relay pin to high to activate the pump
	GPIO.output(26, GPIO.HIGH)
		
