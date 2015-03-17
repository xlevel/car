import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

STEERLEFT = 13
STEERRIGHT = 11

DRIVEFORWARD = 18
DRIVEBACK = 16

SPEEDCONTROL = 12

#Configure Steering
GPIO.setup(STEERLEFT, GPIO.OUT)
GPIO.setup(STEERRIGHT, GPIO.OUT)

#Configure Drive Wheels
GPIO.setup(DRIVEFORWARD, GPIO.OUT)
GPIO.setup(DRIVEBACK, GPIO.OUT)

#Configure the Speed
GPIO.setup(SPEEDCONTROL, GPIO.OUT)

#Test the Steering wheels
GPIO.output(STEERLEFT, True)
time.sleep(1)

GPIO.output(STEERLEFT, False)
time.sleep(1)

GPIO.output(STEERRIGHT, True)
time.sleep(1)

GPIO.output(STEERRIGHT, False)
time.sleep(1)

#Test the drive wheels
GPIO.output(SPEEDCONTROL, True)

GPIO.output(DRIVEFORWARD, True)
time.sleep(1)

GPIO.output(DRIVEFORWARD, False)
time.sleep(1)

GPIO.output(DRIVEBACK, True)
time.sleep(1)

GPIO.output(DRIVEBACK, False)
time.sleep(1)

GPIO.output(SPEEDCONTROL, False)


#Test the drive speed
pwm = GPIO.PWM(SPEEDCONTROL, 50)
pwm.start(90)

GPIO.output(DRIVEBACK, True)
time.sleep(1)

pwm.ChangeDutyCycle(50)
time.sleep(1)

pwm.ChangeDutyCycle(25)
time.sleep(1)

pwm.ChangeDutyCycle(15)
time.sleep(1)

pwm.ChangeDutyCycle(50)
time.sleep(1)

GPIO.output(DRIVEBACK, False)
pwm.stop()


GPIO.cleanup()
