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
            sms_list = db.get_all_numbers_one_sms(db.read_sms())
            sms_list.reverse()
            self.render("templates/test.html",smslist=sms_list,get_token=config["get_token"])

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
        sms_test_list=db.get_all_numbers_one_sms()
        sms_test_list.reverse()
        self.render("templates/test.html",smslist=sms_test_list)

class NumberHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_argument("get_token")==config["get_token"] and self.get_argument("number")!="":
            number=self.get_argument("number")
            sms_list = db.read_sms()
            sms_list.reverse()
            number_list=[]
            for k in sms_list:
                if k[0]==number:
                    number_list.append(k)
            self.render("templates/number.html",
                        smslist=number_list,
                        title=number)

application = tornado.web.Application([
    (r"/test", MainHandler),
	(r"/showyoursms",SmsHandler),
    (r"/number",NumberHandler),
    (r"/(apple-touch-icon-120x120\.png)", tornado.web.StaticFileHandler, {"path": "static/apple-touch-icon"}),
    (r"/(apple-touch-icon-120x120-precomposed\.png)", tornado.web.StaticFileHandler, {"path": "static/apple-touch-icon"}),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "static/css"}),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "static/js"}),
])

if __name__ == "__main__":
    application.listen(7777)
    tornado.ioloop.IOLoop.instance().start()

