#coding:utf-8
'''
    固定返回值的web服务器
'''
import socket

from multiprocessing import Process


def handle_client(client_socket):
    '''处理客户端请求'''
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    print("request data", request_data)

    # 构造响应数据
    response_start_line = "HTTP/1.1 OK\r\n"
    response_headers = "Server:My server\r\n"
    response_body = "lalalallallalalalala"
    response = response_start_line + response_headers + "\r\n" + response_body
    print("response data:", response)

    # 向客户端返回响应数据
    client_socket.send(bytes(response, "utf-8"))

    # 关闭客户端连接
    client_socket.close()

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(("",8000))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept() # 接收请求
        print("[%s,%s]用户连接上了"%client_address)

        handle_client_process = Process(target=handle_client,args=(client_socket,)) # 创建进程
        handle_client_process.start() # 开启进程
        client_socket.close() # 关闭socket