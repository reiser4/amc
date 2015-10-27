from distutils.core import setup
import py2exe


includes = ["sip",
            "PyQt5",
            "PyQt5.QtCore",
            "PyQt5.QtGui"]

setup(console=['configpanel.py'])