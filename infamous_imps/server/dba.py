from os.path import exists
import sqlite3

def start():
        # noinspection SpellCheckingInspection
        """ This programm will check if database exists in server if not create it"""
        if exists("data.db"):
            pass
        else:
            f = open("data.db","w")
            f.close()
            con = sqlite3.connect("data.db")
            cur = con.cursor()
            cur.execute('''CREATE TABLE chat
               (server text,user text,timestamp real,message text)''')
            cur.execute('''CREATE TABLE auth
               (user text, password text)''')
            con.commit()
            con.close()
start()


def add_message(server,timestamp,user,text):
    """ Adds new message to the server"""
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    cur.execute("insert into chat values (?,?,?,?)", (server,user,timestamp,text))
    con.commit()
    con.close()
        
        
def add_user(name,hashed):
    """Adds new player to the database"""
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    cur.execute("insert into auth values (?,?)", (name,hashed))
    con.commit()
    con.close()
        
def check_user(name,hashed):
    """Check if given credentials are correct"""
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    name = (name,)
    c = cur.execute('SELECT * FROM auth where user = ?',name)
    ok = c.fetchall()[0][1]
    con.commit()
    con.close()
    if ok == hashed:
        return True
    else:
        return False

def delete_user(name,hashed):
    """Deletes the user from the database"""
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    print(name)
    if check_user(name,hashed):
        name = (name,)
        cur.execute('DELETE from auth where user =?',name)
    con.commit()
    con.close()
        
def see_message(server):
    """See all message from the server"""
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    return cur.execute('SELECT * FROM chat ORDER BY timestamp where server = ?',(server,))


def update_user_name(name,hashed,new_name):
    """Update the given username"""
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    ok = check_user(name, hashed)
    name = (new_name,hashed)
    print(ok)
    if ok:
     cur.execute('UPDATE auth set user = ? where password =?',name)
     con.commit()
    con.close()


def update_password(name,hashed,password):
    """Update the given password"""
    con = sqlite3.connect("data.db") 
    cur = con.cursor()
    print(name,hashed)
    ok = check_user(name,hashed)
    name = (password,name)
    print(ok)
    if ok:
     cur.execute('UPDATE auth set password = ? where user =?',name)
     con.commit()
    con.close()
