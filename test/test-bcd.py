
pinA = "P9_27"
pinB = "P9_28"
pinC = "P9_29"
pinD = "P9_30"

import time

import Adafruit_BBIO.GPIO as GPIO
GPIO.setup(pinA, GPIO.OUT)
GPIO.setup(pinB, GPIO.OUT)
GPIO.setup(pinC, GPIO.OUT)
GPIO.setup(pinD, GPIO.OUT)


for i in [0, 1]:
	print i
	GPIO.output(pinA, i)
	GPIO.output(pinB, i)
	GPIO.output(pinC, i)
	GPIO.output(pinD, i)
	time.sleep(5)


