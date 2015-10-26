import sys
from PyQt5.QtWidgets import *

class Main(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):

        centralwidget = QWidget()

        self.button = QPushButton("+",self)
        self.button.setStyleSheet("font-size:40px;background-color:#333333;\
        border: 2px solid #222222")
        self.button.setFixedSize(100,100)
        self.button.clicked.connect(self.Button)

        self.grid = QGridLayout()

        self.grid.addWidget(self.button,0,0)

        centralwidget.setLayout(self.grid)

        self.setCentralWidget(centralwidget)

#---------Window settings --------------------------------

        self.setGeometry(300,300,500,100)

def Button(self):
        print("Clicked")

def main():
    app = QApplication(sys.argv)
    main= Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()