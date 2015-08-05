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
            string representing the received data, and timestamp
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

    def __init__(self, data_q, error_q, port_num, port_timeout=0.01):
        threading.Thread.__init__(self)

        self.serial_port = None
        self.serial_arg = dict(port=port_num, timeout=port_timeout)

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

        while self.alive.isSet():
            # Reading 1 byte, followed by whatever is left in the
            # read buffer, as suggested by the developer of PySerial.
            data = self.serial_port.read(1)
            data += self.serial_port.read(self.serial_port.inWaiting())

            if len(data) > 0:
                timestamp = time.clock()
                self.data_q.put((data, timestamp))
            ###
            ### Chiedere ad Enrico per il timeout
            ###
            time.sleep(2)

        # clean up
        if self.serial_port:
            self.serial_port.close()

    def join(self, timeout=None):
        # set self.alive = False
        self.alive.clear()
        threading.Thread.join(self, timeout)


if __name__ == "__main__":
    pass