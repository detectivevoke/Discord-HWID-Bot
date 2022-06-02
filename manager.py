import sqlite3

class Manage(object):
    def __init__(self):
        
        self.db = sqlite3.connect("database.db")
        self.cursor = self.db.cursor()
        self.cursor.execute("""CREATE TABLE  IF NOT EXISTS database (
            hwid text,
            ip text,
            cname text
            )""")

    def insert(self, hwid, ip, cname):
        try:
            with self.db:
                self.cursor.execute("INSERT INTO database VALUES (:hwid, :ip, :cname)", {'hwid': hwid, 'ip': ip, "cname": cname})
            return True
        except Exception as e:
            print(e)
            return False

    def get(self, type, arg):
        try:
            if str(type).lower() == "ip":t="ip"
            elif str(type).lower()=="hwid": t="hwid"
            elif str(type).lower()=="cname": t="cname"
            with self.db:
                if t=="hwid":self.cursor.execute("SELECT * FROM database WHERE hwid=:hwid", {'hwid': arg})
                elif t=="ip": self.cursor.execute("SELECT * FROM database WHERE ip=:ip", {'ip': arg})
                elif t=="cname": self.cursor.execute("SELECT * FROM database WHERE cname=:cname", {'cname': arg})
                return self.cursor.fetchall()
        except Exception as e:
            return e

    def remove(self, type, arg):
        try:
            if str(type).lower() == "ip":t="ip"
            elif str(type).lower()=="hwid": t="hwid"
            elif str(type).lower()=="cname": t="cname"
            with self.db:
                if t=="hwid":self.cursor.execute("DELETE from database WHERE hwid = :hwid", {'hwid': arg})
                elif t=="ip": self.cursor.execute("DELETE from database WHERE hwid ip=:ip", {'ip': arg})
                elif t=="cname": self.cursor.execute("DELETE from database WHERE hwid cname=:cname", {'cname': arg})
                return self.cursor.fetchall()
        except Exception as e:
            return e