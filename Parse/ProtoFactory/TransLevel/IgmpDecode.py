from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver


class IgmpDecode(DecodeProto):
    def decode_data(self):
        self.retdata["info"] = "undecode"
        return None,None,self.retdata,"igmp"
