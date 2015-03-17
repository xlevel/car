import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIGGER = 22
ECHO = 15
DISTANCEFACTOR = 17150

GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIGGER, False)
time.sleep(0.5)

GPIO.output(TRIGGER, True)
time.sleep(0.00001)
GPIO.output(TRIGGER, False)

while GPIO.input(ECHO) == 0:
	start = time.time()

while GPIO.input(ECHO) == 1:
	end = time.time()

length = end - start

distance = length * DISTANCEFACTOR

print(distance,"cm")

GPIO.cleanup()
