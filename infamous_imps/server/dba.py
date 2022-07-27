import os
from os.path import exists
import sqlite3

def start():
        if(exists("data.db")):
            pass
        else:
            f = open("data.db","w")
            f.close()
            con = sqlite3.connect("data.db")
            cur = con.cursor()
            cur.execute('''CREATE TABLE chat
               (user text,timestamp real,message text)''')
            cur.execute('''CREATE TABLE auth
               (user text, password text)''')
            con.commit()
            con.close()
start()
def add_message(server,timestamp,user,text):
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    cur.execute("insert into chat values (?,?,?)", (user,timestamp,text))
    con.commit()
    con.close()
def add_user(name,hashed):
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    cur.execute("insert into auth values (?,?)", (name,hashed))
    con.commit()
    con.close()
def delete_user(name,hashed):
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    print(name)
    name = (name,)
    cur.execute(f'DELETE from auth where user =?',name)
    con.commit()
    con.close()
def see_message(self,server):
            return cur.execute('SELECT * FROM server ORDER BY timestamp')
def check_user(name,hashed):
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    name = (name,)
    c = cur.execute(f'SELECT * FROM auth where user = ?',name)
    ok = c.fetchall()[0][1]
    con.commit()
    con.close()
    if(ok == hashed):
        return True
    else:
        return False
def update_user_name(name,hashed,new_name):
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    ok = check_user(name, hashed)
    name = (new_name,hashed)
    print(ok)
    if(ok):
     cur.execute(f'UPDATE auth set user = ? where password =?',name)
     con.commit()
    con.close()
def update_password(name,hashed,password):
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    print(name,hashed)
    ok = check_user(name,hashed)
    name = (password,name)
    print(ok)
    if(ok):
     cur.execute(f'UPDATE auth set password = ? where user =?',name)
     con.commit()
    con.close()
#print(check_user("Balasai","1915132696"))
print(update_password("iasalab", "1915132696","iasalab"))  