



### preset: classe che gestisce il preset attivo ed i relay da attivare.

import os

class Preset:
	def __init__(self):
		print "Preset caricato"

	def readPreset(self):
		#self.radioArx = self.readPresetFile("/tmp/radioArx.txt")
		#self.radioAtx = self.readPresetFile("/tmp/radioArx.txt")
		#self.radioBrx = self.readPresetFile("/tmp/radioArx.txt")
		#self.radioBtx = self.readPresetFile("/tmp/radioArx.txt")
		print "Chiamata readPreset..."

	def readPresetFile(self, path):
		if os.path.isfile(path):
			in_file = open(path, "r")
			text = in_file.read()
			in_file.close()
			#return ord(text)
			return text
		else:
			#print "Attenzione: file" + path + "non esistente"
			return "0000000000000000"