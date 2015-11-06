import os
import json
import traceback
import time
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import (QDialog, QHBoxLayout, QVBoxLayout, QLabel,
    QComboBox, QPushButton, QProgressBar, QFileDialog, QMessageBox,
    QDesktopWidget)
from PyQt5.QtGui import QFont, QIcon

class DownloadConfigurationPanel(QDialog):
    """docstring for DownloadConfigurationPanel"""
    def __init__(self):
        super(DownloadConfigurationPanel, self).__init__()
        self.portnum = ''
        self.config = ''
        self.initLayout()
        self.initSettingsLayout()

    def initSettingsLayout(self):
        # imposto la grandezza del font
        self.setStyleSheet('font-size: 11pt;')
        self.setWindowIcon(QIcon("icons/download-configuration.png"))
         # imposto il titolo della finestra
        self.setWindowTitle("Download configuration from beaglebone")
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
        self.serials_list = list(serial.tools.list_ports.comports())
        # imposto la porta selezionata con il primo elemento della lista
        self.portnum = self.serials_list[0][0]
        for ser in self.serials_list:
            serials_c.addItem(ser[1])
        serials_c.activated.connect(self.selectSerial)
        serial_layout.addWidget(serials_c)
        serial_layout.addStretch(1)

        bottom_layout =  QHBoxLayout()
        close_btn = QPushButton('Close')
        close_btn.clicked.connect(self.close)
        bottom_layout.addStretch(1)
        bottom_layout.addWidget(close_btn)

        self.progressBar = QProgressBar(self)
        self.progressBar.setRange(0,100)

        main_layout = QVBoxLayout()
        main_layout.addLayout(serial_layout)
        main_layout.addStretch(1)
        download_btn = QPushButton('Start download')
        download_btn.clicked.connect(self.downloadFile)
        main_layout.addWidget(download_btn)
        #main_layout.addWidget(horizontalLine)
        main_layout.addStretch(1)
        main_layout.addWidget(self.progressBar)
        main_layout.addStretch(1)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

    def downloadFile(self):
        #print ("Sono dentro downloadFile")
        if self.portnum:
            try:
                #print ("Sono dentro downloadFile e mi sto per collegare")

                ser = serial.Serial(self.portnum, timeout=3)
                ### TEST
                #ser = serial.Serial("/dev/pts/26", timeout=3)

                ser.write("SENDCFG".encode())
                self.progressBar.setValue(25)
                time.sleep(1)
                data = ser.read().decode()
                waiting = ser.inWaiting()
                if waiting > 0:
                    data += ser.read(waiting).decode()
                    self.progressBar.setValue(50)
                    print (data)
                    edata = data.split("\n")
                    done = False
                    for line in edata:
                        if line[:8] == "CFGJSON:":
                            print ("Carico: "+line[8:])
                            self.config = json.loads(line[8:])
                            self.progressBar.setValue(100)
                            self.informationMessage('Downloaded', 'File downloaded successfully')
                            done = True
                    if done == False:
                        self.progressBar.setValue(0)
                        self.warningMessage('Error', 'No configuration received...')
                else:
                    self.warningMessage('Error', 'Errore nella lettura dalla seriale')
                ser.close()
            except Exception as e:
                self.criticalMessage('Errore', str(e) + str(traceback.format_exc()))
        else:
            self.warningMessage('Error', 'Selezionare una porta')

    def getConfig(self):
        return self.config

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
