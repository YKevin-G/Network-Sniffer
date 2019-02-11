# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sniffer-UI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from UI.pages.bigpages.bigpage2.SpliterContainer import Spliter
from UI.pages.bigpages.bigpage1.mainpage import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Parse.Multithread.Threerowsdata import Threerowsdata
import time
import xlwt
import sys
from Parse.Multithread.Speedofcap import Speedofcap
from Parse.Capturepkt import Capturepkt
from Parse.Multithread.UI2BackParameter import UI2BackParameter


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 800)



        # toolbar 的下拉框1
        self.combo = QtWidgets.QComboBox(MainWindow)
        self.combo.addItem("Tcp")
        self.combo.addItem("Http")
        self.combo.addItem("UDP")
        self.combo.addItem("Ip")
        self.combo.addItem("DHCP")
        self.combo.addItem(" ")
        self.combo.setCurrentText(" ")
        self.combo.currentIndexChanged.connect(self.setfilter)
#        self.combo.setCurrentIndex(3)
        # toolbar 的下拉框2
        self.combo2 = QtWidgets.QComboBox(MainWindow)
        self.combo2.addItem("device1")
        self.combo2.addItem("device2")
        self.combo2.addItem("device3")
        self.combo2.addItem("device4")
        self.combo2.addItem("device5")
        self.combo2.addItem(" ")
        self.combo2.setCurrentText(" ")
        self.combo2.currentIndexChanged.connect(self.setdevice)
        # 放置表盘的页面 tabwidget
#        self.mytab1 = QTabWidget()
#        self.tabgauge = QWidget()
#        self.tabdetail = QWidget()
#        self.tabproto = QWidget()
#       self.mytab1.addTab(self.tabgauge, "tabgauge")
#       self.mytab1.addTab(self.tabdetail, "detail")
#        self.mytab1.addTab(self.tabproto, "proto")
#       self.mtabgauge()
#        self.mtabdetail()
#        self.mtabproto()


#        MainWindow.setCentralWidget(Ui_Form())

#        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
#        self.centralview = QTableView()
        # 此处 添加一个鼠标点击事件，来切换页面
        self.dashshow = Ui_Form()
        self.centralview = Spliter()
        self.centralview.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.centralview, 0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1102, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        self.menu_6 = QtWidgets.QMenu(self.menubar)
        self.menu_6.setObjectName("menu_6")
        self.menu_7 = QtWidgets.QMenu(self.menubar)
        self.menu_7.setObjectName("menu_7")
        self.menu_8 = QtWidgets.QMenu(self.menubar)
        self.menu_8.setObjectName("menu_8")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
#        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
#        self.toolBar_2.setObjectName("toolBar_2")
#        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
#        MainWindow.insertToolBarBreak(self.toolBar_2)
#        self.toolBar_3 = QtWidgets.QToolBar(MainWindow)
#        self.toolBar_3.setObjectName("toolBar_3")
#        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
#        MainWindow.insertToolBarBreak(self.toolBar_3)
        self.action = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action.setIcon(icon)
        self.action.setObjectName("打开")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")

        self.action_3 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_3.setIcon(icon1)
        self.action_3.triggered.connect(self.saveAs)
        self.action_3.setObjectName("保存")

