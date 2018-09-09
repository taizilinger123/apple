#-*-coding:utf-8-*-
import os
import  socket
server = socket.socket()
server.bind(('localhost',6969)) #绑定要监听端口
server.listen(5) #监听

print("我要开始等电话了")
while True:
        conn, addr = server.accept()  # 等电话打进来
        # conn就是客户端连过来而在服务器端为其生成的一个连接实例
        print(conn, addr)
        print("电话来了")
        while True:
            data = conn.recv(1024)
            print("recv:",data)
            if not data:
                print("client has lost...")
                break
            # res = os.popen(data).read()
            # conn.send(res)
            f = open("oldboy-1.avi")
            data = f.read()
            print(len(data))
            conn.sendall(data)
server.close()

