"""

import sys
from Sniffer-UI import *
from PyQt5 import QtCore,QtGui
class MAinwindow(QtGui.QWidget,Ui_MainWindow):
    def __init__(self):
        super(MAinwindow, self).__init__()
        self.setupUI(self)

if __name__ == "__main__":
    app = QtGui.QGuiApplication(sys.argv)
    exe = MianWindow()
    exe.show()
    sys.exit(app.exec_())

"""

