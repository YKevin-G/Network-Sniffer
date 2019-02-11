import socket
from dpkt.compat import compat_ord
import struct
class MacIpAddrConver:
    def mac_addr(address):
        return ':'.join('%02x' % compat_ord(b) for b in address)
    #  %02x' ：表示输出 两位十六进制，字母小写空缺补零
    """Convert a MAC address to a readable/printable string

       Args:
           address (str): a MAC address in hex form (e.g. '\x01\x02\x03\x04\x05\x06')
       Returns:
           str: Printable/readable MAC address
    """


    def inet_to_str(inet):
        try:
            return socket.inet_ntop(socket.AF_INET, inet)
        except ValueError:
            return socket.inet_ntop(socket.AF_INET6, inet)
    """Convert inet object to a string

        Args:
            inet (inet struct): inet network address
        Returns:
            str: Printable/readable IP address
    """
    # First try ipv4 and then ipv6
    def intnum_to_ipaddr(num):
        ip = socket.inet_ntoa(struct.pack('I', socket.htonl(num)))
        return ip

    def ipaddr_to_intnum(ipaddr):
        num = socket.ntohl(struct.unpack("I", socket.inet_aton(str(ipaddr)))[0])
        return num
