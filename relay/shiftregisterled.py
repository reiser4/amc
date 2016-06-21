
import time


def writeFile(filename, byte):
    out_file = open(filename,"w")
    out_file.write(byte)
    out_file.close()

def enableSER():
    writeFile("/sys/class/gpio/gpio48/value","1")

def disableSER():
    writeFile("/sys/class/gpio/gpio48/value","0")
    
def enableRCLK():
        writeFile("/sys/class/gpio/gpio51/value","1")

def disableRCLK():
        writeFile("/sys/class/gpio/gpio51/value","0")

def enableSRCLK():
        writeFile("/sys/class/gpio/gpio50/value","1")

def disableSRCLK():
        writeFile("/sys/class/gpio/gpio50/value","0")

    


def Wait():
    time.sleep(0.5)
    return

class ShiftRegisterLed:
    
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
 


sr = ShiftRegisterLed()

sr.Write("10000000000000000000000000")
Wait()
sr.Write("010000000000000000000000000")
Wait()
sr.Write("001000000000000000000000000")
Wait()
sr.Write("000100000000000000000000000")
Wait()
sr.Write("000010000000000000000000000")
Wait()
sr.Write("000001000000000000000000000")
Wait()
sr.Write("000000100000000000000000000")
Wait()
sr.Write("000000010000000000000000000")
Wait()

sr.Write("00000000000000000000000000000000000000000000000000000000000000000")
sr.Write("00000000000000000000000000000000000000000000000000000000000000000")
sr.Write("00000000000000000000000000000000000000000000000000000000000000000")
sr.Write("00000000000000000000000000000000000000000000000000000000000000000")
#Wait()
#sr.Write("111111110000000000000000000")



