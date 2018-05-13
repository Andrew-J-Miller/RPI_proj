import Rpi.GPIO as GPIO
from pygame import mixer
import time
import sys
import tkinter as tk
from tkinter import ttk


#libraries for thermocouple ADC and GPIO SPI
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855

mixer.init()



#These two classes define functions we need to play audio files
#We will plug in a speaker to the Raspberry pi to play an alarm when the destination temperature is reached

class pinCheck:
    isLoaded = False
    isPaused = False
    
    def __init__(self, song):
        self.song = song

    def hasStarted(self):
        if self.isLoaded == False:
            return 'NULL'
        if mixer.music.get_pos() < 10000:
            return False
        else:
            return True

    def isPlaying(self):
        if self.isLoaded == False:
            return False
        else:
            return mixer.music.get_busy()
 
    def loadSong(self):
        mixer.music.load(self.song)
        self.isLoaded = True

    def playSong(self): 
        if self.isLoaded == False:
            print('Error: no song loaded')
        else:
            mixer.music.play()
        
    def musicStop(self):
        mixer.music.stop()
        mixer.quit()
        mixer.init()
        self.isLoaded = False

    def pauseSong(self):
        if self.isPlaying():
            mixer.music.pause()
            self.isPaused = True
            return True
        else:
            return False

    def unPause(self):
        if self.isPaused == True:
            mixer.music.unpause()
            self.isPaused = False
            return True
        else:
            return False

class songPlayer(pinCheck):

    def pauseResume(self):
        if self.isPaused == True:
            self.unPause()
        else:
            self.pauseSong()

    def fullLoad(self):
        if self.isLoaded == False:
            self.loadSong()

    def playSongFT(self):
        if self.hasStarted() == False:
            self.playSong()
        
    def fullUnload(self):
        self.musicStop()



























alarm = songPlayer(#Alarm filename goes here in '')



#Definition for a simple tk popup that will appear when the target temp is reached		
def popupmsg(msg):
    popup = tk.Tk()

    def leavemini():
        popup.destroy()

    popup.wm_title("Destination Temperature Reached")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1=ttk.Button(popup, text="Okay", command = leavemini)
    B1.pack()
    popup.mainloop()		





#Define a function to convert Celsius to Fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0



#Function for reading the thermocouple temperature
def readTemp():
		temp = sensor.readTempC()
		internal = sensor.readInternalC()
		return temp


		
	
# Raspberry Pi hardware SPI configuration.
SPI_PORT   = 0
SPI_DEVICE = 0
sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))



#Setting up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
#pin for activating pump relay currently set to 17 but may need to be changed later
GPIO.setup(17, GPIO.OUT)


#---------USER DEFINED VARIABLES FROM THE UI ARE DECLARED HERE----------------------------------------------
#after some searching, the way python reads variables from C# is with sys.argv[]
#in this program, I am assuming sys.argv[1] is the destination temperature and sys.argv[2] is a boolean for isF
#In the C# front end, make sure to order the argv[] variables in the same way when you call the function

#variable to keep track of whether the user entered in Fahrenheit
isF = sys.argv[2]

#The desired temperature entered by the user
destTemp = sys.argv[1]


#--------------------------------------------------------------------------------------------------------------------------------


NORM_FONT = ("Helvetica", 10)



#A variable for the current temperature
curTemp = 0

#write the pump relay pin to high to activate the pump
GPIO.output(17, GPIO.HIGH)




#This will be the main loop for cooling the water. Will play an alarm and break out of the loop when it reaches destination cooling temperature
while True:
	if isF == FALSE:
		curTemp = readTemp()
	else
		curTemp = c_to_f(readTemp())
	
	if curTemp <= destTemp:
		# C# pop-up that notifies the user that the target temperature has been reached.
		cur.fullUnload()
		cur = alarm
		cur.fullLoad()
		cur.playSong()
		popupmsg("Destination temperature reached")
		#play alarm for 10 seconds
		time.sleep(10)
		#stop alarm
		cur.fullUnload()
		break
	
	
	
	
	#Wait one second, current temp becomes new previous temp
	time.sleep(1)
	prevTemp = curTemp



#Turn off pump relay
GPIO.output(17, GPIO.LOW)









#At the end, all GPIO pins must be cleaned and unassigned
GPIO.cleanup()
