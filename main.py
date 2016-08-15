
import time
import json
#import Adafruit_BBIO.GPIO as GPIO

from bcdin import BcdIn
from bcdout import BcdOut
from icomin import IcomIn
from band import Band
from settings import Settings
from radio import Radio
from preset import Preset
from front import Front
from relay import Relay

relay = Relay()
front = Front()
icomin = IcomIn("P9_33")
band = Band(icomin)
settings = Settings()
radioa = Radio("P9_15", "P9_29", "P8_19", "P8_7", "P8_9", "P8_11")
radiob = Radio("P9_17", "P9_31", "P8_26", "P8_13", "P8_15", "P8_17")
preset = Preset()
txing = ""
clear = True
lastband = "-1"



while True:
	### devo leggere la banda in cui mi trovo e scriverla sull'uscita del BCD.
	### se necessario aggiornare i rele`, led e display
	### valutare se rallentare questa operazione

	myband = band.readBand()
	if myband != lastband:
		# rilevato cambio banda!
		front.changeBand(myband)
		lastband = myband

	print "Banda: " + str(myband)
	
	logic = settings.readParam("Logic")

	print "Logica: " + logic


	presetA = preset.readPresetFile("/tmp/radioA.txt")
	presetB = preset.readPresetFile("/tmp/radioB.txt")

	print "Preset A: " + presetA
	print "Preset B: " + presetB
	
	with open("test-config.json", 'r') as fin:
		configuration = json.load(fin)
	#print configuration

	bandconfiguration = configuration['relayconfig'][str(myband)+'m']
	print bandconfiguration

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
	

	pttA = radioa.readPTT()
	pttB = radiob.readPTT()

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
				print "Richiesta di TX da Radio A"
				print "Devo inibire radio B e iniziare la procedura di TX"
				relay.writeRelay(settings.getPreset("radioAtx"))

			else:	
				# radio A non vuole trasmettere.
				if pttB == True:
					clear = False
					txing = "B"
					# radio B vuole trasmettere
					print "Richiesta di TX da Radio B"
					print "Inibisco radio A e faccio procedura TX"
					relay.writeRelay(settings.getPreset("radioBtx"))
				else:
					### ASCOLTO
					#sia A che B non vogliono trasmettere: ascolto

					relayconfig = list("0" * 24)
					#devo prendere le prime 8 selezioni per le due radio e attivare i rele corrispondenti
					pos = 0
					for sel in presetA[0:8]:
						print "Controllo preset A in posizione " + str(pos) + ": " + sel
						if sel == "1":
							print " attivo! bandconfiguration "
							print bandconfiguration
							if str(pos) in bandconfiguration:
								print "Trovata chiave " + str(pos)
								relaypos = 0
								print "Attivo i relay " + bandconfiguration[str(pos)]['relayA']
								for relay in bandconfiguration[str(pos)]['relayA']:
									print " verifico " + relay
									if relay == "1":
										print " attivo relay in pos. " + str(relaypos)
										relayconfig[relaypos] = "1"
									relaypos += 1
						pos += 1

					for sel in presetB[0:8]:
						if sel == "1":
							if pos in bandconfiguration:
								relaypos = 0
								for relay in bandconfiguration[pos]['relayB']:
									if relay == "1":
										relayconfig[relaypos] = "1"
									relaypos += 1
						pos += 1

					print "Relayconfig: " + "".join(relayconfig)





					#####relay.writeRelay(settings.getPreset("rx"))
		else:
			#print "Tx attiva per ", txing
			# qualcuno trasmetteva
			if txing == "A":
				#stava trasmettendo A
				if pttA == False:
					#A ha appena finito di trasmettere
					print "Procedura per ripristino ascolto (fine A)"
					relay.writeRelay(settings.getPreset("rx"))
					clear = True
					txing = ""

			else:
				# stava trasmettendo B
				if pttB == False:
					print "Procedura per ripristino ascolto (fine B)"
					relay.writeRelay(settings.getPreset("rx"))
					clear = True
					txing = ""		

	else:
		print "Logica non first-one-wins non implementata."


	time.sleep(1)


