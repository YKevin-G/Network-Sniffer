from Parse.Multithread.Multithread import Multithread
from Parse.Capturepkt import Capturepkt
import time
from PyQt5.QtWidgets import *
from UI.SnifferUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Parse.Multithread.ForwardAnalysis2ShowThread import ForwardAnalysis2ShowThread
from Parse.Multithread.Threerowsdata import Threerowsdata
from PyQt5.QtCore import *
from UI.pages.bigpages.bigpage2.DetailFirstrowdata import UpdateData
from UI.pages.bigpages.bigpage2.SpliterContainer import UpdateSecdata
from UI.pages.bigpages.bigpage1.mainpage import Ui_Form
import threading
def startui():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    update = UpdateData()
    update.update_date.connect(ui.centralview.table1.updatedata)
    update.start()

    # 启动table1里面更新数据的时钟

    MainWindow.show()
#    ui.centralview.table1.timer.start(2050)  # 每2050毫秒显示一次
    sys.exit(app.exec_())
def startdash():
    ad = QApplication(sys.argv)
    ff = Ui_Form()
    ff.show()
    sys.exit(ad.exec_())



if __name__ == "__main__":

    ss = Multithread()
    pp = Capturepkt(1)
    # pp.filter = "tcp"
    print("Start!!!!!")
    t1 = threading.Thread(target=ss.threadpoolofprocess)  #  线程池来解析包
    print("Next one!!!!!")
    t2 = threading.Thread(target=pp.capturepkt)   # 抓包
    t4 = threading.Thread(target=startui)       #  前端
    t3 = threading.Thread(target=ForwardAnalysis2ShowThread.devidedata)  # 分包
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()