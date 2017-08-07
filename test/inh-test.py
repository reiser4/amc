


import os
import sys
sys.path.insert(0, '../common')
from atomicwrite import AtomicWrite



if not os.path.isfile('/sys/class/gpio/gpio70/value'):
    print "Abilito gpio 70..."
    os.system('echo 70 > /sys/class/gpio/export')
    os.system('echo "out" > /sys/class/gpio/gpio70/direction')


def writeFile(filename, byte):
        out_file = open(filename,"w")
        out_file.write(byte)
        out_file.close()

writeFile("/sys/class/gpio/gpio70/value","1")




