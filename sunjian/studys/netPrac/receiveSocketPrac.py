#coding:utf-8
'''
    socket 套接字
        接收
    接收方需要绑定
'''
from socket import *

# 1、创建套接字
udpsocket = socket(AF_INET, SOCK_DGRAM)

# 2、 绑定地址和接收端口
udpsocket.bind(('',7890))

# 3、 接收
recviceData = udpsocket.recvfrom(1024) # 表示本次接收的最大字节；接收的是一个元组

# 3.5、 将接收到的信息再发送给对方
# udpsocket.sendto(recviceData[0],recviceData[1])

# 4、 输出内容
recv_msg = recviceData[0]
send_addr = recviceData[1]
print("发送地址：%s\n接收内容：%s"%(str(send_addr), recv_msg.decode('utf-8')))

# 5、 关闭
# udpsocket.close()