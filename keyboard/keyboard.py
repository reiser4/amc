import os
from evdev import InputDevice, list_devices, categorize, ecodes
from select import select
from keyboardxkeys import HandlerKeyboards
from time import sleep


if __name__ == "__main__":
    devices = [InputDevice(fn) for fn in list_devices()]
    for dev in devices:
        print "Device trovato: ",dev

    #keyboard = HandlerKeyboards("isa0060/serio0/input0")
    #keyboard1 = HandlerKeyboards("usb-musb-hdrc.1.auto-1.1/input1")
    keyboard2 = HandlerKeyboards("usb-musb-hdrc.1.auto-1.2/input1")
    print "\nIstanziata correttamente tastiera\n"
    #keyboard1.startRead()
    keyboard2.startRead()
    
    while 1:
        sleep(30)
        print "\n####################################################\n"
