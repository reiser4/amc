
from display import Display

display = Display("dummy")

#display.setPixel(10,10,True)
#display.writeChar(20,20,"Z")
#display.writeWord(40,40,"ZZ ZZ")
display.writeLine(10, 10, 10, "o")
display.writeLine(10, 10, 10, "v")
display.writeLine(19, 10, 10, "o")
display.writeLine(10, 19, 10, "v")
display.writeRect(40, 40, 10, 10)
display.writePng()
