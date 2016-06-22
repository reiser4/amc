

import sys
sys.path.insert(0, '../common')
import time
#import Adafruit_BBIO.GPIO as GPIO
from atomicwrite import AtomicWrite

pos = 0
count = 56

ledstring = "0" * (count+1)
AtomicWrite.writeFile("/tmp/leds.txt",ledstring)
time.sleep(2)

while True:
	ledstring = "0" * pos + "1" + "0" * (count-pos)
	print ledstring
	pos += 1
	if pos > count:
		pos = 0
	AtomicWrite.writeFile("/tmp/leds.txt",ledstring)
	time.sleep(0.8) 