class HttpHeaderDecode(object):
    def __init__(self, data):
        self.header = str(data)
        if self.header == "OrderedDict()":
            self.header = "OrderedDict([('Info', 'Wrong')])"
        self.sp1str = self.header.split("[")
        self.sp2str = self.sp1str[1].split("]")
        self.raw_info = self.sp2str[0]
#        raw_info = self.sp2str[0]  # 要处理的字段
        # 括号匹配
        self.rmark = [")", "]", "}"]
        self.lmark = ["(", "[", "{"]
        self.dic = {')': '(', ']': '[', '}': '{'}
        self.inputmark = []
        self.inputvalue = []
        self.ripe_info = []
        self.riper_info = []
        self.headerdatadict = {}
    def HttpHeaderDecode(self):
        i = 0  # 来记录由raw_info可以分成几行数据
        for ch in self.raw_info:
#        for ch in self.header:
            if ch in self.lmark:
                self.inputmark.append(ch)
                self.inputvalue.append(ch)
            elif ch in self.rmark:
                if self.inputmark[-1] in self.lmark and self.inputmark[-1] != self.dic[ch]:
                    break
                elif self.inputmark[-1] == self.dic[ch] and len(self.inputmark) == 1:
                    self.ripe_info.append([])
                    self.inputmark.pop()
                    self.ripe_info[i].append(ch)
                    fraglen = len(self.inputvalue)
                    for dd in range(len(self.inputvalue)):
                        if (dd == (fraglen - 1) and self.inputvalue[-1] == ",") or (dd == (fraglen - 2) and self.inputvalue[-1] == " "):
                            self.inputvalue.pop()
                        else:
                            self.ripe_info[i].append(self.inputvalue.pop())
                    i += 1
                elif self.inputmark[-1] == self.dic[ch] and len(self.inputmark) > 1:
                    self.inputmark.pop()
                    self.inputvalue.append(ch)
            else:
                self.inputvalue.append(ch)
        num = 0  # 同上面的i
        for line in self.ripe_info:
            line.reverse()
            self.riper_info.append([])
            self.riper_info[num] = ''.join(line)
#            print(self.riper_info[num])
            num += 1
        # 将列表中的数据去掉括号，引号，存入到字典中去
        for line in self.riper_info:
            ss = line.lstrip("('")  # 去掉左括号 和 左引号
            dd = ss.rstrip("')")  # 去掉右括号 和 右引号
            ee = dd.split(",")[0].strip("'")  # 去掉中间的引号
#            print(ee)  字典的键
#            print(dd[len(ee) + 4:])    字典的值
            self.headerdatadict[ee] = dd[len(ee) + 4:]
        return self.headerdatadict