import pcapy
import dpkt
from Parse.ProtoFactory.DataLinkLevel.EthernetDecode import EthernetDecode
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver
import six
import struct, socket

dhcp_type = {1: "DHCP_OP_REQUEST", 2: "DHCP_OP_REPLY"}
dhcp_opt = {1: "DHCP_OPT_NETMASK", 2: "DHCP_OPT_TIMEOFFSET"
, 3: "DHCP_OPT_ROUTER",
4:"DHCP_OPT_TIMESERVER",
5:"DHCP_OPT_NAMESERVER",
6:"DHCP_OPT_DNS_SVRS",
7: "DHCP_OPT_LOGSERV",
8: "DHCP_OPT_COOKIESERV",
9: "DHCP_OPT_LPRSERV",
10: "DHCP_OPT_IMPSERV",
11: "DHCP_OPT_RESSERV",
12: "DHCP_OPT_HOSTNAME",
13: "DHCP_OPT_BOOTFILESIZ",
14: "DHCP_OPT_DUMPFILE",
15: "DHCP_OPT_DOMAIN ",
16: "DHCP_OPT_SWAPSERV",
17: "DHCP_OPT_ROOTPATH",
18: "DHCP_OPT_EXTENPATH",
19: "DHCP_OPT_IPFORWARD",
20: "DHCP_OPT_SRCROUT",
21: "DHCP_OPT_POLICYFILTER",
22: "DHCP_OPT_MAXASMSIZE",
23: "DHCP_OPT_IPTTL",
24: "DHCP_OPT_MTUTIMEOUT",
25: "DHCP_OPT_MTUTABLE",
26: "DHCP_OPT_MTUSIZE",
27: "DHCP_OPT_LOCALSUBNETS",
28: "DHCP_OPT_BROADCASTADDR",
29: "DHCP_OPT_DOMASKDISCOV ",
30: "DHCP_OPT_MASKSUPPLY",
31: "DHCP_OPT_DOROUTEDISC",
32: "DHCP_OPT_ROUTERSOLICIT",
33: "DHCP_OPT_STATICROUTE",
34: "DHCP_OPT_TRAILERENCAP",
35: "DHCP_OPT_ARPTIMEOUT",
36: "DHCP_OPT_ETHERENCAP",
37: "DHCP_OPT_TCPTTL",
38: "DHCP_OPT_TCPKEEPALIVE",
39: "DHCP_OPT_TCPALIVEGARBAGE",
40: "DHCP_OPT_NISDOMAIN",
41: "DHCP_OPT_NISSERVERS",
42: "DHCP_OPT_NISTIMESERV",
43: "DHCP_OPT_VENDSPECIFIC",
44: "DHCP_OPT_NBNS",
45: "DHCP_OPT_NBDD",
46: "DHCP_OPT_NBTCPIP",
47: "DHCP_OPT_NBTCPSCOPE",
48: "DHCP_OPT_XFONT",
49: "DHCP_OPT_XDISPLAYMGR",
50: "DHCP_OPT_REQ_IP",
51: "DHCP_OPT_LEASE_SEC",
52: "DHCP_OPT_OPTIONOVERLOAD",
53: "DHCP_OPT_MSGTYPE",
54: "DHCP_OPT_SERVER_ID",
55: "DHCP_OPT_PARAM_REQ",
56: "DHCP_OPT_MESSAGE",
57: "DHCP_OPT_MAXMSGSIZE",
58: "DHCP_OPT_RENEWTIME",
59: "DHCP_OPT_REBINDTIME",
60: "DHCP_OPT_VENDOR_ID",
61: "DHCP_OPT_CLIENT_ID",
64: "DHCP_OPT_NISPLUSDOMAIN",
65: "DHCP_OPT_NISPLUSSERVERS",
68: "DHCP_OPT_MOBILEIPAGENT",
69: "DHCP_OPT_SMTPSERVER",
70: "DHCP_OPT_POP3SERVER",
71: "DHCP_OPT_NNTPSERVER",
72: "DHCP_OPT_WWWSERVER",
73: "DHCP_OPT_FINGERSERVER",
74: "DHCP_OPT_IRCSERVER",
75: "DHCP_OPT_STSERVER",
76: "DHCP_OPT_STDASERVER",
81: '\x03\xff\xffDESKTOP-FT2CVVA'
}

