import time
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_14", GPIO.IN)
GPIO.setup("P8_15", GPIO.IN)
GPIO.setup("P8_16", GPIO.IN)
GPIO.setup("P8_17", GPIO.IN)


while True:

	a_a = GPIO.input("P8_14") #band2
	a_b = GPIO.input("P8_15") #band0 MANCANTE
	a_c = GPIO.input("P8_16") #band1
	a_d = GPIO.input("P8_17") #band3

	print a_d, a_a, a_c, a_b

	if a_d == 0 and a_a == 0 and a_c == 0 and a_b == 1:
		print "160 mt"
        if a_d == 0 and a_a == 0 and a_c == 1 and a_b == 0:
                print "80 mt"
        if a_d == 0 and a_a == 0 and a_c == 0 and a_b == 0:
                print "60 mt"
        if a_d == 0 and a_a == 0 and a_c == 1 and a_b == 1:
                print "40 mt"
        if a_d == 0 and a_a == 1 and a_c == 0 and a_b == 0:
                print "30 mt"
        if a_d == 0 and a_a == 1 and a_c == 0 and a_b == 1:
                print "20 mt"
        if a_d == 0 and a_a == 1 and a_c == 1 and a_b == 0:
                print "17 mt"
        if a_d == 0 and a_a == 1 and a_c == 1 and a_b == 1:
                print "15 mt"
        if a_d == 1 and a_a == 0 and a_c == 0 and a_b == 0:
                print "12 mt"
        if a_d == 1 and a_a == 0 and a_c == 0 and a_b == 1:
                print "10 mt"
        if a_d == 1 and a_a == 0 and a_c == 1 and a_b == 0:
                print "6 mt"


	time.sleep(1)
