# coding:utf-8
"""
    tornado学习之options
        从配置文件导入option
"""
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

# 定义服务器监听端口选项
tornado.options.define("port", default=8999, type=int, help="run server on the given port.")
tornado.options.define("sunjian", default=[], type=str, multiple=True, )

class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self):
        """对应http的get请求"""
        self.write("hello sunjian!")


if __name__ == "__main__":
    tornado.options.parse_config_file("./config2.py")
    print(tornado.options.options.sunjian) # 输出多值选项
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()