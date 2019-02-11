from Parse.Multithread.Back2ForwardMQ import Back2ForwardMQ
from Parse.Multithread.Threerowsdata import Threerowsdata
#  解析传给前端的数据，用到forward2showMQ
import time
class ForwardAnalysis2ShowThread():  # 把数据分为 1，和 2，3 栏要显示的
    def __init__(self):
        pass
    @staticmethod
    def devidedata():
        time.sleep(5)
        while True:
            a = Back2ForwardMQ.backforwardMQ.get() #  data 是从消息队列Back2ForwardMQ提取出来的
            Threerowsdata.firstrowdata.put(a[0])
            with Threerowsdata.dictL:
                # print("dd41255555555555555555555555555555555555555555555555555555555555555555555555555555555555555")
                # print(a[0][0],a[1:])
                Threerowsdata.secandthirdrowdata[a[0][0]] = a[1:]  #  这个是显示一个，处理一个，这个东西要包含在线程中

        #  这个字典要作为共享数据，要为其枷锁访问，当数据写入后，释放锁，


