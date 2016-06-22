#### modulo per la gestione della grafica
####

from PIL import Image, ImageFont, ImageDraw

class Gfx:
    def drawCross(self):

        #self.state = list()
        #for i in range(0, self.width*self.height):
        #        self.state.append(1)
        self.draw.line((0,0)+self.img.size,fill=128)
        self.draw.line((0, self.img.size[1], self.img.size[0], 0), fill=128)

    def clear(self):
        self.draw.rectangle([0, 0, 160, 80], fill=(0), outline=None)


    def writeText(self,x,y,word):
        self.draw.text((x,y), word, font=self.font, fill=(255))

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
        #bytes = self.img.tobytes()
        self.font = ImageFont.truetype("DroidSansMono.ttf",11)
        self.draw = ImageDraw.Draw(self.img)
        #draw.text((10,10), "HELLO TEST", font=font, fill=(255))

        count = 0
        #for i in self.img.tobytes():
        #       print "{0:b}".format(ord(i)).zfill(8),
        #       count = count + 1
        #print "Totale: ", count

        #print self.img.tobytes()
        #print bytes
        print "Gfx avviata"

    def getData(self):
        out = ""
        for i in self.img.tobytes():
            out = out + "{0:b}".format(ord(i)).zfill(8)
        return out

    def writeBand(self, band):
        #pulisco la zona superiore con la banda
        print "Banda scritta"

    def refreshScreen(self):
        ### faccio la differenza tra state e oldstate
        ### se trovo dei pixel diversi li mando al driver
        self.oldstate = self.state
        #print "Nuovo stato scritto: ", self.state
