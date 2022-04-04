import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS ise (id INTEGER PRIMARY KEY, name TEXT, USN integer,gender text, phone integer,teacher text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS cse (id INTEGER PRIMARY KEY, name TEXT, USN integer, gender text,phone integer,teacher text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS civil (id INTEGER PRIMARY KEY, name TEXT, USN integer,gender text,phone integer,teacher text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS mech (id INTEGER PRIMARY KEY, name TEXT, USN integer,gender text,phone integer,teacher text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS Attendace (id INTEGER PRIMARY KEY, name TEXT, Attendance integer,time text)")
        self.conn.commit()

    def insert(self,name,usn,gender,phone,teacher):
       
        self.cur.execute("INSERT INTO ise VALUES (NULL,?,?,?,?,?)",(name,usn,gender,phone,teacher))
        self.conn.commit()

    def insertatt(self,name,atten,tim):
       
        self.cur.execute("INSERT INTO Attendace VALUES (NULL,?,?,?)",(name,atten,tim))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM ise")
        rows = self.cur.fetchall()
        return rows

    def search(self,name="",usn="",gender="",phone="",teacher=""):
        self.cur.execute("SELECT * FROM ise WHERE name =? OR USN =? OR gender =? OR phone = ? OR teacher = ?",(name,usn,gender,phone,teacher))
        rows = self.cur.fetchall()
        return rows

    def delete(self,table_name,id):
        self.cur.execute("DELETE FROM ise WHERE id = ?",(id))
        self.conn.commit()

    def update(self,id,name,usn,gender,phone,teacher):
        self.cur.execute("UPDATE ise SET name =?, USN=?, gender=?, phone = ?, teacher = ? WHERE id= ?",(name,usn,gender,phone,teacher,id))
        self.conn.commit()

    def tableview(self):
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' ")
        rows = self.cur.fetchall()
        return rows
    
    def desctable(self,table_name):
        self.cur.execute("PRAGMA table_info('%s')" % table_name)
        rows = self.cur.fetchall()
        return rows

    def aisview(self):
        self.cur.execute("SELECT * FROM Attendace")
        rows = self.cur.fetchall()
        return rows        
    
    def __del__(self):
        self.conn.close()


