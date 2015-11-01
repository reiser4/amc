import queue
import threading
import time
import serial

class ComMonitorThread(threading.Thread):
    """
        A thread for monitoring a COM port. The COM port is
        opened when the thread is started.

        data_q:
            Queue for received data. Items in the queue are
            (data, timestamp) pairs, where data is a binary
            string represeting the received data, and timestamp
            is the time elapsed from the thread's start (in
            seconds).

        error_q:
            Queue for error messages. In particular, if the
            serial port fails to open for some reason, an error
            is placed into this queue.

        port:
            The COM port to open. Must be recognized by the
            system.

        port_baud/stopbits/parity:
            Serial communication parameters

        port_timeout:
            The timeout used for reading the COM port. If this
            value is low, the thread will return data in finer
            grained chunks, with more accurate timestamps, but
            it will also consume more CPU.
    """

    def __init__(   self,
                    data_q, error_q,
                    port_num,
                    port_baud=9600,
                    port_stopbits=serial.STOPBITS_ONE,
                    port_parity=serial.PARITY_NONE,
                    port_timeout=None):
        threading.Thread.__init__(self)

        self.serial_port = None
        self.serial_arg = dict( port=port_num,
                                baudrate=port_baud,
                                stopbits=port_stopbits,
                                parity=port_parity,
                                timeout=port_timeout)

        self.data_q = data_q
        self.error_q = error_q

        self.alive = threading.Event()
        # set self.alive = True
        self.alive.set()

    def run(self):
        try:
            if self.serial_port:
                self.serial_port.close()
            self.serial_port = serial.Serial(**self.serial_arg)
        except Exception as e:
            self.error_q.put(str(e))
            return

        error_value = False
        bands = [b'6', b'10', b'12', b'15', b'17', b'20', b'30', b'40', b'60', b'80', b'160']
        apreset = False
        bpreset = False
        apnametx = False
        apnamerx = False
        bpnametx = False
        bpnamerx = False
        band = False
        relay = False
        atx = False
        btx = False
        apreset_ok = False
        bpreset_ok = False

        while self.alive.isSet():
            # Reading 1 byte, followed by whatever is left in the
            # read buffer, as suggested by the developer of PySerial.
            data = self.serial_port.read(1)
            #data += self.serial_port.read(self.serial_port.inWaiting())
            data += self.serial_port.readline()
            ##print("Data: ", data)
            data_list = data.split(b':')
            ##print(data_list)
            if len(data_list) == 2:
                data_type = data_list[0]
                data_value = data_list[1].strip()

                if error_value:
                    self.error_q.put("ComMonitorThread: parola chiave errata")
                    error_value = False

                if data_type == b'APRESET':
                    if len(data_value) == 16:
                        for v in data_value:
                            #print("apreset: " + v)
                            if v != ord(b'0') and v != ord(b'1'):
                                error_value = True
                                print("Errore in APRESET: letto",data_value,v,str(v))
                                #print "apreset: " + v + " " + str(len(data_value))
                                break
                    else:
                        error_value = True
                    if not error_value:
                        apreset = data_value
                        apreset_ok = True
                if data_type == b'BPRESET':
                    if len(data_value) == 16:
                        for v in data_value:
                            #print "bpreset: " + v
                            if v != ord(b'0') and v != ord(b'1'):
                                error_value = True
                                print("Errore con BPRESET")
                                #print "bpreset: " + v + " " + str(len(data_value))
                                break
                    else:
                        error_value = True
                    if not error_value:
                        bpreset = data_value
                        bpreset_ok = True
                if data_type == b'APNAME':
                    """
                    inserire controllo sui valori, cioe' contare i valori a 1
                    e poi contare i singoli nomi. I due valori devono
                    coincidere
                    """
                    try:
                        apnamerx, apnametx = data_value.split(b';')
                        if apreset_ok:
                            len_apname = len(apnamerx.split(b',')) + len(apnametx.split(b','))
                            len_apresent = sum(list(int(chr(x)) for x in apreset))
                            if len_apname != len_apresent:
                                print ("COM_MONITOR: ERRORE len_apname != len_apresent")
                                # TODO: caso lunghezze diverse
                                pass
                    except:
                        self.error_q.put("ComMonitorThread: errore split APNAME")
                if data_type == b'BPNAME':
                    """
                    inserire controllo sui valori, cioe' contare i valori a 1
                    e poi contare i singoli nomi. I due valori devono
                    coincidere
                    """
                    try:
                        bpnamerx, bpnametx = data_value.split(b';')
                        if bpreset_ok:
                            len_bpname = len(bpnamerx.split(b',')) + len(bpnametx.split(b','))
                            len_bpresent = sum(list(int(chr(x)) for x in bpreset))
                            if len_bpname != len_bpresent:
                                print ("COM_MONITOR: ERRORE len_bpname != len_bpresent")
                                # TODO: caso lunghezze diverse
                                pass
                    except:
                        self.error_q.put("ComMonitorThread: errore split BPNAME")
                if data_type == b'BAND':
                    if data_value in bands:
                        band = data_value
                    else:
                        print("Errore con BAND",data_value,bands)
                        error_value = True
                        #print "band: " + data_value + " " + type(data_value)
                if data_type == b'RELAY':
                    if len(data_value) == 24:
                        for v in data_value:
                            if v != ord(b'0') and v != ord(b'1'):
                                error_value = True
                                #print "relay: " + v + " " + str(len(data_value))
                                break
                    else:
                        print("Errore su RELAY")
                        error_value = True
                    if not error_value:
                        relay = data_value
                if data_type == b'ATX':
                    if data_value == b'0' or data_value == b'1':
                        atx = data_value
                    else:
                        print("Errore su ATX",data_value)
                        #print "atx: " + data_value
                        error_value = True
                if data_type == b'BTX':
                    if data_value == b'0' or data_value == b'1':
                        btx = data_value
                    else:
                        print("Errore su BTX",data_value)
                        #print "btx: " + data_value
                        error_value = True
                """
                if apreset:
                    print "apreset ok"
                if bpreset:
                    print "bpreset ok"
                if apnametx:
                    print "apnametx ok"
                if apnamerx:
                    print "apnamerx ok"
                if bpnametx:
                    print "bpnametx ok"
                if bpnamerx:
                    print "bpnamerx ok"
                if band:
                    print "band ok"
                if relay:
                    print "relay ok"
                if atx:
                    print "atx ok"
                if btx:
                    print "btx ok"
                """
                if ((not (apreset == '')) and
                    (not (bpreset == '')) and
                    (not (apnametx == '')) and
                    (not (apnamerx == '')) and
                    (not (bpnametx == '')) and
                    (not (bpnamerx == '')) and
                    (not (band == '')) and
                    (not (relay == '')) and
                    (not (atx == '')) and
                    (not (btx == '')) ):
                    #print("Ho tutti i dati")
                    #print "ComMonitorThread: sono dentro, sto per" +
                    #    " creare il dizionario"
                    timestamp = time.time()
                    data_dict = dict(   apreset=apreset,
                                        bpreset=bpreset,
                                        apnametx=apnametx,
                                        apnamerx=apnamerx,
                                        bpnametx=bpnametx,
                                        bpnamerx=bpnamerx,
                                        band=band,
                                        relay=relay,
                                        atx=atx,
                                        btx=btx,
                                        timestamp=timestamp)

                    self.data_q.put((data_dict, timestamp))
                    # Preparo le variabili per una nuova ricezione
                    apreset = ''
                    bpreset = ''
                    apnametx = ''
                    apnamerx = ''
                    bpnametx = ''
                    bpnamerx = ''
                    band = ''
                    relay = ''
                    atx = ''
                    btx = ''
                    error_value = False
                    apreset_ok = False
                    bpreset_ok = False
                #else:
                    #print("Manca qualcosa...",apreset,bpreset,apnametx,apnamerx,bpnametx,bpnamerx,band,relay,atx,btx)
            ###
            ### Chiedere ad Enrico per il timeout
            ###
            #time.sleep(0.1)

        # clean up
        if self.serial_port:
            self.serial_port.flushInput()
            self.serial_port.close()

    def join(self, timeout=None):
        # set self.alive = False
        self.alive.clear()
        threading.Thread.join(self, timeout)


if __name__ == "__main__":
    pass