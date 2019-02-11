import pcapy
import dpkt
from Parse.ProtoFactory.DataLinkLevel.EthernetDecode import EthernetDecode
import time
from Parse.ProtoFactory.PublicFunc.DecodeHex import DecodeHex
from Parse.Multithread.Back2ForwardMQ import Back2ForwardMQ
from Parse.Multithread.Speedofcap import Speedofcap
class Parse():
    def __init__(self):
        self.addressbook = { "ReqTHttpDecode":"Parse.ProtoFactory.AppLevel.ReqTHttpDecode", "ResTHttpDecode":"Parse.ProtoFactory.AppLevel.ResTHttpDecode",
                             "UCliDhcpDecode":"Parse.ProtoFactory.AppLevel.UCliDhcpDecode","UCltDhcpDecode":"Parse.ProtoFactory.AppLevel.UCltDhcpDecode",
                             "UDnsDecode":"Parse.ProtoFactory.AppLevel.UDnsDecode", "UOicqDecode":"Parse.ProtoFactory.AppLevel.UOicqDecode",
                             "UServDhcpDecode":"Parse.ProtoFactory.AppLevel.UServDhcpDecode", "ArpDecode":"Parse.ProtoFactory.IPLevel.ArpDecode",
                             "IpDecode":"Parse.ProtoFactory.IPLevel.IpDecode", "PppDecode":"Parse.ProtoFactory.IPLevel.PppDecode",
                             "Eth8021qDecode":"Parse.ProtoFactory.IPLevel.Eth8021qDecode",
                             "PppoeDecode": "Parse.ProtoFactory.IPLevel.PppoeDecode","RarpDecode": "Parse.ProtoFactory.IPLevel.RarpDecode",
                             "IpxDecode": "Parse.ProtoFactory.IPLevel.IpxDecode","IcmpDecode": "Parse.ProtoFactory.TransLevel.IcmpDecode",
                             "TcpDecode": "Parse.ProtoFactory.TransLevel.TcpDecode","UdpDecode": "Parse.ProtoFactory.TransLevel.UdpDecode",
}
#        self.top = []  # 最上层的数据集合，包含每次传递的三组数据
        self.data1 = [[], {}, []]  # 最上层的下一层数据集合，包含每次传递的三组数据
        self.data21 = []  # 用来存放每一组的 第一行的7个数据
        self.data22 = {}  # 用来存放每一组的 第二行的数据{{},{}}
        self.data23 = [[],[]]  # 用来存放每一组的 第三行数据
#        self.data23[0] = retsingledata
#        self.data23[1] = retascdata
#        self.pktnum = 1  # 用来记录每个数据包的编号
#        self.pktlen = pktlen
#        self.limit = 0  # 用来限制 每集起 10 个数据包更新一次

        self.capture = None
        self.rawdata = None
#        self.data = data
        self.returndata = ()
#        self.timestamp = round(time.time()-starttime,6)
#    def initializedata(self, data,starttime,pktlen,retascdata,retsingledata,totalnumofpkt):
#   从rawdata 消息队列中
    def initializedata(self,rawdata):
        self.rawdata = rawdata
        self.data21.append(self.rawdata[1])  # 编号
        self.data21.append(self.rawdata[2])  # 时间戳
        decodehex = DecodeHex(self.rawdata[0])
        hexdata = decodehex.hex2data()
        self.retascdata = hexdata[0]
        self.retsingledata = hexdata[1]
        self.data23[0] = self.retsingledata
        self.data23[1] = self.retascdata         # 第三层要显示的数据已经结束了
        self.data1[2] = self.data23

    def parse(self):
        flag = True
        decode = EthernetDecode(self.rawdata[0])
        self.returndata = decode.decode_data()   # 函数返回值：下一层数据, 下一层协议,本次解析的协议中信息,本层协议
        self.data = self.returndata[0]             # 源数据
        self.payload_proto = self.returndata[1]

        try:
            if self.returndata[2] != None:  # 从返回值中提取出有价值的信息，传入到消息队列中
                self.data22[self.returndata[3]] = self.returndata[2]          #  {}  存放协议，与协议中的具体信息
            if self.returndata[0] == None or self.returndata[0] == None:
                flag = False  # flag = false 表名 上层已经没有协议需要解析
        except:
            flag = False

        while(flag):
            if (self.payload_proto == None):  # 来判断是否还有上层协议需要解析
                flag = False  # 已经没有需要解析的协议
            else:
                processnextdata = self.addressbook.get(self.payload_proto,"Wrong")   # 未添加此地址，即此协议未解析
                if processnextdata == "Wrong":
                    flag = False
                    break
                deocedeobj = __import__(processnextdata, fromlist=True)
                # 通过得到的要使用的模块的引用地址，在程序中动态引入该模块
#                print(self.payload_proto)
                clas = getattr(deocedeobj, self.payload_proto)     # 从该模块中得到该协议解析类
                dd =clas(self.data)             # 因为没有对上一步得到的协议解析类进行初始化，所以现在给它传入参数
                self.returndata = dd.decode_data()  # 此处增加返回值（每一层解析后的协议字典）要逐一添加到字典中
                try:
                    if self.returndata[2] != None:   # 从返回值中提取出有价值的信息，传入到消息队列中
                        self.data22[self.returndata[3]] = self.returndata[2]
                    if self.returndata[0] == None or self.returndata[0] == None:
                        flag = False
                except:
                    flag = False
                    break
                self.data = self.returndata[0]
                self.payload_proto = self.returndata[1]
        # 给data1[]赋值
        self.data1[1] = self.data22                     # 第二层信息已经传给了总的数据data1
        dd1 = self.data22.get("ip",{"srcip":"wrong"})   #  因为 IP协议头中包含多种信息，先取出IP的那一段，然后再去地址
        dd2 = self.data22.get("ip", {"dstip": "wrong"})
        self.data21.append(dd1.get("srcip"))
        self.data21.append(dd2.get("dstip"))
        key = self.data22.keys()
        # print(key)
        lkey = list(key)
        self.data21.append(lkey[-1])  # 最上层协议显示
        self.data21.append(self.rawdata[3])  # 数据包长度
        tiny = self.data22.get(lkey[-1]) #得到最上层协议的字典信息
        tinykey = list(tiny.keys())
        # print(tinykey)
        showdata = ""   # 第三层要存入信息的初始字段
        for i in range(1):          # 只把最上层协议的第一个关键字 字段存入 第一栏的第七列信息中
            showdata = (showdata + tiny[tinykey[i]])
        self.data21.append(showdata)  # 最上层数据包信息
        self.data1[0] = self.data21
        #  这一个数据包的数据收集完毕，清空 data21,22,23
        self.data21 = []  # 用来存放每一组的 第一行的7个数据
        self.data22 = {}  # 用来存放每一组的 第二行的数据
        self.data23 = [[], []]  # 用来存放每一组的 第三行数据
        # print(self.data1)
        Back2ForwardMQ.backforwardMQ.put(self.data1)   # 一定要放在所有数据都等装完毕后

#        if self.limit == 10:
#           data1 给self.top 传值 正好凑够10个
#           发送信号 传送数据给界面
#           limit 置零
#        else:
#            data1 给self.top 传至 self.top.append(self.data1)

