from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver
class RarpDecode(DecodeProto):
    def decode_data(self):
        return None,None,self.retdata,"rarp"