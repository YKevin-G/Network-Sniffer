from Parse.ProtoFactory.AbstrFactory.AbstrProto import DecodeProto
from Parse.ProtoFactory.PublicFunc.MacIpAddrConver import MacIpAddrConver
from Parse.ProtoFactory.PublicFunc.HttpHeaderDecode import HttpHeaderDecode
import dpkt


class ResTHttpDecode(DecodeProto):
    def __init__(self, data):
        super().__init__(data)
        self.retheaddata = {}
        self.fakeretdata = {"info": "undecode"}

    def decode_data(self):
        try:
            self.httpdata = dpkt.http.Response(self.data)
        except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
            return None,None,self.fakeretdata,"reshttp"
        headerdata = HttpHeaderDecode(self.httpdata.headers)
        self.header_data = headerdata.HttpHeaderDecode()
#       self.header_data = HttpHeaderDecode.HttpHeaderDecode(self.data.header)
        self.headerdatakey = self.header_data.keys()
        self.retdata["version"] = ("Response Http Version: "+ str(self.httpdata.version))
        self.retdata["status"] = ("Response Http Status: " + str(self.httpdata.status))
        self.retdata["reson"] = ("Response Http Reason: "+self.httpdata.reason)
        self.retdata["body"] = ("Resquest Http Body: " + str(self.httpdata.body))
        # print("Response Http Version: ", self.httpdata.version)
        # print("Response Http Status: ", self.httpdata.status)
        # print("Response Http Reason: ", self.httpdata.reason)
        # print("Response Http Body: ", str(self.httpdata.body))

        # for key in self.headerdatakey:
        #     print(key + ": " + self.header_data[key])
        return None,None, self.retdata, "reshttp"
"""
    def decode_data(self):
        try:
            self.httpdata = dpkt.http.Response(self.data)
        except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
            return None,None
        self.data = dpkt.http.Message(self.data)
        self.header_data = HttpHeaderDecode.HttpHeaderDecode(self.data.header)
        self.headerdatakey = self.header_data.keys()

        print("Response Http Version: ", self.httpdata.version)
        print("Response Http Status: ", self.httpdata.status)
        print("Response Http Reason: ", self.httpdata.reason)
        for key in self.headerdatakey:
            print(key + " : " + self.header_data[key])
        print("Response Http Body: ", self.httpdata.body)
        return None,None
"""
