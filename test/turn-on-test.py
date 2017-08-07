


import os
import sys
sys.path.insert(0, '../common')
from atomicwrite import AtomicWrite



if not os.path.isfile('/sys/class/gpio/gpio23/value'):
    print "Abilito gpio 23..."
    os.system('echo 23 > /sys/class/gpio/export')
    os.system('echo "out" > /sys/class/gpio/gpio23/direction')


def writeFile(filename, byte):
        out_file = open(filename,"w")
        out_file.write(byte)
        out_file.close()

writeFile("/sys/class/gpio/gpio23/value","1")




