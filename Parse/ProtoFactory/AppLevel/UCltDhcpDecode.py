from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver
class UCltDhcpDecode(DecodeProto):
    def decode_data(self):
        self.retdata["info"] = "undecode"
        return None,None,self.retdata,"cltdhcp"