# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidget,QGridLayout,QWidget ,QHBoxLayout , QPushButton,QHeaderView,QAbstractItemView,QFrame
from Parse.Multithread.Threerowsdata import Threerowsdata
from PyQt5.QtWidgets import *
import time
class Ui_Form(QTreeWidget):
    def __init__(self,parent = None):
        super(Ui_Form, self).__init__(parent)
        self.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self)
        self.treeWidget.setObjectName("treeWidget")

        self.keydict = {"frame": [0, 15], "ethernet": [1, 2], "pppoe": [2, 4], "ppp": [6, 1],
                   "ip": [3, 14] , "tcp": [5, 9], "udp": [4, 4], "uoicq": [7, 6],
                   "reshttp": [8, 5], "reqhttp": [9, 5]}
        # 每一个协议的序号，每一个协议有几个child分支
        self.keyinkeybook = list(self.keydict)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)  # frame
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)  # ethernet
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)  # pppoe
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)  #ip
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)  # udp
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)  #  tcp
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)  # ppp
        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)  # uoicq
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)  # reshttp
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)  # reqhttp
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)


        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.retranslateUi()
#        self.addc()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "1"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "frame"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Form", "interface id"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("Form", "encapsulastion type"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("Form", "arrivetime"))
        self.treeWidget.topLevelItem(0).child(3).setText(0, _translate("Form", "Time shift for this packet : 0seconds"))
        self.treeWidget.topLevelItem(0).child(4).setText(0, _translate("Form", "epoch time"))
        self.treeWidget.topLevelItem(0).child(5).setText(0, _translate("Form", "time delta from previous captured frame "))
        self.treeWidget.topLevelItem(0).child(6).setText(0, _translate("Form", "time delta from previous displayed frame"))
        self.treeWidget.topLevelItem(0).child(7).setText(0, _translate("Form", "frame number"))
        self.treeWidget.topLevelItem(0).child(8).setText(0, _translate("Form", "frame length"))
        self.treeWidget.topLevelItem(0).child(9).setText(0, _translate("Form", "capture length"))
        self.treeWidget.topLevelItem(0).child(10).setText(0, _translate("Form", "frame is masked:false"))
        self.treeWidget.topLevelItem(0).child(11).setText(0, _translate("Form", "frame is ignored"))
        self.treeWidget.topLevelItem(0).child(12).setText(0, _translate("Form", "protocols in frame"))
        self.treeWidget.topLevelItem(0).child(13).setText(0, _translate("Form", "color rule name:***"))
        self.treeWidget.topLevelItem(0).child(14).setText(0, _translate("Form", "color rule string:***"))

        self.treeWidget.topLevelItem(1).setText(0, _translate("Form", "ethernet"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("Form", "destination mac"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("Form", "source mac"))

        self.treeWidget.topLevelItem(2).setText(0, _translate("Form", "pppoe"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("Form", "version:1"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("Form", "type:1"))
        self.treeWidget.topLevelItem(2).child(2).setText(0, _translate("Form", "session id:0x6237"))
        self.treeWidget.topLevelItem(2).child(3).setText(0, _translate("Form", "payload length:42"))



        self.treeWidget.topLevelItem(3).setText(0, _translate("Form", "ipv4"))
        self.treeWidget.topLevelItem(3).child(0).setText(0, _translate("Form", "version"))
        self.treeWidget.topLevelItem(3).child(1).setText(0, _translate("Form", "header length"))
        self.treeWidget.topLevelItem(3).child(2).setText(0, _translate("Form", "type of operation"))
        self.treeWidget.topLevelItem(3).child(3).setText(0, _translate("Form", "total length"))
        self.treeWidget.topLevelItem(3).child(4).setText(0, _translate("Form", "identification of header and data"))
        self.treeWidget.topLevelItem(3).child(5).setText(0, _translate("Form", "1 represent more fragment and 0 rep None"))
        self.treeWidget.topLevelItem(3).child(6).setText(0, _translate("Form", "0 rep fragment and 1 rep None"))
        self.treeWidget.topLevelItem(3).child(7).setText(0, _translate("Form", "reverse Unuse"))
        self.treeWidget.topLevelItem(3).child(8).setText(0, _translate("Form", "offset"))
        self.treeWidget.topLevelItem(3).child(9).setText(0, _translate("Form", "ttl"))
        self.treeWidget.topLevelItem(3).child(10).setText(0, _translate("Form", "protocol"))
        self.treeWidget.topLevelItem(3).child(11).setText(0, _translate("Form", "check sum"))
        self.treeWidget.topLevelItem(3).child(12).setText(0, _translate("Form", "src ip"))
        self.treeWidget.topLevelItem(3).child(13).setText(0, _translate("Form", "dst ip"))

        self.treeWidget.topLevelItem(4).setText(0, _translate("Form", "udp"))
        self.treeWidget.topLevelItem(4).child(0).setText(0, _translate("Form", "src port"))
        self.treeWidget.topLevelItem(4).child(1).setText(0, _translate("Form", "dst port"))
        self.treeWidget.topLevelItem(4).child(2).setText(0, _translate("Form", "the len of pkt"))
        self.treeWidget.topLevelItem(4).child(3).setText(0, _translate("Form", "fake sum"))

        self.treeWidget.topLevelItem(5).setText(0, _translate("Form", "tcp"))
        self.treeWidget.topLevelItem(5).child(0).setText(0, _translate("Form", "src port "))
        self.treeWidget.topLevelItem(5).child(1).setText(0, _translate("Form", "dst port"))
        self.treeWidget.topLevelItem(5).child(2).setText(0, _translate("Form", "pkt sequence"))
        self.treeWidget.topLevelItem(5).child(3).setText(0, _translate("Form", "pkt ack"))
        self.treeWidget.topLevelItem(5).child(4).setText(0, _translate("Form", "tcp data start palce"))
        self.treeWidget.topLevelItem(5).child(5).setText(0, _translate("Form", "tcp flag"))
        self.treeWidget.topLevelItem(5).child(6).setText(0, _translate("Form", "the senders window"))
        self.treeWidget.topLevelItem(5).child(7).setText(0, _translate("Form", "checksum"))
        self.treeWidget.topLevelItem(5).child(8).setText(0, _translate("Form", "botttom of urgent data"))

        self.treeWidget.topLevelItem(6).setText(0, _translate("Form", "ppp"))
        self.treeWidget.topLevelItem(6).child(0).setText(0, _translate("Form", "interface id"))

        self.treeWidget.topLevelItem(7).setText(0, _translate("Form", "uoicq"))   # qq
        self.treeWidget.topLevelItem(7).child(0).setText(0, _translate("Form", "header "))
        self.treeWidget.topLevelItem(7).child(1).setText(0, _translate("Form", "source"))
        self.treeWidget.topLevelItem(7).child(2).setText(0, _translate("Form", "cmd"))
        self.treeWidget.topLevelItem(7).child(3).setText(0, _translate("Form", "sequence"))
        self.treeWidget.topLevelItem(7).child(4).setText(0, _translate("Form", "qq num"))
        self.treeWidget.topLevelItem(7).child(5).setText(0, _translate("Form", "data"))

        self.treeWidget.topLevelItem(8).setText(0, _translate("Form", "reshttp"))    # reshttp
        self.treeWidget.topLevelItem(8).child(0).setText(0, _translate("Form", "version "))
        self.treeWidget.topLevelItem(8).child(1).setText(0, _translate("Form", "status"))
        self.treeWidget.topLevelItem(8).child(2).setText(0, _translate("Form", "reason"))
        self.treeWidget.topLevelItem(8).child(3).setText(0, _translate("Form", "body"))
        self.treeWidget.topLevelItem(8).child(4).setText(0, _translate("Form", "header"))

        self.treeWidget.topLevelItem(9).setText(0, _translate("Form", "reqhttp"))    # reqhttp
        self.treeWidget.topLevelItem(9).child(0).setText(0, _translate("Form", "method "))
        self.treeWidget.topLevelItem(9).child(1).setText(0, _translate("Form", "uri"))
        self.treeWidget.topLevelItem(9).child(2).setText(0, _translate("Form", "version"))
        self.treeWidget.topLevelItem(9).child(3).setText(0, _translate("Form", "body"))
        self.treeWidget.topLevelItem(9).child(4).setText(0, _translate("Form", "header"))


        self.treeWidget.setSortingEnabled(__sortingEnabled)
    # def addc(self):
    #     root = QTreeWidgetItem(self.treeWidget)
    #     root.setText(0,"5655656")


    # def mousePressEvent(self,event):
    #     '''鼠标按下事件'''
    #     # 判断是否为鼠标左键按下
    #         # 发射点击信号
    #     self.clicked.emit()
    #     time.sleep(1)
    def pp(self):

        print("dddddd")
    # 更新数据用下面的这个函数
    def dynamicsetval(self,index):         # 第一栏被点击后实时更新要显示的第二栏的相应数据
        i = 0
        if True:
            Threerowsdata.dictL.acquire(blocking=False)  #  因为是使用字典存储的数据信息，所以需要在数据的访问上加锁
            if len(Threerowsdata.secandthirdrowdata) > 0:
                aa = Threerowsdata.secandthirdrowdata[index]           # 编号对应数据包的第二层数据  s所有数据{协议:{信息种类：信息}，{}，{}}
                i += 1
            Threerowsdata.dictL.release()
            # aa = {0:{"ip":{"d":5,"dd":88,"dede":8}}}
#        keyss = aa[0]
        self.treeWidget.clear()
        if i != 0:
            keyss = list(aa[0].keys())    # 把所有的协议的键 都取出来，然后循环
            for key in keyss:
                singleproto = aa[0][key]   #  每一个协议的具体信息，先把协议名字提取出来
                singleprotopreciseinfo = list(singleproto.keys())   # 具体信息的每一项信息的头部都提出来
                root = QTreeWidgetItem(self.treeWidget)
                root.setText(0, key)
                for ch in singleprotopreciseinfo:  # 循环输出每个协议下的具体内容，
                    child = QTreeWidgetItem(root)
                    child.setText(0,singleproto[ch])

    def setval(self,index):
        mylock = Threerowsdata.dictL
        mydata = Threerowsdata.secandthirdrowdata

        with mylock:
            aa = mydata[index]           # 编号对应数据包的第二层数据  s所有数据{协议:{信息种类：信息}，{}，{}}
        keyss = list(aa[0].keys())    # 把所有的协议的键 都取出来，然后循环
        for key in keyss:
            if key in self.keyinkeybook:
                dd = self.keydict[key]
                info = aa[key]   # 协议信息
                infokind = list(info.keys())    # 协议里面信息种类
                for i in range(dd[1]+1):
                    if i == 0:
                        self.treeWidget.topLevelItem(dd[0]).setText(0, _translate("Form", key))
                    else:  # 不是解析第一个
                        self.treeWidget.topLevelItem(dd[0]).child(i-1).setText(0, _translate("Form", info[infokind[i-1]]))
            else:  # key 不在解析范围内
                break




import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())