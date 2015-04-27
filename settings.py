


### SETTINGS
# classe che si occupa di leggere e scrivere la configurazione



class Settings:

	def __init__(self):
		self.radioAtx = list("0" * 16)
		self.radioBtx = list("0" * 16)
		self.rx = list("0" * 16)
		

	def readParam(self, param):
		if param == "Logic":
			return "first_one_wins"


	def getPreset(self, preset):
		if preset == "radioAtx":
			return ''.join(self.radioAtx)
		else:
			if preset == "radioBtx":
				return ''.join(self.radioBtx)
			else:
				return ''.join(self.rx)

	def setPreset(self, radio, type, preset):

		presetbits = list(preset)
		#print presetbits
		# se ricevo un preset di ricezione sovrascrivo la parte corrispondente di rx
		if type == "rx":
			if radio == "A":
				for i in range(0,8):
					self.rx[i] = presetbits[i]
			else:
				for i in range(0,8):
					self.rx[i+8] = presetbits[i]
		else:
			if radio == "A":
				for i in range(0,8):
					self.radioAtx[i] = presetbits[i]
			else:
				for i in range(0,8):
					self.radioBtx[i+8] = presetbits[i]

		
