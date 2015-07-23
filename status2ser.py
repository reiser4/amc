
import serial
from time import sleep

'''

PER USARE LA PORTA gadget:

root@beaglebone:/etc# systemctl disable "serial-getty@ttyGS0.service"


FORMATO:

	APRESET:0001000100010001 (sequenza lunga 16)
	BPRESET:0001000100010001
	APNAME:Africa,Europa,America;Europa (direzioni rx;direzioni tx)
	BPNAME:  "  "  "  "
	BAND:40
	RELAY:100000 (sequenza lunga 24)

'''

def getFileContent(filename):
	txt = open(filename)
	return txt.read()

def getPreset(radio):
	print "Leggo i preset"
        preset = getFileContent("/tmp/radio"+radio+".txt")
        print "Letto:",preset
        return preset

def getPname(radio):
        print "Leggo i pname"
        pname = getFileContent("/tmp/"+radio+"pname.txt")
        print "Letto:",pname
        return pname

def getBand():
	print "Leggo la banda"
	band = getFileContent("/tmp/band.txt")
	print "Letto:",band
	return band

def getRelay():
	print "Leggo i relay"
	relay = getFileContent("/tmp/relay.txt")
	print "Letto:",relay
	return relay

def serWrite(T,C):
	stringa = T + ":" + C + "\n"
	ser.write(stringa)
	with open("/tmp/ser-out.txt", "a") as myfile:
		myfile.write(stringa)

def getTx(R):
	print "Leggo trasmissione per radio",R
	txs = getFileContent("/tmp/tx"+R+".txt")
	print "Letto:",txs
	return txs

print "Apro porta seriale"
ser = serial.Serial("/dev/ttyGS0",115200)
print "Aperta porta", ser.name


while True:
	# leggo lo stato da temp
	APRESET = getPreset("A")
	BPRESET = getPreset("B")
	APNAME = getPname("A")
	BPNAME = getPname("B")
	BAND = getBand()
	RELAY = getRelay()
	ATX = getTx("A")
	BTX = getTx("B")

	# lo scrivo come stringa
	serWrite("APRESET",APRESET)
	serWrite("BPRESET",BPRESET)
	serWrite("APNAME",APNAME)
	serWrite("BPNAME",BPNAME)
	serWrite("BAND",BAND)
	serWrite("RELAY",RELAY)
        serWrite("ATX",ATX)
        serWrite("BTX",BTX)

	
	sleep(0.5)


ser.close()
