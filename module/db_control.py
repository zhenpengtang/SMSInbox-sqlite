import sqlite3

#db_file="sms.db"
#db_file="sms.db"
class db():
    def __init__(self,db_file):
        self.db_file=db_file

    def write_sms(self,phone,datetime,body):
        data=(phone,datetime.replace(".",":"),body)
        con = sqlite3.connect(self.db_file)
        cu = con.cursor()
        #cu.execute("create table inbox(phone text,datetime text,body text)")
        cu.execute("insert into inbox values (?,?,?)",data)
        con.commit()
        con.close()

    def read_sms(self):
        con=sqlite3.connect(self.db_file)
        cu=con.cursor()
        cu.execute("select * from inbox")
        t=cu.fetchall()
        con.close()
        return t

    def del_all(self):
        con=sqlite3.connect(self.db_file)
        cu=con.cursor()
        cu.execute("delete from inbox")
        con.commit()
        con.close()


#t=db(db_file)
#del_all()
#write_sms("10010","2017-2-11 14:09","hello world")
#print t.read_sms()




