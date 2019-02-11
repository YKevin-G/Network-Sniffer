from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver
import dpkt

class UdpDecode(DecodeProto):
    def decode_data(self):
        # print("src_port: ", self.data.sport)
        # print("dst_port: ", self.data.dport)
        # print("the whole len of pkt(include header and data): ", self.data.ulen)
        # print("fake sum: ", self.data.sum)

        self.retdata["sport"] = ("src_port: "+ str(self.data.sport))
        self.retdata["dport"] = ("dst_port: "+ str(self.data.dport))
        self.retdata["ulen"] = ("the whole len of pkt(include header and data): "+ str(self.data.ulen))
        self.retdata["sum"] = ("fake sum: "+ str(self.data.sum))
        if self.tcpudp_payload_proto.get(self.data.sport,None):
            return self.data.data, self.tcpudp_payload_proto.get(self.data.sport,None),self.retdata,"udp"
        elif self.tcpudp_payload_proto.get(self.data.dport,None):
            return self.data.data, self.tcpudp_payload_proto.get(self.data.sport,None),self.retdata,"udp"
        else:
            return None,None,self.retdata,"udp"