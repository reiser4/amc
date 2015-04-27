
import Adafruit_BBIO.GPIO as GPIO


### classe Relay
# riceve indicazioni su come impostare i vari rele` di uscita

relayPins = ["P8_7","P8_9","P8_11","P8_13","P8_15","P8_17","","","P8_8","P8_10","P8_12","P8_14","P8_16","P8_18","",""]

for pin in relayPins:
	if pin != '':
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, GPIO.HIGH)
		

class Relay:
	def __init__(self):
		print "Relay inizializzato"

	def writeRelay(self, configuration):
		#configuration e` una stringa binaria tipo 0001001000000000
		#devo stamparla in file di output /tmp in modo da presentarlo al simulatore
		# poi per ogni singolo bit devo decidere come agire

		front_file = open("/tmp/relay.txt", "w")
		front_file.write(configuration)
		front_file.close()

		relayPins

		relaylist = list(configuration)
		for i in range(0,16):
			if relayPins[i] != "":
				if relaylist[i] == '0':
					GPIO.output(relayPins[i], GPIO.HIGH)
				else:		
					GPIO.output(relayPins[i], GPIO.LOW)
		#	print "Relay numero ",i,": ",relaylist[i]

