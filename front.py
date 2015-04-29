
from atomicwrite import AtomicWrite

### classe front: gestione del frontale (display e leds)


class Front:
	def __init__(self):

		self.leds = list("0" * 64)
		print "Frontale inizializzato:", self.leds

	def changeBand(self, band):

		pin = -1
		if (band == 6):
			pin = 19
		if (band == 10):
			pin = 20
		if (band == 12):
			pin = 21
		if (band == 15):
			pin = 22
		if (band == 17):
			pin = 23
		if (band == 20):
			pin = 24
		if (band == 30):
			pin = 25
		if (band == 40):
			pin = 26
		if (band == 60):
			pin = 27
		if (band == 80):
			pin = 28
		if (band == 160):
			pin = 29

		for i in range(19,30):
			self.leds[i] = '0';
		self.leds[pin] = '1';		

	def changePreset(self, radio, type, string):
		plist = list(string)
		if radio == "A":
			start = 0
		else:
			start = 39

		if type == "tx":
			start += 9

		for i in range(0,8):
			self.leds[start+i] = plist[i]


	def updateFront(self):

		outstring = ''.join(self.leds)
		outbytes = list()
		c = 0
		while c < 57:
			byte = outstring[c:c+8]
			value = int(byte, 2)
			outbytes.append(chr(value))
			c += 8

		AtomicWrite.writeFile("/tmp/sr_led.txt", ''.join(outbytes))
		#front_file = open("/tmp/sr_led.txt", "w")
		#front_file.write(''.join(outbytes))
		#front_file.close()

