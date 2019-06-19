# coding:utf-8
"""
    手动实现http服务器示例并绑定到给定端口
"""
import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    """主页处理类"""

    def get(self):
        """对应http的get请求方式"""
        self.write("hello sunjian2!")



if __name__ == "__main__":
    app = tornado.web.Application([(r"/", IndexHandler)]) # 实例化一个服务器对象，映射
    # ----------------------------------------
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(9000) # 监听端口
    # ----------------------------------------
    tornado.ioloop.IOLoop.current().start()
