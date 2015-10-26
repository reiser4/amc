import time
from display import Display
from gfx import Gfx


def getFileContent(filename):
	txt = open(filename)
	return txt.read()

gfx = Gfx()
display = Display("dummy")
tstart = time.time()

mygfx = Gfx()

band = getFileContent("/tmp/band.txt")
mygfx.writeText(20,0,"BANDA: " + band)
relay = getFileContent("/tmp/relay.txt")
mygfx.writeText(5,30,"RELAY: " + relay)

data = mygfx.getData()
print data
for i in range(0,160*80):
	y = i / 160
	x = i % 160
	if data[i] == "1":
		display.setPixel(y,x,True)

display.writePng()

print "Tempo impiegato:", time.time() - tstart, "secondi"
