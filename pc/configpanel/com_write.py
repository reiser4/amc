#import Queue
import serial

class ComWrite:
    def __init__(   self,
                    port_num,
                    port_baud=9600,
                    port_stopbits=serial.STOPBITS_ONE,
                    port_parity=serial.PARITY_NONE,
                    port_timeout=None):

        self.serial_port = None
        self.serial_arg = dict( port=port_num,
                                baudrate=port_baud,
                                stopbits=port_stopbits,
                                parity=port_parity,
                                timeout=port_timeout)
        self.isOpen = False

    def connect(self):
        if not self.isOpen:
            try:
                self.serial_port = serial.Serial(**self.serial_arg)
                self.isOpen = True
                #return True
            except: #serial.SerialException, e:
                raise
                #return False

    def close(self):
        if self.serial_port:
            self.serial_port.flush()
            self.serial_port.close()
            self.isOpen = False

    def write(self, data):
        if self.isOpen:
            try:
                self.serial_port.write(bytearray(data, 'utf-8'))
                self.serial_port.flush()
                #print "Scritto"
                #return True
            except:
                raise
        #else:
        #    return False
