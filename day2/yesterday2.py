#f = open("yesterday2",'r+',encoding="utf-8")#文件句柄  读写
#f = open("yesterday2",'a+',encoding="utf-8")#文件句柄  追加读写
#f = open("yesterday2",'w+',encoding="utf-8")#文件句柄  写读
'''f = open("yesterday2",'rb')#文件句柄  二进制文件
print(f.readline())
print(f.readline())
print(f.readline())'''
f = open("yesterday2",'wb')
f.write("hello binary\n".encode())
f.close()
'''f.write("---------------------diao---------------1\n")
f.write("---------------------diao---------------1\n")
f.write("---------------------diao---------------1\n")
f.write("---------------------diao---------------1\n")
print(f.tell())
f.seek(10)
print(f.tell())
print(f.readline())
f.write("should be at the beginning of the second line")
f.close()'''

'''print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.write("-----------------diao----------------")
print(f.readline())'''

'''print(f.tell())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.seek(3)
print(f.readline())

print(f.encoding)
print(f.fileno())
#print(f.flush())
print(dir(f.buffer))'''