from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver


class UServDhcpdecode(DecodeProto):
    def __init__(self, data):
        super().__init__(data)
        self.dhcp_opt = {1: "DHCP_OPT_NETMASK", 2: "DHCP_OPT_TIMEOFFSET", 3: "DHCP_OPT_ROUTER",
                    4: "DHCP_OPT_TIMESERVER", 5: "DHCP_OPT_NAMESERVER",6: "DHCP_OPT_DNS_SVRS",
                    7: "DHCP_OPT_LOGSERV", 8: "DHCP_OPT_COOKIESERV", 9: "DHCP_OPT_LPRSERV",
                    10: "DHCP_OPT_IMPSERV", 11: "DHCP_OPT_RESSERV", 12: "DHCP_OPT_HOSTNAME",
                    13: "DHCP_OPT_BOOTFILESIZ", 14: "DHCP_OPT_DUMPFILE", 15: "DHCP_OPT_DOMAIN ",
                    16: "DHCP_OPT_SWAPSERV", 17: "DHCP_OPT_ROOTPATH", 18: "DHCP_OPT_EXTENPATH",
                    19: "DHCP_OPT_IPFORWARD", 20: "DHCP_OPT_SRCROUT", 21: "DHCP_OPT_POLICYFILTER",
                    22: "DHCP_OPT_MAXASMSIZE", 23: "DHCP_OPT_IPTTL",  24: "DHCP_OPT_MTUTIMEOUT",
                    25: "DHCP_OPT_MTUTABLE", 26: "DHCP_OPT_MTUSIZE", 27: "DHCP_OPT_LOCALSUBNETS",
                    28: "DHCP_OPT_BROADCASTADDR", 29: "DHCP_OPT_DOMASKDISCOV ", 30: "DHCP_OPT_MASKSUPPLY",
                    31: "DHCP_OPT_DOROUTEDISC", 32: "DHCP_OPT_ROUTERSOLICIT", 33: "DHCP_OPT_STATICROUTE",
                    34: "DHCP_OPT_TRAILERENCAP", 35: "DHCP_OPT_ARPTIMEOUT", 36: "DHCP_OPT_ETHERENCAP",
                    37: "DHCP_OPT_TCPTTL", 38: "DHCP_OPT_TCPKEEPALIVE", 39: "DHCP_OPT_TCPALIVEGARBAGE",
                    40: "DHCP_OPT_NISDOMAIN", 41: "DHCP_OPT_NISSERVERS", 42: "DHCP_OPT_NISTIMESERV",
                    43: "DHCP_OPT_VENDSPECIFIC", 44: "DHCP_OPT_NBNS", 45: "DHCP_OPT_NBDD",
                    46: "DHCP_OPT_NBTCPIP", 47: "DHCP_OPT_NBTCPSCOPE", 48: "DHCP_OPT_XFONT",
                    49: "DHCP_OPT_XDISPLAYMGR", 50: "DHCP_OPT_REQ_IP",  51: "DHCP_OPT_LEASE_SEC",
                    52: "DHCP_OPT_OPTIONOVERLOAD", 53: "DHCP_OPT_MSGTYPE", 54: "DHCP_OPT_SERVER_ID",
                    55: "DHCP_OPT_PARAM_REQ", 56: "DHCP_OPT_MESSAGE", 57: "DHCP_OPT_MAXMSGSIZE",
                    58: "DHCP_OPT_RENEWTIME", 59: "DHCP_OPT_REBINDTIME", 60: "DHCP_OPT_VENDOR_ID",
                    61: "DHCP_OPT_CLIENT_ID", 64: "DHCP_OPT_NISPLUSDOMAIN", 65: "DHCP_OPT_NISPLUSSERVERS",
                    68: "DHCP_OPT_MOBILEIPAGENT", 69: "DHCP_OPT_SMTPSERVER", 70: "DHCP_OPT_POP3SERVER",
                    71: "DHCP_OPT_NNTPSERVER", 72: "DHCP_OPT_WWWSERVER", 73: "DHCP_OPT_FINGERSERVER",
                    74: "DHCP_OPT_IRCSERVER", 75: "DHCP_OPT_STSERVER", 76: "DHCP_OPT_STDASERVER",
                    81: '\x03\xff\xffDESKTOP-FT2CVVA'
                    }
        self.dhcp_type = {1: "DHCP_OP_REQUEST", 2: "DHCP_OP_REPLY"}

    def decode_data(self):
        self.retdata["typepkt"] = ("Type of Pkt: ", self.dhcp_type[self.data.op])
        self.retdata["hardware"] = ("Type of Hardware: ", self.dhcp_type[self.data.hrd])
        self.retdata["hardlen"] = ("Type of Hardaddress Length: ", self.dhcp_type[self.data.hln])
        self.retdata["hops"] = ("Hops: ", self.dhcp_type[self.data.hops])
        self.retdata["transactionid"] = ("Transaction ID: ", self.dhcp_type[self.data.xid])
        self.retdata["secsafterreq"] = ("Seconds after send ip request: ", self.dhcp_type[self.data.secs])
        self.retdata["flags"] = ("Flags: ", self.dhcp_type[self.data.flags])
        self.retdata["cliip"] = ("Client IP Address: ", self.dhcp_type[self.data.ciaddr])
        self.retdata["yourip"] = ("Your IP Address: ", self.dhcp_type[self.data.yiaddr])
        self.retdata["siaddr"] = ("(Next)Server IP Address: ", self.dhcp_type[self.data.siaddr])
        self.retdata["giaddr"] = ("Gateway （Relay） IP Address: ", self.dhcp_type[self.data.giaddr])
        self.retdata["chaddr"] = ("Client Hardware Address: ", self.dhcp_type[self.data.chaddr])
        self.retdata["sname"] = ("Server Name: ", self.dhcp_type[self.data.sname])
        self.retdata["file"] = ("Boot File name: ", self.dhcp_type[self.data.file])
        self.retdata["magic"] = ("Magic ??: ", self.dhcp_type[self.data.magic])
        self.retdata["option"] = ("Option: ", self.dhcp_type[self.data.opts])

        # print("Type of Pkt: ", self.dhcp_type[self.data.op])
        # print("Type of Hardware: ", self.data.hrd)
        # print("Type of Hardaddress Length: ", self.data.hln)
        # print("Hops: ", self.data.hops)
        # print("Transaction ID: ", self.data.xid)
        # # 事务ID，随机数，有客户端生成，服务器Reply时，
        # # 会把Request中的Transaction拷贝到Reply报文中
        # print("Seconds after send ip request: ", self.data.secs)
        # print("Flags: ", self.data.flags)  # 1代表广播
        # print("Client IP Address: ", MacIpAddrConver.intnum_to_ipaddr(self.data.ciaddr))
        # print("Your IP Address: ", MacIpAddrConver.intnum_to_ipaddr(self.data.yiaddr))
        # # Your IP Address： 服务器想客户端提供IP地址时，会把IP地址填入本字段
        # print("(Next)Server IP Address: ", MacIpAddrConver.intnum_to_ipaddr(self.data.siaddr))
        # # （Next）Server IP Address：客户端引导时需要的另一个服务器的IP地址
        # print("Gateway （Relay） IP Address: ", MacIpAddrConver.intnum_to_ipaddr(self.data.giaddr))
        # # int 转 byte: bytes((196,))
        # # 网关（中继）IP地址，有DHCP 中继器在转发DHCP报文的时候填入
        # print("Client Hardware Address: ", MacIpAddrConver.mac_addr(self.data.chaddr))
        # print("Server Name: ", self.data.sname)
        # # Server名字，有64bytes，一般不使用，填充为0
        # print("Boot File name: ", self.data.file)
        # # Boot File name： boot file的路径，128bytes， 一般不使用，填充为0
        # print("Magic ??: ", self.data.magic)
        # # !!!WHAT????????
        # print("Option: ")
        # print(self.data.opts)
        # for i in range(len(self.data.opts)):
        #     print(self.dhcp_opt[self.data.opts[i][0]] + " : " + "(" + str(self.data.opts[i][0]) + ")")
        #     print(self.data.opts[i])
        return None,None,self.retdata,"serdhcp"
