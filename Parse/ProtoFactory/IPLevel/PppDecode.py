from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver
import dpkt
import time

class PppDecode(DecodeProto):
    def decode_data(self):
#        print("Addr :", self.data.addr)
#        print("control info :", self.data.cntrl)
#        print("Maybe Proto :", self.data.p)
        print("Maybe Proto :", self.data.p)
        self.retdata["MaybeProto"] = ("Maybe Proto :"+ str(self.data.p))
        return self.data.data, self.ppp_payload_proto.get(self.data.p, None),self.retdata,"ppp"
#       self.ppp_payload_proto[1]