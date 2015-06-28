import time
from display import Display

tstart = time.time()

display = Display("dummy")

for i in range(2000):
    for y in range(80):
        for x in range(0, 160, 2):
            display.setPixel(y, x, True)

#display.writeChar(20,20,"Z")
#display.writeWord(40,40,"ZZ ZZ")
#display.writeLine(10, 10, 10, "o")
#display.writeLine(10, 10, 10, "v")
#display.writeLine(19, 10, 10, "o")
#display.writeLine(10, 19, 10, "v")
#display.writeRect(40, 40, 10, 10)
display.writePng()

print "Tempo impiegato:", time.time() - tstart, "secondi"
