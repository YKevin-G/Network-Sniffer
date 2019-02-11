from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver


class TcpDecode(DecodeProto):
    def decode_data(self):
        # print("src_port: ", self.data.sport)
        # print("dst_port: ", self.data.dport)
        # print("pkt_sequence: ", self.data.seq)
        # print("pkt_ack: ", self.data.ack)
        # print("tcp data starting place: ", self.data.off)  # tcp的数据包是从何处开始的
        # print("tcp_flag ", self.data.flags)
        """TH_FIN = 0x01  # end of data
    TH_SYN = 0x02  # synchronize sequence numbers
    TH_RST = 0x04  # reset connection
    TH_PUSH = 0x08  # push
    TH_ACK = 0x10  # acknowledgment number set
    TH_URG = 0x20  # urgent pointer set
    TH_ECE = 0x40  # ECN echo, RFC 3168
    TH_CWR = 0x80  # congestion window reduced
    """
        # print("the sender's present windows of sending data ", self.data.win)
        # print("cheacsum: ", self.data.sum)
        # print("the bottom of the urgent data", self.data.urp)

        self.retdata["sport"] = ("src_port: "+ str(self.data.sport))
        self.retdata["dport"] = ("dst_port: "+ str(self.data.dport))
        self.retdata["sequence"] = ("pkt_sequence: "+str(self.data.seq))
        self.retdata["ack"] = ("pkt_ack: "+str(self.data.ack))
        self.retdata["startplace"] = ("tcp data starting place: "+ str(self.data.off))  # tcp的数据包是从何处开始的
        self.retdata["flags"] = ("tcp_flag "+str(self.data.flags))
        self.retdata["window"] = ("the sender's present windows of sending data "+ str(self.data.win))
        self.retdata["sum"] = ("cheacsum: "+ str(self.data.sum))
        self.retdata["urp"] = ("the bottom of the urgent data"+ str(self.data.urp))
#        if self.tcpudp_payload_proto[self.data.sport]:
        if self.tcpudp_payload_proto.get(self.data.sport, None):
            if self.data.sport == 80:
                reshttp = ("Res" + self.tcpudp_payload_proto[self.data.sport])
                return self.data.data, reshttp,self.retdata,"tcp"
            return self.data.data, self.tcpudp_payload_proto[self.data.sport],self.retdata,"tcp"
#        elif self.tcpudp_payload_proto[self.data.dport]:
        elif self.tcpudp_payload_proto.get(self.data.dport, None):
            if self.data.dport == 80:
                reqhttp = ("Req" + self.tcpudp_payload_proto[self.data.dport])
                return self.data.data, reqhttp,self.retdata,"tcp"
            return self.data.data, self.tcpudp_payload_proto[self.data.dport],self.retdata,"tcp"
        else:
            return None,None,self.retdata,"tcp"