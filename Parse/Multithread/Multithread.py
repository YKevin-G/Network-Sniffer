from Parse.Multithread.CapturedRawDataMQ import CaptureedRawDataMQ
# 1 、需要一个参数，就是抓包时存放生数据的队列，里面的原子是列表[data, self.totalnumofpkt, self.timestamp,pktlen]，即上面这个
from Parse.Multithread.ForwardAnalysis2ShowMQ import ForwardAnalysis2ShowMQ
from Parse.Parsepkt import Parse
import concurrent.futures
import threading

class Multithread():
    def __init__(self):
        self.processgroup = {}
        for i in range(5):  # 循环构建self.processgroup（）
            process = Parse()
            a = []
            a.append(0)        # 0 代表这个数据没有被占用
            a.append(process)
            self.processgroup[i] = a
        self.flags = True  # 用来表示何时结束解析过程
        self.lock = threading.Lock()
        #    2、用于享元模式，构建多个解析类parsepkt,每一个解析类对应一个标志，
        #    这两个关键字是使用字典来存储的   就需要用列表来表示了，
        #    当使用完后，将其标志位改变
        #  定义线程池 并处理
    def realfunc(self):
        while self.flags:
            data = CaptureedRawDataMQ.rawdataMQ.get()
            # print(data)
            i = 0             # 各个线程之间的信息是不会交互的
            self.lock.acquire()
            while self.processgroup.get(i)[0] != 0:  # 查看标志位
                i += 1
            self.processgroup.get(i)[0] = 1
            self.lock.release()
            process = self.processgroup.get(i)[1]     # 标志位显示未被使用，用数据初始化类
            process.initializedata(data)
            process.parse()
            self.processgroup.get(i)[0] = 0

    def threadpoolofprocess(self):                   # 主线程里面的一个调用解析函数的线程，又新建了5个线程参与解析
        # print("threadpoolofprocess is running")
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.submit(self.realfunc)
            executor.submit(self.realfunc)
            executor.submit(self.realfunc)
            executor.submit(self.realfunc)
            executor.submit(self.realfunc)
        # 3、定义一个线程池

    def endthread(self):
        pass
        # 用按钮来实现，结束线程，检测消息队列是否为空
