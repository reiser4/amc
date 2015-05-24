import sys
from PyQt5.QtWidgets import (QWidget,QApplication, QDesktopWidget, QPushButton,
    QMessageBox, QMainWindow, QAction, qApp, QTextEdit, QLCDNumber, QSlider, QVBoxLayout,
    QGridLayout, QTabWidget)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import QCoreApplication, Qt

tablist = []
tablabellist = []
layoutlist=[]
tablelist = []
Tab = QTabWidget()
headerlist = [ 'ID','Question','Answer 1','Answer 2','Answer 3','Difficulty','Statistics','Date Added','Added By','Date Modified']

num_tab_widgets = 10

for i in range(num_tab_widgets):
    tablist.append(QWidget())
    Tab.addTab(tablist[i], QString('SECTION %s'%chr(ord('A')+i)))
    tablabellist.append(QLabel('title'))
    tablelist.append(QTableWidget())
    setattr(self,'Table%d'%i,tablelist[i])
    layoutlist.append(QVBoxLayout())

    tablelist[i].setColumnCount(len(headerlist))
    tablelist[i].setHorizontalHeaderLabels(headerlist)
    tablelist[i].setEditTriggers(QTableWidget.NoEditTriggers)
    tablelist[i].setSelectionBehavior(QTableWidget.SelectRows)
    tablelist[i].setSelectionMode(QTableWidget.SingleSelection)

    layoutlist[i].addWidget(tablabellist[i])
    layoutlist[i].addWidget(tablelist[i])
    tablist[i].setLayout(layoutlist[i])

CLayout = QVBoxLayout()
CLayout.addWidget(Tab)

Cwidget = QWidget()
Cwidget.setLayout(CLayout)
setCentralWidget(Cwidget)
