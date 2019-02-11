# 2018/4/8 
# versions： 3
from UI.pages.bigpages.bigpage2.DetailSecondrowdata import Ui_Form as DetailSecondrowdata
from UI.pages.bigpages.bigpage2.DetailFirstrowdata import DetailFirstrowdata
from UI.pages.bigpages.bigpage2.DetailThirdrowdata import DetailThirdrowdata
from Parse.Multithread.Threerowsdata import Threerowsdata
from UI.pages.bigpages.bigpage2.DetailFirstrowdata import UpdateData
import sys
from PyQt5.QtCore import Qt, QPointF, pyqtSignal,QThread
from PyQt5.QtGui import QPainter, QPolygonF
from PyQt5.QtWidgets import QTextEdit, QListWidget,\
    QTreeWidget, QSplitter, QApplication, QMainWindow, QSplitterHandle,QTableWidget,QWidget
from PyQt5 import QtCore,QtWidgets
import time
class Spliter(QWidget):
	def __init__(self,parent=None):
		super(Spliter,self).__init__(parent)
		self.splayout = QSplitter(self)
		self.splayout.setGeometry(QtCore.QRect(70, 10, 256, 576))
		self.splayout.setOrientation(QtCore.Qt.Vertical)
		self.table1 = DetailFirstrowdata(self.splayout)
		self.table2 = DetailSecondrowdata(self.splayout)
		self.table3 = DetailThirdrowdata(self.splayout)
		self.gridLayout = QtWidgets.QGridLayout(self)
		self.gridLayout.addWidget(self.splayout)

		self.table1.firstrow.cellClicked['int','int'].connect(self.getindex)     # 点击事件，更新第二栏
		self.table1.firstrow.cellClicked['int','int'].connect(self.getindexnew)   # 点击事件，更新第三栏
		#  鼠标点击后 设置第二行，第三行的数据
	def getindexnew(self):
		row = self.table1.firstrow.currentRow()
		strindex = self.table1.firstrow.item(row, 0).text()      # 取 所点击行的第一个数据，
		index = int(strindex)
		self.table3.dynamicsetval(index)

	def getindex(self):
		row = self.table1.firstrow.currentRow()
		strindex = self.table1.firstrow.item(row, 0).text()
		index = int(strindex)
		self.table2.dynamicsetval(index)
		# if len(Threerowsdata.secandthirdrowdata)> 0:
		# 	print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
		# 	upsecdatathread = UpdateSecdata(index)
		# 	upsecdatathread.update_date.connect(self.table2.dynamicsetval)
		# 	upsecdatathread.start()
class UpdateSecdata(QThread):
	update_date = pyqtSignal(int)
	def __init__(self,index):
		super(UpdateSecdata, self).__init__()
		self.index = index
	def run(self):
		while True:
			self.update_date.emit(self.index)
			time.sleep(3)

		# self.table1.firstrow.clicked.connect(self.pp)   # 已验证可以收到table1的点击
"""
class mainn(QWidget):
	def __init__(self,parent=None):
		super(mainn,self).__init__(parent)
		self.resize(400,400)
	def setctl(self,qq):
		self.setCentralWidget(qq)
"""
if __name__ == "__main__":
	app = QApplication(sys.argv)
#	mm = mainn()
	sp = Spliter()
#	mm.setctl(sp)
#	mm.show()
	sp.show()
	sys.exit(app.exec_())