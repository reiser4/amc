import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SleepProgress(QThread):
    procDone = pyqtSignal(bool)
    partDone = pyqtSignal(int)

    def run(self):
        print 'proc started'
        for a in range(1, 1+35):

            self.partDone.emit(float(a)/35.0*100)
            print 'sleep', a
            time.sleep(0.13)

        self.procDone.emit(True)
        print 'proc ended'

class AddProgresWin(QWidget):
    def __init__(self, parent=None):
        super(AddProgresWin, self).__init__(parent)

        self.thread = SleepProgress()

        self.nameLabel = QLabel("0.0%")
        self.nameLine = QLineEdit()

        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(1)
        self.progressbar.setMaximum(100)

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.progressbar, 0, 0)
        mainLayout.addWidget(self.nameLabel, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Processing")

        self.thread.partDone.connect(self.updatePBar)
        self.thread.procDone.connect(self.fin)

        self.thread.start()

    def updatePBar(self, val):
        self.progressbar.setValue(val)
        perct = "{0}%".format(val)
        self.nameLabel.setText(perct)

    def fin(self):
        sys.exit()
        ##self.hide()

if __name__ == '__main__':

    import sys
    app = QApplication(sys.path)

    pbarwin = AddProgresWin()
    pbarwin.show()

    sys.exit(app.exec_())
