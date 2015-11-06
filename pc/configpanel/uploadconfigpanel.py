import os
import json
import serial
import time
from serial.tools import list_ports
from PyQt5.QtWidgets import (QDialog, QHBoxLayout, QVBoxLayout, QLabel,
    QComboBox, QPushButton, QProgressBar, QFileDialog, QMessageBox,
    QDesktopWidget)
from PyQt5.QtGui import QFont, QIcon

class UploadConfigurationPanel(QDialog):
    """docstring for UploadConfigurationPanel"""
    def __init__(self):
        super(UploadConfigurationPanel, self).__init__()
        self.portnum = ''
        self.configuration = ''
        self.initLayout()
        self.initSettingsLayout()

    def initSettingsLayout(self):
        # imposto la grandezza del font
        self.setStyleSheet('font-size: 11pt;')
        self.setWindowIcon(QIcon("icons/upload-configuration.png"))
         # imposto il titolo della finestra
        self.setWindowTitle("Upload configuration to beaglebone")
        # imposto le dimensioni della finestra
        self.setGeometry(0, 0, 350, 200)
        # sposta la finestra al centro del desktop
        self.centerOnScreen()

    def initLayout(self):
        boldfont = QFont()
        boldfont.setBold(True)
        serial_layout = QHBoxLayout()
        serial_lbl = QLabel('COM Port:')
        serial_lbl.setFont(boldfont)
        serial_layout.addWidget(serial_lbl)
        serials_c = QComboBox(self)
        self.serials_list = list(list_ports.comports())
        # imposto la porta selezionata con il primo elemento della lista
        self.portnum = self.serials_list[0][0]
        for ser in self.serials_list:
            serials_c.addItem(ser[1])
        serials_c.activated.connect(self.selectSerial)
        serial_layout.addWidget(serials_c)
        serial_layout.addStretch(1)

        selectfile_layout = QHBoxLayout()
        selectfile_btn = QPushButton('Select file')
        selectfile_btn.clicked.connect(self.selectFile)
        selectfile_layout.addWidget(selectfile_btn)
        file_lbl = QLabel('File:')
        file_lbl.setFont(boldfont)
        selectfile_layout.addWidget(file_lbl)
        self.selectfile_lbl = QLabel('Nessun file selezionato')

        selectfile_layout.addWidget(self.selectfile_lbl)
        selectfile_layout.addStretch(1)

        bottom_layout =  QHBoxLayout()
        self.upload_btn = QPushButton('Upload')
        self.upload_btn.clicked.connect(self.uploadFile)
        self.upload_btn.setEnabled(False)
        close_btn = QPushButton('Close')
        close_btn.clicked.connect(self.close)
        bottom_layout.addWidget(self.upload_btn)
        bottom_layout.addStretch(1)
        bottom_layout.addWidget(close_btn)

        self.progressBar = QProgressBar(self)
        self.progressBar.setRange(0,100)

        main_layout = QVBoxLayout()
        main_layout.addLayout(serial_layout)
        main_layout.addLayout(selectfile_layout)
        #main_layout.addWidget(horizontalLine)
        main_layout.addStretch(1)
        main_layout.addWidget(self.progressBar)
        main_layout.addStretch(1)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

        self.loadFile("current.json")

    def selectFile(self):
        """
        apre una finestra di selezione in /home dove e' possibile selezionare solo file json
        prendo il primo elemento, cioe' 0 perche' getOpenFileName mi restituisce
        una lista del tipo (u'/home/giulio/workspace/amc/test-config.json',
        u'JSON Files (*.json)')
        """
        fname = QFileDialog.getOpenFileName(self, 'Select configuration',
                    os.getcwd(), "JSON Files (*.json)")[0]
        self.loadFile(fname)

    def loadFile(self, fname):
        if fname:
            #print (fname)
            try:
                name = os.path.split(fname)[-1]
                self.selectfile_lbl.setText(name)
                with open(fname, 'r') as fin:
                    self.configuration = json.dumps(json.load(fin))
                #print (json.dumps(self.configuration))
                fin.close()
                if self.portnum:
                    # Abilito il pulsante per mandare il file
                    self.upload_btn.setEnabled(True)
            except Exception as e:
                self.warningMessage(self, 'Errore', str(e))

    def uploadFile(self):
        #print ("Sono dentro uploadFile")
        if self.configuration and self.portnum:
            try:
                #print ("Sono dentro uploadFile e mi sto per collegare")

                ser = serial.Serial(self.portnum, timeout=3)
                ### TEST
                #ser = serial.Serial("/dev/pts/25", timeout=3)

                ser.write(bytearray(self.configuration, 'utf-8'))
                ser.flush()
                self.progressBar.setValue(25)
                time.sleep(0.5)
                self.progressBar.setValue(50)
                data = ser.read()
                waiting = ser.inWaiting()
                if waiting > 0:
                    data += ser.read(waiting)
                    if 'CFGACK' in str(data):
                        self.progressBar.setValue(100)
                        self.informationMessage('Uploaded', 'File uploaded successfully')
                    else:
                        self.warningMessage('Error', 'Errore nella ricezione del CFGACK'+str(data))
                else:
                    self.warningMessage('Error', 'Errore nella lettura dalla seriale')
                ser.close()
            except Exception as e:
                self.criticalMessage('Errore', str(e))
        else:
            self.warningMessage('Error', 'Selezionare una porta ed un file')

    def centerOnScreen(self):
        """
            Centers the window on the screen.
        """
        # prende le dimensioni della finestra
        qr = self.frameGeometry()
        # prende il punto centrale del display date le sue dimensioni
        cp = QDesktopWidget().availableGeometry().center()
        # muoviamo la finestra al centro dello schermo
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def selectSerial(self, i):
        self.portnum = self.serials_list[i][0]

    def informationMessage(self, title, message):
        QMessageBox.information(self, title, message)

    def warningMessage(self, title, message):
        QMessageBox.warning(self, title, message)

    def criticalMessage(self, title, message):
        QMessageBox.critical(self, title, message)