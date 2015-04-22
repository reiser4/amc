
import time

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
radioa = Radio("P9_15", "P9_29", "P8_8", "P8_7", "P8_9", "P8_11")
radiob = Radio("P9_17", "P9_31", "P8_10", "P8_13", "P8_15", "P8_17")
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
	
	logic = settings.readParam("Logic")

	radioArx = "{0:b}".format(preset.readPresetFile("/tmp/radioArx.txt")).zfill(8)
	radioAtx = "{0:b}".format(preset.readPresetFile("/tmp/radioAtx.txt")).zfill(8)
	radioBrx = "{0:b}".format(preset.readPresetFile("/tmp/radioBrx.txt")).zfill(8)
	radioBtx = "{0:b}".format(preset.readPresetFile("/tmp/radioBtx.txt")).zfill(8)

	#todo: solo se preset cambiati
	
	front.changePreset("A","rx",radioArx)
	front.changePreset("A","tx",radioAtx)
	front.changePreset("B","rx",radioBrx)
	front.changePreset("B","tx",radioBtx)

	#todo: solo se banda o preset cambiati

	front.updateFront()

	print "Presets: ", radioArx, radioAtx, radioBrx, radioBtx

	settings.setPreset("A","rx",radioArx)
	settings.setPreset("A","tx",radioAtx)
	settings.setPreset("B","rx",radioBrx)
	settings.setPreset("B","tx",radioBtx)
	

	pttA = radioa.readPTT()
	pttB = radiob.readPTT()

	print "Stato: clear: ", clear, " txing: ", txing

	if (logic == "first_one_wins"):
		## logica in cui le due radio hanno la stessa priorita` e non possono trasmettere insieme
		if clear == True:
			print "Nessuno trasmetteva"
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
					#sia A che B non vogliono trasmettere: ascolto
					relay.writeRelay(settings.getPreset("rx"))
		else:
			print "Tx attiva per ", txing
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


