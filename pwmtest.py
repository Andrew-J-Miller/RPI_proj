import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)


GPIO.setup(18, GPIO.OUT)


p = GPIO.PWM(18, 50)

p.start(5)

print("Duty cycle = 5")


time.sleep(20)



p.ChangeDutyCycle(65)

print("Duty cycle = 65")

time.sleep(20)

p.ChangeDutyCycle(100)

print("Duty cycle = 100")

time.sleep(20)

p.stop()

GPIO.cleanup()
