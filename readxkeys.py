import os
from evdev import InputDevice, list_devices, categorize, ecodes
from select import select
from keyboardxkeys import HandlerKeyboards
from time import sleep


if __name__ == "__main__":
    devices = [InputDevice(fn) for fn in list_devices()]
    for dev in devices:
        print dev

    #keyboard = HandlerKeyboards("isa0060/serio0/input0")
    keyboard = HandlerKeyboards("usb-musb-hdrc.1.auto-1/input1")
    print "\nIstanziata correttamente tastiera\n"
    keyboard.startRead()
    while 1:
        sleep(30)
        print "\n####################################################\n"


'''
def writeKeystate(file_pointer, message):
    file_pointer.seek(0)
    file_pointer.write(message)

def valueKeystate(value):
    if value == "0":
        return "1"
    else:
        return "0"


devices = map(InputDevice, ("/dev/input/event1", "/dev/input/event2"))
devices = {dev.fd : dev for dev in devices}

for dev in devices.values():
    print(dev)

filename_keystate1 = "/tmp/keystate1.txt"
filename_keystate2 = "/tmp/keystate2.txt"
dict_keystate = { '11': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, '30': 10, '48': 11, '46': 12, '32': 13, '18': 14, '33': 15}

if os.path.isfile(filename_keystate1):
    print "Il file 'keystate1.txt' esiste,",
    f_keystate1 = open(filename_keystate1, "r+")
else:
    print "Il file 'keystate1.txt' non esiste, lo creo con stato '1000000010000000'"
    f_keystate1 = open(filename_keystate1, "w+")
    f_keystate1.write("1000000010000000")
    f_keystate1.seek(0)

if os.path.isfile(filename_keystate2):
    print "Il file 'keystate2.txt' esiste,",
    f_keystate2 = open(filename_keystate2, "r+")
else:
    print "Il file 'keystate2.txt' non esiste, lo creo con stato '1000000010000000'"
    f_keystate2 = open(filename_keystate2, "w+")
    f_keystate2.write("1000000010000000")
    f_keystate2.seek(0)

str_keystate1 = f_keystate1.read()
n_keystate1 = len(str_keystate1)
print "stato: " + str(str_keystate1)
# divido la stringa di valori in due liste contenti ognuna meta' stringa
keystate11 = list(str_keystate1[0:(n_keystate1/2)])
keystate12 = list(str_keystate1[(n_keystate1/2):])
print "keystate11: " + str(keystate11)
print "keystate12: " + str(keystate12)

str_keystate2 = f_keystate2.read()
n_keystate2 = len(str_keystate2)
print "stato: " + str(str_keystate2)
# divido la stringa di valori in due liste contenti ognuna meta' stringa
keystate21 = list(str_keystate2[0:(n_keystate2/2)])
keystate22 = list(str_keystate2[(n_keystate2/2):])
print "keystate21: " + str(keystate21)
print "keystate22: " + str(keystate22)

while True:
    r,w,x = select(devices, [], [])
    for fd in r:
        for event in devices[fd].read():
            if event.type == ecodes.EV_KEY and event.value == 0:
                try:
                    # calcolo il modulo del valore perche' le due liste keystate1 e 2 sono la meta' del dizionario
                    key_module = dict_keystate[str(event.code)] % (n_keystate1/2)
                    
                    if dict_keystate[str(event.code)] < (n_keystate1/2):
                        keystate11[key_module] = valueKeystate(keystate11[key_module])
                    else:
                        keystate12[key_module] = valueKeystate(keystate12[key_module])

                    keystate1 = list(keystate11)
                    keystate1.extend(keystate12)
                    print str(devices[fd]) + " Nuovo keystate: " + str(keystate1)
                    
                    writeKeystate(f_keystate1, "".join(keystate1))

                except Exception as e:
                    print(e)
                    #print "Valore non valido, event.code: " + str(event.code)

f_keystate1.close()
f_keystate2.close()
'''
