import serial
from time import sleep
import json
import sys
import os
sys.path.insert(0, '../common')
from atomicwrite import AtomicWrite

if not os.path.isfile('/tmp/band.txt'):
    print "File presetB non trovato..."
    AtomicWrite.writeFile('/tmp/band.txt', "40")

if not os.path.isfile('/tmp/presetA.txt'):
    print "File presetB non trovato..."
    AtomicWrite.writeFile('/tmp/presetA.txt', "0000000000000000")

if not os.path.isfile('/tmp/presetB.txt'):
    print "File presetB non trovato..."
    AtomicWrite.writeFile('/tmp/presetB.txt', "0000000000000000")
if not os.path.isfile('/tmp/presetTXTA.txt'):
    print "File presetTXTB non trovato..."
    AtomicWrite.writeFile('/tmp/presetTXTA.txt', ";")

if not os.path.isfile('/tmp/presetTXTB.txt'):
    print "File presetTXTB non trovato..."
    AtomicWrite.writeFile('/tmp/presetTXTB.txt', ";")
if not os.path.isfile('/tmp/relay.txt'):
    print "File presetTXTB non trovato..."
    AtomicWrite.writeFile('/tmp/relay.txt', "000000000000000000000000")


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
    #print "Leggo i preset"
    preset = getFileContent("/tmp/preset"+radio+".txt")
    #print "Letto:",preset
    return preset

def getPname(radio):
    #print "Leggo i pname"
    pname = getFileContent("/tmp/presetTXT"+radio+".txt")
    #print "Letto:",pname
    return pname

def getBand():
    #print "Leggo la banda"
    band = getFileContent("/tmp/band.txt")
    #print "Letto:",band
    return band

def getRelay():
    #print "Leggo i relay"
    relay = getFileContent("/tmp/relay.txt")
    #print "Letto:",relay
    return relay

def serWrite(T,C):
    stringa = T + ":" + C + "\n"
    ser.write(stringa)
    #print "Mando stringa",stringa
    with open("/tmp/ser-out.txt", "a") as myfile:
        myfile.write(stringa)

def getTx(R):
    #print "Leggo trasmissione per radio",R
    txs = getFileContent("/tmp/tx.txt")
    #print "Letto:",txs
    if txs == R:
        return "1"
    else:
        return "0"
    #print "Letto:",txs
    #return txs

print "Apro porta seriale"
ser = serial.Serial("/dev/ttyGS0",115200)
print "Aperta porta", ser.name

while True:
    waiting = ser.inWaiting()
    if waiting > 0:
        print "Dati in arrivo!"
        data = ser.read(waiting)
        print "Dati ricevuti:",data
        if data == "SENDCFG":
            mycfg = getFileContent("/root/amc/config.json").replace("\n","") + "\n"
            ser.write("CFGJSON:"+mycfg)
        else:
            jsondec = json.loads(data)
            print "Decodifica JSON:",jsondec
            AtomicWrite.writeFile('/root/amc/config.json', data)
            ser.write("CFGACK\n")

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

    sleep(0.3)
    print "."

ser.close()
