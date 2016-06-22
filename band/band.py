
import time
import os
import sys

sys.path.insert(0, '../common')

from atomicwrite import AtomicWrite

bandarray = ["160", "80", "40", "20", "15", "10"]

band = "40"




def getFileContent(filename):
        txt = open(filename)
        return txt.read()

upFile = "/sys/devices/ocp.3/helper.12/AIN2"
downFile = "/sys/devices/ocp.3/helper.12/AIN3"



if not os.path.isfile(upFile):
    os.system("echo cape-bone-iio > /sys/devices/bone_capemgr.9/slots")
    print "AIN abilitati"

AtomicWrite.writeFile('/tmp/band.txt', band)

while True:

    upValue = getFileContent(upFile)

    if int(upValue) < 10:
        time.sleep(0.05)
        upValue = getFileContent(upFile)
        if int(upValue) < 10:
            index = bandarray.index(band)
            index = index + 1
            if index >= len(bandarray):
                index = 0
            band = bandarray[index]
            print "Banda cambiata!", band
            AtomicWrite.writeFile('/tmp/band.txt', band)
            while int(upValue) < 10:
                time.sleep(0.1)
                upValue = getFileContent(upFile)

    downValue = getFileContent(downFile)

    if int(downValue) < 10:
        time.sleep(0.05)
        downValue = getFileContent(downFile)
        if int(downValue) < 10:
            index = bandarray.index(band)
            index = index - 1
            if index < 0:
                index = len(bandarray) -1
            band = bandarray[index]
            print "Banda cambiata!", band
            AtomicWrite.writeFile('/tmp/band.txt', band)
            while int(downValue) < 10:
                time.sleep(0.1)
                downValue = getFileContent(downFile)

    #print a0Value, a1Value
    #time.sleep(1)