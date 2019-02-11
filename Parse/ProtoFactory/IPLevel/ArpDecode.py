from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver

class ArpDecode(DecodeProto):
    def decode_data(self):
        # print("ethernet_version", self.data.hrd)
        # print("protocol", self.data.pro)
        # print("hd_dev_add_len", self.data.hln, "bytes")
        # print("pro_len", self.data.pln, "bytes")
        # print("operation", self.data.op)
        # # ARP_OP_REQUEST = 1  request to resolve ha(hard address) given pa(ip address)
        # # ARP_OP_REPLY = 2   response giving hardware address
        # # ARP_OP_REVREQUEST = 3   request to resolve pa given ha
        # # ARP_OP_REVREPLY = 4  response giving protocol address
        # print("src_mac",  MacIpAddrConver.mac_addr(self.data.sha))  # arp_data.sha  ':'.join('%02x' % compat_ord(b) for b in arp_data.sha)
        # print("src_ip", MacIpAddrConver.inet_to_str(self.data.spa))
        # print("dst_mac", MacIpAddrConver.mac_addr(self.data.tha))  # arp_data.tha  ':'.join('%02x' % compat_ord(b) for b in arp_data.tha)
        # print("dst_ip", MacIpAddrConver.inet_to_str(self.data.tpa))
        self.retdata["ethversion"] = ("ethernet_version"+str(self.data.hrd))
        self.retdata["protocol"] = ("hd_dev_add_len"+str(self.data.pro))
        self.retdata["hdlen"] = ("hd_dev_add_len"+str(self.data.hln)+"bytes")
        self.retdata["prolen"] = ("hd_dev_add_len"+str(self.data.pln)+ "bytes")
        self.retdata["operation"] = ("hd_dev_add_len"+ str(self.data.op))
        self.retdata["srcmac"] = ("src_mac"+ MacIpAddrConver.mac_addr(self.data.sha))  # arp_data.sha  ':'.join('%02x' % compat_ord(b) for b in arp_data.sha)
        self.retdata["src"] = ("src_ip"+ MacIpAddrConver.inet_to_str(self.data.spa))
        self.retdata["dstmac"] = ("dst_mac"+MacIpAddrConver.mac_addr(self.data.tha))  # arp_data.tha  ':'.join('%02x' % compat_ord(b) for b in arp_data.tha)
        self.retdata["dstip"] = ("dst_ip"+MacIpAddrConver.inet_to_str(self.data.tpa))


        return None,None,self.retdata,"arp"


