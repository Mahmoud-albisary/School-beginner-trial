import sqlite3

def create():
    conn = sqlite3.connect('datas.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    conn.commit()
    conn.close()

def insert(username, password):
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO students VALUES(NULL, ?, ?)",(username, password,))
    conn.commit()
    conn.close()

def view():
    global rows
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur = cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(teacher = ""):
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE username = ? OR password = ?  ", (username, password))
    rows  = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update(id, username, password):
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur.execute("UPDATE students SET username = ?, password = ?  WHERE id = ?",(username, password, id))
    conn.commit()
    conn.close()

create()
