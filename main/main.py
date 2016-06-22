
import time
import json


import os
import sys
sys.path.insert(0, '../common')

#import Adafruit_BBIO.GPIO as GPIO
from atomicwrite import AtomicWrite
#from bcdin import BcdIn
#from bcdout import BcdOut
#from icomin import IcomIn
#from band import Band
from settings import Settings
#from radio import Radio
from preset import Preset
#from front import Front
from relay import Relay


if not os.path.isfile('/tmp/band.txt'):
    print "File banda non trovato..."
    AtomicWrite.writeFile('/tmp/band.txt', "40")


if not os.path.isfile('/tmp/tx.txt'):
    print "File tx non trovato..."
    AtomicWrite.writeFile('/tmp/tx.txt', "")



relay = Relay()
#front = Front()
#icomin = IcomIn("P9_33")
#band = Band(icomin)
settings = Settings()
#radioa = Radio("P9_15", "P9_29", "P8_19", "P8_7", "P8_9", "P8_11")
#radiob = Radio("P9_17", "P9_31", "P8_26", "P8_13", "P8_15", "P8_17")
preset = Preset()
#txing = ""
clear = True
lastband = "-1"
presetchanged = False
oldpresetA = ""
oldpresetB = ""
#def tx(R,S):
#       AtomicWrite.writeFile("/tmp/tx"+R+".txt",str(S))


def getFileContent(filename):
    txt = open(filename)
    return txt.read()

