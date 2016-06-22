

import Adafruit_BBIO.GPIO as GPIO


import os
import sys
import time
sys.path.insert(0, '../common')
from atomicwrite import AtomicWrite


if not os.path.isfile('/sys/class/gpio/gpio67/value'):
    #print "Abilito gpio 5..."
    #os.system('./enablegpio5.sh')
    os.system('echo 67 > /sys/class/gpio/export')
    os.system('echo "in" > /sys/class/gpio/gpio67/direction') 

APIN = "P9_42" #P9_41

GPIO.setup(APIN, GPIO.IN, GPIO.PUD_UP)

#if not os.path.isfile('/sys/class/gpio/gpio77/value'):
#    #print "Abilito gpio 5..."
#    #os.system('./enablegpio5.sh')
#    os.system('echo 77 > /sys/class/gpio/export')
#    os.system('echo "in" > /sys/class/gpio/gpio77/direction') 


if not os.path.isfile('/tmp/relay.txt'):
    print "File tx non trovato..."
    AtomicWrite.writeFile('/tmp/tx.txt', '')


def getFileContent(filename):
    txt = open(filename)
    return txt.read()

# todo: far lavorare col vero GPIO

### TX A
# P8 41 42 43 7
## 74 75 72 66

### TX B
# P8 9, 10, 11, 12
##69 68 45 44


for inum in [69, 68, 45, 44, 66]:
    num = str(inum)
    if not os.path.isfile('/sys/class/gpio/gpio'+num+'/value'):
        #print "Abilito gpio 5..."
        #os.system('./enablegpio5.sh')
        os.system('echo '+num+' > /sys/class/gpio/export')
        os.system('echo "out" > /sys/class/gpio/gpio'+num+'/direction') 
    os.system('echo "0" > /sys/class/gpio/gpio'+num+'/value') 
        

def pttA(en):
    if en:
        os.system('echo "1" > /sys/class/gpio/gpio66/value')
    else:
        os.system('echo "0" > /sys/class/gpio/gpio66/value')

def pttB(en):
    if en:
        os.system('echo "1" > /sys/class/gpio/gpio44/value')
    else:
        os.system('echo "0" > /sys/class/gpio/gpio44/value')



while True:
    #time.sleep(6)
    #AtomicWrite.writeFile('/tmp/tx.txt', 'A')
    #time.sleep(2)
    txB = getFileContent("/sys/class/gpio/gpio67/value")
    ##txB = getFileContent("/sys/class/gpio/gpio67/value")

    if GPIO.input(APIN):
        txA = "1"
        print "A up"
    else:
        txA = "0"
        print "A down"

    txA = "1"

    if int(txA) == 0:
        AtomicWrite.writeFile('/tmp/tx.txt', 'A')
        pttA(True)
    else:
        pttA(False)
        if int(txB) == 0:
            AtomicWrite.writeFile('/tmp/tx.txt', 'B')
            pttB(True)
        else:
            pttB(False)
            AtomicWrite.writeFile('/tmp/tx.txt', '')

