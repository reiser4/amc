
from Adafruit_I2C import Adafruit_I2C
i2c = Adafruit_I2C(0x20,1)
#print i2c.readU8(0x09)


class MCP23017:

	def __init__ (self, busid):
		print "Inizializzo MCP23017 su bus", busid
		self.busid = busid
		self.i2c = Adafruit_I2C(0x20,busid)
		self.pins = list()
		for i in range(16):
			print "Spengo pin",i
			self.pins.append(0)
		i2c.write8(0x00, 0)
		i2c.write8(0x01, 0)	

	def writePin(self, group, number, state):
		# 1 == logico alto, 0 == logico basso
		#imposto pin
		offset = 0
		if group == "B":
			offset += 8
		#print "Imposto pin n.",offset+8-number,state
		self.pins[offset+number] = state
		
	def writeData(self):
		#print "scrivo tutto",self.pins
		i2c.write8(0x12, self.listToByte(self.pins, 0))
		i2c.write8(0x13, self.listToByte(self.pins, 8))

	def listToByte(self, list, start):
		out = ""
		#print "Lista:",list
		for i in range(start, start+8):
			out = out + str(list[7-i])
		#print "Out:",out,start
		value = int(out,2)
		#print "Valore:",value
		return value
