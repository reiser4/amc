

### script relay: scrive su GPIO cio` che legge da /tmp/relay.txt

import os
import sys
sys.path.insert(0, '../common')
from atomicwrite import AtomicWrite


if not os.path.isfile('/sys/class/gpio/gpio49/value'):
    #print "Abilito gpio 5..."
    #os.system('./enablegpio5.sh')
    os.system('echo 49 > /sys/class/gpio/export')
    os.system('echo "out" > /sys/class/gpio/gpio49/direction')

if not os.path.isfile('/sys/class/gpio/gpio3/value'):
    print "Abilito gpio 3..."
    os.system('echo 3 > /sys/class/gpio/export')
    os.system('echo "out" > /sys/class/gpio/gpio3/direction')

if not os.path.isfile('/sys/class/gpio/gpio2/value'):
    print "Abilito gpio 2..."
    os.system('echo 2 > /sys/class/gpio/export')
    os.system('echo "out" > /sys/class/gpio/gpio2/direction')

if not os.path.isfile('/tmp/relay.txt'):
    print "File relay non trovato..."
    AtomicWrite.writeFile('/tmp/relay.txt', '000000000000000000000000')


def readFile(filename):
    if os.path.isfile(filename):
        in_file = open(filename, "r")
        text = in_file.read()
        in_file.close()
        return text
    else:
        print "File non esistente!!!",filename
        return "000000000000000000000000"

class ShiftRegister:

    def writeFile(self, filename, byte):
        out_file = open(filename,"w")
        out_file.write(byte)
        out_file.close()

    def enableSER(self):
        self.writeFile("/sys/class/gpio/gpio2/value","1")

    def disableSER(self):
        self.writeFile("/sys/class/gpio/gpio2/value","0")

    def enableRCLK(self):
        self.writeFile("/sys/class/gpio/gpio49/value","1")

    def disableRCLK(self):
        self.writeFile("/sys/class/gpio/gpio49/value","0")

    def enableSRCLK(self):
        self.writeFile("/sys/class/gpio/gpio3/value","1")

    def disableSRCLK(self):
        self.writeFile("/sys/class/gpio/gpio3/value","0")

    def Write(self, bit_string):
        print "Bit string:",bit_string
        self.disableRCLK()
        for b in bit_string[::-1]:
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

    newrelay = readFile("/tmp/relay.txt")[0:24]
    if newrelay != oldrelay:
        oldrelay = newrelay

        print "Relay cambiati: scrivo in hardware " + newrelay
        sr.Write(newrelay)
