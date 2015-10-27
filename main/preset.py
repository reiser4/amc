



### preset: classe che gestisce il preset attivo ed i relay da attivare.

import os

class Preset:
	def __init__(self):
		print "Preset caricato"


	def getPname(self,preset,bandconfiguration,radio):
		####print "Richiesto Pname"

		rxant = ""
		txant = ""

		for i in range(0,16):
			####print "Posizione",i
			val = preset[i]
			####print "Valore",val
			if val == "1":
				####print "Attivato"
				if i < 8:
					if str(i) in bandconfiguration:
						rxant = rxant + "," + bandconfiguration[str(i)]['label']
					else:
						rxant = rxant + "," + "Rx"+str(i)
				else:
					if str(i) in bandconfiguration:
                                                txant = txant + "," + bandconfiguration[str(i)]['label']
                                        else:
                                                txant = txant + "," + "Tx"+str(i)

		###print preset
		###print bandconfiguration
		###print radio

		out = rxant[1:] + ";" + txant[1:]
		###print "Output:",out
		return out

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
