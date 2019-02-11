import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Parse.Mainn import Mainn
import threading

class ComboxDemo(QWidget):
	def __init__(self, parent=None):
		super(ComboxDemo, self).__init__(parent)
		self.setWindowTitle("Configuration")
		self.resize(400, 400)
		layout = QVBoxLayout()

		self.device = QComboBox()
		self.device.addItem("wlan")
		self.device.addItem("ethernet")
		self.device.currentIndexChanged.connect(self.setdevice)
		layout.addWidget(self.device)

		# mm = Mainn(device)


		self.setLayout(layout)

	def setdevice(self, device):
		if self.device.currentText() == "wlan":
			self.startmianui(0)
		else:
			self.startmianui(1)



	def startmianui(self, device):

		mm = Mainn(device)
		tt = threading.Thread(target=mm.startall)
		tt.start()

class Mainwindow(QThread):
	sinout = pyqtSignal()
	def __init__(self):
		super(Mainwindow, self).__init__()
	def run(self):
		pass

if __name__ == '__main__':
	app = QApplication(sys.argv)
	comboxDemo = ComboxDemo()
	comboxDemo.show()
	sys.exit(app.exec_())

