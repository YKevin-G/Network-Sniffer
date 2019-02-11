# mydashboard
# 2018/4/8
# version:3 (final)
from UI.pages.bigpages.bigpage1.Polygonal import flow

from UI.pages.bigpages.bigpage1.MyDashboard import dashboard
import sys
from PyQt5.QtWidgets import QApplication, QDialog ,QWidget ,QHBoxLayout , QPushButton,QLabel
import threading
from Parse.Multithread.Speedofcap import Speedofcap
class Dashboard(QLabel):
	def __init__(self,parent=None):
		super(Dashboard,self).__init__(parent)
		self.setWindowTitle("Dashboard")
		self.resize(1050, 225)
		self.setMaximumSize(1050, 225)
#		self.resize(1900, 800)
		self.setObjectName("form")
		# 水平布局按照从左到右的顺序进行添加按钮部件。
		self.dashboard1 = dashboard(self)
		self.dashboard2 = dashboard(self)
		self.dashboard3 = dashboard(self)
		self.dashboard4 = dashboard(self)
#		self.dashboard5 = dashboard(self)
		self.hlayout = QHBoxLayout(self)  
       				
		self.hlayout.addWidget( self.dashboard1 )
		self.hlayout.addWidget( self.dashboard2 )
		self.hlayout.addWidget( self.dashboard3 )
		self.hlayout.addWidget( self.dashboard4 )   
#		self.hlayout.addWidget( self.dashboard5 )
		self.hlayout.addStretch(0)

		self.totalnumm = [0,0,0,0,0]
		self.decodenumm = [0,0,0,0,0]
		self.numorder = 0
		self.timer = threading.Timer(0.5,self.computeangle)
		self.timer.start()

	def computeangle(self):       # 计算角度，并且更新每一个角度的值，这是计算平均值的方法
		totalsum = 0
		decodesum = 0
		if self.numorder < 5:
			decodedata = Speedofcap.decodednum.get()
			totaldata = Speedofcap.totalnum.get()
			self.totalnumm[self.numorder] = totaldata
			self.decodenumm[self.numorder] = decodedata
			totalangle = 240 + abs((self.totalnumm[self.numorder] - self.totalnumm[self.numorder - 1]) // 2) * 10
			decodeangle = 240 + abs((self.decodenumm[self.numorder] - self.decodenumm[self.numorder - 1]) // 2) * 10
			self.numorder += 1
			# for i in range(5):
			# 	totalsum += self.totalnumm[i]
			# 	decodesum += self.decodenumm[i]
			# totalangle = 240+(totalsum//5 - 240)
			# decodeangle = 240+(decodesum//5 - 240)

			if totalangle < 480:
				self.dashboard1.angle = totalangle
			else:
				self.dashboard1.angle = 480

			if decodeangle< 480:
				self.dashboard2.angle = decodeangle
			else:
				self.dashboard2.angle = 480
		else:
			self.numorder = 0
			decodedata = Speedofcap.decodednum.get()
			totaldata = Speedofcap.totalnum.get()
			self.totalnumm[self.numorder] = totaldata
			self.decodenumm[self.numorder] = decodedata
			# for i in range(5):
			# 	totalsum += self.totalnumm[i]
			# 	decodesum += self.decodenumm[i]
			# totalangle = 240 + (totalsum//5-240)
			# decodeangle = 240 + (decodesum//5-240)
			totalangle = abs((self.totalnumm[self.numorder] - self.totalnumm[4])//2)*10+240
			decodeangle = abs((self.decodenumm[self.numorder] - self.decodenumm[4])//2)*10+240
			if totalangle < 480:
				self.dashboard1.angle = totalangle
			else:
				self.dashboard1.angle = 480

			if decodeangle < 480:
				self.dashboard2.angle = decodeangle
			else:
				self.dashboard2.angle = 480
		self.timer = threading.Timer(0.7, self.computeangle)
		self.timer.start()

		# 添加伸缩控件
		# self.hlayout.addStretch(0)				
		#设置间距
		#hlayout.setSpacing( 10 )	
		# self.setLayout(self.hlayout)   
 
if __name__ == "__main__":  
	app = QApplication(sys.argv) 
	form = Dashboard()
	form.show()
	sys.exit(app.exec_())
