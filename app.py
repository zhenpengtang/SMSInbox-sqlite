import tornado.ioloop
import tornado.web
import yaml
from module.db_control import db

f=open("config.yaml")
config=yaml.load(f)
db=db(config["sms_sqlite3"])



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_argument("get_token")==config["get_token"]:
            sms_list = db.read_sms()
            sms_list.reverse()
            self.render("templates/test.html",smslist=sms_list)

    def post(self):
        #print self.request.body
        if self.get_argument("post_token")==config["post_token"]:
            phone=self.get_argument("number")#.encode("utf-8")
            datetime=self.get_argument("datetime")#.encode("utf-8")
            body=self.get_argument("text")#.encode("utf-8")
            #print body
            db.write_sms(phone,datetime,body)


class SmsHandler(tornado.web.RequestHandler):
    def get(self):
        sms_list=getSMSList()
        sms_test_list=get_the_test_sms(sms_list)
        self.render("templates/test.html",smslist=sms_test_list)

application = tornado.web.Application([
    (r"/test", MainHandler),
	(r"/showyoursms",SmsHandler),
    (r"/(apple-touch-icon-120x120\.png)", tornado.web.StaticFileHandler, {"path": "static/apple-touch-icon"}),
    (r"/(apple-touch-icon-120x120-precomposed\.png)", tornado.web.StaticFileHandler, {"path": "static/apple-touch-icon"}),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "static/css"}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "static/js"}),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

