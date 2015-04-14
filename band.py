
### BAND
# fa da interfaccia tra il main e i vari tipi di lettura di banda

class Band:
	def __init__(self, obj):
		print "Avviata classe BAND per operare su ", obj
		self.obj = obj
		self.band = obj.readBand()

	def readBand(self):
		newband = self.obj.readBand()
		if newband != self.band:
			self.band = newband
			self.writeBand()

		return self.band


	def writeBand(self):
		self.bcdout.writeBand(self.band)