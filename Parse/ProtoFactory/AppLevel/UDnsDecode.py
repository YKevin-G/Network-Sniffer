from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver

class UDnsDecode(DecodeProto):
    def decode_data(self):
        self.retdata["info"] = "undecode"
        return None,None,self.retdata,"dns"