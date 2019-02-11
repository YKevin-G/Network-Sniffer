import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class GroupCheckBox(QWidget):

	def __init__(self, parent=None):
		super(GroupCheckBox, self).__init__(parent)
		
		groupBox = QGroupBox("Checkboxes")
		groupBox.setFlat( False )
		
		layout = QVBoxLayout()
		self.checkBox1= QCheckBox("&Checkbox1")
		self.checkBox1.setChecked(True)
		self.checkBox1.stateChanged.connect( lambda:self.btnstate(self.checkBox1) )
		layout.addWidget(self.checkBox1)
        
		self.checkBox2 = QCheckBox("&Checkbox2")
		self.checkBox2.toggled.connect( lambda:self.btnstate(self.checkBox2) )
		layout.addWidget(self.checkBox2)

		self.checkBox3 = QCheckBox("&Checkbox3")	
		self.checkBox3.stateChanged.connect( lambda:self.btnstate(self.checkBox3) )
		layout.addWidget(self.checkBox3)
        
		self.checkBox4 = QCheckBox("&Checkbox4")	
		self.checkBox4.stateChanged.connect( lambda:self.btnstate(self.checkBox4) )
		layout.addWidget(self.checkBox4)
		
		self.checkBox5 = QCheckBox("&Checkbox5")	
		self.checkBox5.stateChanged.connect( lambda:self.btnstate(self.checkBox5) )
		layout.addWidget(self.checkBox5)

		groupBox.setLayout(layout)
		mainLayout = QVBoxLayout()
		mainLayout.addWidget(groupBox)
		
		self.setLayout(mainLayout)
		self.setWindowTitle("checkbox demo")
	
	def btnstate(self,btn ):
		chk1Status = self.checkBox1.text()+", isChecked="+  str( self.checkBox1.isChecked() ) + ', checkState=' + str(self.checkBox1.checkState())   +"\n"		 
		chk2Status = self.checkBox2.text()+", isChecked="+  str( self.checkBox2.isChecked() ) + ', checkState=' + str(self.checkBox2.checkState())   +"\n"	
		chk3Status = self.checkBox3.text()+", isChecked="+  str( self.checkBox3.isChecked() ) + ', checkState=' + str(self.checkBox3.checkState())   +"\n"			
		chk4Status = self.checkBox4.text()+", isChecked="+  str( self.checkBox4.isChecked() ) + ', checkState=' + str(self.checkBox4.checkState())   +"\n"	
		chk5Status = self.checkBox5.text()+", isChecked="+  str( self.checkBox5.isChecked() ) + ', checkState=' + str(self.checkBox5.checkState())   +"\n"	
		print(chk1Status + chk2Status + chk3Status + chk4Status +chk5Status )

if __name__ == '__main__':
	app = QApplication(sys.argv)
	checkboxDemo = GroupCheckBox()
	checkboxDemo.show()
	sys.exit(app.exec_())
