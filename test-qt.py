import sys
from PyQt5.QtWidgets import (QWidget,QApplication, QDesktopWidget, QPushButton,
    QMessageBox, QMainWindow, QAction, qApp, QTextEdit, QLCDNumber, QSlider, QVBoxLayout,
    QGridLayout, QTabWidget)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import QCoreApplication, Qt


class Test(QMainWindow):

    def __init__(self):
        super(Test, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 400, 400)
        self.setWindowTitle("Test")
        self.centerOnScreen()

        #cWidget = QWidget(self)
        tab_widget = QTabWidget(self)
        tab1 = QWidget(tab_widget)
        tab2 = QWidget(tab_widget)
        tab3 = QWidget(tab_widget)
        tab_widget.addTab(tab1, "Tab1")
        tab_widget.addTab(tab2, "Tab2")
        tab_widget.addTab(tab3, "Tab3")


        exitAction = QAction(QIcon("icons/exit.png"), "&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        #exitAction.triggered.connect(qApp.quit)
        exitAction.triggered.connect(self.close)

        self.statusBar()

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAction)

        btn = QPushButton("Quit", tab1)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.clicked.connect(self.close)
        btn.resize(btn.sizeHint())

        btn1 = QPushButton("Press1", tab1)
        btn1.clicked.connect(self.buttonClicked)

        btn2 = QPushButton("Press2", tab2)
        btn2.clicked.connect(self.buttonClicked)


        #self.statusBar().showMessage("Ready")
        """
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        #self.setLayout(vbox)
        #self.setCentralWidget(vbox)
        sld.valueChanged.connect(lcd.display)
        """
        #grid = QGridLayout(cWidget)
        grid1 = QGridLayout(tab1)
        grid1.addWidget(btn1, 0, 0)
        grid1.addWidget(btn, 0, 2)

        grid2 = QGridLayout(tab2)
        grid2.addWidget(btn2, 0, 0)
        #textEdit = QTextEdit(cWidget)
        textEdit = QTextEdit(tab2)
        grid2.addWidget(textEdit, 1, 0, 3, 3)

        grid3 = QGridLayout(tab3)
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
        grid3.addWidget(lcd)
        grid3.addWidget(sld)
        sld.valueChanged.connect(lcd.display)

        #self.setLayout(grid)
        self.setCentralWidget(tab_widget)

        self.show()

    def centerOnScreen(self):
        '''
        centerOnScreen()
        Centers the window on the screen.
        '''
        # prende le dimesioni della finestra
        qr = self.frameGeometry()
        # prende le dimensioni del monitor
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


if __name__ == '__main__':

    # Every PyQt5 application must create an application object.
    app = QApplication(sys.argv)
    test = Test()
    sys.exit(app.exec_())




# Altro metodo per instanziare
'''
if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())
    '''
