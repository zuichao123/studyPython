# coding:utf-8
"""
    tornado学习之options
        从配置文件导入option
"""
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

from ..options import config3


class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self):
        """对应http的get请求"""
        self.write("hello sunjian!")


if __name__ == "__main__":
    app = tornado.web.Application([], **config3.settings)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()