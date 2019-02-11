import queue
import threading

class Speedofcap():
    locktotal = threading.Lock()
    lockdecode = threading.Lock()
    totalnum = queue.Queue(-1)
    decodednum = queue.Queue(-1)
    def __init__(self):
        pass
