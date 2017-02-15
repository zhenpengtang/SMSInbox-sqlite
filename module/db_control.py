import sqlite3

#db_file="sms.db"
#db_file="sms.db"
class db():
    def __init__(self,db_file):
        self.db_file=db_file
        self.number_list=[]

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

    def read_test_sms(self):
        test_list=[]
        for i in self.read_sms():
            if str(i).find("test")>=0:
                test_list.append(i)
        return test_list

    def get_all_numbers_one_sms(self,all_sms):
        all_numbers_one_sms_list=[]
        number_list=[]
        for i in all_sms:
            #print i
            if i[0] not in number_list:
                number_list.append(i[0])
                all_numbers_one_sms_list.append(i)

        return all_numbers_one_sms_list
