import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

#Configure Steering
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

#Configure Drive Wheels
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#Test the Steering wheels
GPIO.output(11, True)
time.sleep(1)

GPIO.output(11, False)
time.sleep(1)

GPIO.output(13, True)
time.sleep(1)

GPIO.output(13, False)
time.sleep(1)

#Test the drive wheels
GPIO.output(16, True)
time.sleep(1)

GPIO.output(16, False)
time.sleep(1)

GPIO.output(18, True)
time.sleep(1)

GPIO.output(18, False)
time.sleep(1)


GPIO.cleanup()
