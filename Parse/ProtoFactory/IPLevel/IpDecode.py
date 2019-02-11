from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver


class IpDecode(DecodeProto):
    def decode_data(self):
        # print("the version of ip protocol: ", self.data.v)
        # print("header length: ", self.data.hl)
        # print("type of operation: ", self.data.tos)
        # print("total length of header and data: ", self.data.len)  # max 65535
        # #  __len__ self.__hdr_len__ + len(self.opts) + len(self.data)
        # print("identification of every single pkt: ", self.data.id)
        # print("1 repersents more fragment and 0 rp None: ", self.data.mf)
        # print("0 represent fragment and 1 represent don't fragment: ", self.data.df)
        # print("reserved unuse: ", self.data.rf)  # 未使用位
        # print("offset: ", self.data.offset)
        # print("time to live: ", self.data.ttl)
        # print("protocol: ", self.data.p)
        # print("checksum of header: ", self.data.sum)
        # print("src ip: ", MacIpAddrConver.inet_to_str(self.data.src))
        # print("dst ip: ", MacIpAddrConver.inet_to_str(self.data.dst))


        self.retdata["versionprotocol"] = ("the version of ip protocol:" + str(self.data.v))
        self.retdata["headlen"] = ("header length: "+ str(self.data.hl))
        self.retdata["operation"] = ("type of operation: "+ str(self.data.tos))
        self.retdata["datalen"] = ("total length of header and data: "+ str(self.data.len))  # max 65535
        #  __len__ self.__hdr_len__ + len(self.opts) + len(self.data)
        self.retdata["identification"] = ("identification of every single pkt: "+str(self.data.id))
        self.retdata["fragmentornot"] = ("1 repersents more fragment and 0 rp None: "+str(self.data.mf))
        self.retdata["fragment"] = ("0 represent fragment and 1 represent don't fragment:" + str(self.data.df))
        self.retdata["unuse"] = ("reserved unuse: "+ str(self.data.rf))  # 未使用位
        self.retdata["offsetl"] = ("offset: "+str(self.data.offset))
        self.retdata["ttl"] = ("time to live: "+ str(self.data.ttl))
        self.retdata["protocol"] = ("protocol: "+ str(self.data.p))
        self.retdata["checksum"] = ("checksum of header: "+ str(self.data.sum))
        self.retdata["srcip"] = ("src ip: "+ MacIpAddrConver.inet_to_str(self.data.src))
        self.retdata["dstip"] = ("dst ip: "+ MacIpAddrConver.inet_to_str(self.data.dst))
        return self.data.data, self.ip_payload_proto[self.data.p],self.retdata,"ip"