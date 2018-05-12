import Rpi.GPIO as GPIO
from pygame import mixer
import time


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


#---------USER DEFINED VARIABLES FROM THE UI ARE DECLARED HERE----------------------------------------------
#for the purposes of this script I am declaring them as preset variables but they will need to be passed in from the C# front end

#variable to keep track of whether the user entered in Fahrenheit
isF = FALSE

#The desired temperature entered by the user
destTemp = 100

#A timer passed in by the user (minutes)
timer = 60

#--------------------------------------------------------------------------------------------------------------------------------





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
	#As the temp approaches the destination, the DC needs to be dialled back to stabilize
	else if curTemp > destTemp and DC < 100 and prevTemp > curTemp:
		DC += 1
	
	#If the current temp is not within 1 degree of the target, reset the counter
	if abs(curTemp - desTemp > 1):
		counter = 0
	else:
		counter++

	#This counter number may need to be adjusted with some tests. We need to make sure the temperature is actually stabilized
	#Will currently alert 
	if (counter == 60):
		# C# pop-up that notifies the user that the target temperature has been reached.
		cur.fullUnload()
		cur = alarm
		cur.fullLoad()
		cur.playSong()
		#play alarm for 10 seconds
		time.sleep(10)
		#stop alarm
		cur.fullUnload()
		
	
	#change duty cycle every loop to the new value if applicable
	p.ChangeDutyCycle(DC)
	
	#Wait oner second, current temp becomes new previous temp
	time.sleep(1)
	prevTemp = curTemp














#At the end, all GPIO pins must be cleaned and unassigned
GPIO.cleanup()
