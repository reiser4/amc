

### script relay: scrive su GPIO cio` che legge da /tmp/relay.txt


def readFile(filename):
	if os.path.isfile(path):
		in_file = open(path, "r")
		text = in_file.read()
		in_file.close()
		return text
	else:
		print "File non esistente!!!"
		return "00000000"

class ShiftRegister:

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


oldrelay = ""

sr = ShiftRegister

while True:

	newrelay = readFile("/tmp/relay.txt")[0:8]
	if newrelay != oldrelay:
		oldrelay = newrelay

		print "Relay cambiati: scrivo in hardware " + newrelay
		sr.Write(newrelay)





