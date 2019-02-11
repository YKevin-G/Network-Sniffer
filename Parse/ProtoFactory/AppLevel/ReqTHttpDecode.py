from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver
from Parse.ProtoFactory.PublicFunc.HttpHeaderDecode import HttpHeaderDecode
import dpkt


class ReqTHttpDecode(DecodeProto):
    def __init__(self, data):
        super().__init__(data)
        self.header_data = None
        self.headerdatakey = None
        self.retheaddata = {}
        self.fakeretdata = {"info" :"undecode"}


    def decode_data(self):
        try:
            self.httpdata = dpkt.http.Request(self.data)
        except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
            return None,None,self.fakeretdata,"reqhttp"
        headerdata = HttpHeaderDecode(self.httpdata.headers)
        self.header_data = headerdata.HttpHeaderDecode()
#       self.header_data = HttpHeaderDecode.HttpHeaderDecode(self.data.header)
        self.headerdatakey = self.header_data.keys()
        self.retdata["method"] = ("Resquest Http Method: "+ str(self.httpdata.method))
        self.retdata["uri"] = ("Resquest Http Uri: " + self.httpdata.uri)
        self.retdata["version"] = ("Resquest Http Version: "+self.httpdata.version)
        self.retdata["body"] = ("Resquest Http Body: " + self.httpdata.body)
        print("Resquest Http Method: ", self.httpdata.method)
        print("Resquest Http Uri: ", self.httpdata.uri)
        print("Resquest Http Version: ", self.httpdata.version)
        print("Resquest Http Body: ", self.httpdata.body)
#       print("Resquest Http Reason: ", self.httpdata.reason)
        for key in self.headerdatakey:
            print(key + ": " + self.header_data[key])
            self.retheaddata[(key +": ")] = self.header_data[key]
        self.retdata["headerdata"] = self.retheaddata
        # 写返回值时顺便把 协议名称返回
        return None,None,self.retdata, "reqhttp"
"""
    def decode_data(self):
        print("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
        try:
            httpz = dpkt.http.Request(self.data)
            if httpz.method == 'GET':
                print(httpz.uri)
                print(httpz.version)
                print(httpz.method)
                print(httpz.headers)
                for word in httpz.headers:
                    print(word)
                print(httpz.data)
        except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
            return None,None
"""