import sys
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QTableWidget,QGridLayout,QWidget ,QHBoxLayout , QPushButton,QHeaderView,QAbstractItemView,QFrame
import numpy as np
from Parse.Multithread.Threerowsdata import Threerowsdata
import threading
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import queue
from UI.pages.bigpages.bigpage2.DetailSecondrowdata import Ui_Form as DetailSecondrowdata
import time
from PyQt5.QtCore import QTimer
from Parse.Multithread.Speedofcap import Speedofcap
class DetailFirstrowdata(QTableWidget):
	def __init__(self, parent=None):
		super(DetailFirstrowdata,self).__init__(parent)
#		self.resize(400,500)
#       设置好的布局 已经保证可以完全填充窗体
		self.mylayout =  QGridLayout(self) 
		self.mylayout.setObjectName("gridLayout")
		self.firstrow = pg.TableWidget() # 下面是手动添加信息，需要改变
		self.firstrowdata = [(1156,'0.001001', '192.168.0.101','221.15.13.15','Tcp','62','syn = 2123'),
		(1157,'0.101001', '192.168.0.101','221.15.13.15','Tcp','62','syn = 2235'),
		(1158, '1.001001', '92.168.0.101','221.15.13.15','Tcp','15','syn = 2152'),
		(1159,'10.001001', '192.168.0.101','121.15.13.15','Tcp','25','syn = 2365'),
		(1160,'2.001001', '192.168.0.101','58.15.13.15','Tcp','85','syn = 2155')]
		# np 可以不用，这个更方便的定义了数据格式
		self.showfirstrowdata = np.array(self.firstrowdata, dtype=[('No', int), ( 'Time', object), ('Source', object), ('Destination', object), ('Protocol', object), ('Length', object), ('Info', object)])
		self.firstrow.setData(self.showfirstrowdata)
		self.mylayout.addWidget(self.firstrow)
		self.firstrow.setShowGrid(False)  # 是否显示网格线
		self.firstrow.verticalHeader().setHidden(True)    # 垂直方向的表头删除
# 		self.bottomwindow.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch())   TypeError: 'ResizeMode' object is not callable
		self.firstrow.setColumnWidth(0, 130) # 设置列宽
		self.firstrow.setColumnWidth(1, 180)
		self.firstrow.setColumnWidth(2, 300)
		self.firstrow.setColumnWidth(3, 300)
		self.firstrow.setColumnWidth(4, 130)
		self.firstrow.setColumnWidth(5, 130)

		self.firstrow.horizontalHeader().setStretchLastSection(True)   # 最后一个随机全部占满剩余空间
		self.firstrow.setSelectionBehavior(QAbstractItemView.SelectRows)  # 选中一个 选中整行
		self.firstrow.setFrameShape(QFrame.NoFrame)
#		self.bottomwindow.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch())
#		self.bottomwindow.horizontalHeader().setResizeMode(1,QHeaderView.ResizeToContents()Stretch)
		self.setLayout(self.mylayout)

		self.timer1 = threading.Timer(0.4,self.putnumofdecode)         # 这个是为了显示那个，第一栏显示数据的速度的
		self.timer1.start()


	# def mousePressEvent(self,event):
	# 	'''鼠标按下事件'''
	# 	# 判断是否为鼠标左键按下
	# 	if event.firstrow.clicked() == True:
	# 		# 发射点击信号
	# 		self.clicked.emit(True)
	# 		# 传递至父窗口响应鼠标按下事件
	# 		self.parent().mousePressEvent(event)
	def putnumofdecode(self):
		currentindex = self.firstrow.rowCount()
		print("Decode 传入的数据",currentindex)
		Speedofcap.lockdecode.acquire()
		Speedofcap.decodednum.put(currentindex)
		print("Decode 队列有多少数据", Speedofcap.decodednum.qsize())
		Speedofcap.lockdecode.release()

		self.timer1 = threading.Timer(0.6,self.putnumofdecode)
		self.timer1.start()

	def updatedata(self):
#		a = Threerowsdata.firstrowdata.get()
		a = Threerowsdata.firstrowdata.get()
		self.firstrow.addRow(a)                   # 将要更新的数据加入到保存数据的列表中
	def retindex(self):
		rowindex = self.table1.firstrow.currentRow()
		return rowindex

class UpdateData(QThread):       # 检测到消息队列里面包含数据时，那么此信号槽机制会通知第一栏的信息去更新消息数据
	update_date = pyqtSignal()
	def __init__(self):
		super(UpdateData, self).__init__()
	def run(self):
		time.sleep(5)
		# l = threading.Lock()
		# while True:  # 后加的
		# 	if not Threerowsdata.firstrowdata.empty():
		# 		self.update_date.emit()
		# 		time.sleep(1)
		while not Threerowsdata.firstrowdata.empty():
			self.update_date.emit()
			time.sleep(1)

"""
class Updatedata(QThread):
	updata_data = pyqtSignal()
	def __init__(self,parent=None):
		super(Updatedata,self).__init__(parent)
		self.flags = True
	def __del__(self):
		self.flags = False
		self.wait()
	def run(self):
		while(self.flags):
#			a = Threerowsdata.firstrowdata.get()
			self.updata_data.emit()
"""


"""
class Updatedata(QThread):
	updata_data = pyqtSignal()
	def __init__(self,parent=None):
		super(Updatedata,self).__init__(parent)
		self.flags = True
	def __del__(self):
		self.flags = False
		self.wait()
	def run(self):
		while(self.flags):
#			a = Threerowsdata.firstrowdata.get()
			self.updata_data.emit()
"""

if __name__ == '__main__':
	app = QApplication(sys.argv)
	mydata = DetailFirstrowdata()
	ss = UpdateData(mydata.qq)
	ss.update_date.connect(mydata.updatedata)
	ss.start()
	mydata.show()
	sys.exit(app.exec_())
















