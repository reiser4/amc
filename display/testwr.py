
from Adafruit_I2C import Adafruit_I2C
i2c = Adafruit_I2C(0x20,1)

import time

for i in range(0,256):
    print " ------ "
    i2c.write8(0x12,i)
    print "   ",i
    #time.sleep(0.1)
    rd = i2c.readU8(0x12)
    print "   ",rd
    if i != rd:
        print "Diversi!!","{0:b}".format(i),"{0:b}".format(rd)
    print "   ", "{0:b}".format(rd)
