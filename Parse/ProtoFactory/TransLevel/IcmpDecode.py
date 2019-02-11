from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver


class IcmpDecode(DecodeProto):
    def decode_data(self):
        # print("the type of icmp: ", self.data.type)
        # print("the code of icmp: ", self.data.code)
        # print("the checksum of icmp header: ", self.data.sum)
        # print("real data: ",self.data.data)
        """
        unsigned short icmp_id;//用来唯一标识此请求的id号，通常设置为进程id
        unsigned short icmp_sequence;//序列号
        unsigned long icmp_timestamp;//时间戳
        """
        self.retdata["typeicmp"] = ("the type of icmp: "+ str(self.data.type))
        self.retdata["codeicmp"] = ("the code of icmp: "+ str(self.data.code))
        self.retdata["checksum"] = ("the checksum of icmp header: "+ str(self.data.sum))
        self.retdata["realdata"] = ("real data: "+str(self.data.data))
        return None,None,self.retdata,"icmp"

