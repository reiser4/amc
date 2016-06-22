

from rg16080b import RG16080B
from gfx import Gfx

rg16080b = RG16080B()

mygfx = Gfx()
count = 0
while True:

	count += 1

	#mygfx.setAllWhite()

        #data = mygfx.getData()
#       for i in range(0,160*80):
#               y = i / 160
#               x = i % 160
#               if data[i] == "1":
#                       display.setPixel(y,x,True)

        mygfx.writeText(5,5,"test");

	#mygfx.writeText(5,37,str(count))

        data = mygfx.getData()

        rg16080b.writePixels(data)
        #display.writePng()
        ### attendo

        print "Fine ciclo"


