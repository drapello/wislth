import tornado.ioloop
import tornado.web
from app.handlers import url_specs

application = tornado.web.Application(url_specs())

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()