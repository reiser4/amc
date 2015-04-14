
import time

#import Adafruit_BBIO.GPIO as GPIO

from bcdin import BcdIn
from bcdout import BcdOut
from icomin import IcomIn
from band import Band
from settings import Settings
from radio import Radio



icomin = IcomIn("P9_33")
band = Band(icomin)
settings = Settings()
radioa = Radio("P9_15", "P9_29", "P8_8", "P8_7", "P8_9", "P8_11")
radiob = Radio("P9_17", "P9_31", "P8_10", "P8_13", "P8_15", "P8_17")

txing = ""
clear = True

while True:
	### devo leggere la banda in cui mi trovo e scriverla sull'uscita del BCD.
	### se necessario aggiornare i rele`, led e display
	### valutare se rallentare questa operazione

	myband = band.readBand()
	logic = settings.readParam("Logic")

	pttA = radioa.readPTT()
	pttB = radiob.readPTT()

	print "Stato: clear: ", clear, " txing: ", txing

	if (logic == "first_one_wins"):

		if clear == True:
			print "Nessuno trasmetteva"
			# nessuno stava trasmettendo.
			if pttA == True:
				clear = False
				txing = "A"
				# ora vuole trasmettere la radio A
				print "Richiesta di TX da Radio A"
				print "Devo inibire radio B e iniziare la procedura di TX"
			else:	
				# radio A non vuole trasmettere.
				if pttB == True:
					clear = False
					txing = "B"
					# radio B vuole trasmettere
					print "Richiesta di TX da Radio B"
					print "Inibisco radio A e faccio procedura TX"
		else:
			print "Tx attiva per ", txing
			# qualcuno trasmetteva
			if txing == "A":
				#stava trasmettendo A
				if pttA == False:
					#A ha appena finito di trasmettere
					print "Procedura per ripristino ascolto (fine A)"

					clear = True
					txing = ""

			else:
				# stava trasmettendo B
				if pttB == False:
					print "Procedura per ripristino ascolto (fine B)"
					clear = True
					txing = ""		

	else:
		print "Logica non first-one-wins non implementata."


	time.sleep(1)


