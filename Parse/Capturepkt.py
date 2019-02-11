import pcapy
import time
from Parse.ProtoFactory.PublicFunc.DecodeHex import DecodeHex
import binascii
from Parse.Parsepkt import *
from Parse.Multithread.CapturedRawDataMQ import CaptureedRawDataMQ
import queue
from PyQt5.QtCore import QTimer
from Parse.Multithread.Speedofcap import Speedofcap
import threading
from Parse.Multithread.UI2BackParameter import UI2BackParameter
class Capturepkt():
    def __init__(self,devicenum):
        # 设置一个保存抓取数据的队列(在CapturedRawDataMQ里面)，
        # 这个队列的原子数据 是一个list[rawdata,pktlenn,self.timestamp，self.retascdata,self.retsingledata，self.totalnumofpkt]
        # 包含 没有解析的数据，数据长度，时间戳，ascii 形式信息（可省），单纯的16进制数字信息，目前为止收到的包数量（即编号）
        self.atomdata = []
        self.devlist = pcapy.findalldevs()
        self.snaplen = 65535
        self.capturemode = 1
        self.timeout = 1000
        self.filter = " "
        self.devicenum = devicenum
        # self.filter = UI2BackParameter.myfilter
        # self.devicenum = UI2BackParameter.mydevice
        self.starttime = time.time()
        self.timestamp = time.time()
        self.totalnumofpkt = 0     # 用来计数所抓包的总数量，即每一条数据的编号属性
        self.times = time.time()
        self.timer =threading.Timer(0.6, self.putnumofcap)   # 设置时钟每 秒传第一次数据，来作为折线图显示的数据
        self.timer.start()
    def preprocess(self, hdr, data):
        # 自己没有读出hdr里面的时间戳，自己定义了一个时间戳
#        decodehex = DecodeHex(data)
#        hexdata = decodehex.hex2data()
#        self.retascdata = hexdata[0]
#        self.retsingledata = hexdata[1]
        print("进入预处理")
        self.timestamp = round(time.time()-self.starttime,6)  # 时间戳
        pktlen = len(data)
        self.atomdata.append(data)
        self.atomdata.append(self.totalnumofpkt)
        self.atomdata.append(self.timestamp)
        self.atomdata.append(pktlen)
        CaptureedRawDataMQ.rawdataMQ.put(self.atomdata)
        self.atomdata = []
        self.totalnumofpkt += 1
#        ppdata = Parse(data, self.starttime, pktlen,self.retascdata,self.retsingledata)
#        self.atomdata = [data, self.totalnumofpkt, self.timestamp,pktlen]  # 传递给解析数据的哪一方
#        ppdata.parse()
        print("开始时间：%f,现在时间：%f,抓包数量：%d" % (self.times, time.time(), self.totalnumofpkt))

    def capturepkt(self):
        print("capturepkt is running")
        print(self.devlist)
        cap = pcapy.open_live(self.devlist[1], self.snaplen, self.capturemode, self.timeout)
        cap.setfilter(self.filter)
        # self.timer.start(1000)   # 每0.5秒传第一次抓包数量
        cap.loop(-1, self.preprocess)
    def putnumofcap(self):
        Speedofcap.locktotal.acquire()
        Speedofcap.totalnum.put(self.totalnumofpkt)
        print("传入数据传入数据传入数据传入数据传入数据传入数据传入数据传入数据传入数据传入数据传入数据",self.totalnumofpkt)
        Speedofcap.locktotal.release()

        self.timer =threading.Timer(0.6, self.putnumofcap)   # 设置时钟每2 秒传第一次数据，来作为折线图显示的数据
        self.timer.start()



if __name__ == "__main__":
    pp = Capturepkt(1)
    pp.capturepkt()
#    pp.capturepkt()
