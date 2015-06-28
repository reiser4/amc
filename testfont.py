import Image, ImageFont, ImageDraw
import time

# use a truetype font
#fnt = ImageFont.truetype("8bitOperatorPlus-Regular.ttf",11)

#text = "Hello world!"

tstart = time.time()

width = 160
height = 80
# devo moltiplicare per 2 perche' altrimenti taglia l'altezza, cercare di capire il motivo

im = Image.new("1", (width, height), 0)
#im = Image.new("RGB", (200, 100))

draw = ImageDraw.Draw(im)

#draw.text((0, 0), text, fill='black', font=fnt)
for i in range(2000):
    for y in range(height):
        for x in range(0, width, 2):
            im.putpixel((x,y), 255)

# remove unneccessory whitespaces if needed
#im = im.crop(im.getbbox())

# write into file
im.save("img.png", "png")

im.show()

#print list(im.getdata())
rgb_im = im.convert('RGB')

print "Tempo impiegato:", time.time() - tstart, "secondi"

"""
for y in range(height):
    for x in range(width):
        r, g, b = rgb_im.getpixel((x,y))
        if r != 255 and g != 255 and b != 255:
            print '*',
        else:
            print ' ',
    print '\n'
"""
