import sys
from PyQt5.QtWidgets import (QWidget,QApplication, QDesktopWidget, QPushButton,
    QMessageBox, QMainWindow, QAction, qApp, QTextEdit, QLCDNumber, QSlider, QVBoxLayout,
    QGridLayout, QTabWidget, QFileDialog, QCheckBox, QLabel, QLineEdit)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import QCoreApplication, Qt

# grid = [[" " for x in range(5)] for y in range(5)]
class ConfigurationPanel(QMainWindow):

    def __init__(self):
        super(ConfigurationPanel, self).__init__()
        self.initUI()

    def initUI(self):
        self.bands = ["6m", "10m", "12m", "15m", "17m", "20m", "40m", "80m", "160m"]
        self.setGeometry(0, 0, 1500, 600)
        self.setWindowTitle("Configuration Panel")
        self.centerOnScreen()

        self.initAction()
        self.initMenuBar()
        self.initTab()


        self.setCentralWidget(self.tab_widget)
        self.show()
        self.statusBar().showMessage("Ready")

    def initAction(self):
        # creo l'azione per uscire
        self.exitAction = QAction(QIcon("icons/exit.png"), "&Exit", self)
        self.exitAction.setShortcut("Ctrl+Q")
        self.exitAction.setStatusTip("Exit application")
        self.exitAction.triggered.connect(self.close)
        # azione per caricare il file
        self.openAction = QAction("&Load to file", self)
        self.openAction.setShortcut("Ctrl+L")
        self.openAction.setStatusTip("Load to file")
        self.openAction.triggered.connect(self.showDialog)
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

        saveAction = QAction("&Save on file", self)
        saveAction.setShortcut("")
        saveAction.setStatusTip("")
        saveAction.triggered.connect()
        """


    def initMenuBar(self):
        # creo il menu ed aggiungo i vari campi
        menubar = self.menuBar()
        filemenu = menubar.addMenu("&File")
        filemenu.addSeparator()
        # aggancio al menu il comando per uscire
        filemenu.addAction(self.exitAction)

        configuration_menu = menubar.addMenu("&Configuration")
        configuration_menu.addAction(self.openAction)
        connection_menu = menubar.addMenu("&Connection")

    def initTab(self):
        self.tab_widget = QTabWidget(self)
        labels_name = ["Active", "Label", "Bands"]
        tab_list = list()
        self.tablayout_list = list()
        checkbox_matrix = list()
        labels_matrix = list()
        radio1cb_matrix = list()
        radio2cb_matrix = list()
        for i in range(len(self.bands)):
            tab_list.append(QWidget(self.tab_widget))
            self.tab_widget.addTab(tab_list[i], self.bands[i])
            self.tablayout_list.append(QGridLayout(tab_list[i]))
            self.tablayout_list[i].addWidget(QLabel("Active", tab_list[i]), 0, 0)
            self.tablayout_list[i].addWidget(QLabel("Label", tab_list[i]), 0, 1)
            self.tablayout_list[i].addWidget(QLabel("Radio 1", tab_list[i]), 0, 2, 1, 25)
            self.tablayout_list[i].addWidget(QLabel("Radio 2", tab_list[i]), 0, 27, 1, 25)
            checkbox_matrix.append(list())
            labels_matrix.append(list())
            radio1cb_matrix.append(list())
            radio2cb_matrix.append(list())
            for y in range(16):
                checkbox_matrix[i].append(QCheckBox(tab_list[i]))
                checkbox_matrix[i][y].stateChanged.connect(self.changeCheckBoxState)
                self.tablayout_list[i].addWidget(checkbox_matrix[i][y], y+1, 0)
                labels_matrix[i].append(QLineEdit(tab_list[i]))
                self.tablayout_list[i].addWidget(labels_matrix[i][y], y+1, 1)
                radio1cb_matrix[i].append(list())
                radio2cb_matrix[i].append(list())
                for z in range(24):
                    radio1cb_matrix[i][y].append(QCheckBox(tab_list[i]))
                    radio1cb_matrix[i][y][z].stateChanged.connect(self.changeCheckBoxState)
                    self.tablayout_list[i].addWidget(radio1cb_matrix[i][y][z], y+1, z+2)
                for z in range(24):
                    radio2cb_matrix[i][y].append(QCheckBox(tab_list[i]))
                    radio2cb_matrix[i][y][z].stateChanged.connect(self.changeCheckBoxState)
                    self.tablayout_list[i].addWidget(radio2cb_matrix[i][y][z], y+1, z+27)



    def centerOnScreen(self):
        '''
        Centers the window on the screen.
        '''
        # prende le dimesioni della finestra
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

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Load file', '/home', "Python Files (*.py)")
        print fname[0]
        f = open(fname[0], 'r')
        with f:
            data = f.read()
            print data
        f.close()

    def changeCheckBoxState(self, state):
        if state == Qt.Checked:
            sender = self.sender()
            self.statusBar().showMessage(sender.text())
            currentIndex = self.tab_widget.currentIndex()
            """
            button = self.sender()
            idx = self.layout.indexOf(button)
            location = self.layout.getItemPosition(idx)
            print "Button", button, "at row/col", location[:2]
            """
            idx = self.tablayout_list[currentIndex].indexOf(sender)
            location = self.tablayout_list[currentIndex].getItemPosition(idx)
            print "Tab:", currentIndex, "Row", location[0], "Column", location[1], "Sender:", sender.text()

if __name__ == '__main__':

    # Every PyQt5 application must create an application object.
    app = QApplication(sys.argv)
    configuration_panel = ConfigurationPanel()
    configuration_panel.show()
    sys.exit(app.exec_())
