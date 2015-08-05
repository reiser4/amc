import sys, time, Queue
import serial.tools.list_ports
from com_monitor import ComMonitorThread
from livedatafeed import LiveDataFeed
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer

class ViewPanel(QMainWindow):
    def __init__(self):
        super(ViewPanel, self).__init__()
        # imposto la grandezza del font
        self.setStyleSheet('font-size: 11pt;')
        # all'avvio del programma e' selezionata la radio A
        self.radio = "A"
        self.portname = ""
        self.nantenne = 8
        self.nrelay = 24
        # indica se sono in ascolto o no
        self.monitor_active = False
        # variabile per il thread di ascolto
        self.com_monitor = None
        # indica l'ultimo aggiornamento della view
        self.lastupdateview = None
        # varibile per avere i dati piu' recenti
        self.livefeed = LiveDataFeed()
        # code per i dati e per gli errori
        self.data_q = Queue.LifoQueue()
        self.error_q = Queue.Queue()
        # conto alla rovescia
        self.timer = QTimer()
        #self.setGeometry(0, 0, 600, 600)
        self.initAction()
        # imposto il titolo della finestra
        self.setWindowTitle("RadioA")
        # inizializzo la toolbar
        self.initToolBar()
        # creo gli elementi della finistra
        self.initUI()
        # sposta la finestra al centro del desktop
        self.centerOnScreen()
        # visualizzo la scritta 'Ready' nella status bar
        self.statusBar().showMessage("Ready")
        # impongo che la finestra sia sempre in primo piano
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setActionsEnableState()

    def initAction(self):
        # azione per uscire dall'applicazione
        self.exit_action = QAction(QIcon("icons/exit.png"), "&Exit", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.setStatusTip("Exit application")
        # collego l'azione exit_action all'evento self.close (gia' presente in PyQT)
        self.exit_action.triggered.connect(self.close)

        self.start_action = QAction(QIcon("icons/start.png"), "&Start", self)
        self.start_action.setShortcut("Ctrl+S")
        self.start_action.setStatusTip("Start listening")
        self.start_action.triggered.connect(self.startListening)

        self.stop_action = QAction(QIcon("icons/stop.png"), "&Stop", self)
        self.stop_action.setShortcut("Ctrl+B")
        self.stop_action.setStatusTip("Stop listening")
        self.stop_action.triggered.connect(self.stopListening)

    def initToolBar(self):
        toolbar = self.addToolBar('ToolBar')
        toolbar.addAction(self.start_action)
        toolbar.addSeparator()
        toolbar.addAction(self.stop_action)

    def initUI(self):
        settings_layout = QHBoxLayout()
        settings_layout.addStretch(2)
        settings_layout.addWidget(QLabel('COM Port:'))
        serials_c = QComboBox(self)
        self.serials_list = list(serial.tools.list_ports.comports())
        for ser in self.serials_list:
            serials_c.addItem(ser[1])
        serials_c.activated.connect(self.selectSerial)
        settings_layout.addWidget(serials_c)
        settings_layout.addStretch(1)
        settings_layout.addWidget(QLabel('Radio:'))
        radioA = QRadioButton("A")
        radioA.setChecked(True)
        radioB = QRadioButton("B")
        self.radio_group = QButtonGroup()
        self.radio_group.addButton(radioA, 0)
        self.radio_group.addButton(radioB, 1)
        self.radio_group.buttonClicked.connect(self.selectRadio)
        settings_layout.addWidget(radioA)
        settings_layout.addWidget(radioB)

        self.antenneRX_list = list()
        radioRX_layout = QGridLayout()
        radioRX_layout.addWidget(QLabel("Antenne"), 0, 0)
        radioRX_layout.addWidget(QLabel("Present"), 1, 0)
        for i in range(self.nantenne):
            self.antenneRX_list.append(QLabel(str(i+1)))
            radioRX_layout.addWidget(self.antenneRX_list[i], 0, i+1)
        self.presentRX_label = QLabel()
        #self.presentRX_label.setText("################")
        radioRX_layout.addWidget(self.presentRX_label, 1, 1, 1, self.nantenne)
        radioRX_groupbox = QGroupBox('RX')
        radioRX_groupbox.setLayout(radioRX_layout)
        #radioRX_groupbox.setStyleSheet("background-color: red;")

        self.antenneTX_list = list()
        radioTX_layout = QGridLayout()
        radioTX_layout.addWidget(QLabel("Antenne"), 0, 0)
        radioTX_layout.addWidget(QLabel("Present"), 1, 0)
        for i in range(self.nantenne):
            # +9 perche' l'indice visualizzato parte 9 e non da 0
            self.antenneTX_list.append(QLabel(str(i+9)))
            radioTX_layout.addWidget(self.antenneTX_list[i], 0, i+1)
        self.presentTX_label = QLabel()
        radioTX_layout.addWidget(self.presentTX_label, 1, 1, 1, self.nantenne)
        radioTX_groupbox = QGroupBox('TX')
        radioTX_groupbox.setLayout(radioTX_layout)
        #radioTX_groupbox.setStyleSheet("QGroupBox { border: black; }")

        central_layout = QHBoxLayout()
        central_layout.addWidget(radioRX_groupbox)
        central_layout.addWidget(radioTX_groupbox)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(QLabel('Relay:'))
        self.relay_list = list()
        for i in range(self.nrelay):
            # +1 perche' l'indice visualizzato parte 1 e non da 0
            self.relay_list.append(QLabel(str(i+1)))
            bottom_layout.addWidget(self.relay_list[i])
        #self.relay_list[3].setStyleSheet("background-color: red;")

        """
        horizontalLine = QFrame()
        horizontalLine.setFrameStyle(QFrame.HLine)
        horizontalLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalLine.setStyleSheet("border: gray;")
        """
        main_layout = QVBoxLayout()
        main_layout.addLayout(settings_layout)
        main_layout.addLayout(central_layout)
        #main_layout.addWidget(horizontalLine)
        main_layout.addLayout(bottom_layout)

        main_frame = QWidget()
        main_frame.setLayout(main_layout)
        self.setCentralWidget(main_frame)

    def centerOnScreen(self):
        # prende le dimensioni della finestra
        qr = self.frameGeometry()
        # prende il punto centrale del display date le sue dimensioni
        cp = QDesktopWidget().availableGeometry().center()
        # sposto la finestra al centro dello schermo
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def selectSerial(self, i):
        #print self.serials_list[i]
        self.portname = self.serials_list[i][0]
        #print self.portname
        self.statusBar().showMessage("Selected COM: " + self.portname)
        self.setActionsEnableState()

    def selectRadio(self, radioButton):
        if "A" == radioButton.text():
            self.radio = "A"
            self.setWindowTitle("RadioA")
        elif "B" == radioButton.text():
            self.radio = "B"
            self.setWindowTitle("RadioB")
        else:
            self.warningMessage("Errore", "Errore nella selezione dela radio")
        #print self.radio_group.checkedId()
        self.statusBar().showMessage("Selected radio: " + self.radio)

    def startListening(self):
        """
            Start the listening: com_monitor thread and the update timer
        """
        if self.com_monitor is not None or self.portname == '':
            return
        ###
        ### Chiedere ad Enrico per il timeout
        ###
        self.com_monitor = ComMonitorThread(
            self.data_q,
            self.error_q,
            self.portname,
            5)
        self.com_monitor.start()
        # prendo un elemento dalla coda, se non trovo niente rimango in
        # attesa per 0.1 secondi
        com_error = self.getQueueElementWait(self.error_q, True, 0.1)
        if com_error is not None:
            self.criticalMessage('ComMonitorThread error', com_error)
            self.com_monitor = None
            self.warningMessage('Error', "L'ascolto verra' fermato \
                perche' e' impossibile collegarsi alla porta: " +
                self.portname)
            self.statusBar().showMessage("Error")
        else:
            print "Sono in startListening e sta per partire il monitoraggio"
            self.monitor_active = True
            self.setActionsEnableState()

            self.timer.timeout.connect(self.onTimer)
            ###
            ### Chiedere ad Enrico per la frequenza di aggiornamento
            ###
            # tempo in millisecondi
            self.timer.start(2000)
            self.lastupdateview = time.time()
            self.statusBar().showMessage("Start listening")

    def stopListening(self):
        """
            Stop listening
        """
        print "Sono in stopListening"
        if self.com_monitor is not None:
            self.com_monitor.join(0.01)
            self.com_monitor = None

        self.monitor_active = False
        self.timer.stop()
        self.setActionsEnableState()
        self.statusBar().showMessage("Stop listening")

    def onTimer(self):
        """
            Executed periodically when the monitor update timer
            is fired.
        """
        print "Sono in onTimer"
        com_error = self.getQueueElementNoWait(self.error_q)
        if com_error is not None:
            self.criticalMessage('ComMonitorThread error', com_error)
            reply = QMessageBox.question(
                self,
                'Message',
                "Vuoi fermare l'ascolto?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.stopListening()
        else:
            self.readSerialData()
            self.updateView()

    def updateView(self):
        """
            Updates the state of the monitor window with new
            data. The livefeed is used to find out whether new
            data was received since the last update. If not,
            nothing is updated.
        """
        timetolastupdate = time.time() - self.lastupdateview
        if timetolastupdate < 10:
            if self.livefeed.has_new_data:
                data = self.livefeed.readData()
                if self.radio == 'A':
                    for i in range(self.nantenne):
                        if data['apresent'][i] == '1':
                            self.antenneRX_list[i].setStyleSheet("background-color: red;")
                        if data['apresent'][i+8] == '1':
                            self.antenneTX_list[i].setStyleSheet("background-color: red;")
                    self.presentRX_label.setText(data['apnamerx'])
                    self.presentTX_label.setText(data['apnametx'])
                else:
                    for i in range(self.nantenne):
                        if data['bpresent'][i] == '1':
                            self.antenneRX_list[i].setStyleSheet("background-color: red;")
                        if data['bpresent'][i+8] == '1':
                            self.antenneTX_list[i].setStyleSheet("background-color: red;")
                    self.presentRX_label.setText(data['bpnamerx'])
                    self.presentTX_label.setText(data['bpnametx'])
                for i in range(self.nrelay):
                    if data['relay'][i] == '1':
                        self.relay_list[i].setStyleSheet("background-color: red;")
            self.lastupdateview = time.time()
        else:
            reply = QMessageBox.question(
                self,
                'Message',
                "I dati non sono aggiornati da piu' di 10 secondi,\
                vuoi fermare l'ascolto?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.stopListening()

    def readSerialData(self):
        """
            Called periodically by the update timer to read data
            from the serial port.
        """
        listdata = self.getQueueElementNoWait(self.data_q)
        if listdata is None:
            self.statusBar().showMessage("Non ci sono dati da leggere")
            return
        serialdata = listdata[0]
        timestamp = listdata[1]
        if len(serialdata) > 0:
            n_apresent_active = 0
            n_bpresent_active = 0
            list_element = serialdata.split(';')
            try:
                apresent = list_element[0]
                apnametx = list_element[1]
                apnamerx = list_element[2]
                relay = list_element[3]
                bpresent = list_element[4]
                bpnametx = list_element[5]
                bpnamerx = list_element[6]
                # controllo se i dati ricevuti sono corretti
                for a, b in zip(apresent, bpresent):
                    if a != '0' or a != '1':
                        return
                    if b != '0' or b != '1':
                        return
                    if a == '1':
                        n_apresent_active +=1
                    if b == '1':
                        n_bpresent_active +=1
            except Exception, e:
                print str(e)
            if len(apresent) != len(bpresent):
                return
            if len(apresent) != self.npresent:
                return
            n_apname = len(apnametx.split(',')) + len(apnamerx.split(','))
            if n_apname != n_apresent_active:
                return
            n_bpname = len(bpnametx.split(',')) + len(bpnamerx.split(','))
            if n_bpname != n_bpresent_active:
                return
            for r in relay:
                if r != '0' or r != '1':
                    return
            if len(relay) != self.nrelay:
                return
            # se arrivo qua significa che i dati sono corretti
            data = dict(apresent = apresent,
                        apnametx = apnametx,
                        apnamerx = apnamerx,
                        relay = relay,
                        bpresent = bpresent,
                        bpnametx = bpnametx,
                        bpnamerx = bpnamerx,
                        timestamp = timestamp)
            self.livefeed.addData(data)

    def setActionsEnableState(self):
        if self.portname == '':
            start_enable = stop_enable = False
        else:
            start_enable = not self.monitor_active
            stop_enable = self.monitor_active

        self.start_action.setEnabled(start_enable)
        self.stop_action.setEnabled(stop_enable)

    def getQueueElementWait(self, queue, block, timeout):
        try:
            return queue.get(block, timeout)
        except:
            return None

    def getQueueElementNoWait(self, queue):
        try:
            return queue.get_nowait()
        except:
            return None

    def warningMessage(self, title, message):
        QMessageBox.warning(self, title, message)

    def criticalMessage(self, title, message):
        QMessageBox.critical(self, title, message)

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            'Message',
            "Are you sure to quit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
     # Every PyQt5 application must create an application object.
    app = QApplication(sys.argv)
    view_panel = ViewPanel()
    view_panel.show()
    # l'applicazione rimane in loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()