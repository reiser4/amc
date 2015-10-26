
### ICOM IN
# funzionamento: il modulo legge il piedino analogico e restituisce la banda secondo protocollo icom



class IcomIn:

	def __init__(self, aPin):
		self.aPin = aPin
		print "Avviato icom band decoder (dummy) su pin", aPin

	def readBand(self):
		#print "non implementato: restituisco sempre 40"
		return 40
