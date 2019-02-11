import queue
import threading

class Threerowsdata():    # 将数据分为 1栏显示的和 2，3 栏显示的
    dictL = threading.Semaphore(1)
    firstrowdata = queue.Queue(-1)
    secandthirdrowdata = {}
    # 键：所点击的数据包序号，值 分析数据包时 二三层data 所携带的数据
    def __init__(self):
        pass