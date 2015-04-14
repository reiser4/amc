

### BCD OUT
# funzionamento: questo modulo deve riuscire a pilotare l'uscita BCD out a seconda della banda.


class BcdOut:

	def __init__(self, pinA, pinB, pinC, pinD):
		self.pinA = pinA
		self.pinB = pinB
		self.pinC = pinC
		self.pinD = pinD

	def writeBand(self, band):
		print "Da fare: scrittura banda su piedini ", self.pinA, " ", self.pinB, " ", self.pinC, " ", self.pinD, " "

