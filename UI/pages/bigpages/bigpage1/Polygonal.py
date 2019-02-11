import pyqtgraph as pg
import sys
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5.QtWidgets import QLabel,QWidget,QGridLayout, QGridLayout,QApplication
from PyQt5.QtCore import Qt,QTimer
from Parse.Multithread.Speedofcap import Speedofcap
import time
import threading
class flow(QWidget):
	def __init__(self,parent=None):
		super(flow,self).__init__(parent)
		self.winp = pg.PlotWidget()
		self.winp.addLegend()
		self.resize(500,400)
#		self.setFixedSize(500,400)
		self.startTime = pg.ptime.time()
		self.timer = pg.QtCore.QTimer(self)
		self.timer.timeout.connect(self.update)
		self.winp.setWindowFlags(Qt.FramelessWindowHint)
		self.winp.setDownsampling(mode='peak') # 折线
		self.winp.setClipToView(True)
		self.winp.setRange(xRange=[-10, 0])    # 横坐标
		self.winp.setLimits(xMax=0)

#		self.data = [1,2,10,1,2,52,1,52,5,1000,2,5,21,32,5,15,62,45,12,72,25,61,52,5,21,2,5,1]
		self.data = [0]
		self.pen = self.winp.plot(pen=(0,0,255),name='Total', symbolBrush=(0,0,255),symbolPen='w', symbol='o', symbolSize=10)
		self.layout = QGridLayout()
		self.setLayout(self.layout)
		self.layout.addWidget(self.winp,100, 10, 50, 100)
		self.ptr3 = 0  # 用来截取需要显示的数据

		self.pen2 = self.winp.plot(pen=(255,255,255), name='Decode', symbolBrush=(255,255,255),symbolPen='w', symbol='s', symbolSize=10)
		# self.data2 = [1,2,5,3,5,5,4,6,5,8,2,6,145,8,87,46]
		self.data2=[0]
#		self.timer2 = QTimer(self)
#		self.timer2.timeout.connect(self.updatedata)
		self.start()
		# 设定用来更新数据的timer2


	def updatedata(self):
		a=Speedofcap.totalnum.get()
		self.data.append(a)  # 将要显示的数据加入到列表中

	def start(self):
		self.timer.start(390)
	def update(self):
		global data, ptr3,data2
		now = pg.ptime.time()
#		self.data.append(self.ptr3)
#		self.data.append(ptr3)

		if not Speedofcap.totalnum.empty():
			try:
				a=Speedofcap.totalnum.get()  # block=False
				self.data.append(a)
				print("队列非空成功取数",Speedofcap.totalnum.qsize())
			except:
				c =self.data[-1]
				self.data.append(c)  # 将要显示的数据加入到列表中
				print("队列非空阻塞取数")
		else:
			b = self.data[-1]          # 若此次没有从消息队列中取到数字，那么就再一次添加已有数据的最后一位。
			self.data.append(b)
			print("队列为空取数")
		self.pen.setData(self.data[:self.ptr3])
		self.pen.setPos(-(now-self.startTime), 0)
############################################################

		if not Speedofcap.decodednum.empty():
			try:
				a=Speedofcap.decodednum.get(block=False)
				self.data2.append(a)
			except:
				c =self.data2[-1]
				self.data2.append(c)  # 将要显示的数据加入到列表中
		else:
			b = self.data2[-1]
			self.data2.append(b)

		self.pen2.setData(self.data2[:self.ptr3])
		self.pen2.setPos(-(now-self.startTime), 0)

		self.ptr3 += 1
if __name__ == "__main__":
	app = QApplication(sys.argv)
	pp = flow()
	pp.show()
	sys.exit(app.exec_())

