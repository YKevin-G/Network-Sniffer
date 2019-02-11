from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver
import dpkt

class EthernetDecode(DecodeProto):
    def decode_data(self):
        self.data = dpkt.ethernet.Ethernet(self.data)
        # print("proto_type", self.data.type)
        if self.data.type > 1500:  # 这是ethernet 议
            print("source mac :", MacIpAddrConver.mac_addr(self.data.src))
            print("destiny mac :", MacIpAddrConver.mac_addr(self.data.dst))  # '%02x'输出两位十六进制数，空位补0
            print("proto_type :", self.data.type)
            self.retdata["smac"] = ("source mac :"+MacIpAddrConver.mac_addr(self.data.src))
            self.retdata["dmac"] = ("destiny mac :"+MacIpAddrConver.mac_addr(self.data.dst))
            self.retdata["proto_type"] = ("proto_type :"+ str(self.data.type))
            try:
                ethernet_payload = self.ethernet_payload_proto[self.data.type]
                print("ethernet_payload :", ethernet_payload)
                self.retdata[ethernet_payload] = ("ethernet_payload :"+ ethernet_payload)
            except:
                print("ethernet don't include this payload: ", self.data.type)
            return self.data.data, self.ethernet_payload_proto[self.data.type],self.retdata,"ethernet"
        else:  #IEEE802.2/802.3 LLC   Nove II ,IEEE802.2/802.3 SNAP
            print("IEEE802.2/802.3")
            return None,None,self.retdata,"ethernet"
    def trans_data(self):
        pass