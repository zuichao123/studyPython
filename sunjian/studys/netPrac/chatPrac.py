#coding:utf-8
'''
    多线程聊天室
'''
from socket import *
from threading import Thread

# 收数据，然后打印
def receiveData():
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        print("\r>>%s%s"%(str(recvInfo[1]), recvInfo[0].decode('utf-8')+"\n<<"))

# 检测键盘输入，然后发送
def sendData():
    while True:
        sendData = input('<<')
        udpSocket.sendto(bytes(sendData.encode('utf-8')),(destIp,destPort))

def main():
    global udpSocket
    global destIp
    global destPort

    destIp = input('please input receive ip:')
    destPort = int(input('please inpu receive port:'))

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(('',7890))

    tr = Thread(target=receiveData) # 接收任务线程
    ts = Thread(target=sendData) # 发送任务线程

    tr.start()
    ts.start()

    tr.join()
    ts.join()

if __name__ == "__main__":
    main()