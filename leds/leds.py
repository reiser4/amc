

### script relay: scrive su GPIO cio` che legge da /tmp/relay.txt

import os
import sys
sys.path.insert(0, '../common')
from atomicwrite import AtomicWrite


if not os.path.isfile('/sys/class/gpio/gpio51/value'):
    #print "Abilito gpio 5..."
    #os.system('./enablegpio5.sh')
    os.system('echo 51 > /sys/class/gpio/export')
    os.system('echo "out" > /sys/class/gpio/gpio51/direction') 

if not os.path.isfile('/sys/class/gpio/gpio48/value'):
    print "Abilito gpio 48..."
    os.system('echo 48 > /sys/class/gpio/export')
    os.system('echo "out" > /sys/class/gpio/gpio48/direction')

if not os.path.isfile('/sys/class/gpio/gpio50/value'):
    print "Abilito gpio 50..."
    os.system('echo 50 > /sys/class/gpio/export')
    os.system('echo "out" > /sys/class/gpio/gpio50/direction')

if not os.path.isfile('/tmp/leds.txt'):
    print "File relay non trovato..."
    AtomicWrite.writeFile('/tmp/leds.txt', '0000000000000000000000000000000000000000000000000000000000000')


def readFile(filename):
    if os.path.isfile(filename):
        in_file = open(filename, "r")
        text = in_file.read()
        in_file.close()
        return text
    else:
        print "File non esistente!!!",filename
        return "0000000000000000000000000000000000000000000000000000000000000"

class ShiftRegister:

    def writeFile(self, filename, byte):
        out_file = open(filename,"w")
        out_file.write(byte)
        out_file.close()

    def enableSER(self):
        self.writeFile("/sys/class/gpio/gpio48/value","1")

    def disableSER(self):
        self.writeFile("/sys/class/gpio/gpio48/value","0")

    def enableRCLK(self):
        self.writeFile("/sys/class/gpio/gpio51/value","1")

    def disableRCLK(self):
        self.writeFile("/sys/class/gpio/gpio51/value","0")

    def enableSRCLK(self):
        self.writeFile("/sys/class/gpio/gpio50/value","1")

    def disableSRCLK(self):
        self.writeFile("/sys/class/gpio/gpio50/value","0")

    def Write(self, bit_string):
        print "Bit string:",bit_string
        self.disableRCLK()
        for b in bit_string:
            if int(b) == 1:
                self.enableSER()
            else:
                self.disableSER()
            self.enableSRCLK()
            self.disableSRCLK()
        self.enableRCLK()


oldrelay = ""

sr = ShiftRegister()

while True:

    newrelay = readFile("/tmp/leds.txt")[0:61]
    if newrelay != oldrelay:
        oldrelay = newrelay

        print "Led cambiati: scrivo in hardware " + newrelay
        sr.Write(newrelay)





