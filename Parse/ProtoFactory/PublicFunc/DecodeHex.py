"""
class DecodeHex:
    def __init__(self,data):
        self.data = data
        b = self.data.split('"')
        c = b[1].split("\\")
        i = 0
        for ch in c:
            if len(ch) == 0:
                break
            if ch[0] == "x":
                if len(ch) >= 2:
                    c[i] = ch[1:3]
                    print(ch)
                else:
                    c[i] = " "
            else:
                c[i] = " "
            i += 1
        self.realdata = []
        for i in range(len(c)):
            if c[i] != " ":
                self.realdata.append(c[i])
    def retdata(self):
        print(self.realdata)
        return self.realdata
"""
import binascii
class DecodeHex:
    def __init__(self, data):
        self.data = data
        self.retascdata = []
    def hex2data(self):
        self.retsingledata = binascii.b2a_hex(self.data)
        for i in range(0,len(self.retsingledata),2):
            c = self.retsingledata[i:i+2]
            self.retascdata.append(chr(int(c,16)))
        return self.retascdata,self.retsingledata

