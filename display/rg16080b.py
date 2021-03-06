#from mcp23017 import MCP23017
import time


import Adafruit_BBIO.GPIO as GPIO

#from bbio import *

GPIO.setup("P8_27", GPIO.OUT)
GPIO.setup("P8_28", GPIO.OUT)
GPIO.setup("P8_29", GPIO.OUT)
GPIO.setup("P8_30", GPIO.OUT)
GPIO.setup("P8_31", GPIO.OUT)
GPIO.setup("P8_32", GPIO.OUT)
GPIO.setup("P8_33", GPIO.OUT)
GPIO.setup("P8_34", GPIO.OUT)
GPIO.setup("P8_35", GPIO.OUT)
GPIO.setup("P8_36", GPIO.OUT)
GPIO.setup("P8_37", GPIO.OUT)
GPIO.setup("P8_38", GPIO.OUT)
GPIO.setup("P8_39", GPIO.OUT)

#pinMode(GPIO2_22, OUTPUT) #GPIO.setup("P8_27", GPIO.OUT)
#pinMode(GPIO2_24, OUTPUT) #GPIO.setup("P8_28", GPIO.OUT)
#pinMode(GPIO2_23, OUTPUT) #GPIO.setup("P8_29", GPIO.OUT)
#pinMode(GPIO2_25, OUTPUT) #GPIO.setup("P8_30", GPIO.OUT)
#pinMode(GPIO0_10, OUTPUT) #GPIO.setup("P8_31", GPIO.OUT)
#pinMode(GPIO0_11, OUTPUT) #GPIO.setup("P8_32", GPIO.OUT)
#pinMode(GPIO0_9, OUTPUT) #GPIO.setup("P8_33", GPIO.OUT)
#pinMode(GPIO2_17, OUTPUT) #GPIO.setup("P8_34", GPIO.OUT)
#pinMode(GPIO0_8, OUTPUT) #GPIO.setup("P8_35", GPIO.OUT)
#pinMode(GPIO2_16, OUTPUT) #GPIO.setup("P8_36", GPIO.OUT)
#pinMode(GPIO2_14, OUTPUT) #GPIO.setup("P8_37", GPIO.OUT)
#pinMode(GPIO2_15, OUTPUT) #GPIO.setup("P8_38", GPIO.OUT)
#pinMode(GPIO2_12, OUTPUT) #GPIO.setup("P8_39", GPIO.OUT)


