from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver


class Eth8021qDecode(DecodeProto):
    def decode_data(self):
        print("No Eth8021qDecode")
        return None,None,self.retdata,"eth8021"