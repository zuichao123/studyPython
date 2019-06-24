# coding:utf-8
"""
    IOLoop.current()
        返回当前线程的IOLoop实例。

    IOLoop.start()
            启动IOLoop实例的I/O循环,同时服务器监听被打开。
"""
import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    """主页处理类"""

    def get(self):
        """对应http的get请求方式"""
        self.write("hello sunjian!")



if __name__ == "__main__":
    app = tornado.web.Application([(r"/", IndexHandler)]) # 实例化一个服务器对象，映射
    app.listen(9000) # 监听端口
    tornado.ioloop.IOLoop.current().start()
