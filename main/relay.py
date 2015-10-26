
import Adafruit_BBIO.GPIO as GPIO
from atomicwrite import AtomicWrite


### classe Relay
# riceve indicazioni su come impostare i vari rele` di uscita

#relayPins = ["P8_7","P8_9","P8_11","P8_13","P8_15","P8_17","","","P8_8","P8_10","P8_12","P8_14","P8_16","P8_18","",""]
relayPins = ["","","","","","","","","","","","","","","","","","","","","","","",""]

for pin in relayPins:
	if pin != '':
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, GPIO.HIGH)
		

class Relay:
	def __init__(self):
		print "Relay inizializzato"

	def relayConfigRx(self, presetA, presetB, bandconfiguration):
		return self.relayConfig(presetA, presetB, bandconfiguration)

	def relayConfigTx(self, preset, radio, bandconfiguration):
		relayconfig = list("0" * 24)
		pos = 8
		print "Trasmetto con preset " + preset[8:]
		for sel in preset[8:]:
			if sel == "1":
				if str(pos) in bandconfiguration:
					relaypos = 0
					for relay in bandconfiguration[str(pos)]['relay'+radio]:
						if relay == "1":
							relayconfig[relaypos] = "1"
						relaypos += 1
			pos += 1
		
		return "".join(relayconfig)





	def relayConfig(self, presetA, presetB, bandconfiguration):
		relayconfig = list("0" * 24)
		pos = 0
		for sel in presetA[0:8]:
			if sel == "1":
				if str(pos) in bandconfiguration:
					relaypos = 0
					for relay in bandconfiguration[str(pos)]['relayA']:
						if relay == "1":
							relayconfig[relaypos] = "1"
						relaypos += 1
			pos += 1
		pos = 0
		for sel in presetB[0:8]:
			if sel == "1":
				if str(pos) in bandconfiguration:
					relaypos = 0
					for relay in bandconfiguration[str(pos)]['relayB']:
						if relay == "1":
							relayconfig[relaypos] = "1"
						relaypos += 1
			pos += 1
		return "".join(relayconfig)

	def writeRelay(self, configuration):
		#configuration e` una stringa binaria tipo 0001001000000000
		#devo stamparla in file di output /tmp in modo da presentarlo al simulatore
		# poi per ogni singolo bit devo decidere come agire

		#front_file = open("/tmp/relay.txt", "w")
		#front_file.write(configuration)
		#front_file.close()
		#relayPins

		AtomicWrite.writeFile("/tmp/relay.txt",configuration)

		relaylist = list(configuration)
		for i in range(0,16):
			if relayPins[i] != "":
				if relaylist[i] == '0':
					GPIO.output(relayPins[i], GPIO.HIGH)
				else:		
					GPIO.output(relayPins[i], GPIO.LOW)
		#	print "Relay numero ",i,": ",relaylist[i]

