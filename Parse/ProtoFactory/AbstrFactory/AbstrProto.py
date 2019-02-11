import dpkt


class DecodeProto:

    def __init__(self, data):
        self.data = data
        self.ethernet_payload_proto = {2054: "ArpDecode", 2048: "IpDecode", 33024: "Eth8021qDecode",
                                       34916: "PppoeDecode", 32821: "RarpDecode",33079: "IpxDecode",
                                       34978: "ETH_TYPE_AOE", 187: "ETH_TYPE_EDP",34827: "ETH_TYPE_PPP",
                                       34525: "ETH_TYPE_IP6", 8192: "ETH_TYPE_CDP", 8196: "ETH_TYPE_DTP",
                                       34887: "ETH_TYPE_MPLS", 34888: "ETH_TYPE_MPLS_MCAST", 512: "ETH_TYPE_PUP",
                                       34915:"ETH_TYPE_PPPoE_DISC", 35020: "ETH_TYPE_LLDP", 25944:"ETH_TYPE_TEB"
                                       }
        self.ip_payload_proto = {0: "IP_PROTO_IP", 1: "IcmpDecode", 2: "IgmpDecode", 6: "TcpDecode",
                                 17: "UdpDecode", 3: "IP_PROTO_GGP", 4: "IP_PROTO_IPIP",134: "IP_PROTO_RSVPIGN",
                                 7: "IP_PROTO_CBT", 8: "IP_PROTO_EGP", 9: "IP_PROTO_IGP", 5: "IP_PROTO_ST",
                                 10: "IP_PROTO_BBNRCC", 11: "IP_PROTO_NVP", 12: "IP_PROTO_PUP", 13: "IP_PROTO_ARGUS",
                                 14: "IP_PROTO_EMCON", 15: "IP_PROTO_XNET", 16: "IP_PROTO_CHAOS", 255: "IP_PROTO_RAW",
                                 18: "IP_PROTO_MUX", 19: "IP_PROTO_DCNMEAS", 20: "IP_PROTO_HMP", 21: "IP_PROTO_PRM",
                                 22: "IP_PROTO_IDP", 23: "IP_PROTO_TRUNK1", 24: "IP_PROTO_TRUNK2", 25: "IP_PROTO_LEAF1",
                                 26: "IP_PROTO_LEAF2", 27: "IP_PROTO_RDP", 28: "IP_PROTO_IRTP", 29: "IP_PROTO_TP",
                                 30: "IP_PROTO_NETBLT", 31: "IP_PROTO_MFPNSP", 32: "IP_PROTO_MERITINP", 33: "IP_PROTO_SEP",
                                 34: "IP_PROTO_3PC", 35: "IP_PROTO_IDPR", 36: "IP_PROTO_XTP", 37: "IP_PROTO_DDP",
                                 38: "IP_PROTO_CMTP", 39: "IP_PROTO_TPPP", 40: "IP_PROTO_IL", 41: "IP_PROTO_IP6",
                                 42: "IP_PROTO_SDRP", 43: "IP_PROTO_ROUTING", 44: "IP_PROTO_FRAGMENT", 46: "IP_PROTO_RSVP",
                                 47: "IP_PROTO_GRE", 48: "IP_PROTO_MHRP", 49: "IP_PROTO_ENA", 50: "EspDecode",
                                 51: "IP_PROTO_AH", 52: "IP_PROTO_INLSP", 53: "IP_PROTO_SWIPE", 54: "IP_PROTO_NARP",
                                 55: "IP_PROTO_MOBILE", 56: "IP_PROTO_TLSP", 57: "IP_PROTO_SKIP", 58: "IP_PROTO_ICMP6",
                                 59: "IP_PROTO_NONE", 60: "IP_PROTO_DSTOPTS", 61: "IP_PROTO_ANYHOST", 62: "IP_PROTO_CFTP",
                                 63: "IP_PROTO_ANYNET", 64: "IP_PROTO_EXPAK", 65: "IP_PROTO_KRYPTOLAN", 66: "IP_PROTO_RVD",
                                 67: "IP_PROTO_IPPC", 68: "IP_PROTO_DISTFS", 69: "IP_PROTO_SATMON", 70: "IP_PROTO_VISA",
                                 71: "IP_PROTO_IPCV", 72: "IP_PROTO_CPNX", 73: "IP_PROTO_CPHB", 74: "IP_PROTO_WSN",
                                 75: "IP_PROTO_PVP", 76: "IP_PROTO_BRSATMON", 77: "IP_PROTO_SUNND", 78: "IP_PROTO_WBMON",
                                 79: "IP_PROTO_WBEXPAK", 80: "IP_PROTO_EON", 81: "IP_PROTO_VMTP", 82: "IP_PROTO_SVMTP",
                                 83: "IP_PROTO_VINES", 84: "IP_PROTO_TTP", 85: "IP_PROTO_NSFIGP", 86: "IP_PROTO_DGP",
                                 87: "IP_PROTO_TCF", 88: "IP_PROTO_EIGRP", 89: "IP_PROTO_OSPF", 90: "IP_PROTO_SPRITERPC",
                                 91: "IP_PROTO_LARP", 92: "IP_PROTO_MTP", 93: "IP_PROTO_AX25", 94: "IP_PROTO_IPIPENCAP",
                                 95: "IP_PROTO_MICP", 96: "IP_PROTO_SCCSP", 97: "IP_PROTO_ETHERIP", 98: "IP_PROTO_ENCAP",
                                 99: "IP_PROTO_ANYENC", 100: "IP_PROTO_GMTP", 101: "IP_PROTO_IFMP", 102: "IP_PROTO_PNNI",
                                 103: "IP_PROTO_PIM", 104: "IP_PROTO_ARIS", 105: "IP_PROTO_SCPS", 106: "IP_PROTO_QNX",
                                 107: "IP_PROTO_AN", 108: "IP_PROTO_IPCOMP", 109: "IP_PROTO_SNP", 110: "IP_PROTO_COMPAQPEER",
                                 111: "IP_PROTO_IPXIP", 112: "IP_PROTO_VRRP", 113: "IP_PROTO_PGM", 114: "IP_PROTO_ANY0HOP",
                                 115: "IP_PROTO_L2TP", 116: "IP_PROTO_DDX", 117: "IP_PROTO_IATP", 118: "IP_PROTO_STP",
                                 119: "IP_PROTO_SRP", 120: "IP_PROTO_UTI", 121: "IP_PROTO_SMP", 122: "IP_PROTO_SM",
                                 123: "IP_PROTO_PTP", 124: "IP_PROTO_ISIS", 125: "IP_PROTO_FIRE", 126: "IP_PROTO_CRTP",
                                 127: "IP_PROTO_CRUDP", 128: "IP_PROTO_SSCOPMCE", 129: "IP_PROTO_IPLT", 130: "IP_PROTO_SPS",
                                 131: "IP_PROTO_PIPE", 132: "IP_PROTO_SCTP", 133: "IP_PROTO_FC"
                                 }
        """
        熟知端口，数值一般为0-1023.标记常规的服务进程；
        登记端口号，数值为1024-49151，标记没有熟知端口号的非常规的服务进程，
        使用这个范围的端口号必须在IANA登记，以防止重复；
        客户端口号或短暂端口号，数值为49152-65535，留给客户进程选择暂时使用
        """
        self.tcpudp_payload_proto = {22: "TSshDecode", 23: "TTelnetDecode",53: "UDnsDecode",
                                     80: "THttpDecode", 69: "UTftpDecode", 213: "UIpxDecode",
                                     546: "U6DhcpDecode", 547: "U6ServDhcpDecode", 3306: "TUMysqlDecode",
                                     5050: "TYahooDecode", 5060: "TSessionDecode", 8000: "UOicqDecode",
                                     11211: "MemchachedDecode",67: "UCltDhcpDecode", 68: "UServDhcpDecode"
                                     }
#        self.pppoe_payload_proto = {1: "IpDecode"}
        self.pppoe_payload_proto = {1: "PppDecode"}
        self.ppp_payload_proto = {33: "IpDecode"}
        self.retdata = {}
    def decode_data(self):
        pass

    def trans_data(self):
        pass