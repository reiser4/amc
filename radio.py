

import Adafruit_BBIO.GPIO as GPIO

### Radio
# gestisce l'interfaccia con i due transceiver a livello di PTT e interlock.

class Radio:
	def __init__ (self, inhibitInPin, inhibitOutPin, pttIn, pttOut, pttOutD1, pttOutD2):
		print "Inizializzata Radio con pin: ", inhibitInPin, inhibitOutPin, pttIn,
		pttOut, pttOutD1, pttOutD2

		self.inhibitInPin = inhibitInPin
		self.inhibitOutPin = inhibitOutPin
		self.pttIn = pttIn
		self.pttOut = pttOut
		self.pttOutD1 = pttOutD1
		self.pttOutD2 = pttOutD2

		GPIO.setup(pttIn, GPIO.IN, GPIO.PUD_UP)

	def readPTT(self):
		val = GPIO.input(self.pttIn)
		#print "Valore PTT: ", val
		if val == 1:
			return False
		else:
			return True
