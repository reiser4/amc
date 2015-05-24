import Adafruit_BBIO.GPIO as GPIO

import SocketServer
import json

def fullmsg(texts, lenghts):
   print "fullmsg!"
   print texts
   print lenghts
   MSG = ""
   for i in range(0,len(texts)):
       MSG += texts[i].ljust(lenghts[i], '\0')
   MSG = MSG.ljust(286, '\0')
   PADDED_MSG = ""
   for i in range(0,len(MSG)):
           PADDED_MSG += MSG[i] + '\0'
   return PADDED_MSG

def decodeData(text):
    print "From:" + text[0:16]
    print "To: " + text[16:32]
    print "Type: " + text[32:36]

def getMsgType(msg): #usato
    return msg[32:36]

def getStiStation(msg): #usato
    return msg[36:(36+16)]

def getStiBand(msg): #usato
    return msg[(36+16):(36+16+4)]


def getStiMode(msg): #usato
    return msg[(62):(62+3)]

def getStiFreq(msg): #usato
    return msg[(96):(96+8)]

def getStiRole(msg): #usato
    return msg[(72):(72+1)]


class MyUDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        global STNK3A
        global STNK3B
        data = self.request[0].strip()
        outmsg = ""
        for i in range(0, len(data)):
            if i % 2 == 0:
                outmsg += data[i]
        print "Outmsg: " + outmsg + " (" + str(len(outmsg)) + ")"
        packet = getMsgType(outmsg)
        if getMsgType(outmsg) == "STI\0":
            station = getStiStation(outmsg)
            band = getStiBand(outmsg)

       mode = getStiMode(outmsg)
       freq = getStiFreq(outmsg)
       role = getStiRole(outmsg)
       print "Station: [" + station + "]"
       print "Mode: [" + mode + "]"
       print "Band: [" + band + "]"
       print "Freq: [" + freq + "]"
            print "Role: [" + role + "]"

       fstation = station.rstrip('\0')
       fmode = mode.replace('\0','')
            fband = band.replace('\0','')
            ffreq = freq.replace('\0','')
            frole = role.replace('\0','')

       with open("/tmp/" + fstation + ".txt", 'w') as fp:
           json.dump({"station": fstation, "mode": fmode, "band": fband, "freq": ffreq, "role": frole}, fp)

       if fstation == "STNK3B":
                pin = RadioB[bands[fband]]
                for otherpin in RadioB:
           if otherpin != pin:
               GPIO.output(otherpin, GPIO.HIGH)
               print "Alzo ",otherpin
       GPIO.output(pin, GPIO.LOW)
       print "Abbasso ",pin

       if fstation == "STNK3A":
                pin = RadioA[bands[fband]]
                for otherpin in RadioA:
                        if otherpin != pin:
                                GPIO.output(otherpin, GPIO.HIGH)
                                print "Alzo ",otherpin
                GPIO.output(pin, GPIO.LOW)
                print "Abbasso ",pin


if __name__ == "__main__":

    #invertiti
    RadioA = ["P9_11", "P9_12", "P9_13", "P9_15", "P9_16", "P9_21"]
    RadioB = ["P9_22", "P9_23", "P9_24", "P9_26", "P9_27", "P9_30"]
    bands = {'160': 5, '80': 4, '40': 3, '20': 2, '15': 1, '10': 0}

    for pin in RadioA:
      GPIO.setup(pin, GPIO.OUT)
      GPIO.output(pin, GPIO.HIGH)

    for pin in RadioB:
      GPIO.setup(pin, GPIO.OUT)
      GPIO.output(pin, GPIO.HIGH)




    HOST, PORT = "", 9888
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    print "Avvio server..."
    server.serve_forever()
    print "Server avviato."
