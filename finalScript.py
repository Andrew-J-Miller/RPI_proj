import Rpi.GPIO as GPIO
import time

#libraries for thermocouple ADC and GPIO SPI
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855








#Define a function to convert Celsius to Fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0



#Function for reading the thermocouple temperature
def readTemp():
		temp = sensor.readTempC()
		internal = sensor.readInternalC()
		return temp

#A function that will be called to continuously check if the timer is up		
def timerCheck(st):
		
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

#A variable for the current duty cycle. Starts at 100
DC = 100

#starts p with 100% duty cycle
p.start(DC)


start = time.time()

#This will be the main loop for heating the water. Will break out after a designated amount of time has passed with the read temp being within some percent of the dest temp
while True:
	if isF == FALSE:
		curTemp = readTemp()
	else
		curTemp = c_to_f(readTemp())
	
	
	timerCheck(start)
	
	#Increment duty cycle if not within 10 degrees of target and Duty cycle is not maximum
	if destTemp - curTemp > 10 and DC < 100:
		DC++
		














#At the end, all GPIO pins must be cleaned and unassigned
GPIO.cleanup()