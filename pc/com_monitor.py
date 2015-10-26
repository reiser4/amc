import Queue
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
        except serial.SerialException, e:
            self.error_q.put(e.message)
            return

        error_value = False
        bands = ["6", "10", "12", "15", "17", "20", "30", "40", "60", "80", "160"]
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

        while self.alive.isSet():
            # Reading 1 byte, followed by whatever is left in the
            # read buffer, as suggested by the developer of PySerial.
            data = self.serial_port.read(1)
            #data += self.serial_port.read(self.serial_port.inWaiting())
            data += self.serial_port.readline()
            #print "Data: ", data
            data_list = data.split(':')
            if len(data_list) == 2:
                data_type = data_list[0]
                data_value = data_list[1].strip()

                if error_value:
                    self.error_q.put("ComMonitorThread: parola chiave errata")
                    error_value = False

                if data_type == 'APRESET':
                    if len(data_value) == 16:
                        for v in data_value:
                            #print "apreset: " + v
                            if v != '0' and v != '1':
                                error_value = True
                                #print "apreset: " + v + " " + str(len(data_value))
                                break
                    else:
                        error_value = True

                    if not error_value:
                        apreset = data_value
                if data_type == 'BPRESET':
                    if len(data_value) == 16:
                        for v in data_value:
                            #print "bpreset: " + v
                            if v != '0' and v != '1':
                                error_value = True
                                #print "bpreset: " + v + " " + str(len(data_value))
                                break
                    else:
                        error_value = True
                    if not error_value:
                        bpreset = data_value
                if data_type == 'APNAME':
                    """
                    inserire controllo sui valori, cioe' contare i valori a 1
                    e poi contare i singoli nomi. I due valori devono
                    coincidere
                    """
                    try:
                        apnamerx, apnametx = data_value.split(';')
                    except:
                        self.error_q.put("ComMonitorThread: errore split APNAME")
                if data_type == 'BPNAME':
                    """
                    inserire controllo sui valori, cioe' contare i valori a 1
                    e poi contare i singoli nomi. I due valori devono
                    coincidere
                    """
                    try:
                        bpnamerx, bpnametx = data_value.split(';')
                    except:
                        self.error_q.put("ComMonitorThread: errore split BPNAME")
                if data_type == 'BAND':
                    if data_value in bands:
                        band = data_value
                    else:
                        error_value = True
                        #print "band: " + data_value + " " + type(data_value)
                if data_type == 'RELAY':
                    if len(data_value) == 24:
                        for v in data_value:
                            if v != '0' and v != '1':
                                error_value = True
                                #print "relay: " + v + " " + str(len(data_value))
                                break
                    else:
                        error_value = True
                    if not error_value:
                        relay = data_value
                if data_type == 'ATX':
                    if data_value == '0' or data_value == '1':
                        atx = data_value
                    else:
                        #print "atx: " + data_value
                        error_value = True
                if data_type == 'BTX':
                    if data_value == '0' or data_value == '1':
                        btx = data_value
                    else:
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
                if (apreset and
                    bpreset and
                    apnametx and
                    apnamerx and
                    bpnametx and
                    bpnamerx and
                    band and
                    relay and
                    atx and
                    btx):
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
            ###
            ### Chiedere ad Enrico per il timeout
            ###
            time.sleep(1)

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