#        self.action_3 = QAction(icon1,"Save &As...", self,triggered=self.saveAs)


        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("action_10")
        self.action_11 = QtWidgets.QAction(MainWindow)
        self.action_11.setObjectName("action_11")
        self.action_13 = QtWidgets.QAction(MainWindow)
        self.action_13.setObjectName("action_13")
        self.action_15 = QtWidgets.QAction(MainWindow)
        self.action_15.setObjectName("action_15")
        self.action_17 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_17.setIcon(icon2)
        self.action_17.triggered.connect(self.pgsave)
        self.action_17.setObjectName("打印")
        self.action_18 = QtWidgets.QAction(MainWindow)
        self.action_18.setObjectName("action_18")
        self.action_19 = QtWidgets.QAction(MainWindow)
        self.action_19.setObjectName("action_19")
        self.action_21 = QtWidgets.QAction(MainWindow)
        self.action_21.setObjectName("action_21")
        self.action_23 = QtWidgets.QAction(MainWindow)
        self.action_23.setObjectName("action_23")
        self.action_25 = QtWidgets.QAction(MainWindow)
        self.action_25.setObjectName("action_25")
        self.action_27 = QtWidgets.QAction(MainWindow)
        self.action_27.setObjectName("action_27")
        self.action_28 = QtWidgets.QAction(MainWindow)
        self.action_28.setObjectName("action_28")
        self.action_29 = QtWidgets.QAction(MainWindow)
        self.action_29.setObjectName("action_29")
        self.action_30 = QtWidgets.QAction(MainWindow)
        self.action_30.setObjectName("action_30")
        self.action_31 = QtWidgets.QAction(MainWindow)
        self.action_31.setObjectName("action_31")
        self.action_32 = QtWidgets.QAction(MainWindow)
        self.action_32.setObjectName("action_32")
        self.action_33 = QtWidgets.QAction(MainWindow)
        self.action_33.setObjectName("action_33")
        self.action_35 = QtWidgets.QAction(MainWindow)
        self.action_35.setObjectName("action_35")
        self.action_36 = QtWidgets.QAction(MainWindow)
        self.action_36.setObjectName("action_36")
        self.action_37 = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/archive.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_37.setIcon(icon3)
        self.action_37.setObjectName("地址簿")
        self.action_38 = QtWidgets.QAction(MainWindow)
        self.action_38.setObjectName("action_38")
        self.action_39 = QtWidgets.QAction(MainWindow)
        self.action_39.setObjectName("action_39")
        self.actionReporter = QtWidgets.QAction(MainWindow)
        self.actionReporter.setObjectName("actionReporter")
        self.action_41 = QtWidgets.QAction(MainWindow)
        self.action_41.setObjectName("action_41")
        self.action_43 = QtWidgets.QAction(MainWindow)
        self.action_43.setObjectName("action_43")
        self.action_44 = QtWidgets.QAction(MainWindow)
        self.action_44.setObjectName("action_44")
        self.action_45 = QtWidgets.QAction(MainWindow)
        self.action_45.setObjectName("action_45")
        self.action_46 = QtWidgets.QAction(MainWindow)
        self.action_46.setObjectName("action_46")
        self.action_48 = QtWidgets.QAction(MainWindow)
        self.action_48.setObjectName("action_48")
        self.action_49 = QtWidgets.QAction(MainWindow)
        self.action_49.setObjectName("action_49")
        self.action_50 = QtWidgets.QAction(MainWindow)
        self.action_50.setObjectName("action_50")
        self.action_51 = QtWidgets.QAction(MainWindow)
        self.action_51.setObjectName("action_51")
        self.action_52 = QtWidgets.QAction(MainWindow)
        self.action_52.setObjectName("action_52")
        self.action_53 = QtWidgets.QAction(MainWindow)
        self.action_53.setObjectName("action_53")
        self.action_55 = QtWidgets.QAction(MainWindow)
        self.action_55.setObjectName("action_55")
        self.action_56 = QtWidgets.QAction(MainWindow)
        self.action_56.setObjectName("action_56")
        self.action_57 = QtWidgets.QAction(MainWindow)
        self.action_57.setObjectName("action_57")
        self.action_58 = QtWidgets.QAction(MainWindow)
        self.action_58.setObjectName("action_58")
        self.action_59 = QtWidgets.QAction(MainWindow)
        self.action_59.setObjectName("action_59")
        self.actionDiscovered_Addresses = QtWidgets.QAction(MainWindow)
        self.actionDiscovered_Addresses.setObjectName("actionDiscovered_Addresses")
        self.action_62 = QtWidgets.QAction(MainWindow)
        self.action_62.setObjectName("定义过滤器")
        self.action_63 = QtWidgets.QAction(MainWindow)
        self.action_63.setObjectName("action_63")
        self.action_65 = QtWidgets.QAction(MainWindow)
        self.action_65.setObjectName("action_65")
        self.action_66 = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_66.setIcon(icon4)
        self.action_66.setObjectName("开始")
        self.action_67 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/pause.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.action_67.setIcon(icon5)
        self.action_67.setObjectName("停止")
        self.action_68 = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/pause-camcorder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_68.setIcon(icon6)
        self.action_68.setObjectName("停止并显示")
        self.action_69 = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/presentation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_69.setIcon(icon7)
        self.action_69.setObjectName("显示")
        self.action_71 = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/monitor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_71.setIcon(icon8)
        self.action_71.setObjectName("捕获面板")
        self.action_73 = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/set-filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_73.setIcon(icon9)
        self.action_73.setObjectName("定义过滤器")
        self.action_74 = QtWidgets.QAction(MainWindow)
        self.action_74.setObjectName("action_74")
        self.actionTrigger_Setup = QtWidgets.QAction(MainWindow)
        self.actionTrigger_Setup.setObjectName("actionTrigger_Setup")
        self.action_76 = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/dashboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_76.setIcon(icon10)
        self.action_76.setObjectName("仪表盘")

        self.action_76.triggered.connect(self.dashfunc)
        self.action_76.triggered.connect(self.cleardataqueue)

        self.action_77 = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/site-map.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_77.setIcon(icon11)
        self.action_77.setObjectName("主机列表")
        self.action_78 = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/chart-pie.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_78.setIcon(icon12)
        self.action_78.setObjectName("矩阵")
        self.action_79 = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_79.setIcon(icon13)
        self.action_79.setObjectName("请求响应时间")
        self.action_80 = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/chart-bar-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_80.setIcon(icon14)
        self.action_80.setObjectName("历史矩阵")
        self.action_81 = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/chart-bar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_81.setIcon(icon15)
        self.action_81.setObjectName("协议分布")
        self.action_82 = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/chart-area-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_82.setIcon(icon16)
        self.action_82.setObjectName("全局统计表")
        self.actionSmart_Screen = QtWidgets.QAction(MainWindow)
        self.actionSmart_Screen.setObjectName("actionSmart_Screen")
        self.action_83 = QtWidgets.QAction(MainWindow)
        self.action_83.setObjectName("物理层状态")
        self.actionSonet_Statistics = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/oscilloscope.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSonet_Statistics.setIcon(icon17)
        self.actionSonet_Statistics.setObjectName("actionSonet_Statistics")
        self.actionSwitch = QtWidgets.QAction(MainWindow)
        self.actionSwitch.setObjectName("actionSwitch")
        self.action_85 = QtWidgets.QAction(MainWindow)
        self.action_85.setObjectName("action_85")
        self.action_86 = QtWidgets.QAction(MainWindow)
        self.action_86.setObjectName("action_86")
        self.action_88 = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/toolbar-image/icon/toolbar_pic/alert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_88.setIcon(icon18)
        self.action_88.setObjectName("警报日志")
        self.action_Switch = QtWidgets.QAction(MainWindow)
        self.action_Switch.setObjectName("action_Switch")
        self.action_X = QtWidgets.QAction(MainWindow)
        self.action_X.setObjectName("action_X")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu.addSeparator()
        self.menu.addAction(self.action_6)
        self.menu.addAction(self.action_7)
        self.menu.addAction(self.action_8)
        self.menu.addAction(self.action_9)
        self.menu.addAction(self.action_10)
        self.menu.addAction(self.action_11)
        self.menu.addSeparator()
        self.menu.addAction(self.action_13)
        self.menu.addSeparator()
        self.menu.addAction(self.action_15)
        self.menu.addSeparator()
        self.menu.addAction(self.action_17)
        self.menu.addAction(self.action_18)
        self.menu.addAction(self.action_19)
        self.menu.addSeparator()
        self.menu.addAction(self.action_21)
        self.menu.addSeparator()
        self.menu.addAction(self.action_23)
        self.menu.addSeparator()
        self.menu.addAction(self.action_X)
        self.menu_2.addAction(self.action_76)
        self.menu_2.addAction(self.action_77)
        self.menu_2.addAction(self.action_78)
        self.menu_2.addAction(self.action_79)
        self.menu_2.addAction(self.action_80)
        self.menu_2.addAction(self.action_81)
        self.menu_2.addAction(self.action_82)
        self.menu_2.addAction(self.actionSmart_Screen)
        self.menu_2.addAction(self.action_83)
        self.menu_2.addAction(self.actionSonet_Statistics)
        self.menu_2.addAction(self.actionSwitch)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_85)
        self.menu_2.addAction(self.action_86)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_88)
        self.menu_2.addAction(self.action_Switch)
        self.menu_3.addAction(self.action_66)
        self.menu_3.addAction(self.action_67)
        self.menu_3.addAction(self.action_68)
        self.menu_3.addAction(self.action_69)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_71)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_73)
        self.menu_3.addAction(self.action_74)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionTrigger_Setup)
        self.menu_4.addAction(self.action_45)
        self.menu_4.addAction(self.action_46)
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.action_48)
        self.menu_4.addAction(self.action_49)
        self.menu_4.addAction(self.action_50)
        self.menu_4.addAction(self.action_51)
        self.menu_4.addAction(self.action_52)
        self.menu_4.addAction(self.action_53)
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.action_55)
        self.menu_4.addAction(self.action_56)
        self.menu_4.addAction(self.action_57)
        self.menu_4.addAction(self.action_58)
        self.menu_4.addAction(self.action_59)
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.actionDiscovered_Addresses)
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.action_62)
        self.menu_4.addAction(self.action_63)
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.action_65)
        self.menu_5.addAction(self.action_37)
        self.menu_5.addAction(self.action_38)
        self.menu_5.addAction(self.action_39)
        self.menu_5.addAction(self.actionReporter)
        self.menu_5.addSeparator()
        self.menu_5.addAction(self.action_41)
        self.menu_5.addSeparator()
        self.menu_5.addAction(self.action_43)
        self.menu_5.addAction(self.action_44)
        self.menu_6.addAction(self.action_32)
        self.menu_6.addAction(self.action_33)
        self.menu_6.addSeparator()
        self.menu_6.addAction(self.action_35)
        self.menu_6.addAction(self.action_36)
        self.menu_7.addAction(self.action_28)
        self.menu_7.addAction(self.action_29)
        self.menu_7.addAction(self.action_30)
        self.menu_7.addAction(self.action_31)
        self.menu_8.addAction(self.action_25)
        self.menu_8.addSeparator()
        self.menu_8.addAction(self.action_27)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.menubar.addAction(self.menu_7.menuAction())
        self.menubar.addAction(self.menu_8.menuAction())
        # self.toolBar.addAction(self.action_66)
        # self.toolBar.addAction(self.action_67)
        # self.toolBar.addAction(self.action_69)
        # self.toolBar.addAction(self.action_68)
        # self.toolBar.addAction(self.action_73)
        # self.toolBar.addSeparator()
        # self.toolBar.addWidget(self.combo)
        # self.toolBar.addWidget(self.combo2)
        # self.toolBar.addSeparator()
        # self.toolBar.addSeparator()
        # self.toolBar.addSeparator()
        #
        # self.toolBar.addAction(self.action)
        self.toolBar.addAction(self.action_3)
        self.toolBar.addSeparator()
        # self.toolBar.addAction(self.action_17)
        # self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_76)
        # self.toolBar.addAction(self.action_77)
        # self.toolBar.addAction(self.action_78)
        # self.toolBar.addAction(self.action_79)
        # self.toolBar.addAction(self.action_80)
        # self.toolBar.addAction(self.action_81)
        # self.toolBar.addAction(self.action_82)
        # self.toolBar.addAction(self.action_88)
        # self.toolBar.addSeparator()
        # self.toolBar.addAction(self.action_71)
        # self.toolBar.addSeparator()
        # self.toolBar.addAction(self.action_37)
        # self.toolBar.addSeparator()
        # self.toolBar.addAction(self.action_67)
        # self.toolBar.addSeparator()
        # self.toolBar.addSeparator()
        # self.toolBar.addSeparator()

        # self.toolBar.addAction(self.actionSonet_Statistics)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sniffer"))
        # 设置窗体图标
        MainWindow.setWindowIcon(QtGui.QIcon(':/mainwindow/icon/mainwindow/snail.png'))

        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "监视器"))
        self.menu_3.setTitle(_translate("MainWindow", "捕获"))
        self.menu_4.setTitle(_translate("MainWindow", "显示"))
        self.menu_5.setTitle(_translate("MainWindow", "工具"))
        self.menu_6.setTitle(_translate("MainWindow", "数据库"))
        self.menu_7.setTitle(_translate("MainWindow", "窗口"))
        self.menu_8.setTitle(_translate("MainWindow", "帮助"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
#        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
#        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.action.setText(_translate("MainWindow", "&打开(O)"))
        self.action.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_2.setText(_translate("MainWindow", "&关闭(C)"))
        self.action_3.setText(_translate("MainWindow", "&保存(S)"))
        self.action_3.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_4.setText(_translate("MainWindow", "&另存为(A)"))
        self.action_6.setText(_translate("MainWindow", "&选定设置(L)"))
        self.action_7.setText(_translate("MainWindow", "&记录于(G)"))
        self.action_8.setText(_translate("MainWindow", "&全部重置(T)"))
        self.action_9.setText(_translate("MainWindow", "&回环模式(K)"))
        self.action_10.setText(_translate("MainWindow", "&打开组件查看"))
        self.action_11.setText(_translate("MainWindow", "&远程打开(M)"))
        self.action_13.setText(_translate("MainWindow", "&设置代理记录(E)"))
        self.action_15.setText(_translate("MainWindow", "&更新许可(U)"))
        self.action_17.setText(_translate("MainWindow", "&打印(P)"))
        self.action_17.setShortcut(_translate("MainWindow", "Return"))
        self.action_18.setText(_translate("MainWindow", "&打印选项(U)"))
        self.action_19.setText(_translate("MainWindow", "&打印异常中断(B)"))
        self.action_21.setText(_translate("MainWindow", "&运行脚本(R)"))
        self.action_23.setText(_translate("MainWindow", "&最近的文件"))
        self.action_25.setText(_translate("MainWindow", "&帮助主题"))
        self.action_27.setText(_translate("MainWindow", "&关于(A)"))
        self.action_28.setText(_translate("MainWindow", "&新建窗口(N)"))
        self.action_29.setText(_translate("MainWindow", "&层叠(C)"))
        self.action_30.setText(_translate("MainWindow", "&平铺(T)"))
        self.action_31.setText(_translate("MainWindow", "&排列图标(A)"))
        self.action_32.setText(_translate("MainWindow", "&选项(O)"))
        self.action_33.setText(_translate("MainWindow", "&维护(M)"))
        self.action_35.setText(_translate("MainWindow", "&保存地址簿(A)"))
        self.action_36.setText(_translate("MainWindow", "&恢复数据库(D)"))
        self.action_37.setText(_translate("MainWindow", "&地址簿(A)"))
        self.action_38.setText(_translate("MainWindow", "&数据包发生器(P)"))
        self.action_39.setText(_translate("MainWindow", "&位错误比率测试(B)"))
        self.actionReporter.setText(_translate("MainWindow", "&Reporter(R)"))
        self.action_41.setText(_translate("MainWindow", "&定制用户工具(U)"))
        self.action_43.setText(_translate("MainWindow", "&选项(O)"))
        self.action_44.setText(_translate("MainWindow", "&专家选项(E)"))
        self.action_45.setText(_translate("MainWindow", "&显示专家分析列表(E)"))
        self.action_46.setText(_translate("MainWindow", "&显示传输分析表(Y)"))
        self.action_48.setText(_translate("MainWindow", "&前一个(P)"))
        self.action_48.setShortcut(_translate("MainWindow", "F7"))
        self.action_49.setText(_translate("MainWindow", "&下一个(N)"))
        self.action_49.setShortcut(_translate("MainWindow", "F8"))
        self.action_50.setText(_translate("MainWindow", "&查找帧(F)"))
        self.action_50.setShortcut(_translate("MainWindow", "Alt+F3"))
        self.action_51.setText(_translate("MainWindow", "&查找下一帧(T)"))
        self.action_51.setShortcut(_translate("MainWindow", "F3"))
        self.action_52.setText(_translate("MainWindow", "&运行帧(G)"))
        self.action_53.setText(_translate("MainWindow", "&标志当前的帧(M)"))
        self.action_55.setText(_translate("MainWindow", "&保存已选择的(V)"))
        self.action_56.setText(_translate("MainWindow", "&选择范围(R)"))
        self.action_57.setText(_translate("MainWindow", "&选择切换(L)"))
        self.action_58.setText(_translate("MainWindow", "&前一个已选择的(O)"))
        self.action_59.setText(_translate("MainWindow", "&下一个已选择的(X)"))
        self.actionDiscovered_Addresses.setText(_translate("MainWindow", "&Discovered Addresses"))
        self.action_62.setText(_translate("MainWindow", "&定义过滤器(D)"))
        self.action_63.setText(_translate("MainWindow", "&选择过滤器(S)"))
        self.action_65.setText(_translate("MainWindow", "&显示设置(U)"))
        self.action_66.setText(_translate("MainWindow", "&开始(T)"))
        self.action_66.setShortcut(_translate("MainWindow", "F10"))
        self.action_67.setText(_translate("MainWindow", "&停止(O)"))
        self.action_67.setShortcut(_translate("MainWindow", "F10"))
        self.action_68.setText(_translate("MainWindow", "&停止并显示(Y)"))
        self.action_68.setShortcut(_translate("MainWindow", "F9"))
        self.action_69.setText(_translate("MainWindow", "&显示(I)"))
        self.action_69.setShortcut(_translate("MainWindow", "F5"))
        self.action_71.setText(_translate("MainWindow", "&捕获面板(C)"))
        self.action_73.setText(_translate("MainWindow", "&定义过滤器(D)"))
        self.action_74.setText(_translate("MainWindow", "&选择过滤器(S)"))
        self.actionTrigger_Setup.setText(_translate("MainWindow", "&Trigger Setup(G)"))
        self.action_76.setText(_translate("MainWindow", "&仪表盘(B)"))
        self.action_77.setText(_translate("MainWindow", "&主机列表(T)"))
        self.action_78.setText(_translate("MainWindow", "&矩阵(M)"))
        self.action_79.setText(_translate("MainWindow", "&请求响应时间(R)"))
        self.action_80.setText(_translate("MainWindow", "&历史矩阵(H)"))
        self.action_81.setText(_translate("MainWindow", "&协议分布(U)"))
        self.action_82.setText(_translate("MainWindow", "&全局统计表(I)"))
        self.actionSmart_Screen.setText(_translate("MainWindow", "&Smart Screen"))
        self.action_83.setText(_translate("MainWindow", "&物理层状态(Y)"))
        self.actionSonet_Statistics.setText(_translate("MainWindow", "&Sonet Statistics(N)"))
        self.actionSwitch.setText(_translate("MainWindow", "&Switch(W)"))
        self.action_85.setText(_translate("MainWindow", "&定义过滤器(D)"))
        self.action_86.setText(_translate("MainWindow", "&选择过滤器(S)"))
        self.action_88.setText(_translate("MainWindow", "&警报日志(L)"))
        self.action_Switch.setText(_translate("MainWindow", "&配置矩阵Switch(C)"))
        self.action_X.setText(_translate("MainWindow", "&退出(X)"))

    def setfilter(self):
        UI2BackParameter.myfilter = self.combo.currentText()

    def setdevice(self):
        UI2BackParameter.mydevice = self.combo2.ccurrentText()



    def mtabproto(self):
        layout = QHBoxLayout()
        layout.addWidget(QPushButton(str(1)))
        layout.addWidget(QPushButton(str(2)))
        layout.addWidget(QPushButton(str(3)))
        layout.addWidget(QPushButton(str(4)))
        layout.addWidget(QPushButton(str(5)))
        self.mytab1.setTabText(0, "proto0")
        #  添加伸缩控件
        layout.addStretch(0)
        self.tabproto.setLayout(layout)

    def dashfunc(self):
        self.dashshow.show()
    def saveAs(self):
        fileName, _ = QFileDialog.getSaveFileName()
        if fileName:
            return self.saveFile(fileName)
        return False
    def saveFile(self, fileName):
        # 创建一个xls对象
        wb = xlwt.Workbook()
        # 新增一个表单
        sh = wb.add_sheet("sheet A")
        # 按位置添加数据
        rownum = -1
        columnnum = -1
        aa = []  # 相当于temp,用来循环收集每一行的数据
        data = []
        row = self.centralview.table1.firstrow.rowCount()
        for i in range(row):
            for j in range(7):
                aa.append(str(self.centralview.table1.firstrow.item(i, j).value))
                # sh.write(i,j,self.centralview.table1.firstrow.item(i,j).value)
            data.append(aa)     # 先把第一栏中的数据存入到，data[]列表中，然后，在使用下面的for循环存入到execl中
            aa = []
        for rowdata in data:
            rownum += 1
            columnnum = -1
            for columndata in rowdata:
                columnnum += 1
                sh.write(rownum, columnnum, columndata)
        wb.save(fileName)
        self.statusbar.showMessage("File saved", 2000)
    def pgsave(self):
        self.centralview.table1.firstrow.saveAll()
    def cleardataqueue(self):

        num1 = Speedofcap.decodednum.qsize()
        if num1 > 0:
            Speedofcap.locktotal.acquire()
            for i in range(num1):
                Speedofcap.decodednum.get()
            Speedofcap.locktotal.release()
        num2 = Speedofcap.totalnum.qsize()
        if num2 > 0:
            Speedofcap.lockdecode.acquire()
            for i in range(num2):
                Speedofcap.decodednum.get()
            Speedofcap.lockdecode.release()

## Start Qt event loop unless running in interactive mode or using pyside.

"""
        self.action_76.triggered.connect(self.dashfunc)
class dashthread(QThread):
    update_date = pyqtSignal()
    def __init__(self):
        super(dashthread, self).__init__()
        pass
    def run(self):
        while True:
            self.update_date.emit()
            time.sleep(2)
"""
from UI.qrc.image import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())