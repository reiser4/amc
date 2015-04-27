



### classe Relay
# riceve indicazioni su come impostare i vari rele` di uscita


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

		relaylist = list(configuration)
		#for i in range(0,16):
		#	print "Relay numero ",i,": ",relaylist[i]

