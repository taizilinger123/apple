#-*-coding:gbk -*-
import sys
print(sys.getdefaultencoding())

s = "你哈"    #默认是unicode
print(s.encode("gbk"))
print(s.encode("utf-8"))
print(s.encode("utf-8").decode("utf-8").encode("gb2312").decode("gb2312"))

#gbk_to_utf8 =s.encode("utf-8").decode("gbk").encode("utf-8")
#print("utf8",gbk_to_utf8)

