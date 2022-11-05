import sqlite3

def create():
    conn = sqlite3.connect('datas.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS teachers (id INTEGER PRIMARY KEY, teacher TEXT)")
    conn.commit()
    conn.close()

def create1():
    conn = sqlite3.connect('datas.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS durations (id INTEGER PRIMARY KEY, duration TEXT)")
    conn.commit()
    conn.close()


def insert(teacher):
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO teachers VALUES(NULL, ?)",(teacher,))
    conn.commit()
    conn.close()

def insert1(duration):
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO durations VALUES(NULL, ?)",(duration,))
    conn.commit()
    conn.close()

def view():
    global rows
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur = cur.execute("SELECT * FROM teachers")
    rows = cur.fetchall()
    conn.close()
    return rows

def view1():
    global rows1
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur = cur.execute("SELECT * FROM durations")
    rows1 = cur.fetchall()
    conn.close()
    return rows1

def search(teacher = ""):
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM teachers WHERE teacher = ?", (teacher,))
    rows  = cur.fetchall()
    conn.close()
    return rows

def search1(duration = ""):
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM durations WHERE duration = ?", (duration,))
    rows  = cur.fetchall()
    conn.close()
    return rows1

def delete(id):
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM teachers WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def delete1(id):
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM durations WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update(id, teacher):
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur.execute("UPDATE teachers SET teacher = ? WHERE id = ?",(teacher, id))
    conn.commit()
    conn.close()

def update1(id, duration):
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur.execute("UPDATE durations SET duration = ? WHERE id = ?",(duration, id))
    conn.commit()
    conn.close()

create()
create1()
