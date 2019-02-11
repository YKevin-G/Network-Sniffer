from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver
import dpkt

class UOicqDecode(DecodeProto):
    def __init__(self, data):
        super().__init__(data)
        self.retheaddata = {}
    def decode_data(self):
        self.data = dpkt.qq.QQBasicPacket(self.data)
        self.retdata["header"] = ("Qicq info header: " + str(self.data.header_type))
        self.retdata["source"] = ("Source ???: "+ str(self.data.source))
        self.retdata["command"] = ("Command: "+ str(self.data.command))
        self.retdata["sequence"] = ("Sequence: ", str(self.data.sequence))
        self.retdata["QQnum"] = ("QQnum: ", str(self.data.qqNum))
        self.retdata["QQ main data"] = ("QQ main data: ", str(self.data.data))
        #
        # print("Qicq info header: ", self.data.header_type)
        # print("Source ???: ", self.data.source)
        # print("Command: ", self.data.command)
        # print("Sequence: ", self.data.sequence)
        # print("QQnum: ", self.data.qqNum)
        # print("QQ main data: ", self.data.data)
        return None,None,self.retdata,"uoicq"
