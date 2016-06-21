import time


import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_27", GPIO.OUT)
GPIO.setup("P8_28", GPIO.OUT)
GPIO.setup("P8_29", GPIO.OUT)
GPIO.setup("P8_30", GPIO.OUT)
GPIO.setup("P8_31", GPIO.OUT)
GPIO.setup("P8_32", GPIO.OUT)
GPIO.setup("P8_33", GPIO.OUT)
GPIO.setup("P8_34", GPIO.OUT)
GPIO.setup("P8_35", GPIO.OUT)
GPIO.setup("P8_36", GPIO.OUT)
GPIO.setup("P8_37", GPIO.OUT)
GPIO.setup("P8_38", GPIO.OUT)
GPIO.setup("P8_39", GPIO.OUT)





print "abbasso"

GPIO.output("P8_27", GPIO.LOW)
GPIO.output("P8_28", GPIO.LOW)
GPIO.output("P8_29", GPIO.LOW)
GPIO.output("P8_30", GPIO.LOW)
GPIO.output("P8_31", GPIO.LOW)
GPIO.output("P8_32", GPIO.LOW)
GPIO.output("P8_33", GPIO.LOW)
GPIO.output("P8_34", GPIO.LOW)
GPIO.output("P8_35", GPIO.LOW)
GPIO.output("P8_36", GPIO.LOW)
GPIO.output("P8_37", GPIO.LOW)
GPIO.output("P8_38", GPIO.LOW)
GPIO.output("P8_39", GPIO.LOW)


time.sleep(30)
print "alzo"

GPIO.output("P8_27", GPIO.HIGH)
GPIO.output("P8_28", GPIO.HIGH)
GPIO.output("P8_29", GPIO.HIGH)
GPIO.output("P8_30", GPIO.HIGH)
GPIO.output("P8_31", GPIO.HIGH)
GPIO.output("P8_32", GPIO.HIGH)
GPIO.output("P8_33", GPIO.HIGH)
GPIO.output("P8_34", GPIO.HIGH)
GPIO.output("P8_35", GPIO.HIGH)
GPIO.output("P8_36", GPIO.HIGH)
GPIO.output("P8_37", GPIO.HIGH)
GPIO.output("P8_38", GPIO.HIGH)
GPIO.output("P8_39", GPIO.HIGH)


time.sleep(60)
print "fine"
