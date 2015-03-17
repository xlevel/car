import time
import RPi.GPIO as GPIO

pins = { 'STEERLEFT': 13, 'STEERRIGHT': 11, 'DRIVEFORWARD': 18, 'DRIVEBACK': 16, 'SPEEDCONTROL': 12 }

def initialise(pins, speed):

	GPIO.setmode(GPIO.BOARD)

	#Configure Steering
	GPIO.setup(pins['STEERLEFT'], GPIO.OUT)
	GPIO.setup(pins['STEERRIGHT'], GPIO.OUT)

	#Configure Drive Wheels
	GPIO.setup(pins['DRIVEFORWARD'], GPIO.OUT)
	GPIO.setup(pins['DRIVEBACK'], GPIO.OUT)

	#Configure the Speed
	GPIO.setup(pins['SPEEDCONTROL'], GPIO.OUT)

	#Configure the speed control
	pwm = GPIO.PWM(pins['SPEEDCONTROL'], 50)
	pwm.start(speed)
	return pwm 


def cleanup(pins, pwm):
	pwm.stop();
	GPIO.cleanup()


def goForward(pwm, pins, speed):
	GPIO.output(pins['DRIVEFORWARD'], True)
	GPIO.output(pins['DRIVEBACK'], False)
	pwm.ChangeDutyCycle(speed)


def goBackward(pwm, pins, speed):
	GPIO.output(pins['DRIVEFORWARD'], False)
	GPIO.output(pins['DRIVEBACK'], True)
	pwm.ChangeDutyCycle(speed)


def stop(pwm, pins):
	GPIO.output(pins['DRIVEFORWARD'], False)
	GPIO.output(pins['DRIVEBACK'], False)


def turn(direction, length):
	GPIO.output(direction, True)
	time.sleep(length)
	GPIO.output(direction, False)


pwm = initialise(pins, 50)

goForward(pwm, pins, 50)

turn(pins['STEERLEFT'], 2)

turn(pins['STEERRIGHT'], 2)

time.sleep(1)

stop(pwm, pins)

goBackward(pwm, pins, 50)

turn(pins['STEERRIGHT'], 2)

turn(pins['STEERLEFT'], 2)

time.sleep(1)

stop(pwm, pins)

cleanup(pins, pwm)

