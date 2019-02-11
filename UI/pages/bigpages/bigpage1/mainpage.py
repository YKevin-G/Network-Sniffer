# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from UI.pages.bigpages.bigpage1.GroupofCheckBox import GroupCheckBox
from UI.pages.bigpages.bigpage1.Polygonal import flow
from UI.pages.bigpages.bigpage1.DashboardContainer import Dashboard
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel,QWidget
from PyQt5.QtCore import Qt
import sys


class Ui_Form(QWidget):
    def __init__(self,parent = None):
        super(Ui_Form,self).__init__(parent)
        self.resize(1500, 800)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setFixedHeight(350)
        self.tabWidget.setObjectName("tabWidget")
        self.gauge = QtWidgets.QWidget()
        self.gauge.setObjectName("gauge")
        self.widget = QtWidgets.QWidget(self.gauge)
        self.widget.setGeometry(QtCore.QRect(0,0,900,287))  
#       the QRect class defines a rectangle in the plane using integer precision,(int x, int y, int width, int height)
#        self.widget.setGeometry(QtCore.QRect(180, 11, 300, 287))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = Dashboard(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        
        spacerItem2 = QtWidgets.QSpacerItem(298, 222, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setFixedSize(150,40)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: green")

        self.horizontalLayout_3.addWidget(self.pushButton)
#        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#        self.horizontalLayout_3.addItem(spacerItem3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setFixedSize(150,40)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color: green")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.gauge, "")
        self.detail = QtWidgets.QWidget()
        self.detail.setObjectName("detail")
        self.tabWidget.addTab(self.detail, "")
        self.proto = QtWidgets.QWidget()
        self.proto.setObjectName("proto")
        self.tabWidget.addTab(self.proto, "")
        self.verticalLayout.addWidget(self.tabWidget)
        # 第二个tab
        self.tabWidget_2 = QtWidgets.QTabWidget(self)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolBox = QtWidgets.QToolBox(self.tab)
        self.toolBox.setObjectName("toolBox")
        self.network = QtWidgets.QWidget()
        self.network.setGeometry(QtCore.QRect(0, 0,1900, 600))
        self.network.setObjectName("network")
#        self.network.setBaseSize
        self.widget1 = QtWidgets.QWidget(self.network)
        self.widget1.setGeometry(QtCore.QRect(0,0,1900,380))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.label = flow()
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
#        spacerItem4 = QtWidgets.QSpacerItem(73, 158, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#        self.horizontalLayout_2.addItem(spacerItem4)
        self.groupbox = GroupCheckBox()
#        self.listView = QtWidgets.QListView(self.widget1)
#        self.listView.setObjectName("listView")
#        self.horizontalLayout_2.addWidget(self.listView)
        self.horizontalLayout_2.addWidget(self.groupbox)

        self.toolBox.addItem(self.network, "")
        self.detailerror = QtWidgets.QWidget()
        self.detailerror.setGeometry(QtCore.QRect(0, 0, 723, 215))
        self.detailerror.setObjectName("detailerror")
        self.toolBox.addItem(self.detailerror, "")
        self.sizedistribution = QtWidgets.QWidget()
        self.sizedistribution.setObjectName("sizedistribution")
        self.toolBox.addItem(self.sizedistribution, "")
        self.horizontalLayout.addWidget(self.toolBox)
        self.tabWidget_2.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget_2)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "reset"))
        self.pushButton_2.setText(_translate("Form", "set threashhold"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gauge), _translate("Form", "gauge"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.detail), _translate("Form", "detail"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.proto), _translate("Form", "proto"))
#        self.label.setText(_translate("Form", "TextLabel"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.network), _translate("Form", "network"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.detailerror), _translate("Form", "detail error"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.sizedistribution), _translate("Form", "size distribution"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("Form", "Tab 1"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
#    ui.setupUi(MainWindow)
    ui.show()
    sys.exit(app.exec_())
"""class polygonal(QLabel):
    def __init__(self,imageName = None,n = 2, flag = False, parent = None):
        super(polygonal, self).__init__()
        self.setAlignment(Qt.AlignHCenter)
        self.setAlignment(Qt.AlignVCenter)

"""




