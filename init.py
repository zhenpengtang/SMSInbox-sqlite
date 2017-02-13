import yaml
import sqlite3

f=open("config.yaml")
config=yaml.load(f)
db=config["sms_sqlite3"]

print db
con = sqlite3.connect(db)
cu = con.cursor()
cu.execute("create table inbox(phone text,datetime text,body text)")
#cu.execute("insert into inbox values (?,?,?)", data)
con.commit()
con.close()