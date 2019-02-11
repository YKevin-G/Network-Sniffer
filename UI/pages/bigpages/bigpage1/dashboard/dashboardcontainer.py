from mydashboard import dashboard

import sys
from PyQt5.QtWidgets import QApplication  ,QWidget ,QHBoxLayout , QPushButton

class Winform(QWidget):
	def __init__(self,parent=None):
		super(Winform,self).__init__(parent)
		self.setWindowTitle("水平布局管理例子") 
		self.resize(1900, 800)
		
		# 水平布局按照从左到右的顺序进行添加按钮部件。
		self.dashboard1 = dashboard()
		self.dashboard2 = dashboard()
		self.dashboard3 = dashboard()
		self.dashboard4 = dashboard()
		self.dashboard5 = dashboard()
		self.hlayout = QHBoxLayout()  
		self.hlayout.addWidget(QPushButton(str(1)))
       				
		self.hlayout.addWidget( self.dashboard1 )
		self.hlayout.addWidget( self.dashboard2 )
		self.hlayout.addWidget( self.dashboard3 )
		self.hlayout.addWidget( self.dashboard4 )        
		self.hlayout.addWidget( self.dashboard5 )    
        # 添加伸缩控件		
		self.hlayout.addStretch(0)				
		#设置间距
		#hlayout.setSpacing( 10 )	
		self.setLayout(self.hlayout)   
  
if __name__ == "__main__":  
	app = QApplication(sys.argv) 
	form = Winform()
	form.show()
	sys.exit(app.exec_())
