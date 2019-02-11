import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(1222, 1500)
#        self.setFixedSize(1500, 800)
#        self.setMaximumSize(self.width(), self.height())
#        self.setWindowFlags(QtCore.Qt.MaximizeUsingFullscreenGeometryHint)  #最大化问题未解决
        self.setWindowTitle('Sniffer')
        self.statusBar().showMessage('Ready')

        self.setGeometry(80, 50, 250, 150)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())