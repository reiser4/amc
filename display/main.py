
from rg16080b import RG16080B
from display import Display
from gfx import Gfx

def getFileContent(filename):
        txt = open(filename)
        return txt.read()

rg16080b = RG16080B()
display = Display("dummy")
mygfx = Gfx()

while True:

	### ricavo i dati
	band = getFileContent("/tmp/band.txt")
	relay = getFileContent("/tmp/relay.txt")

	### stampo a schermo
	mygfx.writeText(20,0,"BANDA: " + band)
	mygfx.writeText(5,30,"RELAY: " + relay)



	data = mygfx.getData()
	for i in range(0,160*80):
	        y = i / 160
        	x = i % 160
        	if data[i] == "1":
                	display.setPixel(y,x,True)

	rg16080b.writePixels(pixels)
	display.writePng()
	### attendo
