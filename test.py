
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self,hello):
        self.write(self.request.body)
        print hello

application = tornado.web.Application([
    (r"/(.*)", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()