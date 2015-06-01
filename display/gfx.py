#### modulo per la gestione della grafica
#### 

from PIL import Image, ImageFont, ImageDraw

class Gfx:
	def __init__(self):
		self.width = 160
		self.height = 80
		self.state = list()
		self.oldstate = list()
		for i in range(0, self.width*self.height):
			self.state.append(0)
			self.oldstate.append(0)
		#print self.state

		self.img = Image.new("1", (self.width, self.height))
		bytes = self.img.tobytes()
		font = ImageFont.truetype("8bitOperatorPlus-Regular.ttf")
		draw = ImageDraw.Draw(self.img)
		draw.text((10,10), "hello", font=font, fill=(255))

		count = 0
		for i in self.img.tobytes():
			print "{0:b}".format(ord(i)).zfill(8),		
			count = count + 1

		print "Totale: ", count

		#print self.img.tobytes()
		#print bytes
		print "Gfx avviata"

	def writeBand(self, band):
		#pulisco la zona superiore con la banda

		print "Banda scritta"		


	def refreshScreen(self):
		### faccio la differenza tra state e oldstate
		### se trovo dei pixel diversi li mando al driver
		self.oldstate = self.state
		#print "Nuovo stato scritto: ", self.state	





mygfx = Gfx()
mygfx.writeBand(40)
mygfx.refreshScreen()