class RG16080B:
    def __init__(self):
        print "Inizializzo rg16080b con collegamento diretto"
        #self.mcp23017 = MCP23017(1)
        #self.setReset(0)
        self.setCS(0)
        #self.setReset(1)
        self.reset()

        print "Imposto modo 1 1 0 0 1 0"
        #self.setMode(1,1,0,0,1,0)
	self.setMode(1,1,0,1,0,0)

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

        self.oldsequence = [0] * (160*80)

    def writePixels(self, sequence):
        #print "Sequenza:",sequence
        #print "Len:",len(sequence)
        self.setCursorLower(0,0,0,0,0,0,0,0)
        self.setCursorUpper(0,0,0,0,0,0,0,0)
        oldsequence = self.oldsequence
        i = 0
        skipped = False

        writecount = 0

        while i < len(sequence):
            ###print "s",i
            if (oldsequence[i] != sequence[i]) or (oldsequence[i+1] != sequence[i+1]) or (oldsequence[i+2] != sequence[i+2]) or (oldsequence[i+3] != sequence[i+3]) or (oldsequence[i+4] != sequence[i+4]) or (oldsequence[i+5] != sequence[i+5]) or (oldsequence[i+6] != sequence[i+6]) or (oldsequence[i+7] != sequence[i+7]):
                if skipped:
                    #print "avevo skippato..."
                    skipped = False
                    #writecount = i
                    ##print "Lower",writecount
                    self.setCursorLower(1 if (writecount & 0b10000000) > 0 else 0, 1 if (writecount & 0b01000000) > 0 else 0, 1 if (writecount & 0b00100000) > 0 else 0, 1 if (writecount & 0b00010000) > 0 else 0,
                        1 if (writecount & 0b00001000) > 0 else 0, 1 if (writecount & 0b00000100) > 0 else 0, 1 if (writecount & 0b00000010) > 0 else 0, 1 if (writecount & 0b00000001) > 0 else 0)
                   #if (writecount > 255):
                    writecount2 = writecount / 256
                    ##print "Upper",writecount2

                    self.setCursorUpper(0,0,1 if (writecount2 & 0b00100000) > 0 else 0,1 if (writecount2 & 0b00010000) > 0 else 0,1 if (writecount2 & 0b00001000) > 0 else 0, 1 if (writecount2 & 0b00000100) > 0 else 0,
                          1 if (writecount2 & 0b00000010) > 0 else 0, 1 if (writecount2 & 0b00000001) > 0 else 0)
                #else:
                           #self.setCursorUpper(0,0,0,0,0,0,0,0)

                self.writeDisplayData(sequence[i],sequence[i+1],sequence[i+2],sequence[i+3],sequence[i+4],sequence[i+5],sequence[i+6],sequence[i+7])
            else:
                #print "Skippo"
                skipped = True
            i = i + 8
            writecount = writecount + 1

        print "scritta"
        self.oldsequence = sequence

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
        #self.mcp23017.writeData()
        self.setE(0)

    def setRW(self, state):
        #self.mcp23017.writePin("A", 1, state)
        if state == 0:
            GPIO.output("P8_28", GPIO.LOW)
            #digitalWrite(GPIO2_24, LOW)
        else:
            #digitalWrite(GPIO2_24, HIGH)
            GPIO.output("P8_28", GPIO.HIGH)

    def setRS(self, state):
        #self.mcp23017.writePin("A", 0, state)
        if state == 0:
            GPIO.output("P8_27", GPIO.LOW)
            #digitalWrite(GPIO2_22, LOW)
        else:
            GPIO.output("P8_27", GPIO.HIGH)
            #digitalWrite(GPIO2_22, HIGH)

    def setE(self, state):
        #self.mcp23017.writePin("A", 2, state)
        if state == 0:
            GPIO.output("P8_29", GPIO.LOW)
            #digitalWrite(GPIO2_23, LOW)
        else:
            #digitalWrite(GPIO2_23, HIGH)
            GPIO.output("P8_29", GPIO.HIGH)

    def setDB0(self, state):
        #self.mcp23017.writePin("B", 7, state)
        if int(state) == 0:
            GPIO.output("P8_30", GPIO.LOW)
    #               print "abbasso db0"
    #                digitalWrite(GPIO2_25, LOW)
        else:
    #                digitalWrite(GPIO2_25, HIGH)

            GPIO.output("P8_30", GPIO.HIGH)
    #               print "alzo db0"

    def setDB1(self, state):
        #self.mcp23017.writePin("B", 6, state)
        if int(state) == 0:
            GPIO.output("P8_31", GPIO.LOW)
#                        digitalWrite(GPIO0_10, LOW)
        else:
            GPIO.output("P8_31", GPIO.HIGH)
#                        digitalWrite(GPIO0_10, HIGH)

    def setDB2(self, state):
        #self.mcp23017.writePin("B", 5, state)
        if int(state) == 0:
            GPIO.output("P8_32", GPIO.LOW)
#                        digitalWrite(GPIO0_11, LOW)
        else:
#                       digitalWrite(GPIO0_11, HIGH)
            GPIO.output("P8_32", GPIO.HIGH)

    def setDB3(self, state):
        #self.mcp23017.writePin("B", 4, state)
        if int(state) == 0:
#                        digitalWrite(GPIO0_9, LOW)
            GPIO.output("P8_33", GPIO.LOW)
        else:
#                        digitalWrite(GPIO0_9, HIGH)
            GPIO.output("P8_33", GPIO.HIGH)

    def setDB4(self, state):
        #self.mcp23017.writePin("B", 3, state)
        if int(state) == 0:
            GPIO.output("P8_34", GPIO.LOW)
#                        digitalWrite(GPIO2_17, LOW)
        else:
#                        digitalWrite(GPIO2_17, HIGH)
            GPIO.output("P8_34", GPIO.HIGH)

    def setDB5(self, state):
        #self.mcp23017.writePin("B", 2, state)
        if int(state) == 0:
#                        digitalWrite(GPIO0_8, LOW)
            GPIO.output("P8_35", GPIO.LOW)
        else:
#                        digitalWrite(GPIO0_8, HIGH)
            GPIO.output("P8_35", GPIO.HIGH)

    def setDB6(self, state):
        #self.mcp23017.writePin("B", 1, state)
        if int(state) == 0:
#                        digitalWrite(GPIO2_16, LOW)
            GPIO.output("P8_36", GPIO.LOW)
        else:
#                        digitalWrite(GPIO2_16, HIGH)
            GPIO.output("P8_36", GPIO.HIGH)

    def setDB7(self, state):
        #self.mcp23017.writePin("B", 0, state)
        if int(state) == 0:
