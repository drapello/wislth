import tornado.ioloop
import tornado.web
from app.handlers import url_specs

# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")

# application = tornado.web.Application([
#     (r"/", MainHandler),
# ])

application = tornado.web.Application(url_specs())

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()