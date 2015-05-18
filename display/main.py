

#from Adafruit_I2C import Adafruit_I2C
#i2c = Adafruit_I2C(0x20,1)
#print i2c.readU8(0x09)

#test mcp23017

#from MCP23017 import MCP23017
#mcp23017 = MCP23017(1)

#mcp23017.writePin("A", 1, 1)
#mcp23017.writePin("A", 2, 1)
#mcp23017.writePin("A", 3, 1)
#mcp23017.writePin("A", 4, 1)
#mcp23017.writePin("A", 5, 1)
#mcp23017.writePin("A", 6, 1)

from rg16080b import RG16080B

pixels = list()
for i in range((180*80)/4):
	pixels.append(1)
	pixels.append(0)
        pixels.append(0)
        pixels.append(0)


rg16080b = RG16080B()
rg16080b.writePixels(pixels)
