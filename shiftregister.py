
import time


def writeFile(filename, byte):
	out_file = open(filename,"w")
	out_file.write(byte)
	out_file.close()

def enableSER():
	writeFile("/sys/class/gpio/gpio3/value","1")

def disableSER():
	writeFile("/sys/class/gpio/gpio3/value","0")
	
def enableRCLK():
        writeFile("/sys/class/gpio/gpio5/value","1")

def disableRCLK():
        writeFile("/sys/class/gpio/gpio5/value","0")

def enableSRCLK():
        writeFile("/sys/class/gpio/gpio2/value","1")

def disableSRCLK():
        writeFile("/sys/class/gpio/gpio2/value","0")

	


def Wait():
	#time.sleep(0.05)
	return

class ShiftRegister:
    
    def Write(self,bit_string):
        disableRCLK()
        for b in bit_string:
            if int(b) == 1:
		enableSER()
            else:
		disableSER()
	    enableSRCLK()
	    disableSRCLK()

	enableRCLK()



sr = ShiftRegister()

sr.Write("10000000")
Wait()
sr.Write("01000000")
Wait()
sr.Write("00100000")
Wait()
sr.Write("00010000")
Wait()
sr.Write("00001000")
Wait()
sr.Write("00000100")
Wait()
sr.Write("00000010")
Wait()
sr.Write("00000001")
Wait()

sr.Write("00000000")
Wait()
sr.Write("11111111")



