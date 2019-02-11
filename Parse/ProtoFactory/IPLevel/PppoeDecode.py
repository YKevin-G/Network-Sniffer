from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver
import dpkt

class PppoeDecode(DecodeProto):
    def decode_data(self):
        # print("PPPOE VERSION: ", self.data.v)  # default 0x1
        # print("PPPOE TYPE: ", self.data.type)  # 0x1
        # print("PPPOE CODE：", self.data.code)
        # # default 0x00 会话数据 ,0x09 PADI,0x07 PADO or PADT,0x19 PADR,0x65 PADS
        # print("PPPOE SESSION_ID: ", self.data.session)
        # print("PPPOE LENGTH： ", self.data.len)
        # 其数据域携带标准的PPP data,次数使用的固定的号，因为没有协议类型,这个是包含在pppoe内的不是ethernet 内的，
        # 因为dpkt 没有包含这个直接解析ppp的包，所以就只当存在这一种，
        self.retdata["pppoeversion"] = ("PPPOE VERSION: "+ str(self.data.v))  # default 0x1
        self.retdata["pppoetype"]=("PPPOE TYPE: "+ str(self.data.type))  # 0x1
        self.retdata["pppoecode"]=("PPPOE CODE："+ str(self.data.code))
        # default 0x00 会话数据 ,0x09 PADI,0x07 PADO or PADT,0x19 PADR,0x65 PADS
        self.retdata["pppoesession"] = ("PPPOE SESSION_ID: "+ str(self.data.session))
        self.retdata["pppoelen"]=("PPPOE LENGTH： "+str(self.data.len))
        return self.data.data, self.pppoe_payload_proto[1],self.retdata,"pppoe"