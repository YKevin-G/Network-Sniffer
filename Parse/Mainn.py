from Parse.Multithread.Multithread import Multithread
from Parse.Capturepkt import Capturepkt
from UI.SnifferUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Parse.Multithread.ForwardAnalysis2ShowThread import ForwardAnalysis2ShowThread
from UI.pages.bigpages.bigpage2.DetailFirstrowdata import UpdateData
import threading

class Mainn():
    def __init__(self,devicenum):
        self.devicenum = devicenum
    def startui(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        ss = UpdateData()
        ss.update_date.connect(ui.centralview.table1.updatedata)        # 更新 第一栏的数据
        ss.start()
        # 启动table1里面更新数据的时钟
        MainWindow.show()
        #    ui.centralview.table1.timer.start(2050)  # 每2050毫秒显示一次
        sys.exit(app.exec_())

    def startall(self):
        ss = Multithread()
        pp = Capturepkt(self.devicenum)
        t1 = threading.Thread(target=ss.threadpoolofprocess)  # 线程池来解析包
        print("Next one!!!!!")
        t2 = threading.Thread(target=pp.capturepkt)  # 抓包
        t4 = threading.Thread(target=self.startui)  # 前端
        t3 = threading.Thread(target=ForwardAnalysis2ShowThread.devidedata)  # 分包
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()

if __name__ == "__main__":
    aa = Mainn(1)
    aa.startall()