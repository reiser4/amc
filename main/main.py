
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
#	AtomicWrite.writeFile("/tmp/tx"+R+".txt",str(S))


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

	bandconfiguration = configuration['relayconfig'][str(myband)+'m']
	###print bandconfiguration


	AtomicWrite.writeFile("/tmp/presetTXTA.txt",preset.getPname(presetA,bandconfiguration,"A"))
	####AtomicWrite.writeFile("/tmp/Bpname.txt",preset.getPname(presetA,bandconfiguration,"B"))


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

    relayconfig = relayconfig[0:18]
    band = myband
    if band == "160":
        relayconfig = relayconfig + "100000"
    if band == "80":
        relayconfig = relayconfig + "010000"
    if band == "40":
        relayconfig = relayconfig + "001000"
    if band == "20":
        relayconfig = relayconfig + "000100"
    if band == "15":
        relayconfig = relayconfig + "000010"
    if band == "10":
        relayconfig = relayconfig + "000001"


    AtomicWrite.writeFile("/tmp/relay.txt",relayconfig)
    #print relayconfig
    #print len(relayconfig)
	####relay.writeRelay(relayconfig)

	#time.sleep(1)


