# Ho tenuto la nomeclatura di SPI
# Se si fa riferimento alla nomeclatura 74HC595
# MOSI --> DS (Pin 14)
# SCK --> SH_CP (Pin 11)
# SS --> ST_CP (Pin 12)


def setPin(name,mode):
    print "Attivato Pin", name, "come", mode
    
def setHigh(name):
    print name, "--> HIGH: 1"
    
def setLow(name):
    print name, "--> LOW: 0"
    
class ShiftRegister:
    def __init__(self):
        setPin('MOSI','OUTPUT')
        setPin('SS','OUTPUT')
        setPin('SCK','OUTPUT')
    
    def Write(self,bit_string):
        setLow('SS')
        for b in bit_string:
            if int(b) == 1:
                setHigh('MOSI')
            else:
                setLow('MOSI')
            setHigh('SCK')
            setLow('MOSI')
            setLow('SCK')
        
        setHigh('SS')
        

