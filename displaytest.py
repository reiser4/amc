
from display import Display

display = Display("dummy")

display.setPixel(10,10,True)
display.writeChar(20,20,"Z")
display.writeWord(40,40,"ZZ ZZ")
display.writePng()
