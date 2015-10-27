import sys, time, os.path, queue
import serial.tools.list_ports
from com_monitor import ComMonitorThread
from livedatafeed import LiveDataFeed
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QHBoxLayout,
    QVBoxLayout, QGridLayout, QComboBox, QLabel, QRadioButton, QButtonGroup,
    QGroupBox, QWidget, QDesktopWidget, QMessageBox)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QTimer

class ViewPanel(QMainWindow):
    def __init__(self):
        super(ViewPanel, self).__init__()
        # imposto la grandezza del font
        self.setStyleSheet('font-size: 11pt;')
        # all'avvio del programma e' selezionata la radio A
        self.radio = "A"
        self.portnum = ""
        self.nantenne = 8
        self.nrelay = 24
        # indica se sono in ascolto o no
        self.monitor_active = False
        # variabile per il thread di ascolto
        self.com_monitor = None
        # indica l'ultimo aggiornamento della view
        self.lastupdatedata = None
        # varibile per avere i dati piu' recenti
        self.livefeed = LiveDataFeed()
        # code per i dati e per gli errori
        self.data_q = queue.LifoQueue()
        self.error_q = queue.Queue()
        # conto alla rovescia
        self.timer = QTimer()
        self.initAction()
        # inizializzo la toolbar
        self.initToolBar()
        self.radio_groupbox_defaultStyleSheet = None
        #self.radioTX_groupbox_defaultStyleSheet = None
        self.antenne_defaultStyleSheet = None
        # creo gli elementi della finistra
        self.initLayout()
        self.initSettingsLayout()
        self.setActionsEnableState()

        ### TEST
        #self.portnum = "/dev/pts/26"
        #self.start_action.setEnabled(True)

    def initAction(self):
        # azione per uscire dall'applicazione
        self.exit_action = QAction(
            QIcon(os.path.join("icons", "exit.png")),
            "&Exit",
            self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.setStatusTip("Exit application")
        # collego l'azione exit_action all'evento self.close (gia' presete in PyQT)
        self.exit_action.triggered.connect(self.close)

        self.start_action = QAction(
            QIcon(os.path.join("icons", "start.png")),
            "&Start",
            self)
        self.start_action.setShortcut("Ctrl+S")
        self.start_action.setStatusTip("Start listening")
        self.start_action.triggered.connect(self.startListening)

        self.stop_action = QAction(
            QIcon(os.path.join("icons", "stop.png")),
            "&Stop",
            self)
        self.stop_action.setShortcut("Ctrl+B")
        self.stop_action.setStatusTip("Stop listening")
        self.stop_action.triggered.connect(self.stopListening)

    def initToolBar(self):
        toolbar = self.addToolBar('ToolBar')
        toolbar.addAction(self.start_action)
        toolbar.addSeparator()
        toolbar.addAction(self.stop_action)

    def initSettingsLayout(self):
         # imposto il titolo della finestra
        self.setWindowTitle("RadioA")
        #self.setGeometry(0, 0, 600, 600)
        # sposta la finestra al centro del desktop
        self.centerOnScreen()
        # visualizzo la scritta 'Ready' nella status bar
        self.statusBar().showMessage("Ready")
        # impongo che la finestra sia sempre in primo piano
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def initLayout(self):
        boldfont = QFont()
        boldfont.setBold(True)
        settings_layout = QHBoxLayout()
        settings_layout.addStretch(2)
        com_lbl = QLabel('COM Port:')
        com_lbl.setFont(boldfont)
        settings_layout.addWidget(com_lbl)
        com_c = QComboBox(self)
        self.com_list = list(serial.tools.list_ports.comports())
        # imposto la porta selezionata con il primo elemento della lista
        self.portnum = self.com_list[0][0]
        for ser in self.com_list:
            com_c.addItem(ser[1])
        com_c.activated.connect(self.selectCom)
        settings_layout.addWidget(com_c)
        settings_layout.addStretch(1)
        radio_lbl = QLabel('Radio:')
        radio_lbl.setFont(boldfont)
        settings_layout.addWidget(radio_lbl)
        radioA = QRadioButton("A")
        radioA.setChecked(True)
        radioB = QRadioButton("B")
        self.radio_group = QButtonGroup()
        self.radio_group.addButton(radioA, 0)
        self.radio_group.addButton(radioB, 1)
        self.radio_group.buttonClicked.connect(self.selectRadio)
        settings_layout.addWidget(radioA)
        settings_layout.addWidget(radioB)

        antenneRX_lbl = QLabel('Antenne:')
        self.antenne_defaultStyleSheet = antenneRX_lbl.styleSheet()
        antenneRX_lbl.setFont(boldfont)
        presetRX_lbl = QLabel('preset:')
        presetRX_lbl.setFont(boldfont)
        self.antenneRX_list = list()
        radioRX_layout = QGridLayout()
        radioRX_layout.addWidget(antenneRX_lbl, 0, 0)
        for i in range(self.nantenne):
            self.antenneRX_list.append(QLabel(str(i+1)))
            radioRX_layout.addWidget(self.antenneRX_list[i], 0, i+1)
        radioRX_layout.addWidget(presetRX_lbl, 1, 0)
        self.presetRX_label = QLabel()
        #self.presetRX_label.setText("################")
        radioRX_layout.addWidget(self.presetRX_label, 1, 1, 1, self.nantenne)
        self.radioRX_groupbox = QGroupBox('RX')
        self.radioRX_groupbox.setLayout(radioRX_layout)
        #self.radioRX_groupbox.setStyleSheet("background-color: white;")
        self.radio_groupbox_defaultStyleSheet = self.radioRX_groupbox.styleSheet()

        antenneTX_lbl = QLabel('Antenne:')
        antenneTX_lbl.setFont(boldfont)
        presetTX_lbl = QLabel('Preset:')
        presetTX_lbl.setFont(boldfont)
        self.antenneTX_list = list()
        radioTX_layout = QGridLayout()
        radioTX_layout.addWidget(antenneTX_lbl, 0, 0)
        for i in range(self.nantenne):
            # +9 perche' l'indice visualizzato parte 9 e non da 0
            self.antenneTX_list.append(QLabel(str(i+9)))
            radioTX_layout.addWidget(self.antenneTX_list[i], 0, i+1)
        radioTX_layout.addWidget(presetTX_lbl, 1, 0)
        self.presetTX_label = QLabel()
        radioTX_layout.addWidget(self.presetTX_label, 1, 1, 1, self.nantenne)
        self.radioTX_groupbox = QGroupBox('TX')
        self.radioTX_groupbox.setLayout(radioTX_layout)
        #self.radio_groupbox_defaultStyleSheet = self.radioTX_groupbox.styleSheet()
        #self.radioTX_groupbox.setStyleSheet("QGroupBox { border: black; }")

        central_layout = QHBoxLayout()
        central_layout.addWidget(self.radioRX_groupbox)
        central_layout.addWidget(self.radioTX_groupbox)

        bottom_layout = QHBoxLayout()
        relay_lbl = QLabel('Relay:')
        relay_lbl.setFont(boldfont)
        bottom_layout.addWidget(relay_lbl)
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

    def selectCom(self, i):
        #print self.com_list[i]
        self.portnum = self.com_list[i][0]
        #print self.portnum
        self.statusBar().showMessage("Selected COM port: " + self.portnum)
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
            Start the listening: ComMonitorThread thread and the update timer
        """

        ### TEST
        #self.portnum = "/dev/pts/27"

        if self.com_monitor is not None or self.portnum == '':
            return
        ###
        ### Chiedere ad Enrico per il timeout
        ###
        self.com_monitor = ComMonitorThread(
            data_q=self.data_q,
            error_q=self.error_q,
            port_num=self.portnum,
            port_timeout=5)
        self.com_monitor.start()
        # prendo un elemento dalla coda, se non trovo niente rimango in
        # attesa per 0.1 secondi
        com_error = self.getQueueElementWait(self.error_q, True, 0.1)
        if com_error is not None:
            self.criticalMessage('ComMonitorThread error', com_error)
            self.com_monitor = None
            self.warningMessage('Error', "L'ascolto verra' fermato" +
                " perche' impossibile collegarsi alla porta: " + self.portnum)
            self.statusBar().showMessage("Error")
        else:
            #print "Sono in startListening e sta per partire il " +
            #    "monitoraggio sulla porta: " + self.portnum
            self.monitor_active = True
            self.setActionsEnableState()

            self.timer.timeout.connect(self.onTimer)
            ###
            ### Chiedere ad Enrico per la frequenza di aggiornamento
            ###
            # tempo in millisecondi
            self.timer.start(2000)
            self.statusBar().showMessage("Start listening")

    def stopListening(self):
        """
            Stop listening
        """
        #print "Sono in stopListening"
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
        #print "Sono in onTimer"
        com_error = self.getQueueElementNoWait(self.error_q)
        if com_error is not None:
            self.criticalMessage('ComMonitorThread error', com_error)
            reply = QMessageBox.question(
                self,
                'Message',
                "Vuoi fermare l'ascolto?",
                QMessageBox.No | QMessageBox.Yes,
                QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.stopListening()
        else:
            self.readComData()
            self.updateView()

    def updateView(self):
        """
            Updates the state of the monitor window with new
            data. The livefeed is used to find out whether new
            data was received since the last update. If not,
            nothing is updated.
        """
        #print "Sono in updateView"
        if self.livefeed.has_new_data:
            #print "Sto per leggere i dati"
            data = self.livefeed.readData()
            if self.radio == 'A':
                #print "Sono dentro radio A"
                for i in range(self.nantenne):
                    if data['apreset'][i] == '1':
                        self.antenneRX_list[i].setStyleSheet("background-color: red;")
                    else:
                        self.antenneRX_list[i].setStyleSheet(self.antenne_defaultStyleSheet)
                    if data['apreset'][i+8] == '1':
                        self.antenneTX_list[i].setStyleSheet("background-color: red;")
                    else:
                        self.antenneTX_list[i].setStyleSheet(self.antenne_defaultStyleSheet)
                self.presetRX_label.setText(data['apnamerx'])
                self.presetTX_label.setText(data['apnametx'])
                if data['atx'] == '0':
                    self.radioRX_groupbox.setStyleSheet("QGroupBox { background-color: yellow; }")
                    self.radioTX_groupbox.setStyleSheet(self.radio_groupbox_defaultStyleSheet)
                else:
                    self.radioRX_groupbox.setStyleSheet(self.radio_groupbox_defaultStyleSheet)
                    self.radioTX_groupbox.setStyleSheet("QGroupBox { background-color: yellow; }")
            else:
                #print "Sono dentro radio B"
                for i in range(self.nantenne):
                    if data['bpreset'][i] == '1':
                        self.antenneRX_list[i].setStyleSheet("background-color: red;")
                    else:
                        self.antenneRX_list[i].setStyleSheet(self.antenne_defaultStyleSheet)
                    if data['bpreset'][i+8] == '1':
                        self.antenneRX_list[i].setStyleSheet("background-color: red;")
                    else:
                        self.antenneTX_list[i].setStyleSheet(self.antenne_defaultStyleSheet)
                self.presetRX_label.setText(data['bpnamerx'])
                self.presetTX_label.setText(data['bpnametx'])
                if data['btx'] == '0':
                    self.radioRX_groupbox.setStyleSheet("QGroupBox { background-color: yellow; }")
                    self.radioTX_groupbox.setStyleSheet(self.radio_groupbox_defaultStyleSheet)
                else:
                    self.radioRX_groupbox.setStyleSheet(self.radio_groupbox_defaultStyleSheet)
                    self.radioTX_groupbox.setStyleSheet("QGroupBox { background-color: yellow; }")
            for i in range(self.nrelay):
                if data['relay'][i] == '1':
                    self.relay_list[i].setStyleSheet("background-color: red;")
                else:
                    self.relay_list[i].setStyleSheet(self.antenne_defaultStyleSheet)
            self.lastupdatedata = time.time()
        if self.lastupdatedata:
            timetolastupdate = time.time() - self.livefeed.readTimestamp()
            self.statusBar().showMessage("Dati ricevuti " + str(int(timetolastupdate)) + " secondi fa")
        else:
            self.statusBar().showMessage("Non ci sono dati da leggere")
        """
        reply = QMessageBox.question(
            self,
            'Message',
            "I dati non sono aggiornati da piu' di 10 secondi,\
            vuoi fermare l'ascolto?",
            QMessageBox.No | QMessageBox.Yes,
            QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.stopListening()
        """

    def readComData(self):
        """
            Called periodically by the update timer to read data
            from the COM port.
        """
        #print "Sono in readComData"
        #listdata = self.getQueueElementWait(self.data_q, True, 0.1)
        listdata = self.getQueueElementNoWait(self.data_q)
        #print "listdata", listdata
        if listdata is None:
            #print "Esco da readComData"
            return
        #print "Dati che saranno inseriti: ", listdata[0]
        #print "Timestamp: " + str(listdata[1])
        self.livefeed.addData(listdata[0], listdata[1])

    def setActionsEnableState(self):
        if self.portnum == '':
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
            self, 'Message',
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