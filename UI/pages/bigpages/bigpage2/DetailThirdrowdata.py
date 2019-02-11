import sys
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QTableWidget,QGridLayout,QWidget ,QHBoxLayout , QPushButton,QHeaderView,QAbstractItemView,QFrame
import numpy as np
from Parse.Multithread.Threerowsdata import Threerowsdata
# 缺少i一个第三层的联动选取功能
class DetailThirdrowdata(QTableWidget):
	def __init__(self,parent = None):
		super(DetailThirdrowdata,self).__init__(parent)
		self.layout = QGridLayout(self)
		self.table = pg.TableWidget()
		self.table.horizontalHeader().setHidden(True)
		self.table.setShowGrid(False)
		self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.layout.addWidget(self.table)
		self.thirdrowdata = [
		(4,56,85,5,4,56,85,5," ",4,56,85,5,4,56,85,5," ",4,56,85,5,4,56,85,5," ",4,56,85,5,4,56,85,55),
		(1,20,33,8,1,20,33,8," ",1,20,33,8,1,20,33,8," ",1,20,33,8,1,20,33,8," ",1,20,33,8,1,20,33,8),
		(45,4,56,85,45,4,56,85," ",45,4,56,85,45,4,56,85," ",45,4,56,85,45,4,56,85," ",45,4,56,85,45,4,56,85),
		(1,20,33,85,1,20,33,85," ",1,20,33,85,1,20,33,85," ",1,20,33,85,1,20,33,85," ",1,20,33,85,1,20,33,85),
		(4,56,85,6,4,56,85,6," ",4,56,85,6,4,56,85,6," ",4,56,85,6,4,56,85,6," ",4,56,85,6,4,56,85,6),
		(1,2,12,33,1,2,12,33," ",1,2,12,33,1,2,12,33," ",1,2,12,33,1,2,12,33," ",1,2,12,33,1,2,12,33)]
		self.showthirdrowdata = np.array(self.thirdrowdata, dtype=[('No', int), ( 'Time', object), ('Source', object), ('Destination', object),
			('object1',object),('object2',object),('object3',object),('object4',object),('object5',object),
			('object6',object),('object7',object),('object8',object),('object9',object),('object10',object),
			('object11',object),('object12',object),('object13',object),('object14',object),('object15',object),
			('object16',object),('object17',object),('object18',object),('object19',object),('object20',object),
			('object21',object),('object22',object),('object23',object),('object24',object),('object25',object),
			('object26',object),('object27',object),('object28',object),('object29',object),('object30',object),('object31',object)])
		self.table.verticalHeader().setDefaultSectionSize(20)
		self.table.setData(self.thirdrowdata)
		self.setLayout(self.layout)

	# def updatedata(self):
	# #		a = Threerowsdata.firstrowdata.get()
	# 	a = Threerowsdata.firstrowdata.get()
	# 	self.firstrow.addRow(a)

	def dynamicsetval(self,index):
		i = 0
		if True:
			Threerowsdata.dictL.acquire(blocking=False)
			if len(Threerowsdata.secandthirdrowdata) > 0:
				aa = Threerowsdata.secandthirdrowdata[index]  # 编号对应数据包的第二层数据  s所有数据{协议:{信息种类：信息}，{}，{}}
				i += 1
			Threerowsdata.dictL.release()
		# aa = {0:{"ip":{"d":5,"dd":88,"dede":8}}}
		#        keyss = aa[0]
		self.table.clear()
		if i != 0:
			wholedata = aa[1]  # 把所有的协议的键 都取出来，然后循环
			firstaprt = list(aa[1][0])
			secpart = list(aa[1][1])
			firlen = len(firstaprt)
			seclen = len(secpart)

			if firlen>16:
				fir = firlen//16    # 每行8组16 进制数字，看看可以分为几行
				for i in range(fir):
					data1 = firstaprt[i*8:i*8+8]
					data1.append(" ")
					for word in firstaprt[i*8+8:i*8+16]:  # 用python的切片，来将数据分为若干行
						data1.append(word)
					data1.append(" ")
					data2 = secpart[i*8:i*8+8]
					data1.extend(data2)   # 从这里开始添加了，ascii码的部分数据
					for i in range(9):
						data1.append(" ")     # 当时设计的 多余的控件 ，用空格填充
					self.table.appendRow(data1)
					data1 = []
					data2 = []
				i = 16*fir - firlen
				if i > -8:        # 检查是否是最后一行，，，
					dd = firstaprt[i:]
					for j in range(18+i):
						dd.append(" ")
				else:
					dd = firstaprt[i:i+8]
					dd.append(" ")
					for j in range(-8-i):
						dd.append(" ")
					dd.append(" ")

				k = 8*fir - seclen
				for ch in secpart[k:]:
					dd.append(" ")
				self.table.addRow(dd)
			else:           # 如果连第一行数据都未填满
				for i in range(16-firlen):
					firstaprt.append(" ")
				for j in range(len(secpart)):
					firstaprt.append(secpart[j])
				self.table.addRow(firstaprt)





if __name__ == "__main__":
	app =QApplication(sys.argv)
	aa = DetailThirdrowdata()
	aa.show()
	sys.exit(app.exec_())


