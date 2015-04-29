'''
Classe per la lettura della tastiera collegata via usb
'''
import threading
import os, sys
from evdev import InputDevice, list_devices, categorize, ecodes
from atomicwrite import AtomicWrite

class HandlerKeyboards(object):

    def __init__(self, usbdevice):
        '''
        Come parametri ricevo l'id fisico della porta usb alla quale voglio attaccare la tastiera

        ID fissi presenti nel file sono da cambiare

        chiedere ad Enrico se va bene come viene gestito o se preferisce in altri modi        
        '''
        
        #if usbdevice == "isa0060/serio0/input0":
        if usbdevice == "usb-musb-hdrc.1.auto-1.2/input1":
            print "Tastiera 1: " + usbdevice
            self.keyboard = "1"
            self.radio = "A"
        elif usbdevice == "usb-musb-hdrc.1.auto-1.2/input2":
            print "Tastiera 2: " + usbdevice
            self.keyboard = "2"
            self.radio = "B"
        else:
            # lanciare eccezione
            sys.exit("ERRORE: e' stato passatto un usb id sbagliato, fermo il programma")
        
        devices = [InputDevice(fn) for fn in list_devices()]
        addressusb = None
        for device in devices:
            if device.phys == usbdevice:
                indexevent = str(device.fn).index("event")
                # controllo se esiste veramente una tastiera all'indirizzo ricevuto come parametro
                if str(os.system("ls -l /dev/input/by-id | grep " + str(device.fn)[indexevent:])).find("kbd") or \
                        str(os.system("ls -l /dev/input/by-path | grep " + str(device.fn)[indexevent:])).find("kbd"):
                    print "Trovata tastiera: " + device.fn + ", " + device.name + ", " + device.phys
                    addressusb = device.fn
                    break
                else:
                    sys.exit("ERRORE: all'indirizzo passato non e' attaccata una tastiera riconosciuta, fermo il programma")
        if addressusb:
            self.dev = InputDevice(addressusb)
            print "Effettuata connessione con la tastiera"
        else:
            # lanciare eccezzione
            sys.exit("ERRORE, non e' stato trovato nessun usb con questo indirizzo: " + str(usbdevice))

    def startRead(self):
        # creazione thread
        self.readkeyboardthread = ReadKeyboard(self.keyboard, self.dev, self.radio)
        self.readkeyboardthread.daemon = True
        self.readkeyboardthread.start()


class ReadKeyboard(threading.Thread):
    '''
    trovare un metodo adeguato per fermare il thread in ascolto
    '''
    def __init__(self, keyboard, dev, radio):
        print "##### -> Sono in ReadKeyboard"
        self.keyboard = keyboard
        self.dev = dev
        self.radio = radio
        threading.Thread.__init__(self)        

    def __readKeystate(self, file_pointer):
        file_pointer.seek(0)
        return file_pointer.read()
    
    def run(self):
        print "##### -> Sono nel thread per l'ascolto della tastiera"
        filename_keystate = "/tmp/keystate" + self.keyboard + ".txt"
        dict_keystate = { '11': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, '30': 10, '48': 11, '46': 12, '32': 13, '18': 14, '33': 15}

        if os.path.isfile(filename_keystate):
            print "Il file 'keystate" + self.keyboard + ".txt' esiste,",
            f_keystate = open(filename_keystate, "r+")
            str_keystate = self.__readKeystate(f_keystate)
            print "stato: " + str(str_keystate)
            f_keystate.close()
        else:
            print "Il file 'keystate" + self.keyboard + ".txt' non esiste, lo creo con stato '1000000010000000'"
            AtomicWrite.writeFile(filename_keystate, "1000000010000000")
            str_keystate = "1000000010000000"

        filecorrect = True
        for keystate in str_keystate:
            if keystate != "0" and keystate != "1":
                filecorrect = False
                break
        n_keystate = len(str_keystate)
        if not filecorrect or n_keystate != 16:
            print "ERRORE: il file trovato non e' corretto, lo riscrivo con stato '1000000010000000'"
            AtomicWrite.writeFile(filename_keystate, "1000000010000000")

        print "stato: " + str(str_keystate)
        # divido la stringa di valori in due liste contenti ognuna meta' stringa
        keystate1 = list(str_keystate[0:(n_keystate/2)])
        keystate2 = list(str_keystate[(n_keystate/2):])
        print "keystate1: " + str(keystate1)
        print "keystate2: " + str(keystate2)

        for event in self.dev.read_loop():
            if event.type == ecodes.EV_KEY and event.value == 0:
                try:
                    # calcolo il modulo del valore perche' le due liste keystate1 e 2 sono la meta' del dizionario
                    ##key_module = dict_keystate[str(event.code)] % (n_keystate/2)
                    ##if dict_keystate[str(event.code)] < (n_keystate/2):
                    ##    keystate1[key_module] = self.valueKeystate(keystate1[key_module])
                    ##else:
                    ##    keystate2[key_module] = self.valueKeystate(keystate2[key_module])
                    ##keystate = list(keystate1)
                    ##keystate.extend(keystate2)
                    ##print str(self.dev.phys) + " Nuovo keystate: " + str(keystate)
                    ##self.__writeKeystate(f_keystate, "".join(keystate))

                    key_module = dict_keystate[str(event.code)] % (n_keystate/2) #offset tra 0 e 7
                    print "Modulo: ",key_module
                    if dict_keystate[str(event.code)] < (n_keystate/2): #entro 8
                        keystate1 = self.enableIndex(key_module)
                        type = "rx"
                        ks = keystate1
                    else:
                        keystate2 = self.enableIndex(key_module)
                        type = "tx"
                        ks = keystate2
                    keystate = list(keystate1)
                    keystate.extend(keystate2)
                    print str(self.dev.phys) + " Nuovo keystate: " + str(keystate)
                    AtomicWrite.writeFile("/tmp/radio" + self.radio + type + ".txt", chr(int(ks,2)))

                except Exception as e:
                    print(e)
                    #print "Valore non valido, event.code: " + str(event.code)


    def valueKeystate(self, value):
        if value == "0":
            return "1"
        else:
            return "0"

    def enableIndex(self, index):
        output = "0"*index + "1" + "0"*(8-index-1)
        print "Output: ",output
        return output

