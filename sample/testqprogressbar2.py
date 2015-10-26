import sys, time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal

class MyCustomWidget(QWidget):

    def __init__(self, parent=None):
        super(MyCustomWidget, self).__init__(parent)
        layout = QVBoxLayout(self)

        self.progressBar = QProgressBar(self)
        self.progressBar.setRange(0,100)
        button = QPushButton("Start", self)
        layout.addWidget(self.progressBar)
        layout.addWidget(button)

        button.clicked.connect(self.onStart)

        self.myLongTask = TaskThread()
        self.myLongTask.notifyProgress.connect(self.onProgress)

        self.setLayout(layout)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()


    def onStart(self):
        self.myLongTask.start()

    def onProgress(self, i):
        self.progressBar.setValue(i)


class TaskThread(QThread):
    notifyProgress = pyqtSignal(int)
    def run(self):
        for i in range(101):
            self.notifyProgress.emit(i)
            time.sleep(0.1)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyCustomWidget()
    sys.exit(app.exec_())