def parse_pkt(hdr, data):
    print(data)
"""
    eth = dpkt.ethernet.Ethernet(data)
    ii = EthernetDecode(eth)
    pppoedata, iis = ii.decode_data()
    pppdata = pppoedata.data
    if pppdata.p != 31:
        print("31 wrong")
        return
    tcpdata = pppoedata.data.data.data
    if tcpdata.sport ==80 or tcpdata.dport ==80:
        httpdata = tcpdata.data
    else:
        return None, None
    try:
        httpz = dpkt.http.Request(httpdata)
        if httpz.method == 'GET':
            print(httpz.uri)
            print(httpz.version)
            print(httpz.method)
            print(httpz.headers)
            for word in httpz.headers:
                print(word)
            print(httpz.body)
    except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
            return None,None


                # 解析IP协议

"""


#    pppoedata, iis = ii.decode_data()
#    print("------------------------------------------------------------------------------", iis)
#    if iis != "PppoeDecode":
#        return None
#    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", iis)
#    pppdata=pppoedata.data
#    ipdata = pppdata.data
#    tcpdata = ipdata.data

"""
    ipdata, iis = ii.decode_data()
    tcpdata=ipdata.data
    if isinstance(ipdata.data, dpkt.udp.UDP):
        print("666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666")
        httpdata = tcpdata.data
        if tcpdata.sport == 67 or tcpdata.dport == 68:
            print("well!!!!")
            try:
                a = dpkt.dhcp.DHCP(httpdata)
                print("Type of Pkt: ", dhcp_type[a.op])
                print("Type of Hardware: ", a.hrd)
                print("Type of Hardaddress Length: ", a.hln)
                print("Hops: ", a.hops)
                print("Transaction ID: ", a.xid)
                # 事务ID，随机数，有客户端生成，服务器Reply时，
                # 会把Request中的Transaction拷贝到Reply报文中
                print("Seconds after send ip request: ", a.secs)
                print("Flags: ", a.flags)  # 1代表广播
                print("Client IP Address: ", MacIpAddrConver.intnum_to_ipaddr(a.ciaddr))
                print("Your IP Address: ", MacIpAddrConver.intnum_to_ipaddr(a.yiaddr))
                # Your IP Address： 服务器想客户端提供IP地址时，会把IP地址填入本字段
                print("(Next)Server IP Address: ", MacIpAddrConver.intnum_to_ipaddr(a.siaddr))
                # （Next）Server IP Address：客户端引导时需要的另一个服务器的IP地址
                print("Gateway （Relay） IP Address: ", MacIpAddrConver.intnum_to_ipaddr(a.giaddr))
                # int 转 byte: bytes((196,))
                # 网关（中继）IP地址，有DHCP 中继器在转发DHCP报文的时候填入
                print("Client Hardware Address: ", MacIpAddrConver.mac_addr(a.chaddr))
                print("Server Name: ",  a.sname)
                # Server名字，有64bytes，一般不使用，填充为0
                print("Boot File name: ", a.file)
                # Boot File name： boot file的路径，128bytes， 一般不使用，填充为0
                print("Magic ??: ", a.magic)
                # !!!WHAT????????
                print("Option: ")
                print(a.opts)
                for i in range(len(a.opts)):
                    print(dhcp_opt[a.opts[i][0]] + " : " + "(" + str(a.opts[i][0]) + ")")
                    print( a.opts[i])
#                    print("Option: ", a.opts)
            except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                return None
"""

if __name__ == "__main__":
    dev = pcapy.findalldevs()
    print(dev)
    cap = pcapy.open_live(dev[1], 1500, 0, 50)
    cap.setfilter('')
    cap.loop(-1, parse_pkt)