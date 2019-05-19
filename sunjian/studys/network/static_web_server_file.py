#coding:utf-8
'''
    静态页面的web服务器
'''
import socket
import re

from multiprocessing import Process

# 设置静态文件根目录
HTML_ROOT_DIR = "./html"

class HTTPServer(object):
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        while True:
            client_socket, client_address = self.server_socket.accept()  # 接收请求
            print("[%s,%s]用户连接上了" % client_address)

            handle_client_process = Process(target=self.handle_client, args=(client_socket,))  # 创建进程
            handle_client_process.start()  # 开启进程
            client_socket.close()  # 关闭socket

    def handle_client(self,client_socket):
        '''处理客户端请求'''
        # 获取客户端请求数据
        request_data = client_socket.recv(1024)
        print("request data", request_data)

        request_lines = request_data.splitlines() # 换行截取请求数据
        for line in request_lines:
            print(line) # 输出截取的内容


        # 解析报文
        request_start_line = request_lines[0] # 获取截取的第一个
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1) # 获取匹配的第一组内容

        if "/" == file_name:
            file_name = "/index.html"

        try:
            # 打开文件，读取内容
            file = open(HTML_ROOT_DIR + file_name, "rb")
        except IOError:
            response_start_line = "HTTP/1.1 404 Not Found\r\n"
            response_headers = "Server: My server\r\n"
            response_body = "The file is not found!"
        else:
            file_data = file.read()
            file.close()

            # 构造响应数据
            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_headers = "Server:My server\r\n"
            response_body = file_data.decode("utf-8")

        response = response_start_line + response_headers + "\r\n" + response_body
        print("response data:", response)

        # 向客户端返回响应数据
        client_socket.send(bytes(response, "utf-8"))

        # 关闭客户端连接
        client_socket.close()

    def bind(self,port):
        self.server_socket.bind(("", port))
        self.server_socket.listen(128)


def main():
    http = HTTPServer()
    http.bind(25668)
    http.start()


if __name__ == "__main__":
    main()