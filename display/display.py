
from rg16080b import RG16080B
#from display import Display
from gfx import Gfx
from time import sleep

import sys
import os
sys.path.insert(0, '../common')
from atomicwrite import AtomicWrite

if not os.path.isfile('/tmp/band.txt'):
	print "File banda non trovato..."
	AtomicWrite.writeFile('/tmp/band.txt', "40")

if not os.path.isfile('/tmp/relay.txt'):
	print "File relay non trovato..."
	AtomicWrite.writeFile('/tmp/relay.txt', '0000000000000000000000000')


def getFileContent(filename):
        txt = open(filename)
        return txt.read()

rg16080b = RG16080B()
#display = Display("dummy")
mygfx = Gfx()

while True:

	mygfx.clear()

	### ricavo i dati
	band = getFileContent("/tmp/band.txt")
	relay = getFileContent("/tmp/relay.txt")
	presetA = getFileContent("/tmp/presetA.txt")

	### stampo a schermo
	mygfx.writeText(5,0,"BANDA: " + band)
	mygfx.writeText(5,15,"RELAY: " + relay)
	mygfx.writeText(5,30,"PRESET: " + presetA)


	data = mygfx.getData()
#	for i in range(0,160*80):
#	        y = i / 160
#        	x = i % 160
#        	if data[i] == "1":
#                	display.setPixel(y,x,True)

	rg16080b.writePixels(data)
	#display.writePng()
	### attendo
	
	sleep(0.1)
	print "Fine ciclo"
