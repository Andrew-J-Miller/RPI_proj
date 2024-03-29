import Rpi.GPIO as GPIO
from pygame import mixer
import time
import sys
import tkinter as tk
from tkinter import ttk

#libraries for thermocouple ADC and GPIO SPI
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855

#BoilScript.py
#This is the script that will be run during the boil step. Essentially identical to heating template script

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



























alarm = songPlayer('Alarm.mp3')







#Define a function to convert Celsius to Fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0



#Function for reading the thermocouple temperature
def readTemp():
		temp = sensor.readTempC()
		internal = sensor.readInternalC()
		return temp


		
		
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
		
		
		
		
		
	
# Raspberry Pi hardware SPI configuration.
SPI_PORT   = 0
SPI_DEVICE = 0
sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))



#Setting up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)


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

#p is the pin that uses pwm to control the relay. Currently set to GPIO 18 at 100 Hz
p = GPIO.PWM(18, 100)

#A variable for the current temperature
curTemp = 0

#A variable for the previous temperature
prevTemp = 0

#A variable for the current duty cycle. Starts at 100
DC = 100

#starts p with 100% duty cycle
p.start(DC)

#A counter that will determine when the heating is complete
counter = 0


#This will be the main loop for heating the water. Will break out after a designated amount of time has passed with the read temp being within some percent of the dest temp
while True:
	if isF == FALSE:
		curTemp = readTemp()
	else
		curTemp = c_to_f(readTemp())
	
	
	#less & decreasing
	#Increment duty cycle if current temperature is less than destination and the temperature is decreasing
	if curTemp < destTemp and DC < 100 and curTemp < prevTemp:
		DC += 1
	
	#less and increasing
	#Decrement duty cycle if the current temp is over or within 2 degrees and still increasing	
	else if curTemp < destTemp and DC > 0 and curTemp > prevTemp:
		DC -= 1
	
	#greater and increasing
	#Overshot destTemp need to dial back duty cycle
	else if curTemp > destTemp and DC > 0 and curTemp > prevTemp:
		DC -= 1
	
	#greater and decreasing
	#As the temp approaches the destination, the DC needs to be dialed back to stabilize
	else if curTemp > destTemp and DC < 100 and prevTemp > curTemp:
		DC += 1
	
	#If the current temp is not within 1 degree of the target, reset the counter
	if abs(curTemp - desTemp > 1):
		counter = 0
	else:
		counter += 1

	#This counter number may need to be adjusted with some tests. We need to make sure the temperature is actually stabilized
	#Will currently alert 
	if (counter == 60):
		cur.fullUnload()
		cur = alarm
		cur.fullLoad()
		cur.playSong()
		popupmsg("Destination temperature reached")
		#play alarm for 10 seconds
		time.sleep(10)
		#stop alarm
		cur.fullUnload()
	
	
	printf(curTemp)
	
	#change duty cycle every loop to the new value if applicable
	p.ChangeDutyCycle(DC)
	
	#Wait oner second, current temp becomes new previous temp
	time.sleep(1)
	prevTemp = curTemp














#At the end, all GPIO pins must be cleaned and unassigned
GPIO.cleanup()
