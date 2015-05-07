import Image, ImageFont, ImageDraw


# use a truetype font
fnt = ImageFont.truetype("8bitOperatorPlus-Regular.ttf", 11)

text = "Hello world!"
(width, height) = fnt.getsize(text)
print width, height
# devo moltiplicare per 2 perche' altrimenti taglia l'altezza, cercare di capire il motivo
im = Image.new("RGB", (width, height*2), color='white')
#im = Image.new("RGB", (200, 100))

draw = ImageDraw.Draw(im)

draw.text((0, 0), text, fill='black', font=fnt)

# remove unneccessory whitespaces if needed
im = im.crop(im.getbbox())
(width, height) = im.size
print width, height

# write into file
im.save("img.bmp")

im.show()

#print list(im.getdata())
rgb_im = im.convert('RGB')

for y in range(height):
    for x in range(width):
        r, g, b = rgb_im.getpixel((x,y))
        if r != 255 and g != 255 and b != 255:
            print '*',
        else:
            print ' ',
    print '\n'
