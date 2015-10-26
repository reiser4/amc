from mcp23017 import MCP23017
import time

class RG16080B:
	def __init__(self):
		print "Inizializzo rg16080b con i2c"
		self.mcp23017 = MCP23017(1)
                self.setReset(0)		
		self.setCS(0)
		self.setReset(1)

		print "Imposto modo 1 1 0 0 1 0"
		self.setMode(1,1,0,0,1,0)
		
		print "Pitch caratteri 8"
		self.setChPitch(0,0,0,0,1,1,1)

		print "N. caratteri"
		self.setCharNumber(0,0,0,1,0,0,1,1)

		print "Time division"
		self.setTimeDivision(1,0,1,0,0,0,0,0)

		print "Cur.pos"
		self.setCurPos(0,0,0,0)

		print "Lower e upper"
		self.setStartLower(0,0,0,0,0,0,0,0)
		self.setStartUpper(0,0,0,0,0,0,0,0)

		print "Cursor"
		self.setCursorLower(0,0,0,0,0,0,0,0)
                self.setCursorUpper(0,0,0,0,0,0,0,0)

		#print "Display data"
		#self.writeDisplayData(0,1,0,1,0,1,0,1)


	def writePixels(self, sequence):
		print "Sequenza:",sequence
		print "Len:",len(sequence)
                self.setCursorLower(0,0,0,0,0,0,0,0)
                self.setCursorUpper(0,0,0,0,0,0,0,0)


		i = 0
		while i < len(sequence):	
			self.writeDisplayData(sequence[i],sequence[i+1],sequence[i+2],sequence[i+3],sequence[i+4],sequence[i+5],sequence[i+6],sequence[i+7])
			i = i + 8

	def setPins(self, rw, rs, db7, db6, db5, db4, db3, db2, db1, db0):
		self.setRW(rw)
		self.setRS(rs)
		self.setDB7(db7)
                self.setDB6(db6)
                self.setDB5(db5)
                self.setDB4(db4)
                self.setDB3(db3)
                self.setDB2(db2)
                self.setDB1(db1)
                self.setDB0(db0)
		self.setE(1)
                self.mcp23017.writeData()
		self.setE(0)

	def setRW(self, state):
		#print "RW",state
		self.mcp23017.writePin("A", 1, state)
        def setRS(self, state):
		#print "RS",state
                self.mcp23017.writePin("A", 0, state)
        def setE(self, state):
		#print "E", state
                self.mcp23017.writePin("A", 2, state)
        def setDB0(self, state):
                self.mcp23017.writePin("B", 7, state)
        def setDB1(self, state):
                self.mcp23017.writePin("B", 6, state)
        def setDB2(self, state):
                self.mcp23017.writePin("B", 5, state)
        def setDB3(self, state):
                self.mcp23017.writePin("B", 4, state)
        def setDB4(self, state):
                self.mcp23017.writePin("B", 3, state)
        def setDB5(self, state):
                self.mcp23017.writePin("B", 2, state)
        def setDB6(self, state):
                self.mcp23017.writePin("B", 1, state)
        def setDB7(self, state):
                self.mcp23017.writePin("B", 0, state)
        def setCS(self, state):
                self.mcp23017.writePin("A", 3, state)
        def setReset(self, state):
                self.mcp23017.writePin("A", 4, state)

	

	def reset(self):
		self.setReset(1)
		self.setReset(0)
		self.mcp23017.writeData()

	def setMode(self, DB5, DB4, DB3, DB2, DB1, DB0):
                self.setPins(0,1,0,0,0,0,0,0,0,0)
		self.setPins(0,0,0,0,DB5,DB4,DB3,DB2,DB1,DB0)
                self.mcp23017.writeData()

        def setChPitch(self, DB7, DB6, DB5, DB4, DB2, DB1, DB0):
                self.setPins(0,1,0,0,0,0,0,0,0,1)
                self.setPins(0,0,DB7,DB6,DB5,DB4,0,DB2,DB1,DB0)
                self.mcp23017.writeData()

        def setCharNumber(self, DB7, DB6, DB5, DB4, DB3, DB2, DB1, DB0):
                self.setPins(0,1,0,0,0,0,0,0,1,0)
                self.setPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0)
                self.mcp23017.writeData()

        def setTimeDivision(self, DB7, DB6, DB5, DB4, DB3, DB2, DB1, DB0):
                self.setPins(0,1,0,0,0,0,0,0,1,1)
                self.setPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0)
                self.mcp23017.writeData()

        def setCurPos(self, DB3, DB2, DB1, DB0):
                self.setPins(0,1,0,0,0,0,0,1,0,0)
                self.setPins(0,0,0,0,0,0,DB3,DB2,DB1,DB0)
                self.mcp23017.writeData()

        def setStartLower(self, DB7, DB6, DB5, DB4, DB3, DB2, DB1, DB0):
                self.setPins(0,1,0,0,0,0,1,0,0,0)
                self.setPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0)
                self.mcp23017.writeData()

        def setStartUpper(self, DB7, DB6, DB5, DB4, DB3, DB2, DB1, DB0):
                self.setPins(0,1,0,0,0,0,1,0,0,1)
                self.setPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0)
                self.mcp23017.writeData()

        def setCursorLower(self, DB7, DB6, DB5, DB4, DB3, DB2, DB1, DB0):
                self.setPins(0,1,0,0,0,0,1,0,1,0)
                self.setPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0)
                self.mcp23017.writeData()

        def setCursorUpper(self, DB7, DB6, DB5, DB4, DB3, DB2, DB1, DB0):
                self.setPins(0,1,0,0,0,0,1,0,1,1)
                self.setPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0)
                self.mcp23017.writeData()

        def writeDisplayData(self, DB7, DB6, DB5, DB4, DB3, DB2, DB1, DB0):
                self.setPins(0,1,0,0,0,0,1,1,0,0)
                ### bit invertiti!
		##self.setPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0)
                self.setPins(0,0,DB0,DB1,DB2,DB3,DB4,DB5,DB6,DB7)
		self.mcp23017.writeData()

        def writeBit(self, DB2, DB1, DB0):
                self.setPins(0,1,0,0,0,0,1,1,1,0)
                self.setPins(0,0,0,0,0,0,0,DB2,DB1,DB0)
                self.mcp23017.writeData()


        def clearBit(self, DB2, DB1, DB0):
                self.setPins(0,1,0,0,0,0,1,1,1,0)
                self.setPins(0,0,0,0,0,0,0,DB2,DB1,DB0)
		self.mcp23017.writeData()
