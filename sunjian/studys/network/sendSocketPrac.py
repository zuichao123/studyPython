#coding:utf-8
'''
    socket 套接字
        发送
'''
import socket
# ------------tcp 套接字
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ------------udp 套接字
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ----------------prac1.sh
from socket import *
# 1、创建套接字
udpsocket = socket(AF_INET, SOCK_DGRAM)

# 2、准备接收方的地址，端口
sendAddr = ('127.0.0.1',7890)

# 3、从键盘获取数据
sendData = (input('请输入：'))

# 4、发送数据到指定的电脑上
udpsocket.sendto(bytes(sendData.encode('utf-8')),sendAddr)

# 5、关闭套接字
# udpsocket.close()