#                        digitalWrite(GPIO2_14, LOW)
            GPIO.output("P8_37", GPIO.LOW)
#                       print "basso"
        else:
#                        digitalWrite(GPIO2_14, HIGH)
            GPIO.output("P8_37", GPIO.HIGH)
#                       print "alto"

    def setCS(self, state):
        #self.mcp23017.writePin("A", 3, state)
        if state == 0:
#                        digitalWrite(GPIO2_15, LOW)
            GPIO.output("P8_38", GPIO.LOW)
        else:
#                        digitalWrite(GPIO2_15, HIGH)
            GPIO.output("P8_38", GPIO.HIGH)

    def setReset(self, state):
        #self.mcp23017.writePin("A", 4, state)
        if state == 0:
#                        digitalWrite(GPIO2_12, LOW)
            GPIO.output("P8_39", GPIO.LOW)
        else:
#                        digitalWrite(GPIO2_12, HIGH)
            GPIO.output("P8_39", GPIO.HIGH)



    def reset(self):
        self.setReset(1)
        self.setReset(0)
        #self.mcp23017.writeData()

    def setMode(self, DB5, DB4, DB3, DB2, DB1, DB0):
        self.setPins(0,1,0,0,0,0,0,0,0,0)
        self.setPins(0,0,0,0,DB5,DB4,DB3,DB2,DB1,DB0)
        #self.mcp23017.writeData()

    def setChPitch(self, DB7, DB6, DB5, DB4, DB2, DB1, DB0):
        self.setPins(0,1,0,0,0,0,0,0,0,1)
        self.setPins(0,0,DB7,DB6,DB5,DB4,0,DB2,DB1,DB0)
        #self.mcp23017.writeData()

    def setCharNumber(self, DB7, DB6, DB5, DB4, DB3, DB2, DB1, DB0):
        self.setPins(0,1,0,0,0,0,0,0,1,0)
        self.setPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0)
        #self.mcp23017.writeData()

    def setTimeDivision(self, DB7, DB6, DB5, DB4, DB3, DB2, DB1, DB0):
        self.setPins(0,1,0,0,0,0,0,0,1,1)
        self.setPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0)
        #self.mcp23017.writeData()

    def setCurPos(self, DB3, DB2, DB1, DB0):
        self.setPins(0,1,0,0,0,0,0,1,0,0)
        self.setPins(0,0,0,0,0,0,DB3,DB2,DB1,DB0)
        #self.mcp23017.writeData()

    def setStartLower(self, DB7, DB6, DB5, DB4, DB3, DB2, DB1, DB0):
        self.setPins(0,1,0,0,0,0,1,0,0,0)
        self.setPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0)
        #self.mcp23017.writeData()

    def setStartUpper(self, DB7, DB6, DB5, DB4, DB3, DB2, DB1, DB0):
        self.setPins(0,1,0,0,0,0,1,0,0,1)
        self.setPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0)
        #self.mcp23017.writeData()

    def setCursorLower(self, DB7, DB6, DB5, DB4, DB3, DB2, DB1, DB0):
        self.setPins(0,1,0,0,0,0,1,0,1,0)
        self.setPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0)
        #self.mcp23017.writeData()

    def setCursorUpper(self, DB7, DB6, DB5, DB4, DB3, DB2, DB1, DB0):
        self.setPins(0,1,0,0,0,0,1,0,1,1)
        self.setPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0)
        #self.mcp23017.writeData()

    def writeDisplayData(self, DB7, DB6, DB5, DB4, DB3, DB2, DB1, DB0):
        self.setPins(0,1,0,0,0,0,1,1,0,0)
        ### bit invertiti!
    #       print DB0
        #print DB7
        #self.setPins(0,0,DB7,DB6,DB5,DB4,DB3,DB2,DB1,DB0)
        self.setPins(0,0,DB0,DB1,DB2,DB3,DB4,DB5,DB6,DB7)
        #self.mcp23017.writeData()

    def writeBit(self, DB2, DB1, DB0):
        self.setPins(0,1,0,0,0,0,1,1,1,0)
        self.setPins(0,0,0,0,0,0,0,DB2,DB1,DB0)
        #self.mcp23017.writeData()


    def clearBit(self, DB2, DB1, DB0):
        self.setPins(0,1,0,0,0,0,1,1,1,0)
        self.setPins(0,0,0,0,0,0,0,DB2,DB1,DB0)
        #self.mcp23017.writeData()