while True:
    ### devo leggere la banda in cui mi trovo e scriverla sull'uscita del BCD.
    ### se necessario aggiornare i rele`, led e display
    ### valutare se rallentare questa operazione

    myband = getFileContent("/tmp/band.txt")
    if myband != lastband:
    # rilevato cambio banda!
        print "Banda cambiata!!",myband
        #print configuration
        ##front.changeBand(myband)
        lastband = myband

        #print "Banda: " + str(myband)

    logic = settings.readParam("Logic")

    #print "Logica: " + logic
    presetchanged = False


    presetA = preset.readPresetFile("/tmp/presetA.txt")
    presetB = preset.readPresetFile("/tmp/presetB.txt")
    if presetA != oldpresetA:
        oldpresetA = presetA
        presetchanged = True
    if presetB != oldpresetB:
        oldpresetB = presetB
        presetchanged = True

    #print "Preset A: " + presetA
    ###print "Preset B: " + presetB

    #todo: fare solo se necessario
    with open("/root/amc/config.json", 'r') as fin:
        configuration = json.load(fin)
    ###print configuration

    ##relayband = myband
    relayband = "40" ## DEMO

    bandconfiguration = configuration['relayconfig'][str(relayband)+'m']
    ###print bandconfiguration


    AtomicWrite.writeFile("/tmp/presetTXTA.txt",preset.getPname(presetA,bandconfiguration,"A"))
    AtomicWrite.writeFile("/tmp/presetTXTB.txt",preset.getPname(presetB,bandconfiguration,"B"))


    #radioArx = "{0:b}".format(preset.readPresetFile("/tmp/radioArx.txt")).zfill(8)
    #radioAtx = "{0:b}".format(preset.readPresetFile("/tmp/radioAtx.txt")).zfill(8)
    #radioBrx = "{0:b}".format(preset.readPresetFile("/tmp/radioBrx.txt")).zfill(8)
    #radioBtx = "{0:b}".format(preset.readPresetFile("/tmp/radioBtx.txt")).zfill(8)

    #todo: solo se preset cambiati

    #front.changePreset("A","rx",radioArx)
    #front.changePreset("A","tx",radioAtx)
    #front.changePreset("B","rx",radioBrx)
    #front.changePreset("B","tx",radioBtx)

    #todo: solo se banda o preset cambiati

    #front.updateFront()

    #print "Presets: ", radioArx, radioAtx, radioBrx, radioBtx

    #settings.setPreset("A","rx",radioArx)
    #settings.setPreset("A","tx",radioAtx)
    #settings.setPreset("B","rx",radioBrx)
    #settings.setPreset("B","tx",radioBtx)


    ###pttA = radioa.readPTT()
    ###pttB = radiob.readPTT()

    txing = getFileContent("/tmp/tx.txt")
    if txing == "":
        pttA = False
        pttB = False

    else:
        if txing == "A":
            pttA = True
            pttB = False
        else:
            
            if txing == "B":
                pttB = True
                pttA = False
            else:
                print "Situazione non gestita: txing =",txing

    #print "Stato: clear: ", clear, " txing: ", txing

    if (logic == "first_one_wins"):
        ## logica in cui le due radio hanno la stessa priorita` e non possono trasmettere insieme
        if clear == True:
            #print "Nessuno trasmetteva"
            # nessuno stava trasmettendo.
            if pttA == True:
                clear = False
                txing = "A"
                # ora vuole trasmettere la radio A
                ######print "Richiesta di TX da Radio A"
                ######print "Devo inibire radio B e iniziare la procedura di TX"
                #relay.writeRelay(settings.getPreset("radioAtx"))
                relayconfig = relay.relayConfigTx(presetA, "A", bandconfiguration)
            else:
                # radio A non vuole trasmettere.
                if pttB == True:
                    clear = False
                    txing = "B"
                    # radio B vuole trasmettere
                    ######print "Richiesta di TX da Radio B"
                    ######print "Inibisco radio A e faccio procedura TX"
                    relayconfig = relay.relayConfigTx(presetB, "B", bandconfiguration)
                    #relay.writeRelay(settings.getPreset("radioBtx"))
                else:
                    ### ASCOLTO
                    #sia A che B non vogliono trasmettere: ascolto

                    relayconfig = relay.relayConfigRx(presetA, presetB, bandconfiguration)

                    #####relay.writeRelay(settings.getPreset("rx"))
        else:
            #print "Tx attiva per ", txing
            # qualcuno trasmetteva
            if txing == "A":
                #stava trasmettendo A
                if pttA == False:
                    #A ha appena finito di trasmettere
                    ######print "Procedura per ripristino ascolto (fine A)"
                    relayconfig = relay.relayConfigRx(presetA, presetB, bandconfiguration)
                    #relay.writeRelay(settings.getPreset("rx"))
                    clear = True
                    txing = ""

            else:
                # stava trasmettendo B
                if pttB == False:
                    ######print "Procedura per ripristino ascolto (fine B)"
                    relayconfig = relay.relayConfigRx(presetA, presetB, bandconfiguration)
                    #relay.writeRelay(settings.getPreset("rx"))
                    clear = True
                    txing = ""

    else:
        print "Logica non first-one-wins non implementata."

    '''
    if clear:
            tx("A",0)
            tx("B",0)
    else:
            if txing == "A":
                    tx("A",1)
                    tx("B",0)
            else:
                    tx("A",0)
                    tx("B",1)
    '''

    #####print "Configurazione relay: " + relayconfig
    ledconfig = "0000" + "0000000000000000" + "00000000000000000000000"
    ####ledconfig = "0000000000000000000000000000000"

    relayconfig = relayconfig[0:16]
    band = myband
    if band == "10":
        relayconfig = relayconfig + "10000000"
        bndleds   = "000000000100"
    if band == "15":
        relayconfig = relayconfig + "01000000"
        bndleds   = "000000010000"
    if band == "20":
        relayconfig = relayconfig + "00100000"
        bndleds   = "000001000000"
    if band == "40":
        relayconfig = relayconfig + "00010000"
        bndleds   = "000100000000"
    if band == "80":
        relayconfig = relayconfig + "00001000"
        bndleds   = "010000000000"
    if band == "160":
        relayconfig = relayconfig + "00000100"
        bndleds   = "100000000000"

    ledconfig = ledconfig + "000000" + presetA

    if presetchanged:
        print "Preset cambiato!! nuovi led:",ledconfig

    ### split:   00000000000000000000000000000000000000 00    00000000         1    00000000
    ### preset:  00000000000000000000000000000000000000 00    00000000         0    xxxxxxxx
    ### banda10  00000000000000000000000000000000000010 00    00000000         0    00000000

    rxsplitA = "0"
    rxPAsum = 0
    for rxPA in presetA[0:8]:
        rxPAsum += int(rxPA)
    if rxPAsum > 1:
        rxsplitA = "1"

    rxsplitB = "0"
    rxPBsum = 0
    for rxPB in presetB[0:8]:
        rxPBsum += int(rxPB)
    if rxPBsum > 1:
        rxsplitB = "1"

    txsplitA = "0"
    txPAsum = 0
    for txPA in presetA[8:16]:
        txPAsum += int(txPA)
    if txPAsum > 1:
        txsplitA = "1"

    txsplitB = "0"
    txPBsum = 0
    for txPB in presetB[8:16]:
        txPBsum += int(txPB)
    if txPBsum > 1:
        txsplitB = "1"




    ledconfig = ""+rxsplitB + presetB[0:8][::-1] + txsplitB + presetB[8:16][::-1] + \
        "000000000"+bndleds  + txsplitA + \
        presetA[8:16][::-1] + rxsplitA + presetA[0:8][::-1]

    AtomicWrite.writeFile("/tmp/relay.txt",relayconfig)
    AtomicWrite.writeFile("/tmp/leds.txt",ledconfig)



    #print relayconfig
    #print len(relayconfig)
        ####relay.writeRelay(relayconfig)

        #time.sleep(1)
