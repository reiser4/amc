####

import png


class Display:
    def __init__(self, output):
        if output == "dummy":
            print "Avviato display con output dummy"
            print "Dimensioni: 160x80"
        self.data = []
        for x in range(0,80):
            self.data.append([])
            for y in range(0,160):
                self.data[x].append(153)
                self.data[x].append(204)
                self.data[x].append(255)

    def setPixel(self, x, y, state):
        ### stati possibili: True (acceso) e False (spento)
        ### x e` la colonna, y e` la riga
        if state == True:
            self.data[x][y*3] = 255
            self.data[x][y*3+1] = 255
            self.data[x][y*3+2] = 255
        else:
            self.data[x][y*3] = 153
            self.data[x][y*3+1] = 204
            self.data[x][y*3+2] = 255

    def writePng(self):
        png.from_array(self.data, "RGB").save('webroot/display.png')

    def writeChar(self, startx, starty, char):
        for y in range(0,charwidth):    
            for x in range(0,charheight):
                if font[char][x][y] == 1:
                    self.setPixel(startx+x, starty+y, True)
                else:
                    self.setPixel(startx+x, starty+y, False)

    def writeWord(self, startx, starty, word):
        for i in list(word):
            if i == " ":
                starty += 3
            else:
                self.writeChar(startx, starty, i)
                starty += charwidth+1

    def writeLine(self, startx, starty, npixel, direction):
        ### x e` la colonna, y e` la riga
        if direction == "o":
            for y in range(starty, starty+npixel):
                self.setPixel(startx, y, True)
        elif direction == "v":
            for x in range(startx, startx+npixel):
                self.setPixel(x, starty, True)
    
    def writeRect(self, startx, starty, width, height):
        ### x e` la colonna, y e` la riga
        for h in xrange(height):
            self.writeLine(startx+h, starty, width, "o")

