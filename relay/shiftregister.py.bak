
import time,os


def writeFile(filename, byte):
	out_file = open(filename,"w")
	out_file.write(byte)
	out_file.close()

def enableSER():
	writeFile("/sys/class/gpio/gpio2/value","1")

def disableSER():
	writeFile("/sys/class/gpio/gpio2/value","0")
	
def enableRCLK():
        writeFile("/sys/class/gpio/gpio49/value","1")

def disableRCLK():
        writeFile("/sys/class/gpio/gpio49/value","0")

def enableSRCLK():
        writeFile("/sys/class/gpio/gpio3/value","1")

def disableSRCLK():
        writeFile("/sys/class/gpio/gpio3/value","0")

	


def Wait():
    time.sleep(0.1)
    return

class ShiftRegister:
    
    def Write(self,bit_string):
        print "Stringa: ", bit_string
        
        for b in bit_string:
            if int(b) == 1:
                print "Alzo"
                enableSER()
            else:
                print "Abbasso"
                disableSER()
            enableSRCLK()
            disableSRCLK()
        print "Latch!"
        enableRCLK()
        disableRCLK()



sr = ShiftRegister()


os.system('echo 49 > /sys/class/gpio/export')
os.system('echo 2 > /sys/class/gpio/export')
os.system('echo 3 > /sys/class/gpio/export')

os.system('echo "out" > /sys/class/gpio/gpio2/direction') 
os.system('echo "out" > /sys/class/gpio/gpio3/direction') 
os.system('echo "out" > /sys/class/gpio/gpio49/direction') 

sr.Write("100000000000000000000001")
Wait()
sr.Write("010000000000000000000000")
Wait()
sr.Write("001000000000000000000010")
Wait()
sr.Write("000100000000000000000000")
Wait()
sr.Write("000010000000000000000100")
Wait()
sr.Write("000001000000000000000000")
Wait()
sr.Write("000000100000000000000000")
Wait()
sr.Write("000000010000000000000000")
Wait()
sr.Write("000000001000000000000000")
Wait()
sr.Write("000000000100000000000000")
Wait()
sr.Write("000000000010000000000000")
Wait()
sr.Write("000000000001000000000000")
Wait()
sr.Write("000000000000100000000000")
Wait()
sr.Write("000000000000010000000000")
Wait()
sr.Write("000000000000001000000000")
Wait()
sr.Write("000000000000000100000000")
Wait()
sr.Write("000000000000000010000000")
Wait()
sr.Write("000000000000000001000000")
Wait()
sr.Write("000000000000000000100000")
Wait()
sr.Write("000000000000000000010000")
Wait()
sr.Write("000000000000000000001000")
Wait()
sr.Write("000000000000000000000100")
Wait()
sr.Write("000000000000000000000010")
Wait()
sr.Write("000000000000000000000001")
Wait()
sr.Write("000000000000000000000000")
Wait()
sr.Write("111111111111111111111111")
