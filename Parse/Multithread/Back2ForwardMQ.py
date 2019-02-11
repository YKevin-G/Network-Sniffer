import queue
class Back2ForwardMQ:
    backforwardMQ = queue.Queue(-1)  # 这个数据集的原子是 由Parsepkt 返回的数据。下一步应该是解析数据给前端显示了
    def __init__(self):
        pass