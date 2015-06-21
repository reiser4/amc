import sys, os, json
from PyQt5.QtWidgets import (QWidget,QApplication, QDesktopWidget, QPushButton,
    QMessageBox, QMainWindow, QAction, qApp, QTextEdit, QLCDNumber, QSlider, QVBoxLayout,
    QGridLayout, QTabWidget, QFileDialog, QCheckBox, QLabel, QLineEdit, QAbstractButton)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import QCoreApplication, Qt
from atomicwrite import AtomicWrite

'''
Riga 0:     Active(0,0)  Label(0,1)   Radio1(0,2+25)  Radio2(0,27+25)
Riga 1-16:
'''

# grid = [[" " for x in range(5)] for y in range(5)]
class ConfigurationPanel(QMainWindow):

    def __init__(self):
        super(ConfigurationPanel, self).__init__()
        self.initUI()

    def initUI(self):
        self.bands = ["6m", "10m", "12m", "15m", "17m", "20m", "30m", "40m", "60m", "80m", "160m"]
        self.nrow = 16
        self.nrele = 24
        # imposto le dimensioni della finestra
        self.setGeometry(0, 0, 1500, 600)
        # imposto il titolo della finestra
        self.setWindowTitle("AMC Configuration Panel")
        # sposta la finestra al centro del desktop
        self.centerOnScreen()

        # creo le azioni che usero' in seguito
        self.initAction()
        # creo il menu'
        self.initMenuBar()
        # creo le tab ed il loro contenuto
        self.initTab()

        # imposta il widget dato come widget centrale della finestra principale
        self.setCentralWidget(self.tab_widget)
        # visualizzo il widget
        self.show()
        # visualizzo la scritta 'Ready' nella status bar
        self.statusBar().showMessage("Ready")

    def initAction(self):
        # azione per uscire dall'applicazione
        self.exitAction = QAction(QIcon("icons/exit.png"), "&Exit", self)
        self.exitAction.setShortcut("Ctrl+Q")
        self.exitAction.setStatusTip("Exit application")
        # collego l'azione exitAction all'evento self.close (gia' presente in PyQT)
        self.exitAction.triggered.connect(self.close)

        # azione per caricare la configurazione da file
        self.openAction = QAction("&Load to file", self)
        self.openAction.setShortcut("Ctrl+L")
        self.openAction.setStatusTip("Load to file")
        # collego l'azione openAction al mio evento che ho creato loadConfiguration
        self.openAction.triggered.connect(self.loadConfiguration)

        # azione per salvare la configurazione su file
        self.saveAction = QAction("&Save on file", self)
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.setStatusTip("Save to file")
        self.saveAction.triggered.connect(self.saveConfiguration)

        """
        serialAction = QAction("&Serial", self)
        serialAction.setShortcut("")
        serialAction.setStatusTip("")
        serialAction.triggered.connect()

        downloadAction = QAction("&Download", self)
        downloadAction.setShortcut("")
        downloadAction.setStatusTip("")
        downloadAction.triggered.connect()

        UploadAction = QAction("&Upload", self)
        UploadAction.setShortcut("")
        UploadAction.setStatusTip("")
        UploadAction.triggered.connect()
        """


    def initMenuBar(self):
        # creo il menu ed aggiungo i vari campi
        menubar = self.menuBar()
        filemenu = menubar.addMenu("&File")
        #filemenu.addSeparator()
        # aggancio al menu il comando per uscire
        filemenu.addAction(self.exitAction)

        configuration_menu = menubar.addMenu("&Configuration")
        configuration_menu.addAction(self.saveAction)
        configuration_menu.addAction(self.openAction)
        #connection_menu = menubar.addMenu("&Connection")

    def initTab(self):
        # creo un TabWidget che sara' il widget padre
        self.tab_widget = QTabWidget(self)
        labels_name = ["Active", "Label", "Bands"]
        tab_list = list()
        self.tablayout_list = list()
        self.checkbox_matrix = list()
        self.labels_matrix = list()
        self.radio1cb_matrix = list()
        self.radio2cb_matrix = list()
        for i in range(len(self.bands)):
            # aggiungo alla lista un oggetto QWidget discendente dal padre
            tab_list.append(QWidget(self.tab_widget))
            # per ogni nome band aggiungo una tab nella list che
            # sara' visualizzata nella finestra principale
            self.tab_widget.addTab(tab_list[i], self.bands[i])
            # aggiungo alla lista un oggetto per il layout a griglia discendente
            # dalla i-esima tab
            self.tablayout_list.append(QGridLayout(tab_list[i]))
            self.tablayout_list[i].setObjectName("tab" + str(i).zfill(2))
            #print self.tablayout_list[i].objectName()
            # nella i-esima tab creo un layout a griglia e posiziono i vari elementi
            self.tablayout_list[i].addWidget(QLabel("Active", tab_list[i]), 0, 0)
            self.tablayout_list[i].addWidget(QLabel("Label", tab_list[i]), 0, 1)
            self.tablayout_list[i].addWidget(QLabel("Radio 1", tab_list[i]), 0, 2, 1, self.nrele)
            self.tablayout_list[i].addWidget(QLabel("Radio 2", tab_list[i]), 0, 26, 1, self.nrele)
            self.checkbox_matrix.append(list())
            self.labels_matrix.append(list())
            self.radio1cb_matrix.append(list())
            self.radio2cb_matrix.append(list())
            # per ogni tab devo creare tutti i suoi oggetti al suo interno
            for y in range(self.nrow):
                self.checkbox_matrix[i].append(QCheckBox(tab_list[i]))
                self.checkbox_matrix[i][y].setObjectName("checkboxRowTab" + str(i).zfill(2))
                self.checkbox_matrix[i][y].setCheckState(Qt.Unchecked)
                self.checkbox_matrix[i][y].stateChanged.connect(self.changeStateRow)
                self.tablayout_list[i].addWidget(self.checkbox_matrix[i][y], y+1, 0)
                self.labels_matrix[i].append(QLineEdit(tab_list[i]))
                self.labels_matrix[i][y].setEnabled(False)
                self.tablayout_list[i].addWidget(self.labels_matrix[i][y], y+1, 1)
                self.radio1cb_matrix[i].append(list())
                self.radio2cb_matrix[i].append(list())
                for z in range(self.nrele):
                    self.radio1cb_matrix[i][y].append(QCheckBox(tab_list[i]))
                    #self.radio1cb_matrix[i][y][z].stateChanged.connect(self.changeCheckBoxState)
                    self.radio1cb_matrix[i][y][z].setEnabled(False)
                    # aggiungo 1 a y perche' devo contare le etichette (Active, Label, Radio1, Radio2)
                    # aggiungo 2 a z perche' devo tenere conto dei widget di sinistra (checkbox e label)
                    self.tablayout_list[i].addWidget(self.radio1cb_matrix[i][y][z], y+1, z+2)

                    self.radio2cb_matrix[i][y].append(QCheckBox(tab_list[i]))
                    #self.radio2cb_matrix[i][y][z].stateChanged.connect(self.changeCheckBoxState)
                    self.radio2cb_matrix[i][y][z].setEnabled(False)
                    # aggiungo 1 a y perche' devo contare le etichette (Active, Label, Radio1, Radio2)
                    # aggiungo 2 a z perche' devo tenere conto dei widget di sinistra (checkbox, label e 24 checkbox)
                    self.tablayout_list[i].addWidget(self.radio2cb_matrix[i][y][z], y+1, z+26)


    def centerOnScreen(self):
        '''
        Centers the window on the screen.
        '''
        # prende le dimensioni della finestra
        qr = self.frameGeometry()
        # prende il punto centrale del display date le sue dimensioni
        cp = QDesktopWidget().availableGeometry().center()
        # muoviamo la finestra al centro dello schermo
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def changeStateRow(self, state):
        if state == Qt.Checked or state == Qt.Unchecked:
            sender = self.sender()
            '''
            Trovare un modo migliore per trovare la posizione dell'oggetto
            che effettua la richiesta perche' questo fa schifo!!!!
            '''
            #print "Sender: ", sender.objectName()
            # Recupero l'indice della tab dove si trova la checkbox attraverso il nome
            indexTab = int(sender.objectName()[-2:])
            #print "indexTab: ", indexTab
            indexPos = self.tablayout_list[indexTab].indexOf(sender)
            #print "indexPos:", indexPos
            location = self.tablayout_list[indexTab].getItemPosition(indexPos)
            indexRow = location[0]
            indexColumn = location[1]
            text = "Tab: " + self.bands[indexTab] + ", Row: " + str(indexColumn) + ", Column: " + str(indexRow) + ", State: " + str(state)
            #print text
            self.statusBar().showMessage(text)
            if state == Qt.Checked:
                self.labels_matrix[indexTab][indexRow-1].setEnabled(True)
                for i in range(self.nrele):
                    # -1 perche' e' compresa la riga delle etichette
                    self.radio1cb_matrix[indexTab][indexRow-1][i].setEnabled(True)
                    self.radio2cb_matrix[indexTab][indexRow-1][i].setEnabled(True)
            else:
                self.labels_matrix[indexTab][indexRow-1].setEnabled(False)
                for i in range(self.nrele):
                    self.radio1cb_matrix[indexTab][indexRow-1][i].setEnabled(False)
                    self.radio2cb_matrix[indexTab][indexRow-1][i].setEnabled(False)

    def changeCheckBoxState(self, state):
        '''
        Funzione che stampa a terminale tutte le volte che viene cliccata
        una checkbox
        '''
        if state == Qt.Checked or state == Qt.Unchecked:
        #if True:
            sender = self.sender()
            #self.statusBar().showMessage(sender.text())
            indexTab = self.tab_widget.currentIndex()
            """
            button = self.sender()
            idx = self.layout.indexOf(button)
            location = self.layout.getItemPosition(idx)
            print "Button", button, "at row/col", location[:2]
            """
            idx = self.tablayout_list[indexTab].indexOf(sender)
            location = self.tablayout_list[indexTab].getItemPosition(idx)
            indexRow = location[0]
            indexColumn = location[1]
            '''
            print "indexTab: ", indexTab
            print "idx:", idx
            text = "Tab: " + str(indexTab) + ", Row: " + str(indexColumn) + ", Column: " + str(indexRow) + ", State: " + str(state)
            print text
            self.statusBar().showMessage(text)
            '''
            #trovo la banda
            band = self.bands[indexTab]
            presetnumber = indexRow
            if indexColumn > 1 and indexColumn < 26:
                ptype = "radioA, relay " + str(location[1]-1)
            else:
                # -25 perche' sarebbe -26 (numero oggetti) + 1 (perche' non voglio partire da 0 ma da 1)
                ptype = "radioB, relay " + str(location[1]-25) # attenzione alla "label"
            print "Posizione decodificata: banda ", band, ", preset numero ", presetnumber, ", tipo ", ptype

    def saveConfiguration(self):
        tmpwrite = '{"relayconfig":{\n'
        commaTab = False
        for indexTab in range(len(self.bands)):
            firstRow = True
            nRowChecked = 0
            for indexRow in range(self.nrow):
                if self.checkbox_matrix[indexTab][indexRow].isChecked() == True:
                    nRowChecked += 1
                    if firstRow:
                        if commaTab:
                            # inserisco una virgola per ogni tab a parte l'ultima
                            tmpwrite += ',\n'
                            commaTab = False
                        tmpwrite += '\t"' + self.bands[indexTab] + '":{\n'
                        firstRow = False
                        commaTab = True
                    else:
                        tmpwrite += ',\n'
                    tmpwrite += '\t\t"' + str(indexRow) + '":{\n\t\t\t"label":' + '"' + self.labels_matrix[indexTab][indexRow].text() + '",\n'
                    relayA = ""
                    relayB = ""
                    for z in range(self.nrele):
                        if self.radio1cb_matrix[indexTab][indexRow][z].isChecked() == True:
                            relayA += "1"
                        else:
                            relayA += "0"
                        if self.radio2cb_matrix[indexTab][indexRow][z].isChecked() == True:
                            relayB += "1"
                        else:
                            relayB += "0"
                    tmpwrite += '\t\t\t"relayA":' + '"' + relayA + '",\n\t\t\t"relayB":' + '"' + relayB + '"\n\t\t}'
            if nRowChecked > 0:
                # chiudo parentesi prima di label
                tmpwrite += '\n\t}'
        tmpwrite += '\n}}'
        AtomicWrite.writeFile("test-config.json", tmpwrite)
        print "Scrittura eseguita correttamente su file"

    def loadConfiguration(self):
        # apre una finestra di selezione in /home dove e' possibile selezionare solo file py
        fname = QFileDialog.getOpenFileName(self, 'Load file', os.getcwd(), "JSON Files (*.json)")
        print(fname[0])
        with open(fname[0], 'r') as fin:
            configuration = json.load(fin)
        #print configuration
        fin.close()
        for indexTab in range(len(self.bands)):
            for indexRow in range(self.nrow):
                if self.checkbox_matrix[indexTab][indexRow].isChecked() == True:
                    self.checkbox_matrix[indexTab][indexRow].setCheckState(Qt.Unchecked)
        for tab in configuration['relayconfig']:
            for row in configuration['relayconfig'][tab]:
                #print tab + "-" + row
                label = configuration['relayconfig'][tab][row]['label']
                relayA = configuration['relayconfig'][tab][row]['relayA']
                relayB = configuration['relayconfig'][tab][row]['relayB']
                #print label + relayA + relayB
                #self.checkbox_matrix[self.bands.index(tab)][int(row)].checkStateSet()
                self.checkbox_matrix[self.bands.index(tab)][int(row)].setCheckState(Qt.Checked)
                #self.labels_matrix[self.bands.index(tab)][int(row)].setEnabled(True)
                self.labels_matrix[self.bands.index(tab)][int(row)].setText(label)
                for i in range(self.nrele):
                    # +1 perche' non e' compresa la riga delle etichette
                    #self.radio1cb_matrix[self.bands.index(tab)][int(row)][i].setEnabled(True)
                    if relayA[i] == '1':
                        self.radio1cb_matrix[self.bands.index(tab)][int(row)][i].setCheckState(Qt.Checked)
                    #self.radio2cb_matrix[self.bands.index(tab)][int(row)][i].setEnabled(True)
                    if relayB[i] == '1':
                        self.radio2cb_matrix[self.bands.index(tab)][int(row)][i].setCheckState(Qt.Checked)


if __name__ == '__main__':
    # Every PyQt5 application must create an application object.
    app = QApplication(sys.argv)
    configuration_panel = ConfigurationPanel()
    configuration_panel.show()
    # l'applicazione rimane in loop
    sys.exit(app.exec_())
